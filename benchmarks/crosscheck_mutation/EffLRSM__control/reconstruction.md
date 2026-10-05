# Reconstruction of `sanitized.fr`

## 0. Conventions and scope

The file adds three new particle classes and eight Lagrangian pieces on top of the
Standard Model Lagrangian `LSM`:

```
LTotal := LSM + LWRkin + LZRkin + LNkin + LWRq + LWRl + LZRq + LZRl;
```

Conventions used below:

- `ProjP` = $P_R=\tfrac{1+\gamma_5}{2}$, `ProjM` = $P_L=\tfrac{1-\gamma_5}{2}$.
- `Ga[mu]` = $\gamma^\mu$. `del[X,mu]` = $\partial_\mu X$. `HC[...]` = $+\,\mathrm{h.c.}$
- `CC[psibar]` = $\overline{\psi^{c}}$, with $\psi^{c}=C\bar\psi^{T}$.
- `FS[V,mu,nu]` for a vector that is **not** a declared gauge field is the abelian
  field strength $V_{\mu\nu}=\partial_\mu V_\nu-\partial_\nu V_\mu$. No group
  structure constant enters, so the new vectors have **no self-interactions**.
- SM fields keep their FeynRules names: `uq`$\to u_i$, `dq`$\to d_i$, `l`$\to \ell_i$,
  `vl`$\to \nu_i$, all with a generation index $i$.

**Covariant derivative.** The file itself never calls `DC`. All covariant
derivatives come from `LSM`, and their gauge content is the unbroken Standard Model
group $SU(3)_c\times SU(2)_L\times U(1)_Y$:

$$
D_\mu \;=\; \partial_\mu \;-\; i\,g_s\,T^a G^a_\mu \;-\; i\,g_w\,T^i W^i_\mu \;-\; i\,g_1\,Y B_\mu .
$$

The new vectors $W_R^\pm$ and $Z_R$ are **not** declared as gauge bosons of any new
group. They are mass-eigenstate (Proca) fields. Their masses are put in by hand, and
they reach the Standard Model only through the explicit current terms below. So this
is an *effective* right-handed sector, not a linearly realised extended gauge model.

---

## 1. Lagrangian terms

### 1.1 `LWRkin` — charged heavy vector kinetic and mass term

$$
\mathcal{L}_{W_R}^{\rm kin}
= -\tfrac{1}{2}\,W_{R\,\mu\nu}^{\dagger}\,W_R^{\mu\nu}
\;+\; M_{W_R}^{2}\,W_{R\,\mu}^{\dagger}\,W_R^{\mu},
\qquad
W_{R\,\mu\nu}=\partial_\mu W_{R\,\nu}-\partial_\nu W_{R\,\mu}.
$$

$W_R$ is complex (electric charge $+1$), so the mass term carries no $\tfrac12$.
The kinetic normalisation $-\tfrac12 W^\dagger_{\mu\nu}W^{\mu\nu}$ is the standard
FeynRules form for a charged vector, in which `FS[WRbar,...]FS[WR,...]` already
supplies the two cross terms of a real $-\tfrac14 F^2$ pair.

### 1.2 `LZRkin` — neutral heavy vector kinetic and mass term

$$
\mathcal{L}_{Z_R}^{\rm kin}
= -\tfrac{1}{4}\,Z_{R\,\mu\nu}Z_R^{\mu\nu}
\;+\; \tfrac{1}{2}\,M_{Z_R}^{2}\,Z_{R\,\mu}Z_R^{\mu},
\qquad
Z_{R\,\mu\nu}=\partial_\mu Z_{R\,\nu}-\partial_\nu Z_{R\,\mu}.
$$

$Z_R$ is real (self-conjugate), so both factors carry the real-field $\tfrac14$ and
$\tfrac12$ normalisation.

### 1.3 `LNkin` — heavy Majorana neutrino kinetic and mass term

$$
\mathcal{L}_{N}^{\rm kin}
= \frac{i}{2}\,\overline{N_f}\,\gamma^\mu\,\partial_\mu N_f
\;-\;\frac{1}{2}\,M_{N_f}\,\overline{N_f}\,N_f ,
\qquad f=1,2,3 .
$$

