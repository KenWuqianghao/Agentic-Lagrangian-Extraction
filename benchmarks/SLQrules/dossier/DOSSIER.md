# Model dossier — `SLQrules`

**Status: never cleared the chain.** A residual SU(2)-multiplet covariant-derivative Hermiticity violation, surviving nine repair rounds. This one is genuinely hard physics rather than a tooling gap, and is the most interesting of the three to look at.

This dossier is not a completed reverse-check review package. It collects what exists for this model so you can read the physics without opening the source files. Where a full review package does exist for a model, it is the `REVIEW.pdf` in that model's directory.

| item | value |
|---|---|
| model | `SLQrules` |
| chain status | did not pass |
| Lagrangian source | `repair3/round3/model.fr (last attempt)` |
| Lagrangian terms found | 6 |

## Why this model matters to you

The loop could not get this model through the chain. It is included so the picture is the whole benchmark, not only the successes. The Lagrangian below is the best attempt the loop produced; treat it as a draft that is known not to validate.

## Verbatim Lagrangian terms

Quoted unmodified from the `.fr`. These are the terms any reconstruction would have to account for.

### `LQ2Phi` (`:=`)

```mathematica
Module[{a, b, c, d, sw, tw, uw, aa},
  ExpandIndices[
    -(m12 + Y1 HC[Phi[a]] Phi[a]) HC[S1[aa]] S1[aa]
    - (m1t2 + Y1t HC[Phi[a]] Phi[a]) HC[S1t[aa]] S1t[aa]
    - (m22 + Y2 HC[Phi[a]] Phi[a]) HC[R2[b,aa]] R2[b,aa]
    - (m2t2 + Y2t HC[Phi[a]] Phi[a]) HC[R2t[b,aa]] R2t[b,aa]
    - (m32 + Y3 HC[Phi[a]] Phi[a]) HC[S3[sw,aa]] S3[sw,aa]
    - Y22 HC[Phi[a] Eps[a,b] R2[b,aa]] Phi[c] Eps[c,d] R2[d,aa]
    - Y2t2t HC[Phi[a] Eps[a,b] R2t[b,aa]] Phi[c] Eps[c,d] R2t[d,aa]
    - I Y33 Eps[sw, tw, uw] HC[Phi[a]] Ta[sw,a,b] Phi[b] HC[S3[tw,aa]] S3[uw,aa]
    - (A1t2 HC[R2t[a,aa]] Phi[a] S1[aa]
      + At23 HC[R2t[a,aa]] Ta[sw,a,b] S3[sw,aa] Phi[b]
      + Y2t2 HC[R2[a,aa]] Phi[a] Phi[b] Eps[b,c] R2t[c,aa]
      + Yt13 Phi[a] Eps[a,b] Ta[sw,b,c] HC[S3[sw,aa]] Phi[c] S1t[aa]
      + Y13 HC[Phi[a]] Ta[sw,a,b] S3[sw,aa] Phi[b] HC[S1[aa]]
      + HC[A1t2 HC[R2t[a,aa]] Phi[a] S1[aa]
        + At23 HC[R2t[a,aa]] Ta[sw,a,b] S3[sw,aa] Phi[b]
        + Y2t2 HC[R2[a,aa]] Phi[a] Phi[b] Eps[b,c] R2t[c,aa]
        + Yt13 Phi[a] Eps[a,b] Ta[sw,b,c] HC[S3[sw,aa]] Phi[c] S1t[aa]
        + Y13 HC[Phi[a]] Ta[sw,a,b] S3[sw,aa] Phi[b] HC[S1[aa]]]),
    FlavorExpand -> {SU2D, SU2W}
  ]
]
```

### `LQkin` (`:=`)

```mathematica
Module[{a, sw, aa},
  ExpandIndices[
    DC[HC[S1[aa]], mu] DC[S1[aa], mu]
    + DC[HC[S1t[aa]], mu] DC[S1t[aa], mu]
    + DC[HC[R2[a,aa]], mu] DC[R2[a,aa], mu]
    + DC[HC[R2t[a,aa]], mu] DC[R2t[a,aa], mu]
    + DC[HC[S3[sw,aa]], mu] DC[S3[sw,aa], mu],
    FlavorExpand -> {SU2D, SU2W}
  ]
]
```

