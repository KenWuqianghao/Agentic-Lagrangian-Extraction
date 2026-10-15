# Reconstruction of `sanitized.fr`

## 0. Conventions used below

The file declares no `SU(2)` index and no hypercharge. It declares only `Index[Colour]`
and the electric charge `Q`. The model is therefore written in the **broken phase**: the
unbroken gauge group is

$$
SU(3)_C \times U(1)_{\rm em},
$$

and every covariant derivative `DC` expands to

$$
D_\mu = \partial_\mu \;-\; i\,g_s\,T^a\,G^a_\mu \;-\; i\,e\,Q\,A_\mu ,
$$

with $T^a$ the $SU(3)$ generators in the fundamental representation, $G^a_\mu$ the gluon,
$A_\mu$ the photon, and $Q$ the charge declared in `QuantumNumbers`. A field with no
`Index[Colour]` drops the gluon part. A field with no `Q` drops the photon part.

Index letters:

* $a,b,c$ = colour (fundamental $SU(3)$ indices),
* $m,n$ = generation (1,2,3),
* $u_m$ = up-type quark field `uq`, $d_m$ = down-type quark field `dq`,
* $\psi^{\mathcal C} \equiv C\,\bar\psi^{\,T}$ = charge conjugate field (`CC[...]`),
  so `bar[CC[dq]]` $= \overline{d^{\mathcal C}}$,
* $\gamma_5$ = `Ga[5]`, $\gamma^\mu$ = `Ga[mu]`,
* $P_{L,R} = (1\mp\gamma_5)/2$; a structure $a + b\,\gamma_5$ equals $(a-b)P_L + (a+b)P_R$.

Repeated indices are summed. Every new coupling carries `InteractionOrder -> {NP,1}`.
The order hierarchy is `{{QCD,1},{QED,2},{NP,1}}`.

---

## 1. Lagrangian, term by term

### 1.1 `Lphikin` — real scalar kinetic and mass term

$$
\mathcal{L}_{\phi\,\rm kin}
= \tfrac{1}{2}\,\partial_\mu \phi\,\partial^\mu \phi
\;-\; \tfrac{1}{2}\,M_\phi^2\,\phi^2 .
$$

$\phi$ is a gauge singlet, so `del` is used, not `DC`.

### 1.2 `LVkin` — real vector (Proca) kinetic and mass term

$$
\mathcal{L}_{V\,\rm kin}
= -\tfrac{1}{4}\,V_{\mu\nu}V^{\mu\nu}
\;+\; \tfrac{1}{2}\,M_V^2\,V_\mu V^\mu ,
\qquad
V_{\mu\nu} = \partial_\mu V_\nu - \partial_\nu V_\mu .
$$

$V$ is a singlet, so `FS[V,mu,nu]` is the abelian field strength.

### 1.3 `Lchikin` — Dirac fermion kinetic and mass term

$$
\mathcal{L}_{\chi\,\rm kin}
= i\,\bar\chi\,\gamma^\mu \partial_\mu \chi
\;-\; M_\chi\,\bar\chi\chi .
$$

`DC[chi,mu]` is written in the file, but $\chi$ carries no colour index and no charge.
The covariant derivative therefore reduces to $\partial_\mu$.

### 1.4 `Lvphikin` — coloured charged scalar $\varphi$

$$
\mathcal{L}_{\varphi\,\rm kin}
= \left(D_\mu \varphi\right)^{\dagger a}\left(D^\mu \varphi\right)^{a}
\;-\; M_\varphi^2\,\varphi^{\dagger a}\varphi^{a},
$$

$$
\left(D_\mu \varphi\right)^{a}
= \left(\partial_\mu \delta^{ab} - i g_s T^{c,ab} G^c_\mu
- i\,\tfrac{2}{3}\,e\,A_\mu \delta^{ab}\right)\varphi^{b}.
$$

This term gives the QCD pair production and the photon coupling of $\varphi$.

### 1.5 `Lvphitkin` — coloured charged scalar $\tilde\varphi$

