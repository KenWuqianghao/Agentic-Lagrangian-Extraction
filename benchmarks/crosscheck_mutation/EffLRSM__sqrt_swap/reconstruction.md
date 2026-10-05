# Reconstruction of `sanitized.fr`

Conventions used below:

- `ProjP` = $P_R=\tfrac{1+\gamma_5}{2}$, `ProjM` = $P_L=\tfrac{1-\gamma_5}{2}$, `Ga[mu]` = $\gamma^\mu$.
- `HC[X]` = $X^\dagger$ (hermitian conjugate), `CC[X]` = charge conjugate.
- $i,j,f$ are generation indices. Repeated indices are summed.
- Metric signature and all Standard Model (SM) fields come from `LSM`, which this file adds to.
- `gw` is the SM $SU(2)_L$ gauge coupling $g$; `sw`, `cw` are $\sin\theta_W$, $\cos\theta_W$.

## 1. Lagrangian

The total Lagrangian is

$$\mathcal{L}_{\rm Total}=\mathcal{L}_{\rm SM}+\mathcal{L}_{W_R}^{\rm kin}+\mathcal{L}_{Z_R}^{\rm kin}+\mathcal{L}_{N}^{\rm kin}+\mathcal{L}_{W_Rq}+\mathcal{L}_{W_R\ell}+\mathcal{L}_{Z_Rq}+\mathcal{L}_{Z_R\ell}\qquad(\texttt{LTotal})$$

### Gauge content of the covariant derivative

The file uses **no** `DC`. The only derivative that acts on a new field is the plain
partial derivative `del` in `LNkin`. The two new vectors enter through `FS`, which for a
field that is not a declared gauge boson is the abelian curl:

$$W_{R\,\mu\nu}=\partial_\mu W_{R\,\nu}-\partial_\nu W_{R\,\mu},\qquad
Z_{R\,\mu\nu}=\partial_\mu Z_{R\,\nu}-\partial_\nu Z_{R\,\mu}.$$

So $W_R$ and $Z_R$ are **Proca fields, not gauge fields**: the file declares no $SU(2)_R$
gauge group, no $W_R$/$Z_R$ self-couplings, and no $\gamma W_R^+W_R^-$ vertex, although
$W_R$ carries $Q=+1$. $N_R$ is a gauge singlet and its derivative is $\partial_\mu$.
The only covariant derivative in the model is the SM one inherited from `LSM`,
$D_\mu=\partial_\mu-i g_s T^a G^a_\mu-i g T^k W^k_\mu-i g' Y B_\mu$ for
$SU(3)_C\times SU(2)_L\times U(1)_Y$. All new interactions are written out by hand as
current $\times$ field terms.

### `LWRkin` — charged heavy vector, kinetic and mass

$$\mathcal{L}_{W_R}^{\rm kin}=-\frac{1}{2}\,W_R^{\dagger\,\mu\nu}W_{R\,\mu\nu}
+M_{W_R}^{2}\,W_R^{\dagger\,\mu}W_{R\,\mu}$$

### `LZRkin` — neutral heavy vector, kinetic and mass

$$\mathcal{L}_{Z_R}^{\rm kin}=-\frac{1}{4}\,Z_R^{\mu\nu}Z_{R\,\mu\nu}
+\frac{1}{2}M_{Z_R}^{2}\,Z_R^{\mu}Z_{R\,\mu}$$

### `LNkin` — Majorana neutrino, kinetic and mass

$N_R$ is self-conjugate, so both terms carry the Majorana factor $\tfrac12$:

$$\mathcal{L}_{N}^{\rm kin}=\frac{i}{2}\,\overline{N_R^{\,f}}\,\gamma^\mu\partial_\mu N_R^{\,f}
-\frac{1}{2}\,M_N^{f}\,\overline{N_R^{\,f}}\,N_R^{\,f}$$

with $M_N^f$ the diagonal mass of generation $f$ ($f=1,2,3$; no sum matrix is applied,
the mass is flavour diagonal by declaration).

### `LWRq` — right-handed quark charged current

$$\mathcal{L}_{W_Rq}=
-\frac{\kappa_R^{q}\,g}{\sqrt{2}}\;
\bar{u}_i\,(V^R_{\rm CKM})_{ij}\,\gamma^\mu P_R\, d_j\; W_{R\,\mu}
\;+\;\text{h.c.}$$

