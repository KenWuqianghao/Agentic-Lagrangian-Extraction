# Repair-loop benchmark — failing models through the agentic self-correction loop

Each one-shot validation failure is re-validated, then handed to an isolated repair agent (codex exec, workspace-write sandbox, **no network, no reference files, no model name**) together with the real FeynRules/MadGraph error output; the harness re-validates after each edit, up to 3 rounds.

| Model | Round-0 tags | Rounds | Final | Round-by-round |
|---|---|---|---|---|
| 331 | — | 3 | fail_after_repair | no_lagrangian_symbol → compile_failed → compile_failed → compile_failed |
| ALRM_general | — | 3 | fail_after_repair | no_lagrangian_symbol → compile_timeout → compile_timeout → compile_timeout |
| B-L-SM | builtin_symbol_collision, selfconjugate_quantum_numbers, hermiticity_fail, kinetic_diagonal_fail, mass_diagonal_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd | 3 | fail_after_repair | compiled[H✗Kd✗Md✗S?G✗] → compiled[H✓Kd✗Md✗S?G✗] → compiled[H✓Kd✗Md✗S?G✗] → compiled[H✓Kd✗Md✗S?G✗] |
| ChernSimonsPortal | — | 2 | pass_repaired | no_lagrangian_symbol → no_lagrangian_symbol → PASS |
| EffLRSM | builtin_symbol_collision, selfconjugate_quantum_numbers, mass_diagonal_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd | 3 | fail_after_repair | compiled[H✓Kd✓Md✗S?G✗] → compiled[H✓Kd✓Md✗S?G✗] → compiled[H✓Kd✓Md✗S?G✗] → compiled[H✓Kd✓Md✗S?G✗] |
| GeneralU1 | lag_symbol_undefined, fr_syntax_error, builtin_symbol_collision, selfconjugate_quantum_numbers | 2 | pass_repaired | compile_failed → compiled[H✓Kd✓Md✓S✗G✗] → PASS |
| HeavyN | selfconjugate_quantum_numbers | 0 | pass_oneshot | PASS |
| MDMmodel | duplicate_particle_names, selfconjugate_quantum_numbers, hermiticity_fail, kinetic_diagonal_fail, mass_diagonal_fail | 3 | fail_after_repair | compiled[H✗Kd✗Md✗S?G✓] → compiled[H✗Kd✗Md✗S?G✓] → compiled[H✗Kd✓Md✗S?G✓] → compiled[H✗Kd✓Md✗S?G✓] |
| Monotops | selfconjugate_quantum_numbers | 0 | pass_oneshot | PASS |
| NJLComposite | — | 0 | pass_oneshot | PASS |
| SLQrules | lag_symbol_undefined, fr_syntax_error | 3 | fail_after_repair | compile_failed → compile_failed → compiled[H✗Kd✓Md✗S?G✗] → compiled[H✗Kd✓Md✗S?G✗] |
| SMWeinberg | selfconjugate_quantum_numbers | 0 | pass_oneshot | PASS |
| Top-Philic-Zprime | selfconjugate_quantum_numbers | 0 | pass_oneshot | PASS |
| Wprime | mass_diagonal_fail | 3 | fail_after_repair | compiled[H✓Kd✓Md✗S?G✓] → compiled[H✓Kd✓Md✗S?G✓] → compiled[H✓Kd✓Md✗S?G✓] → compiled[H✓Kd✓Md✗S?G✓] |
| pNG | duplicate_particle_names, selfconjugate_quantum_numbers, hermiticity_fail, mass_diagonal_fail | 3 | fail_after_repair | compiled[H✗Kd✓Md✗S?G✓] → compiled[H✗Kd✓Md✗S?G✓] → compiled[H✗Kd✓Md✗S?G✓] → compiled[H✗Kd✓Md✗S?G✓] |
| pSPSS | selfconjugate_quantum_numbers, hermiticity_fail, kinetic_diagonal_fail, mass_diagonal_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd | 3 | fail_after_repair | compiled[H✗Kd✗Md✗S?G✗] → compiled[H✗Kd✗Md✗S?G✗] → compiled[H✗Kd✗Md✗S?G✗] → compiled[H✗Kd✗Md✓S✓G✗] |

**Aggregate:** {"n_models": 16, "pass_oneshot": 5, "pass_repaired": 2, "fail_after_repair": 9, "agent_no_change": 0, "max_rounds": 3}
