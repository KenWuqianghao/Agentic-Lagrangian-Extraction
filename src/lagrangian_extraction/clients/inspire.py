"""INSPIRE-HEP REST API client."""

from __future__ import annotations

from datetime import date
from typing import Literal
from urllib.parse import urlencode

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.config import INSPIRE_BASE_URL, INSPIRE_FIELDS
from lagrangian_extraction.models import Author, PaperRecord
from lagrangian_extraction.utils import normalize_arxiv_id


class InspireClient:
    """Search INSPIRE literature records."""

    def __init__(self, http: RateLimitedClient) -> None:
        self._http = http

    @staticmethod
    def build_query(model_name: str, keywords: list[str], since: date | None = None) -> str:
        parts = [f'title "{model_name}"']
        if keywords:
            keyword_clause = " or ".join(f"k {kw}" for kw in keywords)
            parts.append(f"({keyword_clause})")
        if since:
            # INSPIRE uses "+" for open-ended lower bound (e.g. date 2015+)
            parts.append(f"date {since.year}+")
        return " and ".join(parts)

    def search(
        self,
        query: str,
        *,
        sort: Literal["mostcited", "mostrecent"] = "mostcited",
        size: int = 25,
        fields: str = INSPIRE_FIELDS,
        max_pages: int = 4,
    ) -> tuple[list[PaperRecord], str, int]:
        """Return (records, first_request_url, total_hits)."""
        params: dict[str, str | int] = {
            "q": query,
            "sort": sort,
            "size": min(size, 1000),
            "page": 1,
            "fields": fields,
        }
        first_url = f"{INSPIRE_BASE_URL}?{urlencode(params)}"
        records: list[PaperRecord] = []
        total = 0
        url: str | None = first_url
        pages_fetched = 0

        while url and pages_fetched < max_pages and len(records) < size:
            response = self._http.get(url)
            payload = response.json()
            hits = payload.get("hits", {})
            total = int(hits.get("total", 0))
            for hit in hits.get("hits", []):
                record = self._parse_hit(hit)
                if record is not None:
                    records.append(record)
                if len(records) >= size:
                    break
            url = payload.get("links", {}).get("next")
            pages_fetched += 1

        return records[:size], first_url, total

    def _parse_hit(self, hit: dict) -> PaperRecord | None:
        metadata = hit.get("metadata", {})
        titles = metadata.get("titles", [])
        if not titles:
            return None

        title = titles[0].get("title", "").strip()
        if not title:
            return None

        arxiv_id = None
        arxiv_eprints = metadata.get("arxiv_eprints", [])
        if arxiv_eprints:
            arxiv_id = normalize_arxiv_id(arxiv_eprints[0].get("value"))

        doi = None
        dois = metadata.get("dois", [])
        if dois:
            doi = dois[0].get("value")

        authors = [
            Author(name=a.get("full_name", "").strip())
            for a in metadata.get("authors", [])
            if a.get("full_name")
        ]

        abstract = None
        abstracts = metadata.get("abstracts", [])
        if abstracts:
            abstract = abstracts[0].get("value")

        published = None
        earliest = metadata.get("earliest_date")
        if earliest:
            published = date.fromisoformat(earliest[:10])

        inspire_id = metadata.get("control_number") or hit.get("id")

        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf" if arxiv_id else None
        abs_url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else None

        return PaperRecord(
            arxiv_id=arxiv_id,
            inspire_id=int(inspire_id) if inspire_id is not None else None,
            doi=doi,
            title=title,
            authors=authors,
            abstract=abstract,
            published=published,
            citation_count=int(metadata.get("citation_count") or 0),
            citation_count_no_self=metadata.get("citation_count_without_self_citations"),
            pdf_url=pdf_url,
            abs_url=abs_url,
            sources=["inspire"],
        )
