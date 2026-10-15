# Option E: deterministic lints replayed on every stored model (2026-09-22)

Question: how many validation failures could a text lint have named before
the compile, and at what false-positive cost?

Code: `fr_lint.py` (the rules), `lint_replay.py` (the replay). Generated
table: `lint_replay.md`, per-file findings: `lint_replay.json`.

## Data

140 stored agent `.fr` files with a verdict from the corrected harness: 93
one-shot reruns (`<page>/rerun/<variant>/s<k>`) and 47 repair-loop rounds
(`<page>/repair_corrected/round<k>`). Outcomes:

| outcome | files |
|---|---|
| harness could not pick a total Lagrangian | 8 |
| compile failed | 10 |
| compile timed out (900 s) | 15 |
| compiled, a FeynRules check failed, MadGraph rejected | 37 |
| compiled, a FeynRules check failed, MadGraph accepted | 33 |
| compiled, checks passed, MadGraph rejected | 7 |
| full pass | 30 |

FeynRules checks and MadGraph import are independent stages: the harness
imports the UFO even when a check fails. A lint that predicts one stage is
scored only on files that reached that stage.

## What each rule is worth

Precision is the fraction of flagged files that failed the predicted stage,
among files that reached it.

| rule | predicts | flagged | reached | failed | precision |
|---|---|---|---|---|---|
| `ambiguous_total` (two root Lagrangian symbols) | harness | 8 | 8 | 8 | 1.00 |
| `bad_particle_name` (quote or space in a UFO name) | MadGraph | 3 | 3 | 3 | 1.00 |
| `feynrules_symbol_name` (class named `HC`, `T`, ...) | compile | 1 | 1 | 1 | 1.00 |
| `majorana_mass_no_half` | checks | 1 | 1 | 1 | 1.00 |
| `mixing_in_definitions` (a class defined as a rotation of two physical fields) | checks | 30 | 26 | 22 | 0.85 |
| `pattern_rule_definition` (`X[i_?NumericQ] :> ...`) | MadGraph | 14 | 11 | 7 | 0.64 |
| `missing_interaction_order` (a term whose parameters all lack an order) | MadGraph | 25 | 15 | 8 | 0.53 |
| `explicit_flavour_sum` (`y[ff1,ff2] qbar[ff1] ... q[ff2]`) | MadGraph | 28 | 24 | 12 | 0.50 |
| `explicit_index_in_dc` on a colour-indexed new field | compile | 3 | 3 | 1 | 0.33 |
| `fieldless_term` | MadGraph | 4 | 0 | — | n/a |

Warnings (no stage claimed, reported for the agent's attention): protected
Mathematica names, SM.fr names redeclared, class index below 100, the total
not named `LTotal`, `SelfConjugate` with quantum numbers, a sextet index
without `AddGaugeRepresentation`, a symbol used in a term that nothing
declares, an explicit SU(2) index inside `DC[]`.

Recall by stage:

| failure stage | files | flagged by a lint for that stage | flagged by any error-level lint |
|---|---|---|---|
| harness | 8 | 8 | 8 |
| compile | 25 | 2 | 17 |
| checks | 70 | 23 | 38 |
| MadGraph | 44 | 19 | 23 |
| full pass (false positives) | 30 | — | 9 |

## What this says

- **The harness stage is fully predictable.** Every file the harness could
  not score had two root Lagrangian symbols, and the lint names both. This
  costs nothing and would have saved 8 agent runs from a null verdict.
- **The mass-basis wall is visible in the text.** A class whose
  `Definitions` mixes two physical fields, with a sine or cosine in the
  rule, fails `CheckDiagonalMassTerms` 22 times in 26. The four exceptions
  are files that wrote the rotation but omitted the potential that produces
  the mixing (the passing pNG file is one), so they are diagonal by omission.
  The lint catches 23 of the 56 files that fail this check; the other 33
  fail it without any rotation in the file, which is the seesaw and
  leptoquark class the repair agents would not touch.
- **The MadGraph rules are half right.** Pattern-rule definitions, explicit
  flavour sums and unordered couplings each predict a rejection in 50 to 64%
  of the flagged files. The misses are files where FeynRules happened to
  serialise the construct cleanly. As a pre-compile warning that costs
  nothing, that is useful; as a hard gate it would block working models.
- **Compile failures are not lintable.** 15 of the 25 are timeouts, and the
  seven sextet timeouts carry no construct the rules know: they are slow,
  not wrong. The two syntax-class failures the rules do catch are a class
  named after a FeynRules symbol and a colour index inside a covariant
  derivative.
- **False positives.** 9 of the 30 fully passing files carry an error-level
  finding. Six are the MadGraph rules on constructs FeynRules serialised
  anyway; two are `mixing_in_definitions` on rotation-by-omission files; one
  is the flavour-sum rule on a file whose explicit sum worked.

## Time

The 93 one-shot reruns spent 12.1 hours in FeynRules compiles. 26 of those
files carry a lint that correctly predicted the stage they failed; those
compiles took 1.8 hours. A lint runs in under a second. Against the whole
chain the saving is small because most compile time goes to timeouts and
to models that fail a physics check the lint cannot see.

## What to build from this

1. Ship `ambiguous_total`, `bad_particle_name`, `feynrules_symbol_name` and
   `mixing_in_definitions` as errors in `validatemodel` before the Wolfram
   call. They are precise and cheap.
2. Ship the three MadGraph rules and the warnings as advisory output in the
   validation report, not as gates.
3. The `mixing_in_definitions` message should point the agent at the
   mass-basis recipe (option A), because the construct it flags is the
   right idea done half-way: the rotation is declared but the couplings
   are not inverted.
