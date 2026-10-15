# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
ndefined symbol LZpF". Fixing the parenthesis resolves this.

3. **Built-in symbol collision (`builtin_symbol_collision`)**: the right-handed-neutrino field class was named `ClassName -> N`, which collides with Mathematica's built-in numeric function `N[]` (this produced the `N::argt: N called with 3 arguments` errors in the log). Renamed the class to `NR` everywhere it is used as a field in the Lagrangian (`N[...]`→`NR[...]`, `Nbar[...]`→`NRbar[...]` in `LZpF`, `LNuDiracYuk`, `LNuMajoranaYuk`). The distinct mass-eigenstate symbols `N1, N2, N3` (ClassMembers, PDG names) were left untouched since they never collide with `N[]`.

4. **Self-conjugate fields with quantum numbers (`selfconjugate_quantum_numbers`)**: `Zp`, `NR` (formerly `N`), `phiX`, and `GZp` are all declared `SelfConjugate -> True` but also carried a `QuantumNumbers -> {...}` entry, which FeynRules flags as invalid for self-conjugate fields. Removed the `QuantumNumbers` line from all four of these classes. Left `PhiX` (the unphysical, non-self-conjugate complex scalar) untouched since its `X -> 2*xPhi` charge is legitimate and needed there.

Additionally, per the task's hard rule that the total Lagrangian must be the last top-level assignment named `LTot`, I renamed the final assignment from `LGeneralU1` to `LTot` (content unchanged: `LZpF + LPhiXKin + LHiggsX - VPhiX + LNuDiracYuk + HC[LNuDiracYuk] + LNuMajoranaYuk`).

No physics content was altered — same fields, same quantum numbers (aside from removing the invalid tags on self-conjugate particles), same operator structure, and same parameter values. The Hermiticity structure was already correct (Dirac Yukawa term paired with its own `HC[...]`, Majorana term already self-Hermitian via its `ProjP`/`ProjM` pair) and mass-diagonal structure was already correct (single generation index per field in mass terms), so no changes were needed there. `REPAIR_HISTORY.md` and `UFO/` were not present in this round, so there was no prior history to avoid repeating.

Validation outcome AFTER that change: status=compiled, hermiticity=pass, kinetic_diagonal=pass, mass_diagonal=pass, mass_spectrum=fail, madgraph_import=False, tags=mass_spectrum_fail, mg5_import_fail, mg5_python_traceback, compile_seconds=61.2

## For reference — the ORIGINAL model's outcome before any repair:
status=compile_failed, hermiticity=None, kinetic_diagonal=None, mass_diagonal=None, mass_spectrum=None, madgraph_import=None, tags=lag_symbol_undefined, fr_syntax_error, builtin_symbol_collision, selfconjugate_quantum_numbers, compile_seconds=17.8
