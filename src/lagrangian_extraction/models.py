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
    doi: str | None = None
    title: str
    authors: list[Author] = Field(default_factory=list)
    abstract: str | None = None
    categories: list[str] = Field(default_factory=list)
    published: date | None = None
    updated: date | None = None
    citation_count: int = 0
    citation_count_no_self: int | None = None
    pdf_url: str | None = None
    abs_url: str | None = None
    sources: list[Literal["inspire", "arxiv"]] = Field(default_factory=list)
    score: float = 0.0
    score_breakdown: dict[str, float] = Field(default_factory=dict)

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
        return ids


class SearchQuery(BaseModel):
    model_name: str
    keywords: list[str] = Field(default_factory=list)
    top_k: int = 20
    since: date | None = None
    sort: Literal["combined", "mostcited", "mostrecent"] = "combined"
    download_pdfs: bool = True
    extract_text: bool = True

    @field_validator("keywords", mode="before")
    @classmethod
    def strip_keywords(cls, value: list[str] | None) -> list[str]:
        if not value:
            return []
        return [k.strip() for k in value if k.strip()]


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


class RawSearchCounts(BaseModel):
    inspire_hits: int = 0
    arxiv_hits: int = 0
    merged_unique: int = 0


class AuditRun(BaseModel):
    run_id: str = Field(default_factory=lambda: uuid4().hex[:12])
    query: SearchQuery
    started_at: datetime
    finished_at: datetime | None = None
    inspire_url: str | None = None
    arxiv_url: str | None = None
    raw_counts: RawSearchCounts = Field(default_factory=RawSearchCounts)
    candidates: list[PaperRecord] = Field(default_factory=list)
    downloads: list[LocalPDF] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)
