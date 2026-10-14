"""Enrich paper records with INSPIRE citation metadata."""

from __future__ import annotations

from lagrangian_extraction.clients.inspire import InspireClient
from lagrangian_extraction.models import PaperRecord
from lagrangian_extraction.utils import normalize_arxiv_id

ARXIV_LOOKUP_BATCH_SIZE = 20


def enrich_inspire_citations(
    papers: list[PaperRecord],
    inspire_client: InspireClient,
) -> list[PaperRecord]:
    """Fill missing INSPIRE citation counts via arXiv ID lookup."""
    lookup_ids: list[str] = []
    for paper in papers:
        arxiv_id = normalize_arxiv_id(paper.arxiv_id)
        if arxiv_id and (paper.citation_count == 0 or paper.inspire_id is None):
            lookup_ids.append(arxiv_id)

    if not lookup_ids:
        return papers

    inspire_data = inspire_client.lookup_by_arxiv_ids(lookup_ids)
    if not inspire_data:
        return papers

    enriched: list[PaperRecord] = []
    for paper in papers:
        arxiv_id = normalize_arxiv_id(paper.arxiv_id)
        if arxiv_id and arxiv_id in inspire_data:
            lookup = inspire_data[arxiv_id]
            updates: dict[str, object] = {}
            if lookup.citation_count > paper.citation_count:
                updates["citation_count"] = lookup.citation_count
            if lookup.citation_count_no_self is not None:
                updates["citation_count_no_self"] = lookup.citation_count_no_self
            if paper.inspire_id is None and lookup.inspire_id is not None:
                updates["inspire_id"] = lookup.inspire_id
            if lookup.subjects and not paper.subjects:
                updates["subjects"] = lookup.subjects
            if lookup.abstract and not paper.abstract:
                updates["abstract"] = lookup.abstract
            if lookup.published and not paper.published:
                updates["published"] = lookup.published
            if "inspire" not in paper.sources:
                updates["sources"] = [*paper.sources, "inspire"]
            enriched.append(paper.model_copy(update=updates) if updates else paper)
        else:
            enriched.append(paper)

    return enriched
