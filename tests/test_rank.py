"""Tests for ranking logic."""

from __future__ import annotations

from datetime import date

from lagrangian_extraction.config import RankConfig
from lagrangian_extraction.models import PaperRecord
from lagrangian_extraction.pipeline.rank import compute_score, rank_candidates


def _paper(citations: int, published: date, title: str = "Paper") -> PaperRecord:
    return PaperRecord(title=title, citation_count=citations, published=published)


def test_highly_cited_ranks_above_recent() -> None:
    old_popular = _paper(500, date(2010, 1, 1), "Old Popular")
    recent_obscure = _paper(5, date(2024, 1, 1), "Recent Obscure")
    ranked = rank_candidates([recent_obscure, old_popular], now=date(2025, 1, 1), top_k=2)
    assert ranked[0].title == "Old Popular"


def test_recency_weight_influences_order() -> None:
    cfg = RankConfig(weight_citation=0.0, weight_recency=1.0)
    older = _paper(0, date(2010, 1, 1), "Older")
    newer = _paper(0, date(2023, 1, 1), "Newer")
    ranked = rank_candidates([older, newer], config=cfg, now=date(2025, 1, 1))
    assert ranked[0].title == "Newer"


def test_score_breakdown_populated() -> None:
    paper = _paper(10, date(2020, 1, 1))
    score, breakdown = compute_score(paper, now=date(2025, 1, 1), config=RankConfig())
    assert score > 0
    assert "citation_norm" in breakdown
    assert "recency" in breakdown
