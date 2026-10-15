# Reconstruction of `sanitized.fr`

The file adds a new abelian gauge group to the Standard Model. Call it
$U(1)_X$, with gauge boson $Z'$, gauge coupling $g_X$, and a family of
charges $x_f$ built from two free numbers $x_H$ and $x_\Phi$. It also adds
one real scalar $H_X$ (the radial mode of a SM-singlet scalar $\Phi$ whose
vacuum expectation value is $v_X$) and three Majorana fermions $N_X^{1,2,3}$
(right-handed neutrinos). The SM part is imported through `LSM`; only the new
terms are written here.

Throughout, $i,j$ are generation indices, $\alpha,\beta$ are $SU(2)_L$ indices,
and color indices are suppressed (all new states are color singlets).

---

## 1. Gauge structure and the covariant derivative

The charges are internal parameters:

$$
x_{q_L}=\tfrac{x_H}{6}+\tfrac{x_\Phi}{3},\quad
x_{u_R}=\tfrac{2x_H}{3}+\tfrac{x_\Phi}{3},\quad
x_{d_R}=-\tfrac{x_H}{3}+\tfrac{x_\Phi}{3},
$$

$$
x_{\ell_L}=-\tfrac{x_H}{2}-x_\Phi,\quad
x_{e_R}=-x_H-x_\Phi,\quad
x_{n_R}=-x_\Phi,\quad
x_{H_d}=\tfrac{x_H}{2},\quad
x_{Sc}=2x_\Phi .
$$

Every entry equals $x_f = x_H\,Y_f + x_\Phi\,(B-L)_f$. So $U(1)_X$ is a linear
combination of SM hypercharge and $B-L$. The choice $x_H=0$ gives pure $B-L$;
$x_\Phi=0$ gives pure hypercharge. With three right-handed neutrinos this
combination is anomaly free for any $x_H,x_\Phi$.

The full covariant derivative implied by the file is

$$
D_\mu = \partial_\mu
- i g_s T^a G^a_\mu
- i g\,T^I W^I_\mu
- i g' Y B_\mu
+ i g_X\, x_f\, Z'_\mu .
$$

The sign of the last term is fixed by the explicit `-gX Zp[mu] ...` in `LZpF`
(see Term 2). It is the opposite sign convention to the other three; it is
equivalent to $Z'\to -Z'$ and has no physical effect.

Two structural points:

- **No kinetic mixing.** There is no $-\tfrac{\epsilon}{2}B^{\mu\nu}Z'_{\mu\nu}$
  term. $Z'$ reaches the SM only through the charges $x_f$.
