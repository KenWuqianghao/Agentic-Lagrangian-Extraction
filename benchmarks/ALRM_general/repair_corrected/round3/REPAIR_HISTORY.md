# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
I made two fixes to `model.fr` in place, both technical, both leaving the physics content untouched.

**Fix 1 — undefined symbol (`Phihat` → `phihat`).** Line 474 defines the tilde bidoublet as `phihat = sig2.Phi.sig2` (lowercase). The Yukawa Lagrangian `LYALRM` on line 482 referred to it as `Phihat` (capital P) in both occurrences of the up-type-quark term. Mathematica is case-sensitive, so `Phihat` was a separate, never-assigned symbol, leaving an undefined field sitting inside the Lagrangian. That is exactly the kind of defect that makes `WriteUFO` abort before FeynRules can even attempt `CheckHermiticity`, `CheckDiagonalKineticTerms`, `CheckDiagonalMassTerms`, or `CheckMassSpectrum` — matching the report's "UFO compile: FAILED" with all four checks "not reached" and no compile log. Every other use of the tilde field in `VHALRM` already used the correct lowercase `phihat`, confirming this was an isolated typo, not a naming choice.

**Fix 2 — missing `LTot`.** The file defined five Lagrangian pieces (`LYALRM`, `VHALRM`, `LSALRM`, `LFALRM`, `LeffALRM`) but never combined them into the required final `LTot := ...;` assignment that `WriteUFO` needs as its entry point. I added:

```
LTot := LYALRM + LSALRM + LFALRM + LeffALRM;
```

as the new last line. `VHALRM` (the scalar potential) is intentionally excluded from this sum because it is already folded into `LSALRM` (`LSALRM = kinetic terms - VHALRM`); adding it again would double-count the potential.

No fields, quantum numbers, couplings, or parameter values were changed. File: `/private/tmp/claude-501/-Users-kenwu-Documents-Github-Agentic-Lagrangian-Extraction/94cf8ff6-6dba-453e-b8ee-ad80d63999c8/scratchpad/hmain/eval/benchmark_runs/ALRM_general/repair_corrected/round1/model.fr`.

Validation outcome AFTER that change: status=compile_timeout, hermiticity=None, kinetic_diagonal=None, mass_diagonal=None, mass_spectrum=None, madgraph_import=None, tags=compile_timeout, selfconjugate_quantum_numbers, compile_seconds=900.1

## Attempt 2
What was changed (the agent's own summary):
`M$vevs -> {Phi[2,2], ...}` and `phihat = sig2.Phi.sig2`). The file already declares `IndexRange` for its two other custom index types (`Scalar4`, `Scalar2`) but was missing the equivalent declaration for `SU2D`, so FeynRules treated that index as length 1 instead of 2, producing a dimension mismatch that plausibly forced expensive, unresolved symbolic branches during the Lagrangian processing that led to the compile timeout. I added `IndexRange[Index[SU2D]] = NoUnfold[Range[2]];` next to the existing two declarations, following the same established pattern.

**Fix 2 — self-conjugate fields declared with quantum numbers.** The log also reports the recurring warning `LoadModel::QN: Selfconjugated fields should not carry quantumnumbers`, matching the harness's `selfconjugate_quantum_numbers` tag. Three classes are declared `SelfConjugate -> True` but still carried a `QuantumNumbers -> {Q -> 0}` entry: `Zp` (V[31]), `h0` (S[31]), and `A0` (S[32]). Per the hard rules ("self-conjugate (Majorana/real) fields declared with quantum numbers" is an explicitly listed defect), I removed the `QuantumNumbers -> {Q -> 0}` line from all three declarations; charge neutrality is already implicit for a self-conjugate field, so no physics content is lost. `Wp` and `Hp` were left untouched since they are correctly declared `SelfConjugate -> False` with nonzero charge.

I left the `Value -> Internal` placeholders on `lam1`, `MH02`, `MH03` alone: they already existed before round 1's fix (which reached the same `compile_timeout` outcome), so they aren't implicated in the current failure mode, and guessing at the closed-form mass-matrix formulas from the cited appendix equations without the source paper risked introducing wrong physics rather than fixing a technical defect.

File edited: `/private/tmp/claude-501/-Users-kenwu-Documents-Github-Agentic-Lagrangian-Extraction/94cf8ff6-6dba-453e-b8ee-ad80d63999c8/scratchpad/hmain/eval/benchmark_runs/ALRM_general/repair_corrected/round2/model.fr`

Validation outcome AFTER that change: status=compile_timeout, hermiticity=None, kinetic_diagonal=None, mass_diagonal=None, mass_spectrum=None, madgraph_import=None, tags=compile_timeout, compile_seconds=900.1

## For reference — the ORIGINAL model's outcome before any repair:
status=no_lagrangian_symbol, hermiticity=None, kinetic_diagonal=None, mass_diagonal=None, mass_spectrum=None, madgraph_import=None, tags=none, compile_seconds=None
