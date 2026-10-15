# Reconstruction of `sanitized.fr`

Conventions used below.

- $u_i$, $d_i$ are the Standard Model (SM) up-type and down-type quark fields of the base model
  (`uq`, `dq`); $i,j$ are generation indices, $a,b,c$ are fundamental $SU(3)_c$ indices.
- `Ga[mu]` $\to \gamma^\mu$, `Ga[5]` $\to \gamma^5$, `del[X,mu]` $\to \partial_\mu X$.
- `CC[psi]` is the charge conjugate $\psi^{c} = C\bar\psi^{\mathsf T}$, so
  `bar[CC[psi]]` $\to \overline{\psi^{c}} = -\psi^{\mathsf T}C^{-1}$.
- `HC[term]` $\to$ the hermitian conjugate, written as $+\,\mathrm{h.c.}$
- `Eps[c1,c2,c3]` $\to \epsilon_{abc}$, the totally antisymmetric $SU(3)_c$ invariant tensor.
- Chiral projectors: $P_{L,R} = (1\mp\gamma^5)/2$. A structure $a + b\,\gamma^5$ equals
  $(a-b)P_L + (a+b)P_R$, and $a\gamma^\mu + b\,\gamma^\mu\gamma^5$ equals
  $\gamma^\mu[(a-b)P_L + (a+b)P_R]$.

**Covariant derivative.** The file declares no gauge group; `DC` is built from the gauge groups of
the base SM model file. The new fields carry only a colour index and an electric charge `Q` (the
model is written in the broken phase: no $SU(2)_L$ representation and no hypercharge are declared,
so every new field is an $SU(2)_L$ singlet). Therefore, for a colour-triplet field $\Phi_a$ of
charge $Q$,

$$
D_\mu \Phi_a = \partial_\mu \Phi_a - i g_s\, T^{A}_{ab} G^{A}_\mu \Phi_b - i e\, Q\, A_\mu \Phi_a ,
$$

and for the colour-singlet, electrically neutral fermion $\chi$,

$$
D_\mu \chi = \partial_\mu \chi .
$$

`FS[V,mu,nu]` and `FS[X,mu,nu]` act on fields that are **not** declared gauge bosons, so FeynRules
returns the abelian curl $\partial_\mu V_\nu - \partial_\nu V_\mu$. For the coloured vector $X$ this
means the kinetic term as written is not $SU(3)_c$-covariant (a QCD-covariant form would need
$D_\mu X_\nu - D_\nu X_\mu$). This is reported as it stands in the file.

---

## 1. Lagrangian

The total Lagrangian is `LTotal`:

$$
\mathcal{L} = \mathcal{L}_{\phi,\rm kin} + \mathcal{L}_{V,\rm kin} + \mathcal{L}_{\chi,\rm kin}
+ \mathcal{L}_{\varphi,\rm kin} + \mathcal{L}_{\tilde\varphi,\rm kin} + \mathcal{L}_{X,\rm kin}
+ \mathcal{L}_{\phi u} + \mathcal{L}_{V u}
+ \mathcal{L}_{\varphi qq} + \mathcal{L}_{\varphi\chi}
+ \mathcal{L}_{\tilde\varphi qq} + \mathcal{L}_{\tilde\varphi\chi}
+ \mathcal{L}_{X qq}.
$$

### 1.1 Kinetic and mass terms

**`Lphikin`** — real (self-conjugate) scalar singlet $\phi$:

$$
\mathcal{L}_{\phi,\rm kin}
= \tfrac{1}{2}\,\partial_\mu \phi\, \partial^\mu \phi
- \tfrac{1}{2}\, M_\phi^{2}\, \phi^{2}
$$

**`LVkin`** — real (self-conjugate) Proca vector singlet $V^\mu$, with
$V_{\mu\nu} = \partial_\mu V_\nu - \partial_\nu V_\mu$:

$$
\mathcal{L}_{V,\rm kin}
= -\tfrac{1}{4}\, V_{\mu\nu} V^{\mu\nu}
+ \tfrac{1}{2}\, M_V^{2}\, V_\mu V^\mu
$$

**`Lchikin`** — Dirac fermion singlet $\chi$ (no gauge charge, so $D_\mu \to \partial_\mu$):

