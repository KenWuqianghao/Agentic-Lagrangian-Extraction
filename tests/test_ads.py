"""Tests for ADS client."""

from __future__ import annotations

import json

import respx

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.clients.ads import AdsClient
from lagrangian_extraction.config import ADS_BASE_URL, RateLimitConfig
from tests.conftest import load_fixture


@respx.mock
def test_ads_search_parses_records(monkeypatch) -> None:
    monkeypatch.setenv("ADS_API_TOKEN", "test-token")
    payload = json.loads(load_fixture("ads_leptoquark.json"))
    respx.get(ADS_BASE_URL).respond(json=payload)

    with RateLimitedClient(RateLimitConfig()) as http:
        client = AdsClient(http, token="test-token")
        records, url, total = client.search('full:"scalar leptoquark"')

    assert total == 2
    assert "api.adsabs.harvard.edu" in url
    assert len(records) == 2
    assert records[0].arxiv_id == "2002.12544"
    assert records[0].ads_bibcode == "2020PhRvD.101.035001"
    assert records[0].citation_count == 107
    assert "ads" in records[0].sources


def test_ads_build_query_with_theory_filter() -> None:
    from datetime import date

    q = AdsClient.build_query(
        "scalar leptoquark",
        ["BSM"],
        since=date(2015, 1, 1),
        theory_only=True,
    )
    assert 'full:"scalar leptoquark"' in q or "full:" in q
    assert "abs:BSM" in q
    assert "arxiv_class:" in q
    assert "year:2015+" in q


def test_ads_skips_without_token(monkeypatch) -> None:
    monkeypatch.delenv("ADS_API_TOKEN", raising=False)
    with RateLimitedClient(RateLimitConfig()) as http:
        client = AdsClient(http, token=None)
        records, url, total = client.search("test")
    assert records == []
    assert total == 0
    assert not client.is_available
