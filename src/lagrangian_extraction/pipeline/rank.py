"""Rank paper candidates for Lagrangian extraction."""

from __future__ import annotations

import math
from datetime import date
from typing import Literal

from lagrangian_extraction.config import RankConfig
from lagrangian_extraction.models import PaperRecord
from lagrangian_extraction.pipeline.semantic import (
    combine_semantic_scores,
    paper_text,
    semantic_similarity,
    semantic_similarity_abstract,
)

# Terms suggesting an explicit model / Lagrangian definition.
_LAGRANGIAN_POSITIVE = (
    "lagrangian",
    "interaction",
    "coupling",
    "yukawa",
    "superpotential",
    "field content",
    "feynrules",
    "ufo",
    "model",
    "potential",
)

# Broad reviews / searches unlikely to contain a single extractable Lagrangian.
_LAGRANGIAN_NEGATIVE = (
    "review",
    "lecture",
    "tasi",
    "overview",
    "global fit",
    "search for",
    "future search",
    "constraints",
    "prospect",
    "dark matter candidates",
    "global fits",
)


def _lagrangian_signal(text: str) -> float:
    """Score how likely a paper contains an explicit Lagrangian (0–1)."""
    lowered = text.lower()
    positive = sum(1 for term in _LAGRANGIAN_POSITIVE if term in lowered)
    negative = sum(1 for term in _LAGRANGIAN_NEGATIVE if term in lowered)
    raw = 0.35 + 0.12 * positive - 0.15 * negative
    return max(0.0, min(1.0, raw))


def compute_score(
    paper: PaperRecord,
    *,
    now: date,
    config: RankConfig,
    max_cites_seen: int | None = None,
) -> tuple[float, dict[str, float]]:
    """Return combined citation + recency score and breakdown dict."""
    cite_ceiling = max_cites_seen or config.max_cites_seen
    cite_ceiling = max(cite_ceiling, paper.citation_count, 1)

    cite_norm = math.log1p(paper.citation_count) / math.log1p(cite_ceiling)

    published = paper.published or now
    age_years = max((now - published).days / 365.25, 0.0)
    recency = math.exp(-age_years / config.recency_half_life_years)

    score = config.weight_citation * cite_norm + config.weight_recency * recency
    breakdown = {
        "citation_norm": round(cite_norm, 6),
        "recency": round(recency, 6),
        "weight_citation": config.weight_citation,
        "weight_recency": config.weight_recency,
    }
    return score, breakdown


def compute_extraction_score(
    paper: PaperRecord,
    *,
    query_text: str,
    now: date,
    config: RankConfig,
    max_cites_seen: int | None = None,
    semantic_scope: Literal["full", "abstract", "combined"] = "combined",
) -> tuple[float, dict[str, float]]:
    """Score a paper for single-paper Lagrangian extraction selection."""
    cite_ceiling = max_cites_seen or config.max_cites_seen
    cite_ceiling = max(cite_ceiling, paper.citation_count, 1)
    cite_norm = math.log1p(paper.citation_count) / math.log1p(cite_ceiling)

    published = paper.published or now
    age_years = max((now - published).days / 365.25, 0.0)
    recency = math.exp(-age_years / config.recency_half_life_years)

    text = paper_text(paper)
    semantic_full = semantic_similarity(query_text, text)
    semantic_abstract = semantic_similarity_abstract(query_text, paper)
    semantic = combine_semantic_scores(
        semantic_full,
        semantic_abstract,
        semantic_scope,
        weight_full=config.weight_semantic_full,
        weight_abstract=config.weight_semantic_abstract,
    )
    lagrangian = _lagrangian_signal(text)
    extractable = 1.0 if paper.arxiv_id else 0.0

    cite_weight = 1.0 - config.weight_semantic - config.weight_lagrangian - 0.1
    cite_weight = max(cite_weight, 0.05)
    recency_weight = 0.1

    score = (
        config.weight_semantic * semantic
        + config.weight_lagrangian * lagrangian
        + cite_weight * cite_norm
        + recency_weight * recency
        + 0.05 * extractable
    )
    breakdown = {
        "semantic": round(semantic, 6),
        "semantic_full": round(semantic_full, 6),
        "semantic_abstract": round(semantic_abstract, 6),
        "lagrangian_signal": round(lagrangian, 6),
        "citation_norm": round(cite_norm, 6),
        "recency": round(recency, 6),
        "extractable": extractable,
    }
    return score, breakdown


def rank_candidates(
    papers: list[PaperRecord],
    *,
    config: RankConfig | None = None,
    now: date | None = None,
    top_k: int | None = None,
) -> list[PaperRecord]:
    """Score and sort papers by citation + recency, returning top_k if specified."""
    cfg = config or RankConfig()
    reference_date = now or date.today()
    max_cites = max((p.citation_count for p in papers), default=0)

    scored: list[PaperRecord] = []
    for paper in papers:
        score, breakdown = compute_score(
            paper, now=reference_date, config=cfg, max_cites_seen=max_cites
        )
        scored.append(
            paper.model_copy(update={"score": round(score, 6), "score_breakdown": breakdown})
        )

    scored.sort(key=lambda p: p.score, reverse=True)
    if top_k is not None:
        return scored[:top_k]
    return scored


def rank_for_extraction(
    papers: list[PaperRecord],
    *,
    query_text: str,
    config: RankConfig | None = None,
    now: date | None = None,
    top_k: int | None = None,
    semantic_scope: Literal["full", "abstract", "combined"] = "combined",
) -> list[PaperRecord]:
    """Rank papers for selecting one source to extract a Lagrangian from."""
    cfg = config or RankConfig()
    reference_date = now or date.today()
    max_cites = max((p.citation_count for p in papers), default=0)

    scored: list[PaperRecord] = []
    for paper in papers:
        score, breakdown = compute_extraction_score(
            paper,
            query_text=query_text,
            now=reference_date,
            config=cfg,
            max_cites_seen=max_cites,
            semantic_scope=semantic_scope,
        )
        scored.append(
            paper.model_copy(update={"score": round(score, 6), "score_breakdown": breakdown})
        )

    scored.sort(key=lambda p: p.score, reverse=True)
    if top_k is not None:
        return scored[:top_k]
    return scored
