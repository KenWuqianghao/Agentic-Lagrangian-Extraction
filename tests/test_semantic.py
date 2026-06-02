"""Tests for semantic ranking."""

from __future__ import annotations

from lagrangian_extraction.models import PaperRecord
from lagrangian_extraction.pipeline.semantic import rank_by_semantic, semantic_similarity


def test_semantic_similarity_prefers_matching_terms() -> None:
    close = semantic_similarity(
        "scalar leptoquark BSM",
        "We study scalar leptoquark models in BSM physics.",
    )
    far = semantic_similarity(
        "scalar leptoquark BSM",
        "Dark matter direct detection with xenon detectors.",
    )
    assert close > far


def test_rank_by_semantic_orders_by_relevance() -> None:
    papers = [
        PaperRecord(title="Dark matter direct detection"),
        PaperRecord(title="Scalar leptoquark phenomenology in BSM models"),
    ]
    ranked = rank_by_semantic(papers, "scalar leptoquark BSM", top_k=2)
    assert "leptoquark" in ranked[0].title.lower()
    assert ranked[0].score >= ranked[1].score
