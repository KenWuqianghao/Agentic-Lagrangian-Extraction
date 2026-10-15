# Reconstruction of `sanitized.fr`

All metadata was removed from the file. The reconstruction below uses only the
declarations, the parameter formulas and the Lagrangian terms in the file.

## 0. Conventions and what is inherited from the base model

The file declares no gauge group and no Standard Model (SM) field. It uses
`gw`, `vev`, `u`, `d`, `c`, `s` and the operators `DC`, `FS`, `Ga`, `ProjM`,
`HC`, `del`. So this file is an add-on that is loaded together with the SM
FeynRules model. From the SM base model come:

* the gauge group $SU(3)_c \times SU(2)_L \times U(1)_Y$, broken to
  $SU(3)_c \times U(1)_{em}$,
* $g_s$, $g_w$, $e$, $s_W$, $c_W$, $v \equiv$ `vev`,
* the quark fields $u, d, c, s$.

`ProjM` $= (1-\gamma_5)/2 = P_L$ and `ProjP` $= (1+\gamma_5)/2 = P_R$.

**Covariant derivative `DC`.** No new field carries an `SU2W` index. Every new
coloured field carries only `Index[Colour]` (the fundamental $\mathbf{3}$ of
$SU(3)_c$). So for each new field $\Phi$ with weak isospin $T^3 = 0$, declared
hypercharge $Y$ and colour rep $R$:

$$
D_\mu \Phi \;=\; \Big(\partial_\mu \;-\; i\,g_s\,G^a_\mu\,T^a_{(R)} \;-\; i\,e\,Y\,A_\mu \;+\; i\,e\,\frac{s_W}{c_W}\,Y\,Z_\mu\Big)\Phi ,
$$

with the $SU(3)_c$ term present only for the coloured fields (`DQ`, `SQ`, `TQ`)
and absent for the colour-singlet scalars and leptons. This follows from
$D_\mu = \partial_\mu - i g_s G^a T^a - i g_1 Y B_\mu$ with $g_1 = e/c_W$ and
$B_\mu = c_W A_\mu - s_W Z_\mu$.

**Important:** the new gauge bosons $Z'$, $Y'$, $V'$ are **not** part of `DC`.
They are declared as plain vector fields, and `FS[Zp,mu,nu]` etc. are the
abelian field strengths $\partial_\mu A_\nu - \partial_\nu A_\mu$. So in this
file the new vectors have no gauge self-interactions and no photon coupling,
even for the electrically charged $Y'^\pm$. Their only interactions are the
explicit ones in `LNPcc`.

---

## 1. Lagrangian

### `LZp` — neutral heavy vector

$$
\mathcal{L}_{Z'} \;=\; -\tfrac{1}{4}\,Z'_{\mu\nu}Z'^{\,\mu\nu} \;+\; \tfrac{1}{2}M_{Z'}^{2}\,Z'_\mu Z'^{\mu},
\qquad Z'_{\mu\nu} = \partial_\mu Z'_\nu - \partial_\nu Z'_\mu .
$$

Real (self-conjugate) Proca field. It has no coupling to anything in this file.

### `LYp` — singly charged heavy vector

$$
\mathcal{L}_{Y'} \;=\; -\tfrac{1}{2}\,Y'^{\dagger}_{\mu\nu}Y'^{\,\mu\nu} \;+\; M_{Y'}^{2}\,Y'^{\dagger}_\mu Y'^{\mu},
\qquad Y'_{\mu\nu} = \partial_\mu Y'_\nu - \partial_\nu Y'_\mu .
$$

