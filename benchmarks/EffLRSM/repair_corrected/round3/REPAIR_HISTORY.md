# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
full, current state of the model file is correct: `ClassName -> HN` for the heavy Majorana neutrino class, no stray `N[...]` field references remain, both self-conjugate particles (`ZR`, `HN`) no longer carry `QuantumNumbers`, and the total Lagrangian is now named `LTot` with delayed assignment (`:=`), as the tool chain requires.

Summary of changes made to `model.fr`:

1. **Fixed the builtin-symbol collision (root cause).** The Majorana heavy-neutrino class was declared with `ClassName -> N`, but `N` is a protected Mathematica built-in (the numericize function). Renamed the class to `ClassName -> HN` and updated every Lagrangian reference (`bar[N[nn]]`, `bar[N[ii]]...N[ii]`) to `HN`. This collision is the most likely cause of the near-total corruption seen in the generated UFO — garbled, unevaluated Mathematica expressions (`PartNameMG[...]`, `ConvertSpinToString[0]`, a vertex literally named `1 = Lorentz(...)`) appeared even in purely-SM vertices (quarks, leptons unrelated to the BSM sector), which is the signature of a global built-in override corrupting FeynRules' internal symbolic evaluation during `WriteUFO`, not a localized bug. This also explains the spurious `mass_diagonal`/`mass_spectrum` failures on the WR charged-current term (a trilinear vector-current vertex, not a mass term at all) — that check output was itself a casualty of the same corruption.
2. **Removed `QuantumNumbers -> {Q -> 0}` from the two self-conjugate classes** (`ZR` and `HN`), per the rule against declaring quantum numbers on Majorana/real self-conjugate fields.
3. **Renamed the total-Lagrangian assignment from `LBSM = ...` to `LTot := ...`**, matching the required convention (last top-level assignment, delayed rule, built only from previously-defined symbols), with no change to which terms are summed.

No field content, quantum numbers (other than the redundant Q=0 removal on self-conjugate fields), couplings, or parameter values were altered — these were purely technical/naming fixes.

Validation outcome AFTER that change: status=compiled, hermiticity=pass, kinetic_diagonal=pass, mass_diagonal=fail, mass_spectrum=inconclusive, madgraph_import=False, tags=mass_diagonal_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=245.3

## Attempt 2
What was changed (the agent's own summary):
s `HN` with a distinct field (`l`, `ve`), which is unproblematic. This single term is the most plausible trigger for the cascading corruption seen in the report: parallel-kernel warnings (`Join::heads`, `Part::partw`, `Part::pkspec1`) during the consistency-check phase, followed by garbled `PartNameMG`/`ConvertSpinToString[0]` output contaminating unrelated, purely-SM flavor-indexed vertices later in the same session — the same failure signature (widespread corruption of vertices unrelated to the edited term) that Attempt 1 diagnosed correctly in kind, just for a different symbol.

I replaced the term with its exact equivalent, `(gZRNR/2) bar[HN[ii]].Ga[mu].Ga[5].HN[ii]`, which preserves the identical physical coupling strength and flavor-diagonal structure while using the standard, robust axial-current form for a self-paired Majorana bilinear. No field content, quantum numbers, other operator structures, or parameter values were changed.

One caveat for the next round: the `mass_diagonal`/`mass_spectrum` failures cite the WR-quark charged-current term (`gWRq·CKMR[i,j]·bar[u].Ga[mu].ProjP.d·WR[mu]`) directly and fairly cleanly, which is consistent with either (a) being a corrupted echo of the same crash (my leading hypothesis, since there is no genuine scalar mass-mixing term anywhere in the file — `CKMR`, `YR`, `XL` are used exclusively inside vector-current terms, never as bare mass insertions), or (b) a separate limitation in how FeynRules numerically resolves the `External` flavor matrices `CKMR`/`YR`/`XL` during the consistency check. If the checks still fail after this fix, that check's handling of those three matrices is the next place to look — I did not alter them here since their `Value` declarations (diagonal defaults) already match the standard FeynRules convention and changing them further would have required either guessing at internal FeynRules check semantics or reducing the matrices' external tunability, which would go beyond a purely technical fix.

Validation outcome AFTER that change: status=compiled, hermiticity=pass, kinetic_diagonal=pass, mass_diagonal=fail, mass_spectrum=inconclusive, madgraph_import=False, tags=mass_diagonal_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=255.1

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=pass, kinetic_diagonal=pass, mass_diagonal=fail, mass_spectrum=inconclusive, madgraph_import=False, tags=builtin_symbol_collision, selfconjugate_quantum_numbers, mass_diagonal_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=311.3