- **No explicit $Z$–$Z'$ or $Z'$–$h$ vertex.** The SM Higgs doublet carries
  $x_{H_d}=x_H/2$ and its vacuum expectation value enters $M_{Z'}$ (Section 4),
  but the corresponding $|D_\mu H|^2$ cross terms are not written in this file.

The scalar sector uses $\Phi = \frac{1}{\sqrt{2}}\,(v_X + H_X)$, a SM singlet
with $x_{Sc}=2x_\Phi$. Its Goldstone mode is eaten by $Z'$; only the real
scalar $H_X$ remains.

---

## 2. Lagrangian, term by term

$$
\mathcal{L}_{\rm total}=\mathcal{L}_{\rm SM}
+\mathcal{L}_{Z'{\rm kin}}+\mathcal{L}_{Z'F}+\mathcal{L}_{N_X{\rm kin}}
+\mathcal{L}_{H_X{\rm kin}}+\mathcal{L}_{Z'H_X}+\mathcal{L}_{N{\rm Yuk}}
+\mathcal{L}_{\nu{\rm Yuk}}+\mathcal{L}_{{\rm pot}X}
$$

### Term 1 — `LZpKin`: $Z'$ kinetic and mass term

$$
\mathcal{L}_{Z'{\rm kin}}
= -\frac{1}{4}\,Z'_{\mu\nu}Z'^{\mu\nu}
+ \frac{1}{2}\,M_{Z'}^{2}\,Z'_\mu Z'^{\mu},
\qquad
Z'_{\mu\nu}=\partial_\mu Z'_\nu-\partial_\nu Z'_\mu .
$$

`FS[Zp,mu,nu]` is the abelian field strength, so there is no $Z'$ self
interaction. The mass term is written by hand; it is the value the Higgs
mechanism produces (Section 4).

### Term 2 — `LZpF`: $Z'$ current

$$
\mathcal{L}_{Z'F} = -\,g_X\,Z'_\mu \Big[
 x_{q_L}\,\bar{Q}_L^{\,i}\gamma^\mu Q_L^{\,i}
+x_{u_R}\,\bar{u}_R^{\,i}\gamma^\mu u_R^{\,i}
+x_{d_R}\,\bar{d}_R^{\,i}\gamma^\mu d_R^{\,i}
$$
$$
\qquad\qquad
+\,x_{\ell_L}\,\bar{L}_L^{\,i}\gamma^\mu L_L^{\,i}
+x_{e_R}\,\bar{e}_R^{\,i}\gamma^\mu e_R^{\,i}
+x_{n_R}\,\bar{N}_R^{\,i}\gamma^\mu N_R^{\,i}\Big].
$$

Details of the FeynRules idioms:

- `Ga[mu]` is $\gamma^\mu$; `QLbar.Ga[mu].QL` is a Dirac bilinear with the
  spinor chain contracted left to right.
- $Q_L$ and $L_L$ are the left-handed $SU(2)_L$ doublets; $u_R,d_R,e_R$ are the
  right-handed singlets. Chirality is carried by the fields themselves, so the
  current is $\bar f_{L,R}\gamma^\mu f_{L,R}$ — it is **not** vector-like.
  Written on Dirac fields: $x_{q_L}\bar q\gamma^\mu P_L q$, and so on.
- `FlavorExpand -> {SU2D}` writes the doublets out in components
  ($Q_L\to(u_L,\,V_{\rm CKM}d_L)$, $L_L\to(\nu_L,\,e_L)$). The replacement rules
  $V_{ab}V^*_{ac}\to\delta_{bc}$ and $V_{ba}V^*_{ca}\to\delta_{bc}$ then apply
  CKM unitarity. The $Z'$ current is therefore **flavour diagonal**: no
  tree-level flavour changing neutral current.
- Generation indices are summed diagonally; the charges are generation
  universal.

The last piece uses the unphysical field $N_R = P_R N_X$, so
$\bar N_R\gamma^\mu N_R = \bar N_X\gamma^\mu P_R N_X$. Because $N_X$ is
Majorana, $\bar N_X\gamma^\mu N_X=0$ and this reduces to a pure axial current:

$$
-\,g_X\,x_{n_R}\,Z'_\mu\,\bar N_X^{\,i}\gamma^\mu P_R N_X^{\,i}
= -\,\frac{g_X x_{n_R}}{2}\,Z'_\mu\,\bar N_X^{\,i}\gamma^\mu\gamma_5 N_X^{\,i}.
$$

### Term 3 — `LNXKin`: Majorana kinetic and mass term

$$
\mathcal{L}_{N_X{\rm kin}}
= \frac{i}{2}\,\bar N_X^{\,i}\gamma^\mu\partial_\mu N_X^{\,i}
- \frac{1}{2}\,\bar N_X^{\,i}\,(m_N)_{ij}\,N_X^{\,j},
\qquad
m_N={\rm diag}(M_{N_1},M_{N_2},M_{N_3}).
$$

The factors of $1/2$ are the standard Majorana normalisation. The mass matrix
is diagonal, so the three heavy neutrinos are already mass eigenstates.

### Term 4 — `LHXKin`: real scalar kinetic and mass term

$$
\mathcal{L}_{H_X{\rm kin}}
= \frac{1}{2}\,\partial_\mu H_X\,\partial^\mu H_X
- \frac{1}{2}\,M_{H_X}^{2}\,H_X^{2}.
$$

### Term 5 — `LZpHX`: $Z'$–$H_X$ gauge interactions

$$
\mathcal{L}_{Z'H_X}
= g_X^{2}\,x_{Sc}^{2}\Big(v_X H_X + \tfrac{1}{2}H_X^{2}\Big)\,Z'_\mu Z'^{\mu}.
$$

This is the remainder of $|D_\mu\Phi|^2$ after the mass term of Term 1 is
split off: with $\Phi=(v_X+H_X)/\sqrt{2}$,
$|D_\mu\Phi|^2 \supset \tfrac{1}{2}g_X^2x_{Sc}^2(v_X+H_X)^2 Z'_\mu Z'^\mu$.
It gives the $Z'Z'H_X$ and $Z'Z'H_XH_X$ vertices.

### Term 6 — `LNYuk`: $H_X$ coupling to the heavy neutrinos

$$
\mathcal{L}_{N{\rm Yuk}}
= -\frac{1}{2\sqrt{2}}\,H_X\;\bar N_X^{\,i}\,(Y_N)_{ij}\,N_X^{\,j},
\qquad
(Y_N)_{ij} = \frac{\sqrt{2}\,M_{N_i}}{v_X}\,\delta_{ij}.
$$

Numerically this is $-\tfrac{1}{2}\,(M_{N_i}/v_X)\,H_X\,\bar N_X^i N_X^i$,
the correct partner of the Majorana mass term: both come from
$-\tfrac{1}{2\sqrt2}Y_N\,\Phi\,\overline{N^c_R}N_R + {\rm h.c.}$ with
$\langle\Phi\rangle=v_X/\sqrt2$.

### Term 7 — `LNuYuk`: Dirac neutrino Yukawa

$$
\mathcal{L}_{\nu{\rm Yuk}}
= -\,(Y_\nu)_{ij}\;\bar L_L^{\,\alpha,i}\,N_R^{\,j}\;
\epsilon_{\alpha\beta}\,H^{*\beta}
\;+\;{\rm h.c.}
$$

Equivalently, with $\tilde H \equiv i\sigma^2 H^{*}$,

$$
\mathcal{L}_{\nu{\rm Yuk}}
= -\,(Y_\nu)_{ij}\;\bar L_L^{\,i}\,\tilde H\,P_R N_X^{\,j}
\;-\;(Y_\nu)^{*}_{ij}\;\bar N_X^{\,j}\,P_L\,\tilde H^{\dagger} L_L^{\,i}.
$$

Points of detail:

- `NR[sp,ff]` is defined as $P_R N_X$, so the operator is explicitly
  right-chiral: $\bar L_L \dots P_R N_X$. `HC` supplies the hermitian
  conjugate, which is left-chiral: $\bar N_X P_L \dots L_L$.
- `Eps[ii,jj]` with `Phibar[jj]` is the $SU(2)$ antisymmetric contraction that
  turns $H^\dagger$ into the hypercharge $-1/2$ doublet $\tilde H$. Index order
  is $\epsilon_{\alpha\beta}$ with $\alpha$ on $\bar L_L$ and $\beta$ on
  $H^{*}$.
- `feynmangaugerules` sets the Goldstone fields $G^0,G^\pm$ to zero in unitary
  gauge. It is bookkeeping only, not physics.
- After electroweak symmetry breaking this gives the Dirac mass
  $m_D = Y_\nu v/\sqrt2$, which together with $m_N$ produces a type-I seesaw
  for the light neutrinos.

### Term 8 — `LPotX`: scalar potential

$$
\mathcal{L}_{{\rm pot}X}
= -\,\lambda_\Phi v_X H_X^{3}
\;-\;\frac{\lambda_\Phi}{4}H_X^{4}
\;-\;\frac{\lambda'}{2}\,H_X^{2}\,\big(H^{\dagger}H\big).
$$

These are the terms left over from
$V \supset \lambda_\Phi|\Phi|^4 + \lambda'|\Phi|^2|H|^2$ after the vacuum
expectation value is inserted and the $H_X$ mass term (Term 4) is separated.
The cubic self coupling is fixed by $\lambda_\Phi$ and $v_X$, as expected.

---

## 3. Field table

| Symbol | Class | Spin | $SU(3)_C$ | $SU(2)_L$ | $U(1)_Y$ | $U(1)_X$ charge | Self-conj. | Mass symbol | Mass value |
|---|---|---|---|---|---|---|---|---|---|
| $Z'$ | `V[100]`, `Zp` | 1 | **1** | **1** | 0 | 0 (the gauge boson) | yes | `MZp` (internal) | $g_X\sqrt{x_{Sc}^2v_X^2+x_{H_d}^2v^2}\approx 7501$ GeV |
| $H_X$ | `S[100]`, `HX` | 0 | **1** | **1** | 0 | 0 (radial mode of $\Phi$, $x_{Sc}=2x_\Phi$) | yes (real) | `MHX` (internal) | $\sqrt{2\lambda_\Phi v_X^2}\approx 4193$ GeV |
| $N_X^{1,2,3}$ | `F[100]`, `NX` | 1/2 | **1** | **1** | 0 | $x_{n_R}=-x_\Phi$ (right chirality) | yes (Majorana) | `MNX1,2,3` | 8000 GeV each |
| $N_R^{1,2,3}$ | `F[110]`, `NR` | 1/2 | **1** | **1** | 0 | $x_{n_R}=-x_\Phi$ | no | — (unphysical) | — |

Notes on the table:

- `NR` is `Unphysical -> True`. It is not a new degree of freedom; it is the
  shorthand $N_R \equiv P_R N_X$ used to write chiral operators. It declares
  `QuantumNumbers -> {Y -> 0, LeptonNumber -> -1}`.
- Widths in the file: $\Gamma_{Z'}=1353$ GeV, $\Gamma_{H_X}=0.1$ GeV,
  $\Gamma_{N_i}=10^{-10}$ GeV.
- PDG codes: $Z'$ 9900032, $H_X$ 9900025, $N_{1,2,3}$ 9900012 / 9900014 /
  9900016.
- Only $Z'$, $H_X$ and $N_i$ are physical new states. The complex scalar
  $\Phi$ never appears as a field; its charged-under-$U(1)_X$ phase is eaten.

Numeric charges at the default point $x_H=2$, $x_\Phi=1$:

| $x_{q_L}$ | $x_{u_R}$ | $x_{d_R}$ | $x_{\ell_L}$ | $x_{e_R}$ | $x_{n_R}$ | $x_{H_d}$ | $x_{Sc}$ |
|---|---|---|---|---|---|---|---|
| $2/3$ | $5/3$ | $-1/3$ | $-2$ | $-3$ | $-1$ | $1$ | $2$ |

---

## 4. Parameters

### External

| Symbol | Block / order | Value | Multiplies | Meaning |
|---|---|---|---|---|
| `gX` | `U1XINPUTS` 1, NP 1 | 0.4 | the whole $Z'$ current and $Z'Z'H_X$ | $U(1)_X$ gauge coupling |
| `xH` | `U1XINPUTS` 2 | 2.0 | the hypercharge part of every $x_f$ | mixing angle between $U(1)_Y$ and $U(1)_{B-L}$ inside $U(1)_X$ |
| `xPhi` | `U1XINPUTS` 3 | 1.0 | the $B-L$ part of every $x_f$ | overall normalisation of the $B-L$ component |
| `vX` | `U1XINPUTS` 4, NP $-1$ | 9375 GeV | $M_{Z'}$, $M_{H_X}$, $Y_N$, the $H_X^3$ term | vacuum expectation value of the singlet $\Phi$; sets the $U(1)_X$ breaking scale |
| `lamX` | `U1XINPUTS` 5, NP 2 | 0.1 | $H_X^3$ and $H_X^4$; sets $M_{H_X}$ | quartic self coupling $\lambda_\Phi$ of $\Phi$ |
| `lamHX` | `U1XINPUTS` 6, NP 2 | 0.01 | $H_X^2\,H^\dagger H$ | Higgs portal coupling $\lambda'$ between $\Phi$ and the SM doublet |
| `ynu` | `YUKNU`, NP 1 | $10^{-6}\,\delta_{ij}$ | $\bar L_L\tilde H N_R$ | Dirac neutrino Yukawa matrix $Y_\nu$ ($3\times3$, generation indices) |

### Internal (derived)

| Symbol | Value | Meaning |
|---|---|---|
| `xqL, xuR, xdR, xlL, xeR, xnR, xHd, xSc` | $x_H Y + x_\Phi (B-L)$ | $U(1)_X$ charges of the SM fields, $N_R$, the Higgs doublet and $\Phi$ |
| `MZp` | $g_X\sqrt{x_{Sc}^2v_X^2 + x_{H_d}^2 v^2}$ | $Z'$ mass from both vacuum expectation values ($v$ = SM `vev`) |
| `MHX` | $\sqrt{2\lambda_\Phi v_X^2}$ | mass of the singlet scalar |
| `mNmaj` | ${\rm diag}(M_{N_1},M_{N_2},M_{N_3})$ | Majorana mass matrix of $N_X$ |
| `yN` | $\sqrt2 M_{N_i}/v_X\,\delta_{ij} \approx 1.21\,\delta_{ij}$ | Majorana Yukawa coupling to $H_X$ |

Interaction order counting: `NP` is the new-physics order. `gX` and `ynu` and
`yN` each carry NP 1, `lamX` and `lamHX` carry NP 2, and `vX` carries NP $-1$
so that $M_{Z'}\propto g_X v_X$ counts as NP 0. The hierarchy is
`{{QCD,1},{QED,2},{NP,1}}`.

---

## 5. Physics summary

This is a minimal, anomaly-free $U(1)_X$ extension of the Standard Model, where
$U(1)_X$ is the general linear combination $x_H Y + x_\Phi (B-L)$. It adds a
heavy neutral gauge boson $Z'$ (about 7.5 TeV here), one real singlet scalar
$H_X$ (about 4.2 TeV) from the symmetry-breaking field $\Phi$, and three
Majorana right-handed neutrinos $N_X^{1,2,3}$ (8 TeV each) whose masses come
from $\langle\Phi\rangle=v_X/\sqrt2$. The light neutrinos get a type-I seesaw
mass from the Dirac Yukawa $Y_\nu$ together with the Majorana mass $m_N$.

At a collider the model gives Drell-Yan $Z'$ production, $q\bar q\to Z'$, with
generation-universal and flavour-diagonal decays to all SM fermion pairs and
to $N_X N_X$ (an axial coupling). It also gives $Z'\to Z' H_X$-type gauge-scalar
vertices, $H_X$ production through the Higgs portal $\lambda'$, and
lepton-number-violating same-sign dilepton signatures from the Majorana $N_X$
(for example $pp\to Z'\to N_XN_X\to \ell^\pm\ell^\pm W^\mp W^\mp$). Because the
charges depend on $x_H$ and $x_\Phi$, the relative $Z'$ branching ratios to
left- and right-handed fermions are tunable, and the pure $B-L$ limit is
$x_H=0$.

---

## 6. Notes for the checker

Three observations that follow only from the file's own content:

1. **Lepton number of `NR`.** `NR` declares `LeptonNumber -> -1`. The Dirac
   Yukawa in `LNuYuk` contracts $\bar L_L$ (lepton number $+1$ on the bar side,
   so $-1$ from the conjugate) with $N_R$. With $L(N_R)=-1$ that vertex carries
   $\Delta L = -2$ rather than conserving lepton number. The usual assignment
   for a right-handed neutrino that pairs with $L_L$ through $\tilde H$ is
   $L(N_R)=+1$. This declaration is FeynRules bookkeeping for conserved-charge
   checks; it does not change any vertex, but it is inconsistent with the
   Yukawa term written in the same file, and it is also inconsistent with
   $x_{n_R}=-x_\Phi$, which is exactly the $B-L=-1$ assignment used for all
   other fermions.

2. **No $H_X\,H^\dagger H$ trilinear.** `LPotX` contains only
   $-\tfrac{\lambda'}{2}H_X^2 H^\dagger H$. The term
   $-\lambda' v_X H_X H^\dagger H$, which comes from the same
   $\lambda'|\Phi|^2|H|^2$ operator, is absent. Without it there is no
   tree-level $h$–$H_X$ mass mixing in this file.

3. **No explicit $Z'$–Higgs-doublet vertex.** $x_{H_d}=x_H/2$ enters `MZp`, so
   the doublet is charged under $U(1)_X$, but the corresponding pieces of
   $|D_\mu H|^2$ ($Z'$–$Z$ mixing, $Z'Z'h$, $Z'Zh$) are not written. The $Z'$
   mass therefore knows about the electroweak vacuum expectation value while
   the interactions do not.
