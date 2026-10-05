# Reconstruction of `sanitized.fr`

## 0. Conventions used below

| `.fr` idiom | Meaning here |
| --- | --- |
| `ProjM` | $P_L=\tfrac{1-\gamma^5}{2}$ (FeynRules convention) |
| `ProjP` | $P_R=\tfrac{1+\gamma^5}{2}$ |
| `Ga[mu]` | $\gamma^\mu$ |
| `FS[V,mu,nu]` | $V_{\mu\nu}=\partial_\mu V_\nu-\partial_\nu V_\mu$ (abelian field strength; no self-coupling is generated for `WR`/`ZR`) |
| `HC[x]` | $x+\mathrm{h.c.}$ when added to `x` |
| `CC[vlbar]` | $\overline{\nu^c}$, the charge-conjugate of the SM neutrino field |
| `del[X,mu]` | $\partial_\mu X$ |
| `Xbar` | $\bar X$ |
| `gw`, `sw`, `cw` | SM $SU(2)_L$ coupling $g$, $\sin\theta_W$, $\cos\theta_W$ (inherited from `LSM`) |

**Gauge content of the covariant derivative.** The file contains **no** `DC[...]` and no
`FS[...,a]` with an adjoint index. The new vectors $W_R$ and $Z_R$ are introduced as
*effective, already-massive* Proca fields with hand-written currents, not as gauge fields
of a gauged $SU(2)_R\times U(1)_{B-L}$. Therefore:

* The only covariant derivative in the model is the SM one, hidden inside `LSM`:
  $D_\mu=\partial_\mu-i g_s G^a_\mu T^a-i g W^i_\mu T^i-i g' Y B_\mu$, acting on the SM fields
  with the usual $SU(3)_C\times SU(2)_L\times U(1)_Y$ content.
* The heavy neutrino `NR` is a total gauge singlet, so its kinetic term uses the **ordinary**
  derivative $\partial_\mu$.
* $W_R$ and $Z_R$ have no triple or quartic self-couplings and no coupling to the photon or
  gluon; all of their interactions are the four explicit current terms below.

The total Lagrangian is

$$\mathcal{L}_{\rm Total}=\mathcal{L}_{\rm SM}+\mathcal{L}_{W_R}^{\rm kin}+\mathcal{L}_{Z_R}^{\rm kin}+\mathcal{L}_{N}^{\rm kin}+\mathcal{L}_{W_R}^{q}+\mathcal{L}_{W_R}^{\ell}+\mathcal{L}_{Z_R}^{q}+\mathcal{L}_{Z_R}^{\ell}.$$

---

## 1. Lagrangian, term by term

### `LWRkin` — complex Proca term for the charged heavy vector

$$\mathcal{L}_{W_R}^{\rm kin}=-\frac{1}{2}\,W_{R\,\mu\nu}^{\dagger}W_R^{\mu\nu}
+M_{W_R}^{2}\,W_{R\,\mu}^{\dagger}W_R^{\mu},
\qquad W_{R\,\mu\nu}=\partial_\mu W_{R\,\nu}-\partial_\nu W_{R\,\mu}.$$

($W_R$ is charged, so the field strength is the abelian one and the mass term has the
complex-field normalisation $M^2|W_R|^2$, not $\tfrac12 M^2 W^2$.)

### `LZRkin` — real Proca term for the neutral heavy vector

$$\mathcal{L}_{Z_R}^{\rm kin}=-\frac{1}{4}\,Z_{R\,\mu\nu}Z_R^{\mu\nu}
+\frac{1}{2}M_{Z_R}^{2}\,Z_{R\,\mu}Z_R^{\mu},
\qquad Z_{R\,\mu\nu}=\partial_\mu Z_{R\,\nu}-\partial_\nu Z_{R\,\mu}.$$

### `LNkin` — Majorana kinetic and mass term for the three heavy neutrinos

$$\mathcal{L}_{N}^{\rm kin}=\sum_{i=1}^{3}\left[\frac{i}{2}\,\overline{N_i}\,\gamma^\mu\partial_\mu N_i
-\frac{1}{2}M_{N_i}\,\overline{N_i}N_i\right].$$

The factors $\tfrac12$ are the Majorana (self-conjugate) normalisation; the flavour index
`ff` is the `Generation` index, and $M_{N_i}=\{m_{n_1},m_{n_2},m_{n_3}\}$ is diagonal.

### `LWRq` — charged current of $W_R$ to quarks

