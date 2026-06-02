"""INSPIRE-HEP REST API client."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Literal
from urllib.parse import urlencode

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.config import INSPIRE_BASE_URL, INSPIRE_FIELDS
from lagrangian_extraction.models import Author, PaperRecord
from lagrangian_extraction.utils import normalize_arxiv_id, quote_search_term

ARXIV_LOOKUP_BATCH_SIZE = 20


def _parse_inspire_date(value: str) -> date | None:
    """Parse INSPIRE earliest_date values (YYYY-MM-DD or YYYY)."""
    value = value.strip()
    if len(value) >= 10:
        return date.fromisoformat(value[:10])
    if len(value) == 4 and value.isdigit():
        return date(int(value), 1, 1)
    return None


@dataclass(frozen=True)
class InspireLookup:
    """Minimal INSPIRE metadata fetched by arXiv ID."""

    citation_count: int
    citation_count_no_self: int | None
    inspire_id: int | None
    subjects: list[str]
    abstract: str | None
    published: date | None


class InspireClient:
    """Search INSPIRE literature records."""

    def __init__(self, http: RateLimitedClient) -> None:
        self._http = http

    @staticmethod
    def _keyword_match_clause(keyword: str) -> str:
        """Match a keyword in abstract, fulltext, title, or INSPIRE keyword metadata."""
        term = quote_search_term(keyword)
        return (
            f"(abstracts.value:{term} OR ft {term} OR title {term} OR k {term})"
        )

    @staticmethod
    def _exclude_keyword_clause(keyword: str) -> str:
        term = quote_search_term(keyword)
        return f"not (abstracts.value:{term} OR ft {term} OR title {term} OR k {term})"

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
        theory_only: bool = False,
        semantic: bool = False,
    ) -> str:
        parts: list[str] = []

        if semantic:
            parts.append(model_name)
        else:
            model_term = quote_search_term(model_name)
            parts.append(
                f'(title {model_term} OR abstracts.value:{model_term} OR ft {model_term})'
            )

        if keywords:
            keyword_clause = " or ".join(
                InspireClient._keyword_match_clause(keyword) for keyword in keywords
            )
            parts.append(f"({keyword_clause})")

        if exclude_keywords:
            for keyword in exclude_keywords:
                parts.append(InspireClient._exclude_keyword_clause(keyword))

        if authors:
            author_clause = " and ".join(f'a "{author}"' for author in authors)
            parts.append(f"({author_clause})")

        if exclude_authors:
            for author in exclude_authors:
                parts.append(f'not a "{author}"')

        if theory_only:
            parts.append("not subject:Experiment-HEP")
            parts.append("not subject:Experiment-Nucl")

        if since and until:
            parts.append(f"date {since.year}->{until.year}")
        elif since:
            parts.append(f"date {since.year}+")
        elif until:
            parts.append(f"date ->{until.year}")

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

    def lookup_by_arxiv_ids(self, arxiv_ids: list[str]) -> dict[str, InspireLookup]:
        """Batch-fetch INSPIRE citation metadata keyed by normalized arXiv ID."""
        normalized_ids = [
            aid for aid in dict.fromkeys(normalize_arxiv_id(arxiv_id) for arxiv_id in arxiv_ids) if aid
        ]
        if not normalized_ids:
            return {}

        results: dict[str, InspireLookup] = {}
        for start in range(0, len(normalized_ids), ARXIV_LOOKUP_BATCH_SIZE):
            batch = normalized_ids[start : start + ARXIV_LOOKUP_BATCH_SIZE]
            query = " or ".join(f"eprint {arxiv_id}" for arxiv_id in batch)
            records, _, _ = self.search(query, sort="mostrecent", size=len(batch), max_pages=1)
            for record in records:
                arxiv_id = normalize_arxiv_id(record.arxiv_id)
                if not arxiv_id:
                    continue
                results[arxiv_id] = InspireLookup(
                    citation_count=record.citation_count,
                    citation_count_no_self=record.citation_count_no_self,
                    inspire_id=record.inspire_id,
                    subjects=record.subjects,
                    abstract=record.abstract,
                    published=record.published,
                )
        return results

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
            published = _parse_inspire_date(earliest)

        inspire_id = metadata.get("control_number") or hit.get("id")

        subjects = [
            subject.get("term", "").strip()
            for subject in metadata.get("subjects", [])
            if subject.get("term")
        ]

        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf" if arxiv_id else None
        abs_url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else None

        return PaperRecord(
            arxiv_id=arxiv_id,
            inspire_id=int(inspire_id) if inspire_id is not None else None,
            doi=doi,
            title=title,
            authors=authors,
            abstract=abstract,
            subjects=subjects,
            published=published,
            citation_count=int(metadata.get("citation_count") or 0),
            citation_count_no_self=metadata.get("citation_count_without_self_citations"),
            pdf_url=pdf_url,
            abs_url=abs_url,
            sources=["inspire"],
        )
