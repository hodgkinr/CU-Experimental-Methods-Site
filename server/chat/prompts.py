from __future__ import annotations

from typing import Any


def _history_messages(history: list[Any]) -> list[dict[str, str]]:
    messages: list[dict[str, str]] = []
    for item in history:
        role = getattr(item, "role", None) or item.get("role")
        content = getattr(item, "content", None) or item.get("content")
        if role in {"user", "assistant"} and content:
            messages.append({"role": role, "content": content.strip()})
    return messages


def build_page_mode_messages(
    student_message: str,
    page_context: dict[str, Any],
    history: list[Any],
) -> list[dict[str, str]]:
    return [
        {
            "role": "system",
            "content": (
                "You are a helpful teacher-style course tutor. "
                "Use only the current page as your source of truth. "
                "Explain clearly, patiently, and in student-friendly language. "
                "Prefer guidance and conceptual explanation over answer dumping. "
                "If the page does not support the answer, say that directly and suggest Course search mode."
            ),
        },
        {
            "role": "system",
            "content": (
                f"Current page title: {page_context.get('title', '')}\n"
                f"Current page URL: {page_context.get('url', '')}\n"
                f"Current page content:\n{page_context.get('text', '')}"
            ),
        },
        *_history_messages(history),
        {"role": "user", "content": student_message.strip()},
    ]


def build_rag_mode_messages(
    student_message: str,
    page_context: dict[str, Any],
    retrieval_results: list[dict[str, Any]],
    history: list[Any],
) -> list[dict[str, str]]:
    retrieval_blob = "\n\n".join(
        f"[Source {index}] {item['title']} ({item['url']})\n{item['text']}"
        for index, item in enumerate(retrieval_results, start=1)
    )
    retrieval_note = retrieval_blob or "No strong course retrieval results were found."
    return [
        {
            "role": "system",
            "content": (
                "You are a helpful teacher-style course tutor. "
                "Use retrieved course materials and the current page context to answer. "
                "Prefer grounded course-specific explanations over general knowledge. "
                "Do not invent pages, quotes, or course facts. "
                "If retrieval is weak, say so."
            ),
        },
        {
            "role": "system",
            "content": (
                f"Current page title: {page_context.get('title', '')}\n"
                f"Current page URL: {page_context.get('url', '')}\n"
                f"Current page content:\n{page_context.get('text', '')}"
            ),
        },
        {"role": "system", "content": f"Retrieved course materials:\n{retrieval_note}"},
        *_history_messages(history),
        {"role": "user", "content": student_message.strip()},
    ]