The hermitian conjugate reads
$-\dfrac{\kappa_R^{q} g}{\sqrt{2}}\,\bar{d}_j (V^{R\,\dagger}_{\rm CKM})_{ji}\gamma^\mu P_R\,u_i\,W_{R\,\mu}^{\dagger}$.
The current is purely right-handed; $V^R_{\rm CKM}$ is a separate unitary matrix from the
SM CKM matrix and is the identity at the default values.

### `LWRl` — right-handed lepton charged current

$$\mathcal{L}_{W_R\ell}=
-\frac{\kappa_R^{\ell}\,g}{\sqrt{2}}\Big[
\overline{N_R^{\,i}}\,(Y_N)_{ij}\,\gamma^\mu P_R\,\ell_j
\;+\;\overline{\nu^{c}_{i}}\,(X_N)_{ij}\,\gamma^\mu P_R\,\ell_j
\Big]W_{R\,\mu}\;+\;\text{h.c.}$$

Here $\ell=(e,\mu,\tau)$ is the SM charged-lepton Dirac field, $\nu$ the SM light
neutrino field, and `CC[vlbar]` $=\overline{\nu^{c}}=\nu^{T}C$ is the charge-conjugated
bar-field. Both currents are right-handed. $Y_N$ controls $W_R\to \ell N$ and is the
identity by default; $X_N$ controls $W_R\to \ell\nu$ (a heavy–light mixing insertion) and
is zero by default, so that vertex is switched off unless the user changes it.

### `LZRq` — heavy neutral current, quarks

$$\mathcal{L}_{Z_Rq}=
-\frac{\kappa_R^{q}\,g}{n_{Z_R}^{q}}\Big[
g_L^{u}\,\bar{u}\gamma^\mu P_L u
+g_R^{u}\,\bar{u}\gamma^\mu P_R u
+g_L^{d}\,\bar{d}\gamma^\mu P_L d
+g_R^{d}\,\bar{d}\gamma^\mu P_R d\Big]Z_{R\,\mu}$$

Flavour diagonal, summed over the three generations.

### `LZRl` — heavy neutral current, leptons

$$\mathcal{L}_{Z_R\ell}=
-\frac{\kappa_R^{\ell}\,g}{n_{Z_R}^{\ell}}\Big[
g_L^{e}\,\bar{\ell}\gamma^\mu P_L \ell
+g_R^{e}\,\bar{\ell}\gamma^\mu P_R \ell
+g_L^{\nu}\,\bar{\nu}\gamma^\mu P_L \nu
+g_R^{N}\,\overline{N_R}\gamma^\mu P_R N_R\Big]Z_{R\,\mu}$$

The light neutrino has a left-handed coupling only; $N_R$ has a right-handed coupling
only. Because $N_R$ is Majorana its vector current vanishes identically, so the last term
is purely axial:
$\overline{N_R}\gamma^\mu P_R N_R=\tfrac12\overline{N_R}\gamma^\mu\gamma_5 N_R$.

### Structure of the neutral-current charges

All eight $Z_R$ charges follow one formula, with $t_W^2=\tan^2\theta_W$:

$$g^{f}=T^{f}_{3R}-\frac{t_W^{2}}{\kappa_R^{2}}\big(Q^{f}-T^{f}_{3L}\big)
=T^{f}_{3R}-\frac{t_W^{2}}{\kappa_R^{2}}\Big(T^{f}_{3R}+\tfrac{B-L}{2}\Big)$$

with $\kappa_R=\kappa_R^{q}$ for quarks and $\kappa_R^{\ell}$ for leptons. This is a
$T_{3R}$ current with a $(B-L)$ admixture set by $\tan^2\theta_W/\kappa_R^2$.

## 2. Field table

