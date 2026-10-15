"""Lightweight semantic similarity ranking for literature search."""

from __future__ import annotations

import math
import re
from typing import Literal

from lagrangian_extraction.models import PaperRecord

_TOKEN_RE = re.compile(r"[a-z0-9]+")


def _tokenize(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for token in _TOKEN_RE.findall(text.lower()):
        counts[token] = counts.get(token, 0) + 1
    return counts


def paper_text(paper: PaperRecord) -> str:
    author_names = " ".join(author.name for author in paper.authors)
    return " ".join(
        part for part in (paper.title, paper.abstract or "", author_names) if part
    )


def abstract_text(paper: PaperRecord) -> str:
    return paper.abstract or ""


def semantic_similarity(query: str, text: str) -> float:
    """Cosine similarity between query and document token bags."""
    query_tokens = _tokenize(query)
    text_tokens = _tokenize(text)
    if not query_tokens or not text_tokens:
        return 0.0

    shared = set(query_tokens) & set(text_tokens)
    if not shared:
        return 0.0

    dot = sum(query_tokens[token] * text_tokens[token] for token in shared)
    query_norm = math.sqrt(sum(v * v for v in query_tokens.values()))
    text_norm = math.sqrt(sum(v * v for v in text_tokens.values()))
    if query_norm == 0 or text_norm == 0:
        return 0.0
    return dot / (query_norm * text_norm)


def semantic_similarity_abstract(query: str, paper: PaperRecord) -> float:
    """Cosine similarity between query and abstract tokens only."""
    return semantic_similarity(query, abstract_text(paper))


def combine_semantic_scores(
    semantic_full: float,
    semantic_abstract: float,
    scope: Literal["full", "abstract", "combined"],
    *,
    weight_full: float = 0.4,
    weight_abstract: float = 0.6,
) -> float:
    if scope == "full":
        return semantic_full
    if scope == "abstract":
        return semantic_abstract
    return weight_full * semantic_full + weight_abstract * semantic_abstract


def build_semantic_query(model_name: str, keywords: list[str]) -> str:
    parts = [model_name, *keywords]
    return " ".join(part.strip() for part in parts if part.strip())


def rank_by_semantic(
    papers: list[PaperRecord],
    query_text: str,
    *,
    top_k: int | None = None,
    scope: Literal["full", "abstract", "combined"] = "combined",
) -> list[PaperRecord]:
    """Rank papers by semantic similarity to the query text."""
    scored: list[PaperRecord] = []
    for paper in papers:
        full = semantic_similarity(query_text, paper_text(paper))
        abstract = semantic_similarity_abstract(query_text, paper)
        similarity = combine_semantic_scores(full, abstract, scope)
        scored.append(
            paper.model_copy(
                update={
                    "score": round(similarity, 6),
                    "score_breakdown": {
                        "semantic_similarity": round(similarity, 6),
                        "semantic_full": round(full, 6),
                        "semantic_abstract": round(abstract, 6),
                    },
                }
            )
        )

    scored.sort(key=lambda p: p.score, reverse=True)
    if top_k is not None:
        return scored[:top_k]
    return scored
