"""Post-search filters for paper candidates."""

from __future__ import annotations

import re

from lagrangian_extraction.config import (
    EXPERIMENTAL_ARXIV_CATEGORIES,
    EXPERIMENTAL_INSPIRE_SUBJECTS,
    THEORY_ARXIV_CATEGORIES,
)
from lagrangian_extraction.models import PaperRecord, SearchQuery


def _normalize_text(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def _abstract_blob(paper: PaperRecord) -> str:
    return _normalize_text(paper.abstract or "")


def _text_blob(paper: PaperRecord) -> str:
    author_names = " ".join(a.name for a in paper.authors)
    parts = [paper.title, paper.abstract or "", author_names]
    return _normalize_text(" ".join(parts))


def _keyword_in_text(text: str, keyword: str) -> bool:
    normalized = _normalize_text(text)
    needle = _normalize_text(keyword)
    if not needle:
        return False
    if needle in normalized:
        return True
    stem = needle[:6]
    return any(token.startswith(stem) or stem in token for token in normalized.split())


def _matches_keyword(paper: PaperRecord, keyword: str) -> bool:
    return _keyword_in_text(_text_blob(paper), keyword)


def _matches_keyword_in_abstract(paper: PaperRecord, keyword: str) -> bool:
    return _keyword_in_text(_abstract_blob(paper), keyword)


def _matches_author(paper: PaperRecord, author: str) -> bool:
    needle = _normalize_text(author)
    if not needle:
        return False
    for paper_author in paper.authors:
        if needle in _normalize_text(paper_author.name):
            return True
    return False


def is_theory_paper(paper: PaperRecord) -> bool:
    """Return True when a record looks like a theory paper, not experiment."""
    if paper.subjects:
        if any(s in EXPERIMENTAL_INSPIRE_SUBJECTS for s in paper.subjects):
            return False
        if any(s.startswith("Theory") for s in paper.subjects):
            return True

    if paper.categories:
        if any(c in EXPERIMENTAL_ARXIV_CATEGORIES for c in paper.categories):
            return False
        if any(c in THEORY_ARXIV_CATEGORIES for c in paper.categories):
            return True
        return not any(c.startswith("hep-ex") or c.startswith("nucl-ex") for c in paper.categories)

    return True


def _has_sufficient_abstract(paper: PaperRecord, min_length: int) -> bool:
    return paper.abstract is not None and len(paper.abstract.strip()) >= min_length


def apply_post_filters(papers: list[PaperRecord], query: SearchQuery) -> list[PaperRecord]:
    """Apply client-side filters that complement API query syntax."""
    filtered = papers

    if query.theory_only:
        filtered = [p for p in filtered if is_theory_paper(p)]

    if query.require_abstract:
        filtered = [p for p in filtered if _has_sufficient_abstract(p, query.abstract_min_length)]

    if query.until is not None:
        filtered = [
            p for p in filtered if p.published is None or p.published <= query.until  # type: ignore[operator]
        ]

    if query.since is not None:
        filtered = [
            p for p in filtered if p.published is None or p.published >= query.since  # type: ignore[operator]
        ]

    if query.abstract_keyword_match and query.keywords:
        filtered = [
            p
            for p in filtered
            if any(_matches_keyword_in_abstract(p, keyword) for keyword in query.keywords)
        ]

    if query.exclude_keywords:
        if query.abstract_exclude_only:
            filtered = [
                p
                for p in filtered
                if not any(
                    _matches_keyword_in_abstract(p, keyword) for keyword in query.exclude_keywords
                )
            ]
        else:
            filtered = [
                p
                for p in filtered
                if not any(_matches_keyword(p, keyword) for keyword in query.exclude_keywords)
            ]

    if query.exclude_authors:
        filtered = [
            p
            for p in filtered
            if not any(_matches_author(p, author) for author in query.exclude_authors)
        ]

    if query.authors:
        filtered = [
            p for p in filtered if all(_matches_author(p, author) for author in query.authors)
        ]

    return filtered
