# Option A, first result: the mass-basis wall falls on pNG (2026-09-22)

Question: can an add-on model pass `CheckDiagonalMassTerms` when a new
scalar mixes with the SM Higgs, given that the Higgs doublet is declared in
`SM.fr`? Seven of the nine models still open after the repair loop fail this
check, and the repair agent on B-L-SM wrote that the fix "must live in the SM
doublet Phi's Definitions, declared in the externally supplied SM.fr,
outside this task's editable scope".

## The evidence in the stored run

The pNG dark-matter one-shot from the tools arm
(`pNG/repair_corrected/round0/model.fr`) already did the physics:

- it redeclared the Higgs doublet, `S[11] == { ClassName -> Phi, ...
  Definitions -> {Phi[2] -> (vh + (ct h + st h2) + I G0)/Sqrt[2]} }`;
- it declared the singlet `S` as an unphysical mixture
  `(vs + (-st h + ct h2) + I X)/Sqrt[2]`;
- it wrote the three quartics and the two mass parameters as functions of
  the physical masses and the angle (the inverted parametrisation).

Checked with sympy (`massbasis.py` has the general derivation; the file's own
conventions were checked directly): tadpoles vanish, the diagonal entries are
`MH^2`, `Mh2^2`, `mX^2`, and every cross term is identically zero.

It failed the mass check, Hermiticity and the harness anyway, for three
reasons that are not physics:

1. it used `h`, `vh` and `Mh` where `SM.fr` declares `H`, `vev` and `MH`
   (undeclared symbols; the lint from option E flags the redeclared class);
2. the harness prepended the whole SM Lagrangian, so `LHiggs` from `SM.fr`
   (with the SM's own `Phi`) and the add-on's Higgs sector were both
   present;
3. three repair rounds, told not to change the physics, declined to touch
   the mixing.

## The corrected file

`massbasis_pNG/model.fr` differs from the stored file in exactly the three
names and one line:

```
LTotal := LSM - LHiggs + LScalarPng;
```

The add-on's total reaches `LSM`, so the harness passes it through as is,
and subtracting `LHiggs` replaces the SM Higgs sector with the add-on's
rotated one. Four `InteractionOrder` lines were added so MadGraph accepts
the new vertices.

## Result, corrected harness (heptapod-dev main driver, checks from return values)

| stage | verdict |
|---|---|
| FeynRules compile | ok, 75 s |
| Hermiticity | pass |
| kinetic terms diagonal | pass |
| mass terms diagonal | **pass** |
| mass spectrum | pass |
| MadGraph import | ok |
| full chain | **pass** |

Proof that the override reached the SM sector: the UFO's `h2 t t~` vertex
carries `GC_68 = -(I st yt)/Sqrt[2]`, the sin-theta-rescaled top Yukawa that
only exists if the SM `LYukawa` was evaluated with the redeclared doublet.
25 vertices involve `h2`, 8 of them mixed `H h2` scalar vertices.

Files: `massbasis_pNG/model.fr`, `result.json`, `compile.log`, `mg5.log`;
runner `run_one_fr.py` (expects the heptapod-dev `main` tree, with
`validation_benchmark.py` copied to its `eval/benchmark_runs/`).

## What follows

- **The toolkit feature is small.** An `sm_overrides` slot in the schema:
  the renderer emits the redeclared SM class and writes the total as
  `LSM - <replaced term> + <add-on>`. The mass-basis derivation is the
  `massbasis.py` prototype (FeynRules' mixing module and ASperGe for the
  general case).
- **Next models in this class.** B-L-SM (its round-3 file already has the
  singlet rotation and the overridden `lam`; it needs the `Phi`
  redeclaration and the total; its seesaw sector is a second, separate
  mixing), then the dilaton and the leptoquark potential.
- **What this changes in the headline.** The dominant failure class of the
  16-paper benchmark is reachable from inside the toolkit, with a
  derivation the agents already produce and refuse to apply without a tool.