### `LQf` (`:=`)

```mathematica
Module[{i, j, a, b, c, sw, aa, bb, cc},
  ExpandIndices[
    Y1RR[i,j] uqbarC[i,aa].ProjR.l[j] HC[S1[aa]]
    + Y1LL[i,j] QbarC[a,i,aa].ProjL.LL[b,j] Eps[a,b] HC[S1[aa]]
    + Y1QLL[i,j] QbarC[a,i,aa].ProjL.Q[b,j,bb] Eps[a,b] S1[cc] Eps[aa,bb,cc]
    + Y1QRR[i,j] uqbarC[i,aa].ProjR.dq[j,bb] S1[cc] Eps[aa,bb,cc]
    + Y1tRR[i,j] dqbarC[i,aa].ProjR.l[j] HC[S1t[aa]]
    + Y1tQRR[i,j] uqbarC[i,aa].ProjR.uq[j,bb] S1t[cc] Eps[aa,bb,cc]
    + Y2RL[i,j] HC[R2[a,aa]] uqbar[i,aa].ProjL.LL[b,j] Eps[a,b]
    + Y2LR[i,j] Qbar[a,i,aa].ProjR.l[j] R2[a,aa]
    + Y2tRL[i,j] HC[R2t[a,aa]] dqbar[i,aa].ProjL.LL[b,j] Eps[a,b]
    + Y3LL[i,j] QbarC[a,i,aa].ProjL.LL[c,j] Eps[a,b] Ta[sw,b,c] HC[S3[sw,aa]]
    + Y3QLL[i,j] QbarC[a,i,aa].ProjL.Q[c,j,bb] Eps[a,b] Ta[sw,b,c] S3[sw,cc] Eps[aa,bb,cc]
    + HC[Y1RR[i,j] uqbarC[i,aa].ProjR.l[j] HC[S1[aa]]
      + Y1LL[i,j] QbarC[a,i,aa].ProjL.LL[b,j] Eps[a,b] HC[S1[aa]]
      + Y1QLL[i,j] QbarC[a,i,aa].ProjL.Q[b,j,bb] Eps[a,b] S1[cc] Eps[aa,bb,cc]
      + Y1QRR[i,j] uqbarC[i,aa].ProjR.dq[j,bb] S1[cc] Eps[aa,bb,cc]
      + Y1tRR[i,j] dqbarC[i,aa].ProjR.l[j] HC[S1t[aa]]
      + Y1tQRR[i,j] uqbarC[i,aa].ProjR.uq[j,bb] S1t[cc] Eps[aa,bb,cc]
      + Y2RL[i,j] HC[R2[a,aa]] uqbar[i,aa].ProjL.LL[b,j] Eps[a,b]
      + Y2LR[i,j] Qbar[a,i,aa].ProjR.l[j] R2[a,aa]
      + Y2tRL[i,j] HC[R2t[a,aa]] dqbar[i,aa].ProjL.LL[b,j] Eps[a,b]
      + Y3LL[i,j] QbarC[a,i,aa].ProjL.LL[c,j] Eps[a,b] Ta[sw,b,c] HC[S3[sw,aa]]
      + Y3QLL[i,j] QbarC[a,i,aa].ProjL.Q[c,j,bb] Eps[a,b] Ta[sw,b,c] S3[sw,cc] Eps[aa,bb,cc]],
    FlavorExpand -> {SU2D, SU2W}
  ]
]
```

### `LQ3Phi` (`:=`)

