# Cross-check: `reconstruction.md` against the paper

RUN-TAG: XM-CROSS-368sextets__flip_charge

Paper: *The phenomenological cornucopia of SU(3) exotica* (Carpenter, Murphy, Tait),
`paper.tex` in the sandbox.

## 1. Where the paper defines the model

The paper gives the model in Section III (`\label{s3}`), not in the operator catalog of
Section II. The definitions are:

- **Eq. `\label{sFmodel}`** (the fermion models, `paper.tex` lines 857-859), for
  `q` in `{u,d}`:

  L ⊃ Ψ̄_q(i D̸ − m_{Ψ_q})Ψ_q
  + (1/Λ_{Ψ_q})[κ_q^I **J**^{s ia} (q̄^c_R)_{Ii} σ^{μν} Ψ_{qs} G_{μν a} + H.c.]
  + (1/Λ³_{Ψ_qB})[κ_{qB}^I **J**^{s ia} (q̄^c_R)_{Ii} Ψ_{qs} B^{μν} G_{μν a} + H.c.]

- **Eq. `\label{sSmodel}`** (the scalar models, lines 861-862):

  L ⊃ (D_μΦ_q)† D^μΦ_q − m²_{Φ_q} Φ_q†Φ_q
  + (1/Λ²_{Φ_q})[λ_q^{XI} **J**^{s ia} Φ_{qs} (q̄^c_R)_{Ii} σ^{μν} ℓ_{RX} G_{μν a} + H.c.]

- **Table X** (`\label{fields}`, lines 1142-1162) gives the quantum numbers of the four new
  fields under G_SM = SU(3)_c x SU(2)_L x U(1)_Y, and their lepton number L.

- **Table IX** (`\label{t9}`, lines 820-843) is the parent operator list for the invariant
  **3** ⊗ **6** ⊗ **8**, with the same couplings, cutoff powers, L and Y.

- **Appendix A**, Eq. `\label{Jdef}` and Eq. `\label{A18}`, defines the Clebsch-Gordan
  tensor **J**^{s ia} = −i√2 **L**^{ijk} [t_3^a]_j^l **K̄**^s_{lk}, with the footnote
  √2 **L**^{ijk} = ε^{ijk}. So **J**^{s ia} = −i ε^{ijk} [t_3^a]_j^l **K̄**^s_{lk}.
  Eq. `\label{Kdef}` gives **K**, Eq. `\label{A16}` gives the normalization
  tr **K**_s **K̄**^t = δ_s^t and tr **J**_s **J̄**^t = δ_s^t.

