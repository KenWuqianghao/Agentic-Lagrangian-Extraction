"""Tests for deduplication logic."""

from __future__ import annotations

from lagrangian_extraction.models import PaperRecord
from lagrangian_extraction.pipeline.dedup import dedup_and_merge, normalize_title, title_similarity


def _paper(**kwargs: object) -> PaperRecord:
    defaults = {"title": "Test Paper", "sources": ["inspire"]}
    defaults.update(kwargs)
    return PaperRecord.model_validate(defaults)


def test_dedup_by_arxiv_id_with_version_suffix() -> None:
    inspire = _paper(arxiv_id="1701.00001", citation_count=100, sources=["inspire"])
    arxiv = _paper(
        arxiv_id="1701.00001v1",
        title="Scalar Leptoquarks at the LHC",
        categories=["hep-ph"],
        pdf_url="https://arxiv.org/pdf/1701.00001.pdf",
        sources=["arxiv"],
    )
    merged = dedup_and_merge([inspire], [arxiv])
    assert len(merged) == 1
    assert merged[0].citation_count == 100
    assert merged[0].categories == ["hep-ph"]
    assert set(merged[0].sources) == {"inspire", "arxiv"}


def test_dedup_by_arxiv_id() -> None:
    inspire = _paper(arxiv_id="1701.00001", citation_count=100, sources=["inspire"])
    arxiv = _paper(
        arxiv_id="1701.00001",
        title="Scalar Leptoquarks at the LHC",
        categories=["hep-ph"],
        pdf_url="https://arxiv.org/pdf/1701.00001.pdf",
        sources=["arxiv"],
    )
    merged = dedup_and_merge([inspire], [arxiv])
    assert len(merged) == 1
    assert merged[0].citation_count == 100
    assert merged[0].categories == ["hep-ph"]
    assert set(merged[0].sources) == {"inspire", "arxiv"}


def test_dedup_by_doi() -> None:
    a = _paper(doi="10.1000/test.doi", title="Paper A")
    b = _paper(doi="10.1000/test.doi", title="paper a", sources=["arxiv"])
    merged = dedup_and_merge([a], [b])
    assert len(merged) == 1


def test_dedup_by_similar_title() -> None:
    a = _paper(title="Scalar Leptoquarks at the LHC")
    b = _paper(title="Scalar Leptoquarks at the LHC!", sources=["arxiv"])
    merged = dedup_and_merge([a], [b])
    assert len(merged) == 1


def test_no_false_merge_different_titles() -> None:
    a = _paper(title="Scalar Leptoquarks")
    b = _paper(title="Two Higgs Doublet Model", sources=["arxiv"])
    merged = dedup_and_merge([a], [b])
    assert len(merged) == 2


def test_normalize_title() -> None:
    assert normalize_title("Hello, World!") == normalize_title("hello world")


def test_title_similarity_threshold() -> None:
    assert title_similarity("Scalar Leptoquarks", "Scalar Leptoquarks!") >= 0.95
    assert title_similarity("Scalar Leptoquark", "Dark Matter Portal") < 0.95
