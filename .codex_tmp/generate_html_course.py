#!/usr/bin/env python3
"""Generate a lightweight LMS-style static course site from forward course content."""

from __future__ import annotations

import argparse
import html
import json
import math
import os
import re
import shutil
import sys
import zipfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse
from xml.etree import ElementTree as ET

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from shared.extraction.markdown_cleaner import clean_text


_INCLUDE_CHATBOT: bool = True

COURSE_ORDER = ["C2", "C3"]
CATEGORY_ORDER = ["lectures", "readings", "assessments"]
MODULE_ORDER = ["week_1", "week_2", "week_3", "week_4", "week_5", "week_6", "capstone"]
IGNORED_DIRS = {"C3_ReadyToRecord"}
IGNORED_SUFFIXES = ("_OLD",)
IGNORED_BASENAMES = {"lectures", "readings", "assessments"}
PLACEHOLDER_RE = re.compile(r"^(lectures|readings|assessments)_", re.IGNORECASE)
ASSESSMENT_GROUP_RE = re.compile(r"(C[23]_(?:W\d+|week_\d+|capstone)_Q\d+)", re.IGNORECASE)
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
XML_NAMESPACES = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}
PREFERRED_VARIANT_ORDER = {
    "lectures": [".md", ".txt", ".pptx", ".json", ".pdf", ".docx"],
    "readings": [".md", ".txt", ".html", ".htm", ".pdf", ".docx", ".json", ".pptx"],
    "assessments": [".md", ".txt", ".docx", ".pdf", ".json"],
}
# Config-mode suffix pattern: strips _slides, _outline, _reading, _prompt, _rubric
CONFIG_SUFFIX_PATTERN = re.compile(r"_(slides|outline|reading|prompt|rubric)$", re.IGNORECASE)
# Config-mode category folder names → CATEGORY_ORDER keys
CONFIG_CATEGORY_MAP = {"lectures": "lectures", "readings": "readings", "assignments": "assessments"}
CONCEPT_QUIZ_FILENAME_RE = re.compile(r"^W(\d+)_short_answer_quiz\.md$", re.IGNORECASE)


@dataclass
class QuizOption:
    label: str
    text: str
    feedback: str
    is_correct: bool


@dataclass
class QuizQuestion:
    number: int
    title: str
    prompt: str
    options: list[QuizOption]


@dataclass
class QuizData:
    intro_markdown: str
    questions: list[QuizQuestion]


@dataclass
class SourceVariant:
    source_path: str
    normalized_path: str
    label: str
    kind: str
    text: str = ""
    summary: str = ""


@dataclass
class ContentItem:
    id: str
    course_key: str
    module_key: str
    module_slug: str
    category: str
    title: str
    slug: str
    order: int
    variants: list[SourceVariant] = field(default_factory=list)
    summary: str = ""
    purpose: str = ""
    type_label: str = ""
    learning_goals: list[str] = field(default_factory=list)
    estimated_minutes: int = 0
    primary_variant_index: int = 0
    body_markdown: str = ""
    body_html: str = ""
    quiz: QuizData | None = None
    page_filename: str = ""


@dataclass
class ModuleMetaEntry:
    category: str
    type_label: str
    title: str
    purpose: str


@dataclass
class ModuleInfo:
    course_key: str
    key: str
    slug: str
    label: str
    order: int
    headline: str
    learning_goals: list[str] = field(default_factory=list)
    weekly_flow: str = ""
    summary: str = ""
    items: dict[str, list[ContentItem]] = field(default_factory=lambda: {c: [] for c in CATEGORY_ORDER})
    activity_meta: list[ModuleMetaEntry] = field(default_factory=list)


@dataclass
class CourseInfo:
    key: str
    title: str
    official_title: str
    overview_path: str | None
    week_by_week_path: str | None
    overview_text: str = ""
    modules: list[ModuleInfo] = field(default_factory=list)
    capstone_summary: str = ""


@dataclass
class MarkdownRenderContext:
    input_dir: Path
    output_dir: Path
    page_path: Path
    source_path: Path | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Input course directory")
    parser.add_argument("--output", required=True, help="Output directory for generated site")
    chatbot_group = parser.add_mutually_exclusive_group()
    chatbot_group.add_argument(
        "--chatbot",
        dest="chatbot",
        action="store_true",
        default=True,
        help="Include chat widget HTML and JS (default)",
    )
    chatbot_group.add_argument(
        "--no-chatbot",
        dest="chatbot",
        action="store_false",
        help="Strip all chat widget HTML and JS from output",
    )
    return parser.parse_args()


def load_config(input_dir: Path) -> dict | None:
    """Read config.json from the bundle root and resolve $ENV_VAR references.

    Returns None if config.json is absent (legacy C2/C3 mode).
    Raises SystemExit with a clear message if a referenced env var is not set.
    """
    config_path = input_dir / "config.json"
    if not config_path.exists():
        return None
    try:
        raw = json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        sys.exit(f"Error: config.json is not valid JSON: {exc}")
    return _resolve_env_vars(raw)


def _resolve_env_vars(value: Any) -> Any:
    """Recursively resolve $ENV_VAR references in string values."""
    if isinstance(value, str) and value.startswith("$"):
        var_name = value[1:]
        resolved = os.environ.get(var_name)
        if resolved is None:
            sys.exit(f"Error: environment variable '{var_name}' is not set (required by config.json)")
        return resolved
    if isinstance(value, dict):
        return {k: _resolve_env_vars(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_resolve_env_vars(item) for item in value]
    return value


def natural_sort_key(text: str) -> list[Any]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", text)]


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def module_sort_tuple(name: str) -> tuple[int, str]:
    lower = name.lower()
    for index, key in enumerate(MODULE_ORDER):
        if key in lower:
            return index, lower
    return len(MODULE_ORDER), lower


def module_label_from_key(key: str) -> str:
    if key == "capstone":
        return "Capstone"
    number = key.split("_")[-1]
    return f"Week {number}"


def module_slug(course_key: str, module_key: str) -> str:
    return f"{course_key.lower()}-{module_key}"


def singular_category(category: str) -> str:
    return {"lectures": "Lecture", "readings": "Reading", "assessments": "Assessment"}[category]


def classify_activity_type(type_label: str) -> str:
    lower = type_label.lower()
    if "video" in lower or "lecture" in lower:
        return "lectures"
    if "reading" in lower or "case study" in lower:
        return "readings"
    return "assessments"


def course_title_from_meta(meta_dir: Path, course_key: str) -> tuple[str, str]:
    overview_path = meta_dir / f"{course_key}_overview.md"
    if not overview_path.exists():
        return course_key, course_key
    lines = [line.strip() for line in read_text(overview_path).splitlines() if line.strip()]
    title = course_key
    official = course_key
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break
    for line in lines:
        if line.lower().startswith("**official title:**"):
            official = re.sub(r"^\*+|\*+$", "", line.split(":", 1)[1].strip()).strip()
            break
    return title, official


def parse_weekly_metadata(text: str) -> dict[str, dict[str, Any]]:
    module_data: dict[str, dict[str, Any]] = {}
    current_course: str | None = None
    current_key: str | None = None
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index].rstrip()
        header_match = re.match(r"^###\s+(C[23])\s+(?:Week|Module)\s+(\d+)\s*(?:[-—].*)?$", line)
        if header_match:
            current_course = header_match.group(1)
            current_key = f"week_{header_match.group(2)}"
            module_data[f"{current_course}:{current_key}"] = {
                "headline": line.lstrip("# ").strip(),
                "learning_goals": [],
                "weekly_flow": "",
                "summary": "",
                "activities": [],
            }
            index += 1
            continue
        if not current_key or not current_course:
            index += 1
            continue

        module_ref = module_data[f"{current_course}:{current_key}"]
        stripped = line.strip()

        if stripped.startswith("* "):
            module_ref["learning_goals"].append(stripped[2:].strip())
            index += 1
            continue

        if stripped.startswith("**") and "→" in stripped:
            module_ref["weekly_flow"] = stripped.strip("* ")
            index += 1
            continue

        activity_match = re.match(r"^###\s+\d+\.\s+([^:]+):\s+\*(.+)\*$", stripped)
        if activity_match:
            type_label = activity_match.group(1).strip()
            title = activity_match.group(2).strip()
            purpose = ""
            search = index + 1
            while search < len(lines):
                candidate = lines[search].rstrip()
                if candidate.startswith("### "):
                    break
                if candidate.strip() == "**Purpose:**":
                    search += 1
                    purpose_lines: list[str] = []
                    while search < len(lines):
                        purpose_line = lines[search].rstrip()
                        if purpose_line.startswith("### ") or purpose_line.strip() == "---":
                            break
                        if purpose_line.strip():
                            purpose_lines.append(purpose_line.strip())
                        search += 1
                    purpose = clean_text(" ".join(purpose_lines))
                    break
                search += 1
            module_ref["activities"].append(
                {
                    "category": classify_activity_type(type_label),
                    "type_label": type_label,
                    "title": title,
                    "purpose": purpose,
                }
            )
            index += 1
            continue

        if stripped and not stripped.startswith("#") and not stripped.startswith("**") and not stripped.startswith("* "):
            current_summary = module_ref.get("summary", "")
            if len(current_summary) < 1200:
                module_ref["summary"] = clean_text((current_summary + "\n" + stripped).strip())

        index += 1
    return module_data


def extract_capstone_summary(overview_text: str) -> str:
    patterns = [
        r"##\s+C2 Mini-Capstone\s+(.*?)(?=\n##\s|\Z)",
        r"##\s+Closing Exercise:?.*?\n(.*?)(?=\n##\s|\Z)",
        r"##\s+Closing Exercise\s+(.*?)(?=\n##\s|\Z)",
    ]
    for pattern in patterns:
        match = re.search(pattern, overview_text, re.DOTALL)
        if match:
            return clean_text(match.group(1))
    return ""


def build_courses(input_dir: Path) -> dict[str, CourseInfo]:
    meta_dir = input_dir / "meta"
    weekly_text_by_course = {
        course_key: read_text(meta_dir / f"{course_key}_week_by_week.md")
        for course_key in COURSE_ORDER
        if (meta_dir / f"{course_key}_week_by_week.md").exists()
    }
    weekly_metadata: dict[str, dict[str, Any]] = {}
    for course_key, text in weekly_text_by_course.items():
        weekly_metadata.update(parse_weekly_metadata(text))

    courses: dict[str, CourseInfo] = {}
    for course_key in COURSE_ORDER:
        title, official = course_title_from_meta(meta_dir, course_key)
        overview_path = meta_dir / f"{course_key}_overview.md"
        overview_text = clean_text(read_text(overview_path)) if overview_path.exists() else ""
        courses[course_key] = CourseInfo(
            key=course_key,
            title=title,
            official_title=official,
            overview_path=str(overview_path.relative_to(input_dir)) if overview_path.exists() else None,
            week_by_week_path=str((meta_dir / f"{course_key}_week_by_week.md").relative_to(input_dir))
            if (meta_dir / f"{course_key}_week_by_week.md").exists()
            else None,
            overview_text=overview_text,
            capstone_summary=extract_capstone_summary(overview_text),
        )

    for course_key, course in courses.items():
        module_names = collect_module_names(input_dir, course_key)
        module_refs: dict[str, ModuleInfo] = {}
        for order, module_key in enumerate(module_names):
            metadata = weekly_metadata.get(f"{course_key}:{module_key}", {})
            headline = sanitize_module_headline(
                str(metadata.get("headline") or f"{course_key} {module_label_from_key(module_key)}")
            )
            module = ModuleInfo(
                course_key=course_key,
                key=module_key,
                slug=module_slug(course_key, module_key),
                label=f"{course_key} {module_label_from_key(module_key)}",
                order=order,
                headline=headline,
                learning_goals=list(metadata.get("learning_goals", [])),
                weekly_flow=str(metadata.get("weekly_flow", "")),
                summary=clean_text(str(metadata.get("summary", ""))) or (course.capstone_summary if module_key == "capstone" else ""),
                activity_meta=[
                    ModuleMetaEntry(**entry) for entry in metadata.get("activities", [])
                ],
            )
            module_refs[module_key] = module
            course.modules.append(module)

        for category in CATEGORY_ORDER:
            category_dir = input_dir / category
            if not category_dir.exists():
                continue
            for directory in sorted(category_dir.iterdir(), key=lambda item: module_sort_tuple(item.name)):
                if not directory.is_dir() or directory.name in IGNORED_DIRS:
                    continue
                if not directory.name.startswith(f"{course_key}_"):
                    continue
                current_module_key = parse_module_key(directory.name)
                if not current_module_key or current_module_key not in module_refs:
                    continue
                items = collect_items_for_directory(input_dir, directory, course_key, current_module_key, category)
                module_refs[current_module_key].items[category].extend(items)

        for module in course.modules:
            apply_metadata_titles(module)
            module.summary = derive_module_summary(course, module)

    return courses


def build_courses_from_config(input_dir: Path, config: dict) -> dict[str, CourseInfo]:
    """Build the courses dict from a config.json bundle (ASEN 3501 / generic structure)."""
    courses: dict[str, CourseInfo] = {}
    for seg_cfg in config.get("segments", []):
        seg_key: str = seg_cfg["key"]
        seg_label: str = seg_cfg.get("label", seg_key)
        seg_dir = input_dir / seg_key
        course_week_start: int = seg_cfg.get("course_week_start", 1)
        num_weeks: int = seg_cfg.get("weeks", 0)

        course = CourseInfo(
            key=seg_key,
            title=seg_label,
            official_title=seg_label,
            overview_path=None,
            week_by_week_path=None,
            overview_text="",
        )

        for rel_week in range(1, num_weeks + 1):
            week_key = f"week_{rel_week}"
            week_dir = seg_dir / week_key
            if not week_dir.exists():
                continue
            flat_week = course_week_start + rel_week - 1
            module_label = f"{seg_key} Week {rel_week} (Course Week {flat_week})"
            module_slug_str = f"{seg_key.lower()}-{week_key}"
            module = ModuleInfo(
                course_key=seg_key,
                key=week_key,
                slug=module_slug_str,
                label=module_label,
                order=rel_week - 1,
                headline=module_label,
            )
            for dir_name, category in CONFIG_CATEGORY_MAP.items():
                cat_dir = week_dir / dir_name
                if cat_dir.exists():
                    items = collect_items_for_config_dir(input_dir, cat_dir, seg_key, week_key, category, config)
                    module.items[category].extend(items)
            course.modules.append(module)

        courses[seg_key] = course
    return courses


def collect_items_for_config_dir(
    input_dir: Path,
    directory: Path,
    course_key: str,
    module_key: str,
    category: str,
    config: dict,
) -> list[ContentItem]:
    """Collect ContentItems from a config-mode category directory."""
    grouped: dict[str, list[Path]] = {}
    for path in sorted(directory.iterdir(), key=lambda p: natural_sort_key(p.name)):
        if not path.is_file():
            continue
        if should_skip_path_config(path):
            continue
        group_key = item_group_key_config(path)
        if not group_key:
            continue
        grouped.setdefault(group_key, []).append(path)

    module_slug_str = f"{course_key.lower()}-{module_key}"
    items: list[ContentItem] = []
    for order, (group_key, paths) in enumerate(
        sorted(grouped.items(), key=lambda pair: natural_sort_key(pair[0])), start=1
    ):
        title = derive_title_config(paths)
        item = ContentItem(
            id=group_key,
            course_key=course_key,
            module_key=module_key,
            module_slug=module_slug_str,
            category=category,
            title=title,
            slug=slugify(group_key),
            order=order,
            type_label=singular_category(category),
        )
        for variant_path in sorted(paths, key=variant_sort_key_config):
            item.variants.append(
                SourceVariant(
                    source_path=str(variant_path.relative_to(input_dir)),
                    normalized_path="",
                    label=variant_label(variant_path),
                    kind=variant_path.suffix.lower().lstrip("."),
                )
            )
        items.append(item)
    return items


def item_group_key_config(path: Path) -> str | None:
    """Strip type suffix (_slides, _outline, etc.) to derive the group key."""
    stem = path.stem
    stripped = CONFIG_SUFFIX_PATTERN.sub("", stem)
    return stripped if stripped else None


