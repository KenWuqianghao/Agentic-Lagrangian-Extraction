## Mandatory self-audit table

Model: **368sextets** — Carpenter, Murphy, Tait, *The phenomenological cornucopia of SU(3) exotica*, arXiv:2110.11359. New states: Table X. Operators: Eqs. `\eqref{sFmodel}` and `\eqref{sSmodel}`. Colour Clebsch–Gordan implementation: Eq. `\eqref{A18}` of Appendix A.

Charge bookkeeping uses SM.fr hypercharges (uR: Y=2/3, dR: Y=−1/3, lR: Y=−1). For a barred charge-conjugate field the charge is **+** that of the field itself: `\overline{u^c_R}` carries Q = Y = +2/3, `\overline{d^c_R}` carries Q = Y = −1/3. All new states are SU(2) singlets, so Q = Y for each.

| term name | fields in the monomial | d | coupling symbol | coupling mass dim (4−d) | 1/Λ power (must be d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L sum | CC[] used | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LPsiuFree | `Psiubar.Ga[mu].DC[Psiu,mu]`; `Psiubar.Psiu` | 4; 3 | MPSU | 1 = 4−3 | n/a | 0 | 0 | singlet (no SU(2) index) | 6 ⊗ 6bar → 1 (T6 via DC) | none | 0 | n/a | n/a | Hermitian by itself |
| LPsidFree | `Psidbar.Ga[mu].DC[Psid,mu]`; `Psidbar.Psid` | 4; 3 | MPSD | 1 = 4−3 | n/a | 0 | 0 | singlet | 6 ⊗ 6bar → 1 | none | 0 | n/a | n/a | Hermitian by itself |
| LPhiuFree | `DC[Phiubar,mu] DC[Phiu,mu]`; `Phiubar Phiu` | 4; 2 | MPHU^2 | 2 = 4−2 | n/a | 0 | 0 | singlet | 6 ⊗ 6bar → 1 | none | 0 | n/a | n/a | Hermitian by itself |
| LPhidFree | `DC[Phidbar,mu] DC[Phid,mu]`; `Phidbar Phid` | 4; 2 | MPHD^2 | 2 = 4−2 | n/a | 0 | 0 | singlet | 6 ⊗ 6bar → 1 | none | 0 | n/a | n/a | Hermitian by itself |
| LPsiuG | `CC[uqbar]`, `Psiu`, `FS[G,mu,nu,aa]` | 5 | kapu[ff]/LamPsu | −1 = 4−5 | 1 ✓ | 2/3 − 2/3 = 0 | 2/3 − 2/3 = 0 | all singlets; ProjP selects uR | J^{s i a} = `-I Eps[i1,i2,i3] T[aa,i2,i4] K6bar[ss,i4,i3]`, 3 ⊗ 6 ⊗ 8 → 1 | none | 0 + 0 = 0 | yes (`CC[uqbar]`) | LaTeX Eq.(A18) + its footnote: √2 L^{ijk}=ε^{ijk} ⇒ J = −i ε t K̄ | `HC[...]` |
| LPsidG | `CC[dqbar]`, `Psid`, `FS[G,mu,nu,aa]` | 5 | kapd[ff]/LamPsd | −1 | 1 ✓ | −1/3 + 1/3 = 0 | −1/3 + 1/3 = 0 | all singlets; ProjP selects dR | same J structure | none | 0 | yes (`CC[dqbar]`) | LaTeX Eq.(A18) | `HC[...]` |
| LPsiuB | `CC[uqbar]`, `Psiu`, `FS[B,mu,nu]`, `FS[G,mu,nu,aa]` | 7 | kapuB[ff]/LamPsuB^3 | −3 = 4−7 | 3 ✓ | 0 | 0 | all singlets; ProjP selects uR | same J structure | none | 0 | yes | LaTeX Eq.(A18) | `HC[...]` |
| LPsidB | `CC[dqbar]`, `Psid`, `FS[B,mu,nu]`, `FS[G,mu,nu,aa]` | 7 | kapdB[ff]/LamPsdB^3 | −3 | 3 ✓ | 0 | 0 | all singlets | same J structure | none | 0 | yes | LaTeX Eq.(A18) | `HC[...]` |
| LPhiuG | `Phiu`, `CC[uqbar]`, `l`, `FS[G,mu,nu,aa]` | 6 | lamu[xx,ff]/LamPhu^2 | −2 = 4−6 | 2 ✓ | 1/3 + 2/3 − 1 = 0 | 1/3 + 2/3 − 1 = 0 | all singlets; ProjP selects uR and lR | same J structure, Φ carries the sextet index | none | −1 + 1 = 0 | yes | LaTeX Eq.(A18) | `HC[...]` |
| LPhidG | `Phid`, `CC[dqbar]`, `l`, `FS[G,mu,nu,aa]` | 6 | lamd[xx,ff]/LamPhd^2 | −2 | 2 ✓ | 4/3 − 1/3 − 1 = 0 | 4/3 − 1/3 − 1 = 0 | all singlets | same J structure | none | −1 + 1 = 0 | yes | LaTeX Eq.(A18) | `HC[...]` |

Per-class kinetic + mass confirmation: `Phiu` → LPhiuFree; `Phid` → LPhidFree; `Psiu` → LPsiuFree; `Psid` → LPsidFree. All four terms appear in `LTotal`.

Non-fundamental colour representation: one (the SU(3)c sextet). `IndexRange[Index[Sextet]] = NoUnfold[Range[6]];` and `AddGaugeRepresentation[SU3C -> {T6, Sextet}];` are both present, before the class declarations.

`SelfConjugate -> True` classes: **none** (all four new states are complex/Dirac, so no class carries a forbidden `QuantumNumbers` block).

Names used — classes `Phiu, Phid, Psiu, Psid`; parameters `MPHU, MPHD, MPSU, MPSD, WPHU, WPHD, WPSU, WPSD, LamPsu, LamPsd, LamPsuB, LamPsdB, LamPhu, LamPhd, kapu, kapd, kapuB, kapdB, lamu, lamd`; index `Sextet`. None is a Mathematica built-in, none is a FeynRules symbol (`HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM, T, T6, K6, K6bar`), and none is declared by SM.fr (`Phi, H, Z, W, A, G, B, lam, vev, ee, gs, gw, sw, cw, MZ, MW, ...`). Class labels are `S[100], S[101], F[100], F[101]`.

Single total: `LTotal = LPsiuFree + LPsidFree + LPhiuFree + LPhidFree + LPsiuG + LPsidG + LPsiuB + LPsidB + LPhiuG + LPhidG`. No other total is defined; no term is a pure constant.

Reference or cached model file read: **none**.

Benchmark defaults (Sec. III.A): κ_q = 0.05, Λ_Ψq = 1 TeV; κ_qB = 0.10, Λ_ΨqB = 1 TeV; λ_q^{XI} = 0.1 δ^{XI}, Λ_Φq = 1 TeV. The paper quotes κ for I ∈ {1,2}, but the branching-fraction footnote in Sec. III.B (BF(Ψu → t̄ g) ≈ 0.21) requires a non-zero third-generation coupling, so the same value is used for I = 3; this is stated in the parameter Descriptions.

```mathematica
(* ************************************************************************ *)
(* *****  FeynRules add-on model file: colour-sextet scalars and     ****** *)
(* *****  fermions coupling to a quark and a gluon.                  ****** *)
(* *****  Extracted from L. M. Carpenter, T. Murphy, T. M. P. Tait,  ****** *)
(* *****  "The phenomenological cornucopia of SU(3) exotica",        ****** *)
(* *****  arXiv:2110.11359.  Loaded on top of SM.fr.                 ****** *)
(* ************************************************************************ *)

M$ModelName = "368sextets_gen";

M$Information = {
  Authors      -> {"automated extraction from arXiv:2110.11359"},
  Version      -> "1.0",
  Date         -> "09. 09. 2026",
  Institutions -> {"n/a"},
  Emails       -> {"n/a"},
  URLs         -> "https://arxiv.org/abs/2110.11359"
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
(* Colour, Gluon, Generation, SU2D and SU2W are declared by SM.fr.          *)
(* The six-dimensional (sextet) representation of SU(3)c is new.            *)

IndexRange[Index[Sextet]] = NoUnfold[Range[6]];

IndexStyle[Sextet, s];

AddGaugeRepresentation[SU3C -> {T6, Sextet}];

(* ************************** *)
(* *****   Parameters   ***** *)
(* ************************** *)

M$Parameters = {

  (* ---------- EFT cutoffs (Eqs. (2) and (3) of the paper) ---------- *)

  LamPsu == {
    ParameterType    -> External,
    BlockName        -> SXTCUTOFF,
    OrderBlock       -> 1,
    Value            -> 1000.,
    InteractionOrder -> {NP, -1},
    Description      -> "EFT cutoff Lambda_Psi_u [GeV] of the (q^c sigma Psi_u) G operator, Eq.(2); paper benchmark 1 TeV"
  },
  LamPsd == {
    ParameterType    -> External,
    BlockName        -> SXTCUTOFF,
    OrderBlock       -> 2,
    Value            -> 1000.,
    InteractionOrder -> {NP, -1},
    Description      -> "EFT cutoff Lambda_Psi_d [GeV] of the (q^c sigma Psi_d) G operator, Eq.(2); paper benchmark 1 TeV"
  },
  LamPsuB == {
    ParameterType    -> External,
    BlockName        -> SXTCUTOFF,
    OrderBlock       -> 3,
    Value            -> 1000.,
    InteractionOrder -> {NP, -1},
    Description      -> "EFT cutoff Lambda_Psi_uB [GeV] of the (q^c Psi_u) B G operator, Eq.(2); paper benchmark 1 TeV"
  },
  LamPsdB == {
    ParameterType    -> External,
    BlockName        -> SXTCUTOFF,
    OrderBlock       -> 4,
    Value            -> 1000.,
    InteractionOrder -> {NP, -1},
    Description      -> "EFT cutoff Lambda_Psi_dB [GeV] of the (q^c Psi_d) B G operator, Eq.(2); paper benchmark 1 TeV"
  },
  LamPhu == {
    ParameterType    -> External,
    BlockName        -> SXTCUTOFF,
    OrderBlock       -> 5,
    Value            -> 1000.,
    InteractionOrder -> {NP, -1},
    Description      -> "EFT cutoff Lambda_Phi_u [GeV] of the Phi_u (q^c sigma l) G operator, Eq.(3); paper benchmark 1 TeV"
  },
  LamPhd == {
    ParameterType    -> External,
    BlockName        -> SXTCUTOFF,
    OrderBlock       -> 6,
    Value            -> 1000.,
    InteractionOrder -> {NP, -1},
    Description      -> "EFT cutoff Lambda_Phi_d [GeV] of the Phi_d (q^c sigma l) G operator, Eq.(3); paper benchmark 1 TeV"
  },

  (* ---------- dimensionless couplings ---------- *)

  kapu == {
    ParameterType    -> External,
    Indices          -> {Index[Generation]},
    BlockName        -> KAPU,
    Value            -> {kapu[1] -> 0.05, kapu[2] -> 0.05, kapu[3] -> 0.05},
    InteractionOrder -> {NP, 1},
    Description      -> "kappa_u^I, dimensionless coupling of Psi_u to an up-type quark and a gluon, Eq.(2); paper benchmark 0.05 for I=1,2, same value taken for I=3 (cf. BF(Psi_u->tbar g) in Sec. III.B)"
  },
  kapd == {
    ParameterType    -> External,
    Indices          -> {Index[Generation]},
    BlockName        -> KAPD,
    Value            -> {kapd[1] -> 0.05, kapd[2] -> 0.05, kapd[3] -> 0.05},
    InteractionOrder -> {NP, 1},
    Description      -> "kappa_d^I, dimensionless coupling of Psi_d to a down-type quark and a gluon, Eq.(2); paper benchmark 0.05"
  },
  kapuB == {
    ParameterType    -> External,
    Indices          -> {Index[Generation]},
    BlockName        -> KAPUB,
    Value            -> {kapuB[1] -> 0.10, kapuB[2] -> 0.10, kapuB[3] -> 0.10},
    InteractionOrder -> {NP, 1},
    Description      -> "kappa_uB^I, dimensionless coupling of Psi_u to an up-type quark, a gluon and a B boson, Eq.(2); paper benchmark 0.10"
  },
  kapdB == {
    ParameterType    -> External,
    Indices          -> {Index[Generation]},
    BlockName        -> KAPDB,
    Value            -> {kapdB[1] -> 0.10, kapdB[2] -> 0.10, kapdB[3] -> 0.10},
    InteractionOrder -> {NP, 1},
    Description      -> "kappa_dB^I, dimensionless coupling of Psi_d to a down-type quark, a gluon and a B boson, Eq.(2); paper benchmark 0.10"
  },
  lamu == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    BlockName        -> LAMU,
    Value            -> {lamu[1,1] -> 0.1, lamu[1,2] -> 0.,  lamu[1,3] -> 0.,
                         lamu[2,1] -> 0.,  lamu[2,2] -> 0.1, lamu[2,3] -> 0.,
                         lamu[3,1] -> 0.,  lamu[3,2] -> 0.,  lamu[3,3] -> 0.1},
    InteractionOrder -> {NP, 1},
    Description      -> "lambda_u^{XI}, dimensionless coupling of Phi_u to a charged lepton (generation X, first index), an up-type quark (generation I, second index) and a gluon, Eq.(3); paper benchmark 0.1 delta^{XI}"
  },
  lamd == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    BlockName        -> LAMD,
    Value            -> {lamd[1,1] -> 0.1, lamd[1,2] -> 0.,  lamd[1,3] -> 0.,
                         lamd[2,1] -> 0.,  lamd[2,2] -> 0.1, lamd[2,3] -> 0.,
                         lamd[3,1] -> 0.,  lamd[3,2] -> 0.,  lamd[3,3] -> 0.1},
    InteractionOrder -> {NP, 1},
    Description      -> "lambda_d^{XI}, dimensionless coupling of Phi_d to a charged lepton (generation X, first index), a down-type quark (generation I, second index) and a gluon, Eq.(3); paper benchmark 0.1 delta^{XI}"
  }
};

(* ************************** *)
(* **** Particle classes **** *)
(* ************************** *)
(* Table X of the paper:                                                    *)
(*   Phi_u ~ (6,1, 1/3), L = -1        Phi_d ~ (6,1, 4/3), L = -1           *)
(*   Psi_u ~ (6,1,-2/3), L =  0        Psi_d ~ (6,1, 1/3), L =  0           *)
(* All four are weak singlets, hence Q = Y.                                 *)

M$ClassesDescription = {

(* Colour-sextet scalars *)
  S[100] == {
    ClassName        -> Phiu,
    SelfConjugate    -> False,
    Indices          -> {Index[Sextet]},
    Mass             -> {MPHU, 1000.},
    Width            -> {WPHU, 10.},
    QuantumNumbers   -> {Q -> 1/3, Y -> 1/3, LeptonNumber -> -1},
    PropagatorLabel  -> "Phiu",
    PropagatorType   -> D,
    PropagatorArrow  -> Forward,
    PDG              -> 9000001,
    ParticleName     -> "phiu",
    AntiParticleName -> "phiu~",
    FullName         -> "Colour-sextet scalar coupling to up-type quarks"
  },
  S[101] == {
    ClassName        -> Phid,
    SelfConjugate    -> False,
    Indices          -> {Index[Sextet]},
    Mass             -> {MPHD, 1000.},
    Width            -> {WPHD, 10.},
    QuantumNumbers   -> {Q -> 4/3, Y -> 4/3, LeptonNumber -> -1},
    PropagatorLabel  -> "Phid",
    PropagatorType   -> D,
    PropagatorArrow  -> Forward,
    PDG              -> 9000002,
    ParticleName     -> "phid",
    AntiParticleName -> "phid~",
    FullName         -> "Colour-sextet scalar coupling to down-type quarks"
  },

(* Colour-sextet Dirac fermions *)
  F[100] == {
    ClassName        -> Psiu,
    SelfConjugate    -> False,
    Indices          -> {Index[Sextet]},
    Mass             -> {MPSU, 1000.},
    Width            -> {WPSU, 10.},
    QuantumNumbers   -> {Q -> -2/3, Y -> -2/3},
    PropagatorLabel  -> "Psiu",
    PropagatorType   -> Straight,
    PropagatorArrow  -> Forward,
    PDG              -> 9000011,
    ParticleName     -> "psiu",
    AntiParticleName -> "psiu~",
    FullName         -> "Colour-sextet Dirac fermion coupling to up-type quarks"
  },
  F[101] == {
    ClassName        -> Psid,
    SelfConjugate    -> False,
    Indices          -> {Index[Sextet]},
    Mass             -> {MPSD, 1000.},
    Width            -> {WPSD, 10.},
    QuantumNumbers   -> {Q -> 1/3, Y -> 1/3},
    PropagatorLabel  -> "Psid",
    PropagatorType   -> Straight,
    PropagatorArrow  -> Forward,
    PDG              -> 9000012,
    ParticleName     -> "psid",
    AntiParticleName -> "psid~",
    FullName         -> "Colour-sextet Dirac fermion coupling to down-type quarks"
  }
};

(* ************************** *)
(* *****   Lagrangian   ***** *)
(* ************************** *)

(* Free (kinetic + mass) terms; first lines of Eqs. (2) and (3).            *)

LPsiuFree := Block[{mu},
  ExpandIndices[I Psiubar.Ga[mu].DC[Psiu, mu] - MPSU Psiubar.Psiu]];

LPsidFree := Block[{mu},
  ExpandIndices[I Psidbar.Ga[mu].DC[Psid, mu] - MPSD Psidbar.Psid]];

LPhiuFree := Block[{mu},
  ExpandIndices[DC[Phiubar, mu] DC[Phiu, mu] - MPHU^2 Phiubar Phiu]];

LPhidFree := Block[{mu},
  ExpandIndices[DC[Phidbar, mu] DC[Phid, mu] - MPHD^2 Phidbar Phid]];

(* The Clebsch-Gordan coefficients J^{s,i,a} of the invariant 3 x 6 x 8 are *)
(* built from the existing FeynRules objects following Eq. (A18):           *)
(*   J^{s i a} = -I Sqrt[2] L^{ijk} [t3^a]_j^l Kbar^s_{lk},                 *)
(* together with Sqrt[2] L^{ijk} = Eps^{ijk}, so that                       *)
(*   J^{s i a} = -I Eps[i,j,k] T[a,j,l] K6bar[s,l,k].                       *)

(* Sextet fermion - quark - gluon operator, second line of Eq. (2).         *)
LPsiuG := Block[{sp1, sp2, sp3, sp4, ff, i1, i2, i3, i4, ss, aa, mu, nu, tmp},
  tmp = ExpandIndices[
    (-I) kapu[ff]/LamPsu *
      Eps[i1, i2, i3] T[aa, i2, i4] K6bar[ss, i4, i3] *
      CC[uqbar][sp1, ff, i1] ProjP[sp1, sp2] *
      (I/2) (Ga[mu, sp2, sp3] Ga[nu, sp3, sp4] - Ga[nu, sp2, sp3] Ga[mu, sp3, sp4]) *
      Psiu[sp4, ss] FS[G, mu, nu, aa]];
  tmp + HC[tmp]];

LPsidG := Block[{sp1, sp2, sp3, sp4, ff, i1, i2, i3, i4, ss, aa, mu, nu, tmp},
  tmp = ExpandIndices[
    (-I) kapd[ff]/LamPsd *
      Eps[i1, i2, i3] T[aa, i2, i4] K6bar[ss, i4, i3] *
      CC[dqbar][sp1, ff, i1] ProjP[sp1, sp2] *
      (I/2) (Ga[mu, sp2, sp3] Ga[nu, sp3, sp4] - Ga[nu, sp2, sp3] Ga[mu, sp3, sp4]) *
      Psid[sp4, ss] FS[G, mu, nu, aa]];
  tmp + HC[tmp]];

(* Sextet fermion - quark - gluon - B operator, third line of Eq. (2).      *)
LPsiuB := Block[{sp1, sp2, ff, i1, i2, i3, i4, ss, aa, mu, nu, tmp},
  tmp = ExpandIndices[
    (-I) kapuB[ff]/LamPsuB^3 *
      Eps[i1, i2, i3] T[aa, i2, i4] K6bar[ss, i4, i3] *
      CC[uqbar][sp1, ff, i1] ProjP[sp1, sp2] Psiu[sp2, ss] *
      FS[B, mu, nu] FS[G, mu, nu, aa]];
  tmp + HC[tmp]];

LPsidB := Block[{sp1, sp2, ff, i1, i2, i3, i4, ss, aa, mu, nu, tmp},
  tmp = ExpandIndices[
    (-I) kapdB[ff]/LamPsdB^3 *
      Eps[i1, i2, i3] T[aa, i2, i4] K6bar[ss, i4, i3] *
      CC[dqbar][sp1, ff, i1] ProjP[sp1, sp2] Psid[sp2, ss] *
      FS[B, mu, nu] FS[G, mu, nu, aa]];
  tmp + HC[tmp]];

(* Sextet scalar - quark - lepton - gluon operator, second line of Eq. (3). *)
LPhiuG := Block[{sp1, sp2, sp3, sp4, ff, xx, i1, i2, i3, i4, ss, aa, mu, nu, tmp},
  tmp = ExpandIndices[
    (-I) lamu[xx, ff]/LamPhu^2 *
      Eps[i1, i2, i3] T[aa, i2, i4] K6bar[ss, i4, i3] Phiu[ss] *
      CC[uqbar][sp1, ff, i1] *
      (I/2) (Ga[mu, sp1, sp2] Ga[nu, sp2, sp3] - Ga[nu, sp1, sp2] Ga[mu, sp2, sp3]) *
      ProjP[sp3, sp4] l[sp4, xx] FS[G, mu, nu, aa]];
  tmp + HC[tmp]];

LPhidG := Block[{sp1, sp2, sp3, sp4, ff, xx, i1, i2, i3, i4, ss, aa, mu, nu, tmp},
  tmp = ExpandIndices[
    (-I) lamd[xx, ff]/LamPhd^2 *
      Eps[i1, i2, i3] T[aa, i2, i4] K6bar[ss, i4, i3] Phid[ss] *
      CC[dqbar][sp1, ff, i1] *
      (I/2) (Ga[mu, sp1, sp2] Ga[nu, sp2, sp3] - Ga[nu, sp1, sp2] Ga[mu, sp2, sp3]) *
      ProjP[sp3, sp4] l[sp4, xx] FS[G, mu, nu, aa]];
  tmp + HC[tmp]];

(* ************************** *)
(* ***  Total Lagrangian  *** *)
(* ************************** *)

LTotal := LPsiuFree + LPsidFree + LPhiuFree + LPhidFree +
          LPsiuG + LPsidG + LPsiuB + LPsidB + LPhiuG + LPhidG;
```