"""Configuration defaults for the literature search pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class RateLimitConfig:
    """Per-host rate limits expressed as max requests per window (seconds)."""

    inspire_max_requests: int = 15
    inspire_window_seconds: float = 5.0
    arxiv_max_requests: int = 1
    arxiv_window_seconds: float = 3.0


@dataclass
class RankConfig:
    """Weights and parameters for combined citation + recency ranking."""

    weight_citation: float = 0.7
    weight_recency: float = 0.3
    recency_half_life_years: float = 5.0
    max_cites_seen: int = 10_000


@dataclass
class PathConfig:
    """Filesystem paths for cached artifacts and audit logs."""

    data_dir: Path = field(default_factory=lambda: Path("data"))
    pdf_dir: Path = field(default_factory=lambda: Path("data/pdfs"))
    text_dir: Path = field(default_factory=lambda: Path("data/text"))
    runs_dir: Path = field(default_factory=lambda: Path("runs"))

    def ensure_dirs(self) -> None:
        self.pdf_dir.mkdir(parents=True, exist_ok=True)
        self.text_dir.mkdir(parents=True, exist_ok=True)
        self.runs_dir.mkdir(parents=True, exist_ok=True)


@dataclass
class HttpConfig:
    """HTTP client settings."""

    user_agent: str = "LagrangianExtraction/0.1 (mailto:ken.wu@uwaterloo.ca)"
    timeout_seconds: float = 30.0
    max_retries: int = 5


@dataclass
class Settings:
    """Top-level settings bundle."""

    paths: PathConfig = field(default_factory=PathConfig)
    rate_limits: RateLimitConfig = field(default_factory=RateLimitConfig)
    rank: RankConfig = field(default_factory=RankConfig)
    http: HttpConfig = field(default_factory=HttpConfig)


DEFAULT_SETTINGS = Settings()

INSPIRE_BASE_URL = "https://inspirehep.net/api/literature"
ARXIV_BASE_URL = "https://export.arxiv.org/api/query"

INSPIRE_FIELDS = (
    "titles,authors.full_name,arxiv_eprints,dois,"
    "citation_count,citation_count_without_self_citations,"
    "earliest_date,abstracts,control_number"
)

TITLE_SIMILARITY_THRESHOLD = 0.95
