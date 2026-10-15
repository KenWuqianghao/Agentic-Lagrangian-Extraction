## Self‑audit table

No reference or cached FeynRules file for SMWeinberg was read — only the paper's LaTeX source and SM.fr, as given. New particle: one Majorana fermion `NM` (paper's "N"; renamed because `N` is a Mathematica builtin). It is an auxiliary state that carries the `(ν_ℓν_ℓ'^c)` current of the Weinberg operator (paper Eqs. 7–10); it does **not** mix with `vl` (no mass matrix to diagonalize, so rule 8 does not apply here). All vertices below are the paper's own post‑EWSB Lagrangian (appendix, verified against the raw LaTeX `\frac{...}{...}` and `\sqrt{...}` commands, so no fraction/root placement is ambiguous). Convention: for a term, an un‑barred field contributes `+Q`, a barred field contributes `−Q`; `Y` is not tracked because this is a post‑EWSB (mass‑eigenstate) Lagrangian where only `Q` survives as a good quantum number.

| term | fields | dim d | coupling | coupling dim (4‑d) | 1/Λ power | Q sum | Y | SU(2) | SU(3) | new‑U(1) | L sum | CC[] used | fraction/root check | H.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LNMfree` (kin+mass) | NMbar,∂,NM / NMbar,NM | 4 / 3 | 1 / `mN` | 0 / 1 | n/a | 0 | n/a | singlet | singlet | n/a | n/a (Majorana) | n/a | n/a | self‑conjugate |
| Line1 `W‑N‑l` | W,NMbar,l | 4 | `gw` | 0 | n/a | +1+0−1=0 | n/a | post‑EWSB | singlet | n/a | l:+1,N:n/a | no | Eq.(lagCC)=appendix line1, `gw/√2`, exact | via `HC[LNint]` |
| Line2 `Z‑N‑ν` | Z,NMbar,vl | 4 | `gw/(2cw)` | 0 | n/a | 0 | n/a | post‑EWSB | singlet | n/a | ν:+1,N:n/a | no | `1/(2cosθW)`, exact | via HC |
| Line3a `h‑N‑ν` | H,NMbar,vl | 4 | `gw*mN/(2MW)` | 0 | n/a | 0 | n/a | post‑EWSB | singlet | n/a | n/a | no | `\frac{g_Wm_N}{2m_W}`, exact | via HC |
| Line3b `hh‑N‑ν` | H,H,NMbar,vl | 5 | `gw^2*mN/(8MW^2)` | −1 | n/a (MW‑suppressed, not a new Λ) | 0 | n/a | post‑EWSB | singlet | n/a | n/a | no | product of `1/(2m_W)`×`1/(4m_W)`, exact | via HC |
| Line4a `G+‑N‑l` | GP,(NMbar,l / lbar^c,NM) | 4 | `gw*mN/(2√2 MW)` | 0 | n/a | +1+0−1=0 / +1−1+0=0 | n/a | post‑EWSB | singlet | n/a | l:+1/N:n/a | yes (`CC[l]`) | `\frac{g_Wm_N}{2\sqrt2 m_W}`, exact | via HC |
| Line4b `G+h‑N‑l` | GP,H,(NMbar,l / lbar^c,NM) | 5 | `gw^2*mN/(4√2MW^2)` | −1 | n/a (MW‑suppressed) | 0 | n/a | post‑EWSB | singlet | n/a | as above | yes | same √2 placement, exact | via HC |
| Line5a `G0‑N‑ν` | G0,NMbar,vl | 4 | `gw*mN/(2MW)` | 0 | n/a | 0 | n/a | post‑EWSB | singlet | n/a | n/a | no | `\frac{g_Wm_N}{2m_W}`, exact | via HC |
| Line5b `G0h‑N‑ν` | G0,H,NMbar,vl | 5 | `gw^2*mN/(4MW^2)` | −1 | n/a (MW‑suppressed) | 0 | n/a | post‑EWSB | singlet | n/a | n/a | no | exact | via HC |
| Line6a `G+G+‑l‑l'` | GP,GP,lbar^c,l (ff1≠ff2 allowed) | 5 | `gw^2*mN/(4MW^2)` | −1 | n/a (MW‑suppressed) | +2−1−1=0 | n/a | post‑EWSB | singlet | n/a | n/a | yes (`CC[l]`) | `2·\frac{g_W^2m_N}{8m_W^2}`, exact | via HC |
| Line6b `G0G0‑N‑ν` | G0,G0,NMbar,vl | 5 | `gw^2*mN/(8MW^2)` | −1 | n/a (MW‑suppressed) | 0 | n/a | post‑EWSB | singlet | n/a | n/a | no | exact | via HC |
| Line7 `G0G+‑N‑l` | G0,GP,(NMbar,l / lbar^c,NM) | 5 | `gw^2*mN/(4√2MW^2)` | −1 | n/a (MW‑suppressed) | 0 | n/a | post‑EWSB | singlet | n/a | as Line4 | yes | exact | via HC |
| `HC[LNint]` | H.c. of all lines above | — | — | — | — | 0 (conjugate) | n/a | — | — | — | — | n/a | n/a | supplies missing chirality of Lines1,2,3a,3b,5a,5b,6b |

