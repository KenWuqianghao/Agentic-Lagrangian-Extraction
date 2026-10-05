# Reconstruction of `sanitized.fr`

## 0. Conventions and notation

The file declares no `QuantumNumbers` and no gauge representations for any new
field, and it contains **no `DC[...]` covariant derivative and no `FS[...]` field
strength**. Every new field is therefore a total singlet of the Standard Model
gauge group, and every derivative in the new terms is a plain partial derivative:

$$
D_\mu \chi = \partial_\mu \chi ,\qquad D_\mu H_2 = \partial_\mu H_2 .
$$

The gauge content of the model is inherited unchanged from the Standard Model
Lagrangian `LSM`, which the file adds through `LTotal`. That is,
$SU(3)_C \times SU(2)_L \times U(1)_Y$ acts only on the SM fields, with the SM
covariant derivative

$$
D_\mu = \partial_\mu - i g_s T^a G^a_\mu - i g \tfrac{\sigma^i}{2} W^i_\mu - i g' Y B_\mu ,
$$

and the new sector is neutral under all three factors.

Symbols used below:

| `.fr` symbol | LaTeX | meaning |
| --- | --- | --- |
| `chi` | $\chi$ | new real scalar, dark matter candidate |
| `H2` | $H_2$ | new real scalar mass eigenstate |
| `H` | $h$ | the SM-file CP-even mass eigenstate (mass `MH`) |
| `phi1` | $\phi_1$ | unphysical CP-even **doublet** direction |
| `s1` | $s_1$ | unphysical CP-even **singlet** direction |
| `vev` | $v$ | SM doublet vacuum expectation value (from `LSM`) |
| `vs` | $v_s$ | singlet vacuum expectation value |
| `thx` | $\theta$ | scalar mixing angle |

The metric contraction is implicit in the FeynRules idiom
`del[chi,mu] del[chi,mu]` $\to \partial_\mu \chi \, \partial^\mu \chi$.
No `HC`, `CC`, `Ga`, `ProjP` or `ProjM` appears: the whole new sector is scalar,
real and parity-blind, so there is no chirality structure and no charge
conjugation to expand.

---

## 1. Lagrangian, term by term

### 1.1 `LX` — free real scalar $\chi$

$$
\mathcal{L}_{\chi}
= \frac{1}{2}\,\partial_\mu \chi \,\partial^\mu \chi
\;-\; \frac{1}{2}\, M_\chi^{2}\, \chi^{2}
$$

$\chi$ is self-conjugate, so the factors of $1/2$ are the canonical real-scalar
normalisation. `Mx` $= M_\chi$.

### 1.2 `LH2` — free real scalar $H_2$

$$
\mathcal{L}_{H_2}
= \frac{1}{2}\,\partial_\mu H_2 \,\partial^\mu H_2
\;-\; \frac{1}{2}\, M_{H_2}^{2}\, H_2^{2}
$$

$H_2$ is also self-conjugate and a gauge singlet in its declaration.

### 1.3 `LPortal3` — trilinear portal, in gauge-direction form

$$
\mathcal{L}_{\rm portal}^{(3)}
= -\frac{1}{2}\,\chi^{2}\Big(\lambda_{\Phi S}\, v \,\phi_1 \;+\; \lambda_{S}\, v_s\, s_1 \Big)
$$

with the two unphysical directions defined (`S[103]`, `S[104]`) as the rotation

$$
\phi_1 = \cos\theta \; h \;+\; \sin\theta \; H_2 ,
\qquad
s_1 = -\sin\theta \; h \;+\; \cos\theta \; H_2 ,
$$

i.e. the inverse of the mass-eigenstate rotation

$$
\begin{pmatrix} h \\ H_2 \end{pmatrix}
=
\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}
\begin{pmatrix} \phi_1 \\ s_1 \end{pmatrix} .
$$

$\phi_1$ is the CP-even fluctuation of the SM doublet, $s_1$ the CP-even
fluctuation of the singlet.

### 1.4 `LPortal3` — same term in the mass basis

Insert the definitions and the internal parameter values

$$
\lambda_{\Phi S} = \frac{(M_{H_2}^2 - M_h^2)\,\sin\theta\cos\theta}{v\,v_s},
\qquad
\lambda_{S} = \frac{M_h^2 \sin^2\theta + M_{H_2}^2 \cos^2\theta}{v_s^2}.
$$