def should_skip_path_config(path: Path) -> bool:
    """Skip image assets and rubric files in config mode."""
    if is_image_asset_path(path):
        return True
    if path.stem.lower().endswith("_rubric"):
        return True
    return False


def variant_sort_key_config(path: Path) -> tuple[int, list[Any]]:
    """Rank slides HTML first, then reading/prompt markdown, then outlines."""
    stem = path.stem.lower()
    suffix = path.suffix.lower()
    if stem.endswith("_slides") and suffix in {".html", ".htm"}:
        return 0, natural_sort_key(path.name)
    if stem.endswith(("_reading", "_prompt")) and suffix == ".md":
        return 1, natural_sort_key(path.name)
    if stem.endswith("_outline") and suffix == ".md":
        return 2, natural_sort_key(path.name)
    return 3, natural_sort_key(path.name)


def select_primary_variant_config(item: ContentItem) -> int:
    """Select primary variant for config-mode items: slides first, then non-outline md."""
    for i, variant in enumerate(item.variants):
        path = Path(variant.source_path)
        if path.stem.lower().endswith("_slides") and path.suffix.lower() in {".html", ".htm"}:
            return i
    for i, variant in enumerate(item.variants):
        path = Path(variant.source_path)
        if path.suffix.lower() == ".md" and not path.stem.lower().endswith("_outline"):
            return i
    for i, variant in enumerate(item.variants):
        if Path(variant.source_path).suffix.lower() not in IMAGE_EXTENSIONS:
            return i
    return 0


def derive_title_config(paths: list[Path]) -> str:
    """Derive a display title by stripping config-mode type suffixes."""
    candidates = []
    for path in paths:
        stripped = CONFIG_SUFFIX_PATTERN.sub("", path.stem)
        title = re.sub(r"\s+", " ", stripped.replace("_", " ")).strip()
        candidates.append(title)
    candidates.sort(key=len, reverse=True)
    return candidates[0] if candidates else "Untitled"


def sanitize_module_headline(headline: str) -> str:
    cleaned = re.sub(r"\s*[-—]\s*<[^>]+>\s*$", "", headline).strip()
    cleaned = re.sub(r"\s{2,}", " ", cleaned)
    return cleaned


def derive_module_summary(course: CourseInfo, module: ModuleInfo) -> str:
    if module.key == "capstone" and course.capstone_summary:
        return summarize_text(course.capstone_summary, 420)
    purpose_lines = [entry.purpose for entry in module.activity_meta if entry.purpose]
    if purpose_lines:
        return summarize_text(" ".join(purpose_lines[:3]), 420)
    if module.summary:
        return summarize_text(module.summary, 420)
    return f"{module.label} moves through ordered lectures, readings, and assessments generated from the source materials."


def collect_module_names(input_dir: Path, course_key: str) -> list[str]:
    found: set[str] = set()
    for category in CATEGORY_ORDER:
        category_dir = input_dir / category
        if not category_dir.exists():
            continue
        for directory in category_dir.iterdir():
            if not directory.is_dir() or directory.name in IGNORED_DIRS:
                continue
            if not directory.name.startswith(f"{course_key}_"):
                continue
            parsed = parse_module_key(directory.name)
            if parsed:
                found.add(parsed)
    return sorted(found, key=lambda item: module_sort_tuple(item))


def parse_module_key(name: str) -> str | None:
    lowered = name.lower()
    if "capstone" in lowered:
        return "capstone"
    match = re.search(r"week[_ ](\d+)", lowered)
    if match:
        return f"week_{match.group(1)}"
    return None


def collect_items_for_directory(
    input_dir: Path,
    directory: Path,
    course_key: str,
    module_key: str,
    category: str,
) -> list[ContentItem]:
    grouped: dict[str, list[Path]] = {}
    for path in sorted(directory.iterdir(), key=lambda item: natural_sort_key(item.name)):
        if not path.is_file():
            continue
        if should_skip_path(path):
            continue
        group_key = item_group_key(path, category)
        if not group_key:
            continue
        grouped.setdefault(group_key, []).append(path)

    items: list[ContentItem] = []
    for order, (group_key, paths) in enumerate(sorted(grouped.items(), key=lambda pair: natural_sort_key(pair[0])), start=1):
        item = ContentItem(
            id=group_key,
            course_key=course_key,
            module_key=module_key,
            module_slug=module_slug(course_key, module_key),
            category=category,
            title=derive_title(paths, category),
            slug=slugify(group_key),
            order=order,
            type_label=singular_category(category),
        )
        for variant_path in sorted(paths, key=variant_sort_key):
            item.variants.append(
                SourceVariant(
                    source_path=str(variant_path.relative_to(input_dir)),
                    normalized_path="",
                    label=variant_label(variant_path),
                    kind=variant_path.suffix.lower().lstrip("."),
                )
            )
        items.append(item)
    return items


def should_skip_path(path: Path) -> bool:
    if is_image_asset_path(path):
        return True
    if path.stem in IGNORED_BASENAMES:
        return True
    if PLACEHOLDER_RE.match(path.name):
        return path.stat().st_size == 0
    if any(path.stem.endswith(suffix) for suffix in IGNORED_SUFFIXES):
        return True
    if "prompt" in path.stem.lower():
        return True
    return False


def item_group_key(path: Path, category: str) -> str | None:
    stem = path.stem
    if category == "lectures":
        return re.sub(r"_presentation_outline$", "", stem, flags=re.IGNORECASE)
    if category == "readings":
        return stem
    if category == "assessments":
        match = ASSESSMENT_GROUP_RE.search(stem)
        if match:
            return match.group(1)
        return stem
    return stem


def derive_title(paths: list[Path], category: str) -> str:
    candidates: list[str] = []
    for path in paths:
        stem = path.stem
        if category == "lectures":
            stem = re.sub(r"_presentation_outline$", "", stem, flags=re.IGNORECASE)
        if category == "assessments":
            stem = re.sub(r"_aligned$", "", stem, flags=re.IGNORECASE)
        title = re.sub(r"\s+", " ", stem.replace("_", " ")).strip()
        candidates.append(title)
    candidates.sort(key=len, reverse=True)
    return candidates[0] if candidates else "Untitled"


def variant_sort_key(path: Path) -> tuple[int, list[Any]]:
    rank_map = {".md": 0, ".txt": 1, ".docx": 2, ".pdf": 3, ".html": 4, ".htm": 4, ".pptx": 5, ".json": 6}
    return rank_map.get(path.suffix.lower(), 99), natural_sort_key(path.name)


def is_image_asset_path(path: Path) -> bool:
    return path.suffix.lower() in IMAGE_EXTENSIONS


def variant_label(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".md":
        return "Markdown"
    if suffix == ".docx":
        return "DOCX"
    if suffix == ".pdf":
        return "PDF"
    if suffix == ".pptx":
        return "PPTX"
    if suffix == ".txt":
        return "Text"
    if suffix == ".json":
        return "JSON"
    if suffix in {".html", ".htm"}:
        return "HTML"
    return suffix.lstrip(".").upper()


def apply_metadata_titles(module: ModuleInfo) -> None:
    grouped_meta: dict[str, list[ModuleMetaEntry]] = {category: [] for category in CATEGORY_ORDER}
    for entry in module.activity_meta:
        grouped_meta[entry.category].append(entry)
    for category in CATEGORY_ORDER:
        items = [item for item in sorted(module.items[category], key=lambda item: item.order) if item_has_content_variants(item)]
        metadata_entries = grouped_meta.get(category, [])
        for index, item in enumerate(items):
            if index < len(metadata_entries):
                item.title = metadata_entries[index].title
                item.purpose = metadata_entries[index].purpose
                item.type_label = metadata_entries[index].type_label
            item.learning_goals = module.learning_goals[:4]


def prepare_output_dir(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for path in output_dir.iterdir():
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()


def normalize_courses(
    input_dir: Path, output_dir: Path, courses: dict[str, CourseInfo], config: dict | None = None
) -> None:
    normalized_root = output_dir / "normalized"
    for course in courses.values():
        for module in course.modules:
            for category in CATEGORY_ORDER:
                for item in module.items[category]:
                    for variant in item.variants:
                        source_path = input_dir / variant.source_path
                        normalized_path, text = normalize_file(source_path, input_dir, normalized_root)
                        variant.normalized_path = str(normalized_path.relative_to(output_dir))
                        variant.text = text
                        variant.summary = summarize_text(text)

                    if config is not None:
                        item.primary_variant_index = select_primary_variant_config(item)
                    else:
                        item.primary_variant_index = select_primary_variant(item)
                    primary_variant = item.variants[item.primary_variant_index]
                    item.body_markdown = primary_variant.text
                    # For slides-primary items (empty text), fall back to outline text for summary
                    if not primary_variant.text and config is not None:
                        for v in item.variants:
                            if Path(v.source_path).stem.lower().endswith("_outline") and v.text:
                                item.body_markdown = v.text
                                break
                    item.summary = item.purpose or primary_variant.summary or summarize_text(item.body_markdown)
                    item.estimated_minutes = estimate_minutes(item)
                    item.quiz = parse_quiz_markdown(item.body_markdown) if category == "assessments" else None
                    item.body_html = ""


def select_primary_variant(item: ContentItem) -> int:
    preferred_suffixes = PREFERRED_VARIANT_ORDER[item.category]
    path_lookup = [Path(variant.source_path).suffix.lower() for variant in item.variants]
    for suffix in preferred_suffixes:
        for index, candidate in enumerate(path_lookup):
            if candidate == suffix:
                if item.category != "assessments":
                    return index
                source_name = Path(item.variants[index].source_path).name.lower()
                if suffix != ".md" or "aligned" in source_name or len(item.variants) == 1:
                    return index
        if item.category == "assessments" and suffix == ".md":
            for index, candidate in enumerate(path_lookup):
                if candidate == ".md":
                    return index
    for index, candidate in enumerate(path_lookup):
        if candidate not in IMAGE_EXTENSIONS:
            return index
    return 0


def item_has_content_variants(item: ContentItem) -> bool:
    return any(Path(variant.source_path).suffix.lower() not in IMAGE_EXTENSIONS for variant in item.variants)


def normalize_file(source_path: Path, input_dir: Path, normalized_root: Path) -> tuple[Path, str]:
    relative = source_path.relative_to(input_dir)
    target = normalized_root / relative.parent / f"{relative.name}.normalized.md"
    target.parent.mkdir(parents=True, exist_ok=True)

    suffix = source_path.suffix.lower()
    if suffix in IMAGE_EXTENSIONS:
        text = ""
    elif source_path.stem.lower().endswith("_slides") and suffix in {".html", ".htm"}:
        # Slides HTML files are rendered artifacts — do not extract text for chatbot grounding
        text = ""
    elif suffix in {".md", ".txt"}:
        text = clean_text(read_text(source_path))
    elif suffix == ".json":
        text = normalize_json(source_path)
    elif suffix == ".pptx":
        text = normalize_pptx(source_path, target.parent / f"{source_path.stem}_assets")
    elif suffix in {".docx", ".pdf", ".html", ".htm"}:
        from shared.extraction.router import extract as routed_extract

        text = routed_extract(str(source_path))
    else:
        text = clean_text(read_text(source_path))

    target.write_text(text + "\n", encoding="utf-8")
    return target, text


def normalize_json(path: Path) -> str:
    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError:
        return clean_text(read_text(path))
    lines: list[str] = []
    render_json_value(data, lines, 0)
    return clean_text("\n".join(lines))


def render_json_value(value: Any, lines: list[str], depth: int) -> None:
    prefix = "  " * depth
    if isinstance(value, dict):
        for key, nested in value.items():
            if isinstance(nested, (dict, list)):
                lines.append(f"{prefix}{key}:")
                render_json_value(nested, lines, depth + 1)
            else:
                lines.append(f"{prefix}{key}: {nested}")
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, (dict, list)):
                lines.append(f"{prefix}-")
                render_json_value(item, lines, depth + 1)
            else:
                lines.append(f"{prefix}- {item}")
    else:
        lines.append(f"{prefix}{value}")


def normalize_pptx(path: Path, assets_dir: Path) -> str:
    slides: list[str] = []
    assets_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path) as archive:
        slide_names = sorted(
            [name for name in archive.namelist() if name.startswith("ppt/slides/slide") and name.endswith(".xml")],
            key=natural_sort_key,
        )
        for slide_number, slide_name in enumerate(slide_names, start=1):
            slide_text, copied_images = extract_slide_content(archive, slide_name, assets_dir)
            lines = [f"## Slide {slide_number}"]
            if slide_text:
                lines.extend(slide_text)
            if copied_images:
                lines.append("")
                lines.append("Images:")
                for image_path in copied_images:
                    lines.append(f"- {image_path.as_posix()}")
            slides.append("\n".join(lines).strip())
    if not any(slide.strip() for slide in slides):
        return f"# {path.stem}\n\nNo slide text extracted."
    return clean_text("\n\n".join(slides))


def extract_slide_content(archive: zipfile.ZipFile, slide_name: str, assets_dir: Path) -> tuple[list[str], list[Path]]:
    root = ET.fromstring(archive.read(slide_name))
    text_bits = [node.text.strip() for node in root.findall(".//a:t", XML_NAMESPACES) if node.text and node.text.strip()]
    slide_lines = collapse_slide_text(text_bits)

    rel_name = slide_name.replace("slides/", "slides/_rels/") + ".rels"
    copied_images: list[Path] = []
    if rel_name in archive.namelist():
        rel_root = ET.fromstring(archive.read(rel_name))
        slide_stem = Path(slide_name).stem
        for rel in rel_root:
            target = rel.attrib.get("Target", "")
            if not target.lower().endswith(tuple(IMAGE_EXTENSIONS)):
                continue
            source = resolve_zip_target(slide_name, target)
            if source not in archive.namelist():
                continue
            destination = assets_dir / f"{slide_stem}_{Path(target).name}"
            with archive.open(source) as image_stream, destination.open("wb") as handle:
                shutil.copyfileobj(image_stream, handle)
            copied_images.append(destination.relative_to(assets_dir.parent.parent))
    return slide_lines, copied_images


def collapse_slide_text(text_bits: list[str]) -> list[str]:
    if not text_bits:
        return []
    lines = [f"Title: {text_bits[0]}"]
    if len(text_bits) > 1:
        lines.append("Bullets:")
        for bullet in text_bits[1:]:
            lines.append(f"- {bullet}")
    return lines


def resolve_zip_target(slide_name: str, target: str) -> str:
    slide_dir = Path(slide_name).parent
    resolved = (slide_dir / target).as_posix()
    parts: list[str] = []
    for part in resolved.split("/"):
        if part in {"", "."}:
            continue
        if part == "..":
            if parts:
                parts.pop()
            continue
        parts.append(part)
    return "/".join(parts)


def summarize_text(text: str, limit: int = 220) -> str:
    flattened = " ".join(text.split())
    if len(flattened) <= limit:
        return flattened
    return flattened[: limit - 3].rstrip() + "..."


def estimate_minutes(item: ContentItem) -> int:
    if item.quiz:
        return max(4, len(item.quiz.questions) * 2)
    word_count = len(item.body_markdown.split())
    if item.category == "lectures":
        return max(4, math.ceil(word_count / 160))
    if item.category == "readings":
        return max(3, math.ceil(word_count / 220))
    return max(3, math.ceil(word_count / 180))


