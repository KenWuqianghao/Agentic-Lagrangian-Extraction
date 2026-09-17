## Self-audit table

| term | fields | dim d | coupling | coupling dim (4−d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | new-U(1)_X sum | lepton/baryon | CC[] | fraction/root check | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LXkin (kinetic) | X, X (via FS) | 4 | 1 | 0 ✓ | n/a | 0 | n/a | singlet | singlet | n/a (gauge kin. term) | n/a | n/a | n/a | self-conjugate |
| LXkin (mass) | X, X | 2 | MX² | dim 2 ✓ | n/a (d≤4) | 0 | n/a | singlet | singlet | n/a | n/a | n/a | n/a | self-conjugate |
| LPortalNeutral, XZZ term | Z, X, ∂Z | 4 | c1·sw (dimensionless) | 0 ✓ | n/a | 0+0+0=0 ✓ | n/a (post-EWSB mass basis) | n/a (unitary-gauge reduction of Eq.(48)) | singlet | n/a | n/a | n/a | Eq.(40) Γ_XZZ, Eq.(59) | self-conjugate (all real fields) |
| LPortalNeutral, XZγ term | Z, X, ∂A | 4 | c1·cw | 0 ✓ | n/a | 0 ✓ | n/a | n/a | singlet | n/a | n/a | n/a | Eq.(40) Γ_XZγ, ratio Eq.(55)=2cw²/sw² verified against Eq.(41) | self-conjugate |
| LPortalCharged, XW⁺W⁻ | W, X, ∂Wbar | 4 | c2 | 0 ✓ | n/a | (+1)+0+(−1)=0 ✓ | n/a | n/a | singlet | n/a | n/a | n/a | Eq.(40) Γ_XWW, Eq.(41) numeric coeff. (1.03 TeV) internally consistent with 45 GeV/307 GeV | +HC[LPortalCharged] (needed; not self-conjugate alone) |

- Kinetic+mass check: X (V[101]) has LXkin (kinetic + Proca mass) defined and summed into LTotal.
- No non-fundamental colour representation is used (X is a colour singlet); no `AddGaugeRepresentation[...]` needed.
- `SelfConjugate -> True` classes: only X (V[101]); it carries no `QuantumNumbers` (Q=Y=0, singlet) — confirmed.
- New symbols introduced: `X, MX, WX, c1, c2, NP, LXkin, LPortalNeutral, LPortalCharged, LTotal, NPCOUPLINGS`. None is a Mathematica builtin, a FeynRules reserved symbol (`N,C,D,E,I,K,O,HC,CC,FS,DC,del,Eps,Ga,ProjP,ProjM`), or a name SM.fr already declares.
- Single total Lagrangian: `LTotal := LSM + LXkin + LPortalNeutral + LPortalCharged + HC[LPortalCharged]` — sums every term this file defines, plus the imported SM.fr `LSM`.
- Reference/cached model file read: none. Only the SM.fr text and the paper's LaTeX source given in this prompt were used.

Design note (physics): the paper's own heavy chiral fermions (Secs. 2–4) that generate the anomaly-driven portal are integrated out at the high scale and are explicitly stated to be inaccessible at LHC energies; they fix, in the UV completion, arbitrary Wilson coefficients c1, c2 of Eq.(48) — they are not part of this low-energy spectrum, so the only new on-shell particle is the massive vector X. Eq.(48) is non-polynomial in H; the paper itself reduces it, in the EW-broken/unitary phase (Dθ_X → X, SM Goldstones eaten), to the polynomial component form of Eq.(59)/Eq.(15) with vertices Eq.(40) and widths Eq.(41), which is what is implemented below directly in the SM.fr mass eigenstates Z, A, W, Wbar. No separate θ_X Goldstone class is introduced since it carries no independent on-shell degree of freedom.

```mathematica
(* ============================================================ *)
(* ChernSimonsPortal add-on for SM.fr                            *)
(* Based on arXiv:0901.0639 (Antoniadis, Boyarsky, Espahbodi,     *)
(* Ruchayskiy, Wells), "Anomaly driven signatures of new          *)
(* invisible physics at the Large Hadron Collider".                *)
(* Loaded on top of SM.fr (no M$GaugeGroups block: add-on).        *)
(* No new index ranges are needed (X carries no internal index).   *)
(* No reference/cached model file was read; only SM.fr and the     *)
(* paper's LaTeX source were used.                                 *)
(* ============================================================ *)

M$ModelName = "ChernSimonsPortal_gen";

M$Information = {
  Authors    -> {"FeynRules extraction agent"},
  Version    -> "1.0",
  Date       -> "17. 09. 2026",
  References -> {"arXiv:0901.0639"}
};

(* ------------------------------------------------------------ *)
(* Physics content: the heavy chiral fermions of Secs. 2-4 that   *)
(* generate the anomaly-induced portal are integrated out at the  *)
(* high scale (too heavy for LHC) and are NOT part of this        *)
(* low-energy spectrum; they only fix, in the UV theory, the      *)
(* dimensionless Wilson coefficients c1, c2 of Eq.(48), which the *)
(* paper states "can have arbitrary values, determined entirely   *)
(* by the properties of the high-energy theory". The only new     *)
(* on-shell state is the massive Stueckelberg vector X (Eq.(39)), *)
(* SM-singlet (SM fields are not charged under U(1)_X).           *)
(*                                                                 *)
(* The covariant portal Lagrangian Eq.(48),                        *)
(*   c1 (H^dag D H /|H|^2) D theta_X F_Y                            *)
(*   + c2 (H F_W D H^dag /|H|^2) D theta_X ,                        *)
(* is non-polynomial in H; the paper itself reduces it, in the     *)
(* EW-broken/unitary phase (D theta_X -> X, SM Goldstones eaten     *)
(* by W/Z), to the polynomial component form of Eq.(59)/Eq.(15),   *)
(* with vertex functions Eq.(40) and partial widths Eq.(41). That  *)
(* polynomial form is implemented below directly in the SM.fr mass *)
(* eigenstates Z, A, W, Wbar. No separate theta_X Goldstone class  *)
(* is introduced: it carries no independent on-shell d.o.f.        *)

M$InteractionOrderHierarchy = {
  {QCD, 1},
  {QED, 2},
  {NP,  1}
};

(* ------------------------------------------------------------ *)
(* Parameters                                                     *)
(* ------------------------------------------------------------ *)
M$Parameters = {

  (* External parameters *)
  c1 == {
    ParameterType    -> External,
    BlockName        -> NPCOUPLINGS,
    OrderBlock       -> 1,
    Value            -> 1.,
    InteractionOrder -> {NP, 1},
    TeX              -> Subscript[c,1],
    Description      -> "Dimensionless XZZ/XZgamma portal coefficient, Eq.(48)/Eq.(40)"
  },
  c2 == {
    ParameterType    -> External,
    BlockName        -> NPCOUPLINGS,
    OrderBlock       -> 2,
    Value            -> 1.,
    InteractionOrder -> {NP, 1},
    TeX              -> Subscript[c,2],
    Description      -> "Dimensionless XW+W- portal coefficient, Eq.(48)/Eq.(40)"
  },

  (* Internal parameters *)
  WX == {
    ParameterType -> Internal,
    Value         -> (c1^2 sw2 MX^3)/(192 Pi MZ^2) (1 - 4 MZ^2/MX^2)^(5/2)
                     + (c2^2 MX^3)/(48 Pi MW^2) (1 - 4 MW^2/MX^2)^(5/2)
                     + (c1^2 cw^2 MX^3)/(96 Pi MZ^2) (1 - MZ^2/MX^2)^3 (1 + MZ^2/MX^2),
    Description   -> "Total width of X: Gamma(X->ZZ)+Gamma(X->WW)+Gamma(X->Zgamma), Eq.(41)"
  }
};

(* ------------------------------------------------------------ *)
(* Particle classes                                               *)
(* ------------------------------------------------------------ *)
M$ClassesDescription = {

  (* Chern-Simons portal vector: Stueckelberg-massive U(1)_X boson, *)
  (* SM-singlet (Eq.(39)); no QuantumNumbers since SelfConjugate.   *)
  V[101] == {
    ClassName       -> X,
    SelfConjugate   -> True,
    Mass            -> {MX, 1000.},
    Width           -> {WX, Internal},
    ParticleName    -> "X",
    PDG             -> 5000023,
    PropagatorLabel -> "X",
    PropagatorType  -> Sine,
    PropagatorArrow -> None,
    FullName        -> "Chern-Simons portal vector boson"
  }

};

(* ------------------------------------------------------------ *)
(* Lagrangian                                                      *)
(* ------------------------------------------------------------ *)

(* Free kinetic + Proca mass term for the new vector X, rule-1 form *)
LXkin := Block[{mu,nu}, -1/4 FS[X,mu,nu] FS[X,mu,nu] + 1/2 MX^2 X[mu] X[mu]];

(* Neutral-current portal: unitary-gauge reduction of Eq.(48)/(15), *)
(* using SM.fr's B[mu] -> -sw Z[mu] + cw A[mu] (F_Y = -sw FS[Z] +   *)
(* cw FS[A]), giving the XZZ and XZgamma couplings of Eq.(40)/(59). *)
LPortalNeutral := Block[{mu,nu,la,rho},
  -c1 sw Eps[mu,nu,la,rho] Z[mu] X[nu] del[Z[rho],la]
  +c1 cw Eps[mu,nu,la,rho] Z[mu] X[nu] del[A[rho],la]
];

(* Charged-current portal: the c2 term of Eq.(48), giving the       *)
(* XW+W- coupling of Eq.(40)/(59); +HC for a Hermitian Lagrangian.  *)
LPortalCharged := Block[{mu,nu,la,rho},
  c2 Eps[mu,nu,la,rho] W[mu] X[nu] del[Wbar[rho],la]
];

LTotal := LSM + LXkin + LPortalNeutral + LPortalCharged + HC[LPortalCharged];
```