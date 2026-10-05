# Reconstruction of `sanitized.fr`

All statements below come only from the content of `sanitized.fr`. The model name,
authors and comments were removed, so no external model identity is assumed.

## 0. Conventions and gauge content

The file declares **no** gauge indices and **no** `QuantumNumbers` for any new field.
Every new field is therefore a total singlet:

$$(\mathbf{1},\mathbf{1},0) \quad \text{under } SU(3)_C\times SU(2)_L\times U(1)_Y .$$

Consequently the covariant derivative that acts on the new fields reduces to the
ordinary partial derivative:

$$D_\mu \chi = \partial_\mu \chi , \qquad D_\mu H_2 = \partial_\mu H_2 .$$

The file uses only `del[field, mu]` (ordinary $\partial_\mu$). It never uses `DC`,
`FS`, `Ga`, `HC`, `CC`, `ProjP` or `ProjM`. There are no fermions, no field
strengths, no chiral projectors and no charge conjugation in this file. The full
SM covariant derivative,

$$D_\mu \Phi = \left(\partial_\mu - i g_s T^a G^a_\mu - i g \tfrac{\sigma^i}{2} W^i_\mu - i g' Y B_\mu\right)\Phi ,$$

enters only through `LSM`, which this file imports but does not define. `LSM` also
supplies the kinetic and Yukawa terms of the SM Higgs mass eigenstate `H`.

`Block[{mu}, ...]` only declares `mu` as a local dummy index. A repeated `mu` in
`del[X,mu] del[X,mu]` is contracted with the metric, i.e. $\partial_\mu X \partial^\mu X$.

Symbol map used below: $\chi \equiv$ `chi`, $M_\chi \equiv$ `Mx`,
$H_2 \equiv$ `H2`, $\phi_1 \equiv$ `phi1`, $s_1 \equiv$ `s1`, $H \equiv$ `H`
(SM Higgs mass eigenstate from `LSM`), $\theta \equiv$ `thx`,
$s_\theta \equiv$ `sxth`, $c_\theta \equiv$ `cxth`, $v \equiv$ `vev`,
$v_s \equiv$ `vs`, $\lambda_{\Phi S} \equiv$ `lamPS`, $\lambda_S \equiv$ `lamS`.

---

## 1. Lagrangian, term by term

### 1.1 Scalar mixing (definitions of the unphysical fields)

`S[103]` (`phi1`) and `S[104]` (`s1`) are declared `Unphysical`. They are the
interaction-basis real scalars. They rotate into the two mass eigenstates $H$ and
$H_2$ by one angle $\theta$:

$$\phi_1 \;=\; c_\theta\, H \;+\; s_\theta\, H_2 ,$$

$$s_1 \;=\; -\,s_\theta\, H \;+\; c_\theta\, H_2 ,$$

$$\begin{pmatrix}\phi_1\\ s_1\end{pmatrix}
=\begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta\end{pmatrix}
\begin{pmatrix} H\\ H_2\end{pmatrix}. \qquad \text{(`S[103]`, `S[104]`)}$$

$\phi_1$ is the neutral CP-even fluctuation of the SM doublet; it is the field that
carries the SM Yukawa and gauge couplings. $s_1$ is the CP-even fluctuation of a
gauge-singlet scalar with vacuum expectation value $v_s$.

### 1.2 `LX` — kinetic and mass term of the dark scalar

The file writes, literally:

```
LX := 2 (Block[{mu}, 1/2 del[chi,mu] del[chi,mu] - 1/2 Mx^2 chi^2];

)
```

Read as physics, this is

$$\boxed{\;\mathcal{L}_{\rm X} \;=\; 2\left[\tfrac{1}{2}\,\partial_\mu \chi\,\partial^\mu \chi
\;-\; \tfrac{1}{2} M_\chi^2\, \chi^2\right]
\;=\; \partial_\mu \chi\,\partial^\mu \chi \;-\; M_\chi^2\,\chi^2 \;}
\qquad \text{(`LX`)}$$

**Anomaly (flagged, not silently corrected).** The overall factor `2` is not the
canonical normalisation. A real self-conjugate scalar must have
$\tfrac12 \partial_\mu\chi\partial^\mu\chi - \tfrac12 M_\chi^2\chi^2$. Every other
term in the file (`LH2`, `LPortal3`, `LPortal4`) uses the canonical convention, and
the internal parameter definitions `lamPS` and `lamS` also assume canonical fields.
So the factor `2` is inconsistent with the rest of the file. See Section 5.

**Syntax note.** The parenthesised block is a Mathematica `CompoundExpression` that
ends with `;`, so `(expr;)` returns `Null`. Taken literally, `LX` evaluates to
`2 Null`, not to a Lagrangian. The intended expression is the boxed one above.

### 1.3 `LH2` — kinetic and mass term of the second CP-even scalar

$$\mathcal{L}_{H_2} \;=\; \tfrac{1}{2}\,\partial_\mu H_2\,\partial^\mu H_2
\;-\; \tfrac{1}{2} M_{H_2}^2\, H_2^2 \qquad \text{(`LH2`)}$$

$H$ gets its kinetic and mass terms from `LSM`, so they are not repeated here.

### 1.4 `LPortal3` — cubic portal terms

Interaction basis:

$$\mathcal{L}_{\rm Portal3} \;=\; -\tfrac{1}{2}\,\chi^2
\Big( \lambda_{\Phi S}\, v\, \phi_1 \;+\; \lambda_S\, v_s\, s_1 \Big)
\qquad \text{(`LPortal3`)}$$

Mass basis (substitute Section 1.1):

$$\mathcal{L}_{\rm Portal3} \;=\;
-\tfrac{1}{2}\Big(\lambda_{\Phi S} v\, c_\theta - \lambda_S v_s\, s_\theta\Big)\chi^2 H
\;-\;\tfrac{1}{2}\Big(\lambda_{\Phi S} v\, s_\theta + \lambda_S v_s\, c_\theta\Big)\chi^2 H_2 .$$

With the internal definitions of $\lambda_{\Phi S}$ and $\lambda_S$ (Section 3) the
two brackets collapse to a very compact form:

$$g_{\chi\chi H} \equiv \lambda_{\Phi S} v c_\theta - \lambda_S v_s s_\theta = -\,\frac{M_H^2\, s_\theta}{v_s} ,
\qquad
g_{\chi\chi H_2} \equiv \lambda_{\Phi S} v s_\theta + \lambda_S v_s c_\theta = +\,\frac{M_{H_2}^2\, c_\theta}{v_s} .$$

$$\mathcal{L}_{\rm Portal3} \;=\; \frac{M_H^2\, s_\theta}{2 v_s}\,\chi^2 H
\;-\; \frac{M_{H_2}^2\, c_\theta}{2 v_s}\,\chi^2 H_2 .$$

This relation is the key fingerprint of the model; see Section 4.

### 1.5 `LPortal4` — quartic portal and dark self-coupling

Interaction basis:

$$\mathcal{L}_{\rm Portal4} \;=\;
-\tfrac{1}{4}\,\lambda_{\Phi S}\,\phi_1^2\,\chi^2
\;-\;\tfrac{1}{4}\,\lambda_S\, s_1^2\,\chi^2
\;-\;\tfrac{1}{8}\,\lambda_S\,\chi^4
\qquad \text{(`LPortal4`)}$$

Mass basis:

$$\mathcal{L}_{\rm Portal4} \;=\;
-\tfrac{1}{4}\Big(\lambda_{\Phi S} c_\theta^2 + \lambda_S s_\theta^2\Big)\chi^2 H^2
-\tfrac{1}{4}\Big(\lambda_{\Phi S} s_\theta^2 + \lambda_S c_\theta^2\Big)\chi^2 H_2^2$$

$$\qquad\qquad
-\tfrac{1}{2}\Big(\lambda_{\Phi S} - \lambda_S\Big) s_\theta c_\theta\, \chi^2 H H_2
\;-\;\tfrac{1}{8}\,\lambda_S\,\chi^4 .$$

### 1.6 `LTotal`

$$\mathcal{L}_{\rm Total} \;=\; \mathcal{L}_{\rm SM} + \mathcal{L}_{\rm X}
+ \mathcal{L}_{H_2} + \mathcal{L}_{\rm Portal3} + \mathcal{L}_{\rm Portal4}
\qquad \text{(`LTotal`)}$$

### 1.7 The scalar potential these terms come from

All $\chi$-dependent terms of `LPortal3` and `LPortal4` are reproduced exactly by

$$V \;\supset\; \frac{\lambda_S}{2}\,|S|^4 \;+\; \lambda_{\Phi S}\,|\Phi|^2 |S|^2 ,
\qquad
S=\frac{v_s + s_1 + i\chi}{\sqrt{2}},\qquad
\Phi^0=\frac{v+\phi_1}{\sqrt{2}} ,$$

because

$$\frac{\lambda_S}{2}|S|^4 \supset \frac{\lambda_S}{2} v_s s_1 \chi^2
+ \frac{\lambda_S}{4} s_1^2 \chi^2 + \frac{\lambda_S}{8}\chi^4 ,
\qquad
\lambda_{\Phi S}|\Phi|^2|S|^2 \supset \frac{\lambda_{\Phi S}}{2} v\,\phi_1 \chi^2
+ \frac{\lambda_{\Phi S}}{4}\phi_1^2 \chi^2 .$$

$\chi$ is the imaginary (CP-odd) part of the complex singlet $S$. The quadratic
terms of $V$ (the $\mu^2$ terms and the $U(1)$-breaking $S^2 + \text{h.c.}$ term)
do not appear in the file. They are traded for the physical inputs $M_\chi$,
$M_{H_2}$, $\theta$ and $v_s$.

Every term is even in $\chi$. A residual $\mathbb{Z}_2$ symmetry $\chi \to -\chi$
therefore holds exactly, and it makes $\chi$ stable. The declared `Width -> 0` for
$\chi$ agrees with this.

---

## 2. Field table

| `.fr` class | Symbol | Spin | $SU(3)_C$ | $SU(2)_L$ | $U(1)_Y$ / charge | Self-conj. | Mass symbol | Mass value | Width | PDG |
|---|---|---|---|---|---|---|---|---|---|---|
| `S[101]` | $\chi$ (`chi`) | 0 | **1** (not declared) | **1** (not declared) | 0 (none declared) | Yes | `Mx` | 62.573 GeV | 0 | 52 |
| `S[102]` | $H_2$ (`H2`) | 0 | **1** (not declared) | **1** (not declared) | 0 (none declared) | Yes | `MH2` | 125.30 GeV | `WH2` = 0. | 35 |
| `S[103]` | $\phi_1$ (`phi1`) | 0 | **1** | **1** | 0 | Yes | — (unphysical) | — | — | — |
| `S[104]` | $s_1$ (`s1`) | 0 | **1** | **1** | 0 | Yes | — (unphysical) | — | — | — |

Notes:

- No `Indices` and no `QuantumNumbers` are declared for any class. All four states
  are gauge singlets and electrically neutral.
- $\phi_1$ and $s_1$ are `Unphysical -> True`. FeynRules replaces them by the
  rotation of Section 1.1 before it makes the vertices.
- $\chi$ has `PropagatorArrow -> None`, which agrees with `SelfConjugate -> True`.
- $2M_\chi = 125.146$ GeV $< M_{H_2} = 125.30$ GeV. The decay
  $H_2 \to \chi\chi$ is therefore kinematically open, although `WH2` is set to 0.
  Whether $H \to \chi\chi$ is open depends on `MH`, which comes from the SM file.

---

## 3. Parameters

### External parameters

| Symbol | Block | Order | Value | Multiplies | Meaning |
|---|---|---|---|---|---|
| `vs` ($v_s$) | `PNGDM` | 1 | 13155.1 | appears in $\lambda_S v_s\, s_1 \chi^2$ and in the definitions of `lamPS`, `lamS` | Vacuum expectation value of the complex singlet $S$, in GeV. It sets the new-physics scale (about 13.2 TeV). |
| `thx` ($\theta$) | `PNGDM` | 2 | 1.53 | the $\phi_1$–$s_1$ rotation, through `sxth`, `cxth` | Mixing angle of the two CP-even scalars, in radians (about $87.7^\circ$). $s_\theta \simeq 0.9992$, $c_\theta \simeq 0.0408$. So the doublet direction $\phi_1$ is almost fully the $H_2$ state, and $H$ is almost fully singlet. |

Masses `Mx` (62.573 GeV) and `MH2` (125.30 GeV) are declared in the particle
classes, not in `M$Parameters`. `MH`, `vev`, and all SM couplings come from the SM
model file.

### Internal (derived) parameters

| Symbol | Definition | Multiplies | Meaning |
|---|---|---|---|
| `sxth` | $\sin\theta$ | rotation matrix | Sine of the scalar mixing angle. |
| `cxth` | $\cos\theta$ | rotation matrix | Cosine of the scalar mixing angle. |
| `lamPS` ($\lambda_{\Phi S}$) | $\dfrac{(M_{H_2}^2 - M_H^2)\, s_\theta c_\theta}{v\, v_s}$ | $\phi_1^2\chi^2$ and $v\,\phi_1\chi^2$ | Higgs-portal quartic coupling $\lambda_{\Phi S}|\Phi|^2|S|^2$. It is the off-diagonal entry of the CP-even mass matrix divided by $v v_s$: $\;(\mathcal{M}^2)_{12} = \lambda_{\Phi S} v v_s$. `InteractionOrder -> {NP,2}`. |
| `lamS` ($\lambda_S$) | $\dfrac{M_H^2 s_\theta^2 + M_{H_2}^2 c_\theta^2}{v_s^2}$ | $s_1^2\chi^2$, $v_s s_1 \chi^2$, $\chi^4$ | Singlet quartic coupling. It is the singlet diagonal entry of the CP-even mass matrix divided by $v_s^2$: $\;(\mathcal{M}^2)_{22} = \lambda_S v_s^2$. `InteractionOrder -> {NP,2}`. |

Both `lamPS` and `lamS` are exactly the inversion of the $2\times 2$ CP-even mass
matrix in the basis $(\phi_1, s_1)$ with the rotation of Section 1.1:

$$\mathcal{M}^2 = R\,\mathrm{diag}(M_H^2, M_{H_2}^2)\,R^{T},
\qquad R=\begin{pmatrix} c_\theta & s_\theta\\ -s_\theta & c_\theta\end{pmatrix},$$

$$(\mathcal{M}^2)_{12} = s_\theta c_\theta (M_{H_2}^2 - M_H^2) = \lambda_{\Phi S} v v_s ,
\qquad
(\mathcal{M}^2)_{22} = M_H^2 s_\theta^2 + M_{H_2}^2 c_\theta^2 = \lambda_S v_s^2 .$$

### Interaction order hierarchy

`{QCD, 1}, {QED, 2}, {NP, 1}`. The two new couplings carry `NP` order 2.

---

## 4. Physics summary

This is a Higgs-portal dark matter model that adds one complex gauge-singlet
scalar $S$ to the Standard Model. Its real part $s_1$ takes a large vacuum
expectation value $v_s = 13.2$ TeV and mixes with the neutral CP-even doublet
component $\phi_1$ by an angle $\theta$, which gives two CP-even mass eigenstates
$H$ and $H_2$ ($M_{H_2} = 125.30$ GeV). Its imaginary part $\chi$ is the dark
matter candidate: a real, neutral, stable scalar with $M_\chi = 62.573$ GeV, kept
stable by the exact $\chi \to -\chi$ symmetry of all terms. The mass $M_\chi$ comes
from a soft breaking of a global $U(1)$ of $S$; the breaking term itself is not
written in the file, so $\chi$ is a *pseudo*-Nambu-Goldstone boson, not an exact
Goldstone boson.

The decisive fingerprint is in Section 1.4. With the internal definitions of
$\lambda_{\Phi S}$ and $\lambda_S$, the two trilinear couplings become
$g_{\chi\chi H} = -M_H^2 s_\theta / v_s$ and
$g_{\chi\chi H_2} = +M_{H_2}^2 c_\theta / v_s$. The spin-independent
dark-matter–nucleon amplitude at zero momentum transfer is the sum of the $H$ and
$H_2$ exchange graphs, weighted by the doublet content $c_\theta$ and $s_\theta$:

$$\mathcal{A}(t\to 0) \;\propto\;
\frac{g_{\chi\chi H}\, c_\theta}{M_H^2} + \frac{g_{\chi\chi H_2}\, s_\theta}{M_{H_2}^2}
= -\frac{s_\theta c_\theta}{v_s} + \frac{s_\theta c_\theta}{v_s} \;=\; 0 .$$

The cancellation is exact and holds for any $\theta$, $v_s$, $M_H$ and $M_{H_2}$.
Tree-level direct detection is therefore momentum-suppressed, which is the defining
property of pseudo-Nambu-Goldstone (pseudo-Goldstone) singlet dark matter.

Processes this model mediates:

- Dark matter annihilation $\chi\chi \to H^{(*)}, H_2^{(*)} \to$ SM final states.
  With $M_\chi = 62.573$ GeV and $M_{H_2}=125.30$ GeV, the point sits on the scalar
  resonance funnel, $2M_\chi \simeq M_{H_2}$.
- Contact annihilation $\chi\chi \to HH,\, HH_2,\, H_2H_2$ from `LPortal4`, and dark
  self-interaction $\chi\chi \to \chi\chi$ from the $\lambda_S \chi^4$ term.
- Invisible scalar decay $H_2 \to \chi\chi$, which is open here
  ($2M_\chi = 125.146 < 125.30$ GeV), and $H \to \chi\chi$ if $M_H > 125.146$ GeV.
- Scalar mixing effects: all SM couplings of $H$ are rescaled by $c_\theta$ and
  those of $H_2$ by $s_\theta$, so the model also predicts a modified 125 GeV Higgs
  signal strength and a second, mostly singlet scalar.
- Spin-independent nucleon scattering only at loop level or at finite momentum
  transfer, because of the cancellation above.

---

## 5. Consistency flags

1. **Non-canonical factor 2 in `LX`.** `LX` carries an overall factor `2` in front
   of the canonical kinetic and mass terms of $\chi$. All other terms in the file
   use canonical normalisation. If the factor is kept, the canonical field is
   $\hat\chi = \sqrt{2}\,\chi$. The mass stays $M_\chi$, because kinetic and mass
   terms scale together, but every $\chi$ interaction is reduced: the trilinear
   $\chi^2 H$ and $\chi^2 H_2$ couplings and the $\chi^2 H^2$-type quartics are
   halved, and the $\chi^4$ coupling is divided by 4. The relic abundance and the
   invisible decay width would change; the direct-detection cancellation of
   Section 4 would survive, because it is an overall rescaling of both trilinear
   couplings. This factor `2` looks like a defect, not like physics.
2. **`LX` syntax.** `2 (expr;)` is `2` times a `CompoundExpression` that ends in
   `;`, so it returns `Null`. As written, `LX` does not evaluate to a Lagrangian in
   FeynRules.
3. **`WH2 -> 0.`** is declared, but $H_2 \to \chi\chi$ is kinematically open and
   $H_2$ also inherits SM decay modes through $s_\theta$. The width must be computed,
   not fixed to zero.
4. **`LSM` and `MH`, `vev`** are used but not defined in this file. The file is a
   fragment that must be loaded together with the SM model file.