$$\mathcal{L}_{W_R}^{q}=-\frac{\kappa_R^{q}\,g}{\sqrt{2}}\;
\overline{u}_i\,(V^{R}_{\rm CKM})_{ij}\,\gamma^\mu P_{L}\,d_j\;W_{R\,\mu}\;+\;\mathrm{h.c.}$$

with $i,j$ generation indices, colour contracted trivially (diagonal), and the hermitian
conjugate giving $-\frac{\kappa_R^q g}{\sqrt2}\,\overline{d}_j (V^{R\,\dagger}_{\rm CKM})_{ji}\gamma^\mu P_L u_i\,W^{\dagger}_{R\mu}$.

> **Chirality note (important).** The quark current is written with `ProjM`, i.e. the
> **left-handed** projector $P_L$, while the lepton current below uses `ProjP` ($P_R$) and the
> $Z_R$ couplings are labelled `gLZR*`↔`ProjM`, `gRZR*`↔`ProjP` consistently. A charged heavy
> vector named "$W_R$" coupling to a *left*-chiral quark current but a *right*-chiral lepton
> current is internally inconsistent: it is not the right-handed analogue of the SM $W$, and
> the $Z_R$ coupling set (built from $T_{3R}$, see §3) assumes right-handed quark doublets.
> I reconstruct the file exactly as written and flag the asymmetry rather than "correcting" it.

### `LWRl` — charged current of $W_R$ to leptons

$$\mathcal{L}_{W_R}^{\ell}=-\frac{\kappa_R^{\ell}\,g}{\sqrt{2}}\left[
\overline{N_i}\,(Y_N)_{ij}\,\gamma^\mu P_{R}\,\ell_j
+\overline{\nu^{c}_i}\,(X_N)_{ij}\,\gamma^\mu P_{R}\,\ell_j\right]W_{R\,\mu}
\;+\;\mathrm{h.c.}$$

* First piece: heavy Majorana neutrino ↔ charged lepton, mixing matrix $Y_N$ (identity by default).
* Second piece: the *charge-conjugated* light neutrino $\overline{\nu^c}$ ↔ charged lepton,
  mixing matrix $X_N$ (zero by default). Because it uses $\nu^c$ rather than $\nu$, this
  operator violates lepton number by two units; it is the light-neutrino admixture of the
  right-handed current.

### `LZRq` — neutral current of $Z_R$ to quarks

$$\mathcal{L}_{Z_R}^{q}=-\frac{\kappa_R^{q}\,g}{n_{Z_R}^{q}}\left[
g^{u}_{L}\,\overline{u}\gamma^\mu P_{L}u+g^{u}_{R}\,\overline{u}\gamma^\mu P_{R}u
+g^{d}_{L}\,\overline{d}\gamma^\mu P_{L}d+g^{d}_{R}\,\overline{d}\gamma^\mu P_{R}d
\right]Z_{R\,\mu}.$$

Flavour- and colour-diagonal (generation index summed implicitly, no mixing matrix).

### `LZRl` — neutral current of $Z_R$ to leptons

$$\mathcal{L}_{Z_R}^{\ell}=-\frac{\kappa_R^{\ell}\,g}{n_{Z_R}^{\ell}}\left[
g^{e}_{L}\,\overline{e}\gamma^\mu P_{L}e+g^{e}_{R}\,\overline{e}\gamma^\mu P_{R}e
+g^{\nu}_{L}\,\overline{\nu}\gamma^\mu P_{L}\nu
+g^{N}_{R}\,\overline{N}\gamma^\mu P_{R}N
\right]Z_{R\,\mu}.$$

Two structural points:

* There is **no** right-handed light-neutrino term (the SM $\nu$ has no $\nu_R$ component here),
  and **no** left-handed $N$ term.
* $N$ is Majorana, so $\overline{N}\gamma^\mu N\equiv 0$ and the last bilinear collapses to a
  purely axial coupling:
  $g^{N}_{R}\,\overline{N}\gamma^\mu P_R N=\tfrac{1}{2}g^{N}_{R}\,\overline{N}\gamma^\mu\gamma^5 N$.
  With three generations the term is diagonal in flavour: $\sum_i \overline{N_i}\gamma^\mu P_R N_i$.

---

## 2. Field table

