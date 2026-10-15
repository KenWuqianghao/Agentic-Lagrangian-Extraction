# Reconstruction of `sanitized.fr`

## 0. Conventions and notation used below

The file is an **add-on module to the FeynRules Standard Model**: it declares no gauge
groups and no SM fields, but uses `uq`, `dq`, `l`, `G`, `B`, `T`, `Eps`, `Ga`, `DC`, `FS`,
`CC`, `HC`, `ProjP`. So the SM gauge group `SU(3)_C x SU(2)_L x U(1)_Y` and the SM field
content are assumed to be already loaded.

New colour representation:

```
IndexRange[Index[Sextet]] = NoUnfold[Range[6]];
AddGaugeRepresentation[SU3C -> {T6, Sextet}];
```

so a **colour-sextet (6) representation of `SU(3)_C`** is added, with generators
$(T_6^a)_{st}$, $s,t = 1\dots 6$.

Symbols used in the equations:

| `.fr` symbol | Meaning here |
| --- | --- |
| $i,j,k,l$ | fundamental (**3**) colour indices, `i1,i2,i3,i4` |
| $s$ | sextet (**6**) colour index, `ss` |
| $a$ | adjoint (**8**) colour index, `aa` |
| $f$ | quark generation, `ff` |
| $x$ | lepton generation, `xx` |
| $(T^a)_{ij}$ | fundamental `SU(3)` generators, `T[aa,i,j]` |
| $\varepsilon_{ijk}$ | `Eps[i1,i2,i3]` |
| $(K^{s})^{*}_{ij}$ | `K6bar[ss,i,j]`, the conjugate sextet Clebsch–Gordan tensor |
| $P_R=\tfrac{1+\gamma_5}{2}$ | `ProjP` |
| $\sigma^{\mu\nu}=\tfrac{i}{2}[\gamma^\mu,\gamma^\nu]$ | `(I/2)(Ga[mu].Ga[nu] - Ga[nu].Ga[mu])` |
| $\overline{q^{c}}$ | `CC[uqbar]`, `CC[dqbar]`; $\overline{q^{c}} = -q^{T}C^{-1}$ |
| $G^{a}_{\mu\nu}$ | `FS[G,mu,nu,aa]` $=\partial_\mu G^a_\nu-\partial_\nu G^a_\mu+g_s f^{abc}G^b_\mu G^c_\nu$ |
| $B_{\mu\nu}$ | `FS[B,mu,nu]` $=\partial_\mu B_\nu-\partial_\nu B_\mu$ |

`K6` is the standard sextet Clebsch–Gordan object. With the usual normalisation it is
symmetric, $K^{s}_{ij}=K^{s}_{ji}$, and obeys

$$ (K^{s})^{*}_{ij}\,K^{t}_{ij}=\delta^{st},\qquad
(K^{s})^{*}_{ij}\,K^{s}_{kl}=\tfrac12\left(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}\right),\qquad
(T_6^a)_{st}=2\,(K^{s})^{*}_{ij}\,(T^a)_{ik}\,K^{t}_{kj}. $$

**Covariant derivative.** No field in this file carries an `SU(2)` index, so every new
field is an `SU(2)_L` singlet and `DC` expands to colour + hypercharge only:

$$ D_\mu \Psi = \Big(\partial_\mu - i g_s\, T_6^{a}\, G^{a}_{\mu} - i g'\, Y\, B_{\mu}\Big)\Psi ,
\qquad
D_\mu \Phi = \Big(\partial_\mu - i g_s\, T_6^{a}\, G^{a}_{\mu} - i g'\, Y\, B_{\mu}\Big)\Phi , $$

with $T_6^a$ the sextet generators and $Y$ the declared hypercharge of the field. For an
`SU(2)` singlet $Q = Y$.

**Common colour tensor.** Every interaction term uses the same colour structure

$$ \mathcal{C}^{a}_{i,s} \;\equiv\; \varepsilon_{ijk}\,(T^{a})_{jl}\,(K^{s})^{*}_{lk}, $$

which is the unique invariant of $\mathbf{3}\otimes\mathbf{6}\otimes\mathbf{8}$
(because $\mathbf{6}\otimes\mathbf{3}=\mathbf{8}\oplus\mathbf{10}$, and
$\mathbf{8}\otimes\mathbf{8}\supset\mathbf{1}$). The $\varepsilon$ tensor makes the sextet
field act, in colour, like a pair of quark (upper **3**) indices.

---

## 1. Lagrangian

### 1.1 `LPsiuFree` — kinetic and mass term of the sextet fermion $\Psi_u$

$$ \mathcal{L}_{\Psi_u}^{\rm free}
= i\,\overline{\Psi}_{u,s}\,\gamma^{\mu}\left(D_\mu \Psi_u\right)_{s}
- M_{\Psi_u}\,\overline{\Psi}_{u,s}\Psi_{u,s},
\qquad
\left(D_\mu\Psi_u\right)_s=\Big(\partial_\mu\delta_{st} - i g_s (T_6^a)_{st}G^a_\mu
+ i \tfrac{2}{3} g' \delta_{st} B_\mu\Big)\Psi_{u,t}. $$

(The hypercharge term uses $Y_{\Psi_u}=-2/3$.)

### 1.2 `LPsidFree` — kinetic and mass term of the sextet fermion $\Psi_d$

$$ \mathcal{L}_{\Psi_d}^{\rm free}
= i\,\overline{\Psi}_{d,s}\,\gamma^{\mu}\left(D_\mu \Psi_d\right)_{s}
- M_{\Psi_d}\,\overline{\Psi}_{d,s}\Psi_{d,s},
\qquad Y_{\Psi_d}=+\tfrac13 . $$

### 1.3 `LPhiuFree` — kinetic and mass term of the sextet scalar $\Phi_u$

$$ \mathcal{L}_{\Phi_u}^{\rm free}
= \left(D^{\mu}\Phi_{u}\right)^{\dagger}_{s}\left(D_{\mu}\Phi_{u}\right)_{s}
- M_{\Phi_u}^{2}\,\Phi^{\dagger}_{u,s}\Phi_{u,s}. $$

### 1.4 `LPhidFree` — kinetic and mass term of the sextet scalar $\Phi_d$

$$ \mathcal{L}_{\Phi_d}^{\rm free}
= \left(D^{\mu}\Phi_{d}\right)^{\dagger}_{s}\left(D_{\mu}\Phi_{d}\right)_{s}
- M_{\Phi_d}^{2}\,\Phi^{\dagger}_{d,s}\Phi_{d,s}. $$

### 1.5 `LPsiuG` — dimension-5 chromomagnetic transition dipole, up-type quark to $\Psi_u$

$$ \mathcal{L}_{\Psi_u G}
= -\,i\,\frac{\kappa_u^{f}}{\Lambda_{\Psi_u}}\;
\varepsilon_{ijk}\,(T^{a})_{jl}\,(K^{s})^{*}_{lk}\;
\overline{\left(u^{c}_{f}\right)}_{i}\;\sigma^{\mu\nu}P_{R}\;\Psi_{u,s}\;
G^{a}_{\mu\nu}\;+\;\mathrm{h.c.} $$

Chirality: $\overline{u^{c}}\,\sigma^{\mu\nu}P_R\,\Psi_u
= \overline{\left(u_{R}\right)^{c}}\,\sigma^{\mu\nu}\,\Psi_{u,R}$, because
$P_R\sigma^{\mu\nu}=\sigma^{\mu\nu}P_R$ and $\overline{u^{c}}P_R=\overline{(u^{c})_L}$ with
$(u^{c})_L=(u_R)^{c}$. So the **right-handed** up-type quark and the **right-handed**
component of $\Psi_u$ take part. The quark enters charge-conjugated (`CC`), so the vertex
absorbs a quark, not an antiquark. $\Lambda_{\Psi_u}=$ `LamPsu`, $\kappa_u^f=$ `kapu[ff]`.

### 1.6 `LPsidG` — dimension-5 chromomagnetic transition dipole, down-type quark to $\Psi_d$

$$ \mathcal{L}_{\Psi_d G}
= -\,i\,\frac{\kappa_d^{f}}{\Lambda_{\Psi_d}}\;
\varepsilon_{ijk}\,(T^{a})_{jl}\,(K^{s})^{*}_{lk}\;
\overline{\left(d^{c}_{f}\right)}_{i}\;\sigma^{\mu\nu}P_{R}\;\Psi_{d,s}\;
G^{a}_{\mu\nu}\;+\;\mathrm{h.c.} $$

Same chirality structure: $\overline{(d_R)^{c}}\,\sigma^{\mu\nu}\,\Psi_{d,R}$.

### 1.7 `LPsiuB` — dimension-7 operator $\;\overline{u^{c}}\Psi_u\, B\!\cdot\! G$

$$ \mathcal{L}_{\Psi_u B}
= -\,i\,\frac{\kappa_{u}^{B,f}}{\Lambda_{\Psi_u B}^{3}}\;
\varepsilon_{ijk}\,(T^{a})_{jl}\,(K^{s})^{*}_{lk}\;
\overline{\left(u^{c}_{f}\right)}_{i}\,P_{R}\,\Psi_{u,s}\;
B_{\mu\nu}\,G^{a\,\mu\nu}\;+\;\mathrm{h.c.} $$

No $\sigma^{\mu\nu}$ here: the fermion bilinear is a scalar bilinear
$\overline{(u_R)^{c}}\,\Psi_{u,R}$, and the two Lorentz indices are contracted between the
hypercharge and the gluon field strengths.

### 1.8 `LPsidB` — dimension-7 operator $\;\overline{d^{c}}\Psi_d\, B\!\cdot\! G$

$$ \mathcal{L}_{\Psi_d B}
= -\,i\,\frac{\kappa_{d}^{B,f}}{\Lambda_{\Psi_d B}^{3}}\;
\varepsilon_{ijk}\,(T^{a})_{jl}\,(K^{s})^{*}_{lk}\;
\overline{\left(d^{c}_{f}\right)}_{i}\,P_{R}\,\Psi_{d,s}\;
B_{\mu\nu}\,G^{a\,\mu\nu}\;+\;\mathrm{h.c.} $$

### 1.9 `LPhiuG` — dimension-6 quark–lepton–scalar–gluon operator (up type)

$$ \mathcal{L}_{\Phi_u G}
= -\,i\,\frac{\lambda_u^{xf}}{\Lambda_{\Phi_u}^{2}}\;
\varepsilon_{ijk}\,(T^{a})_{jl}\,(K^{s})^{*}_{lk}\;\Phi_{u,s}\;
\overline{\left(u^{c}_{f}\right)}_{i}\;\sigma^{\mu\nu}P_{R}\;\ell_{x}\;
G^{a}_{\mu\nu}\;+\;\mathrm{h.c.} $$

Chirality: $\overline{(u_R)^{c}}\,\sigma^{\mu\nu}\,\ell_{x,R}$ — right-handed up-type quark
with right-handed charged lepton, as required for `SU(2)` singlets. The first index of
$\lambda_u$ is the **lepton** generation $x$, the second is the **quark** generation $f$.

### 1.10 `LPhidG` — dimension-6 quark–lepton–scalar–gluon operator (down type)

$$ \mathcal{L}_{\Phi_d G}
= -\,i\,\frac{\lambda_d^{xf}}{\Lambda_{\Phi_d}^{2}}\;
\varepsilon_{ijk}\,(T^{a})_{jl}\,(K^{s})^{*}_{lk}\;\Phi_{d,s}\;
\overline{\left(d^{c}_{f}\right)}_{i}\;\sigma^{\mu\nu}P_{R}\;\ell_{x}\;
G^{a}_{\mu\nu}\;+\;\mathrm{h.c.} $$

### 1.11 `LTotal`

$$ \mathcal{L}_{\rm total}
= \mathcal{L}_{\Psi_u}^{\rm free}+\mathcal{L}_{\Psi_d}^{\rm free}
+ \mathcal{L}_{\Phi_u}^{\rm free}+\mathcal{L}_{\Phi_d}^{\rm free}
+ \mathcal{L}_{\Psi_u G}+\mathcal{L}_{\Psi_d G}
+ \mathcal{L}_{\Psi_u B}+\mathcal{L}_{\Psi_d B}
+ \mathcal{L}_{\Phi_u G}+\mathcal{L}_{\Phi_d G}. $$

The SM Lagrangian is not added here; this module holds only the new-physics part.

Note on the overall phase: each interaction is written as $X+X^{\dagger}$ with an explicit
factor $-i$ inside $X$. The sum is hermitian; the $-i$ is a phase convention.

---

## 2. Field table

All four new fields are colour **sextets** (`Indices -> {Index[Sextet]}`), all are
`SelfConjugate -> False` (complex scalars / Dirac fermions), and none declares an `SU(2)_L`
index, so all are `SU(2)_L` **singlets**. All masses are 1000 (GeV) and all widths 10 (GeV).

| Class | Symbol | Spin | `SU(3)_C` | `SU(2)_L` | $Q$ | $Y$ | $L$ | Self-conj. | Mass | Width | PDG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `S[100]` | $\Phi_u$ (`Phiu`) | 0 | **6** | **1** (not declared) | $+1/3$ | $-1/3$ (see note) | $-1$ | no | `MPHU` = 1000 | `WPHU` = 10 | 9000001 |
| `S[101]` | $\Phi_d$ (`Phid`) | 0 | **6** | **1** (not declared) | $+4/3$ | $+4/3$ | $-1$ | no | `MPHD` = 1000 | `WPHD` = 10 | 9000002 |
| `F[100]` | $\Psi_u$ (`Psiu`) | 1/2 | **6** | **1** (not declared) | $-2/3$ | $-2/3$ | 0 | no | `MPSU` = 1000 | `WPSU` = 10 | 9000011 |
| `F[101]` | $\Psi_d$ (`Psid`) | 1/2 | **6** | **1** (not declared) | $+1/3$ | $+1/3$ | 0 | no | `MPSD` = 1000 | `WPSD` = 10 | 9000012 |

Implied (not declared) baryon numbers, fixed by requiring each interaction term to conserve
$B$: $B(\Psi_u)=B(\Psi_d)=B(\Phi_u)=B(\Phi_d)=-1/3$.

### Note: charge/hypercharge inconsistency for $\Phi_u$

For an `SU(2)_L` singlet the SM relation $Q=T_3+Y$ gives $Q=Y$. Three of the four new
fields satisfy this ($\Phi_d$: $4/3=4/3$; $\Psi_u$: $-2/3=-2/3$; $\Psi_d$: $1/3=1/3$).
$\Phi_u$ does **not**: it declares $Q=+1/3$ but $Y=-1/3$.

Electric-charge conservation of `LPhiuG` fixes the answer independently. The term contains
the fields $u_f$ (charge $+2/3$, entering through `CC[uqbar]`, so it enters with $+2/3$),
$\ell_x$ ($-1$) and $\Phi_u$:

$$ \tfrac23 - 1 + Q_{\Phi_u} = 0 \;\Longrightarrow\; Q_{\Phi_u} = +\tfrac13 . $$

So $Q=+1/3$ is correct and **the declared hypercharge `Y -> -1/3` has the wrong sign**; it
should be $Y=+1/3$. This is not cosmetic: $Y$ enters the covariant derivative in
`LPhiuFree`, so as written $\Phi_u$ couples to $B_\mu$ (hence to the photon and the $Z$)
with the sign of a charge $-1/3$ state while all its other vertices treat it as a charge
$+1/3$ state. The same cross-checks on the other three fields give $Q_{\Phi_d}=+4/3$
($-1/3-1+Q=0$), $Q_{\Psi_u}=-2/3$ ($+2/3+Q=0$) and $Q_{\Psi_d}=+1/3$ ($-1/3+Q=0$), all
matching their declarations.

---

## 3. External parameters

### 3.1 Cutoff scales — block `SXTCUTOFF`, all `Value -> 1000.` (GeV), `InteractionOrder -> {NP,-1}`

| Symbol | Block order | Multiplies | Meaning |
| --- | --- | --- | --- |
| `LamPsu` $\Lambda_{\Psi_u}$ | 1 | $\kappa_u^f/\Lambda_{\Psi_u}$ in `LPsiuG` | effective-theory cutoff of the dim-5 $u$–$\Psi_u$–$g$ dipole |
| `LamPsd` $\Lambda_{\Psi_d}$ | 2 | $\kappa_d^f/\Lambda_{\Psi_d}$ in `LPsidG` | cutoff of the dim-5 $d$–$\Psi_d$–$g$ dipole |
| `LamPsuB` $\Lambda_{\Psi_u B}$ | 3 | $\kappa_u^{B,f}/\Lambda_{\Psi_u B}^{3}$ in `LPsiuB` | cutoff of the dim-7 $u$–$\Psi_u$–$g$–$B$ operator |
| `LamPsdB` $\Lambda_{\Psi_d B}$ | 4 | $\kappa_d^{B,f}/\Lambda_{\Psi_d B}^{3}$ in `LPsidB` | cutoff of the dim-7 $d$–$\Psi_d$–$g$–$B$ operator |
| `LamPhu` $\Lambda_{\Phi_u}$ | 5 | $\lambda_u^{xf}/\Lambda_{\Phi_u}^{2}$ in `LPhiuG` | cutoff of the dim-6 $u$–$\ell$–$\Phi_u$–$g$ operator |
| `LamPhd` $\Lambda_{\Phi_d}$ | 6 | $\lambda_d^{xf}/\Lambda_{\Phi_d}^{2}$ in `LPhidG` | cutoff of the dim-6 $d$–$\ell$–$\Phi_d$–$g$ operator |

Each $\Lambda$ carries `InteractionOrder {NP,-1}`, so $1/\Lambda$ counts as one power of
`NP`. The dipole vertices are therefore $NP^2$, the dim-6 vertices $NP^3$ and the dim-7
vertices $NP^4$.

### 3.2 Dimensionless couplings, all `InteractionOrder -> {NP,1}`

| Symbol | Indices | Block | Value | Multiplies | Meaning |
| --- | --- | --- | --- | --- | --- |
| `kapu[f]` $\kappa_u^{f}$ | quark generation | `KAPU` | $0.05,0.05,0.05$ | `LPsiuG` | strength of the chromomagnetic $u_{R,f}\!-\!\Psi_{u,R}\!-\!g$ transition dipole, one value per up-type generation |
| `kapd[f]` $\kappa_d^{f}$ | quark generation | `KAPD` | $0.05,0.05,0.05$ | `LPsidG` | same for down-type quarks and $\Psi_d$ |
| `kapuB[f]` $\kappa_u^{B,f}$ | quark generation | `KAPUB` | $0.10,0.10,0.10$ | `LPsiuB` | strength of the $u_{R,f}\!-\!\Psi_{u,R}\!-\!g\!-\!B$ operator |
| `kapdB[f]` $\kappa_d^{B,f}$ | quark generation | `KAPDB` | $0.10,0.10,0.10$ | `LPsidB` | same for down-type quarks and $\Psi_d$ |
| `lamu[x,f]` $\lambda_u^{xf}$ | lepton gen. $x$, quark gen. $f$ | `LAMU` | diagonal $0.1$ | `LPhiuG` | lepton-flavour x quark-flavour matrix of the $u_{R}\!-\!\ell_{R}\!-\!\Phi_u\!-\!g$ operator; diagonal values keep lepton flavour aligned with quark generation |
| `lamd[x,f]` $\lambda_d^{xf}$ | lepton gen. $x$, quark gen. $f$ | `LAMD` | diagonal $0.1$ | `LPhidG` | same for down-type quarks and $\Phi_d$ |

All six couplings are real external inputs. Masses (`MPHU`, `MPHD`, `MPSU`, `MPSD`) and
widths (`WPHU`, `WPHD`, `WPSU`, `WPSD`) are external too, through the class declarations,
each 1000 GeV and 10 GeV.

---

## 4. Physics summary

This is a colour-**sextet** extension of the Standard Model. It adds two Dirac fermions
($\Psi_u$ with $Q=-2/3$, $\Psi_d$ with $Q=+1/3$) and two complex scalars ($\Phi_u$ with
$Q=+1/3$, $\Phi_d$ with $Q=+4/3$, both with lepton number $-1$), all in the **6** of
`SU(3)_C`, all `SU(2)_L` singlets and all at 1 TeV. There is no renormalisable coupling to
the SM: every interaction is a higher-dimensional operator that needs a **gluon field
strength**, so each new state connects to exactly one right-handed quark only together with
a gluon — the fermions through a dimension-5 chromomagnetic dipole $\overline{q^{c}_R}
\sigma^{\mu\nu}\Psi_R G_{\mu\nu}/\Lambda$ and a dimension-7 $\overline{q^{c}_R}\Psi_R
B_{\mu\nu}G^{\mu\nu}/\Lambda^{3}$, the scalars through a dimension-6 leptoquark-type
$\overline{q^{c}_R}\sigma^{\mu\nu}\ell_R \Phi\, G_{\mu\nu}/\Lambda^{2}$.

At a hadron collider the model gives QCD pair production of all four states (the sextet
colour charge makes this large), plus single production through the new operators:
$q g \to \Psi_{u,d}$ with $\Psi \to q g$ (a dijet-like resonance) and, from the dim-7
operator, $\Psi \to q g \gamma / q g Z$. The scalars appear in associated production
$q g \to \Phi\,\ell^{\pm}$ and decay back through the same four-point vertex, $\Phi \to
q\,\ell\,g$, giving lepton + jets final states with lepton-flavour structure set by
$\lambda_{u,d}^{xf}$. Lepton number is conserved by the declared $L=-1$ of the scalars;
baryon number is conserved only if the new states are given $B=-1/3$, which the file does
not declare — in colour the $\varepsilon_{ijk}$ structure makes each sextet behave like a
diquark.
