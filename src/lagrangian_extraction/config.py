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
    ads_max_requests: int = 1
    ads_window_seconds: float = 1.0


@dataclass
class RankConfig:
    """Weights and parameters for ranking paper candidates."""

    weight_citation: float = 0.7
    weight_recency: float = 0.3
    weight_semantic: float = 0.45
    weight_semantic_full: float = 0.4
    weight_semantic_abstract: float = 0.6
    weight_lagrangian: float = 0.25
    recency_half_life_years: float = 5.0
    max_cites_seen: int = 10_000

    # Pool size when selecting a single paper for Lagrangian extraction.
    selection_pool_size: int = 50


@dataclass
class PathConfig:
    """Filesystem paths for cached artifacts and audit logs."""

    data_dir: Path = field(default_factory=lambda: Path("data"))
    pdf_dir: Path = field(default_factory=lambda: Path("data/pdfs"))
    text_dir: Path = field(default_factory=lambda: Path("data/text"))
    src_dir: Path = field(default_factory=lambda: Path("data/src"))
    runs_dir: Path = field(default_factory=lambda: Path("runs"))

    def ensure_dirs(self) -> None:
        self.pdf_dir.mkdir(parents=True, exist_ok=True)
        self.text_dir.mkdir(parents=True, exist_ok=True)
        self.src_dir.mkdir(parents=True, exist_ok=True)
        self.runs_dir.mkdir(parents=True, exist_ok=True)


@dataclass
class HttpConfig:
    """HTTP client settings."""

    user_agent: str = "LagrangianExtraction/0.1 (mailto:ken.wu@uwaterloo.ca)"
    timeout_seconds: float = 30.0
    max_retries: int = 3


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
ADS_BASE_URL = "https://api.adsabs.harvard.edu/v1/search/query"
ADS_FIELDS = "bibcode,title,abstract,author,citation_count,arxiv,doi,pubdate,year,arxiv_class"

INSPIRE_FIELDS = (
    "titles,authors.full_name,arxiv_eprints,dois,"
    "citation_count,citation_count_without_self_citations,"
    "earliest_date,abstracts,control_number,subjects.term"
)

TITLE_SIMILARITY_THRESHOLD = 0.95

EXPERIMENTAL_ARXIV_CATEGORIES = frozenset(
    {
        "hep-ex",
        "nucl-ex",
        "physics.ins-det",
        "physics.acc-ph",
        "astro-ph.CO",
        "astro-ph.HE",
        "astro-ph.IM",
        "astro-ph.SR",
    }
)

THEORY_ARXIV_CATEGORIES = frozenset(
    {
        "hep-ph",
        "hep-th",
        "hep-lat",
        "gr-qc",
        "math-ph",
        "nucl-th",
    }
)

EXPERIMENTAL_INSPIRE_SUBJECTS = frozenset(
    {
        "Experiment-HEP",
        "Experiment-Nucl",
        "Astrophysics",
    }
)
