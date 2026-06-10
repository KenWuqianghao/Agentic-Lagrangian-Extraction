# Handoff — Lagrangian Extraction Stage 1 (Week 2)

## Goal

Select **one most relevant theory paper** for a BSM model, download its PDF, extract plain text, optionally probe LaTeX source, and prepare an audit trail for Stage 2 Lagrangian extraction.

Repo: https://github.com/KenWuqianghao/Agentic-Lagrangian-Extraction  
Local: `/home/kenwu/Lagrangian_Extraction`

## Current Progress

Stage 1 + **Week 2 enhancements** are implemented and tested (**52 pytest tests**).

### Week 2 features (new)

| Feature | CLI / code |
|---------|------------|
| Abstract-only filters | `--require-abstract`, `--abstract-keyword-match`, `--abstract-exclude-only` |
| Abstract semantic scoring | `--semantic-scope {full,abstract,combined}`; `semantic_abstract` in score breakdown |
| NASA ADS integration | `clients/ads.py`; `--use-ads`; `ADS_API_TOKEN` env var |
| LaTeX source probe | `--probe-latex-source`; `pipeline/sources.py`; `latex_probe` in audit |
| LaTeX benchmark script | `scripts/latex_availability_benchmark.py` |

### Stage 1 features (existing)

| Feature | CLI / code |
|---------|------------|
| Single-paper selection | `--top-k 1` (default), `selected_paper` in audit |
| Relevance ranking | `--sort relevance` (default) |
| Keyword search (title+abstract) | `-k` / `--keywords` |
| Theory-only filter | `--theory-only` (default) |
| INSPIRE citation enrichment | `pipeline/citations.py` |
| Web UI | `lex-web` |

### Key files

```
src/lagrangian_extraction/
  clients/ads.py            # NASA ADS Search API
  pipeline/sources.py       # arXiv LaTeX /src/ probe
  pipeline/semantic.py      # abstract_text(), semantic_similarity_abstract()
  pipeline/filter.py        # abstract-specific post-filters
  pipeline/rank.py          # semantic_full + semantic_abstract in relevance score
  pipeline/search.py        # 3-way parallel fetch (INSPIRE + arXiv + ADS)
scripts/latex_availability_benchmark.py
.env.example                # ADS_API_TOKEN=
```

### LaTeX findings

- **arXiv**: author LaTeX via `https://arxiv.org/src/{arxiv_id}` — use for Stage 2
- **INSPIRE**: no downloadable author TeX; links to arXiv for e-prints

### Verification

```bash
pytest -v
lex search "scalar leptoquark" -k BSM --require-abstract --semantic-scope abstract --no-download-pdfs
ADS_API_TOKEN=... lex search "scalar leptoquark" -k leptoquark --since 2015-01-01 --no-download-pdfs
lex search "scalar leptoquark" -k BSM --probe-latex-source
python scripts/latex_availability_benchmark.py --audit runs/latest.json
```

## Next Steps (Stage 2)

1. Chunk selected paper text (prefer arXiv LaTeX when available)
2. ChromaDB indexing for retrieval-augmented extraction
3. Pydantic extraction schema + constrained LLM prompts
4. Jinja2 `.fr` generation + FeynRules validation
