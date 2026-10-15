# Reconstruction of `sanitized.fr`

## 0. Conventions used below

The file adds new states on top of an existing Standard Model (SM) implementation.
The last line is `LTotal := LSM + ...`, so `LSM` and the SM field names
(`uq`, `dq`, `l`, `vl`) come from the FeynRules SM model file.

FeynRules idioms are expanded as follows.

| `.fr` idiom | Standard notation |
| --- | --- |
| `Ga[mu]` | $\gamma^{\mu}$ |
| `ProjP` | $P_R=\tfrac{1}{2}(1+\gamma^5)$ |
| `ProjM` | $P_L=\tfrac{1}{2}(1-\gamma^5)$ |
| `del[X, mu]` | $\partial_{\mu}X$ |
| `FS[V, mu, nu]` | $V_{\mu\nu}=\partial_{\mu}V_{\nu}-\partial_{\nu}V_{\mu}$ (abelian; `WR` and `ZR` are **not** gauge fields of a declared group) |
| `Xbar` | $\bar X = X^{\dagger}\gamma^0$ (for a vector field, $V^{\dagger}$) |
| `CC[vlbar]` | $\overline{\nu^{c}}$, with $\nu^{c}=C\bar\nu^{T}$ |
| `HC[t]` | $t^{\dagger}$ |
| `A.B.C` | Dirac-index and flavour-index chain contraction |
| `ExpandIndices` | writes out the implicit Dirac, flavour and colour indices |

**Covariant derivative content.** The file never calls `DC`. Every new kinetic
term uses the plain derivative $\partial_\mu$ and the abelian field strength
$\partial_\mu V_\nu-\partial_\nu V_\mu$. No gauge group is declared in this file.
Therefore:

- $W_R$ and $Z_R$ are **Proca fields** with hand-inserted mass terms. They have
  no coupling to the photon, no gluon coupling, and no triple or quartic gauge
  self-coupling. $W_R$ carries electric charge but has **no** $\gamma W_R W_R$ or
  $Z W_R W_R$ vertex, because `FS` is abelian here.
- $N_R$ is a gauge-singlet Majorana fermion with $\partial_\mu$ only.
- The only covariant derivative in the full model is the SM one inside `LSM`:
  $D_\mu = \partial_\mu - i g_s T^a G^a_\mu - i g_w T^i W^i_\mu - i g_1 \tfrac{Y}{2} B_\mu$
  for $SU(3)_c \times SU(2)_L \times U(1)_Y$.

Repeated generation indices $i,j = 1,2,3$ are summed. $g_w$ is the SM
$SU(2)_L$ coupling.

---

## 1. Lagrangian, term by term

### 1.1 `LWRkin` — charged heavy vector kinetic and mass term

$$
\mathcal{L}_{W_R\,\mathrm{kin}}
= -\frac{1}{2}\, W_R^{\dagger\,\mu\nu}\, W_{R\,\mu\nu}
\; + \; M_{W_R}^{2}\, W_R^{\dagger\,\mu}\, W_{R\,\mu},
\qquad
W_{R\,\mu\nu}=\partial_{\mu}W_{R\,\nu}-\partial_{\nu}W_{R\,\mu}.
$$

This is the standard Proca Lagrangian for a **complex** vector field. The
factors $-\tfrac12$ and $+M^2$ (not $-\tfrac14$ and $+\tfrac12 M^2$) are the
correct normalisation for a non-self-conjugate vector.

### 1.2 `LZRkin` — neutral heavy vector kinetic and mass term

$$
\mathcal{L}_{Z_R\,\mathrm{kin}}
= -\frac{1}{4}\, Z_R^{\mu\nu} Z_{R\,\mu\nu}
\; + \; \frac{1}{2}\, M_{Z_R}^{2}\, Z_R^{\mu} Z_{R\,\mu},
\qquad
Z_{R\,\mu\nu}=\partial_{\mu}Z_{R\,\nu}-\partial_{\nu}Z_{R\,\mu}.
$$

