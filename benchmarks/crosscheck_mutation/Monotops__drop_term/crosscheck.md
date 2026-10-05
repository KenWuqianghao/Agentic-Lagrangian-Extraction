# Cross-check: `reconstruction.md` against "Monotops at the LHC"

**Paper.** J. Andrea, B. Fuks, F. Maltoni, *Monotops at the LHC* (CP3-11-21; IPHC-PHENO-11-03).

**Run tag.** XM-CROSS-Monotops__drop_term

## 1. Where the paper defines the model

- **Section "Effective theory for monotops"**, text at the start of the section: the paper names the
  new states. `$\phi$` (scalar), `$\chi$` (fermion) and `$V$` (vector) are the missing-energy
  particles. `$\varphi$` and `$X$` are scalar and vector fields in the fundamental representation of
  `$SU(3)_c$` that give resonant monotop production. A second heavy scalar `$\tilde\varphi$` is added
  for the four-fermion interactions.
- **Eq. (1), labelled `eq:lag`** (source lines 185-205): the full effective Lagrangian, written in
  terms of mass eigenstates. It has seven new-physics structures plus `$\mathcal{L}_{SM}$`, and one
  global `+ h.c.`
- **Text after Eq. (1)** (source lines 206-220): index conventions, the meaning of each coupling
  matrix, and the flavour symmetry rules that follow from `$\epsilon^{ijk}$`.
- **Section "Model-independent searches"** (source lines 276-297): the benchmark numbers. All axial
  couplings are zero, `$a = 0.1$` for the retained entries, resonance mass 500 GeV, heavy
  four-fermion mass `$M_\varphi = M_{\tilde\varphi} = 3$` TeV, invisible masses 50 GeV and 300 GeV.

