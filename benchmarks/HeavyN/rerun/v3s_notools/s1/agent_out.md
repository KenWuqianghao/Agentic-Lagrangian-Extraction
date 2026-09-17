## Self-audit table

| term name | fields in monomial | operator dim d | coupling symbol | coupling dim (4-d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new-U(1) sum | L/B sum | CC[] used | fraction/root check | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LN1Kin (kin.) | n1bar, n1, del | 4 | (i, implicit) | 0 | n/a | 0 | n/a (singlet) | n/a (SU2 singlet) | n/a (colour singlet) | n/a | ΔL=0 | n/a | n/a | self-Hermitian (Majorana bilinear) |
| LN1Kin (mass) | n1bar, n1 | 3 | MN1 | 1 | n/a | 0 | n/a | n/a | n/a | n/a | ΔL=2 (Majorana mass) | n/a | n/a | self-Hermitian |
| LNCC | W, bar[CC[n1]], l | 4 | gw·Conjugate[VlN[ff]] | 0 | n/a | +1(W)+0(N)−1(l)=0 | n/a (physical-basis current, mirrors SM structure) | n/a (written in mass basis, as in paper) | n/a (colour singlets) | n/a | ΔL=1 (LNV, seesaw) | yes | \frac{g}{\sqrt2}, unambiguous in LaTeX | HC[cc] appended (paper states "+H.c.") |
| LNZ | Z, bar[CC[n1]], vl | 4 | gw/(2cw)·Conjugate[VlN[ff]] | 0 | n/a | 0 | n/a | n/a | n/a | n/a | ΔL=1 | yes | \frac{g}{2\cos\theta_W}, unambiguous | HC[cc] appended |
| LNH | H, bar[CC[n1]], vl | 4 | gw·MN1/(2 MW)·Conjugate[VlN[ff]] | 0 (ratio MN1/MW is dimensionless) | n/a | 0 | n/a | n/a | n/a | n/a | ΔL=1 | yes | \frac{g\,m_N}{2M_W}, unambiguous | HC[cc] appended |

- Kinetic+mass term present for the one new class `n1`, and included in `LTotal`: confirmed.
- No non-fundamental colour representation is introduced by this model: n/a, no `AddGaugeRepresentation[...]` needed.
- `SelfConjugate -> True` classes: `{n1}`. It carries no `QuantumNumbers`: confirmed.
- Chosen names `n1, MN1, WN1, VlN, HEAVYN, NPINPUTS, NP` collide with none of Mathematica's built-ins, FeynRules reserved symbols (`N,C,D,E,I,K,O,HC,CC,FS,DC,del,Eps,Ga,ProjP,ProjM`), or SM.fr names (`H,Phi,Z,W,A,G,ee,gs,gw,sw,cw,vev,MZ,MW,...`): confirmed.
- Single total Lagrangian: `LTotal := LN1Kin + LNCC + LNZ + LNH` sums every term defined above; no alternative total is defined.
- Reference or cached model file read: none. Extraction used only the paper's LaTeX source and the supplied SM.fr.

```mathematica
(* ****************************************************************** *)
(* FeynRules SM add-on: HeavyN_gen                                    *)
(* One heavy Majorana neutrino n1, from arXiv:1602.06957              *)
(* (Degrande, Mattelaer, Ruiz, Turner). Loaded on top of SM.fr.       *)
(* No reference or cached HeavyN model file was read; this extraction *)
(* uses only the paper's LaTeX source and the SM.fr provided.         *)
(* ****************************************************************** *)

M$ModelName = "HeavyN_gen";

M$Information = {
  Authors      -> {"Automated extraction"},
  Version      -> "1.0",
  Date         -> "2026",
  References   -> {"arXiv:1602.06957 (C. Degrande, O. Mattelaer, R. Ruiz, J. Turner)"},
  Description  -> "SM add-on: one heavy Majorana neutrino n1 mixing with SM leptons via V_lN; W/Z/h currents from the interaction Lagrangian of arXiv:1602.06957."
};

M$InteractionOrderHierarchy = {
  {QCD, 1},
  {QED, 2},
  {NP,  1}
};

(* No new index ranges are needed: n1 carries no indices, and the *)
(* mixing parameter uses the existing SM.fr Index[Generation].     *)

M$Parameters = {

  MN1 == {
    ParameterType -> External,
    BlockName     -> HEAVYN,
    OrderBlock    -> 1,
    Value         -> 500.,
    TeX           -> Subscript[m,N],
    Description   -> "Heavy Majorana neutrino mass m_N [GeV] (Eq. Lagrangian; Table I benchmark)"
  },

  WN1 == {
    ParameterType -> External,
    BlockName     -> HEAVYN,
    OrderBlock    -> 2,
    Value         -> 1.,
    TeX           -> Subscript[\[CapitalGamma],N],
    Description   -> "n1 total decay width [GeV]; not given numerically in the paper, representative placeholder"
  },

  VlN == {
    ParameterType    -> External,
    ComplexParameter -> True,
    Indices          -> {Index[Generation]},
    BlockName        -> NPINPUTS,
    Value            -> {VlN[1] -> 1., VlN[2] -> 1., VlN[3] -> 1.},
    InteractionOrder -> {NP, 1},
    TeX              -> Subscript[V,lN],
    Description      -> "Active-heavy mixing V_lN for l = e, mu, tau (Eq. Lagrangian). The paper normalizes all rates by |V_lN|^2 and sets |V_lN|=1 for the model-independent \"bare\" cross section; default set to 1 accordingly."
  }
};

M$ClassesDescription = {

  F[100] == {
    ClassName       -> n1,
    SelfConjugate   -> True,
    Indices         -> {},
    Mass            -> {MN1, 500.},
    Width           -> {WN1, 1.},
    ParticleName    -> "n1",
    PDG             -> 9900012,
    PropagatorLabel -> "n1",
    PropagatorType  -> S,
    PropagatorArrow -> None,
    FullName        -> "Heavy Majorana neutrino"
  }

};

(* ************************** *)
(* *****   Lagrangian   ***** *)
(* ************************** *)

(* Free kinetic + Majorana mass term for the new heavy neutrino. *)
LN1Kin := Block[{mu},
  ExpandIndices[ I/2 n1bar.Ga[mu].del[n1,mu] - 1/2 MN1 n1bar.n1 ]
];

(* Charged current: -g/Sqrt[2] W^+_mu Nbar^c V_{lN}^* gamma^mu P_L l^- + H.c. *)
LNCC := Block[{mu, ff, cc},
  cc = ExpandIndices[
    -(gw/Sqrt[2]) W[mu] bar[CC[n1]].Ga[mu].ProjM.l[ff] Conjugate[VlN[ff]],
    FlavorExpand -> Generation];
  cc + HC[cc]
];

(* Neutral current: -g/(2 cos(theta_W)) Z_mu Nbar^c V_{lN}^* gamma^mu P_L nu_l + H.c. *)
LNZ := Block[{mu, ff, cc},
  cc = ExpandIndices[
    -(gw/(2 cw)) Z[mu] bar[CC[n1]].Ga[mu].ProjM.vl[ff] Conjugate[VlN[ff]],
    FlavorExpand -> Generation];
  cc + HC[cc]
];

(* Higgs coupling: -(g m_N)/(2 M_W) h Nbar^c V_{lN}^* P_L nu_l + H.c. *)
LNH := Block[{ff, cc},
  cc = ExpandIndices[
    -(gw*MN1/(2 MW)) H bar[CC[n1]].ProjM.vl[ff] Conjugate[VlN[ff]],
    FlavorExpand -> Generation];
  cc + HC[cc]
];

LTotal := LN1Kin + LNCC + LNZ + LNH;
```