```mathematica
Module[{a, b, c, sw, tw, uw, aa, bb, cc},
  ExpandIndices[
    A1t2t2 S1[aa] R2t[a,bb] Eps[a,b] R2t[b,cc] Eps[aa,bb,cc]
    + At12t2 S1t[aa] R2[a,bb] Eps[a,b] R2t[b,cc] Eps[aa,bb,cc]
    + Y1t12 S1[aa] S1t[bb] R2[a,cc] Eps[a,b] Phi[b] Eps[aa,bb,cc]
    + Y123 S1[aa] HC[Phi[a]] Ta[sw,a,b] S3[sw,cc] R2[b,bb] Eps[aa,bb,cc]
    + Y1t23 S1[aa] R2t[a,bb] Eps[a,b] Ta[sw,b,c] S3[sw,cc] Phi[c] Eps[aa,bb,cc]
    + Yt123 S1t[aa] R2[a,bb] Eps[a,b] Ta[sw,b,c] S3[sw,cc] Phi[c] Eps[aa,bb,cc]
    + I Y233 HC[Phi[a]] Ta[sw,a,b] R2[b,aa] S3[tw,bb] Eps[sw,tw,uw] S3[uw,cc] Eps[aa,bb,cc]
    + I Yt233 R2t[a,aa] Eps[a,b] Ta[sw,b,c] Phi[c] S3[tw,bb] Eps[sw,tw,uw] S3[uw,cc] Eps[aa,bb,cc]
    + HC[A1t2t2 S1[aa] R2t[a,bb] Eps[a,b] R2t[b,cc] Eps[aa,bb,cc]
      + At12t2 S1t[aa] R2[a,bb] Eps[a,b] R2t[b,cc] Eps[aa,bb,cc]
      + Y1t12 S1[aa] S1t[bb] R2[a,cc] Eps[a,b] Phi[b] Eps[aa,bb,cc]
      + Y123 S1[aa] HC[Phi[a]] Ta[sw,a,b] S3[sw,cc] R2[b,bb] Eps[aa,bb,cc]
      + Y1t23 S1[aa] R2t[a,bb] Eps[a,b] Ta[sw,b,c] S3[sw,cc] Phi[c] Eps[aa,bb,cc]
      + Yt123 S1t[aa] R2[a,bb] Eps[a,b] Ta[sw,b,c] S3[sw,cc] Phi[c] Eps[aa,bb,cc]
      + I Y233 HC[Phi[a]] Ta[sw,a,b] R2[b,aa] S3[tw,bb] Eps[sw,tw,uw] S3[uw,cc] Eps[aa,bb,cc]
      + I Yt233 R2t[a,aa] Eps[a,b] Ta[sw,b,c] Phi[c] S3[tw,bb] Eps[sw,tw,uw] S3[uw,cc] Eps[aa,bb,cc]],
    FlavorExpand -> {SU2D, SU2W}
  ]
]
```

### `LQ4Phi` (`:=`)

