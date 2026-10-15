## Mandatory self-audit table

Charge notation used below (re-derived, see notes after the table):
`xqL = xH/6 + xPhi/3`, `xuR = 2xH/3 + xPhi/3`, `xdR = -xH/3 + xPhi/3`, `xlL = -xH/2 - xPhi`, `xeR = -xH - xPhi`, `xnR = -xPhi`, `xHd = xH/2` (SM.fr `Phi`), `xSc = 2 xPhi` (singlet).

| term | fields in monomial | d | coupling | coup. dim (4-d) | 1/Lam power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | U(1)_X sum | L/B sum | CC[] used | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpKin (a) | FS[Zp]FS[Zp] | 4 | -1/4 | 0 | n/a | 0 | 0 | singlet | singlet | 0 (Zp is the X gauge field) | 0 | n/a | n/a | self-conjugate (real field) |
| LZpKin (b) | Zp Zp | 2 | MZp^2/2 | 2 | n/a | 0 | 0 | singlet | singlet | 0 (from broken \|D Phi\|^2 + \|D H\|^2) | 0 | n/a | LaTeX line `M_{Z'} = g' \sqrt{4 v_\Phi^2 + \frac{1}{4}x_H^2 v^2}` (root taken literally) | self-conjugate |
| LZpF (1) | Zp QLbar QL | 4 | gX xqL | 0 | n/a | 0 | -1/6+1/6=0 | shared SU2D index | 3bar x 3 = 1 | -xqL+xqL=0 | B: -1/3+1/3=0 | n/a | Table I formula, re-derived | self-Hermitian vector current |
| LZpF (2) | Zp uRbar uR | 4 | gX xuR | 0 | n/a | 0 | -2/3+2/3=0 | singlet | 3bar x 3 = 1 | 0 | B 0 | n/a | Table I | self-Hermitian |
| LZpF (3) | Zp dRbar dR | 4 | gX xdR | 0 | n/a | 0 | 1/3-1/3=0 | singlet | 3bar x 3 = 1 | 0 | B 0 | n/a | Table I | self-Hermitian |
| LZpF (4) | Zp LLbar LL | 4 | gX xlL | 0 | n/a | 0 | 1/2-1/2=0 | shared SU2D index | singlet | 0 | L 0 | n/a | Table I | self-Hermitian |
| LZpF (5) | Zp lRbar lR | 4 | gX xeR | 0 | n/a | 0 | 1-1=0 | singlet | singlet | 0 | L 0 | n/a | Table I | self-Hermitian |
| LZpF (6) | Zp NRbar NR | 4 | gX xnR | 0 | n/a | 0 | 0 | singlet | singlet | 0 | L 0 | no (chiral projector on a Majorana class) | Table I | self-Hermitian |
| LNXKin (a) | NXbar Ga del NX | 4 | I/2 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | n/a | Majorana class, no bare-field reuse | n/a | self-conjugate |
| LNXKin (b) | NXbar NX | 3 | mNmaj (=-1/2 M) | 1 | n/a | 0 | 0 | singlet | singlet | parent `Phi Nbar^c N`: 2xPhi-xPhi-xPhi=0 | L broken by 2 (seesaw, intended) | Majorana mass eigenstate replaces psi^c | LaTeX `m_{N_\alpha}=\frac{Y^\alpha_N}{\sqrt 2} v_\Phi` (division by root 2) | self-conjugate, -1/2 M NXbar.NX |
| LNYuk | HX NXbar NX | 4 | yN/(2 Sqrt[2]) | 0 | n/a | 0 | 0 | singlet | singlet | parent: 2xPhi-xPhi-xPhi=0 | L broken by 2 (intended) | Majorana class | same LaTeX line as above | self-conjugate (real yN) |
| LNuYuk | LLbar NR Phibar Eps | 4 | ynu | 0 | n/a | 0 (both SU2D components) | 1/2+0-1/2=0 | Eps[ii,jj]: LLbar[ii] with Phibar[jj] | singlet | (xH/2+xPhi)-xPhi-xH/2=0 | L: -1+1=0 | no (Dirac term) | Eq.(LYk) 4th term | HC[yuk] |
| LHXKin (a) | del HX del HX | 4 | 1/2 | 0 | n/a | 0 | 0 | singlet | singlet | 0 (radial mode) | 0 | n/a | n/a | self-conjugate |
| LHXKin (b) | HX HX | 2 | MHX^2/2 | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | MHX^2 = 2 lamX vX^2 from V (same form as SM `lam = MH^2/(2 vev^2)`) | self-conjugate |
| LZpHX (a) | Zp Zp HX | 3 | gX^2 xSc^2 vX | 1 | n/a | 0 | 0 | singlet | singlet | parent \|D Phi\|^2 invariant | 0 | n/a | M_Z' root line | self-conjugate |
| LZpHX (b) | Zp Zp HX HX | 4 | gX^2 xSc^2/2 | 0 | n/a | 0 | 0 | singlet | singlet | parent invariant | 0 | n/a | M_Z' root line | self-conjugate |
| LPotX (a) | HX HX HX | 3 | lamX vX | 1 | n/a | 0 | 0 | singlet | singlet | parent (Phi^+Phi)^2 invariant | 0 | n/a | V of Sec. II | self-conjugate |
| LPotX (b) | HX HX HX HX | 4 | lamX/4 | 0 | n/a | 0 | 0 | singlet | singlet | parent invariant | 0 | n/a | V of Sec. II | self-conjugate |
| LPotX (c) | HX HX Phibar Phi | 4 | lamHX/2 | 0 | n/a | 0 | 0+0-1/2+1/2=0 | shared SU2D index | singlet | parent (H^+H)(Phi^+Phi) invariant | 0 | n/a | V of Sec. II | self-conjugate |

