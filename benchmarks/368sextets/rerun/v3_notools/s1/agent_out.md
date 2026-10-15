## Mandatory self-audit table

Field mass dimensions: scalar 1, vector 1, fermion 3/2, `FS[...]` 2, `del`/`DC` 1. SM hypercharges are the SM.fr chiral ones (`uR` 2/3, `dR` −1/3, `lR` −1); for a charge-conjugated field the sign flips, and the barred conjugate carries `+Y(q)`.

| term name | fields in the monomial | d | coupling symbol | coupling mass dim (=4−d) | 1/Λ power (=d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L sum | `CC[]` used | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LS6kin` (u) | `DC[Phi6ubar,mu] DC[Phi6u,mu]`, `MPhi6u^2 Phi6ubar Phi6u` | 4 | n/a (mass `MPhi6u`, dim 1) | n/a | 0 | 0 | all singlets | 6⊗6bar → 1 (implicit `Sextet` index) | none | 0 | n/a | n/a | self-conjugate (real) |
| `LS6kin` (d) | `DC[Phi6dbar,mu] DC[Phi6d,mu]`, `MPhi6d^2 Phi6dbar Phi6d` | 4 | n/a | n/a | 0 | 0 | all singlets | 6⊗6bar → 1 | none | 0 | n/a | n/a | self-conjugate |
| `LF6kin` (u) | `I Psi6ubar.Ga[mu].DC[Psi6u,mu]`, `MPsi6u Psi6ubar.Psi6u` | 4 | n/a (mass `MPsi6u`) | n/a | 0 | 0 | all singlets | 6⊗6bar → 1 | none | 0 | n/a | n/a | self-conjugate |
| `LF6kin` (d) | `I Psi6dbar.Ga[mu].DC[Psi6d,mu]`, `MPsi6d Psi6dbar.Psi6d` | 4 | n/a | n/a | 0 | 0 | all singlets | 6⊗6bar → 1 | none | 0 | n/a | n/a | self-conjugate |
| `LF6qg` (u) | `CC[uqbar] Sig ProjP Psi6u FS[G]` | 3/2+3/2+2 = 5 | `kapu[ff]/LamPsi6u` | −1 | 1/Λ¹ | +2/3 − 2/3 = 0 | +2/3 − 2/3 = 0 | all SU(2) singlets (`uR`, `Psi6u`) | `Eps[i,j,k] T[a,j,l] K6bar[s,l,k]` = **J**ˢⁱᵃ, Eq. (A18): 3⊗6⊗8 → 1 | n/a | 0+0 = 0 | yes | Eq. (A18) LaTeX + footnote `√2 L^{ijk} = ε^{ijk}` ⇒ **J** = −i ε t₃ K̄ | `HC[...]` |
| `LF6qg` (d) | `CC[dqbar] Sig ProjP Psi6d FS[G]` | 5 | `kapd[ff]/LamPsi6d` | −1 | 1/Λ¹ | −1/3 + 1/3 = 0 | −1/3 + 1/3 = 0 | singlets | same **J** contraction | n/a | 0 | yes | same | `HC[...]` |
| `LF6qgB` (u) | `CC[uqbar] ProjP Psi6u FS[B] FS[G]` | 3/2+3/2+2+2 = 7 | `kapuB[ff]/LamPsi6uB^3` | −3 | 1/Λ³ | 0 | 0 | singlets | same **J** contraction | n/a | 0 | yes | same | `HC[...]` |
| `LF6qgB` (d) | `CC[dqbar] ProjP Psi6d FS[B] FS[G]` | 7 | `kapdB[ff]/LamPsi6dB^3` | −3 | 1/Λ³ | 0 | 0 | singlets | same **J** contraction | n/a | 0 | yes | same | `HC[...]` |
| `LS6qlg` (u) | `Phi6u CC[uqbar] Sig ProjP l FS[G]` | 1+3/2+3/2+2 = 6 | `lamu[ffX,ffI]/LamPhi6u^2` | −2 | 1/Λ² | 1/3 + 2/3 − 1 = 0 | 1/3 + 2/3 − 1 = 0 | singlets (`lR`, `uR`, `Phi6u`) | same **J** contraction | n/a | −1 + 1 = 0 | yes | same | `HC[...]` |
| `LS6qlg` (d) | `Phi6d CC[dqbar] Sig ProjP l FS[G]` | 6 | `lamd[ffX,ffI]/LamPhi6d^2` | −2 | 1/Λ² | 4/3 − 1/3 − 1 = 0 | 4/3 − 1/3 − 1 = 0 | singlets | same **J** contraction | n/a | −1 + 1 = 0 | yes | same | `HC[...]` |

Per-class kinetic+mass confirmation: `Phi6u` → in `LS6kin`; `Phi6d` → in `LS6kin`; `Psi6u` → in `LF6kin`; `Psi6d` → in `LF6kin`. All four terms are inside `LTotal`.

Non-fundamental colour representation: the four new fields carry the `Sextet` index; `IndexRange[Index[Sextet]] = NoUnfold[Range[6]];` and `AddGaugeRepresentation[SU3C -> {T6, Sextet}];` are both present before the class declarations. `DC[...]` is applied to the whole field, never with an explicit colour index.

`SelfConjugate -> True` classes: none. All four new classes are complex (`SelfConjugate -> False`), so the rule about quantum numbers on real classes does not apply.

Names used — classes `Phi6u, Phi6d, Psi6u, Psi6d`; parameters `MPhi6u, MPhi6d, MPsi6u, MPsi6d, WPhi6u, WPhi6d, WPsi6u, WPsi6d, LamPsi6u, LamPsi6d, LamPsi6uB, LamPsi6dB, LamPhi6u, LamPhi6d, kapu, kapd, kapuB, kapdB, lamu, lamd`; index `Sextet`; order `NP`. None is a Mathematica built-in, a FeynRules symbol, or an SM.fr name.

Single total: `LTotal := LS6kin + LF6kin + LF6qg + LF6qgB + LS6qlg;` — it sums every term defined in the file.

Reference or cached model file read: none. Only the paper source and SM.fr given in the prompt were used.

Two extraction notes. (1) `Q` and `Y` are both declared on the new classes: `Y` is needed so `DC[...]` builds the U(1)ᵧ (photon and Z) interaction of these weak singlets, `Q` gives the UFO electric charge; the values agree because the fields are SU(2) singlets (Table X). (2) The paper's benchmark text quotes κ for I ∈ {1,2}, but the branching-fraction footnote of Section III.B lists non-zero `BF(Psi_u -> t~ g)` and `BF(Psi_u -> t~ g A)`, so the third generation couples as well; all three components take the quoted values 0.05 and 0.10.

```mathematica
(* ************************************************************************ *)
(* *****  FeynRules add-on: colour-sextet scalars and Dirac fermions  ***** *)
(* *****  Extracted from arXiv:2110.11359 (Carpenter, Murphy, Tait)   ***** *)
(* *****  "The phenomenological cornucopia of SU(3) exotica"          ***** *)
(* *****  Load on top of SM.fr.                                       ***** *)
(* ************************************************************************ *)

M$ModelName = "368sextets_gen";

M$Information = {
  Authors      -> {"automated extraction from the paper"},
  Version      -> "1.0",
  Date         -> "09. 09. 2026",
  Institutions -> {"n/a"},
  Emails       -> {"n/a"},
  References   -> {"L. M. Carpenter, T. Murphy, T. M. P. Tait, arXiv:2110.11359"},
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
(* Colour, Gluon, Generation, SU2D and SU2W come from SM.fr.                *)
(* The colour sextet index is new: it needs its own range and the sextet    *)
(* representation of SU3C.                                                  *)

IndexRange[Index[Sextet]] = NoUnfold[Range[6]];
IndexStyle[Sextet, s];

AddGaugeRepresentation[SU3C -> {T6, Sextet}];

(* ************************** *)
(* **** Particle classes **** *)
(* ************************** *)
(* Table X of the paper:                                                    *)
(*   Phi6u ~ (6,1, 1/3)  L = -1     Phi6d ~ (6,1, 4/3)  L = -1              *)
(*   Psi6u ~ (6,1,-2/3)  L =  0     Psi6d ~ (6,1, 1/3)  L =  0              *)
(* All four are SU(2)_L singlets, so Q = Y. Y is declared as well, because  *)
(* DC[] takes the U(1)_Y charge from the QuantumNumbers list.               *)

M$ClassesDescription = {

(* Colour-sextet complex scalars *)
  S[100] == {
    ClassName        -> Phi6u,
    SelfConjugate    -> False,
    Indices          -> {Index[Sextet]},
    Mass             -> {MPhi6u, 1000.},
    Width            -> {WPhi6u, 10.},
    QuantumNumbers   -> {Q -> 1/3, Y -> 1/3, LeptonNumber -> -1},
    PropagatorLabel  -> "Phi6u",
    PropagatorType   -> D,
    PropagatorArrow  -> Forward,
    PDG              -> 6000001,
    ParticleName     -> "phi6u",
    AntiParticleName -> "phi6u~",
    FullName         -> "Colour sextet scalar coupled to up type quarks"
  },

  S[101] == {
    ClassName        -> Phi6d,
    SelfConjugate    -> False,
    Indices          -> {Index[Sextet]},
    Mass             -> {MPhi6d, 1000.},
    Width            -> {WPhi6d, 10.},
    QuantumNumbers   -> {Q -> 4/3, Y -> 4/3, LeptonNumber -> -1},
    PropagatorLabel  -> "Phi6d",
    PropagatorType   -> D,
    PropagatorArrow  -> Forward,
    PDG              -> 6000002,
    ParticleName     -> "phi6d",
    AntiParticleName -> "phi6d~",
    FullName         -> "Colour sextet scalar coupled to down type quarks"
  },

(* Colour-sextet Dirac fermions *)
  F[100] == {
    ClassName        -> Psi6u,
    SelfConjugate    -> False,
    Indices          -> {Index[Sextet]},
    Mass             -> {MPsi6u, 1000.},
    Width            -> {WPsi6u, 10.},
    QuantumNumbers   -> {Q -> -2/3, Y -> -2/3},
    PropagatorLabel  -> "Psi6u",
    PropagatorType   -> Straight,
    PropagatorArrow  -> Forward,
    PDG              -> 6000011,
    ParticleName     -> "psi6u",
    AntiParticleName -> "psi6u~",
    FullName         -> "Colour sextet Dirac fermion coupled to up type quarks"
  },

  F[101] == {
    ClassName        -> Psi6d,
    SelfConjugate    -> False,
    Indices          -> {Index[Sextet]},
    Mass             -> {MPsi6d, 1000.},
    Width            -> {WPsi6d, 10.},
    QuantumNumbers   -> {Q -> 1/3, Y -> 1/3},
    PropagatorLabel  -> "Psi6d",
    PropagatorType   -> Straight,
    PropagatorArrow  -> Forward,
    PDG              -> 6000012,
    ParticleName     -> "psi6d",
    AntiParticleName -> "psi6d~",
    FullName         -> "Colour sextet Dirac fermion coupled to down type quarks"
  }
};

(* ************************** *)
(* *****   Parameters   ***** *)
(* ************************** *)

M$Parameters = {

(* ---- EFT cutoff scales, all set to the paper benchmark of 1 TeV ---- *)

  LamPsi6u == {
    ParameterType -> External,
    BlockName     -> SXTCUT,
    OrderBlock    -> 1,
    Value         -> 1000.,
    Description   -> "EFT cutoff [GeV] of the sextet fermion - up type quark - gluon operator, Eq.(13) second line; d = 5, so the term carries 1/Lambda^1"
  },

  LamPsi6d == {
    ParameterType -> External,
    BlockName     -> SXTCUT,
    OrderBlock    -> 2,
    Value         -> 1000.,
    Description   -> "EFT cutoff [GeV] of the sextet fermion - down type quark - gluon operator, Eq.(13) second line; d = 5, so the term carries 1/Lambda^1"
  },

  LamPsi6uB == {
    ParameterType -> External,
    BlockName     -> SXTCUT,
    OrderBlock    -> 3,
    Value         -> 1000.,
    Description   -> "EFT cutoff [GeV] of the sextet fermion - up type quark - gluon - hypercharge operator, Eq.(13) third line; d = 7, so the term carries 1/Lambda^3"
  },

  LamPsi6dB == {
    ParameterType -> External,
    BlockName     -> SXTCUT,
    OrderBlock    -> 4,
    Value         -> 1000.,
    Description   -> "EFT cutoff [GeV] of the sextet fermion - down type quark - gluon - hypercharge operator, Eq.(13) third line; d = 7, so the term carries 1/Lambda^3"
  },

  LamPhi6u == {
    ParameterType -> External,
    BlockName     -> SXTCUT,
    OrderBlock    -> 5,
    Value         -> 1000.,
    Description   -> "EFT cutoff [GeV] of the sextet scalar - up type quark - lepton - gluon operator, Eq.(14); d = 6, so the term carries 1/Lambda^2"
  },

  LamPhi6d == {
    ParameterType -> External,
    BlockName     -> SXTCUT,
    OrderBlock    -> 6,
    Value         -> 1000.,
    Description   -> "EFT cutoff [GeV] of the sextet scalar - down type quark - lepton - gluon operator, Eq.(14); d = 6, so the term carries 1/Lambda^2"
  },

(* ---- Dimensionless couplings, paper benchmarks ---- *)

  kapu == {
    ParameterType    -> External,
    Indices          -> {Index[Generation]},
    BlockName        -> SXTKAPU,
    Value            -> {kapu[1] -> 0.05, kapu[2] -> 0.05, kapu[3] -> 0.05},
    InteractionOrder -> {NP, 1},
    Description      -> "Dimensionless coupling kappa_u^I of Psi6u to an up type quark and a gluon, Eq.(13)"
  },

  kapd == {
    ParameterType    -> External,
    Indices          -> {Index[Generation]},
    BlockName        -> SXTKAPD,
    Value            -> {kapd[1] -> 0.05, kapd[2] -> 0.05, kapd[3] -> 0.05},
    InteractionOrder -> {NP, 1},
    Description      -> "Dimensionless coupling kappa_d^I of Psi6d to a down type quark and a gluon, Eq.(13)"
  },

  kapuB == {
    ParameterType    -> External,
    Indices          -> {Index[Generation]},
    BlockName        -> SXTKAPUB,
    Value            -> {kapuB[1] -> 0.10, kapuB[2] -> 0.10, kapuB[3] -> 0.10},
    InteractionOrder -> {NP, 1},
    Description      -> "Dimensionless coupling kappa_uB^I of Psi6u to an up type quark, a gluon and a hypercharge boson, Eq.(13)"
  },

  kapdB == {
    ParameterType    -> External,
    Indices          -> {Index[Generation]},
    BlockName        -> SXTKAPDB,
    Value            -> {kapdB[1] -> 0.10, kapdB[2] -> 0.10, kapdB[3] -> 0.10},
    InteractionOrder -> {NP, 1},
    Description      -> "Dimensionless coupling kappa_dB^I of Psi6d to a down type quark, a gluon and a hypercharge boson, Eq.(13)"
  },

  lamu == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    BlockName        -> SXTLAMU,
    Value            -> {lamu[1,1] -> 0.1, lamu[1,2] -> 0., lamu[1,3] -> 0.,
                         lamu[2,1] -> 0., lamu[2,2] -> 0.1, lamu[2,3] -> 0.,
                         lamu[3,1] -> 0., lamu[3,2] -> 0., lamu[3,3] -> 0.1},
    InteractionOrder -> {NP, 1},
    Description      -> "Dimensionless coupling lambda_u^{XI} (X lepton generation, I quark generation) of Phi6u to an up type quark, a lepton and a gluon, Eq.(14); diagonal benchmark 0.1"
  },

  lamd == {
    ParameterType    -> External,
    Indices          -> {Index[Generation], Index[Generation]},
    BlockName        -> SXTLAMD,
    Value            -> {lamd[1,1] -> 0.1, lamd[1,2] -> 0., lamd[1,3] -> 0.,
                         lamd[2,1] -> 0., lamd[2,2] -> 0.1, lamd[2,3] -> 0.,
                         lamd[3,1] -> 0., lamd[3,2] -> 0., lamd[3,3] -> 0.1},
    InteractionOrder -> {NP, 1},
    Description      -> "Dimensionless coupling lambda_d^{XI} (X lepton generation, I quark generation) of Phi6d to a down type quark, a lepton and a gluon, Eq.(14); diagonal benchmark 0.1"
  }
};

(* ************************** *)
(* *****   Lagrangian   ***** *)
(* ************************** *)

(* The Clebsch-Gordan coefficients J^{s i a} of the 3 x 6 x 8 invariant are  *)
(* built from the sextet coefficients K6bar and the totally antisymmetric    *)
(* triplet coefficients, exactly as in Eq.(A18) of the appendix:             *)
(*     J^{s i a} = -I Sqrt[2] L^{ijk} [t3^a]_j^l Kbar^s_{lk}                 *)
(* together with Sqrt[2] L^{ijk} = Eps^{ijk}, this gives                     *)
(*     J^{s i a} = -I Eps[i,j,k] T[a,j,l] K6bar[s,l,k].                      *)

(* ---- Kinetic and mass terms of the sextet scalars ---- *)

LS6kin := Block[{mu},
  ExpandIndices[
      DC[Phi6ubar, mu] DC[Phi6u, mu] - MPhi6u^2 Phi6ubar Phi6u
    + DC[Phi6dbar, mu] DC[Phi6d, mu] - MPhi6d^2 Phi6dbar Phi6d ]];

(* ---- Kinetic and mass terms of the sextet Dirac fermions ---- *)

LF6kin := Block[{mu},
  ExpandIndices[
      I Psi6ubar.Ga[mu].DC[Psi6u, mu] - MPsi6u Psi6ubar.Psi6u
    + I Psi6dbar.Ga[mu].DC[Psi6d, mu] - MPsi6d Psi6dbar.Psi6d ]];

(* ---- Sextet fermion, quark and gluon; Eq.(13), second line, d = 5 ---- *)

LF6qg := Block[{mu, nu, ff, ii, jj, kk, ll, ss, aa, op},
  op = -I/LamPsi6u kapu[ff] Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] *
         (CC[uqbar][ff, ii].Sig[mu, nu].ProjP.Psi6u[ss]) FS[G, mu, nu, aa]
     - I/LamPsi6d kapd[ff] Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] *
         (CC[dqbar][ff, ii].Sig[mu, nu].ProjP.Psi6d[ss]) FS[G, mu, nu, aa];
  ExpandIndices[op + HC[op]]];