def parse_quiz_markdown(text: str) -> QuizData | None:
    cleaned = clean_text(text)
    cleaned = re.sub(r"^-{3,}Importable Content Starts Here-{3,}$", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"^-{3,}End Importable Content Here-+\.?$", "", cleaned, flags=re.MULTILINE)
    cleaned = clean_text(cleaned)
    question_match = re.search(r"(^|\n)Question\s+(\d+)\b", cleaned)
    if not question_match:
        return None

    intro = cleaned[: question_match.start()].strip()
    blocks = re.split(r"\n(?=Question\s+\d+\b)", cleaned[question_match.start():].strip())
    questions: list[QuizQuestion] = []

    for block in blocks:
        lines = [line.rstrip() for line in block.splitlines() if line.strip()]
        if not lines:
            continue
        header_match = re.match(r"^Question\s+(\d+)\s*(.*)$", lines[0].strip())
        if not header_match:
            continue
        number = int(header_match.group(1))
        title = header_match.group(2).strip() or f"Question {number}"
        prompt_lines: list[str] = []
        options: list[QuizOption] = []
        current_option: QuizOption | None = None
        mode = "prompt"

        for line in lines[1:]:
            option_match = re.match(r"^(\*)?([A-Z]):\s*(.*)$", line.strip())
            if option_match:
                if current_option:
                    options.append(current_option)
                current_option = QuizOption(
                    label=option_match.group(2),
                    text=option_match.group(3).strip(),
                    feedback="",
                    is_correct=bool(option_match.group(1)),
                )
                mode = "option"
                continue

            feedback_match = re.match(r"^Feedback:\s*(.*)$", line.strip())
            if feedback_match and current_option:
                current_option.feedback = feedback_match.group(1).strip()
                mode = "feedback"
                continue

            if current_option and mode in {"option", "feedback"}:
                if mode == "feedback":
                    current_option.feedback = clean_text(f"{current_option.feedback}\n{line.strip()}")
                else:
                    current_option.text = clean_text(f"{current_option.text}\n{line.strip()}")
                continue

            prompt_lines.append(line.strip())

        if current_option:
            options.append(current_option)

        if title == f"Question {number}" and prompt_lines:
            candidate = prompt_lines[0].strip()
            if len(candidate) < 120:
                title = candidate
                prompt_lines = prompt_lines[1:]

        if options:
            questions.append(
                QuizQuestion(
                    number=number,
                    title=title,
                    prompt=clean_text("\n".join(prompt_lines)),
                    options=options,
                )
            )

    if not questions:
        return None
    return QuizData(intro_markdown=intro, questions=questions)


def render_item_body_html(item: ContentItem, context: MarkdownRenderContext) -> str:
    if item.quiz:
        return render_quiz_html(item, context)
    return markdown_to_html(item.body_markdown, context)


def render_quiz_html(item: ContentItem, context: MarkdownRenderContext) -> str:
    assert item.quiz is not None
    quiz_id = f"{item.module_slug}-{item.slug}"
    intro_html = markdown_to_html(item.quiz.intro_markdown, context) if item.quiz.intro_markdown else ""
    questions_html: list[str] = []
    for question in item.quiz.questions:
        options_html = []
        for option in question.options:
            options_html.append(
                f"""
                <label class="quiz-option">
                  <input type="radio" name="question-{question.number}" value="{html.escape(option.label)}"
                    data-correct="{str(option.is_correct).lower()}"
                    data-feedback="{html.escape(option.feedback, quote=True)}">
                  <span><strong>{html.escape(option.label)}.</strong> {html.escape(option.text)}</span>
                </label>
                """
            )
        questions_html.append(
            f"""
            <fieldset class="quiz-question" data-question-number="{question.number}">
              <legend>Question {question.number}: {html.escape(question.title)}</legend>
              <div class="quiz-prompt">{markdown_to_html(question.prompt, context)}</div>
              <div class="quiz-options">
                {''.join(options_html)}
              </div>
              <div class="quiz-feedback" hidden></div>
            </fieldset>
            """
        )

    return f"""
    <section class="quiz-shell">
      {intro_html}
      <form class="quiz-form" data-quiz-id="{html.escape(quiz_id)}" data-module-id="{html.escape(item.module_slug)}" data-question-count="{len(item.quiz.questions)}">
        {''.join(questions_html)}
        <div class="quiz-actions">
          <button type="submit" class="primary-button">Check Answers</button>
          <p class="quiz-score" aria-live="polite"></p>
        </div>
      </form>
    </section>
    """


def markdown_to_html(text: str, context: MarkdownRenderContext | None = None) -> str:
    lines = text.splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    in_ul = False
    in_ol = False
    in_code = False
    in_table = False
    table_rows: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            paragraph_text = "\n".join(paragraph).strip()
            embed_html = render_standalone_youtube_embed(paragraph_text)
            include_html = render_standalone_include(paragraph_text, context)
            if include_html:
                output.append(include_html)
            elif embed_html:
                output.append(embed_html)
            else:
                output.append(f"<p>{apply_inline_markdown(' '.join(part.strip() for part in paragraph), context)}</p>")
            paragraph = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            output.append("</ul>")
            in_ul = False
        if in_ol:
            output.append("</ol>")
            in_ol = False

    def flush_table() -> None:
        nonlocal in_table, table_rows
        if not table_rows:
            in_table = False
            return
        rows = table_rows
        table_rows = []
        in_table = False
        header_row: list[str] | None = None
        body_rows: list[list[str]] = []
        for raw_row in rows:
            cells = [c.strip() for c in raw_row.strip("|").split("|")]
            if cells and all(not c or re.match(r"^[-: ]+$", c) for c in cells):
                continue  # separator row
            if header_row is None:
                header_row = cells
            else:
                body_rows.append(cells)
        if header_row is None:
            return
        th_html = "".join(f"<th>{apply_inline_markdown(c, context)}</th>" for c in header_row)
        tbody_html = "".join(
            "<tr>" + "".join(f"<td>{apply_inline_markdown(c, context)}</td>" for c in row) + "</tr>"
            for row in body_rows
        )
        output.append(
            f'<div class="table-wrapper"><table class="md-table">'
            f"<thead><tr>{th_html}</tr></thead>"
            f"<tbody>{tbody_html}</tbody>"
            f"</table></div>"
        )

    for raw_line in lines:
        line = raw_line.rstrip()
        stripped = line.strip()
        if stripped.startswith("```"):
            flush_paragraph()
            close_lists()
            flush_table()
            if in_code:
                output.append("</code></pre>")
                in_code = False
            else:
                output.append("<pre><code>")
                in_code = True
            continue
        if in_code:
            output.append(html.escape(raw_line))
            continue
        if not stripped:
            flush_paragraph()
            close_lists()
            flush_table()
            continue
        if stripped == "---":
            flush_paragraph()
            close_lists()
            flush_table()
            output.append("<hr>")
            continue
        # Pipe table detection
        is_table_line = stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") >= 2
        if in_table and not is_table_line:
            flush_table()
        if is_table_line:
            if not in_table:
                flush_paragraph()
                close_lists()
                in_table = True
            table_rows.append(stripped)
            continue
        heading_match = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading_match:
            flush_paragraph()
            close_lists()
            level = len(heading_match.group(1))
            output.append(f"<h{level}>{apply_inline_markdown(heading_match.group(2), context)}</h{level}>")
            continue
        unordered_match = re.match(r"^[-*]\s+(.*)$", stripped)
        if unordered_match:
            flush_paragraph()
            if in_ol:
                output.append("</ol>")
                in_ol = False
            if not in_ul:
                output.append("<ul>")
                in_ul = True
            output.append(f"<li>{apply_inline_markdown(unordered_match.group(1), context)}</li>")
            continue
        ordered_match = re.match(r"^\d+\.\s+(.*)$", stripped)
        if ordered_match:
            flush_paragraph()
            if in_ul:
                output.append("</ul>")
                in_ul = False
            if not in_ol:
                output.append("<ol>")
                in_ol = True
            output.append(f"<li>{apply_inline_markdown(ordered_match.group(1), context)}</li>")
            continue
        close_lists()
        paragraph.append(stripped)

    flush_paragraph()
    close_lists()
    flush_table()
    if in_code:
        output.append("</code></pre>")
    return "\n".join(output)


def apply_inline_markdown(text: str, context: MarkdownRenderContext | None = None) -> str:
    replacements: dict[str, str] = {}
    counter = 0

    def stash(rendered: str) -> str:
        nonlocal counter
        token = f"@@FORWARD_MD_{counter}@@"
        counter += 1
        replacements[token] = rendered
        return token

    text = re.sub(r"`([^`]+)`", lambda match: stash(f"<code>{html.escape(match.group(1))}</code>"), text)
    text = re.sub(
        r"\[include-text\]\(([^)]+)\)",
        lambda match: stash(render_included_text(match.group(1), context)),
        text,
    )
    text = re.sub(
        r"\{\{include:([^}]+)\}\}",
        lambda match: stash(render_included_text(match.group(1), context)),
        text,
    )
    text = re.sub(
        r"\[video-thumb(?:\:\s*([^\]]*))?\]\(([^|)]+)\|([^)]+)\)",
        lambda match: stash(render_video_thumbnail_link(match.group(1) or "", match.group(2), match.group(3), context)),
        text,
    )
    text = re.sub(
        r"!\[([^\]]*)\]\(([^)]+)\)",
        lambda match: stash(render_markdown_image(match.group(1), match.group(2), context)),
        text,
    )
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda match: stash(render_markdown_link(match.group(1), match.group(2))),
        text,
    )
    text = re.sub(
        r"(?<![\w\"'=])(https?://[^\s<]+)",
        lambda match: stash(render_markdown_link(match.group(1), match.group(1))),
        text,
    )

    escaped = html.escape(text)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)

    for token, rendered in replacements.items():
        escaped = escaped.replace(token, rendered)
    return escaped


def render_markdown_link(label: str, href: str) -> str:
    clean_href = extract_markdown_destination(href)
    return f'<a href="{html.escape(clean_href, quote=True)}">{html.escape(label.strip() or clean_href)}</a>'


def render_markdown_image(alt_text: str, image_target: str, context: MarkdownRenderContext | None) -> str:
    resolved_src = resolve_markdown_image_src(image_target, context)
    return f'<img class="markdown-image" src="{html.escape(resolved_src, quote=True)}" alt="{html.escape(alt_text)}">'


def render_standalone_include(text: str, context: MarkdownRenderContext | None) -> str | None:
    include_target = extract_include_target(text)
    if not include_target:
        return None
    return render_included_text(include_target, context)


def extract_include_target(text: str) -> str | None:
    stripped = text.strip()
    markdown_match = re.fullmatch(r"\[include-text\]\(([^)]+)\)", stripped)
    if markdown_match:
        return markdown_match.group(1).strip()
    curly_match = re.fullmatch(r"\{\{include:([^}]+)\}\}", stripped)
    if curly_match:
        return curly_match.group(1).strip()
    return None


def render_included_text(include_target: str, context: MarkdownRenderContext | None) -> str:
    include_path = resolve_include_path(include_target, context)
    if not include_path:
        return render_include_placeholder(f"Included file not found: {extract_markdown_destination(include_target)}")
    if include_path.suffix.lower() not in {".txt", ".md"}:
        return render_include_placeholder(f"Unsupported include type: {include_path.name}")

    included_text = clean_text(read_text(include_path))
    if not included_text.strip():
        return '<div class="included-text-block muted">Included file is empty.</div>'
    return f'<div class="included-text-block">{markdown_to_html(included_text, context)}</div>'


def render_include_placeholder(message: str) -> str:
    return f'<div class="included-text-block include-error">{html.escape(message)}</div>'


def render_video_thumbnail_link(
    caption: str,
    image_target: str,
    video_target: str,
    context: MarkdownRenderContext | None,
) -> str:
    clean_video_target = extract_markdown_destination(video_target)
    resolved_src = resolve_markdown_image_src(image_target, context)
    clean_caption = caption.strip()
    video_label = clean_caption or "Watch on YouTube"
    image_alt = clean_caption or "Video thumbnail"
    caption_html = f'<span class="video-thumb-caption">{html.escape(clean_caption)}</span>' if clean_caption else ""
    return (
        f'<a class="video-thumb-card" href="{html.escape(clean_video_target, quote=True)}" '
        'target="_blank" rel="noopener noreferrer">'
        '<span class="video-thumb-media">'
        f'<img class="video-thumb-image" src="{html.escape(resolved_src, quote=True)}" alt="{html.escape(image_alt)}">'
        '<span class="video-thumb-overlay" aria-hidden="true"><span class="video-thumb-play"></span>'
        '<span class="video-thumb-badge">Watch on YouTube</span></span>'
        "</span>"
        f'<span class="video-thumb-body"><span class="video-thumb-title">{html.escape(video_label)}</span>{caption_html}</span>'
        "</a>"
    )


def resolve_markdown_image_src(image_target: str, context: MarkdownRenderContext | None) -> str:
    target = extract_markdown_destination(image_target)
    if not context or not target or is_external_url(target) or target.startswith("data:"):
        return target
    if not context.source_path:
        return target

    source_asset = (context.source_path.parent / target).resolve()
    try:
        source_asset.relative_to(context.input_dir.resolve())
    except ValueError:
        return target
    if not source_asset.exists() or not source_asset.is_file():
        return target

    asset_relative = source_asset.relative_to(context.input_dir.resolve())
    copied_relative = Path("assets") / asset_relative
    destination = context.output_dir / copied_relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not destination.exists():
        shutil.copy2(source_asset, destination)
    return Path(os_relative_path(context.page_path.parent, destination)).as_posix()


def resolve_include_path(include_target: str, context: MarkdownRenderContext | None) -> Path | None:
    target = extract_markdown_destination(include_target)
    if not context or not context.source_path or not target:
        return None
    if is_external_url(target):
        return None

    candidate = (context.source_path.parent / target).resolve()
    try:
        candidate.relative_to(context.input_dir.resolve())
    except ValueError:
        return None
    if not candidate.exists() or not candidate.is_file():
        return None
    return candidate


def os_relative_path(from_dir: Path, to_path: Path) -> str:
    return os.path.relpath(to_path, from_dir)


def is_sharepoint_url(url: str) -> bool:
    try:
        return "sharepoint.com" in urlparse(url).netloc.lower()
    except Exception:
        return False


def render_sharepoint_link_card(url: str, label: str = "") -> str:
    display = label.strip() or "Watch video (SharePoint)"
    return (
        f'<a class="video-thumb-card sharepoint-link" href="{html.escape(url, quote=True)}" '
        'target="_blank" rel="noopener noreferrer">'
        '<span class="video-thumb-media sharepoint-icon-wrap" aria-hidden="true">'
        '<span class="sharepoint-icon">&#9654;</span>'
        "</span>"
        f'<span class="video-thumb-body"><span class="video-thumb-title">{html.escape(display)}</span>'
        '<span class="video-thumb-caption">Opens SharePoint video in a new tab</span></span>'
        "</a>"
    )


def render_slides_link_card(slides_path: str, output_dir: Path, page_path: Path, title: str = "") -> str:
    """Render a prominent link card for an HTML slides file."""
    label = title.strip() or "View Slides"
    abs_slides = (output_dir / slides_path).resolve()
    rel = Path(os.path.relpath(abs_slides, page_path.parent)).as_posix()
    return (
        f'<a class="slides-link-card" href="{html.escape(rel, quote=True)}" '
        'target="_blank" rel="noopener noreferrer">'
        '<span class="slides-icon" aria-hidden="true">&#9633;</span>'
        f'<span class="slides-link-label">{html.escape(label)}</span>'
        '<span class="slides-link-hint">Opens slides in a new tab</span>'
        "</a>"
    )


def render_standalone_youtube_embed(text: str) -> str | None:
    candidate = extract_standalone_link_target(text)
    if not candidate:
        return None
    # SharePoint videos: render as link card instead of iframe
    if is_sharepoint_url(candidate):
        label = ""
        stripped = text.strip()
        md_match = re.fullmatch(r"\[([^\]]+)\]\((https?://[^)]+)\)", stripped)
        if md_match:
            label = md_match.group(1)
        return render_sharepoint_link_card(candidate, label)
    video_id = extract_youtube_video_id(candidate)
    if not video_id:
        return None
    embed_url = f"https://www.youtube.com/embed/{video_id}"
    return (
        '<div class="video-embed">'
        f'<iframe src="{embed_url}" title="YouTube video player" loading="lazy" '
        'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
        'allowfullscreen></iframe>'
        "</div>"
    )


def extract_standalone_link_target(text: str) -> str | None:
    stripped = text.strip()
    if not stripped:
        return None
    markdown_link = re.fullmatch(r"\[([^\]]+)\]\((https?://[^)]+)\)", stripped)
    if markdown_link:
        return markdown_link.group(2).strip()
    plain_url = re.fullmatch(r"(https?://\S+)", stripped)
    if plain_url:
        return plain_url.group(1).strip()
    return None


