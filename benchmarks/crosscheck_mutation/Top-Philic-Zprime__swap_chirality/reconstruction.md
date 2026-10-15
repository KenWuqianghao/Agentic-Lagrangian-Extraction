# Reconstruction of `sanitized.fr`

The file adds one new state: a massive, self-conjugate, colour- and electric-charge-neutral
spin-1 field `V1`, coupled only to the top quark through a vector current with independent
left- and right-handed strengths. No new gauge group is declared. The Standard Model
(SM) fields `t`, `tbar` are used from the base SM model file.

---

## 1. Lagrangian (LaTeX)

Conventions used below:

- $V_\mu \equiv$ `V1[mu]`, a real (self-conjugate) vector field.
- $F^{V}_{\mu\nu} \equiv$ `FS[V1, mu, nu]` $= \partial_\mu V_\nu - \partial_\nu V_\mu$.
  Since `V1` carries no gauge index and no gauge group is defined for it, the field
  strength is abelian: there is **no** commutator term.
- `Ga[mu]` $= \gamma^\mu$.
- `ProjM` $= P_L = \tfrac{1}{2}(1-\gamma_5)$, `ProjP` $= P_R = \tfrac{1}{2}(1+\gamma_5)$
  (FeynRules convention: `ProjM` is the **left** projector, `ProjP` the **right** one).
- Repeated Lorentz indices are contracted with the Minkowski metric; FeynRules writes
  `FS[V1,mu,nu] FS[V1,mu,nu]` and `V1[mu] V1[mu]` with repeated *lower* indices, which
  means $F^V_{\mu\nu}F^{V\,\mu\nu}$ and $V_\mu V^\mu$.
- The colour index of the top quark is contracted trivially inside `tbar.…​.t`
  ($\bar t_i \ldots t_i$, $i=1,2,3$), so the current is a colour singlet.
- No `HC` and no `CC` appear in this file. See the hermiticity note below.

### `LV1Kin` — free Lagrangian of the new vector

$$
\mathcal{L}_{\rm V1Kin}
= -\frac{1}{4}\,F^{V}_{\mu\nu}F^{V\,\mu\nu}
\;+\;\frac{1}{2}\,M_{V_1}^{2}\,V_\mu V^\mu ,
\qquad
F^{V}_{\mu\nu}=\partial_\mu V_\nu-\partial_\nu V_\mu .
$$

This is a Proca Lagrangian: a canonically normalised kinetic term plus an explicit
mass term for a real vector field. The factor $1/2$ (not $1$) in the mass term and the
$-1/4$ (not $-1/2$) in the kinetic term confirm that $V_1$ is self-conjugate.

### `LV1Top` — top-philic current interaction

$$
\mathcal{L}_{\rm V1Top}
= \Big(\, c_L\,\bar t\,\gamma^{\mu}P_L\,t
\;+\; c_R\,\bar t\,\gamma^{\mu}P_R\,t \,\Big)\,V_\mu .
$$

Written out with the chiral projectors expanded:

$$
\mathcal{L}_{\rm V1Top}
= \bar t\,\gamma^{\mu}
\left[\frac{c_L+c_R}{2} \;-\; \frac{c_L-c_R}{2}\,\gamma_5\right] t\;V_\mu
\;\equiv\; \bar t\,\gamma^{\mu}\big(g_V - g_A\gamma_5\big) t \; V_\mu ,
$$

with $g_V=(c_L+c_R)/2$ and $g_A=(c_L-c_R)/2$.

Substituting the internal definitions $c_L = c_t\cos\theta_t$, $c_R = c_t\sin\theta_t$:

$$
\mathcal{L}_{\rm V1Top}
= c_t\,\bar t\,\gamma^{\mu}
\big(\cos\theta_t\,P_L + \sin\theta_t\,P_R\big)\,t\;V_\mu .
$$

**Hermiticity.** The operator $\bar t\,\gamma^\mu P_{L,R}\,t$ is *not* hermitian by
itself: $(\bar t\gamma^\mu P_L t)^\dagger = \bar t\gamma^\mu P_R t$. With real $c_L$,
$c_R$ the sum is hermitian only if $c_L=c_R$. The file supplies no `+ HC[...]`, so as
written the two chiralities carry independent real coefficients and the term is
hermitian only in the special case $\theta_t=\pi/4$. FeynRules will still expand it;
the intended reading is a real vector/axial-vector current with independent chiral
couplings, i.e. the standard $Z'$ current above.

### `LTotal` — total new-physics Lagrangian

$$
\mathcal{L}_{\rm Total}
= \mathcal{L}_{\rm V1Kin} + \mathcal{L}_{\rm V1Top}
= -\frac{1}{4}F^{V}_{\mu\nu}F^{V\,\mu\nu}
+\frac{1}{2}M_{V_1}^{2}V_\mu V^\mu
+ \big(c_L\,\bar t\gamma^\mu P_L t + c_R\,\bar t\gamma^\mu P_R t\big)V_\mu .
$$

The SM Lagrangian itself is not restated in this file; `LTotal` holds the new sector only.

### Covariant derivative / gauge content

**There is no covariant derivative in this file.** No `DC[...]` appears, and no new
gauge group is declared (`M$GaugeGroups` is absent). $V_1$ is introduced as a
*non-gauge*, massive vector: its kinetic term uses the abelian field strength `FS`, and
its mass is an explicit Proca mass rather than the result of a Higgs mechanism. $V_1$
is a singlet under $SU(3)_C \times SU(2)_L \times U(1)_Y$; it does not enter the SM
covariant derivative

