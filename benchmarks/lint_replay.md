# Lint replay over stored agent models

140 files ({'rerun': 93, 'repair': 47}), outcomes: checks+mg5_failed 37, checks_failed 33, compile_failed 10, compile_timeout 15, harness 8, mg5_failed 7, pass 30

A rule predicts one stage. Precision counts only files that REACHED that stage (compiled, for checks and MadGraph); a file that never compiled says nothing about its UFO.

## Per rule

| rule | stage | files flagged | reached the stage | failed it | precision |
|---|---|---|---|---|---|
| majorana_mass_no_half | checks | 1 | 1 | 1 | 1.00 |
| mixing_in_definitions | checks | 30 | 26 | 22 | 0.85 |
| explicit_index_in_dc | compile | 3 | 3 | 1 | 0.33 |
| feynrules_symbol_name | compile | 1 | 1 | 1 | 1.00 |
| ambiguous_total | harness | 8 | 8 | 8 | 1.00 |
| bad_particle_name | mg5 | 3 | 3 | 3 | 1.00 |
| explicit_flavour_sum | mg5 | 28 | 24 | 12 | 0.50 |
| fieldless_term | mg5 | 4 | 0 | 0 | n/a |
| missing_interaction_order | mg5 | 25 | 15 | 8 | 0.53 |
| pattern_rule_definition | mg5 | 14 | 11 | 7 | 0.64 |
| explicit_index_in_dc | warn | 38 | — | — | — |
| low_class_index | warn | 28 | — | — | — |
| protected_name | warn | 6 | — | — | — |
| selfconjugate_with_qn | warn | 5 | — | — | — |
| sextet_without_representation | warn | 5 | — | — | — |
| sm_class_redeclared | warn | 12 | — | — | — |
| sm_parameter_redeclared | warn | 3 | — | — | — |
| total_not_named_ltotal | warn | 35 | — | — | — |
| undeclared_symbol | warn | 38 | — | — | — |

## Recall per failure stage

| failure stage | files failing it | with a lint predicting it | with any error-level lint |
|---|---|---|---|
| harness | 8 | 8 | 8 |
| compile | 25 | 2 | 17 |
| checks | 70 | 23 | 38 |
| mg5 | 44 | 19 | 23 |
| pass (false positives) | 30 | — | 9 |

## Error-level lints on files that passed the whole chain

- `331/rerun/v2/s1`: mixing_in_definitions (class `rhoT` is defined as a mixture of ['H0', 'H2', 'H3', 'Hp']; the mass basis of the pa); mixing_in_definitions (class `etaT` is defined as a mixture of ['H0', 'H2', 'H3']; the mass basis of the partner ); mixing_in_definitions (class `chiT` is defined as a mixture of ['H0', 'H2', 'H3', 'HV', 'HY']; the mass basis of ); mixing_in_definitions (class `q1L` is defined as a mixture of ['DQ', 'dq', 'uq']; the mass basis of the partner f); mixing_in_definitions (class `q2L` is defined as a mixture of ['SQ', 'dq', 'uq']; the mass basis of the partner f); mixing_in_definitions (class `q3L` is defined as a mixture of ['TQ', 'dq', 'uq']; the mass basis of the partner f); mixing_in_definitions (class `lL` is defined as a mixture of ['EL', 'l', 'vl']; the mass basis of the partner fie)
- `331/rerun/v3s_tools/s1`: missing_interaction_order (`LH2`: none of its parameters (MH2) carries an InteractionOrder); missing_interaction_order (`LH0`: none of its parameters (MH0) carries an InteractionOrder)
- `GeneralU1/rerun/v3_notools/s2`: explicit_flavour_sum (`LNYukD`: flavour matrix `yv` with explicit generation indices instead of matrix form)
- `GeneralU1/rerun/v3txt_tools/s1`: explicit_flavour_sum (`LNDir`: flavour matrix `yNu` with explicit generation indices instead of matrix form)
- `NJLComposite/rerun/v2/s1`: mixing_in_definitions (class `Pi76` is defined as a mixture of ['Pi23d', 'Pi53']; the mass basis of the partner f); mixing_in_definitions (class `Pi16` is defined as a mixture of ['Pi23u', 'Pim13']; the mass basis of the partner )
- `pNG/rerun/v3s_notools/s1`: mixing_in_definitions (class `phi1` is defined as a mixture of ['H', 'H2']; the mass basis of the partner fields ); mixing_in_definitions (class `s1` is defined as a mixture of ['H', 'H2']; the mass basis of the partner fields de)
- `GeneralU1/repair_corrected/round2`: pattern_rule_definition (parameter `yNu` uses a pattern rule in Definitions/Value; FeynRules exports it verbatim as); explicit_flavour_sum (`LNuDiracYuk`: flavour matrix `yNu` with explicit generation indices instead of matrix for)
- `Monotops/repair_corrected/round0`: pattern_rule_definition (parameter `B0FC` uses a pattern rule in Definitions/Value; FeynRules exports it verbatim a); pattern_rule_definition (parameter `B1FC` uses a pattern rule in Definitions/Value; FeynRules exports it verbatim a); pattern_rule_definition (parameter `B12S` uses a pattern rule in Definitions/Value; FeynRules exports it verbatim a); pattern_rule_definition (parameter `tB12S` uses a pattern rule in Definitions/Value; FeynRules exports it verbatim ); pattern_rule_definition (parameter `BQS` uses a pattern rule in Definitions/Value; FeynRules exports it verbatim as); pattern_rule_definition (parameter `tBQS` uses a pattern rule in Definitions/Value; FeynRules exports it verbatim a); pattern_rule_definition (parameter `B12V` uses a pattern rule in Definitions/Value; FeynRules exports it verbatim a); pattern_rule_definition (parameter `BQV` uses a pattern rule in Definitions/Value; FeynRules exports it verbatim as)
- `NJLComposite/repair_corrected/round0`: explicit_index_in_dc (`LkinNJL`: covariant derivative on `Pi5e` with an explicit colour-type index)

## mixing_in_definitions vs CheckDiagonalMassTerms

- files flagged: 30; of those with a check verdict, mass_diagonal fail: 23, pass: 4
- files with mass_diagonal fail: 56; flagged by the lint: 23
