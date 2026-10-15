I read the whole prompt file (SM.fr, the paper LaTeX source, and the task rules). No cached or reference `.fr` file for this model was read.

## Extraction summary

New physics content of arXiv:1604.07421: **one** new state — a colour-singlet, electrically neutral, real (self-conjugate) spin-1 resonance `V1`, coupled only to the top quark, Eq. (1):
L_int = c_t · t̄ γ_μ (cos θ P_L + sin θ P_R) t V1^μ, with c_L = c_t cos θ, c_R = c_t sin θ, tan θ = c_R/c_L.
Free parameters: M_V1, c_t, θ. Benchmark: M_V1 = 1.5 TeV, c_t = 2.0, θ = π/2.
No other BSM field exists in the paper (the four-top signal is V1-strahlung; the contact operator in Eq. (3) is the heavy-V1 limit of the same field, not a new state).

Width, Eq. (2) — LaTeX read literally: `\frac{c_t^{2} M_{V_1}}{8\pi} \sqrt{1 - \frac{4m_t^2}{M_{V_1}^2}} [1 - \frac{m_t^2}{M_{V_1}^2}(1 - 3\sin 2\theta)]`. At the benchmark (θ = π/2, sin 2θ = 0, m_t = 172): Γ = 4·1500/(8π) · 0.97335 · 0.98685 = **229.31 GeV** (Γ/M = 0.153 ≈ c_t²/8π, as the paper states). This numeric value is the declared width default.

## Mandatory self-audit table

| term name | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L/B sum | CC[] used | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LV1Kin (a) | FS[V1,mu,nu] FS[V1,mu,nu] | 4 | −1/4 | 0 ✓ | n/a | 0 | 0 | singlet (no index) | singlet (no index) | n/a (no new U(1) gauged) | n/a | n/a | n/a | self-conjugate (real field) |
| LV1Kin (b) | V1[mu] V1[mu] | 2 | MV1^2/2 | 2 ✓ | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | n/a | self-conjugate |
| LV1Top (L) | tbar . Ga[mu] . ProjM . t · V1[mu] | 4 | ctL = ct Cos[thV1] | 0 ✓ | n/a | (−2/3)+(2/3)+0 = 0 ✓ | (−1/6)+(1/6) = 0 ✓ | none needed: Eq.(1) is written for the mass-eigenstate top (broken phase), a vector-like current, so each chiral piece is separately Y-neutral | 3̄ ⊗ 3 ⊗ 1, contracted by IndexDelta on Colour | n/a | 0 | n/a (paper writes no ψ^c) | Eq.(1) has no fraction/root; the √ and fractions of Eq.(2) read from the LaTeX line `\frac{c_t^{2} M_{V_1}}{8\pi}\sqrt{1-\frac{4m_t^2}{M_{V_1}^2}}` and used only for the width default | Hermitian by itself (t̄γ^μP_L t is Hermitian, ctL real, V1 real) — no HC[] |
| LV1Top (R) | tbar . Ga[mu] . ProjP . t · V1[mu] | 4 | ctR = ct Sin[thV1] | 0 ✓ | n/a | (−2/3)+(2/3)+0 = 0 ✓ | (−2/3)+(2/3) = 0 ✓ | same as above | same as above | n/a | 0 | n/a | same as above | Hermitian by itself — no HC[] |
| class row: V[100] `V1` | — | — | — | — | — | Q = 0 | Y = 0 | singlet | singlet | — | — | — | — | kinetic + mass term `LV1Kin` exists and is summed in `LTotal` ✓ |
| colour-rep row | — | — | — | — | — | — | — | — | only the fundamental `Colour` index of SM.fr is used; **no** `AddGaugeRepresentation` line is needed (n/a) | — | — | — | — | — |

- SelfConjugate -> True classes: `V1` only — it carries **no** `QuantumNumbers` ✓ (its Q = 0 and it is a colour/SU(2) singlet).
- Names chosen: classes `V1`; parameters `MV1`, `WV1`, `ct`, `thV1`, `ctL`, `ctR`; Lagrangian symbols `LV1Kin`, `LV1Top`, `LTotal`; block `TOPPHILIC`. None is a Mathematica built-in (`N,C,D,E,I,K,O`), a FeynRules symbol (`HC,CC,FS,DC,del,Eps,Ga,ProjP,ProjM`), or an SM.fr name (`H,Phi,Z,W,A,G,ee,gs,gw,sw,cw,vev,MZ,MW,MT,...`). No new index is declared because none is needed. Class label is `V[100]` (≥ 100) ✓.
- Single total: `LTotal := LV1Kin + LV1Top;` — it sums every other term defined in the file ✓ (no second total, no field-free term).
- New U(1) charges: V1 is a simplified-model vector, not the gauge boson of a gauged U(1) with SM charges (with c_L ≠ c_R and no SM-field charges assigned in the paper), so no new U(1) charge column applies; every Q and Y sum is 0 as shown.
- Reference or cached model file read: **none**.

