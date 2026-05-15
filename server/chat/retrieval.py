from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any


TOKEN_RE = re.compile(r"[a-z0-9_]+")


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall((text or "").lower())


def snippet_for(text: str, limit: int = 280) -> str:
    compact = re.sub(r"\s+", " ", text or "").strip()
    if len(compact) <= limit:
        return compact
    return compact[: limit - 3].rstrip() + "..."


class SimpleRetriever:
    def __init__(self, index_path: Path):
        payload = json.loads(index_path.read_text(encoding="utf-8"))
        self.course_id = payload.get("course_id") or ""
        self.chunks: list[dict[str, Any]] = []
        self.doc_term_counts: list[Counter[str]] = []
        self.doc_freq: Counter[str] = Counter()

        for page in payload.get("pages", []):
            page_tokens = tokenize(page.get("title", "")) + tokenize(page.get("module_id", ""))
            for chunk in page.get("chunks", []):
                tokens = tokenize(chunk.get("text", "")) + page_tokens
                record = {
                    "page_id": page.get("page_id"),
                    "title": page.get("title"),
                    "url": page.get("url"),
                    "module_id": page.get("module_id"),
                    "chunk_id": chunk.get("chunk_id"),
                    "text": chunk.get("text", ""),
                    "tokens": tokens,
                }
                counts: Counter[str] = Counter(tokens)
                self.chunks.append(record)
                self.doc_term_counts.append(counts)
                for token in counts:
                    self.doc_freq[token] += 1

        self.num_docs = max(len(self.chunks), 1)

    def score(self, query: str, doc_counts: Counter[str]) -> float:
        query_tokens = tokenize(query)
        if not query_tokens:
            return 0.0

        query_counts = Counter(query_tokens)
        score = 0.0
        for token, q_count in query_counts.items():
            tf = doc_counts.get(token, 0)
            if tf <= 0:
                continue
            df = self.doc_freq.get(token, 0)
            idf = math.log((self.num_docs + 1) / (df + 1)) + 1.0
            score += (1.0 + math.log(tf)) * idf * q_count
        return score

    def search(self, query: str, top_k: int = 5) -> list[dict[str, Any]]:
        scored: list[tuple[float, dict[str, Any]]] = []
        for chunk, counts in zip(self.chunks, self.doc_term_counts):
            score = self.score(query, counts)
            if score > 0:
                scored.append((score, chunk))

        scored.sort(key=lambda item: item[0], reverse=True)
        results: list[dict[str, Any]] = []
        seen_pages: set[tuple[str | None, str | None]] = set()
        for score, chunk in scored:
            page_key = (chunk.get("page_id"), chunk.get("chunk_id"))
            if page_key in seen_pages:
                continue
            seen_pages.add(page_key)
            results.append(
                {
                    "title": chunk.get("title") or "Untitled",
                    "url": chunk.get("url") or "",
                    "page_id": chunk.get("page_id"),
                    "chunk_id": chunk.get("chunk_id"),
                    "snippet": snippet_for(chunk.get("text", "")),
                    "text": chunk.get("text", ""),
                    "score": round(score, 4),
                }
            )
            if len(results) >= top_k:
                break
        return results
