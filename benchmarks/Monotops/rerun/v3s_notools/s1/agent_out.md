## Self-audit (produced before the model)

Fields extracted from Eq. (eq:lag) of the paper (paper's own notation kept in parentheses):

- `phi0` (paper's plain φ): real scalar, colour singlet, Q=0. FCNC coupling to up-type quarks.
- `Vnp` (paper's V): real vector, colour singlet, Q=0. FCNC coupling to up-type quarks.
- `chi` (paper's χ): Dirac fermion, colour singlet, Q=0. Invisible state (paper leaves its statistics generic; a Dirac field is the simplest choice consistent with Q=0).
- `PhiS` (paper's φ, i.e. varphi_i, "S" in the intro): complex scalar, colour triplet, Q=+2/3. Resonant diquark + t‑χ coupling.
- `PhiT` (paper's φtilde_i): complex scalar, colour triplet, Q=-1/3. Four-fermion-limit diquark + d‑χ coupling.
- `XV` (paper's X_{μ,i}): complex vector, colour triplet, Q=+2/3. Resonant/vector diquark + t‑χ coupling.

Charges were derived, not copied, from requiring every vertex neutral in electric charge, using the rule that `bar[CC[psi]]` carries charge +Q(psi) (opposite sign convention to a plain `psibar`, since C-conjugation flips the sign again).

Self-audit table (all new terms are dimension-4; no `1/Lambda` suppression appears anywhere in the paper's own Lagrangian, so the EFT-cutoff rule does not apply — this is the paper's UV-complete simplified Lagrangian, not an integrated-out contact term):

| term | fields | d | coupling | coupling dim | 1/Λ | Q sum | Y sum | SU(2) | SU(3) | new-U(1) | B/L | CC[] | frac/root check | HC partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LchiKin` | chibar,chi | 4 | Mchi | 1 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | n/a | self-conj. (Dirac kin term) |
| `Lphi0Kin` | phi0,phi0 | 4 | Mphi0 | 1 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | n/a | self-conjugate |
| `LVnpKin` | Vnp,Vnp | 4 | MVnp | 1 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | n/a | self-conjugate |
| `LPhiSKin` | PhiSbar,PhiS | 4 | MPhiS | 1 | n/a | 0 | 0 | singlet | 3⊗3bar | n/a | n/a | n/a | n/a | self-Herm. (bar·field) |
| `LPhiTKin` | PhiTbar,PhiT | 4 | MPhiT | 1 | n/a | 0 | 0 | singlet | 3⊗3bar | n/a | n/a | n/a | n/a | self-Herm. |
| `LXVKin` | XVbar,XV | 4 | MXV | 1 | n/a | 0 | 0 | singlet | 3⊗3bar | n/a | n/a | n/a | n/a | self-Herm. |
| `LFCS` | phi0,uqbar,uq | 4 | a0FC,b0FC | 0 | n/a | 0 | 0 | singlet (post-EWSB fields) | 3⊗3bar | n/a | n/a | n/a | n/a | self-Herm. (a0FC Hermitian, b0FC=0) |
| `LFCV` | Vnp,uqbar,uq | 4 | a1FC,b1FC | 0 | n/a | 0 | 0 | singlet | 3⊗3bar | n/a | n/a | n/a | n/a | self-Herm. |
| `LdiquarkPhiS` | PhiS,bar[CC[dq]],dq | 4 | aqSR,bqSR | 0 | n/a | 0 | 0 | singlet | Eps[3,3,3]→singlet | n/a | n/a | yes | n/a | in `HC[LNPSR]` |
| `LPhiSchi` | PhiS,uqbar,chi | 4 | a12SR,b12SR | 0 | n/a | 0 | 0 | singlet | 3⊗3bar | n/a | n/a | n/a | n/a | in `HC[LNPSR]` |
| `LdiquarkPhiT` | PhiT,bar[CC[dq]],uq | 4 | atildeqSR,btildeqSR | 0 | n/a | 0 | 0 | singlet | Eps[3,3,3]→singlet | n/a | n/a | yes | n/a | in `HC[LNPSR]` |
| `LPhiTchi` | PhiT,dqbar,chi | 4 | atilde12SR,btilde12SR | 0 | n/a | 0 | 0 | singlet | 3⊗3bar | n/a | n/a | n/a | n/a | in `HC[LNPSR]` |
| `LdiquarkXV` | XV,bar[CC[dq]],dq | 4 | aqVR,bqVR | 0 | n/a | 0 | 0 | singlet | Eps[3,3,3]→singlet | n/a | n/a | yes | n/a | in `HC[LNPSR]` |
| `LXVchi` | XV,uqbar,chi | 4 | a12VR,b12VR | 0 | n/a | 0 | 0 | singlet | 3⊗3bar | n/a | n/a | n/a | n/a | in `HC[LNPSR]` |

Extra required lines:
- Self-conjugate classes: `phi0`, `Vnp`. Both carry no `QuantumNumbers`.
- Name check: `phi0, Vnp, chi, PhiS, PhiT, XV` and every parameter/index name used (`Mphi0, MVnp, Mchi, MPhiS, MPhiT, MXV, a0FC, b0FC, a1FC, b1FC, aqSR, bqSR, a12SR, b12SR, atildeqSR, btildeqSR, atilde12SR, btilde12SR, aqVR, bqVR, a12VR, b12VR`) — none is a Mathematica/FeynRules built-in and none duplicates an SM.fr name.
- Single total: `LTotal` sums `LSM + LchiKin + Lphi0Kin + LVnpKin + LPhiSKin + LPhiTKin + LXVKin + LFCS + LFCV + LNPSR + LNPSRHC`.
- Reference/cached model file read: none. Only SM.fr (the required base file) and the paper's LaTeX source were used.

```mathematica
(* ****************************************************************** *)
(* FeynRules add-on model for arXiv:1106.6199, "Monotops at the LHC"  *)
(* Loaded on top of SM.fr.                                            *)
(* ****************************************************************** *)

M$ModelName = "Monotops_gen";

M$Information = {
  Authors      -> {"Automated extraction"},
  Version      -> "1.0",
  Date         -> "2026",
  Institutions -> {"n/a"},
  Emails       -> {"n/a"},
  URLs         -> "arXiv:1106.6199"
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
(* **** Particle classes **** *)
(* ************************** *)
M$ClassesDescription = {

  (* Neutral SM-singlet real scalar: FCNC missing-energy state (paper's plain phi) *)
  S[101] == {
    ClassName       -> phi0,
    SelfConjugate   -> True,
    Mass            -> {Mphi0, 300.},
    Width           -> 0,
    ParticleName    -> "phi0",
    PDG             -> 9000001,
    PropagatorLabel -> "phi0",
    PropagatorType  -> D,
    PropagatorArrow -> None,
    FullName        -> "Neutral flavour-changing scalar (missing energy)"
  },

  (* Colour-triplet complex scalar: resonant "S" state, Q = +2/3 *)
  S[102] == {
    ClassName       -> PhiS,
    SelfConjugate   -> False,
    Indices         -> {Index[Colour]},
    QuantumNumbers  -> {Y -> 2/3},
    Mass            -> {MPhiS, 500.},
    Width           -> 0,
    ParticleName    -> "phiS",
    AntiParticleName-> "phiSbar",
    PDG             -> 9000004,
    PropagatorLabel -> "PhiS",
    PropagatorType  -> D,
    PropagatorArrow -> None,
    FullName        -> "Colour-triplet scalar resonance S"
  },

  (* Colour-triplet complex scalar: four-fermion-limit mediator (paper's phi-tilde), Q = -1/3 *)
  S[103] == {
    ClassName       -> PhiT,
    SelfConjugate   -> False,
    Indices         -> {Index[Colour]},
    QuantumNumbers  -> {Y -> -1/3},
    Mass            -> {MPhiT, 3000.},
    Width           -> 0,
    ParticleName    -> "phiT",
    AntiParticleName-> "phiTbar",
    PDG             -> 9000005,
    PropagatorLabel -> "PhiT",
    PropagatorType  -> D,
    PropagatorArrow -> None,
    FullName        -> "Colour-triplet scalar (four-fermion mediator)"
  },

  (* Neutral SM-singlet real vector: FCNC missing-energy state (paper's V) *)
  V[101] == {
    ClassName       -> Vnp,
    SelfConjugate   -> True,
    Mass            -> {MVnp, 50.},
    Width           -> 0,
    ParticleName    -> "Vnp",
    PDG             -> 9000002,
    PropagatorLabel -> "Vnp",
    PropagatorType  -> Sine,
    PropagatorArrow -> None,
    FullName        -> "Neutral flavour-changing vector (missing energy)"
  },

  (* Colour-triplet complex vector: resonant "X" state, Q = +2/3 *)
  V[102] == {
    ClassName       -> XV,
    SelfConjugate   -> False,
    Indices         -> {Index[Colour]},
    QuantumNumbers  -> {Y -> 2/3},
    Mass            -> {MXV, 500.},
    Width           -> 0,
    ParticleName    -> "XV",
    AntiParticleName-> "XVbar",
    PDG             -> 9000006,
    PropagatorLabel -> "XV",
    PropagatorType  -> C,
    PropagatorArrow -> Forward,
    FullName        -> "Colour-triplet vector resonance X"
  },

  (* SM-singlet Dirac fermion: invisible state chi, Q = 0 *)
  F[101] == {
    ClassName        -> chi,
    SelfConjugate    -> False,
    Mass             -> {Mchi, 0.},
    Width            -> 0,
    ParticleName     -> "chi",
    AntiParticleName -> "chibar",
    PDG              -> 9000003,
    PropagatorLabel  -> "chi",
    PropagatorType   -> S,
    PropagatorArrow  -> Forward,
    FullName         -> "Invisible Dirac fermion"
  }
};

(* ************************** *)
(* *****   Parameters   ***** *)
(* ************************** *)
M$Parameters = {

  (* FCNC scalar phi0 couplings to up-type quarks: (a0FC)_13=(a0FC)_31=0.1, rest 0 *)
  a0FC == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    Value            -> {a0FC[1,3] -> 0.1, a0FC[3,1] -> 0.1},
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "phi0 scalar FCNC coupling to up-type quarks, Eq.(1)"
  },
  b0FC == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    Value            -> 0,
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "phi0 pseudoscalar FCNC coupling to up-type quarks, Eq.(1) (paper sets b=0)"
  },

  (* FCNC vector Vnp couplings to up-type quarks *)
  a1FC == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    Value            -> {a1FC[1,3] -> 0.1, a1FC[3,1] -> 0.1},
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "Vnp vector FCNC coupling to up-type quarks, Eq.(1)"
  },
  b1FC == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    Value            -> 0,
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "Vnp axial-vector FCNC coupling to up-type quarks, Eq.(1) (paper sets b=0)"
  },

  (* PhiS - down-down diquark: (aqSR)_12 = -(aqSR)_21 = 0.1 *)
  aqSR == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    Value            -> {aqSR[1,2] -> 0.1, aqSR[2,1] -> -0.1},
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "PhiS scalar diquark coupling to down-type quarks, Eq.(1)"
  },
  bqSR == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    Value            -> 0,
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "PhiS pseudoscalar diquark coupling to down-type quarks, Eq.(1) (paper sets b=0)"
  },

  (* PhiS - up quark - chi: (a12SR)_3 = 0.1 (top only) *)
  a12SR == {
    ParameterType    -> External,
    Indices          -> {Index[Generation]},
    Value            -> {a12SR[3] -> 0.1},
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "PhiS scalar coupling to up-type quark and chi, Eq.(1)"
  },
  b12SR == {
    ParameterType    -> External,
    Indices          -> {Index[Generation]},
    Value            -> 0,
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "PhiS pseudoscalar coupling to up-type quark and chi, Eq.(1) (paper sets b=0)"
  },

  (* PhiT - down-up diquark: (atildeqSR)_13 = (atildeqSR)_23 = 0.1 *)
  atildeqSR == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    Value            -> {atildeqSR[1,3] -> 0.1, atildeqSR[2,3] -> 0.1},
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "PhiT scalar diquark coupling to down- and up-type quarks, Eq.(1)"
  },
  btildeqSR == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    Value            -> 0,
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "PhiT pseudoscalar diquark coupling to down- and up-type quarks, Eq.(1) (paper sets b=0)"
  },

  (* PhiT - down quark - chi: (atilde12SR)_1 = (atilde12SR)_2 = 0.1 *)
  atilde12SR == {
    ParameterType    -> External,
    Indices          -> {Index[Generation]},
    Value            -> {atilde12SR[1] -> 0.1, atilde12SR[2] -> 0.1},
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "PhiT scalar coupling to down-type quark and chi, Eq.(1)"
  },
  btilde12SR == {
    ParameterType    -> External,
    Indices          -> {Index[Generation]},
    Value            -> 0,
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "PhiT pseudoscalar coupling to down-type quark and chi, Eq.(1) (paper sets b=0)"
  },

  (* XV - down-down diquark: (aqVR)_11 = 0.1 *)
  aqVR == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    Value            -> {aqVR[1,1] -> 0.1},
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "XV vector diquark coupling to down-type quarks, Eq.(1)"
  },
  bqVR == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    Value            -> 0,
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "XV axial-vector diquark coupling to down-type quarks, Eq.(1) (paper sets b=0)"
  },

  (* XV - up quark - chi: (a12VR)_3 = 0.1 (top only) *)
  a12VR == {
    ParameterType    -> External,
    Indices          -> {Index[Generation]},
    Value            -> {a12VR[3] -> 0.1},
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "XV vector coupling to up-type quark and chi, Eq.(1)"
  },
  b12VR == {
    ParameterType    -> External,
    Indices          -> {Index[Generation]},
    Value            -> 0,
    InteractionOrder -> {NP,1},
    BlockName        -> NPINPUTS,
    Description      -> "XV axial-vector coupling to up-type quark and chi, Eq.(1) (paper sets b=0)"
  }
};

(* ************************** *)
(* *****   Lagrangian   ***** *)
(* ************************** *)

(* Free kinetic + mass terms for every new field *)
LchiKin  := Block[{mu}, I chibar.Ga[mu].DC[chi,mu] - Mchi chibar.chi];

Lphi0Kin := Block[{mu}, 1/2 del[phi0,mu] del[phi0,mu] - 1/2 Mphi0^2 phi0^2];

LVnpKin  := Block[{mu,nu}, -1/4 FS[Vnp,mu,nu] FS[Vnp,mu,nu] + 1/2 MVnp^2 Vnp[mu] Vnp[mu]];

LPhiSKin := Block[{mu,cc}, DC[PhiSbar,mu][cc] DC[PhiS,mu][cc] - MPhiS^2 PhiSbar[cc] PhiS[cc]];

LPhiTKin := Block[{mu,cc}, DC[PhiTbar,mu][cc] DC[PhiT,mu][cc] - MPhiT^2 PhiTbar[cc] PhiT[cc]];

LXVKin   := Block[{mu,nu,cc}, -1/2 FS[XVbar,mu,nu][cc] FS[XV,mu,nu][cc] + MXV^2 XVbar[mu][cc] XV[mu][cc]];

(* FCNC couplings of phi0 and Vnp to up-type quarks, Eq.(1) line 2 (Hermitian by construction) *)
LFCS := Block[{ff1,ff2,cc},
  ExpandIndices[
    phi0 uqbar[ff1,cc].(a0FC[ff1,ff2] + b0FC[ff1,ff2] Ga[5]).uq[ff2,cc]
  ]
];

LFCV := Block[{ff1,ff2,cc,mu},
  ExpandIndices[
    Vnp[mu] uqbar[ff1,cc].Ga[mu].(a1FC[ff1,ff2] + b1FC[ff1,ff2] Ga[5]).uq[ff2,cc]
  ]
];

(* PhiS: dd diquark (baryon-number violating) and t-chi coupling, Eq.(1) line 3 *)
LdiquarkPhiS := Block[{c1,c2,c3,ff1,ff2},
  ExpandIndices[
    Eps[c1,c2,c3] PhiS[c1] bar[CC[dq]][ff1,c2].(aqSR[ff1,ff2] + bqSR[ff1,ff2] Ga[5]).dq[ff2,c3]
  ]
];

LPhiSchi := Block[{cc,ff},
  ExpandIndices[
    PhiS[cc] uqbar[ff,cc].(a12SR[ff] + b12SR[ff] Ga[5]).chi
  ]
];

(* PhiT: du diquark and d-chi coupling (four-fermion limit), Eq.(1) line 4 *)
LdiquarkPhiT := Block[{c1,c2,c3,ff1,ff2},
  ExpandIndices[
    Eps[c1,c2,c3] PhiT[c1] bar[CC[dq]][ff1,c2].(atildeqSR[ff1,ff2] + btildeqSR[ff1,ff2] Ga[5]).uq[ff2,c3]
  ]
];

LPhiTchi := Block[{cc,ff},
  ExpandIndices[
    PhiT[cc] dqbar[ff,cc].(atilde12SR[ff] + btilde12SR[ff] Ga[5]).chi
  ]
];

(* XV: dd diquark and t-chi coupling, Eq.(1) lines 5-6 *)
LdiquarkXV := Block[{c1,c2,c3,ff1,ff2,mu},
  ExpandIndices[
    Eps[c1,c2,c3] XV[mu,c1] bar[CC[dq]][ff1,c2].Ga[mu].(aqVR[ff1,ff2] + bqVR[ff1,ff2] Ga[5]).dq[ff2,c3]
  ]
];

LXVchi := Block[{cc,ff,mu},
  ExpandIndices[
    XV[mu,cc] uqbar[ff,cc].Ga[mu].(a12VR[ff] + b12VR[ff] Ga[5]).chi
  ]
];

(* PhiS/PhiT/XV terms are not separately Hermitian (complex, charged fields): add h.c., matching the
   "+ h.c." at the end of Eq.(1) *)
LNPSR   := LdiquarkPhiS + LPhiSchi + LdiquarkPhiT + LPhiTchi + LdiquarkXV + LXVchi;
LNPSRHC := HC[LNPSR];

(* Single total Lagrangian: SM (from SM.fr) + all new-physics pieces *)
LTotal := LSM + LchiKin + Lphi0Kin + LVnpKin + LPhiSKin + LPhiTKin + LXVKin +
          LFCS + LFCV + LNPSR + LNPSRHC;
```