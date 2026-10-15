| model | arm | runs (valid) | .fr produced | compiled | MG5 import | 4 checks pass | full chain | Herm | Kin | Mass diag | Mass spec | field F1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nemotron 3 Ultra | hand | 16 (15) | 11 | 5 | 0 | 1 | **0** | 3 | 5 | 3 | 2 | 0.589 |
| Nemotron 3 Ultra | toolkit | 16 (15) | 11 | 6 | 1 | 0 | **0** | 1 | 5 | 3 | 3 | 0.726 |
| Nemotron 3 Ultra | toolkit2 | 16 (15) | 15 | 8 | 2 | 2 | **1** | 4 | 6 | 3 | 3 | 0.647 |
| MiMo v2.6 Flash | hand | 16 (16) | 7 | 5 | 2 | 2 | **0** | 5 | 4 | 3 | 2 | 0.664 |
| MiMo v2.6 Flash | toolkit | 16 (16) | 15 | 9 | 4 | 2 | **0** | 5 | 7 | 6 | 4 | 0.65 |
| MiMo v2.6 Flash | toolkit2 | 16 (16) | 3 | 2 | 0 | 0 | **0** | 0 | 2 | 1 | 1 | 1.0 |
| Sonnet (Sep 17) | hand | 16 (16) | 15 | 11 | 4 | 4 | **2** | 8 | 11 | 5 | 4 | 0.659 |
| Sonnet (Sep 17) | schema one-shot | 16 (16) | 15 | 13 | 7 | 3 | **2** | 9 | 12 | 4 | 3 | 0.674 |

Fisher exact p, toolkit arm vs hand: nemotron:toolkit:rendered 1.0, nemotron:toolkit:compiled 1.0, nemotron:toolkit:mg5 1.0, nemotron:toolkit:full_chain 1.0, nemotron:toolkit2:rendered 0.1, nemotron:toolkit2:compiled 0.462, nemotron:toolkit2:mg5 0.483, nemotron:toolkit2:full_chain 1.0, mimo:toolkit:rendered 0.006, mimo:toolkit:compiled 0.285, mimo:toolkit:mg5 0.654, mimo:toolkit:full_chain 1.0, mimo:toolkit2:rendered 0.252, mimo:toolkit2:compiled 0.394, mimo:toolkit2:mg5 0.484, mimo:toolkit2:full_chain 1.0

| page | v3o_nemotron_hand | v3o_nemotron_toolkit | v3o_nemotron_toolkit2 | v3o_mimo_hand | v3o_mimo_toolkit | v3o_mimo_toolkit2 | v3s_notools | v3s_tools |
|---|---|---|---|---|---|---|---|---|
| 331 | ambiguous_lagrangian_symbol | no .fr (no_spec) | compile_timeout | compile_failed | MG5 fail; fail hermiticity | no .fr (no_spec) | no .fr (?) | **PASS** |
| ALRM_general | no_lagrangian_symbol | no .fr (no_spec) | compile_failed | no .fr (no_model_fr) | MG5 fail; fail hermiticity,mass_spectrum | no .fr (no_spec) | MG5 fail;  | no .fr (?) |
| B-L-SM | compile_failed | compile_failed | MG5 fail; fail hermiticity,kinetic_diagonal,mass_diagonal,mass_spectrum | no .fr (no_model_fr) | compile_timeout | no .fr (no_spec) | fail mass_diagonal,mass_spectrum | fail kinetic_diagonal,mass_diagonal,mass_spectrum |
| ChernSimonsPortal | MG5 fail;  | fail hermiticity | **PASS** | no .fr (no_model_fr) | compile_timeout | no .fr (no_spec) | **PASS** | **PASS** |
| EffLRSM | compile_failed | MG5 fail; fail hermiticity | compile_timeout | fail mass_spectrum | MG5 fail; fail hermiticity | no .fr (no_spec) | MG5 fail; fail mass_spectrum | fail mass_diagonal,mass_spectrum |
| GeneralU1 | MG5 fail; fail mass_spectrum | compile_failed | compile_timeout | MG5 fail; fail mass_diagonal,mass_spectrum | compile_failed | no .fr (no_spec) | fail hermiticity,mass_diagonal,mass_spectrum | fail hermiticity,mass_diagonal,mass_spectrum |
| HeavyN | MG5 fail; fail mass_diagonal,mass_spectrum | compile_failed | fail mass_diagonal,mass_spectrum | no .fr (no_model_fr) | fail mass_diagonal,mass_spectrum | no .fr (no_spec) | MG5 fail; fail mass_diagonal,mass_spectrum | fail mass_diagonal,mass_spectrum |
| MDMmodel | compile_failed | MG5 fail; fail hermiticity,kinetic_diagonal,mass_diagonal,mass_spectrum | compile_timeout | no .fr (no_model_fr) | fail mass_diagonal,mass_spectrum | no .fr (no_spec) | MG5 fail; fail mass_diagonal,mass_spectrum | MG5 fail; fail mass_diagonal,mass_spectrum |
| Monotops | no .fr (no_model_fr) | no .fr (no_spec) | compile_timeout | no .fr (no_model_fr) | compile_timeout | compile_failed | MG5 fail; fail hermiticity,mass_diagonal,mass_spectrum | MG5 fail; fail hermiticity,mass_diagonal,mass_spectrum |
| NJLComposite | no .fr (no_model_fr) | no_lagrangian_symbol | compile_timeout | no .fr (no_model_fr) | compile_failed | no .fr (no_spec) | compile_failed | MG5 fail; fail hermiticity,mass_spectrum |
| SLQrules | no .fr (no_model_fr) | no .fr (no_spec) | provider error | compile_failed | compile_failed | no .fr (no_spec) | compile_timeout | compile_timeout |
| SMWeinberg | MG5 fail; fail hermiticity,mass_diagonal,mass_spectrum | MG5 fail; fail hermiticity,mass_diagonal,mass_spectrum | MG5 fail; fail hermiticity,mass_diagonal,mass_spectrum | no .fr (no_model_fr) | no .fr (no_spec) | MG5 fail; fail hermiticity,mass_diagonal,mass_spectrum | MG5 fail; fail hermiticity,mass_diagonal,mass_spectrum | MG5 fail; fail hermiticity,mass_diagonal,mass_spectrum |
| Top-Philic-Zprime | MG5 fail; fail hermiticity | MG5 fail; fail hermiticity | MG5 fail;  | MG5 fail;  | MG5 fail;  | MG5 fail; fail hermiticity | MG5 fail;  | MG5 fail;  |
| Wprime | compile_failed | compile_timeout | MG5 fail; fail hermiticity | MG5 fail;  | MG5 fail;  | no .fr (no_spec) | ambiguous_lagrangian_symbol | compile_failed |
| pNG | no .fr (no_model_fr) | MG5 fail; fail mass_diagonal,mass_spectrum | MG5 fail; fail hermiticity,kinetic_diagonal,mass_diagonal,mass_spectrum | no .fr (no_model_fr) | fail kinetic_diagonal,mass_spectrum | no .fr (no_spec) | **PASS** | fail kinetic_diagonal,mass_diagonal,mass_spectrum |
| pSPSS | provider error | provider error | MG5 fail; fail mass_diagonal,mass_spectrum | fail kinetic_diagonal,mass_diagonal,mass_spectrum | fail hermiticity,kinetic_diagonal,mass_diagonal,mass_spectrum | no .fr (no_spec) | compile_timeout | MG5 fail; fail mass_diagonal,mass_spectrum |
