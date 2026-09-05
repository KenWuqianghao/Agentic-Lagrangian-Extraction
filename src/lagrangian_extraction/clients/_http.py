"""Shared HTTP client with per-host rate limiting and retries."""

from __future__ import annotations

import threading
import time
from collections import deque
from typing import Any
from urllib.parse import urlparse

import httpx
from tenacity import RetryCallState, retry, retry_if_exception, stop_after_attempt

from lagrangian_extraction.config import HttpConfig, RateLimitConfig

ARXIV_HOSTS = frozenset({"export.arxiv.org", "arxiv.org"})


class TokenBucket:
    """Thread-safe token bucket rate limiter."""

    def __init__(self, max_requests: int, window_seconds: float) -> None:
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._timestamps: deque[float] = deque()
        self._lock = threading.Lock()

    def acquire(self) -> None:
        while True:
            with self._lock:
                now = time.monotonic()
                while self._timestamps and now - self._timestamps[0] >= self.window_seconds:
                    self._timestamps.popleft()
                if len(self._timestamps) < self.max_requests:
                    self._timestamps.append(now)
                    return
                sleep_for = self.window_seconds - (now - self._timestamps[0])
            time.sleep(max(sleep_for, 0.01))


def _is_retryable(exc: BaseException) -> bool:
    if isinstance(exc, httpx.HTTPStatusError):
        return exc.response.status_code in {429, 500, 502, 503, 504}
    return isinstance(exc, httpx.TransportError)


def _retry_wait_seconds(retry_state: RetryCallState) -> float:
    """Honor Retry-After on 429; otherwise exponential backoff (arXiv omits the header)."""
    if retry_state.outcome is not None:
        exc = retry_state.outcome.exception()
        if isinstance(exc, httpx.HTTPStatusError) and exc.response.status_code == 429:
            retry_after = exc.response.headers.get("Retry-After")
            if retry_after:
                try:
                    return max(float(retry_after), 3.0)
                except ValueError:
                    pass
            # arXiv often returns 429 without Retry-After after burst traffic.
            attempt = retry_state.attempt_number
            return min(15.0 * (2 ** (attempt - 1)), 120.0)
    attempt = retry_state.attempt_number
    return min(3.0 * (2 ** (attempt - 1)), 60.0)


class RateLimitedClient:
    """httpx wrapper that enforces per-host rate limits and retries."""

    def __init__(
        self,
        rate_limits: RateLimitConfig,
        http_config: HttpConfig | None = None,
    ) -> None:
        self._http_config = http_config or HttpConfig()
        self._client = httpx.Client(
            timeout=self._http_config.timeout_seconds,
            headers={"User-Agent": self._http_config.user_agent},
            follow_redirects=True,
        )
        # arXiv rate-limits by IP across export.arxiv.org and arxiv.org — one shared bucket.
        self._arxiv_bucket = TokenBucket(
            rate_limits.arxiv_max_requests,
            rate_limits.arxiv_window_seconds,
        )
        self._buckets: dict[str, TokenBucket] = {
            "inspirehep.net": TokenBucket(
                rate_limits.inspire_max_requests,
                rate_limits.inspire_window_seconds,
            ),
        }
        self._default_bucket = TokenBucket(10, 1.0)

    def _bucket_for(self, url: str) -> TokenBucket:
        host = urlparse(url).netloc.lower()
        if host.startswith("www."):
            host = host[4:]
        if host in ARXIV_HOSTS:
            return self._arxiv_bucket
        return self._buckets.get(host, self._default_bucket)

    def get(self, url: str, **kwargs: Any) -> httpx.Response:
        max_attempts = self._http_config.max_retries

        @retry(
            retry=retry_if_exception(_is_retryable),
            stop=stop_after_attempt(max_attempts),
            wait=_retry_wait_seconds,
            reraise=True,
        )
        def _do_get() -> httpx.Response:
            self._bucket_for(url).acquire()
            response = self._client.get(url, **kwargs)
            response.raise_for_status()
            return response

        return _do_get()

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> RateLimitedClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()
