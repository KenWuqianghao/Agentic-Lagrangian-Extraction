"""Tests for arXiv client."""

from __future__ import annotations

import respx

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.clients.arxiv import ArxivClient
from lagrangian_extraction.config import ARXIV_BASE_URL, RateLimitConfig
from tests.conftest import load_fixture


@respx.mock
def test_arxiv_search_parses_atom_feed() -> None:
    respx.get(ARXIV_BASE_URL).respond(text=load_fixture("arxiv_leptoquark.xml"))

    with RateLimitedClient(RateLimitConfig()) as http:
        client = ArxivClient(http)
        records, url, total = client.search("cat:hep-ph")

    assert total == 2
    assert "export.arxiv.org" in url
    assert records[0].arxiv_id == "1701.00001"
    assert records[0].title == "Scalar Leptoquarks at the LHC"
    assert records[0].categories == ["hep-ph"]
    assert "arxiv" in records[0].sources


def test_arxiv_build_query() -> None:
    q = ArxivClient.build_query("scalar leptoquark", ["BSM"])
    assert 'ti:"scalar leptoquark"' in q
    assert "abs:BSM" in q
    assert q.startswith("cat:hep-ph")
