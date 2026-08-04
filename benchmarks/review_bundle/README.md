# Review bundle — agent-extracted FeynRules models

28 published BSM models from the FeynRules model database were re-derived from their own papers by an agent, then pushed through the full validation chain: FeynRules/Wolfram UFO compile, Hermiticity / kinetic-term / mass-spectrum checks, MadGraph import. Models that failed entered a closed repair loop.

| stage | passing | rate |
|---|---:|---:|
| one-shot | 15/28 | 54% |
| + repair phase 1 | 20/28 | 71% |
| + repair phase 2 | 24/28 | 86% |
| **+ repair phase 3** | **25/28** | **89%** |

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

1. `CONVENTION_DISAGREEMENTS.md` — every graded row, grouped by theme. Start with the substantive ones.
2. `passing/<model>/REVIEW.pdf` — the full review package for any model whose rows you want to see in context. The last page is a sign-off block.
3. `REPAIR_BENCHMARK_ANALYSIS.md` — what the loop fixed, what it could not, and the error taxonomy.
4. `reports/` — the machine-generated per-stage results.
5. `failing/` — the three models the loop could not repair.

## Contents

### passing/ (25 models)

`<model>.fr` is the validated FeynRules file, agent-extracted and, where the loop repaired it, self-repaired with no human input. `REVIEW.pdf` is the blank-slate review package.

| model | review |
|---|---|
| 331 | reconstruction incomplete — **not yet reviewed** |
| 368sextets | full term-by-term cross-check |
| B-L-SM | reconstruction incomplete — **not yet reviewed** |
| CHEIDI | reconstruction incomplete — **not yet reviewed** |
| ChernSimonsPortal | full term-by-term cross-check |
| DMsimp | full term-by-term cross-check |
| EffLRSM | full term-by-term cross-check |
| GeneralU1 | full term-by-term cross-check |
| HeavyN | full term-by-term cross-check |
| HiggsCharacterisation | full term-by-term cross-check |
| LeptoQuark | full term-by-term cross-check |
| MDMmodel | full term-by-term cross-check |
| MSSMD | full term-by-term cross-check |
| Monotops | full term-by-term cross-check |
| NJLComposite | full term-by-term cross-check |
| SMWeinberg | full term-by-term cross-check |
| Sextets | full term-by-term cross-check |
| Top-Philic-Zprime | full term-by-term cross-check |
| Triplets | full term-by-term cross-check |
| VLC_LN | reconstruction incomplete — **not yet reviewed** |
| VLQ | full term-by-term cross-check |
| Wprime | full term-by-term cross-check |
| pNG | full term-by-term cross-check |
| pSPSS | full term-by-term cross-check |
| topBSM | full term-by-term cross-check |

4 of these have no cross-check. Their reverse runs hit agent-transport failures, not a physics result. Treat them as not yet reviewed.

### failing/ (3 models)

The loop could not get these through the chain. Included so the picture is complete, not only the successes. `<model>_one_shot.fr` is the first attempt; `<model>.fr` is the best repaired attempt; `VALIDATION_REPORT.md` is the failure it stopped on.

| model | best attempt | why it resisted |
|---|---|---|
| ALRM_general | repair3/round3 | multi-member `ClassMembers` scalar classes serialize to invalid UFO Python; restructuring re-breaks or times out the compile |
| HNLs | repair3/round3 | layered semantic UFO leaks; each was fixed once named, but the stack outlasted the round budget |
| SLQrules | repair3/round3 | residual SU(2)-multiplet covariant-derivative Hermiticity violation — genuinely hard physics, not a tooling gap |

## Caveats

- The repair agent ran isolated (no network, no reference files, no model name), but the underlying model may have seen these public model files in training.
- Repairs that replaced symbolic values with numerics keep the tool chain valid while narrowing the model's parameter generality. The analysis flags them.
- Symbol names survive sanitizing on purpose, so the blank-slate agent was not perfectly blind.
