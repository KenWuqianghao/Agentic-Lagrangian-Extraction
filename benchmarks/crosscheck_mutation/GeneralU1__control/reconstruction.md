# Reconstruction of `sanitized.fr`

The file extends the Standard Model (`LSM` is added in `LTotal`) by one extra abelian
gauge group. Call it $U(1)_X$. The charge of each field is a linear combination of
hypercharge $Y$ and $B-L$:

$$x_f \;=\; x_H\,Y_f \;+\; x_\Phi\,(B-L)_f .$$

The internal parameters reproduce this rule exactly (see the Parameters section).
The model also adds three Majorana fermion singlets and one real singlet scalar.

---

## 1. Lagrangian

### Conventions

* $P_{R}=\tfrac{1+\gamma_5}{2}$ (`ProjP`), $P_{L}=\tfrac{1-\gamma_5}{2}$ (`ProjM`).
* $Q_L,\,L_L$ are the SM left-handed doublets; $u_R,\,d_R,\,e_R$ are the right-handed
  singlets. Generation indices $i,j$ run over 1..3. SU(2) indices are $i,j$ on the
  doublets (`FlavorExpand -> SU2D` writes the components out).
* $\Phi$ is the SM Higgs doublet (`Phi` in the SM file), $v\simeq 246$ GeV (`vev`).
* $\Phi_X$ is the extra complex singlet scalar. It is **not** declared as a field.
  Only its real fluctuation $H_X$ survives, with
  $\Phi_X = \tfrac{1}{\sqrt2}\left(v_\Phi + H_X\right)$ in unitary gauge.
* `FS[Zp,mu,nu]` is the abelian field strength
  $Z'_{\mu\nu}=\partial_\mu Z'_\nu-\partial_\nu Z'_\mu$.

### Covariant derivative

The file writes the gauge currents by hand, so no `DC` appears. The currents and the
$Z'Z'H_X$ term are both reproduced by

$$D_\mu \;=\; \partial_\mu
- i g_s T^a G^a_\mu
- i g \,T^k W^k_\mu
- i g' Y B_\mu
+ i g_X\, x_f\, Z'_\mu ,$$

acting on a field of $U(1)_X$ charge $x_f$. The sign of the last term is fixed by
`LZpF`: $\bar f i\gamma^\mu D_\mu f \supset -g_X x_f\, Z'_\mu \bar f \gamma^\mu f$.
The same sign convention gives $|D_\mu \Phi_X|^2 \supset g_X^2 x_{\rm Sc}^2 Z'_\mu Z'^\mu |\Phi_X|^2$,
which is `LZpHX`. There is **no** kinetic mixing term $-\tfrac{\epsilon}{2}B_{\mu\nu}Z'^{\mu\nu}$
and **no** $Z$–$Z'$ mass mixing term in the file.

---

### `LZpKin` — $Z'$ kinetic and mass term

$$\mathcal{L}_{\rm ZpKin}
= -\frac{1}{4}\,Z'_{\mu\nu}Z'^{\mu\nu}
\;+\;\frac{1}{2}\,M_{Z'}^{2}\,Z'_\mu Z'^\mu ,
\qquad Z'_{\mu\nu}=\partial_\mu Z'_\nu-\partial_\nu Z'_\mu .$$

The mass is put in by hand (broken phase, unitary gauge) with

$$M_{Z'} = g_X\sqrt{x_{\rm Sc}^2 v_\Phi^2 + x_{H_d}^2 v^2}\; .$$

### `LZpF` — $Z'$ neutral currents

$$\mathcal{L}_{\rm ZpF}
= -\,g_X\,Z'_\mu \sum_{i=1}^{3}\Big[
 x_{q_L}\,\bar Q_L^{\,i}\gamma^\mu Q_L^{\,i}
+x_{u_R}\,\bar u_R^{\,i}\gamma^\mu u_R^{\,i}
+x_{d_R}\,\bar d_R^{\,i}\gamma^\mu d_R^{\,i}
+x_{l_L}\,\bar L_L^{\,i}\gamma^\mu L_L^{\,i}
+x_{e_R}\,\bar e_R^{\,i}\gamma^\mu e_R^{\,i}
+x_{n_R}\,\bar N_R^{\,i}\gamma^\mu N_R^{\,i}\Big].$$

Written with explicit projectors on four-component Dirac fields:

$$\mathcal{L}_{\rm ZpF}
= -\,g_X\,Z'_\mu \sum_i \Big[
 x_{q_L}\big(\bar u^i\gamma^\mu P_L u^i+\bar d^i\gamma^\mu P_L d^i\big)
+x_{u_R}\,\bar u^i\gamma^\mu P_R u^i
+x_{d_R}\,\bar d^i\gamma^\mu P_R d^i$$
$$\;+\;x_{l_L}\big(\bar \nu^i\gamma^\mu P_L \nu^i+\bar e^i\gamma^\mu P_L e^i\big)
+x_{e_R}\,\bar e^i\gamma^\mu P_R e^i
+x_{n_R}\,\bar N_X^i\gamma^\mu P_R N_X^i\Big].$$

