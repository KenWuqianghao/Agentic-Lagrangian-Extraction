"""Orchestrate literature search across INSPIRE, arXiv, and ADS."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.clients.ads import AdsClient
from lagrangian_extraction.clients.arxiv import ArxivClient
from lagrangian_extraction.clients.inspire import InspireClient
from lagrangian_extraction.config import Settings
from lagrangian_extraction.models import AuditRun, RawSearchCounts, SearchQuery
from lagrangian_extraction.pipeline.audit import write_audit_log
from lagrangian_extraction.pipeline.citations import enrich_inspire_citations
from lagrangian_extraction.pipeline.dedup import dedup_and_merge
from lagrangian_extraction.pipeline.filter import apply_post_filters
from lagrangian_extraction.pipeline.pdfs import fetch_pdfs_and_extract
from lagrangian_extraction.pipeline.rank import rank_candidates, rank_for_extraction
from lagrangian_extraction.pipeline.semantic import build_semantic_query, rank_by_semantic
from lagrangian_extraction.pipeline.sources import probe_selected_paper


def _build_client_queries(query: SearchQuery) -> tuple[str, str, str | None]:
    semantic = query.search_mode == "semantic"
    shared = {
        "exclude_keywords": query.exclude_keywords,
        "authors": query.authors,
        "exclude_authors": query.exclude_authors,
        "since": query.since,
        "until": query.until,
        "theory_only": query.theory_only,
        "semantic": semantic,
    }
    inspire_query = InspireClient.build_query(
        query.model_name,
        query.keywords,
        **shared,
    )
    arxiv_query = ArxivClient.build_query(
        query.model_name,
        query.keywords,
        **shared,
    )
    ads_query = None
    if query.use_ads:
        ads_query = AdsClient.build_query(
            query.model_name,
            query.keywords,
            **shared,
        )
    return inspire_query, arxiv_query, ads_query


def _fetch_pool_size(query: SearchQuery, cfg: Settings) -> int:
    """Fetch a wider candidate pool when selecting a single extraction source."""
    requested = query.top_k + query.runners_up
    if query.top_k == 1:
        return max(cfg.rank.selection_pool_size, requested)
    return max(requested * 3, 25)


def _rank_papers(
    merged: list,
    query: SearchQuery,
    cfg: Settings,
) -> list:
    rank_cfg = cfg.rank
    total_needed = query.top_k + query.runners_up

    if query.sort == "semantic":
        semantic_query = build_semantic_query(query.model_name, query.keywords)
        return rank_by_semantic(
            merged,
            semantic_query,
            top_k=total_needed,
            scope=query.semantic_scope,
        )
    if query.sort == "mostcited":
        return sorted(merged, key=lambda p: p.citation_count, reverse=True)[:total_needed]
    if query.sort == "mostrecent":
        return sorted(
            merged,
            key=lambda p: p.published or datetime.min.date(),
            reverse=True,
        )[:total_needed]
    if query.sort == "combined":
        return rank_candidates(merged, config=rank_cfg, top_k=total_needed)

    semantic_query = build_semantic_query(query.model_name, query.keywords)
    return rank_for_extraction(
        merged,
        query_text=semantic_query,
        config=rank_cfg,
        top_k=total_needed,
        semantic_scope=query.semantic_scope,
    )


def run_search(query: SearchQuery, settings: Settings | None = None) -> AuditRun:
    """Execute the Stage 1 literature search pipeline."""
    cfg = settings or Settings()
    cfg.paths.ensure_dirs()

    audit = AuditRun(
        query=query,
        started_at=datetime.now(UTC),
    )

    inspire_query, arxiv_query, ads_query = _build_client_queries(query)

    inspire_sort = (
        "mostcited" if query.sort in {"combined", "mostcited", "relevance"} else "mostrecent"
    )
    fetch_size = _fetch_pool_size(query, cfg)

    try:
        with RateLimitedClient(cfg.rate_limits, cfg.http) as http:
            inspire_client = InspireClient(http)
            arxiv_client = ArxivClient(http)
            ads_client = AdsClient(http)

            def search_inspire() -> tuple[list, str, int]:
                return inspire_client.search(
                    inspire_query,
                    sort=inspire_sort,
                    size=fetch_size,
                )

            def search_arxiv() -> tuple[list, str, int]:
                return arxiv_client.search(arxiv_query, max_results=fetch_size)

            def search_ads() -> tuple[list, str, int]:
                if ads_query is None or not ads_client.is_available:
                    return [], "", 0
                return ads_client.search(ads_query, rows=fetch_size)

            with ThreadPoolExecutor(max_workers=3) as pool:
                inspire_future = pool.submit(search_inspire)
                arxiv_future = pool.submit(search_arxiv)
                ads_future = pool.submit(search_ads)
                inspire_records, inspire_url, inspire_total = inspire_future.result()
                arxiv_records, arxiv_url, arxiv_total = arxiv_future.result()
                ads_records, ads_url, ads_total = ads_future.result()

            if query.use_ads and not ads_client.is_available:
                audit.errors.append(
                    "ADS search skipped: ADS_API_TOKEN not set. "
                    "Get a token at https://ui.adsabs.harvard.edu/#user/settings/token"
                )

            audit.inspire_url = inspire_url
            audit.arxiv_url = arxiv_url
            audit.ads_url = ads_url or None

            merged = dedup_and_merge(inspire_records, arxiv_records, ads_records)
            merged = enrich_inspire_citations(merged, inspire_client)
            merged = apply_post_filters(merged, query)
            audit.raw_counts = RawSearchCounts(
                inspire_hits=inspire_total,
                arxiv_hits=arxiv_total,
                ads_hits=ads_total,
                merged_unique=len(merged),
            )

            ranked = _rank_papers(merged, query, cfg)
            selected = ranked[: query.top_k]
            runners = ranked[query.top_k : query.top_k + query.runners_up]

            audit.selected_paper = selected[0] if selected else None
            audit.candidates = selected
            audit.runners_up = runners

            if query.download_pdfs and selected:
                audit.downloads = fetch_pdfs_and_extract(
                    http,
                    selected,
                    cfg.paths,
                    download=True,
                    extract=query.extract_text,
                )

            if query.probe_latex_source and audit.selected_paper is not None:
                audit.latex_probe = probe_selected_paper(
                    audit.selected_paper,
                    cfg.paths,
                    http,
                )

    except Exception as exc:  # noqa: BLE001 - capture pipeline-level failures in audit
        audit.errors.append(str(exc))
        raise
    finally:
        audit.finished_at = datetime.now(UTC)
        write_audit_log(audit, cfg.paths.runs_dir)

    return audit