$$
\mathcal{L}_{\tilde\varphi\,\rm kin}
= \left(D_\mu \tilde\varphi\right)^{\dagger a}\left(D^\mu \tilde\varphi\right)^{a}
\;-\; M_{\tilde\varphi}^2\,\tilde\varphi^{\dagger a}\tilde\varphi^{a},
$$

$$
\left(D_\mu \tilde\varphi\right)^{a}
= \left(\partial_\mu \delta^{ab} - i g_s T^{c,ab} G^c_\mu
+ i\,\tfrac{1}{3}\,e\,A_\mu \delta^{ab}\right)\tilde\varphi^{b}.
$$

### 1.6 `LXkin` — coloured charged massive vector $X$

$$
\mathcal{L}_{X\,\rm kin}
= -\tfrac{1}{2}\,X^{\dagger}_{\mu\nu}{}^{a}\,X^{\mu\nu\,a}
\;+\; M_X^2\,X^{\dagger a}_\mu X^{\mu\,a},
\qquad
X^{a}_{\mu\nu} = \left(D_\mu X_\nu\right)^{a} - \left(D_\nu X_\mu\right)^{a},
$$

with $D_\mu$ containing $g_s T^a G^a_\mu$ and $\tfrac{2}{3} e A_\mu$.
$X$ is **not** a gauge field of a new group. It is a massive vector in the fundamental
of $SU(3)_C$. Its only gauge interactions are the minimal ones from $D_\mu$. There is no
extra magnetic-moment ($\kappa$) operator in the file.

### 1.7 `Lphiu` — flavour-changing scalar coupling to up-type quarks

$$
\mathcal{L}_{\phi u}
= \phi\;\Big[
a^{0}_{mn}\,\bar u^{a}_{m}\,u^{a}_{n}
\;+\; b^{0}_{mn}\,\bar u^{a}_{m}\,\gamma_5\,u^{a}_{n}
\Big].
$$

The colour index $a$ is the same on both quarks, so the operator is colour diagonal.
Equivalently, in chiral form:

$$
\mathcal{L}_{\phi u} = \phi\;\bar u_m \Big[(a^{0}-b^{0})_{mn} P_L + (a^{0}+b^{0})_{mn} P_R\Big] u_n .
$$

No `HC` is added. Hermiticity of $\mathcal{L}$ therefore requires $a^{0}$ hermitian and
$b^{0}$ anti-hermitian. The given real values satisfy this: $a^{0}$ is symmetric and
$b^{0}$ is zero.

### 1.8 `LVu` — flavour-changing vector coupling to up-type quarks

$$
\mathcal{L}_{V u}
= V_\mu\;\Big[
a^{1}_{mn}\,\bar u^{a}_{m}\,\gamma^\mu\,u^{a}_{n}
\;+\; b^{1}_{mn}\,\bar u^{a}_{m}\,\gamma^\mu\gamma_5\,u^{a}_{n}
\Big].
$$

Colour diagonal. Both $a^1$ and $b^1$ must be hermitian for a real Lagrangian; the given
values are real symmetric and zero respectively.

### 1.9 `LvphiDiquark` — scalar $\varphi$ as a down-down diquark

$$
\mathcal{L}_{\varphi\,qq}
= \epsilon_{abc}\,\varphi^{a}\,\Big[
a^{q}_{mn}\,\overline{d^{\mathcal C}_{m}}{}^{\,b}\,d^{c}_{n}
\;+\; b^{q}_{mn}\,\overline{d^{\mathcal C}_{m}}{}^{\,b}\,\gamma_5\,d^{c}_{n}
\Big]
\;+\; \text{h.c.}
$$

$\overline{d^{\mathcal C}}$ carries a fundamental colour index, so
$\epsilon_{abc}\,3\otimes3\otimes3$ is an $SU(3)$ singlet. Charge:
$-\tfrac13-\tfrac13+\tfrac23 = 0$.

Because $\epsilon_{abc}$ is antisymmetric in $b\leftrightarrow c$ and the bilinears
$\overline{\psi^{\mathcal C}}\,\{1,\gamma_5\}\,\psi$ are symmetric under exchange of the two
fermions, **only the antisymmetric part of $a^{q}$ and $b^{q}$ in generation space
contributes**. The numerical input respects this: $a^{q}_{12}=+0.1$, $a^{q}_{21}=-0.1$.

