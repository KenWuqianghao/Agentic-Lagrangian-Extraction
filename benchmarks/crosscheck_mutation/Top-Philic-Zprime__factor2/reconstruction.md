# Reconstruction of `sanitized.fr`

All statements below come only from the content of `sanitized.fr`. The file adds one
new field class (`V[100]`), two external parameters, two internal parameters, and two
Lagrangian terms.

---

## 1. Lagrangian (LaTeX)

### Conventions used to expand the FeynRules idioms

- `FS[V1, mu, nu]` is the abelian field strength of the self-conjugate vector `V1`:
  $V_{\mu\nu} \equiv \partial_\mu V_\nu - \partial_\nu V_\mu$.
  `V1` carries no gauge index in its class declaration, so no `DC` covariant derivative
  appears anywhere in the file, and the field strength has no commutator (non-abelian) part.
- `Ga[mu]` is $\gamma^\mu$.
- `ProjM` is the **left**-handed projector $P_L = \tfrac{1}{2}(1-\gamma_5)$.
- `ProjP` is the **right**-handed projector $P_R = \tfrac{1}{2}(1+\gamma_5)$.
- `tbar.Ga[mu].ProjM.t` is the Dirac-index chain $\bar t\,\gamma^\mu P_L\,t$, with the
  color index of the top quark contracted between $\bar t$ and $t$ (see the note on
  index contractions below).
- Repeated Lorentz indices inside `ExpandIndices` are summed with the Minkowski metric,
  so `V1[mu] V1[mu]` means $V_\mu V^\mu$.
- No `HC` and no `CC` appear in the file. Both terms are already hermitian by themselves
  (`V1` is self-conjugate and the two currents are hermitian), so no hermitian conjugate
  is added.

### Covariant derivative content

The file declares `V1` with **no** `Indices` entry and no gauge quantum numbers. It is a
singlet of $SU(3)_C \times SU(2)_L \times U(1)_Y$. Therefore, for this field,

$$
D_\mu V_\nu \;=\; \partial_\mu V_\nu ,
\qquad
V_{\mu\nu} \;=\; \partial_\mu V_\nu - \partial_\nu V_\mu .
$$

The top quark $t$ keeps the covariant derivative of the underlying Standard Model
implementation (`t` is not declared in this file); this file adds no new gauge
interaction for it. The new gauge content of this file is therefore an ungauged,
massive, neutral vector (Proca) field.

### Term 1 — `LV1Kin`

$$
\boxed{\;
\mathcal{L}_{\texttt{LV1Kin}}
= -\frac{1}{4}\, V_{\mu\nu} V^{\mu\nu}
\;+\; \frac{1}{2}\, M_{V_1}^{2}\, V_\mu V^{\mu}
\;}
$$

with $V_{\mu\nu} = \partial_\mu V_\nu - \partial_\nu V_\mu$.

This is the standard Proca Lagrangian for a real (self-conjugate) massive spin-1 field.
The mass term has the canonical $+\tfrac{1}{2}M^2 V_\mu V^\mu$ normalization for a real
vector, so the propagator mass is $M_{V_1} = 1500$ GeV.

### Term 2 — `LV1Top` (exactly as written in the file)

$$
\boxed{\;
\mathcal{L}_{\texttt{LV1Top}}
= 2\Big[\, c_L\, \bar t\,\gamma^\mu P_L\, t
\;+\; c_R\, \bar t\,\gamma^\mu P_R\, t \,\Big] V_\mu
\;}
$$

Written out with the chiral projectors expanded:

$$
\mathcal{L}_{\texttt{LV1Top}}
= 2\,\bar t\,\gamma^\mu
\left[ c_L \frac{1-\gamma_5}{2} + c_R \frac{1+\gamma_5}{2} \right] t\; V_\mu
= \bar t\,\gamma^\mu\Big[(c_L + c_R) - (c_L - c_R)\,\gamma_5\Big] t\; V_\mu .
$$

In vector/axial form, the effective couplings are
$g_V^{\text{eff}} = c_L + c_R$ and $g_A^{\text{eff}} = -(c_L - c_R) = c_R - c_L$,
i.e. twice the values that the parameter names $c_L, c_R$ alone would suggest.

With the color index $i = 1,2,3$ written explicitly (the current is a color singlet,
because $V_1$ is a color singlet):

