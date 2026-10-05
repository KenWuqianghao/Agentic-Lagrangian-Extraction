# Cross-check: `reconstruction.md` against the paper

RUN-TAG: XM-CROSS-GeneralU1__control

**Paper**: "Probing the minimal $U(1)_X$ model at future electron-positron colliders via
fermion pair-production channels", Das, Dev, Hosotani, Mandal (preprint OU-HET-1085).

## 1. Where the paper defines the model

| Item | Location in `paper.tex` |
|---|---|
| Gauge group $SU(3)_C\otimes SU(2)_L\otimes U(1)_Y\otimes U(1)_X$ | Sec. II, first paragraph after Table 1 |
| Field content and all $U(1)_X$ charges | Table 1 (`tab1`) |
| Yukawa Lagrangian (5 terms) | Eq. `LYk` (the single numbered equation in Sec. II) |
| Scalar potential | unnumbered `align` in Sec. II (the "renormalizable Higgs potential") |
| VEV definitions $\langle H\rangle$, $\langle\Phi\rangle$ | unnumbered `align` in Sec. II |
| $Z'$ mass | unnumbered `eqnarray` in Sec. II: $M_{Z'}=g'\sqrt{4v_\Phi^2+\tfrac14 x_H^2v^2}$ |
| Majorana and Dirac neutrino masses | text after the $M_{Z'}$ equation |
| Neutrino mass matrix and seesaw | Eq. `num` |
| $Z'$ neutral currents | Eq. `Lag1`, Sec. II A |
| $Z'$ partial widths | Eqs. `2f`, `2v`, `2N` |
| Charges at benchmark $x_H$ values | Table 2 (`tab2`) |
| Benchmarks $M_{Z'}=7.5$ TeV, $g'=0.4$, $x_\Phi=1$ | Sec. II B, text after Fig. `gp-MZp-1` |
| FeynRules file of the model exists | Sec. II B, citation `\cite{U1X}` |

The paper gives no Lagrangian for the scalar kinetic terms, for the gauge kinetic
terms, or for the $Z'$ coupling to the scalars. It writes only the fermion currents.

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Gauge group: SM plus one extra abelian factor $U(1)_X$ (Sec. II) | SM (`LSM`) plus one extra abelian group, gauge boson `Zp` = $Z'$ | **agree** | Same structure. The reconstruction adds `LSM` inside `LTotal`. |
| 3 generations of RHNs $N_R^i$, SM singlets (Table 1) | 3 Majorana singlets $N_X^{1,2,3}$, `F[100]`, with `NR` $=P_RN_X$ (`F[110]`, unphysical) | **agree** | Same count, same representation, same chirality. The four-component Majorana form is a notation choice. |
| SM-singlet complex scalar $\Phi$ (Table 1) | $\Phi_X$, not declared; only the real part $H_X$ (`S[100]`) survives | **agree** | Unitary gauge. The $U(1)_X$ Goldstone is eaten by $Z'$. |
| $x_{q_L}=\frac16x_H+\frac13x_\Phi$ (Table 1) | `xqL` $=x_H/6+x_\Phi/3$ | **agree** | Identical. |
| $x_{u_R}=\frac23x_H+\frac13x_\Phi$ (Table 1) | `xuR` $=2x_H/3+x_\Phi/3$ | **agree** | Identical. |
| $x_{d_R}=-\frac13x_H+\frac13x_\Phi$ (Table 1) | `xdR` $=-x_H/3+x_\Phi/3$ | **agree** | Identical. |
| $x_{\ell_L}=-\frac12x_H-x_\Phi$ (Table 1) | `xlL` $=-x_H/2-x_\Phi$ | **agree** | Identical. |
| $x_{e_R}=-x_H-x_\Phi$ (Table 1) | `xeR` $=-x_H-x_\Phi$ | **agree** | Identical. |
| $x_{N_R}=-x_\Phi$ (Table 1) | `xnR` $=-x_\Phi$ | **agree** | Identical. |
| $x_H^{\rm doublet}=-\frac{x_H}{2}$ (Table 1) | `xHd` $=+x_H/2$ | **disagree (sign)** | The paper's $H$ is the conjugate doublet (see D1). The sign only enters squared, in $M_{Z'}$. |
| $x_\Phi^{\rm singlet}=2x_\Phi$ (Table 1) | `xSc` $=2x_\Phi$ | **agree** | Identical. |
| Charge rule: $U(1)_X$ is a linear combination of $U(1)_Y$ and $U(1)_{B-L}$ (Sec. II text) | $x_f=x_HY_f+x_\Phi(B-L)_f$ | **agree** | The reconstruction states the rule that the paper only describes in words. Every fermion charge above follows from it. |
| Anomaly free for general $x_H$, $x_\Phi$ (Sec. II, Table 1 caption) | Same claim, argued from the two anomaly-free directions | **agree** | Same physics content. |
| $-Y_u\overline{q_L}Hu_R-Y_d\overline{q_L}\tilde Hd_R-Y_e\overline{\ell_L}\tilde He_R$ (Eq. `LYk`) | inherited from `LSM`; not written out | **agree** | The SM Yukawa sector is unchanged by the extension. |
| $-Y_\nu^{\alpha\beta}\overline{\ell_L^\alpha}HN_R^\beta+{\rm H.c.}$ (Eq. `LYk`) | `LNuYuk` $=-(y_\nu)_{ab}\bar L_L^{a,i}P_RN_X^b\,\epsilon_{ij}\Phi_j^*+{\rm h.c.}$ | **agree** | Same term. The paper's $H$ equals the reconstruction's $\tilde\Phi$ (see D1). Both couple $N_R$ to the neutral component. |
| $m_D^{\alpha\beta}=\frac{Y_\nu^{\alpha\beta}}{\sqrt2}v$ (Sec. II text) | $m_D=y_\nu v/\sqrt2$ | **agree** | Identical relation. |
| $-Y_N^\alpha\Phi\,\overline{N_R^{\alpha c}}N_R^\alpha+{\rm H.c.}$ (Eq. `LYk`) | `LNYuk` $=-\frac{1}{2\sqrt2}H_X\bar N_X^i(y_N)_{ij}N_X^j$ | **agree** | Both are flavour diagonal (the paper carries one index $\alpha$). The factor $\tfrac12$ is the Majorana normalisation for the self-conjugate four-component field. |
| $m_{N_\alpha}=\frac{Y_N^\alpha}{\sqrt2}v_\Phi$ (Sec. II text) | $(y_N)_{ij}=\sqrt2(m_N)_{ij}/v_\Phi$ | **agree** | Same relation, inverted. |
| Majorana mass term for the RHNs after $U(1)_X$ breaking (Sec. II text) | `LNXKin` $=\frac{i}{2}\bar N_X\gamma^\mu\partial_\mu N_X-\frac12\bar N_X(m_N)_{ij}N_X$ | **agree** | The mass is inserted directly in the broken phase. The paper generates it from $\langle\Phi\rangle$. Both give the same spectrum, and the reconstruction keeps the $H_X\bar NN$ vertex tied to $m_N/v_\Phi$. |
| $V=-m_h^2(H^\dag H)+\lambda(H^\dag H)^2$ (potential) | inherited from `LSM` | **agree** | SM doublet sector unchanged. |
| $m_\Phi^2(\Phi^\dag\Phi)+\lambda_\Phi(\Phi^\dag\Phi)^2$ (potential) | $-\frac12M_{H_X}^2H_X^2$ (in `LHXKin`) $-\lambda_\Phi v_\Phi H_X^3-\frac{\lambda_\Phi}{4}H_X^4$, with $M_{H_X}=\sqrt{2\lambda_\Phi}\,v_\Phi$ | **agree** | The reconstruction is the exact expansion of $\lambda_\Phi(|\Phi_X|^2-v_\Phi^2/2)^2$ around $v_\Phi$. This needs $m_\Phi^2<0$; the paper prints $+m_\Phi^2$ (see D2). |
| $\lambda'(H^\dag H)(\Phi^\dag\Phi)$, quartic part (potential) | $-\frac{\lambda'}{2}H_X^2\,\Phi^\dag\Phi$ in `LPotX` | **agree** | Correct coefficient for $\Phi_X=(v_\Phi+H_X)/\sqrt2$. |
| $\lambda'(H^\dag H)(\Phi^\dag\Phi)$, trilinear part $\lambda'v_\Phi H_X(H^\dag H)$ (potential) | absent; the reconstruction states this itself | **missing-in-reconstruction** | Removes all $h$–$H_X$ mass mixing. The paper works in the small-$\lambda'$ limit where this mixing is negligible (see D3). |
| $\langle H\rangle=\frac{1}{\sqrt2}(v+h,0)^T$, $\langle\Phi\rangle=(v_\Phi+\phi)/\sqrt2$ | $\Phi_X=\frac{1}{\sqrt2}(v_\Phi+H_X)$, $v\simeq246$ GeV | **agree** | $H_X$ is the paper's $\phi$. The upper-component VEV is part of the paper's doublet convention (see D1). |
| $M_{Z'}=g'\sqrt{4v_\Phi^2+\frac14x_H^2v^2}\simeq2g'v_\Phi$ | `MZp` $=g_X\sqrt{x_{\rm Sc}^2v_\Phi^2+x_{H_d}^2v^2}$ | **agree** | With $x_{\rm Sc}=2x_\Phi$, $x_{H_d}=x_H/2$ and the paper's $x_\Phi=1$ this is term-by-term identical. The reconstruction keeps $x_\Phi$ general, which is a superset. |
| $Z'$ kinetic term (implied, never written) | `LZpKin` $=-\frac14Z'_{\mu\nu}Z'^{\mu\nu}+\frac12M_{Z'}^2Z'_\mu Z'^\mu$, $Z'_{\mu\nu}=\partial_\mu Z'_\nu-\partial_\nu Z'_\mu$ | **agree** | Standard abelian field strength and mass term. Nothing in the paper contradicts it. |
| $\mathcal{L}^q=-g'(\bar q\gamma^\mu q_x^{q_L}P_Lq+\bar q\gamma^\mu q_x^{q_R}P_Rq)Z'_\mu$ (Eq. `Lag1`) | `LZpF` quark part: $-g_XZ'_\mu[x_{q_L}\bar Q_L\gamma^\mu Q_L+x_{u_R}\bar u_R\gamma^\mu u_R+x_{d_R}\bar d_R\gamma^\mu d_R]$ | **agree** | Same overall sign, same coupling $-g'x_f$, same projector structure, same charges. |
| $-g'(\bar\ell\gamma^\mu q_x^{\ell_L}P_L\ell+\bar e\gamma^\mu q_x^{\ell_R}P_Re)Z'_\mu$ (Eq. `Lag1`) | `LZpF` lepton part with $x_{l_L}$ on $(\nu,e)_L$ and $x_{e_R}$ on $e_R$ | **agree** | Identical. |
| $P_{L,R}=(1\mp\gamma_5)/2$ (text under Eq. `Lag1`) | `ProjM` $=(1-\gamma_5)/2$, `ProjP` $=(1+\gamma_5)/2$ | **agree** | Same convention. |
| Generation-independent, family-universal charges (Sec. II, Sec. III) | All $Z'$ currents flavour diagonal; CKM unitarity rules applied | **agree** | Both exclude flavour-changing $Z'$ vertices. |
| $Z'$ coupling to RHNs, $g_R^N[g',x_\Phi]$, with $\beta^3$ threshold factor (Eq. `2N`) | `LZpF` $N$ part: $-g_Xx_{n_R}Z'_\mu\bar N_X\gamma^\mu P_RN_X$, which is a pure axial current | **agree** | The $\beta^3$ factor in Eq. `2N` is the phase space of an axial coupling to a Majorana pair. This confirms the reconstruction's axial reading. |
| $Z'$ decay widths, Eqs. `2f`, `2v`; $\Gamma$ at $M_{Z'}=7.5$ TeV (Fig. `Zp-decay-1`) | `WZp` $=1353$ GeV | **agree** | Independent check: Eqs. `2f`+`2v` at $x_H=2$, $x_\Phi=1$, $g'=0.4$, $M_{Z'}=7.5$ TeV, with $Z'\to NN$ closed, give $\Gamma=1353$ GeV. The stored width reproduces the paper exactly. |
| $m_N>M_{Z'}$ assumed, so $Z'\to NN$ is closed (Sec. II A) | $M_{N_i}=8000$ GeV, $M_{Z'}\approx7500$ GeV | **agree** | The benchmark satisfies the paper's assumption. |
| $\mathcal{M}_\nu=\begin{pmatrix}0&m_D\\m_D^T&m_N\end{pmatrix}$, $m_\nu\simeq-m_Dm_N^{-1}m_D^T$ (Eq. `num`) | Not diagonalised; the seesaw stays implicit in `LNuYuk` plus the Majorana mass | **missing-in-reconstruction** | The light-heavy mixing angle and the light mass eigenstates are not built in (see D4). |
| $M_{Z'}=7.5$ TeV, $g'=0.4$, $x_\Phi=1$ benchmarks (Sec. II B) | `gX` $=0.4$, `vX` $=9375$ GeV, `xPhi` $=1.0$, `xH` $=2.0$ | **agree** | $2g'v_\Phi=0.4\times2\times9375=7500$ GeV. $x_H=2$ is one of the paper's four benchmarks. |
| No kinetic mixing $B_{\mu\nu}Z'^{\mu\nu}$ is ever written | No kinetic mixing term | **agree** | Both omit it. |
| Doublet carries $x_{H_d}\neq0$, so $|D_\mu H|^2$ implies $Z'$–doublet currents and $Z$–$Z'$ mass mixing | No $Z'$ coupling to the Higgs-doublet current, no $Z$–$Z'$ mass mixing, no $Z'Z'h$ or $Z'Zh$ vertex | **missing-in-reconstruction** | The paper keeps the $\frac14x_H^2v^2$ doublet piece inside $M_{Z'}$ but never writes the matching vertices (see D5). |
| $|D_\mu\Phi|^2$ is never written in the paper | `LZpHX` $=g_X^2x_{\rm Sc}^2(v_\Phi H_X+\frac12H_X^2)Z'_\mu Z'^\mu$ | **extra-in-reconstruction** | Required by gauge invariance and consistent with the singlet part of $M_{Z'}$. Not a conflict; the paper simply never states it. |
| $\lambda_\Phi$, $\lambda'$, $Y_\nu$, $m_N$, $v_\Phi$ values | `lamX` $=0.1$, `lamHX` $=0.01$, `ynu` $={\rm diag}(10^{-6})$, `MNX` $=8$ TeV, `vX` $=9375$ GeV | **extra-in-reconstruction** | The paper fixes none of these. They are implementation benchmarks. All are consistent with the paper's constraints. |
| $M_{H_X}$ (the paper gives no $\phi$ mass) | `MHX` $=\sqrt{2\lambda_\Phi}v_\Phi\approx4.19$ TeV | **extra-in-reconstruction** | Follows from the paper's potential with the chosen $\lambda_\Phi$. |
| PDG codes, widths `WHX`, propagator labels, interaction orders `{QCD,1},{QED,2},{NP,1}` | present | **extra-in-reconstruction** | Pure implementation data. No paper counterpart. |
| Table 2, cell $x_H=2$, $q_L$: printed value $1/3$ | `xqL` numeric at $x_H=2$, $x_\Phi=1$: $2/3$ | **disagree (numeric)** | The paper's own Table 1 formula gives $\frac16(2)+\frac13=\frac23$. The reconstruction follows the formula (see D6). |

---

## 3. Disagreements, with severity

**D1 — Sign of the Higgs-doublet $U(1)_X$ charge. Severity: convention.**
Table 1 gives the doublet $x=-x_H/2$; the reconstruction gives $x_{H_d}=+x_H/2$.
The paper's Yukawa Eq. `LYk` writes $\overline{q_L}Hu_R$, $\overline{q_L}\tilde Hd_R$ and
$\overline{\ell_L}HN_R$. Gauge invariance of those three terms forces $Y_H=-1/2$, so the
paper's $H$ is the conjugate of the standard SM doublet. The reconstruction uses the
standard doublet ($Y=+1/2$, $\bar L_L\tilde\Phi N_R$), for which the same rule
$x=x_HY+x_\Phi(B-L)$ gives $+x_H/2$. The two are the same physics in mirrored notation.
*A human should check that the `.fr` file uses the standard-convention doublet with
$\bar L\,\tilde\Phi\,N_R$, because the paper's Table 1 also prints $U(1)_Y=+1/2$ for $H$,
which contradicts the paper's own Yukawa convention.*

**D2 — Sign of $m_\Phi^2$ in the potential. Severity: cosmetic (paper-side typo).**
The paper prints $+m_\Phi^2(\Phi^\dag\Phi)$, which alone would not break $U(1)_X$, yet the
paper then gives $\Phi$ a VEV. The reconstruction assumes the breaking form
$\lambda_\Phi(|\Phi_X|^2-v_\Phi^2/2)^2$.
*A human should confirm that the paper means $m_\Phi^2<0$ (or a $-m_\Phi^2$ sign), because
every later result in the paper needs $\langle\Phi\rangle\neq0$.*

**D3 — Missing trilinear portal $\lambda'v_\Phi H_X(H^\dag H)$. Severity: substantive, but
likely intended.**
The paper's potential contains the full $\lambda'(H^\dag H)(\Phi^\dag\Phi)$. Expanding it
around both VEVs produces a trilinear term that mixes $h$ and $H_X$. The reconstruction
keeps only the quartic $H_X^2(H^\dag H)$, so $h$ and $H_X$ stay mass eigenstates. The
paper states it works "in the limit of small $\lambda'$", where this mixing is negligible,
so the omission matches the paper's approximation but not the paper's written potential.
*A human should decide whether the implementation is meant to be exact or to encode the
small-$\lambda'$ limit, and should not use this file for any $h$–$H_X$ mixing study.*

**D4 — Seesaw not diagonalised. Severity: substantive for neutrino observables,
irrelevant for the paper's analysis.**
Eq. `num` defines the full $6\times6$ mass matrix and the light mass
$m_\nu\simeq-m_Dm_N^{-1}m_D^T$. The reconstruction keeps $m_D$ and $m_N$ as separate terms
and does not rotate to mass eigenstates, so there is no explicit light-heavy mixing angle.
*A human should check that no process of interest needs the active-heavy mixing; with
$y_\nu\sim10^{-6}$ the mixing is tiny, and the paper's $e^+e^-\to f\bar f$ study never uses it.*

**D5 — No $Z'$ coupling to the Higgs-doublet current, and no $Z$–$Z'$ mass mixing.
Severity: substantive, but consistent with the paper's own treatment.**
For $x_H\neq0$ the doublet carries $U(1)_X$ charge, so $|D_\mu H|^2$ generates $Z'$–$H$
currents and a $Z$–$Z'$ mass mixing of order $x_Hv^2/v_\Phi^2$. The paper retains the
doublet piece $\frac14x_H^2v^2$ inside $M_{Z'}$, which is exactly the trace of that mixing,
but never writes the vertices. The reconstruction reports that the file has none either.
*A human should confirm that the intended use is limited to $Z'$ exchange with SM fermions,
where the neglected mixing is of order $v^2/v_\Phi^2\sim10^{-3}$, and should not use the
file for $Z$-pole electroweak fits, $Z'\to Zh$, or $Z'Z'h$ studies.*

**D6 — Numeric charge of $q_L$ at $x_H=2$. Severity: cosmetic (paper-side typo).**
Paper Table 2 prints $q_L=1/3$ for $x_H=2$. The paper's own Table 1 formula gives
$\frac16(2)+\frac13(1)=\frac23$, which is what the reconstruction reports. Every other cell
of the $x_H=2$ row and every other $q_L$ cell of Table 2 matches the formula.
*A human should confirm this is a typographical slip in Table 2 and check whether the
paper's numerical results for $x_H=2$ used $1/3$ or $2/3$ for the left-handed quarks.*

---

## 4. Overall assessment

The reconstruction and the paper describe the same model. All eight $U(1)_X$ charges
follow the paper's Table 1, the $Z'$ neutral-current Lagrangian reproduces Eq. `Lag1`
term by term including the overall sign and the chirality projectors, the $Z'$ mass
formula is algebraically identical to the paper's once $x_\Phi=1$ is inserted, and the
Dirac and Majorana mass relations $m_D=y_\nu v/\sqrt2$ and $m_N=y_Nv_\Phi/\sqrt2$ match the
paper exactly. Two independent numerical checks support the match: the stored total width
`WZp` $=1353$ GeV is what Eqs. `2f` and `2v` give at $x_H=2$, $g'=0.4$, $M_{Z'}=7.5$ TeV
with $Z'\to NN$ closed, and the benchmark $2g'v_\Phi$ reproduces the paper's $M_{Z'}=7.5$
TeV; the RHN mass of 8 TeV also honours the paper's stated assumption $m_N>M_{Z'}$. The
differences fall into three groups. First, two apparent conflicts trace back to
convention or to paper typographical slips: the doublet charge sign (the paper's $H$ is the
conjugate doublet) and the $q_L$ entry at $x_H=2$ in Table 2, where the reconstruction
follows the paper's own formula. Second, three terms that a complete implementation of the
paper's written Lagrangian would contain are absent: the trilinear Higgs portal, the
$Z'$–doublet currents with the associated $Z$–$Z'$ mass mixing, and the seesaw
diagonalisation. Each of these is small in the regime the paper works in, and the
reconstruction flags all three itself in its own caveat list. Third, a set of numerical
inputs ($v_\Phi$, $\lambda_\Phi$, $\lambda'$, $Y_\nu$, $m_N$, PDG codes, widths) is present
in the implementation but absent from the paper; none conflicts with the paper. The human
reviewer should focus on D3 and D5, because these decide whether the file is an exact
implementation of the published potential and covariant derivative or an implementation of
the paper's stated approximations.