### 1.10 `LvphiChi` — $\varphi$ coupling to an up-type quark and $\chi$

$$
\mathcal{L}_{\varphi\chi}
= \varphi^{a}\,\Big[
a^{1/2}_{m}\,\bar u^{a}_{m}\,\chi
\;+\; b^{1/2}_{m}\,\bar u^{a}_{m}\,\gamma_5\,\chi
\Big]
\;+\; \text{h.c.}
$$

Chiral form: $\varphi^{a}\,\bar u^{a}_m\big[(a^{1/2}-b^{1/2})_m P_L + (a^{1/2}+b^{1/2})_m P_R\big]\chi + \text{h.c.}$
Charge: $-\tfrac23 + 0 + \tfrac23 = 0$.

### 1.11 `LvphitDiquark` — scalar $\tilde\varphi$ as a down-up diquark

$$
\mathcal{L}_{\tilde\varphi\,qq}
= \epsilon_{abc}\,\tilde\varphi^{a}\,\Big[
\tilde a^{q}_{mn}\,\overline{d^{\mathcal C}_{m}}{}^{\,b}\,u^{c}_{n}
\;+\; \tilde b^{q}_{mn}\,\overline{d^{\mathcal C}_{m}}{}^{\,b}\,\gamma_5\,u^{c}_{n}
\Big]
\;+\; \text{h.c.}
$$

The two quarks are of different type, so there is no symmetry condition on
$\tilde a^{q}$, $\tilde b^{q}$. Charge: $-\tfrac13 + \tfrac23 - \tfrac13 = 0$.

### 1.12 `LvphitChi` — $\tilde\varphi$ coupling to a down-type quark and $\chi$

$$
\mathcal{L}_{\tilde\varphi\chi}
= \tilde\varphi^{a}\,\Big[
\tilde a^{1/2}_{m}\,\bar d^{a}_{m}\,\chi
\;+\; \tilde b^{1/2}_{m}\,\bar d^{a}_{m}\,\gamma_5\,\chi
\Big]
\;+\; \text{h.c.}
$$

Charge: $+\tfrac13 - \tfrac13 = 0$.

### 1.13 `LXDiquark` — vector $X$ as a down-down diquark

$$
\mathcal{L}_{X\,qq}
= \epsilon_{abc}\,X^{a}_{\mu}\,\Big[
a^{qV}_{mn}\,\overline{d^{\mathcal C}_{m}}{}^{\,b}\,\gamma^\mu\,d^{c}_{n}
\;+\; b^{qV}_{mn}\,\overline{d^{\mathcal C}_{m}}{}^{\,b}\,\gamma^\mu\gamma_5\,d^{c}_{n}
\Big]
\;+\; \text{h.c.}
$$

Here $\overline{\psi^{\mathcal C}}\gamma^\mu\psi$ and $\overline{\psi^{\mathcal C}}\gamma^\mu\gamma_5\psi$
are **antisymmetric** under exchange of the two fermions. Combined with $\epsilon_{abc}$,
**only the symmetric part of $a^{qV}$, $b^{qV}$ survives**. The input again respects this:
the one non-zero entry is the diagonal $a^{qV}_{11}=0.1$.

### 1.14 `LXChi` — $X$ coupling to an up-type quark and $\chi$

$$
\mathcal{L}_{X\chi}
= X^{a}_{\mu}\,\Big[
a^{1/2\,V}_{m}\,\bar u^{a}_{m}\,\gamma^\mu\,\chi
\;+\; b^{1/2\,V}_{m}\,\bar u^{a}_{m}\,\gamma^\mu\gamma_5\,\chi
\Big]
\;+\; \text{h.c.}
$$

### 1.15 `LTotal`

