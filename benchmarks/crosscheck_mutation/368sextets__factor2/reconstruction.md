# Reconstruction of `sanitized.fr`

## 0. Conventions and setup

The file is a FeynRules *add-on* model. It uses, but does not define, the Standard Model
fields and couplings: the quark mass eigenstates `uq`, `dq`, the charged lepton `l`,
the gluon `G`, the hypercharge boson `B`, the fundamental generators `T[a,i,j]`, and the
strong coupling. It must be loaded together with the SM model file.

Index conventions used below:

| Symbol | Meaning | Range |
| --- | --- | --- |
| $i,j,k,l$ | SU(3)$_C$ fundamental (triplet) index | 1–3 |
| $a$ | SU(3)$_C$ adjoint index | 1–8 |
| $s$ | SU(3)$_C$ sextet index (`Index[Sextet]`, `IndexStyle -> s`) | 1–6 |
| $f$ | quark generation index | 1–3 |
| $x$ | lepton generation index | 1–3 |
| $\mu,\nu$ | Lorentz index | 0–3 |

The line

```
AddGaugeRepresentation[SU3C -> {T6, Sextet}];
```

declares a new SU(3)$_C$ representation: the sextet **6**, with generators
$(T_6^a)_{ss'}$. The tensor `K6bar[s,i,j]` is the conjugate Clebsch–Gordan tensor of this
representation. It is symmetric in $(i,j)$ and it maps a pair of triplet indices onto one
sextet index. Write it as $\bar K^{s}_{\,ij}$, with
$\bar K^{s}_{\,ij} = (K^{s}_{\,ij})^{*}$ and $\bar K^{s}_{\,ij} K^{s'}_{\,ij} = \delta^{ss'}$.

Every interaction term uses the same colour tensor. Define it once:

$$
\mathcal{C}^{\,a,s}_{\;i_1}\;\equiv\;\epsilon^{\,i_1 i_2 i_3}\,(T^{a})_{i_2 i_4}\,\bar K^{s}_{\,i_4 i_3}
$$

It carries one triplet index $i_1$ (contracted with a SM quark), one adjoint index $a$
(contracted with the gluon field strength), and one sextet index $s$ (contracted with the
new sextet field). The product $\mathbf{3}\otimes\mathbf{8}\otimes\mathbf{6}$ contains a
singlet, so each term is colour neutral.

FeynRules idioms are expanded as follows:

* `Ga[mu]` $\to \gamma^{\mu}$.
* `(I/2)(Ga[mu].Ga[nu] - Ga[nu].Ga[mu])` $\to \sigma^{\mu\nu} = \tfrac{i}{2}[\gamma^{\mu},\gamma^{\nu}]$.
* `ProjP` $\to P_R = \tfrac{1}{2}(1+\gamma_5)$. (`ProjM` does not appear; every vertex is purely right-handed.)
* `CC[uqbar]` $\to \overline{u^{c}}$, the Dirac adjoint of the charge-conjugate up-type quark. Because $P_L\,\psi^{c} = (\psi_R)^{c}$, the combination $\overline{u^{c}}\,P_R$ equals $\overline{(u_R)^{c}}$: only the **right-handed** quark takes part.
* `FS[G,mu,nu,a]` $\to G^{a}_{\mu\nu} = \partial_\mu G^a_\nu - \partial_\nu G^a_\mu + g_s f^{abc} G^b_\mu G^c_\nu$ (the non-abelian part gives the extra two-gluon vertex).
* `FS[B,mu,nu]` $\to B_{\mu\nu} = \partial_\mu B_\nu - \partial_\nu B_\mu$.
* `HC[tmp]` $\to +\,\text{h.c.}$
* `DC[.,mu]` $\to D_\mu$ (see below).

**Covariant derivative.** All four new fields carry a sextet colour index and a
hypercharge `Y`. No SU(2)$_L$ quantum number and no SU(2) index are declared, so every new
field is an SU(2)$_L$ singlet. For a sextet field $X^{s}$ with hypercharge $Y_X$:

$$
(D_\mu X)^{s} \;=\; \partial_\mu X^{s} \;-\; i\,g_s\,G^{a}_{\mu}\,(T_6^{a})^{ss'}X^{s'}\;-\;i\,g_1\,Y_X\,B_\mu\,X^{s}
$$

with $B_\mu = c_W A_\mu - s_W Z_\mu$ and $e = g_1 c_W$. Because $T^3 = 0$ for these
fields, $Q = Y$, which the file confirms: every class declares the same value for `Q` and
`Y`. So the derivative contains the gluon (sextet rep), the photon with strength $eQ$, and
the $Z$ with strength $-g_1 s_W Y$. There is no $W^{\pm}$ coupling.

The interaction order hierarchy is `{QCD,1}, {QED,2}, {NP,1}`.

---

## 1. Lagrangian

The total Lagrangian is

$$
\mathcal{L}_{\rm total} = \mathcal{L}_{\Psi_u}^{\rm free} + \mathcal{L}_{\Psi_d}^{\rm free}
+ \mathcal{L}_{\Phi_u}^{\rm free} + \mathcal{L}_{\Phi_d}^{\rm free}
+ \mathcal{L}_{\Psi_u G} + \mathcal{L}_{\Psi_d G}
+ \mathcal{L}_{\Psi_u B} + \mathcal{L}_{\Psi_d B}
+ \mathcal{L}_{\Phi_u G} + \mathcal{L}_{\Phi_d G}
$$

(`LTotal`). Each piece follows.

### 1.1 `LPsiuFree`

$$
\mathcal{L}_{\Psi_u}^{\rm free} \;=\; i\,\overline{\Psi}_u^{\,s}\,\gamma^{\mu}\,(D_\mu \Psi_u)^{s}\;-\;M_{\Psi_u}\,\overline{\Psi}_u^{\,s}\,\Psi_u^{\,s}
$$

$\Psi_u$ is a vector-like Dirac fermion. $D_\mu$ uses the sextet generators $T_6^a$ and
$Y_{\Psi_u} = -2/3$.

### 1.2 `LPsidFree`

$$
\mathcal{L}_{\Psi_d}^{\rm free} \;=\; i\,\overline{\Psi}_d^{\,s}\,\gamma^{\mu}\,(D_\mu \Psi_d)^{s}\;-\;M_{\Psi_d}\,\overline{\Psi}_d^{\,s}\,\Psi_d^{\,s}
$$

with $Y_{\Psi_d} = +1/3$.

### 1.3 `LPhiuFree`

$$
\mathcal{L}_{\Phi_u}^{\rm free} \;=\; (D^{\mu}\Phi_u^{\,s})^{\dagger}\,(D_\mu \Phi_u^{\,s})\;-\;M_{\Phi_u}^{2}\,\Phi_u^{\,s\dagger}\,\Phi_u^{\,s}
$$

$\Phi_u$ is a complex scalar. $Y_{\Phi_u} = +1/3$. No scalar self-interaction and no Higgs
portal term is present.

### 1.4 `LPhidFree`

$$
\mathcal{L}_{\Phi_d}^{\rm free} \;=\; (D^{\mu}\Phi_d^{\,s})^{\dagger}\,(D_\mu \Phi_d^{\,s})\;-\;M_{\Phi_d}^{2}\,\Phi_d^{\,s\dagger}\,\Phi_d^{\,s}
$$

with $Y_{\Phi_d} = +4/3$.

### 1.5 `LPsiuG` — chromomagnetic dipole, up-type quark + sextet fermion

Dimension-5 operator, suppressed by one power of $\Lambda_{\Psi u}$.
**Note the explicit overall factor of 2 in the file** (`LPsiuG := 2 (...)`), which the
down-type partner `LPsidG` does not have:

$$
\mathcal{L}_{\Psi_u G} \;=\; 2\left\{\,-\,i\,\frac{\kappa_u^{f}}{\Lambda_{\Psi u}}\;
\mathcal{C}^{\,a,s}_{\;i_1}\;
\overline{\left(u^{c}_{f}\right)}_{i_1}\,\sigma^{\mu\nu}P_R\,\Psi_u^{\,s}\;G^{a}_{\mu\nu}\;+\;\text{h.c.}\right\}
$$

In fully explicit index form:

$$
\mathcal{L}_{\Psi_u G} = 2\left\{-\,i\,\frac{\kappa_u^{f}}{\Lambda_{\Psi u}}\,
\epsilon^{\,i_1 i_2 i_3}(T^{a})_{i_2 i_4}\bar K^{s}_{\,i_4 i_3}\,
\overline{u^{c}_{f}}{}_{\,i_1}\,P_R\,\tfrac{i}{2}\big[\gamma^{\mu},\gamma^{\nu}\big]\,\Psi_{u,s}\,G^{a}_{\mu\nu} + \text{h.c.}\right\}
$$

$P_R$ commutes with $\sigma^{\mu\nu}$, so the two orderings agree. The chirality structure
is $\overline{(u_R)^{c}}\,\sigma^{\mu\nu}\,P_R\Psi_u$: a same-chirality (charge-conjugate)
bilinear, not a vector current.

### 1.6 `LPsidG` — chromomagnetic dipole, down-type quark + sextet fermion

$$
\mathcal{L}_{\Psi_d G} \;=\; -\,i\,\frac{\kappa_d^{f}}{\Lambda_{\Psi d}}\;
\epsilon^{\,i_1 i_2 i_3}(T^{a})_{i_2 i_4}\bar K^{s}_{\,i_4 i_3}\;
\overline{\left(d^{c}_{f}\right)}_{i_1}\,\sigma^{\mu\nu}P_R\,\Psi_d^{\,s}\;G^{a}_{\mu\nu}\;+\;\text{h.c.}
$$

This is the exact image of §1.5 with $u\to d$, $\kappa_u\to\kappa_d$,
$\Lambda_{\Psi u}\to\Lambda_{\Psi d}$, $\Psi_u\to\Psi_d$ — **and with no factor of 2**.

### 1.7 `LPsiuB` — mixed $B$–$G$ operator, up-type

Dimension-7 operator, suppressed by $\Lambda_{\Psi u B}^{3}$. There is no $\sigma^{\mu\nu}$
here: the bilinear is a chiral scalar, and the Lorentz indices of the two field strengths
are contracted with each other.

$$
\mathcal{L}_{\Psi_u B} \;=\; -\,i\,\frac{\kappa^{B,f}_{u}}{\Lambda_{\Psi u B}^{3}}\;
\epsilon^{\,i_1 i_2 i_3}(T^{a})_{i_2 i_4}\bar K^{s}_{\,i_4 i_3}\;
\overline{\left(u^{c}_{f}\right)}_{i_1}P_R\,\Psi_u^{\,s}\;B_{\mu\nu}\,G^{a\,\mu\nu}\;+\;\text{h.c.}
$$

### 1.8 `LPsidB` — mixed $B$–$G$ operator, down-type

$$
\mathcal{L}_{\Psi_d B} \;=\; -\,i\,\frac{\kappa^{B,f}_{d}}{\Lambda_{\Psi d B}^{3}}\;
\epsilon^{\,i_1 i_2 i_3}(T^{a})_{i_2 i_4}\bar K^{s}_{\,i_4 i_3}\;
\overline{\left(d^{c}_{f}\right)}_{i_1}P_R\,\Psi_d^{\,s}\;B_{\mu\nu}\,G^{a\,\mu\nu}\;+\;\text{h.c.}
$$

### 1.9 `LPhiuG` — quark–lepton–scalar dipole, up-type

Dimension-6 operator, suppressed by $\Lambda_{\Phi u}^{2}$. The sextet scalar $\Phi_u$
replaces the sextet fermion, and the second fermion leg is a SM charged lepton $\ell_x$.

$$
\mathcal{L}_{\Phi_u G} \;=\; -\,i\,\frac{\lambda_u^{\,x f}}{\Lambda_{\Phi u}^{2}}\;
\epsilon^{\,i_1 i_2 i_3}(T^{a})_{i_2 i_4}\bar K^{s}_{\,i_4 i_3}\;\Phi_u^{\,s}\;
\overline{\left(u^{c}_{f}\right)}_{i_1}\,\sigma^{\mu\nu}\,P_R\,\ell_{x}\;G^{a}_{\mu\nu}\;+\;\text{h.c.}
$$

Index order matters: `lamu[xx,ff]` carries the **lepton** generation first and the
**quark** generation second. The lepton enters right-handed ($P_R \ell_x$), and the quark
enters as $\overline{(u_R)^{c}}$. $\Phi_u$ appears unconjugated, contracted with
$\bar K^{s}$.

### 1.10 `LPhidG` — quark–lepton–scalar dipole, down-type

$$
\mathcal{L}_{\Phi_d G} \;=\; -\,i\,\frac{\lambda_d^{\,x f}}{\Lambda_{\Phi d}^{2}}\;
\epsilon^{\,i_1 i_2 i_3}(T^{a})_{i_2 i_4}\bar K^{s}_{\,i_4 i_3}\;\Phi_d^{\,s}\;
\overline{\left(d^{c}_{f}\right)}_{i_1}\,\sigma^{\mu\nu}\,P_R\,\ell_{x}\;G^{a}_{\mu\nu}\;+\;\text{h.c.}
$$

### 1.11 Structural remarks

* Every interaction is a **gluon field-strength (dipole) operator**. There is no
  renormalizable Yukawa-type coupling between the new states and the SM.
* Every interaction picks the **right-handed** quark and the **right-handed** lepton only.
* Every interaction uses the **charge-conjugate** quark bilinear
  $\overline{q^{c}}\,\Gamma\,X$, never $\bar q\,\Gamma\,X$.
* The explicit $-i$ prefactor, added to its hermitian conjugate, gives a hermitian
  Lagrangian of the form $-i(\mathcal{O}-\mathcal{O}^{\dagger})$.
* **Asymmetry to flag:** `LPsiuG` carries an overall factor of 2 that `LPsidG` does not.
  Nothing else in the file breaks the $u \leftrightarrow d$ symmetry of the operator set
  (`LPsiuB`/`LPsidB` and `LPhiuG`/`LPhidG` are exact mirrors). All up-type $\Psi$ dipole
  couplings are therefore effectively $2\kappa_u^f/\Lambda_{\Psi u}$.

---

## 2. Field table

All four new classes are SU(2)$_L$ singlets (no SU(2) index and no `SU2W` quantum number
declared), all are colour **sextets**, and all have $Q = Y$. Masses and widths are in GeV.

| Class | `ClassName` | Spin | SU(3)$_C$ | SU(2)$_L$ | $Y$ | $Q$ | Lepton no. | Self-conj. | Mass | Width | PDG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `S[100]` | $\Phi_u$ (`Phiu`) | 0 | **6** | **1** | $+1/3$ | $+1/3$ | $-1$ | No | `MPHU` = 1000 | `WPHU` = 10 | 9000001 |
| `S[101]` | $\Phi_d$ (`Phid`) | 0 | **6** | **1** | $+4/3$ | $+4/3$ | $-1$ | No | `MPHD` = 1000 | `WPHD` = 10 | 9000002 |
| `F[100]` | $\Psi_u$ (`Psiu`) | 1/2 (Dirac) | **6** | **1** | $-2/3$ | $-2/3$ | — | No | `MPSU` = 1000 | `WPSU` = 10 | 9000011 |
| `F[101]` | $\Psi_d$ (`Psid`) | 1/2 (Dirac) | **6** | **1** | $+1/3$ | $+1/3$ | — | No | `MPSD` = 1000 | `WPSD` = 10 | 9000012 |

Particle / antiparticle names: `phiu`/`phiu~`, `phid`/`phid~`, `psiu`/`psiu~`,
`psid`/`psid~`. Propagator types: dashed (`D`) for the scalars, straight for the fermions;
all arrows forward, as required for non-self-conjugate fields.

Baryon number is not declared, but the vertices fix it. Charge conservation at the
vertices gives:

* $\Psi_u$ behaves as a sextet partner of $u^{c}_{R}$: $Q=-2/3$, and the vertex
  $\overline{u^{c}}\Psi_u$ needs $B(\Psi_u) = -1/3$.
* $\Psi_d$ behaves as a sextet partner of $d^{c}_{R}$: $Q=+1/3$, $B(\Psi_d) = -1/3$.
* $\Phi_u$ and $\Phi_d$ are **leptoquark-like**: with the declared $L=-1$ and the vertex
  $\overline{q^{c}}\,\ell\,\Phi$, they need $B = -1/3$. The charges work out:
  $Q(\overline{u^{c}}\ell) = 2/3-1 = -1/3 = -Q(\Phi_u)$, and
  $Q(\overline{d^{c}}\ell) = -1/3-1 = -4/3 = -Q(\Phi_d)$.

---

## 3. External parameters

### 3.1 Cut-off scales — block `SXTCUTOFF`, all `InteractionOrder -> {NP,-1}`

| Symbol | Block order | Value | Multiplies (appears in denominator of) | Meaning |
| --- | --- | --- | --- | --- |
| `LamPsu` $\Lambda_{\Psi u}$ | 1 | 1000. | $\mathcal{L}_{\Psi_u G}$, power 1 | New-physics scale of the up-type fermion chromomagnetic dipole |
| `LamPsd` $\Lambda_{\Psi d}$ | 2 | 1000. | $\mathcal{L}_{\Psi_d G}$, power 1 | Same, down-type |
| `LamPsuB` $\Lambda_{\Psi u B}$ | 3 | 1000. | $\mathcal{L}_{\Psi_u B}$, power 3 | Scale of the up-type $B_{\mu\nu}G^{\mu\nu}$ operator |
| `LamPsdB` $\Lambda_{\Psi d B}$ | 4 | 1000. | $\mathcal{L}_{\Psi_d B}$, power 3 | Same, down-type |
| `LamPhu` $\Lambda_{\Phi u}$ | 5 | 1000. | $\mathcal{L}_{\Phi_u G}$, power 2 | Scale of the up-type quark–lepton–scalar dipole |
| `LamPhd` $\Lambda_{\Phi d}$ | 6 | 1000. | $\mathcal{L}_{\Phi_d G}$, power 2 | Same, down-type |

All six have dimension of mass (GeV). All are set to 1 TeV, equal to every new particle
mass.

### 3.2 Dimensionless couplings — all `InteractionOrder -> {NP,1}`

| Symbol | Block | Indices | Value | Multiplies | Meaning |
| --- | --- | --- | --- | --- | --- |
| `kapu` $\kappa_u^{f}$ | `KAPU` | quark generation $f$ | 0.05, 0.05, 0.05 | $\overline{u^{c}_f}\sigma^{\mu\nu}P_R\Psi_u G^{a}_{\mu\nu}$ | Flavour-diagonal chromomagnetic dipole coupling, up-type fermion |
| `kapd` $\kappa_d^{f}$ | `KAPD` | quark generation $f$ | 0.05, 0.05, 0.05 | $\overline{d^{c}_f}\sigma^{\mu\nu}P_R\Psi_d G^{a}_{\mu\nu}$ | Same, down-type |
| `kapuB` $\kappa_u^{B,f}$ | `KAPUB` | quark generation $f$ | 0.10, 0.10, 0.10 | $\overline{u^{c}_f}P_R\Psi_u\,B_{\mu\nu}G^{a\,\mu\nu}$ | Coupling of the mixed hypercharge–gluon operator, up-type |
| `kapdB` $\kappa_d^{B,f}$ | `KAPDB` | quark generation $f$ | 0.10, 0.10, 0.10 | $\overline{d^{c}_f}P_R\Psi_d\,B_{\mu\nu}G^{a\,\mu\nu}$ | Same, down-type |
| `lamu` $\lambda_u^{xf}$ | `LAMU` | (lepton gen $x$, quark gen $f$) | $0.1\,\delta_{xf}$ | $\Phi_u\,\overline{u^{c}_f}\sigma^{\mu\nu}P_R\ell_x G^{a}_{\mu\nu}$ | Lepton-flavour matrix of the up-type leptoquark dipole |
| `lamd` $\lambda_d^{xf}$ | `LAMD` | (lepton gen $x$, quark gen $f$) | $0.1\,\delta_{xf}$ | $\Phi_d\,\overline{d^{c}_f}\sigma^{\mu\nu}P_R\ell_x G^{a}_{\mu\nu}$ | Lepton-flavour matrix of the down-type leptoquark dipole |

`lamu` and `lamd` are set to $0.1$ on the diagonal and zero off it, so the benchmark point
has no lepton-flavour violation. All six couplings are real at the benchmark point.

Masses and widths (`MPHU`, `MPHD`, `MPSU`, `MPSD`, `WPHU`, `WPHD`, `WPSU`, `WPSD`) are
declared inside the particle classes; each mass is 1000 GeV and each width is 10 GeV.

**New-physics order counting.** A coupling counts `NP` $= +1$ and each cut-off counts
`NP` $= -1$ in the denominator, so: the $\Psi G$ vertices are `NP` $=2$, the $\Phi G$
vertices are `NP` $=3$, and the $\Psi B$ vertices are `NP` $=4$.

---

## 4. Physics summary

This model adds four heavy colour-**sextet** states at 1 TeV: two vector-like Dirac
fermions $\Psi_u$ ($Q=-2/3$) and $\Psi_d$ ($Q=+1/3$), which are sextet partners of the
right-handed up-type and down-type antiquarks, and two complex scalars $\Phi_u$ ($Q=1/3$)
and $\Phi_d$ ($Q=4/3$) with lepton number $-1$, which act as sextet leptoquarks. All are
SU(2)$_L$ singlets. They have normal QCD and electroweak gauge couplings through the
covariant derivative, but they talk to the SM matter fields **only** through
higher-dimension dipole operators built on the gluon field strength, with right-handed,
charge-conjugated quark bilinears and 1 TeV cut-off scales.

At a hadron collider the model gives: QCD pair production of the sextets (the sextet
colour factor makes this large); single production of $\Psi_{u,d}$ in quark–gluon fusion,
$q\,g \to \Psi$, through the $\kappa$ dipole, with the decay back to $q + g$, so a dijet or
$jj$-resonance signature; associated production with a photon or a $Z$ through the
$\kappa^{B}$ operator, $q\,g \to \Psi\,\gamma/Z$; and, from the $\lambda$ operators,
single production and decay of the scalars in the lepton-plus-jet channel,
$q\,g \to \Phi\,\ell$ and $\Phi \to q\,\ell\,g$. Because $G^{a}_{\mu\nu}$ contains the
non-abelian term, every dipole operator also produces a two-gluon contact vertex, so
$gg$-initiated and extra-jet channels come with the same couplings.

One point for the reviewer: the up-type fermion dipole term `LPsiuG` carries an extra
overall factor of 2 that its down-type mirror `LPsidG` does not. Every other operator pair
in the file is symmetric under $u \leftrightarrow d$. Check whether this factor is
intended.
