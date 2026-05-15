from __future__ import annotations

import logging
import traceback
from pathlib import Path

from fastapi import APIRouter

from chat.llm_service import generate_chat_response
from chat.prompts import build_page_mode_messages, build_rag_mode_messages
from chat.retrieval import SimpleRetriever
from chat.schemas import ChatRequest, ChatResponse, ChatSource


router = APIRouter()
_RETRIEVER_CACHE: dict[str, SimpleRetriever] = {}
OUTPUT_ROOT = Path(__file__).resolve().parents[1] / "course_content"
LOGGER = logging.getLogger(__name__)


def _candidate_index_paths(course_id: str) -> list[Path]:
    return [
        OUTPUT_ROOT / course_id / "course_index.json",
        OUTPUT_ROOT / "course_index.json",
    ]


def get_retriever(course_id: str) -> SimpleRetriever | None:
    if course_id in _RETRIEVER_CACHE:
        return _RETRIEVER_CACHE[course_id]

    for index_path in _candidate_index_paths(course_id):
        if index_path.exists():
            try:
                retriever = SimpleRetriever(index_path)
            except Exception:
                LOGGER.exception("Failed to load course index", extra={"index_path": str(index_path), "course_id": course_id})
                return None
            _RETRIEVER_CACHE[course_id] = retriever
            return retriever
    return None


def _normalize_mode(value: str) -> str:
    return "course_rag" if value == "course_rag" else "page"


def _normalize_page_context(req: ChatRequest) -> dict[str, str | None]:
    page_context = req.page_context.model_dump() if req.page_context else {}
    course_id = (req.course_id or page_context.get("course_id") or "").strip()
    url = (req.current_page_url or page_context.get("url") or "").strip()
    return {
        "course_id": course_id,
        "page_id": str(page_context.get("page_id") or "").strip(),
        "title": str(page_context.get("title") or "").strip() or "Current page",
        "url": url,
        "text": str(page_context.get("text") or "").strip(),
        "module_id": page_context.get("module_id"),
        "source_type": str(page_context.get("source_type") or "page"),
    }


def _normalized_history(req: ChatRequest) -> list[dict[str, str]]:
    history: list[dict[str, str]] = []
    for item in req.history or []:
        payload = item.model_dump() if hasattr(item, "model_dump") else dict(item)
        role = str(payload.get("role") or "").strip()
        content = str(payload.get("content") or "").strip()
        if role in {"user", "assistant"} and content:
            history.append({"role": role, "content": content})
    return history


def _best_index_path(course_id: str) -> Path | None:
    for path in _candidate_index_paths(course_id):
        if path.exists():
            return path
    return None


def _fallback_answer(mode: str, page_context: dict[str, str | None], rag_available: bool) -> str:
    page_text = str(page_context.get("text") or "").strip()
    title = str(page_context.get("title") or "this page").strip()
    if mode == "course_rag" and not rag_available:
        if page_text:
            return (
                "Course search is not available right now, so I used the current page instead. "
                f"From {title}: {page_text[:500].rstrip()}{'...' if len(page_text) > 500 else ''}"
            )
        return "Course search is not available right now, and this page did not include enough text to answer confidently."
    if page_text:
        return (
            "I couldn't reach the model service, so here is a grounded fallback from the current page. "
            f"From {title}: {page_text[:500].rstrip()}{'...' if len(page_text) > 500 else ''}"
        )
    return "I couldn't reach the model service, and the request did not include enough page context to answer safely."


@router.post("/api/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    mode = _normalize_mode(req.mode)
    page_context = _normalize_page_context(req)
    history = _normalized_history(req)
    course_id = str(page_context.get("course_id") or "").strip()
    current_page_url = str(page_context.get("url") or "").strip()
    index_path = _best_index_path(course_id)
    index_exists = index_path is not None
    LOGGER.info(
        "Forward chat request mode=%s course_id=%s current_page_url=%s page_text_exists=%s course_index_exists=%s",
        mode,
        course_id or "<missing>",
        current_page_url or "<missing>",
        bool(page_context.get("text")),
        index_exists,
    )
    try:
        if mode == "page":
            messages = build_page_mode_messages(req.message or "", page_context, history)
            answer = generate_chat_response(messages)
            return ChatResponse(answer=answer, mode="page", sources=[])

        retriever = get_retriever(course_id) if course_id else None
        results = retriever.search(req.message or "", top_k=5) if retriever else []
        if not index_exists:
            return ChatResponse(
                answer=_fallback_answer(mode, page_context, rag_available=False),
                mode="course_rag",
                sources=[],
            )
        messages = build_rag_mode_messages(req.message or "", page_context, results, history)
        answer = generate_chat_response(messages)
        sources = [
            ChatSource(
                title=item["title"],
                url=item["url"],
                snippet=item["snippet"],
                page_id=item.get("page_id"),
                chunk_id=item.get("chunk_id"),
                score=item.get("score"),
            )
            for item in results
        ]
        return ChatResponse(answer=answer, mode="course_rag", sources=sources)
    except Exception:
        LOGGER.error("Forward chat request failed\n%s", traceback.format_exc())
        return ChatResponse(
            answer=_fallback_answer(mode, page_context, rag_available=index_exists),
            mode="course_rag" if mode == "course_rag" else "page",
            sources=[],
        )