$$
\mathcal{L} =
\mathcal{L}_{\phi\,\rm kin}+\mathcal{L}_{V\,\rm kin}+\mathcal{L}_{\chi\,\rm kin}
+\mathcal{L}_{\varphi\,\rm kin}+\mathcal{L}_{\tilde\varphi\,\rm kin}+\mathcal{L}_{X\,\rm kin}
+\mathcal{L}_{\phi u}+\mathcal{L}_{V u}
+\mathcal{L}_{\varphi qq}+\mathcal{L}_{\varphi\chi}
+\mathcal{L}_{\tilde\varphi qq}+\mathcal{L}_{\tilde\varphi\chi}
+\mathcal{L}_{X qq}+\mathcal{L}_{X\chi}.
$$

The Standard Model part is not in this file. The file adds new states on top of it.

---

## 2. Field table

| `.fr` class | Symbol | Spin | $SU(3)_C$ | $SU(2)_L$ | $U(1)$ charge | Self-conj. | Mass symbol | Mass value | Width | PDG |
|---|---|---|---|---|---|---|---|---|---|---|
| `S[100]` `phi` | $\phi$ | 0 | **1** (singlet) | not declared | $Q=0$ (none declared) | yes (real) | `Mphi` | 300 GeV | `Wphi` = 0 | 9900001 |
| `V[101]` `V` | $V_\mu$ | 1 | **1** (singlet) | not declared | $Q=0$ (none declared) | yes (real) | `MV` | 50 GeV | `WV` = 0 | 9900002 |
| `F[102]` `chi` | $\chi$ | 1/2 | **1** (singlet) | not declared | $Q=0$ (none declared) | no (Dirac) | `Mchi` | 50 GeV | `Wchi` = 0 | 9900003 |
| `S[103]` `vphi` | $\varphi^a$ | 0 | **3** (`Index[Colour]`) | not declared | $Q=+2/3$ | no (complex) | `Mvphi` | 500 GeV | `Wvphi` = 50 GeV | 9900004 |
| `S[104]` `vphit` | $\tilde\varphi^a$ | 0 | **3** (`Index[Colour]`) | not declared | $Q=-1/3$ | no (complex) | `Mvphit` | 3000 GeV | `Wvphit` = 300 GeV | 9900005 |
| `V[105]` `X` | $X^a_\mu$ | 1 | **3** (`Index[Colour]`) | not declared | $Q=+2/3$ | no (complex) | `MX` | 500 GeV | `WX` = 50 GeV | 9900006 |

Notes:

* The colour index is declared as a fundamental `Index[Colour]`. The $\epsilon_{abc}$
  contraction in the diquark terms makes the operator a colour singlet. The three coloured
  states act as **diquark** fields.
* $\phi$, $V$ and $\chi$ carry no colour and no electric charge. $\phi$ and $V$ have zero
  width, so they are stable and invisible in a detector. $\chi$ also has zero width and is
  stable.
* No $SU(2)_L$ representation is declared anywhere. The model is defined after electroweak
  symmetry breaking.

---

## 3. External parameters

All parameters are `External`, all sit in LHA block `MONOTOP`, and all carry
`InteractionOrder -> {NP,1}`. All values are real.