def extract_youtube_video_id(url: str) -> str | None:
    try:
        parsed = urlparse(url)
    except ValueError:
        return None

    host = parsed.netloc.lower()
    path = parsed.path.strip("/")
    video_id = None
    if host in {"youtu.be", "www.youtu.be"}:
        video_id = path.split("/", 1)[0]
    elif host in {"youtube.com", "www.youtube.com", "m.youtube.com", "youtube-nocookie.com", "www.youtube-nocookie.com"}:
        if path == "watch":
            video_id = parse_qs(parsed.query).get("v", [None])[0]
        elif path.startswith("embed/"):
            video_id = path.split("/", 1)[1]
        elif path.startswith("shorts/"):
            video_id = path.split("/", 1)[1]

    if not video_id:
        return None
    video_id = video_id.split("/", 1)[0]
    if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
        return None
    return video_id


def is_external_url(target: str) -> bool:
    parsed = urlparse(target)
    return parsed.scheme in {"http", "https"}


def extract_markdown_destination(target: str) -> str:
    stripped = target.strip()
    if stripped.startswith("<") and stripped.endswith(">"):
        stripped = stripped[1:-1].strip()
    for delimiter in (' "', " '"):
        marker_index = stripped.find(delimiter)
        if marker_index != -1:
            return stripped[:marker_index].strip()
    return stripped


def ordered_modules(courses: dict[str, CourseInfo], course_order: list[str] | None = None) -> list[ModuleInfo]:
    order = course_order if course_order is not None else COURSE_ORDER
    modules: list[ModuleInfo] = []
    for course_key in order:
        course = courses.get(course_key)
        if course:
            modules.extend(course.modules)
    # For config-mode bundles, any course key not in a legacy order should still appear
    seen = set(order)
    for key, course in courses.items():
        if key not in seen:
            modules.extend(course.modules)
    return modules