$$
\mathcal{L}_{\texttt{LV1Top}}
= 2\sum_{i=1}^{3}\Big[ c_L\, \bar t^{\,i}\gamma^\mu P_L t^{\,i}
+ c_R\, \bar t^{\,i}\gamma^\mu P_R t^{\,i}\Big] V_\mu .
$$

The current is flavor-diagonal and involves **only** the top quark. No other fermion
appears in the file.

**Anomalies in this term as written (flagged, not silently corrected).**

1. **Overall factor 2.** The interaction carries an explicit multiplicative `2` in front
   of the whole block. The conventional normalization for such a current-vector coupling
   is $\mathcal{L} = (c_L\,\bar t\gamma^\mu P_L t + c_R\,\bar t\gamma^\mu P_R t)V_\mu$,
   i.e. with no prefactor, because $c_L$ and $c_R$ are already defined as the full
   couplings ($c_L = c_t\cos\theta_t$, $c_R = c_t\sin\theta_t$). The factor 2 doubles
   every $V_1 t \bar t$ vertex and therefore multiplies $\Gamma(V_1 \to t\bar t)$ and
   every production cross section by 4. The stored width `WV1 = 229.31` GeV does not
   agree with this doubled coupling (see the note in Section 3), so the factor 2 looks
   like an injected defect rather than an intended convention.
2. **Malformed brackets.** The text is
   `LV1Top := 2 (Block[{mu}, ExpandIndices[...]];` followed, after a blank line, by `)`.
   The opening parenthesis after `2` is never closed before the `;`, and the stray `)`
   sits after the statement terminator. As written the expression does not parse in
   Mathematica. The physics reading above assumes the intended grouping
   `2 (Block[{mu}, ExpandIndices[...]])`.

### Total — `LTotal`

$$
\mathcal{L}_{\texttt{LTotal}}
= \mathcal{L}_{\texttt{LV1Kin}} + \mathcal{L}_{\texttt{LV1Top}}
= -\frac{1}{4} V_{\mu\nu}V^{\mu\nu} + \frac{1}{2} M_{V_1}^2 V_\mu V^\mu
+ 2\Big[c_L\,\bar t\gamma^\mu P_L t + c_R\,\bar t\gamma^\mu P_R t\Big]V_\mu .
$$

---

## 2. Field table

| Symbol | Class | Spin | $SU(3)_C$ | $SU(2)_L$ | $U(1)_Y$ / electric charge | Self-conjugate | Mass symbol & value | Width | PDG |
|---|---|---|---|---|---|---|---|---|---|
| $V_1$ (`V1`) | `V[100]` (vector) | 1 | **1** (singlet; no color index declared) | not declared → singlet | not declared → 0 (neutral; forced by `SelfConjugate -> True`) | Yes | `MV1` $= 1500.$ GeV | `WV1` $= 229.31$ GeV | 32 |

Notes on the table:

- `V[100]` is a FeynRules vector class, hence spin 1.
- The class has no `Indices -> {Index[Colour]}` and no `Indices -> {Index[SU2W]}`, so the
  field is a total singlet under the Standard Model gauge group.
- `SelfConjugate -> True` makes $V_1$ a real field. A real vector cannot carry electric
  charge or hypercharge, so its $U(1)$ charge is zero. There is no antiparticle.
- Auxiliary display settings: `PropagatorType -> Sine`, `PropagatorArrow -> None`
  (both consistent with a neutral, self-conjugate vector), `ParticleName -> "V1"`.
- PDG 32 is the slot conventionally reserved for a second neutral heavy vector ($Z''$-like).
- The top quark $t$ is used but not declared here. It comes from the underlying Standard
  Model model file.

---

## 3. Parameters

### External parameters

| Symbol | Block / order | Value | Interaction order | TeX | What it multiplies | Physical meaning |
|---|---|---|---|---|---|---|
| `ct` | `TOPPHILIC`, 1 | $2.0$ | `{NP, 1}` | $c_t$ | Overall strength of both terms in `LV1Top`, through $c_L$ and $c_R$ | Dimensionless overall coupling of the new vector to the top quark. It sets the magnitude $\sqrt{c_L^2 + c_R^2} = c_t$. |
| `thV1` | `TOPPHILIC`, 2 | $1.5707963267948966 = \pi/2$ | none (no `InteractionOrder`) | $\theta_t$ | Nothing directly; it only enters through $c_L$ and $c_R$ | Chirality mixing angle. It splits the overall coupling $c_t$ between the left- and right-handed top currents. |

### Internal (derived) parameters

