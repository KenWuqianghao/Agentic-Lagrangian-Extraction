# Cross-check: `reconstruction.md` against the paper

RUN-TAG: XM-CROSS-331__sqrt_swap

Paper: *Collider Phenomenology of the 3-3-1 Model*, Qing-Hong Cao and Dong-Ming Zhang.
Gauge group `SU(3)_C x SU(3)_L x U(1)_X`.

## 1. Where the paper defines the model

The paper writes the model in Sec. 2 ("The Model"). The parts that matter here are:

| Content | Place in the paper |
| --- | --- |
| Scalar triplets `rho`, `eta`, `chi` and their charges `Q_Y`, `Q_V` | Sec. 2.1, eq. labelled (1); `X` charges in eq. (xqn) |
| Higgs Lagrangian and full potential `V_Higgs` | Sec. 2.1, eq. (VHiggs) |
| Charge generator `Q = T3 + beta*T8 + X`, hypercharge `Y = beta*T8 + X` | Sec. 2.1 |
| Neutral-scalar mass matrix and eigenvalues `m_h`, `M_H2`, `M_H3`, `M_H0` | Sec. 2.1.1; repeated in Sec. 2.6, eqs. (4) and (5) |
| Charged-scalar mass matrices and eigenvalues `M_Hpm`, `M_H^{QY}`, `M_H^{QV}` | Sec. 2.1.2; repeated in Sec. 2.6 |
| Gauge Lagrangian, `G_mu` matrix, gauge-boson masses | Sec. 2.2, eqs. (gaugemass), (Gmu), (gauge mass), (MVY), (3) |
| `Z'` definition, `s_331`, `c_331`, `g_Y`, `M_Z'` | Sec. 2.2, eqs. (ZP), (B) and the two lines after them |
| Fermion Lagrangian, covariant derivative, triplets and anti-triplets | Sec. 2.3 |
| Charges of `D`, `S`, `T`, `E_l` | Sec. 2.3 and Table `tbl:charge` |
| Yukawa Lagrangian | Sec. 2.4 |
| Residual `Z_2` symmetry and dark-matter candidates | Sec. 2.5 |
| All vertices in unitary gauge | Appendix A, Tables `1gauge-2scalars`, `2gauges-1scalar`, `2gauges-2scalars`, `gauges`, `gauge-fermion`, `scalar-fermion` |
| Scalar mixing matrices `U` and `O` | Sec. 2.1.1 and Appendix B |