(* ---- Sextet fermion, quark, gluon and hypercharge boson;
        Eq.(13), third line, d = 7 ---- *)

LF6qgB := Block[{mu, nu, ff, ii, jj, kk, ll, ss, aa, op},
  op = -I/LamPsi6uB^3 kapuB[ff] Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] *
         (CC[uqbar][ff, ii].ProjP.Psi6u[ss]) FS[B, mu, nu] FS[G, mu, nu, aa]
     - I/LamPsi6dB^3 kapdB[ff] Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] *
         (CC[dqbar][ff, ii].ProjP.Psi6d[ss]) FS[B, mu, nu] FS[G, mu, nu, aa];
  ExpandIndices[op + HC[op]]];

(* ---- Sextet scalar, quark, lepton and gluon; Eq.(14), d = 6 ---- *)

LS6qlg := Block[{mu, nu, ff1, ff2, ii, jj, kk, ll, ss, aa, op},
  op = -I/LamPhi6u^2 lamu[ff2, ff1] Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] *
         Phi6u[ss] (CC[uqbar][ff1, ii].Sig[mu, nu].ProjP.l[ff2]) FS[G, mu, nu, aa]
     - I/LamPhi6d^2 lamd[ff2, ff1] Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] *
         Phi6d[ss] (CC[dqbar][ff1, ii].Sig[mu, nu].ProjP.l[ff2]) FS[G, mu, nu, aa];
  ExpandIndices[op + HC[op]]];

(* ---- One total ---- *)

LTotal := LS6kin + LF6kin + LF6qg + LF6qgB + LS6qlg;
```