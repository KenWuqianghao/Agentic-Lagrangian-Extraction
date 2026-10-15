# Cross-check: reconstruction vs. paper

**Run tag:** XM-CROSS-pNG__control

**Paper:** *Global fit of pseudo-Nambu-Goldstone Dark Matter*, Arina, Beniwal, Degrande,
Heisig, Scaffidi, arXiv:1912.04008 (`paper.tex`).

**Reconstruction:** `reconstruction.md`, run tag XM-RECON-pNG__control, produced from a
FeynRules file `sanitized.fr` that this cross-check cannot see.

---

## 1. Where the paper defines the model

| Item | Location in `paper.tex` |
| --- | --- |
| Full Lagrangian split | eq. (2.1), `\label{eqn:mdl_lagr}` |
| Singlet part $\lagr_S$ | eq. (2.2), `\label{eqn:S_part}` |
| Soft $U(1)$-breaking part $\lagr_{\rm soft}$ | eq. (2.3), `\label{eqn:soft_part}` |
| Dark $U(1)$ and residual $\mathbb{Z}_2$ | eq. (2.4) and text after it |
| Dark $CP$ symmetry $S \to S^*$ | eq. (2.5), `\label{eqn:CP_sym}` |
| SM potential $V_{\rm SM}$ | eq. (2.7) |
| Field decomposition, unitary gauge | eq. (2.8); $m_\chi^2 = \mu_S'^2$ in the text |
| Stationary conditions | eqs. (2.9)–(2.10) |
| CP-even mass matrix $\calM^2$ | eq. (2.11) |
| Rotation $\mathcal{O}(\theta)$ | eqs. (2.12)–(2.14) |
| Mass eigenvalues; $m_h = 125$, $v_h = 246$ GeV | eqs. (2.15)–(2.16) |
| Free parameters $\{m_\chi, v_s, \theta, m_H\}$ | eq. (2.17), `\label{eqn:free_pars}` |
| Derived $\lambda_\Phi$, $\lambda_S$, $\lambda_{\Phi S}$, $\mu$'s | eqs. (2.18)–(2.20), labels `eqn:dep-Pars-start`, `eqn:lamS`, `eqn:lamPS` |
| Invisible widths $h,H \to \chi\chi$ | eqs. (3.4)–(3.5) |
| Rescaled SM production $\cos^2\theta$ | eq. (3.12) |
| $\chi^2 \phi$, $\chi^2 s$ expansion | appendix A, eqs. (A.1)–(A.3) |
| Mass-basis couplings $\kappa_{\chi\chi h}$, $\kappa_{\chi\chi H}$ | appendix A, eqs. (A.5)–(A.6) |
| Yukawa couplings $\kappa_{hf\bar f}$, $\kappa_{Hf\bar f}$ | appendix A, eqs. (A.7)–(A.8) |
| Tree-level direct-detection amplitude | appendix A, eqs. (A.9)–(A.12) |

**Name map.** The two documents use different names for the same states. The map below
is used in the whole table. It follows from the substitution rules quoted in the
reconstruction, which are identical to eq. (A.4) of the paper.