def schedule_rows(courses: dict[str, CourseInfo]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for module in ordered_modules(courses):
        item_count = sum(len(module.items[category]) for category in CATEGORY_ORDER)
        quiz_count = sum(1 for item in module.items["assessments"] if item.quiz)
        rows.append(
            {
                "module_slug": module.slug,
                "label": module.label,
                "headline": module.headline,
                "summary": module.summary or summarize_text(" ".join(item.summary for category in CATEGORY_ORDER for item in module.items[category]), 180),
                "item_count": item_count,
                "quiz_count": quiz_count,
            }
        )
    return rows


def site_title(courses: dict[str, CourseInfo]) -> str:
    if len(courses) == 1:
        return next(iter(courses.values())).title
    return "Generative AI Course Sequence"


def site_subtitle(courses: dict[str, CourseInfo]) -> str:
    return "CU Boulder-branded static LMS site generated from forward course materials."


def course_id_from_input_dir(input_dir: Path) -> str:
    return slugify(input_dir.name) or "forward-course"


def make_page_context(
    course_id: str,
    page_id: str,
    title: str,
    url: str,
    text: str,
    module_id: str | None = None,
    source_type: str = "page",
) -> dict[str, Any]:
    return {
        "course_id": course_id,
        "page_id": page_id,
        "title": title,
        "url": url,
        "text": clean_text(text),
        "module_id": module_id,
        "source_type": source_type,
    }


def html_to_visible_text(value: str) -> str:
    if not value:
        return ""
    text = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", value, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</(p|div|section|article|li|ul|ol|h[1-6]|pre|blockquote|fieldset|legend)>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    return clean_text(html.unescape(text))


def page_context_script(page_context: dict[str, Any] | None) -> str:
    if not page_context:
        return ""
    payload = json.dumps(page_context, ensure_ascii=True).replace("</", "<\\/")
    return f'\n  <script id="bobpe-page-context" type="application/json">{payload}</script>'


def render_page(
    title: str,
    body: str,
    relative_root: str,
    page_class: str = "",
    page_context: dict[str, Any] | None = None,
) -> str:
    class_attr = f' class="{page_class}"' if page_class else ""
    chat_links = (
        f'\n  <link rel="stylesheet" href="{relative_root}chat_widget.css">'
        f'\n  <script defer src="{relative_root}chat_widget.js"></script>'
        if _INCLUDE_CHATBOT
        else ""
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{relative_root}style.css">{chat_links}
  <script defer src="{relative_root}app.js"></script>
</head>
<body{class_attr}>
  {body}
  {page_context_script(page_context)}
</body>
</html>
"""


def render_site_header(relative_root: str, current: str = "", config: dict | None = None) -> str:
    def nav_link(href: str, label: str, key: str) -> str:
        class_name = ' class="is-current"' if current == key else ""
        return f'<a{class_name} href="{href}">{html.escape(label)}</a>'

    if config:
        brand = config.get("course_title", "Course")
        # Build nav from admin public files + always-present Home and Results
        nav_links = [nav_link(f"{relative_root}index.html", "Home", "home")]
        for fname in config.get("admin", {}).get("public_files", []):
            stem = Path(fname).stem
            out_name = f"{slugify(stem)}.html"
            label = stem.replace("_", " ").title()
            nav_links.append(nav_link(f"{relative_root}{out_name}", label, slugify(stem)))
        nav_links.append(nav_link(f"{relative_root}labs.html", "Labs", "labs"))
        nav_links.append(nav_link(f"{relative_root}results.html", "Results", "results"))
        nav_html = "\n          ".join(nav_links)
    else:
        brand = "CU Boulder Forward LMS"
        nav_html = "\n          ".join([
            nav_link(f"{relative_root}index.html", "Home", "home"),
            nav_link(f"{relative_root}syllabus.html", "Syllabus", "syllabus"),
            nav_link(f"{relative_root}schedule.html", "Schedule", "schedule"),
            nav_link(f"{relative_root}results.html", "Results", "results"),
        ])

    return f"""
    <header class="site-header">
      <div class="site-header-inner">
        <a class="brand" href="{relative_root}index.html">{html.escape(brand)}</a>
        <nav class="top-nav">
          {nav_html}
        </nav>
      </div>
    </header>
    """


def render_site_footer() -> str:
    return """
    <footer class="site-footer">
      <p>Generated by <code>Forward/generate_html_course.py</code> with relative-link navigation and client-side quiz state.</p>
    </footer>
    """


def write_assets(output_dir: Path, chatbot_config: dict | None = None) -> None:
    (output_dir / "style.css").write_text(STYLE_CSS, encoding="utf-8")
    (output_dir / "app.js").write_text(APP_JS, encoding="utf-8")

    if not _INCLUDE_CHATBOT:
        return

    widget_js = (Path(__file__).resolve().parent / "ui" / "chat_widget.js").read_text(encoding="utf-8")
    if chatbot_config is not None:
        # Bake the chatbot config into the generated JS at build time
        config_payload = json.dumps(chatbot_config, ensure_ascii=True).replace("</", "<\\/")
        config_prefix = f"window.BOBPE_CHATBOT_CONFIG = {config_payload};\n"
        widget_js = config_prefix + widget_js
    (output_dir / "chat_widget.js").write_text(widget_js, encoding="utf-8")
    (output_dir / "chat_widget.css").write_text((Path(__file__).resolve().parent / "ui" / "chat_widget.css").read_text(encoding="utf-8"), encoding="utf-8")


def module_slug_for_course_week(config: dict, course_week: int) -> str | None:
    for seg_cfg in config.get("segments", []):
        seg_key = seg_cfg.get("key")
        if not seg_key:
            continue
        start_week = seg_cfg.get("course_week_start", 1)
        week_count = seg_cfg.get("weeks", 0)
        end_week = start_week + week_count - 1
        if start_week <= course_week <= end_week:
            rel_week = course_week - start_week + 1
            return f"{str(seg_key).lower()}-week_{rel_week}"
    return None


def parse_concept_quiz_question(block: str) -> dict[str, Any] | None:
    type_match = re.search(r"\*\*Type:\*\*\s*(.+)", block)
    prompt_match = re.search(r"\*\*Learner-facing question:\*\*\s*(.+?)(?:\n\n\*\*Expert response:\*\*)", block, flags=re.DOTALL)
    if not type_match or not prompt_match:
        return None

    question_type_raw = clean_text(type_match.group(1)).lower()
    prompt_section = prompt_match.group(1).strip()
    prompt_lines = [line.rstrip() for line in prompt_section.splitlines()]
    prompt = clean_text(prompt_lines[0]) if prompt_lines else ""
    options: list[str] = []
    for line in prompt_lines[1:]:
        stripped = line.strip()
        option_match = re.match(r"^[A-D]\.\s*(.+)$", stripped)
        if option_match:
            options.append(clean_text(option_match.group(1)))

    question_type = "multiple_choice" if "multiple choice" in question_type_raw else "open_response"
    payload: dict[str, Any] = {
        "type": question_type,
        "prompt": prompt,
    }
    if options:
        payload["options"] = options
    return payload


def parse_concept_quiz_markdown(markdown_text: str) -> tuple[str, list[dict[str, Any]]]:
    focus_match = re.search(r"## Week Focus\s+(.+?)(?:\n## |\Z)", markdown_text, flags=re.DOTALL)
    week_focus = clean_text(focus_match.group(1)) if focus_match else ""

    question_blocks = re.findall(r"### Q\d+\s+(.+?)(?=\n### Q\d+\s+|\Z)", markdown_text, flags=re.DOTALL)
    questions: list[dict[str, Any]] = []
    for block in question_blocks:
        question = parse_concept_quiz_question(block)
        if question:
            questions.append(question)
    return week_focus, questions


def build_concept_quiz_previews(input_dir: Path, config: dict | None) -> dict[str, dict[str, Any]]:
    if config is None:
        return {}

    concept_quiz_dir = input_dir / "concept_quizzes"
    if not concept_quiz_dir.exists():
        return {}

    previews: dict[str, dict[str, Any]] = {}
    for path in sorted(concept_quiz_dir.iterdir(), key=lambda p: natural_sort_key(p.name)):
        if not path.is_file():
            continue
        match = CONCEPT_QUIZ_FILENAME_RE.match(path.name)
        if not match:
            continue

        course_week = int(match.group(1))
        module_slug = module_slug_for_course_week(config, course_week)
        if not module_slug:
            continue

        week_focus, questions = parse_concept_quiz_markdown(read_text(path))
        if not questions:
            continue

        previews[module_slug] = {
            "week_label": f"Week {course_week}",
            "week_focus": week_focus,
            "questions": questions,
        }
    return previews


def write_concept_quiz_previews(output_dir: Path, previews: dict[str, dict[str, Any]]) -> None:
    (output_dir / "concept_quizzes_preview.json").write_text(
        json.dumps(previews, indent=2),
        encoding="utf-8",
    )


def write_manifest(output_dir: Path, courses: dict[str, CourseInfo], course_id: str) -> None:
    payload = {
        "course_id": course_id,
        "site_title": site_title(courses),
        "courses": [asdict(course) for course in courses.values()],
        "schedule": schedule_rows(courses),
    }
    (output_dir / "manifest.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")


def write_admin_pages(
    input_dir: Path,
    output_dir: Path,
    config: dict,
    course_id: str,
    page_contexts: list[dict[str, Any]],
) -> None:
    """Render each admin.public_files entry from meta/ as a top-level HTML page."""
    meta_dir = input_dir / "meta"
    public_files: list[str] = config.get("admin", {}).get("public_files", [])
    brand = config.get("course_title", "Course")
    for filename in public_files:
        source = meta_dir / filename
        if not source.exists():
            continue
        stem = Path(filename).stem
        out_name = f"{slugify(stem)}.html"
        text = clean_text(read_text(source))
        page_path = output_dir / out_name
        render_ctx = MarkdownRenderContext(
            input_dir=input_dir, output_dir=output_dir, page_path=page_path, source_path=source.resolve()
        )
        content_html = markdown_to_html(text, render_ctx)
        page_title = stem.replace("_", " ").title()
        body = f"""
        {render_site_header('./', slugify(stem), config=config)}
        <main class="page-shell">
          <section class="hero compact">
            <p class="eyebrow">{html.escape(brand)}</p>
            <h1>{html.escape(page_title)}</h1>
          </section>
          <section class="content-card markdown-body" style="padding:1.5rem">
            {content_html}
          </section>
        </main>
        {render_site_footer()}
        """
        page_ctx = make_page_context(
            course_id=course_id,
            page_id=slugify(stem),
            title=page_title,
            url=out_name,
            text=text,
            source_type="overview",
        )
        page_contexts.append(page_ctx)
        page_path.write_text(render_page(page_title, body, "./", page_context=page_ctx), encoding="utf-8")


def compute_item_page_filenames(module: ModuleInfo) -> dict[str, str]:
    """Map item.id → page filename using the same ordering as write_module_pages."""
    pages = flatten_module_items(module)
    return {item.id: f"page-{i:02d}.html" for i, item in enumerate(pages, start=1)}


def render_week_detail_panel(module: ModuleInfo, page_filenames: dict[str, str]) -> str:
    """Render the hidden expanded detail panel for a dashboard week cell."""
    parts: list[str] = []
    icon_map = {"lectures": "📽", "readings": "📖", "assessments": "📋"}
    for category in CATEGORY_ORDER:
        items = [item for item in module.items.get(category, []) if item_has_content_variants(item)]
        if not items:
            continue
        icon = icon_map[category]
        rows: list[str] = []
        for item in items:
            filename = page_filenames.get(item.id, "index.html")
            page_href = f"modules/{html.escape(module.slug)}/{html.escape(filename)}"
            slides_btn = ""
            for v in item.variants:
                vpath = Path(v.source_path)
                if vpath.stem.lower().endswith("_slides") and vpath.suffix.lower() in {".html", ".htm"}:
                    slides_btn = (
                        f'<a class="dash-btn dash-btn--slides" href="{html.escape(v.source_path)}"'
                        f' target="_blank" rel="noopener">View Slides →</a>'
                    )
                    break
            item_class = "dash-item dash-item--assessment" if category == "assessments" else "dash-item"
            rows.append(
                f'<div class="{item_class}">'
                f'<span class="dash-item-icon">{icon}</span>'
                f'<span class="dash-item-title">{html.escape(item.title)}</span>'
                f'<div class="dash-item-actions">{slides_btn}'
                f'<a class="dash-btn dash-btn--go" href="{page_href}">Go to Page →</a>'
                f"</div></div>"
            )
        sec_class = "dash-section dash-section--assessments" if category == "assessments" else "dash-section"
        parts.append(
            f'<div class="{sec_class}">'
            f'<h4 class="dash-section-label">{category.upper()}</h4>'
            f'{"".join(rows)}'
            f"</div>"
        )
    return "".join(parts)


def render_dashboard_grid(courses: dict[str, CourseInfo], config: dict) -> str:
    """Render three-column segment dashboard grid for the config-mode home page."""
    seg_order = [seg["key"] for seg in config.get("segments", [])]
    seg_labels = {seg["key"]: seg.get("label", seg["key"]) for seg in config.get("segments", [])}

    cols: list[str] = []
    for seg_key in seg_order:
        course = courses.get(seg_key)
        if course is None:
            continue
        cells: list[str] = []
        for module in course.modules:
            page_filenames = compute_item_page_filenames(module)
            has_content = any(
                item_has_content_variants(item)
                for cat in CATEGORY_ORDER
                for item in module.items.get(cat, [])
            )
            if not has_content:
                continue
            week_key = html.escape(f"{seg_key}-{module.key}")
            badges: list[str] = []
            if any(item_has_content_variants(i) for i in module.items.get("lectures", [])):
                badges.append('<span class="dash-badge dash-badge--lecture" title="Lectures">📽</span>')
            if any(item_has_content_variants(i) for i in module.items.get("readings", [])):
                badges.append('<span class="dash-badge dash-badge--reading" title="Readings">📖</span>')
            if any(item_has_content_variants(i) for i in module.items.get("assessments", [])):
                badges.append('<span class="dash-badge dash-badge--assess" title="Assessments">📋</span>')
            detail = render_week_detail_panel(module, page_filenames)
            cells.append(
                f'<div class="dash-week-cell" data-week-key="{week_key}">'
                f'<button class="dash-week-header" aria-expanded="false">'
                f'<span class="dash-week-label">{html.escape(module.label)}</span>'
                f'<span class="dash-week-badges">{"".join(badges)}</span>'
                f'<span class="dash-chevron" aria-hidden="true">▶</span>'
                f"</button>"
                f'<div class="dash-week-detail" hidden>{detail}</div>'
                f"</div>"
            )
        if not cells:
            cells = ['<p class="dash-placeholder muted">Content coming soon</p>']
        cols.append(
            f'<div class="dash-segment-col">'
            f'<div class="dash-segment-header">'
            f'<p class="eyebrow">{html.escape(seg_key)}</p>'
            f'<h2 class="dash-segment-title">{html.escape(seg_labels.get(seg_key, seg_key))}</h2>'
            f"</div>"
            f'<div class="dash-week-list">{"".join(cells)}</div>'
            f"</div>"
        )
    return f'<section class="dash-grid">{"".join(cols)}</section>'


def write_root_pages(
    input_dir: Path,
    output_dir: Path,
    courses: dict[str, CourseInfo],
    course_id: str,
    page_contexts: list[dict[str, Any]],
    config: dict | None = None,
) -> None:
    course_order = [seg["key"] for seg in config["segments"]] if config else None
    modules = ordered_modules(courses, course_order)
    first_module_href = f"modules/{modules[0].slug}/index.html" if modules else "schedule.html"

    # Determine display titles from config or legacy logic
    if config:
        page_site_title = config.get("course_title", "Course")
        page_site_subtitle = config.get("course_subtitle", "")
        page_eyebrow = config.get("course_subtitle", "Lightweight LMS Site")
    else:
        page_site_title = site_title(courses)
        page_site_subtitle = site_subtitle(courses)
        page_eyebrow = "Lightweight LMS Site"

    # Build content area — dashboard in config mode, card grid in legacy mode
    if config is not None:
        content_grid = render_dashboard_grid(courses, config)
    else:
        course_cards = []
        for course in courses.values():
            intro = course_excerpt(course.overview_text)
            course_cards.append(
                f"""
                <article class="feature-card">
                  <p class="eyebrow">{html.escape(course.key)}</p>
                  <h2>{html.escape(course.title)}</h2>
                  <p class="muted">{html.escape(course.official_title)}</p>
                  <p>{html.escape(intro)}</p>
                </article>
                """
            )
        content_grid = f'<section class="card-grid">{"".join(course_cards)}</section>'

    # Build hero action buttons: always Start + Results; add admin public pages links if config
    hero_links = [f'<a class="primary-button" href="{first_module_href}">Start the sequence</a>']
    if config:
        for fname in config.get("admin", {}).get("public_files", []):
            stem = Path(fname).stem
            out_name = f"{slugify(stem)}.html"
            label = stem.replace("_", " ").title()
            hero_links.append(f'<a class="secondary-button" href="{out_name}">{html.escape(label)}</a>')
        hero_links.append(f'<a class="secondary-button" href="labs.html">Labs</a>')
    else:
        hero_links.append('<a class="secondary-button" href="syllabus.html">View syllabus</a>')
        hero_links.append('<a class="secondary-button" href="schedule.html">Open schedule</a>')

    landing_body = f"""
    {render_site_header('./', 'home', config=config)}
    <main class="page-shell">
      <section class="hero">
        <p class="eyebrow">{html.escape(page_eyebrow)}</p>
        <h1>{html.escape(page_site_title)}</h1>
        <p class="lead">{html.escape(page_site_subtitle)}</p>
        <div class="hero-actions">
          {''.join(hero_links)}
        </div>
      </section>
      {content_grid}
    </main>
    {render_site_footer()}
    """
    landing_context = make_page_context(
        course_id=course_id,
        page_id="home",
        title=page_site_title,
        url="index.html",
        text="\n".join([page_site_title, page_site_subtitle, *(course.title for course in courses.values())]),
        source_type="overview",
    )
    page_contexts.append(landing_context)
    (output_dir / "index.html").write_text(
        render_page(page_site_title, landing_body, "./", page_context=landing_context),
        encoding="utf-8",
    )

    # In config mode, syllabus/schedule come from admin pages (write_admin_pages).
    # In legacy mode, write the auto-generated syllabus and schedule.
    if config is None:
        syllabus_sections = []
        ladder_path = input_dir / "meta" / "C2_C3_learning_ladder.md"
        ladder_text = ""
        if ladder_path.exists():
            ladder_text = clean_text(read_text(ladder_path))
        for course in courses.values():
            assessment_count = sum(len(module.items["assessments"]) for module in course.modules)
            syllabus_sections.append(
                f"""
                <section class="content-card">
                  <p class="eyebrow">{html.escape(course.key)}</p>
                  <h2>{html.escape(course.title)}</h2>
                  <p class="muted">{html.escape(course.official_title)}</p>
                  <div class="markdown-body">{markdown_to_html(course.overview_text, MarkdownRenderContext(input_dir=input_dir, output_dir=output_dir, page_path=output_dir / "syllabus.html", source_path=(input_dir / course.overview_path).resolve() if course.overview_path else None))}</div>
                  <div class="syllabus-meta">
                    <div><strong>Assessment structure</strong><span>{assessment_count} assessment page(s) with immediate-feedback quizzes where structured quiz markup exists.</span></div>
                    <div><strong>Learning mode</strong><span>Asynchronous lecture, reading, and module-based assessment flow.</span></div>
                    <div><strong>Progression</strong><span>Modules unlock sequentially through relative-link navigation; quiz completion is tracked client-side.</span></div>
                  </div>
                </section>
                """
            )
        if ladder_text:
            syllabus_sections.append(
                f"""
                <section class="content-card">
                  <p class="eyebrow">Learning Ladder</p>
                  <h2>Conceptual Progression</h2>
                  <div class="markdown-body">{markdown_to_html(ladder_text, MarkdownRenderContext(input_dir=input_dir, output_dir=output_dir, page_path=output_dir / "syllabus.html", source_path=ladder_path.resolve()))}</div>
                </section>
                """
            )

        syllabus_body = f"""
        {render_site_header('./', 'syllabus', config=None)}
        <main class="page-shell">
          <section class="hero compact">
            <p class="eyebrow">Syllabus</p>
            <h1>Course sequence overview</h1>
            <p class="lead">High-level course descriptions, learning structure, and assessment posture derived from the source meta files.</p>
          </section>
          {''.join(syllabus_sections)}
        </main>
        {render_site_footer()}
        """
        syllabus_context = make_page_context(
            course_id=course_id,
            page_id="syllabus",
            title="Syllabus",
            url="syllabus.html",
            text="\n".join([course.overview_text for course in courses.values()] + ([ladder_text] if ladder_text else [])),
            source_type="overview",
        )
        page_contexts.append(syllabus_context)
        (output_dir / "syllabus.html").write_text(
            render_page("Syllabus", syllabus_body, "./", page_context=syllabus_context),
            encoding="utf-8",
        )

        schedule_cards = []
        for row in schedule_rows(courses):
            schedule_cards.append(
                f"""
                <article class="schedule-card">
                  <p class="eyebrow">{html.escape(row['label'])}</p>
                  <h2>{html.escape(row['headline'])}</h2>
                  <p>{html.escape(row['summary'])}</p>
                  <div class="schedule-meta">
                    <span>{row['item_count']} pages</span>
                    <span>{row['quiz_count']} quiz page(s)</span>
                  </div>
                  <a class="secondary-button" href="modules/{row['module_slug']}/index.html">Open module</a>
                </article>
                """
            )
        schedule_body = f"""
        {render_site_header('./', 'schedule', config=None)}
        <main class="page-shell">
          <section class="hero compact">
            <p class="eyebrow">Schedule</p>
            <h1>Module-by-module sequence</h1>
            <p class="lead">Ordered module overview spanning the full sample-course sequence.</p>
          </section>
          <section class="card-grid">
            {''.join(schedule_cards)}
          </section>
        </main>
        {render_site_footer()}
        """
        schedule_context = make_page_context(
            course_id=course_id,
            page_id="schedule",
            title="Schedule",
            url="schedule.html",
            text="\n".join(
                f"{row['label']} {row['headline']} {row['summary']}"
                for row in schedule_rows(courses)
            ),
            source_type="overview",
        )
        page_contexts.append(schedule_context)
        (output_dir / "schedule.html").write_text(
            render_page("Schedule", schedule_body, "./", page_context=schedule_context),
            encoding="utf-8",
        )

    results_body = f"""
    {render_site_header('./', 'results', config=config)}
    <main class="page-shell">
      <section class="hero compact">
        <p class="eyebrow">Results</p>
        <h1>Client-side quiz summary</h1>
        <p class="lead">Scores are stored in your browser only. Reopening the site on this machine will retain them until local storage is cleared.</p>
      </section>
      <section class="content-card">
        <div class="results-summary" data-results-root="true"></div>
      </section>
    </main>
    {render_site_footer()}
    """
    results_context = make_page_context(
        course_id=course_id,
        page_id="results",
        title="Results",
        url="results.html",
        text="Client-side quiz summary page for the generated Forward LMS.",
        source_type="overview",
    )
    page_contexts.append(results_context)
    (output_dir / "results.html").write_text(
        render_page("Results", results_body, "./", page_context=results_context),
        encoding="utf-8",
    )


def course_excerpt(text: str) -> str:
    paragraphs = [paragraph.strip() for paragraph in text.split("\n\n") if paragraph.strip()]
    if not paragraphs:
        return ""
    cleaned: list[str] = []
    for paragraph in paragraphs:
        if paragraph.startswith("#"):
            continue
        cleaned.append(re.sub(r"[*#`_]+", "", paragraph).strip())
        if len(cleaned) == 2:
            break
    return summarize_text(" ".join(cleaned), 420)


def flatten_module_items(module: ModuleInfo) -> list[ContentItem]:
    ordered: list[ContentItem] = []
    for category in CATEGORY_ORDER:
        ordered.extend(sorted(module.items[category], key=lambda item: item.order))
    return ordered


def write_module_pages(
    input_dir: Path,
    output_dir: Path,
    courses: dict[str, CourseInfo],
    course_id: str,
    page_contexts: list[dict[str, Any]],
    config: dict | None = None,
) -> None:
    course_order = [seg["key"] for seg in config["segments"]] if config else None
    modules = ordered_modules(courses, course_order)
    modules_root = output_dir / "modules"
    modules_root.mkdir(parents=True, exist_ok=True)

    for module_index, module in enumerate(modules):
        module_dir = modules_root / module.slug
        module_dir.mkdir(parents=True, exist_ok=True)
        pages = flatten_module_items(module)
        for page_number, item in enumerate(pages, start=1):
            item.page_filename = f"page-{page_number:02d}.html"

        write_module_index(module_dir, module, modules, module_index, pages, course_id, page_contexts, config=config)

        for page_number, item in enumerate(pages):
            prev_href, next_href, requires_quiz = page_navigation(modules, module_index, pages, page_number, item)
            page_html = render_module_item_page(
                input_dir, output_dir, module, item, prev_href, next_href, requires_quiz, course_id, page_contexts,
                config=config,
            )
            (module_dir / item.page_filename).write_text(page_html, encoding="utf-8")


def write_module_index(
    module_dir: Path,
    module: ModuleInfo,
    modules: list[ModuleInfo],
    module_index: int,
    pages: list[ContentItem],
    course_id: str,
    page_contexts: list[dict[str, Any]],
    config: dict | None = None,
) -> None:
    previous_module = modules[module_index - 1] if module_index > 0 else None
    next_module = modules[module_index + 1] if module_index + 1 < len(modules) else None

    objectives_html = "".join(f"<li>{html.escape(goal)}</li>" for goal in module.learning_goals)
    page_cards = []
    for item in pages:
        page_cards.append(
            f"""
            <li class="module-page-row">
              <a href="{item.page_filename}">{html.escape(item.title)}</a>
              <span>{html.escape(item.type_label)}</span>
              <span>{item.estimated_minutes} min</span>
            </li>
            """
        )

    quiz_count = sum(1 for item in pages if item.quiz)
    body = f"""
    {render_site_header('../../', '', config=config)}
    <main class="page-shell">
      <nav class="breadcrumbs">
        <a href="../../index.html">Home</a>
        <a href="../../schedule.html">Schedule</a>
        <span>{html.escape(module.label)}</span>
      </nav>
      <section class="hero compact">
        <p class="eyebrow">{html.escape(module.label)}</p>
        <h1>{html.escape(module.headline)}</h1>
        <p class="lead">{html.escape(module.summary or 'Work through the sequence below in order. Lectures, readings, and assessments are arranged to match the source module structure.')}</p>
        <div class="hero-actions">
          <a class="primary-button" href="{pages[0].page_filename if pages else '../../schedule.html'}">Start module</a>
          <a class="secondary-button" href="../../results.html">View results</a>
        </div>
      </section>
      <section class="module-overview-grid">
        <article class="content-card">
          <h2>Learning Goals</h2>
          <ul>{objectives_html or '<li>No explicit learning goals were found in the source meta file.</li>'}</ul>
        </article>
        <article class="content-card">
          <h2>Module Details</h2>
          <dl class="meta-list">
            <div><dt>Weekly flow</dt><dd>{html.escape(module.weekly_flow or 'Lecture -> reading -> assessment')}</dd></div>
            <div><dt>Total pages</dt><dd>{len(pages)}</dd></div>
            <div><dt>Interactive quizzes</dt><dd>{quiz_count}</dd></div>
          </dl>
          <div class="module-quiz-summary" data-module-id="{html.escape(module.slug)}"></div>
        </article>
      </section>
      <section class="content-card">
        <h2>Sequence</h2>
        <ol class="module-page-list">
          {''.join(page_cards)}
        </ol>
      </section>
      <section class="module-footer-nav">
        {f'<a class="secondary-button" href="../{previous_module.slug}/index.html">Previous module</a>' if previous_module else '<span></span>'}
        {f'<a class="secondary-button" href="../{next_module.slug}/index.html">Next module</a>' if next_module else '<a class="secondary-button" href="../../results.html">Results</a>'}
      </section>
    </main>
    {render_site_footer()}
    """
    module_context = make_page_context(
        course_id=course_id,
        page_id=f"{module.slug}-index",
        title=module.headline,
        url=f"modules/{module.slug}/index.html",
        text="\n".join(
            [
                module.headline,
                module.summary,
                module.weekly_flow,
                *module.learning_goals,
                *(f"{item.title} {item.summary}" for item in pages),
            ]
        ),
        module_id=module.slug,
        source_type="module_index",
    )
    page_contexts.append(module_context)
    (module_dir / "index.html").write_text(
        render_page(module.headline, body, "../../", page_context=module_context),
        encoding="utf-8",
    )


def page_navigation(
    modules: list[ModuleInfo],
    module_index: int,
    pages: list[ContentItem],
    page_index: int,
    item: ContentItem,
) -> tuple[str, str, bool]:
    prev_href = "index.html" if page_index == 0 else pages[page_index - 1].page_filename
    if page_index + 1 < len(pages):
        next_href = pages[page_index + 1].page_filename
    elif module_index + 1 < len(modules):
        next_href = f"../{modules[module_index + 1].slug}/index.html"
    else:
        next_href = "../../results.html"
    return prev_href, next_href, bool(item.quiz)


def render_module_item_page(
    input_dir: Path,
    output_dir: Path,
    module: ModuleInfo,
    item: ContentItem,
    prev_href: str,
    next_href: str,
    requires_quiz: bool,
    course_id: str,
    page_contexts: list[dict[str, Any]],
    config: dict | None = None,
) -> str:
    page_path = output_dir / "modules" / module.slug / item.page_filename
    source_path = None
    if item.variants:
        source_path = (input_dir / item.variants[item.primary_variant_index].source_path).resolve()
    render_context = MarkdownRenderContext(
        input_dir=input_dir,
        output_dir=output_dir,
        page_path=page_path,
        source_path=source_path,
    )

    # In config mode: separate out slides and chatbot_only variants from the source panel
    slides_card_html = ""
    if config is not None:
        visible_variants = []
        for variant in item.variants:
            vpath = Path(variant.source_path)
            vstem = vpath.stem.lower()
            vsuffix = vpath.suffix.lower()
            if vstem.endswith("_slides") and vsuffix in {".html", ".htm"}:
                # Render slides as prominent link card — copy the file to output
                dest = output_dir / variant.source_path
                dest.parent.mkdir(parents=True, exist_ok=True)
                src_abs = input_dir / variant.source_path
                if src_abs.exists() and not dest.exists():
                    shutil.copy2(src_abs, dest)
                slides_card_html += render_slides_link_card(variant.source_path, output_dir, page_path, item.title)
            elif not vstem.endswith("_outline"):
                # Public non-slides variants appear in source panel
                visible_variants.append(variant)
        source_links = "".join(
            f'<li><a href="../../{html.escape(v.normalized_path)}">{html.escape(v.label)}</a>'
            f'<span>{html.escape(v.source_path)}</span></li>'
            for v in visible_variants
        )
    else:
        source_links = "".join(
            f'<li><a href="../../{html.escape(variant.normalized_path)}">{html.escape(variant.label)}</a>'
            f'<span>{html.escape(variant.source_path)}</span></li>'
            for variant in item.variants
        )

    goals_html = "".join(f"<li>{html.escape(goal)}</li>" for goal in item.learning_goals)
    next_classes = "primary-button next-button"
    if requires_quiz:
        next_classes += " is-disabled"
    rendered_body_html = render_item_body_html(item, render_context)
    rendered_body_text = html_to_visible_text(rendered_body_html)

    # In config mode, include chatbot_only (outline) variant text in grounding even though
    # those files are not rendered on the page.
    extra_grounding_text = ""
    if config is not None:
        for variant in item.variants:
            vpath = Path(variant.source_path)
            if vpath.stem.lower().endswith("_outline") and variant.text:
                extra_grounding_text += "\n" + variant.text

    supplemental_page_text = clean_text(
        "\n".join(
            [
                module.label,
                item.type_label,
                item.title,
                item.summary,
                *item.learning_goals,
                rendered_body_text,
                extra_grounding_text,
            ]
        )
    )

    site_header = render_site_header("../../", "", config=config)
    body = f"""
    {site_header}
    <main class="page-shell">
      <nav class="breadcrumbs">
        <a href="../../index.html">Home</a>
        <a href="../../schedule.html">Schedule</a>
        <a href="index.html">{html.escape(module.label)}</a>
        <span>{html.escape(item.title)}</span>
      </nav>
      <section class="hero compact">
        <p class="eyebrow">{html.escape(module.label)} · {html.escape(item.type_label)}</p>
        <h1>{html.escape(item.title)}</h1>
        <p class="lead">{html.escape(item.summary)}</p>
        <div class="meta-chips">
          <span>{item.estimated_minutes} min</span>
          <span>{html.escape(item.category.title())}</span>
          <span>{len(item.variants)} source variant(s)</span>
        </div>
      </section>
      {f'<section class="content-card slides-card-section">{slides_card_html}</section>' if slides_card_html else ''}
      <section class="module-overview-grid">
        <article class="content-card">
          <h2>Learning Objectives</h2>
          <ul>{goals_html or '<li>No item-specific objectives found; module-level goals are unavailable for this page.</li>'}</ul>
        </article>
        <article class="content-card">
          <h2>Source Variants</h2>
          <ul class="source-link-list">{source_links}</ul>
        </article>
      </section>
      <section class="content-card lesson-body">
        {rendered_body_html}
      </section>
      <section class="page-nav">
        <a class="secondary-button" href="{prev_href}">Previous</a>
        <a class="{next_classes}" href="{next_href}" {'data-requires-quiz="true"' if requires_quiz else ''}>Next</a>
      </section>
    </main>
    {render_site_footer()}
    """
    page_context = make_page_context(
        course_id=course_id,
        page_id=f"{module.slug}-{item.slug}",
        title=item.title,
        url=f"modules/{module.slug}/{item.page_filename}",
        text=supplemental_page_text,
        module_id=module.slug,
    )
    page_contexts.append(page_context)
    return render_page(item.title, body, "../../", page_context=page_context)


STYLE_CSS = """\
:root {
  --cu-gold: #CFB87C;
  --cu-light-gray: #A2A4A3;
  --cu-ink: #1f1f1f;
  --cu-paper: #f7f5ef;
  --cu-card: rgba(255, 255, 255, 0.94);
  --cu-border: #d5d0c4;
  --cu-shadow: 0 18px 45px rgba(44, 42, 37, 0.08);
  --font-sans: "Helvetica Neue", Helvetica, Arial, sans-serif;
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  font-family: var(--font-sans);
  color: var(--cu-ink);
  background:
    radial-gradient(circle at top left, rgba(207, 184, 124, 0.25), transparent 32%),
    linear-gradient(180deg, rgba(162, 164, 163, 0.18), rgba(247, 245, 239, 0.88)),
    var(--cu-paper);
}

a {
  color: inherit;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 20;
  backdrop-filter: blur(12px);
  background: rgba(31, 31, 31, 0.92);
  color: white;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.site-header-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem 1.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.brand {
  text-decoration: none;
  font-weight: 800;
  letter-spacing: 0.03em;
}

.top-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
}

.top-nav a {
  text-decoration: none;
  color: rgba(255, 255, 255, 0.85);
  padding: 0.55rem 0.85rem;
  border-radius: 999px;
}

.top-nav a.is-current,
.top-nav a:hover {
  background: rgba(207, 184, 124, 0.18);
  color: white;
}

.page-shell {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1.5rem 1.25rem 3rem;
}

.hero,
.feature-card,
.content-card,
.schedule-card {
  background: var(--cu-card);
  border: 1px solid var(--cu-border);
  box-shadow: var(--cu-shadow);
  border-radius: 22px;
}

.hero {
  padding: 2rem;
  margin-bottom: 1.5rem;
  background:
    linear-gradient(135deg, rgba(207, 184, 124, 0.24), rgba(255, 255, 255, 0.96)),
    var(--cu-card);
}

.hero.compact {
  padding: 1.5rem;
}

.eyebrow {
  margin: 0 0 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-weight: 800;
  font-size: 0.78rem;
  color: #6b6148;
}

.lead {
  font-size: 1.05rem;
  max-width: 70ch;
}

.muted {
  color: #626764;
}

.hero-actions,
.page-nav,
.module-footer-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1.25rem;
}

.primary-button,
.secondary-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  border-radius: 999px;
  padding: 0.8rem 1.1rem;
  text-decoration: none;
  font-weight: 700;
  border: 1px solid transparent;
}

