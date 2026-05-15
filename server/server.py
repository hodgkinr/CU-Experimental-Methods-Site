from __future__ import annotations

import logging
import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from chat.chat_api import router as chat_router


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(title="Forward LMS")
    app.include_router(chat_router)

    env_val = os.environ.get("FORWARD_STATIC_DIR", "")
    if env_val:
        static_dir = Path(env_val).resolve()
    else:
        static_dir = Path(__file__).resolve().parent / "course_content"

    if static_dir.exists():
        logger.info("Serving static files from %s", static_dir)
        app.mount("/", StaticFiles(directory=static_dir, html=True), name="forward-static")
    else:
        logger.warning("Static directory not found: %s", static_dir)
    return app


app = create_app()
