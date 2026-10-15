# Reconstruction of `sanitized.fr`

The file adds two heavy spin-1 states ($W_R^\pm$, $Z_R$) and three heavy Majorana
neutrinos to the Standard Model, and couples them through **purely right-handed**
currents. The new vectors carry no covariant derivative: their kinetic terms are
built from the *abelian* field strength `FS[...]` and their masses are put in by
hand (Proca form). The model is therefore an **effective**, mass-eigenstate
description of a right-handed sector, not a full $SU(2)_R$ gauge theory.

Conventions used below (FeynRules defaults):

* `ProjP` $= P_R = \tfrac{1}{2}(1+\gamma^5)$, `ProjM` $= P_L = \tfrac{1}{2}(1-\gamma^5)$.
* `Ga[mu]` $= \gamma^\mu$.
* `FS[V,mu,nu]` $= \partial_\mu V_\nu - \partial_\nu V_\mu$ (abelian; no gauge self-coupling).
* `HC[...]` = hermitian conjugate of the whole expression.
* `CC[vlbar]` $= \overline{\nu^c}$, the Dirac bar of the charge-conjugate SM neutrino field,
  $\nu^c = C\,\bar\nu^{\,T}$.
* `uq`, `dq`, `l`, `vl` are the SM up-quark, down-quark, charged-lepton and neutrino
  fields; `gw` $= g_L$ is the SM $SU(2)_L$ coupling; `sw`, `cw` are $\sin\theta_W$, $\cos\theta_W$.
* Repeated generation indices $i,j = 1,2,3$ are summed. Color is summed trivially:
  no new field carries a color index.

## 1. Lagrangian

The total Lagrangian is
$$
\mathcal{L}_{\rm Total}
=\mathcal{L}_{\rm SM}
+\mathcal{L}_{W_R\rm kin}
+\mathcal{L}_{Z_R\rm kin}
+\mathcal{L}_{N\rm kin}
+\mathcal{L}_{W_R q}
+\mathcal{L}_{W_R \ell}
+\mathcal{L}_{Z_R q}.
$$

### Covariant-derivative / gauge content

No `DC` appears anywhere in the file. Consequences, stated explicitly:

* $W_R^\pm$ and $Z_R$ propagate **freely** apart from the explicit fermion currents
  written below. Although $W_R$ declares `QuantumNumbers -> {Q -> 1}`, the file uses
  `FS[WR,mu,nu]` (abelian), so there is **no** $\gamma W_R^+W_R^-$ or $Z W_R^+ W_R^-$
  vertex from this file, and no $SU(3)_c$ or $SU(2)_L$ structure on the new vectors.
* $N_R$ is a gauge singlet: its kinetic term uses the plain derivative `del[NR,mu]`.
* The only gauge information entering is numerical: the SM coupling $g_L$ (`gw`) and
  the weak mixing angle through $t_W^2 = s_W^2/c_W^2$, both rescaled by the
  right-handed coupling ratios $\kappa_R^q$, $\kappa_R^\ell$ (see §3).
* All SM fields keep their usual $\mathcal{L}_{\rm SM}$ covariant derivative
  $D_\mu = \partial_\mu - i g_s T^a G^a_\mu - i g_L T^k W^k_\mu - i g' Y B_\mu$.

### `LWRkin` — charged heavy vector, Proca kinetic + mass

$$
\mathcal{L}_{W_R\rm kin}
= -\tfrac{1}{2}\,W_{R\,\mu\nu}^{\dagger}\,W_R^{\mu\nu}
\;+\; M_{W_R}^{2}\,W_{R\,\mu}^{\dagger}\,W_R^{\mu},
\qquad
W_{R\,\mu\nu} \equiv \partial_\mu W_{R\,\nu}-\partial_\nu W_{R\,\mu}.
$$
(`WRbar` is the conjugate field $W_R^{-}$; the $\tfrac12$ and the unit mass
coefficient are the standard normalization for a complex vector.)

### `LZRkin` — neutral heavy vector, Proca kinetic + mass