The $\tfrac12$ factors are the Majorana normalisation. The mass matrix is diagonal in
the generation index $f$, with eigenvalues $M_{N_f}=\{m_{n1},m_{n2},m_{n3}\}$.
The sum over $f$ is implicit.

### 1.4 `LWRq` — right-handed charged quark current

$$
\mathcal{L}_{W_R}^{q}
= -\frac{\kappa_R^{q}\,g_w}{\sqrt{2}}\;
\overline{u_i}\,\bigl(V^{R}_{\rm CKM}\bigr)_{ij}\,\gamma^\mu P_R\, d_j\; W_{R\,\mu}
\;+\;\mathrm{h.c.}
$$

Written out, the hermitian conjugate is
$-\dfrac{\kappa_R^{q} g_w}{\sqrt{2}}\,\overline{d_j}\,\bigl(V^{R\,\dagger}_{\rm CKM}\bigr)_{ji}\,\gamma^\mu P_R\,u_i\,W_{R\,\mu}^{\dagger}$.

Chirality is purely **right-handed** ($P_R$): only $u_R$ and $d_R$ take part.
Index contraction: the up-type field is the barred one and carries the first index of
$V^R_{\rm CKM}$.

### 1.5 `LWRl` — right-handed charged lepton current

$$
\mathcal{L}_{W_R}^{\ell}
= -\frac{\kappa_R^{l}\,g_w}{\sqrt{2}}\;
\Bigl[\;
\overline{N_i}\,(Y_N)_{ij}\,\gamma^\mu P_R\,\ell_j
\;+\;
\overline{\nu_i^{\,c}}\,(X_N)_{ij}\,\gamma^\mu P_R\,\ell_j
\;\Bigr]\; W_{R\,\mu}
\;+\;\mathrm{h.c.}
$$

Two points on conjugation:

- The second current uses `CC[vlbar]`, that is $\overline{\nu^{c}}$ and not
  $\overline{\nu}$. It is the light-neutrino analogue of the heavy-$N$ current, and
  it lets $W_R$ couple to the light mass eigenstates through the mixing matrix $X_N$.
  With the default $X_N=0$ this term gives no vertex.
- $N$ is self-conjugate, so $\overline{N}\gamma^\mu P_R \ell$ and its conjugate both
  describe the same Majorana field. This is the source of lepton-number violation.

### 1.6 `LZRq` — neutral heavy-vector quark current

$$
\mathcal{L}_{Z_R}^{q}
= -\frac{\kappa_R^{q}\,g_w}{n_{Z_R}^{q}}\;
\Bigl[\;
g^{u}_{L}\,\overline{u}\,\gamma^\mu P_L\,u
+ g^{u}_{R}\,\overline{u}\,\gamma^\mu P_R\,u
+ g^{d}_{L}\,\overline{d}\,\gamma^\mu P_L\,d
+ g^{d}_{R}\,\overline{d}\,\gamma^\mu P_R\,d
\;\Bigr]\; Z_{R\,\mu}.
$$

The current is flavour-diagonal, and the generation index is summed. No `HC` is
needed: the expression is already hermitian, because $Z_R$ is real and the couplings
are real.

### 1.7 `LZRl` — neutral heavy-vector lepton current

$$
\mathcal{L}_{Z_R}^{\ell}
= -\frac{\kappa_R^{l}\,g_w}{n_{Z_R}^{l}}\;
\Bigl[\;
g^{e}_{L}\,\overline{\ell}\,\gamma^\mu P_L\,\ell
+ g^{e}_{R}\,\overline{\ell}\,\gamma^\mu P_R\,\ell
+ g^{\nu}_{L}\,\overline{\nu}\,\gamma^\mu P_L\,\nu
+ g^{N}_{R}\,\overline{N}\,\gamma^\mu P_R\,N
\;\Bigr]\; Z_{R\,\mu}.
$$

Note the asymmetry, which is deliberate: the light neutrino enters with $P_L$ only,
and the heavy neutrino with $P_R$ only.

**Majorana detail.** For the self-conjugate field $N$ the vector bilinear vanishes
identically, $\overline{N}\gamma^\mu N \equiv 0$. Therefore

$$
\overline{N}\gamma^\mu P_R N \;=\; \tfrac{1}{2}\,\overline{N}\gamma^\mu\gamma_5 N ,
$$

so the $Z_R N N$ vertex is purely **axial**, with half the naive strength.

