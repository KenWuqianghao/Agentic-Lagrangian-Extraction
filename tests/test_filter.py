"""Tests for post-search filters."""

from __future__ import annotations

from datetime import date

from lagrangian_extraction.models import Author, PaperRecord, SearchQuery
from lagrangian_extraction.pipeline.filter import apply_post_filters, is_theory_paper


def _paper(**kwargs: object) -> PaperRecord:
    defaults: dict[str, object] = {"title": "Test Paper", "sources": ["inspire"]}
    defaults.update(kwargs)
    return PaperRecord.model_validate(defaults)


def test_theory_filter_excludes_experimental_arxiv_category() -> None:
    experimental = _paper(categories=["hep-ex"], sources=["arxiv"])
    theory = _paper(categories=["hep-ph"], sources=["arxiv"])
    assert not is_theory_paper(experimental)
    assert is_theory_paper(theory)


def test_theory_filter_uses_inspire_subjects() -> None:
    experimental = _paper(subjects=["Experiment-HEP"])
    theory = _paper(subjects=["Theory-HEP"])
    assert not is_theory_paper(experimental)
    assert is_theory_paper(theory)


def test_exclude_keywords_post_filter() -> None:
    papers = [
        _paper(title="Scalar leptoquark phenomenology"),
        _paper(title="Supersymmetric squark production"),
    ]
    query = SearchQuery(model_name="test", exclude_keywords=["supersymmetry"])
    filtered = apply_post_filters(papers, query)
    assert len(filtered) == 1
    assert "leptoquark" in filtered[0].title


def test_author_filter() -> None:
    papers = [
        _paper(authors=[Author(name="Crivellin, Andreas")]),
        _paper(authors=[Author(name="Someone Else")]),
    ]
    query = SearchQuery(model_name="test", authors=["Crivellin"])
    filtered = apply_post_filters(papers, query)
    assert len(filtered) == 1
    assert filtered[0].authors[0].name.startswith("Crivellin")


def test_until_date_filter() -> None:
    papers = [
        _paper(published=date(2018, 1, 1)),
        _paper(published=date(2024, 1, 1)),
    ]
    query = SearchQuery(model_name="test", until=date(2020, 1, 1))
    filtered = apply_post_filters(papers, query)
    assert len(filtered) == 1
    assert filtered[0].published == date(2018, 1, 1)