$$
\mathcal{L}_{Z_R\rm kin}
= -\tfrac{1}{4}\,Z_{R\,\mu\nu}Z_R^{\mu\nu}
\;+\;\tfrac{1}{2}M_{Z_R}^{2}\,Z_{R\,\mu}Z_R^{\mu},
\qquad
Z_{R\,\mu\nu} \equiv \partial_\mu Z_{R\,\nu}-\partial_\nu Z_{R\,\mu}.
$$
$Z_R$ is real (self-conjugate), hence the $\tfrac14$ and $\tfrac12$ factors.

### `LNkin` — Majorana kinetic and mass term

$$
\mathcal{L}_{N\rm kin}
= \frac{i}{2}\,\overline{N_i}\,\gamma^\mu \partial_\mu N_i
\;-\;\frac{1}{2}\,M_{N_i}\,\overline{N_i}\,N_i ,
\qquad N_i = N_i^{\,c},\quad i=1,2,3 .
$$
The $\tfrac12$ factors are the Majorana normalization; `ff` is the flavor index and
`sp` the spinor index, so $M_N$ is diagonal in generation space (it is declared as a
per-member mass, not a matrix).

### `LWRq` — right-handed charged quark current

$$
\mathcal{L}_{W_R q}
= -\frac{\kappa_R^{q}\,g_L}{\sqrt{2}}\;
\overline{u}_i\,\bigl(V^{R}_{\rm CKM}\bigr)_{ij}\,\gamma^\mu P_R\, d_j\;W_{R\,\mu}
\;+\;{\rm h.c.}
$$
equivalently $-\dfrac{\kappa_R^{q}g_L}{\sqrt2}\,\overline{u_{R\,i}}\,(V^R_{\rm CKM})_{ij}\,\gamma^\mu d_{R\,j}\,W^+_{R\,\mu}+{\rm h.c.}$
Only right-handed quark chiralities take part. Color is contracted diagonally
($\delta^{ab}$), as in the SM charged current.

### `LWRl` — right-handed charged lepton current (two pieces)

$$
\mathcal{L}_{W_R \ell}
= -\frac{\kappa_R^{\ell}\,g_L}{\sqrt{2}}
\Bigl[\;
\overline{N}_i\,(Y_N)_{ij}\,\gamma^\mu P_R\,\ell_j
\;+\;
\overline{\nu^{c}}_i\,(X_N)_{ij}\,\gamma^\mu P_R\,\ell_j
\;\Bigr] W_{R\,\mu}
\;+\;{\rm h.c.}
$$

Reading the two pieces with $\bar\psi_1\gamma^\mu P_R\psi_2=\overline{\psi_{1R}}\gamma^\mu\psi_{2R}$:

* **heavy piece:** $\overline{N_i}\,(Y_N)_{ij}\gamma^\mu \ell_{R\,j}\,W^+_{R\,\mu}$ —
  a heavy Majorana neutrino with a right-handed charged lepton.
* **light piece:** $\overline{(\nu_{L})^{c}}_i\,(X_N)_{ij}\gamma^\mu \ell_{R\,j}\,W^+_{R\,\mu}$,
  because the right-chiral part of $\nu^c$ is $(\nu_L)^c$. This is the
  heavy–light mixing insertion: it lets the **light** SM neutrino enter the
  right-handed current. $X_N$ is zero in the default numerical input, so this
  vertex vanishes unless the user changes it.

### `LZRq` — neutral heavy-vector quark current

$$
\mathcal{L}_{Z_R q}
= -\frac{\kappa_R^{q}\,g_L}{n_{Z_R}^{q}}
\Bigl[
 g^{u}_{L}\,\overline{u}\gamma^\mu P_L u
+g^{u}_{R}\,\overline{u}\gamma^\mu P_R u
+g^{d}_{L}\,\overline{d}\gamma^\mu P_L d
+g^{d}_{R}\,\overline{d}\gamma^\mu P_R d
\Bigr] Z_{R\,\mu},
$$
with (see §3)
$$
g^{u}_{L}=-\tfrac16\frac{t_W^2}{\kappa_R^{q\,2}},\quad
g^{u}_{R}=\tfrac12-\tfrac23\frac{t_W^2}{\kappa_R^{q\,2}},\quad
g^{d}_{L}=-\tfrac16\frac{t_W^2}{\kappa_R^{q\,2}},\quad
g^{d}_{R}=-\tfrac12+\tfrac13\frac{t_W^2}{\kappa_R^{q\,2}} .
$$
The current is flavor-diagonal (no mixing matrix), and generation indices are summed
over all three families.

