# Handoff — Lagrangian Extraction Stage 1

## Goal

Select **one most relevant theory paper** for a BSM model, download its PDF, extract plain text, and prepare an audit trail for Stage 2 Lagrangian extraction (LLM + FeynRules).

Repo: https://github.com/KenWuqianghao/Agentic-Lagrangian-Extraction  
Local: `/home/kenwu/Lagrangian_Extraction`

## Current Progress

Stage 1 literature search pipeline is **feature-complete and tested** (33 unit tests + live API checks). **Not yet committed/pushed** — only initial commit on `origin/main`.

### Implemented features

| Feature | CLI / code |
|---------|------------|
| Single-paper selection | `--top-k 1` (default), `selected_paper` in audit |
| Relevance ranking | `--sort relevance` (default): semantic + Lagrangian heuristics + INSPIRE cites |
| Keyword search (title+abstract) | `-k` / `--keywords` |
| Keyword negation | `-K` / `--exclude-keywords` |
| Author search / exclusion | `-a` / `--author`, `-A` / `--exclude-author` |
| Date range | `--since`, `--until` |
| Theory-only filter | `--theory-only` (default) |
| Semantic search/ranking | `--search-mode semantic`, `--sort semantic` |
| INSPIRE citations | Batch lookup by arXiv ID; fixes 0-cite bug |
| Runners-up (optional) | `--runners-up N` |

### Key files

```
src/lagrangian_extraction/
  cli.py                    # lex search command
  clients/inspire.py        # INSPIRE API, query builder, citation lookup
  clients/arxiv.py          # arXiv API, query builder
  pipeline/search.py        # orchestration
  pipeline/rank.py          # combined + rank_for_extraction (relevance)
  pipeline/citations.py     # enrich_inspire_citations()
  pipeline/filter.py        # theory filter, post-filters
  pipeline/semantic.py      # token cosine similarity
  models.py                 # SearchQuery, AuditRun, PaperRecord
```

### Default behavior

```bash
lex search "scalar leptoquark" -k BSM -k leptoquark --since 2015-01-01
```

- Searches ~50-paper pool, ranks with `relevance`, selects 1 paper
- Downloads PDF + extracts text to `data/pdfs/`, `data/text/`
- Writes audit to `runs/{run_id}.json` with `selected_paper`

## What Worked

- **INSPIRE citation enrichment** via `eprint {arxiv_id}` batch lookup — fixes arXiv-only 0-cite records
- **Keyword search in abstract/fulltext** — `(abstracts.value:… OR ft … OR title …)` on INSPIRE; `(ti:… OR abs:…)` on arXiv
- **Theory filter** — exclude `Experiment-HEP/Nucl` in query + post-filter; NOT `subject:Theory-HEP` (too narrow)
- **Relevance ranking** — penalizes reviews/TASI/“search for”; boosts Lagrangian/Yukawa/coupling terms
- **Year-only INSPIRE dates** — `_parse_inspire_date()` handles `"2015"` format

## What Didn't Work

- INSPIRE `k keyword` alone — only matches curated metadata, not abstract
- INSPIRE `subject:Theory-HEP` in query — reduced 47 hits to 1 for leptoquark search
- arXiv `AND ANDNOT` without parens — broke query (fixed with `(cat:hep-ph ANDNOT …)`)
- Raw citation ranking — picked review papers over model-definition papers

## Verification

```bash
pytest -v                                          # 33 passed
lex search "scalar leptoquark" -k BSM -k leptoquark --since 2015-01-01 --no-download-pdfs
lex search "squark" -k sugra --since 2015-01-01 --no-download-pdfs   # ~47 papers
lex search "squark" -k sugra -K MSSM -K GAMBIT --since 2015-01-01 --no-download-pdfs  # ~13 papers
lex search "leptoquark" --author Crivellin --since 2015-01-01 --no-download-pdfs
```

## Next Steps

1. **Commit and push** all local changes to GitHub (user has not requested yet)
2. **Stage 2**: Chunk selected paper text, index in ChromaDB, LLM extraction of Lagrangian terms
3. **Optional improvements**:
   - Embedding-based semantic search (replace token cosine)
   - LaTeX source download for higher-fidelity extraction
   - `--runners-up` in default output for debugging selection

## Git state

```
Branch: main (tracks origin/main)
Uncommitted: 12 modified + 6 new files (~665 insertions)
Remote: only initial commit pushed
```
