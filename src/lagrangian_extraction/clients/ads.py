"""NASA ADS (Astrophysics Data System) API client."""

from __future__ import annotations

import os
from datetime import date
from typing import Literal
from urllib.parse import urlencode

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.config import ADS_BASE_URL, ADS_FIELDS
from lagrangian_extraction.models import Author, PaperRecord
from lagrangian_extraction.utils import normalize_arxiv_id, quote_search_term

ADS_PHENOMENOLOGY = '"High Energy Physics - Phenomenology"'
ADS_EXPERIMENT = '"High Energy Physics - Experiment"'


def get_ads_token() -> str | None:
    token = os.environ.get("ADS_API_TOKEN", "").strip()
    return token or None


class AdsClient:
    """Search NASA ADS literature records."""

    def __init__(self, http: RateLimitedClient, token: str | None = None) -> None:
        self._http = http
        self._token = token or get_ads_token()

    @property
    def is_available(self) -> bool:
        return bool(self._token)

    @staticmethod
    def _keyword_clause(keyword: str) -> str:
        term = quote_search_term(keyword)
        return f'abs:{term}'

    @staticmethod
    def _exclude_keyword_clause(keyword: str) -> str:
        term = quote_search_term(keyword)
        return f'NOT abs:{term}'

    @staticmethod
    def build_query(
        model_name: str,
        keywords: list[str] | None = None,
        *,
        exclude_keywords: list[str] | None = None,
        authors: list[str] | None = None,
        exclude_authors: list[str] | None = None,
        since: date | None = None,
        until: date | None = None,
        theory_only: bool = True,
        semantic: bool = False,
    ) -> str:
        parts: list[str] = []

        if semantic:
            parts.append(f'full:"{model_name}"')
        else:
            model_term = quote_search_term(model_name)
            parts.append(f'full:{model_term}')

        if keywords:
            keyword_clause = " OR ".join(
                AdsClient._keyword_clause(keyword) for keyword in keywords
            )
            parts.append(f"({keyword_clause})")

        if exclude_keywords:
            for keyword in exclude_keywords:
                parts.append(AdsClient._exclude_keyword_clause(keyword))

        if authors:
            author_clause = " AND ".join(f'author:"{author}"' for author in authors)
            parts.append(f"({author_clause})")

        if exclude_authors:
            for author in exclude_authors:
                parts.append(f'NOT author:"{author}"')

        if theory_only:
            parts.append(f"arxiv_class:{ADS_PHENOMENOLOGY}")
            parts.append(f"NOT arxiv_class:{ADS_EXPERIMENT}")

        if since and until:
            parts.append(f"year:{since.year}-{until.year}")
        elif since:
            parts.append(f"year:{since.year}+")
        elif until:
            parts.append(f"year:-{until.year}")

        return " AND ".join(parts)

    def search(
        self,
        query: str,
        *,
        rows: int = 25,
        sort: Literal["citation_count desc", "date desc"] = "citation_count desc",
    ) -> tuple[list[PaperRecord], str, int]:
        """Return (records, request_url, total_hits)."""
        if not self._token:
            return [], "", 0

        params = {
            "q": query,
            "fl": ADS_FIELDS,
            "rows": min(rows, 2000),
            "start": 0,
            "sort": sort,
        }
        url = f"{ADS_BASE_URL}?{urlencode(params)}"
        response = self._http.get(
            url,
            headers={"Authorization": f"Bearer {self._token}"},
        )
        payload = response.json()
        response_block = payload.get("response", {})
        total = int(response_block.get("numFound", 0))
        docs = response_block.get("docs", [])
        records = [r for doc in docs if (r := self._parse_doc(doc)) is not None]
        return records[:rows], url, total

    def _parse_doc(self, doc: dict) -> PaperRecord | None:
        title_field = doc.get("title")
        if isinstance(title_field, list):
            title = title_field[0] if title_field else ""
        else:
            title = title_field or ""
        title = str(title).strip()
        if not title:
            return None

        arxiv_id = None
        arxiv_field = doc.get("arxiv")
        if isinstance(arxiv_field, list) and arxiv_field:
            arxiv_id = normalize_arxiv_id(str(arxiv_field[0]))
        elif isinstance(arxiv_field, str):
            arxiv_id = normalize_arxiv_id(arxiv_field)

        doi = None
        doi_field = doc.get("doi")
        if isinstance(doi_field, list) and doi_field:
            doi = str(doi_field[0])
        elif isinstance(doi_field, str):
            doi = doi_field

        authors = []
        for name in doc.get("author", []) or []:
            if name:
                authors.append(Author(name=str(name).strip()))

        abstract = doc.get("abstract")
        if abstract:
            abstract = str(abstract).strip()

        published = None
        pubdate = doc.get("pubdate")
        if isinstance(pubdate, str) and len(pubdate) >= 4:
            try:
                published = date.fromisoformat(pubdate[:10])
            except ValueError:
                if pubdate[:4].isdigit():
                    published = date(int(pubdate[:4]), 1, 1)
        elif doc.get("year"):
            published = date(int(doc["year"]), 1, 1)

        categories: list[str] = []
        for cls in doc.get("arxiv_class", []) or []:
            if cls:
                categories.append(str(cls))

        bibcode = doc.get("bibcode")
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf" if arxiv_id else None
        abs_url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else None

        return PaperRecord(
            arxiv_id=arxiv_id,
            ads_bibcode=str(bibcode) if bibcode else None,
            doi=doi,
            title=title,
            authors=authors,
            abstract=abstract,
            categories=categories,
            published=published,
            citation_count=int(doc.get("citation_count") or 0),
            pdf_url=pdf_url,
            abs_url=abs_url,
            sources=["ads"],
        )