The $-\tfrac14$, $+\tfrac12 M^2$ normalisation is the real (self-conjugate)
vector case.

### 1.3 `LNkin` — heavy Majorana neutrino kinetic and mass term

$$
\mathcal{L}_{N\,\mathrm{kin}}
= \frac{i}{2}\, \overline{N_i}\, \gamma^{\mu}\, \partial_{\mu} N_i
\; - \; \frac{1}{2}\, M_{N_i}\, \overline{N_i}\, N_i .
$$

Both $\tfrac12$ factors are the Majorana normalisation, which follows from
`SelfConjugate -> True`. The mass matrix is diagonal in the flavour basis:
$M_{N_i} = \mathrm{diag}(m_{n_1}, m_{n_2}, m_{n_3})$. The sum runs over the
generation index `ff`.

### 1.4 `LWRq` — right-handed charged quark current

$$
\mathcal{L}_{W_R q}
= -\frac{\kappa_R^{q}\, g_w}{\sqrt{2}}\;
\overline{u_i}\, \bigl(V^{\mathrm{CKM}}_R\bigr)_{ij}\, \gamma^{\mu} P_R\, d_j\;
W_{R\,\mu}
\;+\; \mathrm{h.c.}
$$

with the hermitian conjugate written out:

$$
\mathrm{h.c.} =
-\frac{\kappa_R^{q}\, g_w}{\sqrt{2}}\;
\overline{d_j}\, \bigl(V^{\mathrm{CKM}\,\dagger}_R\bigr)_{ji}\,
\gamma^{\mu} P_R\, u_i\; W_{R\,\mu}^{\dagger}.
$$

The current is **purely right-handed** (`ProjP`). The mixing matrix
$V_R^{\mathrm{CKM}}$ is the right-handed analogue of the CKM matrix and is
contracted as $\bar u_i (V_R)_{ij} d_j$. Colour indices are contracted
diagonally ($\bar u^a \dots d^a$).

### 1.5 `LWRl` — right-handed charged lepton current

$$
\mathcal{L}_{W_R \ell}
= -\frac{\kappa_R^{l}\, g_w}{\sqrt{2}}
\Bigl[\;
\overline{N_i}\,(Y_N)_{ij}\,\gamma^{\mu} P_R\, \ell_j
\;+\;
\overline{\nu^{c}_{i}}\,(X_N)_{ij}\,\gamma^{\mu} P_R\, \ell_j
\;\Bigr] W_{R\,\mu}
\;+\; \mathrm{h.c.}
$$

with

$$
\mathrm{h.c.} =
-\frac{\kappa_R^{l}\, g_w}{\sqrt{2}}
\Bigl[\;
\overline{\ell_j}\,(Y_N^{\dagger})_{ji}\,\gamma^{\mu} P_R\, N_i
\;+\;
\overline{\ell_j}\,(X_N^{\dagger})_{ji}\,\gamma^{\mu} P_R\, \nu^{c}_{i}
\;\Bigr] W_{R\,\mu}^{\dagger}.
$$

Notes on chirality and conjugation:

- $\ell$ is the SM charged-lepton field; only its right-handed part enters.
- $N$ is Majorana, so $\overline{N}\gamma^{\mu}P_R\,\ell$ and its conjugate both
  exist with the same $N$ state. This is the source of lepton-number violation.
- $\nu^{c} = C\bar\nu^{T}$. Because $\nu$ is the left-handed SM neutrino,
  $\nu^{c}$ is right-handed, so $\overline{\nu^{c}}\gamma^\mu P_R \ell$ is a
  well-formed right-handed current. This term is the light-neutrino part of the
  $W_R$ charged current, switched on by the heavy-light mixing matrix $X_N$.

### 1.6 `LZRq` — $Z_R$ quark neutral current

