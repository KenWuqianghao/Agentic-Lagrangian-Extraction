## Mandatory self-audit

**Model content extracted from the paper (Sec. II, Eqs. (4)–(11), Tbl. I–II):** three new states — `WR` (complex vector, Q = +1), `ZR` (real vector), and three heavy Majorana neutrinos `N1,N2,N3` (one class with a `Generation` index). The paper states in Sec. II C that the LRSM scalars are decoupled (15–20 TeV) and are **not** part of the effective model, so no new scalar is declared. The paper also states that `WR`/`ZR` are aligned with their mass eigenstates and `N` with the RH chiral states, so no gauge-boson mixing angle exists to declare (rule 8); the only mixing the paper parametrises is the lepton mixing `X`, `Y`, which I declare as `VXL`, `VYN`.

| term | fields in monomial | d | coupling | coupling dim (4−d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L/B sum | CC[] used | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWRkin | FS[WRbar]FS[WR]; WRbar[mu]WR[mu] | 4; 2 | −1/2; MWR^2 | 0; 2 ✓ | n/a | −1+1 = 0 ✓ | n/a (physical eigenstate) | none (SU(2)_L singlet) | singlet | n/a (no new gauged U(1); Z_R is a mass eigenstate) | 0 | n/a | n/a | self-conjugate pair (Xbar X) |
| LZRkin | FS[ZR]FS[ZR]; ZR[mu]ZR[mu] | 4; 2 | −1/4; 1/2 MZR^2 | 0; 2 ✓ | n/a | 0 ✓ | n/a | none | singlet | n/a | 0 | n/a | n/a | real field, self-Hermitian |
| LNRkin | NRbar Ga del NR; NRbar MNmat NR | 4; 3 | I/2; MNmat (dim 1) | 0; 1 ✓ | n/a | 0 ✓ | n/a | none | singlet | n/a | L not assigned (Majorana) | n/a | n/a | Majorana form I/2 …, −1/2 M NRbar.NR |
| LWRqq | uqbar VCKMR Ga ProjP dq WR[mu] | 4 | gWRq = −kapRq gw/Sqrt[2] | 0 ✓ | n/a | −2/3 −1/3 +1 = 0 ✓ | n/a (mass eigenstates) | none | 3bar⊗3 = singlet ✓ | n/a | B: −1/3+1/3 = 0 ✓ | no | Eq.(4) LaTeX `\frac{-\kappa_R^q g}{\sqrt{2}}`; width Γ(WR→qq′)=Nc κ²g²M/(48π) gives 25.4 GeV, Tbl. II 50.7/2 ✓ | HC[LWRqq] |
| LWRlN | NRbar VYN Ga ProjP l WR[mu] | 4 | gWRl = −kapRl gw/Sqrt[2] | 0 ✓ | n/a | 0 −1 +1 = 0 ✓ | n/a | none | singlet | n/a | ΔL = 1 (Majorana N, intended LNV) | n/a (N is the Majorana eigenstate) | Eq.(5); Γ(WR→ℓN)=8.41 GeV and Γ(N1→e q q′)=2.1e−8 GeV reproduced ✓ | HC[LWRlN] |
| LWRlv | CC[vlbar] VXL Ga ProjP l WR[mu] | 4 | gWRl × VXL (=0 in benchmark) | 0 ✓ | n/a | 0 −1 +1 = 0 ✓ | n/a | none | singlet | n/a | ΔL = 2 (X mixing) | yes — `CC[vlbar]` for the paper's `\overline{\nu^c_m}` | same prefactor as Eq.(5) | HC[LWRlv] |
| LZRff | fbar Ga Proj f ZR[mu], f = uq, dq, l, vl, NR | 4 | gZRq/gZRl × gZR{L,R}f | 0 ✓ | n/a | 0 per bilinear ✓ | n/a | none | 3bar⊗3 singlet (quarks) | n/a | 0 (N row: not assigned) | n/a | Eq.(6) LaTeX `\frac{-\kappa_R^f g}{\sqrt{1-(1/\kappa_R^f)^2\tan^2\theta_W}}` → root in the **denominator**; confirmed by the width, which carries `[1-(1/κ)²tan²θ_W]` in its denominator, and numerically: qq̄ 82.3, tt̄ 11.3, ℓℓ 7.64, νν 2.78, NN 10.2 GeV of Tbl. II all reproduced ✓ | vector/axial current with real couplings: self-Hermitian |

Per-class free-field rows: `WR` → LWRkin (in LTotal ✓); `ZR` → LZRkin (in LTotal ✓); `NR` (N1,N2,N3) → LNRkin, mass from `Mass -> {MN,{MN1,…}}` through the diagonal matrix `MNmat` (in LTotal ✓).

Non-fundamental colour representations: none. All new fields are colour singlets, so no `AddGaugeRepresentation` line is needed.

`SelfConjugate -> True` classes: `ZR` and `NR`. Both carry no `QuantumNumbers`.

Names used — WR, ZR, NR, N1, N2, N3, MWR, MZR, MN, MN1, MN2, MN3, WWR, WZR, WN1, WN2, WN3, kapRq, kapRl, VCKMR, VXL, VYN, MNmat, tw2, gWRq, gWRl, gZRq, gZRl, gZRLu, gZRRu, gZRLd, gZRRd, gZRLl, gZRRl, gZRLv, gZRRn. None is a Mathematica built-in, a FeynRules symbol, or a name declared by SM.fr. No new index is needed: the heavy neutrinos use the SM.fr `Generation` index.

Interaction orders: `kapRq`/`kapRl` get **no** InteractionOrder, because they appear at powers +1, −2 and inside a square root; an order on them is not an integer and breaks the FeynRules order count. Every coupling that enters a vertex (`gWRq`, `gWRl`, `gZRq`, `gZRl`) carries an explicit `InteractionOrder -> {NP,1}`, so no vertex is order-less.

New U(1) charges (rule 5): the effective model gauges no new unbroken U(1). I re-derived the Z_R chiral charges from Tbl. I with `gL = (T3L−Q) tan²θW/κ²` and `gR = T3R − tan²θW Q/κ²`, and validated them against all five partial widths of Tbl. II. I add no hypercharge to any physical field.

Total Lagrangian: `LTotal := LSM + LWRkin + LZRkin + LNRkin + LWRqq + LWRlN + LWRlv + LZRff;`

Reference or cached model file read: none.

```mathematica
(* ****************************************************************************** *)
(* *****  FeynRules add-on model file: Effective Left-Right Symmetric Model  ***** *)
(* *****  Extracted from arXiv:1610.08985 (O. Mattelaer, M. Mitra, R. Ruiz)  ***** *)
(* *****  This file is loaded on top of SM.fr.                              ***** *)
(* *****                                                                    ***** *)
(* *****  New states: W_R^+- (complex vector), Z_R (real vector),           ***** *)
(* *****              N_1,N_2,N_3 (heavy Majorana neutrinos).               ***** *)
(* *****  The LRSM scalar sector is decoupled (15-20 TeV, Sec. II C) and    ***** *)
(* *****  is therefore absent, as are the non-Abelian W_R/Z_R couplings     ***** *)
(* *****  to SM bosons, which the paper declares ill-defined.               ***** *)
(* ****************************************************************************** *)

M$ModelName = "EffLRSM_gen";

M$Information = {
  Authors      -> {"Automated extraction from arXiv:1610.08985"},
  Version      -> "1.0",
  Date         -> "09. 09. 2026",
  Institutions -> {"n/a"},
  Emails       -> {"n/a"},
  URLs         -> "https://arxiv.org/abs/1610.08985"
};

(* ************************** *)
(* *** Interaction orders *** *)
(* ***  (as used by mg5)  *** *)
(* ************************** *)

M$InteractionOrderHierarchy = {
  {QCD, 1},
  {QED, 2},
  {NP,  1}
};

(* ************************** *)
(* *****    Indices     ***** *)
(* ************************** *)
(* No new index is required.  The three heavy Majorana neutrinos use the   *)
(* index Generation (Range[3]) that SM.fr declares.  Colour, Gluon, SU2D   *)
(* and SU2W also come from SM.fr.                                          *)

(* ************************** *)
(* **** Particle classes **** *)
(* ************************** *)

M$ClassesDescription = {

(* Heavy charged gauge boson W_R^+- : complex vector, colour singlet, Q = +1 *)
  V[100] == {
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
    FullName         -> "WR"
  },

(* Heavy neutral gauge boson Z_R : real vector, colour singlet, Q = 0 *)
  V[101] == {
    ClassName       -> ZR,
    SelfConjugate   -> True,
    Mass            -> {MZR, 5070.},
    Width           -> {WZR, 114.},
    ParticleName    -> "zr",
    PDG             -> 9900023,
    PropagatorLabel -> "ZR",
    PropagatorType  -> Sine,
    PropagatorArrow -> None,
    FullName        -> "ZR"
  },

(* Heavy Majorana neutrinos N_1, N_2, N_3 : colour singlets, Q = 0.       *)
(* Masses of Eq.(15): m_N1 = m_t = 173.3 GeV, m_N2 = m_N3 = 10^12 GeV.    *)
  F[100] == {
    ClassName       -> NR,
    ClassMembers    -> {N1, N2, N3},
    Indices         -> {Index[Generation]},
    FlavorIndex     -> Generation,
    SelfConjugate   -> True,
    Mass            -> {MN, {MN1, 173.3}, {MN2, 1.*^12}, {MN3, 1.*^12}},
    Width           -> {{WN1, 2.12*^-8}, {WN2, 1.*^-8}, {WN3, 1.*^-8}},
    PropagatorLabel -> {"NR", "N1", "N2", "N3"},
    PropagatorType  -> Straight,
    PropagatorArrow -> None,
    PDG             -> {9900012, 9900014, 9900016},
    ParticleName    -> {"n1", "n2", "n3"},
    FullName        -> {"HeavyN1", "HeavyN2", "HeavyN3"}
  }
};

(* ************************** *)
(* *****   Parameters   ***** *)
(* ************************** *)

M$Parameters = {

(* ----- External parameters ----- *)

  kapRq == {
    ParameterType -> External,
    BlockName     -> LRSMINPUTS,
    OrderBlock    -> 1,
    Value         -> 1.,
    Description   -> "Normalisation kappa_R^q of the W_R and Z_R couplings to quarks, Eqs.(4),(6). Appears at powers +1, -2 and inside a square root, so it carries no InteractionOrder"
  },
  kapRl == {
    ParameterType -> External,
    BlockName     -> LRSMINPUTS,
    OrderBlock    -> 2,
    Value         -> 1.,
    Description   -> "Normalisation kappa_R^l of the W_R and Z_R couplings to leptons, Eqs.(5),(6)"
  },

(* Right-handed CKM matrix V^CKM' of Eq.(4). Diagonal with unit entries. *)
  VCKMR == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    BlockName        -> RHCKMBLOCK,
    ComplexParameter -> False,
    Value            -> {VCKMR[1,1] -> 1., VCKMR[1,2] -> 0., VCKMR[1,3] -> 0.,
                         VCKMR[2,1] -> 0., VCKMR[2,2] -> 1., VCKMR[2,3] -> 0.,
                         VCKMR[3,1] -> 0., VCKMR[3,2] -> 0., VCKMR[3,3] -> 1.},
    Description      -> "Right-handed CKM matrix, Eq.(4)"
  },

(* Light neutrino mixing X_{l m} of Eq.(5). Zero in the benchmark, Eq.(8). *)
  VXL == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    BlockName        -> LMIXING,
    ComplexParameter -> False,
    Value            -> {VXL[1,1] -> 0., VXL[1,2] -> 0., VXL[1,3] -> 0.,
                         VXL[2,1] -> 0., VXL[2,2] -> 0., VXL[2,3] -> 0.,
                         VXL[3,1] -> 0., VXL[3,2] -> 0., VXL[3,3] -> 0.},
    Description      -> "Light neutrino mixing, VXL[m,l] = X_{l m} of Eq.(5); |X| = 0 in Eq.(8)"
  },

(* Heavy neutrino mixing Y_{l m'} of Eq.(5). Diagonal with unit entries, Eq.(8). *)
  VYN == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    BlockName        -> NMIXING,
    ComplexParameter -> False,
    Value            -> {VYN[1,1] -> 1., VYN[1,2] -> 0., VYN[1,3] -> 0.,
                         VYN[2,1] -> 0., VYN[2,2] -> 1., VYN[2,3] -> 0.,
                         VYN[3,1] -> 0., VYN[3,2] -> 0., VYN[3,3] -> 1.},
    Description      -> "Heavy neutrino mixing, VYN[m,l] = Y_{l m} of Eq.(5); diagonal with unit entries, Eq.(8)"
  },

(* ----- Internal parameters ----- *)

  tw2 == {
    ParameterType -> Internal,
    Value         -> sw^2/cw^2,
    Description   -> "Squared tangent of the Weinberg angle, tan^2(theta_W)"
  },

(* W_R charged current normalisations, Eqs.(4) and (5): -kappa_R g/Sqrt[2] *)
  gWRq == {
    ParameterType    -> Internal,
    Value            -> -kapRq*gw/Sqrt[2],
    InteractionOrder -> {NP, 1},
    Description      -> "W_R coupling to quarks, Eq.(4): -kappa_R^q g/Sqrt[2]"
  },
  gWRl == {
    ParameterType    -> Internal,
    Value            -> -kapRl*gw/Sqrt[2],
    InteractionOrder -> {NP, 1},
    Description      -> "W_R coupling to leptons, Eq.(5): -kappa_R^l g/Sqrt[2]"
  },

(* Z_R neutral current normalisations, Eq.(6).                             *)
(* The LaTeX source gives -kappa_R^f g / Sqrt[1 - (1/kappa_R^f)^2 tw2],    *)
(* i.e. the root sits in the DENOMINATOR.  The partial width Eq.(12) has   *)
(* [1 - (1/kappa_R^f)^2 tw2] in its denominator, which confirms this.      *)
  gZRq == {
    ParameterType    -> Internal,
    Value            -> -kapRq*gw/Sqrt[1 - tw2/kapRq^2],
    InteractionOrder -> {NP, 1},
    Description      -> "Z_R coupling normalisation for quarks, Eq.(6)"
  },
  gZRl == {
    ParameterType    -> Internal,
    Value            -> -kapRl*gw/Sqrt[1 - tw2/kapRl^2],
    InteractionOrder -> {NP, 1},
    Description      -> "Z_R coupling normalisation for leptons, Eq.(6)"
  },

(* Chiral coefficients of Eqs.(7),(8) with the charges of Tbl. I:          *)
(* gL = (T3L - Q) tw2/kappa^2 ,  gR = T3R - tw2 Q/kappa^2                  *)
  gZRLu == {
    ParameterType -> Internal,
    Value         -> -tw2/(6*kapRq^2),
    Description   -> "gL(Z_R,u) = (1/2 - 2/3) tan^2thW/kappa_q^2"
  },
  gZRRu == {
    ParameterType -> Internal,
    Value         -> 1/2 - 2*tw2/(3*kapRq^2),
    Description   -> "gR(Z_R,u) = 1/2 - (2/3) tan^2thW/kappa_q^2"
  },
  gZRLd == {
    ParameterType -> Internal,
    Value         -> -tw2/(6*kapRq^2),
    Description   -> "gL(Z_R,d) = (-1/2 + 1/3) tan^2thW/kappa_q^2"
  },
  gZRRd == {
    ParameterType -> Internal,
    Value         -> -1/2 + tw2/(3*kapRq^2),
    Description   -> "gR(Z_R,d) = -1/2 + (1/3) tan^2thW/kappa_q^2"
  },
  gZRLl == {
    ParameterType -> Internal,
    Value         -> tw2/(2*kapRl^2),
    Description   -> "gL(Z_R,e) = (-1/2 + 1) tan^2thW/kappa_l^2"
  },
  gZRRl == {
    ParameterType -> Internal,
    Value         -> -1/2 + tw2/kapRl^2,
    Description   -> "gR(Z_R,e) = -1/2 + tan^2thW/kappa_l^2"
  },
  gZRLv == {
    ParameterType -> Internal,
    Value         -> tw2/(2*kapRl^2),
    Description   -> "gL(Z_R,nu) = (1/2) tan^2thW/kappa_l^2"
  },
  gZRRn == {
    ParameterType -> Internal,
    Value         -> 1/2,
    Description   -> "gR(Z_R,N) = T3R(N_R) = 1/2, Tbl. I"
  },

(* Diagonal heavy Majorana neutrino mass matrix, Eq.(15) *)
  MNmat == {
    ParameterType -> Internal,
    Indices       -> {Index[Generation], Index[Generation]},
    Value         -> {MNmat[1,1] -> MN1, MNmat[1,2] -> 0,   MNmat[1,3] -> 0,
                      MNmat[2,1] -> 0,   MNmat[2,2] -> MN2, MNmat[2,3] -> 0,
                      MNmat[3,1] -> 0,   MNmat[3,2] -> 0,   MNmat[3,3] -> MN3},
    Description   -> "Diagonal heavy Majorana neutrino mass matrix [GeV], Eq.(15)"
  }
};

(* ************************** *)
(* *****   Lagrangian   ***** *)
(* ************************** *)

(* ---- Free field terms ---- *)

LWRkin := Block[{mu, nu},
  -1/2 FS[WRbar, mu, nu] FS[WR, mu, nu] + MWR^2 WRbar[mu] WR[mu]
];

LZRkin := Block[{mu, nu},
  -1/4 FS[ZR, mu, nu] FS[ZR, mu, nu] + 1/2 MZR^2 ZR[mu] ZR[mu]
];

LNRkin := Block[{mu},
  I/2 NRbar.Ga[mu].del[NR, mu] - 1/2 NRbar.MNmat.NR
];

(* ---- W_R charged currents, Eqs.(4) and (5) ---- *)

LWRqq := Block[{mu, lag},
  lag = gWRq uqbar.VCKMR.Ga[mu].ProjP.dq WR[mu];
  lag + HC[lag]
];

LWRlN := Block[{mu, lag},
  lag = gWRl NRbar.VYN.Ga[mu].ProjP.l WR[mu];
  lag + HC[lag]
];

LWRlv := Block[{mu, lag},
  lag = gWRl CC[vlbar].VXL.Ga[mu].ProjP.l WR[mu];
  lag + HC[lag]
];

(* ---- Z_R neutral currents, Eqs.(6)-(8) ---- *)

LZRff := Block[{mu},
   gZRq ( gZRLu uqbar.Ga[mu].ProjM.uq + gZRRu uqbar.Ga[mu].ProjP.uq
        + gZRLd dqbar.Ga[mu].ProjM.dq + gZRRd dqbar.Ga[mu].ProjP.dq ) ZR[mu]
 + gZRl ( gZRLl  lbar.Ga[mu].ProjM.l  + gZRRl   lbar.Ga[mu].ProjP.l
        + gZRLv vlbar.Ga[mu].ProjM.vl
        + gZRRn NRbar.Ga[mu].ProjP.NR ) ZR[mu]
];

(* ---- Total Lagrangian ---- *)

LTotal := LSM + LWRkin + LZRkin + LNRkin + LWRqq + LWRlN + LWRlv + LZRff;
```