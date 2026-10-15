# Cross-check: reconstruction of `sanitized.fr` against the paper

**Paper:** L. M. Carpenter, T. Murphy, T. M. P. Tait, *The phenomenological cornucopia of SU(3) exotica*, preprint UCI-HEP-TR-2021-26.

**Reconstruction under test:** `reconstruction.md`, an independent read of an unseen FeynRules file.

---

## 1. Where the paper defines the model

The paper has two parts. Section II builds a general catalog of colour-sextet operators. Section III picks a small subset of that catalog and makes a concrete model. Only Section III is a Lagrangian. The comparison below uses Section III.

| Item | Location in the paper |
| --- | --- |
| Sextet fermion model Lagrangian | Eq. `\label{sFmodel}`, Section III, three lines: kinetic/mass, dipole with `G`, dipole with `G`·`B` |
| Sextet scalar model Lagrangian | Eq. `\label{sSmodel}`, Section III, two lines: kinetic/mass, lepton-quark-gluon dipole |
| Field content and quantum numbers | Table X (`\label{fields}`), Section III |
| Parent operator list for both models | Table IX (`\label{t9}`), invariant **3** ⊗ **6** ⊗ **8** |
| Colour tensor **J**<sup>s ia</sup>, definition | Table I (`\label{t1}`); explicit values eq. `\label{Jdef}`; normalisation eq. `\label{A16}` |
| Colour tensor built from **K**, **t**<sub>3</sub>, **L** for FeynRules | Eq. `\label{A18}` and the text after it, Appendix A |
| Sextet generators **t**<sub>6</sub><sup>a</sup> | Eq. `\label{gen6}`, Appendix A |
| Representation products (**6** ⊗ **3** = **8** ⊕ **10**, **3** ⊗ **8** = **3** ⊕ **6bar** ⊕ **15**) | Eq. `\label{decomp}`, Section II; eq. `\label{A1}`, Appendix A |
| Benchmark numbers (couplings, cutoffs) | Section III.A text near Figures 3, 4 and 5 |

