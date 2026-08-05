# Review bundle — agent-extracted FeynRules models

28 published BSM models from the FeynRules model database were re-derived from their own papers by an agent, then pushed through the full validation chain: FeynRules/Wolfram UFO compile, Hermiticity / kinetic-term / mass-spectrum checks, MadGraph import. Models that failed entered a closed repair loop.

| outcome | models |
|---|---:|
| clear the full chain | **18** |
| fail the full chain | 1 |
| cannot be scored — see below | 9 |
| **total** | **28** |

## Read this first

An earlier version of this bundle reported 25 of 28 passing. That number was wrong and is withdrawn.

The harness used to choose each model's total-Lagrangian symbol by file position — the last `L... =` line. For 11 models that picked a sub-Lagrangian, so FeynRules compiled only a fragment. A fragment is easier to satisfy than the whole: it can be Hermitian when the full Lagrangian is not, and it can show a clean mass spectrum simply by omitting most fields. Those fragments passed every check and imported into MadGraph. `VLQ` was scored as passing having compiled 1 of its 11 Lagrangian terms.

The total is now resolved by reference analysis — the term no other term refers to — and where a model never declares one, the harness **refuses to guess** and leaves it unscored. Everything was re-run. All 19 scoreable models reproduced their previous verdict, so the pipeline did not get worse; 9 models were simply never measured.

**Unscoreable is not failed.** Those 9 models may be perfectly correct. They just never say which symbol is the whole model, so there is nothing defensible to compile. `LAGRANGIAN_AMBIGUITY.md` lists what each one defines — it is a short decision list, and four of the nine are genuine physics choices only you can make.

Three of the ten repairs the loop claimed are also affected: `331`, `CHEIDI` and `VLC_LN` were scored `pass_repaired` against fragments, so those claims cannot be evaluated. Seven repairs stand.

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

1. `LAGRANGIAN_AMBIGUITY.md` — the nine unscoreable models and what each defines. Four need a physics decision from you.
2. `CONVENTION_DISAGREEMENTS.md` — every graded row, grouped by theme. Start with the substantive ones.
3. `passing/<model>/REVIEW.pdf` — the full review package for any model whose rows you want to see in context. The last page is a sign-off block.
4. `REPAIR_BENCHMARK_ANALYSIS.md` — what the loop fixed, what it could not, and the error taxonomy.
5. `reports/` — the machine-generated per-stage results.
6. `failing/` and `unscored/` — the models that did not clear the chain, and the nine that could not be scored at all.

## Contents

### passing/ (18 models)

`<model>.fr` is the validated FeynRules file, agent-extracted and, where the loop repaired it, self-repaired with no human input. **Every model has exactly one PDF — open that and you have everything.**

`REVIEW.pdf` is a completed reverse-check package: verbatim Lagrangian terms, the blank-slate reconstruction, the term-by-term paper comparison, and a sign-off block. `DOSSIER.pdf` appears where the reverse run did not finish — it carries the verbatim Lagrangian, whatever reconstruction exists, the validation result and the repair history, so the model is still readable without opening source files.

| model | PDF | pages | state |
|---|---|---:|---|
| 368sextets | `REVIEW.pdf` | 8 | full term-by-term cross-check |
| B-L-SM | `DOSSIER.pdf` | 6 | reverse run unfinished — **not yet reviewed** |
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
| Wprime | `REVIEW.pdf` | 8 | full term-by-term cross-check |
| pNG | `REVIEW.pdf` | 8 | full term-by-term cross-check |
| pSPSS | `REVIEW.pdf` | 9 | full term-by-term cross-check |

4 of these have no cross-check. Their reverse runs hit agent-transport failures, not a physics result. Treat them as not yet reviewed — their `DOSSIER.pdf` says so on page 1.

### failing/ (1 models)

Scored, and did not clear the chain.

| model | best attempt | why |
|---|---|---|
| SLQrules | repair3/round3 | A syntax error at line 660 stops FeynRules loading the model, so its total Lagrangian is never defined. The repair loop never produced a working version, so this is the one-shot file. Behind it sits a residual SU(2)-multiplet covariant-derivative Hermiticity violation that survived nine rounds — genuinely hard physics rather than a tooling gap. |

### unscored/ (9 models)

**Neither passed nor failed.** These models define several independent top-level Lagrangians and never say which one — or which sum — is the model, so there is nothing defensible to compile. Earlier numbers scored them by picking whichever came last in the file, which is how `VLQ` came to be reported as passing on 1 of its 11 terms.

`LAGRANGIAN_AMBIGUITY.md` lists the competing definitions for each. Five look like complementary sectors where a sum is the natural reading; four are genuine alternatives — `ChernSimonsPortal` (symmetric versus broken phase), `DMsimp` (spin-0 versus spin-1 mediator), `topBSM` (four simplified models in one file) and `CHEIDI` (full top loop versus heavy-top limit). Those four need a physicist, not a parser.

| model | competing definitions |
|---|---|
| 331 | LHiggs331, LGauge331Mass, LScalarFermion331, LTot |
| ALRM_general | LYALRM, LSALRM, LFALRM, LeffALRM |
| CHEIDI | LHEIDI, LHEIDIgg, LTot |
| ChernSimonsPortal | LChernSimonsPortal, LChernSimonsPortalBroken |
| DMsimp | L0DM, L1DM |
| HNLs | LagHeavyN, LHeavyNDiracMass, LHeavyNEW + 4 hadronic terms |
| VLC_LN | LChiralFull, LEDM, LTot |
| VLQ | 11 separate T'/B' coupling terms |
| topBSM | LS0, LO0, LS1, LO1 |

## Caveats

- The repair agent ran isolated (no network, no reference files, no model name), but the underlying model may have seen these public model files in training.
- Repairs that replaced symbolic values with numerics keep the tool chain valid while narrowing the model's parameter generality. The analysis flags them.
- Symbol names survive sanitizing on purpose, so the blank-slate agent was not perfectly blind.
