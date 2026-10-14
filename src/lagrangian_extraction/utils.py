"""Utilities for normalizing literature identifiers."""

from __future__ import annotations

import re

ARXIV_VERSION_SUFFIX = re.compile(r"v\d+$")


def normalize_arxiv_id(arxiv_id: str | None) -> str | None:
    """Strip arXiv version suffix (e.g. 1701.00001v2 -> 1701.00001)."""
    if not arxiv_id:
        return None
    return ARXIV_VERSION_SUFFIX.sub("", arxiv_id.strip())


def quote_search_term(term: str) -> str:
    """Quote multi-word search terms for API query strings."""
    stripped = term.strip()
    if not stripped:
        return '""'
    if " " in stripped or "-" in stripped:
        return f'"{stripped}"'
    return stripped
