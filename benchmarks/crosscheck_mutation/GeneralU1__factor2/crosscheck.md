# Cross-check: `reconstruction.md` against the paper

RUN-TAG: XM-CROSS-GeneralU1__factor2

Paper: "Probing the minimal $U(1)_X$ model at future electron-positron colliders
via fermion pair-production channels" (Das, Dev, Hosotani, Mandal; OU-HET-1085).

## 1. Where the paper defines the model

The paper defines the model in Sec. II ("The $U(1)_X$ Model"). The equations have
no printed numbers in the source. I count the numbered display equations in
order and give both the number and the LaTeX label.

| Ref | Label | Content |
|---|---|---|
| Table I | `tab1` | Field content and all $U(1)_X$ charges |
| Eq. (1) | `LYk` | Full Yukawa Lagrangian (quark, charged lepton, Dirac neutrino, Majorana) |
| Eq. (2) | — | Renormalizable Higgs potential $V$ |
| Eq. (3) | — | The two VEVs $\langle H\rangle$ and $\langle\Phi\rangle$ |
| Eq. (4) | — | $M_{Z'} = g'\sqrt{4v_\Phi^2 + \tfrac14 x_H^2 v^2}\simeq 2g'v_\Phi$ |
| Eq. (5) | `num` | Seesaw mass matrix $\mathcal{M}_\nu$ |
| Eq. (6) | `Lag1` | $Z'$ interactions with quarks and leptons (Sec. II A) |
| Eq. (7) | `2f` | $\Gamma(Z'\to f\bar f)$ |
| Eq. (8) | `2v` | $\Gamma(Z'\to \nu\bar\nu)$ |
| Eq. (9) | `2N` | $\Gamma(Z'\to NN)$ |
| Table II | `tab2` | Charge values for benchmark $x_H$ with $x_\Phi=1$ |

Text near Eq. (1) gives $m_{N_\alpha}=\frac{Y_N^\alpha}{\sqrt2}v_\Phi$ and
$m_D^{\alpha\beta}=\frac{Y_\nu^{\alpha\beta}}{\sqrt2}v$. The benchmark point of
the paper is $M_{Z'}=7.5$ TeV, $g'=0.4$, $x_\Phi=1$, and $x_H\in\{-2,-1,1,2\}$.

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Gauge group $SU(3)_C\otimes SU(2)_L\otimes U(1)_Y\otimes U(1)_X$ (Sec. II text) | SM plus one broken abelian group (Sec. 1.0) | **agree** | Same group. Same breaking pattern. |
| $U(1)_X$ is a linear combination of $U(1)_Y$ and $U(1)_{B-L}$ (Sec. II text) | $x_f = x_H Y_f + x_\Phi (B-L)_f$ (Sec. 3.2) | **agree** | Same rule. Same anomaly-free structure. |
| Charges of $q_L,u_R,d_R,\ell_L,e_R,N_R,\Phi$ (Table I) | `xqL, xuR, xdR, xlL, xeR, xnR, xSc` (Sec. 3.2) | **agree** | All seven formulas match Table I term by term. |
| Charge of the SM doublet: $-x_H/2$ (Table I) | `xHd` $=+x_H/2$ (Sec. 3.2) | **agree** | Sign differs, convention differs too. See D4. |
| Three RHNs $N_R^i$, SM singlets, $Y=0$, $x=-x_\Phi$ (Table I) | `F[100]` Majorana $N_X$ plus `F[110]` helper $N_R=P_RN_X$ (Sec. 2) | **agree** | Four-component Majorana field versus two-component Weyl field is notation. |
| Complex SM-singlet scalar $\Phi$, $x=2x_\Phi$ (Table I) | $\Phi_X$ never declared; only the real mode $H_X$ and $v_\Phi$ (Sec. 2) | **agree** | Unitary gauge. The $Z'$ eats the Goldstone mode. See D6. |
| Quark and charged-lepton Yukawas, first three terms of Eq. (1) | Inherited from `LSM`, not restated (Sec. 1.0) | **agree** | The reconstruction states that `LSM` is unchanged. |
| Dirac neutrino Yukawa $-Y_\nu\,\overline{\ell_L}HN_R$, Eq. (1) | $-(y_\nu)_{ab}\bar L_{L,a}\tilde\Phi P_RN_{X,b}$ + h.c. (Sec. 1.7) | **agree** | Both give $m_D=y_\nu v/\sqrt2$. The $H$ versus $\tilde\Phi$ swap follows the doublet convention. Chirality $L\to R$ is the same. |
| Majorana Yukawa $-Y_N^\alpha\Phi\,\overline{N_R^{\alpha c}}N_R^\alpha$, Eq. (1) | `LNYuk` $-\frac{1}{2\sqrt2}H_X\bar N_X y_N N_X$ plus mass $-\frac12\bar N_X m_N N_X$ (Secs. 1.3, 1.6) | **agree** | The file splits one term into a constant mass and a fluctuation. It gives $M_{N_a}=y_{N,aa}v_\Phi/\sqrt2$, which is the paper's $m_{N_\alpha}=Y_N^\alpha v_\Phi/\sqrt2$. Both are flavour diagonal. |
| $m_{N}$ is $\Delta L=2$ and feeds the seesaw, Eq. (5) | Same statement; `NR` carries `LeptonNumber -> 1` (Secs. 1.3, 2) | **agree** | The light mass $m_\nu\simeq-m_Dm_N^{-1}m_D^T$ follows from the same two terms. |
| $-m_h^2(H^\dagger H)+\lambda(H^\dagger H)^2$, Eq. (2) | In `LSM` (Sec. 1.0) | **agree** | SM part, unchanged. |
| $m_\Phi^2(\Phi^\dagger\Phi)+\lambda_\Phi(\Phi^\dagger\Phi)^2$, Eq. (2) | `LPotX` $-\lambda_\Phi v_\Phi H_X^3-\frac{\lambda_\Phi}{4}H_X^4$, with $M_{H_X}^2=2\lambda_\Phi v_\Phi^2$ (Sec. 1.8) | **agree** | This is the expansion of $\lambda_\Phi(|\Phi_X|^2-v_\Phi^2/2)^2$ at the minimum. The quadratic piece sits in `MHX`. |
| Portal $\lambda'(H^\dagger H)(\Phi^\dagger\Phi)$, quartic part, Eq. (2) | $-\frac{\lambda'}{2}H_X^2\Phi^\dagger\Phi$ (Sec. 1.8) | **agree** | Correct coefficient after $\Phi_X\to(v_\Phi+H_X)/\sqrt2$. |
| Portal $\lambda'(H^\dagger H)(\Phi^\dagger\Phi)$, cubic part $\lambda'v_\Phi H_X(H^\dagger H)$, Eq. (2) | Absent (Sec. 1.8, Note 4) | **missing-in-reconstruction** | No $h$–$H_X$ mixing at tree level. See D2. |
| $M_{Z'}=g'\sqrt{4v_\Phi^2+\frac14x_H^2v^2}$, Eq. (4) | `MZp` $=g_X\sqrt{x_{Sc}^2v_\Phi^2+x_{Hd}^2v^2}$ (Sec. 3.2) | **agree** | The two formulas are identical at $x_\Phi=1$. The value $7500.6$ GeV matches the paper's $7.5$ TeV benchmark at $g'=0.4$, $v_\Phi=9375$ GeV. |
| $Z'$ kinetic term (implied by the gauge group) | `LZpKin` $-\frac14Z'_{\mu\nu}Z'^{\mu\nu}+\frac12M_{Z'}^2Z'_\mu Z'^\mu$ (Sec. 1.1) | **agree** | The mass is written in Proca form, not generated by a covariant derivative. See D5. |
| $Z'$ mass from $\vert D_\mu\Phi\vert^2$: vertices $H_XZ'Z'$ and $H_X^2Z'Z'$ (Eq. 4 source) | `LZpHX` $g_X^2x_{Sc}^2(v_\Phi H_X+\frac12H_X^2)Z'_\mu Z'^\mu$ (Sec. 1.5) | **agree** | Exactly what $\vert D_\mu\Phi_X\vert^2$ gives. This block carries **no** factor 2. |
| $Z'$ mass from $\vert D_\mu H\vert^2$: the $\frac14x_H^2v^2$ term of Eq. (4) needs a $Z'$–$H$ vertex and $Z$–$Z'$ mixing | Absent (Sec. 1.0, Note 2) | **missing-in-reconstruction** | The mass keeps the term. The matching vertices are not there. See D3. |
| $Z'$ fermion current, overall coefficient $-g'$, Eq. (6) | `LZpF` overall coefficient $-2g_X$ (Sec. 1.2, Note 1) | **disagree** | Extra factor of 2 on every $Z'$–fermion vertex. See D1. |
| $Z'$ current chiral structure $x_{f_L}P_L+x_{f_R}P_R$, Eq. (6) | Same structure on all SM fermions (Sec. 1.2) | **agree** | Chiral, generation universal, flavour diagonal. CKM drops out by unitarity. |
| $Z'$–$N$ current, implied by $g_R^N$ in Eq. (9) | $x_{n_R}\bar N_X\gamma^\mu P_RN_X$ inside `LZpF` (Sec. 1.2) | **agree** | Right-chiral only, as the charge assignment requires. |
| $\Gamma(Z'\to f\bar f)$, $\Gamma(Z'\to\nu\bar\nu)$, Eqs. (7) and (8); Fig. 1 | Hard-coded `WZp` $=1353$ GeV (Sec. 2) | **agree** (numerically) | I evaluated Eqs. (7) and (8) at $x_H=2$, $x_\Phi=1$, $g'=0.4$, $M_{Z'}=7.5$ TeV, three generations, $Z'\to NN$ closed: the result is $1352.8$ GeV. So the stored width uses the paper's normalisation, **without** the factor 2. See D1 and D8. |
| $Z'\to NN$ is closed because $m_N>M_{Z'}$ (Sec. II A text) | $M_{N_a}=8000$ GeV, $M_{Z'}=7500$ GeV (Secs. 2, 3.1) | **agree** | The channel is closed at the file's own benchmark. |
| Table II, row $x_H=2$, column $q_L$: printed value $1/3$ | `xqL` $=2/3$ at $x_H=2$, $x_\Phi=1$ (Sec. 3.2) | **disagree** | The reconstruction follows the Table I formula and is right. The paper's printed number is a typographic error. See D7. |
| $x_\Phi$ fixed to 1 "without loss of generality" (Sec. II text) | `xPhi` is an input with value $1.0$ (Sec. 3.1) | **agree** | The file keeps the parameter free and sets the paper's value. |
| $Y_\nu^{\alpha\beta}$ is a general matrix, Eq. (1) | `ynu` $={\rm diag}(10^{-6},10^{-6},10^{-6})$ (Sec. 3.1) | **agree** | A numeric benchmark, not a structural change. It gives $m_\nu\sim4\times10^{-3}$ eV by Eq. (5). |
| No gauge kinetic mixing $B_{\mu\nu}Z'^{\mu\nu}$ anywhere in the paper | Absent (Sec. 1.0, Note 3) | **agree** | Both set it to zero. |
| — | PDG codes, propagator labels, `M$InteractionOrderHierarchy`, widths of $H_X$ and $N_X$ (Secs. 2, 3.2) | **extra-in-reconstruction** | Implementation bookkeeping. The paper has no counterpart. |
| $Z'$ decay to RHNs studied only when open, Eq. (9) | Physics summary lists $Z'\to N_XN_X$ among the decays (Sec. 4) | **extra-in-reconstruction** | Generic statement. At this benchmark $2M_N>M_{Z'}$, so the channel is shut. See D9. |

## 3. Disagreements

**D1. Factor of 2 in the $Z'$ fermion current. Severity: substantive.**
Eq. (6) of the paper has the coefficient $-g'$. The file has $-2g_X$. Every
$Z'$–fermion vertex is twice the paper's value, so every $Z'$ partial width and
every $Z'$-mediated cross section is four times too large. A human should open
the `LZpF` block, find the explicit `2`, and compare it with Eq. (6). Two facts
point the same way: the scalar block `LZpHX` and the mass `MZp` use the
unmultiplied normalisation $g_Xx_{Sc}$, and the stored width $1353$ GeV
reproduces Eqs. (7) and (8) only without the 2.

**D2. Missing $h$–$H_X$ mixing term. Severity: substantive.**
Expanding $\lambda'(H^\dagger H)(\Phi^\dagger\Phi)$ of Eq. (2) gives both
$\frac{\lambda'}{2}H_X^2(H^\dagger H)$ and $\lambda'v_\Phi H_X(H^\dagger H)$. The
file keeps the first and drops the second, so the two scalars never mix. A human
should decide if the paper's stated small-$\lambda'$ limit covers this: at
$\lambda'=0.01$ and $v_\Phi=9375$ GeV the mixing angle is about $1.3\times10^{-3}$,
but the term is not zero and it controls $H_X\to WW,ZZ,hh$.

**D3. Missing $Z'$ coupling to the SM doublet. Severity: substantive, small in size.**
The $\frac14x_H^2v^2$ piece of Eq. (4) comes from $|D_\mu H|^2$, so the paper's
$H$ carries $U(1)_X$ charge. The file keeps that piece in `MZp` but writes no
$Z'$–$H$ vertex and no $Z$–$Z'$ mass mixing. A human should check whether the
missing $Z$–$Z'$ mixing matters for the observables; the mass piece itself is
about $1.7\times10^{-4}$ of $M_{Z'}^2$ at the benchmark.

**D4. Sign of the SM doublet charge. Severity: convention.**
Table I gives $-x_H/2$; the reconstruction gives $+x_H/2$. The paper puts the VEV
in the upper doublet component (Eq. 3) and uses $H$ itself in the up-type and
neutrino Yukawas (Eq. 1). The file uses the standard lower-component doublet and
$\tilde\Phi=i\sigma_2\Phi^*$. The two descriptions give the same invariants and
the same $M_{Z'}$, because the charge enters squared. A human should confirm the
doublet convention once, then treat the sign as fixed.

**D5. Proca mass instead of a gauged mass. Severity: convention.**
The file writes $\frac12M_{Z'}^2Z'_\mu Z'^\mu$ by hand and never puts $Z'$ into a
covariant derivative. The value equals Eq. (4), so tree-level rates agree. A
human should note that gauge invariance is not manifest in the file, which
matters for high-energy or loop use, not for the paper's $2\to2$ results.

**D6. The breaking scalar $\Phi_X$ is not declared. Severity: convention.**
The paper has a complex singlet $\Phi$ with a radial mode $\phi$ (Eq. 3). The
file declares only the real scalar $H_X$ and the VEV $v_\Phi$. This is unitary
gauge, and the Goldstone mode is eaten. A human should confirm that no analysis
needs the Goldstone.

**D7. Paper typographic error, not a reconstruction error. Severity: cosmetic.**
Table II, row $x_H=2$, column $q_L$, prints $1/3$. The Table I formula
$\frac16x_H+\frac13x_\Phi$ gives $2/3$, which is what the reconstruction has. A
human should read Table II's $q_L$ entry at $x_H=2$ as $2/3$; my width check
above only reproduces $1353$ GeV with $2/3$.

**D8. Hard-coded $Z'$ width. Severity: convention, with a reuse risk.**
`WZp` is fixed at $1353$ GeV, about $18\%$ of $M_{Z'}$. The paper computes the
width from Eqs. (7) to (9) as a function of $x_H$ (Fig. 1). The stored number is
correct only at $x_H=2$, $x_\Phi=1$, $g'=0.4$, $M_{Z'}=7.5$ TeV. A human should
recompute the width after any change of $g_X$, $x_H$, or $v_\Phi$.

**D9. Decay list in the physics summary. Severity: cosmetic.**
The summary names $Z'\to N_XN_X$ as an available channel. At the file's own
masses, $2M_N=16$ TeV is above $M_{Z'}=7.5$ TeV, and the paper assumes the same
closure. A human should read that sentence as a general remark, not as a
benchmark statement.

## 4. Overall assessment

The reconstruction matches the paper on the whole structure of the model: the
gauge group, the field content, all eight charge formulas of Table I, both
Yukawa terms of Eq. (1), the scalar potential of Eq. (2), the mass relations
$M_{Z'}$, $m_N$, and $m_D$, and the chiral, generation-universal,
flavour-diagonal form of the $Z'$ current in Eq. (6). The benchmark numbers also
line up with the paper: $g'=0.4$, $x_H=2$, $x_\Phi=1$, $M_{Z'}=7500.6$ GeV, and a
$Z'\to NN$ channel that is kinematically shut. One difference is arithmetic and
not cosmetic: the $Z'$ fermion current carries an overall factor of 2 that Eq. (6)
does not have, while the scalar block, the mass formula, and the stored width all
use the unmultiplied normalisation. Three further gaps are omissions rather than
contradictions: the $h$–$H_X$ mixing term, the $Z'$ coupling to the SM doublet,
and the gauged form of the $Z'$ mass. The remaining differences are conventions,
mostly the placement of the doublet VEV, plus one typographic error on the
paper's side in Table II. The human reviewer should weigh the factor of 2 first,
because it changes every $Z'$ rate by four, and then decide whether the three
omitted structures fall inside the approximations the paper states.
