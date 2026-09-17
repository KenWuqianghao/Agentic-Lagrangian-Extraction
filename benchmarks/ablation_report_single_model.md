# Rerun ablation report

Variants: v3s_tools, v3s_notools. Models: 331, ALRM_general, B-L-SM, ChernSimonsPortal, EffLRSM, GeneralU1, HeavyN, MDMmodel, Monotops, NJLComposite, SLQrules, SMWeinberg, Top-Philic-Zprime, Wprime, pNG, pSPSS. Seeds per model: 1.

## Headline

| variant | findings resolved | full chain | mean field F1 |
|---|---|---|---|
| v3s_tools | 1/16 | 2/15 | 0.674 |
| v3s_notools | 2/16 | 2/15 | 0.659 |

*findings resolved* counts runs where every predicate for that model passed; there are 4 predicates across 16 models. *full chain* is FeynRules compile + all four consistency checks + MadGraph import, over the runs that reached validation.

## Physicist findings (deterministic predicates; resolved seeds / seeds with a file)

| model | finding | v3s_tools | v3s_notools |
|---|---|---|---|
| EffLRSM | efflrsm_charge_conjugation | 1/1 | 1/1 |
| EffLRSM | efflrsm_zr_normalisation | 0/1 | 1/1 |
| GeneralU1 | generalu1_eps_and_higgs_charge | 0/1 | 0/1 |
| Top-Philic-Zprime | zprime_free_field_terms | 1/1 | 1/1 |

## Validation chain and reference score, per run

