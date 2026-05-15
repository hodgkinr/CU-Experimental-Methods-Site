"""Central environment configuration for shared inference."""

from __future__ import annotations

import os
from dotenv import load_dotenv

# Load local environment variables from .env (if present).
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
KIMI_API_KEY = os.getenv("KIMI_API_KEY")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