| Symbol | Class | Spin | $SU(3)_C$ | $SU(2)$ | $U(1)$ charge | Self-conj. | Mass symbol | Mass value (GeV) | Width (GeV) | PDG |
|---|---|---|---|---|---|---|---|---|---|---|
| $W_R^{\pm}$ (`WR`) | `V[100]` | 1 | singlet (no colour index) | none declared | $Q=+1$ | No | `MWR` | 3000. | `WWR` = 84.3 | 9900024 |
| $Z_R$ (`ZR`) | `V[101]` | 1 | singlet | none declared | $Q=0$ | Yes | `MZR` | 5070. | `WZR` = 114. | 9900023 |
| $N_1$ (`n1`) | `F[100]`, gen. 1 | 1/2 | singlet | none declared | $Q=0$ | Yes (Majorana) | `mn1` | 173.3 | `Wn1` = $2.12\times10^{-8}$ | 9900012 |
| $N_2$ (`n2`) | `F[100]`, gen. 2 | 1/2 | singlet | none declared | $Q=0$ | Yes (Majorana) | `mn2` | $1\times10^{12}$ | `Wn2` = 0 | 9900014 |
| $N_3$ (`n3`) | `F[100]`, gen. 3 | 1/2 | singlet | none declared | $Q=0$ | Yes (Majorana) | `mn3` | $1\times10^{12}$ | `Wn3` = 0 | 9900016 |

Notes:

- No class declares a `Colour` or an $SU(2)$ index, so every new state is a colour and
  weak-isospin singlet in the implementation. The right-handed isospin quantum number
  appears only through the numerical values of the $Z_R$ charges.
- `NR` carries `Indices -> {Index[Generation]}` with `FlavorIndex -> Generation`, and the
  three members share the common mass symbol `MN[f]`.
- $N_2$ and $N_3$ sit at $10^{12}$ GeV, so only $N_1$ (173.3 GeV) is kinematically
  relevant at collider energies.
- Propagator types: `Sine` for both vectors, `Straight` with no arrow for the Majorana
  fermions.

## 3. Parameters

### External parameters

| Symbol | Block / order | Value | Multiplies | Meaning |
|---|---|---|---|---|
| $\kappa_R^{q}$ (`kapRq`) | `LRSMINPUTS`, 1 | 1. | Overall factor of `LWRq` and `LZRq`; also enters $n_{Z_R}^{q}$, `gLZRu`, `gRZRu`, `gLZRd`, `gRZRd` as $t_W^2/\kappa_R^{q\,2}$ | Ratio of the right-handed to the left-handed gauge coupling in the **quark** sector, $\kappa_R^q=g_R^{q}/g$. `InteractionOrder -> {NP,1}`, so every quark vertex it multiplies counts as one new-physics order. |
| $\kappa_R^{\ell}$ (`kapRl`) | `LRSMINPUTS`, 2 | 1. | Overall factor of `LWRl` and `LZRl`; also enters $n_{Z_R}^{\ell}$, `gLZRe`, `gRZRe`, `gLZRv` as $t_W^2/\kappa_R^{\ell\,2}$ | Same ratio for the **lepton** sector, $\kappa_R^\ell=g_R^{\ell}/g$. `InteractionOrder -> {NP,1}`. |

Masses and widths (`MWR`, `WWR`, `MZR`, `WZR`, `MN`/`mn1..3`, `WN`/`Wn1..3`) are declared
inside the particle classes and are external inputs as well.

### Internal (derived) parameters