Notes on index contractions:

* All currents are flavour diagonal. The replacement rules
  $V_{ab}V^{*}_{ac}\to\delta_{bc}$ and $V_{ba}V^{*}_{ca}\to\delta_{bc}$ apply CKM
  unitarity, so no flavour-changing $Z'$ vertex survives.
* $N_R = P_R N_X$, so $\bar N_R\gamma^\mu N_R = \bar N_X\gamma^\mu P_R N_X$.
  Because $N_X$ is Majorana, the vector part cancels and this equals
  $\tfrac12 \bar N_X \gamma^\mu \gamma_5 N_X$: the $Z'$ couples to a pure axial
  current of the heavy neutrinos.
* The $Z'$ has no coupling to the Higgs doublet current in this file, although
  $x_{H_d}$ does enter $M_{Z'}$.

### `LNXKin` — Majorana kinetic and mass term

$$\mathcal{L}_{\rm NXKin}
= \frac{i}{2}\,\bar N_X^{\,i}\gamma^\mu \partial_\mu N_X^{\,i}
\;-\;\frac{1}{2}\,\bar N_X^{\,i}\,(m_N)_{ij}\,N_X^{\,j},
\qquad (m_N)_{ij}={\rm diag}(M_{N_1},M_{N_2},M_{N_3}).$$

The factors $\tfrac12$ are the standard Majorana normalisation.

### `LHXKin` — singlet scalar kinetic and mass term

$$\mathcal{L}_{\rm HXKin}
= \frac{1}{2}\,\partial_\mu H_X\,\partial^\mu H_X
\;-\;\frac{1}{2}\,M_{H_X}^{2}\,H_X^{2},
\qquad M_{H_X}=\sqrt{2\lambda_\Phi}\;v_\Phi .$$

### `LZpHX` — gauge–scalar vertices from $|D_\mu\Phi_X|^2$

$$\mathcal{L}_{\rm ZpHX}
= g_X^{2}\,x_{\rm Sc}^{2}\left(v_\Phi H_X + \frac{1}{2}H_X^{2}\right) Z'_\mu Z'^\mu .$$

This is $|D_\mu \Phi_X|^2$ with the constant piece removed; that constant piece is the
$v_\Phi$ part of $M_{Z'}$ in `LZpKin`.

### `LNYuk` — $H_X$ coupling to the heavy neutrinos

$$\mathcal{L}_{\rm NYuk}
= -\frac{1}{2\sqrt{2}}\;H_X\;\bar N_X^{\,i}\,(y_N)_{ij}\,N_X^{\,j}
\;=\;-\frac{1}{2}\,\frac{(m_N)_{ij}}{v_\Phi}\;H_X\,\bar N_X^{\,i} N_X^{\,j},$$

because $(y_N)_{ij}=\sqrt{2}\,(m_N)_{ij}/v_\Phi$. The coupling is diagonal and fixed by
the heavy mass and $v_\Phi$.

### `LNuYuk` — Dirac neutrino Yukawa

$$\mathcal{L}_{\rm NuYuk}
= -\,(y_\nu)_{ab}\;\bar L_L^{\,a,\,i}\,P_R N_X^{\,b}\;\epsilon_{ij}\,\Phi_j^{*}
\;+\;\mathrm{h.c.}
\;=\;-\,(y_\nu)_{ab}\;\bar L_L^{\,a}\,\tilde\Phi\,N_R^{\,b}\;+\;\mathrm{h.c.},$$

with $\tilde\Phi_i=\epsilon_{ij}\Phi_j^{*}$, $\epsilon_{12}=+1$, and $N_R=P_R N_X$.
The hermitian conjugate (`HC`) gives $-(y_\nu)^{*}_{ab}\,\bar N_X^{\,b} P_L L_L^{\,a}\,\tilde\Phi^{\dagger}$.
Goldstone fields $G^0,G^\pm$ are set to zero unless `FeynmanGauge` is true.

After electroweak symmetry breaking this gives the Dirac mass

$$m_D = \frac{y_\nu\, v}{\sqrt{2}} .$$

### `LPotX` — scalar potential terms

$$\mathcal{L}_{\rm PotX}
= -\,\lambda_\Phi\, v_\Phi\, H_X^{3}
\;-\;\frac{\lambda_\Phi}{4}\,H_X^{4}
\;-\;\frac{\lambda'}{2}\,H_X^{2}\,\Phi^{\dagger}\Phi .$$

The quadratic piece $-\tfrac12 M_{H_X}^2 H_X^2$ sits in `LHXKin`, so the three terms
above complete $V \supset \lambda_\Phi\big(|\Phi_X|^2-\tfrac{v_\Phi^2}{2}\big)^2
+ \lambda'|\Phi_X|^2|\Phi|^2$ up to constants.

Term that is **absent**: the trilinear portal $-\lambda' v_\Phi H_X\,\Phi^\dagger\Phi$
that a full expansion of $\lambda'|\Phi_X|^2|\Phi|^2$ would produce. So the file
carries no $h$–$H_X$ mass mixing; $h$ and $H_X$ stay mass eigenstates and the portal
acts only through the quartic $H_X^2 |\Phi|^2$.

### `LTotal`

$$\mathcal{L} = \mathcal{L}_{\rm SM}
+\mathcal{L}_{\rm ZpKin}+\mathcal{L}_{\rm ZpF}+\mathcal{L}_{\rm NXKin}
+\mathcal{L}_{\rm HXKin}+\mathcal{L}_{\rm ZpHX}+\mathcal{L}_{\rm NYuk}
+\mathcal{L}_{\rm NuYuk}+\mathcal{L}_{\rm PotX}.$$

---

## 2. Field table

| `.fr` class | Symbol | Spin | SU(3)$_c$ | SU(2)$_L$ | $U(1)_Y$ | $U(1)_X$ charge | Self-conj. | Mass symbol | Mass value |
|---|---|---|---|---|---|---|---|---|---|
| `V[100]` | $Z'$ (`Zp`) | 1 | **1** | **1** (not declared) | 0 | 0 (gauge boson) | Yes | `MZp`, internal | $g_X\sqrt{x_{\rm Sc}^2v_\Phi^2+x_{H_d}^2v^2}\approx 7.5$ TeV |
| `S[100]` | $H_X$ | 0 | **1** | **1** (not declared) | 0 | 0 (radial mode of $\Phi_X$) | Yes (real scalar) | `MHX`, internal | $\sqrt{2\lambda_\Phi}\,v_\Phi\approx 4.19$ TeV |
| `F[100]` | $N_X^{1,2,3}$ | 1/2 | **1** | **1** (not declared) | 0 | $x_{n_R}=-x_\Phi$ (right-handed part) | Yes (Majorana) | `MNX1/2/3` | 8000 GeV each |
| `F[110]` | $N_R$ | 1/2 | **1** | **1** | 0 | $x_{n_R}$ | No | — | unphysical |

Extra data:

* $Z'$: PDG 9900032, width `WZp` = 1353 GeV, propagator `Sine`.
* $H_X$: PDG 9900025, width `WHX` = 0.1 GeV, propagator `D`.
* $N_X$: PDG 9900012 / 9900014 / 9900016, names `nx1,nx2,nx3`, full names
  RHN1..RHN3, width $10^{-10}$ GeV each, flavour index `Generation`.
* `NR` is `Unphysical -> True` with
  $N_R[{\rm sp},f] = P_R\,N_X[{\rm sp},f]$. It carries `LeptonNumber -> 1` and
  $Y=0$. It only names the right-handed chiral part of the Majorana field $N_X$.

Interaction order hierarchy: `{QCD,1}, {QED,2}, {NP,1}`.

---

## 3. Parameters

### External

| Symbol | Block / order | Value | Multiplies | Meaning |
|---|---|---|---|---|
| `gX` | `U1XINPUTS` 1, NP 1 | 0.4 | $Z'_\mu \bar f\gamma^\mu f$ and $Z'Z'H_X$ | $U(1)_X$ gauge coupling |
| `xH` | `U1XINPUTS` 2 | 2.0 | enters every $x_f$ | weight of hypercharge in the $U(1)_X$ charge |
| `xPhi` | `U1XINPUTS` 3 | 1.0 | enters every $x_f$ | weight of $B-L$ in the $U(1)_X$ charge |
| `vX` | `U1XINPUTS` 4, NP $-1$ | 9375 GeV | $M_{Z'}$, $M_{H_X}$, $y_N$, $H_X^3$ | vacuum expectation value $v_\Phi$ of the singlet $\Phi_X$ |
| `lamX` | `U1XINPUTS` 5, NP 2 | 0.1 | $H_X^3$, $H_X^4$, $M_{H_X}$ | quartic self-coupling $\lambda_\Phi$ of $\Phi_X$ |
| `lamHX` | `U1XINPUTS` 6, NP 2 | 0.01 | $H_X^2\,\Phi^\dagger\Phi$ | Higgs-portal quartic $\lambda'$ |
| `ynu` | `YUKNU`, NP 1, 3×3 | ${\rm diag}(10^{-6},10^{-6},10^{-6})$ | $\bar L_L \tilde\Phi N_R$ | Dirac neutrino Yukawa matrix $Y_\nu$ |

### Internal (charges)

| Symbol | Value | Equals $x_H Y + x_\Phi (B-L)$ for | Numeric at $x_H=2,\;x_\Phi=1$ |
|---|---|---|---|
| `xqL` | $x_H/6 + x_\Phi/3$ | $Q_L$ ($Y=1/6$, $B-L=1/3$) | $2/3$ |
| `xuR` | $2x_H/3 + x_\Phi/3$ | $u_R$ ($Y=2/3$, $B-L=1/3$) | $5/3$ |
| `xdR` | $-x_H/3 + x_\Phi/3$ | $d_R$ ($Y=-1/3$, $B-L=1/3$) | $-1/3$ |
| `xlL` | $-x_H/2 - x_\Phi$ | $L_L$ ($Y=-1/2$, $B-L=-1$) | $-2$ |
| `xeR` | $-x_H - x_\Phi$ | $e_R$ ($Y=-1$, $B-L=-1$) | $-3$ |
| `xnR` | $-x_\Phi$ | $N_R$ ($Y=0$, $B-L=-1$) | $-1$ |
| `xHd` | $x_H/2$ | Higgs doublet $\Phi$ ($Y=1/2$, $B-L=0$) | $1$ |
| `xSc` | $2x_\Phi$ | singlet $\Phi_X$ ($Y=0$, $B-L=+2$) | $2$ |

The charge set is anomaly free for any $x_H,x_\Phi$, because it is a linear
combination of two anomaly-free charges once three $N_R$ are present.

### Internal (masses and derived couplings)

| Symbol | Value | Meaning |
|---|---|---|
| `MZp` | $g_X\sqrt{x_{\rm Sc}^2 v_\Phi^2 + x_{H_d}^2 v^2}$ | $Z'$ mass; both the singlet and the doublet feed it. $\approx 7.50$ TeV |
| `MHX` | $\sqrt{2\lambda_\Phi v_\Phi^2}$ | mass of the real singlet scalar. $\approx 4.19$ TeV |
| `mNmaj` | ${\rm diag}(M_{N_1},M_{N_2},M_{N_3})$ | Majorana mass matrix of $N_X$ |
| `yN` | $\sqrt{2}\,M_{N_i}/v_\Phi\,\delta_{ij}$ | Majorana Yukawa of $\Phi_X$ to $N_X$; $\approx 1.21$ for 8 TeV |

---

## 4. Physics summary

This is a general $U(1)_X$ extension of the Standard Model. The charge of each field
is $x_H Y + x_\Phi (B-L)$, so the model interpolates between pure $B-L$ ($x_H=0$) and
other abelian extensions by one continuous parameter. The new states are a heavy
neutral gauge boson $Z'$ (7.5 TeV), a real singlet scalar $H_X$ (4.2 TeV) from the
$U(1)_X$-breaking field $\Phi_X$, and three Majorana right-handed neutrinos $N_X$
(8 TeV). The $\Phi_X$ vacuum value breaks $U(1)_X$ and lepton number and gives the
$N_X$ their Majorana mass.

The interactions are: flavour-diagonal $Z'$ currents to all SM fermions and an axial
$Z'$ current to $N_X$; a $Z'Z'H_X$ and $Z'Z'H_XH_X$ vertex; a diagonal $H_X\bar N N$
coupling set by $M_N/v_\Phi$; a Dirac Yukawa $\bar L\tilde\Phi N_R$; and a Higgs
portal $H_X^2|\Phi|^2$. With $y_\nu\sim10^{-6}$ and $M_N=8$ TeV the type-I seesaw
gives $m_\nu = m_D^2/M_N \sim 4\times10^{-3}$ eV, in the observed range.

Typical processes: Drell-Yan $Z'$ production at a hadron collider with decays to
dileptons, dijets, $t\bar t$ and $N_X N_X$; pair production of heavy neutrinos through
$Z'$ or through the small active-heavy mixing, with lepton-number-violating same-sign
dilepton final states; $H_X$ production through its mixing-free portal and decay to
$N_X N_X$ or to $Z'Z'$ when kinematically open.

### Implementation caveats a checker should note

1. No gauge kinetic mixing $B_{\mu\nu}Z'^{\mu\nu}$ and no $Z$–$Z'$ mass mixing term.
   The $Z'$ mass is inserted by hand, although the doublet contribution $x_{H_d}^2v^2$
   is kept inside `MZp`.
2. No $Z'$ coupling to the Higgs-doublet current, and no $Z'Z'h$ or $Z'Zh$ vertex.
3. The trilinear portal $-\lambda' v_\Phi H_X|\Phi|^2$ is missing, so there is no
   $h$–$H_X$ scalar mixing.
4. The light-heavy neutrino mixing is not diagonalised. The seesaw stays implicit in
   `LNuYuk` plus the Majorana mass in `LNXKin`.
