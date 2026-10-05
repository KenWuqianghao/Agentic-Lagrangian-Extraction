# Reconstruction of `sanitized.fr`

## 0. Conventions and gauge content

The file declares **no new gauge group**. It only adds parameters, particle classes and
Lagrangian pieces, so every FeynRules `DC[...]` in this file is built from the gauge groups of
the host (Standard Model) model file that this file is loaded on top of:

$$SU(3)_C \times SU(2)_L \times U(1)_Y ,$$

with coupling constants $g_s$ (`gs`), $g_w$ (`gw`) and $g_1$ (`g1`), generators $T^a$
(`Index[Colour]`) and $T^i = \sigma^i/2$ (`Index[SU2D]`), and hypercharge read from the
`QuantumNumbers -> {Y -> ...}` entry.

**None of the new fields carries an `SU2D` / isospin index.** Every new field is therefore an
$SU(2)_L$ singlet, and the covariant derivative acting on a new field $\Phi$ reduces to

$$D_\mu \Phi \;=\; \Big( \partial_\mu \;-\; i\,g_s\, G^a_\mu\, T^a \;-\; i\,g_1\, Y_\Phi\, B_\mu \Big)\Phi ,$$

where the $SU(3)_C$ piece is present only for the colour-triplet fields `DQ`, `SQ`, `TQ`.
Because these states have $T^3 = 0$, their declared $Y$ equals their electric charge $Q$, and
after electroweak symmetry breaking ($B_\mu = c_W A_\mu - s_W Z_\mu$, $e = g_1 c_W$) the abelian
part becomes

$$-\,i g_1 Y_\Phi B_\mu \;=\; -\,i e\, Q_\Phi A_\mu \;+\; i e\, Q_\Phi \tan\theta_W\, Z_\mu .$$

For fields with $Y=0$ and no colour index (`EL`, `HQV`) the covariant derivative degenerates to
the ordinary derivative, $D_\mu = \partial_\mu$.

`FS[V,mu,nu]` for a vector that is **not** the gauge field of a declared group is the abelian
field strength

$$F^{V}_{\mu\nu} \;=\; \partial_\mu V_\nu - \partial_\nu V_\mu ,$$

i.e. the charged vectors `Yp` (and the complex neutral `Vp`) are written with a *free* Proca
field strength, **not** a $U(1)_{\rm em}$-covariant one. Repeated Lorentz indices in the `.fr`
source denote contraction with $\eta_{\mu\nu}$. `Xbar` denotes $X^\dagger$ for bosons and
$\bar\psi = \psi^\dagger \gamma^0$ for fermions; `Ga[mu]` is $\gamma^\mu$.

Interaction-order hierarchy: `{{QCD,1},{QED,2},{NP,1}}`.

---

## 1. Lagrangian, term by term

### `LZp` — real (self-conjugate) neutral vector $Z'$

