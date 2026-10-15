# Reconstruction of `sanitized.fr`

The file is an add-on module. It does not declare gauge groups, and it uses
`LSM`, `Phi`, `QL`, `uR`, `dR`, `LL`, `lR`, `CKM`, `vev` and `FeynmanGauge` from a
Standard Model (SM) base file. It adds one abelian gauge boson, one real scalar and
three Majorana fermions.

## 0. Conventions used below

* `Ga[mu]` = $\gamma^\mu$. `ProjP` = $P_R=\tfrac{1}{2}(1+\gamma_5)$, `ProjM` = $P_L=\tfrac{1}{2}(1-\gamma_5)$.
* `FS[Zp,mu,nu]` = $Z'_{\mu\nu}=\partial_\mu Z'_\nu-\partial_\nu Z'_\mu$ (abelian, no self-coupling).
* `HC[x]` = $x^\dagger$ (hermitian conjugate). `Eps[i,j]` = $\epsilon_{ij}$, the SU(2) antisymmetric symbol.
* Repeated `Generation` indices $i,j = 1,2,3$ are summed. Repeated SU(2) indices $a,b$ are summed.
* $\Phi$ is the SM Higgs doublet with vacuum value $v =$ `vev` $\simeq 246$ GeV.
  $\Phi_X$ is the new complex singlet with vacuum value $v_\Phi/\sqrt{2}$, and
  $\Phi_X = (v_\Phi + H_X)/\sqrt{2}$ in unitary gauge. Only $H_X$ appears in the file;
  the Goldstone of $\Phi_X$ is eaten by $Z'$.

### Covariant derivative

The file writes the gauge current by hand, not with `DC`. The sign of the `LZpF`
prefactor fixes the convention. The full covariant derivative is

$$
D_\mu \;=\; \partial_\mu \;-\; i g_s T^A G^A_\mu \;-\; i g\,\frac{\sigma^k}{2} W^k_\mu \;-\; i g' Y B_\mu \;+\; i g_X\, x_f\, Z'_\mu ,
$$

where $x_f$ is the U(1)$_X$ charge of the field $f$. The last term is the only new
piece. With this sign, $\bar f\,i\gamma^\mu D_\mu f$ gives $-g_X x_f Z'_\mu \bar f\gamma^\mu f$,
which is exactly the form in `LZpF`. The SM part of $D_\mu$ is unchanged.

The charges are a linear combination of hypercharge and $B-L$:

$$
x_f \;=\; x_H\, Y_f \;+\; x_\Phi\, (B-L)_f .
$$

