# Reconstruction of `sanitized.fr`

All statements below come only from the content of `sanitized.fr`. The file is a
FeynRules add-on module: it declares new parameters, new particle classes and a
new Lagrangian `LTotal`, but it does **not** declare any gauge group. It
therefore imports the gauge groups, the gauge fields and the Standard Model
fields from a base model file. The symbols `gw`, `gs`, `g1`, `vev`, `ee`,
`u`, `c`, `d`, `s`, `G`, `B`, `W` used below are taken from that base model and
are not defined in this file.

---

## 0. Conventions and the covariant derivative

The file uses the standard FeynRules idioms. They expand as follows.

| Idiom | Meaning |
| --- | --- |
| `FS[X,mu,nu]` | field strength; for these non-gauge vectors $F_{\mu\nu}[X]=\partial_\mu X_\nu-\partial_\nu X_\mu$ |
| `Ga[mu]` | Dirac matrix $\gamma^\mu$ |
| `ProjM` | left chiral projector $P_L=\tfrac{1}{2}(1-\gamma^5)$ |
| `ProjP` | right chiral projector $P_R=\tfrac{1}{2}(1+\gamma^5)$ (not used in this file) |
| `Xbar` | $\bar X=X^\dagger\gamma^0$ for fermions, $X^\dagger$ for scalars and vectors |
| `HC[...]` | hermitian conjugate of the full expression |
| `del[X,mu]` | $\partial_\mu X$ |
| `DC[X,mu]` | gauge covariant derivative $D_\mu X$ |

**Gauge content of `DC`.** No new gauge group is declared in this file. Every
new field is an SU(2)$_L$ singlet (no `Index[SU2D]` or `Index[SU2W]` is given),
so `DC` contains only the colour group and the hypercharge group of the base
model:

$$
D_\mu \Psi \;=\; \Big(\partial_\mu \;-\; i\,g_s\,G_\mu^{a}\,T^{a}\;-\;i\,g'\,Y\,B_\mu\Big)\Psi ,
\qquad T^a = \tfrac{\lambda^a}{2},
$$

where $Y$ is the value declared in `QuantumNumbers`. Consequences, field by
field:

* `DQ`, `SQ`, `TQ` — colour triplets with $Y\neq 0$: both the gluon term and the
  $B_\mu$ term are present. In the photon/$Z$ basis $B_\mu=c_W A_\mu-s_W Z_\mu$
  and $Y=Q$ for all three, so they couple as $-i e Q A_\mu + i e\,(s_W/c_W)\,Q\,Z_\mu$.
* `Hpm`, `HQY` — colour singlets with $Y=Q=1$: only the $B_\mu$ (hence $A_\mu$, $Z_\mu$) term.
* `EL`, `HQV` — all charges zero and no colour, so $D_\mu\to\partial_\mu$ and the
  kinetic terms are free.
* The **new** vectors `Zp`, `Yp`, `Vp` never appear inside any `DC`. They are
  introduced as free fields; their only interaction with matter is the explicit
  current `LNPcc`.

Colour indices are implicit in FeynRules. In `LDQ`, `LSQ`, `LTQ` and in `LNPcc`
they are contracted as $\delta_{ij}$ between the barred and unbarred fields, so
every fermion bilinear is a colour singlet.

---

## 1. Lagrangian, term by term

### `LZp` — neutral heavy vector $Z'$ (real)

$$
\mathcal{L}_{Z'} \;=\; 2\left[-\frac{1}{4}\,Z'_{\mu\nu}Z'^{\mu\nu}
\;+\;\frac{1}{2}\,M_{Z'}^{2}\,Z'_\mu Z'^{\mu}\right]
\;=\; -\frac{1}{2}\,Z'_{\mu\nu}Z'^{\mu\nu}\;+\;M_{Z'}^{2}\,Z'_\mu Z'^{\mu},
\qquad Z'_{\mu\nu}=\partial_\mu Z'_\nu-\partial_\nu Z'_\mu .
$$

> **Normalisation note.** The overall factor `2` in the source is written
> explicitly and is kept above. For a **real** (self-conjugate) vector field the
> canonical Proca Lagrangian is $-\frac14 F^2+\frac12 M^2 Z'^2$ without the
> factor. The factor multiplies the kinetic and the mass term by the same
> amount, so the pole position stays at $M_{Z'}$, but the field is not
> canonically normalised: the propagator residue is halved. The complex vectors
> `Yp` and `Vp` below use the standard complex normalisation $-\frac12|F|^2+M^2|Y|^2$,
> so `Zp` is normalised like a complex field although it is declared
> `SelfConjugate -> True`. Flag this for the physicist: it is either a
> deliberate convention or a factor-of-2 defect.

### `LYp` — singly charged heavy vector $Y'^{\pm}$ (complex)

$$
\mathcal{L}_{Y'} \;=\; -\frac{1}{2}\,Y'^{\dagger}_{\mu\nu}Y'^{\mu\nu}
\;+\;M_{Y'}^{2}\,Y'^{\dagger}_{\mu}Y'^{\mu},
\qquad Y'_{\mu\nu}=\partial_\mu Y'_\nu-\partial_\nu Y'_\mu .
$$

### `LVp` — neutral **non-hermitian** heavy vector $V'$ (complex, $Q=0$)

$$
\mathcal{L}_{V'} \;=\; -\frac{1}{2}\,V'^{\dagger}_{\mu\nu}V'^{\mu\nu}
\;+\;M_{V'}^{2}\,V'^{\dagger}_{\mu}V'^{\mu},
\qquad V'_{\mu\nu}=\partial_\mu V'_\nu-\partial_\nu V'_\mu .
$$

$V'$ carries $Q=0$ but is declared `SelfConjugate -> False`, so $V'$ and
$\bar V'$ are distinct states. They are separated by a non-electric charge
(lepton-like / bilepton number) that is not gauged in this file.

### `LDQ`, `LSQ`, `LTQ` — vector-like exotic quarks

$$
\mathcal{L}_{D} \;=\; i\,\bar D\,\gamma^{\mu}D_\mu D\;-\;M_{D}\,\bar D D ,
\qquad
D_\mu D = \Big(\partial_\mu - i g_s G^a_\mu T^a + \tfrac{i}{3} g' B_\mu\Big)D ,
\quad Y_D=-\tfrac13 .
$$

$$
\mathcal{L}_{S} \;=\; i\,\bar S\,\gamma^{\mu}D_\mu S\;-\;M_{S}\,\bar S S ,
\qquad Y_S=-\tfrac13 .
$$

$$
\mathcal{L}_{T} \;=\; i\,\bar T\,\gamma^{\mu}D_\mu T\;-\;M_{T}\,\bar T T ,
\qquad
D_\mu T = \Big(\partial_\mu - i g_s G^a_\mu T^a - \tfrac{2i}{3} g' B_\mu\Big)T ,
\quad Y_T=+\tfrac23 .
$$

The mass terms are **Dirac** and chirality-blind ($\bar D D = \bar D_L D_R + \bar D_R D_L$),
so all three exotic quarks are vector-like.

### `LEL` — three heavy neutral leptons

$$
\mathcal{L}_{E} \;=\; i\sum_{i=1}^{3}\bar E_i\,\gamma^{\mu}\partial_\mu E_i
\;-\;M_{E_e}\,\bar E_e E_e \;-\; M_{E_\mu}\,\bar E_\mu E_\mu \;-\; M_{E_\tau}\,\bar E_\tau E_\tau .
$$

Because $Q=Y=0$ and there is no colour index, $D_\mu E=\partial_\mu E$: the
kinetic term is free. The generation index is summed implicitly in
`ELbar.Ga[mu].DC[EL,mu]`; the mass matrix is written out member by member and is
therefore diagonal in the generation basis.

### `LH2`, `LH3`, `LH0` — three real neutral scalars

$$
\mathcal{L}_{H_2} \;=\; \frac{1}{2}\,\partial_\mu H_2\,\partial^{\mu}H_2
\;-\;\frac{1}{2}\,M_{H_2}^{2}\,H_2^{2}.
$$

$$
\mathcal{L}_{H_3} \;=\; \frac{1}{2}\,\partial_\mu H_3\,\partial^{\mu}H_3
\;-\;\frac{1}{2}\,M_{H_3}^{2}\,H_3^{2}.
$$

$$
\mathcal{L}_{H_0} \;=\; \frac{1}{2}\,\partial_\mu H_0\,\partial^{\mu}H_0
\;-\;\frac{1}{2}\,M_{H_0}^{2}\,H_0^{2}.
$$

These use `del`, not `DC`, which is consistent: all three are real and neutral.

### `LHpm`, `LHQY` — singly charged scalars

$$
\mathcal{L}_{H^{\pm}} \;=\; \big(D_\mu H^{+}\big)^{\dagger}\big(D^{\mu}H^{+}\big)
\;-\;M_{H^{\pm}}^{2}\,H^{-}H^{+},
\qquad
D_\mu H^{+}=\big(\partial_\mu - i g' B_\mu\big)H^{+},\quad Y=Q=+1 .
$$

$$
\mathcal{L}_{H_{QY}} \;=\; \big(D_\mu H_{QY}^{+}\big)^{\dagger}\big(D^{\mu}H_{QY}^{+}\big)
\;-\;M_{H_{QY}}^{2}\,H_{QY}^{-}H_{QY}^{+},
\qquad Y=Q=+1 .
$$

Both give the usual scalar QED vertices with $A_\mu$ and $Z_\mu$ plus the
seagull terms.

### `LHQV` — neutral complex scalar

$$
\mathcal{L}_{H_{QV}} \;=\; \partial_\mu H_{QV}^{\dagger}\,\partial^{\mu}H_{QV}
\;-\;M_{H_{QV}}^{2}\,H_{QV}^{\dagger}H_{QV}.
$$

Since $Q=Y=0$, `DC` reduces to $\partial_\mu$, so this is a free complex scalar.
Like $V'$, it is neutral yet not self-conjugate.

### `LNPcc` — the new charged-current interaction

$$
\begin{aligned}
\mathcal{L}_{\rm NP}^{\rm CC} \;=\; \frac{g}{\sqrt{2}}\Big[\;
&\bar u\,\gamma^{\mu}P_L\,D\;Y'_{\mu}
\;+\;\bar c\,\gamma^{\mu}P_L\,S\;Y'_{\mu}\\
+\;&\bar d\,\gamma^{\mu}P_L\,D\;V'_{\mu}
\;+\;\bar s\,\gamma^{\mu}P_L\,S\;V'_{\mu}\;\Big]
\;+\;{\rm h.c.}
\end{aligned}
$$

Written out, the hermitian conjugate is

$$
\frac{g}{\sqrt{2}}\Big[\bar D\,\gamma^{\mu}P_L\,u\;Y'^{\dagger}_{\mu}
+\bar S\,\gamma^{\mu}P_L\,c\;Y'^{\dagger}_{\mu}
+\bar D\,\gamma^{\mu}P_L\,d\;V'^{\dagger}_{\mu}
+\bar S\,\gamma^{\mu}P_L\,s\;V'^{\dagger}_{\mu}\Big].
$$

Points to check term by term:

* The coupling is **purely left-handed** (`ProjM` $=P_L$). There is no $P_R$ piece.
* The strength is the SM weak coupling $g/\sqrt2$ — the same normalisation as
  the SM $W$ current — and it carries `InteractionOrder` NP through `gX`? No:
  `gw` carries no NP order, so these vertices count as QED order in the
  hierarchy `{{QCD,1},{QED,2},{NP,1}}`.
* Electric charge is conserved at each vertex:
  $\bar u D Y'^{+}:\;-\tfrac23-\tfrac13+1=0$; $\;\bar d D V'^{0}:\;+\tfrac13-\tfrac13+0=0$.
* Colour is contracted as a singlet, $\bar u_i \gamma^\mu P_L D_i$.
* `TQ` ($Q=+2/3$) has **no** interaction term anywhere in the file. It appears
  only in its own kinetic and mass term. The same is true of all six new
  scalars (apart from their gauge couplings) and of the three heavy leptons.
  There is no Yukawa sector and no scalar potential in this file.

### `LTotal`

$$
\mathcal{L}_{\rm Total}=\mathcal{L}_{Z'}+\mathcal{L}_{Y'}+\mathcal{L}_{V'}
+\mathcal{L}_{D}+\mathcal{L}_{S}+\mathcal{L}_{T}+\mathcal{L}_{E}
+\mathcal{L}_{H_2}+\mathcal{L}_{H_3}+\mathcal{L}_{H_0}
+\mathcal{L}_{H^{\pm}}+\mathcal{L}_{H_{QY}}+\mathcal{L}_{H_{QV}}
+\mathcal{L}_{\rm NP}^{\rm CC}.
$$

---

## 2. Field table

| `.fr` symbol | Class | Spin | SU(3)$_C$ | SU(2)$_L$ | $Q$ | $Y$ | Self-conj. | Mass symbol | Mass value |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Zp` | `V[101]` | 1 | **1** | singlet (not declared) | 0 | 0 | yes | `MZp` | internal, $\sqrt{(g^2+\beta^2 g_X^2)v_3^2/6}\approx0.58$ TeV |
| `Yp` | `V[102]` | 1 | **1** | singlet | $+1$ | — | no | `MYp` | internal, $\sqrt{g^2(v_3^2+v_2^2)/4}\approx0.65$ TeV |
| `Vp` | `V[103]` | 1 | **1** | singlet | $0$ | — | no | `MVp` | internal, $\sqrt{g^2(v_3^2+v_1^2)/4}\approx0.65$ TeV |
| `DQ` | `F[101]` | 1/2 | **3** | singlet | $-1/3$ | $-1/3$ | no | `MDQ` | 1000 GeV (external, default) |
| `SQ` | `F[102]` | 1/2 | **3** | singlet | $-1/3$ | $-1/3$ | no | `MSQ` | 1000 GeV |
| `TQ` | `F[103]` | 1/2 | **3** | singlet | $+2/3$ | $+2/3$ | no | `MTQ` | 1000 GeV |
| `EL` = {`Ee`,`Emu`,`Etau`} | `F[104]` | 1/2 | **1** | singlet | $0$ | $0$ | no | `MEL` = {`MEE`,`MEM`,`MET`} | 1000 GeV each |
| `H2` | `S[101]` | 0 | **1** | singlet | 0 | 0 | yes | `MH2` | internal, $\approx2.83$ TeV |
| `H3` | `S[102]` | 0 | **1** | singlet | 0 | 0 | yes | `MH3` | internal, $\sqrt{2\lambda_3}\,v_3\approx0.89$ TeV |
| `H0` | `S[103]` | 0 | **1** | singlet | 0 | 0 | yes | `MH0` | internal, $\approx2.83$ TeV |
| `Hpm` | `S[104]` | 0 | **1** | singlet | $+1$ | $+1$ | no | `MHpm` | internal, $\approx2.83$ TeV |
| `HQY` | `S[105]` | 0 | **1** | singlet | $+1$ | $+1$ | no | `MHQY` | internal, $\approx2.06$ TeV |
| `HQV` | `S[106]` | 0 | **1** | singlet | $0$ | $0$ | no | `MHQV` | internal, $\approx2.06$ TeV |

PDG codes run 4000001–4000015. All widths are external with default 1 GeV.
The numeric mass estimates use $v_3=2$ TeV, $k=1$, $\lambda_3=0.1$,
$g\simeq0.652$, $g_X=0.5$, $\beta=1/\sqrt3$ and the base-model `vev`
$\simeq246.2$ GeV; they change if the base model sets `vev` or `gw` differently.

Notes on the table:

* No field declares an SU(2)$_L$ index, so every new state is an electroweak
  singlet **in this file**, even though the mass formulas (below) clearly come
  from a larger broken group.
* `Vp` and `HQV` are electrically neutral but **not** self-conjugate; they carry
  a conserved non-electric charge (bilepton-like) that distinguishes particle
  from antiparticle.
* `EL` carries `Q -> 0` and `Y -> 0` in `QuantumNumbers`, but its surviving
  `FullName` strings read "Heavy charged lepton (… partner)". The two disagree.
  The gauge couplings that FeynRules generates follow `QuantumNumbers`, so these
  states are **neutral** heavy leptons as written. Treat the name as stale.

---

## 3. Parameters

### External

| Symbol | Value | Block / order | Multiplies | Physical meaning |
| --- | --- | --- | --- | --- |
| `beta` | $0.5773502691896258=1/\sqrt3$ | NPINPUTS 1 | enters $M_{Z'}$ only, as $\beta^2 g_X^2$ | the U(1)$_X$ embedding parameter $\beta$ that fixes $Q=T_3-\beta\,T_8+X$ in an SU(3)$_L\times$U(1)$_X$ theory. $\beta=1/\sqrt3$ is the value for which the exotic gauge bosons have charges $+1$ and $0$, as declared here |
| `gX` | 0.5 | NPINPUTS 2, NP order 1 | $M_{Z'}$ | gauge coupling of the extra abelian group U(1)$_X$ |
| `v1` | 173.95 GeV | NPINPUTS 3 | $M_{V'}$, $M_{H_2}$, $M_{H_0}$, $M_{H^\pm}$, $M_{H_{QY}}$, $M_{H_{QV}}$ | first electroweak vacuum expectation value. $173.95\simeq v/\sqrt2$, i.e. the default choice is $v_1=v_2$ |
| `v3` | 2000 GeV | NPINPUTS 4 | $M_{Z'}$, $M_{Y'}$, $M_{V'}$, all scalar masses, $f$ | the high-scale vev that breaks the extended gauge group down to the SM |
| `k` | 1 | NPINPUTS 5 | $f=k\,v_3$ | dimensionless ratio setting the size of the trilinear scalar coupling relative to $v_3$ |
| `lam3` | 0.1 | NPINPUTS 6, NP order 1 | $M_{H_3}^2=2\lambda_3 v_3^2$ | quartic self-coupling of the third (high-scale) scalar multiplet |
| `lampr12` | 0.1 | NPINPUTS 7, NP order 1 | $M_{H^\pm}^2$ | quartic cross-coupling $\lambda'_{12}$ between scalar multiplets 1 and 2 |
| `lampr23` | 0.1 | NPINPUTS 8, NP order 1 | $M_{H_{QY}}^2$ | quartic cross-coupling $\lambda'_{23}$ between multiplets 2 and 3 |
| `lampr13` | 0.1 | NPINPUTS 9, NP order 1 | $M_{H_{QV}}^2$ | quartic cross-coupling $\lambda'_{13}$ between multiplets 1 and 3 |

The exotic fermion masses `MDQ`, `MSQ`, `MTQ`, `MEE`, `MEM`, `MET` and every
width are also external, declared inline in `M$ClassesDescription` with default
value 1000 GeV (widths 1 GeV).

### Internal (derived)

| Symbol | Definition | Meaning |
| --- | --- | --- |
| `v2` | $\sqrt{v^2-v_1^2}$ | second electroweak vev, fixed by $v_1^2+v_2^2=v^2$ so that the $W$ mass is reproduced |
| `f` | $k\,v_3$ | trilinear scalar coupling with mass dimension 1; it sets the mass of the scalars that would otherwise be massless pseudo-Goldstone states |
| `MZp` | $\sqrt{(g^2+\beta^2 g_X^2)\,v_3^2/6}$ | $Z'$ mass |
| `MYp` | $\sqrt{g^2(v_3^2+v_2^2)/4}$ | $Y'^\pm$ mass |
| `MVp` | $\sqrt{g^2(v_3^2+v_1^2)/4}$ | $V'$ mass |
| `MH2` | $\sqrt{(v^2/(v_1v_2))\,f\,v_3}$ | CP-even heavy scalar mass |
| `MH3` | $\sqrt{2\lambda_3 v_3^2}$ | mass of the scalar aligned with the high-scale vev |
| `MH0` | $\sqrt{(v_1v_2/v_3+v_1v_3/v_2+v_2v_3/v_1)\,f}$ | mass of the pseudoscalar; the symmetric $f$-dependent form is the signature of a trilinear-generated CP-odd state |
| `MHpm` | $\sqrt{(2fv_3+\lambda'_{12}v_1v_2)\,v^2/(2v_1v_2)}$ | charged scalar mass |
| `MHQY` | $\sqrt{(2fv_1+\lambda'_{23}v_2v_3)(v_2^2+v_3^2)/(2v_2v_3)}$ | charged scalar mass, high-scale sector |
| `MHQV` | $\sqrt{(2fv_2+\lambda'_{13}v_1v_3)(v_1^2+v_3^2)/(2v_1v_3)}$ | neutral complex scalar mass, high-scale sector |

Every internal mass vanishes in the limit $f\to0$ except `MH3`, which is the
expected behaviour of Goldstone-like states lifted only by the trilinear term.

`M$InteractionOrderHierarchy = {{QCD,1},{QED,2},{NP,1}}` adds an `NP` counter;
`gX`, `lam3` and the three `lampr` couplings carry NP order 1, while the
charged-current vertices in `LNPcc` carry the SM coupling `gw` and so count as
QED.

---

## 4. Physics summary

This is an effective, mass-eigenstate description of an SU(3)$_C\times$SU(3)$_L\times$U(1)$_X$
("331") extension broken at $v_3=2$ TeV with the embedding parameter
$\beta=1/\sqrt3$: the mass formulas for $Z'$, $Y'^{\pm}$ and $V'$ and the three
vevs $v_1,v_2,v_3$ with $v_1^2+v_2^2=v^2$ are exactly the spectrum of three
scalar triplets breaking that group. The new states are one real neutral $Z'$,
a charged bilepton $Y'^{\pm}$ and a non-hermitian neutral bilepton $V'$; three
vector-like exotic quarks ($D$, $S$ with $Q=-1/3$ and $T$ with $Q=+2/3$); three
heavy neutral leptons; and six physical scalars (three real neutral, two singly
charged, one complex neutral). The only new interaction written out is a purely
left-handed charged current of SM weak strength $g/\sqrt2$ that couples the
bileptons to one SM quark and one exotic quark: $\bar u\,D\,Y'$, $\bar c\,S\,Y'$,
$\bar d\,D\,V'$, $\bar s\,S\,V'$.

Processes it mediates: resonant or $t$-channel exchange of $Y'$ and $V'$ in
quark–quark scattering, single production of the exotic quarks $D$ and $S$ in
association with a bilepton, and decays $D\to u\,Y'^{-}$, $D\to d\,\bar V'$,
$S\to c\,Y'^{-}$, $S\to s\,\bar V'$ (or the inverse orderings, set by the mass
hierarchy), all with left-handed chirality only. Because the remaining new
states — $Z'$, $T$, the heavy leptons and all six scalars — appear only in
kinetic and mass terms, they are produced solely through their SM gauge charges
(QCD for $T$, electroweak for the charged scalars) and are completely inert
otherwise: $Z'$, $H_2$, $H_3$, $H_0$, the neutral $H_{QV}$ and the heavy
neutral leptons have **no** vertices at all in this file. Any realistic use of
this model would need the missing Yukawa sector and scalar potential.

### Open points for the reviewer

1. `LZp` carries an explicit overall factor `2`, which is non-canonical for a
   self-conjugate vector (see the note under `LZp`).
2. `EL` is declared with $Q=0$ but its `FullName` strings call it a charged lepton.
3. `TQ` is declared but never interacts; `Zp` is given a mass formula but no current.
