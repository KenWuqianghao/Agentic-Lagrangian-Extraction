# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
I fixed the model by correcting the treatment of the right-handed neutrino field `vR`.

What I changed, in `model.fr`:

1. **`vR` class**: changed `SelfConjugate -> False` to `SelfConjugate -> True`, and removed the `AntiParticleName -> {"veR~", "vmR~", "vtR~"}` line.
2. **Mass term**: changed `LkinNuR` from `- MvR bar[vR][sp1,i].vR[sp1,i]` to `- 1/2 MvR bar[vR][sp1,i].vR[sp1,i]`.

Why this was needed. `vR` has only one chirality (`Chirality -> R`) and no left-handed partner class. A field with a single chirality cannot carry a Dirac mass — the bilinear `bar[psi].psi` is identically zero for a purely chiral 4-component spinor. This is why FeynRules could not read the mass term: it saw a term that did not fit its Dirac mass pattern, so it flagged the mass matrix as non-diagonal and could not compute the mass spectrum.

The physical intent here is a heavy Majorana right-handed neutrino, the standard field content for this class of W' + right-handed-neutrino model. Marking `vR` as `SelfConjugate -> True` tells FeynRules to build the full 4-component Majorana field from the right-handed piece and its charge conjugate. With that field structure, `bar[vR].vR` is a valid, non-zero mass bilinear. The standard Majorana mass convention has a `1/2` coefficient (so the pole mass equals the declared `MvR`), so I added that factor. I also removed `AntiParticleName`, because a self-conjugate (Majorana) particle is its own antiparticle — keeping a separate antiparticle name conflicts with `SelfConjugate -> True` and would show up as a duplicate-name error.

No other fields, couplings, or parameter values were touched. The `Wp` mass term, the W'-fermion coupling terms, and quantum numbers are unchanged, so the physics content (charges, couplings, mixing matrices) is preserved.

Validation outcome AFTER that change: status=compiled, hermiticity=pass, kinetic_diagonal=pass, mass_diagonal=fail, mass_spectrum=inconclusive, madgraph_import=True, tags=selfconjugate_quantum_numbers, mass_diagonal_fail, compile_seconds=112.9

## Attempt 2
What was changed (the agent's own summary):
The file now reads correctly and both fixes are in place. This is my final report.

Summary of changes to `model.fr`:

1. **Removed the extra spin index in the Majorana mass bilinear.** `LkinNuR` wrote the mass term as `bar[vR][sp1,i].vR[sp1,i]`, pinning the same explicit spinor index `sp1` on both sides and then joining them with `.` — the FeynRules convention for a plain mass bilinear (no Dirac matrix in between) is to leave the spinor index out entirely and let `.` do the implicit spin contraction, as in `bar[vR][i].vR[i]`. The stray `sp1` left a dangling spin-space structure that FeynRules could not reduce to a plain number, which is exactly why `mass_diagonal` failed with "not numerical value encountered ... Non diagonal mass term found" and `mass_spectrum` came back inconclusive — both symptoms untouched by the prior repair attempt because that attempt never touched this line. I changed the term to `- 1/2 MvR bar[vR][i].vR[i]`, keeping the Majorana `1/2` factor and the generation index `i`, so the mass matrix is now a clean, manifestly diagonal `MvR` times the identity, matching the declared `Mass -> {MvR, 100.}`.

2. **Removed `QuantumNumbers -> {Q -> 0}` from the self-conjugate `vR` class.** A self-conjugate (Majorana) field must not carry an explicit `QuantumNumbers` declaration (it triggered the `LoadModel::QN` warning and the `selfconjugate_quantum_numbers` heuristic tag); dropping the line removes the warning without changing any physics, since the field was already neutral.

No fields, couplings, masses, or interaction terms were otherwise altered — the `Wp` sector, the W′–fermion coupling terms, and all parameter values are untouched, so the physics content is preserved while only the two technical FeynRules-syntax/declaration defects were corrected.

Validation outcome AFTER that change: status=compiled, hermiticity=pass, kinetic_diagonal=pass, mass_diagonal=fail, mass_spectrum=inconclusive, madgraph_import=True, tags=mass_diagonal_fail, compile_seconds=114.9

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=pass, kinetic_diagonal=pass, mass_diagonal=fail, mass_spectrum=inconclusive, madgraph_import=True, tags=mass_diagonal_fail, compile_seconds=99.7