---

## 2. Field table

| `.fr` class | Symbol | Spin | $SU(3)_c$ | $SU(2)_L$ | U(1) charge | Self-conj. | Mass symbol | Mass value (GeV) | Width (GeV) | PDG |
|---|---|---|---|---|---|---|---|---|---|---|
| `V[100]` | $W_R^{+}$ (`WR`) | 1 | **1** (none declared) | **1** (none declared) | $Q=+1$ | No | `MWR` | 3000. | `WWR` $=84.3$ | 9900024 |
| `V[101]` | $Z_R$ (`ZR`) | 1 | **1** (none declared) | **1** (none declared) | $Q=0$ | Yes | `MZR` | 5070. | `WZR` $=114.$ | 9900023 |
| `F[100]` | $N_1$ (`n1`) | 1/2 | **1** (none declared) | **1** (none declared) | $Q=0$ | Yes (Majorana) | `mn1` | 173.3 | `Wn1` $=2.12\times10^{-8}$ | 9900012 |
| `F[100]` | $N_2$ (`n2`) | 1/2 | **1** | **1** | $Q=0$ | Yes (Majorana) | `mn2` | $1.\times10^{12}$ | 0 | 9900014 |
| `F[100]` | $N_3$ (`n3`) | 1/2 | **1** | **1** | $Q=0$ | Yes (Majorana) | `mn3` | $1.\times10^{12}$ | 0 | 9900016 |

Remarks:

- No `Indices -> {Index[Colour]}` and no `Indices -> {Index[SU2W]}` appear, and no new
  gauge group is declared. All three states are singlets under every declared group.
  The only quantum number given is the electric charge of $W_R$.
- `F[100]` is one class with three members and a `Generation` flavour index. The mass
  symbol is `MN`, whose members are `mn1`, `mn2`, `mn3`.
- The generation-2 and generation-3 heavy neutrinos are at $10^{12}$ GeV with zero
  width. They are decoupled in practice; only $N_1$ is light enough to be produced.
- `M$InteractionOrderHierarchy` declares `{QCD,1}, {QED,2}, {NP,1}`, so all new
  vertices count as one power of `NP`.

---

## 3. Parameters

### 3.1 External parameters (block `LRSMINPUTS`)

| Symbol | `.fr` name | Order | Value | What it multiplies | Meaning |
|---|---|---|---|---|---|
| $\kappa_R^{q}$ | `kapRq` | 1 | 1. | `LWRq` and `LZRq` (overall factor) | Ratio of the right-handed gauge coupling to $g_w$ in the **quark** sector, $\kappa_R^q = g_R^q/g_L$. `InteractionOrder -> {NP,1}`. |
| $\kappa_R^{l}$ | `kapRl` | 2 | 1. | `LWRl` and `LZRl` (overall factor) | Same ratio for the **lepton** sector, $\kappa_R^l = g_R^l/g_L$. `InteractionOrder -> {NP,1}`. |

Two independent $\kappa$ values are the defining freedom of this file. A true gauge
model would force $\kappa_R^q=\kappa_R^l$. Here the quark and lepton right-handed
currents can be rescaled apart.

### 3.2 Internal parameters

