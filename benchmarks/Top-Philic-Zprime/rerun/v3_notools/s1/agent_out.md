## Mandatory self-audit

**Model content found in the paper (arXiv:1604.07421):** exactly one new state — a colour‑singlet, electrically neutral, real (self‑conjugate) spin‑1 resonance $V_1$, Eq.(1). Free parameters: $M_{V_1}$, $c_t$, $\theta$ (benchmark $M_{V_1}=1.5$ TeV, $c_t=2.0$, $\theta=\pi/2$). No other BSM field appears (the unused LaTeX macros `\Xx`, `\MX` are template leftovers, never used in the body).

| term | fields in monomial | d | coupling | coupling dim (4−d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | new U(1) sum | L / B sum | CC[] | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LV1Kin` (kinetic) | `FS[V1,mu,nu] FS[V1,mu,nu]` | 4 | −1/4 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | n/a (no new U(1) gauged) | 0 | n/a | n/a | self‑conjugate (real V1) |
| `LV1Kin` (mass) | `V1[mu] V1[mu]` | 2 | `MV1^2` | 2 ✓ | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | $M_{V_1}$ of Eq.(2) | self‑conjugate |
| `LV1Top` (L part) | `uqbar`, `uq`, `V1[mu]` | 4 | `cVL[3,3] = ct Cos[thV]` | 0 ✓ | n/a | −2/3+2/3+0 = 0 ✓ | −1/6+1/6+0 = 0 ✓ | `V1` is an SU(2) singlet; Eq.(1) is written for the physical top mass eigenstate, so no doublet/`Eps` contraction exists in the paper's simplified model | `3bar ⊗ 3 ⊗ 1` → singlet ✓ | n/a | B: −1/3+1/3 = 0; L: 0 ✓ | n/a | LaTeX Eq.(1): `c_t \, \bar{t} \, \gamma_{\mu} (\cos \theta P_{L} + \sin \theta P_{R}) \, t \, V_{1}^{\mu}` — no fraction or root in the coupling | self‑Hermitian (real coupling, real vector) |
| `LV1Top` (R part) | `uqbar`, `uq`, `V1[mu]` | 4 | `cVR[3,3] = ct Sin[thV]` | 0 ✓ | n/a | 0 ✓ | −2/3+2/3+0 = 0 ✓ | as above | as above | n/a | 0 ✓ | n/a | same LaTeX line | self‑Hermitian |
| class row: `V1` | — | — | — | — | — | — | — | — | — | — | — | — | — | kinetic + mass term `LV1Kin` exists and is summed in `LTotal` ✓ |
| colour‑rep row | — | — | — | — | — | — | — | — | — | — | — | — | — | no non‑fundamental colour rep in this model, so no `AddGaugeRepresentation` line is needed ✓ |

- **`SelfConjugate -> True` classes:** `V1` only. It carries **no** `QuantumNumbers`. ✓
- **Names used:** classes `V1`; parameters `MV1`, `WV1`, `ct`, `thV`, `cVL`(components `cVL11`…`cVL33`), `cVR`(components `cVR11`…`cVR33`); order `NP`; terms `LV1Kin`, `LV1Top`, `LTotal`. None is a Mathematica built‑in, a FeynRules symbol (`HC`,`CC`,`FS`,`DC`,`del`,`Eps`,`Ga`,`ProjP`,`ProjM`), or a name declared by SM.fr. No primes or punctuation in `ParticleName`. Class label `V[100]` ≥ 100. ✓
- **Indices:** no new index is introduced; only SM.fr indices (`Generation`, `Colour`) are used, so no `IndexRange` line is required. ✓
- **Interaction orders:** `ct`, `cVL`, `cVR` carry `{NP, 1}`; `thV` is an angle, not a coupling (same treatment as `cabi` in SM.fr). `M$InteractionOrderHierarchy` declares `{QCD,1}`, `{QED,2}`, `{NP,1}`. ✓
- **Flavour structure:** written as matrix products between class fields (`uqbar.cVL.Ga[mu].ProjM.uq`), never as explicit index sums; all nine components of each matrix get explicit numeric values, no `_?NumericQ` pattern rules. ✓
- **Single total:** `LTotal := LV1Kin + LV1Top;` — sums every term defined. No term without a field. ✓
- **Width default:** from Eq.(2), $\Gamma=\frac{c_t^2 M_{V_1}}{8\pi}\sqrt{1-\frac{4m_t^2}{M_{V_1}^2}}\big[1-\frac{m_t^2}{M_{V_1}^2}(1-3\sin 2\theta)\big]$ with $c_t=2$, $M_{V_1}=1500$, $m_t=172$ (SM.fr `MT`), $\theta=\pi/2$ ⇒ $\Gamma\simeq 229.31$ GeV (consistent with the paper's $\Gamma/M\approx c_t^2/8\pi$).
- **Reference or cached model file read:** none.

```mathematica
(* ****************************************************************************** *)
(* *****  FeynRules add-on model file                                       ***** *)
(* *****  Top-philic colour-singlet vector resonance V1                     ***** *)
(* *****  Extracted from arXiv:1604.07421 (Kim, Kong, Lee, Mohlabeng)       ***** *)
(* *****  "Probing TeV scale Top-Philic Resonances with Boosted Top-Tagging" ***** *)
(* *****  This file is loaded ON TOP OF SM.fr                               ***** *)
(* ****************************************************************************** *)

M$ModelName = "Top-Philic-Zprime_gen";

M$Information = {
  Authors      -> {"Automated extraction from arXiv:1604.07421"},
  Version      -> "1.0",
  Date         -> "09. 09. 2026",
  Institutions -> {"n/a"},
  Emails       -> {"n/a"},
  URLs         -> "https://arxiv.org/abs/1604.07421"
};

(* ****************************************************************************** *)
(* *****    Indices                                                         ***** *)
(* ****************************************************************************** *)
(* No new index is required.  The model uses only the indices already declared    *)
(* by SM.fr (Generation, Colour, Gluon, SU2D, SU2W).                              *)
(* No new colour representation is required: V1 is a colour singlet, so no        *)
(* AddGaugeRepresentation[...] line is needed.                                    *)

(* ****************************************************************************** *)
(* *****    Interaction orders (as used by mg5)                             ***** *)
(* ****************************************************************************** *)

M$InteractionOrderHierarchy = {
  {QCD, 1},
  {QED, 2},
  {NP,  1}
};

(* ****************************************************************************** *)
(* *****    Particle classes                                                ***** *)
(* ****************************************************************************** *)
(* Eq.(1) of the paper: V1 is a colour-singlet, electrically neutral, real        *)
(* (self-conjugate) spin-1 resonance that couples dominantly to the top quark.    *)

M$ClassesDescription = {

  V[100] == {
    ClassName       -> V1,
    SelfConjugate   -> True,
    Mass            -> {MV1, 1500.},
    Width           -> {WV1, 229.31},
    ParticleName    -> "V1",
    PDG             -> 32,
    PropagatorLabel -> "V1",
    PropagatorType  -> Sine,
    PropagatorArrow -> None,
    FullName        -> "Top-philic colour-singlet vector resonance"
  }

};

(* ****************************************************************************** *)
(* *****    Parameters                                                      ***** *)
(* ****************************************************************************** *)

M$Parameters = {

  (* -------------------- External parameters -------------------- *)

  ct == {
    ParameterType    -> External,
    BlockName        -> TOPPHILIC,
    OrderBlock       -> 1,
    Value            -> 2.0,
    InteractionOrder -> {NP, 1},
    ComplexParameter -> False,
    TeX              -> Subscript[c, t],
    Description      -> "Overall V1-top coupling strength, ct = Sqrt[cL^2 + cR^2], Eq.(1); benchmark ct = 2.0"
  },

  thV == {
    ParameterType    -> External,
    BlockName        -> TOPPHILIC,
    OrderBlock       -> 2,
    Value            -> 1.5707963267948966,
    ComplexParameter -> False,
    TeX              -> Subscript[\[Theta], t],
    Description      -> "Chirality angle theta of Eq.(1), Tan[theta] = cR/cL; benchmark theta = Pi/2 (purely right-handed coupling)"
  },

  (* -------------------- Internal parameters -------------------- *)
  (* Eq.(1): cL = ct Cos[theta], cR = ct Sin[theta].  The resonance is        *)
  (* top-philic, so only the (3,3) entry of the generation-space matrices is  *)
  (* non-zero.  All nine components are given explicitly (no pattern rules).  *)

  cVL == {
    ParameterType    -> Internal,
    Indices          -> {Index[Generation], Index[Generation]},
    ComplexParameter -> False,
    Value            -> {cVL[1,1] -> 0, cVL[1,2] -> 0, cVL[1,3] -> 0,
                         cVL[2,1] -> 0, cVL[2,2] -> 0, cVL[2,3] -> 0,
                         cVL[3,1] -> 0, cVL[3,2] -> 0, cVL[3,3] -> ct*Cos[thV]},
    ParameterName    -> {cVL[1,1] -> cVL11, cVL[1,2] -> cVL12, cVL[1,3] -> cVL13,
                         cVL[2,1] -> cVL21, cVL[2,2] -> cVL22, cVL[2,3] -> cVL23,
                         cVL[3,1] -> cVL31, cVL[3,2] -> cVL32, cVL[3,3] -> cVL33},
    InteractionOrder -> {NP, 1},
    TeX              -> Superscript[c, L],
    Description      -> "Left-handed V1 coupling matrix to up-type quarks; cVL[3,3] = ct Cos[thV] = cL of Eq.(1), all other entries vanish (top-philic)"
  },

  cVR == {
    ParameterType    -> Internal,
    Indices          -> {Index[Generation], Index[Generation]},
    ComplexParameter -> False,
    Value            -> {cVR[1,1] -> 0, cVR[1,2] -> 0, cVR[1,3] -> 0,
                         cVR[2,1] -> 0, cVR[2,2] -> 0, cVR[2,3] -> 0,
                         cVR[3,1] -> 0, cVR[3,2] -> 0, cVR[3,3] -> ct*Sin[thV]},
    ParameterName    -> {cVR[1,1] -> cVR11, cVR[1,2] -> cVR12, cVR[1,3] -> cVR13,
                         cVR[2,1] -> cVR21, cVR[2,2] -> cVR22, cVR[2,3] -> cVR23,
                         cVR[3,1] -> cVR31, cVR[3,2] -> cVR32, cVR[3,3] -> cVR33},
    InteractionOrder -> {NP, 1},
    TeX              -> Superscript[c, R],
    Description      -> "Right-handed V1 coupling matrix to up-type quarks; cVR[3,3] = ct Sin[thV] = cR of Eq.(1), all other entries vanish (top-philic)"
  }

};

(* ****************************************************************************** *)
(* *****    Lagrangian                                                      ***** *)
(* ****************************************************************************** *)

(* Free field terms for the new real vector V1: Proca kinetic + mass term. *)

LV1Kin := Block[{mu, nu},
  ExpandIndices[
    -1/4 FS[V1, mu, nu] FS[V1, mu, nu] + 1/2 MV1^2 V1[mu] V1[mu]
  ]];

(* Eq.(1):  L_int = tbar Ga[mu] (cL ProjM + cR ProjP) t V1[mu]                *)
(*                = ct tbar Ga[mu] (Cos[theta] ProjM + Sin[theta] ProjP) t V1[mu] *)
(* Written as a matrix product in generation space between the class fields.  *)
(* The couplings are real and V1 is self-conjugate, so the term is Hermitian  *)
(* by itself and needs no HC[] partner.                                       *)

LV1Top := Block[{mu},
  ExpandIndices[
    uqbar.cVL.Ga[mu].ProjM.uq V1[mu] + uqbar.cVR.Ga[mu].ProjP.uq V1[mu]
  ]];

(* Single total Lagrangian of the add-on. *)

LTotal := LV1Kin + LV1Top;
```