.primary-button {
  background: var(--cu-gold);
  color: #1b1b1b;
}

.secondary-button {
  background: rgba(162, 164, 163, 0.14);
  border-color: rgba(162, 164, 163, 0.4);
  color: #2a2e2d;
}

.primary-button.is-disabled,
.primary-button[aria-disabled="true"] {
  pointer-events: none;
  opacity: 0.5;
}

.card-grid,
.module-overview-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
}

.feature-card,
.content-card,
.schedule-card {
  padding: 1.4rem;
  margin-bottom: 1rem;
}

.breadcrumbs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  align-items: center;
  font-size: 0.95rem;
  margin-bottom: 1rem;
}

.breadcrumbs a {
  color: #5b4d29;
  text-decoration: none;
}

.breadcrumbs a::after {
  content: "/";
  margin-left: 0.55rem;
  color: var(--cu-light-gray);
}

.meta-chips,
.schedule-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1rem;
}

.meta-chips span,
.schedule-meta span {
  background: rgba(162, 164, 163, 0.18);
  border-radius: 999px;
  padding: 0.35rem 0.65rem;
  font-size: 0.88rem;
}

.meta-list {
  margin: 0;
}

.meta-list div,
.syllabus-meta div {
  display: grid;
  gap: 0.2rem;
  margin-bottom: 0.9rem;
}

.module-page-list,
.source-link-list {
  margin: 0;
  padding-left: 1.2rem;
}

.module-page-row,
.source-link-list li {
  display: grid;
  gap: 0.25rem;
  margin: 0.7rem 0;
}

.module-page-row span,
.source-link-list span {
  color: #606563;
  font-size: 0.9rem;
}

.concept-preview-card {
  background:
    linear-gradient(135deg, rgba(207, 184, 124, 0.16), rgba(255, 255, 255, 0.96)),
    var(--cu-card);
}

.concept-preview-intro,
.concept-preview-focus {
  margin: 0 0 0.85rem;
}

.concept-preview-focus {
  color: #49453b;
}

.concept-preview-list {
  list-style: none;
  padding: 0;
  margin: 1rem 0 0;
  display: grid;
  gap: 0.9rem;
}

.concept-preview-item {
  padding: 1rem 1.05rem;
  border-radius: 18px;
  border: 1px solid rgba(162, 164, 163, 0.28);
  background: rgba(255, 255, 255, 0.88);
}

.concept-preview-item-header {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.55rem;
  margin-bottom: 0.6rem;
}

.concept-preview-number,
.concept-preview-badge {
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  padding: 0.3rem 0.65rem;
  font-size: 0.8rem;
  font-weight: 800;
}

.concept-preview-number {
  background: rgba(31, 31, 31, 0.88);
  color: white;
}

.concept-preview-badge {
  background: rgba(207, 184, 124, 0.28);
  color: #473a18;
}

.concept-preview-prompt {
  margin: 0;
  font-weight: 700;
  line-height: 1.5;
}

.concept-preview-options {
  margin: 0.8rem 0 0 1.4rem;
  padding-left: 0.5rem;
  display: grid;
  gap: 0.45rem;
  color: #525754;
}

.lesson-body {
  line-height: 1.7;
}

.markdown-body h1,
.markdown-body h2,
.markdown-body h3,
.lesson-body h1,
.lesson-body h2,
.lesson-body h3,
.lesson-body h4 {
  line-height: 1.2;
  color: #2a2824;
}

.markdown-body hr,
.lesson-body hr {
  border: 0;
  border-top: 1px solid var(--cu-border);
  margin: 1.2rem 0;
}

.markdown-body code,
.lesson-body code {
  background: rgba(162, 164, 163, 0.16);
  border-radius: 4px;
  padding: 0.12rem 0.32rem;
}

.markdown-body pre,
.lesson-body pre {
  overflow-x: auto;
  background: #efebe3;
  border-radius: 14px;
  padding: 1rem;
}

.markdown-image {
  display: block;
  max-width: 100%;
  height: auto;
  margin: 1.25rem auto;
  border-radius: 16px;
  border: 1px solid rgba(162, 164, 163, 0.25);
  box-shadow: 0 10px 24px rgba(44, 42, 37, 0.08);
}

.video-thumb-card {
  display: block;
  margin: 1.5rem 0;
  overflow: hidden;
  border-radius: 18px;
  border: 1px solid rgba(162, 164, 163, 0.28);
  background: rgba(255, 255, 255, 0.88);
  box-shadow: 0 16px 32px rgba(44, 42, 37, 0.1);
  text-decoration: none;
}

.video-thumb-media {
  position: relative;
  display: block;
  background: #111;
}

.video-thumb-image {
  display: block;
  width: 100%;
  max-width: 100%;
  height: auto;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

.video-thumb-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 1rem;
  background: linear-gradient(180deg, rgba(0, 0, 0, 0.08), rgba(0, 0, 0, 0.66));
}

.video-thumb-play {
  width: 3.5rem;
  height: 3.5rem;
  border-radius: 999px;
  background: rgba(207, 184, 124, 0.95);
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.24);
  position: relative;
  flex: 0 0 auto;
}

.video-thumb-play::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-38%, -50%);
  border-top: 0.7rem solid transparent;
  border-bottom: 0.7rem solid transparent;
  border-left: 1.1rem solid #1f1f1f;
}

.video-thumb-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.4rem 0.7rem;
  border-radius: 999px;
  background: rgba(31, 31, 31, 0.82);
  color: white;
  font-size: 0.82rem;
  font-weight: 700;
}

.video-thumb-body {
  display: grid;
  gap: 0.25rem;
  padding: 1rem 1.1rem 1.15rem;
}

.video-thumb-title {
  font-weight: 800;
  color: #2a2824;
}

.video-thumb-caption {
  color: #5b605d;
  font-size: 0.95rem;
}

.included-text-block {
  margin: 1.25rem 0;
  padding: 1rem 1.1rem;
  border-radius: 16px;
  border: 1px solid rgba(162, 164, 163, 0.25);
  background: rgba(247, 245, 239, 0.74);
}

.include-error {
  color: #7b3f35;
  border-color: rgba(159, 95, 85, 0.35);
  background: rgba(159, 95, 85, 0.08);
}

.video-embed {
  position: relative;
  width: 100%;
  margin: 1.5rem 0;
  padding-top: 56.25%;
  overflow: hidden;
  border-radius: 18px;
  background: #111;
  box-shadow: 0 16px 32px rgba(31, 31, 31, 0.16);
}

.video-embed iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: 0;
}

.quiz-shell {
  display: grid;
  gap: 1.25rem;
}

.quiz-form {
  display: grid;
  gap: 1rem;
}

.quiz-question {
  border: 1px solid var(--cu-border);
  border-radius: 18px;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.72);
}

.quiz-question.is-correct {
  border-color: #4c7a43;
  background: rgba(76, 122, 67, 0.08);
}

.quiz-question.is-incorrect {
  border-color: #9f5f55;
  background: rgba(159, 95, 85, 0.08);
}

.quiz-question legend {
  font-weight: 800;
  padding: 0 0.3rem;
}

.quiz-options {
  display: grid;
  gap: 0.6rem;
  margin-top: 0.85rem;
}

.quiz-option {
  display: flex;
  gap: 0.75rem;
  align-items: flex-start;
  padding: 0.8rem 0.85rem;
  border-radius: 14px;
  border: 1px solid rgba(162, 164, 163, 0.28);
  background: rgba(247, 245, 239, 0.78);
}

.quiz-option input {
  margin-top: 0.18rem;
}

.quiz-feedback {
  margin-top: 0.8rem;
  padding: 0.8rem 0.95rem;
  border-radius: 12px;
  background: rgba(207, 184, 124, 0.16);
}

.quiz-actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.75rem;
}

.quiz-score {
  font-weight: 700;
}

.results-summary table {
  width: 100%;
  border-collapse: collapse;
}

.results-summary th,
.results-summary td {
  text-align: left;
  padding: 0.75rem 0.6rem;
  border-bottom: 1px solid var(--cu-border);
}

.site-footer {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.25rem 2rem;
  color: #555b58;
}

/* ── Dashboard grid ─────────────────────────────────── */

.dash-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-top: 1rem;
}

.dash-segment-col {
  background: var(--cu-card);
  border: 1px solid var(--cu-border);
  box-shadow: var(--cu-shadow);
  border-radius: 22px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.dash-segment-header {
  background: rgba(31, 31, 31, 0.92);
  color: white;
  padding: 1rem 1.1rem 0.85rem;
}

.dash-segment-header .eyebrow {
  color: var(--cu-gold);
  margin-bottom: 0.3rem;
}

.dash-segment-title {
  margin: 0;
  font-size: 0.95rem;
  font-weight: 700;
  line-height: 1.3;
  color: white;
}

.dash-week-list {
  padding: 0.5rem 0.6rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.dash-placeholder {
  padding: 1rem 0.4rem;
  font-size: 0.9rem;
}

.dash-week-cell {
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid transparent;
  transition: border-color 0.15s;
}

.dash-week-cell.is-active {
  border-color: var(--cu-gold);
}

.dash-week-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  width: 100%;
  background: none;
  border: none;
  cursor: pointer;
  text-align: left;
  padding: 0.6rem 0.7rem;
  border-radius: 12px;
  font-family: var(--font-sans);
  font-size: 0.88rem;
  color: var(--cu-ink);
  transition: background 0.12s;
}

.dash-week-header:hover {
  background: rgba(207, 184, 124, 0.14);
}

.dash-week-cell.is-active .dash-week-header {
  background: rgba(207, 184, 124, 0.18);
}

.dash-week-label {
  flex: 1;
  font-weight: 600;
  line-height: 1.3;
}

.dash-week-badges {
  display: flex;
  gap: 0.2rem;
  flex-shrink: 0;
}

.dash-badge {
  font-size: 0.8rem;
  padding: 0.1rem 0.28rem;
  border-radius: 999px;
  background: rgba(162, 164, 163, 0.16);
  line-height: 1.6;
}

.dash-chevron {
  font-size: 0.65rem;
  color: var(--cu-light-gray);
  transition: transform 0.2s;
  flex-shrink: 0;
}

.dash-week-cell.is-active .dash-chevron {
  transform: rotate(90deg);
}

.dash-week-detail {
  padding: 0 0.7rem 0.7rem;
}

.dash-section {
  margin-top: 0.6rem;
}

.dash-section-label {
  margin: 0 0 0.4rem;
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #6b6148;
}

.dash-item {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.35rem 0.5rem;
  padding: 0.45rem 0.5rem;
  border-radius: 8px;
  font-size: 0.85rem;
  margin-bottom: 0.2rem;
}

.dash-item--assessment {
  border: 1px solid rgba(207, 184, 124, 0.6);
  background: rgba(207, 184, 124, 0.1);
  border-radius: 10px;
  padding: 0.55rem 0.65rem;
}

.dash-item-icon {
  flex-shrink: 0;
  font-size: 0.85rem;
}

.dash-item-title {
  flex: 1;
  min-width: 0;
  font-weight: 600;
  line-height: 1.3;
}

.dash-item--assessment .dash-item-title {
  font-weight: 700;
}

.dash-item-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem;
  margin-left: auto;
}

