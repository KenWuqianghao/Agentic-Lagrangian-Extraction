Self-audit table (produced before the model, per the task's mandatory-audit rule):

| term | fields | d | coupling | coupling dim (4−d) | Λ power | ΣQ | ΣY | SU(2) | SU(3) | new-U(1) | L/B | CC[] | fraction/root check | H.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lsdilkin (kin) | del[s,mu] del[s,mu] | 4 | 1/2 (numeric) | 0 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | n/a | self-conj. |
| Lsdilkin (mass) | s·s | 2 | Mdil² | 2 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | n/a | self-conj. |
| LTQkin (kin) | TQbar·Ga·DC[TQ] | 4 | i (numeric) | 0 | n/a | 0 | 0 | singlet | 3⊗3̄ | n/a | n/a | n/a | n/a | self-Herm. |
| LTQkin (mass) | TQbar·TQ | 3 | MTQ | 1 | n/a | 0 | 0 | singlet | 3⊗3̄ | n/a | n/a | n/a | n/a | self-Herm. |
| LMDMpot κ-term | Sf²·Hgf² | 4 | kappaMDM | 0 | n/a | 0 | 0 | singlet (Sf,Hgf real) | singlet | n/a | n/a | n/a | Eq.(lambda), LaTeX \frac | self-Herm. |
| LMDMpot λH-term | Hgf⁴ | 4 | lambdaHMDM | 0 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | Eq.(lambda), LaTeX \frac | self-Herm. |
| LMDMpot λS-term | Sf⁴ | 4 | lambdaSMDM | 0 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | Eq.(lambda), LaTeX \frac | self-Herm. |
| LMDMTcoup (H) | H·TQbar·TQ | 4 | gTNP·Sin[thetaS] | 0 | n/a | 0 | 0 | singlet | 3⊗3̄ | n/a | n/a | n/a | n/a (textual def. of η, l.977) | self-Herm. |
| LMDMTcoup (s) | s·TQbar·TQ | 4 | gTNP·Cos[thetaS] | 0 | n/a | 0 | 0 | singlet | 3⊗3̄ | n/a | n/a | n/a | n/a | self-Herm. |
| LMDMYuk | TQbar·QL·Phi·Eps | 4 | yprime | 0 | n/a | 0 (checked component-wise: t-piece 0, CKM d-piece 0) | 0 (−2/3+1/6+1/2=0) | doublet⊗doublet via Eps[ii,jj], singlet | 3⊗3̄ | n/a | n/a | n/a | n/a | HC[LMDMYuk] added |

- Kinetic+mass rows present and in `LTotal` for both new classes: `s` (rows 1–2) and `TQ` (rows 3–4).
- No non-fundamental colour representation is introduced (`TQ` uses the existing fundamental `Colour` index only) — `AddGaugeRepresentation` not needed.
- `SelfConjugate -> True` classes with no `QuantumNumbers`: `s`, `Sf`, `Hgf`.
- New symbols (`s`, `TQ`, `Sf`, `Hgf`, `fdil`, `thetaS`, `Mdil`, `Wdil`, `MTQ`, `WTQ`, `yprime`, `etaMDM`, `etaInvMDM`, `kappaMDM`, `lambdaHMDM`, `lambdaSMDM`, `gTNP`) are checked against Mathematica/FeynRules builtins and SM.fr names (`H`,`Phi`,`Z`,`W`,`A`,`G`,`T`,`f`,`ee`,`gs`,`gw`,`sw`,`cw`,`vev`,`MZ`,`MW`,`MS`,…) — none collide.
- Single total: `LTotal := Lsdilkin + LTQkin + LMDMpot + LMDMTcoup + LMDMYuk`, summing every term above.
- No reference or cached `.fr` file for this model was read: none — only the paper (arXiv:1311.6661 LaTeX source) and the supplied `SM.fr` were used.
- Approximation noted: the bare `mS²`, `mH²` pieces of Eq.(potential) are not written explicitly (the h,s masses are fixed instead via the declared `Mass->{MH,125}` / `Mass->{Mdil,...}` class entries, avoiding double-counting); only the portal/self-coupling (κ, λH, λS) pieces of the potential are encoded. `SM.fr`'s own Higgs kinetic/gauge/Yukawa sector is left untouched (h↔s mixing is realized through the new dilaton potential and through the T–q3L Yukawa mixing, not by rewriting `Phi`'s `Definitions`).

