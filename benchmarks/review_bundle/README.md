# Review bundle — agent-extracted FeynRules models

28 published BSM models from the FeynRules model database were re-derived from their own papers by an agent, then pushed through the full validation chain: FeynRules/Wolfram UFO compile, Hermiticity / kinetic-term / mass-spectrum checks, MadGraph import. Models that failed entered a closed repair loop.

| stage | passing | rate |
|---|---:|---:|
| one-shot | 15/28 | 54% |
| + repair phase 1 | 20/28 | 71% |
| + repair phase 2 | 24/28 | 86% |
| **+ repair phase 3** | **25/28** | **89%** |

## Read this first

**The pass rate above overstates coverage for 9 of the 25 passing models.** The harness picks each model's total-Lagrangian symbol by file position — the last `L... =` line — and for those 9 that symbol is not the model's total, so FeynRules compiled a fragment. A fragment can be Hermitian, pass every check and import into MadGraph. `VLQ` passed on 1 of its 11 Lagrangian terms; `topBSM` on 5 of 23; `331` on 2 of 5.

This is our bug, not a defect in the models, and it is unfixed as of this bundle. `LAGRANGIAN_COVERAGE.md` lists every affected model and what was omitted. Please weigh the pass rate accordingly.

## What we are asking you to check

Passing means **the tool chain accepts the model**. It does not mean the physics matches the paper, and we are not claiming it does.

To test the physics we ran the chain backwards. For each passing model, an agent that never saw the paper reconstructed the Lagrangian from the sanitized `.fr` alone. A second fresh agent then compared that reconstruction against the paper term by term and graded every difference.

**Those grades come from an agent, not a physicist. They are the question list, not the answer.** That is what your sign-off is for.

| grade | rows | meaning |
|---|---:|---|
| convention | 45 | probably the same physics written differently |
| substantive | 79 | a real difference in content — these are the ones worth your time |
| cosmetic | 13 | presentation only |

## Reading order

1. `LAGRANGIAN_COVERAGE.md` — which models were only partly compiled, and what was left out. This bounds what the rest means.
2. `CONVENTION_DISAGREEMENTS.md` — every graded row, grouped by theme. Start with the substantive ones.
3. `passing/<model>/REVIEW.pdf` — the full review package for any model whose rows you want to see in context. The last page is a sign-off block.
4. `REPAIR_BENCHMARK_ANALYSIS.md` — what the loop fixed, what it could not, and the error taxonomy.
5. `reports/` — the machine-generated per-stage results.
6. `failing/` — the three models the loop could not repair.

## Contents

### passing/ (25 models)

`<model>.fr` is the validated FeynRules file, agent-extracted and, where the loop repaired it, self-repaired with no human input. **Every model has exactly one PDF — open that and you have everything.**

`REVIEW.pdf` is a completed reverse-check package: verbatim Lagrangian terms, the blank-slate reconstruction, the term-by-term paper comparison, and a sign-off block. `DOSSIER.pdf` appears where the reverse run did not finish — it carries the verbatim Lagrangian, whatever reconstruction exists, the validation result and the repair history, so the model is still readable without opening source files.

| model | PDF | pages | state |
|---|---|---:|---|
| 331 | `DOSSIER.pdf` | 6 | reverse run unfinished — **not yet reviewed** |
| 368sextets | `REVIEW.pdf` | 8 | full term-by-term cross-check |
| B-L-SM | `DOSSIER.pdf` | 6 | reverse run unfinished — **not yet reviewed** |
| CHEIDI | `DOSSIER.pdf` | 10 | reverse run unfinished — **not yet reviewed** |
| ChernSimonsPortal | `REVIEW.pdf` | 7 | full term-by-term cross-check |
| DMsimp | `REVIEW.pdf` | 8 | full term-by-term cross-check |
| EffLRSM | `REVIEW.pdf` | 8 | full term-by-term cross-check |
| GeneralU1 | `REVIEW.pdf` | 9 | full term-by-term cross-check |
| HeavyN | `REVIEW.pdf` | 9 | full term-by-term cross-check |
| HiggsCharacterisation | `REVIEW.pdf` | 14 | full term-by-term cross-check |
| LeptoQuark | `REVIEW.pdf` | 9 | full term-by-term cross-check |
| MDMmodel | `REVIEW.pdf` | 8 | full term-by-term cross-check |
| MSSMD | `REVIEW.pdf` | 8 | full term-by-term cross-check |
| Monotops | `REVIEW.pdf` | 8 | full term-by-term cross-check |
| NJLComposite | `REVIEW.pdf` | 9 | full term-by-term cross-check |
| SMWeinberg | `REVIEW.pdf` | 9 | full term-by-term cross-check |
| Sextets | `REVIEW.pdf` | 9 | full term-by-term cross-check |
| Top-Philic-Zprime | `REVIEW.pdf` | 7 | full term-by-term cross-check |
| Triplets | `REVIEW.pdf` | 7 | full term-by-term cross-check |
| VLC_LN | `DOSSIER.pdf` | 7 | reverse run unfinished — **not yet reviewed** |
| VLQ | `REVIEW.pdf` | 10 | full term-by-term cross-check |
| Wprime | `REVIEW.pdf` | 8 | full term-by-term cross-check |
| pNG | `REVIEW.pdf` | 8 | full term-by-term cross-check |
| pSPSS | `REVIEW.pdf` | 9 | full term-by-term cross-check |
| topBSM | `REVIEW.pdf` | 15 | full term-by-term cross-check |

4 of these have no cross-check. Their reverse runs hit agent-transport failures, not a physics result. Treat them as not yet reviewed — their `DOSSIER.pdf` says so on page 1.

### failing/ (3 models)

The loop could not get these through the chain. Included so the picture is complete, not only the successes. Read `DOSSIER.pdf`; `<model>_one_shot.fr` is the first attempt, `<model>.fr` the best repaired attempt, and `VALIDATION_REPORT.md` the failure it stopped on.

| model | best attempt | why it resisted |
|---|---|---|
| ALRM_general | repair3/round3 | multi-member `ClassMembers` scalar classes serialize to invalid UFO Python; restructuring re-breaks or times out the compile |
| HNLs | repair3/round3 | layered semantic UFO leaks; each was fixed once named, but the stack outlasted the round budget |
| SLQrules | repair3/round3 | residual SU(2)-multiplet covariant-derivative Hermiticity violation — genuinely hard physics, not a tooling gap |

## Caveats

- The repair agent ran isolated (no network, no reference files, no model name), but the underlying model may have seen these public model files in training.
- Repairs that replaced symbolic values with numerics keep the tool chain valid while narrowing the model's parameter generality. The analysis flags them.
- Symbol names survive sanitizing on purpose, so the blank-slate agent was not perfectly blind.
