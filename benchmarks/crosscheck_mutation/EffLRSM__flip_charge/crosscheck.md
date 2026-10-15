# Cross-check: `reconstruction.md` against `paper.tex`

RUN-TAG: XM-CROSS-EffLRSM__flip_charge

Paper: *Automated Neutrino Jet and Top Jet Predictions at Next-to-Leading-Order
with Parton Shower Matching in Effective Left-Right Symmetric Models*
(Mattelaer, Mitra, Ruiz; IPPP-16-102, CP3-16-51).

---

## 1. Where the paper defines the model

The paper defines the model in **Sec. II, "Effective Left-Right Symmetric
Model"** (`\label{sec:theory}`). The source has no printed equation numbers, so
I quote the LaTeX labels and the line numbers of `paper.tex`.

| Item | Location in `paper.tex` |
| --- | --- |
| Full LRSM gauge group $SU(3)_c\otimes SU(2)_L\otimes SU(2)_R\otimes U(1)_{B-L}$ | Sec. I, unlabelled equation (line 175) |
| Field content: SM states, $W_R^\pm$, $Z_R$, three heavy Majorana $N_i$ | Sec. II, lines 275-277 |
| $W_R$ charged current to quarks | Eq. `(chcurrent)`, lines 280-283 |
| $W_R$ charged current to leptons | Unlabelled equation, lines 292-299 |
| Mixing size and default mixing values | Eq. `(eq:lrsmNuMixing)`, lines 313-316 |
| Quantum numbers $T_L^{3,f}$, $T_R^{3,f}$, $Q^f$ | Table `tb:qNumbers`, lines 323-340 |
| $Z_R$ neutral current | Eq. `(neucurrent)`, lines 351-355 |
| Chiral coefficients $g_L^{Z_R,f}$, $g_R^{Z_R,f}$ | Unlabelled equations, lines 358-362 |
| LO partial widths of $W_R$, $Z_R$ | Lines 366-383 |
| Masses and total widths used | Table `tb:lrsmParam` (lines 392-409) and Eq. `(eq:lrsmInputs)` |
| $M_{Z_R}$-$M_{W_R}$ relation | Eq. `(eq:massRelationship)`, line 413 |
| Model limitations (no scalars, no non-abelian $W_R$/$Z_R$ vertices) | Sec. II C `(sec:modelLimits)`, lines 454-465 |
| Gauge choice and FeynRules version | Sec. III A, lines 480-483 |
| MG5 particle names `wr+`, `wr-`, `n1` | App. A `(app:sigDef)`, lines 1023-1069 |
| Heavy neutrino PDG code 9900012 | App. C `(app:GenCuts)`, line 1105 |

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| Effective model: only the currents of Eqs. `(chcurrent)`-`(neucurrent)` are implemented; scalars and non-abelian vertices are excluded (Sec. II C) | Sec. 0: no gauge group declared, no `DC`, $W_R$ and $Z_R$ are Proca fields, abelian `FS` | **agree** | The paper calls these interactions "ill-defined" and says pair production and VBS are "not correctly modeled". The reconstruction states the stronger form (the vertices are absent). Same physics content. |
| $W_R$ kinetic and mass term (not written in the paper; implied by "aligned with their mass eigenstates", Sec. II, and by the unitary gauge, Sec. III A) | Sec. 1.1: $-\tfrac12 W_R^{\dagger\mu\nu}W_{R\mu\nu}+M_{W_R}^2 W_R^{\dagger\mu}W_{R\mu}$ | **extra-in-reconstruction** | The paper never prints a kinetic term. The quoted form is the standard complex-Proca normalisation, so it is consistent, but the paper gives nothing to compare against. |
| $Z_R$ kinetic and mass term (not written in the paper) | Sec. 1.2: $-\tfrac14 Z_R^{\mu\nu}Z_{R\mu\nu}+\tfrac12 M_{Z_R}^2 Z_R^\mu Z_{R\mu}$ | **extra-in-reconstruction** | Same as above, real-vector normalisation. $Z_R$ neutral and self-conjugate is consistent with Eq. `(neucurrent)`. |
| $N$ kinetic and Majorana mass term (not written in the paper; "three heavy Majorana neutrinos $N_i$", Sec. II line 276) | Sec. 1.3: $\tfrac{i}{2}\overline{N_i}\gamma^\mu\partial_\mu N_i-\tfrac12 M_{N_i}\overline{N_i}N_i$ | **agree** (on the Majorana nature) / **extra-in-reconstruction** (on the explicit term) | The Majorana character and the diagonal mass matrix follow the paper. The $\tfrac12$ normalisation is not stated in the paper. |
| $\mathcal{L}_{W_R qq'}=\frac{-\kappa_R^q g}{\sqrt2}\sum_{i,j}\overline{u}_i V_{ij}^{\rm CKM'} W_{R\mu}^{+}\gamma^\mu P_R d_j+{\rm H.c.}$, Eq. `(chcurrent)` | Sec. 1.4: $-\frac{\kappa_R^q g_w}{\sqrt2}\overline{u}_i (V_R^{\rm CKM})_{ij}\gamma^\mu P_R d_j W_{R\mu}+{\rm h.c.}$ | **agree** | Same prefactor, same sign, same chirality $P_R$, same index order $\overline{u}_i V_{ij} d_j$, diagonal colour contraction. |
| $V_{ij}^{\rm CKM'}$: RH CKM matrix, taken diagonal with unit entries (Sec. II, line 287) | `VCKMR`, $3\times3$ unitary, identity by default | **agree** | Default value matches the paper's working assumption. |
| h.c. of the quark current, Eq. `(chcurrent)` | Sec. 1.4: $-\frac{\kappa_R^q g_w}{\sqrt2}\overline{d}_j (V_R^\dagger)_{ji}\gamma^\mu P_R u_i W^{\dagger}_{R\mu}$ | **agree** | Correct conjugate of a $\bar\psi\gamma^\mu P_R\psi$ bilinear. |
| $\mathcal{L}_{W_R\ell\nu/N}=\frac{-\kappa_R^\ell g}{\sqrt2}\sum_\ell\big[\sum_m\overline{\nu^c_m}X_{\ell m}+\sum_{m'}\overline{N_{m'}}Y_{\ell m'}\big]W^+_{R\mu}\gamma^\mu P_R \ell^-+{\rm H.c.}$ (lines 292-299) | Sec. 1.5: $-\frac{\kappa_R^l g_w}{\sqrt2}\big[\overline{N_i}(Y_N)_{ij}\gamma^\mu P_R\ell_j+\overline{\nu^c_i}(X_N)_{ij}\gamma^\mu P_R\ell_j\big]W_{R\mu}+{\rm h.c.}$ | **agree** on physics; index order differs | Both terms, both prefactors, both chiralities and the charge conjugation $\nu^c=C\bar\nu^T$ match. The paper writes the mixing matrices as $X_{\ell m}$, $Y_{\ell m'}$ (lepton index first); the reconstruction contracts $(X_N)_{ij}$, $(Y_N)_{ij}$ with the neutrino index first. That is the transpose. See D2. |
| Chirality of the lepton current: $P_R$ acting on $\ell^-$, $N$ "aligned with the RH chiral states" (line 277) | Sec. 1.5 notes: only the RH part of $\ell$ enters; $\nu^c$ is RH, so $\overline{\nu^c}\gamma^\mu P_R\ell$ is well formed | **agree** | The bilinear $\bar\chi\gamma^\mu P_R\psi=\overline{\chi_R}\gamma^\mu\psi_R$ selects the RH part of both fields, as the reconstruction states. |
| Lepton-number violation by the Majorana $N$; Keung-Senjanovic signature, Eq. `(eq:ppWRff)` and Ref. `Keung:1983uu` | Sec. 1.5 notes and Sec. 4 | **agree** | Same mechanism and same signature $\ell^\pm\ell^\pm+nj$. |
| Default mixing: $|Y_{eN}|=|Y_{\mu N_2}|=|Y_{\tau N_3}|=1$, $|Y_{\rm others}|=|X_{\ell m}|=0$, Eq. `(eq:lrsmNuMixing)` | `YN` identity by default, `XN` zero by default | **agree** | Exact match, including $X=0$ as the default. |
| $\mathcal{L}_{Z_R ff}=\frac{-\kappa_R^f g}{\sqrt{1-(1/\kappa_R^f)^2\tan^2\theta_W}}\sum_f \overline{f}Z_{R\mu}\gamma^\mu(g_L^{Z_R,f}P_L+g_R^{Z_R,f}P_R)f$, Eq. `(neucurrent)` | Sec. 1.6 and 1.7: $-\frac{\kappa_R^{q,l}g_w}{n_{Z_R}^{q,l}}[\,g_L\bar f\gamma^\mu P_L f+g_R\bar f\gamma^\mu P_R f\,]Z_{R\mu}$ | **agree** | $n_{Z_R}=\sqrt{1-t_W^2/\kappa_R^2}$ is the same denominator. Sign and prefactor match. |
| $\kappa_R^f$ in Eq. `(neucurrent)` "are the same $\kappa_R^{q,\ell}$ as for $W_R$" (line 356) | `kapRq` multiplies the $W_R$ and $Z_R$ quark currents; `kapRl` multiplies the $W_R$ and $Z_R$ lepton currents | **agree** | One parameter per sector, shared between charged and neutral currents. |
| $g_L^{Z_R,f}=(T_L^{3,f}-Q^f)\frac{1}{\kappa_R^{f2}}\tan^2\theta_W$ (line 359) with Table `tb:qNumbers` | `gLZRu`$=-\tfrac16 t_W^2/\kappa_q^2$, `gLZRd`$=-\tfrac16 t_W^2/\kappa_q^2$, `gLZRe`$=+\tfrac12 t_W^2/\kappa_l^2$, `gLZRv`$=+\tfrac12 t_W^2/\kappa_l^2$ | **agree** | Checked each: $u_L$ $(\tfrac12-\tfrac23)=-\tfrac16$; $d_L$ $(-\tfrac12+\tfrac13)=-\tfrac16$; $e_L$ $(-\tfrac12+1)=+\tfrac12$; $\nu_L$ $(\tfrac12-0)=+\tfrac12$. All four match. |
| $g_R^{Z_R,f}=T_R^{3,f}-\frac{1}{\kappa_R^{f2}}\tan^2\theta_W\,Q^f$ (line 361) with Table `tb:qNumbers` | `gRZRu`$=\tfrac12-\tfrac23 t_W^2/\kappa_q^2$, `gRZRd`$=-\tfrac12+\tfrac13 t_W^2/\kappa_q^2$, `gRZRe`$=-\tfrac12+t_W^2/\kappa_l^2$, `gRZRn`$=\tfrac12$ | **agree** | Checked each against Table `tb:qNumbers`. All four match, including $N_R$ with $T_R^3=+\tfrac12$ and $Q=0$. |
| Reconstruction's own rule $g^f=T_{3R}^f-\frac{Y_f}{2}\frac{\tan^2\theta_W}{\kappa_R^2}$, $\frac{Y_f}{2}=T_{3R}^f+\frac{(B-L)_f}{2}$ (Sec. 3.2) | — | **agree** (equivalent form) | For RH fields $Y_f/2=Q^f$; for LH fields $Y_f/2=Q^f-T_L^{3,f}$. The rule is algebraically the same as the paper's two formulas. See D3. |
| $Z_R$ couples to all fields with $(B-L)$ charge, "including $\nu_L$ and $N_R$" (line 348) | Sec. 1.7: $g_L^{Z_R\nu}$ for $\nu$ and $g_R^{Z_Rn}$ for $N$ only | **agree** | The absent entries are zero by the paper's own formulas: $g_R^{Z_R,\nu_L}=T_R^3=0$ and $g_L^{Z_R,N_R}=(0-0)t_W^2/\kappa^2=0$. The omission is correct. |
| $g=\sqrt{4\pi\alpha_{\rm EM}(M_Z)}/\sin\theta_W$, the SM weak coupling (line 288) | $g_w$, "the SM $SU(2)_L$ coupling" | **agree** | Same object. |
| $\kappa_R^{q},\kappa_R^{\ell}\in\mathbb{R}$, independent normalisations (lines 289, 309) | `kapRq`, `kapRl`, real, default 1.0, block `LRSMINPUTS`, `InteractionOrder {NP,1}` | **agree** | The block name, the order and the default 1.0 are extra detail not given in the paper, but nothing conflicts. |
| $M_{W_R}=3$ TeV, $m_{N_1}=m_t=173.3$ GeV, $m_{N_2}=m_{N_3}=10^{12}$ GeV, Eq. `(eq:lrsmInputs)` | Field table: `MWR` 3000, $m_{n_1}=173.3$, $m_{n_2}=m_{n_3}=10^{12}$ | **agree** | Exact match. |
| $M_{Z_R}=5070$ GeV, $\Gamma_{W_R}=84.3$ GeV, $\Gamma_{Z_R}=114$ GeV, $\Gamma_{N_1}=2.12\times10^{-8}$ GeV, Table `tb:lrsmParam` | `MZR` 5070, `WWR` 84.3, `WZR` 114, $W_{n_1}=2.12\times10^{-8}$ | **agree** | Exact match on all four numbers. |
| $M_{Z_R}=\sqrt{2\cos^2\theta_W/\cos2\theta_W}\,M_{W_R}\approx1.7\,M_{W_R}$, Eq. `(eq:massRelationship)` | Note: $M_{Z_R}/M_{W_R}=1.69$ | **agree** | Consistent statement and consistent number. |
| $N_2$, $N_3$ decoupled by hand (lines 446-447) | $W_{n_2}=W_{n_3}=0$, only $n_1$ active | **agree** | The zero widths are not in the paper but follow from the decoupling. |
| $W_R^{+}$ is the field in Eq. `(chcurrent)` and in the lepton current; MG5 process `p p > wr+ > n1 e+` (App. A, line 1045) | `WR` declared with `QuantumNumbers -> {Q -> -1}`, `ParticleName -> "wr+"` | **disagree** | The paper's currents ($\overline{u}\gamma^\mu P_R d$, $\overline{N}\gamma^\mu P_R\ell^-$) each carry charge $-1$, so the field must carry $Q=+1$. The declared $Q=-1$ contradicts the paper. See D1. The reconstruction itself flags the value as a sign error and reads the field as $W_R^+$. |
| Heavy neutrino PDG code 9900012 (App. C, line 1105) | PDG 9900012 / 9900014 / 9900016 for $n_1,n_2,n_3$ | **agree** | The paper confirms only 9900012. The other two are plausible but unverifiable here. |
| MG5 particle labels `wr+`, `wr-`, `zr`, `n1` (App. A) | `ParticleName -> "wr+"`, `AntiParticleName -> "wr-"` | **agree** | Names match the paper's syntax. $Z_R$ and $N$ labels are consistent with `zr` and `n1`. |
| $W_R$/$Z_R$ PDG codes (not given in the paper) | 9900024 for $W_R$, 9900023 for $Z_R$ | **extra-in-reconstruction** | Standard $W'$/$Z'$ codes, but the paper does not state them. |
| Restrictions `massless.rst` and `diagonalCKM.rst`; "assume five massless quarks"; light neutrino masses and mixing set to zero (lines 287, 311, 318-319) | Not mentioned | **missing-in-reconstruction** | The default values quoted (identity CKM, identity $Y$, zero $X$) are equivalent to the restricted model, so the physics is not contradicted. See D5. |
| LO partial width formulas for $W_R\to q\bar q'$, $tb$, $\ell N$ and $Z_R\to f\bar f$ (lines 366-383) | Not reproduced | **missing-in-reconstruction** | These are analytic cross-checks, not Lagrangian terms. The reconstruction quotes the resulting numerical widths, which match. See D8. |
| $R_2$ and UV counterterms from NLOCT 1.02 and FeynArts 3.8 (Sec. III A, line 483) | Not mentioned | **missing-in-reconstruction** | Counterterms are generated after the `.fr` file, so their absence from the reconstruction is expected. |
| SM sector "fully supported", SM Lagrangian in Feynman gauge with Goldstone couplings (lines 465, 480-481) | `LTotal := LSM + ...`, SM fields taken from the FeynRules SM model | **agree** | Same structure: new terms added on top of an unchanged SM. |
| $\mathcal{L}_{\rm total}$ = SM + the listed new terms | Sec. 1.8 | **agree** | The seven new pieces cover exactly the paper's Eqs. `(chcurrent)`-`(neucurrent)` plus the implied kinetic and mass terms. |

---

## 3. Disagreements, with severity

**D1. Electric charge of `WR` declared as $Q=-1$. Severity: substantive.**
The paper writes $W_{R\mu}^{+}$ in both charged-current equations, and App. A
generates `p p > wr+ > n1 e+`. A human should open the implementation file, read
the `QuantumNumbers` entry of the `WR` class, and confirm whether it says
`Q -> -1` while `ParticleName` says `"wr+"`; if so, the charge must be changed to
$+1$, because every $W_R$ vertex would otherwise break charge conservation and
the MG5 commands in App. A would fail.

**D2. Mixing matrices are contracted in transposed index order. Severity: convention.**
The paper uses $X_{\ell m}$ and $Y_{\ell m'}$ with the charged-lepton flavour
first; the reconstruction writes $(X_N)_{ij}$ and $(Y_N)_{ij}$ with the neutrino
index first. A human should check which index the implementation puts first,
because the two orders differ once the matrices are not symmetric, even though
the default identity and zero matrices hide the difference.

**D3. Different but equivalent parametrisation of the chiral $Z_R$ couplings. Severity: cosmetic.**
The paper uses $(T_L^{3,f}-Q^f)$ and $T_R^{3,f}-Q^f t_W^2/\kappa^2$; the
reconstruction uses $T_{3R}^f-(Y_f/2)t_W^2/\kappa^2$ with $Y_f/2=T_{3R}^f+(B-L)_f/2$.
A human should confirm the eight numerical values only, since the two rules give
the same eight numbers.

**D4. Kinetic and mass terms are quoted with normalisations the paper never prints. Severity: cosmetic.**
The $-\tfrac12$ / $+M^2$ complex-Proca and $-\tfrac14$ / $+\tfrac12M^2$ real-Proca
and $\tfrac12$ Majorana factors come from the implementation, not from the paper.
A human should confirm these factors directly against the implementation file,
because the paper offers no equation to compare them with.

**D5. Restriction cards and the massless-quark assumption are not reported. Severity: convention.**
The paper names `massless.rst` and `diagonalCKM.rst` and assumes five massless
quarks. A human should check whether the implementation ships these restriction
files, because the reconstruction describes only the unrestricted defaults.

**D6. "No $\gamma W_R W_R$ vertex" versus the paper's "ill-defined". Severity: cosmetic.**
Sec. II C says non-abelian $W_R$, $Z_R$ interactions and their couplings to SM
bosons are ill-defined; the reconstruction says they are absent. A human should
confirm that no covariant derivative is used for $W_R$, which would make the two
statements the same.

**D7. PDG codes 9900024 and 9900023 are not confirmed by the paper. Severity: cosmetic.**
Only the heavy-neutrino code 9900012 appears in the paper (App. C). A human
should read the codes from the implementation file.

**D8. Width values are reported as declared inputs. Severity: cosmetic.**
The paper computes the widths in Table `tb:lrsmParam` from the analytic formulas.
The reconstruction lists them as fixed numbers in the field declarations. A human
should confirm that the hard-coded widths are the ones the formulas produce for
Eq. `(eq:lrsmInputs)`; the four quoted numbers do match the table.

---

## 4. Overall assessment

The reconstruction maps onto the paper's Sec. II very closely. Every interaction
term in the paper appears in the reconstruction with the same prefactor, the same
sign, the same chiral projector, the same field content and the same index
contraction, and no interaction term appears in the reconstruction that the paper
does not define. All eight chiral $Z_R$ couplings, the $Z_R$ normalisation
denominator, the two independent $\kappa_R$ parameters, the default mixing
matrices, and all six mass and width numbers agree with the paper item by item.
The extra material in the reconstruction is of two kinds: kinetic and mass terms
that the paper never prints but that the effective construction requires, and
implementation detail (Les Houches block, interaction order, PDG codes) that the
paper does not discuss. The one conflict with real physics content is the
declared electric charge of the `WR` field: the paper's Lagrangian and its MG5
commands both need $Q(W_R)=+1$, while the reconstruction reports $Q=-1$ in the
declaration next to the label `"wr+"`. The reconstruction does not hide this; it
states plainly that the value is inconsistent with every $W_R$ vertex and with the
particle label, and it argues for $+1$. A reviewer therefore has to decide two
separate things: whether the implementation file really carries $Q=-1$, and
whether the remaining differences (transposed mixing indices, unstated kinetic
normalisations, unreported restriction cards) are conventions or real defects.
