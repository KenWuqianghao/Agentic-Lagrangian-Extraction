# Cross-check: `reconstruction.md` against the Effective LRSM paper

RUN-TAG: XM-CROSS-EffLRSM__sqrt_swap

**Paper:** Mattelaer, Mitra, Ruiz, *Automated Neutrino Jet and Top Jet Predictions at
Next-to-Leading-Order with Parton Shower Matching in Effective Left-Right Symmetric
Models* (IPPP-16-102, CP3-16-51).

**Reconstruction:** an independent read of `sanitized.fr`, the FeynRules source of the
`EffLRSM_NLO` model.

---

## 1. Where the paper defines the model

The paper puts the whole model in **Sec. II, "Effective Left-Right Symmetric Model"**.
The relevant items are:

| Item | Location in `paper.tex` |
|---|---|
| Field content: SM + $W_R^\pm$ + $Z_R$ + three heavy Majorana $N_i$ | Sec. II, opening paragraph |
| $W_R$ charged current, quarks | Eq. labelled `chcurrent` (first displayed equation of Sec. II) |
| $W_R$ charged current, leptons | second displayed equation of Sec. II (unlabelled), citing Atre et al. and Han et al. |
| Size of the $X$ and $Y$ mixings | third displayed equation of Sec. II |
| Default mixing values | Eq. (`eq:lrsmNuMixing`) |
| Chiral charges $T_L^{3,f}$, $T_R^{3,f}$, $Q^f$ | Table I (`tb:qNumbers`) |
| $Z_R$ neutral current | Eq. labelled `neucurrent` |
| $g_L^{Z_R,f}$ and $g_R^{Z_R,f}$ | the two displayed equations directly after `neucurrent` |
| LO partial widths of $W_R$, $Z_R$ | the width equations after the charge equations |
| Benchmark masses | Eq. (`eq:lrsmInputs`) |
| Benchmark masses and widths (numbers) | Table II (`tb:lrsmParam`) |
| $M_{Z_R}$–$M_{W_R}$ relation | Eq. (`eq:massRelationship`) |
| Missing scalars, ill-defined $W_R/Z_R$ self-interactions | Sec. II C (`sec:modelLimits`) |
| Gauge choice (SM in Feynman gauge, new terms in Unitary gauge) | Sec. III A (`sec:setup`) |
| Heavy-neutrino PDG code 9900012 | App. C (`app:GenCuts`) |

