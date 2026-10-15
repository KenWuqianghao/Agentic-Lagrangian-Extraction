I inspected `model.fr`, `VALIDATION_REPORT.md`, and `REPAIR_HISTORY.md`. Two prior repair rounds already fixed the obvious defects in the right-handed-neutrino sector (`SelfConjugate -> True` declaration, dropped stray `AntiParticleName`, removed the extraneous `sp1` index and added the Majorana `1/2` factor in the mass bilinear), yet `mass_diagonal` still failed identically to the original, unrepaired model — a strong signal the true defect was never touched by those edits.

Root cause found: in `LkinNuR`, the kinetic and mass terms for the 3-generation Majorana field `vR` were wrapped in an explicit `Sum[..., {i,1,3}]` with `i` also declared as a `Block`-local variable:

```
LkinNuR = Block[{mu,sp1,sp2,i}, Sum[I bar[vR][sp1,i].Ga[mu,sp1,sp2].del[vR[sp2,i],mu] - 1/2 MvR bar[vR][i].vR[i], {i,1,3}]];
```

Because `{i,1,3}` has explicit numeric bounds, Mathematica evaluates this `Sum` eagerly at load time, before FeynRules's own engine ever processes the Lagrangian. That expansion replaces the flavor index `i` with bare integer literals (1, 2, 3), stripping away the `Index[Generation]` tag FeynRules needs to recognize `vR`'s mass term as belonging to a proper 3×3 flavor structure over the class's `ClassMembers`. This is exactly consistent with the reported symptom: `CheckDiagonalMassTerms` could not resolve the term to a clean numeric diagonal matrix ("not numerical value encountered ... Unable to decide whether mass term is diagonal"), and `CheckMassSpectrum` then came back inconclusive as a direct consequence.

Every other flavor-diagonal term in the file (e.g. `LkinWp`) is written without an explicit `Sum`, relying on FeynRules's native automatic summation over repeated `Index[Generation]`/spinor/Lorentz indices — the standard, idiomatic convention (matching how `SM.fr` itself writes flavor-diagonal kinetic terms). `LkinNuR` was the one term that deviated from this pattern and combined it with a degenerate, non-flavor-dependent mass coefficient, which made the `Sum` wrapper both unnecessary and harmful.

Fix applied (the only change in this round): removed the `Sum[...]` wrapper from `LkinNuR`, letting the repeated Generation index `i` (and the spinor/Lorentz indices) auto-sum via FeynRules's own index-contraction engine, matching the file's own established style elsewhere:

```
LkinNuR = Block[{mu,sp1,sp2,i}, I bar[vR][sp1,i].Ga[mu,sp1,sp2].del[vR[sp2,i],mu] - 1/2 MvR bar[vR][i].vR[i]];
```

No fields, quantum numbers, couplings, or parameter values were changed — the `Wp` sector, the `VpLQ`/`VpRQ`/`VpLL`/`VpRL` mixing structure, and all masses/widths are untouched (the two `Sum`-wrapped charged-current interaction terms, `LWpQuarkNonHC`/`LWpLeptonNonHC`, were deliberately left as-is since they are genuine 3-point vertices with non-trivial two-index mixing matrices, are excluded from the 2-point mass check, and were never implicated by the failure). This is a purely technical fix to how the Majorana mass/kinetic term's flavor index was declared.

File modified: `/private/tmp/claude-501/-Users-kenwu-Documents-Github-Agentic-Lagrangian-Extraction/94cf8ff6-6dba-453e-b8ee-ad80d63999c8/scratchpad/hmain/eval/benchmark_runs/Wprime/repair_corrected/round3/model.fr` (line 141).