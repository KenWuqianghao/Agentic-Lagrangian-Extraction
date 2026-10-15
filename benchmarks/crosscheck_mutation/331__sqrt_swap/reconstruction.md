# Reconstruction of `sanitized.fr`

All statements below come only from the content of `sanitized.fr`. The file is an
*add-on* model: it declares new particles and new parameters, and it uses symbols
(`gw`, `g1`, `gs`, `vev`, `u`, `c`, `d`, `s`, `DC`, `Ga`, `ProjM`, `HC`) that are
not defined in the file. These come from a base Standard Model (SM) implementation
that must be loaded together with this file.

---

## 1. Lagrangian

### Conventions used to expand the FeynRules idioms

* `Ga[mu]` = `\(\gamma^\mu\)`.
* `ProjM` = `\(P_L=\tfrac{1-\gamma^5}{2}\)` (left-handed projector).
  (`ProjP` = `\(P_R\)` does not appear in this file.)
* `Xbar` = `\(\bar X = X^\dagger\gamma^0\)` for fermions, `\(X^\dagger\)` for
  scalars and vectors.
* `FS[X,mu,nu]` for a vector field that is **not** a declared gauge field is the
  abelian field strength `\(X_{\mu\nu}=\partial_\mu X_\nu-\partial_\nu X_\mu\)`.
* `HC[...]` = hermitian conjugate of the whole bracket.
* A repeated index inside `Block[{mu,nu}, ...]` is contracted with the Minkowski
  metric `\(\eta_{\mu\nu}\)`.
* No charge conjugation (`CC`) and no Majorana field appears in this file.

### Covariant derivative `DC`

None of the new fields carries an `Index[SU2W]` or an `Index[Gluon]`, and none of
them is declared as a gauge boson. Therefore each new field is an **SU(2)\(_L\)
singlet**, and `DC` reduces to the colour and hypercharge pieces of the base SM
covariant derivative:

$$
D_\mu \Phi \;=\; \Big(\partial_\mu
\;-\; i\,g_s\,T^a_{ij}\,G^a_\mu
\;-\; i\,g_1\,Y_\Phi\,B_\mu\Big)\Phi ,
$$

where the gluon term is present only for fields that carry `Index[Colour]`
(`DQ`, `SQ`, `TQ`, in the fundamental **3**), and `\(Y_\Phi\)` is the declared `Y`
quantum number. Explicitly:

| Field | `DC` content |
| --- | --- |
| `DQ`, `SQ` (`Y=-1/3`) | `\(\partial_\mu - i g_s T^a G^a_\mu + \tfrac{i}{3} g_1 B_\mu\)` |
| `TQ` (`Y=+2/3`) | `\(\partial_\mu - i g_s T^a G^a_\mu - \tfrac{2i}{3} g_1 B_\mu\)` |
| `EL` (`Y=0`, colourless) | `\(\partial_\mu\)` (free field) |
| `Hpm`, `HQY` (`Y=+1`) | `\(\partial_\mu - i g_1 B_\mu\)` |
| `HQV` (`Y=0`) | `\(\partial_\mu\)` (free field) |

Note that the new heavy vectors `Zp`, `Yp`, `Vp` are **not** declared as gauge
fields of any group; they are put in by hand as massive (Proca) vectors, so they
do not enter `DC` and they have no self-interactions. Because every new state is
an SU(2)\(_L\) singlet, `\(Q=T^3+Y\)` gives `\(Q=Y\)`, which is exactly what the
declarations show.

---

### `LZp` — real massive neutral vector