The reconstruction reproduces one benchmark of the paper: `beta = +1/sqrt(3)`.
The declared charges (`Q_D = Q_S = -1/3`, `Q_T = +2/3`, `Q_E = 0`, `Q_Y = +1`, `Q_V = 0`)
are exactly the `beta = +1/sqrt(3)` column of Table `tbl:charge`.

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| Free `Z'` field from `L_Gauge` (Sec. 2.2) | `L_Zp = -1/4 Z'_{mu nu} Z'^{mu nu} + 1/2 M_Zp^2 Z'^2` | agree | Real (self-conjugate) Proca field. The factors 1/4 and 1/2 are correct. |
| Free `Y^{+Q_Y}` field (Sec. 2.2) | `L_Yp = -1/2 Y'^dag_{mu nu} Y'^{mu nu} + M_Yp^2 Y'^dag Y'` | agree | Correct normalisation for a complex vector. |
| Free `V^{+Q_V}` field (Sec. 2.2) | `L_Vp`, complex, `Q = 0` | agree | The paper keeps `V` and its antiparticle distinct at `beta = +1/sqrt(3)`; `V` is a dark-matter candidate (Sec. 2.5). `SelfConjugate -> False` is correct. |
| `M_W^2 = g^2 v^2/4`, `M_Y^2 = g^2 (v3^2+v2^2)/4`, `M_V^2 = g^2 (v3^2+v1^2)/4` (eq. MVY) | `MYp = Sqrt[gw^2 (v3^2+v2^2)/4]`, `MVp = Sqrt[gw^2 (v3^2+v1^2)/4]` | agree | Same formulas. |
| `M_Z'^2 = (g^2 + beta^2 g_X^2) v3^2 / 3`, equal to `c_W^2 g^2 v3^2 / (3 a_0^2)` (Sec. 2.2 and eq. (3)) | `MZp = Sqrt[(gw^2 + beta^2 gX^2) v3^2 / 6]` | **disagree** | The paper's term is `L = (1/6)(g^2+beta^2 g_X^2) v3^2 Z'^2`. For a real vector this term equals `(1/2) M^2 Z'^2`, so `M^2 = (...) v3^2/3`. The file divides by 6. `M_Z'` is too small by `sqrt(2)`. |
| `g_X` fixed by `g_Y = g g_X / sqrt(g^2+beta^2 g_X^2)` (Sec. 2.2) | `gX` external input, `gX = 0.5` | **disagree** | In the paper `g_X` is not free. With `s_W^2 = 0.2312` and `beta = 1/sqrt(3)`, the paper's relation gives `g_X = 0.38`. |
| `beta` sets every new charge (Sec. 2.3, Table `tbl:charge`) | `beta` external input; charges declared as fixed numbers | **disagree** | `beta` enters only `MZp`. A different input `beta` would not change the charges, so the file is valid for `beta = +1/sqrt(3)` only. |
| `Q = T3 + beta T8 + X` and `Y = beta T8 + X` (Sec. 2.1) | `Q = T3 + Y`, all new states `SU(2)_L` singlets, so `Q = Y` | agree | Correct for the heavy states, which all sit in the third component of a triplet or anti-triplet. |
| Three scalar triplets `rho`, `eta`, `chi` (eq. (1)) | Not present; only mass eigenstates | missing-in-reconstruction | The file is a mass-eigenstate model, so the triplet structure is not kept. |
| Potential `V_Higgs` with `mu_i`, `lambda_1,2,3`, `lambda_12,13,23`, `lambda'_12,13,23`, `f` (eq. VHiggs) | No potential. Only `f`, `lam3`, `lampr12`, `lampr23`, `lampr13` as mass inputs | missing-in-reconstruction | No scalar self-interaction of any kind is implemented. |
| `f = k v3`, `k ~ O(1)` (Sec. 2.1) | `f = k*v3`, `k = 1` | agree | |
| `v = sqrt(v1^2 + v2^2) = 246 GeV` (Sec. 2.1.1) | `v2 = 1/Sqrt[vev^2 - v1^2]` | **disagree** | The paper needs `v2 = Sqrt[vev^2 - v1^2]`. The file takes the reciprocal. The value becomes `0.0057 GeV^-1` in place of `174.2 GeV`. |
| `m_h^2 = 2(lambda_1 v1^4 + lambda_12 v1^2 v2^2 + lambda_2 v2^4)/v^2` (eq. (4)) | Not implemented | missing-in-reconstruction | The 125 GeV scalar stays the unmodified base-SM Higgs. |
| `M_H2^2 = (v^2/(v1 v2)) f v3` (eq. (4)) | `MH2 = Sqrt[(vev^2/(v1 v2)) f v3]` | agree | Same formula. The number is wrong only through `v2`. |
| `M_H3^2 = 2 lambda_3 v3^2` (eq. (5)) | `MH3 = Sqrt[2 lam3 v3^2]` | agree | |
| `M_H0^2 = (v1 v2/v3 + v1 v3/v2 + v2 v3/v1) f` (Sec. 2.6) | `MH0` | agree | Same formula. |
| `M_Hpm^2 = (2 f v3 + lambda'_12 v1 v2) v^2/(2 v1 v2)` (Sec. 2.1.2) | `MHpm` | agree | |
| `M_H^{QY}^2 = (2 f v1 + lambda'_23 v2 v3)(v2^2+v3^2)/(2 v2 v3)` | `MHQY` | agree | |
| `M_H^{QV}^2 = (2 f v2 + lambda'_13 v1 v3)(v1^2+v3^2)/(2 v1 v3)` | `MHQV` | agree | |
| Goldstone bosons `G_Z`, `G_Z'`, `G^pm`, `G^{pm Q_Y}`, `G^{pm Q_V}` (Sec. 2.1.1, 2.1.2) | Absent | agree | The paper's Appendix A also works in unitary gauge. |
| Mixing matrices `U` (eq. (U)) and `O` (Appendix B) | Absent | missing-in-reconstruction | Without `U` and `O` no scalar couples to the SM sector. |
| `H^pm` is a mix of `eta^pm` and `rho^pm`, i.e. of `SU(2)_L` doublet components (Sec. 2.1.2) | `Hpm` declared as an `SU(2)_L` singlet with `Y = +1` | **disagree** | The photon coupling comes out right (`i e (p1-p2)`), but the `Z H^+ H^-` coupling does not. The paper gives `i e (c_W^2-s_W^2)/(2 c_W s_W)`; a `Y=1` singlet gives `-e s_W/c_W`. |
| `H^{pm Q_Y}` and `H^{pm Q_V}` are mostly the third components of `eta` and `rho` (eqs. sc23, sc13) | `HQY` singlet `Y=+1`, `HQV` singlet `Y=0` | agree | In the decoupling limit `s23, s13 -> 1`, so both are singlets. This reproduces the paper's `A` and `Z` couplings for these states. |
| `W W H_2`, `Z Z H_2`, `W W H_3`, `Z Z H_3` and all other `VVS` vertices (Table `2gauges-1scalar`) | None. `H2`, `H3`, `H0` are inert real singlets | missing-in-reconstruction | The new neutral scalars have no interaction at all in the file. |
| All `VSS` and `VVSS` vertices (Tables `1gauge-2scalars`, `2gauges-2scalars`) | Absent | missing-in-reconstruction | |
| Gauge self-couplings `A V V`, `Z V V`, `Z' V V`, `W Y V`, and the four-point set (Table `gauges`) | Absent. `Zp`, `Yp`, `Vp` are hand-made Proca fields | missing-in-reconstruction | The paper produces `VV` and `YY` pairs mainly through these vertices (Sec. 5.1). |
| Quark triplets `q_1L = (u,d,D)`, `q_2L = (c,s,S)` (Sec. 2.3) | `D`, `S` as colour-triplet Dirac fields with `Q = -1/3` | agree | Charges match the `beta = +1/sqrt(3)` column of Table `tbl:charge`. |
| Quark anti-triplet `q_3L = (b,-t,T)` (Sec. 2.3) | `T` as a colour-triplet Dirac field with `Q = +2/3` | agree | The charge is right. The anti-triplet structure is not kept; see the `T` current row below. |
| Lepton anti-triplets `l_iL = (l, -nu_l, E_l)` (Sec. 2.3), `Q_E = 0` | `EL = {Ee, Emu, Etau}`, gauge singlets, `Q = 0`, diagonal masses | agree | The charge matches the `beta = +1/sqrt(3)` column. |
| `L_Fermion = psi-bar i D_mu gamma^mu psi` for `D`, `S`, `T`, `E` (Sec. 2.3) | `LDQ`, `LSQ`, `LTQ`, `LEL` with QCD and hypercharge only | agree | A singlet with `Y = Q` gives exactly the `A` and `Z` rows of Table `gauge-fermion` for `D`, `S`, `T` and `E_l`. |
| Heavy-fermion masses from `y^J q-bar chi J_R` and `y^E l-bar chi* E_R` (Sec. 2.4) | Explicit Dirac masses `MDQ`, `MSQ`, `MTQ`, `MEE`, `MEM`, `MET`, all 1000 GeV | agree | The paper states the heavy masses are free (Sec. 2.6). A vector-like Dirac mass is the correct mass-basis form. |
| Full Yukawa Lagrangian `L_Yuk` (Sec. 2.4) | Absent | missing-in-reconstruction | No Yukawa coupling of any kind is implemented. |
| `(g/sqrt 2) u-bar gamma^mu P_L D Y_mu` and `(g/sqrt 2) c-bar gamma^mu P_L S Y_mu` (eq. (Gmu); Table `gauge-fermion`; Sec. 6.1) | First two terms of `LNPcc` | agree | The paper confirms the strength `g/sqrt(2)` in Sec. 6.1 and gives `g_R = 0`, so the current is purely left-handed. |
| `(g/sqrt 2) V_ud d-bar gamma^mu P_L D V_mu` and `(g/sqrt 2) V_cs s-bar gamma^mu P_L S V_mu` (Table `gauge-fermion`) | Last two terms of `LNPcc`, without any CKM element | **disagree** | The paper puts `V_ud` and `V_cs` on the down-type current. The file uses 1. |
| `t-bar T V^{+Q_V}` and `T-bar b Y^{-Q_Y}`, both `g/sqrt(2)`, `P_L` (Table `gauge-fermion`; Sec. 6.2) | Absent | missing-in-reconstruction | `T` has no non-QCD interaction in the file, so `T -> tV` and `T -> bY` cannot be produced. |
| `l-bar E_l Y^{+Q_Y}` and `nu-bar E_l V^{+Q_V}`, both `g/sqrt(2)`, `P_L` (Table `gauge-fermion`) | Absent | missing-in-reconstruction | The heavy leptons are inert in the file. |
| `Z'` couplings to every SM and heavy fermion, `g_L` and `g_R` (eq. eq:effcoup; Table `gauge-fermion`) | Absent | missing-in-reconstruction | The whole `Z'` phenomenology of Sec. 4 rests on these couplings. |
| Scalar-fermion couplings (Table `scalar-fermion`) | Absent | missing-in-reconstruction | |
| `Z`-`Z'` mixing matrix `M_NG` (Sec. 2.2) | Absent | agree | The paper drops this mixing on purpose (Sec. 1). |
| Residual `Z_2` / `U(1)_G` symmetry (Sec. 2.5) | Not declared. The reconstruction infers a hidden conserved charge for `Vp` and `HQV` | agree | This inference matches the paper's residual symmetry. |
| — | PDG codes 4000001-4000015 and a default width of 1 GeV per state | extra-in-reconstruction | Bookkeeping only. |
| — | `M$InteractionOrderHierarchy` with the new order `NP` | extra-in-reconstruction | Bookkeeping only. |

