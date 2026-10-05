# Reconstruction of `sanitized.fr`

## 0. Conventions and notation used below

The file adds a colour-**sextet** representation of $SU(3)_C$ to an existing Standard Model
implementation:

```
IndexRange[Index[Sextet]] = NoUnfold[Range[6]];
AddGaugeRepresentation[SU3C -> {T6, Sextet}];
```

so `T6` is the $6$-dimensional generator $T_6^a$ ($a=1\dots 8$), and sextet indices $s,s'$ run
over $1\dots 6$. The SM fields `uq`, `dq`, `l` are the up-type quark, down-type quark and
charged-lepton classes; `G` and `B` are the gluon and the hypercharge gauge boson.

**Colour tensor.** Every interaction term contains the same colour structure
`Eps[i1,i2,i3] T[aa,i2,i4] K6bar[ss,i4,i3]`. Write it as

$$
\mathcal{K}^{a}_{\,i\,s}\;\equiv\;\varepsilon_{i\,i_2\,i_3}\;(T^{a})_{i_2 i_4}\;\bar{K}^{\,s}_{\;i_4 i_3},
$$

with $\varepsilon$ the rank-3 antisymmetric tensor, $(T^a)_{ij}$ the **fundamental** $SU(3)_C$
generator, and $\bar K^{\,s}_{\;ij}=\big(K^{s}_{\;ij}\big)^{*}$ the sextet Clebsch–Gordan
tensor (symmetric in $ij$) that converts a symmetric pair of triplet indices into one sextet
index. $\mathcal{K}^{a}_{\,i\,s}$ is the unique invariant contracting one quark triplet index
$i$, one gluon adjoint index $a$, and one sextet index $s$ (it exists because
$\mathbf{6}\otimes\mathbf{3}=\mathbf{10}\oplus\mathbf{8}$ and $\mathbf{8}\otimes\mathbf{8}\supset\mathbf{1}$).

**Other idioms.**

- `Ga[mu]` $=\gamma^\mu$; the combination $\tfrac{i}{2}\big(\gamma^\mu\gamma^\nu-\gamma^\nu\gamma^\mu\big)=\tfrac{i}{2}[\gamma^\mu,\gamma^\nu]\equiv\sigma^{\mu\nu}$ appears written out explicitly in four of the terms.
- `ProjP` $=P_R=\tfrac{1}{2}(1+\gamma_5)$, `ProjM` $=P_L$. Since $[\sigma^{\mu\nu},\gamma_5]=0$, the position of $P_R$ inside a $\sigma^{\mu\nu}$ bilinear is irrelevant.
- `CC[qbar]` is the Dirac-conjugated charge-conjugate field, $\overline{q^{c}}$ with $q^{c}=C\bar q^{\,T}$.
- `FS[G,mu,nu,aa]` $=G^{a}_{\mu\nu}=\partial_\mu G^a_\nu-\partial_\nu G^a_\mu+g_s f^{abc}G^b_\mu G^c_\nu$; `FS[B,mu,nu]` $=B_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu$.
- `HC[tmp]` adds the hermitian conjugate; every interaction term below is understood as $\mathcal{O}+\mathcal{O}^\dagger$.

**Covariant derivative.** The new fields carry a `Sextet` index and a hypercharge `Y`, and
carry **no** $SU(2)_L$ index. Hence `DC` expands to $SU(3)_C$ (in the sextet) $\times\,U(1)_Y$
only:

$$
D_\mu\,X^{s} \;=\; \partial_\mu X^{s}\;-\;i\,g_s\,G^{a}_{\mu}\,\big(T_6^{a}\big)^{s}{}_{s'}X^{s'}\;-\;i\,g_1\,Y_X\,B_\mu\,X^{s},
\qquad X\in\{\Psi_u,\Psi_d,\Phi_u,\Phi_d\}
$$

with $Y_{\Psi_u}=-\tfrac23$, $Y_{\Psi_d}=+\tfrac13$, $Y_{\Phi_u}=+\tfrac13$, $Y_{\Phi_d}=+\tfrac43$.
There is no $SU(2)_L$ term and no Higgs coupling anywhere in the file: the new states are
electroweak singlets whose electric charge equals their hypercharge.

---

## 1. Lagrangian, term by term

### 1.1 Free / kinetic terms

**`LPsiuFree`** — Dirac kinetic + mass term for the colour-sextet fermion $\Psi_u$ (sextet index contracted):

$$
\mathcal{L}_{\Psi_u}^{\rm free}
=\;i\,\overline{\Psi}_{u}^{\,s}\,\gamma^{\mu}\big(D_\mu \Psi_u\big)^{s}
\;-\;M_{\Psi_u}\,\overline{\Psi}_{u}^{\,s}\,\Psi_u^{s}
$$