```mathematica
Module[{a, b, sw, tw, uw, aa, bb, cc, dd},
  ExpandIndices[
    1/2 Y1x1 HC[S1[aa]] S1[aa] HC[S1[bb]] S1[bb]
    + 1/2 Y1tx1 HC[S1t[aa]] S1t[aa] HC[S1t[bb]] S1t[bb]
    + 1/2 Y2x1 HC[R2[a,aa]] R2[a,aa] HC[R2[b,bb]] R2[b,bb]
    + 1/2 Y2tx1 HC[R2t[a,aa]] R2t[a,aa] HC[R2t[b,bb]] R2t[b,bb]
    + 1/2 Y3x1 HC[S3[sw,aa]] S3[sw,aa] HC[S3[tw,bb]] S3[tw,bb]
    + 1/2 Y2x3 HC[R2[a,aa]] R2[a,bb] HC[R2[b,bb]] R2[b,aa]
    + 1/2 Y2tx3 HC[R2t[a,aa]] R2t[a,bb] HC[R2t[b,bb]] R2t[b,aa]
    + 1/2 Y3x3 HC[S3[sw,aa]] S3[sw,bb] HC[S3[tw,bb]] S3[tw,aa]
    + 1/2 Y3x5 HC[S3[sw,aa]] S3[tw,aa] HC[S3[sw,bb]] S3[tw,bb]
    + ((Y2t2x3 IndexDelta[Index[Colour, aa], Index[Colour, bb]] IndexDelta[Index[Colour, cc], Index[Colour, dd]] + Yprime2t2x3 IndexDelta[Index[Colour, aa], Index[Colour, dd]] IndexDelta[Index[Colour, bb], Index[Colour, cc]]) HC[R2[a,aa]] R2t[a,bb] HC[R2t[b,cc]] R2[b,dd]
      + (Y1223 IndexDelta[Index[Colour, aa], Index[Colour, bb]] IndexDelta[Index[Colour, cc], Index[Colour, dd]] + Yprime1223 IndexDelta[Index[Colour, aa], Index[Colour, dd]] IndexDelta[Index[Colour, bb], Index[Colour, cc]]) HC[S1[aa]] HC[R2[a,cc]] Ta[sw,a,b] S3[sw,dd] R2[b,bb]
      + (Y1t2t23 IndexDelta[Index[Colour, aa], Index[Colour, bb]] IndexDelta[Index[Colour, cc], Index[Colour, dd]] + Yprime1t2t23 IndexDelta[Index[Colour, aa], Index[Colour, dd]] IndexDelta[Index[Colour, bb], Index[Colour, cc]]) HC[S1[aa]] HC[R2t[a,cc]] Ta[sw,a,b] S3[sw,dd] R2t[b,bb]
      + (Y1t22t3 IndexDelta[Index[Colour, aa], Index[Colour, bb]] IndexDelta[Index[Colour, cc], Index[Colour, dd]] + Yprime1t22t3 IndexDelta[Index[Colour, aa], Index[Colour, dd]] IndexDelta[Index[Colour, bb], Index[Colour, cc]]) HC[S1t[aa]] HC[R2[a,cc]] Ta[sw,a,b] S3[sw,dd] R2t[b,bb]
      + (Y1t1t22 IndexDelta[Index[Colour, aa], Index[Colour, bb]] IndexDelta[Index[Colour, cc], Index[Colour, dd]] + Yprime1t1t22 IndexDelta[Index[Colour, aa], Index[Colour, dd]] IndexDelta[Index[Colour, bb], Index[Colour, cc]]) HC[S1[aa]] S1t[bb] HC[R2t[a,cc]] R2[a,dd]
      + 1/2 Y1313 HC[S1[aa]] S3[sw,bb] HC[S1[cc]] S3[sw,dd] Eps[aa,bb,cc] Eps[aa,bb,dd]
      + I Y1333 HC[S1[aa]] S3[sw,bb] HC[S3[tw,cc]] Eps[sw,tw,uw] S3[uw,dd]
      + (HC[Y2t2x3] IndexDelta[Index[Colour, aa], Index[Colour, bb]] IndexDelta[Index[Colour, cc], Index[Colour, dd]] + HC[Yprime2t2x3] IndexDelta[Index[Colour, aa], Index[Colour, dd]] IndexDelta[Index[Colour, bb], Index[Colour, cc]]) R2[a,aa] HC[R2t[a,bb]] R2t[b,cc] HC[R2[b,dd]]
      + (HC[Y1223] IndexDelta[Index[Colour, aa], Index[Colour, bb]] IndexDelta[Index[Colour, cc], Index[Colour, dd]] + HC[Yprime1223] IndexDelta[Index[Colour, aa], Index[Colour, dd]] IndexDelta[Index[Colour, bb], Index[Colour, cc]]) S1[aa] R2[a,cc] Ta[sw,a,b] HC[S3[sw,dd]] HC[R2[b,bb]]
      + (HC[Y1t2t23] IndexDelta[Index[Colour, aa], Index[Colour, bb]] IndexDelta[Index[Colour, cc], Index[Colour, dd]] + HC[Yprime1t2t23] IndexDelta[Index[Colour, aa], Index[Colour, dd]] IndexDelta[Index[Colour, bb], Index[Colour, cc]]) S1[aa] R2t[a,cc] Ta[sw,a,b] HC[S3[sw,dd]] HC[R2t[b,bb]]
      + (HC[Y1t22t3] IndexDelta[Index[Colour, aa], Index[Colour, bb]] IndexDelta[Index[Colour, cc], Index[Colour, dd]] + HC[Yprime1t22t3] IndexDelta[Index[Colour, aa], Index[Colour, dd]] IndexDelta[Index[Colour, bb], Index[Colour, cc]]) S1t[aa] R2[a,cc] Ta[sw,a,b] HC[S3[sw,dd]] HC[R2t[b,bb]]
      + (HC[Y1t1t22] IndexDelta[Index[Colour, aa], Index[Colour, bb]] IndexDelta[Index[Colour, cc], Index[Colour, dd]] + HC[Yprime1t1t22] IndexDelta[Index[Colour, aa], Index[Colour, dd]] IndexDelta[Index[Colour, bb], Index[Colour, cc]]) S1[aa] HC[S1t[bb]] R2t[a,cc] HC[R2[a,dd]]
      + 1/2 HC[Y1313] S1[aa] HC[S3[sw,bb]] S1[cc] HC[S3[sw,dd]] Eps[aa,bb,cc] Eps[aa,bb,dd]
      - I HC[Y1333] S1[aa] HC[S3[sw,bb]] S3[tw,cc] Eps[sw,tw,uw] HC[S3[uw,dd]]),
    FlavorExpand -> {SU2D, SU2W}
  ]
]
```

