# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
LIDATION_REPORT.md`'s "(no compile log)" result with every downstream check listed as "not reached."

The fix: appended one line at the end of the file,
```
LTot := LHiggs331 + LGauge331Mass + LYukawaQuark331 + LYukawaLepton331 + LFermionGauge331 + LZpFermions331 + LGaugeSelf331 + LScalarFermion331;
```
This sums every previously-defined BSM term with no omissions, satisfies the hard requirement that `LTot` be the last top-level assignment built only from symbols defined above it, and does not touch any field content, quantum numbers, parameter values, or operator structure — it only wires the already-written pieces into the required total.

I verified there are no reserved-word collisions (`N, C, D, E, I, K, O`) among any `ClassName`/`ParameterName` entries, no obviously unbalanced brackets in `M$Parameters`/`M$ClassesDescription`/`M$MixingsDescription`, and that each individual Lagrangian term already carries its explicit `+ HC[...]` conjugate where needed for Hermiticity (Higgs potential trilinear term, both Yukawa blocks). I did not alter the cosmetic double-backslash TeX label strings (e.g. `"\\\\beta"`) since they only affect diagram-label rendering, not any of the four FeynRules checks or MadGraph import, and touching them would be out of scope for a minimal technical fix.

One caveat for the next round if this still fails: several symbols referenced inside `LFermionGauge331`, `LZpFermions331`, and `LScalarFermion331` (e.g. `qL`, `uR`, `dR`, `lL`, `eR`, `JR`, `TR`, `ER`, `psi`, generic `f`, `GHZpL[f]`/`GHZpR[f]`, `VVV[mu,nu,rho]`, and the gauge-basis scalar components `xirho`/`zetarho`/`etaP`/`rhoP`/`chiQY`/`etaQY`/`chiQV`/`rhoQV`) are never declared anywhere in this file as classes, parameters, or component-field definitions. If the validation still fails after this round, that missing declaration/definition layer (not addressed here, since it would require substantial new structure rather than a minimal technical correction) is the most likely next culprit.

Validation outcome AFTER that change: status=compile_failed, hermiticity=None, kinetic_diagonal=None, mass_diagonal=None, mass_spectrum=None, madgraph_import=None, tags=mixing_declaration_error, selfconjugate_quantum_numbers, wolfram_aborted, compile_seconds=17.3

## Attempt 2
What was changed (the agent's own summary):
 not carry quantumnumbers`, tag `selfconjugate_quantum_numbers`). The four particles declared `SelfConjugate -> True` — `H2`, `H3`, `H0` (scalars) and `Zp` (vector) — each also carried a `QuantumNumbers -> {Q -> 0, ColourRep -> 1, SU2Rep -> 1}` entry. Since a self-conjugate field is by definition neutral under all these charges, I removed the redundant `QuantumNumbers` line from all four class declarations (nothing else in those declarations changed). No physics content was altered: the values were already trivial (Q=0, singlet color, singlet SU2Rep), so no charge, mass, width, or PDG assignment changed.

No fields, quantum numbers (for charged particles), operator structure, or parameter values were touched otherwise.

One open risk for a possible next round, carried over from the prior repair attempt's note: several symbols used deep in the gauge/fermion interaction terms (`LFermionGauge331`, `LZpFermions331`, `LScalarFermion331`, `LGaugeSelf331`) — e.g. `psi`, `f`, `GHZpL`, `GHZpR`, `VVV`, `qL`, `uR`, `dR`, `lL`, `eR`, `JR`, `TR`, `ER`, and the gauge-basis scalar components `xirho`, `zetarho`, `etaP`, `rhoP`, `chiQY`, `etaQY`, `chiQV`, `rhoQV` — are never declared as classes, parameters, or component-field substitutions in this file. These look like paper-notation placeholders (implicit sums over generic fermion species, an undefined triple-gauge tensor `VVV`, and un-expanded scalar-triplet components) rather than valid FeynRules constructs. I left them untouched this round since resolving them would require substantial new structural content (declaring chiral field classes and gauge-basis component substitutions) rather than a minimal technical fix, and the current validation failure occurred earlier in the pipeline (before Lagrangian evaluation) so their effect on the check chain isn't yet confirmed. If the tool chain still fails after this round with an "undefined Lagrangian symbol" error, that undefined-symbol layer is the most likely next culprit to address.

Validation outcome AFTER that change: status=compile_failed, hermiticity=None, kinetic_diagonal=None, mass_diagonal=None, mass_spectrum=None, madgraph_import=None, tags=mixing_declaration_error, wolfram_aborted, compile_seconds=15.3

## For reference — the ORIGINAL model's outcome before any repair:
status=no_lagrangian_symbol, hermiticity=None, kinetic_diagonal=None, mass_diagonal=None, mass_spectrum=None, madgraph_import=None, tags=none, compile_seconds=None
