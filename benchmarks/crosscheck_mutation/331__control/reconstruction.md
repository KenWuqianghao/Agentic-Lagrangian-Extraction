# Reconstruction of `sanitized.fr`

## 0. Scope and conventions

The file is **not a stand-alone model**. It declares no `M$GaugeGroups`, no `M$IndexDefinitions`,
and it uses symbols it never defines: `vev`, `gw`, `u`, `c`, `d`, `s`, and the gauge fields implied
by `DC[...]`. It is therefore a **new-physics module loaded on top of a Standard Model `.fr` file**,
and it extends that model with new vectors, new fermions and new scalars.

Conventions used below:

| FeynRules idiom | Standard notation |
| --- | --- |
| `Ga[mu]` | $\gamma^\mu$ |
| `ProjM` | $P_L=\tfrac{1}{2}(1-\gamma_5)$ |
| `ProjP` | $P_R=\tfrac{1}{2}(1+\gamma_5)$ |
| `Xbar` | $\bar X=X^\dagger\gamma^0$ (fermion) or $X^\dagger$ (scalar/vector) |
| `FS[X,mu,nu]` | $X_{\mu\nu}=\partial_\mu X_\nu-\partial_\nu X_\mu$ (see note) |
| `DC[X,mu]` | $D_\mu X$ (gauge content below) |
| `HC[L]` | $L+\text{h.c.}$ partner term |
| `del[X,mu]` | $\partial_\mu X$ |

**Note on `FS`.** `Zp`, `Yp` and `Vp` are *not* gauge fields of any declared group. `FS` therefore
reduces to the abelian curl $\partial_\mu X_\nu-\partial_\nu X_\mu$, with **no** non-abelian
self-couplings and **no** photon/gluon terms inside the field strength.

### Covariant derivative content

`DC` acts with the gauge groups of the underlying SM file, using each field's declared indices and
quantum numbers. No new field in this file carries `Index[SU2D]`, so **every new state is an
$SU(2)_L$ singlet** ($T^3=0$), and consistently every declared pair satisfies $Q=Y$.

For a colour-triplet fermion $\psi$ with hypercharge $Y$:

$$
D_\mu \psi=\Big(\partial_\mu-i g_s G^a_\mu T^a-i g_1 Y B_\mu\Big)\psi ,
\qquad T^a=\tfrac{\lambda^a}{2}
$$

For a colour-singlet field $\phi$ with hypercharge $Y$:

$$
D_\mu \phi=\Big(\partial_\mu-i g_1 Y B_\mu\Big)\phi
$$

In the mass basis, with $T^3=0$ and $Q=Y$, $g_1YB_\mu=eQ\big(A_\mu-\tan\theta_W Z_\mu\big)$, so

$$
D_\mu=\partial_\mu-i g_s G^a_\mu T^a-i e Q\big(A_\mu-\tan\theta_W\,Z_\mu\big)
$$

(the gluon piece only for colour triplets). For $Y=0$ states (`EL`, `HQV`) the covariant derivative
degenerates to $\partial_\mu$.

**The new vectors `Zp`, `Yp`, `Vp` do not appear in any `DC`.** They couple to matter *only* through
the single explicit term `LNPcc`.

---

## 1. Lagrangian (term by term)

### `LZp` — neutral heavy vector, kinetic + mass

$$
\mathcal{L}_{Z'}=-\frac{1}{4}Z'_{\mu\nu}Z'^{\mu\nu}+\frac{1}{2}M_{Z'}^{2}Z'_\mu Z'^\mu ,
\qquad Z'_{\mu\nu}=\partial_\mu Z'_\nu-\partial_\nu Z'_\mu
$$

Real (self-conjugate) Proca field: the $1/4$ and $1/2$ normalisations are the real-field ones.

### `LYp` — singly charged heavy vector, kinetic + mass

$$
\mathcal{L}_{Y'}=-\frac{1}{2}Y'^{\dagger}_{\mu\nu}Y'^{\mu\nu}+M_{Y'}^{2}\,Y'^{\dagger}_\mu Y'^\mu ,
\qquad Y'_{\mu\nu}=\partial_\mu Y'_\nu-\partial_\nu Y'_\mu
$$