**`LPsidFree`** — same for $\Psi_d$:

$$
\mathcal{L}_{\Psi_d}^{\rm free}
=\;i\,\overline{\Psi}_{d}^{\,s}\,\gamma^{\mu}\big(D_\mu \Psi_d\big)^{s}
\;-\;M_{\Psi_d}\,\overline{\Psi}_{d}^{\,s}\,\Psi_d^{s}
$$

**`LPhiuFree`** — complex-scalar kinetic + mass term for the colour-sextet scalar $\Phi_u$:

$$
\mathcal{L}_{\Phi_u}^{\rm free}
=\;\big(D^{\mu}\Phi_u\big)^{\dagger}_{s}\big(D_\mu \Phi_u\big)^{s}
\;-\;M_{\Phi_u}^{2}\,\Phi_{u\,s}^{\dagger}\,\Phi_u^{s}
$$

**`LPhidFree`** — same for $\Phi_d$:

$$
\mathcal{L}_{\Phi_d}^{\rm free}
=\;\big(D^{\mu}\Phi_d\big)^{\dagger}_{s}\big(D_\mu \Phi_d\big)^{s}
\;-\;M_{\Phi_d}^{2}\,\Phi_{d\,s}^{\dagger}\,\Phi_d^{s}
$$

No quartic or trilinear scalar potential terms are present (beyond the mass terms), and there is
no $\Phi$–Higgs portal.

### 1.2 Dimension-5 chromo-dipole transition operators (quark $\to$ sextet fermion)

**`LPsiuG`** — as literally written in the file (see the consistency note in §5):

$$
\mathcal{L}_{\Psi_u G}
=\;-\,i\,\frac{\kappa_u^{f}}{\Lambda_{\Psi_u}}\;
\mathcal{K}^{a}_{\,i\,s}\;
\overline{u}_{f,i}\;P_R\,\sigma^{\mu\nu}\,\Psi_{u}^{s}\;G^{a}_{\mu\nu}
\;+\;{\rm h.c.}
$$

The chirality structure is $\overline{u}\,P_R\,\sigma^{\mu\nu}\Psi_u=\overline{u_L}\,\sigma^{\mu\nu}\,\Psi_{u,R}$.
*(This is the one term in the file whose quark field is **not** charge-conjugated; see §5 — it
is almost certainly meant to be $\mathrm{CC}[\overline{u}]=\overline{u^{c}}$ like its three
partners, in which case the bilinear is $\overline{(u_R)^{c}}\,\sigma^{\mu\nu}\Psi_{u,R}$.)*

**`LPsidG`**:

$$
\mathcal{L}_{\Psi_d G}
=\;-\,i\,\frac{\kappa_d^{f}}{\Lambda_{\Psi_d}}\;
\mathcal{K}^{a}_{\,i\,s}\;
\overline{d^{\,c}_{f,i}}\;P_R\,\sigma^{\mu\nu}\,\Psi_{d}^{s}\;G^{a}_{\mu\nu}
\;+\;{\rm h.c.}
$$

with $\overline{d^{\,c}}\,P_R\,\sigma^{\mu\nu}\Psi_d=\overline{(d_R)^{c}}\,\sigma^{\mu\nu}\,\Psi_{d,R}$,
i.e. only the **right-handed** down-type quark participates. $f$ is a quark generation index,
summed.

### 1.3 Dimension-7 double-field-strength operators (quark $\to$ sextet fermion)

**`LPsiuB`**:

$$
\mathcal{L}_{\Psi_u B}
=\;-\,i\,\frac{\kappa_{u}^{B,f}}{\Lambda_{\Psi_u B}^{3}}\;
\mathcal{K}^{a}_{\,i\,s}\;
\overline{u^{\,c}_{f,i}}\;P_R\,\Psi_{u}^{s}\;B_{\mu\nu}\,G^{a\,\mu\nu}
\;+\;{\rm h.c.}
$$

Here the Lorentz indices of the two field strengths are contracted **with each other**
($B_{\mu\nu}G^{a\,\mu\nu}$), and the fermion bilinear is a pure scalar
$\overline{(u_R)^{c}}\,\Psi_{u,R}$ (no $\sigma^{\mu\nu}$). Operator dimension $3+2+2=7$,
consistent with $\Lambda^{-3}$.

**`LPsidB`**:

$$
\mathcal{L}_{\Psi_d B}
=\;-\,i\,\frac{\kappa_{d}^{B,f}}{\Lambda_{\Psi_d B}^{3}}\;
\mathcal{K}^{a}_{\,i\,s}\;
\overline{d^{\,c}_{f,i}}\;P_R\,\Psi_{d}^{s}\;B_{\mu\nu}\,G^{a\,\mu\nu}
\;+\;{\rm h.c.}
$$

### 1.4 Dimension-6 leptoquark operators (quark + lepton + sextet scalar + gluon)

**`LPhiuG`**:

$$
\mathcal{L}_{\Phi_u G}
=\;-\,i\,\frac{\lambda_u^{x f}}{\Lambda_{\Phi_u}^{2}}\;
\mathcal{K}^{a}_{\,i\,s}\;\Phi_{u}^{s}\;
\overline{u^{\,c}_{f,i}}\;\sigma^{\mu\nu}\,P_R\,\ell_{x}\;G^{a}_{\mu\nu}
\;+\;{\rm h.c.}
$$

Chirality: $\overline{u^{\,c}}\,\sigma^{\mu\nu}P_R\,\ell=\overline{(u_R)^{c}}\,\sigma^{\mu\nu}\,\ell_R$
— right-handed up-type quark with right-handed charged lepton. $x$ is the lepton generation
index, $f$ the quark generation index; both are summed. Operator dimension $1+3+2=6$,
consistent with $\Lambda^{-2}$.

**`LPhidG`**:

$$
\mathcal{L}_{\Phi_d G}
=\;-\,i\,\frac{\lambda_d^{x f}}{\Lambda_{\Phi_d}^{2}}\;
\mathcal{K}^{a}_{\,i\,s}\;\Phi_{d}^{s}\;
\overline{d^{\,c}_{f,i}}\;\sigma^{\mu\nu}\,P_R\,\ell_{x}\;G^{a}_{\mu\nu}
\;+\;{\rm h.c.}
$$

### 1.5 Total

**`LTotal`**:

$$
\mathcal{L}_{\rm tot}=
\mathcal{L}_{\Psi_u}^{\rm free}+\mathcal{L}_{\Psi_d}^{\rm free}
+\mathcal{L}_{\Phi_u}^{\rm free}+\mathcal{L}_{\Phi_d}^{\rm free}
+\mathcal{L}_{\Psi_u G}+\mathcal{L}_{\Psi_d G}
+\mathcal{L}_{\Psi_u B}+\mathcal{L}_{\Psi_d B}
+\mathcal{L}_{\Phi_u G}+\mathcal{L}_{\Phi_d G}
$$

(The SM Lagrangian itself is supplied by the base model this file extends.)

---

## 2. Field table

| `.fr` class | Symbol | Spin | $SU(3)_C$ | $SU(2)_L$ | $Q$ | $Y$ | $L$ | Self-conj. | Mass (symbol, value) | Width | PDG |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `S[100]` `Phiu` | $\Phi_u^{s}$ | 0 (complex scalar) | $\mathbf{6}$ (`Sextet`, $T_6$) | not declared $\Rightarrow$ singlet | $+1/3$ | $+1/3$ | $-1$ | No | `MPHU` $=1000$ GeV | `WPHU` $=10$ GeV | 9000001 |
| `S[101]` `Phid` | $\Phi_d^{s}$ | 0 (complex scalar) | $\mathbf{6}$ | singlet | $+4/3$ | $+4/3$ | $-1$ | No | `MPHD` $=1000$ GeV | `WPHD` $=10$ GeV | 9000002 |
| `F[100]` `Psiu` | $\Psi_u^{s}$ | 1/2 (Dirac) | $\mathbf{6}$ | singlet | $-2/3$ | $-2/3$ | 0 (not declared) | No | `MPSU` $=1000$ GeV | `WPSU` $=10$ GeV | 9000011 |
| `F[101]` `Psid` | $\Psi_d^{s}$ | 1/2 (Dirac) | $\mathbf{6}$ | singlet | $+1/3$ | $+1/3$ | 0 (not declared) | No | `MPSD` $=1000$ GeV | `WPSD` $=10$ GeV | 9000012 |

Notes:

- All four are `SelfConjugate -> False`, so each has a distinct antiparticle (`phiu~`, `phid~`, `psiu~`, `psid~`).
- Propagator types: `D` (dashed, scalar) for $\Phi$, `Straight` for $\Psi$; all with `PropagatorArrow -> Forward`.
- Baryon number is **not** declared but is fixed by the interactions: $B(\Phi_u)=B(\Phi_d)=-1/3$ and $B(\Psi_d)=-1/3$ (from $\overline{q^{c}}$ carrying $B=+1/3$). $\Psi_u$ is ambiguous as the file stands — see §5.
- The declared $L=-1$ on $\Phi_{u,d}$ together with $B=-1/3$ makes them **leptoquarks** in the colour-sextet representation.

