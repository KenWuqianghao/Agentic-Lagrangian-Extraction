# Cross-check: `reconstruction.md` against `paper.tex`

RUN-TAG: XM-CROSS-331__flip_charge

## 1. Where the paper defines the model

The paper is "Collider Phenomenology of the 3-3-1 Model" (Cao and Zhang). The model
definition is in Sec. 2 ("The Model") and in Appendix A ("Feynman rules interaction
vertices"). The relevant places are:

* **Gauge group and charge operator** — Sec. 2.1: `SU(3)_C x SU(3)_L x U(1)_X`,
  with `Y = beta T^8 + X` and `Q = T^3 + beta T^8 + X`.
* **Scalar sector** — Sec. 2.1, Eq. (1) gives the three triplets `rho`, `eta`, `chi`
  and the charges `Q_Y = sqrt(3)beta/2 + 1/2`, `Q_V = sqrt(3)beta/2 - 1/2`
  (Eq. after Eq. `\eqref{xqn}`). The potential is Eq. `\eqref{VHiggs}`, with
  `f = k v_3`.
* **Scalar masses** — Sec. 2.1.1 and Sec. 2.5: `M_H2^2`, `M_H3^2` (Eqs. `\label{4}`,
  `\label{5}`), `M_H0^2`, `M_Hpm^2`, `M_H^{QY}^2`, `M_H^{QV}^2`.
* **Gauge sector** — Sec. 2.2: mass terms in Eq. `\eqref{gauge mass}`, charged vector
  masses in Eq. `\eqref{MVY}`, `M_Z'^2` in Eq. `\label{3}` and in the text after
  Eq. `\eqref{B}`.
* **Fermion sector** — Sec. 2.3: the triplets `q_1L`, `q_2L`, the anti-triplet `q_3L`,
  the lepton anti-triplets `l_iL`, the exotic-quark charges
  `Q_D = Q_S = 1/6 - sqrt(3)beta/2`, `Q_T = 1/6 + sqrt(3)beta/2`, and
  `Q_E = -1/2 + sqrt(3)beta/2`.
* **Yukawa sector** — Sec. 2.4, the two Lagrangians `-L^q_Yuk` and `-L^l_Yuk`.
* **Charge table for each beta** — Table `tbl:charge` (Sec. 2.5).
* **All vertices** — Appendix A: Table `gauge-fermion` (gauge boson to fermion),
  Table `gauges` (gauge self-couplings), Tables `1gauge-2scalars`,
  `2gauges-1scalar`, `2gauges-2scalars` (gauge to scalar), Table `scalar-fermion`.
* Sec. 6.1 states that the `V-J-q` and `Y-J-q` couplings are both equal to
  `g/sqrt(2)`.

The reconstruction is a broken-phase (mass-eigenstate) file for the benchmark
`beta = +1/sqrt(3)`. Column `beta = 1/sqrt(3)` of Table `tbl:charge` is therefore the
correct reference column. That column gives `Q_D = Q_S = -1/3`, `Q_T = +2/3`,
`Q_E = 0`, `Q_V = 0`, `Q_Y = +1`, `Q_{H^{QV}} = 0`, `Q_{H^{QY}} = +1`, `Q_{H^pm} = 1`.

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Gauge group `SU(3)_C x SU(3)_L x U(1)_X`, `Q = T^3 + beta T^8 + X` (Sec. 2.1) | no gauge group declared; broken-phase add-on on the SM model | agree (in scope) | The file is a mass-eigenstate implementation. This is a valid reduction of the paper, but it removes the `SU(3)_L` structure that fixes all new couplings. |
| `beta = +1/sqrt(3)` benchmark (Sec. 2.5, Table `tbl:charge`) | `beta = 0.5773502692` external input | agree | One of the four benchmarks of the paper. |
| `-1/4 F_munu F^munu` for `Z'` and Proca mass, Eq. `\eqref{gauge mass}` | `L_Zp = -1/4 Zp_munu Zp^munu + 1/2 M_Zp^2 Zp^2`, real field | agree | Real neutral vector, correct normalisation. |
| `M_Z'^2 = c_W^2 g^2 v_3^2 / (3[1-(1+beta^2)s_W^2])`, Eq. `\label{3}`; equal to `(g^2 + beta^2 g_X^2) v_3^2 / 3` | `MZp = sqrt((g_w^2 + beta^2 g_X^2) v_3^2 / 6)` | **disagree** | The reconstruction is smaller by a factor `sqrt(2)`. See D2. |
| `M_Y^2 = g^2 (v_3^2 + v_2^2)/4`, Eq. `\eqref{MVY}` | `MYp = sqrt(g_w^2 (v_3^2+v_2^2)/4)` | agree | |
| `M_V^2 = g^2 (v_3^2 + v_1^2)/4`, Eq. `\eqref{MVY}` | `MVp = sqrt(g_w^2 (v_3^2+v_1^2)/4)` | agree | |
| `Y^{+Q_Y}` with `Q_Y = +1` (Table `tbl:charge`) | `Yp`, complex vector, `Q = +1` | agree | Charge value correct. |
| `V^{+Q_V}` with `Q_V = 0` (Table `tbl:charge`) | `Vp`, complex vector, `Q = 0`, not self-conjugate | agree | A neutral but complex (bilepton-type) vector is correct for this beta. |
| Photon coupling of `Y`: `A Y^{+Q_Y} Y^{-Q_Y} = i a_+ e / 2` (Table `gauges`) | absent; `FS[Yp]` is the plain curl, `Yp` is not in `DC` | **missing-in-reconstruction** | See D3. |
| `Z`, `Z'` couplings of `Y` and `V`, and `V-W-Y` triple coupling (Table `gauges`) | absent | **missing-in-reconstruction** | See D3. |
| Quartic gauge couplings (Table `gauges`) | absent | **missing-in-reconstruction** | Follows from the same cause as D3. |
| Exotic quarks `D`, `S` in the third place of `q_1L`, `q_2L` (Sec. 2.3), colour triplets, vector-like Dirac mass from `y^J chi` (Sec. 2.4) | `DQ`, `SQ`: colour-triplet Dirac fields, mass term `-M Qbar Q` with no projector | agree | Vector-like Dirac mass is the correct outcome of the `chi` Yukawa term. |
| `Q_D = Q_S = 1/6 - sqrt(3)beta/2 = -1/3` (Sec. 2.3, Table `tbl:charge`) | `Q_DQ = Q_SQ = -1/3` | agree | |
| Hypercharge of `D`: `Y = Q = -1/3` for a `T^3 = 0` state; confirmed by `Dbar D A = -i(3sqrt(3)beta-1)e/6 = -ie/3` (Table `gauge-fermion`) | `Y_DQ = +1/3` | **disagree** | Sign flip. See D1. This is the most serious item. |
| Hypercharge of `S`: `Y = Q = -1/3`; `Sbar S A = -ie/3` (Table `gauge-fermion`) | `Y_SQ = -1/3` | agree | `S` has the same role as `D`, and here the file is consistent. |
| `Q_T = 1/6 + sqrt(3)beta/2 = +2/3`; `Tbar T A = +2ie/3` (Table `gauge-fermion`) | `TQ`, `Q = Y = +2/3` | agree | |
| `Z` couplings of `D`, `S`, `T` (Table `gauge-fermion`) | generated by `DC` from the declared `Y` | agree for `S`, `T`; **disagree** for `D` | Same root cause as D1. |
| Heavy leptons `E_e, E_mu, E_tau`, third place of the lepton anti-triplets; `Q_E = -1/2 + sqrt(3)beta/2 = 0` (Sec. 2.3) | `EL`, three Dirac fields, `Q = Y = 0`, colour singlet, independent masses | agree | Neutral heavy leptons are correct for `beta = +1/sqrt(3)`. |
| `Ebar E Z'` coupling `= i e[(a_-^2+1)s_W^2-2] / (2 sqrt(3) c_W s_W a_0)`, non-zero (Table `gauge-fermion`) | none; `E` is a free field | **missing-in-reconstruction** | Part of D4. |
| CP-even scalars `h`, `H_2`, `H_3`, real neutral (Sec. 2.1.1) | `H2`, `H3`: real self-conjugate scalars, free kinetic term with `del` | agree on field type; `h` is **missing-in-reconstruction** | The 125 GeV state `h` and the mixing matrix `U` are not in the file. |
| CP-odd scalar `H_0`, real neutral (Sec. 2.1.1) | `H0`: real self-conjugate scalar | agree | |
| `M_H2^2 = (v^2 / (v_1 v_2)) f v_3` (Eq. `\label{4}`) | same formula | agree | |
| `M_H3^2 = 2 lambda_3 v_3^2` (Eq. `\label{5}`) | same formula | agree | |
| `M_H0^2 = (v_1v_2/v_3 + v_1v_3/v_2 + v_2v_3/v_1) f` (Sec. 2.5) | same formula | agree | |
| `M_Hpm^2 = (2 f v_3 + lambda'_12 v_1 v_2) v^2 / (2 v_1 v_2)` (Sec. 2.5) | same formula | agree | |
| `M_H^{QY}^2 = (2 f v_1 + lambda'_23 v_2 v_3)(v_2^2+v_3^2)/(2 v_2 v_3)` (Sec. 2.5) | same formula | agree | |
| `M_H^{QV}^2 = (2 f v_2 + lambda'_13 v_1 v_3)(v_1^2+v_3^2)/(2 v_1 v_3)` (Sec. 2.5) | same formula | agree | |
| `H^pm` with `Q = 1` (Table `tbl:charge`) | `Hpm`, `Q = Y = 1`, gauge kinetic term through `DC` | agree | |
| `H^{±Q_Y}` with `Q_Y = 1` (Table `tbl:charge`) | `HQY`, `Q = Y = 1`, `DC` kinetic term | agree | |
| `H^{±Q_V}` with `Q_V = 0` (Table `tbl:charge`) | `HQV`, neutral complex scalar, `Q = Y = 0` | agree | |
| `f = k v_3`, `k ~ O(1)` (Sec. 2.1) | `f = k v_3`, `k = 1` | agree | |
| `v^2 = v_1^2 + v_2^2 = (246 GeV)^2` (Sec. 2.1.1) | `v2 = sqrt(vev^2 - v1^2)`, `vev = 246.2 GeV` | agree | Only a 0.2 GeV difference in the SM input. Cosmetic. |
| Higgs potential `V_Higgs`, Eq. `\eqref{VHiggs}` (mu terms, `lambda_i`, `lambda_ij`, `lambda'_ij`, trilinear `f`) | no potential; only the mass terms above | **missing-in-reconstruction** | All scalar self-interactions are absent. See D5. |
| Quark and lepton Yukawa Lagrangians (Sec. 2.4) and Table `scalar-fermion` | none | **missing-in-reconstruction** | See D5. |
| `VSS`, `VVS`, `VVSS` couplings (Tables `1gauge-2scalars`, `2gauges-1scalar`, `2gauges-2scalars`) | only the `DC` gauge couplings of the charged scalars | **missing-in-reconstruction** | The neutral scalars `H_2`, `H_3`, `H_0` use `del`, so they have no `ZZ`, `Z'Z'`, `VV`, `YY` couplings. |
| `Dbar u Y^{+Q_Y}`, `g_L = -ie/(sqrt(2) s_W) = -i g/sqrt(2)`, `g_R = 0` (Table `gauge-fermion`) | `(g_w/sqrt(2)) ubar gamma^mu P_L D Yp_mu` + h.c. | agree | Left-handed only, SM strength. The paper's row is the conjugate of the written term. Same vertex. |
| `Sbar c Y^{+Q_Y}`, same coefficient | `(g_w/sqrt(2)) cbar gamma^mu P_L S Yp_mu` + h.c. | agree | |
| `Dbar d V^{+Q_V}`, coefficient `-i e V_ud / (sqrt(2) s_W)` | `(g_w/sqrt(2)) dbar gamma^mu P_L D Vp_mu` + h.c., no CKM factor | **disagree** | The factor `V_ud` is dropped. See D6. |
| `Sbar s V^{+Q_V}`, coefficient `-i e V_cs / (sqrt(2) s_W)` | `(g_w/sqrt(2)) sbar gamma^mu P_L S Vp_mu` + h.c., no CKM factor | **disagree** | The factor `V_cs` is dropped. See D6. |
| `tbar T V^{+Q_V}`, `g_L = -i g/sqrt(2)` (Table `gauge-fermion`) | none | **missing-in-reconstruction** | See D7. |
| `Tbar b Y^{-Q_Y}`, `g_L = -i e V_tb/(sqrt(2) s_W)` (Table `gauge-fermion`) | none | **missing-in-reconstruction** | See D7. |
| `ebar E_e Y^{+Q_Y}`, `mubar E_mu Y`, `taubar E_tau Y`, `g_L = -i g/sqrt(2)` (Table `gauge-fermion`) | none | **missing-in-reconstruction** | See D8. |
| `nubar_e E_e V^{+Q_V}` and the `mu`, `tau` analogues (Table `gauge-fermion`) | none | **missing-in-reconstruction** | See D8. |
| `Z'` couplings to all SM fermions, to `D`, `S`, `T` and to `E_l` (Table `gauge-fermion`) | none; `Z'` is a free field | **missing-in-reconstruction** | See D4. |
| Colour contraction of the new currents (`SU(3)_c` triplet with triplet) | trivial index sum, `ubar_i gamma^mu P_L D_i` | agree | |
| `InteractionOrderHierarchy` and `NP` order | `{{QCD,1},{QED,2},{NP,1}}`, `NP` order on `gX`, `lam3`, `lampr*` | agree (no paper statement) | The paper does not fix coupling orders. This is an implementation choice. |
| Heavy fermion masses free; benchmark 1000 GeV (Sec. 2.5, Figs. of Sec. 4-6) | `MDQ = MSQ = MTQ = MEE = MEM = MET = 1000 GeV` | agree | Matches the paper's benchmark value. |
| `v_1` benchmark (174 GeV or 200 GeV in the figures; fit prefers ~150 GeV) | `v1 = 173.95 GeV` | agree | A parameter-point choice, not a model statement. |

---

## 3. Disagreements, with severity

**D1. Hypercharge of the exotic quark `D` is `+1/3` while its electric charge is
`-1/3`. Severity: substantive.**
The paper puts `D` in the third place of the triplet `q_1L`, so `T^3 = 0` and
`Q = Y = -1/3`. Table `gauge-fermion` confirms this: `Dbar D A = -i e/3` and
`Dbar D Z = +i e s_W/(3 c_W)`, exactly as for `S`. In the implementation the covariant
derivative `DC` uses the declared `Y`, so the `D` quark gets photon and `Z` couplings
with the wrong sign, while its mass, its charge label and its `LNPcc` current stay at
`Q = -1/3`. A human should set `Y_DQ = -1/3` and then re-check every `D`-quark
electroweak vertex, in particular `D Dbar A` and `D Dbar Z`, against Table
`gauge-fermion`. The reconstruction itself flags this same internal contradiction.

**D2. `M_Z'` is smaller than the paper value by a factor `sqrt(2)`. Severity:
substantive.**
The paper's mass term is `(1/6) v_3^2 (-g W^8 + beta g_X X)^2`. For a real vector the
mass term is `(1/2) M^2 Z'^2`, so `M_Z'^2 = (g^2 + beta^2 g_X^2) v_3^2 / 3`. This
agrees with Eq. `\label{3}`. The implementation uses `v_3^2/6`, which gives 580 GeV
instead of 821 GeV at the quoted parameter point. The paper also states
`M_Z' ~ 1.2 M_{V(Y)}` for `beta = ±1/sqrt(3)` (Sec. 5.1 and Eq. `\eqref{zpvy}`); the
reconstruction gives `M_Z' < M_Y`, which contradicts that statement. A human should
divide by 3, not 6, and then check that `M_Z'/M_Y = 1.26` at the benchmark point.

**D3. The new vectors `Y'` and `V'` have no gauge interactions. Severity:
substantive.**
The file uses plain abelian field strengths and keeps `Yp` and `Vp` out of `DC`. The
paper's Table `gauges` gives `A Y^+ Y^- = i a_+ e/2` (equal to `i e` at this beta),
`Z Y^+ Y^-`, `Z' Y^+ Y^-`, `Z' V^+ V^-`, `V^- W^+ Y^+` and the matching quartic
couplings. A singly charged vector with no photon coupling is not electromagnetically
gauge invariant. The paper's unitarity check in Sec. 5.1.1 needs the `A`, `Z` and `Z'`
diagrams to cancel the `D`-exchange diagram in `u ubar -> Y Y`. A human should decide
whether this file is only meant for single-exotic-quark processes, and should not use
it for `VV` or `YY` pair production.

**D4. `Z'` has no fermion couplings. Severity: substantive.**
Table `gauge-fermion` gives `Z'` couplings to `e`, `nu`, `u`, `c`, `t`, `d`, `s`, `b`,
`D`, `S`, `T` and `E_l`, with both `g_L` and `g_R`. In the file `Z'` is a free Proca
field. The whole `Z'` phenomenology of the paper (Sec. 4: Drell-Yan production,
decays, `A_FB`) cannot be reproduced. A human should check whether a second model file
supplies the `Z'` currents.

**D5. No scalar potential and no Yukawa sector. Severity: substantive.**
Eq. `\eqref{VHiggs}` and the two Yukawa Lagrangians of Sec. 2.4 produce all
scalar self-couplings, the `h` couplings of Sec. 3, and the scalar-fermion vertices of
Table `scalar-fermion` (for example `H^{+Q_Y} ubar D` and `H^{-Q_V} Dbar d`). The file
keeps only the mass terms. Therefore the charged scalars `H^pm`, `H^{Q_Y}`, `H^{Q_V}`
have no decay channel, and the heavy-quark decay mode `T -> t H^{Q_V}` of Sec. 6.2 is
absent. A human should confirm that the omission is intentional.

**D6. The CKM factors `V_ud` and `V_cs` are dropped from the `d-D-V'` and `s-S-V'`
currents. Severity: convention.**
Table `gauge-fermion` carries `V_ud` and `V_cs` in these two rows. Both are close to
0.974, so the numerical effect on rates is about 5 percent. The structural effect is
larger: without the CKM matrix there is no `d-s` flavour mixing in the new current. A
human should check whether the model file intends `V_CKM = 1`.

**D7. The `T` quark has no current term, and `t`, `b` do not appear. Severity:
substantive.**
The paper gives `tbar T V^{+Q_V}` and `Tbar b Y^{-Q_Y}` with the same `g/sqrt(2)`
strength (Table `gauge-fermion`, and Sec. 6.2 where `T -> tV` and `T -> bY` are the
dominant modes). In the file `T` only has QCD and electroweak gauge couplings, so it
is stable. Note also that `q_3L` is an anti-triplet in the paper, so the `T` couplings
differ in structure from the `D` and `S` ones; a human should reproduce them from the
anti-triplet covariant derivative of Sec. 2.3, not by copying the `D` row.

**D8. The lepton currents through `Y'` and `V'` are absent. Severity: substantive.**
Table `gauge-fermion` gives `lbar E_l Y^{+Q_Y}` and `nubar_l E_l V^{+Q_V}`, both with
`g_L = -i g/sqrt(2)`. Without them the heavy leptons `E_l` are stable free fields.
For `beta = +1/sqrt(3)` the paper treats `E_l` as a dark matter candidate and uses
`Y -> l^+ E_l` and `V -> nu E_l` for the signatures of Sec. 5.3 and Sec. 6.3. A human
should add these four-flavour-blind lepton terms if the file is used for that study.

**D9. `h` and the scalar mixing matrices `U` and `O` are absent. Severity:
substantive for Higgs studies, otherwise convention.**
The file relies on the SM Higgs of the base model. The paper's `h` is a mixture of
`xi_rho`, `xi_eta` and `xi_chi`, and all its couplings carry `U_11`, `U_21`, `U_31`
factors (Sec. 3). A human should not use this file for the Higgs results of Sec. 3.

**D10. The electroweak input `v = 246.2 GeV` against the paper's `246 GeV`. Severity:
cosmetic.**
No physics consequence. A human can ignore this.

---

## 4. Overall assessment

The reconstruction and the paper agree on the skeleton of the
`beta = +1/sqrt(3)` benchmark: the particle content is complete and correctly typed
(one real `Z'`, one charged complex `Y'`, one neutral complex `V'`, three vector-like
colour-triplet exotic quarks with charges `-1/3, -1/3, +2/3`, three neutral heavy
leptons, three real neutral scalars, two singly charged scalars and one neutral
complex scalar), every scalar mass formula matches Sec. 2.5 exactly, the two charged
vector masses match Eq. `\eqref{MVY}`, and the four implemented currents have the
correct chirality (`P_L` only), the correct colour contraction and the correct
strength `g_w/sqrt(2)` stated in Sec. 6.1. Two numerical items do not match the paper:
the hypercharge of the `D` quark carries the opposite sign to its electric charge
(D1), which makes its photon and `Z` couplings disagree with Table `gauge-fermion`
while every other field in the file obeys `Y = Q`; and `M_Z'` is low by a factor
`sqrt(2)` (D2), which also breaks the paper's mass ordering `M_Z' ~ 1.2 M_{V(Y)}`.
Beyond these, the file is a deliberate subset: it implements only the exotic-quark
charged currents, and it leaves out the `Z'` fermion couplings, the `T` and lepton
currents, the gauge self-couplings of the new vectors, the scalar potential and the
whole Yukawa sector. Whether that subset is adequate depends on the intended process;
it supports single exotic-quark production and `D`/`S` decay, but not `Z'` production,
`VV`/`YY` pair production, or any Higgs or charged-scalar study. The decision on
acceptance belongs to the human reviewer.