| Symbol | Definition | Interaction order | TeX | What it multiplies | Physical meaning |
|---|---|---|---|---|---|
| `ctL` | $c_L = c_t \cos\theta_t$ | `{NP, 1}` | $c_L$ | $\bar t\,\gamma^\mu P_L\, t\; V_\mu$ | Coupling of $V_1$ to the left-handed top current. |
| `ctR` | $c_R = c_t \sin\theta_t$ | `{NP, 1}` | $c_R$ | $\bar t\,\gamma^\mu P_R\, t\; V_\mu$ | Coupling of $V_1$ to the right-handed top current. |

### Mass and width parameters

| Symbol | Value | Meaning |
|---|---|---|
| `MV1` | $1500.$ GeV | Pole mass of $V_1$. It also appears explicitly in the Proca mass term of `LV1Kin`. |
| `WV1` | $229.31$ GeV | Total decay width of $V_1$. |

### Numerical consequence of the default values

$\theta_t = \pi/2$ exactly, so with the stored values

$$
c_L = 2\cos(\pi/2) = 0, \qquad c_R = 2\sin(\pi/2) = 2 .
$$

At the default point the vector couples **purely right-handed** to the top quark. The
parametrization $(c_t, \theta_t)$ is nevertheless general: $\theta_t = 0$ gives a purely
left-handed coupling, and $\theta_t = \pi/4$ gives a pure vector coupling.

**Width consistency check (supports the factor-2 flag).** For a neutral vector of mass
$M$ decaying to $t\bar t$ with couplings $g_{L,R}$ in
$\mathcal{L} = \bar t\gamma^\mu(g_L P_L + g_R P_R) t\,V_\mu$, and taking $m_t \ll M$,

$$
\Gamma(V_1 \to t\bar t) \simeq \frac{N_c\,M}{24\pi}\,(g_L^2 + g_R^2).
$$

With $g_R = c_R = 2$, $g_L = 0$, $N_c = 3$ and $M = 1500$ GeV this gives about
$239$ GeV, which matches the stored $W_{V_1} = 229.31$ GeV once the finite top mass is
kept. With the explicit factor 2 in `LV1Top` the effective coupling is $g_R = 2c_R = 4$,
which gives roughly $4 \times 229$ GeV $\approx 917$ GeV, four times the stored width.
The stored width is therefore consistent with the Lagrangian **without** the prefactor 2.

### Interaction-order bookkeeping

`M$InteractionOrderHierarchy` declares `{QCD, 1}`, `{QED, 2}`, `{NP, 1}`. The new physics
coupling is counted as order `NP = 1` per vertex, so each $V_1 t\bar t$ vertex adds one
power of `NP`. `thV1` carries no interaction order, which is correct for an angle.

---

## 4. Physics summary

This model adds one new state: a heavy, neutral, color-singlet, self-conjugate spin-1
boson $V_1$ of mass 1.5 TeV, described by a Proca kinetic and mass term. Its only
interaction is a flavor-diagonal coupling to the top quark, split into left- and
right-handed pieces by an overall strength $c_t$ and a chirality angle $\theta_t$; at the
stored values the coupling is purely right-handed with $c_R = 2$. Because the new vector
talks to no other Standard Model fermion, it is a "top-philic" heavy vector resonance
(a $Z'$-like state), as the parameter block name `TOPPHILIC` also indicates.

Such a state is produced mainly through top-quark loops or in association with tops
($t\bar t V_1$, $t\bar t$ + jets with $V_1$ radiation, $tW$-associated production), since
it has no tree-level coupling to light quarks or gluons. It decays almost entirely to
$t\bar t$ when $M_{V_1} > 2 m_t$, so its signature is a heavy resonance in the $t\bar t$
invariant mass spectrum, plus four-top final states ($t\bar t t\bar t$) from
$t\bar t V_1$ production with $V_1 \to t\bar t$. The large width-to-mass ratio
($\Gamma/M \approx 0.15$) means the resonance is broad.

---

## 5. Defects found in the file

For a term-by-term checker, the two points that need attention:

1. `LV1Top` carries an overall factor `2` that the parameter definitions do not call for.
   It doubles every $V_1 t\bar t$ coupling and disagrees with the stored width `WV1` by a
   factor of 4 in the rate.
2. `LV1Top` has unbalanced parentheses: `2 (Block[{mu}, ExpandIndices[...]];` with the
   closing `)` placed after the semicolon, on a later line. The definition will not
   evaluate as written.
