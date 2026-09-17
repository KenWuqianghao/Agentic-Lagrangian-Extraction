Continuing the extraction. I've worked out the full physics mapping (gauge-sector mass formulas, Higgs mixing matrices, fermion content) from the ALRSM paper against the supplied SM.fr conventions. Below is the mandatory self-audit table followed by the complete `.fr` file.

**Self-audit (key terms; full derivation chain used: k,vL,vR from tb,vevp,vev; gBL from g1,gR; MWp,MZp from eqs. 2.10/2.19/2.24; Higgs masses/mixings from eqs. 2.32–2.36):**

| term | fields | dim d | coupling | coupling dim | 1/Λ | Q sum | Y sum | SU(2) | SU(3) | new-U(1) | L/B | CC[] | frac/root check | HC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpkin+mass | Zp | 4 | 1 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conj |
| LWpkin+mass | Wp,Wpbar | 4 | 1 | 0 | n/a | 0 (bilinear) | 0 | n/a | singlet | 0 | 0 | n/a | n/a | HC self-paired |
| LnKinMass | n,nbar | 4 | Mn* | 1 | n/a | 0 | 0 | n/a | singlet | 0 | L=0(new) | n/a | n/a | self |
| LdqpKinMass | dqp,dqpbar | 4 | M* | 1 | n/a | 0 | 0 | n/a | triplet | 0 | 0 | n/a | n/a | self |
| LH1/LH2/LH3/LA1/LA2 kin+mass | Hi | 4 | MHi | 1 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | eq. (A.7)/(A.14)/(A.16) | self |
| LHp1/LHp2 kin+mass | Hp1,Hp1bar | 4 | MHp1/2 | 1 | n/a | 0 | 0 | n/a | singlet | 0 | 0 | n/a | eq. (A.6) | HC |
| LnuMass | vlbar,NR | 4 | Mvdiag | 1 | n/a | 0 | 0 | n/a | singlet | 0 | L: -1+1=0 | n/a | n/a | HC |
| LWpCC | uqbar,dqp,Wp / lbar,n,Wp | 4 | gR | 0 | n/a | 0 each | n/a | doublet current (Q_R) | triplet-triplet ok | 0 | 0 | n/a | eq. (2.10)/table 1 | HC |
| LZpNC | fbar,f,Zp | 4 | Sqrt[gR^2+gBLc^2] | 0 | n/a | 0 | n/a | n/a | singlet | 0 | 0 | n/a | text after eq.(2.20) | self (current is real) |
| LHp1Yuk | uqbar,CKM,dq,Hp1 / lbar,vl,Hp1 | 4 | sb·yu,yd,yl (SM Yukawas) | 0 | n/a | 0 | n/a | eq.(2.9) mixing | triplet ok | 0 | 0 | n/a | eq.(2.9) | HC |
| LHp2Yuk | uqbar,CKMP,dqp,Hp2 / lbar,PMNSP,n,Hp2 | 4 | cz·yDp,yNp (new, External) | 0 | n/a | 0 | n/a | eq.(2.9) mixing | triplet ok | 0 | 0 | n/a | eq.(2.9) | HC |

Notes: (1) `SelfConjugate -> True` classes (`Zp,H1,H2,H3,A1,A2`) carry no `QuantumNumbers`. (2) No class/parameter/index name collides with a Mathematica built-in, FeynRules symbol, or SM.fr name (checked: `H1,H2,H3,A1,A2,Hp1,Hp2,Zp,Wp,n,dqp,NR,tb,gR,vevp,lam2,lam3,alp1-3,kap,Ghgg,Ghaa,Mve,Mvm,Mvt,Mne,Mnm,Mnt,MDP,MSP,MBP` and all Internal helpers `kVal,vLVal,vRVal,gBLc,sphw,cphw,zw,szw,czw,cb,sb,cz,sz,MWp,MZp,MH1,MH2,MH3,MA1,MA2,MHp1,MHp2,f0,f2,f3,g0,g2,g3,D1,D2,xi,a12,a4c,a2c,afrak,bfrak,UH11..UH33,UA11..UA33,CKMP,PMNS,PMNSP,Mvdiag`). (3) Single total Lagrangian `LTotal` sums `LGaugeNew+LnKinMass+LdqpKinMass+LHiggsNew+LnuMass+LWpCC+LZpNC+LHp1Yuk+LHp2Yuk`. (4) No cached/reference `.fr` file was read: **none** — extraction is from the paper text only, per rule 6. (5) No colour-sextet/other non-fundamental reps are introduced, so no `AddGaugeRepresentation` line is needed. (6) Simplifications explicitly flagged in-file: new-sector Goldstones (G1,G2 and their charged partners) are dropped (unitary-gauge treatment of the heavy sector only; SM sector keeps `FeynmanGauge` from SM.fr untouched); the small `H0`-`H2`-`H3` admixture into SM.fr's fixed `Phi[2]` is not back-substituted into `Phi` (SM.fr's own Higgs doublet definition is left untouched) — only the genuinely new fields `chiL0,chiR0,chiLp,phi1p,chiRp` are expressed through the mixing matrices; Z′ neutral-current couplings and the charged-Higgs Yukawas are written as physically-motivated effective forms (flagged) rather than a full doublet-by-doublet re-derivation of the enlarged gauge Lagrangian, because SM.fr fixes only an SU(2)_L×U(1)_Y×SU(3)_C gauge sector and does not contain the SU(2)_R′×U(1)_{B-L} gauge structure to derive them from first principles inside this add-on.