$$
\mathcal{L}_{\chi,\rm kin}
= i\, \bar\chi\, \gamma^\mu \partial_\mu \chi - M_\chi\, \bar\chi \chi
$$

**`Lvphikin`** — complex colour-triplet scalar $\varphi_a$ with $Q = +2/3$:

$$
\mathcal{L}_{\varphi,\rm kin}
= \left(D_\mu \varphi_a\right)^{\dagger} \left(D^\mu \varphi_a\right)
- M_\varphi^{2}\, \varphi_a^{\dagger}\varphi_a
$$

**`Lvphitkin`** — complex colour-triplet scalar $\tilde\varphi_a$ with $Q = -1/3$:

$$
\mathcal{L}_{\tilde\varphi,\rm kin}
= \left(D_\mu \tilde\varphi_a\right)^{\dagger} \left(D^\mu \tilde\varphi_a\right)
- M_{\tilde\varphi}^{2}\, \tilde\varphi_a^{\dagger}\tilde\varphi_a
$$

**`LXkin`** — complex colour-triplet vector $X^\mu_a$ with $Q = +2/3$, with
$X_{\mu\nu,a} = \partial_\mu X_{\nu,a} - \partial_\nu X_{\mu,a}$:

$$
\mathcal{L}_{X,\rm kin}
= -\tfrac{1}{2}\, X^{\dagger}_{\mu\nu,a} X^{\mu\nu}_{a}
+ M_X^{2}\, X^{\dagger}_{\mu,a} X^{\mu}_{a}
$$

### 1.2 Flavour-changing neutral couplings to up-type quarks

**`Lphiu`** — scalar $\phi$ coupled to a flavour-changing up-type quark current. The colour index
`cc` is contracted between $\bar u$ and $u$ (colour diagonal, $\delta_{ab}$); no explicit `HC` is
added, so hermiticity requires $a^{0}$ hermitian and $b^{0}$ anti-hermitian (the supplied numerical
values satisfy this: $a^{0}$ is real symmetric, $b^{0}=0$):

$$
\mathcal{L}_{\phi u}
= \phi \sum_{i,j} \bar u_{i,a}\left[a^{0}_{ij} + b^{0}_{ij}\,\gamma^5\right]u_{j,a}
= \phi \sum_{i,j} \bar u_{i,a}\left[(a^{0}_{ij}-b^{0}_{ij})P_L + (a^{0}_{ij}+b^{0}_{ij})P_R\right]u_{j,a}
$$

**`LVu`** — vector $V^\mu$ coupled to a flavour-changing up-type quark current (same colour and
hermiticity remarks; $a^{1}$ must be hermitian, $b^{1}$ hermitian):

$$
\mathcal{L}_{V u}
= V_\mu \sum_{i,j} \bar u_{i,a}\,\gamma^\mu\left[a^{1}_{ij} + b^{1}_{ij}\,\gamma^5\right]u_{j,a}
= V_\mu \sum_{i,j} \bar u_{i,a}\,\gamma^\mu\left[(a^{1}_{ij}-b^{1}_{ij})P_L + (a^{1}_{ij}+b^{1}_{ij})P_R\right]u_{j,a}
$$

### 1.3 Scalar colour triplet $\varphi$ ($Q=+2/3$)

**`LvphiDiquark`** — diquark coupling to two down-type quarks, colour-antisymmetric through
$\epsilon_{abc}$:

$$
\mathcal{L}_{\varphi qq}
= \epsilon_{abc}\, \varphi_a \sum_{i,j}
\overline{d^{\,c}_{i,b}}\left[a^{q}_{ij} + b^{q}_{ij}\,\gamma^5\right] d_{j,c}
\;+\; \mathrm{h.c.}
$$

Index note: the first quark enters charge-conjugated, $\overline{d^{\,c}_{i,b}} = -d_{i,b}^{\mathsf T}C^{-1}$.
Since $\overline{\psi_1^{c}}\,\Gamma\,\psi_2 = +\,\overline{\psi_2^{c}}\,\Gamma\,\psi_1$ for
$\Gamma \in \{1,\gamma^5\}$, and the colour tensor is antisymmetric, Fermi statistics force
$a^{q}$ and $b^{q}$ to be **antisymmetric** in generation space. The supplied values obey this
($a^{q}_{12} = +0.1$, $a^{q}_{21} = -0.1$).