### `LTot` (`:=`)

```mathematica
LQ2Phi + LQkin + LQf + LQ3Phi + LQ4Phi
```

## The last failure the loop worked on

This is the validation report handed to the repair agent at the start of `repair3/round3` — the problem it was asked to fix. The model still did not pass after this round.

# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: False
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: True
- Heuristic error tags: hermiticity_fail

## FeynRules check `hermiticity` output
```
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.

Inner::incom: Length 2 of dimension 1 in {SU2D, Generation} is incommensurate with length 1 of dimension 1 in {Index[SU2D, 1]}.

Inner::incom: Length 2 of dimension 1 in {SU2D, Generation} is incommensurate with length 1 of dimension 1 in {Index[SU2D, 1]}.

Inner::incom: Length 2 of dimension 1 in {SU2D, Generation} is incommensurate with length 1 of dimension 1 in {Index[SU2D, 1]}.

General::stop: Further output of Inner::incom will be suppressed during this calculation.
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
45 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 45.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Y not conserved in vertex {R2p23hat}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Y not conserved in vertex {R2p53hat}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
Quantum number Y not conserved in vertex {R2tm13hat}.
Quantum number Y not conserved in vertex {R2tp23hat}.
Quantum number Q not conserved in vertex {R2p23hatbar, R2p53hat, S1bar, S3m13hat}.
Quantum number Q not conserved in vertex {R2tm13hatbar, R2tp23hat, S1bar, S3m13hat}.
Quantum number Q not conserved in vertex {R2p53hatbar, R2tm13hat, S1tbar, S3m13hat}.
Quantum number Q not conserved in vertex {R2p23hatbar, R2tp23hat, S1tbar, S3m13hat}.
Quantum number Q not conserved in vertex {R2p23hat, R2p53hatbar, S1bar, S3m13hat}.
Quantum number Q not conserved in vertex {R2tm13hat, R2tp23hatbar, S1bar, S3m13hat}.
Quantum number Q not conserved in vertex {R2p23hat, R2p53hatbar, S1, S3m13hatbar}.
Quantum number Q not conserved in vertex {R2tm13hat, R2tp23hatbar, S1, S3m13hatbar}.
Quantum number Q not conserved in vertex {R2p53hat, R2tm13hatbar, S1t, S3m13hatbar}.
Quantum number Q not conserved in vertex {R2p23hat, R2tp23hatbar, S1t, S3m13hatbar}.
Quantum number Q not conserved in vertex {R2p23hatbar, R2p53hat, S1, S3m13hatbar}.
Quantum number Q not conserved in vertex {R2tm13hatbar, R2tp23hat, S1, S3m13hatbar}.
Quantum number Y not conserved in vertex {R2p23hatbar}.
Quantum number Y not conserved in vertex {R2p53hatbar}.
Quantum number Y not conserved in vertex {R2tm13hatbar}.
Quantum number Y not conserved in vertex {R2tp23hatbar}.
20 vertices obtained.
The lagrangian appears not to be hermitian.
Non vanishing terms during the Feynman rule calculation for L - HC[L]:
{{{R2p23hat, 1}}, -I*(Conjugate[Y2RL[Index[Generation, 1], Index[Generation, 2]]]*LLbar[Index[Spin, q], Index[SU2D, 1]] . ProjL . u[Index[Spin, r]]*Ga[0, 1, r$3432]*Ga[0, r$3431, 2]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, 1]] + Conjugate[Y2RL[Index[Generation, 3], Index[Generation, 2]]]*LLbar[Index[Spin, s], Index[SU2D, 1]] . ProjL . u[Index[Spin, t]]*Ga[0, 3, r$3432]*Ga[0, r$3431, 2]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, 1]] + Conjugate[Y2RL[Index[Generation, 1], Index[Generation, 3]]]*LLbar[Index[Spin, u], Index[SU2D, 1]] . ProjL . u[Index[Spin, v]]*Ga[0, 1, r$3432]*Ga[0, r$3431, 3]*IndexDelta[Index[Colour, Ext[1]], Index[Colour, 1]] + Conjugate[Y2RL[Index[Generati
[... block truncated ...]
```

