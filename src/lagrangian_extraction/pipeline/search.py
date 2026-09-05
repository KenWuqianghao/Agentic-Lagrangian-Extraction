"""Orchestrate literature search across INSPIRE and arXiv."""

from __future__ import annotations

from datetime import UTC, datetime

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.clients.arxiv import ArxivClient
from lagrangian_extraction.clients.inspire import InspireClient
from lagrangian_extraction.config import Settings
from lagrangian_extraction.models import AuditRun, RawSearchCounts, SearchQuery
from lagrangian_extraction.pipeline.audit import write_audit_log
from lagrangian_extraction.pipeline.dedup import dedup_and_merge
from lagrangian_extraction.pipeline.pdfs import fetch_pdfs_and_extract
from lagrangian_extraction.pipeline.rank import rank_candidates


def run_search(query: SearchQuery, settings: Settings | None = None) -> AuditRun:
    """Execute the Stage 1 literature search pipeline."""
    cfg = settings or Settings()
    cfg.paths.ensure_dirs()

    audit = AuditRun(
        query=query,
        started_at=datetime.now(UTC),
    )

    inspire_query = InspireClient.build_query(query.model_name, query.keywords, query.since)
    arxiv_query = ArxivClient.build_query(query.model_name, query.keywords)

    inspire_sort = "mostcited" if query.sort in {"combined", "mostcited"} else "mostrecent"
    fetch_size = max(query.top_k * 2, 25)

    try:
        with RateLimitedClient(cfg.rate_limits, cfg.http) as http:
            inspire_client = InspireClient(http)
            arxiv_client = ArxivClient(http)

            inspire_records: list = []
            inspire_url = ""
            inspire_total = 0
            arxiv_records: list = []
            arxiv_url = ""
            arxiv_total = 0

            try:
                inspire_records, inspire_url, inspire_total = inspire_client.search(
                    inspire_query,
                    sort=inspire_sort,
                    size=fetch_size,
                )
            except Exception as exc:  # noqa: BLE001
                audit.errors.append(f"INSPIRE search failed: {exc}")

            try:
                if not query.skip_arxiv:
                    arxiv_records, arxiv_url, arxiv_total = arxiv_client.search(
                        arxiv_query, max_results=fetch_size
                    )
            except Exception as exc:  # noqa: BLE001
                audit.errors.append(f"arXiv search failed: {exc}")

            if not inspire_records and not arxiv_records:
                raise RuntimeError(
                    "Both INSPIRE and arXiv searches failed; see audit errors for details."
                )

            audit.inspire_url = inspire_url
            audit.arxiv_url = arxiv_url

            merged = dedup_and_merge(inspire_records, arxiv_records)
            audit.raw_counts = RawSearchCounts(
                inspire_hits=inspire_total,
                arxiv_hits=arxiv_total,
                merged_unique=len(merged),
            )

            rank_cfg = cfg.rank
            if query.sort == "mostcited":
                ranked = sorted(merged, key=lambda p: p.citation_count, reverse=True)[: query.top_k]
            elif query.sort == "mostrecent":
                ranked = sorted(
                    merged,
                    key=lambda p: p.published or datetime.min.date(),
                    reverse=True,
                )[: query.top_k]
            else:
                ranked = rank_candidates(merged, config=rank_cfg, top_k=query.top_k)

            audit.candidates = ranked

            if query.download_pdfs:
                audit.downloads = fetch_pdfs_and_extract(
                    http,
                    ranked,
                    cfg.paths,
                    download=True,
                    extract=query.extract_text,
                )

    except Exception as exc:  # noqa: BLE001 - capture pipeline-level failures in audit
        audit.errors.append(str(exc))
        raise
    finally:
        audit.finished_at = datetime.now(UTC)
        write_audit_log(audit, cfg.paths.runs_dir)

    return audit
