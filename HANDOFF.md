# Handoff — Agentic Lagrangian Extraction

Written 2026-09-06 for a switch in dev assistant (Claude Code → Grok Bot).
This file is the one durable record of project state that lived only in
Claude's memory before now. Read it before making changes.

## What this repo is

Stage 1 of the HEPSIM5 agentic pipeline (a GSoC project): search
INSPIRE-HEP and arXiv for BSM (Beyond Standard Model) physics papers, rank
candidates, download and extract text, and hand a paper's content to a
downstream pipeline that writes a FeynRules `.fr` model file and validates
it through FeynRules → UFO → MadGraph.

This repo (`Agentic-Lagrangian-Extraction`) holds the literature-search
stage and the benchmark/validation harness. The actual extraction pipeline
and the FeynRules validation code live in a sibling repo, **heptapod**, at
`~/Documents/Github/heptapod` (path is hardcoded in
`benchmarks/agent_bench/drivers.py`). You need both repos checked out at
that relative location for the benchmarks to run.

A third sibling repo, **aster** (`~/Documents/Github/aster`,
github.com/emipanek/aster), holds an unrelated exoplanet-research toolkit
that used to live in heptapod. It moved out on 2026-08-26. Its own
`CLAUDE.md` still names Claude Code explicitly — rename it or add an
`AGENTS.md` copy before pointing Grok Bot at it.

## Repo conventions

- **Hard cutover, no backward compatibility.** When changing an interface,
  change all callers. Don't add compat shims, deprecated aliases, or
  feature flags for old behavior.
- **No speculative abstraction.** A one-shot script doesn't need a
  framework. Three similar lines beats a premature helper.
- **`config.py` is small and secret-free by design.** It holds only
  dataclass defaults (timeouts, retry counts, rate limits) — see
  `src/lagrangian_extraction/config.py`. Nothing in this repo's config
  carries an API key. If you add one, put it in an environment variable,
  never a literal, and never print it in logs or commit messages.
- **The CLI binary is `lag-extract`, not `lex`** — macOS ships
  `/usr/bin/lex` (the flex lexer) which shadows a package named `lex`
  when it's not installed. This was already renamed once; don't revert it.

## Current state (as of the last commit, `1253db5` on
`benchmarks/loop-results`)

### Literature search (this repo, `src/`)
Working: INSPIRE + arXiv search, dedup/rank by citation + recency, PDF
download, PyMuPDF text extraction, audit trail under `runs/`. Recently
fixed: arXiv 429 rate-limit handling now honors `Retry-After` and uses a
configurable retry count (`HttpConfig.max_retries`, default raised 3→5)
instead of a fixed 3 attempts — see `src/lagrangian_extraction/clients/_http.py`.

### FeynRules validation chain (heptapod repo, exercised from
`benchmarks/`)
The chain is FeynRules `.fr` → UFO → MadGraph 3.7.3 import. As of the last
full sandboxed rerun:

- **Fleet of 28 benchmark models**: 11/28 pass the full chain end to end,
  21/28 compile to UFO (some stop at MadGraph import).
- **Repair loop** (an agent given a failing model + error log, asked to
  fix it): lifts full-chain pass rate 15/28 → 25/28 over 3 rounds. See
  memory note `repair-loop-benchmark` — no local equivalent file yet;
  fold this into a repo doc if Grok Bot needs the failure taxonomy.
