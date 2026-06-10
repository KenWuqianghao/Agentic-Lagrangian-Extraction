# Lagrangian Extraction — Stage 1 Literature Search

Stage 1 of the HEPSIM5 agentic pipeline: search **INSPIRE-HEP**, **arXiv**, and **NASA ADS** for BSM model papers, filter and rank candidates (with abstract-focused semantic scoring), download PDFs from arXiv, extract plain text, optionally probe LaTeX source availability, and write a reproducible audit trail.

## Quickstart

```bash
uv venv .venv && source .venv/bin/activate
uv pip install -e ".[dev,web]"

# Copy and fill in your ADS token (optional but recommended)
cp .env.example .env

# Default: select one theory paper with relevance ranking
lex search "scalar leptoquark" -k BSM -k leptoquark --since 2015-01-01

# Abstract-focused search and ranking
lex search "scalar leptoquark" -k BSM \
  --require-abstract --abstract-keyword-match \
  --semantic-scope abstract --no-download-pdfs

# Probe LaTeX source for the selected paper
lex search "scalar leptoquark" -k BSM --probe-latex-source
```

### Key CLI flags

| Flag | Default | Description |
|------|---------|-------------|
| `-k` / `--keywords` | (none) | Include keywords (title + abstract) |
| `-K` / `--exclude-keywords` | (none) | Exclude keywords |
| `--sort` | `relevance` | `relevance`, `combined`, `mostcited`, `mostrecent`, `semantic` |
| `--semantic-scope` | `combined` | `full`, `abstract`, or `combined` token-cosine scoring |
| `--require-abstract` | off | Drop papers without a long abstract |
| `--abstract-keyword-match` | off | Require include-keywords in abstract |
| `--use-ads / --no-ads` | on | Include NASA ADS (needs `ADS_API_TOKEN`) |
| `--probe-latex-source` | off | Check arXiv `/src/` LaTeX availability |
| `--theory-only` | on | Exclude experimental papers |

### ADS setup

1. Create an account at [ui.adsabs.harvard.edu](https://ui.adsabs.harvard.edu)
2. Generate a token at Settings → API Token
3. Export `ADS_API_TOKEN=...` or add to `.env`

If no token is set, ADS is skipped with a warning in the audit log.

## What a run produces

```
runs/{run_id}.json       # Audit trail (selected paper, score breakdown, latex_probe)
data/pdfs/{arxiv_id}.pdf
data/text/{arxiv_id}.txt
data/src/{arxiv_id}/     # Cached main .tex when --probe-latex-source
```

## Architecture

```
CLI / lex-web
  └─ run_search()
       ├─ InspireClient  → INSPIRE-HEP REST API
       ├─ ArxivClient    → arXiv Atom API
       ├─ AdsClient      → NASA ADS Search API (Bearer token)
       ├─ dedup_and_merge (arxiv_id / DOI / bibcode / title)
       ├─ enrich_inspire_citations()
       ├─ apply_post_filters()  # theory, abstract, keywords, dates
       ├─ rank_for_extraction() # semantic_full + semantic_abstract + Lagrangian heuristics
       ├─ fetch_pdfs_and_extract (PyMuPDF)
       ├─ probe_arxiv_source()  # optional LaTeX /src/ probe
       └─ write_audit_log
```

## LaTeX source investigation

| Source | Author LaTeX available? |
|--------|-------------------------|
| **arXiv** | Yes — `https://arxiv.org/src/{arxiv_id}` (gzipped tar or single `.tex.gz`) |
| **INSPIRE** | No — metadata and indexed full-text only; no downloadable TeX |

Benchmark availability on a prior audit run:

```bash
python scripts/latex_availability_benchmark.py --audit runs/{run_id}.json
```

## Web UI

```bash
lex-web
# Open http://127.0.0.1:8000
```

## Testing

```bash
pytest -v   # 52 tests, mocked HTTP
```

## Deferred (Stage 2+)

- Chunking + ChromaDB indexing
- Embedding-based semantic search
- LLM Lagrangian extraction + Jinja2 `.fr` templates
- FeynRules / MadGraph validation

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) and [docs/IMPLEMENTATION_NOTES.md](docs/IMPLEMENTATION_NOTES.md) for details.
