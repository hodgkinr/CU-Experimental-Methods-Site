from __future__ import annotations

import logging
import os

from inference.router import generate


DEFAULT_CHAT_MODEL = os.getenv("FORWARD_CHAT_MODEL", "ollama:llama3.2")
LOGGER = logging.getLogger(__name__)


def messages_to_prompt(messages: list[dict[str, str]]) -> str:
    rendered: list[str] = []
    for message in messages:
        role = message.get("role", "user").upper()
        content = (message.get("content") or "").strip()
        if content:
            rendered.append(f"{role}:\n{content}")
    rendered.append("ASSISTANT:")
    return "\n\n".join(rendered)


def generate_chat_response(messages: list[dict[str, str]], model: str | None = None) -> str:
    prompt = messages_to_prompt(messages)
    try:
        response = generate(prompt=prompt, model=model or DEFAULT_CHAT_MODEL)
    except Exception:
        LOGGER.exception("Forward chat LLM call failed", extra={"model": model or DEFAULT_CHAT_MODEL})
        raise
    return response.strip()
