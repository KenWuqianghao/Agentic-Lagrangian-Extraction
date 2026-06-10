"""Pydantic schemas for the literature search pipeline."""

from __future__ import annotations

from datetime import date, datetime
from typing import Literal
from uuid import uuid4

from pydantic import BaseModel, Field, field_validator


class Author(BaseModel):
    name: str
    affiliations: list[str] = Field(default_factory=list)


class PaperRecord(BaseModel):
    """Normalized paper metadata from INSPIRE and/or arXiv."""

    arxiv_id: str | None = None
    inspire_id: int | None = None
    ads_bibcode: str | None = None
    doi: str | None = None
    title: str
    authors: list[Author] = Field(default_factory=list)
    abstract: str | None = None
    categories: list[str] = Field(default_factory=list)
    subjects: list[str] = Field(default_factory=list)
    published: date | None = None
    updated: date | None = None
    citation_count: int = 0
    citation_count_no_self: int | None = None
    pdf_url: str | None = None
    abs_url: str | None = None
    sources: list[Literal["inspire", "arxiv", "ads"]] = Field(default_factory=list)
    score: float = 0.0
    score_breakdown: dict[str, float] = Field(default_factory=dict)

    @property
    def is_extractable(self) -> bool:
        """True when the paper has an arXiv ID suitable for PDF/text extraction."""
        return self.arxiv_id is not None

    @property
    def source_ids(self) -> list[str]:
        """Canonical identifiers for audit trail / downstream extraction."""
        ids: list[str] = []
        if self.arxiv_id:
            ids.append(f"arxiv:{self.arxiv_id}")
        if self.inspire_id is not None:
            ids.append(f"inspire:{self.inspire_id}")
        if self.doi:
            ids.append(f"doi:{self.doi}")
        if self.ads_bibcode:
            ids.append(f"ads:{self.ads_bibcode}")
        return ids


class SearchQuery(BaseModel):
    model_name: str
    keywords: list[str] = Field(default_factory=list)
    exclude_keywords: list[str] = Field(default_factory=list)
    authors: list[str] = Field(default_factory=list)
    exclude_authors: list[str] = Field(default_factory=list)
    top_k: int = 1
    runners_up: int = 0
    since: date | None = None
    until: date | None = None
    sort: Literal["relevance", "combined", "mostcited", "mostrecent", "semantic"] = "relevance"
    search_mode: Literal["keyword", "semantic"] = "keyword"
    theory_only: bool = True
    use_ads: bool = True
    require_abstract: bool = False
    abstract_keyword_match: bool = False
    abstract_exclude_only: bool = False
    abstract_min_length: int = 80
    semantic_scope: Literal["full", "abstract", "combined"] = "combined"
    probe_latex_source: bool = False
    download_pdfs: bool = True
    extract_text: bool = True

    @field_validator(
        "keywords",
        "exclude_keywords",
        "authors",
        "exclude_authors",
        mode="before",
    )
    @classmethod
    def strip_terms(cls, value: list[str] | None) -> list[str]:
        if not value:
            return []
        return [item.strip() for item in value if item.strip()]


class LocalPDF(BaseModel):
    arxiv_id: str
    pdf_path: str | None = None
    text_path: str | None = None
    pages: int = 0
    bytes: int = 0
    sha256: str | None = None
    extract_seconds: float = 0.0
    cached: bool = False
    error: str | None = None


class SourceProbeResult(BaseModel):
    arxiv_id: str
    src_url: str
    available: bool
    format: Literal["tex_tar", "single_tex", "pdf_only", "unavailable", "error"] = "unavailable"
    main_tex: str | None = None
    tex_char_count: int = 0
    pdf_text_char_count: int | None = None
    equation_markers: int = 0
    section_count: int = 0
    error: str | None = None


class RawSearchCounts(BaseModel):
    inspire_hits: int = 0
    arxiv_hits: int = 0
    ads_hits: int = 0
    merged_unique: int = 0


class AuditRun(BaseModel):
    run_id: str = Field(default_factory=lambda: uuid4().hex[:12])
    query: SearchQuery
    started_at: datetime
    finished_at: datetime | None = None
    inspire_url: str | None = None
    arxiv_url: str | None = None
    ads_url: str | None = None
    raw_counts: RawSearchCounts = Field(default_factory=RawSearchCounts)
    latex_probe: SourceProbeResult | None = None
    selected_paper: PaperRecord | None = None
    runners_up: list[PaperRecord] = Field(default_factory=list)
    candidates: list[PaperRecord] = Field(default_factory=list)
    downloads: list[LocalPDF] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)