---

## 3. External parameters

### 3.1 Cut-off scales — block `SXTCUTOFF`, all `InteractionOrder -> {NP,-1}`, all $=1000$ GeV

| Symbol | Block entry | Multiplies | Meaning |
|---|---|---|---|
| `LamPsu` $\Lambda_{\Psi_u}$ | SXTCUTOFF 1 | $1/\Lambda_{\Psi_u}$ in `LPsiuG` | EFT cut-off of the dim-5 $u$–$\Psi_u$ chromo-dipole |
| `LamPsd` $\Lambda_{\Psi_d}$ | SXTCUTOFF 2 | $1/\Lambda_{\Psi_d}$ in `LPsidG` | EFT cut-off of the dim-5 $d$–$\Psi_d$ chromo-dipole |
| `LamPsuB` $\Lambda_{\Psi_u B}$ | SXTCUTOFF 3 | $1/\Lambda_{\Psi_uB}^{3}$ in `LPsiuB` | EFT cut-off of the dim-7 $u$–$\Psi_u$ $BG$ operator |
| `LamPsdB` $\Lambda_{\Psi_d B}$ | SXTCUTOFF 4 | $1/\Lambda_{\Psi_dB}^{3}$ in `LPsidB` | EFT cut-off of the dim-7 $d$–$\Psi_d$ $BG$ operator |
| `LamPhu` $\Lambda_{\Phi_u}$ | SXTCUTOFF 5 | $1/\Lambda_{\Phi_u}^{2}$ in `LPhiuG` | EFT cut-off of the dim-6 $u$–$\ell$–$\Phi_u$ operator |
| `LamPhd` $\Lambda_{\Phi_d}$ | SXTCUTOFF 6 | $1/\Lambda_{\Phi_d}^{2}$ in `LPhidG` | EFT cut-off of the dim-6 $d$–$\ell$–$\Phi_d$ operator |

### 3.2 Dimensionless couplings, all `InteractionOrder -> {NP,1}`

| Symbol | Block | Indices | Default value | Multiplies | Meaning |
|---|---|---|---|---|---|
| `kapu` $\kappa_u^{f}$ | KAPU | 1 quark generation | $0.05$ for $f=1,2,3$ | `LPsiuG` | chromo-dipole transition coupling, up-type quark $\leftrightarrow\Psi_u$ + gluon |
| `kapd` $\kappa_d^{f}$ | KAPD | 1 quark generation | $0.05$ for $f=1,2,3$ | `LPsidG` | chromo-dipole transition coupling, down-type quark $\leftrightarrow\Psi_d$ + gluon |
| `kapuB` $\kappa_u^{B,f}$ | KAPUB | 1 quark generation | $0.10$ for $f=1,2,3$ | `LPsiuB` | coupling of the dim-7 $\overline{u^{c}}\Psi_u B_{\mu\nu}G^{\mu\nu}$ operator |
| `kapdB` $\kappa_d^{B,f}$ | KAPDB | 1 quark generation | $0.10$ for $f=1,2,3$ | `LPsidB` | coupling of the dim-7 $\overline{d^{c}}\Psi_d B_{\mu\nu}G^{\mu\nu}$ operator |
| `lamu` $\lambda_u^{xf}$ | LAMU | lepton gen. $\times$ quark gen. | $0.1\,\delta_{xf}$ (diagonal) | `LPhiuG` | leptoquark Yukawa-like coupling, $u_R$–$\ell_R$–$\Phi_u$–gluon |
| `lamd` $\lambda_d^{xf}$ | LAMD | lepton gen. $\times$ quark gen. | $0.1\,\delta_{xf}$ (diagonal) | `LPhidG` | leptoquark Yukawa-like coupling, $d_R$–$\ell_R$–$\Phi_d$–gluon |

No internal parameters and no new gauge couplings are declared. The interaction-order hierarchy
is `{QCD,1}, {QED,2}, {NP,1}`; the $\Lambda$'s carry `NP` order $-1$, so every interaction vertex
comes out at net `NP` order $0$ from the $\kappa/\Lambda$ or $\lambda/\Lambda^{n}$ combination
plus the explicit `{NP,1}` on the coupling.

---

## 4. Physics summary