$$\mathcal{L}_{Z'} \;=\; -\frac{1}{4}\, F^{Z'}_{\mu\nu} F^{Z'\,\mu\nu} \;+\; \frac{1}{2}\, M_{Z'}^{2}\, Z'_\mu Z'^{\mu},
\qquad F^{Z'}_{\mu\nu} = \partial_\mu Z'_\nu - \partial_\nu Z'_\mu .$$

A Proca Lagrangian for a self-conjugate, colour- and charge-neutral spin-1 field.

### `LYp` — complex charged vector $Y^{\pm}$ ($Q=+1$)

$$\mathcal{L}_{Y'} \;=\; -\frac{1}{2}\, F^{Y'\,\dagger}_{\mu\nu} F^{Y'\,\mu\nu} \;+\; M_{Y'}^{2}\, Y'^{\dagger}_\mu Y'^{\mu},
\qquad F^{Y'}_{\mu\nu} = \partial_\mu Y'_\nu - \partial_\nu Y'_\mu .$$

Note the normalisation $-\tfrac12$ (not $-\tfrac14$) and $M^2$ (not $\tfrac12 M^2$), which is the
correct convention for a complex vector. **The derivative here is ordinary, not covariant**, so
as written this charged vector has *no* photon coupling.

### `LVp` — complex neutral vector $V^{0}$ ($Q=0$, not self-conjugate)

$$\mathcal{L}_{V'} \;=\; -\frac{1}{2}\, F^{V'\,\dagger}_{\mu\nu} F^{V'\,\mu\nu} \;+\; M_{V'}^{2}\, V'^{\dagger}_\mu V'^{\mu},
\qquad F^{V'}_{\mu\nu} = \partial_\mu V'_\nu - \partial_\nu V'_\mu .$$

A complex (particle $\ne$ antiparticle) but electrically neutral massive vector.

### `LDQ` — exotic down-type quark $D$ ($Q=-1/3$, colour triplet)

$$\mathcal{L}_{D} \;=\; i\, \bar{D}\, \gamma^\mu D_\mu D \;-\; M_{D}\, \bar{D} D ,
\qquad D_\mu D = \Big(\partial_\mu - i g_s G^a_\mu T^a - i g_1 \big(-\tfrac13\big) B_\mu\Big) D .$$

Vector-like (**non-chiral**) Dirac mass: no `ProjP`/`ProjM` appears anywhere in the file, so the
left- and right-handed components carry identical quantum numbers.

### `LSQ` — exotic down-type quark $S$ ($Q=-1/3$, colour triplet)

$$\mathcal{L}_{S} \;=\; i\, \bar{S}\, \gamma^\mu D_\mu S \;-\; M_{S}\, \bar{S} S ,
\qquad D_\mu S = \Big(\partial_\mu - i g_s G^a_\mu T^a + \tfrac{i}{3} g_1 B_\mu\Big) S .$$

### `LTQ` — exotic up-type quark $T$ ($Q=+2/3$, colour triplet)

$$\mathcal{L}_{T} \;=\; i\, \bar{T}\, \gamma^\mu D_\mu T \;-\; M_{T}\, \bar{T} T ,
\qquad D_\mu T = \Big(\partial_\mu - i g_s G^a_\mu T^a - \tfrac{2i}{3} g_1 B_\mu\Big) T .$$

### `LEL` — three heavy neutral leptons $E_{e},E_{\mu},E_{\tau}$

$$\mathcal{L}_{E} \;=\; i\, \bar{E}_a\, \gamma^\mu \partial_\mu E_a \;-\; M_{E_e}\bar{E}_e E_e \;-\; M_{E_\mu}\bar{E}_\mu E_\mu \;-\; M_{E_\tau}\bar{E}_\tau E_\tau ,\qquad a = e,\mu,\tau .$$

The generation index $a$ is summed in the kinetic term (FeynRules contracts the repeated
`Generation` index automatically). Because `EL` is declared with $Q=0$, $Y=0$ and **no** colour
index, `DC[EL,mu]` collapses to $\partial_\mu$. The mass term is written **member by member**
with the numeric entries $M_{EE},M_{EM},M_{ET}$ rather than through the class symbol `MEL`, so it
is diagonal in flavour by construction.

*Internal inconsistency worth flagging:* the `FullName` strings call these "heavy **charged**
leptons", but the declared quantum numbers are $Q=0$, $Y=0$. The quantum numbers are what the
Feynman rules will use, so these are heavy **neutral** leptons (heavy-neutrino-like states).

### `LH2` — real scalar $H_2$

$$\mathcal{L}_{H_2} \;=\; \frac{1}{2}\, \partial_\mu H_2\, \partial^\mu H_2 \;-\; \frac{1}{2}\, M_{H_2}^{2}\, H_2^{2} .$$

### `LH3` — real scalar $H_3$

$$\mathcal{L}_{H_3} \;=\; \frac{1}{2}\, \partial_\mu H_3\, \partial^\mu H_3 \;-\; \frac{1}{2}\, M_{H_3}^{2}\, H_3^{2} .$$

### `LH0` — real scalar $H_0$

$$\mathcal{L}_{H_0} \;=\; \frac{1}{2}\, \partial_\mu H_0\, \partial^\mu H_0 \;-\; \frac{1}{2}\, M_{H_0}^{2}\, H_0^{2} .$$

All three use `del` (plain derivative), consistent with `SelfConjugate -> True` and $Q=0$.

### `LHpm` — charged scalar $H^{\pm}$ ($Q=+1$, $Y=+1$)

$$\mathcal{L}_{H^\pm} \;=\; \big(D_\mu H^{+}\big)^{\dagger} \big(D^\mu H^{+}\big) \;-\; M_{H^\pm}^{2}\, H^{-} H^{+},
\qquad D_\mu H^{+} = \big(\partial_\mu - i g_1 B_\mu\big) H^{+} .$$

Here `DC[Hpmbar,mu]` is exactly $(D_\mu H^{+})^{\dagger}$ (the covariant derivative of the
conjugate field, i.e. with the opposite charge). After EWSB this gives the standard
$\gamma H^{+} H^{-}$ and $Z H^{+} H^{-}$ vertices with $e\,Q = e$ and $-e\tan\theta_W$
respectively.

### `LHQY` — charged scalar $H^{\pm}_{QY}$ ($Q=+1$, $Y=+1$)

$$\mathcal{L}_{H_{QY}} \;=\; \big(D_\mu H_{QY}^{+}\big)^{\dagger} \big(D^\mu H_{QY}^{+}\big) \;-\; M_{H_{QY}}^{2}\, H_{QY}^{-} H_{QY}^{+},
\qquad D_\mu H_{QY}^{+} = \big(\partial_\mu - i g_1 B_\mu\big) H_{QY}^{+} .$$

A second, independent singly-charged scalar with the same electroweak couplings as $H^\pm$.

### `LHQV` — complex neutral scalar $H_{QV}$ ($Q=0$, $Y=0$)

$$\mathcal{L}_{H_{QV}} \;=\; \partial_\mu H_{QV}^{\dagger}\, \partial^\mu H_{QV} \;-\; M_{H_{QV}}^{2}\, H_{QV}^{\dagger} H_{QV} .$$

`DC` degenerates to $\partial_\mu$ because $Q=Y=0$ and there is no colour index; the field is
nevertheless complex (`SelfConjugate -> False`), so particle and antiparticle are distinct.

### `LTotal` — total

$$\mathcal{L}_{\rm total} \;=\; \mathcal{L}_{Z'} + \mathcal{L}_{Y'} + \mathcal{L}_{V'} + \mathcal{L}_{D} + \mathcal{L}_{S} + \mathcal{L}_{T} + \mathcal{L}_{E} + \mathcal{L}_{H_2} + \mathcal{L}_{H_3} + \mathcal{L}_{H_0} + \mathcal{L}_{H^\pm} + \mathcal{L}_{H_{QY}} + \mathcal{L}_{H_{QV}} .$$

**Important structural observation.** Every one of the thirteen pieces is a *kinetic + mass* term
only. There is no Yukawa sector, no scalar potential (no cubic or quartic scalar terms), no
gauge self-interaction among $Z',Y',V'$, and no current coupling the new vectors to any fermion.
Consequently, apart from the QCD and QED/$Z$ couplings that `DC` generates automatically for the
coloured and electrically charged states, **the new sector is completely decoupled from the
Standard Model and from itself.** The parameters `gX`, `beta`, `k`, `lam3`, `lampr12`, `lampr23`,
`lampr13`, `v1`, `v2`, `v3` appear *only* inside internal mass formulas and never multiply a
field operator. A physically complete model of this type would contain the corresponding
interaction terms; they are absent from this file.

---

## 2. Field table

Spin is read from the class prefix (`V[...]` $=1$, `F[...]` $=1/2$, `S[...]` $=0$).
No field carries an `SU2D`/isospin index, so all are $SU(2)_L$ singlets.
Colour rep is $\mathbf{3}$ when `Indices -> {Index[Colour]}` is declared, $\mathbf{1}$ otherwise.

| `.fr` class | Symbol | Spin | $SU(3)_C$ | $SU(2)_L$ | $Q$ | $Y$ | Self-conj.? | Mass symbol | Mass value | Width | PDG |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `V[101]` `Zp` | $Z'$ | 1 | $\mathbf{1}$ | $\mathbf{1}$ | 0 | — | **yes** | `MZp` | internal: $\sqrt{(g_w^2+\beta^2 g_X^2)v_3^2/6}$ | `WZp` $=1$ | 4000001 |
| `V[102]` `Yp` | $Y^{\pm}$ | 1 | $\mathbf{1}$ | $\mathbf{1}$ | $+1$ | — | no | `MYp` | internal: $\sqrt{g_w^2 (v_3^2+v_2^2)/4}$ | `WYp` $=1$ | 4000002 |
| `V[103]` `Vp` | $V^{0}$ | 1 | $\mathbf{1}$ | $\mathbf{1}$ | 0 | — | no | `MVp` | internal: $\sqrt{g_w^2 (v_3^2+v_1^2)/4}$ | `WVp` $=1$ | 4000003 |
| `F[101]` `DQ` | $D$ | 1/2 | $\mathbf{3}$ | $\mathbf{1}$ | $-1/3$ | $-1/3$ | no | `MDQ` | 1000 GeV | `WDQ` $=1$ | 4000004 |
| `F[102]` `SQ` | $S$ | 1/2 | $\mathbf{3}$ | $\mathbf{1}$ | $-1/3$ | $-1/3$ | no | `MSQ` | 1000 GeV | `WSQ` $=1$ | 4000005 |
| `F[103]` `TQ` | $T$ | 1/2 | $\mathbf{3}$ | $\mathbf{1}$ | $+2/3$ | $+2/3$ | no | `MTQ` | 1000 GeV | `WTQ` $=1$ | 4000006 |
| `F[104]` `EL` | $E_e,E_\mu,E_\tau$ (3 gen.) | 1/2 | $\mathbf{1}$ | $\mathbf{1}$ | 0 | 0 | no | `MEL` $\to$ `MEE`,`MEM`,`MET` | 1000 GeV each | `WEE`,`WEM`,`WET` $=1$ | 4000007–9 |
| `S[101]` `H2` | $H_2$ | 0 | $\mathbf{1}$ | $\mathbf{1}$ | 0 | — | **yes** | `MH2` | internal: $\sqrt{\dfrac{v^2}{v_1 v_2} f v_3}$ | `WH2` $=1$ | 4000010 |
| `S[102]` `H3` | $H_3$ | 0 | $\mathbf{1}$ | $\mathbf{1}$ | 0 | — | **yes** | `MH3` | internal: $\sqrt{2\lambda_3 v_3^2}$ | `WH3` $=1$ | 4000011 |
| `S[103]` `H0` | $H_0$ | 0 | $\mathbf{1}$ | $\mathbf{1}$ | 0 | — | **yes** | `MH0` | internal: $\sqrt{\Big(\tfrac{v_1 v_2}{v_3}+\tfrac{v_1 v_3}{v_2}+\tfrac{v_2 v_3}{v_1}\Big) f}$ | `WH0` $=1$ | 4000012 |
| `S[104]` `Hpm` | $H^{\pm}$ | 0 | $\mathbf{1}$ | $\mathbf{1}$ | $+1$ | $+1$ | no | `MHpm` | internal: $\sqrt{\dfrac{(2 f v_3 + \lambda'_{12} v_1 v_2)\,v^2}{2 v_1 v_2}}$ | `WHpm` $=1$ | 4000013 |
| `S[105]` `HQY` | $H^{\pm}_{QY}$ | 0 | $\mathbf{1}$ | $\mathbf{1}$ | $+1$ | $+1$ | no | `MHQY` | internal: $\sqrt{\dfrac{(2 f v_1 + \lambda'_{23} v_2 v_3)(v_2^2+v_3^2)}{2 v_2 v_3}}$ | `WHQY` $=1$ | 4000014 |
| `S[106]` `HQV` | $H_{QV}$ | 0 | $\mathbf{1}$ | $\mathbf{1}$ | 0 | 0 | no | `MHQV` | internal: $\sqrt{\dfrac{(2 f v_2 + \lambda'_{13} v_1 v_3)(v_1^2+v_3^2)}{2 v_1 v_3}}$ | `WHQV` $=1$ | 4000015 |

Notes:

* The vectors `Zp`, `Yp`, `Vp` declare no `Y`; `Yp` and `Vp` declare $Q$ explicitly ($+1$ and $0$).
  Since their kinetic terms use `FS` rather than `DC`, the declared $Q$ is used for charge-flow
  bookkeeping only and generates no gauge vertex in this file.
* All three exotic quarks are **vector-like Dirac** fields: a bare Dirac mass is written directly,
  and no chiral projector appears anywhere in the file.
* `EL` is a three-member flavour class with `FlavorIndex -> Generation`; the mass is diagonal.
* Numerical PDG codes run 4000001–4000015 (the standard BSM block).

---

## 3. External parameters

| Symbol | Value | Block / order | Where it enters | Physical meaning |
|---|---|---|---|---|
| `beta` $\beta$ | $0.5773502691896258 = 1/\sqrt{3}$ | `NPINPUTS` 1 | $M_{Z'}^2 = (g_w^2+\beta^2 g_X^2)v_3^2/6$ | Dimensionless embedding parameter of the extra $U(1)$ inside the enlarged electroweak group; it fixes the electric-charge operator $Q = T^3 + \beta T^8 + X$. The value $1/\sqrt3$ is the choice that keeps all exotic charges within $\{-1/3,+2/3,\pm1,0\}$ (no exotic-charge states). |
| `gX` $g_X$ | $0.5$ | `NPINPUTS` 2, `{NP,1}` | $M_{Z'}$ | Gauge coupling of the extra abelian factor $U(1)_X$. Carries NP interaction order 1. |
| `v1` $v_1$ | $173.95$ GeV | `NPINPUTS` 3 | $M_{Y'}$, $M_{V'}$, $M_{H_2}$, $M_{H_0}$, $M_{H^\pm}$, $M_{H_{QY}}$, $M_{H_{QV}}$, and $v_2$ | First electroweak-scale vacuum expectation value (one of two EW doublet-like VEVs). |
| `v3` $v_3$ | $2000$ GeV | `NPINPUTS` 4 | $M_{Z'}$, $M_{Y'}$, $M_{V'}$, $f$, all scalar masses | VEV of the high-scale direction; it sets the breaking scale of the extended gauge group down to the SM, and hence the overall mass of $Z'$, $Y^\pm$, $V^0$. |
| `k` $k$ | $1$ | `NPINPUTS` 5 | $f = k\,v_3$ | Dimensionless ratio defining the trilinear scalar coupling $f$ (mass dimension 1) in units of $v_3$. |
| `lam3` $\lambda_3$ | $0.1$ | `NPINPUTS` 6, `{NP,1}` | $M_{H_3}^2 = 2\lambda_3 v_3^2$ | Quartic self-coupling of the high-scale scalar multiplet; sets the mass of the heavy CP-even scalar $H_3$. |
| `lampr12` $\lambda'_{12}$ | $0.1$ | `NPINPUTS` 7, `{NP,1}` | $M_{H^\pm}^2$ | Quartic cross-coupling between scalar multiplets 1 and 2; contributes to the mass splitting of the $H^\pm$ state built from that pair. |
| `lampr23` $\lambda'_{23}$ | $0.1$ | `NPINPUTS` 8, `{NP,1}` | $M_{H_{QY}}^2$ | Quartic cross-coupling between multiplets 2 and 3; sets the $H^{\pm}_{QY}$ mass. |
| `lampr13` $\lambda'_{13}$ | $0.1$ | `NPINPUTS` 9, `{NP,1}` | $M_{H_{QV}}^2$ | Quartic cross-coupling between multiplets 1 and 3; sets the neutral complex $H_{QV}$ mass. |

Additional numeric masses declared inside the particle classes (external in practice, taken from
the `Mass -> {..., value}` entries): $M_{DQ}=M_{SQ}=M_{TQ}=1000$ GeV and
$M_{EE}=M_{EM}=M_{ET}=1000$ GeV. All widths are initialised to $1$ GeV.

### Internal (derived) parameters

| Symbol | Definition | Meaning |
|---|---|---|
| `v2` $v_2$ | $\sqrt{v^2 - v_1^2}$ | Second electroweak VEV, fixed so that $v_1^2+v_2^2 = v^2$ equals the SM VEV `vev` (constraint from $M_W$). With $v_1 = 173.95$ GeV this gives $v_2 \simeq v_1$, i.e. $\tan\beta' \simeq 1$. |
| `f` | $k\, v_3$ | Trilinear (dimension-one) scalar coupling of the three scalar multiplets; it is the source of the mass of the pseudo-Goldstone-like states $H_2$, $H_0$ and of the charged/neutral scalars. |
| `MZp` | $\sqrt{(g_w^2+\beta^2 g_X^2)\,v_3^2/6}$ | Neutral heavy gauge-boson mass. |
| `MYp` | $\sqrt{g_w^2 (v_3^2+v_2^2)/4}$ | Charged heavy gauge-boson mass. |
| `MVp` | $\sqrt{g_w^2 (v_3^2+v_1^2)/4}$ | Neutral complex heavy gauge-boson mass. |
| `MH2`, `MH3`, `MH0`, `MHpm`, `MHQY`, `MHQV` | see field table | Physical scalar masses from diagonalising the (not-included) scalar potential. |

$g_w$ (`gw`) and `vev` are **not** declared here; they are inherited from the host SM model file.

---

## 4. Physics summary

This is a **331-type extension** of the Standard Model: the electroweak group is enlarged to
$SU(3)_L \times U(1)_X$, broken at $v_3 = 2$ TeV down to $SU(2)_L\times U(1)_Y$ by a third VEV,
with the remaining two VEVs $v_1, v_2$ satisfying $v_1^2+v_2^2 = v_{\rm SM}^2$. The embedding
parameter is $\beta = 1/\sqrt3$, the "331 with neutral heavy leptons / right-handed-neutrino-like"
variant: the five extra gauge bosons form a neutral $Z'$ plus a complex pair $(Y^{\pm}, V^{0})$
with charges $\pm1$ and $0$, and the exotic quarks carry ordinary SM-like charges $-1/3$ (two of
them, $D$ and $S$) and $+2/3$ (one, $T$), accompanied by three heavy neutral leptons
$E_{e,\mu,\tau}$. The three scalar triplets leave a spectrum of three real neutral scalars
($H_0, H_2, H_3$), two singly-charged scalars ($H^{\pm}, H^{\pm}_{QY}$) and one complex neutral
scalar ($H_{QV}$).

Physically such a model mediates flavour-changing neutral currents through tree-level $Z'$
exchange, single and pair production of the vector-like quarks $D,S,T$ at a hadron collider
(QCD pair production, plus $Y^\pm / V^0$-mediated transitions into SM quarks), bilepton-like
$Y^{\pm}, V^{0}$ exchange connecting leptons to the heavy neutral leptons, and $Z' \to$ dilepton
resonance signals.

**Caveat on this particular file.** As written, `LTotal` contains **only** free kinetic and mass
terms. There are no gauge-boson self-interactions, no fermion currents for $Z'$, $Y^\pm$, $V^0$,
no Yukawa couplings for the exotic quarks or heavy leptons, and no scalar potential. The 331
structure therefore survives only in the *mass formulas* (through $\beta$, $g_X$, $v_3$, $f$,
$\lambda_3$, $\lambda'_{ij}$), not in any vertex. Every new-physics parameter carrying
`InteractionOrder -> {NP,1}` multiplies nothing. The only vertices this file generates are the
automatic QCD and QED/$Z$ couplings of the coloured states $D,S,T$ and of the charged scalars
$H^\pm, H^\pm_{QY}$; the states $Z'$, $Y^\pm$, $V^0$, $E_{e,\mu,\tau}$, $H_0$, $H_2$, $H_3$ and
$H_{QV}$ are completely sterile and would be stable and unproducible. The interaction sector
appears to be missing.