$Z'$ is treated as a mass eigenstate. The file adds no kinetic mixing term and no
explicit $Z$–$Z'$ mixing term. The $Z$–$Z'$ mixing enters only through the $x_{H_d}^2 v^2$
piece of $M_{Z'}$.

---

## 1. Lagrangian, term by term

Total (`LTotal`):

$$
\mathcal{L} = \mathcal{L}_{\rm SM} + \mathcal{L}_{Z'{\rm kin}} + \mathcal{L}_{Z'F} + \mathcal{L}_{N{\rm kin}} + \mathcal{L}_{H_X{\rm kin}} + \mathcal{L}_{Z'H_X} + \mathcal{L}_{N{\rm Yuk}} + \mathcal{L}_{\nu{\rm Yuk}} + \mathcal{L}_{V_X}
$$

### `LZpKin` — $Z'$ kinetic and mass term

$$
\mathcal{L}_{Z'{\rm kin}} \;=\; -\frac{1}{4}\,Z'_{\mu\nu}Z'^{\mu\nu} \;+\; \frac{1}{2}\,M_{Z'}^{2}\,Z'_\mu Z'^{\mu}
$$

The mass term is put in by hand. It is the value that the two vacuum values produce
(see `MZp` in Section 3). The $Z'$ mass term from $\Phi_X$ is therefore counted once,
not twice: `LZpHX` keeps only the $H_X$-dependent parts.

### `LZpF` — $Z'$ current of the fermions

$$
\mathcal{L}_{Z'F} \;=\; -\,g_X\,Z'_\mu \Big[
 x_{q_L}\,\bar Q_L^{\,i}\gamma^\mu Q_L^{\,i}
+x_{u_R}\,\bar u_R^{\,i}\gamma^\mu u_R^{\,i}
+x_{d_R}\,\bar d_R^{\,i}\gamma^\mu d_R^{\,i}
+x_{\ell_L}\,\bar L_L^{\,i}\gamma^\mu L_L^{\,i}
+x_{e_R}\,\bar e_R^{\,i}\gamma^\mu e_R^{\,i}
+x_{n_R}\,\bar N_R^{\,i}\gamma^\mu N_R^{\,i}\Big]
$$

Details that the physicist must check:

* The current is purely vector for each chirality block, and flavour diagonal.
* `FlavorExpand -> {SU2D}` expands the SU(2) doublets into components:
  $\bar Q_L\gamma^\mu Q_L = \bar u_L\gamma^\mu u_L + \bar d_L\gamma^\mu d_L$ (with CKM rotation), and
  $\bar L_L\gamma^\mu L_L = \bar \nu_L\gamma^\mu \nu_L + \bar e_L\gamma^\mu e_L$.
* The replacement rules $V_{ab}V^*_{ac}\to\delta_{bc}$ and $V_{ba}V^*_{ca}\to\delta_{bc}$
  apply CKM unitarity. So no flavour-changing $Z'$ coupling survives.
* The last term uses $N_R$, which is the right-chiral part of the Majorana field (see
  below). With $N_R = P_R N_X$ and $\overline{N_R} = \bar N_X P_L$:

$$
\bar N_R^{\,i}\gamma^\mu N_R^{\,i} \;=\; \bar N_X^{\,i}\,\gamma^\mu P_R\,N_X^{\,i}.
$$

### `LNXKin` — Majorana kinetic and mass term

$$
\mathcal{L}_{N{\rm kin}} \;=\; \frac{i}{2}\,\bar N_X^{\,i}\gamma^\mu \partial_\mu N_X^{\,i}
\;-\;\frac{1}{2}\,\bar N_X^{\,i}\,(m_N)_{ij}\,N_X^{\,j}
$$

The factors $\tfrac12$ are the standard Majorana normalisation. $(m_N)_{ij} = {\rm diag}(M_{N_1},M_{N_2},M_{N_3})$.
The derivative is the plain $\partial_\mu$: the file gives the gauge current separately, in `LZpF`.

### `LHXKin` — real singlet scalar

$$
\mathcal{L}_{H_X{\rm kin}} \;=\; \frac{1}{2}\,\partial_\mu H_X\,\partial^\mu H_X \;-\;\frac{1}{2}\,M_{H_X}^{2}\,H_X^{2}
$$

### `LZpHX` — $Z'$–scalar gauge couplings

$$
\mathcal{L}_{Z'H_X} \;=\; g_X^{2}\,x_{S_c}^{2}\left(v_\Phi H_X + \frac{1}{2}H_X^{2}\right) Z'_\mu Z'^{\mu}
$$

This is the $H_X$-dependent remainder of $|D_\mu \Phi_X|^2$ with $x_{S_c}=2x_\Phi$ the charge of
$\Phi_X$. The constant piece $\tfrac12 g_X^2 x_{S_c}^2 v_\Phi^2 Z'_\mu Z'^\mu$ is not repeated here,
because `LZpKin` already carries the full $Z'$ mass.

### `LNYuk` — Majorana Yukawa with the singlet

$$
\mathcal{L}_{N{\rm Yuk}} \;=\; -\frac{1}{2\sqrt{2}}\,H_X\,\bar N_X^{\,i}\,(y_N)_{ij}\,N_X^{\,j}
\;=\; -\frac{1}{2}\,\frac{M_{N_i}}{v_\Phi}\,H_X\,\bar N_X^{\,i} N_X^{\,i}
$$

The second form uses $(y_N)_{ij}=\sqrt{2}M_{N_i}\delta_{ij}/v_\Phi$. The coupling is a scalar
bilinear, with no $\gamma_5$ and no chiral projector.

### `LNuYuk` — Dirac (neutrino) Yukawa

$$
\mathcal{L}_{\nu{\rm Yuk}} \;=\; -\,(y_\nu)_{ij}\;\overline{L_L^{\,i}}{}_{a}\,\epsilon_{ab}\,\Phi^{*}_{b}\;P_R N_X^{\,j} \;+\; \mathrm{h.c.}
$$

Equivalently, with $\tilde\Phi_a \equiv \epsilon_{ab}\Phi^*_b$:

$$
\mathcal{L}_{\nu{\rm Yuk}} \;=\; -\,(y_\nu)_{ij}\,\overline{L_L^{\,i}}\,\tilde\Phi\,N_R^{\,j}
\;-\;(y_\nu)^{*}_{ij}\,\overline{N_R^{\,j}}\,\tilde\Phi^{\dagger}\,L_L^{\,i}
$$

Details:

* `NR[sp,ff]` is defined as $P_R N_X$, so the right side of the bilinear is right-chiral,
  and the left side is left-chiral. The Lorentz index `sp` is shared, so the two spinors
  contract directly (no $\gamma$ matrix).
* The contraction with $\epsilon_{ab}$ and $\Phi^\dagger$ is the "charge conjugate Higgs"
  contraction. It is the one that makes the term U(1)$_X$ and hypercharge neutral:
  $x_{\ell_L} - x_{H_d} + x_{n_R} = (-x_H/2-x_\Phi)-(x_H/2)+(-x_\Phi)$ — this does not vanish
  for general $x_H$. With $\tilde\Phi$ the doublet enters with charge $-x_{H_d}$:
  $-x_{\ell_L} + x_{H_d} + x_{n_R}$ is not zero either. See the note in Section 5.
* After electroweak symmetry breaking this gives the Dirac mass $m_D = y_\nu v/\sqrt{2}$.
* `feynmangaugerules` removes the Goldstone fields $G^0,G^+$ when `FeynmanGauge` is `False`.

### `LPotX` — scalar potential of the singlet

$$
\mathcal{L}_{V_X} \;=\; -\,\lambda_\Phi v_\Phi H_X^{3} \;-\;\frac{\lambda_\Phi}{4}H_X^{4}\;-\;\frac{\lambda'}{2}\,H_X^{2}\,\Phi^{\dagger}_{a}\Phi_{a}
$$

This is what is left of $V = \lambda_\Phi\left(|\Phi_X|^2 - v_\Phi^2/2\right)^2 + \lambda'|\Phi_X|^2|\Phi|^2$
after the mass term is moved to `LHXKin`. The trilinear portal term
$-\tfrac{\lambda'}{2}\,2 v_\Phi H_X \Phi^\dagger\Phi$ is **not** in the file. So $h$–$H_X$ mass
mixing is absent, and the portal acts only through the $H_X^2 h^2$ quartic.

---

## 2. Field table

| Symbol | Class | Spin | SU(3)$_c$ | SU(2)$_L$ | $Y$ | U(1)$_X$ charge | Self-conj. | Mass symbol | Value |
|---|---|---|---|---|---|---|---|---|---|
| $Z'$ (`Zp`) | `V[100]` | 1 | **1** | **1** | 0 | 0 (gauge boson) | yes | `MZp` (internal) | $\simeq 7.50$ TeV |
| $H_X$ (`HX`) | `S[100]` | 0 | **1** | **1** | 0 | 0 (real part of $\Phi_X$) | yes | `MHX` (internal) | see Section 3 |
| $N_X^{1,2,3}$ (`NX`) | `F[100]` | 1/2 | **1** | **1** | 0 | $x_{n_R}=-x_\Phi$ (right-chiral part) | yes (Majorana) | `MNX1/2/3` | 8000 GeV each |
| $N_R$ (`NR`) | `F[110]` | 1/2 | **1** | **1** | 0 | $x_{n_R}=-x_\Phi$ | no | — (unphysical) | — |

Notes:

* No SU(3) or SU(2) representation is declared for any new field. All are singlets.
* `NR` is `Unphysical -> True`. It is only a shorthand: $N_R[s,f] = P_R\,N_X[s,f]$. It carries
  `LeptonNumber -> 1` and `Y -> 0`.
* Widths: $W_{Z'} = 1353$ GeV, $W_{H_X}=0.1$ GeV, $W_{N_i}=10^{-10}$ GeV.
* PDG codes: $Z'$ 9900032, $H_X$ 9900025, $N_{1,2,3}$ 9900012 / 9900014 / 9900016.
* The parent complex singlet $\Phi_X$ has charge $x_{S_c}=2x_\Phi$. Its imaginary part is the
  Goldstone eaten by $Z'$, and it is not declared as a field.

---

## 3. Parameters

### External parameters

| Symbol | Block / order | Value | Multiplies | Meaning |
|---|---|---|---|---|
| `gX` $= g_X$ | `U1XINPUTS` 1 | 0.4 | the $Z'$ current `LZpF`, and $g_X^2$ in `LZpHX` | U(1)$_X$ gauge coupling, `NP` order 1 |
| `xH` $= x_H$ | `U1XINPUTS` 2 | 2.0 | the hypercharge part of every $x_f$ | mixing parameter between U(1)$_Y$ and U(1)$_X$; dimensionless charge |
| `xPhi` $= x_\Phi$ | `U1XINPUTS` 3 | 1.0 | the $B-L$ part of every $x_f$ | overall $B-L$ charge unit; dimensionless charge |
| `vX` $= v_\Phi$ | `U1XINPUTS` 4 | 9375 GeV | `LZpHX` trilinear, $H_X^3$ term, $M_{Z'}$, $y_N$ | vacuum value of the singlet, i.e. the U(1)$_X$ breaking scale; `NP` order $-1$ |
| `lamX` $= \lambda_\Phi$ | `U1XINPUTS` 5 | 0.1 | $H_X^3$ and $H_X^4$ in `LPotX` | singlet quartic self-coupling |
| `lamHX` $= \lambda'$ | `U1XINPUTS` 6 | 0.01 | $H_X^2\,\Phi^\dagger\Phi$ in `LPotX` | Higgs-portal quartic coupling |
| `ynu` $= (y_\nu)_{ij}$ | `YUKNU` | $10^{-6}\,\delta_{ij}$ | $\bar L_L \tilde\Phi N_R$ in `LNuYuk` | Dirac neutrino Yukawa matrix, $3\times3$, diagonal |
| `MNX1/2/3` | mass block | 8000 GeV | `mNmaj`, `yN` | Majorana masses of the three heavy neutrinos |

### Internal (derived) parameters

| Symbol | Definition | Numeric value with the defaults |
|---|---|---|
| `xqL` | $x_H/6 + x_\Phi/3$ | $2/3$ |
| `xuR` | $2x_H/3 + x_\Phi/3$ | $5/3$ |
| `xdR` | $-x_H/3 + x_\Phi/3$ | $-1/3$ |
| `xlL` | $-x_H/2 - x_\Phi$ | $-2$ |
| `xeR` | $-x_H - x_\Phi$ | $-3$ |
| `xnR` | $-x_\Phi$ | $-1$ |
| `xHd` | $x_H/2$ | $1$ |
| `xSc` | $2x_\Phi$ | $2$ |
| `MZp` | $g_X\sqrt{x_{S_c}^2 v_\Phi^2 + x_{H_d}^2 v^2}$ | $\simeq 7501$ GeV |
| `MHX` | **as written:** $1/\sqrt{2\lambda_\Phi v_\Phi^2}$ | $2.4\times10^{-4}\ {\rm GeV}^{-1}$ |
| `mNmaj` | ${\rm diag}(M_{N_1},M_{N_2},M_{N_3})$ | ${\rm diag}(8000,8000,8000)$ GeV |
| `yN` | $\sqrt{2}\,M_{N_i}\,\delta_{ij}/v_\Phi$ | $1.207\,\delta_{ij}$ |

Each $x_f$ satisfies $x_f = x_H Y_f + x_\Phi (B-L)_f$. You can verify this line by line:
$Q_L$ has $Y=1/6,\,B-L=1/3$; $u_R$ has $Y=2/3$; $d_R$ has $Y=-1/3$; $L_L$ has $Y=-1/2,\,B-L=-1$;
$e_R$ has $Y=-1$; $N_R$ has $Y=0,\,B-L=-1$; $\Phi$ has $Y=1/2,\,B-L=0$; $\Phi_X$ has $B-L=2$.

---

## 4. Physics summary

This is a general (non-minimal) U(1)$_X$ extension of the Standard Model. The new charge is
a free linear combination of hypercharge and $B-L$, set by the two numbers $x_H$ and $x_\Phi$;
$x_H=0$ would give pure $B-L$. A complex scalar singlet $\Phi_X$ with charge $2x_\Phi$ breaks
U(1)$_X$ at $v_\Phi \simeq 9.4$ TeV. It leaves one heavy $Z'$ (about 7.5 TeV), one real singlet
scalar $H_X$, and three Majorana right-handed neutrinos $N_{1,2,3}$ at 8 TeV, whose masses
come from the same vacuum value through $y_N = \sqrt2 M_N/v_\Phi$. The three $N_i$ make the
U(1)$_X$ gauge anomalies cancel for any $x_H$ and $x_\Phi$.

The model gives light neutrino masses by the type-I seesaw: the Dirac Yukawa $y_\nu\sim10^{-6}$
plus $M_N = 8$ TeV gives $m_\nu \sim m_D^2/M_N \sim 4\times10^{-3}$ eV. The processes it mediates are:
Drell-Yan $Z'$ production at a hadron collider with decays to all SM fermion pairs and to
$N_iN_i$; $Z'\to Z' H_X$-type gauge-scalar vertices; $H_X$ production through the $Z'Z'H_X$ and
$H_X N\bar N$ vertices, and through the Higgs portal $\lambda'$; and $N_i$ decay to $W\ell$, $Zν$
and $h\nu$ through the small Dirac mixing, which gives lepton-number-violating same-sign
dilepton signatures.

---

## 5. Two points the file gets wrong (please check)

1. **`MHX` is dimensionally wrong.** The file has

   `MHX -> 1/Sqrt[2 lamX vX^2]`, that is $M_{H_X} = \left(\sqrt{2\lambda_\Phi}\,v_\Phi\right)^{-1}$.

   A mass cannot be an inverse mass. The potential $V=\lambda_\Phi(|\Phi_X|^2-v_\Phi^2/2)^2$ gives
   $M_{H_X}^2 = 2\lambda_\Phi v_\Phi^2$, so the correct value is

   $$M_{H_X} \;=\; \sqrt{2\lambda_\Phi v_\Phi^2} \;=\;\sqrt{2\lambda_\Phi}\,v_\Phi \;\simeq\; 4193\ \text{GeV}.$$

   The file's form evaluates to $2.4\times10^{-4}$ instead of $4193$. The numerator `1/` and the
   square root are swapped: the reciprocal does not belong there. Every $H_X$ propagator and
   every decay that uses $M_{H_X}$ is affected.

2. **The portal trilinear is missing.** $\lambda'|\Phi_X|^2|\Phi|^2$ also produces
   $-\lambda' v_\Phi H_X \Phi^\dagger\Phi$. `LPotX` keeps only the $H_X^2\Phi^\dagger\Phi$ quartic.
   This may be a deliberate choice (no $h$–$H_X$ mixing), but it is not the full expansion.

A third point is a convention, not an error: for general $x_H\neq 0$ the term `LNuYuk` is not
U(1)$_X$ invariant unless the charge sum $-x_{\ell_L}+x_{H_d}+x_{n_R}$ vanishes. With
$x_{\ell_L}=-x_H/2-x_\Phi$, $x_{H_d}=x_H/2$ and $x_{n_R}=-x_\Phi$ this sum is
$(x_H/2+x_\Phi)+(x_H/2)+(-x_\Phi) = x_H$. So the Dirac Yukawa is U(1)$_X$ invariant only for
$x_H=0$ (pure $B-L$), yet the default value is $x_H=2$. Check the intended charge of $\tilde\Phi$
against the source model.
