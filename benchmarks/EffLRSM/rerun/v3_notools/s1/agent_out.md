```mathematica
(* ********************************************************************* *)
(* *****  FeynRules add-on model file                              ***** *)
(* *****  Effective Left-Right Symmetric Model (EffLRSM)           ***** *)
(* *****  Extracted from arXiv:1610.08985                          ***** *)
(* *****  (O. Mattelaer, M. Mitra, R. Ruiz)                        ***** *)
(* *****                                                           ***** *)
(* *****  Add-on file: load on top of SM.fr, e.g.                  ***** *)
(* *****     LoadModel["SM.fr", "EffLRSM_gen.fr"];                 ***** *)
(* *****                                                           ***** *)
(* *****  New states: WR+ / WR- , ZR , and three heavy Majorana    ***** *)
(* *****  neutrinos n1, n2, n3.  The LRSM scalar sector is not     ***** *)
(* *****  included (decoupled at 15-20 TeV, Sec. II C), and the    ***** *)
(* *****  non-Abelian WR/ZR self-couplings are not defined in the  ***** *)
(* *****  effective model.                                         ***** *)
(* ********************************************************************* *)

M$ModelName = "EffLRSM_gen";

M$Information = {
  Authors      -> {"Automated extraction from arXiv:1610.08985"},
  Version      -> "1.0",
  Date         -> "09. 09. 2026",
  Institutions -> {"Effective LRSM at NLO, arXiv:1610.08985"},
  Emails       -> {"n/a"},
  URLs         -> "http://feynrules.irmp.ucl.ac.be/wiki/EffLRSM"
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
(* *****    Indices     ***** *)
(* ************************** *)
(* No new index type is required.  The three heavy Majorana neutrinos    *)
(* use the index Generation, which is already declared in SM.fr.         *)

(* ************************** *)
(* **** Particle classes **** *)
(* ************************** *)

M$ClassesDescription = {

(* Right-handed charged gauge boson W_R^+ : complex vector, Q = +1 *)
  V[100] == {
    ClassName        -> WR,
    SelfConjugate    -> False,
    Mass             -> {MWR, 3000.},
    Width            -> {WWR, 84.3},
    QuantumNumbers   -> {Q -> 1},
    PDG              -> 9900024,
    ParticleName     -> "wr+",
    AntiParticleName -> "wr-",
    PropagatorLabel  -> "WR",
    PropagatorType   -> Sine,
    PropagatorArrow  -> Forward,
    FullName         -> "WR"
  },

(* Right-handed neutral gauge boson Z_R : real vector *)
  V[101] == {
    ClassName        -> ZR,
    SelfConjugate    -> True,
    Mass             -> {MZR, 5070.},
    Width            -> {WZR, 114.},
    PDG              -> 9900023,
    ParticleName     -> "zr",
    PropagatorLabel  -> "ZR",
    PropagatorType   -> Sine,
    PropagatorArrow  -> None,
    FullName         -> "ZR"
  },

(* Three heavy Majorana neutrinos, aligned with the RH chiral states *)
  F[100] == {
    ClassName        -> NR,
    ClassMembers     -> {n1, n2, n3},
    Indices          -> {Index[Generation]},
    FlavorIndex      -> Generation,
    SelfConjugate    -> True,
    Mass             -> {MN, {mn1, 173.3}, {mn2, 1.*^12}, {mn3, 1.*^12}},
    Width            -> {WN, {Wn1, 2.12*^-8}, {Wn2, 0}, {Wn3, 0}},
    PDG              -> {9900012, 9900014, 9900016},
    ParticleName     -> {"n1", "n2", "n3"},
    PropagatorLabel  -> {"NR", "n1", "n2", "n3"},
    PropagatorType   -> Straight,
    PropagatorArrow  -> None,
    FullName         -> {"HeavyN1", "HeavyN2", "HeavyN3"}
  }
};

(* ************************** *)
(* *****   Parameters   ***** *)
(* ************************** *)

M$Parameters = {

  (* ---------- External parameters ---------- *)

  kapRq == {
    ParameterType    -> External,
    BlockName        -> LRSMINPUTS,
    OrderBlock       -> 1,
    Value            -> 1.,
    InteractionOrder -> {NP, 1},
    TeX              -> Superscript[Subscript[\[Kappa], R], q],
    Description      -> "Normalisation of the RH gauge coupling to quarks, Eq.(4)"
  },

  kapRl == {
    ParameterType    -> External,
    BlockName        -> LRSMINPUTS,
    OrderBlock       -> 2,
    Value            -> 1.,
    InteractionOrder -> {NP, 1},
    TeX              -> Superscript[Subscript[\[Kappa], R], l],
    Description      -> "Normalisation of the RH gauge coupling to leptons, Eq.(5)"
  },

  (* ---------- Internal parameters ---------- *)

  tw2 == {
    ParameterType -> Internal,
    Value         -> sw^2/cw^2,
    Description   -> "tan^2(theta_W)"
  },

  nZRq == {
    ParameterType -> Internal,
    Value         -> Sqrt[1 - tw2/kapRq^2],
    Description   -> "sqrt(1-(1/kapRq)^2 tan^2thetaW): ZR quark coupling denominator, Eq.(7)"
  },

  nZRl == {
    ParameterType -> Internal,
    Value         -> Sqrt[1 - tw2/kapRl^2],
    Description   -> "sqrt(1-(1/kapRl)^2 tan^2thetaW): ZR lepton coupling denominator, Eq.(7)"
  },

  gLZRu == {
    ParameterType -> Internal,
    Value         -> -1/6 tw2/kapRq^2,
    Description   -> "(TL3-Q) tan^2thetaW/kapRq^2 for up-type quarks, Eq.(8)"
  },

  gRZRu == {
    ParameterType -> Internal,
    Value         -> 1/2 - 2/3 tw2/kapRq^2,
    Description   -> "TR3 - Q tan^2thetaW/kapRq^2 for up-type quarks, Eq.(9)"
  },

  gLZRd == {
    ParameterType -> Internal,
    Value         -> -1/6 tw2/kapRq^2,
    Description   -> "(TL3-Q) tan^2thetaW/kapRq^2 for down-type quarks, Eq.(8)"
  },

  gRZRd == {
    ParameterType -> Internal,
    Value         -> -1/2 + 1/3 tw2/kapRq^2,
    Description   -> "TR3 - Q tan^2thetaW/kapRq^2 for down-type quarks, Eq.(9)"
  },

  gLZRe == {
    ParameterType -> Internal,
    Value         -> 1/2 tw2/kapRl^2,
    Description   -> "(TL3-Q) tan^2thetaW/kapRl^2 for charged leptons, Eq.(8)"
  },

  gRZRe == {
    ParameterType -> Internal,
    Value         -> -1/2 + tw2/kapRl^2,
    Description   -> "TR3 - Q tan^2thetaW/kapRl^2 for charged leptons, Eq.(9)"
  },

  gLZRv == {
    ParameterType -> Internal,
    Value         -> 1/2 tw2/kapRl^2,
    Description   -> "(TL3-Q) tan^2thetaW/kapRl^2 for light neutrinos, Eq.(8); gR = 0"
  },

  gRZRn == {
    ParameterType -> Internal,
    Value         -> 1/2,
    Description   -> "TR3 of the RH (heavy Majorana) neutrinos, Eq.(9); gL = 0"
  },

  VCKMR == {
    ParameterType -> Internal,
    Indices       -> {Index[Generation], Index[Generation]},
    Unitary       -> True,
    Value         -> {VCKMR[1,1] -> 1, VCKMR[1,2] -> 0, VCKMR[1,3] -> 0,
                      VCKMR[2,1] -> 0, VCKMR[2,2] -> 1, VCKMR[2,3] -> 0,
                      VCKMR[3,1] -> 0, VCKMR[3,2] -> 0, VCKMR[3,3] -> 1},
    Description   -> "RH CKM matrix, diagonal with unit entries (diagonalCKM.rst)"
  },

  YN == {
    ParameterType -> Internal,
    Indices       -> {Index[Generation], Index[Generation]},
    Value         -> {YN[1,1] -> 1, YN[1,2] -> 0, YN[1,3] -> 0,
                      YN[2,1] -> 0, YN[2,2] -> 1, YN[2,3] -> 0,
                      YN[3,1] -> 0, YN[3,2] -> 0, YN[3,3] -> 1},
    Description   -> "Heavy neutrino mixing Y (first index = N, second = lepton), Eq.(17)"
  },

  XN == {
    ParameterType -> Internal,
    Indices       -> {Index[Generation], Index[Generation]},
    Value         -> {XN[1,1] -> 0, XN[1,2] -> 0, XN[1,3] -> 0,
                      XN[2,1] -> 0, XN[2,2] -> 0, XN[2,3] -> 0,
                      XN[3,1] -> 0, XN[3,2] -> 0, XN[3,3] -> 0},
    Description   -> "Light neutrino mixing X (first index = nu, second = lepton), set to zero, Eq.(17)"
  }
};

(* ************************** *)
(* *****   Lagrangian   ***** *)
(* ************************** *)

(* ----- Free field terms of the new states ----- *)

LWRkin := Block[{mu, nu},
  ExpandIndices[
    -1/2 FS[WRbar, mu, nu] FS[WR, mu, nu] + MWR^2 WRbar[mu] WR[mu] ]];

LZRkin := Block[{mu, nu},
  ExpandIndices[
    -1/4 FS[ZR, mu, nu] FS[ZR, mu, nu] + 1/2 MZR^2 ZR[mu] ZR[mu] ]];

LNkin := Block[{mu, sp, ff},
  ExpandIndices[
    I/2 NRbar.Ga[mu].del[NR, mu] - 1/2 MN[ff] NRbar[sp, ff].NR[sp, ff] ]];

(* ----- RH charged currents, Eqs.(4) and (5) ----- *)

LWRq := Block[{mu, tmp},
  tmp = ExpandIndices[
    -(kapRq gw/Sqrt[2]) uqbar.VCKMR.Ga[mu].ProjP.dq WR[mu] ];
  tmp + HC[tmp] ];

LWRl := Block[{mu, tmp},
  tmp = ExpandIndices[
    -(kapRl gw/Sqrt[2]) (
        NRbar.YN.Ga[mu].ProjP.l
      + CC[vlbar].XN.Ga[mu].ProjP.l ) WR[mu] ];
  tmp + HC[tmp] ];

(* ----- RH neutral currents, Eqs.(7)-(9) ----- *)

LZRq := Block[{mu},
  ExpandIndices[
    -(kapRq gw/nZRq) (
        gLZRu uqbar.Ga[mu].ProjM.uq + gRZRu uqbar.Ga[mu].ProjP.uq
      + gLZRd dqbar.Ga[mu].ProjM.dq + gRZRd dqbar.Ga[mu].ProjP.dq ) ZR[mu] ]];

LZRl := Block[{mu},
  ExpandIndices[
    -(kapRl gw/nZRl) (
        gLZRe lbar.Ga[mu].ProjM.l + gRZRe lbar.Ga[mu].ProjP.l
      + gLZRv vlbar.Ga[mu].ProjM.vl
      + gRZRn NRbar.Ga[mu].ProjP.NR ) ZR[mu] ]];

(* ----- Total Lagrangian ----- *)

LTotal := LSM + LWRkin + LZRkin + LNkin + LWRq + LWRl + LZRq + LZRl;
```