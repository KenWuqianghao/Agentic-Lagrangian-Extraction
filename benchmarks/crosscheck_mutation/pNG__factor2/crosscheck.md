# Cross-check: reconstruction vs. paper

RUN-TAG: XM-CROSS-pNG__factor2

Paper: *Global fit of pseudo-Nambu-Goldstone Dark Matter*, Arina, Beniwal, Degrande,
Heisig, Scaffidi, arXiv:1912.04008.

---

## 0. Where the paper defines the model

- **Section 2** (`sec:model`), eqs. (2.1)–(2.3): the full Lagrangian
  $\lagr = \lagr_{\rm SM} + \lagr_S + \lagr_{\rm soft}$.
- Eq. (2.9): the field decomposition $\Phi = (0, v_h+\phi)^T/\sqrt2$ and
  $S = (v_s + s + i\chi)/\sqrt2$.
- Eqs. (2.10)–(2.16): tadpole conditions, the CP-even mass matrix, the rotation
  $\mathcal{O}$, and the two mass eigenvalues.
- Eqs. (2.17)–(2.21): the four free parameters and the derived couplings
  $\lambda_\Phi$, $\lambda_S$, $\lambda_{\Phi S}$.
- **Appendix A** (`app:dm-nucleon`), eqs. (A.1)–(A.6): the $\chi^2 h$ and $\chi^2 H$
  couplings $\kappa_{\chi\chi h}$, $\kappa_{\chi\chi H}$, the SM Yukawa rescaling,
  and the tree-level direct-detection cancellation.
- Section 3.3, eqs. (3.5)–(3.6): the invisible widths $h,H \to \chi\chi$.

## 0.1 Symbol map

The two documents use different names for the same states. The map below is used
in the whole table.

| paper | reconstruction | meaning |
|---|---|---|
| $h$ | `H` | lighter CP-even eigenstate, 125 GeV, taken from `LSM` |
| $H$ | `H2` | second CP-even eigenstate, $m_H$ free, best fit 125.30 GeV |
| $\phi$ | `phi1` | CP-even fluctuation of the doublet |
| $s$ | `s1` | CP-even fluctuation of the singlet |
| $\chi$ | `chi` | pNG dark matter |
| $v_h$ | `vev` | doublet VEV, 246 GeV |
| $v_s$ | `vs` | singlet VEV |
| $\theta$ | `thx` | CP-even mixing angle |

Name changes alone are **not** counted as disagreements.

---

