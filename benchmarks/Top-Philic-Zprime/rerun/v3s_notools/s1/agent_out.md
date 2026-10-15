## Self-audit table

I read only the paper's LaTeX source and the supplied `SM.fr`. No cached or reference FeynRules file for this model was read.

The paper adds exactly one new particle: a colour-singlet, SU(2)-singlet, real (self-conjugate) massive vector resonance `V1`, called `Zp` below, coupling only to the top quark (Eq. v0inttop) with a width formula (Eq. width). No other new states, mixings, or EFT operators appear in the paper.

| term name | fields in monomial | dim d | coupling symbol | coupling dim (4-d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new-U(1) sum | B/L sum | CC[] used | fraction/root check | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpKin (kinetic) | Zp, Zp | 4 | 1 | 0 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | n/a | self-conjugate |
| LZpKin (mass) | Zp, Zp | 4 | MZp^2 | 2 (matches d=2 operator) | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | n/a | self-conjugate |
| LZpTop | tbar, t, Zp | 4 | ct·Cos[θ]/ct·Sin[θ] | 0 | n/a | -2/3+2/3+0=0 | Y(tbar)+Y(t)=0 | singlet (mass-eigenstate current) | colour-singlet bilinear (shared cc) | n/a | -1/3+1/3+0=0 | n/a | checked against Eq. v0inttop (θ appears as Cos/Sin, not a fraction or root) | self-Hermitian (tbar γ^μ P_{L,R} t is Hermitian on its own) |

Additional confirmations:
- Kinetic + mass term exists for the one new class (`Zp`) and is in `LTotal`.
- No non-fundamental colour representation is used (`Zp` is a colour singlet); no `AddGaugeRepresentation[...]` is needed.
- The only `SelfConjugate -> True` new class is `Zp`; it carries no `QuantumNumbers`.
- New names chosen: `Zp`, `MZp`, `WZp`, `ct`, `thetat`. None is a Mathematica built-in, a FeynRules symbol, or a name already declared in `SM.fr`.
- The single total Lagrangian is `LTotal`, defined as `LZpKin + LZpTop` (both terms are summed, nothing else is defined).
- No reference or cached model file was read: none.

```mathematica
(* ************************** *)
(* *****  Information   ***** *)
(* ************************** *)
M$ModelName = "Top-Philic-Zprime_gen";

M$Information = {
  Authors      -> {"Automated Lagrangian extraction"},
  Version      -> "1.0",
  Date         -> "17. 09. 2026",
  References   -> {"arXiv:1604.07421"}
};

(* ************************** *)
(* *** Interaction orders *** *)
(* ************************** *)
M$InteractionOrderHierarchy = {
  {QCD, 1},
  {QED, 2},
  {NP,  1}
};

(* ************************** *)
(* *****   Parameters   ***** *)
(* ************************** *)
M$Parameters = {

  (* External parameters *)
  ct == {
    ParameterType    -> External,
    BlockName        -> TOPPHILIC,
    OrderBlock       -> 1,
    Value            -> 2.0,
    InteractionOrder -> {NP, 1},
    TeX              -> Subscript[c, t],
    Description      -> "Overall coupling strength of the top-philic vector resonance V1 to top quarks, ct = Sqrt[cL^2+cR^2], Eq.(1) of 1604.07421"
  },
  thetat == {
    ParameterType -> External,
    BlockName     -> TOPPHILIC,
    OrderBlock    -> 2,
    Value         -> Pi/2,
    TeX           -> \[Theta],
    Description   -> "Chirality angle of the V1-top coupling, tan(theta) = cR/cL, Eq.(1) of 1604.07421; paper benchmark theta = pi/2 (purely right-handed coupling)"
  },

  (* Internal parameters *)
  WZp == {
    ParameterType -> Internal,
    Value         -> (ct^2 MZp)/(8 Pi) Sqrt[1 - 4 MT^2/MZp^2] (1 - (MT^2/MZp^2) (1 - 3 Sin[2 thetat])),
    TeX           -> Subscript[\[CapitalGamma], Zp],
    Description   -> "Total width of the top-philic resonance V1 -> t tbar, Eq.(2) of 1604.07421"
  }
};

(* ************************** *)
(* **** Particle classes **** *)
(* ************************** *)
M$ClassesDescription = {

(* New colour- and SU(2)-singlet vector resonance V1 (top-philic Z'), Sec. II A of 1604.07421 *)
  V[100] == {
    ClassName       -> Zp,
    SelfConjugate   -> True,
    Mass            -> {MZp, 1500.},
    Width           -> {WZp, Internal},
    PropagatorLabel -> "Zp",
    PropagatorType  -> Sine,
    PropagatorArrow -> None,
    PDG             -> 32,
    ParticleName    -> "zp",
    FullName        -> "Top-philic vector resonance V1"
  }
};

(* ************************** *)
(* *****   Lagrangian   ***** *)
(* ************************** *)

(* Free kinetic + mass term for the new vector resonance (real singlet vector) *)
LZpKin := Block[{mu, nu},
  -1/4 FS[Zp, mu, nu] FS[Zp, mu, nu] + 1/2 MZp^2 Zp[mu] Zp[mu]
];

(* Top-philic current: L = tbar.Ga[mu].(cL ProjM + cR ProjP).t Zp[mu], Eq.(1) of 1604.07421,
   with cL = ct Cos[thetat], cR = ct Sin[thetat] *)
LZpTop := Block[{mu},
  ct (Cos[thetat] tbar.Ga[mu].ProjM.t + Sin[thetat] tbar.Ga[mu].ProjP.t) Zp[mu]
];

LTotal := LZpKin + LZpTop;
```