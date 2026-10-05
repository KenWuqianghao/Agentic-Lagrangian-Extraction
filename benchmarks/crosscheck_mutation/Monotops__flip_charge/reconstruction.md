# Reconstruction of `sanitized.fr`

Conventions used below:

* Generation (flavour) indices: $i,j,k = 1,2,3$. Colour (fundamental SU(3)$_c$) indices: $a,b,c$.
* $u_i$ = up-type quark mass eigenstates (`uq`), $d_i$ = down-type quark mass eigenstates (`dq`). Both are the Standard-Model 4-component Dirac fields.
* Charge conjugation: $\psi^{c} \equiv C\bar\psi^{\,T}$, and `bar[CC[psi]]` $= \overline{\psi^{c}}$. FeynRules leaves the colour index of `CC[dq[ff,cc]]` on the field, so $\overline{(d_i)^c}$ still carries a **fundamental** colour index.
* $\gamma^5$ is `Ga[5]`; a structure $a + b\gamma^5$ is equal to $(a-b)P_L + (a+b)P_R$ with $P_{L,R}=\tfrac{1}{2}(1\mp\gamma^5)$.
* "+ h.c." is the FeynRules `HC[term]`.
* Repeated generation and colour indices are summed.

## 0. Gauge content of the covariant derivative

The new states declare only `Indices -> {Index[Colour]}` and `QuantumNumbers -> {Q -> ...}`. No SU(2)$_L$ representation and no hypercharge are declared anywhere in the file. Therefore every `DC` in this file is the QCD $\times$ U(1)$_{\rm em}$ covariant derivative only — there is **no** $W^\pm$ or $Z$ coupling to the new fields:

$$
D_\mu \;=\; \partial_\mu \;-\; i\,g_s\,T^A_{(R)} G^A_\mu \;-\; i\,e\,Q\,A_\mu ,
$$

with $T^A_{(R)}$ in the fundamental $\mathbf{3}$ for $\varphi$, $\tilde\varphi$, $X$ (and in $\bar{\mathbf{3}}$ for their conjugates), and $T^A_{(R)}=0$, $Q=0$ for the colour-singlet, electrically neutral states $\phi$, $V$, $\chi$. For $\chi$ the covariant derivative collapses to an ordinary derivative, $D_\mu\chi = \partial_\mu\chi$.

`FS[V,mu,nu]` and `FS[X,mu,nu]` are applied to fields that are *not* declared gauge bosons, so FeynRules expands them as the abelian curl $\partial_\mu A_\nu-\partial_\nu A_\mu$ (see the note in §5 about the coloured vector $X$).

## 1. Lagrangian, term by term

### `Lphikin` — real scalar singlet kinetic + mass

$$
\mathcal{L}_{\phi,\rm kin} \;=\; \tfrac{1}{2}\,\partial^\mu\phi\,\partial_\mu\phi \;-\; \tfrac{1}{2}\,M_\phi^2\,\phi^2
$$

### `LVkin` — real (Proca) vector singlet

$$
\mathcal{L}_{V,\rm kin} \;=\; -\tfrac{1}{4}\,V^{\mu\nu}V_{\mu\nu} \;+\; \tfrac{1}{2}\,M_V^2\,V^\mu V_\mu ,
\qquad V_{\mu\nu}=\partial_\mu V_\nu-\partial_\nu V_\mu
$$

### `Lchikin` — Dirac singlet fermion

$$
\mathcal{L}_{\chi,\rm kin} \;=\; i\,\bar\chi\,\gamma^\mu \partial_\mu \chi \;-\; M_\chi\,\bar\chi\chi
$$

($\,$`DC[chi,mu]` $=\partial_\mu\chi$ because $\chi$ is colour- and charge-neutral.)

### `Lvphikin` — coloured scalar $\varphi$

$$
\mathcal{L}_{\varphi,\rm kin} \;=\; \left(D^\mu \varphi\right)^{\dagger}_a \left(D_\mu \varphi\right)^{a} \;-\; M_\varphi^2\,\varphi^{\dagger}_a \varphi^{a},
\qquad
(D_\mu\varphi)^a = \partial_\mu\varphi^a - i g_s (T^A)^a{}_b G^A_\mu \varphi^b - i e Q_\varphi A_\mu \varphi^a
$$

### `Lvphitkin` — coloured scalar $\tilde\varphi$

