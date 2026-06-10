# Implementation Notes: Bug Fixes, Semantic Search, and Theory vs. Experiment

This document explains how earlier pipeline errors were fixed, how semantic search/ranking works today, and how experimental papers are distinguished from theory papers. It complements [ARCHITECTURE.md](ARCHITECTURE.md) and [HANDOFF.md](../HANDOFF.md).

---

## Table of contents

1. [Previous errors and fixes](#previous-errors-and-fixes)
2. [Semantic search and ranking](#semantic-search-and-ranking)
3. [Theory vs. experimental papers](#theory-vs-experimental-papers)
4. [Quick reference: CLI flags](#quick-reference-cli-flags)

---

## Previous errors and fixes

### 1. INSPIRE returned 0 hits with `--since`

**Symptom**

```text
INSPIRE hits: 0
arXiv hits:   25
```

All candidates came from arXiv only, with `citation_count: 0` and no INSPIRE metadata.

**Cause**

The query builder used invalid INSPIRE date syntax:

```text
date 2015->
```

INSPIRE treats `->` as part of a **closed range** (e.g. `date 2015->2020`), not “from 2015 onward.” A lone `date 2015->` matches nothing.

**Fix** (`clients/inspire.py`)

| Intent | Wrong | Correct |
|--------|-------|---------|
| Papers from year Y onward | `date 2015->` | `date 2015+` |
| Papers up to year Y | — | `date ->2020` |
| Closed range | — | `date 2015->2020` |

After the fix, the same search returns dozens of INSPIRE hits (e.g. ~47 for scalar leptoquark with keywords and `--since 2015-01-01`).

---

### 2. All papers showed 0 citations

**Symptom**

Ranked list had `Cites: 0` for every paper even when INSPIRE had citation data.

**Cause**

- arXiv Atom API does not expose citation counts.
- Many merged records were arXiv-primary; INSPIRE fields were missing unless the paper appeared in the initial INSPIRE search result set.

**Fix** (`pipeline/citations.py`, `clients/inspire.py`)

Post-dedup step **`enrich_inspire_citations()`**:

1. Collect arXiv IDs where `citation_count == 0` or `inspire_id is None`.
2. Batch-query INSPIRE: `eprint 1701.00001 or eprint 2002.12544 or …` (20 IDs per request).
3. Merge back: `citation_count`, `inspire_id`, `subjects`, `abstract`, `published`.

INSPIRE is the **only** citation source used in ranking and the CLI table.

---

### 3. INSPIRE `k keyword` missed abstract matches

**Symptom**

Keyword `leptoquark` in abstract did not match when only `k leptoquark` was used in the API query.

**Cause**

INSPIRE’s `k` field is curated keyword metadata, not full abstract text.

**Fix** (`clients/inspire.py` — `_keyword_match_clause()`)

Per keyword, search across:

```text
(abstracts.value:TERM OR ft TERM OR title TERM OR k TERM)
```

arXiv uses `(ti:TERM OR abs:TERM)` for the same intent.

---

### 4. `subject:Theory-HEP` over-filtered INSPIRE

**Symptom**

Adding `subject:Theory-HEP` to the query collapsed ~47 hits to ~1 for leptoquark searches.

**Cause**

Many phenomenology papers lack that exact INSPIRE subject tag.

**Fix**

Do **not** require `Theory-HEP` in the API query. Instead:

- Exclude experimental subjects at query time: `not subject:Experiment-HEP`, `not subject:Experiment-Nucl`.
- Apply a softer post-filter (`is_theory_paper()` in `filter.py`).

---

### 5. arXiv `ANDNOT` without parentheses broke queries

**Symptom**

Exclude-category clauses produced malformed arXiv query strings.

**Fix** (`clients/arxiv.py`)

Wrap the positive category filter:

```text
(cat:hep-ph ANDNOT cat:hep-ex ANDNOT cat:nucl-ex)
```

Exclude keywords use `ANDNOT (ti:TERM OR abs:TERM)` per term.

---

### 6. Citation-only ranking picked reviews over model papers

**Symptom**

`--sort mostcited` favored TASI lectures and review articles over papers that define a Lagrangian.

**Fix**

Default sort is now **`relevance`** (`rank_for_extraction()` in `pipeline/rank.py`), combining semantic match, Lagrangian heuristics, citations, and recency (see below).

---

### 7. arXiv ID version suffix broke deduplication

**Symptom**

INSPIRE record `1701.00001` and arXiv record `1701.00001v1` were treated as different papers.

**Fix** (`utils.normalize_arxiv_id()`)

Strip trailing `vN` before matching and merging.

---

### 8. INSPIRE year-only dates failed parsing

**Symptom**

`earliest_date: "2015"` caused parse errors or missing `published` dates.

**Fix** (`clients/inspire.py` — `_parse_inspire_date()`)

Accept `YYYY-MM-DD` and bare `YYYY` (mapped to January 1 of that year).

---

## Semantic search and ranking

Semantic features are implemented in **`pipeline/semantic.py`**. This is **not** embedding-based (no ChromaDB or sentence-transformers in Stage 1). It uses **bag-of-words cosine similarity** — lightweight, deterministic, no extra ML dependencies.

### Two roles of “semantic”

| Mode | Flag | What it does |
|------|------|----------------|
| **Search mode** | `--search-mode semantic` | Changes how INSPIRE/arXiv queries are built (free text vs structured title clauses). |
| **Sort mode** | `--sort semantic` | Ranks the merged pool purely by similarity to the query string. |

Default production path uses **`--sort relevance`**, which **includes** semantic similarity as one signal among several.

### Search mode: `keyword` vs `semantic`

**Keyword mode** (default) — structured queries:

| API | Model clause | Keywords |
|-----|--------------|----------|
| INSPIRE | `(title "model" OR abstracts.value:"model" OR ft "model")` | Per-keyword abstract/fulltext/title/`k` OR clauses |
| arXiv | `(ti:"model" OR abs:"model")` | `(ti:kw OR abs:kw)` |

**Semantic mode** — free text:

| API | Model / query |
|-----|----------------|
| INSPIRE | Plain model string (no `title "..."` wrapper) |
| arXiv | `all:"model name keywords"` |

### Similarity function

```python
# pipeline/semantic.py (conceptual)
query_tokens = tokenize(query)      # lowercase [a-z0-9]+
text_tokens  = tokenize(paper_text) # title + abstract + author names
score = dot(query_tokens, text_tokens) / (||query|| * ||text||)
```

- Returns `0.0` if there is no token overlap.
- `build_semantic_query(model_name, keywords)` joins model name and keywords into one string for ranking.

### Sort: `semantic`

`rank_by_semantic()` scores each `PaperRecord`, sorts descending, returns `top_k`. Score breakdown: `semantic_similarity` only.

### Sort: `relevance` (default for extraction)

`rank_for_extraction()` → `compute_extraction_score()` in `pipeline/rank.py`:

| Signal | Weight (default) | Source |
|--------|------------------|--------|
| Semantic similarity | 45% | `semantic_similarity(query, paper_text)` |
| Lagrangian heuristics | 25% | `_lagrangian_signal()` — boosts “lagrangian”, “yukawa”, “coupling”; penalizes “review”, “TASI”, “search for” |
| Citations (log-normalized) | ~20% | INSPIRE `citation_count` |
| Recency | 10% | Exponential decay, 5-year half-life |
| Has arXiv ID | 5% | Needed for PDF download |

### Selection pool

When `top_k=1` (default), the pipeline still fetches and ranks **`selection_pool_size=50`** candidates, then returns the single best paper as `selected_paper`.

### What is *not* implemented yet

- ChromaDB / vector index over PDF chunks (planned Stage 2).
- Embedding models (e.g. sentence-transformers). HANDOFF notes this as an optional upgrade.

---

## Theory vs. experimental papers

Goal: prefer **theory / phenomenology** papers suitable for Lagrangian extraction, and drop **experimental** collider or detector papers.

Filtering uses a **two-layer** design: API query constraints + client-side post-filter.

### Layer 1: API query (`theory_only=True`, default)

**INSPIRE** (`clients/inspire.py`)

```text
not subject:Experiment-HEP
not subject:Experiment-Nucl
```

**arXiv** (`clients/arxiv.py`)

```text
(cat:hep-ph ANDNOT cat:hep-ex ANDNOT cat:nucl-ex)
```

We intentionally **do not** require `subject:Theory-HEP` or `cat:hep-th` only — too many BSM model papers are tagged `hep-ph` without a theory subject.

### Layer 2: Post-filter (`pipeline/filter.py`)

`apply_post_filters()` calls `is_theory_paper()` when `--theory-only` is on (default).

**Reject** if any of:

| Source | Rule |
|--------|------|
| INSPIRE `subjects` | `Experiment-HEP`, `Experiment-Nucl`, `Astrophysics` |
| arXiv `categories` | `hep-ex`, `nucl-ex`, `physics.ins-det`, `physics.acc-ph`, selected astro-ph.* |

**Accept** if any of:

| Source | Rule |
|--------|------|
| INSPIRE `subjects` | Starts with `Theory` (e.g. `Theory-HEP`) |
| arXiv `categories` | `hep-ph`, `hep-th`, `hep-lat`, `gr-qc`, `math-ph`, `nucl-th` |

**Ambiguous metadata** (no categories/subjects): **keep** the record unless it is explicitly experimental. This avoids dropping valid theory papers with incomplete tags.

Constants live in `config.py`: `EXPERIMENTAL_ARXIV_CATEGORIES`, `THEORY_ARXIV_CATEGORIES`, `EXPERIMENTAL_INSPIRE_SUBJECTS`.

### Citation enrichment helps theory filtering

`enrich_inspire_citations()` fills `subjects` from INSPIRE for arXiv-only hits, so `is_theory_paper()` can classify papers that initially lacked INSPIRE metadata.

### Disable theory filter

```bash
lex search "scalar leptoquark" --include-experiment
```

---

## Week 2 additions

### Abstract-focused filter and semantic scoring

- **Filters:** `--require-abstract`, `--abstract-keyword-match`, `--abstract-exclude-only`
- **Semantic scope:** `--semantic-scope {full,abstract,combined}` — token cosine on title+abstract+authors vs abstract-only
- **Relevance breakdown:** `semantic_full`, `semantic_abstract`, plus combined `semantic` term (default 40% full + 60% abstract)

### NASA ADS integration

- Client: `clients/ads.py`
- Requires `ADS_API_TOKEN` (see `.env.example`)
- Merged via `dedup_and_merge()` on arxiv_id / DOI / ads_bibcode
- INSPIRE remains canonical for citations when `inspire_id` is present

### LaTeX source availability

| Source | Author LaTeX? | How |
|--------|---------------|-----|
| arXiv | Yes | `GET https://arxiv.org/src/{arxiv_id}` → gzipped tar or `.tex.gz` |
| INSPIRE | No | Metadata + search-indexed `ft` only |

Probe with `--probe-latex-source` or `scripts/latex_availability_benchmark.py`.

---

## Quick reference: CLI flags

| Flag | Default | Purpose |
|------|---------|---------|
| `--sort relevance` | yes | Semantic + Lagrangian + cites + recency |
| `--sort semantic` | | Pure token cosine ranking |
| `--search-mode keyword` | yes | Title/abstract structured queries |
| `--search-mode semantic` | | Free-text API queries |
| `--theory-only` | yes | Exclude experimental papers |
| `--include-experiment` | | Turn off theory filter |
| `-k` / `--keywords` | | Include keywords (abstract + title) |
| `-K` / `--exclude-keywords` | | Exclude terms (API + post-filter) |
| `--since` / `--until` | | Date range (INSPIRE `date Y+` / range syntax) |
| `--no-download-pdfs` | | Search/rank only |

### Example commands

```bash
# Default: one theory paper, relevance ranking, INSPIRE cites enriched
lex search "scalar leptoquark" -k BSM -k leptoquark --since 2015-01-01

# Pure semantic ranking on merged pool
lex search "scalar leptoquark" -k BSM --search-mode semantic --sort semantic --no-download-pdfs

# Include experimental collider papers
lex search "scalar leptoquark" -k BSM --include-experiment --no-download-pdfs
```

---

## Files touched by these features

| Topic | Primary files |
|-------|----------------|
| INSPIRE date / query syntax | `clients/inspire.py` |
| arXiv query syntax | `clients/arxiv.py` |
| Citation enrichment | `pipeline/citations.py`, `clients/inspire.py` (`lookup_by_arxiv_ids`) |
| Semantic similarity | `pipeline/semantic.py` |
| Relevance ranking | `pipeline/rank.py` |
| Theory filter | `pipeline/filter.py`, `config.py` |
| Orchestration | `pipeline/search.py` |