Per-class rows (kinetic + mass present and summed in the total):

| class | free-field term | in LTotal |
|---|---|---|
| V[100] Zp (real vector) | LZpKin | yes |
| S[100] HX (real scalar) | LHXKin | yes |
| F[100] NX1,NX2,NX3 (Majorana) | LNXKin | yes |
| F[110] NR (Unphysical) | none needed; it is `ProjP` acting on NX | n/a |

Colour representations: no field carries a colour index other than the SM `Colour`/`Gluon`. No `AddGaugeRepresentation` line is needed.

SelfConjugate -> True classes: `Zp`, `HX`, `NX`. None of them carries `QuantumNumbers`. The chiral charge and the lepton number sit on the Unphysical class `NR`.

Names used: classes `Zp`, `HX`, `NX` (`NX1`,`NX2`,`NX3`), `NR`; parameters `gX`, `xH`, `xPhi`, `vX`, `lamX`, `lamHX`, `ynu`, `yN`, `mNmaj`, `MZp`, `WZp`, `MHX`, `WHX`, `MNX`, `MNX1..3`, `WNX`, `WNX1..3`, `xqL`, `xuR`, `xdR`, `xlL`, `xeR`, `xnR`, `xHd`, `xSc`; no new index. None is a Mathematica built-in, a FeynRules symbol, or an SM.fr name.

Total Lagrangian: one total, `LTotal := LSM + LZpKin + LZpF + LNXKin + LHXKin + LZpHX + LNYuk + LNuYuk + LPotX`. Every term above appears once.

Reference or cached model file read: none. Only the paper and SM.fr in this message were used.

Charge sign choice (required report): SM.fr gives `Phi` hypercharge +1/2 and puts the VEV in `Phi[2]`. The paper puts the VEV in the upper component and writes `qLbar H uR`, so the paper's `H` has Y = -1/2. Therefore SM.fr's `Phi` is the paper's `Htilde`, and its U(1)_X charge is `+xH/2`, the opposite sign of the `-xH/2` in Table I. All other charges follow from `X = xH * Y(SM.fr) + xPhi * (B-L)` and then reproduce Table I exactly. With this rule the three SM Yukawas of SM.fr and the new Dirac Yukawa are all X invariant (rows above). Note: the Table II entry for `q_L` at `x_H = 2` reads 1/3 in the paper, but the formula gives 2/3; the file uses the formula, not the table entry.

