# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
** `LChernSimonsPortal` (the gauge-invariant D'Hoker-Farhi operator) contains `HC[H].H` in a denominator, which is non-polynomial in the Higgs field and cannot be expanded into UFO vertices. Since the model runs in unitary gauge (`FeynmanGauge = False`) and the file already supplies the equivalent post-EWSB, polynomial, mass-eigenstate realization (`LChernSimonsPortalBroken`, written in `Z`, `A`, `W`, `xb`), I built `LTot` only from that polynomial piece. `LChernSimonsPortal` is left in the file, unreferenced, purely as documentation of the parent EFT operator — it is never evaluated, so it is harmless.

3. **Non-Hermitian charged-current term.** `c2 xb[mu] W[nu] HC[del[W[ro], la]] Eps[mu, nu, la, ro]` involves the complex `W` field but had no `+ HC[...]` conjugate, so `L - HC[L]` was nonzero (fails `CheckHermiticity`). Rewrote it as `c2 xb[mu] (W[nu] HC[del[W[ro], la]] + HC[W[nu]] del[W[ro], la]) Eps[mu, nu, la, ro]`, i.e. explicitly adding the term's own Hermitian conjugate, which restores a real Lagrangian while keeping the same operator structure and coefficient `c2`.

4. **Missing kinetic and mass terms for the new field `xb`.** `xb` is declared in `M$ClassesDescription` with `Mass -> {Mxb, 1.}`, but no term in the Lagrangian actually gives it a kinetic term or a mass term — so `CheckDiagonalKineticTerms` and `CheckMassSpectrum` had nothing to diagonalize/compare against the declared `Mxb` (the classic "declared Mass with no matching mass term" defect), and MadGraph would have no valid propagator for it. Added a standard free Proca Lagrangian for the self-conjugate vector: `LXKin := -1/4 FS[xb, mu, nu] FS[xb, mu, nu] + 1/2 Mxb^2 xb[mu] xb[mu];`, included in `LTot`.

All original fields, quantum numbers, couplings (`c1`, `c2`), and the portal operator structure from arXiv:0901.0639 are preserved unchanged; only the missing/malformed technical pieces (total-Lagrangian wiring, Hermiticity completion, and the new particle's free Lagrangian) were added or corrected.

Validation outcome AFTER that change: status=no_lagrangian_symbol, hermiticity=None, kinetic_diagonal=None, mass_diagonal=None, mass_spectrum=None, madgraph_import=None, tags=none, compile_seconds=None

## For reference — the ORIGINAL model's outcome before any repair:
status=no_lagrangian_symbol, hermiticity=None, kinetic_diagonal=None, mass_diagonal=None, mass_spectrum=None, madgraph_import=None, tags=none, compile_seconds=None