| Symbol | `.fr` name | Value | Role |
|---|---|---|---|
| $t_W^2$ | `tw2` | $s_W^2/c_W^2=\tan^2\theta_W$ | Weak mixing, squared tangent. |
| $n_{Z_R}^{q}$ | `nZRq` | $\sqrt{1-t_W^2/\kappa_{R,q}^{2}}$ | Normalisation of the $Z_R$ quark coupling. Gives $\kappa_R^q g_w/n_{Z_R}^q = g_R^q/\sqrt{1-t_W^2 g_L^2/g_R^{q\,2}}$, the standard $g_{Z_R}$. |
| $n_{Z_R}^{l}$ | `nZRl` | $\sqrt{1-t_W^2/\kappa_{R,l}^{2}}$ | Same for the lepton sector. |
| $g^{u}_{L}$ | `gLZRu` | $-\tfrac16\,t_W^2/\kappa_{R,q}^{2}$ | $Z_R\bar u_L u_L$ coupling. |
| $g^{u}_{R}$ | `gRZRu` | $\tfrac12-\tfrac23\,t_W^2/\kappa_{R,q}^{2}$ | $Z_R\bar u_R u_R$ coupling. |
| $g^{d}_{L}$ | `gLZRd` | $-\tfrac16\,t_W^2/\kappa_{R,q}^{2}$ | $Z_R\bar d_L d_L$ coupling. |
| $g^{d}_{R}$ | `gRZRd` | $-\tfrac12+\tfrac13\,t_W^2/\kappa_{R,q}^{2}$ | $Z_R\bar d_R d_R$ coupling. |
| $g^{e}_{L}$ | `gLZRe` | $\tfrac12\,t_W^2/\kappa_{R,l}^{2}$ | $Z_R\bar\ell_L\ell_L$ coupling. |
| $g^{e}_{R}$ | `gRZRe` | $-\tfrac12+t_W^2/\kappa_{R,l}^{2}$ | $Z_R\bar\ell_R\ell_R$ coupling. |
| $g^{\nu}_{L}$ | `gLZRv` | $\tfrac12\,t_W^2/\kappa_{R,l}^{2}$ | $Z_R\bar\nu_L\nu_L$ coupling. |
| $g^{N}_{R}$ | `gRZRn` | $\tfrac12$ | $Z_R\bar N N$ axial coupling. Free of $t_W$, because $N$ is electrically neutral. |
| $V^{R}_{\rm CKM}$ | `VCKMR` | identity $3\times3$, `Unitary -> True` | Right-handed quark mixing matrix in `LWRq`. |
| $Y_N$ | `YN` | identity $3\times3$ | Mixing of heavy $N$ with charged leptons in the $W_R$ current. |
| $X_N$ | `XN` | zero $3\times3$ | Mixing of light $\nu$ with charged leptons in the $W_R$ current. Zero by default, so the light-neutrino $W_R$ vertex is switched off. |

**Coupling pattern.** Every $Z_R$ coupling above follows one formula:

$$
g_\psi \;=\; T^{3}_{R}(\psi)\;-\;\Bigl[\,T^{3}_{R}(\psi)+\tfrac{B-L}{2}(\psi)\,\Bigr]\frac{t_W^{2}}{\kappa_R^{2}} .
$$

For left-handed fields $T^3_R=0$, so $g=-\tfrac{B-L}{2}t_W^2/\kappa_R^2$, which
reproduces $-\tfrac16 t_W^2$ for quarks and $+\tfrac12 t_W^2$ for leptons.
For right-handed fields it reduces to $T^3_R-Q\,t_W^2/\kappa_R^2$. This is the
canonical $SU(2)_R\times U(1)_{B-L}$ pattern, with $\kappa_R$ inserted by hand.

---

## 4. Physics summary

This is an effective right-handed extension of the Standard Model. It adds a charged
vector $W_R^\pm$ at 3 TeV, a neutral vector $Z_R$ at 5.07 TeV, and three Majorana
neutrinos $N_{1,2,3}$, with $N_1$ at 173.3 GeV and the other two decoupled at
$10^{12}$ GeV. $W_R$ couples only to right-handed quark and lepton currents through a
separate right-handed mixing matrix $V^R_{\rm CKM}$ and a lepton mixing matrix $Y_N$.
$Z_R$ couples to both chiralities with the $SU(2)_R\times U(1)_{B-L}$ charge pattern,
and to $N$ purely axially. The right-handed coupling strength is set by two free
ratios, $\kappa_R^q$ and $\kappa_R^l$, so the quark and lepton sectors can be scaled
apart; this breaks the single-gauge-coupling relation and marks the model as
effective, not as a complete gauge theory.

The model mediates resonant $W_R$ production with the decay
$pp\to W_R\to \ell^\pm N$, followed by $N\to \ell^\pm jj$ through an off-shell $W_R$.
Because $N$ is Majorana, the two leptons can carry the same sign, so the signature is
a same-sign dilepton pair plus jets with no missing energy, and lepton number changes
by two units. It also gives a narrow dilepton and dijet resonance from
$pp\to Z_R\to \ell^+\ell^-,\,q\bar q$, plus $Z_R\to NN$ pair production of the heavy
neutrinos. Because the new vectors carry no self-interactions, there are no
$W_RW_RZ_R$ or $W_RW_R\gamma$ vertices, and diboson channels are absent.