## FeynRules check `kinetic_terms` output
```
Neglecting all terms with more than 2 particles.
All kinetic terms are diagonal.
```

## FeynRules check `mass_spectrum` output
```
Neglecting all terms with more than 2 particles.
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 1]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[1, 2, aa$3424]]*Ga[0, r$3430, 1]*R2p23hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 1]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[2, 2, aa$3424]]*Ga[0, r$3430, 1]*R2p23hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 1]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[3, 2, aa$3424]]*Ga[0, r$3430, 1]*R2p23hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 2]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[1, 2, aa$3424]]*Ga[0, r$3430, 2]*R2p23hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 2]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[2, 2, aa$3424]]*Ga[0, r$3430, 2]*R2p23hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 2]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[3, 2, aa$3424]]*Ga[0, r$3430, 2]*R2p23hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 3]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[1, 2, aa$3424]]*Ga[0, r$3430, 3]*R2p23hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 3]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[2, 2, aa$3424]]*Ga[0, r$3430, 3]*R2p23hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 3]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[3, 2, aa$3424]]*Ga[0, r$3430, 3]*R2p23hatbar[Index[Colour, aa$3424]]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 1]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[1, 1, aa$3424]]*Ga[0, r$3430, 1]*R2p53hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 1]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[2, 1, aa$3424]]*Ga[0, r$3430, 1]*R2p53hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 1]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[3, 1, aa$3424]]*Ga[0, r$3430, 1]*R2p53hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 2]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[1, 1, aa$3424]]*Ga[0, r$3430, 2]*R2p53hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 2]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[2, 1, aa$3424]]*Ga[0, r$3430, 2]*R2p53hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 2]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[3, 1, aa$3424]]*Ga[0, r$3430, 2]*R2p53hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 3]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[1, 1, aa$3424]]*Ga[0, r$3430, 3]*R2p53hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 3]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[2, 1, aa$3424]]*Ga[0, r$3430, 3]*R2p53hatbar[Index[Colour, aa$3424]] + Conjugate[Y2LR[Index[Generation, 3], Index[Generation, 3]]]*lbar[Index[Spin, r$3430]] . ProjR . HC[Qbar[3, 1, aa$3424]]*Ga[0, r$3430, 3]*R2p53hatbar[Index[Colour, aa$3424]]
Non diagonal mass term found: (vev^2*Y2t2*R2p23hatbar[Index[Colour,
[... block truncated ...]
```