| Paper | Reconstruction | Meaning |
| --- | --- | --- |
| $h$ | `H` (`MH`) | first CP-even mass eigenstate, the one the paper fixes at 125 GeV |
| $H$ | `H2` (`MH2`) | second CP-even mass eigenstate |
| $\phi$ | `phi1` | CP-even neutral part of the doublet (gauge basis) |
| $s$ | `s1` | CP-even part of the singlet (gauge basis) |
| $\chi$ | `chi` (`Mx`) | pNG dark matter |
| $v_h$ | `vev` | electroweak VEV |
| $v_s$ | `vs` | singlet VEV |
| $\theta$ | `thx` (`sxth`, `cxth`) | scalar mixing angle |

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| $\lagr = \lagr_{\rm SM} + \lagr_S + \lagr_{\rm soft}$ (2.1) | `LTotal = LSM + LX + LH2 + LPortal3 + LPortal4` | **agree** | Same structure after the rotation to the mass basis. The paper writes the gauge basis; the file writes the mass basis. |
| $(\partial_\mu S)^*(\partial^\mu S)$ (2.2) | $\tfrac12 (\partial\chi)^2$ in `LX`, $\tfrac12(\partial H_2)^2$ in `LH2`, $H$ kinetic term from `LSM` | **agree** | The rotation is orthogonal, so the kinetic terms stay canonical in the mass basis. Real-scalar factor $1/2$ is correct for both parts of $S$. |
| $-\lambda_{\Phi S}\,\Phi^\dagger\Phi\,|S|^2 \supset -\tfrac12 \lambda_{\Phi S} v_h\, \phi\,\chi^2$ (A.1), (A.3) | `-(1/2) lamPS*vev*phi1*chi^2` in `LPortal3` | **agree** | Sign, factor $1/2$ and field structure all match. |
| $-\tfrac{\lambda_S}{2}|S|^4 \supset -\tfrac12 \lambda_S v_s\, s\,\chi^2$ (A.2), (A.3) | `-(1/2) lamS*vs*s1*chi^2` in `LPortal3` | **agree** | Matches eq. (A.3) exactly. |
| $-\tfrac{\lambda_{\Phi S}}{4}\,\phi^2\chi^2$ (expansion of (2.2), see (A.1)) | `-(1/4) lamPS phi1^2 chi^2` in `LPortal4` | **agree** | Coefficient $1/4$ is the correct one for $\tfrac{\lambda_{\Phi S}}{4}(v_h+\phi)^2[\dots+\chi^2]$. |
| $-\tfrac{\lambda_S}{4}\,s^2\chi^2$ (expansion of (2.2), see (A.2)) | `-(1/4) lamS s1^2 chi^2` in `LPortal4` | **agree** | Correct. |
| $-\tfrac{\lambda_S}{8}\,\chi^4$ (expansion of (2.2)) | `-(1/8) lamS chi^4` in `LPortal4` | **agree** | Correct for $-\tfrac{\lambda_S}{8}[(v_s+s)^2+\chi^2]^2$. |
| $\lagr_{\rm soft} = \tfrac{\mu_S'^2}{4}(S^2+S^{*2})$, with $m_\chi^2 = \mu_S'^2$ (2.3) | $-\tfrac12 M_\chi^2 \chi^2$ in `LX`; the soft term itself is not written | **agree** | The reconstruction states the mass comes from a soft $U(1)$-breaking term of $S^2+{\rm h.c.}$ type. That is the paper's eq. (2.3). $M_\chi$ as a free input matches the paper's free parameter $m_\chi$. |
| Potential normalisation $V \supset \lambda_{\Phi S}|\Phi|^2|S|^2 + \tfrac{\lambda_S}{2}|S|^4$ (2.2) | Same, section 1.6 of the reconstruction | **agree** | The reconstruction rebuilds the parent potential and reproduces all five coefficients. |
| Dark $U(1)$: $S \to e^{i\alpha}S$ (2.4) | Global $U(1)$ on $S$, stated in section 1.6 | **agree** | Same symmetry. |
| $(\phi, s)^T = \mathcal{O}(\theta)\,(h, H)^T$, $\mathcal{O} = \begin{pmatrix}c_\theta & s_\theta\\ -s_\theta & c_\theta\end{pmatrix}$ (2.13), (A.4) | `phi1 = cxth H + sxth H2`, `s1 = -sxth H + cxth H2` | **agree** | Identical rotation, identical sign placement. The reconstruction's reading — $H, H_2$ are the mass eigenstates, $\phi_1, s_1$ the gauge eigenstates — is the paper's reading. |
| $\calM^2 = \begin{pmatrix}\lambda_\Phi v_h^2 & \lambda_{\Phi S}v_h v_s\\ \lambda_{\Phi S}v_h v_s & \lambda_S v_s^2\end{pmatrix}$ (2.11) | Mass matrix in section 3.2 | **agree** (with one defect) | The off-diagonal and $(s,s)$ entries match. The $(\phi,\phi)$ entry is printed as a broken expression instead of $\lambda_\Phi v_h^2$. See D6. |
| $\lambda_S = \dfrac{m_h^2\sin^2\theta + m_H^2\cos^2\theta}{v_s^2}$ (2.19) | `lamS` $= \dfrac{M_H^2\sin^2\theta + M_{H_2}^2\cos^2\theta}{v_s^2}$ | **agree** | Exact match under the name map. |
| $\lambda_{\Phi S} = \dfrac{(m_H^2-m_h^2)\sin\theta\cos\theta}{v_h v_s}$ (2.20) | `lamPS` $= \dfrac{(M_{H_2}^2-M_H^2)\sin\theta\cos\theta}{v\,v_s}$ | **agree** | Exact match, including the sign of the mass difference. |
| $\kappa_{\chi\chi h} = \lambda_{\Phi S}v_h\cos\theta - \lambda_S v_s \sin\theta = -\dfrac{m_h^2\sin\theta}{v_s}$ (A.5) | $\mathcal{L}_3 \supset +\dfrac{M_H^2\sin\theta}{2 v_s}\chi^2 H$, i.e. $\kappa = -\dfrac{M_H^2\sin\theta}{v_s}$ | **agree** | Sign and magnitude match eq. (A.5). |
| $\kappa_{\chi\chi H} = \lambda_{\Phi S}v_h\sin\theta + \lambda_S v_s \cos\theta = +\dfrac{m_H^2\cos\theta}{v_s}$ (A.6) | $\mathcal{L}_3 \supset -\dfrac{M_{H_2}^2\cos\theta}{2 v_s}\chi^2 H_2$, i.e. $\kappa = +\dfrac{M_{H_2}^2\cos\theta}{v_s}$ | **agree** | Sign and magnitude match eq. (A.6). |
| Free parameters $\{m_\chi, v_s, \theta, m_H\}$ (2.17) | `Mx`, `vs`, `thx`, `MH2` | **agree** | Same four inputs. |
| Best-fit point, table 2 column 1: $m_\chi = 62.573$, $v_h/v_s = 0.0187$, $\theta = 1.53$, $m_H = 125.30$ | $M_\chi = 62.573$, $v_s = 13155.1$, $\theta = 1.53$, $M_{H_2} = 125.30$ | **agree** | $246/13155.1 = 0.01870$, so the VEV ratio also matches. The file holds the global-fit best-fit point. |
| Tree-level DD amplitude $\propto q^2\sin\theta\cos\theta(1/m_h^2 - 1/m_H^2)$, so it vanishes at $q^2 = 0$ (A.10)–(A.12) | Exact cancellation of the two Higgs-exchange diagrams at zero momentum transfer, section 4 | **agree** | Same result, same mechanism. |
| Invisible widths $\Gamma(h\to\chi\chi) \propto m_h^3\sin^2\theta/v_s^2$, $\Gamma(H\to\chi\chi)\propto m_H^3\cos^2\theta/v_s^2$ (3.4)–(3.5) | Not written; they follow from the cubic couplings | **agree** | These are consequences of $\kappa_{\chi\chi h}$, $\kappa_{\chi\chi H}$, which match. No separate Lagrangian term is needed. |
| Only one new field, a complex gauge singlet $S$; no new fermions, no new vectors (2.2) | `chi` `S[101]`, `H2` `S[102]`, plus unphysical `phi1`, `s1` | **agree** | Field count and spin match. $\chi$ real, $C$-odd, $(\mathbf 1,\mathbf 1,0)$ is right for ${\rm Im}\,S$. |
| Stability of $\chi$ from the dark $CP$ symmetry $S\to S^*$, under which $\chi\to-\chi$ (2.5 and following text); the residual $\mathbb{Z}_2$, $S\to-S$, only forbids terms linear in $S$ | "The residual $\mathbb{Z}_2$ $\chi\to-\chi$ ... is the unbroken remnant of the global $U(1)$" | **disagree** | Same physical outcome (even powers of $\chi$, stable $\chi$), wrong label for the symmetry. See D1. |
| Non-$\chi$ parts of $\lambda_{\Phi S}\Phi^\dagger\Phi|S|^2$: $\phi s$, $v_h\phi s^2$, $v_s\phi^2 s$, $\phi^2 s^2$ (2.2) | absent | **missing-in-reconstruction** | These give the CP-even triple and quartic scalar vertices. See D2. |
| Non-$\chi$ parts of $\tfrac{\lambda_S}{2}|S|^4$: $v_s s^3$, $s^4$ (2.2) | absent | **missing-in-reconstruction** | Same family of vertices. See D2. |
| $V_{\rm SM} = -\tfrac{\mu_\Phi^2}{2}\Phi^\dagger\Phi + \tfrac{\lambda_\Phi}{2}(\Phi^\dagger\Phi)^2$ with $\lambda_\Phi = \dfrac{m_h^2\cos^2\theta + m_H^2\sin^2\theta}{v_h^2}$ (2.7), (2.18) | absent; `LSM` is added unchanged, so the SM value $\lambda_\Phi = m_h^2/v_h^2$ is kept | **missing-in-reconstruction** | The mixed value of $\lambda_\Phi$ is a defining part of the paper's scalar sector. See D3. |
| $\kappa_{hf\bar f} = \dfrac{m_f}{v_h}\cos\theta$, $\kappa_{Hf\bar f} = \dfrac{m_f}{v_h}\sin\theta$ (A.7)–(A.8) | absent; `LSM` unchanged gives $H$ full SM Yukawa strength and gives $H_2$ no Yukawa coupling at all | **missing-in-reconstruction** | The reconstruction flags this itself ("Caveat on the SM sector"). See D4. |
| $\sigma(pp\to h) = \cos^2\theta\,\sigma^{\rm SM}_{pp\to h}$, and the same $\sin\theta$ rescaling for $H$ (3.12) | absent, same root cause as the row above | **missing-in-reconstruction** | Without it the gauge couplings of both mass eigenstates are wrong. See D4. |
| $\Gamma_H^{\rm tot}$ is non-zero and drives the $H$ resonance (3.9), (5.2) | `WH2 = 0` in the field declaration | **disagree** | A zero width for a 125.30 GeV state that must decay to SM particles. See D5. |
| Goldstone parts $G^0G^0\chi^2$, $G^+G^-\chi^2$ of $\lambda_{\Phi S}|\Phi|^2|S|^2$ | absent | **agree** | Not a defect. The paper also works in the unitary gauge, eq. (2.8). The reconstruction states this correctly. |
| $\mu_\Phi^2$, $\mu_S^2$ stationary conditions (2.9)–(2.10), (2.18)–(2.20) | absent | **missing-in-reconstruction** | Expected. A mass-basis FeynRules file trades them for physical inputs. Cosmetic. |
| Perturbative unitarity $\lambda_S < 8\pi/3$ and boundedness (3.1)–(3.2) | absent | **missing-in-reconstruction** | Scan constraints, not Lagrangian terms. Cosmetic. |
| One-loop $\sigma_{\chi N}$ (3.20)–(3.23); oblique parameters (appendix B) | absent | **missing-in-reconstruction** | Loop-level results, outside a tree-level model file. Cosmetic. |
| — | `LH2` written as a standalone free real scalar with its own $-\tfrac12 M_{H_2}^2 H_2^2$ | **extra-in-reconstruction** | No such separate term exists in the paper. It is the correct diagonalised form, so the physics content agrees. Cosmetic. |

---

## 3. Disagreements, with severity

**D1. Symmetry that protects $\chi$ is labelled wrongly.** *Severity: convention.*
The reconstruction says the $\mathbb{Z}_2$ $\chi \to -\chi$ is the remnant of the global
$U(1)$. The paper says stability comes from the dark $CP$ symmetry $S \to S^*$
(eq. 2.5), and that the $\mathbb{Z}_2$ $S \to -S$ only forbids terms linear in $S$.
*Check:* confirm which symmetry the model file intends, because $S\to-S$ leaves
$\chi \to -\chi$ and $s \to -s$ together, which is not the same statement.

**D2. Pure CP-even scalar self-interactions are absent.** *Severity: substantive.*
`LPortal3` and `LPortal4` keep only the terms with $\chi$. The paper's eq. (2.2)
also produces $\phi s$, $v_h \phi s^2$, $v_s \phi^2 s$, $\phi^2 s^2$, $v_s s^3$ and
$s^4$. These give the $hhh$, $hhH$, $hHH$ and $HHH$ vertices. The paper needs them for
$\Gamma(h \to HH)$ in eq. (3.11) and for $s$-channel $\chi\chi \to hh,\,hH,\,HH$ in
section 3.2. *Check:* run the model file and confirm whether any triple-scalar vertex
exists; if not, every Higgs-pair rate in the paper is unreproducible.

**D3. The mixed Higgs quartic $\lambda_\Phi$ is not used.** *Severity: substantive.*
The paper fixes $\lambda_\Phi = (m_h^2\cos^2\theta + m_H^2\sin^2\theta)/v_h^2$
(eq. 2.18). An unmodified `LSM` keeps the pure SM value $m_h^2/v_h^2$. At the benchmark
angle $\theta = 1.53$ the two differ by a large factor. *Check:* look for any
redefinition of the SM Higgs quartic or of the SM Higgs field inside the real `.fr`
file; the reconstruction may have missed a replacement rule applied to `LSM`.

**D4. Mass eigenstates do not carry the rotated SM couplings.** *Severity: substantive.*
The paper attaches $\cos\theta$ to every $h$–SM coupling and $\sin\theta$ to every
$H$–SM coupling (eqs. 3.12, A.7–A.8). The reconstruction reports that `LSM` is added
unchanged, so `H` keeps full SM strength and `H2` has no SM coupling at all. At the
benchmark $\theta = 1.53$ rad this is the worst case: $\cos^2\theta \simeq 0.0017$, so
the paper's $h$ is almost decoupled from the SM while the file's `H` is not, and the
paper's $H$ carries nearly all the SM coupling while the file's `H2` carries none.
*Check:* confirm whether the real `.fr` file substitutes `phi1` inside the SM Yukawa and
gauge sectors, or whether a separate patched SM file is loaded with it.

**D5. `WH2 = 0`.** *Severity: substantive.*
A 125.30 GeV mostly-doublet scalar has a non-zero total width in the paper
(eqs. 3.9, 5.2), and the resonant annihilation rate is inversely proportional to it.
A zero width makes the resonance singular or the state stable, depending on the tool.
*Check:* whether `WH2` is meant to be computed at run time, or is a placeholder in the
parameter card. This may be a card value, not a model defect.

**D6. Broken mass-matrix expression.** *Severity: cosmetic.*
Section 3.2 of the reconstruction prints the $(\phi_1,\phi_1)$ entry as
"$\lambda_{\Phi S} v v_s / \tan(2\theta)$-fixed diagonal". The paper's eq. (2.11) gives
$\lambda_\Phi v_h^2$. *Check:* nothing physical; the derived `lamS` and `lamPS` that
follow are still correct.

**D7. Which resonance the benchmark sits on.** *Severity: cosmetic.*
The reconstruction says the point sits on the `H2` resonance because
$M_\chi = 62.573 \simeq M_{H_2}/2 = 62.65$ GeV. The paper says the column-1 best-fit
point lies in the $h$-resonance region, and $m_h/2 = 62.5$ GeV. The two scalars differ
by 0.3 GeV, so both statements describe the same corner of parameter space.
*Check:* nothing, unless a rate is quoted per channel.

**D8. `MH` is assumed but not pinned.** *Severity: cosmetic.*
The reconstruction treats `MH` as "the SM-file Higgs mass parameter" and never gives its
value, while the paper fixes $m_h = 125$ GeV exactly (eq. 2.16). *Check:* that the
restriction or parameter card sets `MH = 125` GeV, since `lamS` and `lamPS` both depend
on it.

**Note on naming.** The reconstruction concludes that `H2` is the SM-Higgs-like state and
`H` is mostly singlet, because $\theta = 1.53$ rad is close to $\pi/2$. This is not a
disagreement. The paper reaches the same conclusion in its own names: section 6 says the
fit prefers the second Higgs at 125.3 GeV with "non-suppressed couplings to the SM
particles". The paper still calls $h$ the SM-like Higgs by definition, so a reader who
compares the two documents word by word will see a clash that is not there.

---

## 4. Overall assessment

The reconstruction and the paper agree on the whole dark-sector core of the model. Every
term that contains $\chi$ matches term by term: the real-scalar kinetic and mass
normalisation, the two cubic portal terms of eq. (A.3), the three quartic terms that come
from expanding $\lambda_{\Phi S}\Phi^\dagger\Phi|S|^2$ and $\tfrac{\lambda_S}{2}|S|^4$,
and the parent potential the reconstruction rebuilds in its section 1.6. The mixing
convention is the paper's eq. (A.4) with the same sign placement, the derived couplings
`lamS` and `lamPS` are the paper's eqs. (2.19)–(2.20) exactly, the mass-basis couplings
reproduce $\kappa_{\chi\chi h} = -m_h^2\sin\theta/v_s$ and
$\kappa_{\chi\chi H} = +m_H^2\cos\theta/v_s$ of eqs. (A.5)–(A.6) with the correct relative
sign, and the direct-detection cancellation at zero momentum transfer comes out as the
paper derives it. The numeric inputs are the paper's table 2, column 1, best-fit point,
including the VEV ratio. The gaps all sit outside the $\chi$ sector: the pure CP-even
scalar self-couplings are not written, the mixed Higgs quartic $\lambda_\Phi$ is not
imposed, and the $\cos\theta$ / $\sin\theta$ rescaling of the two mass eigenstates'
couplings to SM fermions and gauge bosons is not applied. The reconstruction itself
flags the last of these as a caveat, which suggests the reconstruction is reading the
file correctly and the gap is in the file, in a companion file the reconstruction could
not see, or in a restriction card. A human reviewer should decide whether those gaps are
real omissions of the implementation or an artefact of reconstructing from one file in
isolation, and should resolve D2, D3 and D4 before treating the file as an
implementation of this paper's full model.