The $h$ coefficient is $\lambda_{\Phi S} v \cos\theta - \lambda_S v_s \sin\theta
= -M_h^2 \sin\theta / v_s$, and the $H_2$ coefficient is
$\lambda_{\Phi S} v \sin\theta + \lambda_S v_s \cos\theta
= +M_{H_2}^2 \cos\theta / v_s$. Hence

$$
\boxed{\;
\mathcal{L}_{\rm portal}^{(3)}
= +\,\frac{M_h^{2}\,\sin\theta}{2\,v_s}\;\chi^{2}\, h
\;-\;\frac{M_{H_2}^{2}\,\cos\theta}{2\,v_s}\;\chi^{2}\, H_2 \; }
$$

Two points a checker should verify, because they are the physical content of the
parameter choices:

1. Each trilinear coupling is proportional to the **square of the mass of the
   scalar that is exchanged**, divided by $v_s$.
2. The two contributions carry opposite signs. In a $t$-channel exchange with
   amplitude $\propto g_{\chi\chi h}/(t - M_h^2) + g_{\chi\chi H_2}/(t - M_{H_2}^2)$,
   the $t \to 0$ limit gives
   $-\sin\theta\cos\theta/v_s \cdot (\,{-1} + 1\,) \cdot \dots = 0$:
   the zero-momentum-transfer amplitude cancels exactly. This is the signature of
   a pseudo-Nambu-Goldstone dark matter construction.

### 1.5 `LTotal`

$$
\mathcal{L}
= \mathcal{L}_{\rm SM}
+ \mathcal{L}_{\chi}
+ \mathcal{L}_{H_2}
+ \mathcal{L}_{\rm portal}^{(3)}
$$

`LSM` is not defined in this file; it comes from the loaded SM model.

### 1.6 What is **not** in the file

For completeness, because a physicist will look for them: the file contains **no**
quartic portal $\chi^2 \phi_1^2$ or $\chi^2 s_1^2$ term, **no** $\chi^4$
self-interaction, **no** scalar potential for $\phi_1/s_1$ beyond the $H_2$ mass
term, and **no** soft $U(1)$-breaking mass term for $\chi$ other than `Mx`.
Only the single trilinear portal `LPortal3` couples the dark sector to the
visible sector.

---

## 2. Field table

| `.fr` class | Symbol | Spin | $SU(3)_C$ | $SU(2)_L$ | $U(1)_Y$ / charge | Self-conjugate | Mass symbol | Mass value | Width | PDG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `S[101]` | $\chi$ | 0 (scalar) | **1** (not declared) | **1** (not declared) | 0 (not declared) | Yes | `Mx` | 62.573 GeV | 0 (stable) | 52 |
| `S[102]` | $H_2$ | 0 (scalar) | **1** (not declared) | **1** (not declared) | 0 (not declared) | Yes | `MH2` | 125.30 GeV | `WH2` $= 0$ | 35 |
| `S[103]` | $\phi_1$ | 0 (scalar) | — | — | — | Yes | unphysical | — | — | — |
| `S[104]` | $s_1$ | 0 (scalar) | — | — | — | Yes | unphysical | — | — | — |

Notes.

- $\chi$ carries `Width -> 0` and no decay operator, so it is absolutely stable:
  the dark matter candidate. Its mass $62.573\ \mathrm{GeV} \simeq M_{H_2}/2$ sits
  right on the Higgs-resonance point.
- $H_2$ is declared with `Width -> {WH2, 0.}`, i.e. a width parameter whose
  numerical value is left at zero for FeynRules to compute or for the card to
  overwrite.
- $\phi_1$ and $s_1$ are `Unphysical -> True`. They are not propagating states;
  FeynRules substitutes their `Definitions` before vertex extraction.
- Since $\theta = 1.53\ \mathrm{rad} \approx 87.7^{\circ}$, we have
  $\sin\theta \approx 0.9995$ and $\cos\theta \approx 0.0408$. Therefore
  $H_2 = \sin\theta\,\phi_1 + \cos\theta\,s_1$ is **almost purely doublet-like**,
  and it is the 125.30 GeV state. The SM-file state $h$ (mass `MH`) is the
  **almost purely singlet-like** state in this convention.