The paper writes eq. `sFmodel` and eq. `sSmodel` once for `q ∈ {u,d}`. This gives four new fields in total: two Dirac sextets and two complex scalar sextets.

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| `Psi_q(bar) (i D-slash − m_Psi_q) Psi_q`, line 1 of eq. `sFmodel`, for `q=u` | `LSextetKin`, first term: `Fu(bar)^k (i γ·D − M_Fu) Fu_k` | **agree** | Dirac kinetic term plus explicit Dirac mass. One sextet index, no generation index. |
| Same, for `q=d` | `LSextetKin`, second term with `Fd`, `M_Fd` | **agree** | |
| `(D_mu Phi_q)† D^mu Phi_q − m²_Phi_q Phi_q† Phi_q`, line 1 of eq. `sSmodel`, `q=u` | `LSextetKin`, third term with `Su`, `M_Su` | **agree** | Complex scalar, not self-conjugate. |
| Same, for `q=d` | `LSextetKin`, fourth term with `Sd`, `M_Sd` | **agree** | |
| Covariant derivative acting on a `(6,1,Y)` field | `D_mu = ∂_mu − i g_s G^a T^a_6 − i g_1 Y B_mu` | **agree** | The paper fixes the reps in Table X. The reconstruction reads `T6` and no `SU2W` index, so weak singlet with `Q = Y`. This follows from Table X. |
| `(1/Λ_Psi_u) κ_u^I J^{s ia} (q_R^c(bar)_{Ii} σ^{μν} Psi_{us}) G_{μν a} + H.c.`, line 2 of eq. `sFmodel` | `L_Fu^(σ) = i C_u^m K^a_{k i} Fu(bar)^k σ^{μν} (u_R^c)_m^i G^a_{μν} + h.c.` | **agree** | Same operator. The reconstruction writes the Hermitian-conjugate half explicitly. See disagreement D1 (which half is written) and D2 (the cutoff Λ). Chirality matches: only `P_R Psi` and the charge-conjugated `u_R` take part. |
| `(1/Λ³_Psi_uB) κ_uB^I J^{s ia} (q_R^c(bar)_{Ii} Psi_{us}) B^{μν} G_{μν a} + H.c.`, line 3 of eq. `sFmodel` | `L_Fu^(B) = i C_Bu^m K^a_{k i} Fu(bar)^k (u_R^c)_m^i G^a_{μν} B^{μν} + h.c.` | **agree** | Scalar bilinear, `Γ = 1`, no `σ^{μν}`. Two field strengths. Mass dimension seven, so the coefficient has dimension −3. This matches the paper's `1/Λ³`. |
| Line 2 of eq. `sFmodel` with `q = d` | `L_Fd^(σ)` with `C_d^m`, `Fd`, `d_R^c` | **agree** | |
| Line 3 of eq. `sFmodel` with `q = d` | `L_Fd^(B)` with `C_Bd^m` | **agree** | |
| `(1/Λ²_Phi_u) λ_u^{XI} J^{s ia} Phi_{us} (q_R^c(bar)_{Ii} σ^{μν} ℓ_{R X}) G_{μν a} + H.c.`, line 2 of eq. `sSmodel` | `L_Su = i C_Su^{m ℓ} K^a_{k i} Su†^k l_R(bar)_ℓ σ^{μν} (u_R^c)_m^i G^a_{μν} + h.c.` | **agree** | Same operator. Both fermions are `SU(2)` singlets. The reconstruction writes the conjugate half (`Phi†` and the reversed bilinear). See D1 and D3. Mass dimension six, coefficient dimension −2, which matches `1/Λ²`. |
| Line 2 of eq. `sSmodel` with `q = d` | `L_Sd` with `C_Sd^{m ℓ}`, `Sd†`, `d_R^c` | **agree** | |
| `Psi_u ~ (6, 1, −2/3)`, `L = 0`, Table X | `sFu`: **6**, weak singlet, `Y = −2/3`, no lepton number | **agree** | Hypercharge, colour rep, weak rep and lepton number all match. |
| `Psi_d ~ (6, 1, +1/3)`, `L = 0`, Table X | `sFd`: **6**, weak singlet, `Y = +1/3`, no lepton number | **agree** | |
| `Phi_u ~ (6, 1, +1/3)`, `L = −1`, Table X | `sSu`: **6**, weak singlet, `Y = +1/3`, `LeptonNumber = −1` | **agree** | |
| `Phi_d ~ (6, 1, +4/3)`, `L = −1`, Table X | `sSd`: **6**, weak singlet, `Y = +4/3`, `LeptonNumber = −1` | **agree** | |
| `J(bar)_{s ai} = i √2 K_s^{kl} [t_3^a]_l^j L(bar)_{ijk}`, eq. `A18` | `K^a_{k i} = √2 (K6)_k^{yz} (T^a)_z^x (K3bar)_{i xy}`, with an explicit `i` in each Lagrangian term | **agree** | Same index topology, same `√2`, same factor `i`. This is exactly the construction the paper describes in Appendix A: FeynRules cannot hold `J` directly, so `J` is rebuilt from the hard-coded `K` and `L` objects and one `t_3^a`. See D4 for the normalisation of the `L`-type object. |
| `J^{s ia} = −i √2 L^{ijk} [t_3^a]_j^l K(bar)^s_{lk}`, eq. `A18` | conjugate tensor `(K^a_{k i})* = √2 (K3)_i^{xy} (T^a)_x^z (K6bar)^k_{zy}`; file writes the conjugate half with `−i √2 C*` | **agree** | The relative sign between the two halves matches Hermitian conjugation. |
| `t_3^a = λ^a / 2`, Gell-Mann basis, Appendix A | FeynRules `T[a,i,j]` used for `T^a` | **agree** | Same basis and same normalisation. |
| `t_6^a` given explicitly in eq. `gen6` | `Tr(T_6^a T_6^b) = (5/2) δ^{ab}` | **agree** | The trace of the paper's explicit `t_6^7` is `5/2`. The claim is correct. |
| `6 ⊗ 3 = 8 ⊕ 10`, eq. `decomp`; `3 ⊗ 8 ⊃ 6bar`, eq. `A1` | "6⊗3 holds no colour singlet, so no renormalisable single-quark coupling"; "3⊗8 ⊃ 6bar" | **agree** | The group theory statements match the paper. |
| Couplings `κ_q^I`, `κ_qB^I`, `λ_q^{XI}` are complex matrices in generation space (Table VIII footnote and eq. `FCNCs`, which uses `λ*`) | Six complex internal couplings, each built from a real part and an imaginary part | **agree** | The paper allows complex couplings. The file supports them. |
| Cutoff scales `Λ_Psi_q`, `Λ_Psi_qB`, `Λ_Phi_q` as separate inputs | No `Λ` parameter; one dimensionful Wilson coefficient per operator | **disagree** (see D2) | The file cannot vary `κ` and `Λ` on their own. |
| Benchmark values: `κ_u^I = κ_d^I = 0.05` for `I ∈ {1,2}`, `Λ = 1 TeV`; `κ_uB^I = 0.10`, `Λ_uB = 1 TeV`; `λ_{u,d}^{XI} = 0.1 δ^{XI}`, `Λ = 1 TeV` | All twelve external parameters default to `0.1` (real part) and `0` (imaginary part), for every generation entry | **disagree** (see D5) | Benchmark inputs only. The operator content is not affected. |
| Sextet mass `m_Psi`, `m_Phi` scanned over roughly 0.5-2 TeV in Figures 2-6 | All four masses fixed at `500. GeV`, with widths `WFu = WFd = 4.7740`, `WSu = 4.4108`, `WSd = 4.0647` | **agree** (default choice) | The paper leaves the mass free. `500 GeV` is a valid point inside the scanned range. |
| `M$InteractionOrderHierarchy`, QCD/QED/NP order counting | `{{QCD,1},{QED,2},{NP,2}}`, every new coupling at `{QCD,1}` | **extra-in-reconstruction** (see D6) | The paper says nothing about coupling-order bookkeeping. |
| PDG codes `9000001`-`9000004`, propagator styles | Given in the reconstruction field table | **extra-in-reconstruction** | Implementation detail. No physics content. Harmless. |
| Baryon number of the scalars | Reconstruction infers `B(S_u) = B(S_d) = −1/3` and calls them leptoquark-like | **extra-in-reconstruction** | The paper gives `L` in Table X but never states `B`. The inference is self-consistent with the written operator. |
| `(q Psi) |H|² G` dimension-7 operator, Table IX, row 3 | absent | **agree** (correct omission) | The paper lists this operator in the catalog but leaves it out of eq. `sFmodel`. The file leaves it out too. |
| `(ℓ(bar) q) Phi G` operator, Table IX, scalar row 2 | absent | **agree** (correct omission) | Also catalog-only. Not in eq. `sSmodel`. |
| Operators built on **3** ⊗ **3** ⊗ **6bar** (Table VIII), the "sextet diquark" family | absent | **agree** (correct omission) | Section III uses only the **3** ⊗ **6** ⊗ **8** invariant. The file does the same. |
| Section III treats `q = u` and `q = d` as separate simplified models | One file holds all four fields at once | **agree** (see D7) | No operator mixes the up-type and down-type sectors, so the combined file reproduces both models. |