Complex Proca field ($1/2$ and $1$ normalisations). Note that the kinetic term is written with the
*ordinary* derivative curl, **not** $D_\mu$: as written, the $Q=+1$ vector $Y'$ has **no photon
coupling**. This is an internal inconsistency of the file (a charged field whose kinetic term is not
gauged), and it is flagged here rather than silently repaired.

### `LVp` — neutral but complex heavy vector, kinetic + mass

$$
\mathcal{L}_{V'}=-\frac{1}{2}V'^{\dagger}_{\mu\nu}V'^{\mu\nu}+M_{V'}^{2}\,V'^{\dagger}_\mu V'^\mu ,
\qquad V'_{\mu\nu}=\partial_\mu V'_\nu-\partial_\nu V'_\mu
$$

$V'$ has $Q=0$ but is **not** self-conjugate: it carries a conserved non-electromagnetic charge
(particle/antiparticle are distinct — a "bilepton-like" quantum number).

### `LDQ`, `LSQ`, `LTQ` — exotic quark kinetic + Dirac mass

$$
\mathcal{L}_{D}= i\,\bar D\,\gamma^\mu D_\mu D-M_D\,\bar D D,
\qquad
D_\mu D=\Big(\partial_\mu-ig_sG^a_\mu T^a-ig_1\big(-\tfrac13\big)B_\mu\Big)D
$$

$$
\mathcal{L}_{S}= i\,\bar S\,\gamma^\mu D_\mu S-M_S\,\bar S S,
\qquad Y_S=-\tfrac13
$$

$$
\mathcal{L}_{T}= i\,\bar T\,\gamma^\mu D_\mu T-M_T\,\bar T T,
\qquad Y_T=+\tfrac23
$$

All three are **vector-like Dirac** colour triplets: the mass term $-M\bar\psi\psi$ is explicit and
chirality-mixing, so left and right components share identical gauge charges. No chiral projector
appears, so the gauge couplings are purely **vector-like** (no $\gamma_5$).

### `LEL` — heavy lepton kinetic + diagonal masses

$$
\mathcal{L}_{E}= i\sum_{i}\bar E_i\,\gamma^\mu \partial_\mu E_i
-M_{E_e}\bar E_e E_e-M_{E_\mu}\bar E_\mu E_\mu-M_{E_\tau}\bar E_\tau E_\tau
$$

The generation index $i\in\{e,\mu,\tau\}$ is summed implicitly by the `EL` class. Because
$Y_E=0$ and $E$ is colourless, $D_\mu E=\partial_\mu E$ — these leptons are **gauge-inert**. The mass
term is written member by member (`MEE`, `MEM`, `MET`), i.e. diagonal in generation, not via the
class symbol `MEL`.

### `LH2`, `LH3`, `LH0` — three real neutral scalars

$$
\mathcal{L}_{H_2}=\frac{1}{2}\,\partial_\mu H_2\,\partial^\mu H_2-\frac{1}{2}M_{H_2}^{2}H_2^{2}
$$

$$
\mathcal{L}_{H_3}=\frac{1}{2}\,\partial_\mu H_3\,\partial^\mu H_3-\frac{1}{2}M_{H_3}^{2}H_3^{2}
$$

$$
\mathcal{L}_{H_0}=\frac{1}{2}\,\partial_\mu H_0\,\partial^\mu H_0-\frac{1}{2}M_{H_0}^{2}H_0^{2}
$$

Real scalars, so $\partial_\mu$ (not $D_\mu$) is correct.

### `LHpm` — singly charged complex scalar

$$
\mathcal{L}_{H^\pm}=\big(D_\mu H^{+}\big)^{\dagger}\big(D^{\mu}H^{+}\big)-M_{H^\pm}^{2}\,H^{-}H^{+},
\qquad D_\mu H^{+}=\big(\partial_\mu-ig_1(+1)B_\mu\big)H^{+}
$$