Approximations kept from the paper: Z-Z' mixing is not diagonalised, because the paper treats Z' as a mass eigenstate with the couplings of Eq.(Lag1) and uses `M_Z' ~ 2 g' v_Phi`; so no doublet-Z' operator and no mixing angle are written. The scalar portal keeps only the `HX^2 (H^+H)` piece, because the paper works in the small-`lambda'` limit where h-phi mixing is negligible.

```mathematica
(* ****************************************************************************** *)
(* ***  Minimal general U(1)_X extension of the Standard Model                *** *)
(* ***  FeynRules add-on file. Load it on top of SM.fr.                       *** *)
(* ***  Physics source: A. Das, P. S. B. Dev, Y. Hosotani, S. Mandal,         *** *)
(* ***  "Probing the minimal U(1)_X model at future electron-positron         *** *)
(* ***   colliders via fermion pair-production channels", arXiv:2104.10902.   *** *)
(* ***                                                                        *** *)
(* ***  New states: one real vector Zp (U(1)_X gauge boson), one real scalar  *** *)
(* ***  HX (radial mode of the SM-singlet scalar Phi_X), three Majorana       *** *)
(* ***  right-handed neutrinos NX1, NX2, NX3.                                 *** *)
(* ***                                                                        *** *)
(* ***  Charge convention: X = xH * Y(SM.fr) + xPhi * (B-L).                  *** *)
(* ***  SM.fr uses Y(Phi) = +1/2 with the VEV in Phi[2], so SM.fr's Phi is    *** *)
(* ***  the paper's Htilde and carries X = +xH/2 (Table I lists -xH/2 for H). *** *)
(* ****************************************************************************** *)

M$ModelName = "GeneralU1_gen";

M$Information = {
  Authors      -> {"Automated extraction from arXiv:2104.10902"},
  Institutions -> {"n/a"},
  Emails       -> {"n/a"},
  Date         -> "2026-09-09",
  Version      -> "1.0",
  References   -> {"A. Das, P. S. B. Dev, Y. Hosotani, S. Mandal, arXiv:2104.10902"},
  URLs         -> {"https://arxiv.org/abs/2104.10902"}
};

(* ************************** *)
(* *** Interaction orders *** *)
(* ************************** *)

M$InteractionOrderHierarchy = { {QCD, 1}, {QED, 2}, {NP, 1} };

(* ************************** *)
(* *****    Indices     ***** *)
(* ************************** *)
(* No new index is needed. The three right-handed neutrinos use the Generation *)
(* index of SM.fr. Colour, Gluon, SU2D and SU2W also come from SM.fr.          *)

(* ************************** *)
(* *****   Parameters   ***** *)
(* ************************** *)

M$Parameters = {

(* ----- External parameters ----- *)

  gX == {
    ParameterType    -> External,
    BlockName        -> U1XINPUTS,
    OrderBlock       -> 1,
    Value            -> 0.4,
    InteractionOrder -> {NP, 1},
    TeX              -> Subscript[g, X],
    Description      -> "U(1)X gauge coupling g-prime, Eq.(Lag1); benchmark 0.4 for MZp = 7.5 TeV"
  },

  xH == {
    ParameterType -> External,
    BlockName     -> U1XINPUTS,
    OrderBlock    -> 2,
    Value         -> 2.,
    TeX           -> Subscript[x, H],
    Description   -> "U(1)X charge parameter x_H (Table I). x_H = 0 is B-L, x_H = -2 is U(1)_R"
  },

  xPhi == {
    ParameterType -> External,
    BlockName     -> U1XINPUTS,
    OrderBlock    -> 3,
    Value         -> 1.,
    TeX           -> Subscript[x, \[CapitalPhi]],
    Description   -> "U(1)X charge parameter x_Phi (Table I). The paper fixes x_Phi = 1"
  },

  vX == {
    ParameterType    -> External,
    BlockName        -> U1XINPUTS,
    OrderBlock       -> 4,
    Value            -> 9375.,
    InteractionOrder -> {NP, -1},
    TeX              -> Subscript[v, \[CapitalPhi]],
    Description      -> "U(1)X breaking VEV v_Phi [GeV], free parameter; 9375 GeV gives MZp = 7.5 TeV for gX = 0.4"
  },

  lamX == {
    ParameterType    -> External,
    BlockName        -> U1XINPUTS,
    OrderBlock       -> 5,
    Value            -> 0.1,
    InteractionOrder -> {NP, 2},
    TeX              -> Subscript[\[Lambda], \[CapitalPhi]],
    Description      -> "Quartic coupling lambda_Phi of the singlet scalar, Higgs potential of Sec. II"
  },

  lamHX == {
    ParameterType    -> External,
    BlockName        -> U1XINPUTS,
    OrderBlock       -> 6,
    Value            -> 0.01,
    InteractionOrder -> {NP, 2},
    TeX              -> Superscript[\[Lambda], \[Prime]],
    Description      -> "Higgs portal coupling lambda-prime, (H^+H)(Phi^+Phi); the paper keeps it small"
  },

  ynu == {
    ParameterType    -> External,
    BlockName        -> YUKNU,
    Indices          -> {Index[Generation], Index[Generation]},
    InteractionOrder -> {NP, 1},
    Value            -> {ynu[1,1] -> 1.*^-6, ynu[1,2] -> 0.,      ynu[1,3] -> 0.,
                         ynu[2,1] -> 0.,     ynu[2,2] -> 1.*^-6,  ynu[2,3] -> 0.,
                         ynu[3,1] -> 0.,     ynu[3,2] -> 0.,      ynu[3,3] -> 1.*^-6},
    TeX              -> Subscript[Y, \[Nu]],
    Description      -> "Dirac neutrino Yukawa Y_nu, 4th term of Eq.(LYk); m_D = Y_nu v / Sqrt[2]"
  },

(* ----- Internal parameters: U(1)X charges of Table I ----- *)

  xqL == {
    ParameterType -> Internal,
    Value         -> xH/6 + xPhi/3,
    Description   -> "U(1)X charge of the quark doublet q_L"
  },
  xuR == {
    ParameterType -> Internal,
    Value         -> 2 xH/3 + xPhi/3,
    Description   -> "U(1)X charge of u_R"
  },
  xdR == {
    ParameterType -> Internal,
    Value         -> -xH/3 + xPhi/3,
    Description   -> "U(1)X charge of d_R"
  },
  xlL == {
    ParameterType -> Internal,
    Value         -> -xH/2 - xPhi,
    Description   -> "U(1)X charge of the lepton doublet l_L"
  },
  xeR == {
    ParameterType -> Internal,
    Value         -> -xH - xPhi,
    Description   -> "U(1)X charge of e_R"
  },
  xnR == {
    ParameterType -> Internal,
    Value         -> -xPhi,
    Description   -> "U(1)X charge of N_R"
  },
  xHd == {
    ParameterType -> Internal,
    Value         -> xH/2,
    Description   -> "U(1)X charge of the SM.fr doublet Phi (Y = +1/2). It is minus the charge of the paper's H"
  },
  xSc == {
    ParameterType -> Internal,
    Value         -> 2 xPhi,
    Description   -> "U(1)X charge of the SM-singlet scalar Phi_X"
  },

(* ----- Internal parameters: masses and Yukawa matrices ----- *)

  MZp == {
    ParameterType -> Internal,
    Value         -> gX Sqrt[xSc^2 vX^2 + xHd^2 vev^2],
    TeX           -> Subscript[M, Zp],
    Description   -> "Zp mass, MZp = gX Sqrt[4 xPhi^2 vX^2 + xH^2 vev^2/4] (Sec. II)"
  },

  MHX == {
    ParameterType -> Internal,
    Value         -> Sqrt[2 lamX vX^2],
    TeX           -> Subscript[M, HX],
    Description   -> "Mass of the singlet scalar radial mode, MHX^2 = 2 lamX vX^2"
  },

  mNmaj == {
    ParameterType -> Internal,
    Indices       -> {Index[Generation], Index[Generation]},
    Value         -> {mNmaj[1,1] -> MNX1, mNmaj[1,2] -> 0,     mNmaj[1,3] -> 0,
                      mNmaj[2,1] -> 0,    mNmaj[2,2] -> MNX2,  mNmaj[2,3] -> 0,
                      mNmaj[3,1] -> 0,    mNmaj[3,2] -> 0,     mNmaj[3,3] -> MNX3},
    TeX           -> Subscript[m, N],
    Description   -> "Diagonal Majorana mass matrix of the right-handed neutrinos [GeV]"
  },

  yN == {
    ParameterType    -> Internal,
    Indices          -> {Index[Generation], Index[Generation]},
    InteractionOrder -> {NP, 1},
    Value            -> {yN[1,1] -> Sqrt[2] MNX1/vX, yN[1,2] -> 0,               yN[1,3] -> 0,
                         yN[2,1] -> 0,               yN[2,2] -> Sqrt[2] MNX2/vX, yN[2,3] -> 0,
                         yN[3,1] -> 0,               yN[3,2] -> 0,               yN[3,3] -> Sqrt[2] MNX3/vX},
    TeX              -> Subscript[Y, N],
    Description      -> "Majorana Yukawa Y_N, 5th term of Eq.(LYk); inverted from m_N = Y_N vX / Sqrt[2]"
  }

};

(* ************************** *)
(* **** Particle classes **** *)
(* ************************** *)

M$ClassesDescription = {

(* --- New neutral gauge boson: real vector, SM gauge singlet --- *)
  V[100] == {
    ClassName       -> Zp,
    SelfConjugate   -> True,
    Mass            -> {MZp, Internal},
    Width           -> {WZp, 1353.},
    ParticleName    -> "Zp",
    PDG             -> 9900032,
    PropagatorLabel -> "Zp",
    PropagatorType  -> Sine,
    PropagatorArrow -> None,
    FullName        -> "Zprime"
  },

(* --- Radial mode of the SM-singlet U(1)X scalar: real scalar --- *)
  S[100] == {
    ClassName       -> HX,
    SelfConjugate   -> True,
    Mass            -> {MHX, Internal},
    Width           -> {WHX, 0.1},
    ParticleName    -> "HX",
    PDG             -> 9900025,
    PropagatorLabel -> "HX",
    PropagatorType  -> D,
    PropagatorArrow -> None,
    FullName        -> "U1XHiggs"
  },

(* --- Right-handed neutrinos: three Majorana mass eigenstates --- *)
  F[100] == {
    ClassName        -> NX,
    ClassMembers     -> {NX1, NX2, NX3},
    Indices          -> {Index[Generation]},
    FlavorIndex      -> Generation,
    SelfConjugate    -> True,
    Mass             -> {MNX, {MNX1, 8000.}, {MNX2, 8000.}, {MNX3, 8000.}},
    Width            -> {WNX, {WNX1, 1.*^-10}, {WNX2, 1.*^-10}, {WNX3, 1.*^-10}},
    PropagatorLabel  -> {"NX", "NX1", "NX2", "NX3"},
    PropagatorType   -> Straight,
    PropagatorArrow  -> None,
    PDG              -> {9900012, 9900014, 9900016},
    ParticleName     -> {"nx1", "nx2", "nx3"},
    FullName         -> {"RHN1", "RHN2", "RHN3"}
  },

(* --- Right-handed neutrino chiral field: unphysical --- *)
  F[110] == {
    ClassName      -> NR,
    Unphysical     -> True,
    Indices        -> {Index[Generation]},
    FlavorIndex    -> Generation,
    SelfConjugate  -> False,
    QuantumNumbers -> {Y -> 0, LeptonNumber -> 1},
    Definitions    -> { NR[sp1_, ff_] :> Module[{sp2}, ProjP[sp1, sp2] NX[sp2, ff]] }
  }

};

(* ************************** *)
(* *****   Lagrangian   ***** *)
(* ************************** *)

(* Free Zp field: kinetic term and mass term *)
LZpKin := Block[{mu, nu},
  -1/4 FS[Zp, mu, nu] FS[Zp, mu, nu] + 1/2 MZp^2 Zp[mu] Zp[mu]];

(* Zp currents of the SM fermions and of the RHNs, Eq.(Lag1) *)
LZpF := Block[{mu},
  ExpandIndices[
    -gX Zp[mu] (
        xqL QLbar.Ga[mu].QL
      + xuR uRbar.Ga[mu].uR
      + xdR dRbar.Ga[mu].dR
      + xlL LLbar.Ga[mu].LL
      + xeR lRbar.Ga[mu].lR
      + xnR NRbar.Ga[mu].NR ),
    FlavorExpand -> {SU2D}] /. {CKM[a_, b_] Conjugate[CKM[a_, c_]] -> IndexDelta[b, c],
                                CKM[b_, a_] Conjugate[CKM[c_, a_]] -> IndexDelta[b, c]}];

(* Free RHN fields: Majorana kinetic term and Majorana mass term *)
LNXKin := Block[{mu},
  I/2 NXbar.Ga[mu].del[NX, mu] - 1/2 NXbar.mNmaj.NX];

(* Free singlet scalar: kinetic term and mass term *)
LHXKin := Block[{mu},
  1/2 del[HX, mu] del[HX, mu] - 1/2 MHX^2 HX^2];

(* Zp-Zp-HX and Zp-Zp-HX-HX from the singlet covariant kinetic term *)
LZpHX := Block[{mu},
  gX^2 xSc^2 (vX HX + 1/2 HX^2) Zp[mu] Zp[mu]];

(* Majorana Yukawa, 5th term of Eq.(LYk), written for the Majorana eigenstates *)
LNYuk := -1/(2 Sqrt[2]) HX NXbar.yN.NX;

(* Dirac neutrino Yukawa, 4th term of Eq.(LYk); Htilde-type Eps contraction *)
LNuYuk := Block[{sp, ii, jj, ff1, ff2, yuk, feynmangaugerules},
  feynmangaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar -> 0}, {}];
  yuk = ExpandIndices[
    -ynu[ff1, ff2] LLbar[sp, ii, ff1].NR[sp, ff2] Phibar[jj] Eps[ii, jj],
    FlavorExpand -> SU2D];
  yuk + HC[yuk] /. feynmangaugerules];

(* New scalar potential: singlet self-couplings and Higgs portal.            *)
(* The constant term is dropped, the tadpole cancels by m_Phi^2 = -lamX vX^2 *)
(* and the mass term is already in LHXKin. The trilinear vX HX (H^+H) piece  *)
(* would mix h and HX; the paper works in the small lambda-prime limit where *)
(* this mixing is negligible, so it is not written and not diagonalised.     *)
LPotX := Block[{ii, feynmangaugerules},
  feynmangaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar -> 0}, {}];
  ExpandIndices[
    -lamX vX HX^3 - lamX/4 HX^4 - lamHX/2 HX^2 Phibar[ii] Phi[ii],
    FlavorExpand -> SU2D] /. feynmangaugerules];

(* One total Lagrangian *)
LTotal := LSM + LZpKin + LZpF + LNXKin + LHXKin + LZpHX + LNYuk + LNuYuk + LPotX;
```