---

## 3. Disagreements, with severity

**D1. Which half of each interaction is written out.**
Severity: **convention**.
The paper writes `(q_R^c(bar) Γ Psi)` and `Phi_s (q_R^c(bar) σ ℓ_R)`. The reconstruction writes the Hermitian conjugate of each: `Fu(bar) Γ (u_R^c)` and `S† l_R(bar) σ (u_R^c)`. Both add "+ h.c.", so the total Lagrangian is the same. The effect is that the file's coupling is the complex conjugate of the paper's coupling. A human should check the sign of the imaginary part of each coupling before reading any CP-violating result, because the two conventions flip that sign. The default imaginary parts are zero, so no current benchmark number is affected.

**D2. The cutoff scale Λ is absorbed into the coupling.**
Severity: **substantive**.
The paper carries `1/Λ_Psi_q`, `1/Λ³_Psi_qB` and `1/Λ²_Phi_q` as separate, explicit factors, and Figure 6 is drawn in the `(m_Psi_u, Λ_Psi_u)` plane. The file has no `Λ`. It has one coefficient per operator and enters it as the plain number `0.1`, with no unit attached. A human should confirm which unit the implementers meant (`GeV^-1`, `TeV^-1`, or a truly dimensionless placeholder), because a wrong choice rescales every cross section by many orders of magnitude, and because the paper's EFT validity line `m_Psi = 2 Λ_Psi` cannot be drawn at all without `Λ`.