## FeynRules / Wolfram Engine output (tail)
```
bar, S3p23hatbar}.
Quantum number Y not conserved in vertex {GPbar, R2p53hatbar, S1tbar, S3p23hatbar}.
Quantum number Q not conserved in vertex {S1bar, S3m13hat, S3m43hat, S3p23hatbar}.
Quantum number Q not conserved in vertex {S1, S1, S3p23hatbar, S3p23hatbar}.
Quantum number Q not conserved in vertex {R2p23hat, R2p53hatbar, W}.
Quantum number Q not conserved in vertex {A, R2p23hat, R2p53hatbar, W}.
Quantum number Q not conserved in vertex {R2tm13hat, R2tp23hatbar, W}.
Quantum number Q not conserved in vertex {A, R2tm13hat, R2tp23hatbar, W}.
Quantum number Q not conserved in vertex {S3m13hat, S3m43hatbar, W}.
Quantum number Q not conserved in vertex {S3m13hatbar, S3m43hat, W}.
Quantum number Q not conserved in vertex {S3m43hat, S3p23hatbar, W}.
Quantum number Q not conserved in vertex {A, S3m13hatbar, S3m43hat, W}.
Quantum number Q not conserved in vertex {S3m43hatbar, S3p23hat, W}.
Quantum number Q not conserved in vertex {A, S3m13hat, S3m43hatbar, W}.
Quantum number Q not conserved in vertex {A, S3m43hatbar, S3p23hat, W}.
Quantum number Q not conserved in vertex {A, S3m43hat, S3p23hatbar, W}.
Quantum number Q not conserved in vertex {G, R2p23hat, R2p53hatbar, W}.
Quantum number Q not conserved in vertex {G, R2tm13hat, R2tp23hatbar, W}.
Quantum number Q not conserved in vertex {G, S3m13hatbar, S3m43hat, W}.
Quantum number Q not conserved in vertex {G, S3m13hat, S3m43hatbar, W}.
Quantum number Q not conserved in vertex {G, S3m43hatbar, S3p23hat, W}.
Quantum number Q not conserved in vertex {G, S3m43hat, S3p23hatbar, W}.
Quantum number Q not conserved in vertex {S3m13hat, S3m13hatbar, W, W}.
Quantum number Q not conserved in vertex {S3m13hatbar, S3p23hat, W, W}.
Quantum number Q not conserved in vertex {S3m13hat, S3p23hatbar, W, W}.
Quantum number Q not conserved in vertex {S3p23hat, S3p23hatbar, W, W}.
Quantum number Q not conserved in vertex {R2p23hatbar, R2p53hat, Wbar}.
Quantum number Q not conserved in vertex {A, R2p23hatbar, R2p53hat, Wbar}.
Quantum number Q not conserved in vertex {R2tm13hatbar, R2tp23hat, Wbar}.
Quantum number Q not conserved in vertex {A, R2tm13hatbar, R2tp23hat, Wbar}.
Quantum number Q not conserved in vertex {S3m13hat, S3m43hatbar, Wbar}.
Quantum number Q not conserved in vertex {S3m13hatbar, S3m43hat, Wbar}.
Quantum number Q not conserved in vertex {S3m43hat, S3p23hatbar, Wbar}.
Quantum number Q not conserved in vertex {A, S3m13hatbar, S3m43hat, Wbar}.
Quantum number Q not conserved in vertex {S3m43hatbar, S3p23hat, Wbar}.
Quantum number Q not conserved in vertex {A, S3m13hat, S3m43hatbar, Wbar}.
Quantum number Q not conserved in vertex {A, S3m43hatbar, S3p23hat, Wbar}.
Quantum number Q not conserved in vertex {A, S3m43hat, S3p23hatbar, Wbar}.
Quantum number Q not conserved in vertex {G, R2p23hatbar, R2p53hat, Wbar}.
Quantum number Q not conserved in vertex {G, R2tm13hatbar, R2tp23hat, Wbar}.
Quantum number Q not conserved in vertex {G, S3m13hatbar, S3m43hat, Wbar}.
Quantum number Q not conserved in vertex {G, S3m13hat, S3m43hatbar, Wbar}.
Quantum number Q not conserved in vertex {G, S3m43hatbar, S3p23hat, Wbar}.
Quantum number Q not conserved in vertex {G, S3m43hat, S3p23hatbar, Wbar}.
Quantum number Q not conserved in vertex {S3m13hat, S3m13hatbar, Wbar, Wbar}.
Quantum number Q not conserved in vertex {S3m13hatbar, S3p23hat, Wbar, Wbar}.
Quantum number Q not conserved in vertex {S3m13hat, S3p23hatbar, Wbar, Wbar}.
Quantum number Q not conserved in vertex {S3p23hat, S3p23hatbar, Wbar, Wbar}.
Quantum number Y not conserved in vertex {R2p23hatbar}.
Quantum number Y not conserved in vertex {R2p53hatbar}.
Quantum number Y not conserved in vertex {R2tm13hatbar}.
Quantum number Y not conserved in vertex {R2tp23hatbar}.
Quantum number Q not conserved in vertex {R2p23hat, R2p53hatbar, W, Z}.
Quantum number Q not conserved in vertex {R2tm13hat, R2tp23hatbar, W, Z}.
Quantum number Q not conserved in vertex {S3m13hatbar, S3m43hat, W, Z}.
Quantum number Q not conserved in vertex {S3m13hat, S3m43hatbar, W, Z}.
Quantum number Q not conserved in vertex {S3m43hatbar, S3p23hat, W, Z}.
Quantum number Q not conserved in vertex {S3m43hat, S3p23hatbar, W, Z}.
Quantum number Q not conserved in vertex {R2p23hatbar, R2p53hat, Wbar, Z}.
Quantum number Q not conserved in vertex {R2tm13hatbar, R2tp23hat, Wbar, Z}.
Quantum number Q not conserved in vertex {S3m13hatbar, S3m43hat, Wbar, Z}.
Quantum number Q not conserved in vertex {S3m13hat, S3m43hatbar, Wbar, Z}.
Quantum number Q not conserved in vertex {S3m43hatbar, S3p23hat, Wbar, Z}.
Quantum number Q not conserved in vertex {S3m43hat, S3p23hatbar, Wbar, Z}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/729 .
    - Writing files.
Warning: Non positive interaction order QED.
                This might reduce the efficiency of certain matrix element generators.
                See logfile for more details.
Done!
[INFO] Done.

```

