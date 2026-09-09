# Rerun ablation report

Variants: v1, v2. Models: Top-Philic-Zprime, 368sextets, EffLRSM, GeneralU1. Seeds per model: 2.

## Headline

| variant | findings resolved | full chain | mean field F1 |
|---|---|---|---|
| v1 | 4/8 | 2/8 | 0.901 |
| v2 | 6/8 | 3/8 | 0.884 |

*findings resolved* counts runs where every predicate for that model passed; there are 6 predicates across 4 models. *full chain* is FeynRules compile + all three consistency checks + MadGraph import, over the runs that reached validation.

## Physicist findings (deterministic predicates; resolved seeds / seeds with a file)

| model | finding | v1 | v2 |
|---|---|---|---|
| Top-Philic-Zprime | zprime_free_field_terms | 2/2 | 2/2 |
| 368sextets | sextets_explicit_cutoffs | 2/2 | 2/2 |
| 368sextets | sextets_gauge_representation | 0/2 | 0/2 |
| EffLRSM | efflrsm_charge_conjugation | 2/2 | 2/2 |
| EffLRSM | efflrsm_zr_normalisation | 1/2 | 2/2 |
| GeneralU1 | generalu1_eps_and_higgs_charge | 1/2 | 2/2 |

## Validation chain and reference score, per run

| model | seed | variant | mode/source | agent | tools | paper read | tainted | rendered | predicates | lag | compile | checks H/K/M | MG5 | full chain | field F1 | QN F1 | fields gen/ref |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Top-Philic-Zprime | 1 | v1 | tools/txt | ok | 6 | True | False | True | 1/1 | compiled | True | ✓✓✓ | True | True | 1.00 | 1.00 | 1/1 |
| Top-Philic-Zprime | 2 | v1 | tools/txt | ok | 9 | True | False | True | 1/1 | compiled | True | ✓✓✓ | True | True | 1.00 | 1.00 | 1/1 |
| 368sextets | 1 | v1 | tools/txt | ok | 6 | True | False | True | 1/2 | compiled | True | ✓✓✓ | False | False | 1.00 | 1.00 | 4/4 |
| 368sextets | 2 | v1 | tools/txt | ok | 7 | True | False | True | 1/2 | compile_timeout | False | — | None | False | 1.00 | 1.00 | 4/4 |
| EffLRSM | 1 | v1 | tools/txt | ok | 4 | True | False | True | 1/2 | compiled | True | ✗✓✓ | False | False | 1.00 | 1.00 | 3/3 |
| EffLRSM | 2 | v1 | tools/txt | ok | 4 | True | False | True | 2/2 | compiled | True | ✓✓✓ | False | False | 1.00 | 1.00 | 3/3 |
| GeneralU1 | 1 | v1 | tools/txt | ok | 5 | True | False | True | 0/1 | compile_timeout | False | — | None | False | 0.64 | 0.64 | 7/15 |
| GeneralU1 | 2 | v1 | tools/txt | ok | 5 | True | False | True | 1/1 | compiled | True | ✓✓✓ | False | False | 0.57 | 0.57 | 6/15 |
| Top-Philic-Zprime | 1 | v2 | tools/txt | ok | 6 | True | False | True | 1/1 | compiled | True | ✓✓✓ | True | True | 1.00 | 1.00 | 1/1 |
| Top-Philic-Zprime | 2 | v2 | tools/txt | ok | 6 | True | False | True | 1/1 | compiled | True | ✓✓✓ | True | True | 1.00 | 1.00 | 1/1 |
| 368sextets | 1 | v2 | tools/txt | ok | 4 | True | False | True | 1/2 | compiled | True | ✓✓✓ | True | True | 1.00 | 1.00 | 4/4 |
| 368sextets | 2 | v2 | tools/txt | ok | 5 | True | False | True | 1/2 | compile_timeout | False | — | None | False | 1.00 | 1.00 | 4/4 |
| EffLRSM | 1 | v2 | tools/txt | ok | 5 | True | False | True | 2/2 | compiled | True | ✗✗✗ | False | False | 1.00 | 1.00 | 3/3 |
| EffLRSM | 2 | v2 | tools/txt | ok | 5 | True | False | True | 2/2 | compiled | True | ✗✓✓ | False | False | 1.00 | 1.00 | 3/3 |
| GeneralU1 | 1 | v2 | tools/txt | ok | 4 | True | False | True | 1/1 | compiled | True | ✓✓✓ | False | False | 0.50 | 0.50 | 5/15 |
| GeneralU1 | 2 | v2 | tools/txt | ok | 5 | True | False | True | 1/1 | compiled | True | ✓✓✓ | False | False | 0.57 | 0.57 | 6/15 |

## Aggregate per variant

| variant | mode | source | engine | tool policy | runs | agent ok | paper read | tainted | audit fail | rendered | all findings resolved | validated | compiled | all checks | MG5 | full chain | mean field F1 (n) | mean QN F1 | mean tool calls |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v1 | tools | txt | claude-cli | enforced | 8 | 8/8 | 8/8 | 0 | 0 | 8/8 | 4/8 | 8 | 6/8 | 5/8 | 2/8 | 2/8 | 0.901 (8) | 0.901 | 5.75 |
| v2 | tools | txt | claude-cli | enforced | 8 | 8/8 | 8/8 | 0 | 0 | 8/8 | 6/8 | 8 | 7/8 | 5/8 | 3/8 | 3/8 | 0.884 (8) | 0.884 | 5.0 |

`tool policy` says how the agent's tool restriction was imposed: `enforced` when the engine was started with `--allowedTools` / `--tools ''`, `instructed+audited` when the policy was given in the prompt and the transcript checked afterwards (`audit fail` counts runs that broke it). Predicates are evidence, not verdicts: a physicist reading the file decides. Field F1 compares new-field signatures with the FeynRules-DB reference; it is undefined for references with no new fields.