```mathematica
(* ****************************************************************************** *)
(* *****  Top-philic colour-singlet vector resonance V1  (FeynRules add-on)  **** *)
(* *****  Loaded on top of SM.fr; field names, indices and hypercharge      ***** *)
(* *****  conventions are those of SM.fr.                                  ***** *)
(* *****                                                                   ***** *)
(* *****  Extracted from:                                                  ***** *)
(* *****    J. H. Kim, K. Kong, S. J. Lee, G. Mohlabeng, arXiv:1604.07421   ***** *)
(* *****    "Probing TeV scale Top-Philic Resonances with Boosted           ***** *)
(* *****     Top-Tagging at the High Luminosity LHC"                        ***** *)
(* *****                                                                   ***** *)
(* *****  Eq.(1):  L_int = ct tbar Ga[mu] (Cos[th] ProjM + Sin[th] ProjP) t V1[mu] *)
(* *****  Eq.(2):  Gamma(V1 -> t tbar) =                                    ***** *)
(* *****      ct^2 MV1/(8 Pi) Sqrt[1 - 4 MT^2/MV1^2]                        ***** *)
(* *****        (1 - MT^2/MV1^2 (1 - 3 Sin[2 th]))                          ***** *)
(* *****  Benchmark of the paper: MV1 = 1500 GeV, ct = 2.0, th = Pi/2.      ***** *)
(* *****  At that point Eq.(2) gives Gamma = 229.31 GeV, used as the        ***** *)
(* *****  default width below (Gamma/MV1 = 0.153 ~ ct^2/(8 Pi)).            ***** *)
(* ****************************************************************************** *)

(* ************************** *)
(* *****  Information   ***** *)
(* ************************** *)

M$ModelName = "Top-Philic-Zprime_gen";

M$Information = {
  Authors      -> {"Automated extraction from arXiv:1604.07421"},
  Version      -> "1.0",
  Date         -> "09. 09. 2026",
  Institutions -> {"n/a"},
  Emails       -> {"n/a"},
  References   -> {"J. H. Kim, K. Kong, S. J. Lee and G. Mohlabeng, arXiv:1604.07421 [hep-ph]"},
  URLs         -> "https://arxiv.org/abs/1604.07421"
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

(* No new index is needed: V1 is a colour singlet and an SU(2) singlet.     *)
(* Colour, Gluon, Generation, SU2D and SU2W are already declared by SM.fr.  *)

(* ************************** *)
(* **** Particle classes **** *)
(* ************************** *)

M$ClassesDescription = {

(* Colour-singlet, electrically neutral, real (self-conjugate) vector resonance *)
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
    FullName        -> "Top-philic vector resonance"
  }
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
    Value            -> 2.,
    InteractionOrder -> {NP, 1},
    TeX              -> Subscript[c, t],
    Description      -> "Overall coupling strength of V1 to the top quark, ct = Sqrt[cL^2+cR^2], Eq.(1)"
  },
  thV1 == {
    ParameterType -> External,
    BlockName     -> TOPPHILIC,
    OrderBlock    -> 2,
    Value         -> 1.5707963267948966,
    TeX           -> Subscript[\[Theta], t],
    Description   -> "Chirality angle theta with Tan[theta] = cR/cL, Eq.(1); benchmark theta = Pi/2 (purely right-handed)"
  },

  (* Internal parameters *)
  ctL == {
    ParameterType    -> Internal,
    Value            -> ct Cos[thV1],
    InteractionOrder -> {NP, 1},
    ParameterName    -> ctL,
    TeX              -> Subscript[c, L],
    Description      -> "Left-handed top coupling cL = ct Cos[theta], Eq.(1)"
  },
  ctR == {
    ParameterType    -> Internal,
    Value            -> ct Sin[thV1],
    InteractionOrder -> {NP, 1},
    ParameterName    -> ctR,
    TeX              -> Subscript[c, R],
    Description      -> "Right-handed top coupling cR = ct Sin[theta], Eq.(1)"
  }
};

(* ************************** *)
(* *****   Lagrangian   ***** *)
(* ************************** *)

(* Free field terms of the real vector resonance *)
LV1Kin := Block[{mu, nu},
  ExpandIndices[-1/4 FS[V1, mu, nu] FS[V1, mu, nu] + 1/2 MV1^2 V1[mu] V1[mu]]
];

(* Top-philic interaction, Eq.(1). The current tbar.Ga[mu].ProjM(P).t is        *)
(* Hermitian and V1 is real, so the term is self-conjugate: no HC[...] is added. *)
LV1Top := Block[{mu},
  ExpandIndices[(ctL tbar.Ga[mu].ProjM.t + ctR tbar.Ga[mu].ProjP.t) V1[mu]]
];

(* Single total Lagrangian of the add-on *)
LTotal := LV1Kin + LV1Top;
```