$$
\mathcal{L}_{Z_R q}
= -\frac{\kappa_R^{q}\, g_w}{n_{Z_R}^{q}}
\Bigl[\;
g_L^{Z_R u}\,\overline{u}\gamma^{\mu}P_L u
+ g_R^{Z_R u}\,\overline{u}\gamma^{\mu}P_R u
+ g_L^{Z_R d}\,\overline{d}\gamma^{\mu}P_L d
+ g_R^{Z_R d}\,\overline{d}\gamma^{\mu}P_R d
\;\Bigr] Z_{R\,\mu}.
$$

The current is flavour-diagonal (no mixing matrix), summed over generations and
colour.

### 1.7 `LZRl` — $Z_R$ lepton neutral current

$$
\mathcal{L}_{Z_R \ell}
= -\frac{\kappa_R^{l}\, g_w}{n_{Z_R}^{l}}
\Bigl[\;
g_L^{Z_R e}\,\overline{\ell}\gamma^{\mu}P_L \ell
+ g_R^{Z_R e}\,\overline{\ell}\gamma^{\mu}P_R \ell
+ g_L^{Z_R \nu}\,\overline{\nu}\gamma^{\mu}P_L \nu
+ g_R^{Z_R n}\,\overline{N}\gamma^{\mu}P_R N
\;\Bigr] Z_{R\,\mu}.
$$

The light neutrino gets a left-handed coupling only, and $N$ gets a
right-handed coupling only. For a Majorana $N$ the vector current vanishes, so
$\overline{N}\gamma^{\mu}P_R N = \tfrac12\overline{N}\gamma^{\mu}\gamma^{5}N$
is an axial current.

### 1.8 `LTotal`

$$
\mathcal{L}_{\mathrm{total}} = \mathcal{L}_{\mathrm{SM}}
+ \mathcal{L}_{W_R\,\mathrm{kin}} + \mathcal{L}_{Z_R\,\mathrm{kin}}
+ \mathcal{L}_{N\,\mathrm{kin}}
+ \mathcal{L}_{W_R q} + \mathcal{L}_{W_R \ell}
+ \mathcal{L}_{Z_R q} + \mathcal{L}_{Z_R \ell}.
$$

---

## 2. Field table

| Class | Symbol | Spin | $SU(3)_c$ | $SU(2)$ | $U(1)$ charge $Q$ | Self-conj. | Mass symbol | Mass value (GeV) | Width (GeV) | PDG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `V[100]` | $W_R$ | 1 | singlet (no colour index) | not declared | $-1$ **as declared** (see note) | No | `MWR` | 3000 | `WWR` = 84.3 | 9900024 |
| `V[101]` | $Z_R$ | 1 | singlet | not declared | 0 (no `QuantumNumbers`) | Yes (real) | `MZR` | 5070 | `WZR` = 114 | 9900023 |
| `F[100]` | $N_i$, members $n_1,n_2,n_3$ | 1/2 | singlet | not declared | 0 (no `QuantumNumbers`) | Yes (Majorana) | `MN` | $m_{n_1}=173.3$, $m_{n_2}=m_{n_3}=10^{12}$ | $W_{n_1}=2.12\times10^{-8}$, $W_{n_2}=W_{n_3}=0$ | 9900012 / 9900014 / 9900016 |

Notes.

- No gauge group block is declared in this file, so no field carries an
  $SU(2)$ or colour index. All three new states are colour singlets.
- $N$ carries a `Generation` flavour index and is the flavour index of the
  `NR` class.
- $M_{Z_R}/M_{W_R} = 1.69$, which is the left-right relation
  $M_{Z_R}\simeq 1.7\,M_{W_R}$ for $g_R=g_L$.
- $n_2$ and $n_3$ sit at $10^{12}$ GeV with zero width, so only $n_1$ is
  kinematically active.

### Charge inconsistency in the `WR` declaration