.dash-btn {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.55rem;
  border-radius: 999px;
  font-size: 0.78rem;
  font-weight: 700;
  text-decoration: none;
  white-space: nowrap;
  border: 1px solid transparent;
}

.dash-btn--slides {
  background: rgba(162, 164, 163, 0.16);
  border-color: rgba(162, 164, 163, 0.35);
  color: #2a2e2d;
}

.dash-btn--go {
  background: var(--cu-gold);
  color: #1b1b1b;
}

.dash-item--assessment .dash-btn--go {
  background: rgba(207, 184, 124, 0.85);
  border: 1px solid rgba(180, 150, 80, 0.5);
  font-weight: 800;
}

/* ── Markdown pipe tables ───────────────────────────── */

.table-wrapper {
  overflow-x: auto;
  margin: 1.25rem 0;
  border-radius: 14px;
  border: 1px solid var(--cu-border);
}

.md-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.92rem;
}

.md-table thead tr {
  background: rgba(31, 31, 31, 0.88);
  color: white;
}

.md-table th {
  text-align: left;
  padding: 0.7rem 0.85rem;
  font-weight: 700;
  white-space: nowrap;
}

.md-table td {
  padding: 0.6rem 0.85rem;
  border-bottom: 1px solid var(--cu-border);
  vertical-align: top;
}

.md-table tbody tr:last-child td {
  border-bottom: none;
}

.md-table tbody tr:nth-child(even) td {
  background: rgba(162, 164, 163, 0.08);
}

@media (max-width: 760px) {
  .site-header-inner {
    flex-direction: column;
    align-items: flex-start;
  }

  .page-shell {
    padding: 1rem 1rem 2.5rem;
  }

  .hero,
  .feature-card,
  .content-card,
  .schedule-card {
    border-radius: 16px;
    padding: 1rem;
  }

  .page-nav,
  .module-footer-nav,
  .hero-actions {
    flex-direction: column;
  }

  .dash-grid {
    grid-template-columns: 1fr;
  }
}

/* ── Labs section ─────────────────────────────────── */

.labs-hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1.25rem;
}

.labs-card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.labs-card {
  background: var(--cu-card);
  border: 1px solid var(--cu-border);
  box-shadow: var(--cu-shadow);
  border-radius: 22px;
  padding: 1.4rem;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.labs-card h2 {
  margin: 0;
  font-size: 1.1rem;
  line-height: 1.25;
  color: #2a2824;
}

.labs-card p {
  margin: 0;
  color: #626764;
  font-size: 0.95rem;
  flex: 1;
}

.labs-card-footer {
  margin-top: 0.5rem;
}

.experiment-scaffold {
  background: var(--cu-card);
  border: 1px solid var(--cu-border);
  box-shadow: var(--cu-shadow);
  border-radius: 22px;
  padding: 1.5rem;
  margin-top: 1rem;
}

.experiment-scaffold h2 {
  margin: 0 0 0.75rem;
  color: #2a2824;
}

.scaffold-section {
  border: 1px dashed var(--cu-border);
  border-radius: 14px;
  padding: 1rem 1.1rem;
  margin-bottom: 0.85rem;
  background: rgba(247, 245, 239, 0.6);
}

.scaffold-section h3 {
  margin: 0 0 0.4rem;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #6b6148;
}

.scaffold-section p {
  margin: 0;
  color: #888;
  font-size: 0.9rem;
  font-style: italic;
}

.scaffold-section.compiled {
  border: 1px solid var(--cu-border);
  border-left: 3px solid var(--cu-gold);
  background: rgba(255, 255, 255, 0.82);
}

.scaffold-section.compiled h3 {
  color: #2a2824;
}

.compiled-content {
  line-height: 1.7;
  font-size: 0.95rem;
}

.compiled-content h1,
.compiled-content h2,
.compiled-content h3,
.compiled-content h4 {
  line-height: 1.25;
  color: #2a2824;
  margin-top: 1.2rem;
}

.compiled-content p {
  margin: 0.6rem 0;
}

.compiled-content ul,
.compiled-content ol {
  padding-left: 1.4rem;
  margin: 0.5rem 0;
}

.compiled-content code {
  background: rgba(162, 164, 163, 0.16);
  border-radius: 4px;
  padding: 0.12rem 0.32rem;
  font-size: 0.9em;
}

.compiled-content pre {
  overflow-x: auto;
  background: #efebe3;
  border-radius: 12px;
  padding: 0.9rem 1rem;
}

.compiled-content table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
  margin: 0.75rem 0;
}

.compiled-content th {
  background: rgba(31, 31, 31, 0.85);
  color: white;
  padding: 0.55rem 0.75rem;
  text-align: left;
}

.compiled-content td {
  padding: 0.5rem 0.75rem;
  border-bottom: 1px solid var(--cu-border);
  vertical-align: top;
}

.compiled-content tr:last-child td {
  border-bottom: none;
}

.compiled-content tr:nth-child(even) td {
  background: rgba(162, 164, 163, 0.07);
}

.instructor-resource-bar {
  background: rgba(31, 31, 31, 0.06);
  border: 1px solid var(--cu-border);
  border-radius: 16px;
  padding: 1rem 1.25rem;
  margin-top: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.instructor-resource-bar span {
  font-size: 0.88rem;
  color: #626764;
  flex: 1;
}
"""


APP_JS = """\
const STORAGE_KEY = "forwardLmsQuizScores";
let conceptQuizPreviewCache = null;

function loadScores() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
  } catch (_error) {
    return {};
  }
}

function saveScores(scores) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(scores));
}

function renderModuleSummaries() {
  const scores = loadScores();
  document.querySelectorAll("[data-module-id].module-quiz-summary").forEach((node) => {
    const moduleId = node.dataset.moduleId;
    const entries = Object.values(scores).filter((entry) => entry.moduleId === moduleId);
    if (!entries.length) {
      node.innerHTML = "<p class=\\"muted\\">No quiz attempts recorded yet for this module.</p>";
      return;
    }
    const correct = entries.reduce((sum, entry) => sum + entry.correct, 0);
    const total = entries.reduce((sum, entry) => sum + entry.total, 0);
    node.innerHTML = `<p><strong>Quiz progress:</strong> ${correct}/${total} correct across ${entries.length} quiz page(s).</p>`;
  });
}

function renderResultsPage() {
  const target = document.querySelector("[data-results-root]");
  if (!target) return;
  const scores = loadScores();
  const entries = Object.entries(scores);
  if (!entries.length) {
    target.innerHTML = "<p class=\\"muted\\">No quiz scores stored yet. Complete a quiz page to populate this summary.</p>";
    return;
  }
  const rows = entries.map(([quizId, entry]) => `
    <tr>
      <td>${quizId}</td>
      <td>${entry.moduleId}</td>
      <td>${entry.correct}/${entry.total}</td>
    </tr>
  `).join("");
  target.innerHTML = `
    <table>
      <thead>
        <tr>
          <th>Quiz</th>
          <th>Module</th>
          <th>Score</th>
        </tr>
      </thead>
      <tbody>${rows}</tbody>
    </table>
  `;
}

function enableLockedNextButton(form) {
  const nextButton = document.querySelector(".next-button[data-requires-quiz]");
  if (!nextButton) return;
  nextButton.classList.remove("is-disabled");
  nextButton.removeAttribute("aria-disabled");
}

function setupQuizzes() {
  document.querySelectorAll(".quiz-form").forEach((form) => {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const questions = Array.from(form.querySelectorAll(".quiz-question"));
      let correct = 0;
      questions.forEach((question) => {
        question.classList.remove("is-correct", "is-incorrect");
        const selected = question.querySelector("input[type=radio]:checked");
        const feedbackNode = question.querySelector(".quiz-feedback");
        if (!selected) {
          feedbackNode.hidden = false;
          feedbackNode.textContent = "Select an answer to see feedback.";
          question.classList.add("is-incorrect");
          return;
        }
        const isCorrect = selected.dataset.correct === "true";
        if (isCorrect) correct += 1;
        question.classList.add(isCorrect ? "is-correct" : "is-incorrect");
        feedbackNode.hidden = false;
        feedbackNode.innerHTML = `${isCorrect ? "<strong>Correct.</strong> " : "<strong>Not quite.</strong> "}${selected.dataset.feedback || ""}`;
      });

      const total = questions.length;
      const scoreNode = form.querySelector(".quiz-score");
      if (scoreNode) {
        scoreNode.textContent = `Score: ${correct}/${total}`;
      }

      const scores = loadScores();
      scores[form.dataset.quizId] = {
        moduleId: form.dataset.moduleId,
        correct,
        total,
      };
      saveScores(scores);
      enableLockedNextButton(form);
      renderModuleSummaries();
      renderResultsPage();
    });
  });
}

function setupDashboard() {
  document.querySelectorAll(".dash-week-cell").forEach((cell) => {
    const header = cell.querySelector(".dash-week-header");
    const detail = cell.querySelector(".dash-week-detail");
    if (!header || !detail) return;
    header.addEventListener("click", () => {
      const isOpen = !detail.hidden;
      detail.hidden = isOpen;
      header.setAttribute("aria-expanded", String(!isOpen));
      cell.classList.toggle("is-active", !isOpen);
    });
  });
}

function getAssetBaseUrl() {
  const appScript = document.querySelector('script[src$="app.js"]');
  if (!appScript) return new URL("./", window.location.href);
  return new URL("./", appScript.src);
}

function getPageContext() {
  const node = document.getElementById("bobpe-page-context");
  if (!node) return null;
  try {
    return JSON.parse(node.textContent || "{}");
  } catch (_error) {
    return null;
  }
}

async function loadConceptQuizPreviews() {
  if (conceptQuizPreviewCache) return conceptQuizPreviewCache;
  const response = await fetch(new URL("concept_quizzes_preview.json", getAssetBaseUrl()));
  if (!response.ok) {
    throw new Error(`Failed to load concept quiz previews: ${response.status}`);
  }
  conceptQuizPreviewCache = await response.json();
  return conceptQuizPreviewCache;
}

function createQuestionCard(question, index) {
  const item = document.createElement("li");
  item.className = "concept-preview-item";

  const header = document.createElement("div");
  header.className = "concept-preview-item-header";

  const number = document.createElement("span");
  number.className = "concept-preview-number";
  number.textContent = `Q${index + 1}`;

  const badge = document.createElement("span");
  badge.className = "concept-preview-badge";
  badge.textContent = question.type === "multiple_choice" ? "Multiple Choice" : "Open Response";

  header.append(number, badge);

  const prompt = document.createElement("p");
  prompt.className = "concept-preview-prompt";
  prompt.textContent = question.prompt;

  item.append(header, prompt);

  if (question.options?.length) {
    const options = document.createElement("ol");
    options.className = "concept-preview-options";
    options.type = "A";
    question.options.forEach((optionText) => {
      const option = document.createElement("li");
      option.textContent = optionText;
      options.appendChild(option);
    });
    item.appendChild(options);
  }

  return item;
}

function renderConceptQuizPreview(preview) {
  const pageShell = document.querySelector(".page-shell");
  const moduleGrid = document.querySelector(".module-overview-grid");
  const sequenceCard = document.querySelector(".module-page-list")?.closest(".content-card");
  if (!pageShell || !moduleGrid || !sequenceCard) return;

  const existing = document.querySelector("[data-concept-preview]");
  if (existing) existing.remove();

  const section = document.createElement("section");
  section.className = "content-card concept-preview-card";
  section.dataset.conceptPreview = "true";

  const title = document.createElement("h2");
  title.textContent = "Questions to Think Through Before Class";

  const intro = document.createElement("p");
  intro.className = "concept-preview-intro";
  intro.textContent = "These are possible in-class concept questions for this week. They are here to help you think ahead; answers are intentionally hidden.";

  const focus = document.createElement("p");
  focus.className = "concept-preview-focus";
  focus.innerHTML = `<strong>${preview.week_label} focus:</strong> ${preview.week_focus}`;

  const list = document.createElement("ol");
  list.className = "concept-preview-list";
  preview.questions.forEach((question, index) => {
    list.appendChild(createQuestionCard(question, index));
  });

  section.append(title, intro, focus, list);
  pageShell.insertBefore(section, sequenceCard);

  const metaList = document.querySelector(".meta-list");
  if (metaList && !metaList.querySelector("[data-concept-count]")) {
    const row = document.createElement("div");
    row.dataset.conceptCount = "true";
    row.innerHTML = `<dt>Concept questions</dt><dd>${preview.questions.length}</dd>`;
    metaList.appendChild(row);
  }
}