**D3. Index order of the scalar coupling matrix.**
Severity: **convention**.
The paper writes `λ_q^{XI}` with `X` the lepton generation first and `I` the quark generation second. The reconstruction reports `CSu[mm,ll]` with the quark generation first. A human should check the index order in the file against the paper before using any non-diagonal flavour pattern, because a transposed matrix changes which lepton pairs with which quark. The paper's own benchmark is diagonal (`λ = 0.1 δ^{XI}`), so the order does not matter at that point.

**D4. Normalisation of the triplet epsilon object inside the colour tensor.**
Severity: **substantive**.
Eq. `A18` uses `L(bar)_{ijk}`, and the paper's footnote fixes `√2 L(bar)_{ijk} = ε_{ijk}`. The reconstruction only says that the file's `K3bar` is "proportional to" `ε_{ijk}`. If the file's `K3bar` equals `ε` rather than `ε/√2`, every new vertex is larger by `√2` and every cross section is larger by a factor of two. A human should read the FeynRules colour-module definitions of `K3`, `K3bar`, `K6` and `K6bar` and check them against eq. `A16` (`tr J_s J(bar)^t = δ_s^t`).

**D5. Default coupling values do not match the paper's benchmarks.**
Severity: **cosmetic**.
The paper uses `κ_q^I = 0.05` for the plain dipole, `κ_qB^I = 0.10` for the `G·B` operator, and a diagonal `λ^{XI} = 0.1 δ^{XI}` for the scalars, all with `Λ = 1 TeV`, and switches on only the first two quark generations in the single-production figures. The file sets every real part to `0.1` and every imaginary part to `0`, for every generation entry and with no diagonal structure. A human should reset the LHA input values before trying to reproduce any figure in Section III.A.

**D6. Coupling-order assignment is an implementation choice, not a paper statement.**
Severity: **convention**.
The file declares `M$InteractionOrderHierarchy = {{QCD,1},{QED,2},{NP,2}}` and puts every new coupling at `{QCD,1}`. The paper never discusses coupling orders. The new vertices carry a gluon field strength, so `QCD` order 1 is a defensible label, but it is not the paper's. A human should check that MadGraph order selection with this hierarchy gives the diagram set drawn in Figure 1 and does not silently drop or add diagrams.

**D7. Four fields in one file versus two models in the paper.**
Severity: **cosmetic**.
The paper writes eq. `sFmodel` and eq. `sSmodel` once per `q ∈ {u,d}`, and Table X presents four fields. The file holds all four at the same time and gives them the same mass. No operator in either equation couples an up-type sextet to a down-type sextet, so the combined file is equivalent. A human should still confirm that no unintended mixed vertex appears in the generated model output.

---

## 4. Overall assessment

The reconstruction tracks the paper's Section III model closely. Every term in eq. `sFmodel` and eq. `sSmodel` has a matching term in the file, and no term in the file lacks a source in the paper. The four field assignments agree with Table X item by item: colour sextet, weak singlet, `Y = −2/3, +1/3, +1/3, +4/3`, and lepton number `0, 0, −1, −1`. The chirality analysis is right: the charge-conjugated right-handed quark forces the right-handed part of the sextet fermion, and forces the right-handed charged lepton in the scalar operator. The mass dimensions line up with the paper's `1/Λ`, `1/Λ²` and `1/Λ³` factors. Most notably, the reconstruction recovers the exact colour construction that Appendix A describes as a workaround: `J` rebuilt from `K`, one `t_3^a` and the triplet epsilon tensor, with the `√2` and the factor `i` of eq. `A18` both in the right place. The open items are not about which operators exist but about how numbers attach to them. The largest is that the file folds the EFT cutoff into a single Wilson coefficient with no stated unit (D2), which blocks a direct reproduction of any cross section or of the `(m, Λ)` exclusion plot until the intended unit is confirmed. Next is the normalisation of the file's epsilon-type colour object (D4), which is a possible factor of two in every rate. The rest are conventions and default values: the conjugation convention that flips the sign of any CP phase (D1), the quark/lepton index order in the scalar coupling (D3), the benchmark inputs (D5), and the coupling-order hierarchy that the paper never specifies (D6). A human reviewer should settle D2 and D4 first, since both change absolute rates, and should treat D1, D3, D5 and D6 as bookkeeping to confirm rather than as evidence of a different model.