- **Benchmark values**: lines 1184, 1191 and 1197 give κ_u^I = κ_d^I = 0.05,
  κ_{uB}^I = 0.10 (both for I in {1,2}), λ_{u,d}^{XI} = 0.1 δ^{XI}, and all cutoffs
  Λ = 1 TeV.

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| Ψ̄_u(i D̸ − m_{Ψ_u})Ψ_u — Eq. (sFmodel), line 1 | §1.1 `LPsiuFree` | agree | Dirac sextet, SU(2)_L singlet. D_μ carries the sextet generator t_6 and the hypercharge. Kinetic and mass signs match. |
| Ψ̄_d(i D̸ − m_{Ψ_d})Ψ_d — Eq. (sFmodel), line 1 | §1.2 `LPsidFree` | agree | Same structure, Y = +1/3 as in Table X. |
| (D_μΦ_u)† D^μΦ_u − m²_{Φ_u} Φ_u†Φ_u — Eq. (sSmodel), line 1 | §1.3 `LPhiuFree` | agree | Operator structure matches. The hypercharge inside D_μ does not match; see the Φ_u row below. |
| (D_μΦ_d)† D^μΦ_d − m²_{Φ_d} Φ_d†Φ_d — Eq. (sSmodel), line 1 | §1.4 `LPhidFree` | agree | |
| (κ_u^I/Λ_{Ψ_u}) **J**^{s ia}(ū^c_R)_{Ii} σ^{μν} Ψ_{us} G_{μν a} + H.c. — Eq. (sFmodel), line 2 | §1.5 `LPsiuG` | agree | The reconstruction's −i ε_{ijk}(T^a)_{jl}(K^s)*_{lk} is exactly **J**^{s ia} of Eq. (A18) with √2 **L** = ε. P_R selects u_R and Ψ_{u,R}, as the paper's q̄^c_R and σ^{μν} do. One coupling index = quark generation. Cutoff power 1. |
| (κ_d^I/Λ_{Ψ_d}) **J**^{s ia}(d̄^c_R)_{Ii} σ^{μν} Ψ_{ds} G_{μν a} + H.c. — Eq. (sFmodel), line 2 | §1.6 `LPsidG` | agree | |
| (κ_{uB}^I/Λ³_{Ψ_uB}) **J**^{s ia}(ū^c_R)_{Ii} Ψ_{us} B^{μν}G_{μν a} + H.c. — Eq. (sFmodel), line 3 | §1.7 `LPsiuB` | agree | Scalar bilinear, no σ^{μν}. The two Lorentz indices join B and G. The explicit P_R is redundant but harmless, because the paper's q̄^c_R already fixes the chirality. Cutoff power 3. |
| (κ_{dB}^I/Λ³_{Ψ_dB}) **J**^{s ia}(d̄^c_R)_{Ii} Ψ_{ds} B^{μν}G_{μν a} + H.c. — Eq. (sFmodel), line 3 | §1.8 `LPsidB` | agree | |
| (λ_u^{XI}/Λ²_{Φ_u}) **J**^{s ia} Φ_{us}(ū^c_R)_{Ii} σ^{μν} ℓ_{RX} G_{μν a} + H.c. — Eq. (sSmodel), line 2 | §1.9 `LPhiuG` | agree | Φ enters unconjugated, as in the paper. Index order of λ (lepton X first, quark I second) matches `lamu[x,f]`. Cutoff power 2. |
| (λ_d^{XI}/Λ²_{Φ_d}) **J**^{s ia} Φ_{ds}(d̄^c_R)_{Ii} σ^{μν} ℓ_{RX} G_{μν a} + H.c. — Eq. (sSmodel), line 2 | §1.10 `LPhidG` | agree | |
| Φ_u ~ (**6**, **1**, +1/3), L = −1 — Table X | Φ_u: colour **6**, SU(2) singlet, Q = +1/3, **Y = −1/3**, L = −1 | **disagree** | The paper fixes Y_{Φ_u} = +1/3. The reconstruction reports Y = −1/3 in the file, with Q = +1/3. The sign of Y is opposite to the paper. |
| Φ_d ~ (**6**, **1**, +4/3), L = −1 — Table X | Φ_d: colour **6**, SU(2) singlet, Q = Y = +4/3, L = −1 | agree | |
| Ψ_u ~ (**6**, **1**, −2/3), L = 0 — Table X | Ψ_u: colour **6**, SU(2) singlet, Q = Y = −2/3, L = 0 | agree | |
| Ψ_d ~ (**6**, **1**, +1/3), L = 0 — Table X | Ψ_d: colour **6**, SU(2) singlet, Q = Y = +1/3, L = 0 | agree | |
| Sextet of SU(3)_c for all four new fields; complex scalars and Dirac fermions — Table X, Eq. (sextet_numbers) | `AddGaugeRepresentation[SU3C -> {T6, Sextet}]`, `SelfConjugate -> False` | agree | |
| Λ_{Ψ_q}, Λ_{Ψ_qB}, Λ_{Φ_q} with powers 1, 3, 2 — Eqs. (sFmodel), (sSmodel), Table IX | `LamPsu`, `LamPsd`, `LamPsuB`, `LamPsdB`, `LamPhu`, `LamPhd` | agree | Six independent cutoffs, correct power for each operator. |
| **K** normalization tr **K**_s **K̄**^t = δ; t_6 from **K** — Eqs. (Kdef), (A16), line 1361 | §0 relations for `K6`/`K6bar` and (T_6^a)_{st} = 2(K^s)*(T^a)K^t | agree | Same content. The reconstruction puts the conjugation on the first **K** and the paper puts it on the second; this is only index height. |
| κ_u^I = κ_d^I = 0.05, κ_{uB}^I = 0.10 for I in {1,2}; Λ = 1 TeV — lines 1184, 1191 | `kapu`, `kapd` = 0.05 and `kapuB`, `kapdB` = 0.10 for three generations; all Λ = 1000 GeV | agree | The paper states the benchmark for the first two generations only. See the third-generation item below. |
| λ_{u,d}^{XI} = 0.1 δ^{XI}, Λ_Φ = 1 TeV — line 1197 | `lamu`, `lamd` diagonal 0.1 | agree | |
| third-generation couplings κ_q^3, κ_{qB}^3 — only implied by the branching fractions in the footnote at line 1211 | `kapu[3] = 0.05`, `kapuB[3] = 0.10` | extra-in-reconstruction | The paper's footnote quotes BF(Ψ_u → t̄ g) ≈ 0.21, so a non-zero third-generation coupling is consistent, but no value is printed. |
| sextet masses (scanned in Figures 2-6) | `MPHU` = `MPHD` = `MPSU` = `MPSD` = 1000 GeV | extra-in-reconstruction | The paper treats the mass as a free variable, not a fixed number. |
| widths (not given in the paper) | `WPHU` = `WPHD` = `WPSU` = `WPSD` = 10 GeV | extra-in-reconstruction | Implementation placeholder. |
| PDG codes (not given in the paper) | 9000001, 9000002, 9000011, 9000012 | extra-in-reconstruction | Implementation detail. |
| baryon number (not assigned in the paper) | B = −1/3 for all four fields, marked as implied | extra-in-reconstruction | The value is consistent with the operators, but the paper assigns only L and Y. |