$$
\mathcal{L}_{\tilde\varphi,\rm kin} \;=\; \left(D^\mu \tilde\varphi\right)^{\dagger}_a \left(D_\mu \tilde\varphi\right)^{a} \;-\; M_{\tilde\varphi}^2\,\tilde\varphi^{\dagger}_a \tilde\varphi^{a}
$$

### `LXkin` — complex coloured vector $X$

$$
\mathcal{L}_{X,\rm kin} \;=\; -\tfrac{1}{2}\,X^{\dagger}_{\mu\nu\,a}\,X^{\mu\nu\,a} \;+\; M_X^2\,X^{\dagger}_{\mu\,a} X^{\mu\,a},
\qquad X^{\mu\nu\,a} \;=\; \partial^\mu X^{\nu\,a}-\partial^\nu X^{\mu\,a}
$$

Note: as written, `FS` gives the plain curl, so the QCD covariant derivative does **not** appear in the $X$ kinetic term (no $g_s\,G\,X^\dagger X$ vertex from this term), even though $X$ carries colour. A fully gauge-covariant treatment would replace $\partial^\mu\to D^\mu$. This is how the file is written; it is stated here because it changes the $X$ production rate through gluon fusion.

### `Lphiu` — flavour-changing scalar coupling of $\phi$ to up-type quarks

$$
\mathcal{L}_{\phi u} \;=\; \phi \left[\, a^{0}_{ij}\; \bar u_i^{\,a}\,u_{j\,a} \;+\; b^{0}_{ij}\; \bar u_i^{\,a}\,\gamma^5\,u_{j\,a} \,\right]
$$

The colour index is contracted inside the bilinear (colour-diagonal). There is no explicit `HC`, so hermiticity of $\mathcal{L}$ requires $a^{0}$ hermitian and $b^{0}$ anti-hermitian. Chirally, $a^0+b^0\gamma^5=(a^0-b^0)P_L+(a^0+b^0)P_R$.

### `LVu` — flavour-changing vector/axial coupling of $V$ to up-type quarks

$$
\mathcal{L}_{V u} \;=\; V_\mu \left[\, a^{1}_{ij}\; \bar u_i^{\,a}\,\gamma^\mu\,u_{j\,a} \;+\; b^{1}_{ij}\; \bar u_i^{\,a}\,\gamma^\mu\gamma^5\,u_{j\,a} \,\right]
$$

($a^1$ hermitian, $b^1$ hermitian, for a real $\mathcal{L}$; no explicit `HC` in the file.)

### `LvphiDiquark` — $\varphi$ as a down-type diquark

$$
\mathcal{L}_{\varphi\,qq} \;=\; \epsilon_{abc}\,\varphi^{a}\left[\, a^{q}_{ij}\;\overline{(d_i^{\,b})^{c}}\;d_j^{\,c} \;+\; b^{q}_{ij}\;\overline{(d_i^{\,b})^{c}}\;\gamma^5\,d_j^{\,c} \,\right] \;+\; \mathrm{h.c.}
$$

(Here the superscript $c$ on the field means charge conjugation, the lower $b,c$ are colour labels.) Because $\overline{\psi^{c}}\,\Gamma\,\chi = +\,\overline{\chi^{c}}\,\Gamma\,\psi$ for $\Gamma=\mathbb{1},\gamma^5$, and $\epsilon_{abc}$ is antisymmetric in the two quark colour indices, **$a^{q}$ and $b^{q}$ must be antisymmetric in generation space**, $a^q_{ij}=-a^q_{ji}$. The numerical input respects this ($a^q_{12}=+0.1$, $a^q_{21}=-0.1$).

### `LvphiChi` — $\varphi$–up-quark–$\chi$ coupling

$$
\mathcal{L}_{\varphi\chi} \;=\; \varphi^{a}\left[\, a^{1/2}_{i}\;\bar u_{i\,a}\,\chi \;+\; b^{1/2}_{i}\;\bar u_{i\,a}\,\gamma^5\,\chi \,\right] \;+\; \mathrm{h.c.}
$$

### `LvphitDiquark` — $\tilde\varphi$ as an up–down diquark

$$
\mathcal{L}_{\tilde\varphi\,qq} \;=\; \epsilon_{abc}\,\tilde\varphi^{a}\left[\, \tilde a^{q}_{ij}\;\overline{(d_i^{\,b})^{c}}\;u_j^{\,c} \;+\; \tilde b^{q}_{ij}\;\overline{(d_i^{\,b})^{c}}\;\gamma^5\,u_j^{\,c} \,\right] \;+\; \mathrm{h.c.}
$$

The two quarks are of different type, so no (anti)symmetry constraint applies to $\tilde a^{q}$, $\tilde b^{q}$.

### `LvphitChi` — $\tilde\varphi$–down-quark–$\chi$ coupling

$$
\mathcal{L}_{\tilde\varphi\chi} \;=\; \tilde\varphi^{a}\left[\, \tilde a^{1/2}_{i}\;\bar d_{i\,a}\,\chi \;+\; \tilde b^{1/2}_{i}\;\bar d_{i\,a}\,\gamma^5\,\chi \,\right] \;+\; \mathrm{h.c.}
$$

### `LXDiquark` — $X$ as a vector down-type diquark

$$
\mathcal{L}_{X\,qq} \;=\; \epsilon_{abc}\,X_\mu^{\,a}\left[\, a^{qV}_{ij}\;\overline{(d_i^{\,b})^{c}}\;\gamma^\mu\,d_j^{\,c} \;+\; b^{qV}_{ij}\;\overline{(d_i^{\,b})^{c}}\;\gamma^\mu\gamma^5\,d_j^{\,c} \,\right] \;+\; \mathrm{h.c.}
$$

Since $\overline{\psi^{c}}\gamma^\mu\chi = -\,\overline{\chi^{c}}\gamma^\mu\psi$ and $\overline{\psi^{c}}\gamma^\mu\gamma^5\chi = +\,\overline{\chi^{c}}\gamma^\mu\gamma^5\psi$, the $\epsilon$ contraction forces **$a^{qV}$ symmetric** ($a^{qV}_{ij}=a^{qV}_{ji}$, and the input has only the diagonal $a^{qV}_{11}$) and **$b^{qV}$ antisymmetric**.

### `LXChi` — $X$–up-quark–$\chi$ coupling

$$
\mathcal{L}_{X\chi} \;=\; X_\mu^{\,a}\left[\, a^{1/2V}_{i}\;\bar u_{i\,a}\,\gamma^\mu\,\chi \;+\; b^{1/2V}_{i}\;\bar u_{i\,a}\,\gamma^\mu\gamma^5\,\chi \,\right] \;+\; \mathrm{h.c.}
$$

### `LTotal`

$$
\mathcal{L} \;=\; \mathcal{L}_{\phi,\rm kin}+\mathcal{L}_{V,\rm kin}+\mathcal{L}_{\chi,\rm kin}+\mathcal{L}_{\varphi,\rm kin}+\mathcal{L}_{\tilde\varphi,\rm kin}+\mathcal{L}_{X,\rm kin}
+\mathcal{L}_{\phi u}+\mathcal{L}_{V u}+\mathcal{L}_{\varphi qq}+\mathcal{L}_{\varphi\chi}+\mathcal{L}_{\tilde\varphi qq}+\mathcal{L}_{\tilde\varphi\chi}+\mathcal{L}_{X qq}+\mathcal{L}_{X\chi}
$$

## 2. Field table

| `.fr` class | Symbol | Spin | SU(3)$_c$ | SU(2)$_L$ | U(1) charge $Q$ | Self-conjugate | Mass (symbol, value) | Width | PDG |
|---|---|---|---|---|---|---|---|---|---|
| `S[100]` `phi` | $\phi$ | 0 | singlet | not declared | 0 | yes (real) | $M_\phi = 300$ GeV | $W_\phi=0$ | 9900001 |
| `V[101]` `V` | $V_\mu$ | 1 | singlet | not declared | 0 | yes (real) | $M_V = 50$ GeV | $W_V=0$ | 9900002 |
| `F[102]` `chi` | $\chi$ | 1/2 | singlet | not declared | 0 | no (Dirac) | $M_\chi = 50$ GeV | $W_\chi=0$ | 9900003 |
| `S[103]` `vphi` | $\varphi^a$ | 0 | triplet ($\mathbf{3}$, one `Index[Colour]`) | not declared | **declared $-2/3$** (see note) | no (complex) | $M_\varphi = 500$ GeV | $W_\varphi=50$ GeV | 9900004 |
| `S[104]` `vphit` | $\tilde\varphi^a$ | 0 | triplet ($\mathbf{3}$) | not declared | $-1/3$ | no (complex) | $M_{\tilde\varphi} = 3000$ GeV | $W_{\tilde\varphi}=300$ GeV | 9900005 |
| `V[105]` `X` | $X^a_\mu$ | 1 | triplet ($\mathbf{3}$) | not declared | $+2/3$ | no (complex) | $M_X = 500$ GeV | $W_X=50$ GeV | 9900006 |

All three coloured states carry a single fundamental colour index that is contracted with $\epsilon_{abc}$ against two quark colour indices, so each behaves as the antisymmetric ($\bar{\mathbf{3}}$-type) diquark structure $\epsilon\,\varphi\,qq$.

No SU(2)$_L$ representation and no hypercharge are declared for any new state, and the quark couplings are written for mass-eigenstate Dirac quarks with both chiralities. The model is therefore an effective parametrisation in the broken phase; it is not manifestly SU(2)$_L$ invariant.

### Charge-assignment check (inconsistency found)

Electric-charge conservation of each interaction term fixes the charges of the coloured states. With $Q_u=+2/3$, $Q_d=-1/3$, and with $\overline{(\psi)^c}$ raising the charge like $\bar\psi^{\,c}$:

* `LvphiDiquark`: $\overline{(d)^{c}}\,d$ removes $-2/3$, so $Q_\varphi = +2/3$ is required.
* `LvphiChi`: $\bar u\,\chi$ requires the same, $Q_\varphi = +2/3$.
* `LvphitDiquark` and `LvphitChi`: both require $Q_{\tilde\varphi} = -1/3$ — consistent with the declaration.
* `LXDiquark` and `LXChi`: both require $Q_X = +2/3$ — consistent with the declaration.

The file declares `QuantumNumbers -> {Q -> -2/3}` for `vphi`. Both `vphi` interaction terms need $Q_\varphi=+2/3$. The declared charge of `vphi` therefore has the **wrong sign**: it violates electric-charge conservation in `LvphiDiquark` and `LvphiChi`, and it gives the $\varphi$ photon coupling in `Lvphikin` the wrong sign. Every other charge in the file is self-consistent. The physics reconstruction below assumes the value required by the interactions, $Q_\varphi = +2/3$.

## 3. External parameters

All parameters are `External`, live in LHA block `MONOTOP`, and carry `InteractionOrder -> {NP,1}`. All are dimensionless. Generation indices are written $i,j$.

| `.fr` symbol | LaTeX | Multiplies | Non-zero input values | Physical meaning |
|---|---|---|---|---|
| `a0FC[i,j]` | $a^{0}_{ij}$ | $\phi\,\bar u_i u_j$ | $a^0_{13}=a^0_{31}=0.1$ | Scalar (parity-even) flavour-changing neutral Yukawa of $\phi$ to up-type quarks; the $1$–$3$ entries are the $u$–$t$ coupling |
| `b0FC[i,j]` | $b^{0}_{ij}$ | $\phi\,\bar u_i\gamma^5 u_j$ | all 0 | Pseudo-scalar (parity-odd) part of the same coupling |
| `a1FC[i,j]` | $a^{1}_{ij}$ | $V_\mu\,\bar u_i\gamma^\mu u_j$ | $a^1_{13}=a^1_{31}=0.1$ | Vector flavour-changing neutral coupling of $V$ to up-type quarks ($u$–$t$) |
| `b1FC[i,j]` | $b^{1}_{ij}$ | $V_\mu\,\bar u_i\gamma^\mu\gamma^5 u_j$ | all 0 | Axial-vector part of the same coupling |
| `aqSR[i,j]` | $a^{q}_{ij}$ | $\epsilon\,\varphi\,\overline{(d_i)^c}d_j$ | $a^q_{12}=+0.1$, $a^q_{21}=-0.1$ | Scalar diquark coupling of $\varphi$ to two down-type quarks ($d$–$s$); antisymmetric in flavour |
| `bqSR[i,j]` | $b^{q}_{ij}$ | $\epsilon\,\varphi\,\overline{(d_i)^c}\gamma^5 d_j$ | all 0 | Pseudo-scalar diquark coupling of $\varphi$ |
| `ahalfSR[i]` | $a^{1/2}_{i}$ | $\varphi\,\bar u_i\chi$ | $a^{1/2}_3=0.1$ | Scalar coupling $\varphi$–up-type quark–$\chi$; entry 3 is the top |
| `bhalfSR[i]` | $b^{1/2}_{i}$ | $\varphi\,\bar u_i\gamma^5\chi$ | all 0 | Pseudo-scalar part of the same coupling |
| `atildeqSR[i,j]` | $\tilde a^{q}_{ij}$ | $\epsilon\,\tilde\varphi\,\overline{(d_i)^c}u_j$ | $\tilde a^q_{13}=\tilde a^q_{23}=0.1$ | Scalar diquark coupling of $\tilde\varphi$ to one down-type and one up-type quark ($d\,t$ and $s\,t$) |
| `btildeqSR[i,j]` | $\tilde b^{q}_{ij}$ | $\epsilon\,\tilde\varphi\,\overline{(d_i)^c}\gamma^5 u_j$ | all 0 | Pseudo-scalar part |
| `atildehalfSR[i]` | $\tilde a^{1/2}_{i}$ | $\tilde\varphi\,\bar d_i\chi$ | $\tilde a^{1/2}_1=\tilde a^{1/2}_2=0.1$ | Scalar coupling $\tilde\varphi$–down-type quark–$\chi$ ($d$ and $s$) |
| `btildehalfSR[i]` | $\tilde b^{1/2}_{i}$ | $\tilde\varphi\,\bar d_i\gamma^5\chi$ | all 0 | Pseudo-scalar part |
| `aqVR[i,j]` | $a^{qV}_{ij}$ | $\epsilon\,X_\mu\,\overline{(d_i)^c}\gamma^\mu d_j$ | $a^{qV}_{11}=0.1$ | Vector diquark coupling of $X$ to two down-type quarks ($dd$); symmetric in flavour |
| `bqVR[i,j]` | $b^{qV}_{ij}$ | $\epsilon\,X_\mu\,\overline{(d_i)^c}\gamma^\mu\gamma^5 d_j$ | all 0 | Axial-vector diquark coupling of $X$ |
| `ahalfVR[i]` | $a^{1/2V}_{i}$ | $X_\mu\,\bar u_i\gamma^\mu\chi$ | $a^{1/2V}_3=0.1$ | Vector coupling $X$–up-type quark–$\chi$ (top) |
| `bhalfVR[i]` | $b^{1/2V}_{i}$ | $X_\mu\,\bar u_i\gamma^\mu\gamma^5\chi$ | all 0 | Axial-vector part |

The interaction-order hierarchy is `{{QCD,1},{QED,2},{NP,1}}`; every new coupling counts as one power of `NP`.

## 4. Physics summary

This is a monotop model: it adds a set of new states whose only job is to produce a single top quark together with invisible particles. The invisible sector holds a real scalar $\phi$ (300 GeV), a real vector $V$ (50 GeV) and a gauge-singlet Dirac fermion $\chi$ (50 GeV); the mediator sector holds three colour-triplet states with diquark couplings — the scalars $\varphi$ ($Q=+2/3$ by charge conservation, 500 GeV) and $\tilde\varphi$ ($Q=-1/3$, 3 TeV), and the vector $X$ ($Q=+2/3$, 500 GeV).

Two production mechanisms are encoded. In the *flavour-changing* mode, $a^{0}_{13}$ and $a^{1}_{13}$ give a neutral $u$–$t$–$\phi$ and $u$–$t$–$V$ vertex, so $u\,g \to t\,\phi$ or $t\,V$ and $u\,\bar u/g g \to t\,\bar t$-free single-top topologies give one top plus missing transverse energy. In the *resonant* mode, a coloured state is produced in the $s$ channel from two quarks — $d\,s \to \varphi$, $d\,d \to X$, $d\,t$ or $s\,t \to \tilde\varphi$ — and then decays to a top quark plus the invisible fermion, $\varphi,X \to t\,\bar\chi$ (with $\tilde\varphi \to d\,\bar\chi$, $s\,\bar\chi$), again giving a monotop signature with a resonant $t+\slashed{E}_T$ mass edge.

Because the diquark couplings also allow the mediators to decay back to two jets, the same Lagrangian mediates dijet and paired-dijet resonance signals, baryon-number-violating $\Delta B$ processes, and same-sign top-quark production; $\chi$ (or $V$/$\phi$) is the stable, weakly interacting final state that carries the missing energy.

> Note for the reviewer: the only internal inconsistency found is the declared electric charge of `vphi` (`Q -> -2/3`), which conflicts with both of its interaction terms; they require $Q_\varphi = +2/3$. See §2.