| Symbol | Value in the file | Role |
|---|---|---|
| `tw2` | $s_W^2/c_W^2=\tan^2\theta_W$ | Weak mixing, shorthand. |
| `nZRq` | $1/\sqrt{1-t_W^2/\kappa_R^{q\,2}}$ | Divides the $Z_R$ quark coupling: prefactor $=\kappa_R^q g/n_{Z_R}^q=\kappa_R^q g\sqrt{1-t_W^2/\kappa_R^{q\,2}}$. |
| `nZRl` | $\sqrt{1-t_W^2/\kappa_R^{\ell\,2}}$ | Divides the $Z_R$ lepton coupling: prefactor $=\kappa_R^\ell g/\sqrt{1-t_W^2/\kappa_R^{\ell\,2}}$. |
| `gLZRu` | $-\tfrac16\,t_W^2/\kappa_R^{q\,2}$ | $u_L$ charge; $= -t_W^2/\kappa_R^2\cdot\tfrac{B-L}{2}$ with $B-L=\tfrac13$. |
| `gRZRu` | $\tfrac12-\tfrac23\,t_W^2/\kappa_R^{q\,2}$ | $u_R$ charge; $T_{3R}=+\tfrac12$, $Q=+\tfrac23$. |
| `gLZRd` | $-\tfrac16\,t_W^2/\kappa_R^{q\,2}$ | $d_L$ charge (same as $u_L$, as $(B-L)$ is shared). |
| `gRZRd` | $-\tfrac12+\tfrac13\,t_W^2/\kappa_R^{q\,2}$ | $d_R$ charge; $T_{3R}=-\tfrac12$, $Q=-\tfrac13$. |
| `gLZRe` | $\tfrac12\,t_W^2/\kappa_R^{\ell\,2}$ | $e_L$ charge; $B-L=-1$. |
| `gRZRe` | $-\tfrac12+t_W^2/\kappa_R^{\ell\,2}$ | $e_R$ charge; $T_{3R}=-\tfrac12$, $Q=-1$. |
| `gLZRv` | $\tfrac12\,t_W^2/\kappa_R^{\ell\,2}$ | $\nu_L$ charge; equal to $g_L^{e}$. |
| `gRZRn` | $\tfrac12$ | $N_R$ charge; $T_{3R}=+\tfrac12$, $Q=0$, so no $t_W^2$ piece. |
| `VCKMR` | unitary $3\times3$, identity by default | Right-handed quark mixing matrix in `LWRq`. |
| `YN` | $3\times3$, identity by default | Heavy-neutrino/charged-lepton mixing in the $W_R$ current. |
| `XN` | $3\times3$, zero by default | Light-neutrino/charged-lepton mixing in the $W_R$ current; off by default. |

### Interaction-order hierarchy

`{QCD,1}, {QED,2}, {NP,1}` — new-physics vertices are counted at the same weight as QCD
and below QED in the hierarchy used for diagram selection.

## 4. Consistency note on the $Z_R$ normalisation

The two normalisation factors are not the same function:

- lepton sector: $\kappa_R^\ell g/n_{Z_R}^{\ell}=\dfrac{\kappa_R^\ell g}{\sqrt{1-t_W^2/\kappa_R^{\ell\,2}}}$
- quark sector: $\kappa_R^q g/n_{Z_R}^{q}=\kappa_R^q g\,\sqrt{1-t_W^2/\kappa_R^{q\,2}}$

`nZRq` is the **reciprocal** of the form used for `nZRl`. Since the charges `gLZR*`,
`gRZR*` follow one common formula for both sectors, the natural reading is that both
prefactors should have the same functional form, and the square root is inverted in the
quark line. At the default $\kappa_R^q=\kappa_R^\ell=1$ and $s_W^2\simeq0.2312$ the two
prefactors differ by a factor $1/(1-t_W^2)\simeq1.43$, so quark-side $Z_R$ couplings are
suppressed by about $1.2$ relative to the lepton side instead of matching them. This
looks like a defect in the file rather than deliberate sector-dependent physics. The
reconstruction above records the file as written.

## 5. Physics summary

This is an effective right-handed-current extension of the SM. It adds a charged spin-1
$W_R^\pm$ (3 TeV), a neutral spin-1 $Z_R$ (5.07 TeV) and three Majorana gauge-singlet
neutrinos $N_{1,2,3}$, with only $N_1$ (173.3 GeV) light enough to matter. The new vectors
are Proca fields with hand-written currents rather than gauge fields of a realised
$SU(2)_R$, so there are no heavy-boson self-interactions and no scalar sector; the whole
new-physics strength is set by two coupling ratios $\kappa_R^{q}$ and $\kappa_R^{\ell}$,
a right-handed quark mixing matrix $V^R_{\rm CKM}$, and the lepton mixings $Y_N$ (heavy)
and $X_N$ (light, zero by default).

The $W_R$ mediates purely right-handed charged currents: $q\bar q'\to W_R\to \ell N$ and
$W_R\to \bar u d$. Because $N$ is Majorana, the chain $pp\to W_R\to \ell N$, $N\to \ell
W_R^{(*)}\to \ell q\bar q'$ gives the same-sign dilepton plus jets signature and, at low
energy, neutrinoless double beta decay. The $Z_R$ mediates a $T_{3R}$-plus-$(B-L)$ neutral
current, so it shows up as a high-mass dilepton or dijet resonance and can also decay to
$N\bar N$ pairs through its axial Majorana coupling.
