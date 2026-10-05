# Reconstruction of `sanitized.fr`

The file adds **one** new field: a real (self-conjugate) massive spin-1 boson `V1`, a
colour and electroweak singlet, that couples **only to the top quark**, with an
independent left- and right-handed strength set by one overall coupling and one
mixing angle. The Standard Model part of the Lagrangian is not in this file; only
the new-physics terms are.

Conventions used below:

- Metric $\eta_{\mu\nu} = \mathrm{diag}(+,-,-,-)$. FeynRules writes a contracted
  pair with both indices "down" (`FS[V1,mu,nu] FS[V1,mu,nu]`); this means
  $V_{\mu\nu}V^{\mu\nu}$.
- `ProjM` $= P_L = \tfrac{1}{2}(1-\gamma_5)$, `ProjP` $= P_R = \tfrac{1}{2}(1+\gamma_5)$.
- `Ga[mu]` $= \gamma^\mu$; `tbar.Ga[mu].P.t` is the Dirac-index chain
  $\bar t\,\gamma^\mu P\,t$, with the colour index of $t$ and $\bar t$ contracted
  by $\delta_{ij}$ (an implicit, suppressed sum: `V1` carries no colour index).
- `FS[V1,mu,nu]` is the **abelian** field strength, because `V1` is declared with
  no gauge-group indices and no structure constant:
  $V_{\mu\nu} = \partial_\mu V_\nu - \partial_\nu V_\mu$.

---

## 1. Lagrangian (LaTeX)

### 1.1 `LV1Kin` — Proca kinetic and mass term

$$
\mathcal{L}_{\rm V1Kin} \;=\; -\frac{1}{4}\,V_{\mu\nu}V^{\mu\nu}
\;+\;\frac{1}{2}\,M_{V_1}^{2}\,V_{\mu}V^{\mu},
\qquad
V_{\mu\nu} \equiv \partial_\mu V_\nu - \partial_\nu V_\mu .
$$

Notes:

- The factor $\tfrac12$ in the mass term and $-\tfrac14$ in the kinetic term are
  the normalisation for a **real** vector field ($V_\mu^\dagger = V_\mu$), which
  matches `SelfConjugate -> True`.
- The mass is written by hand (Proca / Stückelberg form). No scalar and no
  symmetry-breaking sector generates it in this file.

### 1.2 `LV1Top` — top-quark current coupling

$$
\mathcal{L}_{\rm V1Top} \;=\;
\Big(\, c_L\,\bar t\,\gamma^{\mu}P_L\,t \;+\; c_R\,\bar t\,\gamma^{\mu}P_R\,t \,\Big)\,V_{\mu}
\;=\;
\bar t\,\gamma^{\mu}\big(c_L P_L + c_R P_R\big)\,t\;V_{\mu}.
$$

with colour indices contracted inside the bilinear,
$\bar t_i \gamma^\mu (\dots) t_i$, $i = 1,2,3$.

Equivalent vector/axial-vector form:

$$
\mathcal{L}_{\rm V1Top} \;=\;
\bar t\,\gamma^{\mu}\big(g_V + g_A\gamma_5\big)\,t\;V_{\mu},
\qquad
g_V = \frac{c_R + c_L}{2},\quad g_A = \frac{c_R - c_L}{2}.
$$

Notes on conjugation:

- No `HC` is applied, and none is needed. Each bilinear is separately hermitian,
  $\big(\bar t\,\gamma^\mu P_{L,R}\,t\big)^\dagger = \bar t\,\gamma^\mu P_{L,R}\,t$,
  and $V_\mu$ is real, so $\mathcal{L}_{\rm V1Top}^\dagger = \mathcal{L}_{\rm V1Top}$
  for real $c_L, c_R$.
- No `CC` (charge conjugation) appears: the coupling is flavour-diagonal
  $t$–$\bar t$, not a $t$–$t$ or $t$–$q$ transition. The interaction conserves
  top number, so $V_1$ carries no top number and is not a leptoquark-like or
  diquark-like state.

### 1.3 `LTotal` — total new-physics Lagrangian

$$
\mathcal{L}_{\rm Total} \;=\; \mathcal{L}_{\rm V1Kin} + \mathcal{L}_{\rm V1Top}
\;=\;
-\frac{1}{4}V_{\mu\nu}V^{\mu\nu} + \frac{1}{2}M_{V_1}^{2}V_\mu V^\mu
+ \bar t\,\gamma^{\mu}\big(c_L P_L + c_R P_R\big)t\,V_\mu .
$$

### 1.4 Covariant-derivative / gauge content

There is **no `DC` in the file**, so no covariant derivative is written
explicitly. The gauge content is therefore fixed by the field declarations:

- $V_1$ carries no `Indices` (no `Colour`, no `SU2W`), no `QuantumNumbers`
  (no `Q`, no `Y`), and no gauge-boson class assignment. It is a **complete
  singlet** of $SU(3)_C \times SU(2)_L \times U(1)_Y$ and electrically neutral.
  Its field strength is abelian, and its derivative in $V_{\mu\nu}$ is the
  ordinary derivative $\partial_\mu$, not a covariant one. $V_1$ has no
  self-interactions and no gauge interactions.