## 3. Disagreements, with severity

1. **`v2 = 1/Sqrt[vev^2 - v1^2]` — substantive.**
   Check the sign of the exponent in the `v2` definition: the paper needs
   `v2 = Sqrt[vev^2 - v1^2]`, so that `v1^2 + v2^2 = v^2` and `M_W` comes out right.
   The present form has mass dimension `-1` and pushes `MH2`, `MH0`, `MHpm` and
   `MHQY` up by two orders of magnitude.

2. **`M_Zp^2` divided by 6 in place of 3 — substantive.**
   Check the factor against Sec. 2.2: the paper's mass term is
   `(1/6)(g^2 + beta^2 g_X^2) v3^2 Z'^2`, which for a real vector means
   `M_Z'^2 = (g^2 + beta^2 g_X^2) v3^2 / 3`, in agreement with eq. (3).

3. **`gX` used as a free input — substantive.**
   Check whether `gX = 0.5` is compatible with the base SM `g1` and `gw`: the paper
   fixes `g_X` through `g_Y = g g_X / sqrt(g^2 + beta^2 g_X^2)`, which gives about 0.38.

4. **`beta` is an input, but the charges are hard-coded — substantive.**
   Check that nobody changes `beta` alone: the file is only valid for
   `beta = +1/sqrt(3)`, because every `Q` in the particle classes is a fixed number.

