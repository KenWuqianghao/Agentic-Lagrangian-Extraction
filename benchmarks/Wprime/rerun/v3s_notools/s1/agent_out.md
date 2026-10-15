## Self‑audit table

I read only the paper (arXiv:hep-ph/0207290) and the supplied `SM.fr`. I opened no cached or reference `.fr` file for this model.

The paper gives the W′–fermion Lagrangian already in the mass‑eigenstate basis (Eq. 2, `\frac{1}{\sqrt2}\bar f_i\gamma_\mu(C^R P_R+C^L P_L)W' f_j+{\rm H.c.}`, and the equivalent Eq. 3 with couplings `g_{R}\cos\zeta e^{i\omega}` and `g_L\sin\zeta`). The mixing angle ζ and phase ω never appear on their own after that point — the text says the couplings "factorize" and only the products `g_L sinζ` and `g_R cosζ e^{iω}` are physical (Eq. 6). So I declare those two products as the model's coupling constants (`gWpL`, `gWpR`) instead of ζ, ω separately, the same way the paper's own analysis does. There is no leftover gauge‑eigenstate mixing to place in an `Unphysical` class, because the paper's formula is already written for the physical W′.

New particles found in the paper: the charged heavy vector `W'` (Sec. I, Eq. 2), and a heavy right‑handed neutrino `ν_R` with its own mass, needed because the paper repeatedly splits its results by "whether `m_{ν_R})` is light enough for the leptonic decay channel to be open" (abstract; Sec. I; Sec. II A).