**`LvphiChi`** — coupling of $\varphi$ to one up-type quark and the singlet fermion $\chi$
(colour contracted as $3 \otimes \bar 3 \to 1$):

$$
\mathcal{L}_{\varphi\chi}
= \varphi_a \sum_{i}
\bar u_{i,a}\left[a^{1/2}_{i} + b^{1/2}_{i}\,\gamma^5\right]\chi
\;+\; \mathrm{h.c.}
$$

### 1.4 Scalar colour triplet $\tilde\varphi$ ($Q=-1/3$)

**`LvphitDiquark`** — diquark coupling to one down-type and one up-type quark:

$$
\mathcal{L}_{\tilde\varphi qq}
= \epsilon_{abc}\, \tilde\varphi_a \sum_{i,j}
\overline{d^{\,c}_{i,b}}\left[\tilde a^{q}_{ij} + \tilde b^{q}_{ij}\,\gamma^5\right] u_{j,c}
\;+\; \mathrm{h.c.}
$$

Here the two quarks are different fields, so no symmetry condition applies to $\tilde a^{q}$,
$\tilde b^{q}$ (the values are indeed not symmetric).

**`LvphitChi`** — coupling of $\tilde\varphi$ to one down-type quark and $\chi$:

$$
\mathcal{L}_{\tilde\varphi\chi}
= \tilde\varphi_a \sum_{i}
\bar d_{i,a}\left[\tilde a^{1/2}_{i} + \tilde b^{1/2}_{i}\,\gamma^5\right]\chi
\;+\; \mathrm{h.c.}
$$

### 1.5 Vector colour triplet $X$ ($Q=+2/3$)

**`LXDiquark`** — vector diquark coupling to two down-type quarks:

$$
\mathcal{L}_{X qq}
= \epsilon_{abc}\, X_{\mu,a} \sum_{i,j}
\overline{d^{\,c}_{i,b}}\,\gamma^\mu\left[a^{qV}_{ij} + b^{qV}_{ij}\,\gamma^5\right] d_{j,c}
\;+\; \mathrm{h.c.}
$$

Index note: $\overline{\psi_1^{c}}\,\gamma^\mu\,\psi_2 = -\,\overline{\psi_2^{c}}\,\gamma^\mu\,\psi_1$
while $\overline{\psi_1^{c}}\,\gamma^\mu\gamma^5\,\psi_2 = +\,\overline{\psi_2^{c}}\,\gamma^\mu\gamma^5\,\psi_1$.
With the antisymmetric colour tensor this forces $a^{qV}$ to be **symmetric** and $b^{qV}$ to be
**antisymmetric** in generation space. The values agree ($a^{qV}_{11} = 0.1$, $b^{qV} = 0$).

### 1.6 Charge bookkeeping

Every interaction is electrically neutral, which fixes the charges of the new coloured states:

| Term | Quark bilinear charge | New field charge |
| --- | --- | --- |
| `LvphiDiquark` | $\overline{d^{\,c}}\,d: -1/3-1/3 = -2/3$ | $\varphi: +2/3$ |
| `LvphiChi` | $\bar u\,\chi: -2/3 + 0 = -2/3$ | $\varphi: +2/3$ |
| `LvphitDiquark` | $\overline{d^{\,c}}\,u: -1/3+2/3 = +1/3$ | $\tilde\varphi: -1/3$ |
| `LvphitChi` | $\bar d\,\chi: +1/3 + 0 = +1/3$ | $\tilde\varphi: -1/3$ |
| `LXDiquark` | $\overline{d^{\,c}}\,\gamma^\mu d: -2/3$ | $X: +2/3$ |

### 1.7 Term that is declared but absent

The external parameters `ahalfVR` and `bhalfVR` are defined (with `ahalfVR[3] -> 0.1`) but appear
in **no** Lagrangian term, and `LTotal` contains no $X\!-\!u\!-\!\chi$ piece. By symmetry with
`LvphiChi` and by the pattern of the other blocks, the missing term is the vector analogue

$$
\mathcal{L}_{X\chi}
= X_{\mu,a} \sum_{i}
\bar u_{i,a}\,\gamma^\mu\left[a^{1/2V}_{i} + b^{1/2V}_{i}\,\gamma^5\right]\chi
\;+\; \mathrm{h.c.} \qquad \textbf{(not present in the file)}
$$

