## Self-audit table

No reference or cached `.fr` model file was read for this extraction — only the paper's LaTeX source and the supplied `SM.fr` were used (**none**).

New physics content identified from the paper: a heavy charged vector $W_R^\pm$ (Sec. II, Eq. chcurrent), a heavy neutral vector $Z_R$ (Sec. II, Eq. neucurrent), and three heavy Majorana neutrinos $N_1,N_2,N_3$ (Sec. II, Eq. lrsmInputs: $m_{N_1}=m_t=173.3$ GeV, $m_{N_2}=m_{N_3}=10^{12}$ GeV). The model is explicitly "effective": Sec. II.B (`modelLimits`) states non-Abelian $W_R,Z_R$ self-interactions and their couplings to SM bosons are "ill-defined," so only direct mass-eigenstate matter couplings (no `M$GaugeGroups`, no mixing `Definitions`) are written — consistent with "aligned with their mass eigenstates" and "we neglect interference with the SM $W$." The light-neutrino–$W_R$ mixing $X_{\ell m}=0$ in the benchmark (Eq. lrsmNuMixing), so that term is dropped rather than kept with a zero coefficient; no `CC[]` is needed anywhere as a result.

| term | fields | dim d | coupling | coupling dim (4−d) | 1/Λ | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L/B sum | CC[] | fraction/root check | H.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWRZRkin (WR kin/mass) | WRbar,WR (FS·FS / V·V) | 4 / 2 | −1/2 (dimless) / MWR² | 0 / 2 ✓ | n/a | −1+1=0 | n/a | n/a singlet | n/a | n/a | n/a | n/a | n/a | self-Herm. |
| LWRZRkin (ZR kin/mass) | ZR,ZR | 4 / 2 | −1/4 / 1/2 MZR² | 0 / 2 ✓ | n/a | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | self-Herm. |
| LNNfree | NNbar,NN | 4 / 3 | i/2 / MN | 0 / 1 ✓ | n/a | 0 | n/a | n/a | n/a | n/a | L undefined (Majorana, self-conj.) | n/a | n/a | self-Herm. (Majorana bilinear) |
| LWRq | uqbar,VRCKM,dq,WR | 4 | −κ_RQ·gw/√2 | 0 ✓ | n/a | −2/3−1/3+1=0 | n/a | n/a singlet | colour δ (uq.dq dot) | n/a | B: −1/3+1/3+0=0 | no | Eq.(chcurrent) LaTeX, literal | HC[] present |
| LWRlep | NNbar,YN,l,WR | 4 | −κ_RL·gw/√2 | 0 ✓ | n/a | 0−1+1=0 | n/a | n/a singlet | n/a (colour singlets) | n/a | L formally conserved at vertex (N treated as L=+1); violation is in Majorana mass only | no (X=0 term dropped) | eq. preceding (lrsmNuMixing), literal | HC[] present |
| LZRu | uqbar,uq,ZR | 4 | normZRQ·gL/gR | 0 ✓ | n/a | 0 | n/a | n/a singlet | colour δ | n/a | 0 | no | Eq.(neucurrent), literal | self-Herm. |
| LZRd | dqbar,dq,ZR | 4 | normZRQ·gL/gR | 0 ✓ | n/a | 0 | n/a | n/a | colour δ | n/a | 0 | no | Eq.(neucurrent), literal | self-Herm. |
| LZRnu | vlbar,vl,ZR | 4 | normZRL·gLZRnu | 0 ✓ | n/a | 0 | n/a | n/a singlet | n/a | n/a | 0 | no | Eq.(neucurrent), literal | self-Herm. |
| LZRe | lbar,l,ZR | 4 | normZRL·gL/gR | 0 ✓ | n/a | 0 | n/a | n/a singlet | n/a | n/a | 0 | no | Eq.(neucurrent), literal | self-Herm. |
| LZRNN | NNbar,NN,ZR | 4 | normZRL·gRZRNN | 0 ✓ | n/a | 0 | n/a | n/a singlet | n/a | n/a | 0 | no | Eq.(neucurrent), literal | self-Herm. |