Equivalently $D_\mu H^{+}=\big(\partial_\mu-ie(A_\mu-\tan\theta_W Z_\mu)\big)H^{+}$.

### `LHQY` — second singly charged complex scalar

$$
\mathcal{L}_{H_{QY}}=\big(D_\mu H_{QY}\big)^{\dagger}\big(D^{\mu}H_{QY}\big)-M_{H_{QY}}^{2}\,H_{QY}^{\dagger}H_{QY},
\qquad Q=Y=+1
$$

Same gauge content as $H^\pm$; it is a distinct state with an independent mass.

### `LHQV` — neutral complex scalar

$$
\mathcal{L}_{H_{QV}}=\partial_\mu H_{QV}^{\dagger}\,\partial^{\mu}H_{QV}-M_{H_{QV}}^{2}\,H_{QV}^{\dagger}H_{QV}
$$

$Q=Y=0$, so $D_\mu\to\partial_\mu$; complex, hence carrying a conserved global charge, the scalar
counterpart of $V'$.

### `LNPcc` — the only interaction term in the file

$$
\mathcal{L}_{\rm NP\text{-}cc}=
\frac{g_w}{\sqrt{2}}\Big[
\bar u\,\gamma^\mu P_L\,D\;Y'_\mu+
\bar c\,\gamma^\mu P_L\,S\;Y'_\mu+
\bar d\,\gamma^\mu P_L\,D\;V'_\mu+
\bar s\,\gamma^\mu P_L\,S\;V'_\mu\Big]+\text{h.c.}
$$

Written out, the hermitian conjugate half is

$$
\frac{g_w}{\sqrt{2}}\Big[
\bar D\,\gamma^\mu P_L\,u\;Y'^{\dagger}_\mu+
\bar S\,\gamma^\mu P_L\,c\;Y'^{\dagger}_\mu+
\bar D\,\gamma^\mu P_L\,d\;V'^{\dagger}_\mu+
\bar S\,\gamma^\mu P_L\,s\;V'^{\dagger}_\mu\Big]
$$

Points of precision:

* **Chirality.** `ProjM` $=P_L$. The current is **purely left-handed**: $\bar q\gamma^\mu P_L\psi$.
  In the h.c. term the projector stays $P_L$ because
  $\big(\bar q\gamma^\mu P_L\psi\big)^\dagger=\bar\psi\gamma^\mu P_L q$.
* **Colour.** The `Colour` index is contracted implicitly between the SM quark and the exotic quark;
  the current is a colour singlet, so $Y'$ and $V'$ are **colour singlets**.
* **Charge.** $\bar u\,\Gamma\,D\,Y'$: $-\tfrac23+(-\tfrac13)+Q_{Y'}=0\Rightarrow Q_{Y'}=+1$. ✔
  $\bar d\,\Gamma\,D\,V'$: $+\tfrac13+(-\tfrac13)+Q_{V'}=0\Rightarrow Q_{V'}=0$. ✔
  Charges are consistent with the class declarations.
* **Pairing.** First generation quarks $(u,d)$ pair only with $D$; second generation $(c,s)$ pair
  only with $S$. There is **no** $b$/$t$ current and **no** current involving `TQ` anywhere in the
  file.
* **No charge conjugation.** `CC` does not appear; every current is of the $\bar\psi\Gamma\chi$ type,
  not $\psi^c$.
* **Coupling strength.** The prefactor is the SM weak coupling $g_w/\sqrt2$, i.e. exactly the SM
  charged-current normalisation, and it carries no `InteractionOrder`, so these vertices count as
  QED order, not `NP`.

### `LTotal`

$$
\mathcal{L}_{\rm total}=\mathcal{L}_{Z'}+\mathcal{L}_{Y'}+\mathcal{L}_{V'}
+\mathcal{L}_{D}+\mathcal{L}_{S}+\mathcal{L}_{T}+\mathcal{L}_{E}
+\mathcal{L}_{H_2}+\mathcal{L}_{H_3}+\mathcal{L}_{H_0}
+\mathcal{L}_{H^\pm}+\mathcal{L}_{H_{QY}}+\mathcal{L}_{H_{QV}}
+\mathcal{L}_{\rm NP\text{-}cc}
$$

The SM Lagrangian itself is not added here; it comes from the file this module is loaded with.

---

## 2. Field table

| `.fr` class | Symbol | Spin | $SU(3)_C$ | $SU(2)_L$ | $Q$ | $Y$ | Self-conj. | Mass symbol | Mass value | PDG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `V[101]` `Zp` | $Z'_\mu$ | 1 | **1** | **1** (not declared) | 0 | 0 | yes | `MZp` | internal | 4000001 |
| `V[102]` `Yp` | $Y'^{\pm}_\mu$ | 1 | **1** | **1** | $+1$ | — | no | `MYp` | internal | 4000002 |
| `V[103]` `Vp` | $V'_\mu$ | 1 | **1** | **1** | $0$ | — | no | `MVp` | internal | 4000003 |
| `F[101]` `DQ` | $D$ | 1/2 | **3** | **1** | $-1/3$ | $-1/3$ | no | `MDQ` | 1000 GeV | 4000004 |
| `F[102]` `SQ` | $S$ | 1/2 | **3** | **1** | $-1/3$ | $-1/3$ | no | `MSQ` | 1000 GeV | 4000005 |
| `F[103]` `TQ` | $T$ | 1/2 | **3** | **1** | $+2/3$ | $+2/3$ | no | `MTQ` | 1000 GeV | 4000006 |
| `F[104]` `EL` | $E_e,E_\mu,E_\tau$ | 1/2 | **1** | **1** | $0$ | $0$ | no | `MEE`,`MEM`,`MET` | 1000 GeV each | 4000007–9 |
| `S[101]` `H2` | $H_2$ | 0 | **1** | **1** | 0 | 0 | yes | `MH2` | internal | 4000010 |
| `S[102]` `H3` | $H_3$ | 0 | **1** | **1** | 0 | 0 | yes | `MH3` | internal | 4000011 |
| `S[103]` `H0` | $H_0$ | 0 | **1** | **1** | 0 | 0 | yes | `MH0` | internal | 4000012 |
| `S[104]` `Hpm` | $H^{\pm}$ | 0 | **1** | **1** | $+1$ | $+1$ | no | `MHpm` | internal | 4000013 |
| `S[105]` `HQY` | $H_{QY}^{\pm}$ | 0 | **1** | **1** | $+1$ | $+1$ | no | `MHQY` | internal | 4000014 |
| `S[106]` `HQV` | $H_{QV}$ | 0 | **1** | **1** | $0$ | $0$ | no | `MHQV` | internal | 4000015 |

Notes on the table:

* No field declares `Index[SU2D]`, so all are electroweak singlets. This is confirmed by $Q=Y$ for
  every field that declares both, which is $Q=T^3+Y$ with $T^3=0$.
* Only `DQ`, `SQ`, `TQ` carry `Index[Colour]`; everything else is a colour singlet.
* `Yp` and `Vp` declare `Q` but no `Y`, so their `DC` coupling is never used — consistent with the
  fact that their kinetic terms use `FS`, not `DC`.
* `EL` declares $Q=0$ while its `FullName` strings read "Heavy charged lepton". The quantum numbers
  are authoritative: these states are **electrically neutral**, heavy, gauge-inert Dirac leptons.
  This is a documented internal inconsistency of the file.
* All widths are placeholders (`1.` GeV), not computed values.

---

## 3. Parameters

### External

| Symbol | Value | Block / order | Where it enters | Physical meaning |
| --- | --- | --- | --- | --- |
| `beta` | $0.5773502691896258=1/\sqrt3$ | `NPINPUTS` 1 | $M_{Z'}$ | Dimensionless embedding/mixing parameter fixing how the extra $U(1)$ generator sits inside the extended gauge group; it weights $g_X$ in the $Z'$ mass. The exact value $1/\sqrt3$ is a specific choice, not a free scan point. |
| `gX` | $0.5$ | `NPINPUTS` 2, `NP` 1 | $M_{Z'}$ | Gauge coupling of the extra abelian factor $U(1)_X$. |
| `v1` | $173.95$ GeV | `NPINPUTS` 3 | $v_2$, $M_{H_2}$, $M_{V'}$, $M_{H^\pm}$, $M_{H_{QY}}$, $M_{H_{QV}}$, $M_{H_0}$ | First electroweak-scale vacuum expectation value. Numerically $\approx v_{\rm SM}/\sqrt2$, so $v_1\simeq v_2$. |
| `v3` | $2000$ GeV | `NPINPUTS` 4 | $f$, $M_{Z'}$, $M_{Y'}$, $M_{V'}$, all scalar masses | High-scale vev that breaks the extended gauge group down to the SM. It sets the whole new-physics mass scale. |
| `k` | $1$ | `NPINPUTS` 5 | $f=k\,v_3$ | Dimensionless coefficient of the trilinear scalar term; it converts $v_3$ into the dimension-one soft parameter $f$. |
| `lam3` | $0.1$ | `NPINPUTS` 6, `NP` 1 | $M_{H_3}^2=2\lambda_3 v_3^2$ | Quartic self-coupling of the high-scale scalar multiplet; it alone fixes the mass of the $v_3$-direction CP-even scalar $H_3$. |
| `lampr12` | $0.1$ | `NPINPUTS` 7, `NP` 1 | $M_{H^\pm}$ | Quartic portal coupling between scalar multiplets 1 and 2 ($\lambda'_{12}$); it shifts the mass of the charged scalar built from the $v_1$–$v_2$ pair. |
| `lampr23` | $0.1$ | `NPINPUTS` 8, `NP` 1 | $M_{H_{QY}}$ | Quartic portal coupling between multiplets 2 and 3 ($\lambda'_{23}$). |
| `lampr13` | $0.1$ | `NPINPUTS` 9, `NP` 1 | $M_{H_{QV}}$ | Quartic portal coupling between multiplets 1 and 3 ($\lambda'_{13}$). |

### Internal (derived)

| Symbol | Definition | Meaning |
| --- | --- | --- |
| `v2` | $v_2=\sqrt{v_{\rm SM}^2-v_1^2}$ | Second electroweak vev, fixed by the constraint $v_1^2+v_2^2=v_{\rm SM}^2$ so that $M_W$ stays at its measured value. With $v_1=173.95$ GeV this gives $v_2\simeq174$ GeV, i.e. $\tan\beta_{12}\simeq1$. |
| `f` | $f=k\,v_3$ | Dimension-one trilinear scalar coupling. It is the source of all the "$f\,v$"-type pseudo-Goldstone masses below; $f\to0$ makes $H_0$, $H_2$ massless. |
| `MZp` | $M_{Z'}=\sqrt{(g_w^2+\beta^2 g_X^2)\,v_3^2/6}$ | Neutral heavy gauge boson mass from $v_3$ breaking. Numerically $\approx 550$ GeV for the given inputs. |
| `MYp` | $M_{Y'}=\sqrt{g_w^2(v_3^2+v_2^2)/4}$ | Charged heavy vector mass; the $g_w^2 v^2/4$ form is the $W$-mass formula generalised to $v_3^2+v_2^2$. |
| `MVp` | $M_{V'}=\sqrt{g_w^2(v_3^2+v_1^2)/4}$ | Neutral complex heavy vector mass, same form with $v_3^2+v_1^2$. |
| `MH2` | $M_{H_2}=\sqrt{(v_{\rm SM}^2/(v_1v_2))\,f\,v_3}$ | Mass of the second neutral CP-even scalar; vanishes with $f$ (pseudo-Goldstone). |
| `MH3` | $M_{H_3}=\sqrt{2\lambda_3 v_3^2}$ | Mass of the high-scale CP-even scalar; the only scalar mass set by a quartic alone. |
| `MH0` | $M_{H_0}=\sqrt{\left(\frac{v_1v_2}{v_3}+\frac{v_1v_3}{v_2}+\frac{v_2v_3}{v_1}\right)f}$ | Mass of the CP-odd neutral scalar; the fully symmetric combination in $v_1,v_2,v_3$ is the standard $f$-induced pseudoscalar mass. |
| `MHpm` | $M_{H^\pm}=\sqrt{(2fv_3+\lambda'_{12}v_1v_2)\,v_{\rm SM}^2/(2v_1v_2)}$ | Charged scalar mass, with both an $f$ piece and a quartic piece. |
| `MHQY` | $M_{H_{QY}}=\sqrt{(2fv_1+\lambda'_{23}v_2v_3)(v_2^2+v_3^2)/(2v_2v_3)}$ | Second charged scalar, built from the 2–3 vev pair. |
| `MHQV` | $M_{H_{QV}}=\sqrt{(2fv_2+\lambda'_{13}v_1v_3)(v_1^2+v_3^2)/(2v_1v_3)}$ | Neutral complex scalar, built from the 1–3 vev pair. |

The mass formulae reuse `gw`, `vev` and (implicitly) `g1` from the underlying SM file, confirming
that this module extends an existing SM implementation.

**Interaction-order hierarchy.** `M$InteractionOrderHierarchy = {{QCD,1},{QED,2},{NP,1}}`: one new
coupling order `NP` is declared alongside QCD and QED. Only `gX`, `lam3` and the three `lampr*`
carry `NP` order, and none of them enters a vertex — they appear only inside mass expressions.

---

## 4. Physics summary

This is a **heavy-gauge-boson extension of the Standard Model with a three-vev scalar sector and a
family of vector-like exotic quarks and neutral heavy leptons**. The gauge sector adds a real
neutral $Z'$, a singly charged vector $Y'^{\pm}$ and a neutral-but-complex vector $V'$, whose masses
all scale with a single high vev $v_3=2$ TeV and whose mass formulae ($M_{Z'}^2\propto(g_w^2+\beta^2
g_X^2)v_3^2/6$, with $\beta=1/\sqrt3$) point to an enlarged $SU(3)_C\times SU(3)_L\times U(1)_X$-type
gauge structure that has been broken down to the SM and then integrated into an SM file as explicit
massive states. The matter sector adds vector-like colour triplets $D,S$ ($Q=-1/3$) and $T$
($Q=+2/3$) at 1 TeV, three gauge-inert neutral heavy leptons, and nine scalar degrees of freedom
(three real neutrals, two singly charged, one neutral complex) whose masses are generated by the
trilinear parameter $f=k v_3$ and three quartic portal couplings.

Phenomenologically, the only non-gauge interaction in the file is a purely left-handed
charged-current coupling of SM quarks to the exotic quarks through $Y'$ and $V'$, with SM weak
strength $g_w/\sqrt2$: $u\!-\!D\!-\!Y'$, $c\!-\!S\!-\!Y'$, $d\!-\!D\!-\!V'$, $s\!-\!S\!-\!V'$. It
would therefore mediate single and pair production of the exotic quarks $D,S$ in association with
first- and second-generation quarks, $s$-channel $Y'/V'$ exchange in $q\bar q$ scattering giving
quark-plus-exotic-quark final states, and decays $D\to u\,Y'^{-}$ / $D\to d\,V'^{\dagger}$ (or the
off-shell three-body analogues, since $M_D=1$ TeV sits below $M_{Y'},M_{V'}\simeq1$ TeV only
marginally).

**Coverage gaps worth flagging to a physicist reader.** The file is interaction-poor relative to its
particle content: `TQ`, all three heavy leptons, all six new scalars and the $Z'$ have **no** vertex
beyond their gauge/kinetic terms, and the $Z'$ in particular is completely decoupled and would be
stable. There is no scalar potential, no Yukawa sector, and no third-generation exotic current. The
charged vectors $Y'^{\pm}$ are given ungauged (`FS`, not `DC`) kinetic terms despite carrying $Q=1$,
so they have no photon coupling as written. These are properties of the file as given, not of the
reconstruction.