Without it the vector resonance $X$ has no decay into $t\,\bar\chi$, although it is given a
non-zero width `WX = 50` GeV. This looks like an omission in the file, not a physical choice.

---

## 2. Field table

All new fields are $SU(2)_L$ singlets: no `SU2` or hypercharge assignment is declared, only the
electric charge `Q`, so the model is written in the electroweak broken phase.

| `.fr` symbol | Class | Spin | $SU(3)_c$ | $SU(2)_L$ | $Q$ | Self-conj. | Mass symbol / value | Width / value | PDG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `phi` ($\phi$) | `S[100]` | 0 | **1** | **1** | 0 | yes (real) | `Mphi` = 300 GeV | `Wphi` = 0 | 9900001 |
| `V` ($V^\mu$) | `V[101]` | 1 | **1** | **1** | 0 | yes (real) | `MV` = 50 GeV | `WV` = 0 | 9900002 |
| `chi` ($\chi$) | `F[102]` | 1/2 | **1** | **1** | 0 | no (Dirac) | `Mchi` = 50 GeV | `Wchi` = 0 | 9900003 |
| `vphi` ($\varphi_a$) | `S[103]` | 0 | **3** | **1** | $+2/3$ | no (complex) | `Mvphi` = 500 GeV | `Wvphi` = 50 GeV | 9900004 |
| `vphit` ($\tilde\varphi_a$) | `S[104]` | 0 | **3** | **1** | $-1/3$ | no (complex) | `Mvphit` = 3000 GeV | `Wvphit` = 300 GeV | 9900005 |
| `X` ($X^\mu_a$) | `V[105]` | 1 | **3** | **1** | $+2/3$ | no (complex) | `MX` = 500 GeV | `WX` = 50 GeV | 9900006 |

Notes.

- `Indices -> {Index[Colour]}` on a non-self-conjugate field puts it in the fundamental **3** of
  $SU(3)_c$. In the $\epsilon_{abc}$ diquark terms the contraction $3\otimes3\otimes3 \to 1$ is the
  antisymmetric singlet; in the $\bar q\,\chi$ terms the contraction is $3\otimes\bar3 \to 1$.
- $\chi$ is a Dirac fermion with no gauge charge: it is stable and invisible unless it can be
  produced through one of the coloured states. It is the dark-matter-like state of the model.

---

## 3. Parameters

All parameters are `External`, live in LHA block `MONOTOP`, and carry `InteractionOrder -> {NP,1}`.
The interaction-order hierarchy is `{{QCD,1},{QED,2},{NP,1}}`.

