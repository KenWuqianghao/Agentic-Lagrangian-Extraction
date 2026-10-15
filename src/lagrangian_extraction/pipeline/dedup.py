"""Deduplicate and merge paper records from INSPIRE, arXiv, and ADS."""

from __future__ import annotations

import re
from difflib import SequenceMatcher

from lagrangian_extraction.config import TITLE_SIMILARITY_THRESHOLD
from lagrangian_extraction.models import PaperRecord
from lagrangian_extraction.utils import normalize_arxiv_id


def normalize_title(title: str) -> str:
    """Lowercase and strip non-alphanumeric characters for fuzzy matching."""
    return re.sub(r"[^a-z0-9]+", "", title.lower())


def title_similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, normalize_title(a), normalize_title(b)).ratio()


def _merge_records(existing: PaperRecord, incoming: PaperRecord) -> PaperRecord:
    """Merge two records, preferring INSPIRE for citations and arXiv for PDF metadata."""
    data = existing.model_dump()
    incoming_data = incoming.model_dump()

    for field in (
        "arxiv_id",
        "inspire_id",
        "ads_bibcode",
        "doi",
        "title",
        "abstract",
        "published",
        "updated",
    ):
        if not data.get(field) and incoming_data.get(field):
            data[field] = incoming_data[field]

    # Prefer INSPIRE citations when present; fill from ADS only if higher and no inspire_id.
    if incoming.inspire_id is not None or existing.inspire_id is not None:
        if incoming.citation_count > existing.citation_count and existing.inspire_id is None:
            data["citation_count"] = incoming.citation_count
    elif incoming.citation_count > existing.citation_count:
        data["citation_count"] = incoming.citation_count

    if incoming.citation_count_no_self is not None:
        if data.get("citation_count_no_self") is None or (
            incoming.citation_count_no_self > (data.get("citation_count_no_self") or 0)
        ):
            data["citation_count_no_self"] = incoming.citation_count_no_self

    if not data.get("pdf_url") and incoming.pdf_url:
        data["pdf_url"] = incoming.pdf_url
    if not data.get("abs_url") and incoming.abs_url:
        data["abs_url"] = incoming.abs_url

    if incoming.categories:
        merged_cats = list(dict.fromkeys([*(data.get("categories") or []), *incoming.categories]))
        data["categories"] = merged_cats

    if incoming.subjects:
        merged_subjects = list(dict.fromkeys([*(data.get("subjects") or []), *incoming.subjects]))
        data["subjects"] = merged_subjects

    if incoming.authors and not data.get("authors"):
        data["authors"] = incoming.authors

    sources = list(dict.fromkeys([*(existing.sources or []), *(incoming.sources or [])]))
    data["sources"] = sources

    return PaperRecord.model_validate(data)


def _find_match(record: PaperRecord, pool: list[PaperRecord]) -> PaperRecord | None:
    record_arxiv = normalize_arxiv_id(record.arxiv_id)
    for candidate in pool:
        candidate_arxiv = normalize_arxiv_id(candidate.arxiv_id)
        if record_arxiv and candidate_arxiv and record_arxiv == candidate_arxiv:
            return candidate
        if record.doi and candidate.doi and record.doi.lower() == candidate.doi.lower():
            return candidate
        if (
            record.ads_bibcode
            and candidate.ads_bibcode
            and record.ads_bibcode == candidate.ads_bibcode
        ):
            return candidate
        if title_similarity(record.title, candidate.title) >= TITLE_SIMILARITY_THRESHOLD:
            return candidate
    return None


def dedup_and_merge(*record_lists: list[PaperRecord]) -> list[PaperRecord]:
    """Merge results from multiple sources, deduplicating by arxiv_id, DOI, bibcode, or title."""
    merged: list[PaperRecord] = []

    for records in record_lists:
        for record in records:
            match = _find_match(record, merged)
            if match is None:
                merged.append(record)
            else:
                idx = merged.index(match)
                merged[idx] = _merge_records(match, record)

    return merged
