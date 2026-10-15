Continuing straight into the physics extraction and file construction.

**Self-audit table**

| term | fields | dim d | coupling | coupling dim (4-d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | new-U(1)_X sum | L/B number | CC[] | fraction/root check | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpkin (kin+mass) | Zp,Zp | 4 / 2 | 1 / MZp² | 0 / 2 | n/a | 0 | n/a | singlet | singlet | 0 (Zp neutral under its own gauge group) | 0 | n/a | n/a | self-conj. |
| LphiXkin (kin+mass) | phiX,phiX | 4 / 2 | 1/2 / MphiX² | 0 / 2 | n/a | 0 | n/a | singlet | singlet | 0 (radial mode is X-neutral) | 0 | n/a | n/a | self-conj. |
| LphiXPot (quartic+portal) | phiX⁴; H†H·phiX² | 4 / 4 | lamPhiX / lamPortal | 0 / 0 | n/a | 0 | 0 | H†H is std. singlet | singlet | X(H) set to 0 here — Z–Z′/portal-induced X-breaking of H is neglected, matching the paper's stated small-λ′ decoupling of the H and Φ sectors | 0 | n/a | n/a | self-conj. (real) |
| LNRkin (Majorana kin+mass) | NR,NR | 4 / 3 | I/2 / MN | 0 / 1 | n/a | 0 | 0 (N_R is Y=0) | singlet | singlet | bare mass breaks X by 2xNR — this is the low-energy remnant of the gauge-invariant Yukawa Y_N Φ N̄_R^c N_R after ⟨Φ⟩=vΦX/√2 (X(Φ)=−2xNR cancels it); no explicit Φ vev field is carried here (see LNRYuk) | 2 (Majorana, breaks L by 2) | CC[] used | n/a | self-conj. |
| LZpFermion (gauge current) | Zp·f̄Γf for f=QL,uR,dR,LL,lR,NR | 4 | gX·x_f | 0 | n/a | 0 (minimal-coupling current, Noether-current construction) | n/a | doublets summed over both components (same X per multiplet, as in Table 2) | colour-singlet contraction on existing SM colour index | invariant by construction (minimal coupling to Noether current of U(1)_X with charges of Table 2) | 0 | ProjP inserted on NR term (Majorana vector current f̄γ^μf vanishes identically unless chirally projected) | n/a | self-conj. current |
| LNRYuk (Φ_X–N–N Yukawa) | phiX,NR,NR | 4 | yNMaj | 0 | n/a | 0 | 0 | singlet | singlet | written in unitary gauge for U(1)_X: the parent term Y_N Φ N̄_R^cN_R has X-sum 2xΦ+2(−xΦ)=0; the Goldstone that would restore manifest invariance term-by-term has been gauged away, standard unitary-gauge practice | 2 | CC[] used | n/a | self-conj. (real Yukawa × real scalar) |
| LNuDirac (Dirac seesaw Yukawa) | LL,NR,Phibar,Eps | 4 | yN | 0 | n/a | 0 (same Eps/Phibar contraction as SM's up-Yukawa) | −(−1/2)+(−1/2)+0=0 | Eps[ii,jj] contraction (Htilde-type, rule 4) | n/a | −xlL+xH(as tabulated, unflipped)+xNR = (½xH+xΦ)+(−½xH)+(−xΦ)=0 | 1 (broken by Majorana sector) | not needed (Dirac term) | resolved: paper's literal "H" in this term must be Htilde for both Y- and X-invariance (rule 5's flagged case); implemented via Phibar·Eps exactly as SM.fr's own uR Yukawa | HC[...] added |

Kinetic+mass confirmed present for every new class: Zp (LZpkin), phiX (LZpkin/LphiXkin split correctly — phiX in LphiXkin), NR (LNRkin). No non-fundamental colour representation is introduced (no `AddGaugeRepresentation` needed). SelfConjugate→True classes: Zp, phiX, NR — none carries `QuantumNumbers`. All new names (Zp, phiX, NR, N1, N2, N3, gX, xH, xPhi, xqL, xuR, xdR, xlL, xeR, xNR, MZp, WZp, MphiX, WphiX, MN, MN1, MN2, MN3, WN, WN1, WN2, WN3, yN, yNMaj, lamPhiX, lamPortal, NP) were checked against Mathematica/FeynRules built-ins and SM.fr's own names — no collisions. Single total Lagrangian: `LTotal = LZpkin + LphiXkin + LphiXPot + LNRkin + LZpFermion + LNRYuk + LNuDirac`. No reference or cached model file was read: none — extraction is from the paper text above only.

```mathematica
(* ======================================================================= *)
(*  GeneralU1_gen.fr -- minimal U(1)_X extension of the SM (arXiv:2104.10902) *)
(*  Loaded ON TOP of SM.fr. No M$GaugeGroups block (add-on rule).            *)
(*  No new colour or SU(2) index is introduced; Generation is reused for NR. *)
(* ======================================================================= *)

M$ModelName = "GeneralU1_gen";

M$Information = {
  Authors      -> {"GitNexus benchmark extraction"},
  Version      -> "1.0",
  Date         -> "2026",
  References   -> {"arXiv:2104.10902 (Das, Dev, Hosotani, Mandal)"}
};

(* ----------------------------------------------------------------------- *)
(* Interaction orders                                                       *)
(* ----------------------------------------------------------------------- *)
M$InteractionOrderHierarchy = {
  {QCD, 1},
  {QED, 2},
  {NP,  1}
};

(* No new IndexRange declarations: NR only carries the SM.fr Generation index. *)

(* ----------------------------------------------------------------------- *)
(* Parameters                                                               *)
(* ----------------------------------------------------------------------- *)
M$Parameters = {

  (* --- U(1)_X charge parameters (External; x_Phi fixed to 1 in the paper, Table 2) --- *)
  xH == {
    ParameterType -> External,
    Value         -> 1.,
    Description   -> "U(1)_X mixing angle parameter x_H (free), Table 2 of 2104.10902; benchmarks -2,-1,-0.5,0,0.5,1,2"
  },
  xPhi == {
    ParameterType -> External,
    Value         -> 1.,
    Description   -> "U(1)_X charge x_Phi of the SM-singlet scalar Phi_X; paper fixes x_Phi=1 WLOG"
  },

  (* --- New gauge coupling --- *)
  gX == {
    ParameterType    -> External,
    Value            -> 0.4,
    InteractionOrder -> {NP, 1},
    Description      -> "U(1)_X gauge coupling g', benchmark value used with M_Zp=7.5 TeV in Sec. II"
  },

  (* --- Dirac (seesaw) Yukawa matrix lL-H-NR, Eq. (LYk) 4th term --- *)
  yN == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    Value            -> {yN[1,1] -> 1.*^-6, yN[1,2] -> 0., yN[1,3] -> 0.,
                         yN[2,1] -> 0.,     yN[2,2] -> 1.*^-6, yN[2,3] -> 0.,
                         yN[3,1] -> 0.,     yN[3,2] -> 0.,     yN[3,3] -> 1.*^-6},
    InteractionOrder -> {NP, 1},
    Description      -> "Dirac neutrino Yukawa matrix (lLbar H NR), Eq. (LYk) 4th term; seesaw-suppressed default"
  },

  (* --- Majorana Yukawa Phi_X-NR-NR, Eq. (LYk) 5th term --- *)
  yNMaj == {
    ParameterType    -> External,
    Indices          -> {Index[Generation]},
    Value            -> {yNMaj[1] -> 0.1, yNMaj[2] -> 0.1, yNMaj[3] -> 0.1},
    InteractionOrder -> {NP, 1},
    Description      -> "Diagonal Majorana Yukawa Y_N^alpha of Phi_X to N_R, Eq. (LYk) 5th term"
  },

  (* --- Scalar potential couplings, unlabeled Higgs potential Eq. in Sec. II --- *)
  lamPhiX == {
    ParameterType    -> External,
    Value            -> 0.1,
    InteractionOrder -> {NP, 2},
    Description      -> "Phi_X self-quartic coupling lambda_Phi (Higgs potential Eq., Sec. II)"
  },
  lamPortal == {
    ParameterType    -> External,
    Value            -> 0.01,
    InteractionOrder -> {NP, 2},
    Description      -> "H-Phi_X portal coupling lambda' ; kept small per the paper's own small-lambda' decoupling assumption (Sec. II)"
  },

  (* --- Internal U(1)_X charge combinations, Table 2 of 2104.10902 (x_Phi normalization) --- *)
  xqL == { ParameterType -> Internal, Value -> (1/6) xH + (1/3) xPhi,   Description -> "U(1)_X charge of q_L doublet, Table 2" },
  xuR == { ParameterType -> Internal, Value -> (2/3) xH + (1/3) xPhi,   Description -> "U(1)_X charge of u_R, Table 2" },
  xdR == { ParameterType -> Internal, Value -> -(1/3) xH + (1/3) xPhi,  Description -> "U(1)_X charge of d_R, Table 2" },
  xlL == { ParameterType -> Internal, Value -> -(1/2) xH - xPhi,        Description -> "U(1)_X charge of l_L doublet, Table 2" },
  xeR == { ParameterType -> Internal, Value -> -xH - xPhi,              Description -> "U(1)_X charge of e_R, Table 2" },
  xNR == { ParameterType -> Internal, Value -> -xPhi,                   Description -> "U(1)_X charge of N_R, Table 2" }

  (* Note: Mass/Width entries below (MZp, WZp, MphiX, WphiX, MN/MN1-3, WN/WN1-3) are
     declared through M$ClassesDescription, FeynRules convention identical to SM.fr's
     own MZ, WZ, Me, etc. *)
};

(* ----------------------------------------------------------------------- *)
(* New particle classes (all indices n >= 100)                             *)
(* ----------------------------------------------------------------------- *)
M$ClassesDescription = {

  (* New neutral massive gauge boson Z' *)
  V[101] == {
    ClassName       -> Zp,
    SelfConjugate   -> True,
    Mass            -> {MZp, 7500.},
    Width           -> {WZp, 350.},
    ParticleName    -> "Zp",
    PDG             -> 9900032,
    PropagatorLabel -> "Zp",
    PropagatorType  -> Sine,
    PropagatorArrow -> None,
    FullName        -> "Zprime"
  },

  (* Physical U(1)_X-breaking real scalar (radial mode of Phi_X, unitary gauge) *)
  S[101] == {
    ClassName       -> phiX,
    SelfConjugate   -> True,
    Mass            -> {MphiX, 1000.},
    Width           -> {WphiX, 1.},
    ParticleName    -> "phiX",
    PDG             -> 9900025,
    PropagatorLabel -> "phiX",
    PropagatorType  -> D,
    PropagatorArrow -> None,
    FullName        -> "U(1)X-breaking scalar"
  },

  (* Three generations of right-handed (Majorana) neutrinos *)
  F[101] == {
    ClassName        -> NR,
    ClassMembers     -> {N1, N2, N3},
    Indices          -> {Index[Generation]},
    FlavorIndex      -> Generation,
    SelfConjugate    -> True,
    Mass             -> {MN, {MN1,8000.}, {MN2,8000.}, {MN3,8000.}},
    Width            -> {WN, {WN1,10.}, {WN2,10.}, {WN3,10.}},
    PropagatorLabel  -> {"NR","N1","N2","N3"},
    PropagatorType   -> S,
    PropagatorArrow  -> None,
    PDG              -> {9900012, 9900014, 9900016},
    ParticleName     -> {"N1","N2","N3"},
    FullName         -> {"Heavy Majorana neutrino 1","Heavy Majorana neutrino 2","Heavy Majorana neutrino 3"}
  }
};

(* ----------------------------------------------------------------------- *)
(* Lagrangian                                                               *)
(* ----------------------------------------------------------------------- *)

(* Z' free kinetic + mass term (real massive vector, gauge singlet) *)
LZpkin := Block[{mu,nu},
  -1/4 FS[Zp,mu,nu] FS[Zp,mu,nu] + 1/2 MZp^2 Zp[mu] Zp[mu]
];

(* Phi_X radial-mode free kinetic + mass term (real scalar) *)
LphiXkin := Block[{mu},
  1/2 del[phiX,mu] del[phiX,mu] - 1/2 MphiX^2 phiX^2
];

(* Scalar potential: self-quartic and H-Phi_X portal (Higgs potential Eq., Sec. II) *)
LphiXPot := Block[{ii},
  ExpandIndices[ -(lamPhiX/24) phiX^4 - (lamPortal/2) Phibar[ii] Phi[ii] phiX^2, FlavorExpand -> SU2D]
];

(* N_R free Majorana kinetic + mass term *)
LNRkin := Block[{mu,ff},
  ExpandIndices[ I/2 NRbar[ff].Ga[mu].del[NR[ff],mu] - 1/2 MN[ff] NRbar[ff].CC[NR[ff]], FlavorExpand -> {} ]
];

(* Z' minimal-coupling gauge current with all SM fermions and N_R, Eq. (Lag1) *)
LZpFermion := Block[{mu},
  ExpandIndices[
    -gX Zp[mu] (
      xqL QLbar.Ga[mu].QL + xuR uRbar.Ga[mu].uR + xdR dRbar.Ga[mu].dR +
      xlL LLbar.Ga[mu].LL + xeR lRbar.Ga[mu].lR + xNR NRbar.Ga[mu].ProjP.NR
    ), FlavorExpand -> {SU2W,SU2D}]
];

(* Phi_X - N_R - N_R Majorana Yukawa (unitary gauge for U(1)_X), Eq. (LYk) 5th term *)
LNRYuk := Block[{ff},
  ExpandIndices[ -1/2 yNMaj[ff] phiX NRbar[ff].CC[NR[ff]], FlavorExpand -> {}]
];

(* Dirac seesaw Yukawa l_L - H - N_R, Eq. (LYk) 4th term; Htilde via Phibar.Eps, cf. SM.fr uR Yukawa *)
LNuDirac := Block[{sp,ii,jj,ff1,ff2,yuk},
  yuk = ExpandIndices[
    -yN[ff1,ff2] LLbar[sp,ii,ff1].NR[sp,ff2] Phibar[jj] Eps[ii,jj],
    FlavorExpand -> SU2D];
  yuk + HC[yuk]
];

LTotal := LZpkin + LphiXkin + LphiXPot + LNRkin + LZpFermion + LNRYuk + LNuDirac;
```