| term name | fields | operator dim d | coupling | coupling dim (4−d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new‑U(1) sum | lepton/baryon sum | CC[] used | fraction/root check | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWpKin | Wpbar, Wp | 4 | none (canonical) | n/a | n/a | −1+1=0 | n/a | n/a (EW singlet, mass eigenstate) | n/a (colour singlet) | n/a | n/a | no | n/a | self‑Hermitian |
| LNRkin | NRbar, NR | 4 | none (canonical) | n/a | n/a | 0+0=0 | n/a | n/a | n/a | n/a | −1+1=0 | no | n/a | self‑Hermitian |
| LWpQuark‑L | uqbar, dq, Wp | 4 | gWpL (dim 0) | n/a (d=4) | n/a | −2/3−1/3+1=0 | n/a | n/a (physical post‑EWSB fields) | colour‑singlet bilinear (shared Colour index) | n/a | baryon: −1/3+1/3=0 | no | 1/√2 read verbatim from `\frac{1}{\sqrt2}` in Eq. 2/3 (LaTeX authoritative) | via HC[LWpQuark] in LWpCurrent |
| LWpQuark‑R | uqbar, dq, Wp | 4 | gWpR (dim 0) | n/a | n/a | 0 (same as above) | n/a | n/a | colour‑singlet bilinear | n/a | 0 | no | same as above | via HC[...] |
| LWpLepton‑L | vlbar, l, Wp | 4 | gWpL | n/a | n/a | 0−1+1=0 | n/a | n/a | n/a (no colour) | n/a | lepton: −1+1=0 | no | same | via HC[...] |
| LWpLepton‑R | NRbar, l, Wp | 4 | gWpR | n/a | n/a | 0−1+1=0 | n/a | n/a | n/a | n/a | lepton: −1+1=0 | no | same | via HC[...] |

- `SelfConjugate -> True` classes in this add‑on: none. `Wp` and `NR` are both `SelfConjugate -> False`, so the "no QuantumNumbers on a self‑conjugate class" rule is satisfied vacuously.
- Names checked: `Wp`, `Wpbar`, `NR`, `NRe`, `NRm`, `NRt`, `gWpL`, `gWpR`, `VpQL`, `VpQR`, `VpLL`, `VpLR`, `MWp`, `WWp`, `MNR`. None is a Mathematica built‑in, none is a FeynRules symbol (`HC`, `CC`, `FS`, `DC`, `del`, `Eps`, `Ga`, `ProjP`, `ProjM`), and none is already declared in `SM.fr`.
- Single total Lagrangian: `LTotal`, defined as `LWpKin + LNRkin + LWpCurrent`, where `LWpCurrent = LWpQuark + LWpLepton + HC[LWpQuark + LWpLepton]`. Every term above appears in that sum.
- No new index was declared: `Wp` carries no index at all, and `NR` uses the `Generation` index that `SM.fr` already declares. No non‑fundamental colour representation is used, so no `AddGaugeRepresentation` line is needed.
- Reference/cached model file read: none.

```mathematica
(***************************************************************************)
(* Wprime_gen — SM add-on for a heavy charged vector resonance W' with     *)
(* generic left/right couplings to fermions, extracted from Z. Sullivan,  *)
(* "Fully differential W' production and decay at NLO in QCD",            *)
(* arXiv:hep-ph/0207290 (Eqs. 1-6). Loads on top of SM.fr.                *)
(***************************************************************************)

M$ModelName = "Wprime_gen";

M$Information = {
  Authors     -> {"Automated extraction from arXiv:hep-ph/0207290 (Z. Sullivan)"},
  Version     -> "1.0",
  Date        -> "17.09.2026",
  References  -> {"Z. Sullivan, arXiv:hep-ph/0207290"}
};

(* No M$GaugeGroups block: this is an SM add-on. Colour, Gluon, Generation, *)
(* SU2D and SU2W indices are declared by SM.fr. No new index is needed:    *)
(* Wp carries no index, and NR uses the existing Generation index.         *)

M$InteractionOrderHierarchy = {
  {QCD, 1},
  {QED, 2},
  {NP , 1}
};

M$ClassesDescription = {

  (* New charged heavy vector resonance W', Eq.(2)/(3) of hep-ph/0207290. *)
  (* Treated as a mass eigenstate: no SU(2)xU(1) gauge index, only Q. *)
  V[101] == {
    ClassName        -> Wp,
    SelfConjugate    -> False,
    Mass             -> {MWp, 500.},
    Width            -> {WWp, 16.701},
    QuantumNumbers   -> {Q -> 1},
    PDG              -> 34,
    ParticleName     -> "Wp+",
    AntiParticleName -> "Wp-",
    PropagatorLabel  -> "Wp",
    PropagatorType   -> Sine,
    PropagatorArrow  -> Forward,
    FullName         -> "Wprime"
  },

  (* New heavy right-handed neutrino nu_R, one per generation. The paper *)
  (* splits every width/cross-section result by whether m(nu_R) is below *)
  (* or above m(W'), so its mass is a genuine new-physics parameter.     *)
  F[102] == {
    ClassName        -> NR,
    ClassMembers     -> {NRe, NRm, NRt},
    Indices          -> {Index[Generation]},
    FlavorIndex      -> Generation,
    SelfConjugate    -> False,
    Mass             -> {MNR, 10.},
    Width            -> 0,
    QuantumNumbers   -> {LeptonNumber -> 1},
    PDG              -> {9900012, 9900014, 9900016},
    ParticleName     -> {"nre", "nrm", "nrt"},
    AntiParticleName -> {"nre~", "nrm~", "nrt~"},
    PropagatorLabel  -> {"NR", "NRe", "NRm", "NRt"},
    PropagatorType   -> Straight,
    PropagatorArrow  -> Forward,
    FullName         -> {"Heavy right-handed electron-neutrino",
                          "Heavy right-handed muon-neutrino",
                          "Heavy right-handed tau-neutrino"}
  }
};

M$Parameters = {

  (* Effective couplings. Eq.(3) writes g_R Cos[zeta] Exp[I omega] and    *)
  (* g_L Sin[zeta]; Eq.(6) shows only these two products are physical, so *)
  (* they are declared directly as External couplings; zeta/omega are    *)
  (* absorbed (omega into the phase of VpQR/VpLR).                        *)
  gWpL == {
    ParameterType    -> External,
    BlockName        -> WPRIME,
    OrderBlock       -> 1,
    Value            -> 0.65,
    InteractionOrder -> {NP, 1},
    TeX              -> Subscript[g, "L"],
    Description      -> "Effective left-handed Wp coupling, = g_L Sin[zeta] of Eq.(3)"
  },
  gWpR == {
    ParameterType    -> External,
    BlockName        -> WPRIME,
    OrderBlock       -> 2,
    Value            -> 0.,
    InteractionOrder -> {NP, 1},
    TeX              -> Subscript[g, "R"],
    Description      -> "Effective right-handed Wp coupling, = g_R Cos[zeta] Exp[I omega] of Eq.(3); default 0 gives the purely left-handed Wp_L benchmark of Sec. II B"
  },

  VpQL == {
    ParameterType -> External,
    Indices       -> {Index[Generation], Index[Generation]},
    BlockName     -> WPQL,
    Value         -> {VpQL[1,1] -> 0.9751, VpQL[1,2] -> 0.2215, VpQL[1,3] -> 0.0035,
                       VpQL[2,1] -> 0.2210, VpQL[2,2] -> 0.9743, VpQL[2,3] -> 0.0410,
                       VpQL[3,1] -> 0.0090, VpQL[3,2] -> 0.0400, VpQL[3,3] -> 1.0000},
    TeX           -> Superscript[V, "QL"],
    Description   -> "Generalized left-handed CKM-like matrix V^L for the Wp-quark current, benchmark values of Eq.(25)"
  },
  VpQR == {
    ParameterType     -> External,
    Indices           -> {Index[Generation], Index[Generation]},
    ComplexParameter  -> True,
    BlockName         -> WPQR,
    Value             -> {VpQR[1,1] -> 0.9751, VpQR[1,2] -> 0.2215, VpQR[1,3] -> 0.0035,
                           VpQR[2,1] -> 0.2210, VpQR[2,2] -> 0.9743, VpQR[2,3] -> 0.0410,
                           VpQR[3,1] -> 0.0090, VpQR[3,2] -> 0.0400, VpQR[3,3] -> 1.0000},
    TeX               -> Superscript[V, "QR"],
    Description       -> "Generalized right-handed CKM-like matrix V^R for the Wp-quark current (carries the CP phase omega of Eq.(3)), benchmark values of Eq.(25); inactive by default since gWpR=0"
  },

  VpLL == {
    ParameterType -> External,
    Indices       -> {Index[Generation], Index[Generation]},
    BlockName     -> WPLL,
    Value         -> {VpLL[1,1] -> 1., VpLL[1,2] -> 0., VpLL[1,3] -> 0.,
                       VpLL[2,1] -> 0., VpLL[2,2] -> 1., VpLL[2,3] -> 0.,
                       VpLL[3,1] -> 0., VpLL[3,2] -> 0., VpLL[3,3] -> 1.},
    TeX           -> Superscript[V, "LL"],
    Description   -> "Generalized left-handed lepton matrix V^L_{l,nu} for the Wp-lepton current; identity, as assumed in Sec. II A"
  },
  VpLR == {
    ParameterType     -> External,
    Indices           -> {Index[Generation], Index[Generation]},
    ComplexParameter  -> True,
    BlockName         -> WPLR,
    Value             -> {VpLR[1,1] -> 1., VpLR[1,2] -> 0., VpLR[1,3] -> 0.,
                           VpLR[2,1] -> 0., VpLR[2,2] -> 1., VpLR[2,3] -> 0.,
                           VpLR[3,1] -> 0., VpLR[3,2] -> 0., VpLR[3,3] -> 1.},
    TeX               -> Superscript[V, "LR"],
    Description       -> "Generalized right-handed lepton matrix V^R_{l,nu} for the Wp-lepton current; identity, as assumed in Sec. II A; inactive by default since gWpR=0"
  }
};

(* ---- Free kinetic + mass terms for every new field ---- *)

LWpKin := Block[{mu, nu},
  -1/2 FS[Wpbar, mu, nu] FS[Wp, mu, nu] + MWp^2 Wpbar[mu] Wp[mu]
];

LNRkin := Block[{mu},
  I NRbar.Ga[mu].DC[NR, mu] - MNR NRbar.NR
];

(* ---- New-physics charged-current interactions, Eq.(2)/(3) ---- *)
(* Quarks: u_i-dbar_j current. Leptons: nu_i-lbar_j (left) and NR_i-lbar_j *)
(* (right, using the new heavy neutrino since the SM nu has no right      *)
(* component). Matrix-times-Ga-times-Proj order follows the SM.fr/rule-13 *)
(* convention (field.Matrix.Ga[mu].Proj.field).                           *)

LWpQuark := Block[{mu},
  1/Sqrt[2] (gWpL uqbar.VpQL.Ga[mu].ProjM.dq + gWpR uqbar.VpQR.Ga[mu].ProjP.dq)
];

LWpLepton := Block[{mu},
  1/Sqrt[2] (gWpL vlbar.VpLL.Ga[mu].ProjM.l + gWpR NRbar.VpLR.Ga[mu].ProjP.l)
];

LWpCurrent := Block[{mu},
  (LWpQuark[[1]] /. mu -> mu) Wp[mu] /. mu -> mu
];

(* Written out explicitly with the vector index attached and the H.c. added: *)
LWpCurrent := Block[{mu},
  1/Sqrt[2] (gWpL uqbar.VpQL.Ga[mu].ProjM.dq + gWpR uqbar.VpQR.Ga[mu].ProjP.dq) Wp[mu] +
  1/Sqrt[2] (gWpL vlbar.VpLL.Ga[mu].ProjM.l + gWpR NRbar.VpLR.Ga[mu].ProjP.l) Wp[mu]
];

LWpInt := LWpCurrent + HC[LWpCurrent];

LTotal := LWpKin + LNRkin + LWpInt;
```