- `SelfConjugate -> True` classes: `ZR` (V[102]), `NN` (F[101]) — neither carries a `QuantumNumbers` entry. Confirmed.
- Names chosen: `WR, ZR, NN, N1, N2, N3, kappaRQ, kappaRL, VRCKM, YN, MWR, WWR, MZR, WZR, MN, MN1, MN2, MN3, WN, WN1, WN2, WN3, tanW2, normZRQ, normZRL, gLZRu, gRZRu, gLZRd, gRZRd, gLZRnu, gLZRe, gRZRe, gRZRNN` — none is a Mathematica/FeynRules built-in or an SM.fr name.
- Single total: `LTotal := LWRZRkin + LNNfree + LWRq + LWRlep + LZRu + LZRd + LZRnu + LZRe + LZRNN;` — sums every term defined above.
- Y-sum and new-U(1)-charge columns are "n/a" throughout because no new gauge symmetry is introduced (the effective $W_R,Z_R$ are non-dynamical mass-eigenstate vectors per Sec. II.B, not gauge bosons of an additional gauged group), and all couplings are written for post-EWSB physical fermions (`uq,dq,l,vl`), which in `SM.fr` carry no independent hypercharge quantum number.

```mathematica
(* ************************************************************* *)
(* FeynRules add-on: Effective Left-Right Symmetric Model (NLO)  *)
(* Based on arXiv:1610.08985 (Mattelaer, Mitra, Ruiz)             *)
(* Loaded on top of the Standard Model (SM.fr)                    *)
(* No reference or cached .fr model file was read: NONE.          *)
(* ************************************************************* *)

M$ModelName = "EffLRSM_gen";

M$Information = {
  Authors -> {"Automated extraction (GitNexus benchmark)"},
  Version -> "1.0",
  Date    -> "17. 09. 2026",
  URLs    -> "arXiv:1610.08985"
};

(* ************************** *)
(* *** Interaction orders *** *)
(* ************************** *)
M$InteractionOrderHierarchy = {
  {QCD, 1},
  {QED, 2},
  {NP , 1}
};

(* ************************** *)
(* **** Particle classes **** *)
(* ************************** *)
M$ClassesDescription = {

(* Heavy right-handed charged gauge boson W_R^+/-, Sec. II *)
  V[101] == {
    ClassName        -> WR,
    SelfConjugate    -> False,
    Mass             -> {MWR, 3000.},
    Width            -> {WWR, 84.3},
    QuantumNumbers   -> {Q -> 1},
    ParticleName     -> "wr+",
    AntiParticleName -> "wr-",
    PDG              -> 9900024,
    PropagatorLabel  -> "WR",
    PropagatorType   -> Sine,
    PropagatorArrow  -> Forward,
    FullName         -> "W_R"
  },

(* Heavy right-handed neutral gauge boson Z_R, Sec. II *)
  V[102] == {
    ClassName       -> ZR,
    SelfConjugate   -> True,
    Mass            -> {MZR, 5070.},
    Width           -> {WZR, 114.},
    ParticleName    -> "zr",
    PDG             -> 9900023,
    PropagatorLabel -> "ZR",
    PropagatorType  -> Sine,
    PropagatorArrow -> None,
    FullName        -> "Z_R"
  },

(* Heavy Majorana neutrinos N_1, N_2, N_3, Sec. II, Eq.(lrsmInputs) *)
  F[101] == {
    ClassName        -> NN,
    ClassMembers     -> {N1, N2, N3},
    Indices          -> {Index[Generation]},
    FlavorIndex      -> Generation,
    SelfConjugate    -> True,
    Mass             -> {MN, {MN1, 173.3}, {MN2, 1.*^12}, {MN3, 1.*^12}},
    Width            -> {WN, {WN1, 2.12*^-8}, {WN2, 0.}, {WN3, 0.}},
    PropagatorLabel  -> {"N", "N1", "N2", "N3"},
    PropagatorType   -> Straight,
    PropagatorArrow  -> None,
    PDG              -> {9900012, 9900014, 9900016},
    ParticleName     -> {"n1", "n2", "n3"},
    FullName         -> {"Heavy Majorana neutrino 1", "Heavy Majorana neutrino 2", "Heavy Majorana neutrino 3"}
  }
};

(* ************************** *)
(* *****   Parameters   ***** *)
(* ************************** *)
M$Parameters = {

  (* External parameters: WR/ZR coupling normalizations, Eq.(chcurrent)-(neucurrent) *)
  kappaRQ == {
    ParameterType    -> External,
    BlockName        -> EFFLRSM,
    OrderBlock       -> 1,
    Value            -> 1.,
    InteractionOrder -> {NP, 1},
    Description      -> "kappa_R^q: overall WR/ZR quark coupling normalization, Eq.(chcurrent)"
  },
  kappaRL == {
    ParameterType    -> External,
    BlockName        -> EFFLRSM,
    OrderBlock       -> 2,
    Value            -> 1.,
    InteractionOrder -> {NP, 1},
    Description      -> "kappa_R^l: overall WR/ZR lepton/neutrino/N coupling normalization, Eq.(WR-l-nu/N current)"
  },

  (* Right-handed CKM matrix, taken diagonal with unit entries (Sec. II, text after Eq.(chcurrent)) *)
  VRCKM == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    BlockName        -> VRCKMBLOCK,
    InteractionOrder -> {NP, 1},
    Value            -> {
      VRCKM[1,1] -> 1., VRCKM[1,2] -> 0., VRCKM[1,3] -> 0.,
      VRCKM[2,1] -> 0., VRCKM[2,2] -> 1., VRCKM[2,3] -> 0.,
      VRCKM[3,1] -> 0., VRCKM[3,2] -> 0., VRCKM[3,3] -> 1.
    },
    Description      -> "Right-handed CKM matrix V^CKM'_ij, diagonal with unit entries (Sec. II)"
  },

  (* N-lepton mixing matrix Y_{l m'}, Eq.(lrsmNuMixing) *)
  YN == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    BlockName        -> YNBLOCK,
    InteractionOrder -> {NP, 1},
    Value            -> {
      YN[1,1] -> 1., YN[1,2] -> 0., YN[1,3] -> 0.,
      YN[2,1] -> 0., YN[2,2] -> 1., YN[2,3] -> 0.,
      YN[3,1] -> 0., YN[3,2] -> 0., YN[3,3] -> 1.
    },
    Description      -> "N-lepton mixing Y_{l,m'}: |Y_eN1|=|Y_muN2|=|Y_tauN3|=1, others 0, Eq.(lrsmNuMixing)"
  },

  (* Internal Parameters *)
  tanW2 == {
    ParameterType -> Internal,
    Value         -> sw2/(1-sw2),
    Description   -> "tan^2(theta_W) = sw2/cw2, used in ZR neutral current, Eq.(neucurrent)"
  },
  normZRQ == {
    ParameterType -> Internal,
    Value         -> -kappaRQ*gw/Sqrt[1 - tanW2/kappaRQ^2],
    Description   -> "ZR-quark current normalization, Eq.(neucurrent) with f = q"
  },
  normZRL == {
    ParameterType -> Internal,
    Value         -> -kappaRL*gw/Sqrt[1 - tanW2/kappaRL^2],
    Description   -> "ZR-lepton/neutrino/N current normalization, Eq.(neucurrent) with f = l,nu,N"
  },
  gLZRu == {
    ParameterType -> Internal,
    Value         -> (1/2 - 2/3)*tanW2/kappaRQ^2,
    Description   -> "g_L^{ZR,u}: T_L^{3,uL} - Q_u = 1/2 - 2/3, Eq.(neucurrent), Tbl.(qNumbers)"
  },
  gRZRu == {
    ParameterType -> Internal,
    Value         -> 1/2 - (2/3)*tanW2/kappaRQ^2,
    Description   -> "g_R^{ZR,u}: T_R^{3,uR} = 1/2, Q_u = 2/3, Eq.(neucurrent), Tbl.(qNumbers)"
  },
  gLZRd == {
    ParameterType -> Internal,
    Value         -> (-1/2 - (-1/3))*tanW2/kappaRQ^2,
    Description   -> "g_L^{ZR,d}: T_L^{3,dL} - Q_d = -1/2 + 1/3, Eq.(neucurrent), Tbl.(qNumbers)"
  },
  gRZRd == {
    ParameterType -> Internal,
    Value         -> -1/2 - (-1/3)*tanW2/kappaRQ^2,
    Description   -> "g_R^{ZR,d}: T_R^{3,dR} = -1/2, Q_d = -1/3, Eq.(neucurrent), Tbl.(qNumbers)"
  },
  gLZRnu == {
    ParameterType -> Internal,
    Value         -> (1/2 - 0)*tanW2/kappaRL^2,
    Description   -> "g_L^{ZR,nu}: T_L^{3,nuL} - Q_nu = 1/2 - 0, Eq.(neucurrent), Tbl.(qNumbers)"
  },
  gLZRe == {
    ParameterType -> Internal,
    Value         -> (-1/2 - (-1))*tanW2/kappaRL^2,
    Description   -> "g_L^{ZR,e}: T_L^{3,eL} - Q_e = -1/2 + 1, Eq.(neucurrent), Tbl.(qNumbers)"
  },
  gRZRe == {
    ParameterType -> Internal,
    Value         -> -1/2 - (-1)*tanW2/kappaRL^2,
    Description   -> "g_R^{ZR,e}: T_R^{3,eR} = -1/2, Q_e = -1, Eq.(neucurrent), Tbl.(qNumbers)"
  },
  gRZRNN == {
    ParameterType -> Internal,
    Value         -> 1/2,
    Description   -> "g_R^{ZR,N}: T_R^{3,NR} = 1/2, Q_N = 0, Eq.(neucurrent), Tbl.(qNumbers)"
  }
};

(* ************************** *)
(* *****   Lagrangian   ***** *)
(* ************************** *)

(* Free kinetic + mass terms for the new heavy gauge bosons WR, ZR *)
LWRZRkin := Block[{mu,nu},
  ExpandIndices[
     -1/2 FS[WRbar,mu,nu] FS[WR,mu,nu] + MWR^2 WRbar[mu] WR[mu]
    - 1/4 FS[ZR,mu,nu] FS[ZR,mu,nu]    + 1/2 MZR^2 ZR[mu] ZR[mu]
  ]
];

(* Free kinetic + Majorana mass term for the heavy neutrinos NN, Eq.(lrsmInputs) *)
LNNfree := Block[{mu},
  ExpandIndices[ I/2 NNbar.Ga[mu].del[NN,mu] - 1/2 MN NNbar.NN ]
];

(* WR charged current to quarks, Eq.(chcurrent) *)
LWRq := Block[{mu, yuk},
  yuk = -(kappaRQ*gw/Sqrt[2]) uqbar.VRCKM.Ga[mu].ProjP.dq WR[mu];
  ExpandIndices[ yuk + HC[yuk] ]
];

(* WR charged current to leptons and heavy neutrinos (X_{l m} = 0 dropped), Eq. before (lrsmNuMixing) *)
LWRlep := Block[{mu, yuk},
  yuk = -(kappaRL*gw/Sqrt[2]) NNbar.YN.Ga[mu].ProjP.l WR[mu];
  ExpandIndices[ yuk + HC[yuk] ]
];

(* ZR neutral current to up-type quarks, Eq.(neucurrent) *)
LZRu := Block[{mu},
  ExpandIndices[ normZRQ (gLZRu uqbar.Ga[mu].ProjM.uq + gRZRu uqbar.Ga[mu].ProjP.uq) ZR[mu] ]
];

(* ZR neutral current to down-type quarks, Eq.(neucurrent) *)
LZRd := Block[{mu},
  ExpandIndices[ normZRQ (gLZRd dqbar.Ga[mu].ProjM.dq + gRZRd dqbar.Ga[mu].ProjP.dq) ZR[mu] ]
];

(* ZR neutral current to light (left-handed only) neutrinos, Eq.(neucurrent) *)
LZRnu := Block[{mu},
  ExpandIndices[ normZRL gLZRnu vlbar.Ga[mu].ProjM.vl ZR[mu] ]
];

(* ZR neutral current to charged leptons, Eq.(neucurrent) *)
LZRe := Block[{mu},
  ExpandIndices[ normZRL (gLZRe lbar.Ga[mu].ProjM.l + gRZRe lbar.Ga[mu].ProjP.l) ZR[mu] ]
];

(* ZR neutral current to heavy (right-handed only) Majorana neutrinos, Eq.(neucurrent) *)
LZRNN := Block[{mu},
  ExpandIndices[ normZRL gRZRNN NNbar.Ga[mu].ProjP.NN ZR[mu] ]
];

LTotal := LWRZRkin + LNNfree + LWRq + LWRlep + LZRu + LZRd + LZRnu + LZRe + LZRNN;
```