| model | seed | variant | mode/source | agent | tools | paper read | tainted | rendered | predicates | lag | compile | checks H/Kd/Md/S | MG5 | full chain | field F1 | QN F1 | fields gen/ref |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 331 | 1 | v3s_tools | tools/tex | ok | 10 | True | False | True | — | compiled | True | ✓✓✓✓ | True | True | 0.31 | 0.31 | 13/38 |
| ALRM_general | 1 | v3s_tools | tools/tex | ok | 9 | True | False | False | — | — | — | — | — | — | — | — | —/— |
| B-L-SM | 1 | v3s_tools | tools/tex | ok | 4 | True | False | True | — | compiled | True | ✓✗✗? | True | False | 0.62 | 0.75 | 6/10 |
| ChernSimonsPortal | 1 | v3s_tools | tools/tex | ok | 5 | True | False | True | — | compiled | True | ✓✓✓✓ | True | True | 1.00 | 1.00 | 1/1 |
| EffLRSM | 1 | v3s_tools | tools/tex | ok | 6 | True | False | True | 1/2 | compiled | True | ✓✓✗? | True | False | 1.00 | 1.00 | 3/3 |
| GeneralU1 | 1 | v3s_tools | tools/tex | ok | 10 | True | False | True | 0/1 | compiled | True | ✗✓✗? | True | False | 0.33 | 0.33 | 3/15 |
| HeavyN | 1 | v3s_tools | tools/tex | ok | 6 | True | False | True | — | compiled | True | ✓✓✗? | True | False | 0.50 | 0.50 | 1/3 |
| MDMmodel | 1 | v3s_tools | tools/tex | ok | 7 | True | False | True | — | compiled | True | ✓✓✗? | False | False | 0.61 | 0.61 | 4/9 |
| Monotops | 1 | v3s_tools | tools/tex | ok | 5 | True | False | True | — | compiled | True | ✗✓✗? | False | False | 1.00 | 1.00 | 6/6 |
| NJLComposite | 1 | v3s_tools | tools/tex | ok | 8 | True | False | True | — | compiled | True | ✗✓✓✗ | False | False | 0.00 | 0.36 | 10/18 |
| SLQrules | 1 | v3s_tools | tools/tex | ok | 12 | True | False | True | — | compile_timeout | False | ✗✓✗· | None | False | 0.53 | 0.53 | 5/14 |
| SMWeinberg | 1 | v3s_tools | tools/tex | ok | 5 | True | False | True | — | compiled | True | ✗✓✗? | False | False | 1.00 | 1.00 | 1/1 |
| Top-Philic-Zprime | 1 | v3s_tools | tools/tex | ok | 8 | True | False | True | 1/1 | compiled | True | ✓✓✓✓ | False | False | 1.00 | 1.00 | 1/1 |
| Wprime | 1 | v3s_tools | tools/tex | ok | 7 | True | False | True | — | compile_failed | False | — | None | False | 0.67 | 0.67 | 2/1 |
| pNG | 1 | v3s_tools | tools/tex | ok | 10 | True | False | True | — | compiled | True | ✓✗✗? | True | False | 0.86 | 0.86 | 4/3 |
| pSPSS | 1 | v3s_tools | tools/tex | ok | 6 | True | False | True | — | compiled | True | ✓✓✗? | False | False | 0.67 | 0.67 | 3/6 |
| 331 | 1 | v3s_notools | notools/tex | fail | 9 | inlined | False | False | — | — | — | — | — | — | — | — | —/— |
| ALRM_general | 1 | v3s_notools | notools/tex | ok | 4 | inlined | False | True | — | compiled | True | ✓✓✓✓ | False | False | 0.48 | 0.44 | 17/16 |
| B-L-SM | 1 | v3s_notools | notools/tex | ok | 5 | inlined | False | True | — | compiled | True | ✓✓✗? | True | False | 0.53 | 0.67 | 5/10 |
| ChernSimonsPortal | 1 | v3s_notools | notools/tex | ok | 3 | inlined | False | True | — | compiled | True | ✓✓✓✓ | True | True | 1.00 | 1.00 | 1/1 |
| EffLRSM | 1 | v3s_notools | notools/tex | ok | 3 | inlined | False | True | 2/2 | compiled | True | ✓✓✓✗ | False | False | 1.00 | 1.00 | 3/3 |
| GeneralU1 | 1 | v3s_notools | notools/tex | ok | 6 | inlined | False | True | 0/1 | compiled | True | ✗✓✗? | True | False | 0.33 | 0.33 | 3/15 |
| HeavyN | 1 | v3s_notools | notools/tex | ok | 2 | inlined | False | True | — | compiled | True | ✓✓✗? | False | False | 0.50 | 0.50 | 1/3 |
| MDMmodel | 1 | v3s_notools | notools/tex | ok | 3 | inlined | False | True | — | compiled | True | ✓✓✗? | False | False | 0.46 | 0.46 | 4/9 |
| Monotops | 1 | v3s_notools | notools/tex | ok | 2 | inlined | False | True | — | compiled | True | ✗✓✗? | False | False | 0.50 | 1.00 | 6/6 |
| NJLComposite | 1 | v3s_notools | notools/tex | ok | 9 | inlined | False | True | — | compile_failed | False | — | None | False | 0.18 | 0.41 | 26/18 |
| SLQrules | 1 | v3s_notools | notools/tex | ok | 14 | inlined | False | True | — | compile_timeout | False | — | None | False | 0.53 | 0.53 | 5/14 |
| SMWeinberg | 1 | v3s_notools | notools/tex | ok | 4 | inlined | False | True | — | compiled | True | ✗✓✗? | False | False | 1.00 | 1.00 | 1/1 |
| Top-Philic-Zprime | 1 | v3s_notools | notools/tex | ok | 6 | inlined | False | True | 1/1 | compiled | True | ✓✓✓✓ | False | False | 1.00 | 1.00 | 1/1 |
| Wprime | 1 | v3s_notools | notools/tex | ok | 6 | inlined | False | True | — | ambiguous_lagrangian_symbol | None | — | None | None | 0.67 | 0.67 | 2/1 |
| pNG | 1 | v3s_notools | notools/tex | ok | 5 | inlined | False | True | — | compiled | True | ✓✓✓✓ | True | True | 0.86 | 0.86 | 4/3 |
| pSPSS | 1 | v3s_notools | notools/tex | ok | 5 | inlined | False | True | — | compile_timeout | False | ✗✗✗? | None | False | 0.83 | 0.83 | 6/6 |

## Aggregate per variant

| variant | mode | source | engine | model | tool policy | runs | agent ok | paper read | tainted | audit fail | rendered | all findings resolved | validated | compiled | all checks | MG5 | full chain | mean field F1 (n) | mean QN F1 | mean tool calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v3s_tools | tools | tex | claude-code-subagent | claude-sonnet-5 | instructed+audited | 16 | 16/16 | 16/16 | 0 | 8 | 15/16 | 1/16 | 15 | 13/15 | 3/15 | 7/15 | 2/15 | 0.674 (15) | 0.706 | 7.375 |
| v3s_notools | notools | tex | claude-code-subagent | claude-sonnet-5 | instructed+audited | 16 | 15/16 | 16/16 | 0 | 1 | 15/16 | 2/16 | 15 | 11/15 | 4/15 | 4/15 | 2/15 | 0.659 (15) | 0.713 | 5.375 |

`tool policy` says how the agent's tool restriction was imposed: `enforced` when the engine was started with `--allowedTools` / `--tools ''`, `instructed+audited` when the policy was given in the prompt and the transcript checked afterwards (`audit fail` counts runs that broke it). Predicates are evidence, not verdicts: a physicist reading the file decides. Field F1 compares new-field signatures with the FeynRules-DB reference; it is undefined for references with no new fields.
