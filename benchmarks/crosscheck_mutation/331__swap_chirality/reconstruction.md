# Reconstruction of `sanitized.fr`

The file adds new states on top of a Standard Model (SM) base implementation. It uses
SM symbols that it does not itself declare: `gw`, `gs`, `vev`, the SM quark fields
`u, c, d, s`, and the SM gauge fields. The covariant derivative `DC` therefore refers to
the SM gauge groups of the base file.

**Gauge content of `DC`.** No new field carries an `SU2W` index, and no new gauge group is
declared. For a field `phi` with colour index and hypercharge `Y`:

$$
D_\mu \phi \;=\; \Big(\partial_\mu \;-\; i\,g_s\,G^a_\mu\,T^a \;-\; i\,g'\,Y\,B_\mu\Big)\phi ,
\qquad
B_\mu = c_W A_\mu - s_W Z_\mu ,
$$

$$
\Rightarrow\quad
D_\mu \phi \;=\; \Big(\partial_\mu \;-\; i\,g_s\,G^a_\mu\,T^a \;-\; i\,e\,Q\,A_\mu \;+\; i\,e\,t_W\,Y\,Z_\mu\Big)\phi ,
\qquad t_W = \tan\theta_W .
$$

Every new field has `Q == Y`, so all of them are $SU(2)_L$ singlets with $T^3=0$.
Colour-singlet fields drop the $G^a_\mu$ term. Fields with $Q=Y=0$ (`EL`, `H2`, `H3`, `H0`,
`HQV`) have a covariant derivative equal to the plain derivative $\partial_\mu$.

**Important:** the new vectors `Zp`, `Yp`, `Vp` are *not* declared as gauge fields. They do
not enter `DC`. Their only interactions in this file are the explicit terms in `LNPcc`.

`FS[X,mu,nu]` for these non-gauge vectors is the abelian field strength
$X_{\mu\nu} = \partial_\mu X_\nu - \partial_\nu X_\mu$.
`ProjP` $= P_R = (1+\gamma^5)/2$, `ProjM` $= P_L = (1-\gamma^5)/2$.

---

## 1. Lagrangian

### `LZp` — neutral heavy vector, kinetic + mass

$$
\mathcal{L}_{Z'} \;=\; -\tfrac{1}{4}\,Z'_{\mu\nu}Z'^{\,\mu\nu} \;+\; \tfrac{1}{2} M_{Z'}^2\, Z'_\mu Z'^\mu ,
\qquad Z'_{\mu\nu} = \partial_\mu Z'_\nu - \partial_\nu Z'_\mu .
$$

$Z'$ is real (self-conjugate), hence the $1/4$ and $1/2$ factors.

### `LYp` — singly charged complex vector, kinetic + mass

$$
\mathcal{L}_{Y'} \;=\; -\tfrac{1}{2}\, Y'^{\dagger}_{\mu\nu} Y'^{\,\mu\nu} \;+\; M_{Y'}^2\, Y'^{\dagger}_\mu Y'^\mu ,
\qquad Y'_{\mu\nu} = \partial_\mu Y'_\nu - \partial_\nu Y'_\mu .
$$

Note: the term is written with the plain derivative field strength, so $Y'$ has **no**
photon coupling even though it carries $Q=+1$. This is a literal reading of the file.

### `LVp` — neutral complex vector, kinetic + mass

$$
\mathcal{L}_{V'} \;=\; -\tfrac{1}{2}\, V'^{\dagger}_{\mu\nu} V'^{\,\mu\nu} \;+\; M_{V'}^2\, V'^{\dagger}_\mu V'^\mu .
$$

$V'$ is neutral but not self-conjugate, so $V'$ and $V'^\dagger$ are distinct states.

### `LDQ` — exotic down-type quark $D$

$$
\mathcal{L}_{D} \;=\; i\,\bar{D}\,\gamma^\mu D_\mu D \;-\; M_{D}\,\bar{D}D ,
\qquad
D_\mu D = \Big(\partial_\mu - i g_s G^a_\mu T^a - i e (-\tfrac{1}{3}) A_\mu + i e t_W (-\tfrac{1}{3}) Z_\mu\Big) D .
$$

Vector-like Dirac mass: both chiralities have the same gauge charges.

### `LSQ` — exotic down-type quark $S$

$$
\mathcal{L}_{S} \;=\; i\,\bar{S}\,\gamma^\mu D_\mu S \;-\; M_{S}\,\bar{S}S ,
\qquad Q_S = Y_S = -\tfrac{1}{3},\ \ \text{colour triplet}.
$$

### `LTQ` — exotic up-type quark $T$

$$
\mathcal{L}_{T} \;=\; i\,\bar{T}\,\gamma^\mu D_\mu T \;-\; M_{T}\,\bar{T}T ,
\qquad Q_T = Y_T = +\tfrac{2}{3},\ \ \text{colour triplet}.
$$

### `LEL` — three heavy neutral leptons $E_i = (E_e, E_\mu, E_\tau)$

$$
\mathcal{L}_{E} \;=\; i\,\bar{E}_i\,\gamma^\mu \partial_\mu E_i
\;-\; M_{E_e}\bar{E}_e E_e \;-\; M_{E_\mu}\bar{E}_\mu E_\mu \;-\; M_{E_\tau}\bar{E}_\tau E_\tau ,
\qquad i = e,\mu,\tau .
$$

$Q=Y=0$ and no colour, so $D_\mu \to \partial_\mu$: these states are complete SM gauge
singlets with Dirac masses. The generation index is summed in the kinetic term; the mass
terms are written flavour by flavour (diagonal, non-degenerate symbols).

### `LH2`, `LH3`, `LH0` — three real neutral scalars

$$
\mathcal{L}_{H_2} \;=\; \tfrac{1}{2}\,\partial_\mu H_2\,\partial^\mu H_2 \;-\; \tfrac{1}{2} M_{H_2}^2 H_2^2 ,
$$

$$
\mathcal{L}_{H_3} \;=\; \tfrac{1}{2}\,\partial_\mu H_3\,\partial^\mu H_3 \;-\; \tfrac{1}{2} M_{H_3}^2 H_3^2 ,
$$

$$
\mathcal{L}_{H_0} \;=\; \tfrac{1}{2}\,\partial_\mu H_0\,\partial^\mu H_0 \;-\; \tfrac{1}{2} M_{H_0}^2 H_0^2 .
$$

### `LHpm` — singly charged scalar

$$
\mathcal{L}_{H^\pm} \;=\; \big(D_\mu H^+\big)^\dagger \big(D^\mu H^+\big) \;-\; M_{H^\pm}^2\, H^{+\dagger} H^+ ,
\qquad
D_\mu H^+ = \big(\partial_\mu - i e A_\mu + i e t_W Z_\mu\big) H^+ ,
$$

with $Q = Y = +1$.

### `LHQY` — second singly charged scalar

$$
\mathcal{L}_{H_{QY}} \;=\; \big(D_\mu H_{QY}\big)^\dagger \big(D^\mu H_{QY}\big) \;-\; M_{H_{QY}}^2\, H_{QY}^\dagger H_{QY} ,
\qquad Q = Y = +1 .
$$

Same gauge quantum numbers as $H^\pm$; only the mass formula differs.

### `LHQV` — neutral complex scalar

$$
\mathcal{L}_{H_{QV}} \;=\; \partial_\mu H_{QV}^\dagger\, \partial^\mu H_{QV} \;-\; M_{H_{QV}}^2\, H_{QV}^\dagger H_{QV} ,
\qquad Q = Y = 0 .
$$

$H_{QV}$ is neutral but complex, so particle and antiparticle are distinct.

### `LNPcc` — new charged-current couplings of the heavy vectors

The file writes an explicit block plus an `HC[...]` of a *different* block. Written out:

$$
\mathcal{L}_{\rm NP}^{\rm cc} \;=\;
\frac{g}{\sqrt{2}}\Big[
\bar{u}\,\gamma^\mu P_R\, D\; Y'_\mu
\;+\; \bar{c}\,\gamma^\mu P_L\, S\; Y'_\mu
\;+\; \bar{d}\,\gamma^\mu P_L\, D\; V'_\mu
\;+\; \bar{s}\,\gamma^\mu P_L\, S\; V'_\mu \Big]
$$

$$
\;+\;
\frac{g}{\sqrt{2}}\Big[
\bar{D}\,\gamma^\mu P_L\, u\; Y'^{\dagger}_\mu
\;+\; \bar{S}\,\gamma^\mu P_L\, c\; Y'^{\dagger}_\mu
\;+\; \bar{D}\,\gamma^\mu P_L\, d\; V'^{\dagger}_\mu
\;+\; \bar{S}\,\gamma^\mu P_L\, s\; V'^{\dagger}_\mu \Big] .
$$

The second bracket is `HC[...]` applied to the four terms with `ProjM` throughout, using
$(\bar\psi_1\gamma^\mu P_L \psi_2)^\dagger = \bar\psi_2\gamma^\mu P_L \psi_1$ (the chiral
label is preserved by hermitian conjugation).

**Chirality inconsistency (as written in the file).** Three of the four couplings are
hermitian pairs, purely left-handed ($V-A$):

$$
\bar{c}\gamma^\mu P_L S\,Y'_\mu + \bar{S}\gamma^\mu P_L c\,Y'^\dagger_\mu,\quad
\bar{d}\gamma^\mu P_L D\,V'_\mu + \bar{D}\gamma^\mu P_L d\,V'^\dagger_\mu,\quad
\bar{s}\gamma^\mu P_L S\,V'_\mu + \bar{S}\gamma^\mu P_L s\,V'^\dagger_\mu .
$$

The $u$–$D$–$Y'$ coupling is **not** hermitian: the direct term uses $P_R$
(`ProjP`) while its conjugate partner inside `HC[...]` uses $P_L$ (`ProjM`). A hermitian
$u$–$D$–$Y'$ vertex needs either $P_R$ on both sides or $P_L$ on both sides. As written the
Lagrangian violates hermiticity in exactly this one term, and the $u$–$D$–$Y'$ vertex is
right-handed in one direction and left-handed in the other. Every other new-physics
current in the file is left-handed, so the lone $P_R$ is the odd one out.

Charge conservation check for each vertex (they all balance):
$-\tfrac{2}{3} - \tfrac{1}{3} + 1 = 0$ ($u,D,Y'$); $-\tfrac{2}{3}-\tfrac{1}{3}+1 = 0$
($c,S,Y'$); $+\tfrac{1}{3}-\tfrac{1}{3}+0 = 0$ ($d,D,V'$ and $s,S,V'$). Colour flows
$\bar{3}\otimes 3$ and is contracted between the SM quark and the exotic quark.

### `LTotal`

$$
\mathcal{L}_{\rm total} = \mathcal{L}_{Z'} + \mathcal{L}_{Y'} + \mathcal{L}_{V'}
+ \mathcal{L}_{D} + \mathcal{L}_{S} + \mathcal{L}_{T} + \mathcal{L}_{E}
+ \mathcal{L}_{H_2} + \mathcal{L}_{H_3} + \mathcal{L}_{H_0}
+ \mathcal{L}_{H^\pm} + \mathcal{L}_{H_{QY}} + \mathcal{L}_{H_{QV}}
+ \mathcal{L}_{\rm NP}^{\rm cc} .
$$

---

## 2. Field table

No new field declares an `SU2W` index, so all of them are $SU(2)_L$ singlets and $Q = Y$.

| `.fr` class | Symbol | Spin | $SU(3)_c$ | $SU(2)_L$ | $Q = Y$ | Self-conj. | Mass symbol | Mass value |
|---|---|---|---|---|---|---|---|---|
| `V[101]` `Zp` | $Z'_\mu$ | 1 | **1** | **1** | 0 | yes | `MZp` | internal: $\sqrt{(g^2+\beta^2 g_X^2)v_3^2/6}$ |
| `V[102]` `Yp` | $Y'^{\pm}_\mu$ | 1 | **1** | **1** | $+1$ | no | `MYp` | internal: $\sqrt{g^2(v_3^2+v_2^2)/4}$ |
| `V[103]` `Vp` | $V'_\mu$ | 1 | **1** | **1** | 0 | no | `MVp` | internal: $\sqrt{g^2(v_3^2+v_1^2)/4}$ |
| `F[101]` `DQ` | $D$ | 1/2 | **3** | **1** | $-1/3$ | no | `MDQ` | 1000 GeV |
| `F[102]` `SQ` | $S$ | 1/2 | **3** | **1** | $-1/3$ | no | `MSQ` | 1000 GeV |
| `F[103]` `TQ` | $T$ | 1/2 | **3** | **1** | $+2/3$ | no | `MTQ` | 1000 GeV |
| `F[104]` `EL` | $E_e,E_\mu,E_\tau$ | 1/2 | **1** | **1** | 0 | no | `MEE`,`MEM`,`MET` | 1000 GeV each |
| `S[101]` `H2` | $H_2$ | 0 | **1** | **1** | 0 | yes | `MH2` | internal (see below) |
| `S[102]` `H3` | $H_3$ | 0 | **1** | **1** | 0 | yes | `MH3` | internal: $\sqrt{2\lambda_3 v_3^2}$ |
| `S[103]` `H0` | $H_0$ | 0 | **1** | **1** | 0 | yes | `MH0` | internal (see below) |
| `S[104]` `Hpm` | $H^{\pm}$ | 0 | **1** | **1** | $+1$ | no | `MHpm` | internal (see below) |
| `S[105]` `HQY` | $H_{QY}^{\pm}$ | 0 | **1** | **1** | $+1$ | no | `MHQY` | internal (see below) |
| `S[106]` `HQV` | $H_{QV}$ | 0 | **1** | **1** | 0 | no | `MHQV` | internal (see below) |

Notes.

- `EL` carries a `Generation` flavour index with three members and non-degenerate mass
  symbols. Its declared charges are $Q=Y=0$, so the three states are neutral SM singlets.
  The surviving `FullName` strings call them "heavy charged lepton", which contradicts the
  declared $Q=0$. Trust the quantum numbers: they are neutral.
- PDG codes run from 4000001 (`Zp`) to 4000015 (`HQV`). All widths are set to 1 GeV
  placeholders.
- `Colour` index means the fundamental **3** for the particle and $\bar{\mathbf 3}$ for the
  antiparticle.

---

## 3. Parameters

### External parameters (block `NPINPUTS`)

| Symbol | Value | Multiplies / enters | Physical meaning |
|---|---|---|---|
| `beta` $\beta$ | $0.5773502691896258 = 1/\sqrt{3}$ | $M_{Z'}$ formula, as $\beta^2 g_X^2$ | Dimensionless embedding parameter that fixes the electric charge operator, $Q = T^3 + \beta T^8 + X$. The value $1/\sqrt3$ is the choice that gives exotic quarks of SM-like charge $(-1/3,-1/3,+2/3)$ — exactly the `DQ`, `SQ`, `TQ` charges. |
| `gX` $g_X$ | 0.5 | $M_{Z'}$ formula; `InteractionOrder {NP,1}` | Gauge coupling of the extra abelian factor $U(1)_X$ that the extended group contains. |
| `v1` $v_1$ | 173.95 GeV | $M_{V'}$, $M_{H_2}$, $M_{H_0}$, $M_{H^\pm}$, $M_{H_{QY}}$, $M_{H_{QV}}$; defines $v_2$ | First electroweak vacuum expectation value (VEV). |
| `v3` $v_3$ | 2000 GeV | $M_{Z'}$, $M_{Y'}$, $M_{V'}$, $f$, all heavy scalar masses | Large VEV that breaks the extended gauge group down to the SM. It sets the new-physics scale. |
| `k` $k$ | 1.0 | $f = k\,v_3$ | Dimensionless ratio that fixes the trilinear scalar coupling in units of $v_3$. |
| `lam3` $\lambda_3$ | 0.1 | $M_{H_3}^2 = 2\lambda_3 v_3^2$; `{NP,1}` | Quartic self-coupling of the scalar multiplet whose VEV is $v_3$. |
| `lampr12` $\lambda'_{12}$ | 0.1 | $M_{H^\pm}$ formula, term $\lambda'_{12} v_1 v_2$; `{NP,1}` | Cross-quartic coupling between scalar multiplets 1 and 2. |
| `lampr23` $\lambda'_{23}$ | 0.1 | $M_{H_{QY}}$ formula, term $\lambda'_{23} v_2 v_3$; `{NP,1}` | Cross-quartic coupling between scalar multiplets 2 and 3. |
| `lampr13` $\lambda'_{13}$ | 0.1 | $M_{H_{QV}}$ formula, term $\lambda'_{13} v_1 v_3$; `{NP,1}` | Cross-quartic coupling between scalar multiplets 1 and 3. |

### Internal (derived) parameters

| Symbol | Definition | Meaning |
|---|---|---|
| `v2` $v_2$ | $\sqrt{v_{\rm SM}^2 - v_1^2}$ | Second electroweak VEV, fixed so that $v_1^2 + v_2^2 = v_{\rm SM}^2$. With $v_1 = 173.95$ this gives $v_2 \approx 174.3$ GeV, i.e. $\tan\beta_{12} = v_2/v_1 \approx 1$. |
| `f` | $k\,v_3$ | Dimensionful trilinear scalar coupling (mass dimension 1) that couples the three scalar multiplets. It sets the mass of the heavy CP-odd and charged states. |
| `MZp` | $\sqrt{(g^2+\beta^2 g_X^2)\,v_3^2/6}$ | Mass of $Z'$. |
| `MYp` | $\sqrt{g^2 (v_3^2+v_2^2)/4}$ | Mass of $Y'^{\pm}$. |
| `MVp` | $\sqrt{g^2 (v_3^2+v_1^2)/4}$ | Mass of $V'$. |
| `MH2` | $\sqrt{(v_{\rm SM}^2/(v_1 v_2))\,f\,v_3}$ | Mass of $H_2$. |
| `MH3` | $\sqrt{2\lambda_3 v_3^2}$ | Mass of $H_3$ (the state from the $v_3$ multiplet). |
| `MH0` | $\sqrt{(v_1 v_2/v_3 + v_1 v_3/v_2 + v_2 v_3/v_1)\,f}$ | Mass of the CP-odd neutral $H_0$; the typical $f$-driven pseudoscalar mass formula. |
| `MHpm` | $\sqrt{(2 f v_3 + \lambda'_{12} v_1 v_2)\,v_{\rm SM}^2/(2 v_1 v_2)}$ | Mass of $H^\pm$. |
| `MHQY` | $\sqrt{(2 f v_1 + \lambda'_{23} v_2 v_3)(v_2^2+v_3^2)/(2 v_2 v_3)}$ | Mass of $H_{QY}^\pm$. |
| `MHQV` | $\sqrt{(2 f v_2 + \lambda'_{13} v_1 v_3)(v_1^2+v_3^2)/(2 v_1 v_3)}$ | Mass of $H_{QV}$. |

Numerical values follow once the SM inputs are supplied. With the usual
$v_{\rm SM} = 246.22$ GeV and $g = g_w \simeq 0.652$ the file gives approximately:
$M_{Z'} \approx 0.58$ TeV, $M_{Y'} \approx M_{V'} \approx 0.65$ TeV,
$M_{H_3} \approx 0.89$ TeV, $M_{H_{QY}} \approx M_{H_{QV}} \approx 2.06$ TeV,
$M_{H_2} \approx M_{H_0} \approx M_{H^\pm} \approx 2.83$ TeV.

`M$InteractionOrderHierarchy = {{QCD,1},{QED,2},{NP,1}}` declares a new coupling order `NP`
for the new-physics couplings ($g_X$, $\lambda_3$, $\lambda'_{ij}$).

---

## 4. Physics summary

This is a 3-3-1 type extension of the SM: the charge operator parameter
$\beta = 1/\sqrt3$, the single large VEV $v_3$ that sits above two electroweak VEVs
$v_1, v_2$, and the particle list (one extra neutral gauge boson $Z'$, one singly charged
gauge boson $Y'^\pm$, one complex *neutral* gauge boson $V'$, two exotic $-1/3$ quarks
$D, S$, one exotic $+2/3$ quark $T$, three heavy neutral leptons, and a three-multiplet
scalar sector giving two extra charged scalars, one complex neutral scalar and three real
neutral scalars) all match the pattern of an $SU(3)_c\times SU(3)_L\times U(1)_X$ model of
the type with neutral leptons in the third component of the lepton triplet. The file itself
implements only the free (kinetic and mass) Lagrangian for every new state, plus one
interaction block: charged-current-like couplings of strength $g/\sqrt2$ that join each
exotic quark to a SM quark and one heavy vector, $u\,D\,Y'$, $c\,S\,Y'$, $d\,D\,V'$ and
$s\,S\,V'$.

Processes it mediates: single and pair production of the exotic quarks $D$ and $S$ at
hadron colliders through $s$-channel and $t$-channel $Y'$ and $V'$ exchange, decays such as
$D \to u\,Y'^-$, $D \to d\,V'$, $S \to c\,Y'^-$, $S \to s\,V'$ (or the reverse order when
the vector is heavier), and new flavour-changing four-quark contact interactions from
$Y'$/$V'$ exchange between the first two generations, which feed $D^0$ and $K$ meson
mixing. Everything else in the file is inert: $Z'$, $T$, the three heavy leptons and all
six new scalars have no couplings at all beyond their gauge (photon, $Z$, gluon) couplings
from `DC`, so they cannot be produced through any new vertex in this file.

Two internal problems are worth flagging to whoever uses this file:

1. **Non-hermitian $u$–$D$–$Y'$ coupling.** In `LNPcc` the direct term is
   $\bar u\gamma^\mu P_R D\,Y'_\mu$ while its conjugate partner is
   $\bar D\gamma^\mu P_L u\,Y'^\dagger_\mu$. These are not hermitian conjugates of each
   other, and this single right-handed current breaks the left-handed ($V-A$) pattern that
   the other three currents follow. This points to a chirality projector that was swapped
   in one place only.
2. **$Y'^\pm$ has no photon coupling.** `LYp` uses `FS[Yp,mu,nu]` (plain curl) and not a
   covariant field strength, so the charged vector is not electromagnetically gauge
   invariant as written. The same applies to the mass terms of all three heavy vectors,
   which are put in by hand rather than generated by a Higgs mechanism.