- The top quark $t$ keeps its usual SM covariant derivative from the SM model
  file that this file extends,
  $D_\mu t = \big(\partial_\mu - i g_s G^a_\mu T^a - i g' Y B_\mu - \dots\big)t$,
  with $T^a$ the $SU(3)_C$ generators in the fundamental, and with the
  left-handed part also coupling to $W^a_\mu$. Nothing in this file changes it.
- $V_1$ is **not** a gauge field of a new gauge group in the FeynRules sense: it
  is declared as a plain `V[100]` with an explicit Proca mass and no gauge
  structure. Any underlying $U(1)'$ is implicit.

---

## 2. Field table

| Symbol | Class | Spin | $SU(3)_C$ | $SU(2)_L$ | $U(1)_Y$ / $Q$ | Self-conjugate | Mass symbol | Mass value | Width | PDG |
|---|---|---|---|---|---|---|---|---|---|---|
| $V_1^\mu$ (`V1`) | `V[100]` | 1 (vector) | **1** (singlet, no colour index declared) | not declared → singlet | not declared → $Y=0$, $Q=0$ | **Yes** (real field) | `MV1` | 1500. GeV | `WV1` $=229.31$ GeV | 32 |

Other properties declared for `V1`: `ParticleName -> "V1"`,
`PropagatorLabel -> "V1"`, `PropagatorType -> Sine` (wavy line, as for a gauge
boson), `PropagatorArrow -> None` (consistent with a self-conjugate state).
PDG 32 is the slot conventionally used for a second neutral heavy vector
($Z''$-like), but nothing in the file fixes it to any published model.

No new fermions and no new scalars are added. The only SM field that appears is
the top quark $t$ (and $\bar t$), taken from the base model.

---

## 3. Parameters

### External

| Symbol | LHA block / order | Value | Multiplies | Physical meaning |
|---|---|---|---|---|
| `ct` ($c_t$) | `TOPPHILIC`, entry 1 | 2. | overall factor of the whole $\bar t\gamma^\mu(\dots)t\,V_\mu$ term, through $c_L$ and $c_R$ | Overall dimensionless strength of the $V_1$–top coupling. Carries `InteractionOrder -> {NP,1}`, so each $V_1 t\bar t$ vertex counts one power of NP. |
| `thV1` ($\theta_t$) | `TOPPHILIC`, entry 2 | 1.5707963267948966 $= \pi/2$ | nothing directly; it splits $c_t$ between the chiralities | Chirality mixing angle. $\theta_t = 0$ gives a pure left-handed coupling, $\theta_t = \pi/2$ a pure right-handed one, $\theta_t = \pi/4$ a pure vector coupling. No `InteractionOrder` (it is an angle, not a coupling). |
| `MV1` | mass block (from the `Mass` declaration) | 1500. GeV | $\tfrac12 M_{V_1}^2 V_\mu V^\mu$ | Mass of the new vector. |
| `WV1` | decay block (from the `Width` declaration) | 229.31 GeV | propagator only | Total width of $V_1$; $\Gamma/M \approx 0.15$, a broad resonance, consistent with a single open $t\bar t$ channel at $c_t = 2$. |

### Internal (derived)

| Symbol | Definition | Multiplies | Meaning |
|---|---|---|---|
| `ctL` ($c_L$) | $c_t\cos\theta_t$ | $\bar t\,\gamma^\mu P_L\,t\,V_\mu$ | Left-handed $V_1 t\bar t$ coupling. `InteractionOrder -> {NP,1}`. |
| `ctR` ($c_R$) | $c_t\sin\theta_t$ | $\bar t\,\gamma^\mu P_R\,t\,V_\mu$ | Right-handed $V_1 t\bar t$ coupling. `InteractionOrder -> {NP,1}`. |

With the default values, $\theta_t = \pi/2$ gives

$$
c_L = c_t\cos(\pi/2) = 0,\qquad c_R = c_t\sin(\pi/2) = 2,
$$

so the default benchmark is a **purely right-handed** coupling to the top,
$\mathcal{L} \to 2\,\bar t\,\gamma^\mu P_R\,t\,V_\mu$, i.e. $g_V = -g_A = 1$
in the $(g_V + g_A\gamma_5)$ basis... explicitly $g_V = g_A = 1$ with the sign
convention $g_V = (c_R+c_L)/2$, $g_A = (c_R-c_L)/2$.

### Interaction-order hierarchy

`M$InteractionOrderHierarchy = {{QCD,1},{QED,2},{NP,1}}` puts the new coupling on
the same counting footing as $g_s$, so `NP` powers can be limited in the matrix
element generator.

---

## 4. Physics summary

This is a **top-philic heavy neutral vector ($Z'$-like) model**: one real,
colour-singlet, electroweak-singlet spin-1 boson of mass 1.5 TeV, with a Proca
mass term put in by hand and no gauge self-interactions, whose only interaction
is a flavour-diagonal current coupling to the top quark. One coupling $c_t$ sets
the strength and one angle $\theta_t$ sets the left/right chirality mix; the
default point ($c_t = 2$, $\theta_t = \pi/2$) is a purely right-handed coupling
to $t$.

Because $V_1$ talks to nothing but the top, it has no tree-level production from
light-quark annihilation and no tree-level couplings to leptons, gauge bosons, or
the Higgs. It would be produced at a hadron collider in association with tops
($pp \to t\bar t V_1$, $pp \to t V_1$ with an extra top, four-top final states
through $t\bar t V_1$ with $V_1 \to t\bar t$), and it decays essentially
100% to $t\bar t$ when kinematically open ($M_{V_1} = 1500\ \mathrm{GeV} > 2m_t$),
giving the large 229.31 GeV width. It therefore shows up as a broad $t\bar t$
invariant-mass resonance and as an excess in four-top production, and it induces
loop-level $gg \to V_1$ production and $V_1 \to gg,\ \gamma\gamma$ decays through
the top loop.