| `.fr` symbol | Rank | Multiplies | Physical meaning | Non-zero values |
|---|---|---|---|---|
| `a0FC` | $3\times3$ generation | $\phi\,\bar u_m u_n$ | Scalar (parity-even) flavour-changing coupling of the neutral scalar to up-type quarks | $[1,3]=[3,1]=0.1$ ($u$–$t$) |
| `b0FC` | $3\times3$ | $\phi\,\bar u_m \gamma_5 u_n$ | Pseudo-scalar flavour-changing coupling | all 0 |
| `a1FC` | $3\times3$ | $V_\mu\,\bar u_m \gamma^\mu u_n$ | Vector flavour-changing coupling of the neutral vector to up-type quarks | $[1,3]=[3,1]=0.1$ ($u$–$t$) |
| `b1FC` | $3\times3$ | $V_\mu\,\bar u_m \gamma^\mu\gamma_5 u_n$ | Axial-vector flavour-changing coupling | all 0 |
| `aqSR` | $3\times3$ | $\epsilon_{abc}\varphi^a\,\overline{d^{\mathcal C}_m} d_n$ | Scalar diquark coupling of $\varphi$ to two down-type quarks; only its antisymmetric part acts | $[1,2]=+0.1$, $[2,1]=-0.1$ ($d$–$s$) |
| `bqSR` | $3\times3$ | same with $\gamma_5$ | Pseudo-scalar diquark coupling of $\varphi$ | all 0 |
| `ahalfSR` | 3-vector | $\varphi^a\,\bar u^a_m \chi$ | Scalar coupling of $\varphi$ to an up-type quark and the new fermion | $[3]=0.1$ (top) |
| `bhalfSR` | 3-vector | same with $\gamma_5$ | Pseudo-scalar version | all 0 |
| `atildeqSR` | $3\times3$ | $\epsilon_{abc}\tilde\varphi^a\,\overline{d^{\mathcal C}_m} u_n$ | Scalar diquark coupling of $\tilde\varphi$ to one down-type and one up-type quark | $[1,3]=0.1$ ($d$–$t$), $[2,3]=0.1$ ($s$–$t$) |
| `btildeqSR` | $3\times3$ | same with $\gamma_5$ | Pseudo-scalar version | all 0 |
| `atildehalfSR` | 3-vector | $\tilde\varphi^a\,\bar d^a_m \chi$ | Scalar coupling of $\tilde\varphi$ to a down-type quark and the new fermion | $[1]=0.1$ ($d$), $[2]=0.1$ ($s$) |
| `btildehalfSR` | 3-vector | same with $\gamma_5$ | Pseudo-scalar version | all 0 |
| `aqVR` | $3\times3$ | $\epsilon_{abc}X^a_\mu\,\overline{d^{\mathcal C}_m}\gamma^\mu d_n$ | Vector diquark coupling of $X$ to two down-type quarks; only its symmetric part acts | $[1,1]=0.1$ ($dd$) |
| `bqVR` | $3\times3$ | same with $\gamma^\mu\gamma_5$ | Axial-vector diquark coupling of $X$ | all 0 |
| `ahalfVR` | 3-vector | $X^a_\mu\,\bar u^a_m \gamma^\mu \chi$ | Vector coupling of $X$ to an up-type quark and the new fermion | $[3]=0.1$ (top) |
| `bhalfVR` | 3-vector | same with $\gamma^\mu\gamma_5$ | Axial-vector version | all 0 |

Masses and widths (`Mphi`, `Wphi`, `MV`, `WV`, `Mchi`, `Wchi`, `Mvphi`, `Wvphi`,
`Mvphit`, `Wvphit`, `MX`, `WX`) are the other external inputs. They come from the particle
class declarations, not from `M$Parameters`.

At this benchmark point **every `b`-type coupling is zero**. The interactions are therefore
purely scalar or purely vector, and parity is conserved in the new sector.

---

## 4. Physics summary

This is a **monotop** model (the LHA block is literally named `MONOTOP`). It adds two
classes of new states. The first class is three colour-singlet, electrically neutral and
stable states: a real scalar $\phi$, a real vector $V_\mu$, and a Dirac fermion $\chi$. All
three escape the detector and give missing transverse energy. The second class is three
coloured, electrically charged and unstable resonances that act as diquarks: two scalars
$\varphi$ ($Q=2/3$) and $\tilde\varphi$ ($Q=-1/3$), and one massive vector $X_\mu$ ($Q=2/3$).

Two production mechanisms follow. (i) **Flavour-changing, non-resonant**: $\phi$ or $V$
couples one up-type quark to another, so $u\,g$ or $u\,\bar u$ initial states give a single
top quark plus the invisible $\phi$ or $V$. (ii) **Resonant**: two down-type quarks fuse
through the $\epsilon_{abc}$ diquark vertex into $\varphi$, $\tilde\varphi$ or $X$, which then
decays to a quark plus the invisible fermion $\chi$. With the given inputs, $\varphi$ and $X$
are made from $d\,s$ and $d\,d$ and decay to a top quark and $\chi$; $\tilde\varphi$ is made
from a down-type quark and a top and decays to a down-type quark and $\chi$.

The signature in both cases is one top quark and nothing else visible: a single top plus
large missing transverse energy. The coloured states are also pair-produced by pure QCD
through their covariant-derivative kinetic terms, which gives a second, coupling-independent
signal.