async function setupConceptQuizPreviews() {
  const context = getPageContext();
  if (!context || context.source_type !== "module_index" || !context.module_id) return;
  try {
    const previews = await loadConceptQuizPreviews();
    const preview = previews[context.module_id];
    if (!preview) return;
    renderConceptQuizPreview(preview);
  } catch (error) {
    console.error(error);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  setupQuizzes();
  renderModuleSummaries();
  renderResultsPage();
  setupDashboard();
  setupConceptQuizPreviews();
});
"""


def write_labs_assignment_page(
    input_dir: Path,
    output_dir: Path,
    assignment: dict,
    course_id: str,
    page_contexts: list[dict],
    config: dict,
) -> None:
    """Render a single assignment markdown file as a labs/assignments/<key>/index.html page."""
    source_path = input_dir / assignment["source"]
    if not source_path.exists():
        return
    text = clean_text(read_text(source_path))
    key = assignment["key"]
    page_dir = output_dir / "labs" / "assignments" / key
    page_dir.mkdir(parents=True, exist_ok=True)
    page_path = page_dir / "index.html"
    render_ctx = MarkdownRenderContext(
        input_dir=input_dir,
        output_dir=output_dir,
        page_path=page_path,
        source_path=source_path.resolve(),
    )
    content_html = markdown_to_html(text, render_ctx)

    # Optionally append a FAQ file if specified in the config
    faq_html = ""
    faq_source_rel = assignment.get("faq_source")
    if faq_source_rel:
        faq_path = input_dir / faq_source_rel
        if faq_path.exists():
            faq_text = clean_text(read_text(faq_path))
            faq_render_ctx = MarkdownRenderContext(
                input_dir=input_dir,
                output_dir=output_dir,
                page_path=page_path,
                source_path=faq_path.resolve(),
            )
            faq_html = f"""
      <section class="content-card markdown-body" style="padding:1.5rem; margin-top:1.5rem">
        <hr style="margin-bottom:1.5rem">
        {markdown_to_html(faq_text, faq_render_ctx)}
      </section>"""
        else:
            print(f"  [warn] faq_source not found: {faq_path}")

    title = assignment["title"]
    brand = config.get("course_title", "Course")
    body = f"""
    {render_site_header('../../', 'labs', config=config)}
    <main class="page-shell">
      <nav class="breadcrumbs">
        <a href="../../index.html">Home</a>
        <a href="../../labs.html">Labs</a>
        <span>{html.escape(title)}</span>
      </nav>
      <section class="hero compact">
        <p class="eyebrow">{html.escape(assignment.get('eyebrow', brand))}</p>
        <h1>{html.escape(title)}</h1>
        <p class="lead">{html.escape(assignment.get('description', ''))}</p>
      </section>
      <section class="content-card markdown-body" style="padding:1.5rem">
        {content_html}
      </section>{faq_html}
    </main>
    {render_site_footer()}
    """
    page_ctx = make_page_context(
        course_id=course_id,
        page_id=f"labs-assignment-{key}",
        title=title,
        url=f"labs/assignments/{key}/index.html",
        text=text,
        source_type="overview",
    )
    page_contexts.append(page_ctx)
    page_path.write_text(render_page(title, body, "../../", page_context=page_ctx), encoding="utf-8")


def write_labs_experiment_page(
    output_dir: Path,
    experiment: dict,
    tier_key: str,
    course_id: str,
    page_contexts: list[dict],
    config: dict,
    input_dir: Path | None = None,
) -> None:
    """Write a lab experiment page under labs/tier1/ or labs/tier2/.

    If compiled markdown files exist in the bundle at
    assignments/lab_compilations/{tier_key}_lab_{key}/, they are rendered
    into the respective sections. Falls back to placeholder text otherwise.
    """
    key = experiment["key"]
    title = experiment["title"]
    eyebrow = experiment.get("eyebrow", tier_key.upper())
    description = experiment.get("description", "")
    tier_label = "Tier 1" if tier_key == "tier1" else "Tier 2"
    tier_url = f"labs/{tier_key}_candidates.html"

    page_dir = output_dir / "labs" / tier_key / key
    page_dir.mkdir(parents=True, exist_ok=True)
    page_path = page_dir / "index.html"

    render_ctx = MarkdownRenderContext(
        input_dir=input_dir or output_dir,
        output_dir=output_dir,
        page_path=page_path,
        source_path=None,
    )

    # Try to locate compiled markdown for this experiment in the bundle.
    # Convention: assignments/lab_compilations/{tier_key}_lab_{key}/
    compilation_dir: Path | None = None
    if input_dir is not None:
        candidate = input_dir / "assignments" / "lab_compilations" / f"{tier_key}_lab_{key}"
        if candidate.is_dir():
            compilation_dir = candidate

    def read_section(*rel_paths: str) -> str:
        """Read and concatenate one or more markdown files from the compilation dir."""
        if compilation_dir is None:
            return ""
        parts: list[str] = []
        for rel in rel_paths:
            p = compilation_dir / rel
            if p.exists() and p.is_file():
                parts.append(clean_text(read_text(p)))
        return "\n\n".join(parts).strip()

    def render_section(sec_title: str, placeholder: str, *rel_paths: str) -> str:
        """Return a scaffold-section div: rendered markdown if available, else placeholder."""
        content_md = read_section(*rel_paths)
        if content_md:
            rendered = markdown_to_html(content_md, render_ctx)
            return (
                f'<div class="scaffold-section compiled">'
                f'<h3>{html.escape(sec_title)}</h3>'
                f'<div class="compiled-content">{rendered}</div>'
                f'</div>'
            )
        return (
            f'<div class="scaffold-section">'
            f'<h3>{html.escape(sec_title)}</h3>'
            f'<p>{html.escape(placeholder)}</p>'
            f'</div>'
        )

    has_content = compilation_dir is not None

    scaffold_html = "".join([
        render_section(
            "Procedure",
            "How to set up and conduct the experiment. Step-by-step instructions and setup photos will appear here.",
            "procedure/procedure_agent.md",
        ),
        render_section(
            "Model / Derivation",
            "Governing equations, derivation, assumptions, and known model limitations will appear here.",
            "model/derivation_agent.md",
            "model/model_equations_agent.md",
        ),
        render_section(
            "Instrumentation",
            "Sensor specifications, DAQ configuration, sampling rates, and datasheets will appear here.",
            "instrumentation/sensor_specs_summary_agent.md",
        ),
        render_section(
            "Sample Data",
            "A complete sample dataset with collection conditions and a MATLAB analysis template will appear here.",
            "data/data_notes_agent.md",
        ),
        render_section(
            "Notes",
            "Additional instructor notes and known issues from prior runs will appear here.",
            "notes/additional_notes_agent.md",
        ),
    ])

    status_note = (
        '<p class="muted" style="margin-bottom:1rem">Lab content compiled from source materials. '
        'Sections marked as incomplete will be updated as additional source files become available.</p>'
        if has_content else
        '<p class="muted" style="margin-bottom:1rem">Content is being compiled by the lab development team. '
        'Each section below will be populated with verified, student-ready materials.</p>'
    )

    body = f"""
    {render_site_header('../../', 'labs', config=config)}
    <main class="page-shell">
      <nav class="breadcrumbs">
        <a href="../../index.html">Home</a>
        <a href="../../labs.html">Labs</a>
        <a href="../../{html.escape(tier_url)}">{html.escape(tier_label)} Candidates</a>
        <span>{html.escape(title)}</span>
      </nav>
      <section class="hero compact">
        <p class="eyebrow">{html.escape(eyebrow)}</p>
        <h1>{html.escape(title)}</h1>
        <p class="lead">{html.escape(description)}</p>
      </section>
      <section class="experiment-scaffold">
        <h2>Lab Content</h2>
        {status_note}
        {scaffold_html}
      </section>
    </main>
    {render_site_footer()}
    """
    page_ctx = make_page_context(
        course_id=course_id,
        page_id=f"labs-{tier_key}-{key}",
        title=title,
        url=f"labs/{tier_key}/{key}/index.html",
        text=f"{title} {description}",
        source_type="overview",
    )
    page_contexts.append(page_ctx)
    page_path.write_text(render_page(title, body, "../../", page_context=page_ctx), encoding="utf-8")


def write_labs_tier_page(
    input_dir: Path,
    output_dir: Path,
    tier_cfg: dict,
    tier_key: str,
    course_id: str,
    page_contexts: list[dict],
    config: dict,
) -> None:
    """Write the tier candidate landing page (labs/tier1_candidates.html or tier2_candidates.html)."""
    title = tier_cfg["title"]
    description = tier_cfg.get("description", "")
    experiments = tier_cfg.get("experiments", [])
    checklist_path = tier_cfg.get("instructor_checklist", "")
    checklist_url = f"instructor/checklist.html"  # relative to labs/ output directory

    # Build experiment cards
    experiment_cards = []
    for exp in experiments:
        exp_url = f"{tier_key}/{exp['key']}/index.html"
        experiment_cards.append(f"""
        <article class="labs-card">
          <p class="eyebrow">{html.escape(exp.get('eyebrow', tier_key.upper()))}</p>
          <h2>{html.escape(exp['title'])}</h2>
          <p>{html.escape(exp.get('description', ''))}</p>
          <div class="labs-card-footer">
            <a class="secondary-button" href="{html.escape(exp_url)}">View Lab →</a>
          </div>
        </article>
        """)

    # Instructor resource bar
    instructor_bar = f"""
    <div class="instructor-resource-bar">
      <span>Instructor resource: lab content compilation checklist for the lab development team.</span>
      <a class="secondary-button" href="{html.escape(checklist_url)}">Content Compile Checklist →</a>
    </div>
    """ if checklist_path else ""

    body = f"""
    {render_site_header('../', 'labs', config=config)}
    <main class="page-shell">
      <nav class="breadcrumbs">
        <a href="../index.html">Home</a>
        <a href="../labs.html">Labs</a>
        <span>{html.escape(title)}</span>
      </nav>
      <section class="hero compact">
        <p class="eyebrow">{"Tier 1" if tier_key == "tier1" else "Tier 2"} — Lab Candidates</p>
        <h1>{html.escape(title)}</h1>
        <p class="lead">{html.escape(description)}</p>
      </section>
      <section class="labs-card-grid">
        {''.join(experiment_cards)}
      </section>
      {instructor_bar}
    </main>
    {render_site_footer()}
    """
    out_name = f"labs/{tier_key}_candidates.html"
    page_path = output_dir / out_name
    page_path.parent.mkdir(parents=True, exist_ok=True)
    page_ctx = make_page_context(
        course_id=course_id,
        page_id=f"labs-{tier_key}-candidates",
        title=title,
        url=out_name,
        text=f"{title} {description} " + " ".join(e["title"] for e in experiments),
        source_type="overview",
    )
    page_contexts.append(page_ctx)
    page_path.write_text(render_page(title, body, "../", page_context=page_ctx), encoding="utf-8")


def write_labs_instructor_page(
    input_dir: Path,
    output_dir: Path,
    checklist_source: str,
    course_id: str,
    page_contexts: list[dict],
    config: dict,
) -> None:
    """Render the instructor lab content compilation checklist as labs/instructor/checklist.html."""
    source_path = input_dir / checklist_source
    if not source_path.exists():
        return
    text = clean_text(read_text(source_path))
    page_dir = output_dir / "labs" / "instructor"
    page_dir.mkdir(parents=True, exist_ok=True)
    page_path = page_dir / "checklist.html"
    render_ctx = MarkdownRenderContext(
        input_dir=input_dir,
        output_dir=output_dir,
        page_path=page_path,
        source_path=source_path.resolve(),
    )
    content_html = markdown_to_html(text, render_ctx)
    title = "Lab Content Compilation Checklist"
    body = f"""
    {render_site_header('../../', 'labs', config=config)}
    <main class="page-shell">
      <nav class="breadcrumbs">
        <a href="../../index.html">Home</a>
        <a href="../../labs.html">Labs</a>
        <span>{html.escape(title)}</span>
      </nav>
      <section class="hero compact">
        <p class="eyebrow">Instructor Resource</p>
        <h1>{html.escape(title)}</h1>
        <p class="lead">Step-by-step checklist for test engineers compiling Tier 1 lab content from the lab catalog.</p>
      </section>
      <section class="content-card markdown-body" style="padding:1.5rem">
        {content_html}
      </section>
    </main>
    {render_site_footer()}
    """
    page_ctx = make_page_context(
        course_id=course_id,
        page_id="labs-instructor-checklist",
        title=title,
        url="labs/instructor/checklist.html",
        text=text,
        source_type="overview",
    )
    page_contexts.append(page_ctx)
    page_path.write_text(render_page(title, body, "../../", page_context=page_ctx), encoding="utf-8")


def write_labs_page(
    input_dir: Path,
    output_dir: Path,
    labs_cfg: dict,
    course_id: str,
    page_contexts: list[dict],
    config: dict,
) -> None:
    """Write labs.html and all labs/* sub-pages from the config labs block."""
    brand = config.get("course_title", "Course")
    assignments = labs_cfg.get("assignments", [])
    tier1_cfg = labs_cfg.get("tier1", {})
    tier2_cfg = labs_cfg.get("tier2", {})

    # --- Write each assignment page ---
    for assignment in assignments:
        write_labs_assignment_page(input_dir, output_dir, assignment, course_id, page_contexts, config)

    # --- Write experiment scaffold pages ---
    for exp in tier1_cfg.get("experiments", []):
        write_labs_experiment_page(output_dir, exp, "tier1", course_id, page_contexts, config, input_dir=input_dir)
    for exp in tier2_cfg.get("experiments", []):
        write_labs_experiment_page(output_dir, exp, "tier2", course_id, page_contexts, config, input_dir=input_dir)

    # --- Write tier candidate landing pages ---
    if tier1_cfg:
        write_labs_tier_page(input_dir, output_dir, tier1_cfg, "tier1", course_id, page_contexts, config)
    if tier2_cfg:
        write_labs_tier_page(input_dir, output_dir, tier2_cfg, "tier2", course_id, page_contexts, config)

    # --- Write instructor checklist page ---
    checklist_source = tier1_cfg.get("instructor_checklist", "")
    if checklist_source:
        write_labs_instructor_page(input_dir, output_dir, checklist_source, course_id, page_contexts, config)

    # --- Build assignment cards for labs.html ---
    assignment_cards = []
    for assignment in assignments:
        assignment_url = f"labs/assignments/{assignment['key']}/index.html"
        assignment_cards.append(f"""
        <article class="labs-card">
          <p class="eyebrow">{html.escape(assignment.get('eyebrow', brand))}</p>
          <h2>{html.escape(assignment['title'])}</h2>
          <p>{html.escape(assignment.get('description', ''))}</p>
          <div class="labs-card-footer">
            <a class="secondary-button" href="{html.escape(assignment_url)}">View Assignment →</a>
          </div>
        </article>
        """)

    # --- Build tier buttons ---
    tier_buttons = ""
    if tier1_cfg:
        tier_buttons += f'<a class="secondary-button" href="labs/tier1_candidates.html">Tier 1 Candidates →</a>'
    if tier2_cfg:
        tier_buttons += f'<a class="secondary-button" href="labs/tier2_candidates.html">Tier 2 Candidates →</a>'

    # --- Write labs.html ---
    title = "Labs"
    body = f"""
    {render_site_header('./', 'labs', config=config)}
    <main class="page-shell">
      <section class="hero">
        <p class="eyebrow">{html.escape(brand)}</p>
        <h1>Labs</h1>
        <p class="lead">Lab assignments and experiment resources for ASEN 3501. Tier 1 experiments are used in E1; Tier 2 experiments are used in E2.</p>
        <div class="labs-hero-actions">
          {tier_buttons}
        </div>
      </section>
      <section class="labs-card-grid">
        {''.join(assignment_cards)}
      </section>
    </main>
    {render_site_footer()}
    """
    page_path = output_dir / "labs.html"
    page_ctx = make_page_context(
        course_id=course_id,
        page_id="labs",
        title=title,
        url="labs.html",
        text="Labs assignments and experiment resources for ASEN 3501. Tier 1 and Tier 2 canned experiments.",
        source_type="overview",
    )
    page_contexts.append(page_ctx)
    page_path.write_text(render_page(title, body, "./", page_context=page_ctx), encoding="utf-8")


def write_site(
    input_dir: Path, output_dir: Path, courses: dict[str, CourseInfo], course_id: str, config: dict | None = None
) -> None:
    from Forward.chat.indexer import build_course_index

    page_contexts: list[dict[str, Any]] = []
    chatbot_cfg = config.get("chatbot") if config else None
    concept_quiz_previews = build_concept_quiz_previews(input_dir, config)
    if chatbot_cfg and not chatbot_cfg.get("enabled", True):
        chatbot_cfg = None  # Disabled — don't inject gate
    write_assets(output_dir, chatbot_config=chatbot_cfg)
    write_concept_quiz_previews(output_dir, concept_quiz_previews)
    write_manifest(output_dir, courses, course_id)
    write_root_pages(input_dir, output_dir, courses, course_id, page_contexts, config=config)
    if config is not None:
        write_admin_pages(input_dir, output_dir, config, course_id, page_contexts)
    labs_cfg = config.get("labs") if config else None
    if labs_cfg is not None:
        write_labs_page(input_dir, output_dir, labs_cfg, course_id, page_contexts, config)
    write_module_pages(input_dir, output_dir, courses, course_id, page_contexts, config=config)
    build_course_index(course_id, page_contexts, output_dir / "course_index.json")


def main() -> None:
    global _INCLUDE_CHATBOT
    args = parse_args()
    _INCLUDE_CHATBOT = args.chatbot
    input_dir = Path(args.input).resolve()
    output_dir = Path(args.output).resolve()

    config = load_config(input_dir)
    prepare_output_dir(output_dir)

    if config is not None:
        course_id = config.get("course_id") or course_id_from_input_dir(input_dir)
        courses = build_courses_from_config(input_dir, config)
        normalize_courses(input_dir, output_dir, courses, config=config)
    else:
        course_id = course_id_from_input_dir(input_dir)
        courses = build_courses(input_dir)
        normalize_courses(input_dir, output_dir, courses, config=None)

    write_site(input_dir, output_dir, courses, course_id, config=config)


if __name__ == "__main__":
    main()