- No non‑fundamental colour representation is introduced anywhere in this add‑on; no `AddGaugeRepresentation[...]` line is needed.
- `SelfConjugate -> True` classes: only `NM`; it carries no `QuantumNumbers` (confirmed by the declaration below).
- Chosen names — classes: `NM`; parameters: `Lambda`, `Cll`, `mN`, `wN`. None is a Mathematica builtin, a FeynRules symbol, or an SM.fr name (bare `N` was deliberately avoided).
- Single total Lagrangian: `LTotal := LSM + LNMfree + LNint + LNintHC`, where `LNintHC = HC[LNint]` and `LNint` sums Lines 1–7 above.
- Reference/cached model file read: none.

```mathematica
(***************************************************************************************************************)
(******   FeynRules add-on: Weinberg operator via an auxiliary Majorana state (arXiv:2012.09882)          ******)
(******   Loaded on top of SM.fr (Standard Model, v1.4.7)                                                  ******)
(***************************************************************************************************************)

M$ModelName = "SMWeinberg_gen";

M$Information = {
  Authors      -> {"Automated extraction from arXiv:2012.09882 (Fuks, Neundorf, Peters, Ruiz, Saimpert)"},
  Version      -> "1.0",
  Date         -> "17.09.2026",
  Institutions -> {"extracted add-on model"},
  URLs         -> "https://arxiv.org/abs/2012.09882"
};

(* extend the SM.fr order hierarchy with the new-physics order NP, carried by the Weinberg-operator
   Wilson coefficient Cll and by the auxiliary mass mN derived from it *)
M$InteractionOrderHierarchy = {
  {QCD, 1},
  {QED, 2},
  {NP,  1}
};

(* ************************** *)
(* *****  New particle  ***** *)
(* ************************** *)
(* NM models the (nu_l nu_l'^c) current of the d=5 Weinberg operator as an auxiliary Majorana
   fermion, Eqs. (7)-(10) and the appendix of arXiv:2012.09882. It does not mix with the SM
   neutrinos vl (no mass matrix to diagonalize): it is an independent, self-conjugate state. *)
M$ClassesDescription = {
  F[100] == {
    ClassName       -> NM,
    SelfConjugate   -> True,
    Mass            -> {mN, Internal},
    Width           -> {wN, Internal},
    PropagatorLabel -> "NM",
    PropagatorType  -> Straight,
    PropagatorArrow -> None,
    PDG             -> 9900012,
    ParticleName    -> "n5",
    FullName        -> "Effective Majorana neutrino (Weinberg-operator current)"
  }
};

(* ************************** *)
(* *****   Parameters   ***** *)
(* ************************** *)
M$Parameters = {

  (* External parameters *)
  Lambda == {
    ParameterType    -> External,
    BlockName        -> NUPHYSICS,
    OrderBlock       -> 1,
    Value            -> 200000.,
    Description      -> "Weinberg-operator EFT cutoff Lambda [GeV], Eq. (2); benchmark Lambda=200 TeV, the scale above which the (nu nu^c) expansion of Eq. (10)-(11) is valid"
  },

  Cll == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    Symmetric        -> True,
    ComplexParameter -> False,
    BlockName        -> NUPHYSICS,
    OrderBlock       -> {2, 3, 4, 5, 6, 7},
    Value            -> {Cll[1,1] -> 0, Cll[1,2] -> 0, Cll[1,3] -> 0,
                          Cll[2,2] -> 1, Cll[2,3] -> 0, Cll[3,3] -> 0},
    InteractionOrder -> {NP, 1},
    TeX              -> Subscript[C,5],
    Description      -> "Weinberg-operator Wilson coefficient C_5^{ll'}, Eq. (2); flavour-symmetric 3x3 matrix in (e,mu,tau); benchmark C_5^{mumu}=1, others 0 (paper's mu mu benchmark)"
  },

  (* Internal parameters *)
  mN == {
    ParameterType    -> Internal,
    Value            -> Abs[Cll[1,1] + Cll[1,2] + Cll[1,3] + Cll[2,2] + Cll[2,3] + Cll[3,3]] * vev^2 / Lambda,
    InteractionOrder -> {NP, 1},
    TeX              -> Subscript[m,N],
    Description      -> "Effective Majorana mass of the auxiliary state NM that encodes the (nu nu^c) current, Eq. (9)"
  },

  wN == {
    ParameterType -> Internal,
    Value         -> 0,
    TeX           -> Subscript[\[CapitalGamma], N],
    Description   -> "Width of the auxiliary state NM; the paper gives no analytic formula for it (NM enters only as the off-shell (nu nu^c) current of Eqs. (7)-(8)), so it defaults to zero and should be computed numerically if NM is ever produced on-shell"
  }
};

(* ************************** *)
(* *****   Lagrangian   ***** *)
(* ************************** *)

(* Free kinetic + Majorana mass term for NM, required for completeness even though the paper
   only exhibits the interaction Lagrangian. *)
LNMfree := Block[{mu},
  ExpandIndices[ I/2 NMbar.Ga[mu].del[NM,mu] - 1/2 mN NMbar.NM ]
];

(* Interaction Lagrangian, transcribed verbatim from the appendix of arXiv:2012.09882
   ("the interaction Lagrangian by which we extend the SM Lagrangian in the SMWeinberg UFO"),
   with the overall Hermitian conjugate added separately below (the paper states the H.c.
   applies to the full expression, not just the last line). *)
LNint := Block[{mu, ff1, ff2},
  ExpandIndices[
    (* line 1: W+ - NM - l  (Eq. lagCC / appendix line 1) *)
    -(gw/Sqrt[2]) W[mu] NMbar.Ga[mu].ProjM.l
    (* line 2: Z - NM - nu *)
    -(gw/(2*cw)) Z[mu] NMbar.Ga[mu].ProjM.vl
    (* line 3: h - NM - nu  and  hh - NM - nu *)
    -(gw*mN/(2*MW)) H NMbar.ProjM.vl
    -(gw^2*mN/(8*MW^2)) H H NMbar.ProjM.vl
    (* line 4: G+ - NM - l  and  G+ h - NM - l *)
    -I*(gw*mN/(2*Sqrt[2]*MW)) GP (NMbar.ProjM.l + bar[CC[l]].ProjM.NM)
    -I*(gw^2*mN/(4*Sqrt[2]*MW^2)) GP H (NMbar.ProjM.l + bar[CC[l]].ProjM.NM)
    (* line 5: G0 - NM - nu  and  G0 h - NM - nu *)
    -I*(gw*mN/(2*MW)) G0 NMbar.ProjM.vl
    -I*(gw^2*mN/(4*MW^2)) G0 H NMbar.ProjM.vl
    (* line 6: quartic Goldstone terms; the G+G+ piece is an independent double flavour sum *)
    +(gw^2*mN/(4*MW^2)) GP GP Module[{sp1, sp2}, bar[CC[l[sp1,ff1]]] ProjM[sp1,sp2] l[sp2,ff2]]
    +(gw^2*mN/(8*MW^2)) G0 G0 NMbar.ProjM.vl
    (* line 7: mixed quartic Goldstone term *)
    +(gw^2*mN/(4*Sqrt[2]*MW^2)) G0 GP (NMbar.ProjM.l + bar[CC[l]].ProjM.NM),
  FlavorExpand -> Generation]
];

LNintHC := HC[LNint];

LTotal := LSM + LNMfree + LNint + LNintHC;
```