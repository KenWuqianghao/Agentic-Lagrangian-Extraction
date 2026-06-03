"""FastAPI app serving a minimal search UI."""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from lagrangian_extraction.config import PathConfig, RankConfig, Settings
from lagrangian_extraction.models import AuditRun, PaperRecord, SearchQuery
from lagrangian_extraction.pipeline.search import run_search

STATIC_DIR = Path(__file__).parent / "static"

SORT_OPTIONS = ("relevance", "combined", "mostcited", "mostrecent", "semantic")
SEARCH_MODES = ("keyword", "semantic")


def _split_terms(value: str) -> list[str]:
    return [part.strip() for part in value.split(",") if part.strip()]


class SearchRequest(BaseModel):
    model_name: str = Field(min_length=1)
    keywords: str = ""
    exclude_keywords: str = ""
    authors: str = ""
    exclude_authors: str = ""
    since: date | None = None
    until: date | None = None
    sort: Literal["relevance", "combined", "mostcited", "mostrecent", "semantic"] = "relevance"
    search_mode: Literal["keyword", "semantic"] = "keyword"
    theory_only: bool = True
    runners_up: int = Field(default=0, ge=0, le=10)
    download_pdfs: bool = False
    extract_text: bool = False


class PaperResponse(BaseModel):
    title: str
    arxiv_id: str | None
    inspire_id: int | None
    citation_count: int
    published: date | None
    score: float
    score_breakdown: dict[str, float]
    abs_url: str | None
    text_path: str | None = None


class SearchResponse(BaseModel):
    run_id: str
    selected_paper: PaperResponse | None
    runners_up: list[PaperResponse]
    pool_searched: int
    inspire_hits: int
    arxiv_hits: int
    audit_log: str
    errors: list[str]


def _paper_to_response(paper: PaperRecord, text_path: str | None = None) -> PaperResponse:
    return PaperResponse(
        title=paper.title,
        arxiv_id=paper.arxiv_id,
        inspire_id=paper.inspire_id,
        citation_count=paper.citation_count,
        published=paper.published,
        score=paper.score,
        score_breakdown=paper.score_breakdown,
        abs_url=paper.abs_url,
        text_path=text_path,
    )


def _build_query(body: SearchRequest) -> SearchQuery:
    return SearchQuery(
        model_name=body.model_name.strip(),
        keywords=_split_terms(body.keywords),
        exclude_keywords=_split_terms(body.exclude_keywords),
        authors=_split_terms(body.authors),
        exclude_authors=_split_terms(body.exclude_authors),
        top_k=1,
        runners_up=body.runners_up,
        since=body.since,
        until=body.until,
        sort=body.sort,
        search_mode=body.search_mode,
        theory_only=body.theory_only,
        download_pdfs=body.download_pdfs,
        extract_text=body.extract_text,
    )


def _audit_to_response(audit: AuditRun, audit_path: Path) -> SearchResponse:
    downloads = {item.arxiv_id: item.text_path for item in audit.downloads}

    selected: PaperResponse | None = None
    if audit.selected_paper is not None:
        arxiv_id = audit.selected_paper.arxiv_id
        selected = _paper_to_response(
            audit.selected_paper,
            downloads.get(arxiv_id) if arxiv_id else None,
        )

    runners = [
        _paper_to_response(paper, downloads.get(paper.arxiv_id) if paper.arxiv_id else None)
        for paper in audit.runners_up
    ]

    return SearchResponse(
        run_id=audit.run_id,
        selected_paper=selected,
        runners_up=runners,
        pool_searched=audit.raw_counts.merged_unique,
        inspire_hits=audit.raw_counts.inspire_hits,
        arxiv_hits=audit.raw_counts.arxiv_hits,
        audit_log=str(audit_path / f"{audit.run_id}.json"),
        errors=audit.errors,
    )


def create_app(data_dir: Path | None = None, runs_dir: Path | None = None) -> FastAPI:
    app = FastAPI(title="Lagrangian Extraction Search", version="0.1.0")

    root_data = data_dir or Path("data")
    root_runs = runs_dir or Path("runs")
    settings = Settings(
        paths=PathConfig(
            data_dir=root_data,
            pdf_dir=root_data / "pdfs",
            text_dir=root_data / "text",
            runs_dir=root_runs,
        ),
        rank=RankConfig(),
    )

    @app.get("/")
    def index() -> FileResponse:
        return FileResponse(STATIC_DIR / "index.html")

    @app.get("/api/filters")
    def filters() -> dict[str, object]:
        return {
            "sort_options": list(SORT_OPTIONS),
            "search_modes": list(SEARCH_MODES),
            "defaults": {
                "sort": "relevance",
                "search_mode": "keyword",
                "theory_only": True,
                "runners_up": 0,
                "download_pdfs": False,
                "extract_text": False,
            },
        }

    @app.post("/api/search", response_model=SearchResponse)
    def search(body: SearchRequest) -> SearchResponse:
        try:
            audit = run_search(_build_query(body), settings)
        except Exception as exc:  # noqa: BLE001 - surface pipeline errors to UI
            raise HTTPException(status_code=500, detail=str(exc)) from exc
        return _audit_to_response(audit, settings.paths.runs_dir)

    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
    return app


app = create_app()