### Terms that are declared but never used

`LTotal` contains **no leptonic $Z_R$ term.** The file nevertheless defines the
complete set of internal parameters that such a term needs —
`nZRl`, `gLZRe`, `gRZRe`, `gLZRv`, `gRZRn` — and none of them appears in any
Lagrangian expression. The charge pattern of those five parameters is exactly the
lepton counterpart of `LZRq` (charged leptons, light neutrinos and the heavy $N$),
so the natural completion of this Lagrangian, absent from the file, is
$$
\mathcal{L}_{Z_R \ell}
= -\frac{\kappa_R^{\ell} g_L}{n_{Z_R}^{\ell}}
\Bigl[g^{e}_{L}\overline{e}\gamma^\mu P_L e+g^{e}_{R}\overline{e}\gamma^\mu P_R e
+g^{\nu}_{L}\overline{\nu}\gamma^\mu P_L \nu
+\tfrac12 g^{N}_{R}\overline{N}\gamma^\mu P_R N\Bigr]Z_{R\,\mu}.
$$
I flag this as an **observation about the file**, not as part of the reconstruction:
as written, $Z_R$ couples to quarks only, so it has no leptonic decay channel and no
Drell–Yan dilepton signal, which is inconsistent with the declared $Z_R$ width.

## 2. Field table

| `.fr` class | Symbol | Spin | $SU(3)_c$ | $SU(2)$ | $U(1)$ charge | Self-conj. | Mass symbol / value (GeV) | Width (GeV) | PDG |
|---|---|---|---|---|---|---|---|---|---|
| `V[100]` | $W_R^{\pm}$ (`WR`) | 1 | singlet (no color index) | none declared (mass eigenstate) | $Q=+1$ | No (antiparticle `wr-`) | `MWR` $=3000$ | `WWR` $=84.3$ | 9900024 |
| `V[101]` | $Z_R$ (`ZR`) | 1 | singlet | none declared | $Q=0$ (none declared) | Yes (real vector) | `MZR` $=5070$ | `WZR` $=114$ | 9900023 |
| `F[100]` | $N_i$ (`NR`: `n1,n2,n3`) | 1/2 | singlet | none declared | $Q=0$ | Yes (Majorana) | `MN`: `mn1` $=173.3$, `mn2` $=10^{12}$, `mn3` $=10^{12}$ | `Wn1` $=2.12\times10^{-8}$, `Wn2`=`Wn3`$=0$ | 9900012/14/16 |

Notes:

* $N$ carries one `Generation` index and uses it as `FlavorIndex`, so the three
  members are flavor states with a diagonal mass matrix.
* $n_2$ and $n_3$ sit at $10^{12}$ GeV with zero width: they are decoupled, and only
  $n_1$ is phenomenologically active.
* The mass pair obeys the left–right relation
  $M_{Z_R}=\sqrt{2}\,M_{W_R}/\sqrt{1-t_W^2}\approx1.69\,M_{W_R}$:
  $1.69\times3000\approx5070$ GeV, consistent with $\kappa_R=1$.
* `M$InteractionOrderHierarchy` declares `{QCD,1},{QED,2},{NP,1}`, so every new
  vertex counts as one power of `NP`.

## 3. Parameters

### External (block `LRSMINPUTS`)

