# Lagrangian Extraction — Stage 1 Literature Search

Stage 1 of the HEPSIM5 agentic pipeline: search INSPIRE-HEP and arXiv for BSM model papers, deduplicate and rank candidates by citation count and recency, download PDFs from arXiv, extract plain text, and write a reproducible audit trail.

This implements **Weeks 1–2 (first half)** of the [GSoC HEPSIM5 proposal](https://github.com/KenWuqianghao): literature retrieval and PDF text extraction. Chunking, ChromaDB indexing, LLM extraction, Jinja2 `.fr` generation, and FeynRules validation are deferred to later stages.

## Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# Search for scalar leptoquark papers (CLI is `lag-extract`, not `lex` — macOS ships
# /usr/bin/lex as the flex lexer, which conflicts if the package is not installed)
lag-extract search "scalar leptoquark" \
  --keywords BSM --keywords leptoquark \
  --top-k 10 \
  --since 2015-01-01 \
  --w-cite 0.7 --w-recent 0.3
```

### CLI options

| Flag | Default | Description |
|------|---------|-------------|
| `--keywords / -k` | (none) | Additional BSM keywords (repeatable) |
| `--top-k` | 10 | Number of ranked candidates |
| `--since` | (none) | Earliest publication date (`YYYY-MM-DD`) |
| `--sort` | `combined` | `combined`, `mostcited`, or `mostrecent` |
| `--download-pdfs / --no-download-pdfs` | on | Download arXiv PDFs |
| `--extract-text / --no-extract-text` | on | Extract text with PyMuPDF |
| `--skip-arxiv` | off | INSPIRE-only search (skip arXiv API; use if rate-limited) |
| `--w-cite` | 0.7 | Citation weight (combined ranking) |
| `--w-recent` | 0.3 | Recency weight (combined ranking) |
| `--out` | `runs/` | Audit log output directory |
| `--data-dir` | `data/` | Root for cached PDFs and text |

## What a run produces

```
runs/{run_id}.json     # Audit trail (query URLs, candidates, downloads, errors)
data/pdfs/{arxiv_id}.pdf
data/text/{arxiv_id}.txt
```

The audit JSON includes the exact INSPIRE and arXiv URLs queried, raw hit counts, ranked candidates with score breakdowns, and per-PDF download/extraction outcomes.

## Architecture

```
CLI (lag-extract search)
  └─ run_search()
       ├─ InspireClient  → INSPIRE-HEP REST API (15 req / 5 s)
       ├─ ArxivClient    → arXiv Atom API (1 req / 3 s)
       ├─ dedup_and_merge (arxiv_id / DOI / title similarity)
       ├─ rank_candidates (log-citation + exponential recency)
       ├─ fetch_pdfs_and_extract (PyMuPDF)
       └─ write_audit_log
```

Both API clients run concurrently via a thread pool. HTTP requests use per-host token-bucket rate limiting and tenacity retries on 429/5xx.

## Python API

```python
from lagrangian_extraction.models import SearchQuery
from lagrangian_extraction.pipeline.search import run_search

audit = run_search(SearchQuery(
    model_name="scalar leptoquark",
    keywords=["BSM", "leptoquark"],
    top_k=10,
))

for paper in audit.candidates:
    print(paper.score, paper.arxiv_id, paper.title)
```

## Testing

```bash
pytest -v
```

Tests use `respx` to mock INSPIRE/arXiv HTTP responses and synthetic PDFs for extraction — no network required.

## Deferred (future stages)

- **Chunking + ChromaDB indexing** — semantic chunk retrieval for Stage 2 extraction
- **LangGraph / LangChain tool wrapper** — HEPTAPOD integration
- **Pydantic extraction schema + Jinja2 `.fr` templates** — Stage 2–3
- **FeynRules / MadGraph validation** — Stage 4
- **LaTeX source bundles** — higher-fidelity term extraction from arXiv source tarballs

## License

Part of the GSoC 2026 ML4SCI / HEPSIM5 project.