This is a colour-**sextet** extension of the Standard Model containing four new heavy
electroweak-singlet states at $1$ TeV: two Dirac sextet fermions $\Psi_u$ ($Q=-2/3$) and
$\Psi_d$ ($Q=+1/3$), and two complex sextet scalar leptoquarks $\Phi_u$ ($Q=+1/3$) and $\Phi_d$
($Q=+4/3$), each carrying $L=-1$ and $B=-1/3$. The new states do not couple through
renormalisable Yukawa terms; instead they couple only through higher-dimensional,
gluon-field-strength operators built on the invariant $\varepsilon\,T^{a}\bar K^{s}$ that ties
one quark triplet index, one gluon and one sextet index together: dimension-5 chromo-dipole
transitions $\overline{q_R^{c}}\,\sigma^{\mu\nu}\Psi\,G^{a}_{\mu\nu}$, dimension-7
$\overline{q_R^{c}}\,\Psi\,B_{\mu\nu}G^{a\,\mu\nu}$ operators, and dimension-6
$\overline{q_R^{c}}\,\sigma^{\mu\nu}\ell_R\,\Phi\,G^{a}_{\mu\nu}$ leptoquark operators. All
couplings are purely right-handed in the quark and lepton sector.

Phenomenologically this mediates **single, gluon-initiated production** of the sextet states at
a hadron collider: $q g \to \Psi$ (and $q g \to \Psi$ plus a photon/$Z$ via the $B_{\mu\nu}$
operator) through the dipole vertices, and $q g \to \Phi\,\ell$ / resonant $\Phi$ production with
subsequent $\Phi \to q\,\ell\,g$ decay through the leptoquark vertices, on top of QCD pair
production $gg,q\bar q \to \Psi\bar\Psi,\ \Phi\Phi^{\dagger}$ which follows from the sextet
covariant derivatives alone. The signatures are heavy sextet resonances decaying back to
jet + gluon (for $\Psi$) and to jet + charged lepton + gluon (for $\Phi$), with the sextet
colour charge giving markedly larger QCD production rates than a triplet of the same mass.

---

## 5. Consistency note: `LPsiuG` breaks charge conservation as written

Three of the four quark–sextet operators use the charge-conjugated quark,
`CC[uqbar]` / `CC[dqbar]`, but `LPsiuG` uses the plain `uqbar[sp1,ff,i1]`. With the convention
$\psi\to e^{iQ\theta}\psi$, $\overline{\psi^{c}}$ carries charge $+Q_\psi$ while $\overline{\psi}$
carries $-Q_\psi$. Checking every interaction:

| term | bilinear | $\sum Q$ |
|---|---|---|
| `LPsidG` | $\overline{d^{c}}\;\Psi_d$ | $-\tfrac13+\tfrac13=0$ ✅ |
| `LPsiuB` | $\overline{u^{c}}\;\Psi_u$ | $+\tfrac23-\tfrac23=0$ ✅ |
| `LPsidB` | $\overline{d^{c}}\;\Psi_d$ | $-\tfrac13+\tfrac13=0$ ✅ |
| `LPhiuG` | $\overline{u^{c}}\;\ell\;\Phi_u$ | $+\tfrac23-1+\tfrac13=0$ ✅ |
| `LPhidG` | $\overline{d^{c}}\;\ell\;\Phi_d$ | $-\tfrac13-1+\tfrac43=0$ ✅ |
| **`LPsiuG`** | $\overline{u}\;\Psi_u$ | $-\tfrac23-\tfrac23=-\tfrac43$ ❌ |

`LPsiuG` therefore violates electric charge (and hypercharge) by $4/3$, and it also assigns
$\Psi_u$ baryon number $+1/3$, in contradiction with the $B(\Psi_u)=-1/3$ required by `LPsiuB`.
The colour contraction is likewise inconsistent: $\varepsilon_{i i_2 i_3}$ expects the
fundamental-index quark object supplied by $\overline{u^{c}}$ (which transforms as a
$\mathbf 3$), not by $\overline{u}$ (a $\bar{\mathbf 3}$). The chirality also flips from
right-handed ($\overline{(u_R)^{c}}$) in every other term to left-handed
($\overline{u_L}$) here. The intended term is almost certainly

$$
\mathcal{L}_{\Psi_u G}
=\;-\,i\,\frac{\kappa_u^{f}}{\Lambda_{\Psi_u}}\;
\mathcal{K}^{a}_{\,i\,s}\;
\overline{u^{\,c}_{f,i}}\;P_R\,\sigma^{\mu\nu}\,\Psi_{u}^{s}\;G^{a}_{\mu\nu}
\;+\;{\rm h.c.},
$$

i.e. `CC[uqbar]` in place of `uqbar`, which restores exact parallelism with `LPsidG`,
`LPsiuB` and `LPsidB`. §1.2 reports the term as it literally appears in the file.
