from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def chunk_text(text: str, chunk_size: int = 800, overlap: int = 120) -> list[str]:
    normalized = normalize_text(text)
    if not normalized:
        return []

    chunks: list[str] = []
    start = 0
    while start < len(normalized):
        end = min(len(normalized), start + chunk_size)
        if end < len(normalized):
            boundary = normalized.rfind(" ", start, end)
            if boundary > start + max(80, overlap):
                end = boundary
        chunk = normalized[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(normalized):
            break
        start = max(end - overlap, start + 1)
    return chunks


def build_course_index(course_id: str, pages: list[dict[str, Any]], output_path: Path) -> None:
    indexed_pages: list[dict[str, Any]] = []

    for page in pages:
        text = normalize_text(str(page.get("text") or ""))
        page_id = str(page["page_id"])
        chunks = [
            {
                "chunk_id": f"{page_id}-chunk-{index:03d}",
                "text": chunk,
                "anchor": "",
            }
            for index, chunk in enumerate(chunk_text(text), start=1)
        ]
        indexed_pages.append(
            {
                "page_id": page_id,
                "title": str(page.get("title") or page_id),
                "module_id": page.get("module_id"),
                "url": str(page.get("url") or ""),
                "source_type": str(page.get("source_type") or "page"),
                "text": text,
                "chunks": chunks,
            }
        )

    payload = {
        "course_id": course_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pages": indexed_pages,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