The paper gives no kinetic terms, no mass terms and no covariant derivatives for the new fields.
Those parts of the reconstruction have no counterpart in the paper text.

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| `$\mathcal{L}_{SM}$` (Eq. 1, line 186) | base SM model file; `uq`, `dq` taken from it | **agree** | The reconstruction says the file declares no gauge group and uses the base SM model. This matches "in terms of mass eigenstates". |
| `$\phi\,\bar u[a^0_{FC} + b^0_{FC}\gamma_5]u$` (Eq. 1, line 188) | `Lphiu` = `$\phi\,\bar u_{i,a}[a^0_{ij} + b^0_{ij}\gamma^5]u_{j,a}$` | **agree** | Same field content, same coefficient structure, colour-diagonal. `a0FC[1,3] = a0FC[3,1] = 0.1`, `b0FC = 0` match the paper benchmark `$(a^0_{FC})_{13} = (a^0_{FC})_{31} = 0.1$`, `$b = 0$`. |
| `$V_\mu\,\bar u[a^1_{FC}\gamma^\mu + b^1_{FC}\gamma^\mu\gamma_5]u$` (Eq. 1, line 189) | `LVu` = `$V_\mu\,\bar u_{i,a}\gamma^\mu[a^1_{ij} + b^1_{ij}\gamma^5]u_{j,a}$` | **agree** | Same structure. `a1FC[1,3] = a1FC[3,1] = 0.1`, `b1FC = 0` match the paper. |
| `$\epsilon^{ijk}\varphi_i\,\bar d^c_j[a^q_{SR} + b^q_{SR}\gamma_5]d_k$` (Eq. 1, lines 191-192) | `LvphiDiquark` = `$\epsilon_{abc}\varphi_a\,\overline{d^c_{i,b}}[a^q_{ij} + b^q_{ij}\gamma^5]d_{j,c}$ + h.c.` | **agree** | Colour contraction, charge conjugation and coefficient structure all match. The reconstruction derives that `$a^q$` and `$b^q$` are antisymmetric in flavour; the paper states the same result in words ("identical quark couplings to the scalar field `$\varphi$` vanish"). Values `$[1,2] = 0.1$`, `$[2,1] = -0.1$` match `$(a^q_{SR})_{12} = -(a^q_{SR})_{21} = 0.1$`. |
| `$\varphi_i\,\bar u^i[a^{1/2}_{SR} + b^{1/2}_{SR}\gamma_5]\chi$` (Eq. 1, line 193) | `LvphiChi` = `$\varphi_a\,\bar u_{i,a}[a^{1/2}_i + b^{1/2}_i\gamma^5]\chi$ + h.c.` | **agree** | The paper's upper/lower index pair `$\varphi_i\,\bar u^i$` is the `$3\otimes\bar 3\to 1$` contraction that the reconstruction describes. `ahalfSR[3] = 0.1` matches `$(a^{1/2}_{SR})_3 = 0.1$`. |
| `$\epsilon^{ijk}\tilde\varphi_i\,\bar d^c_j[\tilde a^q_{SR} + \tilde b^q_{SR}\gamma_5]u_k$` (Eq. 1, lines 195-196) | `LvphitDiquark` = `$\epsilon_{abc}\tilde\varphi_a\,\overline{d^c_{i,b}}[\tilde a^q_{ij} + \tilde b^q_{ij}\gamma^5]u_{j,c}$ + h.c.` | **agree** | Two different quark fields, so no flavour symmetry rule. The reconstruction says this explicitly and the paper implies it. Values `$[1,3] = [2,3] = 0.1$` match `$(\tilde a^q_{SR})_{\{1,2\}3} = 0.1$`. |
| `$\tilde\varphi_i\,\bar d^i[\tilde a^{1/2}_{SR} + \tilde b^{1/2}_{SR}\gamma_5]\chi$` (Eq. 1, line 197) | `LvphitChi` = `$\tilde\varphi_a\,\bar d_{i,a}[\tilde a^{1/2}_i + \tilde b^{1/2}_i\gamma^5]\chi$ + h.c.` | **agree** | Values `$[1] = [2] = 0.1$` match `$(\tilde a^{1/2}_{SR})_{\{1,2\}} = 0.1$`. |
| `$\epsilon^{ijk}X_{\mu,i}\,\bar d^c_j[a^q_{VR}\gamma^\mu + b^q_{VR}\gamma^\mu\gamma_5]d_k$` (Eq. 1, lines 199-200) | `LXDiquark` = `$\epsilon_{abc}X_{\mu,a}\,\overline{d^c_{i,b}}\gamma^\mu[a^{qV}_{ij} + b^{qV}_{ij}\gamma^5]d_{j,c}$ + h.c.` | **agree** | The reconstruction derives `$a^{qV}$` symmetric and `$b^{qV}$` antisymmetric. The paper states the axial half of the same rule ("so do their axial couplings to the vector field `$X$`"). `aqVR[1,1] = 0.1` matches `$(a^q_{VR})_{11} = 0.1$` and needs the symmetric assignment, so the two agree. |
| **`$X_{\mu,i}\,\bar u^i[a^{1/2}_{VR}\gamma^\mu + b^{1/2}_{VR}\gamma^\mu\gamma_5]\chi$` (Eq. 1, lines 202-203)** | **absent** — `LTotal` has no `$X\!-\!u\!-\!\chi$` piece; `ahalfVR` and `bhalfVR` multiply nothing (§1.7) | **missing-in-reconstruction** | This is the one real physics gap. The reconstruction finds it and reports it, and it even writes the expected form correctly. The paper needs this vertex: it sets `$(a^{1/2}_{VR})_3 = 0.1$` and assumes `$BR(X \to t\chi) = 1$` for scenario II (vector resonant monotop). |
| `+ h.c.` applied to the whole of Eq. (1) (line 204) | h.c. added only to the five coloured-state terms; `Lphiu` and `LVu` carry no `HC` | **disagree** (convention) | The reconstruction handles this by requiring `$a^0$` hermitian, `$b^0$` anti-hermitian, `$a^1$` and `$b^1$` hermitian. The supplied real symmetric values satisfy this, so the physics is the same. The bookkeeping differs from the paper's single global `+ h.c.` |
| flavour indices "understood" (line 208) | explicit generation indices `$i,j$` on every coupling | **agree** | Notation only. |
| colour indices `$i,j,k$` in the fundamental (line 207) | colour indices `$a,b,c$`; all new coloured fields in the **3** | **agree** | Notation only. |
| no kinetic or mass terms given | `Lphikin`, `LVkin`, `Lchikin`, `Lvphikin`, `Lvphitkin`, `LXkin` | **extra-in-reconstruction** | An implementation must have them. They are not in the paper, so the paper cannot confirm the field-strength form, the self-conjugation choices or the mass normalisations. See §3. |
| `$\phi$`, `$V$` neutral missing-energy states (section text, line 171) | `$\phi$` real scalar, `$V$` real Proca vector, both colour singlet and `$Q = 0$` | **agree** | The paper does not say real or complex. Real is the natural reading for an invisible state with a hermitian FCNC current. See §3. |
| `$\chi$` invisible fermion (section text, line 171) | Dirac fermion, colour singlet, `$Q = 0$`, `Mchi` | **agree** | The paper does not fix Dirac or Majorana. Dirac is consistent with Eq. (1), where `$\chi$` is never charge-conjugated. |
| `$\varphi$`, `$X$` in the fundamental of `$SU(3)_c$` (line 173) | `$\varphi$`: **3**, `$Q = +2/3$`; `$X$`: **3**, `$Q = +2/3$` | **agree** | The paper gives no electric charge. The reconstruction derives it from neutrality of each vertex (§1.6), and the result is forced by Eq. (1). |
| `$\tilde\varphi$` heavy scalar for four-fermion interactions (line 183) | **3**, `$Q = -1/3$`, complex | **agree** | Charge again derived from Eq. (1), and forced. |
| all axial couplings zero, `$b = \tilde b = 0$` (line 277) | every `b`-type parameter is 0 | **agree** | |
| `$M_\varphi = M_{\tilde\varphi} = 3$ TeV in the four-fermion limit (line 284) | `Mvphit` = 3000 GeV, `Mvphi` = 500 GeV | **disagree** (benchmark) | The file stores one default set. 500 GeV is the resonance scenario value (line 297), 3 TeV is the four-fermion value. The two paper scenarios cannot both be the default. |
| resonance mass 500 GeV (line 297) | `Mvphi` = `MX` = 500 GeV | **agree** | |
| invisible masses: `$m_\chi = 50$` (scalar) or 300 GeV (vector); scalar FCNC state 300 GeV, vector FCNC state 50 GeV (lines 287-290) | `Mchi` = 50, `Mphi` = 300, `MV` = 50 GeV | **agree** | Only one `$m_\chi$` value can be stored; 50 GeV is the scenario-I choice. |
| no widths given | `Wvphi` = 50, `Wvphit` = 300, `WX` = 50, other widths 0 | **extra-in-reconstruction** | Needed for event generation. `WX` is non-zero while the `$X$` decay to `$t\chi$` is missing, which is self-inconsistent. |
| no PDG codes, no LHA block, no interaction order | PDG 9900001-9900006, LHA block `MONOTOP`, `InteractionOrder -> {NP,1}` | **extra-in-reconstruction** | Implementation bookkeeping only. |

## 3. Disagreements, with severity

1. **The `$X\!-\!u\!-\!\chi$` vertex of Eq. (1) is absent from the implementation.**
   Severity: **substantive**.
   A human should check whether the `.fr` file truly has no `LXChi` block, because without it the
   paper's scenario II (vector resonant monotop, `$BR(X \to t\chi) = 1$`, `$(a^{1/2}_{VR})_3 = 0.1$`)
   cannot be generated at all.

2. **`ahalfVR` and `bhalfVR` are declared but multiply nothing.**
   Severity: **substantive** (same defect, seen from the parameter side).
   A human should check the parameter list against the vertex list, because an orphan external
   parameter with a non-zero value is a strong sign of a dropped Lagrangian term.

3. **`WX` = 50 GeV with no open `$X$` decay to `$t\chi$`.**
   Severity: **substantive**.
   A human should check the width, because a width that does not match the sum of the available
   partial widths corrupts the Breit-Wigner and the cross section of any resonant process.

4. **Hermitian-conjugate bookkeeping for `Lphiu` and `LVu`.**
   Severity: **convention**.
   A human should check that the `.fr` file really omits `HC` on these two terms, and confirm that
   the hermiticity conditions on `$a^0$`, `$b^0$`, `$a^1$`, `$b^1$` hold for every value a user may
   later set, not only for the supplied real symmetric defaults.

5. **`FS[X,mu,nu]` gives the abelian curl, not a QCD-covariant field strength.**
   Severity: **substantive** (implementation, not a paper disagreement).
   A human should check the `$X$` kinetic term, because a colour-triplet vector needs
   `$D_\mu X_\nu - D_\nu X_\mu$` for `$SU(3)_c$` gauge invariance, and the abelian form changes the
   `$X$`-gluon vertices.

6. **`Mvphi` = 500 GeV, while the paper's four-fermion limit uses `$M_\varphi = 3$ TeV.**
   Severity: **cosmetic**.
   A human should check which scenario the shipped defaults are meant to reproduce, because the
   four-fermion scenario V needs `$M_\varphi$` raised to 3 TeV before it is run.

