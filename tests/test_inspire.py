"""Tests for INSPIRE client."""

from __future__ import annotations

import json

import respx

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.clients.inspire import InspireClient
from lagrangian_extraction.config import INSPIRE_BASE_URL, RateLimitConfig
from tests.conftest import load_fixture


@respx.mock
def test_inspire_search_parses_records() -> None:
    payload = json.loads(load_fixture("inspire_leptoquark.json"))
    respx.get(INSPIRE_BASE_URL).respond(json=payload)

    with RateLimitedClient(RateLimitConfig()) as http:
        client = InspireClient(http)
        records, url, total = client.search('title "scalar leptoquark"')

    assert total == 2
    assert "inspirehep.net" in url
    assert len(records) == 2
    assert records[0].arxiv_id == "1701.00001"
    assert records[0].citation_count == 120
    assert records[0].inspire_id == 1234567
    assert "inspire" in records[0].sources


def test_inspire_build_query_with_keywords_and_since() -> None:
    from datetime import date

    q = InspireClient.build_query(
        "scalar leptoquark",
        ["BSM", "leptoquark"],
        since=date(2015, 1, 1),
        theory_only=True,
    )
    assert 'title "scalar leptoquark"' in q or "abstracts.value:" in q
    assert "abstracts.value:BSM" in q
    assert "ft BSM" in q
    assert "date 2015+" in q
    assert "not subject:Experiment-HEP" in q


def test_inspire_build_query_with_negation_and_authors() -> None:
    q = InspireClient.build_query(
        "scalar leptoquark",
        exclude_keywords=["supersymmetry"],
        authors=["Crivellin"],
        exclude_authors=["ATLAS"],
        semantic=True,
    )
    assert "scalar leptoquark" in q
    assert 'title "' not in q
    assert "not (abstracts.value:supersymmetry" in q
    assert "ft supersymmetry" in q
    assert 'a "Crivellin"' in q
    assert 'not a "ATLAS"' in q


def test_inspire_keyword_clause_searches_abstract_and_title() -> None:
    clause = InspireClient._keyword_match_clause("sugra")
    assert "abstracts.value:sugra" in clause
    assert "ft sugra" in clause
    assert "title sugra" in clause