- **Every failure classified is a construct problem, not a physics
  error** — the physics content of the generated `.fr` files is usually
  right; the renderer emits FeynRules syntax that doesn't compile or
  MadGraph rejects. Known failure classes, all traced to a specific
  construct:
  - No `InteractionOrder` declared → UFO couplings default to order `'1'`,
    MadGraph rejects.
  - Pattern-rule `Definitions` applied to a tensor-valued parameter →
    UFO parameter serializes as a literal string like `YN1x1 /. YN`.
  - Explicit numeric indices where FeynRules expects matrix form
    (e.g. `DC[Psiu[ss],mu]`, `VCKMR[ff1,ff2] uqbar[ff1,cc]…`) → UFO
    writer leaks internal helper calls (`ConvertSpinToString[0]`,
    `MakeIdenticalFermions`) into the output.
  - **Sextet stall** (diagnosed this session): an explicit sextet color
    index inside `DC[]` with no matching `AddGaugeRepresentation` produces
    garbage gluon–sextet vertices that violate charge/hypercharge. This
    doesn't fail fast — FeynRules' Hermiticity check hangs on it. A longer
    timeout does not help; a 60-minute retry on the two affected files
    (368sextets v1/s2, v2/s2) still stalled, with `Part::pkspec1` errors
    and non-Hermitian vertices including `{G, Phiu}` in the log.
  - Also seen: particle names with primes (`W'+`, invalid as a Python
    identifier in the UFO writer), field-free constant terms producing a
    vertex with no particles, FeynRules `$RecursionLimit` crashes on two
    models (Monotops, SLQrules — not yet root-caused), and ambiguous total
    Lagrangians where the renderer emits `LTotal :=` in only some files,
    leaving the harness to guess which root is total.
- **Harness bug, not yet fixed**: `compile_to_ufo` in
  `eval/benchmark_runs/validation_benchmark.py` (heptapod repo) uses
  `subprocess.communicate(timeout=...)`, which is wall-clock on Linux but
  effectively monotonic-vs-wall-mismatched under macOS sleep — a sleeping
  laptop once stretched a 3600s budget to 17471s. Needs a real wall-clock
  watchdog (e.g. `caffeinate` wrapper, or checking `time.monotonic()`
  against elapsed real time explicitly).
- **Wolfram Engine activation lapsed** since 2026-09-02. Every FeynRules
  compile will fail with an activation notice until someone runs
  `wolframscript -activate` interactively on the machine running the
  benchmarks. This requires a human at the keyboard — it is a licensing
  prompt, not something an agent should attempt to script around.

### Model-agnostic agent benchmark (`benchmarks/agent_bench/`)
A harness to compare AI coding agents (not just models) driving the
heptapod MCP toolkit on fixed, deterministically-scored cases — never
scored by asking the model if it succeeded (`run.py` docstring is explicit
about this). Structure:
- `drivers.py` — one `Driver` subclass per harness (CLI or SDK), single
  signature `run(case, workdir, model) -> Trace`. Only `ClaudeCodeDriver`
  is implemented against a real CLI today. `CodexDriver` and
  `OrchestralDriver` are declared but return `unavailable` (no credentials
  / not implemented) so a run reports why a model is missing instead of
  silently comparing against nothing.
- `trace.py` — a harness-neutral event schema (`agent-bench-trace-1.0`):
  tool calls, shell commands, messages, errors. Each driver's raw output
  (Claude's `stream-json`, a shared toolbase log, Codex's own event
  format) gets parsed into this schema so cases score identically
  regardless of which agent ran them.
- **To add Grok Bot as a benchmarked model**: write one `Driver` subclass
  in `drivers.py` (see `ClaudeCodeDriver` for the shape: check
  availability, build the command, capture stdout, hand it to a new
  `from_grok_*` parser in `trace.py`), then register it in the `DRIVERS`
  dict at the bottom of `drivers.py`. Do not confuse `GROQ_API_KEY`
  (Groq, the inference company, already referenced in
  `OrchestralDriver`) with Grok (xAI) — these are unrelated and the name
  collision has caused confusion before.

### Ian's four-findings review (this week's deliverable, in `benchmarks/`)
A physicist (Ian) flagged four defects across four benchmark models. 3/4
were confirmed real; 1 was a misread of an already-correct file. Separately,
an audit of the *original* (non-sandboxed) agent runs found 18/28 had read
their own reference answer file during generation — a contamination bug in
the original benchmark setup, unrelated to the models' actual capability.
Sandboxed reruns (agent cannot see the reference) resolved 15/16 of the
findings. Reference materials, in case they're needed for a follow-up:
`benchmarks/ian_four_findings.html` (presentation deck), `ian_rerun_email.md`
(email draft to Ian, not yet sent), `contamination_audit.py`/`.json`,
`rerun_extract.py`, `rerun_predicates.py`, `rerun_score.py`, and per-model
results under `benchmarks/<model>/rerun/`.

## Cross-repo state Grok Bot should know about