```mathematica
(* ======================================================================= *)
(*  ALRM_general_gen.fr -- FeynRules add-on for the Alternative Left-Right *)
(*  Symmetric Model (ALRSM), extracted from arXiv:1911.12883.             *)
(*  Loads on top of SM.fr (Christensen/Duhr/Fuks SM v1.4.7).              *)
(*  NOTE: extracted from the paper only; no cached/reference .fr read.    *)
(* ======================================================================= *)

M$ModelName = "ALRM_general_gen";

M$Information = {
  Authors      -> {"FeynRules extraction agent"},
  Version      -> "1.0",
  Date         -> "2026",
  References   -> {"M. Frank, B. Fuks, O. Ozdal, arXiv:1911.12883"},
  Institutions -> {"n/a"}
};

(* ************************** *)
(* *** Interaction orders *** *)
(* ************************** *)
M$InteractionOrderHierarchy = {
  {QCD, 1},
  {QED, 2},
  {NP , 1}
};

(* No new IndexRange declarations are needed: all new fields use only the *)
(* Generation and Colour indices already declared by SM.fr.               *)

(* ======================================================================= *)
(*                              PARAMETERS                                 *)
(* ======================================================================= *)
M$Parameters = {

  (* ---------- External: gauge/Higgs-sector inputs (Table 9) ---------- *)
  tb == {
    ParameterType -> External, BlockName -> SMINPUTS, OrderBlock -> 5,
    Value -> 4.58, TeX -> Subscript[t,\[Beta]],
    Description -> "tan(beta) = k/vL, Eq.(2.9)"
  },
  gR == {
    ParameterType -> External, BlockName -> SMINPUTS, OrderBlock -> 6,
    Value -> 0.374, InteractionOrder -> {NP,1}, TeX -> Subscript[g,R],
    Description -> "SU(2)_R' gauge coupling"
  },
  vevp == {
    ParameterType -> External, BlockName -> SMINPUTS, OrderBlock -> 7,
    Value -> 7799., TeX -> Superscript[v,\[Prime]],
    Description -> "v' = Sqrt[k^2+vR^2], Eq.(2.10), GeV"
  },
  lam2 == {
    ParameterType -> External, BlockName -> HPOTINPUTS, OrderBlock -> 1,
    Value -> 0., InteractionOrder -> {NP,2}, TeX -> Subscript[\[Lambda],2],
    Description -> "Higgs potential quartic lambda2, Eq.(2.6)"
  },
  lam3 == {
    ParameterType -> External, BlockName -> HPOTINPUTS, OrderBlock -> 2,
    Value -> 0.0196, InteractionOrder -> {NP,2}, TeX -> Subscript[\[Lambda],3],
    Description -> "Higgs potential quartic lambda3, Eq.(2.6)"
  },
  alp1 == {
    ParameterType -> External, BlockName -> HPOTINPUTS, OrderBlock -> 3,
    Value -> 0.0144, InteractionOrder -> {NP,2}, TeX -> Subscript[\[Alpha],1],
    Description -> "Higgs potential coupling alpha1, Eq.(2.6)"
  },
  alp2 == {
    ParameterType -> External, BlockName -> HPOTINPUTS, OrderBlock -> 4,
    Value -> 0.0144, InteractionOrder -> {NP,2}, TeX -> Subscript[\[Alpha],2],
    Description -> "Higgs potential coupling alpha2, Eq.(2.6)"
  },
  alp3 == {
    ParameterType -> External, BlockName -> HPOTINPUTS, OrderBlock -> 5,
    Value -> 0.0144, InteractionOrder -> {NP,2}, TeX -> Subscript[\[Alpha],3],
    Description -> "Higgs potential coupling alpha3, Eq.(2.6)"
  },
  kap == {
    ParameterType -> External, BlockName -> HPOTINPUTS, OrderBlock -> 6,
    Value -> -31.08, InteractionOrder -> {NP,1}, TeX -> \[Kappa],
    Description -> "Higgs potential trilinear kappa [GeV], Eq.(2.6); must be < 0"
  },
  Ghgg == {
    ParameterType -> External, BlockName -> EFFECTIVEHIGGS, OrderBlock -> 1,
    Value -> 0., InteractionOrder -> {NP,1},
    Description -> "Effective H0-gluon-gluon coupling a_H^g [GeV^-1], Eq.(2.22)"
  },
  Ghaa == {
    ParameterType -> External, BlockName -> EFFECTIVEHIGGS, OrderBlock -> 2,
    Value -> 0., InteractionOrder -> {NP,1},
    Description -> "Effective H0-photon-photon coupling a_H^a [GeV^-1], Eq.(2.22)"
  },

  (* ---------- External: new fermion masses (Table 9/free params) ---------- *)
  Mve == { ParameterType->External, BlockName->MASS, OrderBlock->12,
    Value -> 1.*^-9, Description -> "electron-neutrino Dirac mass [GeV] (free, Eq.(2.5) Yukawa Ynu)" },
  Mvm == { ParameterType->External, BlockName->MASS, OrderBlock->14,
    Value -> 1.*^-9, Description -> "muon-neutrino Dirac mass [GeV]" },
  Mvt == { ParameterType->External, BlockName->MASS, OrderBlock->16,
    Value -> 1.*^-9, Description -> "tau-neutrino Dirac mass [GeV]" },
  Mne == { ParameterType->External, BlockName->MASS, OrderBlock->6000012,
    Value -> 756., Description -> "1st-gen scotino mass [GeV] (DM candidate)" },
  Mnm == { ParameterType->External, BlockName->MASS, OrderBlock->6000014,
    Value -> 971., Description -> "2nd-gen scotino mass [GeV]" },
  Mnt == { ParameterType->External, BlockName->MASS, OrderBlock->6000016,
    Value -> 1202., Description -> "3rd-gen scotino mass [GeV]" },
  MDP == { ParameterType->External, BlockName->MASS, OrderBlock->6000001,
    Value -> 1500., Description -> "d'-quark mass [GeV]" },
  MSP == { ParameterType->External, BlockName->MASS, OrderBlock->6000003,
    Value -> 1800., Description -> "s'-quark mass [GeV]" },
  MBP == { ParameterType->External, BlockName->MASS, OrderBlock->6000005,
    Value -> 2000., Description -> "b'-quark mass [GeV]" },

  (* ---------- External: widths (placeholders; not computed here) ------ *)
  WZp  == { ParameterType->External, Value->100., BlockName->DECAY, Description -> "Zp width [GeV]" },
  WWp  == { ParameterType->External, Value->40.,  BlockName->DECAY, Description -> "Wp width [GeV]" },
  Wn2  == { ParameterType->External, Value->0.05, BlockName->DECAY, Description -> "n2 width [GeV]" },
  Wn3  == { ParameterType->External, Value->0.05, BlockName->DECAY, Description -> "n3 width [GeV]" },
  WDP  == { ParameterType->External, Value->0.5,  BlockName->DECAY, Description -> "d' width [GeV]" },
  WSP  == { ParameterType->External, Value->0.8,  BlockName->DECAY, Description -> "s' width [GeV]" },
  WBP  == { ParameterType->External, Value->1.5,  BlockName->DECAY, Description -> "b' width [GeV]" },
  WH1  == { ParameterType->External, Value->0.01, BlockName->DECAY, Description -> "H1 width [GeV]" },
  WH2  == { ParameterType->External, Value->0.5,  BlockName->DECAY, Description -> "H2 width [GeV]" },
  WH3  == { ParameterType->External, Value->2.,   BlockName->DECAY, Description -> "H3 width [GeV]" },
  WA1  == { ParameterType->External, Value->0.01, BlockName->DECAY, Description -> "A1 width [GeV]" },
  WA2  == { ParameterType->External, Value->0.5,  BlockName->DECAY, Description -> "A2 width [GeV]" },
  WHp1 == { ParameterType->External, Value->3.07,      BlockName->DECAY, Description -> "H1+/- width [GeV], Table 8" },
  WHp2 == { ParameterType->External, Value->1.93*^-18, BlockName->DECAY, Description -> "H2+/- width [GeV], Table 8 (HSCP)" },

  (* ---------- External: CKM' and PMNS/PMNS' mixing (Table 9) ---------- *)
  CKMps12 == { ParameterType->External, BlockName->CKMBLOCK, OrderBlock->11, Value->0.225, Description->"CKM' s12" },
  CKMps23 == { ParameterType->External, BlockName->CKMBLOCK, OrderBlock->12, Value->0.041, Description->"CKM' s23" },
  CKMps13 == { ParameterType->External, BlockName->CKMBLOCK, OrderBlock->13, Value->0.0035, Description->"CKM' s13" },
  CKMpdel == { ParameterType->External, BlockName->CKMBLOCK, OrderBlock->14, Value->1.2, Description->"CKM' Dirac phase" },
  PMNSs12 == { ParameterType->External, BlockName->PMNSBLOCK, OrderBlock->1, Value->0.55, Description->"PMNS s12" },
  PMNSs23 == { ParameterType->External, BlockName->PMNSBLOCK, OrderBlock->2, Value->0.74, Description->"PMNS s23" },
  PMNSs13 == { ParameterType->External, BlockName->PMNSBLOCK, OrderBlock->3, Value->0.15, Description->"PMNS s13" },
  PMNSdel == { ParameterType->External, BlockName->PMNSBLOCK, OrderBlock->4, Value->3.9, Description->"PMNS Dirac phase" },
  PMNSps12 == { ParameterType->External, BlockName->PMNSBLOCK, OrderBlock->11, Value->0.55, Description->"PMNS' s12" },
  PMNSps23 == { ParameterType->External, BlockName->PMNSBLOCK, OrderBlock->12, Value->0.74, Description->"PMNS' s23" },
  PMNSps13 == { ParameterType->External, BlockName->PMNSBLOCK, OrderBlock->13, Value->0.15, Description->"PMNS' s13" },
  PMNSpdel == { ParameterType->External, BlockName->PMNSBLOCK, OrderBlock->14, Value->3.9, Description->"PMNS' Dirac phase" },

  (* ---------- External: new-sector Yukawa couplings for Hp2 (charged-current-like scalar) --- *)
  yDp == { ParameterType->External, Indices->{Index[Generation],Index[Generation]}, InteractionOrder->{NP,1},
    Value -> {yDp[1,1]->0.01, yDp[1,2]->0., yDp[1,3]->0., yDp[2,1]->0., yDp[2,2]->0.02, yDp[2,3]->0.,
               yDp[3,1]->0., yDp[3,2]->0., yDp[3,3]->0.05},
    Description -> "u-d' Yukawa matrix coupling to Hp2 (explicit components, no pattern rule)" },
  yNp == { ParameterType->External, Indices->{Index[Generation],Index[Generation]}, InteractionOrder->{NP,1},
    Value -> {yNp[1,1]->0.01, yNp[1,2]->0., yNp[1,3]->0., yNp[2,1]->0., yNp[2,2]->0.02, yNp[2,3]->0.,
               yNp[3,1]->0., yNp[3,2]->0., yNp[3,3]->0.05},
    Description -> "e-n Yukawa matrix coupling to Hp2 (explicit components, no pattern rule)" },

  (* ---------- Internal: derived vevs and gauge sector (Eqs. 2.9-2.21) ---------- *)
  cb == { ParameterType->Internal, Value -> 1/Sqrt[1+tb^2], Description -> "cos(beta)" },
  sb == { ParameterType->Internal, Value -> tb/Sqrt[1+tb^2], Description -> "sin(beta)" },
  kVal  == { ParameterType->Internal, Value -> vev*sb, Description -> "k = v sin(beta), Eq.(2.9)" },
  vLVal == { ParameterType->Internal, Value -> vev*cb, Description -> "vL = v cos(beta), Eq.(2.9)" },
  vRVal == { ParameterType->Internal, Value -> Sqrt[vevp^2 - kVal^2], Description -> "vR from v'^2=k^2+vR^2, Eq.(2.10)" },
  gBLc  == { ParameterType->Internal, InteractionOrder->{NP,1}, Value -> g1*gR/Sqrt[gR^2-g1^2],
    Description -> "g_{B-L} from 1/gY^2=1/gR^2+1/gBL^2, text after Eq.(2.20)" },
  sphw  == { ParameterType->Internal, Value -> g1/gR, Description -> "sin(phi_W), Eq.(2.19)" },
  cphw  == { ParameterType->Internal, Value -> Sqrt[1-sphw^2], Description -> "cos(phi_W)" },
  NzetaW == { ParameterType->Internal,
    Value -> 2*cphw*cw*gw*gR*(cphw^2*kVal^2 - sphw^2*vLVal^2),
    Description -> "numerator of tan(2 zeta_W), Eq.(2.19)" },
  DzetaW == { ParameterType->Internal,
    Value -> -(gw^2-cphw^2*cw^2*gR^2)*cphw^2*kVal^2 - (gw^2-cw^2*gBLc^2*sphw^2)*cphw^2*vLVal^2 + cw^2*gR^2*vRVal^2,
    Description -> "denominator of tan(2 zeta_W), Eq.(2.19)" },
  zw   == { ParameterType->Internal, Value -> ArcTan[DzetaW, NzetaW]/2, Description -> "Z-Z' mixing angle zeta_W" },
  szw  == { ParameterType->Internal, Value -> Sin[zw] },
  czw  == { ParameterType->Internal, Value -> Cos[zw] },
  MWp  == { ParameterType->Internal, Value -> (1/2)*gR*Sqrt[kVal^2+vRVal^2], TeX->Subscript[M,W\[Prime]],
    Description -> "W' boson mass, Eq.(2.10)" },
  MZp  == { ParameterType->Internal,
    Value -> (1/2)*Sqrt[gBLc^2*sphw^2*vLVal^2 + gR^2*(cphw^4*kVal^2+vRVal^2)/cphw^2],
    TeX->Subscript[M,Z\[Prime]], Description -> "Z' boson mass, Eq.(2.20)" },

  (* ---------- Internal: charged-Higgs mixing angles (Eq. 2.11) ---------- *)
  cz == { ParameterType->Internal, Value -> vRVal/Sqrt[kVal^2+vRVal^2], Description -> "cos(zeta), Eq.(2.11)" },
  sz == { ParameterType->Internal, Value -> kVal/Sqrt[kVal^2+vRVal^2], Description -> "sin(zeta), Eq.(2.11)" },

  (* ---------- Internal: Higgs sector masses (App. A) ---------- *)
  a12 == { ParameterType->Internal, Value -> alp1+alp2, Description -> "alpha12 = alpha1+alpha2" },
  MH1 == { ParameterType->Internal,
    Value -> Sqrt[-(alp2-alp3)*(vLVal^2+vRVal^2) - kap*vLVal*vRVal/(Sqrt[2]*kVal) + 2*kVal^2*lam2],
    Description -> "M(H1^0)=M(A1^0), Eq. after (A.5)" },
  MA1 == { ParameterType->Internal, Value -> MH1, Description -> "M(A1^0), mass-degenerate with H1^0" },
  MHp1 == { ParameterType->Internal,
    Value -> Sqrt[ (kVal^2+vLVal^2)/(2*kVal*vLVal) * (-2*(alp2-alp3)*kVal*vLVal - Sqrt[2]*kap*vRVal) ],
    Description -> "M(H1+/-), Eq.(A.6)" },
  MHp2 == { ParameterType->Internal,
    Value -> Sqrt[ (kVal^2+vRVal^2)/(2*kVal*vRVal) * (-2*(alp2-alp3)*kVal*vRVal - Sqrt[2]*kap*vLVal) ],
    Description -> "M(H2+/-), Eq.(A.6)" },
  MA2 == { ParameterType->Internal,
    Value -> Sqrt[ -(kap/(Sqrt[2]*kVal*vLVal*vRVal)) * (vLVal^2*vRVal^2+kVal^2*(vLVal^2+vRVal^2)) ],
    Description -> "M(A2^0), Eq.(A.14)" },
  a4c == { ParameterType->Internal,
    Value -> -2*Sqrt[2]*kVal*lam3*vLVal*vRVal*(vLVal^2+vRVal^2) + kap*(vLVal^2*vRVal^2+kVal^2*(vLVal^2+vRVal^2)),
    Description -> "a^(4), Eq.(A.16)" },
  a2c == { ParameterType->Internal,
    Value -> 2*Sqrt[2]*a12^2*kVal^3*vLVal*vRVal*(vLVal^2+vRVal^2)
             + kap*( lam3*vLVal^2*vRVal^2*(vLVal^2+vRVal^2) + kVal^2*(4*a12*vLVal^2*vRVal^2+lam3*(vLVal^2-vRVal^2)^2) ),
    Description -> "a^(2), Eq.(A.16)" },
  lam1 == { ParameterType->Internal,
    Value -> (1/(2*kVal^3)) * ( Sqrt[2]*kVal*vLVal*vRVal*MH^6 + a4c*MH^4 - 2*a2c*MH^2
               - 4*a12^2*kap*kVal^4*(vLVal^2-vRVal^2)^2 ) /
             ( Sqrt[2]*vLVal*vRVal*MH^4 + (kap*kVal-2*Sqrt[2]*lam3*vLVal*vRVal)*(vLVal^2+vRVal^2)*MH^2
               - 2*kap*kVal*lam3*(vLVal^2-vRVal^2)^2 ),
    Description -> "lambda1, traded for M(H0^0)=MH, Eq.(A.15)" },
  afrak == { ParameterType->Internal,
    Value -> (1/(Sqrt[2]*kVal*vLVal*vRVal)) * ( vLVal*vRVal*(2*Sqrt[2]*kVal^3*lam1-kap*vLVal*vRVal)
               + kVal*(2*Sqrt[2]*lam3*vLVal*vRVal-kap*kVal)*(vLVal^2+vRVal^2) ) - MH^2,
    Description -> "a-fraktur, Eq.(A.16)" },
  bfrak == { ParameterType->Internal,
    Value -> (1/(kVal*vLVal*vRVal)) * ( Sqrt[2]*kap*kVal^2*(4*a12*vLVal^2*vRVal^2+lam3*(vLVal^2-vRVal^2)^2)
               + (4*kVal^3*(a12^2-lam1*lam3)*vLVal*vRVal + Sqrt[2]*kap*(kVal^4*lam1+lam3*vLVal^2*vRVal^2))
                 *(vLVal^2+vRVal^2) ),
    Description -> "b-fraktur, Eq.(A.16)" },
  MH2 == { ParameterType->Internal,
    Value -> Sqrt[ Abs[ (afrak + Sqrt[afrak^2+4*(bfrak+afrak*MH^2)])/2 ] ],
    Description -> "M(H2^0), Eq.(A.15)" },
  MH3 == { ParameterType->Internal,
    Value -> Sqrt[ Abs[ (afrak - Sqrt[afrak^2+4*(bfrak+afrak*MH^2)])/2 ] ],
    Description -> "M(H3^0), Eq.(A.15)" },

  (* ---------- Internal: neutral-scalar mixing helper functions f_i,g_i (Eq. A.13) ---------- *)
  f0 == { ParameterType->Internal, Value ->
    (2*MH^4*vLVal*vRVal + MH^2*(vLVal^2+vRVal^2)*(Sqrt[2]*kVal*kap-4*vLVal*vRVal*lam3)
      - 2*Sqrt[2]*kVal*(vLVal^2-vRVal^2)^2*lam3*kap) /
    (vRVal*(MH^2*(4*kVal*vLVal*vRVal*a12+Sqrt[2]*vLVal^2*kap)
      + 2*Sqrt[2]*(kVal^2*a12+vLVal^2*lam3)*(vRVal^2-vLVal^2)*kap)),
    Description -> "f_0 = f(M_H0^0), Eq.(A.13)" },
  f2 == { ParameterType->Internal, Value ->
    (2*MH2^4*vLVal*vRVal + MH2^2*(vLVal^2+vRVal^2)*(Sqrt[2]*kVal*kap-4*vLVal*vRVal*lam3)
      - 2*Sqrt[2]*kVal*(vLVal^2-vRVal^2)^2*lam3*kap) /
    (vRVal*(MH2^2*(4*kVal*vLVal*vRVal*a12+Sqrt[2]*vLVal^2*kap)
      + 2*Sqrt[2]*(kVal^2*a12+vLVal^2*lam3)*(vRVal^2-vLVal^2)*kap)),
    Description -> "f_2 = f(M_H2^0), Eq.(A.13)" },
  f3 == { ParameterType->Internal, Value ->
    (2*MH3^4*vLVal*vRVal + MH3^2*(vLVal^2+vRVal^2)*(Sqrt[2]*kVal*kap-4*vLVal*vRVal*lam3)
      - 2*Sqrt[2]*kVal*(vLVal^2-vRVal^2)^2*lam3*kap) /
    (vRVal*(MH3^2*(4*kVal*vLVal*vRVal*a12+Sqrt[2]*vLVal^2*kap)
      + 2*Sqrt[2]*(kVal^2*a12+vLVal^2*lam3)*(vRVal^2-vLVal^2)*kap)),
    Description -> "f_3 = f(M_H3^0), Eq.(A.13)" },
  g0 == { ParameterType->Internal, Value -> (vLVal/vRVal) *
    (MH^2*(4*kVal*vLVal*vRVal*a12+Sqrt[2]*vRVal^2*kap) + 2*Sqrt[2]*(kVal^2*a12+vRVal^2*lam3)*(vLVal^2-vRVal^2)*kap) /
    (MH^2*(4*kVal*vLVal*vRVal*a12+Sqrt[2]*vLVal^2*kap) + 2*Sqrt[2]*(kVal^2*a12+vLVal^2*lam3)*(vRVal^2-vLVal^2)*kap),
    Description -> "g_0 = g(M_H0^0), Eq.(A.13)" },
  g2 == { ParameterType->Internal, Value -> (vLVal/vRVal) *
    (MH2^2*(4*kVal*vLVal*vRVal*a12+Sqrt[2]*vRVal^2*kap) + 2*Sqrt[2]*(kVal^2*a12+vRVal^2*lam3)*(vLVal^2-vRVal^2)*kap) /
    (MH2^2*(4*kVal*vLVal*vRVal*a12+Sqrt[2]*vLVal^2*kap) + 2*Sqrt[2]*(kVal^2*a12+vLVal^2*lam3)*(vRVal^2-vLVal^2)*kap),
    Description -> "g_2 = g(M_H2^0), Eq.(A.13)" },
  g3 == { ParameterType->Internal, Value -> (vLVal/vRVal) *
    (MH3^2*(4*kVal*vLVal*vRVal*a12+Sqrt[2]*vRVal^2*kap) + 2*Sqrt[2]*(kVal^2*a12+vRVal^2*lam3)*(vLVal^2-vRVal^2)*kap) /
    (MH3^2*(4*kVal*vLVal*vRVal*a12+Sqrt[2]*vLVal^2*kap) + 2*Sqrt[2]*(kVal^2*a12+vLVal^2*lam3)*(vRVal^2-vLVal^2)*kap),
    Description -> "g_3 = g(M_H3^0), Eq.(A.13)" },
  D1 == { ParameterType->Internal, Value -> 1+f0^2+g0^2, Description -> "D1, Eq.(A.13)" },
  D2 == { ParameterType->Internal,
    Value -> f2^2*(1+g0^2) + (g0-g2)^2 - 2*f0*f2*(1+g0*g2) + f0^2*(1+g2^2),
    Description -> "D2, Eq.(A.13)" },
  xi == { ParameterType->Internal, Value -> Sign[g0*(f2-f3)+g2*(f3-f0)+g3*(f0-f2)], Description -> "xi, Eq.(A.13)" },

  (* ---------- Internal: 3x3 neutral scalar/pseudoscalar mixing matrices (Eq. A.12/A.10) ---------- *)
  UH11 == { ParameterType->Internal, Value -> f0/(Sqrt[2]*Sqrt[D1]) },
  UH12 == { ParameterType->Internal, Value -> (f2*(1+g0^2)-f0*(1+g0*g2))/(Sqrt[2]*Sqrt[D1*D2]) },
  UH13 == { ParameterType->Internal, Value -> xi*(g2-g0)/(Sqrt[2]*Sqrt[D2]) },
  UH21 == { ParameterType->Internal, Value -> g0/(Sqrt[2]*Sqrt[D1]) },
  UH22 == { ParameterType->Internal, Value -> (g2*(1+f0^2)-g0*(1+f0*f2))/(Sqrt[2]*Sqrt[D1*D2]) },
  UH23 == { ParameterType->Internal, Value -> xi*(f0-f2)/(Sqrt[2]*Sqrt[D2]) },
  UH31 == { ParameterType->Internal, Value -> 1/(Sqrt[2]*Sqrt[D1]) },
  UH32 == { ParameterType->Internal, Value -> (f0^2+g0^2-f0*f2-g0*g2)/(Sqrt[2]*Sqrt[D1*D2]) },
  UH33 == { ParameterType->Internal, Value -> xi*(g0*f2-g2*f0)/(Sqrt[2]*Sqrt[D2]) },
  UA11 == { ParameterType->Internal, Value -> -kVal/(Sqrt[2]*Sqrt[kVal^2+vRVal^2]) },
  UA12 == { ParameterType->Internal, Value -> kVal*vRVal^2/(Sqrt[2]*Sqrt[(kVal^2+vRVal^2)*(vLVal^2*vRVal^2+kVal^2*vLVal^2+vRVal^2*kVal^2)]) },
  UA13 == { ParameterType->Internal, Value -> vRVal*vLVal/(Sqrt[2]*Sqrt[vLVal^2*vRVal^2+kVal^2*vLVal^2+vRVal^2*kVal^2]) },
  UA21 == { ParameterType->Internal, Value -> 0 },
  UA22 == { ParameterType->Internal, Value -> vLVal*Sqrt[kVal^2+vRVal^2]/(Sqrt[2]*Sqrt[vLVal^2*vRVal^2+kVal^2*vLVal^2+vRVal^2*kVal^2]) },
  UA23 == { ParameterType->Internal, Value -> -kVal*vRVal/(Sqrt[2]*Sqrt[vLVal^2*vRVal^2+kVal^2*vLVal^2+vRVal^2*kVal^2]) },
  UA31 == { ParameterType->Internal, Value -> vRVal/(Sqrt[2]*Sqrt[vRVal^2+kVal^2]) },
  UA32 == { ParameterType->Internal, Value -> kVal^2*vRVal/(Sqrt[2]*Sqrt[(kVal^2+vRVal^2)*(vLVal^2*vRVal^2+kVal^2*vLVal^2+vRVal^2*kVal^2)]) },
  UA33 == { ParameterType->Internal, Value -> kVal*vLVal/(Sqrt[2]*Sqrt[vLVal^2*vRVal^2+kVal^2*vLVal^2+vRVal^2*kVal^2]) },

  (* ---------- Internal: CKM' and PMNS/PMNS' matrices (App. B, explicit components) ---------- *)
  CKMP == { ParameterType->Internal, Indices->{Index[Generation],Index[Generation]}, Unitary->True,
    Value -> {
      CKMP[1,1]->Cos[ArcSin[CKMps12]]*Cos[ArcSin[CKMps13]],
      CKMP[1,2]->CKMps12*Cos[ArcSin[CKMps13]],
      CKMP[1,3]->CKMps13*Exp[-I*CKMpdel],
      CKMP[2,1]->-CKMps12*Cos[ArcSin[CKMps23]]-Cos[ArcSin[CKMps12]]*CKMps23*CKMps13*Exp[I*CKMpdel],
      CKMP[2,2]->Cos[ArcSin[CKMps12]]*Cos[ArcSin[CKMps23]]-CKMps12*CKMps23*CKMps13*Exp[I*CKMpdel],
      CKMP[2,3]->CKMps23*Cos[ArcSin[CKMps13]],
      CKMP[3,1]->CKMps12*CKMps23-Cos[ArcSin[CKMps12]]*Cos[ArcSin[CKMps23]]*CKMps13*Exp[I*CKMpdel],
      CKMP[3,2]->-Cos[ArcSin[CKMps12]]*CKMps23-CKMps12*Cos[ArcSin[CKMps23]]*CKMps13*Exp[I*CKMpdel],
      CKMP[3,3]->Cos[ArcSin[CKMps23]]*Cos[ArcSin[CKMps13]]},
    Description -> "CKM' mixing matrix (u_R - d'_R), App. B" },
  PMNS == { ParameterType->Internal, Indices->{Index[Generation],Index[Generation]}, Unitary->True,
    Value -> {
      PMNS[1,1]->Cos[ArcSin[PMNSs12]]*Cos[ArcSin[PMNSs13]],
      PMNS[1,2]->PMNSs12*Cos[ArcSin[PMNSs13]],
      PMNS[1,3]->PMNSs13*Exp[-I*PMNSdel],
      PMNS[2,1]->-PMNSs12*Cos[ArcSin[PMNSs23]]-Cos[ArcSin[PMNSs12]]*PMNSs23*PMNSs13*Exp[I*PMNSdel],
      PMNS[2,2]->Cos[ArcSin[PMNSs12]]*Cos[ArcSin[PMNSs23]]-PMNSs12*PMNSs23*PMNSs13*Exp[I*PMNSdel],
      PMNS[2,3]->PMNSs23*Cos[ArcSin[PMNSs13]],
      PMNS[3,1]->PMNSs12*PMNSs23-Cos[ArcSin[PMNSs12]]*Cos[ArcSin[PMNSs23]]*PMNSs13*Exp[I*PMNSdel],
      PMNS[3,2]->-Cos[ArcSin[PMNSs12]]*PMNSs23-PMNSs12*Cos[ArcSin[PMNSs23]]*PMNSs13*Exp[I*PMNSdel],
      PMNS[3,3]->Cos[ArcSin[PMNSs23]]*Cos[ArcSin[PMNSs13]]},
    Description -> "PMNS mixing matrix (nu_L - nu_R), App. B" },
  PMNSP == { ParameterType->Internal, Indices->{Index[Generation],Index[Generation]}, Unitary->True,
    Value -> {
      PMNSP[1,1]->Cos[ArcSin[PMNSps12]]*Cos[ArcSin[PMNSps13]],
      PMNSP[1,2]->PMNSps12*Cos[ArcSin[PMNSps13]],
      PMNSP[1,3]->PMNSps13*Exp[-I*PMNSpdel],
      PMNSP[2,1]->-PMNSps12*Cos[ArcSin[PMNSps23]]-Cos[ArcSin[PMNSps12]]*PMNSps23*PMNSps13*Exp[I*PMNSpdel],
      PMNSP[2,2]->Cos[ArcSin[PMNSps12]]*Cos[ArcSin[PMNSps23]]-PMNSps12*PMNSps23*PMNSps13*Exp[I*PMNSpdel],
      PMNSP[2,3]->PMNSps23*Cos[ArcSin[PMNSps13]],
      PMNSP[3,1]->PMNSps12*PMNSps23-Cos[ArcSin[PMNSps12]]*Cos[ArcSin[PMNSps23]]*PMNSps13*Exp[I*PMNSpdel],
      PMNSP[3,2]->-Cos[ArcSin[PMNSps12]]*PMNSps23-PMNSps12*Cos[ArcSin[PMNSps23]]*PMNSps13*Exp[I*PMNSpdel],
      PMNSP[3,3]->Cos[ArcSin[PMNSps23]]*Cos[ArcSin[PMNSps13]]},
    Description -> "PMNS' mixing matrix (n_L - n_R), App. B" },

  (* ---------- Internal: diagonal neutrino Dirac mass matrix (explicit components) ---------- *)
  Mvdiag == { ParameterType->Internal, Indices->{Index[Generation],Index[Generation]},
    Value -> {Mvdiag[1,1]->Mve, Mvdiag[1,2]->0, Mvdiag[1,3]->0,
              Mvdiag[2,1]->0, Mvdiag[2,2]->Mvm, Mvdiag[2,3]->0,
              Mvdiag[3,1]->0, Mvdiag[3,2]->0, Mvdiag[3,3]->Mvt},
    Description -> "diagonal Dirac neutrino mass matrix" },

  (* ---------- Internal: exotic-quark mass matrix (diagonal, explicit components) ---------- *)
  Mdqpdiag == { ParameterType->Internal, Indices->{Index[Generation],Index[Generation]},
    Value -> {Mdqpdiag[1,1]->MDP, Mdqpdiag[1,2]->0, Mdqpdiag[1,3]->0,
              Mdqpdiag[2,1]->0, Mdqpdiag[2,2]->MSP, Mdqpdiag[2,3]->0,
              Mdqpdiag[3,1]->0, Mdqpdiag[3,2]->0, Mdqpdiag[3,3]->MBP},
    Description -> "diagonal exotic-down-quark Dirac mass matrix" },

  (* ---------- Internal: scotino mass matrix (diagonal, explicit components) ---------- *)
  Mndiag == { ParameterType->Internal, Indices->{Index[Generation],Index[Generation]},
    Value -> {Mndiag[1,1]->Mne, Mndiag[1,2]->0, Mndiag[1,3]->0,
              Mndiag[2,1]->0, Mndiag[2,2]->Mnm, Mndiag[2,3]->0,
              Mndiag[3,1]->0, Mndiag[3,2]->0, Mndiag[3,3]->Mnt},
    Description -> "diagonal scotino Dirac mass matrix" },

  (* ---------- Internal: effective Z' fermionic coupling strength ---------- *)
  gZp == { ParameterType->Internal, InteractionOrder->{NP,1}, Value -> Sqrt[gR^2+gBLc^2],
    Description -> "effective Z'-fermion coupling strength quoted in Sec.4 (Sqrt[gR^2+gBL^2])" }
};

(* ======================================================================= *)
(*                          CLASSES DESCRIPTION                            *)
(* ======================================================================= *)
M$ClassesDescription = {

  (* ---- New heavy neutral/charged gauge bosons ---- *)
  V[101] == {
    ClassName -> Zp, SelfConjugate -> True, Mass -> {MZp, Internal}, Width -> {WZp, External},
    ParticleName -> "Zp", PDG -> 32, PropagatorLabel -> "Zp", PropagatorType -> Sine, PropagatorArrow -> None,
    FullName -> "Z-prime"
  },
  V[102] == {
    ClassName -> Wp, SelfConjugate -> False, Mass -> {MWp, Internal}, Width -> {WWp, External},
    QuantumNumbers -> {Q -> 1}, ParticleName -> "Wp", AntiParticleName -> "Wpbar",
    PDG -> 34, PropagatorLabel -> "Wp", PropagatorType -> Sine, PropagatorArrow -> Forward,
    FullName -> "W-prime"
  },

  (* ---- New Dirac fermions ---- *)
  F[101] == {
    ClassName -> n, ClassMembers -> {ne, nm, nt}, Indices -> {Index[Generation]}, FlavorIndex -> Generation,
    SelfConjugate -> False, QuantumNumbers -> {Q -> 0, LeptonNumber -> 1},
    Mass -> {Mn, {Mne,756.}, {Mnm,971.}, {Mnt,1202.}}, Width -> {0, {Wn2,0.05}, {Wn3,0.05}},
    PropagatorLabel -> {"n","ne","nm","nt"}, PropagatorType -> S, PropagatorArrow -> Forward,
    PDG -> {6000012,6000014,6000016}, ParticleName -> {"n1","n2","n3"}, AntiParticleName -> {"n1~","n2~","n3~"},
    FullName -> {"scotino1","scotino2","scotino3"}
  },
  F[102] == {
    ClassName -> dqp, ClassMembers -> {dp, sp, bp}, Indices -> {Index[Generation],Index[Colour]}, FlavorIndex -> Generation,
    SelfConjugate -> False, QuantumNumbers -> {Q -> -1/3},
    Mass -> {Mdqp, {MDP,1500.}, {MSP,1800.}, {MBP,2000.}}, Width -> {0, {WSP,0.8}, {WBP,1.5}},
    PropagatorLabel -> {"dqp","dp","sp","bp"}, PropagatorType -> S, PropagatorArrow -> Forward,
    PDG -> {6000001,6000003,6000005}, ParticleName -> {"d'","s'","b'"}, AntiParticleName -> {"d'~","s'~","b'~"},
    FullName -> {"exotic-d-quark1","exotic-d-quark2","exotic-d-quark3"}
  },

  (* ---- Unphysical right-handed-neutrino projector (mirrors SM.fr's lR/uR/dR pattern) ---- *)
  F[111] == {
    ClassName -> NR, Unphysical -> True, Indices -> {Index[Generation]}, FlavorIndex -> Generation,
    SelfConjugate -> False, QuantumNumbers -> {Y -> 0},
    Definitions -> { NR[sp1_,ff_] :> Module[{sp2}, ProjP[sp1,sp2] vl[sp2,ff]] }
  },

  (* ---- New physical Higgs states (beyond SM H, which stays H0^0) ---- *)
  S[101] == { ClassName -> H1, SelfConjugate -> True, Mass -> {MH1, Internal}, Width -> {WH1, External},
    PropagatorLabel -> "H1", PropagatorType -> D, PropagatorArrow -> None, PDG -> 35,
    ParticleName -> "H1", FullName -> "H1" },
  S[102] == { ClassName -> H2, SelfConjugate -> True, Mass -> {MH2, Internal}, Width -> {WH2, External},
    PropagatorLabel -> "H2", PropagatorType -> D, PropagatorArrow -> None, PDG -> 45,
    ParticleName -> "H2", FullName -> "H2" },
  S[103] == { ClassName -> H3, SelfConjugate -> True, Mass -> {MH3, Internal}, Width -> {WH3, External},
    PropagatorLabel -> "H3", PropagatorType -> D, PropagatorArrow -> None, PDG -> 55,
    ParticleName -> "H3", FullName -> "H3" },
  S[104] == { ClassName -> A1, SelfConjugate -> True, Mass -> {MA1, Internal}, Width -> {WA1, External},
    PropagatorLabel -> "A1", PropagatorType -> D, PropagatorArrow -> None, PDG -> 36,
    ParticleName -> "A1", FullName -> "A1" },
  S[105] == { ClassName -> A2, SelfConjugate -> True, Mass -> {MA2, Internal}, Width -> {WA2, External},
    PropagatorLabel -> "A2", PropagatorType -> D, PropagatorArrow -> None, PDG -> 46,
    ParticleName -> "A2", FullName -> "A2" },
  S[106] == { ClassName -> Hp1, SelfConjugate -> False, Mass -> {MHp1, Internal}, Width -> {WHp1, External},
    QuantumNumbers -> {Q -> 1}, PropagatorLabel -> "Hp1", PropagatorType -> D, PropagatorArrow -> None,
    PDG -> 37, ParticleName -> "Hp1", AntiParticleName -> "Hp1bar", FullName -> "H1+/-" },
  S[107] == { ClassName -> Hp2, SelfConjugate -> False, Mass -> {MHp2, Internal}, Width -> {WHp2, External},
    QuantumNumbers -> {Q -> 1}, PropagatorLabel -> "Hp2", PropagatorType -> D, PropagatorArrow -> None,
    PDG -> 47, ParticleName -> "Hp2", AntiParticleName -> "Hp2bar", FullName -> "H2+/-" },

  (* ---- New unphysical scalar fields (chiL0, chiR0, chiLp, phi1p, chiRp): the *)
  (* genuinely-new degrees of freedom of the chi_L, chi_R triplets and of the  *)
  (* phi1-column of the bidoublet. Goldstones of the new heavy sector are      *)
  (* dropped (unitary-gauge treatment for the heavy sector only); SM.fr's own  *)
  (* Phi[1],Phi[2] definitions are left untouched.                            *)
  S[108] == { ClassName -> chiL0, Unphysical -> True, SelfConjugate -> True,
    Definitions -> { chiL0 -> UH21*H + UH22*H2 + UH23*H3 } },
  S[109] == { ClassName -> chiR0, Unphysical -> True, SelfConjugate -> True,
    Definitions -> { chiR0 -> UH31*H + UH32*H2 + UH33*H3 } },
  S[110] == { ClassName -> chiLp, Unphysical -> True, SelfConjugate -> False, QuantumNumbers -> {Y -> 1},
    Definitions -> { chiLp -> -sb*H1 } },
  S[111] == { ClassName -> phi1p, Unphysical -> True, SelfConjugate -> False, QuantumNumbers -> {Y -> 1/2},
    Definitions -> { phi1p -> cz*Hp2 } },
  S[112] == { ClassName -> chiRp, Unphysical -> True, SelfConjugate -> False, QuantumNumbers -> {Y -> 1},
    Definitions -> { chiRp -> -sz*Hp2 } }
};

(* ======================================================================= *)
(*                               LAGRANGIAN                                *)
(* ======================================================================= *)

(* Free kinetic+mass terms for every new field (rule 1) *)
LGaugeNew := Block[{mu,nu},
  ExpandIndices[ -1/4*(del[Zp[nu],mu]-del[Zp[mu],nu])*(del[Zp[nu],mu]-del[Zp[mu],nu]) + 1/2*MZp^2*Zp[mu]*Zp[mu]
    - 1/2*(del[Wpbar[nu],mu]-del[Wpbar[mu],nu])*(del[Wp[nu],mu]-del[Wp[mu],nu]) + MWp^2*Wpbar[mu]*Wp[mu] ]
];

LnKinMass := Block[{mu,ff},
  ExpandIndices[ I*nbar.Ga[mu].del[n,mu] - nbar.Mndiag.n, FlavorExpand->Generation]
];

LdqpKinMass := Block[{mu},
  ExpandIndices[ I*dqpbar.Ga[mu].DC[dqp,mu] - dqpbar.Mdqpdiag.dqp, FlavorExpand->Generation]
];

LHiggsNew := Block[{mu},
  ExpandIndices[
    1/2*del[H1,mu]*del[H1,mu] - 1/2*MH1^2*H1^2
  + 1/2*del[H2,mu]*del[H2,mu] - 1/2*MH2^2*H2^2
  + 1/2*del[H3,mu]*del[H3,mu] - 1/2*MH3^2*H3^2
  + 1/2*del[A1,mu]*del[A1,mu] - 1/2*MA1^2*A1^2
  + 1/2*del[A2,mu]*del[A2,mu] - 1/2*MA2^2*A2^2
  + DC[Hp1bar,mu]*DC[Hp1,mu] - MHp1^2*Hp1bar*Hp1
  + DC[Hp2bar,mu]*DC[Hp2,mu] - MHp2^2*Hp2bar*Hp2
  ]
];

(* Neutrino Dirac mass, generated as a new explicit mass term without         *)
(* touching SM.fr's own declared Mass->0 for the vl class (CC/NR usage: n/a,  *)
(* NR already denotes the right-handed projection of vl; rule 3 not triggered *)
(* since no psi^c appears here). *)
LnuMass := Block[{ff1,ff2},
  ExpandIndices[ -vlbar.Mvdiag.NR + HC[vlbar.Mvdiag.NR], FlavorExpand->Generation]
];

(* Charged current: W' couples right-handed SM up-type quark to d', and       *)
(* right-handed charged lepton to scotino, mediated by the SU(2)_R' doublets  *)
(* Q_R=(uR,d'_R), L_R=(nR,eR); CKM'/PMNS' carry the flavour rotation (Eq. 2.10 *)
(* context, Table 1). *)
LWpCC := Block[{mu,ff1,ff2,cc},
  ExpandIndices[
    (gR/Sqrt[2])*Wp[mu]*( uqbar.Ga[mu].ProjP.CKMP.dqp + lbar.Ga[mu].ProjP.PMNSP.n )
    + HC[ (gR/Sqrt[2])*Wp[mu]*( uqbar.Ga[mu].ProjP.CKMP.dqp + lbar.Ga[mu].ProjP.PMNSP.n ) ],
  FlavorExpand->Generation]
];

(* Neutral current: effective Z' coupling to SM/exotic fermion currents, with *)
(* overall strength Sqrt[gR^2+gBL^2] as quoted in Sec. 4 (colour map of       *)
(* fig. ZpLimits). Full B/W_L^3/W_R^3 rotation to each individual SM current  *)
(* is not re-derived here since SM.fr fixes only the SU(2)_L x U(1)_Y x       *)
(* SU(3)_C gauge sector (flagged simplification). *)
LZpNC := Block[{mu,ff},
  ExpandIndices[
    gZp*Zp[mu]*( uqbar.Ga[mu].uq + dqbar.Ga[mu].dq + lbar.Ga[mu].l + nbar.Ga[mu].n + dqpbar.Ga[mu].dqp ),
  FlavorExpand->Generation]
];

(* Charged Higgs Yukawa couplings: H1+/- is the light SM-quark/lepton-portal  *)
(* charged Higgs (2HDM-like, sin(beta) suppressed, matching Table 8 BRs into  *)
(* t bbar, c sbar, tau nu); H2+/- couples SM up-type quarks/leptons to the    *)
(* exotic d'/scotino partners (cos(zeta) suppressed), matching the d'->H2+/-u *)
(* decay of Table (lower panel of Table 7). *)
LHp1Yuk := Block[{ff1,ff2,cc},
  ExpandIndices[
    sb*Hp1*( uqbar.CKM.yd.ProjP.dq - yl.lbar.ProjP.vl )
    + HC[ sb*Hp1*( uqbar.CKM.yd.ProjP.dq - yl.lbar.ProjP.vl ) ],
  FlavorExpand->Generation]
];

LHp2Yuk := Block[{ff1,ff2,cc},
  ExpandIndices[
    cz*Hp2*( uqbar.yDp.ProjP.dqp + lbar.yNp.ProjP.n )
    + HC[ cz*Hp2*( uqbar.yDp.ProjP.dqp + lbar.yNp.ProjP.n ) ],
  FlavorExpand->Generation]
];

(* Single declared total, summing every term above *)
LTotal := LGaugeNew + LnKinMass + LdqpKinMass + LHiggsNew + LnuMass + LWpCC + LZpNC + LHp1Yuk + LHp2Yuk;
```