| Symbol (`ClassName`) | Class | Spin | $SU(3)_C$ | $SU(2)_L$ | U(1) charge $Q$ | Self-conj. | Mass symbol / value (GeV) | Width symbol / value (GeV) | PDG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `WR` ($W_R^{\pm}$) | `V[100]` | 1 | singlet (no colour index) | not declared (mass eigenstate) | $+1$ | No (antiparticle `wr-`) | `MWR` $=3000$ | `WWR` $=84.3$ | 9900024 |
| `ZR` ($Z_R$) | `V[101]` | 1 | singlet | not declared | $0$ | Yes | `MZR` $=5070$ | `WZR` $=114$ | 9900023 |
| `NR` ($N_{1,2,3}$) | `F[100]` | 1/2 (Majorana) | singlet | not declared | $0$ | Yes | `MN[i]`: `mn1` $=173.3$, `mn2` $=1\times10^{12}$, `mn3` $=1\times10^{12}$ | `WN[i]`: `Wn1` $=2.12\times10^{-8}$, `Wn2` $=0$, `Wn3` $=0$ | 9900012, 9900014, 9900016 |

Notes:

* `NR` carries `Indices -> {Index[Generation]}` with `FlavorIndex -> Generation` and members
  `n1, n2, n3`; it is a three-flavour Majorana multiplet.
* No class declares `Indices -> {Index[Colour]}` and none declares an $SU(2)$ multiplet
  structure, which confirms the effective (mass-eigenstate, non-gauged) construction.
* All SM fields (`uq, dq, l, vl`, and their bars) come from the imported `LSM`.
* `M$InteractionOrderHierarchy = {{QCD,1},{QED,2},{NP,1}}` adds a new coupling order `NP`
  carried by $\kappa_R^{q}$ and $\kappa_R^{\ell}$.

---

## 3. Parameters

### External (the only true inputs)

| Symbol | Block / order | Value | Interaction order | Multiplies | Physical meaning |
| --- | --- | --- | --- | --- | --- |
| `kapRq` $\kappa_R^{q}$ | `LRSMINPUTS`, 1 | $1.0$ | `{NP,1}` | the whole of `LWRq` (as $\kappa_R^q g/\sqrt2$) and `LZRq` (as $\kappa_R^q g/n_{Z_R}^q$); also enters `nZRq`, `gLZRu`, `gRZRu`, `gLZRd`, `gRZRd` | Ratio of the right-handed gauge coupling to the SM one, $\kappa_R^{q}=g_R/g_L$, in the **quark** sector. $\kappa_R^q=1$ is the manifestly left-right-symmetric point. |
| `kapRl` $\kappa_R^{\ell}$ | `LRSMINPUTS`, 2 | $1.0$ | `{NP,1}` | the whole of `LWRl` and `LZRl`; also enters `nZRl`, `gLZRe`, `gRZRe`, `gLZRv` | Same ratio $g_R/g_L$ for the **lepton** sector, allowed to differ from the quark one. |

Every other quantity is `Internal` (derived) or inherited from the SM (`gw`, `sw`, `cw`) or is
a declared mass/width (`MWR`, `MZR`, `mn1..mn3`, `WWR`, `WZR`, `Wn1..Wn3`), which FeynRules
creates as numerical inputs from the `Mass`/`Width` entries of §2.

### Internal (derived) parameters