## 1. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| $\lagr = \lagr_{\rm SM} + \lagr_S + \lagr_{\rm soft}$ (2.1) | `LTotal = LSM + LX + LH2 + LPortal3 + LPortal4` | **agree** | Same content, split differently. The reconstruction splits $\lagr_S$ into a $\chi$ piece, an $H_2$ piece and two portal pieces. |
| $(\partial_\mu S)^*(\partial^\mu S) \supset \tfrac12 \partial_\mu\chi\,\partial^\mu\chi$ (2.2, 2.9) | `LX` $\supset 2\cdot\tfrac12\,\partial_\mu\chi\partial^\mu\chi = \partial_\mu\chi\partial^\mu\chi$ | **disagree** | The reconstruction carries an overall factor 2. The paper's complex kinetic term gives the canonical $\tfrac12$ for the real field $\chi$. |
| $\chi$ mass term $-\tfrac12 m_\chi^2 \chi^2$, $m_\chi^2 = \mu_S'^2$ (2.3, 2.8, text after 2.9) | `LX` $\supset -2\cdot\tfrac12 M_\chi^2\chi^2 = -M_\chi^2\chi^2$ | **disagree** | Same factor 2. Kinetic and mass terms scale together, so the pole mass stays $M_\chi$; all $\chi$ interactions change. |
| $(\partial_\mu S)^*(\partial^\mu S) \supset \tfrac12 \partial_\mu s\,\partial^\mu s$ (2.2, 2.9) | `LH2` $=\tfrac12 \partial_\mu H_2 \partial^\mu H_2 - \tfrac12 M_{H_2}^2 H_2^2$; $h$ from `LSM` | **agree** | Canonical, no factor 2 here. |
| $\lagr_{\rm soft} = \tfrac{\mu_S'^2}{4}(S^2 + S^{*2})$ (2.3) | not written; traded for the input $M_\chi$ | **missing-in-reconstruction** | Equivalent after the tadpole conditions, because the soft term only shifts the $\chi^2$ coefficient. |
| $\tfrac{\mu_S^2}{2}|S|^2$, $V_{\rm SM}$ $\mu_\Phi^2$ term, tadpole conditions (2.2, 2.6, 2.10, 2.11) | not written; traded for $M_\chi$, $M_{H_2}$, $\theta$, $v_s$ | **missing-in-reconstruction** | Standard practice for a mass-basis implementation. |
| $\Phi=(0,\;v_h+\phi)^T/\sqrt2$, $S=(v_s+s+i\chi)/\sqrt2$ (2.9) | same decomposition, stated in Section 1.7 | **agree** | The reconstruction derives it back from the portal terms and gets the paper's form. |
| $S$ is a complex gauge singlet, electrically neutral (Section 2) | `chi`, `s1` singlets, no `Indices`, no `QuantumNumbers`, `SelfConjugate -> True` | **agree** | Field reps and charges match: $(\mathbf 1,\mathbf 1,0)$. |
| Rotation $(\phi,s)^T = \mathcal{O}\,(h,H)^T$, $\mathcal{O}=\begin{pmatrix}c_\theta & s_\theta\\ -s_\theta & c_\theta\end{pmatrix}$ (2.13, A.4) | $\phi_1 = c_\theta H + s_\theta H_2$, $s_1 = -s_\theta H + c_\theta H_2$ | **agree** | Identical matrix, identical sign convention, under the symbol map. |
| $-\tfrac12\chi^2(\lambda_{\Phi S} v_h\,\phi + \lambda_S v_s\,s)$ (A.3) | `LPortal3` $= -\tfrac12\chi^2(\lambda_{\Phi S} v\,\phi_1 + \lambda_S v_s\, s_1)$ | **agree** | Same coefficients, same structure. |
| $\kappa_{\chi\chi h} = \lambda_{\Phi S} v_h c_\theta - \lambda_S v_s s_\theta = -\,m_h^2 s_\theta/v_s$ (A.5) | $g_{\chi\chi H} = -\,M_H^2 s_\theta / v_s$ | **agree** | Sign and magnitude match. |
| $\kappa_{\chi\chi H} = \lambda_{\Phi S} v_h s_\theta + \lambda_S v_s c_\theta = +\,m_H^2 c_\theta/v_s$ (A.6) | $g_{\chi\chi H_2} = +\,M_{H_2}^2 c_\theta / v_s$ | **agree** | Sign and magnitude match. |
| $-\tfrac{\lambda_{\Phi S}}{4}\phi^2\chi^2$ (from 2.2, expanded in A.2) | `LPortal4` $\supset -\tfrac14 \lambda_{\Phi S}\phi_1^2\chi^2$ | **agree** | |
| $-\tfrac{\lambda_S}{4}s^2\chi^2$ (from 2.2, expanded in A.2) | `LPortal4` $\supset -\tfrac14 \lambda_S s_1^2\chi^2$ | **agree** | |
| $-\tfrac{\lambda_S}{8}\chi^4$ (from $-\tfrac{\lambda_S}{2}|S|^4$, 2.2) | `LPortal4` $\supset -\tfrac18 \lambda_S \chi^4$ | **agree** | |
| $\lambda_S = \dfrac{m_h^2 s_\theta^2 + m_H^2 c_\theta^2}{v_s^2}$ (2.20) | `lamS` $=\dfrac{M_H^2 s_\theta^2 + M_{H_2}^2 c_\theta^2}{v_s^2}$ | **agree** | |
| $\lambda_{\Phi S} = \dfrac{(m_H^2 - m_h^2) s_\theta c_\theta}{v_h v_s}$ (2.21) | `lamPS` $=\dfrac{(M_{H_2}^2 - M_H^2) s_\theta c_\theta}{v\, v_s}$ | **agree** | |
| $\lambda_\Phi = \dfrac{m_h^2 c_\theta^2 + m_H^2 s_\theta^2}{v_h^2}$ (2.19) | not present; `LSM` keeps the SM value $m_h^2/v_h^2$ | **missing-in-reconstruction** | The paper's $\lambda_\Phi$ differs from the SM one whenever $m_H \neq m_h$ and $\theta \neq 0$. |
| Pure scalar self-couplings from $V$: $v_s s\phi^2$, $v_h\phi s^2$, $\phi^2 s^2$, $s^3$, $s^4$ (2.2, 2.6) | absent | **missing-in-reconstruction** | These give the trilinear $hHH$, $hhH$, $HHH$ vertices. The paper needs them for $\Gamma(h\to HH)$ (3.13) and for $\chi\chi\to hh,hH,HH$ via $s$-channel scalar exchange (Section 3.2). |
| $\kappa_{h f\bar f} = \dfrac{m_f}{v_h}c_\theta$, $\kappa_{H f\bar f} = \dfrac{m_f}{v_h}s_\theta$; gauge couplings scaled the same way (A.7, A.8, 3.9) | claimed in prose, but `LSM` is imported and not redefined | **agree (unverified)** | The reconstruction says both that $\phi_1$ carries the SM Yukawa and gauge couplings and that `LSM` supplies the kinetic and Yukawa terms of the mass eigenstate $H$. Only the first choice reproduces the paper. |
| Residual $\mathbb{Z}_2 \otimes CP$, $\chi\to-\chi$, $\chi$ stable (2.4–2.6) | every term even in $\chi$; `Width -> 0` for $\chi$ | **agree** | |
| Tree-level DD amplitude vanishes at $q^2\to0$ (A.10–A.12) | same cancellation, shown explicitly in Section 4 | **agree** | Both reach exactly zero for any $\theta$, $v_s$, $m_h$, $m_H$. |
| Free parameters $\{m_\chi, v_s, \theta, m_H\}$ (2.17) | `Mx`, `vs`, `thx`, `MH2` | **agree** | Default values 62.573 GeV, 13155.1 GeV, 1.53 rad, 125.30 GeV reproduce the global-fit best-fit point of table 3 ($v_h/v_s = 0.0187$). |
| $\Gamma_{\rm inv}(H\to\chi\chi)$ non-zero, plus SM modes through $s_\theta$ (3.6, 3.12) | `WH2 -> 0.` fixed in the particle class | **disagree** | A decay that the paper computes is set to zero in the implementation. |
| $\lambda_S < 8\pi/3$ perturbative unitarity (3.2) | not present | **missing-in-reconstruction** | A scan constraint, not a Lagrangian term. |
| — | extra overall factor 2 in `LX`; `LX := 2(expr;)` returns `Null` | **extra-in-reconstruction** | No counterpart in the paper. See D1 and D2. |

---

## 2. Disagreements, with severity

**D1 — Factor 2 in the $\chi$ kinetic and mass terms. Severity: substantive.**
The paper gives $\tfrac12\partial_\mu\chi\partial^\mu\chi - \tfrac12 m_\chi^2\chi^2$;
the reconstruction gives twice that. A human should check the `LX` line in the
implementation file, because with the factor kept the canonical field is
$\hat\chi=\sqrt2\,\chi$, every $\chi^2 h$ and $\chi^2 H$ coupling is halved, the
$\chi^4$ coupling is divided by 4, and the relic density and invisible width change.

**D2 — `LX` syntax. Severity: substantive.**
The reconstruction reports `LX := 2 (Block[{mu}, ...];)`, a compound expression that
ends with `;` and therefore returns `Null`. A human should load the file in
FeynRules and print `LX` to see whether any $\chi$ term survives at all.

**D3 — Missing pure scalar self-couplings and missing $\lambda_\Phi$ redefinition.
Severity: substantive.**
The paper's potential produces $hHH$, $hhH$ and $HHH$ vertices and redefines
$\lambda_\Phi$ by eq. (2.19); the reconstruction has neither. A human should check
whether the implementation file is only a fragment, and whether the accompanying SM
file supplies the modified scalar potential, because $\Gamma(h\to HH)$ and the
$s$-channel part of $\chi\chi\to hh, hH, HH$ depend on it.

**D4 — SM coupling rescaling by $c_\theta$ and $s_\theta$. Severity: substantive.**
The paper requires every SM coupling of $h$ ($H$) to be scaled by $\cos\theta$
($\sin\theta$). This only happens if `LSM` is written in terms of the unphysical
`phi1`. A human should check which field `LSM` uses, since the best-fit point has
$\theta = 1.53$ rad, where the rescaling is very large ($c_\theta \simeq 0.041$).

**D5 — `WH2 -> 0.` Severity: substantive for phenomenology, convention for the
Lagrangian.**
$2M_\chi = 125.146$ GeV is below $M_{H_2} = 125.30$ GeV, so $H_2\to\chi\chi$ is open,
and $H_2$ also inherits SM modes. A human should replace the fixed zero by a computed
width, above all near the resonance, where eq. (3.20) shows the cross section depends
on $1/\Gamma^{\rm tot}$.

**D6 — Soft term, $\mu_S^2$, $\mu_\Phi^2$ and the tadpole conditions absent.
Severity: convention.**
They are traded for the physical inputs, which is the normal mass-basis choice. A
human should only confirm that no linear or tadpole term was left behind.

**D7 — Naming of the two CP-even states. Severity: cosmetic.**
The paper's SM-like 125 GeV state is $h$; the reconstruction calls it `H`, and calls
the paper's $H$ by the name `H2`. The physics is the same. A human should keep the map
in mind when reading any vertex list.

**D8 — Perturbative unitarity bound absent. Severity: cosmetic.**
It is a scan cut, not a model term. A human needs it only for the fit, not for the
model file.

---

## 3. Overall assessment

The reconstruction matches the paper on almost all of the physics that defines the
model. The field content, the gauge representations and charges, the $\mathbb{Z}_2
\otimes CP$ structure that makes $\chi$ stable, the mixing matrix and its sign
convention, the cubic and quartic portal terms with their exact $\tfrac12$,
$\tfrac14$ and $\tfrac18$ coefficients, the two derived couplings $\lambda_S$ and
$\lambda_{\Phi S}$, the closed forms $\kappa_{\chi\chi h} = -m_h^2 s_\theta/v_s$ and
$\kappa_{\chi\chi H} = +m_H^2 c_\theta/v_s$, and the exact tree-level
direct-detection cancellation all reproduce Section 2 and Appendix A of the paper.
The default parameter values also reproduce the global-fit best-fit point of table 3.
One clear numerical conflict stands out: the $\chi$ kinetic and mass terms carry an
overall factor 2 that the paper does not have, and the same line also has a syntax
form that may evaluate to `Null`. The reconstruction itself flags both, which helps.
Three further gaps are about completeness rather than about a wrong coefficient: the
pure scalar self-couplings and the redefined $\lambda_\Phi$ are absent, the SM
coupling rescaling by $c_\theta$ and $s_\theta$ cannot be confirmed from the fragment
alone, and the second scalar width is pinned to zero. Whether those gaps are real
defects or only the effect of reading one file out of a larger model set cannot be
settled from the two documents in hand; that judgement, and the decision on the
factor 2, belong to the human reviewer.