7. **`$m_\chi$` = 50 GeV only, while the paper's vector scenario uses 300 GeV.**
   Severity: **cosmetic**.
   A human should check the benchmark table, because scenario II needs `Mchi` changed at run time.

8. **Real/complex and Dirac/Majorana choices for `$\phi$`, `$V$`, `$\chi$`.**
   Severity: **convention**.
   A human should check these class options against the intended phenomenology, because the paper
   does not state them and a self-conjugate `$\chi$` would change the monotop rate by a factor.

9. **Kinetic terms, mass terms, widths, PDG codes and interaction orders have no paper counterpart.**
   Severity: **cosmetic**.
   A human should confirm the normalisations (`$-\tfrac14 V_{\mu\nu}V^{\mu\nu}$` for the real vector,
   `$-\tfrac12 X^\dagger_{\mu\nu}X^{\mu\nu}$` for the complex one), because the paper gives no rule
   for them.

## 4. Overall assessment

The reconstruction tracks the paper's Eq. (1) closely. Seven of the eight new-physics structures
match the paper in field content, colour contraction, charge conjugation, chirality structure and
coefficient structure, and the derived electric charges (`$\varphi: +2/3$`, `$\tilde\varphi: -1/3$`,
`$X: +2/3$`) are the unique values that make each vertex neutral. The flavour symmetry rules that
the reconstruction derives from Fermi statistics and `$\epsilon_{abc}$` reproduce the paper's own
statement that identical-quark scalar couplings and identical-quark axial vector couplings vanish,
and every default parameter value matches the paper's benchmark line `$a = 0.1$` with all axial
couplings zero. The one gap of physics substance is the final term of Eq. (1), the
`$X_{\mu,i}\,\bar u^i[a^{1/2}_{VR}\gamma^\mu + b^{1/2}_{VR}\gamma^\mu\gamma_5]\chi$` coupling: the
implementation does not contain it, although it declares the `ahalfVR` parameter with a non-zero top
entry and gives `$X$` a 50 GeV width. The reconstruction identifies this gap by itself, writes the
expected form of the missing term, and states the consequence — the vector resonance `$X$` then gives
dijets only and no monotop signal, which contradicts the paper's scenario II assumption of
`$BR(X \to t\chi) = 1$`. The remaining differences are of two kinds: bookkeeping that the paper
never fixes (kinetic and mass terms, widths, PDG codes, the placement of `h.c.`), and benchmark
values that the paper varies across five scenarios but that a single file can only store once. One
implementation issue deserves attention on its own merits even though the paper says nothing about
it: the `$X$` field strength is the abelian curl and is not `$SU(3)_c$`-covariant.
