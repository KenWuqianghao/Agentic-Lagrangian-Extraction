# Loop benchmark results — 28 FeynRules-DB models

> **Correction, 2026-09-13.** Every FeynRules check verdict and every full-chain number in this document was measured with a classifier that could not report a failure, and some runs counted the Standard Model Lagrangian twice. [CORRECTION_2026-09-13.md](CORRECTION_2026-09-13.md) has the re-scored numbers. Field-content scores and the physicist-finding checks read the `.fr` text and are not affected.

Evidence for the heptapod PR
[tonymenzo/heptapod#23](https://github.com/tonymenzo/heptapod/pull/23). The
tools live in that PR. The measurements live here, because 577 files of
benchmark output do not belong in a tools merge request.

## What was measured

Each of 28 published BSM models from the FeynRules model database was
re-derived from its own paper by an agent, then pushed through the full
validation chain:

```
paper -> .fr -> FeynRules/Wolfram UFO compile
             -> Hermiticity / kinetic-term / mass-spectrum checks
             -> MadGraph import
```

A model counts as passing only if every stage accepts it.

Failing models then entered a closed repair loop: re-validate, hand an
**isolated** repair agent the real tool output (no network, no reference
files, no model name), re-validate, up to 3 rounds. Three phases ran, each
adding better diagnostics rather than a better agent.

## Headline

With the corrected checks, **9 of the 19 scoreable models** pass the full
chain with their best `.fr`, repaired or one-shot. Before the correction this
set was reported as 18 of 19. Full chain means the model compiles, all four
default FeynRules checks pass, and MadGraph imports the UFO. The ten new
failures are Hermiticity, kinetic-term, mass-term or mass-spectrum failures
that the old classifier could not report. `CORRECTION_2026-09-13.md` lists
each one.

The repair-loop funnel below is kept as history. Its numbers are **invalid**,
because the loop only saw a check fail when the check crashed.

| stage | passing, as reported | rate |
|---|---:|---:|
| one-shot | 15/28 | 54% |
| + repair phase 1 | 20/28 | 71% |
| + repair phase 2 | 24/28 | 86% |
| + repair phase 3 | 25/28 | 89% |

One conclusion survives, because it does not depend on the checks. On
UFO-serialization defects, which MadGraph reports, the agent scored 0/5
while blind; once the harness pinpointed the offending file and line, the
same class became routine.

Full analysis: [`REPAIR_BENCHMARK_ANALYSIS.md`](REPAIR_BENCHMARK_ANALYSIS.md).

## What passing does and does not mean

Passing means **the tool chain accepts the model**. It does not mean the
physics matches the paper.

That is tested separately. For each passing model, an agent that never saw
the paper reconstructed the physics from the sanitized `.fr` alone, and a
second fresh agent graded that reconstruction against the paper term by
term. Those graded rows are collected in
[`CONVENTION_DISAGREEMENTS.md`](CONVENTION_DISAGREEMENTS.md):

| grade | rows | meaning |
|---|---:|---|
| convention | 45 | probably the same physics written differently |
| substantive | 79 | a real difference in content — read these |
| cosmetic | 13 | presentation only |

**These grades come from an agent, not a physicist. They are the question
list, not the answer.**

Four of the 25 review packages have no cross-check, because the reverse run
hit agent-transport failures rather than a physics result. They are listed
in `CONVENTION_DISAGREEMENTS.md` and should be treated as not yet reviewed.

## Layout

```
<model>/
  model/       the agent-generated .fr
  repair*/     per-round repair attempts, diffs and logs
  review/      sanitized.fr, reconstruction.md, crosscheck.md, REVIEW.pdf
  text/        paper source (untracked; re-fetch with db_run_prep.py)

validation_benchmark_report.{json,md}     one-shot chain results
repair_benchmark_report.md                phase 1
repair_benchmark_phase2_report.md         phase 2
repair_benchmark_phase3_report.md         phase 3
REPAIR_BENCHMARK_ANALYSIS.md              full write-up and error taxonomy
CONVENTION_DISAGREEMENTS.md               graded reconstruction-vs-paper rows
collect_disagreements.py                  regenerates the two files above
ian_review_bundle/                        per-model .fr + REVIEW.pdf, for review
```

## Reproducing

The harness scripts are here (`validation_benchmark.py`,
`repair_benchmark.py`, `repair_summary.py`). They need a configured
FeynRules + Wolfram Engine + MadGraph install, and an agent CLI for the
repair and reverse stages.

```bash
python collect_disagreements.py     # no external software needed
```

### Sandboxed reruns and the no-tools ablation (2026-09)

`FINDINGS_2026-09.md` is the entry point: what the physicists reported, what
caused each defect, what changed, and how it was measured.

| file | what it does |
|---|---|
| `rerun_extract.py` | runs one arm: sandboxed agent, `tools` or `notools` engine mode, LaTeX or PDF-text paper source, then render, validate, score |
| `prompt_addendum_v3.txt` | the physics and FeynRules-construct rules appended to the extraction prompt |
| `rerun_predicates.py` | one deterministic check per reported finding, written against the construct rather than symbol names |
| `test_rerun_predicates.py` | 29 unit test cases for those checks, including the reference file and the reviewed file |
| `single_model_select.py` | turns the paper classification into `single_model_papers.{json,md}`: which papers define exactly one model, and which reference pairings are broken |
| `subagent_bench.py` | drives the agent stage from an interactive Claude Code session when the headless CLI is not logged in |
| `ablation_report.py` | the per-finding, per-run and per-variant comparison across arms |
| `run_ablation.sh` | runs every arm end to end and writes the report |

They run from the heptapod checkout, where the tools and paper texts live;
this directory mirrors the scripts and the results.
`ablation_report_v1v2.md` is the v1-vs-v2 baseline on the four reviewed models.

### Check-verdict correction (2026-09-13)

Every FeynRules check verdict before 2026-09-13 came from a classifier that
could not report a failure, and some runs counted the Standard Model
Lagrangian twice. `CORRECTION_2026-09-13.md` is the entry point. The harness
now reads verdicts from each check's return value, through the generator and
`tools/feynrules/lagrangian_checks.py` on heptapod `main`.

| file | what it does |
|---|---|
| `rescore_checks.py` | re-runs only the consistency checks (`ChecksOnly=true`) on each stored run's `.fr`, rewrites its verdicts and full-chain result, and logs the old values to a ledger; resumable |
| `correction_report.py` | builds `CORRECTION_2026-09-13.{md,json}` from the ledger alone |
| `rescore_ledger_2026-09-13.jsonl` | one line per re-scored run: old verdicts, new verdicts, the Lagrangian expression used |
| `test_validation_benchmark.py` | unit tests for when the checks count as passing and when `LSM` is added |

```bash
python correction_report.py --ledger rescore_ledger_2026-09-13.jsonl
```

## Caveats

- The repair agent is isolated, but the underlying model may have seen these
  public model files in training.
- Repairs that replace symbolic values with numerics preserve tool-chain
  validity while narrowing the model's parameter generality. They are
  flagged in the analysis.
- Three models remain unfixed: `ALRM_general`, `HNLs`, `SLQrules`. The
  analysis explains why each resisted repair.