- **heptapod has a dirty working tree** (branch `feature/lagrangian-extraction`,
  53 uncommitted files as of this handoff) mixing an exoplanet-tools
  deletion (superseded by the aster migration) with unrelated
  in-progress literature work. Separate these before committing — don't
  commit them together.
- **heptapod has an open PR stack**: PR #11 was split into #11 → #14 → #15
  → #16 on 2026-09-02, with worktrees under `~/Documents/Github/hep-pr`.
  Merge in that order.
- **aster PR #3** (emipanek/aster, branch `measurements-bundle`) is open,
  ships the exoplanet bundle migrated out of heptapod. License is TBD —
  aster has no LICENSE file yet; that's Emilie Panek's call, not ours.

## Repo hygiene fixed in this handoff's commit

- Added `.DS_Store` and a stray generated file (`py.py`, a PLY parser
  table accidentally written to the repo root by some tool run from the
  wrong cwd) to `.gitignore`. Neither was tracked; if `py.py` reappears,
  find what generates it and fix its output directory rather than
  re-ignoring it repeatedly.
- `AGENTS.md` and `CLAUDE.md` in this repo are identical, GitNexus-authored
  files describing code-intelligence tooling (a knowledge-graph MCP
  server). Both are now committed. If Grok Bot has no equivalent MCP
  tool, the file degrades gracefully — it also documents a CLI fallback
  (`node .gitnexus/run.cjs ...`) for every command it recommends.

## What's NOT done

- Renderer lints proposed but not implemented: reject pattern-rule
  `Definitions` on tensor parameters, require `InteractionOrder` on every
  vertex, reject identifier-invalid particle names, drop field-free
  constant terms, require `AddGaugeRepresentation` whenever an explicit
  gauge index appears in `DC[]`, require exactly one declared total
  Lagrangian.
- Harness fixes proposed but not implemented: wall-clock compile
  watchdog, stall detection (vs. hard timeout) for the sextet class of
  failure.
- Root cause not yet found: the `$RecursionLimit` crashes in Monotops and
  SLQrules, and the nested-index construct in GeneralU1's original defect.
- `lag_overrides.json` (in heptapod) is reserved for a physicist to set
  ground-truth override values — it is intentionally all-null right now.
  Do not populate it programmatically; that decision belongs to a
  physicist, not an agent.

## Update 2026-09-09 — physicist round 2, v3 harness, no-tools ablation

Ian and Konstantin sent one more finding on EffLRSM: the overall Z_R
coupling (paper arXiv:1610.08985 Eq. 8) is `-kappa g / sqrt(1 - tan^2/kappa^2)`;
the reviewed file (and the crosscheck that graded it "agree") put the root in
the numerator, so every Z_R rate is low by a factor 0.49. Root cause: the
PDF-extracted paper text flattens `\frac{num}{\sqrt{den}}` into three lines.
One sandboxed rerun (v1/s1) repeated the slip; v2/s1 noticed the split
fraction and recovered it from the width formula.

What changed (heptapod `eval/benchmark_runs/`, mirrored here in `benchmarks/`):

- Every benchmark paper now has its LaTeX source at
  `<page>/text/<id>_source.tex` (fetched with heptapod's ArxivSourceTool;
  manifest `latex_sources.json`). `rerun_extract.py --paper-source tex|txt`.
- `rerun_extract.py --engine-mode tools|notools`. `notools` is the ablation
  arm: `claude -p --tools ''`, SM.fr and the paper inlined in the prompt, the
  agent writes the whole `.fr` in one fenced block, no schema, no renderer.
  Both arms run with `--setting-sources ''` so the operator's CLAUDE.md and
  settings never reach the benchmarked agent.
- `prompt_addendum_v3.txt`: v2 rules plus fraction/root reading (LaTeX
  first, else cross-check a width or cross-section equation), mass mixing,
  and the FeynRules/UFO construct rules every earlier compile failure traced
  to (AddGaugeRepresentation for sextets, no Protected/SM names, class index
  >= 100, InteractionOrder on every coupling, explicit tensor values,
  matrix-form flavour couplings, one LTotal, no field-free terms).
- `rerun_predicates.py`: two new predicates, `efflrsm_zr_normalisation`
  (root must divide) and `sextets_gauge_representation` (all four earlier
  sextet reruns fail it: no gluon coupling).