$$
D_\mu = \partial_\mu - i g_s T^a G^a_\mu - i g\,T^i W^i_\mu - i g' Y B_\mu ,
$$

which acts on the SM fields exactly as in the base SM model. The top quark's own
kinetic and gauge terms come from the SM file and are unchanged.

**Interaction-order counting.** `M$InteractionOrderHierarchy` declares `QCD`=1,
`QED`=2, `NP`=1. Both $c_t$ and the internal $c_L$, $c_R$ carry
`InteractionOrder -> {NP, 1}`, so every $V_1 t\bar t$ vertex counts as one power of NP.

---

## 2. Field table

| Symbol | Class | Spin | SU(3)$_C$ | SU(2)$_L$ | U(1)$_Y$ / charge | Self-conjugate | Mass symbol | Mass value | Width | PDG |
|---|---|---|---|---|---|---|---|---|---|---|
| $V_1^\mu$ (`V1`) | `V[100]`, vector | 1 | singlet (**1**) — no `Indices` declared | singlet — not declared | 0 (no `QuantumNumbers`, so `Q = 0`) | **Yes** (`SelfConjugate -> True`) | `MV1` | 1500. GeV | `WV1` = 229.31 GeV | 32 |

Notes:

- No `Indices -> {Index[Gluon]}` and no `QuantumNumbers` entry: $V_1$ is a colour
  singlet with zero electric charge, hypercharge and lepton/baryon number.
- `SelfConjugate -> True` means $V_1^\dagger = V_1$; there is no separate antiparticle.
- `PropagatorType -> Sine`, `PropagatorArrow -> None` are drawing directives only
  (wavy line, no arrow), consistent with a real neutral vector boson.
- PDG 32 is the slot conventionally used for a $Z'$-like neutral vector.
- The width 229.31 GeV is large, $\Gamma/M \simeq 0.153$, which is what a strongly
  coupled ($c_t = 2$) decay to $t\bar t$ gives for a 1.5 TeV resonance.

No other new classes are defined. All fermions (`t`, `tbar`) come from the SM.

---

## 3. Parameters

### External parameters

| Symbol | Block / order | Value | Multiplies | Physical meaning |
|---|---|---|---|---|
| `ct` ($c_t$) | `TOPPHILIC`, 1 | 2. | overall factor of the whole $V_1 t\bar t$ current, $c_t\,\bar t\gamma^\mu(\cos\theta_t P_L+\sin\theta_t P_R)t\,V_\mu$ | Overall dimensionless coupling strength of $V_1$ to the top quark. Carries `InteractionOrder {NP,1}`. |
| `thV1` ($\theta_t$) | `TOPPHILIC`, 2 | 1.5707963267948966 $=\pi/2$ | nothing directly; enters only through $c_L$, $c_R$ | Chirality mixing angle. It divides the fixed total strength $c_t$ between the left- and right-handed top currents. No `InteractionOrder` (it is a pure angle, NP-order neutral). |

### Internal (derived) parameters

| Symbol | Definition | Multiplies | Physical meaning |
|---|---|---|---|
| `ctL` ($c_L$) | $c_t\cos\theta_t$ | $\bar t\,\gamma^\mu P_L\,t\;V_\mu$ (`ProjM` = left projector) | Coupling of $V_1$ to the **left-handed** top current. |
| `ctR` ($c_R$) | $c_t\sin\theta_t$ | $\bar t\,\gamma^\mu P_R\,t\;V_\mu$ (`ProjP` = right projector) | Coupling of $V_1$ to the **right-handed** top current. |

Both internal parameters carry `InteractionOrder {NP,1}`.

**Numerical point encoded in the file.** With $c_t = 2$ and $\theta_t = \pi/2$:

$$
c_L = 2\cos(\pi/2) = 0,\qquad c_R = 2\sin(\pi/2) = 2 .
$$

So the default benchmark is a **purely right-handed** coupling,
$\mathcal{L} = 2\,\bar t\gamma^\mu P_R t\,V_\mu$, i.e. $g_V = -g_A = 1$. The angle is
parameterised so that $c_L^2+c_R^2 = c_t^2$ is held fixed while $\theta_t$ rotates the
coupling between pure left ($\theta_t=0$), maximal parity-even ($\theta_t=\pi/4$,
$c_L=c_R$, pure vector) and pure right ($\theta_t=\pi/2$).

---

## 4. Physics summary

This is a minimal **top-philic $Z'$** model: a single real, colour-neutral,
electrically neutral massive spin-1 resonance $V_1$ (PDG 32, $M = 1.5$ TeV,
$\Gamma = 229$ GeV) added on top of the SM, with a Proca kinetic and mass term and one
interaction — a chiral vector current made only of top quarks. The coupling is set by
an overall strength $c_t$ and a chirality angle $\theta_t$ that splits it into
left-handed ($c_L = c_t\cos\theta_t$) and right-handed ($c_R = c_t\sin\theta_t$) pieces;
the shipped benchmark ($c_t=2$, $\theta_t = \pi/2$) is purely right-handed.

Because $V_1$ talks to nothing but the top quark, it is produced at hadron colliders
only through top loops or in association with tops — $gg \to V_1$ through a top loop,
$t\bar t V_1$, and $tW/tj$-associated production — and it decays essentially
100% to $t\bar t$ once $M_{V_1} > 2 m_t$. The characteristic signatures are a
$t\bar t$ invariant-mass resonance (with interference against SM $gg \to t\bar t$
producing a peak–dip line shape), four-top final states from $t\bar t V_1$ with
$V_1 \to t\bar t$, and, below threshold, loop-induced effects. The chirality angle is
observable through top polarisation and spin-correlation observables in the $t\bar t$
decay products.