---

## 3. Parameters

### 3.1 External

| Symbol | Block / order | Value | Multiplies | Physical meaning |
| --- | --- | --- | --- | --- |
| `vs` ($v_s$) | `PNGDM`, 1 | 13155.1 GeV | appears in $\lambda_{\Phi S}$, $\lambda_S$ and directly in `LPortal3` as $\lambda_S v_s s_1$ | vacuum expectation value of the singlet. It sets the overall $1/v_s$ suppression of both $\chi\chi h$ and $\chi\chi H_2$ couplings. |
| `thx` ($\theta$) | `PNGDM`, 2 | 1.53 rad ($\approx 87.7^{\circ}$) | enters through `sxth`, `cxth` in the $\phi_1$, $s_1$ definitions | mixing angle between the doublet direction $\phi_1$ and the singlet direction $s_1$. |

### 3.2 Internal (derived)

| Symbol | Value | Multiplies | Physical meaning |
| --- | --- | --- | --- |
| `sxth` | $\sin\theta$ | the $H_2$ part of $\phi_1$ and (with a minus sign) the $h$ part of $s_1$ | sine of the scalar mixing angle. |
| `cxth` | $\cos\theta$ | the $h$ part of $\phi_1$ and the $H_2$ part of $s_1$ | cosine of the scalar mixing angle. |
| `lamPS` ($\lambda_{\Phi S}$) | $(M_{H_2}^2 - M_h^2)\sin\theta\cos\theta/(v\,v_s)$, `InteractionOrder -> {NP,2}` | $-\tfrac12 \chi^2 v \phi_1$ | Higgs-portal quartic coupling between the doublet and the dark scalar bilinear. It is fixed, not free: it is the value that reproduces the observed mass splitting for the given mixing. |
| `lamS` ($\lambda_S$) | $(M_h^2\sin^2\theta + M_{H_2}^2\cos^2\theta)/v_s^2$, `InteractionOrder -> {NP,2}` | $-\tfrac12 \chi^2 v_s s_1$ | singlet quartic coupling. Also fixed by the mass eigenvalues and the mixing angle. |

`MH`, `vev` and everything in `LSM` are external inputs of the loaded Standard
Model file, not of this file.

`M$InteractionOrderHierarchy` declares `{QCD,1}, {QED,2}, {NP,1}`, so the new
couplings are counted in a separate `NP` order; both portal couplings carry
`NP = 2`.

---

## 4. Physics summary

This is a real-scalar Higgs-portal dark matter model with an extended CP-even
scalar sector: a stable, gauge-singlet real scalar $\chi$ (62.573 GeV, PDG 52)
plus a second CP-even mass eigenstate $H_2$ (125.30 GeV, PDG 35) that mixes with
the SM-like CP-even scalar through an angle $\theta = 1.53$. The singlet gets a
large vacuum expectation value $v_s = 13.16$ TeV, and the two portal couplings
are not free: they are fixed by the two scalar masses, the mixing angle and the
two vacuum expectation values, so that the trilinear couplings come out as
$+M_h^2\sin\theta/(2 v_s)$ for $\chi\chi h$ and $-M_{H_2}^2\cos\theta/(2 v_s)$
for $\chi\chi H_2$.

Those two couplings have opposite signs and scale with the exchanged scalar's own
mass squared, so the spin-independent dark-matter–nucleon scattering amplitude
cancels exactly at zero momentum transfer. This is the defining property of a
pseudo-Nambu-Goldstone dark matter candidate: $\chi$ behaves as the would-be
Goldstone boson of a broken global symmetry of the singlet, with only a soft mass
term $M_\chi$.

Processes mediated by this file: $s$-channel scalar exchange giving
$\chi\chi \to f\bar f, VV, hh$ annihilation (near-resonant, since
$2 M_\chi \approx M_{H_2}$, which is how the relic density is obtained); invisible
decay $H_2 \to \chi\chi$ and $h \to \chi\chi$ where phase space allows; mono-X and
vector-boson-fusion missing-energy signals at colliders through an off-shell
mixed scalar; and loop-level or momentum-suppressed direct detection, since the
tree-level zero-momentum amplitude vanishes.