| `.fr` symbol | Indices | Multiplies | Physical meaning | Non-zero values |
| --- | --- | --- | --- | --- |
| `a0FC` | $(i,j)$ gen. | $\phi\,\bar u_i u_j$ | Scalar flavour-changing neutral coupling of $\phi$ to up-type quarks (scalar part) | $[1,3]=[3,1]=0.1$ ($u\!-\!t$) |
| `b0FC` | $(i,j)$ gen. | $\phi\,\bar u_i \gamma^5 u_j$ | Same, pseudoscalar part (CP-odd) | all 0 |
| `a1FC` | $(i,j)$ gen. | $V_\mu\,\bar u_i \gamma^\mu u_j$ | Vector flavour-changing neutral coupling of $V$ to up-type quarks (vector part) | $[1,3]=[3,1]=0.1$ ($u\!-\!t$) |
| `b1FC` | $(i,j)$ gen. | $V_\mu\,\bar u_i \gamma^\mu\gamma^5 u_j$ | Same, axial-vector part | all 0 |
| `aqSR` | $(i,j)$ gen. | $\epsilon_{abc}\varphi_a \overline{d^{\,c}_i} d_j$ | Scalar diquark coupling of $\varphi$; antisymmetric in flavour | $[1,2]=0.1$, $[2,1]=-0.1$ ($d\!-\!s$) |
| `bqSR` | $(i,j)$ gen. | $\epsilon_{abc}\varphi_a \overline{d^{\,c}_i}\gamma^5 d_j$ | Pseudoscalar diquark coupling of $\varphi$ | all 0 |
| `ahalfSR` | $(i)$ gen. | $\varphi_a \bar u_i \chi$ | Scalar coupling $\varphi\!-\!u_i\!-\!\chi$ (monotop decay vertex) | $[3]=0.1$ (top) |
| `bhalfSR` | $(i)$ gen. | $\varphi_a \bar u_i \gamma^5 \chi$ | Pseudoscalar version of the same vertex | all 0 |
| `atildeqSR` | $(i,j)$ gen. | $\epsilon_{abc}\tilde\varphi_a \overline{d^{\,c}_i} u_j$ | Scalar diquark coupling of $\tilde\varphi$ to $d_i u_j$ | $[1,3]=0.1$, $[2,3]=0.1$ ($d\,t$, $s\,t$) |
| `btildeqSR` | $(i,j)$ gen. | $\epsilon_{abc}\tilde\varphi_a \overline{d^{\,c}_i}\gamma^5 u_j$ | Pseudoscalar version | all 0 |
| `atildehalfSR` | $(i)$ gen. | $\tilde\varphi_a \bar d_i \chi$ | Scalar coupling $\tilde\varphi\!-\!d_i\!-\!\chi$ | $[1]=0.1$, $[2]=0.1$ ($d$, $s$) |
| `btildehalfSR` | $(i)$ gen. | $\tilde\varphi_a \bar d_i \gamma^5 \chi$ | Pseudoscalar version | all 0 |
| `aqVR` | $(i,j)$ gen. | $\epsilon_{abc}X_{\mu,a} \overline{d^{\,c}_i}\gamma^\mu d_j$ | Vector diquark coupling of $X$; symmetric in flavour | $[1,1]=0.1$ ($dd$) |
| `bqVR` | $(i,j)$ gen. | $\epsilon_{abc}X_{\mu,a} \overline{d^{\,c}_i}\gamma^\mu\gamma^5 d_j$ | Axial-vector diquark coupling of $X$ | all 0 |
| `ahalfVR` | $(i)$ gen. | **nothing** (see 1.7) | Intended vector coupling $X\!-\!u_i\!-\!\chi$ | $[3]=0.1$ (top) |
| `bhalfVR` | $(i)$ gen. | **nothing** (see 1.7) | Intended axial-vector version of the same vertex | all 0 |

Internal mass and width symbols (`Mphi`, `Wphi`, `MV`, `WV`, `Mchi`, `Wchi`, `Mvphi`, `Wvphi`,
`Mvphit`, `Wvphit`, `MX`, `WX`) are declared inside the particle classes, not as separate external
parameters.

The `NP` order 1 on every coupling means each new vertex counts once in the new-physics coupling
order, so a production-plus-decay chain through a coloured resonance is `NP=2`.

---

## 4. Physics summary

This is a monotop model: it adds a neutral scalar $\phi$, a neutral vector $V^\mu$, a neutral Dirac
fermion $\chi$ that carries no gauge charge, and three coloured triplet resonances — two scalars
$\varphi$ ($Q=+2/3$) and $\tilde\varphi$ ($Q=-1/3$) and one vector $X^\mu$ ($Q=+2/3$). The coloured
states carry diquark couplings to two SM quarks (via $\epsilon_{abc}$) and Yukawa-type couplings to
one quark plus $\chi$; the neutral $\phi$ and $V$ instead carry flavour-changing neutral couplings
between the up quark and the top quark. Non-zero default values switch on exactly the top-quark
entries, so the model is tuned to produce a single top.

It would mediate two production paths for the same final state, a single top plus missing energy.
The non-resonant path uses the $u\!-\!t\!-\!\phi$ or $u\!-\!t\!-\!V$ flavour-changing vertex, where
the light, long-lived $\phi$ or $V$ (widths set to zero, $M_V = M_\chi = 50$ GeV) escapes the
detector. The resonant path produces a coloured scalar on shell from two quarks in the initial state
($dd \to \varphi$, $d\bar u$-type $\to \tilde\varphi$, $dd \to X$) which then decays to a quark and
the invisible $\chi$. The same couplings also give dijet resonances through the diquark vertex
alone, and $\chi$ pair production. As noted in §1.7, the $X\!-\!u\!-\!\chi$ decay vertex is missing
from the file, so as written the vector resonance $X$ produces dijets only and contributes no
monotop signal, even though its coupling parameters `ahalfVR` and `bhalfVR` are declared.
