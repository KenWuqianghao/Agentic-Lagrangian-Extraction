"""Tests for the web search UI."""

from __future__ import annotations

from datetime import UTC, date, datetime
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from lagrangian_extraction.models import AuditRun, PaperRecord, RawSearchCounts, SearchQuery
from lagrangian_extraction.web.app import create_app


@pytest.fixture
def client() -> TestClient:
    return TestClient(create_app())


def test_index_page_loads(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "Paper Search" in response.text


def test_filters_endpoint(client: TestClient) -> None:
    response = client.get("/api/filters")
    assert response.status_code == 200
    payload = response.json()
    assert "relevance" in payload["sort_options"]
    assert payload["defaults"]["theory_only"] is True


@patch("lagrangian_extraction.web.app.run_search")
def test_search_endpoint_returns_selected_paper(mock_run: object, client: TestClient) -> None:
    paper = PaperRecord(
        title="Scalar leptoquark Lagrangian",
        arxiv_id="2002.12544",
        inspire_id=123,
        citation_count=50,
        published=date(2020, 1, 1),
        score=0.85,
        score_breakdown={"semantic": 0.4, "lagrangian_signal": 0.7},
        abs_url="https://arxiv.org/abs/2002.12544",
    )
    mock_run.return_value = AuditRun(
        query=SearchQuery(model_name="scalar leptoquark"),
        started_at=datetime.now(UTC),
        finished_at=datetime.now(UTC),
        selected_paper=paper,
        candidates=[paper],
        raw_counts=RawSearchCounts(inspire_hits=10, arxiv_hits=5, merged_unique=12),
    )

    response = client.post(
        "/api/search",
        json={
            "model_name": "scalar leptoquark",
            "keywords": "BSM, leptoquark",
            "since": "2015-01-01",
            "theory_only": True,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["selected_paper"]["title"] == "Scalar leptoquark Lagrangian"
    assert payload["selected_paper"]["citation_count"] == 50
    assert payload["pool_searched"] == 12

    call_args = mock_run.call_args[0][0]
    assert call_args.keywords == ["BSM", "leptoquark"]
    assert call_args.since == date(2015, 1, 1)