The paper never writes the kinetic or mass terms of the new fields. It gives them only
through the mass parameters $M_{W_R}$, $M_{Z_R}$, $m_{N}$ and the Unitary-gauge statement.

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Gauge group and field content: SM + $W_R^\pm$, $Z_R$ aligned with mass eigenstates, three Majorana $N_i$ aligned with RH chiral states (Sec. II, opening) | `LTotal` = `LSM` + kinetic terms + four current terms; $W_R$, $Z_R$, $N_{1,2,3}$ added to `LSM` | **agree** | Same states, same alignment. No extra state on either side. |
| $N_R$ is a singlet under SM symmetries, charged under $SU(2)_R\otimes U(1)_{B-L}$ (Sec. II, opening) | $N_R$ declared a full gauge singlet; derivative is $\partial_\mu$; $SU(2)_R$ never declared | **agree** | The paper does not gauge $SU(2)_R$ in the effective model, so a plain $\partial_\mu$ is the correct implementation. The RH isospin survives only inside the numerical $Z_R$ charges, exactly as the reconstruction states. |
| $W_R$, $Z_R$ are not dynamical non-Abelian gauge fields; their self-interactions and their couplings to SM bosons are ill-defined (Sec. II C) | $W_R$, $Z_R$ are Proca fields; `FS` gives the Abelian curl; no self-coupling and no $\gamma W_R^+W_R^-$ vertex | **agree** | The reconstruction matches the paper's own stated limitation. |
| Kinetic and mass term of $W_R$ (implied only; $M_{W_R}$ in Eq. `eq:lrsmInputs`) | $-\tfrac12 W_R^{\dagger\mu\nu}W_{R\mu\nu}+M_{W_R}^2 W_R^{\dagger\mu}W_{R\mu}$ | **extra-in-reconstruction** | The paper writes no kinetic term. The form shown is the standard complex Proca normalisation, so it does not contradict the paper. |
| Kinetic and mass term of $Z_R$ (implied only; $M_{Z_R}$ in Table II) | $-\tfrac14 Z_R^{\mu\nu}Z_{R\mu\nu}+\tfrac12 M_{Z_R}^2 Z_R^\mu Z_{R\mu}$ | **extra-in-reconstruction** | Standard real Proca normalisation. No conflict with the paper. |
| Kinetic and mass term of $N$ (implied only; $m_N$ in Eq. `eq:lrsmInputs`) | $\tfrac{i}{2}\overline{N_R^f}\gamma^\mu\partial_\mu N_R^f-\tfrac12 M_N^f\overline{N_R^f}N_R^f$ | **extra-in-reconstruction** | Standard Majorana normalisation with the $\tfrac12$ factors, and a flavour-diagonal mass. Consistent with three decoupled Majorana states. |
| $\mathcal{L}_{W_R qq'}=\frac{-\kappa_R^q g}{\sqrt2}\,\overline{u}_i V^{\rm CKM'}_{ij} W^+_{R\mu}\gamma^\mu P_R d_j+{\rm H.c.}$ (Eq. `chcurrent`) | $-\frac{\kappa_R^q g}{\sqrt2}\,\bar u_i (V^R_{\rm CKM})_{ij}\gamma^\mu P_R d_j W_{R\mu}+{\rm h.c.}$ | **agree** | Same prefactor, same sign, same $\sqrt2$, same right-handed projector, same flavour matrix position. The h.c. term quoted by the reconstruction is the correct conjugate. |
| $V^{\rm CKM'}$ is the RH CKM matrix, taken diagonal with unit entries (Sec. II, after Eq. `chcurrent`) | `VCKMR`: unitary $3\times3$, identity by default | **agree** | Same default. See disagreement D3 for a wording point. |
| $\mathcal{L}_{W_R\ell\nu/N}=\frac{-\kappa_R^\ell g}{\sqrt2}\big[\overline{\nu^c_m}X_{\ell m}+\overline{N_{m'}}Y_{\ell m'}\big]W^+_{R\mu}\gamma^\mu P_R\,\ell^-+{\rm H.c.}$ (second displayed eq. of Sec. II) | $-\frac{\kappa_R^\ell g}{\sqrt2}\big[\overline{N^i_R}(Y_N)_{ij}\gamma^\mu P_R\ell_j+\overline{\nu^c_i}(X_N)_{ij}\gamma^\mu P_R\ell_j\big]W_{R\mu}+{\rm h.c.}$ | **agree** | Both currents are right-handed. Both use the charge-conjugated light-neutrino bar-field. The two pieces only change order. Index order differs; see D2. |
| $\vert Y_{eN_1}\vert=\vert Y_{\mu N_2}\vert=\vert Y_{\tau N_3}\vert=1$, all other $Y$ and all $X$ zero (Eq. `eq:lrsmNuMixing`) | `YN` identity by default; `XN` zero by default, so the $W_R\ell\nu$ vertex is off | **agree** | Identical default. |
| $\mathcal{L}_{Z_R ff}=\frac{-\kappa_R^f g}{\sqrt{1-(1/\kappa_R^f)^2\tan^2\theta_W}}\,\overline f Z_{R\mu}\gamma^\mu\big(g_L^{Z_R,f}P_L+g_R^{Z_R,f}P_R\big)f$ — **lepton part** (Eq. `neucurrent`) | $-\frac{\kappa_R^\ell g}{n_{Z_R}^\ell}\big[\dots\big]Z_{R\mu}$ with $n_{Z_R}^\ell=\sqrt{1-t_W^2/\kappa_R^{\ell2}}$ | **agree** | The lepton prefactor is exactly the paper's form. |
| Same Eq. `neucurrent` — **quark part** | $-\frac{\kappa_R^q g}{n_{Z_R}^q}\big[\dots\big]Z_{R\mu}$ with $n_{Z_R}^q=1/\sqrt{1-t_W^2/\kappa_R^{q2}}$, so the prefactor is $\kappa_R^q g\sqrt{1-t_W^2/\kappa_R^{q2}}$ | **disagree** | The paper uses **one** prefactor for every fermion $f$: divide by the square root. The reconstructed quark line **multiplies** by the square root. The square root is inverted. See D1. |
| $g_L^{Z_R,f}=(T_L^{3,f}-Q^f)\frac{1}{\kappa_R^{f2}}\tan^2\theta_W$ | $g^f=T^f_{3R}-\frac{t_W^2}{\kappa_R^2}(Q^f-T^f_{3L})$, which for a LH field ($T_{3R}=0$) gives $(T^f_{3L}-Q^f)t_W^2/\kappa_R^2$ | **agree** | The single reconstruction formula reproduces the paper's $g_L$ exactly. |
| $g_R^{Z_R,f}=T_R^{3,f}-\frac{1}{\kappa_R^{f2}}\tan^2\theta_W\,Q^f$ | Same formula for a RH field ($T_{3L}=0$): $T^f_{3R}-t_W^2 Q^f/\kappa_R^2$ | **agree** | The single reconstruction formula reproduces the paper's $g_R$ exactly. |
| $u_L$: $T_L^3=+\tfrac12$, $Q=+\tfrac23$ (Table I) $\Rightarrow g_L^u=-\tfrac16 t_W^2/\kappa_R^{q2}$ | `gLZRu` $=-\tfrac16 t_W^2/\kappa_R^{q2}$ | **agree** | |
| $d_L$: $T_L^3=-\tfrac12$, $Q=-\tfrac13$ $\Rightarrow g_L^d=-\tfrac16 t_W^2/\kappa_R^{q2}$ | `gLZRd` $=-\tfrac16 t_W^2/\kappa_R^{q2}$ | **agree** | |
| $u_R$: $T_R^3=+\tfrac12$, $Q=+\tfrac23$ $\Rightarrow g_R^u=\tfrac12-\tfrac23 t_W^2/\kappa_R^{q2}$ | `gRZRu` $=\tfrac12-\tfrac23 t_W^2/\kappa_R^{q2}$ | **agree** | |
| $d_R$: $T_R^3=-\tfrac12$, $Q=-\tfrac13$ $\Rightarrow g_R^d=-\tfrac12+\tfrac13 t_W^2/\kappa_R^{q2}$ | `gRZRd` $=-\tfrac12+\tfrac13 t_W^2/\kappa_R^{q2}$ | **agree** | |
| $e_L$: $T_L^3=-\tfrac12$, $Q=-1$ $\Rightarrow g_L^e=+\tfrac12 t_W^2/\kappa_R^{\ell2}$ | `gLZRe` $=\tfrac12 t_W^2/\kappa_R^{\ell2}$ | **agree** | |
| $e_R$: $T_R^3=-\tfrac12$, $Q=-1$ $\Rightarrow g_R^e=-\tfrac12+t_W^2/\kappa_R^{\ell2}$ | `gRZRe` $=-\tfrac12+t_W^2/\kappa_R^{\ell2}$ | **agree** | |
| $\nu_L$: $T_L^3=+\tfrac12$, $Q=0$ $\Rightarrow g_L^\nu=+\tfrac12 t_W^2/\kappa_R^{\ell2}$; $T_R^3=0$, $Q=0$ $\Rightarrow g_R^\nu=0$ | `gLZRv` $=\tfrac12 t_W^2/\kappa_R^{\ell2}$; no RH $\nu$ term | **agree** | The light neutrino couples left-handed only, as Table I requires. |
| $N_R$: $T_R^3=+\tfrac12$, $Q=0$ $\Rightarrow g_R^N=+\tfrac12$; $T_L^3=0$, $Q=0$ $\Rightarrow g_L^N=0$ | `gRZRn` $=\tfrac12$; no LH $N$ term | **agree** | The reconstruction also notes the term is purely axial because $N$ is Majorana. That is correct and does not change the vertex. |
| $\kappa_R^{q},\kappa_R^{\ell}\in\mathbb{R}$, real normalisations, the same ones in $W_R$ and $Z_R$ (Sec. II, after Eq. `neucurrent`) | `kapRq`, `kapRl` real external inputs, value 1., shared by the $W_R$ and $Z_R$ terms of each sector | **agree** | Same role, same split into a quark and a lepton normalisation. |
| $\kappa_{R}^{q,\ell}=1$ used for all limits and benchmarks (Sec. II B) | Default `kapRq` = `kapRl` = 1. | **agree** | |
| Coupling $g=\sqrt{4\pi\alpha_{\rm EM}(M_Z)}/\sin\theta_W$ (Sec. II, after Eq. `chcurrent`) | `gw` is the SM $SU(2)_L$ coupling $g$, taken from `LSM` | **agree** | |
| $M_{W_R}=3$ TeV, $\Gamma_{W_R}=84.3$ GeV (Eq. `eq:lrsmInputs`, Table II) | `MWR` = 3000., `WWR` = 84.3 | **agree** | |
| $M_{Z_R}=5070$ GeV, $\Gamma_{Z_R}=114$ GeV (Table II) | `MZR` = 5070., `WZR` = 114. | **agree** | Also consistent with Eq. (`eq:massRelationship`), $M_{Z_R}\approx1.7\,M_{W_R}$. |
| $m_{N_1}=m_t=173.3$ GeV, $\Gamma_{N_1}=2.12\times10^{-8}$ GeV (Eq. `eq:lrsmInputs`, Table II) | `mn1` = 173.3, `Wn1` = $2.12\times10^{-8}$ | **agree** | |
| $m_{N_2},m_{N_3}=10^{12}$ GeV (Eq. `eq:lrsmInputs`) | `mn2` = `mn3` = $10^{12}$, widths 0 | **agree** | Both heavy states decouple, as the paper intends. |
| Heavy-neutrino PDG code 9900012 (App. C, `cuts.f` snippet) | $N_1$ PDG 9900012 | **agree** | The codes 9900024, 9900023, 9900014, 9900016 do not appear in the paper, so they cannot be checked. |
| Five massless quarks assumed; SM and RH CKM both diagonal (Sec. II, after Eq. `chcurrent`) | $Z_R$ quark current flavour diagonal, summed over three generations; `VCKMR` identity | **agree** | |
| No LRSM scalar sector; LRSM Higgs states decoupled at 15–20 TeV (Sec. II C) | No scalar field added; no new Yukawa term | **agree** | |
| SM Lagrangian with Goldstone couplings, new terms in Unitary gauge (Sec. III A) | All new terms written with physical fields only, no Goldstone partner | **agree** | |
| Interaction-order counting | `{QCD,1}, {QED,2}, {NP,1}`; `kapRq`, `kapRl` carry `InteractionOrder -> {NP,1}` | **extra-in-reconstruction** | The paper says nothing about order counting, so this cannot be checked against it. |
| Propagator drawing style | `Sine` for both vectors, `Straight` with no arrow for the Majorana fermions | **extra-in-reconstruction** | Drawing information only. No physics content in the paper to compare. |

---

## 3. Disagreements

### D1 — The $Z_R$ quark normalisation inverts the square root. **Severity: substantive.**

The paper writes one prefactor for every fermion in Eq. (`neucurrent`):

$$\frac{-\kappa_R^f g}{\sqrt{1-(1/\kappa_R^f)^2\tan^2\theta_W}}.$$

The reconstructed lepton line has this form. The reconstructed quark line has
$\kappa_R^q g\,\sqrt{1-t_W^2/\kappa_R^{q2}}$, which is the reciprocal square root. The
reconstruction itself flags this in its Sec. 4 and records the file as written.

The paper's own width table settles which form is right. Using
$\alpha(M_Z)=1/127.940$ and $\sin^2\theta_W=0.23126$ (Eq. `eq:smInputs`), so
$g^2=0.4248$ and $t_W^2=0.3008$, the paper's width formula **with division by the square
root** gives $\Gamma(Z_R\to t\bar t)=11.3$ GeV, $\Gamma(Z_R\to q\bar q)=82.3$ GeV,
$\Gamma(Z_R\to\ell^+\ell^-)=7.64$ GeV, $\Gamma(Z_R\to\nu\nu)=2.77$ GeV and
$\Gamma(Z_R\to N_1N_1)=10.2$ GeV, for a total of 114 GeV. Every number reproduces Table
II. The reconstructed quark prefactor would scale each quark partial width by
$(1-t_W^2)^2=0.489$, so the $q\bar q$ entry would fall from 82.3 GeV to about 40 GeV and
the total from 114 GeV to about 61 GeV. That contradicts Table II.

At the default $\kappa_R^q=1$, the reconstructed quark coupling is a factor
$1-t_W^2=0.699$ of the paper value, that is smaller by $1/(1-t_W^2)=1.43$. Rates that
carry two such vertices, for example $q\bar q\to Z_R$ production and $Z_R\to q\bar q$
decay, move by $1.43^2\approx2.0$.

**What a human should check:** open `sanitized.fr`, read the definition of `nZRq` and
`nZRl`, and confirm whether `nZRq` really holds $1/\sqrt{1-t_W^2/\kappa_R^{q2}}$ while
`nZRl` holds $\sqrt{1-t_W^2/\kappa_R^{\ell2}}$; then recompute $\Gamma_{Z_R}$ from the
UFO and compare it with the 114 GeV of Table II.

### D2 — Index order of the lepton mixing matrices. **Severity: convention.**

The paper writes $\overline{N_{m'}}Y_{\ell m'}$ and $\overline{\nu^c_m}X_{\ell m}$, so the
first index is the charged-lepton flavour $\ell$ and the second is the neutrino state.
The reconstruction writes $\overline{N^i_R}(Y_N)_{ij}\ell_j$ and
$\overline{\nu^c_i}(X_N)_{ij}\ell_j$, so the first index is the neutrino and the second is
the charged lepton. The two forms are transposes of each other. Nothing changes at the
default values, because $Y_N$ is the identity and $X_N$ is zero.

**What a human should check:** if anyone regenerates the UFO with a non-diagonal $Y$ or
$X$, confirm which index of the file's matrix is the charged-lepton flavour, because a
transpose would move the lepton-flavour-violating vertices.

### D3 — Wording about the right-handed CKM matrix. **Severity: cosmetic.**

The paper says $V^{\rm CKM'}$ "is related to the SM CKM matrix". The reconstruction says
it is "a separate unitary matrix from the SM CKM matrix". Both descriptions lead to the
same implementation, an independent unitary matrix that is the identity by default, so
there is no numerical difference.

**What a human should check:** nothing for the numbers. Fix the sentence if the
reconstruction becomes user documentation.

### D4 — Internal arithmetic slip inside the reconstruction's own warning. **Severity: cosmetic.**

The reconstruction's Sec. 4 correctly states that the two prefactors differ by
$1/(1-t_W^2)\simeq1.43$, then says the quark couplings are "suppressed by about $1.2$".
The two statements do not match. The correct suppression of the coupling is 1.43; 1.2 is
its square root.

**What a human should check:** correct the sentence so the size of the defect is not
understated by a factor of about 1.2 in the coupling, and about 1.4 in the rate.

### D5 — Kinetic and mass terms cannot be checked against the paper. **Severity: convention.**

`LWRkin`, `LZRkin` and `LNkin` have no counterpart in the paper, which supplies only the
three interaction Lagrangians and the mass values. The normalisations the reconstruction
reports are the standard ones, and the Majorana $\tfrac12$ factors are consistent with the
paper's $\Gamma(Z_R\to N_1N_1)=10.2$ GeV entry, which the formula above reproduces.

**What a human should check:** confirm in `sanitized.fr` that the Majorana kinetic and
mass terms carry the $\tfrac12$ factors, because a missing factor would rescale every $N$
propagator and every $N$ width.

---

## 4. Overall assessment

The reconstruction matches the paper closely across the field content, the chirality
structure, the mixing matrices and all eight neutral-current charges. The $W_R$ quark and
lepton currents reproduce Eq. (`chcurrent`) and the lepton current of Sec. II term by
term, including the $-\kappa_R g/\sqrt2$ prefactor, the right-handed projector, the
charge-conjugated light-neutrino field and the default values of $V^R_{\rm CKM}$, $Y_N$
and $X_N$. The unified charge formula quoted in the reconstruction is algebraically
identical to the paper's separate $g_L$ and $g_R$ expressions once Table I is inserted,
and every numerical charge it lists is correct. All masses, widths and PDG information
that the paper states also agree. One item does not match: the $Z_R$ quark prefactor
inverts the square root that Eq. (`neucurrent`) places in the denominator, while the
lepton prefactor keeps it. This is not a notation difference. An independent recomputation
of the paper's own width table from Eq. (`neucurrent`) reproduces all five $Z_R$ entries
and the 114 GeV total with the denominator form, and fails with the reconstructed quark
form, so the paper and the reconstructed quark line disagree on a physical coupling
strength by a factor of about 1.43, and on quark-initiated $Z_R$ rates by about a factor
of two. The reconstruction flags the same point itself and labels it a likely defect of
the implementation file, although its own estimate of the size is understated. The
remaining differences are an index-order convention in the lepton mixing matrices, a
wording point about the right-handed CKM matrix, and three kinetic and mass terms that the
paper never writes down and that therefore cannot be confirmed from the paper alone.
