# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
article class (the `F[100]` block holding `n4` and `n5`). This class is declared `SelfConjugate -> True`, meaning `n4` and `n5` are Majorana fields. A Majorana field must not carry a declared `QuantumNumbers` entry: self-conjugacy already forces neutral charge, and giving it an explicit `QuantumNumbers` list conflicts with FeynRules' own bookkeeping for self-conjugate fields. This exact defect was named directly by the validation report's heuristic tag `selfconjugate_quantum_numbers` and matches a defect type the task explicitly calls out for repair. I judge this to be the root technical fault: it corrupts FeynRules' internal treatment of the Majorana condition on `n4`/`n5`, which explains why `CheckHermiticity`, `CheckDiagonalKineticTerms`, `CheckDiagonalMassTerms`, and `CheckMassSpectrum` all failed together, and why the generated UFO was corrupted across unrelated Standard Model vertices too (a single broken internal state during Feynman-rule generation poisons the rest of the same Mathematica session's UFO-writing pass, matching the garbled `ConvertSpinToString`/`PartNameMG` calls and the stray `NameError: name 'e' is not defined` seen in the old UFO output). I traced the mixing-matrix (`Un`, `UnCL`) construction by hand and confirmed it is unitary to the needed order in `theta`, so the pseudo-Dirac kinetic and mass terms are physically correct as written; no change to the physics content, field content, or operator structure was needed there.

I also renamed the final Lagrangian assignment from `LpSPSS = RemoveHigherOrder[LSM + LKineticSterile + LNP];` to the required `LTot := RemoveHigherOrder[LSM + LKineticSterile + LNP];`, matching the mandated `LTot := Lterm1 + Lterm2 + ...;` format for the last top-level statement, with no change to its content.

File modified: `/private/tmp/claude-501/-Users-kenwu-Documents-Github-Agentic-Lagrangian-Extraction/94cf8ff6-6dba-453e-b8ee-ad80d63999c8/scratchpad/hmain/eval/benchmark_runs/pSPSS/repair_corrected/round1/model.fr`

Validation outcome AFTER that change: status=compiled, hermiticity=fail, kinetic_diagonal=fail, mass_diagonal=fail, mass_spectrum=inconclusive, madgraph_import=False, tags=hermiticity_fail, kinetic_diagonal_fail, mass_diagonal_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=74.2

## Attempt 2
What was changed (the agent's own summary):
pSPSS Lagrangian.

`model.fr` wrote several parameter default values using C-style scientific notation (`1.000000e+02`, `1.000000e-12`, `1.000000e-03`, and three `0.000000e+00` instances). Mathematica has no such literal syntax — it does not recognize lowercase `e` as an exponent marker. It parsed `1.000000e+02` as implicit multiplication by the undefined symbol `e` plus an integer, i.e. `1.000000*e + 2`. I confirmed this directly in the generated `UFO/parameters.py`, where `Mmaj`, `deltaM`, and `theta2` came out as literal broken values `2 + 1.*e`, `-12 + 1.*e`, and `-3 + 1.*e` (the three zero-valued parameters happened to evaluate to plain `0.` by luck, since `0.` times anything is `0.`).

Because `Mmaj`, `deltaM`, and `theta2` feed into `Mn4`, `Mn5`, `thetaSq`, and every entry of the `Un` mixing matrix, this corruption propagated everywhere: FeynRules could not algebraically confirm Hermiticity, kinetic-diagonality, or mass-diagonality, and `CheckMassSpectrum` came back inconclusive. The same corrupted symbolic expressions were dumped verbatim into the UFO's `parameters.py`, producing the exact `NameError: name 'e' is not defined`, and the resulting confusion during vertex/Feynman-rule generation is what produced the garbled `ConvertSpinToString` output and the mismatched-parenthesis syntax error in `vertices.py`.

Fix applied in `/private/tmp/claude-501/.../repair_corrected/round2/model.fr`: replaced the six invalid literals with valid Mathematica syntax, preserving the exact intended numeric values:
- `Mmaj`: `1.000000e+02` → `100.0`
- `deltaM`: `1.000000e-12` → `1.0*^-12`
- `theta1`, `theta3`, `damping`: `0.000000e+00` → `0.0`
- `theta2`: `1.000000e-03` → `1.0*^-3`

No fields, quantum numbers, operator structure, or parameter magnitudes were changed — only the numeric literal syntax. This does not repeat the round-1 approach (which addressed an unrelated `QuantumNumbers`-on-Majorana-field issue that had already been fixed and left the real failures untouched).

Validation outcome AFTER that change: status=compiled, hermiticity=fail, kinetic_diagonal=fail, mass_diagonal=fail, mass_spectrum=inconclusive, madgraph_import=False, tags=hermiticity_fail, kinetic_diagonal_fail, mass_diagonal_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=76.2

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=fail, kinetic_diagonal=fail, mass_diagonal=fail, mass_spectrum=inconclusive, madgraph_import=False, tags=selfconjugate_quantum_numbers, hermiticity_fail, kinetic_diagonal_fail, mass_diagonal_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=129.8