## Repair history

What the loop tried, and what each attempt measured.

# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` to add hermitian-conjugation rules for the chiral projectors: `ProjL /: HC[ProjL] = ProjL;` and `ProjR /: HC[ProjR] = ProjR;`. The validation failure showed leftover `HC[ProjL]`/`HC[ProjR]` inside the nonzero `L - HC[L]` vertices, so this is a technical FeynRules simplification fix that preserves the fields, parameters, quantum numbers, and operator structure; `LTot` remains the final top-level assignment. I could not rerun the full Wolfram check locally because `wolframscript` is installed but no Wolfram kernel path is configured.

Validation outcome AFTER that change: status=compiled, hermiticity=False, kinetic=True, mass=True, madgraph_import=True, tags=hermiticity_fail, compile_seconds=3563.2

## Attempt 2
What was changed (the agent's own summary):
Updated `model.fr` in place by rewriting the affected `LQf` fermion interaction terms so that only spinor bilinears are connected with `.` while `Eps[...]`, `Ta[...]`, and scalar fields are ordinary multiplicative factors; the same correction was applied inside the explicit `HC[...]` copy. This preserves the fields, quantum numbers, parameters, and operator structure, but fixes the technical FeynRules/Mathematica contraction defect that produced the `{SU2D, Generation}` dimension mismatch and nonzero `L - HC[L]` hermiticity vertices. `LTot` remains the final top-level assignment; I could not rerun Wolfram validation locally because `wolframscript` still has no configured Wolfram kernel path.

Validation outcome AFTER that change: status=compiled, hermiticity=False, kinetic=True, mass=True, madgraph_import=True, tags=hermiticity_fail, compile_seconds=246.2

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=False, kinetic=True, mass=True, madgraph_import=True, tags=hermiticity_fail, compile_seconds=2623.3

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:
