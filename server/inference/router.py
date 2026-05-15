"""Unified model router for shared inference."""

from __future__ import annotations

from .provider import (
    call_deepseek,
    call_gemini,
    call_kimi,
    call_ollama,
    call_openai,
)


def parse_model_identifier(model: str) -> tuple[str, str]:
    """Parse `provider:model_name` and return normalized provider/model parts."""
    if ":" not in model:
        raise ValueError("model must be formatted as 'provider:model_name'")

    provider, model_name = model.split(":", 1)
    provider = provider.strip().lower()
    model_name = model_name.strip()

    if not model_name:
        raise ValueError("model_name must be non-empty")

    return provider, model_name


def generate(prompt: str, model: str) -> str:
    """Generate text from `provider:model_name` using the matching backend."""
    if not prompt or not prompt.strip():
        raise ValueError("prompt must be a non-empty string")

    provider, model_name = parse_model_identifier(model)

    if provider == "openai":
        return call_openai(prompt, model_name)
    if provider == "gemini":
        return call_gemini(prompt, model_name)
    if provider == "deepseek":
        return call_deepseek(prompt, model_name)
    if provider == "kimi":
        return call_kimi(prompt, model_name)
    if provider == "ollama":
        return call_ollama(prompt, model_name)

    raise ValueError(f"Unsupported provider: {provider}")


def call_model(prompt: str, model: str) -> str:
    """Backward-compatible alias for the shared inference entrypoint."""
    return generate(prompt, model)
