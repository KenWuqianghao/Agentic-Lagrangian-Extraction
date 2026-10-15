# Model dossier — `ALRM_general`

**Status: never cleared the chain.** Multi-member `ClassMembers` scalar classes serialize to invalid UFO Python (2D-typeset exponents, `PRIVATE\`` internals). Every attempt to restructure them either re-broke the model or exceeded the compile budget. Best fixed deterministically in the generator, not by a repair agent.

This dossier is not a completed reverse-check review package. It collects what exists for this model so you can read the physics without opening the source files. Where a full review package does exist for a model, it is the `REVIEW.pdf` in that model's directory.

| item | value |
|---|---|
| model | `ALRM_general` |
| chain status | did not pass |
| Lagrangian source | `repair3/round3/model.fr (last attempt)` |
| Lagrangian terms found | 9 |

## Why this model matters to you

The loop could not get this model through the chain. It is included so the picture is the whole benchmark, not only the successes. The Lagrangian below is the best attempt the loop produced; treat it as a draft that is known not to validate.

## Verbatim Lagrangian terms

Quoted unmodified from the `.fr`. These are the terms any reconstruction would have to account for.

### `phihat` (`:=`)

```mathematica
sig2.Phi.sig2
```

### `chiLhat` (`:=`)

```mathematica
I sig2.chiL
```

### `chiRhat` (`:=`)

```mathematica
I sig2.chiR
```

### `LYALRM` (`:=`)

```mathematica
Yu[i,j] HC[QL[i]].phihat.QR[j] - Yd[i,j] HC[QL[i]].chiL.dR[j] - Ydp[i,j] HC[QR[i]].chiR.dPL[j] - Ye[i,j] HC[LL[i]].Phi.LR[j] + Ynu[i,j] HC[LL[i]].chiLhat.nuR[j] + Yn[i,j] HC[LR[i]].chiRhat.nL[j] + HC[Yu[i,j] HC[QL[i]].phihat.QR[j] - Yd[i,j] HC[QL[i]].chiL.dR[j] - Ydp[i,j] HC[QR[i]].chiR.dPL[j] - Ye[i,j] HC[LL[i]].Phi.LR[j] + Ynu[i,j] HC[LL[i]].chiLhat.nuR[j] + Yn[i,j] HC[LR[i]].chiRhat.nL[j]]
```

### `VHALRM` (`:=`)

```mathematica
-mu1sq Tr[HC[Phi].Phi] - mu2sq (HC[chiL].chiL + HC[chiR].chiR) + lam1 Tr[HC[Phi].Phi]^2 + lam2 (Phi.phihat) (HC[phihat].HC[Phi]) + lam3 ((HC[chiL].chiL)^2 + (HC[chiR].chiR)^2) + 2 lam4 (HC[chiL].chiL) (HC[chiR].chiR) + 2 alp1 Tr[HC[Phi].Phi] (HC[chiL].chiL + HC[chiR].chiR) + 2 alp2 ((HC[chiL].Phi) (chiL.HC[Phi]) + (HC[Phi].HC[chiR]) (Phi.chiR)) + 2 alp3 ((HC[chiL].HC[phihat]) (chiL.phihat) + (phihat.HC[chiR]) (HC[phihat].chiR)) + kap (HC[chiL].Phi.chiR + HC[chiR].HC[Phi].chiL)
```

### `LSALRM` (`:=`)

```mathematica
DC[Phi,mu] HC[DC[Phi,mu]] + DC[chiL,mu] HC[DC[chiL,mu]] + DC[chiR,mu] HC[DC[chiR,mu]] - VHALRM
```

### `LFALRM` (`:=`)

```mathematica
I HC[nl].Ga[mu].DC[nl,mu] + I HC[dqp].Ga[mu].DC[dqp,mu]
```

### `LeffALRM` (`:=`)

```mathematica
-1/4 Ghgg h0 FS[G,mu,nu,a] FS[G,mu,nu,a] - 1/4 Ghaa h0 FS[A,mu,nu] FS[A,mu,nu]
```

### `LTot` (`:=`)