| Symbol | Block order | Value | Multiplies | Meaning |
|---|---|---|---|---|
| `kapRq` $=\kappa_R^{q}$ | 1 | 1.0 | overall factor of `LWRq` and of `LZRq` (and, inversely squared, inside $n^q_{Z_R}$ and every $g^{q}_{L,R}$) | ratio of the right-handed to the left-handed gauge coupling in the **quark** sector, $\kappa_R^q=g_R/g_L$; `InteractionOrder -> {NP,1}` |
| `kapRl` $=\kappa_R^{\ell}$ | 2 | 1.0 | overall factor of `LWRl` (and, inversely squared, inside $n^\ell_{Z_R}$ and the lepton $g$'s) | same coupling ratio for the **lepton** sector; `InteractionOrder -> {NP,1}` |

Splitting $\kappa$ into a quark and a lepton copy is what makes this an *effective*
model: the two sectors can be rescaled independently, which a genuine gauge theory
would not allow.

### Internal (derived)

| Symbol | Value | Role |
|---|---|---|
| `tw2` | $t_W^2=s_W^2/c_W^2=\tan^2\theta_W$ | weak-mixing shorthand |
| `nZRq` | $\sqrt{1-t_W^2/\kappa_R^{q\,2}}$ | normalization of the $Z_R$ coupling to quarks; the overall $Z_R$ coupling is $g_L\kappa_R^q/n^q_{Z_R}=g_R/\sqrt{1-t_W^2 g_L^2/g_R^2}$ |
| `nZRl` | $\sqrt{1-t_W^2/\kappa_R^{\ell\,2}}$ | same for leptons — **defined but never used** |
| `gLZRu`, `gLZRd` | $-\tfrac16 t_W^2/\kappa_R^{q\,2}$ | left-handed quark $Z_R$ charges |
| `gRZRu` | $\tfrac12-\tfrac23 t_W^2/\kappa_R^{q\,2}$ | right-handed up-quark $Z_R$ charge |
| `gRZRd` | $-\tfrac12+\tfrac13 t_W^2/\kappa_R^{q\,2}$ | right-handed down-quark $Z_R$ charge |
| `gLZRe`, `gLZRv` | $+\tfrac12 t_W^2/\kappa_R^{\ell\,2}$ | left-handed charged-lepton / neutrino $Z_R$ charges — **unused** |
| `gRZRe` | $-\tfrac12+t_W^2/\kappa_R^{\ell\,2}$ | right-handed charged-lepton $Z_R$ charge — **unused** |
| `gRZRn` | $+\tfrac12$ | heavy-neutrino $Z_R$ charge — **unused** |
| `VCKMR` | $3\times3$, `Unitary -> True`, default $\mathbb{1}$ | right-handed quark mixing matrix $V^R_{\rm CKM}$ in `LWRq` |
| `YN` | $3\times3$, default $\mathbb{1}$ | heavy-neutrino–charged-lepton mixing in the right-handed current |
| `XN` | $3\times3$, default $0$ | light-neutrino ($\nu^c$)–charged-lepton mixing in the right-handed current; heavy–light mixing, switched off by default |

All $Z_R$ charges follow one formula,
$$
g_{L,R}^{f}=T_{3R}^{f}-\frac{t_W^2}{\kappa_R^{2}}\,Y_f ,
\qquad Y_f = Q_f - T_{3L}^{f},
$$
which is the standard $Z_R$ current of the left–right symmetric model:
$T_{3R}$ for the right-handed multiplets, and a hypercharge piece suppressed by
$t_W^2/\kappa_R^2$ for both chiralities.

## 4. Physics summary

This is an effective right-handed (left–right symmetric) extension of the Standard
Model: a 3 TeV charged vector $W_R^\pm$, a 5.07 TeV neutral vector $Z_R$, and three
heavy Majorana neutrinos $N_{1,2,3}$ (only $N_1$ at 173.3 GeV is light enough to
matter). The new vectors are added as Proca fields with hand-inserted masses rather
than as gauge bosons, and they couple only through explicit currents whose strength
is the SM $g_L$ rescaled by independent quark and lepton coupling ratios
$\kappa_R^{q,\ell}$.

$W_R$ mediates a purely right-handed charged current: $\bar u_R V^R_{\rm CKM} d_R$ for
quarks, and $\bar N Y_N \ell_R$ plus the mixing term $\overline{(\nu_L)^c} X_N \ell_R$
for leptons. $Z_R$, as written, couples only to quarks, with chiral charges
$T_{3R}-t_W^2 Y/\kappa_R^2$.

The processes it would mediate are the classic left–right collider signals:
$pp\to W_R\to \ell^\pm N$ followed by $N\to \ell^\pm jj$ through an off-shell $W_R$ —
the Keung–Senjanović same-sign dilepton plus dijet final state, which violates lepton
number because $N$ is Majorana — plus $W_R\to jj$ and $Z_R\to q\bar q$ dijet
resonances. Because the leptonic $Z_R$ current is missing from this file, $Z_R$ here
produces dijets only and has no dilepton or invisible decay mode.