`WR` is declared with `QuantumNumbers -> {Q -> -1}`, `ParticleName -> "wr+"`,
`AntiParticleName -> "wr-"`. This value does **not** agree with the
Lagrangian. Every $W_R$ interaction term multiplies the field `WR[mu]`
(not `WRbar[mu]`) by a current of charge $-1$:

- $\overline{u}\,\gamma^\mu P_R\, d$: $-\tfrac23 - \tfrac13 = -1$
- $\overline{N}\,\gamma^\mu P_R\, \ell$: $0 - 1 = -1$
- $\overline{\nu^c}\,\gamma^\mu P_R\, \ell$: $0 - 1 = -1$

Charge conservation therefore requires $Q(W_R) = +1$. The particle label
`"wr+"` also implies $+1$. The declared $Q=-1$ is the odd one out, and it
would break the quantum-number check on the $W_R$ vertices. Read the field as
the positively charged $W_R^{+}$; the declared value $-1$ appears to be a sign
error.

---

## 3. Parameters

### 3.1 External parameters

Both live in the Les Houches block `LRSMINPUTS` and both carry
`InteractionOrder -> {NP, 1}`.

| Symbol | `.fr` name | Block / order | Default | Multiplies | Physical meaning |
| --- | --- | --- | --- | --- | --- |
| $\kappa_R^{q}$ | `kapRq` | LRSMINPUTS, 1 | 1.0 | the whole $W_R$ quark current and the whole $Z_R$ quark current | Ratio of the right-handed gauge coupling to the SM $SU(2)_L$ coupling, in the **quark** sector: $\kappa_R^q = g_R^q/g_w$. |
| $\kappa_R^{l}$ | `kapRl` | LRSMINPUTS, 2 | 1.0 | the whole $W_R$ lepton current and the whole $Z_R$ lepton current | Same ratio in the **lepton** sector: $\kappa_R^l = g_R^l/g_w$. |

Two separate $\kappa$ values is what makes the model "effective": the quark and
lepton right-handed couplings are free and are not tied together by one gauge
group.

### 3.2 Internal parameters

| Symbol | `.fr` name | Value | Meaning |
| --- | --- | --- | --- |
| $t_W^2$ | `tw2` | $s_W^2/c_W^2 = \tan^2\theta_W$ | Square of the tangent of the weak mixing angle. |
| $n_{Z_R}^{q}$ | `nZRq` | $\sqrt{1-t_W^2/(\kappa_R^q)^2}$ | Normalisation of the $Z_R$ quark coupling. The effective coupling is $g_R^q/n_{Z_R}^q$, the usual left-right factor $g_R/\sqrt{1-g_L^2 t_W^2/g_R^2}$. Real only for $\kappa_R^q > t_W$. |
| $n_{Z_R}^{l}$ | `nZRl` | $\sqrt{1-t_W^2/(\kappa_R^l)^2}$ | Same for the lepton sector. |
| $g_L^{Z_R u}$ | `gLZRu` | $-\tfrac16\,t_W^2/(\kappa_R^q)^2$ | $Z_R$ chiral coupling, left-handed up quark. |
| $g_R^{Z_R u}$ | `gRZRu` | $\tfrac12-\tfrac23\,t_W^2/(\kappa_R^q)^2$ | $Z_R$ chiral coupling, right-handed up quark. |
| $g_L^{Z_R d}$ | `gLZRd` | $-\tfrac16\,t_W^2/(\kappa_R^q)^2$ | $Z_R$ chiral coupling, left-handed down quark. |
| $g_R^{Z_R d}$ | `gRZRd` | $-\tfrac12+\tfrac13\,t_W^2/(\kappa_R^q)^2$ | $Z_R$ chiral coupling, right-handed down quark. |
| $g_L^{Z_R e}$ | `gLZRe` | $+\tfrac12\,t_W^2/(\kappa_R^l)^2$ | $Z_R$ chiral coupling, left-handed charged lepton. |
| $g_R^{Z_R e}$ | `gRZRe` | $-\tfrac12+t_W^2/(\kappa_R^l)^2$ | $Z_R$ chiral coupling, right-handed charged lepton. |
| $g_L^{Z_R \nu}$ | `gLZRv` | $+\tfrac12\,t_W^2/(\kappa_R^l)^2$ | $Z_R$ chiral coupling, left-handed light neutrino. |
| $g_R^{Z_R n}$ | `gRZRn` | $\tfrac12$ | $Z_R$ chiral coupling, right-handed heavy neutrino. Pure $T_{3R}$, because $N$ has zero hypercharge. |
| $V_R^{\mathrm{CKM}}$ | `VCKMR` | $3\times3$, unitary, identity by default | Right-handed quark mixing matrix in the $W_R$ charged current. |
| $Y_N$ | `YN` | $3\times3$, identity by default | Mixing matrix between $N_i$ and $\ell_j$ in the $W_R$ charged current. |
| $X_N$ | `XN` | $3\times3$, **zero** by default | Mixing matrix between the conjugate light neutrino $\nu^c_i$ and $\ell_j$ in the $W_R$ charged current. It is the light-heavy mixing switch. Zero by default means $W_R$ talks only to $N$. |