$$
\mathcal{L}_{Z'} \;=\; -\frac{1}{4}\,Z'_{\mu\nu}Z'^{\mu\nu}
\;+\;\frac{1}{2}\,M_{Z'}^{2}\,Z'_\mu Z'^\mu ,
\qquad
Z'_{\mu\nu}=\partial_\mu Z'_\nu-\partial_\nu Z'_\mu .
$$

`Zp` is self-conjugate (a real vector), hence the `\(1/4\)` and `\(1/2\)` factors.

### `LYp` — complex massive vector, \(Q=+1\)

$$
\mathcal{L}_{Y'} \;=\; -\frac{1}{2}\,Y'^{\dagger}_{\mu\nu}Y'^{\mu\nu}
\;+\; M_{Y'}^{2}\,Y'^{\dagger}_\mu Y'^\mu ,
\qquad
Y'_{\mu\nu}=\partial_\mu Y'_\nu-\partial_\nu Y'_\mu .
$$

### `LVp` — complex massive vector, \(Q=0\)

$$
\mathcal{L}_{V'} \;=\; -\frac{1}{2}\,V'^{\dagger}_{\mu\nu}V'^{\mu\nu}
\;+\; M_{V'}^{2}\,V'^{\dagger}_\mu V'^\mu .
$$

`Vp` is electrically neutral but **not** self-conjugate: `\(V'\)` and
`\(\bar V'\)` are distinct states (they carry a non-zero conserved quantum number
that is not electric charge).

### `LDQ` — exotic down-type quark

$$
\mathcal{L}_{D} \;=\; i\,\bar D\,\gamma^\mu D_\mu D \;-\; M_{D}\,\bar D D ,
\qquad
D_\mu D = \Big(\partial_\mu - i g_s T^a G^a_\mu + \tfrac{i}{3}g_1 B_\mu\Big)D .
$$

(Colour index contracted between `\(\bar D\)` and `\(D\)`; vector-like Dirac mass,
no chiral projector, so both chiralities couple identically to the gauge fields.)

### `LSQ` — second exotic down-type quark

$$
\mathcal{L}_{S} \;=\; i\,\bar S\,\gamma^\mu D_\mu S \;-\; M_{S}\,\bar S S .
$$

### `LTQ` — exotic up-type quark

$$
\mathcal{L}_{T} \;=\; i\,\bar T\,\gamma^\mu D_\mu T \;-\; M_{T}\,\bar T T ,
\qquad
D_\mu T = \Big(\partial_\mu - i g_s T^a G^a_\mu - \tfrac{2i}{3}g_1 B_\mu\Big)T .
$$

### `LEL` — three heavy neutral Dirac leptons

$$
\mathcal{L}_{E} \;=\; i\sum_{i=1}^{3}\bar E_i\,\gamma^\mu \partial_\mu E_i
\;-\; M_{E_e}\,\bar E_e E_e
\;-\; M_{E_\mu}\,\bar E_\mu E_\mu
\;-\; M_{E_\tau}\,\bar E_\tau E_\tau .
$$

The kinetic term is written with the generation index summed
(`ELbar.Ga[mu].DC[EL,mu]`), while the mass term is written member by member, so
the mass matrix is diagonal in the flavour basis. Since `Y = 0` and there is no
colour index, `DC` degenerates to `\(\partial_\mu\)`: these leptons are complete
gauge singlets in this file.

### `LH2` — real neutral scalar

$$
\mathcal{L}_{H_2} \;=\; \frac{1}{2}\,\partial_\mu H_2\,\partial^\mu H_2
\;-\;\frac{1}{2}\,M_{H_2}^{2}\,H_2^{2}.
$$

### `LH3` — real neutral scalar

$$
\mathcal{L}_{H_3} \;=\; \frac{1}{2}\,\partial_\mu H_3\,\partial^\mu H_3
\;-\;\frac{1}{2}\,M_{H_3}^{2}\,H_3^{2}.
$$

### `LH0` — real neutral (pseudo)scalar

$$
\mathcal{L}_{H_0} \;=\; \frac{1}{2}\,\partial_\mu H_0\,\partial^\mu H_0
\;-\;\frac{1}{2}\,M_{H_0}^{2}\,H_0^{2}.
$$

### `LHpm` — charged scalar, \(Q=+1\)

$$
\mathcal{L}_{H^\pm} \;=\; \big(D_\mu H^{+}\big)^{\dagger}\big(D^\mu H^{+}\big)
\;-\; M_{H^\pm}^{2}\,H^{-}H^{+},
\qquad
D_\mu H^{+}=\big(\partial_\mu - i g_1 B_\mu\big)H^{+}.
$$

### `LHQY` — second charged scalar, \(Q=+1\)

$$
\mathcal{L}_{H_{QY}} \;=\; \big(D_\mu H_{QY}\big)^{\dagger}\big(D^\mu H_{QY}\big)
\;-\; M_{H_{QY}}^{2}\,H_{QY}^{\dagger}H_{QY},
\qquad
D_\mu H_{QY}=\big(\partial_\mu - i g_1 B_\mu\big)H_{QY}.
$$

### `LHQV` — complex neutral scalar

$$
\mathcal{L}_{H_{QV}} \;=\; \partial_\mu H_{QV}^{\dagger}\,\partial^\mu H_{QV}
\;-\; M_{H_{QV}}^{2}\,H_{QV}^{\dagger}H_{QV}.
$$

Because `Q = Y = 0`, `DC` again degenerates to `\(\partial_\mu\)`.

### `LNPcc` — new charged/neutral current mixing SM quarks with exotic quarks

$$
\begin{aligned}
\mathcal{L}_{\rm NP} \;=\; \frac{g_w}{\sqrt{2}}\Big[
&\ \bar u\,\gamma^\mu P_L\,D\;Y'_\mu
\;+\; \bar c\,\gamma^\mu P_L\,S\;Y'_\mu \\
+&\ \bar d\,\gamma^\mu P_L\,D\;V'_\mu
\;+\; \bar s\,\gamma^\mu P_L\,S\;V'_\mu \Big]
\;+\;\text{h.c.}
\end{aligned}
$$

Written out, the hermitian conjugate gives

$$
\frac{g_w}{\sqrt{2}}\Big[
\bar D\,\gamma^\mu P_L\,u\;Y'^{\dagger}_\mu
+\bar S\,\gamma^\mu P_L\,c\;Y'^{\dagger}_\mu
+\bar D\,\gamma^\mu P_L\,d\;V'^{\dagger}_\mu
+\bar S\,\gamma^\mu P_L\,s\;V'^{\dagger}_\mu\Big].
$$

Points to check term by term:

* The current is **purely left-handed** (`ProjM` = `\(P_L\)`) on both the SM quark
  and the exotic quark.
* Colour is contracted directly between the SM quark and the exotic quark
  (both are colour triplets), so the vertex is colour-diagonal and `\(Y'\)`,
  `\(V'\)` are colour singlets.
* Charge is conserved at every vertex:
  `\(-Q_u+Q_D+Q_{Y'} = -\tfrac23-\tfrac13+1 = 0\)`, and
  `\(-Q_d+Q_D+Q_{V'} = +\tfrac13-\tfrac13+0 = 0\)`.
* Only the first two generations appear. `\(T\)` (the `\(Q=+2/3\)` exotic quark)
  and the third-generation SM quarks `\(t,b\)` have **no** such coupling in this
  file. The heavy leptons `\(E_i\)` likewise have no coupling to `\(Y'\)` or
  `\(V'\)`.
* The overall strength is the SM weak coupling `\(g_w/\sqrt2\)`, i.e. the same
  normalisation as the SM charged current, with no mixing angle.

### `LTotal`

$$
\mathcal{L}_{\rm total}=\mathcal{L}_{Z'}+\mathcal{L}_{Y'}+\mathcal{L}_{V'}
+\mathcal{L}_{D}+\mathcal{L}_{S}+\mathcal{L}_{T}+\mathcal{L}_{E}
+\mathcal{L}_{H_2}+\mathcal{L}_{H_3}+\mathcal{L}_{H_0}
+\mathcal{L}_{H^\pm}+\mathcal{L}_{H_{QY}}+\mathcal{L}_{H_{QV}}
+\mathcal{L}_{\rm NP}.
$$

No scalar potential, no Yukawa couplings and no `\(Z'\)`–fermion couplings are
written. The scalar masses and the vector masses are supplied as *internal
parameters* (see §3), i.e. the symmetry-breaking sector is encoded only through
the mass formulas, not through an explicit potential.

---

## 2. Field table

All new fields are **SU(2)\(_L\) singlets** (no `SU2W` index is declared).
"3" means the fundamental of colour SU(3)\(_C\); the antiparticle is in `\(\bar 3\)`.
Because \(T^3=0\) for every new state, \(Q=Y\) throughout.

| Symbol (`ClassName`) | Class | Spin | SU(3)\(_C\) | SU(2)\(_L\) | \(Q\) | \(Y\) | Self-conj. | Mass symbol | Numeric mass |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Zp` (\(Z'\)) | `V[101]` | 1 | **1** | **1** | 0 | – | yes | `MZp` | internal |
| `Yp` (\(Y'^{\pm}\)) | `V[102]` | 1 | **1** | **1** | \(+1\) | – | no | `MYp` | internal |
| `Vp` (\(V'\)) | `V[103]` | 1 | **1** | **1** | \(0\) | – | no | `MVp` | internal |
| `DQ` | `F[101]` | 1/2 | **3** | **1** | \(-1/3\) | \(-1/3\) | no | `MDQ` | 1000 GeV |
| `SQ` | `F[102]` | 1/2 | **3** | **1** | \(-1/3\) | \(-1/3\) | no | `MSQ` | 1000 GeV |
| `TQ` | `F[103]` | 1/2 | **3** | **1** | \(+2/3\) | \(+2/3\) | no | `MTQ` | 1000 GeV |
| `EL` = {`Ee`,`Emu`,`Etau`} | `F[104]` | 1/2 | **1** | **1** | \(0\) | \(0\) | no | `MEL` = {`MEE`,`MEM`,`MET`} | 1000 GeV each |
| `H2` | `S[101]` | 0 | **1** | **1** | 0 | – | yes | `MH2` | internal |
| `H3` | `S[102]` | 0 | **1** | **1** | 0 | – | yes | `MH3` | internal |
| `H0` | `S[103]` | 0 | **1** | **1** | 0 | – | yes | `MH0` | internal |
| `Hpm` (\(H^{\pm}\)) | `S[104]` | 0 | **1** | **1** | \(+1\) | \(+1\) | no | `MHpm` | internal |
| `HQY` | `S[105]` | 0 | **1** | **1** | \(+1\) | \(+1\) | no | `MHQY` | internal |
| `HQV` | `S[106]` | 0 | **1** | **1** | \(0\) | \(0\) | no | `MHQV` | internal |

PDG codes run from 4000001 (`Zp`) to 4000015 (`HQV`). Every new state gets a
default width of 1 GeV (`WZp`, `WYp`, ... , `WHQV`).

Two remarks on internal consistency of the declarations:

* `EL` carries `Q -> 0` but its leftover `FullName` strings call it a
  "Heavy charged lepton". The quantum numbers (which is what FeynRules uses)
  say the state is electrically **neutral**.
* `Vp` and `HQV` have `Q -> 0` yet `SelfConjugate -> False`. This is consistent
  only if they carry another conserved charge (e.g. a lepton-number-like or
  bilepton-like quantum number) that is not declared in the file.

---

## 3. Parameters

### External parameters (block `NPINPUTS`)

| Symbol | Value | Order | Interaction order | What it multiplies | Physical meaning |
| --- | --- | --- | --- | --- | --- |
| `beta` (\(\beta\)) | 0.57735026919 = \(1/\sqrt3\) | 1 | – | appears only inside `MZp` | Embedding parameter that fixes how the extra abelian charge enters the heavy neutral-vector mass; \(\beta=1/\sqrt3\) is a specific choice of the extended gauge embedding. |
| `gX` (\(g_X\)) | 0.5 | 2 | NP, 1 | appears only inside `MZp` | Gauge coupling of the extra abelian group. It never appears in a Lagrangian term of this file, only in the \(Z'\) mass. |
| `v1` (\(v_1\)) | 173.95 GeV | 3 | – | inside `MVp`, `MH2`, `MH0`, `MHpm`, `MHQY`, `MHQV`, `v2` | First electroweak-scale vacuum expectation value (VEV). |
| `v3` (\(v_3\)) | 2000 GeV | 4 | – | inside `f`, `MZp`, `MYp`, `MVp`, and all scalar masses | Large VEV that breaks the extended gauge group; it sets the heavy-vector scale. |
| `k` | 1 | 5 | – | `f = k*v3` | Dimensionless ratio that fixes the trilinear scalar parameter \(f\) in units of \(v_3\). |
| `lam3` (\(\lambda_3\)) | 0.1 | 6 | NP, 1 | `MH3` | Quartic self-coupling of the large-VEV scalar direction; fixes \(M_{H_3}\). |
| `lampr12` (\(\lambda'_{12}\)) | 0.1 | 7 | NP, 1 | `MHpm` | Quartic coupling between scalar multiplets 1 and 2; fixes the \(H^{\pm}\) mass. |
| `lampr23` (\(\lambda'_{23}\)) | 0.1 | 8 | NP, 1 | `MHQY` | Quartic coupling between multiplets 2 and 3; fixes the \(H_{QY}\) mass. |
| `lampr13` (\(\lambda'_{13}\)) | 0.1 | 9 | NP, 1 | `MHQV` | Quartic coupling between multiplets 1 and 3; fixes the \(H_{QV}\) mass. |

Fermion masses `MDQ`, `MSQ`, `MTQ`, `MEE`, `MEM`, `MET` (all 1000 GeV) are also
external, declared inside the particle classes; they multiply the Dirac bilinears
`\(\bar D D\)`, `\(\bar S S\)`, `\(\bar T T\)`, `\(\bar E_i E_i\)`.

`gw`, `g1`, `gs` and `vev` are **not** declared here; they come from the base SM
file. `gw` multiplies the whole of `LNPcc`.

### Internal parameters

| Symbol | Definition in the file | Meaning |
| --- | --- | --- |
| `v2` | \(v_2 = 1/\sqrt{v_{\rm ew}^2-v_1^2}\) | Second electroweak-scale VEV, fixed by the electroweak constraint (see the note below). |
| `f` | \(f = k\,v_3\) | Dimension-one trilinear scalar parameter. |
| `MZp` | \(M_{Z'}=\sqrt{(g_w^{2}+\beta^{2}g_X^{2})\,v_3^{2}/6}\) | Heavy neutral-vector mass; mixes the non-abelian and the extra abelian coupling through \(\beta\). |
| `MYp` | \(M_{Y'}=\sqrt{g_w^{2}\,(v_3^{2}+v_2^{2})/4}\) | Mass of the \(Q=+1\) heavy vector. |
| `MVp` | \(M_{V'}=\sqrt{g_w^{2}\,(v_3^{2}+v_1^{2})/4}\) | Mass of the neutral complex heavy vector. |
| `MH2` | \(M_{H_2}=\sqrt{\dfrac{v_{\rm ew}^{2}}{v_1 v_2}\,f\,v_3}\) | Mass of the real scalar \(H_2\); set by the trilinear term \(f\). |
| `MH3` | \(M_{H_3}=\sqrt{2\lambda_3 v_3^{2}}\) | Mass of the real scalar \(H_3\); the only mass set by a quartic coupling alone. |
| `MH0` | \(M_{H_0}=\sqrt{\Big(\dfrac{v_1v_2}{v_3}+\dfrac{v_1v_3}{v_2}+\dfrac{v_2v_3}{v_1}\Big) f}\) | Mass of the CP-odd-like real scalar \(H_0\); vanishes as \(f\to0\), i.e. it is a pseudo-Goldstone of the trilinear term. |
| `MHpm` | \(M_{H^\pm}=\sqrt{\dfrac{(2f v_3+\lambda'_{12}v_1v_2)\,v_{\rm ew}^{2}}{2 v_1 v_2}}\) | Charged-scalar mass from the 1–2 sector. |
| `MHQY` | \(M_{H_{QY}}=\sqrt{\dfrac{(2f v_1+\lambda'_{23}v_2v_3)(v_2^{2}+v_3^{2})}{2 v_2 v_3}}\) | Charged-scalar mass from the 2–3 sector. |
| `MHQV` | \(M_{H_{QV}}=\sqrt{\dfrac{(2f v_2+\lambda'_{13}v_1v_3)(v_1^{2}+v_3^{2})}{2 v_1 v_3}}\) | Neutral complex-scalar mass from the 1–3 sector. |

**Note on `v2` (dimensional inconsistency in the file as given).**
`v2` is written as `1/Sqrt[vev^2 - v1^2]`, which has mass dimension \(-1\)
(numerically \(\approx 5.74\times10^{-3}\,\mathrm{GeV^{-1}}\) for
\(v_{\rm ew}=246.22\) GeV, \(v_1=173.95\) GeV). Every other use of `v2` in the
file (`MYp`, `MH2`, `MH0`, `MHpm`, `MHQY`, `MHQV`) treats it as a VEV of mass
dimension \(+1\), and the pattern `\(v_1^2+v_2^2=v_{\rm ew}^2\)` — which is what
`MHpm` and `MH2` assume through the factor \(v_{\rm ew}^2/(v_1v_2)\) — requires
\(v_2=\sqrt{v_{\rm ew}^2-v_1^2}\approx 174.1\) GeV. As written, the definition is
the reciprocal of that, so `MH2` evaluates to roughly \(5\times10^{5}\) GeV
instead of roughly \(3\times10^{3}\) GeV. I report the formula exactly as it
appears in the file, and flag it as an evident sign/inversion defect in the
`Sqrt` expression rather than intended physics.

### Interaction-order hierarchy

`M$InteractionOrderHierarchy = {{QCD,1},{QED,2},{NP,1}}` declares a new coupling
order `NP`, carried by `gX`, `lam3` and the three `lampr` quartics. The
`LNPcc` vertex itself carries no `NP` order because it is proportional to `gw`.

---

## 4. Physics summary

This file adds, on top of the Standard Model, a heavy vector sector
(\(Z'\), a charged \(Y'^{\pm}\), a neutral-but-complex \(V'\)), three colour-triplet
vector-like exotic quarks (\(D\) and \(S\) with \(Q=-1/3\), \(T\) with \(Q=+2/3\),
all at 1 TeV), three gauge-singlet heavy Dirac leptons, and an extended scalar
sector of three real neutral scalars, two \(Q=+1\) scalars and one complex neutral
scalar. The \(Z'\) mass formula \(M_{Z'}^2=(g_w^2+\beta^2 g_X^2)v_3^2/6\) with
\(\beta=1/\sqrt3\), the three VEVs \(v_1,v_2,v_3\) with \(v_3\gg v_1\), the
bilepton-like \(Y'^{\pm}\)/\(V'\) pair, and the exotic-quark charges
\((-1/3,-1/3,+2/3)\) together identify the underlying structure as an
SU(3)\(_C\)×SU(3)\(_L\)×U(1)\(_X\) ("331-type") extension, with \(v_3\) breaking
the enlarged group down to the SM and \(v_1,v_2\) doing electroweak breaking.

Dynamically, however, the only genuinely new *interaction* written in the file is
`LNPcc`: a purely left-handed current of SM strength \(g_w/\sqrt2\) that connects
\(u\leftrightarrow D\) and \(c\leftrightarrow S\) through \(Y'^{\pm}\), and
\(d\leftrightarrow D\) and \(s\leftrightarrow S\) through \(V'\). Everything else
enters only through gauge-covariant kinetic terms (QCD and hypercharge), so the
\(Z'\), the scalars, \(T\) and the heavy leptons have no non-gauge couplings here.

Processes the model would mediate: QCD pair production of \(D\), \(S\), \(T\) at a
hadron collider, followed by \(D\to u\,Y'^{-}\) / \(D\to d\,\bar V'\) (or the
off-shell three-body versions when \(M_{D}<M_{Y'}\)); single exotic-quark
production from a light quark plus a \(Y'\) or \(V'\); resonant \(Y'^{\pm}\) and
\(V'\) production from \(q\bar q'\) initial states with decays back to a light
quark plus an exotic quark; and tree-level \(Y'\)/\(V'\) exchange generating new
four-quark contact operators among the first two generations. The \(T\) quark and
the heavy leptons are produced only through gauge interactions (strong for \(T\),
none at all for the \(E_i\), which are stable and invisible as written), and the
new scalars and the \(Z'\) are likewise inert apart from their electromagnetic and
hypercharge couplings.