```mathematica
LYALRM + LSALRM + LFALRM + LeffALRM
```

## The last failure the loop worked on

This is the validation report handed to the repair agent at the start of `repair3/round3` — the problem it was asked to fix. The model still did not pass after this round.

# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: FAILED (TIMED OUT — the compile exceeded the time limit; the model may need simplification of redundant/expanded terms, without changing the physics)
- Hermiticity check: not reached
- Kinetic-terms check: not reached
- Mass-spectrum check: not reached
- MadGraph import: not reached
- Heuristic error tags: compile_timeout

## FeynRules / Wolfram Engine output (tail)
```
[INFO] Loading via explicit file: $FEYNRULES_PATH/FeynRules.m
 - FeynRules - 
Version: 2.3.49 (*29 September 2021).
Authors: A. Alloul, N. Christensen, C. Degrande, C. Duhr, B. Fuks
 
Please cite:
    - Comput.Phys.Commun.185:2250-2300,2014 (arXiv:1310.1921);
    - Comput.Phys.Commun.180:1614-1641,2009 (arXiv:0806.4194).
 
http://feynrules.phys.ucl.ac.be
 
The FeynRules palette can be opened using the command FRPalette[].
[INFO] Loading SM from: $FEYNRULES_PATH/Models/SM/SM.fr
From kernel 1 (Local):
ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.
From kernel 2 (Local):
ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.
From kernel 4 (Local):
ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.
From kernel 6 (Local):
ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.
From kernel 3 (Local):
ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.

General::stop: Further output of ToExpression::argb will be suppressed during this calculation.
From kernel 1 (Local):
Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.
From kernel 2 (Local):
Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.
From kernel 3 (Local):
Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.
From kernel 6 (Local):
Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.
From kernel 7 (Local):
Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.

General::stop: Further output of Length `1` of dimension `2` in `3` is incommensurate with length `4` of dimension 1 in `5`. will be suppressed during this calculation.
Merging model-files...
This model implementation was created by
Mariana Frank
Benjamin Fuks
Ozer Ozdal
Model Version: 1.0
For more information, type ModelInformation[].

   - Loading particle classes.

ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.
   - Loading gauge group classes.
   - Loading parameter classes.

Model ALRM_general_gen loaded.

Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.

Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.
[INFO] Total Lagrangian: LSM + LTot
[INFO] Running FeynRules consistency checks.
HEPTAPOD-CHECK-BEGIN: hermiticity
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.

```

## Repair history

What the loop tried, and what each attempt measured.

# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: I added explicit `Indices -> {Index[Scalar4]}` / `Indices -> {Index[Scalar2]}` to the multi-member scalar classes `h0`, `A0`, and `Hp`, which fixes the malformed `Index[{}[[1]]]` structures leaking into the generated UFO; removed trivial `Q -> 0` quantum-number declarations from self-conjugate neutral classes `Zp`, `h0`, and `A0`; and added the required final top-level `LTot := LYALRM + LSALRM + LFALRM + LeffALRM;` assignment so the total BSM Lagrangian is defined last.

Validation outcome AFTER that change: status=compile_timeout, hermiticity=None, kinetic=None, mass=None, madgraph_import=None, tags=compile_timeout, compile_seconds=5274.4

## Attempt 2
What was changed (the agent's own summary):
Updated `model.fr` by undoing the timeout-causing artificial scalar flavor indices and splitting `h0/h01/h02/h03`, `A01/A02`, and `Hp1/Hp2` into separate scalar classes instead of indexed multiplets. This preserves the same fields, masses, widths, charges, and Lagrangian terms, while avoiding the malformed empty-index UFO serialization and the heavy scalar-flavor expansion that caused the compile timeout; I also assigned `h01` a unique PDG code and kept `LTot := LYALRM + LSALRM + LFALRM + LeffALRM;` as the final top-level assignment.

Validation outcome AFTER that change: status=compile_timeout, hermiticity=None, kinetic=None, mass=None, madgraph_import=None, tags=compile_timeout, compile_seconds=5240.8

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=selfconjugate_quantum_numbers, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=37.1

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:
