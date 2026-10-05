# Reconstruction of `sanitized.fr`

## 0. Conventions and structures used below

**Gauge group.** The file declares no new gauge group. It only adds a new
colour representation to the existing QCD group:

```
IndexRange[Index[Sextet]] = NoUnfold[Range[6]];
AddGaugeRepresentation[SU3C -> {T6, Sextet}];
```

So `SU3C` now also acts on a 6-dimensional index (`Sextet`, index letter `s`)
with generators $T_6^a$ (the $6\times 6$ generators of the symmetric
two-index representation $\mathbf{6}$ of $SU(3)_C$).

**Covariant derivative.** No `SU2W` representation is declared for any new
field, so all new states are weak singlets. `DC[X,mu]` therefore expands to

$$
D_\mu X \;=\; \Big(\partial_\mu \;-\; i\,g_s\,G^a_\mu\,T^a_{(\mathbf 6)} \;-\; i\,g_1\,Y_X\,B_\mu\Big) X ,
$$

with $g_s$ the strong coupling, $G^a_\mu$ the gluon, $g_1=g'$ the hypercharge
coupling, $B_\mu$ the hypercharge boson, and $Y_X$ the declared `Y` quantum
number. The declared charges obey $Q = T_3 + Y = Y$ for every new field,
which confirms the $SU(2)_L$-singlet assignment.

**Field strengths.**

$$
\texttt{FS[G,mu,nu,a]} = G^a_{\mu\nu}=\partial_\mu G^a_\nu-\partial_\nu G^a_\mu+g_s f^{abc}G^b_\mu G^c_\nu ,
\qquad
\texttt{FS[B,mu,nu]} = B_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu .
$$

**Dirac structures.**

$$
\texttt{ProjM}=P_L=\tfrac{1-\gamma_5}{2},\qquad
\texttt{ProjP}=P_R=\tfrac{1+\gamma_5}{2},
$$

$$
\tfrac{i}{2}\big(\gamma^\mu\gamma^\nu-\gamma^\nu\gamma^\mu\big)
=\tfrac{i}{2}[\gamma^\mu,\gamma^\nu]\;\equiv\;\sigma^{\mu\nu}.
$$

Every `(I/2)(Ga[mu].Ga[nu] - Ga[nu].Ga[mu])` block in the file is exactly
$\sigma^{\mu\nu}$.

**Charge conjugation.** `CC[uqbar]` is the Dirac conjugate of the
charge-conjugate up-quark field,

$$
\texttt{CC[uqbar]} = \overline{u^{c}} = -\,u^{T}C^{-1},
\qquad u^{c}=C\,\bar u^{T},\quad C=i\gamma^2\gamma^0 .
$$

Useful identities used below: $\overline{\psi}P_L=\overline{\psi_R}$,
$\overline{\psi}P_R=\overline{\psi_L}$, and $(\psi^{c})_{R}=(\psi_L)^{c}$,
$(\psi^{c})_{L}=(\psi_R)^{c}$.

**Colour tensors.**

* $\texttt{Eps[i1,i2,i3]}=\varepsilon_{i_1i_2i_3}$ — the antisymmetric
  invariant tensor of $SU(3)$ on triplet indices.
* $\texttt{T[a,i,j]}=(T^a)_{ij}$ — fundamental ($\mathbf 3$) generators,
  $\mathrm{Tr}(T^aT^b)=\tfrac12\delta^{ab}$.
* $\texttt{K6bar[s,i,j]}=(\bar K^{s})_{ij}=\big[(K^{s})_{ij}\big]^{*}$ — the
  Clebsch–Gordan tensor for $\mathbf 6\subset\mathbf 3\otimes\mathbf 3$. It is
  **symmetric** in $i\leftrightarrow j$, with the standard normalisation
  $(K^{s})_{ij}(\bar K^{s'})_{ij}=\delta^{ss'}$ and
  $\sum_s (K^{s})_{ij}(\bar K^{s})_{kl}=\tfrac12(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})$.

Every interaction term uses one and the same colour structure, which I
abbreviate as

$$
\boxed{\;\mathcal{C}^{a,s}_{\,i_1}\;\equiv\;\varepsilon_{i_1 i_2 i_3}\,(T^a)_{i_2 i_4}\,(\bar K^{s})_{i_4 i_3}\;}
$$

It ties one quark triplet index $i_1$, one gluon adjoint index $a$, and one
sextet index $s$ into an $SU(3)_C$ invariant. Because $(\bar K^s)_{i_4i_3}$ is
symmetric and $\varepsilon$ is antisymmetric, the generator insertion $T^a$ is
what makes the contraction non-zero: the structure exists only together with
the gluon field strength. In group terms, $\mathbf 3\otimes\mathbf 8\supset
\bar{\mathbf 6}$, which pairs with the $\mathbf 6$ of the new state.

**SM fields used.** `uq`, `dq` are the SM up- and down-type quark classes
(generation index `ff`, colour index `i1`), and `l` is the SM charged-lepton
class (generation index `xx`).

---

## 1. Lagrangian, term by term

### 1.1 `LPsiuFree` — kinetic and mass term of the sextet fermion $\Psi_u$

$$
\mathcal{L}_{\texttt{LPsiuFree}}
= i\,\overline{\Psi}_u^{\,s}\,\gamma^\mu \big(D_\mu \Psi_u\big)^{s}
\;-\; M_{\Psi_u}\,\overline{\Psi}_u^{\,s}\,\Psi_u^{\,s},
$$

$$
\big(D_\mu\Psi_u\big)^{s}
=\partial_\mu\Psi_u^{\,s}
- i g_s G^a_\mu\,(T_6^a)^{s s'}\Psi_u^{\,s'}
- i g_1\Big(-\tfrac23\Big)B_\mu\,\Psi_u^{\,s}.
$$

($M_{\Psi_u}\equiv$ `MPSU`. Sextet index $s$ summed over $1\dots6$.)

### 1.2 `LPsidFree` — kinetic and mass term of the sextet fermion $\Psi_d$

$$
\mathcal{L}_{\texttt{LPsidFree}}
= i\,\overline{\Psi}_d^{\,s}\,\gamma^\mu \big(D_\mu \Psi_d\big)^{s}
\;-\; M_{\Psi_d}\,\overline{\Psi}_d^{\,s}\,\Psi_d^{\,s},
\qquad
D_\mu \supset - i g_1\Big(+\tfrac13\Big)B_\mu .
$$

($M_{\Psi_d}\equiv$ `MPSD`.)

### 1.3 `LPhiuFree` — kinetic and mass term of the sextet scalar $\Phi_u$

$$
\mathcal{L}_{\texttt{LPhiuFree}}
= \big(D^\mu \Phi_u^{\,s}\big)^{\dagger}\big(D_\mu \Phi_u^{\,s}\big)
\;-\; M_{\Phi_u}^{2}\,\Phi_u^{\,s\dagger}\Phi_u^{\,s},
\qquad
D_\mu \supset - i g_1\Big(+\tfrac13\Big)B_\mu .
$$

($M_{\Phi_u}\equiv$ `MPHU`.)

### 1.4 `LPhidFree` — kinetic and mass term of the sextet scalar $\Phi_d$

$$
\mathcal{L}_{\texttt{LPhidFree}}
= \big(D^\mu \Phi_d^{\,s}\big)^{\dagger}\big(D_\mu \Phi_d^{\,s}\big)
\;-\; M_{\Phi_d}^{2}\,\Phi_d^{\,s\dagger}\Phi_d^{\,s},
\qquad
D_\mu \supset - i g_1\Big(+\tfrac43\Big)B_\mu .
$$

($M_{\Phi_d}\equiv$ `MPHD`.)

### 1.5 `LPsiuG` — dimension-5 chromomagnetic transition dipole, up-type quark $\to \Psi_u$

$$
\mathcal{L}_{\texttt{LPsiuG}}
= -\,i\,\frac{\kappa_u^{f}}{\Lambda_{\Psi_u}}\;
\mathcal{C}^{a,s}_{\,i_1}\;
\Big[\overline{(u_f)^{c}}_{\,i_1}\,P_L\,\sigma^{\mu\nu}\,\Psi_u^{\,s}\Big]\,
G^{a}_{\mu\nu}
\;+\;\text{h.c.}
$$

Sums: $f=1,2,3$ (quark generation), $a=1\dots8$, $s=1\dots6$,
$i_{1..4}=1,2,3$, $\mu,\nu$ contracted with $G^a_{\mu\nu}$.

Chirality, written out explicitly:

$$
\overline{u^{c}}\,P_L\,\sigma^{\mu\nu}\,\Psi_u
=\overline{(u_L)^{c}}\;\sigma^{\mu\nu}\;\Psi_{u,L}.
$$

So this operator joins the **left-handed** up-type quark to the
**left-handed** component of $\Psi_u$.

### 1.6 `LPsidG` — dimension-5 chromomagnetic transition dipole, down-type quark $\to \Psi_d$

$$
\mathcal{L}_{\texttt{LPsidG}}
= -\,i\,\frac{\kappa_d^{f}}{\Lambda_{\Psi_d}}\;
\mathcal{C}^{a,s}_{\,i_1}\;
\Big[\overline{(d_f)^{c}}_{\,i_1}\,P_R\,\sigma^{\mu\nu}\,\Psi_d^{\,s}\Big]\,
G^{a}_{\mu\nu}
\;+\;\text{h.c.}
$$

$$
\overline{d^{c}}\,P_R\,\sigma^{\mu\nu}\,\Psi_d
=\overline{(d_R)^{c}}\;\sigma^{\mu\nu}\;\Psi_{d,R}.
$$

So this operator uses the **right-handed** down-type quark and the
**right-handed** $\Psi_d$.

### 1.7 `LPsiuB` — dimension-7 $G\!-\!B$ operator, up-type quark $\to \Psi_u$

$$
\mathcal{L}_{\texttt{LPsiuB}}
= -\,i\,\frac{\kappa^{B,f}_{u}}{\Lambda_{\Psi_u B}^{3}}\;
\mathcal{C}^{a,s}_{\,i_1}\;
\Big[\overline{(u_f)^{c}}_{\,i_1}\,P_R\,\Psi_u^{\,s}\Big]\,
B_{\mu\nu}\,G^{a\,\mu\nu}
\;+\;\text{h.c.}
$$

The fermion bilinear is a **scalar** (no $\sigma^{\mu\nu}$); the two Lorentz
indices are carried by the two field strengths and contracted with each other.
Chirality:

$$
\overline{u^{c}}\,P_R\,\Psi_u=\overline{(u_R)^{c}}\;\Psi_{u,R}.
$$

### 1.8 `LPsidB` — dimension-7 $G\!-\!B$ operator, down-type quark $\to \Psi_d$

$$
\mathcal{L}_{\texttt{LPsidB}}
= -\,i\,\frac{\kappa^{B,f}_{d}}{\Lambda_{\Psi_d B}^{3}}\;
\mathcal{C}^{a,s}_{\,i_1}\;
\Big[\overline{(d_f)^{c}}_{\,i_1}\,P_R\,\Psi_d^{\,s}\Big]\,
B_{\mu\nu}\,G^{a\,\mu\nu}
\;+\;\text{h.c.},
\qquad
\overline{d^{c}}P_R\Psi_d=\overline{(d_R)^{c}}\,\Psi_{d,R}.
$$

### 1.9 `LPhiuG` — dimension-6 quark–lepton–scalar–gluon operator (up-type)

$$
\mathcal{L}_{\texttt{LPhiuG}}
= -\,i\,\frac{\lambda_u^{x f}}{\Lambda_{\Phi_u}^{2}}\;
\mathcal{C}^{a,s}_{\,i_1}\;\Phi_u^{\,s}\;
\Big[\overline{(u_f)^{c}}_{\,i_1}\,\sigma^{\mu\nu}\,P_R\,\ell_x\Big]\,
G^{a}_{\mu\nu}
\;+\;\text{h.c.}
$$

Index order of the coupling is `lamu[xx, ff]`: the **first** index $x$ is the
charged-lepton generation, the **second** index $f$ is the up-type quark
generation. Chirality:

$$
\overline{u^{c}}\,\sigma^{\mu\nu}\,P_R\,\ell
=\overline{(u_R)^{c}}\;\sigma^{\mu\nu}\;\ell_R .
$$

### 1.10 `LPhidG` — dimension-6 quark–lepton–scalar–gluon operator (down-type)

$$
\mathcal{L}_{\texttt{LPhidG}}
= -\,i\,\frac{\lambda_d^{x f}}{\Lambda_{\Phi_d}^{2}}\;
\mathcal{C}^{a,s}_{\,i_1}\;\Phi_d^{\,s}\;
\Big[\overline{(d_f)^{c}}_{\,i_1}\,\sigma^{\mu\nu}\,P_R\,\ell_x\Big]\,
G^{a}_{\mu\nu}
\;+\;\text{h.c.},
\qquad
\overline{d^{c}}\sigma^{\mu\nu}P_R\ell=\overline{(d_R)^{c}}\,\sigma^{\mu\nu}\,\ell_R .
$$

### 1.11 `LTotal`

$$
\mathcal{L}_{\rm total}=
\mathcal{L}_{\texttt{LPsiuFree}}+\mathcal{L}_{\texttt{LPsidFree}}
+\mathcal{L}_{\texttt{LPhiuFree}}+\mathcal{L}_{\texttt{LPhidFree}}
+\mathcal{L}_{\texttt{LPsiuG}}+\mathcal{L}_{\texttt{LPsidG}}
+\mathcal{L}_{\texttt{LPsiuB}}+\mathcal{L}_{\texttt{LPsidB}}
+\mathcal{L}_{\texttt{LPhiuG}}+\mathcal{L}_{\texttt{LPhidG}} .
$$

The SM Lagrangian itself is not in this file; the file is an add-on model that
is loaded together with the SM.

### 1.12 Chirality pattern (observation)

| Term | Quark chirality | Partner chirality | Projector in file |
| --- | --- | --- | --- |
| `LPsiuG` | $u_L$ | $\Psi_{u,L}$ | `ProjM` |
| `LPsidG` | $d_R$ | $\Psi_{d,R}$ | `ProjP` |
| `LPsiuB` | $u_R$ | $\Psi_{u,R}$ | `ProjP` |
| `LPsidB` | $d_R$ | $\Psi_{d,R}$ | `ProjP` |
| `LPhiuG` | $u_R$ | $\ell_R$ | `ProjP` |
| `LPhidG` | $d_R$ | $\ell_R$ | `ProjP` |

Nine of the ten operators (counting the h.c. pairs once) are purely
right-handed. `LPsiuG` is the single exception: it is the only left-handed
structure in the file. It is also inconsistent with `LPsiuB`, which couples the
same two fields $u$ and $\Psi_u$ with the opposite chirality. I report the file
as written; the mismatch is stated here as an observation, not corrected.

---

## 2. Field table

All four new states are $SU(3)_C$ **sextets** ($\mathbf 6$), $SU(2)_L$
**singlets** (no `SU2W` representation declared), and **not** self-conjugate
(complex scalars / Dirac fermions). Hypercharge is given in the
$Q=T_3+Y$ normalisation, so $Y=Q$ here.

| Symbol | FR class | Spin | $SU(3)_C$ | $SU(2)_L$ | $Q$ | $Y$ | Lepton no. | Self-conj. | Mass (value) | Width (value) | PDG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\Phi_u$ | `S[100]` `Phiu` | 0 | $\mathbf 6$ | $\mathbf 1$ | $+1/3$ | $+1/3$ | $-1$ | No | `MPHU` $=1000$ GeV | `WPHU` $=10$ GeV | 9000001 |
| $\Phi_d$ | `S[101]` `Phid` | 0 | $\mathbf 6$ | $\mathbf 1$ | $+4/3$ | $+4/3$ | $-1$ | No | `MPHD` $=1000$ GeV | `WPHD` $=10$ GeV | 9000002 |
| $\Psi_u$ | `F[100]` `Psiu` | 1/2 | $\mathbf 6$ | $\mathbf 1$ | $-2/3$ | $-2/3$ | 0 (not declared) | No | `MPSU` $=1000$ GeV | `WPSU` $=10$ GeV | 9000011 |
| $\Psi_d$ | `F[101]` `Psid` | 1/2 | $\mathbf 6$ | $\mathbf 1$ | $+1/3$ | $+1/3$ | 0 (not declared) | No | `MPSD` $=1000$ GeV | `WPSD` $=10$ GeV | 9000012 |

Implied baryon number (not declared in the file, but fixed by the
interactions): $B=-1/3$ for all four states. Charge checks of every
interaction term:

* $\overline{u^{c}}\,\Psi_u$: $-2/3 = Q(\Psi_u) = -2/3$ ✓
* $\overline{d^{c}}\,\Psi_d$: $+1/3 = Q(\Psi_d) = +1/3$ ✓
* $\overline{u^{c}}\,\ell\,\Phi_u$: $-2/3 = -1 + 1/3$ ✓ (and $L$: $0 = +1-1$ ✓)
* $\overline{d^{c}}\,\ell\,\Phi_d$: $+1/3 = -1 + 4/3$ ✓ (and $L$: $0 = +1-1$ ✓)

With $B=-1/3$ and $L=-1$, the two scalars are **colour-sextet leptoquarks**.
The two fermions are colour-sextet quark partners; they carry no lepton number.

---

## 3. External parameters

### 3.1 Cut-off scales (block `SXTCUTOFF`, all `InteractionOrder -> {NP,-1}`)

| Symbol | `OrderBlock` | Value | Where it multiplies | Meaning |
| --- | --- | --- | --- | --- |
| $\Lambda_{\Psi_u}$ (`LamPsu`) | 1 | 1000 GeV | $1/\Lambda_{\Psi_u}$ in `LPsiuG` | new-physics scale of the $u$–$\Psi_u$–$g$ dipole (dim-5) |
| $\Lambda_{\Psi_d}$ (`LamPsd`) | 2 | 1000 GeV | $1/\Lambda_{\Psi_d}$ in `LPsidG` | new-physics scale of the $d$–$\Psi_d$–$g$ dipole (dim-5) |
| $\Lambda_{\Psi_u B}$ (`LamPsuB`) | 3 | 1000 GeV | $1/\Lambda^3$ in `LPsiuB` | new-physics scale of the $u$–$\Psi_u$–$g$–$B$ operator (dim-7) |
| $\Lambda_{\Psi_d B}$ (`LamPsdB`) | 4 | 1000 GeV | $1/\Lambda^3$ in `LPsidB` | new-physics scale of the $d$–$\Psi_d$–$g$–$B$ operator (dim-7) |
| $\Lambda_{\Phi_u}$ (`LamPhu`) | 5 | 1000 GeV | $1/\Lambda^2$ in `LPhiuG` | new-physics scale of the $u$–$\ell$–$\Phi_u$–$g$ operator (dim-6) |
| $\Lambda_{\Phi_d}$ (`LamPhd`) | 6 | 1000 GeV | $1/\Lambda^2$ in `LPhidG` | new-physics scale of the $d$–$\ell$–$\Phi_d$–$g$ operator (dim-6) |

All six have mass dimension 1.

### 3.2 Dimensionless couplings (all `InteractionOrder -> {NP,1}`)

| Symbol | Indices | Block | Value | Where it multiplies | Meaning |
| --- | --- | --- | --- | --- | --- |
| $\kappa_u^{f}$ (`kapu`) | 1 × Generation | `KAPU` | $0.05,\,0.05,\,0.05$ | `LPsiuG` | dipole strength of $u_f \leftrightarrow \Psi_u$ per quark generation |
| $\kappa_d^{f}$ (`kapd`) | 1 × Generation | `KAPD` | $0.05,\,0.05,\,0.05$ | `LPsidG` | dipole strength of $d_f \leftrightarrow \Psi_d$ per quark generation |
| $\kappa_u^{B,f}$ (`kapuB`) | 1 × Generation | `KAPUB` | $0.10,\,0.10,\,0.10$ | `LPsiuB` | strength of the dim-7 $u_f$–$\Psi_u$–$g$–$B$ operator |
| $\kappa_d^{B,f}$ (`kapdB`) | 1 × Generation | `KAPDB` | $0.10,\,0.10,\,0.10$ | `LPsidB` | strength of the dim-7 $d_f$–$\Psi_d$–$g$–$B$ operator |
| $\lambda_u^{x f}$ (`lamu`) | Generation × Generation | `LAMU` | $0.1\,\delta_{xf}$ | `LPhiuG` | lepton-generation $x$ to up-quark-generation $f$ leptoquark coupling |
| $\lambda_d^{x f}$ (`lamd`) | Generation × Generation | `LAMD` | $0.1\,\delta_{xf}$ | `LPhidG` | lepton-generation $x$ to down-quark-generation $f$ leptoquark coupling |

The two matrix couplings are set diagonal (flavour-diagonal in the
lepton–quark generation pair), so at the default point each leptoquark couples
each charged lepton only to the quark of the same generation.

### 3.3 Masses and widths

`MPHU`, `MPHD`, `MPSU`, `MPSD` are all $1000$ GeV; `WPHU`, `WPHD`, `WPSU`,
`WPSD` are all $10$ GeV. They are declared inside the particle classes, not in
`M$Parameters`.

### 3.4 Coupling-order bookkeeping

```
M$InteractionOrderHierarchy = { {QCD,1}, {QED,2}, {NP,1} };
```

With `NP` $=-1$ for each $\Lambda$ and `NP` $=+1$ for each $\kappa$ or
$\lambda$, the vertices count as: `LPsiuG`/`LPsidG` $\to$ NP$^2$,
`LPhiuG`/`LPhidG` $\to$ NP$^3$, `LPsiuB`/`LPsidB` $\to$ NP$^4$.

---

## 4. Physics summary

This is an effective-field-theory extension of the Standard Model by four
heavy colour-**sextet** states at 1 TeV: two complex scalar leptoquarks
$\Phi_u$ ($Q=1/3$) and $\Phi_d$ ($Q=4/3$), both with $L=-1$, and two Dirac
sextet fermions $\Psi_u$ ($Q=-2/3$) and $\Psi_d$ ($Q=1/3$). All four are weak
singlets, and they get their gauge interactions only from the QCD covariant
derivative in the $\mathbf 6$ plus their hypercharge.

No renormalisable Yukawa coupling to SM matter exists. The states talk to the
SM only through higher-dimension operators that all carry one gluon field
strength and the same colour tensor
$\varepsilon_{i_1i_2i_3}(T^a)_{i_2i_4}(\bar K^{s})_{i_4i_3}$: a dimension-5
chromomagnetic transition dipole $\bar q^{\,c}\sigma^{\mu\nu}\Psi\,G_{\mu\nu}$,
a dimension-7 $\bar q^{\,c}\Psi\,B_{\mu\nu}G^{\mu\nu}$ operator, and a
dimension-6 $\bar q^{\,c}\sigma^{\mu\nu}\ell\,\Phi\,G_{\mu\nu}$ leptoquark
operator. Each operator conserves electric charge, baryon number and lepton
number with $B(\Phi)=B(\Psi)=-1/3$ and $L(\Phi)=-1$.

At a hadron collider the model gives: resonant single production of the sextet
fermions from quark–gluon fusion, $q\,g \to \Psi$, with the decay back
$\Psi \to q\,g$ (a dijet-type resonance) and the radiative
$\Psi \to q\,g\,\gamma/Z$ channel from the dimension-7 operator; associated
leptoquark production $q\,g \to \Phi\,\ell$ with $\Phi \to q\,\ell\,g$, giving
lepton-plus-jets final states; and QCD pair production
$gg,\,q\bar q \to \Psi\overline{\Psi},\,\Phi\Phi^{\dagger}$, whose rate is
fixed by the sextet colour charge alone. The sextet colour flow also allows
same-sign colour-charged final states that a triplet leptoquark cannot
produce.