5. **`Hpm` declared as an `SU(2)_L` singlet — substantive.**
   Check the `Z H^+ H^-` vertex against Table `1gauge-2scalars`: `H^pm` comes from the
   doublet parts of `rho` and `eta`, so `T3 = -/+ 1/2`, not 0.

6. **No CKM element on the `d-D` and `s-S` currents — convention.**
   Check whether the missing `V_ud` and `V_cs` of Table `gauge-fermion` matter for the
   intended use; the numerical effect is about 3 percent in the rate.

7. **No `Z'` couplings to fermions — substantive (missing).**
   Check whether the base SM file supplies them; if not, `Z'` production and decay,
   the whole of Sec. 4, cannot be simulated.

8. **No `T` and no `E_l` currents — substantive (missing).**
   Check Table `gauge-fermion`: the paper couples `T` to `t` and `b`, and each `E_l`
   to its own `l` and `nu_l`, all with `g/sqrt(2)` and `P_L`.

9. **No scalar sector dynamics — substantive (missing).**
   Check whether the potential, the mixing matrices `U` and `O`, the `VSS`, `VVS`,
   `VVSS` and scalar-fermion tables are meant to live in a separate file; without them
   the six new scalars are inert.

10. **No gauge self-couplings for `Zp`, `Yp`, `Vp` — substantive (missing).**
    Check Table `gauges`: pair production of `V` and `Y` in Sec. 5.1 needs
    `A/Z/Z'-V-V` and `W-Y-V` vertices, which hand-made Proca fields cannot have.

11. **`EL` named "Heavy charged lepton" while `Q -> 0` — cosmetic.**
    Check the string only; the charge 0 is correct for `beta = +1/sqrt(3)`.

12. **`MH2` written with `vev` where the paper writes `v^2 = v1^2 + v2^2` — cosmetic.**
    Check that `vev` in the base SM file is 246 GeV; then the two forms agree once
    item 1 is fixed.

13. **PDG codes, 1 GeV default widths, `NP` interaction order — cosmetic.**
    Check nothing in the paper; these are implementation bookkeeping.

## 4. Overall assessment

The reconstruction and the paper describe the same model and the same benchmark. Every
electric charge, every colour assignment, the chirality and the strength `g/sqrt(2)` of
the one implemented new current, and seven of the eight heavy-state mass formulas match
the paper term by term, including the less obvious points: the complex but neutral `V'`,
the vector-like Dirac masses of the exotic quarks, and the `Y = Q` singlet treatment of
`D`, `S`, `T` and `E_l`, which reproduces the paper's photon and `Z` couplings exactly.
Two numerical relations do not match: the `v2` definition is the reciprocal of the
paper's value, and `M_Z'^2` carries a factor 1/6 where the paper's mass term gives 1/3.
Both are single-symbol differences with large numerical effect, and the reconstruction
itself flags the first one. Beyond that, the file is a small subset of the paper: it
implements the new states, their gauge-covariant kinetic terms and one charged current,
but it leaves out the scalar potential, the Yukawa sector, the scalar mixing matrices,
the `Z'` couplings to fermions, the third-generation and lepton currents, and all gauge
self-couplings. Whether that subset is the intended scope, or a loss against the paper,
is the judgement a human reviewer must make, together with the two numerical items.