```mathematica
(***************************************************************************************************************)
(******            FeynRules add-on model file for the Minimal Dilaton Model (MDM)                        ******)
(******            Source: J. Cao, Y. He, P. Wu, M. Zhang, J. Zhu, arXiv:1311.6661                         ******)
(******            Loads on top of SM.fr; extracted from the paper's LaTeX source only.                    ******)
(***************************************************************************************************************)

M$ModelName = "MDMmodel_gen";

M$Information = {
  Authors      -> {"Automated extraction"},
  Version      -> "1.0",
  Date         -> "17. 09. 2026",
  Institutions -> {"n/a"},
  Emails       -> {"n/a"},
  URLs         -> "http://arxiv.org/abs/1311.6661"
};

(* ************************** *)
(* *** Interaction orders *** *)
(* ************************** *)

M$InteractionOrderHierarchy = {
  {QCD, 1},
  {QED, 2},
  {NP , 1}
};

(* No new gauge groups (SM add-on). No new indices are needed: TQ carries only the *)
(* already-declared fundamental Colour index; Sf, Hgf, s carry no indices at all.  *)

(* ************************** *)
(* ****   Parameters      **** *)
(* ************************** *)

M$Parameters = {

  (* External parameters *)
  fdil == {
    ParameterType    -> External,
    BlockName        -> MDMIN,
    OrderBlock       -> 1,
    Value            -> 1000.,
    TeX              -> Subscript[f,S],
    Description      -> "Dilaton decay constant f [GeV], Eq.(MDM)"
  },
  thetaS == {
    ParameterType    -> External,
    BlockName        -> MDMIN,
    OrderBlock       -> 2,
    Value            -> 0.1,
    TeX              -> Subscript[\[Theta],S],
    Description      -> "Higgs-dilaton mixing angle theta_S [rad]"
  },
  Mdil == {
    ParameterType    -> External,
    BlockName        -> MDMIN,
    OrderBlock       -> 3,
    Value            -> 300.,
    TeX              -> Subscript[m,s],
    Description      -> "Dilaton mass m_s [GeV]"
  },
  Wdil == {
    ParameterType    -> External,
    BlockName        -> MDMIN,
    OrderBlock       -> 4,
    Value            -> 1.0,
    TeX              -> Subscript[\[CapitalGamma],s],
    Description      -> "Dilaton width [GeV] (not computed in the paper, placeholder)"
  },
  MTQ == {
    ParameterType    -> External,
    BlockName        -> MDMIN,
    OrderBlock       -> 5,
    Value            -> 1000.,
    TeX              -> Subscript[M,T],
    Description      -> "Top-partner mass scale M [GeV], Eq.(MDM)"
  },
  WTQ == {
    ParameterType    -> External,
    BlockName        -> MDMIN,
    OrderBlock       -> 6,
    Value            -> 10.,
    TeX              -> Subscript[\[CapitalGamma],T],
    Description      -> "Top-partner width [GeV] (not computed in the paper, placeholder)"
  },
  yprime == {
    ParameterType    -> External,
    BlockName        -> MDMIN,
    OrderBlock       -> 7,
    Value            -> 1.0,
    InteractionOrder -> {NP,1},
    TeX              -> Superscript[y,\[Prime]],
    Description      -> "T_R - q3L.H Yukawa coupling y', Eq.(MDM)"
  },

  (* Internal parameters *)
  etaMDM == {
    ParameterType -> Internal,
    Value         -> vev/fdil,
    Description   -> "eta = (v/f) N_T, N_T = 1 for the MDM"
  },
  etaInvMDM == {
    ParameterType -> Internal,
    Value         -> fdil/vev,
    Description   -> "eta^-1 = f/v"
  },
  kappaMDM == {
    ParameterType    -> Internal,
    Value            -> (Abs[MH^2 - Mdil^2]/(2*fdil*vev)) * Abs[Sin[2*thetaS]],
    InteractionOrder -> {NP,2},
    TeX              -> \[Kappa],
    Description      -> "Portal coupling kappa, Eq.(lambda)"
  },
  lambdaHMDM == {
    ParameterType    -> Internal,
    Value            -> (Abs[MH^2 - Mdil^2]/vev^2) *
                          ( Abs[(MH^2 + Mdil^2)/(MH^2 - Mdil^2)] + Sign[Sin[2*thetaS]]*Cos[2*thetaS] ),
    InteractionOrder -> {NP,2},
    TeX              -> Subscript[\[Lambda],H],
    Description      -> "Higgs quartic coupling lambda_H of Vtilde(S,H), Eq.(lambda)"
  },
  lambdaSMDM == {
    ParameterType    -> Internal,
    Value            -> (3*Abs[MH^2 - Mdil^2]/(2*fdil^2)) *
                          ( Abs[(MH^2 + Mdil^2)/(MH^2 - Mdil^2)] - Sign[Sin[2*thetaS]]*Cos[2*thetaS] ),
    InteractionOrder -> {NP,2},
    TeX              -> Subscript[\[Lambda],S],
    Description      -> "Dilaton quartic coupling lambda_S of Vtilde(S,H), Eq.(lambda)"
  },
  gTNP == {
    ParameterType    -> Internal,
    Value            -> MTQ/fdil,
    InteractionOrder -> {NP,1},
    Description      -> "Trace-anomaly coupling M/f of the dilaton field to the top partner, Eq.(MDM)"
  }
};

(* ************************** *)
(* **** Particle classes  **** *)
(* ************************** *)

M$ClassesDescription = {

(* New physical scalar: the dilaton mass eigenstate s *)
  S[101] == {
    ClassName       -> s,
    SelfConjugate   -> True,
    Mass            -> {Mdil, 300.},
    Width           -> {Wdil, 1.0},
    PropagatorLabel -> "s",
    PropagatorType  -> D,
    PropagatorArrow -> None,
    PDG             -> 9000025,
    ParticleName    -> "s",
    FullName        -> "Dilaton"
  },

(* New physical fermion: vector-like top-quark partner T, same SU(3)xSU(2)xU(1) *)
(* quantum numbers as the SM right-handed top quark (colour triplet, SU(2) singlet, Y=2/3) *)
  F[101] == {
    ClassName        -> TQ,
    SelfConjugate    -> False,
    Indices          -> {Index[Colour]},
    Mass             -> {MTQ, 1000.},
    Width            -> {WTQ, 10.},
    QuantumNumbers   -> {Q -> 2/3},
    PDG              -> 8000006,
    PropagatorLabel  -> "TQ",
    PropagatorType   -> Straight,
    PropagatorArrow  -> Forward,
    ParticleName     -> "TQ",
    AntiParticleName -> "TQbar",
    FullName         -> "Top-quark partner"
  },

(* Unphysical gauge-basis dilaton field S = f + h sin(thetaS) + s cos(thetaS), Eq.(3) *)
  S[111] == {
    ClassName     -> Sf,
    Unphysical    -> True,
    SelfConjugate -> True,
    Definitions   -> { Sf -> fdil + H*Sin[thetaS] + s*Cos[thetaS] }
  },

(* Unphysical real neutral Higgs-doublet component Sqrt[2] Re[H0] = v + h cos(thetaS) - s sin(thetaS), Eq.(3) *)
  S[112] == {
    ClassName     -> Hgf,
    Unphysical    -> True,
    SelfConjugate -> True,
    Definitions   -> { Hgf -> vev + H*Cos[thetaS] - s*Sin[thetaS] }
  }
};

(* ************************** *)
(* *****   Lagrangian   ***** *)
(* ************************** *)

(* Free kinetic + mass term for the new physical scalar s *)
Lsdilkin := Block[{mu},
  1/2 del[s,mu] del[s,mu] - 1/2 Mdil^2 s^2
];

(* Free kinetic + mass term for the new physical fermion TQ (Dirac, vector-like) *)
LTQkin := Block[{mu},
  I*TQbar.Ga[mu].DC[TQ,mu] - MTQ*TQbar.TQ
];

(* New-physics scalar potential Vtilde(S,H), portal + self-interaction pieces only *)
(* (the bare mS^2, mH^2 pieces of Eq.(potential) are absorbed into the declared    *)
(* physical masses MH, Mdil above and are not written again here).                *)
LMDMpot := -(kappaMDM/4)*Sf^2*Hgf^2 - (lambdaHMDM/16)*Hgf^4 - (lambdaSMDM/24)*Sf^4;

(* Dilaton trace-anomaly coupling to the top partner: T-bar (M/f) S T, Eq.(MDM);   *)
(* the constant (M/f)*f = M piece is already the bare mass in LTQkin, so only the  *)
(* fluctuating h,s pieces are written here. *)
LMDMTcoup := -gTNP*( H*Sin[thetaS] + s*Cos[thetaS] )*TQbar.TQ;

(* y' T-bar_R (q3L . H) + h.c., Eq.(MDM); q3L.H = Eps[ii,jj] QL[ii] Phi[jj] *)
LMDMYuk := Block[{sp,ii,jj,cc,yukT},
  yukT = ExpandIndices[ yprime * TQbar[sp,cc].QL[sp,ii,3,cc] * Phi[jj] * Eps[ii,jj], FlavorExpand -> SU2D];
  yukT + HC[yukT]
];

LTotal := Lsdilkin + LTQkin + LMDMpot + LMDMTcoup + LMDMYuk;
```