**Structure of the chiral $Z_R$ couplings.** All eight numbers follow one rule:

$$
g^{f} \;=\; T_{3R}^{f} \;-\; \frac{Y_f}{2}\,\frac{\tan^{2}\theta_W}{\kappa_R^{2}},
\qquad \frac{Y_f}{2} = T_{3R}^{f} + \frac{(B-L)_f}{2}.
$$

Check: $u_L$ has $Y/2=\tfrac16$, $T_{3R}=0 \Rightarrow -\tfrac16 t_W^2/\kappa^2$;
$u_R$ has $Y/2=\tfrac23$, $T_{3R}=\tfrac12 \Rightarrow \tfrac12-\tfrac23 t_W^2/\kappa^2$;
$e_R$ has $Y/2=-1$, $T_{3R}=-\tfrac12 \Rightarrow -\tfrac12+t_W^2/\kappa^2$;
$N_R$ has $Y/2=0$, $T_{3R}=\tfrac12 \Rightarrow \tfrac12$. All match the file.

### 3.3 Interaction order

`M$InteractionOrderHierarchy` sets `{QCD,1}, {QED,2}, {NP,1}`. Only
`kapRq` and `kapRl` carry `NP`, so every new vertex is order `NP=1`.

---

## 4. Physics summary

This is an **effective left-right symmetric model**. It adds three new states
to the SM: a heavy charged vector $W_R$ (3 TeV), a heavy neutral vector $Z_R$
(5.07 TeV), and three heavy Majorana neutrinos $N_{1,2,3}$, of which only
$N_1$ (173.3 GeV) is light enough to matter. The new gauge bosons couple only
through right-handed currents to quarks and leptons, with strengths set by two
free ratios $\kappa_R^q$ and $\kappa_R^l$; the $Z_R$ chiral couplings follow the
left-right pattern $T_{3R} - (Y/2)\tan^2\theta_W/\kappa_R^2$. The model is
"effective" because no $SU(2)_R$ gauge group, no scalar sector, and no
$W$–$W_R$ or $Z$–$Z_R$ mixing are included: the heavy bosons are Proca fields
with masses and widths put in by hand, and $W_R$ has no photon or self-gauge
coupling.

It would mediate, at a hadron collider: $pp \to W_R^{\pm} \to \ell^{\pm} N$
with $N \to \ell^{\pm} jj$, which is the Keung-Senjanović signature of
same-sign dileptons plus jets and violates lepton number by two units, because
$N$ is Majorana; $pp \to W_R \to jj$ dijet resonances; and
$pp \to Z_R \to \ell^+\ell^-$, $jj$, $\nu\bar\nu$ or $NN$. With $X_N \neq 0$ the
$W_R$ also couples to the light neutrinos, which opens $W_R \to \ell \nu$ and
contributes to neutrinoless double beta decay.