Two more points on completeness:

- Nothing in Eqs. (sFmodel) and (sSmodel) is absent from the reconstruction. All ten pieces
  (four free terms plus six interactions) are present, for both the up-type and the
  down-type field.
- Table IX also lists the operators (q̄^c_R σ^{μν} q_R)-type with `|H|²` and the
  (L̄_L H σ^{μν} q_R)Φ G operator. The paper does not put them in Eqs. (sFmodel) and
  (sSmodel), so their absence from the reconstruction is correct, not a gap.

## 3. Disagreements

1. **Hypercharge of Φ_u. Severity: substantive.**
   Table X of the paper gives Φ_u ~ (**6**, **1**, +1/3). The reconstruction reports the
   implementation file declaring Y = −1/3 together with Q = +1/3. The reconstruction
   detects the internal inconsistency by itself and argues from charge conservation in
   `LPhiuG` that Q = +1/3 is right, so it concludes the declared Y has the wrong sign. The
   paper confirms that conclusion. A human should open the field declaration for `Phiu`,
   compare `Y -> -1/3` with Table X, and decide whether the file or the reconstruction
   introduced the sign. The effect is physical, not cosmetic: Y enters the covariant
   derivative in `LPhiuFree`, so the Φ_u coupling to B_μ (and thus to the photon and the Z)
   gets the wrong sign. Note that Φ_u pair production is dominated by QCD, so a cross-check
   of the total rate may hide this defect; the check must be made on the declaration or on
   a Φ_u Z / Φ_u γ vertex.

2. **Third-generation coupling values. Severity: cosmetic.**
   The reconstruction reports κ and κ_B for three generations; the paper writes the
   benchmark for I in {1,2} only. A human should confirm that a flavour-universal value
   over three generations is the intended benchmark, using the branching fractions in the
   footnote at line 1211.

3. **Fixed masses and widths. Severity: convention.**
   The file fixes 1000 GeV and 10 GeV; the paper scans the mass and never states a width. A
   human should treat these as run-card defaults, not as model predictions.

4. **Description of the −i factor. Severity: cosmetic.**
   The reconstruction calls the explicit −i in every interaction "a phase convention". It
   is in fact the exact factor that turns ε(T)(K*) into the paper's **J**^{s ia}, per
   Eq. (A18). A human should keep the factor, and should not remove it as an arbitrary
   phase.

5. **Prose on the decay final state. Severity: cosmetic.**
   The reconstruction's summary says "q g → Ψ with Ψ → q g". The paper is more precise:
   q g fusion makes the conjugate state Ψ̄_q, and Ψ_u decays to an antiquark and a gluon
   (BF(Ψ_u → ū g) ≈ 0.26). The Lagrangian in the reconstruction is consistent with the
   paper; only the summary text is loose.

## 4. Overall assessment

The reconstruction reproduces the model of Eqs. (sFmodel) and (sSmodel) closely. All ten
Lagrangian pieces are present with the correct field representations, the correct
chirality (right-handed quark, charge-conjugated, with a right-handed lepton or sextet
partner), the correct colour tensor, and the correct cutoff power for each operator
dimension. The colour structure −i ε(T)(K*) is exactly the paper's new Clebsch-Gordan
tensor **J**^{s ia}, including the √2 that the paper hides in **L**^{ijk}, and the
coupling index orders match Table IX. The benchmark numbers for κ, κ_B and λ agree with
Section III.A. The one physics mismatch is the weak hypercharge of the sextet scalar Φ_u:
the paper fixes Y = +1/3, while the file, as read by the reconstruction, declares
Y = −1/3 next to Q = +1/3. The reconstruction flags this by itself and reasons correctly
from electric-charge conservation, so the analysis is sound even where the source file
appears not to be. The remaining differences are implementation data that the paper never
fixes (masses, widths, PDG codes, baryon number) or loose wording in the summary. A human
reviewer should focus on the Φ_u declaration, decide whether the sign comes from the model
file or from the reconstruction, and confirm the third-generation benchmark values.