- `ablation_report.py`: per-finding x variant table, per-run chain table,
  aggregate per variant, field-F1 against the DB reference. Baseline on the
  four Ian models, v1 vs v2 (txt, tools): `ablation_report_v1v2.md`.
- `run_ablation.sh`: runs arms `v3_tools`, `v3_notools`, `v3txt_tools`
  (the last isolates the paper-source effect), scores and reports.
  `PAGES=single` selects the papers that define exactly one model
  (`single_model_papers.json`, classified by reader + two adversarial
  refuters per paper) plus Ian's four.
- `validation_benchmark.compile_to_ufo` has the wall-clock watchdog the
  earlier handoff asked for.

Blocked: the headless `claude` CLI on this Mac is logged out
(`claude auth status` -> `loggedIn: false`, "OAuth session expired"). Every
real agent run fails in 0 s until a human runs `claude login` in a terminal.
The harness was dry-run end to end with a stub engine (both modes render,
predicates and the full FeynRules -> UFO -> MadGraph chain pass on a
known-good file). Then:

```bash
cd ~/Documents/Github/heptapod
PAGES=single SEEDS=2 eval/benchmark_runs/run_ablation.sh
```

Never call `timeout` (or any missing binary) from a shell on this Mac: the
zsh `command_not_found_handler` recurses into `pacman` and fork-storms the
per-user process limit.

## The heptapod PR stack, 2026-09-09: rebased locally, needs one push

PR #11 was `CONFLICTING` against `dev/main`, so Tony could not merge it. The
whole four-PR stack has been rebased onto current `dev/main` (`36cd1e9`) in a
worktree and verified, but the force-push was blocked by this environment's
permission classifier, so it is the one step left for a human.

Verified before the push was attempted:

- Every slice's own files are byte-identical to the pre-rebase tip, and the
  per-PR file counts are unchanged at 17 / 15 / 24 / 19.
- Three conflicts were resolved by union merge (`.gitignore`, `tools/README.md`,
  `toolkit.yaml`) and the `--only` choices list in `test_runner.py` was merged
  so that both main's bundles (`wolfram`, `llp`) and the stack's (`frgen`,
  `extract`, `validate`, `jobs`, `reverse`) survive.
- `main` and the stack each added a way to detect pytest-style suites and
  neither subsumes the other, so both are kept and the merged code says why.
- Suites pass on the rebased tip: literature, frgen, extract, validate, jobs,
  logging, reverse, inspire, plus the worked example. `feynrules` was not
  cleanly measured — every attempt so far ran beside a benchmark compile, and
  the two contend for the Wolfram kernel. Run it on an idle machine.
- No secrets and no stray artifacts in the stack's 58 files.

To finish, from a checkout with the `dev` remote:

```bash
git push --force-with-lease=refs/heads/feat/lagrangian-tools-dev:46c499f54fb20609b81b875f38c26a9bf6769dce dev rb/s1:refs/heads/feat/lagrangian-tools-dev
git push --force-with-lease=refs/heads/lagrangian/2-frgen-extract:9fa44afb33bf671ca9009a73fb97a1a1a8a2cd47 dev rb/s2:refs/heads/lagrangian/2-frgen-extract
git push --force-with-lease=refs/heads/lagrangian/3-validate-jobs-logging:9cddfd7fbc9b1b9f84bf5ec153b347f44016f37c dev rb/s3:refs/heads/lagrangian/3-validate-jobs-logging
git push --force-with-lease=refs/heads/lagrangian/4-reverse:2e835b5e99dbfbf6cdd32a4b4bfb86303cedf4f4 dev rb/s4:refs/heads/lagrangian/4-reverse
```

The rebased branches are local refs `rb/s1` .. `rb/s4` in the heptapod clone.
To undo, force-push the pre-rebase SHA named in each `--force-with-lease`
above back to its branch; the pre-rebase tips also survive as
`lagrangian/s1-tmp` .. `s4-tmp`.

The four PR descriptions have already been updated with an Evidence section
pointing at `benchmarks/FINDINGS_2026-09.md` in this repo. The bases are
unchanged, so the stack structure survives the push.
