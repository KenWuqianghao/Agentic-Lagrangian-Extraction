"""Tests for the rate-limited HTTP client."""

from __future__ import annotations

import httpx
import respx

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.config import ARXIV_BASE_URL, HttpConfig, RateLimitConfig


@respx.mock
def test_retries_on_429_with_retry_after() -> None:
    route = respx.get(ARXIV_BASE_URL).mock(
        side_effect=[
            httpx.Response(429, headers={"Retry-After": "0.01"}),
            httpx.Response(200, text="<feed/>"),
        ]
    )

    with RateLimitedClient(
        RateLimitConfig(arxiv_window_seconds=0.01),
        HttpConfig(max_retries=3),
    ) as http:
        response = http.get(ARXIV_BASE_URL)

    assert response.status_code == 200
    assert route.call_count == 2


@respx.mock
def test_arxiv_hosts_share_rate_limit_bucket() -> None:
    api = respx.get("https://export.arxiv.org/api/query").respond(200, text="<feed/>")
    pdf = respx.get("https://arxiv.org/pdf/1701.00001.pdf").respond(200, content=b"%PDF-")

    limits = RateLimitConfig(arxiv_max_requests=1, arxiv_window_seconds=10.0)
    with RateLimitedClient(limits, HttpConfig(max_retries=1)) as http:
        http.get("https://export.arxiv.org/api/query")
        http.get("https://arxiv.org/pdf/1701.00001.pdf")

    assert api.call_count == 1
    assert pdf.call_count == 1
