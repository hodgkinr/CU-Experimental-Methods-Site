from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: str = "user"
    content: str = ""


class PageContext(BaseModel):
    course_id: str = ""
    page_id: str = ""
    title: str = ""
    url: str = ""
    text: str = ""
    module_id: str | None = None
    source_type: str = "page"


class ChatRequest(BaseModel):
    course_id: str = ""
    current_page_url: str = ""
    mode: str = "page"
    message: str = ""
    page_context: PageContext = Field(default_factory=PageContext)
    history: list[ChatMessage] = Field(default_factory=list)


class ChatSource(BaseModel):
    title: str
    url: str
    snippet: str
    page_id: str | None = None
    chunk_id: str | None = None
    score: float | None = None


class ChatResponse(BaseModel):
    answer: str
    mode: Literal["page", "course_rag"]
    sources: list[ChatSource] = Field(default_factory=list)


class IndexedChunk(BaseModel):
    chunk_id: str
    text: str
    anchor: str = ""


class IndexedPage(BaseModel):
    page_id: str
    title: str
    module_id: str | None = None
    url: str
    source_type: str = "page"
    text: str
    chunks: list[IndexedChunk] = Field(default_factory=list)


class CourseIndex(BaseModel):
    course_id: str
    generated_at: str
    pages: list[IndexedPage] = Field(default_factory=list)