Complex Proca field, $Q(Y') = +1$. The field strength is the ordinary curl, so
$Y'^\pm$ carries no electromagnetic coupling here.

### `LVp` — neutral complex heavy vector

$$
\mathcal{L}_{V'} \;=\; -\tfrac{1}{2}\,V'^{\dagger}_{\mu\nu}V'^{\,\mu\nu} \;+\; M_{V'}^{2}\,V'^{\dagger}_\mu V'^{\mu},
\qquad V'_{\mu\nu} = \partial_\mu V'_\nu - \partial_\nu V'_\mu .
$$

$Q(V') = 0$ but the field is **not** self-conjugate: a complex neutral vector
(a bilepton-type $X^0$).

### `LDQ` — exotic quark $D$

$$
\mathcal{L}_{D} \;=\; i\,\bar{D}\,\gamma^{\mu}D_\mu D \;-\; M_{D}\,\bar{D}D ,
\qquad
D_\mu D = \Big(\partial_\mu - i g_s G^a_\mu T^a - i e Y_D A_\mu + i e \tfrac{s_W}{c_W} Y_D Z_\mu\Big) D .
$$

Colour triplet, Dirac field, vector-like mass term (no chiral projector), so
$D_L$ and $D_R$ have the same charges.

### `LSQ` — exotic quark $S$

$$
\mathcal{L}_{S} \;=\; i\,\bar{S}\,\gamma^{\mu}D_\mu S \;-\; M_{S}\,\bar{S}S ,
\qquad Y_S = -\tfrac{1}{3}.
$$

### `LTQ` — exotic quark $T$

$$
\mathcal{L}_{T} \;=\; i\,\bar{T}\,\gamma^{\mu}D_\mu T \;-\; M_{T}\,\bar{T}T ,
\qquad Y_T = +\tfrac{2}{3}.
$$

### `LEL` — three heavy leptons

$$
\mathcal{L}_{E} \;=\; i\,\bar{E}_i\,\gamma^{\mu}D_\mu E_i \;-\; M_{E_e}\,\bar{E}_e E_e \;-\; M_{E_\mu}\,\bar{E}_\mu E_\mu \;-\; M_{E_\tau}\,\bar{E}_\tau E_\tau ,
\qquad i = e,\mu,\tau .
$$

They carry $Q = Y = 0$ and no colour, so $D_\mu \to \partial_\mu$: in this file
they are free Dirac fields. The mass term is written member by member, so the
three masses are independent. The mass term is vector-like (no projector).

### `LH2`, `LH3`, `LH0` — three real neutral scalars

$$
\mathcal{L}_{H_2} \;=\; \tfrac{1}{2}\,\partial_\mu H_2\,\partial^{\mu}H_2 \;-\; \tfrac{1}{2}M_{H_2}^{2}H_2^{2},
$$

$$
\mathcal{L}_{H_3} \;=\; \tfrac{1}{2}\,\partial_\mu H_3\,\partial^{\mu}H_3 \;-\; \tfrac{1}{2}M_{H_3}^{2}H_3^{2},
$$

$$
\mathcal{L}_{H_0} \;=\; \tfrac{1}{2}\,\partial_\mu H_0\,\partial^{\mu}H_0 \;-\; \tfrac{1}{2}M_{H_0}^{2}H_0^{2}.
$$

Note the ordinary derivative `del`, not `DC`: these are neutral and free.

### `LHpm` — charged scalar

$$
\mathcal{L}_{H^\pm} \;=\; \big(D_\mu H^{+}\big)^{\dagger}\big(D^{\mu}H^{+}\big) \;-\; M_{H^\pm}^{2}\,H^{-}H^{+},
$$

$$
D_\mu H^{+} = \Big(\partial_\mu - i e A_\mu + i e \tfrac{s_W}{c_W} Z_\mu\Big)H^{+}\qquad (Q = Y = 1).
$$

### `LHQY` — charged scalar of the $Y$ sector

$$
\mathcal{L}_{H_{QY}} \;=\; \big(D_\mu H_{QY}\big)^{\dagger}\big(D^{\mu}H_{QY}\big) \;-\; M_{H_{QY}}^{2}\,H_{QY}^{\dagger}H_{QY},
\qquad Q = Y = 1 .
$$

### `LHQV` — neutral complex scalar of the $V$ sector

$$
\mathcal{L}_{H_{QV}} \;=\; \big(\partial_\mu H_{QV}\big)^{\dagger}\big(\partial^{\mu}H_{QV}\big) \;-\; M_{H_{QV}}^{2}\,H_{QV}^{\dagger}H_{QV},
\qquad Q = Y = 0 .
$$

`DC` is used in the file, but with $Q = Y = 0$ it reduces to $\partial_\mu$.

### `LNPcc` — new charged and neutral currents

$$
\mathcal{L}_{\rm NP}^{\rm cc} \;=\; \frac{g_w}{\sqrt{2}}\Big[\;
\bar{u}\,\gamma^{\mu}P_L\,D\;Y'_\mu
+ \bar{c}\,\gamma^{\mu}P_L\,S\;Y'_\mu
+ \bar{d}\,\gamma^{\mu}P_L\,D\;V'_\mu
+ \bar{s}\,\gamma^{\mu}P_L\,S\;V'_\mu \Big] \;+\; \text{h.c.}
$$

with the hermitian conjugate written out:

$$
\text{h.c.} \;=\; \frac{g_w}{\sqrt{2}}\Big[\;
\bar{D}\,\gamma^{\mu}P_L\,u\;Y'^{\dagger}_\mu
+ \bar{S}\,\gamma^{\mu}P_L\,c\;Y'^{\dagger}_\mu
+ \bar{D}\,\gamma^{\mu}P_L\,d\;V'^{\dagger}_\mu
+ \bar{S}\,\gamma^{\mu}P_L\,s\;V'^{\dagger}_\mu \Big].
$$

Points to check term by term:

* The current is purely left-handed (`ProjM` $= P_L$). There is no
  right-handed piece, although the exotic-quark mass terms are vector-like.
* Colour is contracted in the trivial way: $\bar{u}_i \gamma^\mu P_L D_i$ etc.
  (both fields are colour triplets, index summed).
* Charge flow: $-Q_u + Q_D + Q_{Y'} = -\tfrac{2}{3} - \tfrac{1}{3} + 1 = 0$;
  $-Q_c + Q_S + Q_{Y'} = 0$; $-Q_d + Q_D + Q_{V'} = \tfrac{1}{3} - \tfrac{1}{3} + 0 = 0$;
  $-Q_s + Q_S + Q_{V'} = 0$. All four terms conserve electric charge with
  $Q_D = Q_S = -1/3$.
* The coupling is the SM $SU(2)_L$ coupling $g_w/\sqrt{2}$, the same strength
  as the SM charged current.
* $T$ has **no** current term, and the third-generation quarks $t, b$ do not
  appear. $Z'$ has no current term either.

### `LTotal`

$$
\mathcal{L}_{\rm total} = \mathcal{L}_{Z'}+\mathcal{L}_{Y'}+\mathcal{L}_{V'}
+\mathcal{L}_{D}+\mathcal{L}_{S}+\mathcal{L}_{T}+\mathcal{L}_{E}
+\mathcal{L}_{H_2}+\mathcal{L}_{H_3}+\mathcal{L}_{H_0}
+\mathcal{L}_{H^\pm}+\mathcal{L}_{H_{QY}}+\mathcal{L}_{H_{QV}}
+\mathcal{L}_{\rm NP}^{\rm cc}.
$$

There is no scalar potential and no Yukawa term. All scalars are free fields
except for their gauge couplings through `DC`.

---

## 2. Field table

| Class | Symbol | FR class | Spin | $SU(3)_c$ | $SU(2)_L$ | $Q$ | $Y$ | Self-conj. | Mass symbol | Mass value |
|---|---|---|---|---|---|---|---|---|---|---|
| `Zp` | $Z'$ | V[101] | 1 | $\mathbf{1}$ | not declared | 0 | – | yes | `MZp` | internal, $\sqrt{(g_w^2+\beta^2 g_X^2)v_3^2/6}\approx 580$ GeV |
| `Yp` | $Y'^{\pm}$ | V[102] | 1 | $\mathbf{1}$ | not declared | $+1$ | – | no | `MYp` | internal, $\sqrt{g_w^2(v_3^2+v_2^2)/4}\approx 650$ GeV |
| `Vp` | $V'^{0}$ | V[103] | 1 | $\mathbf{1}$ | not declared | 0 | – | no | `MVp` | internal, $\sqrt{g_w^2(v_3^2+v_1^2)/4}\approx 650$ GeV |
| `DQ` | $D$ | F[101] | 1/2 | $\mathbf{3}$ | not declared | $-1/3$ | $+1/3$ (see note) | no | `MDQ` | 1000 GeV |
| `SQ` | $S$ | F[102] | 1/2 | $\mathbf{3}$ | not declared | $-1/3$ | $-1/3$ | no | `MSQ` | 1000 GeV |
| `TQ` | $T$ | F[103] | 1/2 | $\mathbf{3}$ | not declared | $+2/3$ | $+2/3$ | no | `MTQ` | 1000 GeV |
| `EL` | $E_e, E_\mu, E_\tau$ | F[104] | 1/2 | $\mathbf{1}$ | not declared | 0 | 0 | no | `MEL` (`MEE`,`MEM`,`MET`) | 1000 GeV each |
| `H2` | $H_2$ | S[101] | 0 | $\mathbf{1}$ | not declared | 0 | – | yes | `MH2` | internal $\approx 2829$ GeV |
| `H3` | $H_3$ | S[102] | 0 | $\mathbf{1}$ | not declared | 0 | – | yes | `MH3` | internal, $\sqrt{2\lambda_3 v_3^2}\approx 894$ GeV |
| `H0` | $H_0$ | S[103] | 0 | $\mathbf{1}$ | not declared | 0 | – | yes | `MH0` | internal $\approx 2834$ GeV |
| `Hpm` | $H^{\pm}$ | S[104] | 0 | $\mathbf{1}$ | not declared | $+1$ | $+1$ | no | `MHpm` | internal $\approx 2830$ GeV |
| `HQY` | $H_{QY}^{\pm}$ | S[105] | 0 | $\mathbf{1}$ | not declared | $+1$ | $+1$ | no | `MHQY` | internal $\approx 2056$ GeV |
| `HQV` | $H_{QV}^{0}$ | S[106] | 0 | $\mathbf{1}$ | not declared | 0 | 0 | no | `MHQV` | internal $\approx 2059$ GeV |

PDG codes run from 4000001 to 4000015. All widths are declared with the
placeholder value 1 GeV. No field carries an `SU2W` index, so all of them are
weak-isospin singlets in the broken phase; the electroweak quantum numbers are
given only through `Q` and `Y`.

Numerical mass values use the SM defaults $v \approx 246.2$ GeV and
$g_w \approx 0.65$, with $v_1 = 173.95$ GeV, $v_2 = \sqrt{v^2-v_1^2} \approx 174.3$ GeV,
$v_3 = 2000$ GeV, $f = 2000$ GeV.

### Note on the `DQ` hypercharge — internal inconsistency

Every other field in the file satisfies $Y = Q$, which is the correct relation
for a weak-isospin singlet ($Q = T^3 + Y$ with $T^3 = 0$). `DQ` breaks this
pattern: it declares $Q = -1/3$ but $Y = +1/3$.

The electric charge $Q_D = -1/3$ is confirmed independently by `LNPcc`: the
terms $\bar{u}\gamma^\mu P_L D\,Y'^+$ and $\bar{d}\gamma^\mu P_L D\,V'^0$ only
conserve charge for $Q_D = -1/3$. Also $S$, which has exactly the same role
(it pairs with $c$ and $s$ in the same way), carries $Y = -1/3$.

Consequence: because `DC` uses the declared `Y`, the $D$ quark in this file
couples to the photon and to the $Z$ with strength $+1/3$ while its declared
electric charge is $-1/3$. The two signs disagree. The value $Y_D = +1/3$ looks
like a sign error; the consistent value is $Y_D = -1/3$.

---

## 3. Parameters

### External

| Symbol | Value | Block / order | Multiplies | Meaning |
|---|---|---|---|---|
| `beta` | $0.5773502692 = 1/\sqrt{3}$ | NPINPUTS 1 | enters $M_{Z'}$ through $\beta^2 g_X^2$ | The $\beta$ parameter of the $SU(3)_L\times U(1)_X$ charge operator $Q = T^3 + \beta T^8 + X$. It fixes the charges of the exotic states. |
| `gX` | 0.5 | NPINPUTS 2, NP order 1 | enters $M_{Z'}$ | Gauge coupling of the extra $U(1)_X$ factor. |
| `v1` | 173.95 GeV | NPINPUTS 3 | $M_{V'}, M_{H_2}, M_{H_0}, M_{H^\pm}, M_{H_{QY}}, M_{H_{QV}}$ | Vacuum expectation value of the first scalar triplet. |
| `v3` | 2000 GeV | NPINPUTS 4 | all new masses | Vacuum expectation value of the third scalar triplet: the high scale that breaks the extended group down to the SM. |
| `k` | 1 | NPINPUTS 5 | $f = k\,v_3$ | Dimensionless ratio that sets the trilinear scalar coupling $f$ relative to $v_3$. |
| `lam3` | 0.1 | NPINPUTS 6, NP order 1 | $M_{H_3}^2 = 2\lambda_3 v_3^2$ | Quartic self-coupling of the third triplet. |
| `lampr12` | 0.1 | NPINPUTS 7, NP order 1 | $M_{H^\pm}^2$ | Quartic mixed coupling between triplets 1 and 2. |
| `lampr23` | 0.1 | NPINPUTS 8, NP order 1 | $M_{H_{QY}}^2$ | Quartic mixed coupling between triplets 2 and 3. |
| `lampr13` | 0.1 | NPINPUTS 9, NP order 1 | $M_{H_{QV}}^2$ | Quartic mixed coupling between triplets 1 and 3. |

Masses given directly as numbers: `MDQ` = `MSQ` = `MTQ` = 1000 GeV and
`MEE` = `MEM` = `MET` = 1000 GeV. All widths default to 1 GeV.

### Internal

| Symbol | Formula | Meaning |
|---|---|---|
| `v2` | $\sqrt{v^2 - v_1^2}$ | VEV of the second triplet, fixed so that $v_1^2 + v_2^2 = v^2$ (the SM VEV). The electroweak VEV is shared between the first two triplets. |
| `f` | $k\,v_3$ | Trilinear scalar coupling with mass dimension 1, from the $f\,\epsilon_{ijk}\eta^i\rho^j\chi^k$ type term. It gives mass to the pseudo-Goldstone-like states. |
| `MZp` | $\sqrt{(g_w^2+\beta^2 g_X^2)\,v_3^2/6}$ | Mass of the extra neutral gauge boson. |
| `MYp` | $\sqrt{g_w^2 (v_3^2+v_2^2)/4}$ | Mass of the charged heavy vector: it eats the VEVs of triplets 2 and 3. |
| `MVp` | $\sqrt{g_w^2 (v_3^2+v_1^2)/4}$ | Mass of the neutral complex heavy vector: VEVs of triplets 1 and 3. |
| `MH2` | $\sqrt{(v^2/(v_1 v_2))\,f\,v_3}$ | Mass of the second neutral scalar. |
| `MH3` | $\sqrt{2\lambda_3 v_3^2}$ | Mass of the heavy scalar of the third triplet. |
| `MH0` | $\sqrt{(v_1 v_2/v_3 + v_1 v_3/v_2 + v_2 v_3/v_1)\,f}$ | Mass of the neutral pseudoscalar-like state, fully generated by $f$. |
| `MHpm` | $\sqrt{(2 f v_3 + \lambda'_{12} v_1 v_2)\,v^2/(2 v_1 v_2)}$ | Mass of the singly charged scalar from the 1-2 sector. |
| `MHQY` | $\sqrt{(2 f v_1 + \lambda'_{23} v_2 v_3)(v_2^2+v_3^2)/(2 v_2 v_3)}$ | Mass of the charged scalar from the 2-3 sector (the $Y'$ sector). |
| `MHQV` | $\sqrt{(2 f v_2 + \lambda'_{13} v_1 v_3)(v_1^2+v_3^2)/(2 v_1 v_3)}$ | Mass of the neutral complex scalar from the 1-3 sector (the $V'$ sector). |

`InteractionOrderHierarchy` is `{{QCD,1},{QED,2},{NP,1}}`: a new coupling order
`NP` is added beside QCD and QED, and `gX`, `lam3`, `lampr12`, `lampr23`,
`lampr13` carry `NP` order 1.

---

## 4. Physics summary

This is a broken-phase (mass-eigenstate) implementation of a 3-3-1 model,
that is an extension of the SM to
$SU(3)_c \times SU(3)_L \times U(1)_X$ with $Q = T^3 + \beta T^8 + X$ and
$\beta = 1/\sqrt{3}$. Three scalar triplets with VEVs $v_1, v_2, v_3$ break the
group; $v_1^2+v_2^2 = v^2$ gives the electroweak scale and $v_3 = 2$ TeV gives
the new scale. The new states are: one neutral gauge boson $Z'$, one singly
charged heavy vector $Y'^\pm$ and one neutral complex heavy vector $V'^0$
(bilepton-type, masses near 650 GeV); three vector-like exotic quarks $D$, $S$
with $Q=-1/3$ and $T$ with $Q=+2/3$ (1 TeV, colour triplets); three heavy
neutral leptons $E_e, E_\mu, E_\tau$ (1 TeV); and a scalar spectrum of three
real neutral states $H_2$, $H_3$, $H_0$, two singly charged states $H^\pm$ and
$H_{QY}^\pm$, and one neutral complex state $H_{QV}$, all with masses set by
$f = k v_3$ and by the quartic couplings.

The only explicit new interaction is a left-handed current of SM strength
$g_w/\sqrt{2}$ that joins a SM quark of the first two generations to an exotic
quark through the new vectors: $u$-$D$-$Y'$, $c$-$S$-$Y'$, $d$-$D$-$V'$ and
$s$-$S$-$V'$. This mediates single exotic-quark production at a hadron
collider ($q\,g \to Q\,Y'^{*}/V'^{*}$, and $q\bar{q} \to D\bar{D}$, $S\bar{S}$
by $Y'$ or $V'$ exchange in the $t$-channel, beside QCD pair production), the
decays $D \to u\,Y'^{-*} \to u\,\bar{u}d$ type chains, and flavour-changing
$d$-$s$ transitions at loop level through the shared $V'$ coupling. Because
$M_{Y'}, M_{V'} < M_{D}, M_{S}$, the new vectors cannot decay into an exotic
quark on-shell in this parameter point; with only these interactions written
down they decay through the off-shell exotic quark. $Z'$, the heavy leptons and
the neutral scalars have no interaction at all in this file beyond their gauge
couplings; the Yukawa sector and the scalar potential interactions are not
implemented here.

**Caveat.** The hypercharge of `DQ` ($Y = +1/3$ with $Q = -1/3$) contradicts
both the $Y = Q$ pattern of every other field and the charge flow of `LNPcc`.
See the note in section 2. With $Y_D = -1/3$ the whole spectrum is consistent:
exotic quarks of charge $-1/3, -1/3, +2/3$, neutral heavy leptons, one charged
and one neutral new vector.
