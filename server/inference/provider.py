"""Provider-specific inference calls for the shared model router."""

from __future__ import annotations

import json
from urllib import error, request

import httpx

from .config import (
    DEEPSEEK_API_KEY,
    GEMINI_API_KEY,
    KIMI_API_KEY,
    OLLAMA_HOST,
    OPENAI_API_KEY,
)


def _post_json(url: str, payload: dict, headers: dict | None = None) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req_headers = {"Content-Type": "application/json"}
    if headers:
        req_headers.update(headers)

    req = request.Request(url=url, data=data, headers=req_headers, method="POST")
    try:
        with request.urlopen(req, timeout=120) as response:
            return json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"Provider HTTP error ({exc.code}): {body}") from exc
    except error.URLError as exc:
        raise RuntimeError(f"Provider request failed: {exc}") from exc


def _extract_openai_like_text(response_json: dict) -> str:
    choices = response_json.get("choices") or []
    if not choices:
        return ""
    message = choices[0].get("message") or {}
    content = message.get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = [part.get("text", "") for part in content if isinstance(part, dict)]
        return "".join(parts).strip()
    return ""


def _extract_chat_completion_text(response: object) -> str:
    choices = getattr(response, "choices", None) or []
    if not choices:
        return ""
    message = getattr(choices[0], "message", None)
    if message is None and isinstance(choices[0], dict):
        message = choices[0].get("message")
    content = getattr(message, "content", None)
    if content is None and isinstance(message, dict):
        content = message.get("content")
    return str(content or "").strip()


def _openai_http_client() -> httpx.Client:
    """Build a compatible HTTP client for the installed OpenAI SDK/httpx pair."""
    return httpx.Client(timeout=120.0, follow_redirects=True)


def call_openai(prompt: str, model: str) -> str:
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is not set.")

    from openai import OpenAI

    # `openai==1.55.x` can fail against `httpx==0.28.x` when it tries to build
    # its own default client with the removed `proxies` argument. Supplying an
    # explicit client keeps the shared inference path compatible with the
    # currently installed SDK/runtime combination.
    with _openai_http_client() as http_client:
        client = OpenAI(api_key=OPENAI_API_KEY, http_client=http_client)
        if hasattr(client, "responses"):
            response = client.responses.create(model=model, input=prompt)

            output_text = getattr(response, "output_text", None)
            if output_text:
                return output_text.strip()

            # Fallback for SDK shape changes.
            response_dict = response.model_dump() if hasattr(response, "model_dump") else dict(response)
            return str(response_dict.get("output_text") or "").strip()

        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        text = _extract_chat_completion_text(response)
        if text:
            return text

        response_dict = response.model_dump() if hasattr(response, "model_dump") else dict(response)
        return _extract_openai_like_text(response_dict)


def call_gemini(prompt: str, model: str) -> str:
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not set.")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_API_KEY}"
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    response_json = _post_json(url, payload)

    candidates = response_json.get("candidates") or []
    if not candidates:
        return ""
    parts = (((candidates[0] or {}).get("content") or {}).get("parts")) or []
    return "".join(part.get("text", "") for part in parts if isinstance(part, dict)).strip()


def call_deepseek(prompt: str, model: str) -> str:
    if not DEEPSEEK_API_KEY:
        raise RuntimeError("DEEPSEEK_API_KEY is not set.")

    url = "https://api.deepseek.com/chat/completions"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
    }
    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    response_json = _post_json(url, payload, headers=headers)
    return _extract_openai_like_text(response_json)


def call_kimi(prompt: str, model: str) -> str:
    if not KIMI_API_KEY:
        raise RuntimeError("KIMI_API_KEY is not set.")

    url = "https://api.moonshot.cn/v1/chat/completions"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
    }
    headers = {"Authorization": f"Bearer {KIMI_API_KEY}"}
    response_json = _post_json(url, payload, headers=headers)
    return _extract_openai_like_text(response_json)


def call_ollama(prompt: str, model: str) -> str:
    host = OLLAMA_HOST.rstrip("/")
    url = f"{host}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }
    response_json = _post_json(url, payload)
    return (response_json.get("response") or "").strip()
