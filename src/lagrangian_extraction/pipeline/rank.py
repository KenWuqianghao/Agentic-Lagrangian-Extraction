"""Rank paper candidates by citation count and recency."""

from __future__ import annotations

import math
from datetime import date

from lagrangian_extraction.config import RankConfig
from lagrangian_extraction.models import PaperRecord


def compute_score(
    paper: PaperRecord,
    *,
    now: date,
    config: RankConfig,
    max_cites_seen: int | None = None,
) -> tuple[float, dict[str, float]]:
    """Return combined score and breakdown dict."""
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


def rank_candidates(
    papers: list[PaperRecord],
    *,
    config: RankConfig | None = None,
    now: date | None = None,
    top_k: int | None = None,
) -> list[PaperRecord]:
    """Score and sort papers, returning top_k if specified."""
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