| Symbol | Value | Role |
| --- | --- | --- |
| `tw2` | $s_W^2/c_W^2=\tan^2\theta_W$ | Shorthand for the weak mixing. |
| `nZRq` | $\sqrt{1-\tan^2\theta_W/\kappa_R^{q\,2}}$ | Normalisation of the $Z_R$ quark current; the overall $Z_R$ coupling is $\kappa_R^q g/n_{Z_R}^q$. It goes imaginary for $\kappa_R^q<\tan\theta_W\simeq0.55$, the usual lower bound on $g_R/g_L$. |
| `nZRl` | $\sqrt{1-\tan^2\theta_W/\kappa_R^{\ell\,2}}$ | Same for the lepton current. |
| `gLZRu` | $-\tfrac16\tan^2\theta_W/\kappa_R^{q\,2}$ | $Z_R$ coupling to $\bar u\gamma^\mu P_L u$. |
| `gRZRu` | $\tfrac12-\tfrac23\tan^2\theta_W/\kappa_R^{q\,2}$ | $Z_R$ coupling to $\bar u\gamma^\mu P_R u$. |
| `gLZRd` | $-\tfrac16\tan^2\theta_W/\kappa_R^{q\,2}$ | $Z_R$ coupling to $\bar d\gamma^\mu P_L d$. |
| `gRZRd` | $-\tfrac12+\tfrac13\tan^2\theta_W/\kappa_R^{q\,2}$ | $Z_R$ coupling to $\bar d\gamma^\mu P_R d$. |
| `gLZRe` | $+\tfrac12\tan^2\theta_W/\kappa_R^{\ell\,2}$ | $Z_R$ coupling to $\bar e\gamma^\mu P_L e$. |
| `gRZRe` | $-\tfrac12+\tan^2\theta_W/\kappa_R^{\ell\,2}$ | $Z_R$ coupling to $\bar e\gamma^\mu P_R e$. |
| `gLZRv` | $+\tfrac12\tan^2\theta_W/\kappa_R^{\ell\,2}$ | $Z_R$ coupling to $\bar\nu\gamma^\mu P_L \nu$. |
| `gRZRn` | $+\tfrac12$ | $Z_R$ coupling to $\bar N\gamma^\mu P_R N$ (pure $T_{3R}$, since $Q_N=0$). |
| `VCKMR` | $3\times3$, `Unitary -> True`, set to $\mathbb{1}$ | Right-handed quark mixing matrix $V^{R}_{\rm CKM}$ in `LWRq`; the analogue of the CKM matrix for the heavy charged current. Identity by default (no flavour violation). |
| `YN` | $3\times3$, set to $\mathbb{1}$ | Mixing of the heavy Majorana neutrinos with the charged leptons in `LWRl`; $N_i \leftrightarrow \ell_i$ one-to-one by default. |
| `XN` | $3\times3$, set to $0$ | Mixing of the *light* neutrinos (through $\nu^c$) with the charged leptons in `LWRl`; switched off by default, so the light-neutrino right-handed current vanishes numerically. |

All ten chiral $Z_R$ couplings follow one formula,
$$g^{f}_{L,R}=T_{3R}^{f}-\bigl(Q_f-T_{3L}^{f}\bigr)\frac{\tan^2\theta_W}{\kappa_R^{2}}
\;=\;T_{3R}^{f}-\Bigl(T_{3R}^{f}+\tfrac{B-L}{2}\Bigr)\frac{\tan^2\theta_W}{\kappa_R^{2}},$$
which is the standard $SU(2)_R\times U(1)_{B-L}\to U(1)_Y$ result. This is why the `gL*`
entries are $B\!-\!L$-only ($T_{3R}=0$ for left-chiral fields) while the `gR*` entries start
from $\pm\tfrac12$.

---

## 4. Physics summary

This is an **effective right-handed / left-right-symmetric extension of the SM**: a charged
spin-1 state $W_R^{\pm}$ ($3$ TeV), a neutral spin-1 state $Z_R$ ($5.07$ TeV) and three
right-handed **Majorana** neutrinos $N_{1,2,3}$ (one light at $173.3$ GeV, two decoupled at
$10^{12}$ GeV) are added as mass eigenstates with hand-written currents, so the heavy bosons
have Proca kinetic terms, no self-interactions, and couplings fixed by two free strengths
$\kappa_R^{q,\ell}=g_R/g_L$, a right-handed CKM matrix $V^R$, and the lepton mixings $Y_N$
(heavy) and $X_N$ (light, $\nu^c$, lepton-number violating).

It mediates resonant $pp\to W_R\to \ell N$ with the heavy neutrino then decaying through an
off-shell $W_R$ to $\ell jj$ — the Keung–Senjanović same-sign dilepton plus dijet signature,
whose lepton-number violation comes from the Majorana nature of $N$ — as well as $W_R\to$
dijet, $Z_R\to \ell^+\ell^-/q\bar q/NN$ Drell–Yan resonances, and (through the $X_N$ operator,
zero by default) $W_R$–light-neutrino transitions relevant to neutrinoless double beta decay.

One caveat for whoever uses this file: as noted in §1, the $W_R$ **quark** current is written
with $P_L$ (`ProjM`) while the $W_R$ **lepton** current uses $P_R$ (`ProjP`) and the whole
$Z_R$ sector is built on right-handed $T_{3R}$ assignments. Taken literally, the model's
charged current is a left-handed quark current times a right-handed lepton current, which is
neither the SM $W$ nor a genuine $W_R$; it interferes with the SM $W$ amplitude in quark-side
processes and breaks the $g_R/g_L$ interpretation of $\kappa_R^{q}$.
