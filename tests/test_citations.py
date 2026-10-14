"""Tests for INSPIRE citation enrichment."""

from __future__ import annotations

import json

import respx

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.clients.inspire import InspireClient
from lagrangian_extraction.config import INSPIRE_BASE_URL, RateLimitConfig
from lagrangian_extraction.models import PaperRecord
from lagrangian_extraction.pipeline.citations import enrich_inspire_citations
from tests.conftest import load_fixture


@respx.mock
def test_enrich_inspire_citations_fills_missing_counts() -> None:
    payload = json.loads(load_fixture("inspire_leptoquark.json"))
    respx.get(INSPIRE_BASE_URL).respond(json=payload)

    arxiv_only = PaperRecord(
        title="Scalar Leptoquarks at the LHC",
        arxiv_id="1701.00001",
        citation_count=0,
        sources=["arxiv"],
    )

    with RateLimitedClient(RateLimitConfig()) as http:
        client = InspireClient(http)
        enriched = enrich_inspire_citations([arxiv_only], client)

    assert enriched[0].citation_count == 120
    assert enriched[0].inspire_id == 1234567
    assert "inspire" in enriched[0].sources


@respx.mock
def test_lookup_by_arxiv_ids_returns_mapping() -> None:
    payload = json.loads(load_fixture("inspire_leptoquark.json"))
    respx.get(INSPIRE_BASE_URL).respond(json=payload)

    with RateLimitedClient(RateLimitConfig()) as http:
        client = InspireClient(http)
        lookup = client.lookup_by_arxiv_ids(["1701.00001", "1802.00002"])

    assert lookup["1701.00001"].citation_count == 120
    assert lookup["1802.00002"].citation_count == 45
