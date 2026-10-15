# Reconstruction of `sanitized.fr`

## 0. Conventions and scope

Metric: FeynRules default mostly-plus-time signature $\eta_{\mu\nu}=\mathrm{diag}(+,-,-,-)$.
Repeated Lorentz indices written twice in the `.fr` source (e.g. `V1[mu] V1[mu]`) are contracted
with $\eta_{\mu\nu}$, i.e. `V1[mu] V1[mu]` $= V_{1\,\mu}V_1^{\,\mu}$.

**Important caveat on completeness.** The file declares an interaction coupling `ct`, a mixing
angle `thV1`, and two internal chiral couplings `ctL`, `ctR` with `InteractionOrder -> {NP, 1}`,
but **no Lagrangian term in the file uses any of them**. `LTotal := LV1Kin` contains only the
free (Proca) Lagrangian of `V1`. Section 1 gives the terms that are literally present.
Section 1b states, as an explicit inference and clearly marked as *not present in the file*,
the interaction term that the parameter block, the `BlockName -> TOPPHILIC`, the `InteractionOrder`
assignments and the numerical `Width` all point to.

---

## 1. Lagrangian terms present in the file

### 1.1 `LV1Kin` — kinetic term of the vector $V_1$

Source: `-1/4 FS[V1, mu, nu] FS[V1, mu, nu]`.

`V1` is `SelfConjugate -> True` and carries no gauge indices, so `FS[V1,mu,nu]` is the abelian
field strength

$$
V_{1}^{\mu\nu} \;=\; \partial^{\mu} V_{1}^{\nu} \;-\; \partial^{\nu} V_{1}^{\mu}\,,
$$

and the term is

$$
\boxed{\;\mathcal{L}_{\rm kin}^{V_1} \;=\; -\frac{1}{4}\,V_{1\,\mu\nu}\,V_{1}^{\,\mu\nu}
\;=\; -\frac{1}{4}\left(\partial_{\mu}V_{1\,\nu}-\partial_{\nu}V_{1\,\mu}\right)
\left(\partial^{\mu}V_{1}^{\,\nu}-\partial^{\nu}V_{1}^{\,\mu}\right)\;}
\qquad \text{[\texttt{LV1Kin}, 1st term]}
$$

No `HC[...]` is applied and none is needed: the field is real (self-conjugate), so the term is
already hermitian.

### 1.2 `LV1Kin` — mass term of the vector $V_1$

Source: `+1/2 MV1^2 V1[mu] V1[mu]`.

$$
\boxed{\;\mathcal{L}_{\rm mass}^{V_1} \;=\; \frac{1}{2}\,M_{V_1}^{2}\,V_{1\,\mu}V_{1}^{\,\mu}\;}
\qquad \text{[\texttt{LV1Kin}, 2nd term]}
$$

The factor $1/2$ (rather than $1$) is the correct normalisation for a **real** vector field and
is consistent with `SelfConjugate -> True`. Together with 1.1 this is the Proca Lagrangian; the
mass is put in by hand (no Higgs/Stückelberg field appears in the file), so $V_1$ is an
explicitly massive, non-gauge-invariant vector, or equivalently a gauge boson whose
symmetry-breaking sector has been integrated out.

### 1.3 `LTotal`

$$
\mathcal{L}_{\rm total} \;=\; \mathcal{L}^{V_1}_{\rm kin} + \mathcal{L}^{V_1}_{\rm mass}
\qquad \text{[\texttt{LTotal} := \texttt{LV1Kin}]}
$$

This is the **entire** new-physics Lagrangian in the file. It is added to the Standard Model
Lagrangian supplied by whatever base model this file is loaded on top of (the file itself
declares no SM fields, so it is a model *extension* file, not a standalone model).

### 1.4 Covariant derivative content

No `DC[...]` appears anywhere in the file, and $V_1$ carries **no** colour, isospin or
hypercharge index. Its covariant derivative is therefore the plain partial derivative:

$$
D_\mu V_{1\,\nu} \;=\; \partial_\mu V_{1\,\nu}\,,
$$

i.e. the gauge content acting on $V_1$ from $SU(3)_C\times SU(2)_L\times U(1)_Y$ is empty:
$g_s T^a = 0$, $g\,\tau^i/2 = 0$, $g' Y = 0$ for this field. Any Standard Model field appearing
in an interaction with $V_1$ would keep its usual SM covariant derivative
$D_\mu = \partial_\mu - i g_s T^a G^a_\mu - i g\,\tfrac{\tau^i}{2}W^i_\mu - i g' Y B_\mu$,
but the file itself contains no such term.

---

## 1b. The missing interaction term (inference — NOT present in the file)

Everything in the parameter block is dangling. The following evidence fixes what the removed
term must have been:

1. `BlockName -> TOPPHILIC` and `TeX -> Subscript[c, t]` for `ct` — a coupling to the **top quark**.
2. `ctL = ct Cos[thV1]`, `ctR = ct Sin[thV1]`, with `TeX` $c_L$ and $c_R$ — a **left/right chiral
   decomposition** of a single overall strength `ct`, with the chirality mix set by one angle.
   This is the standard idiom for $c_{L}P_L + c_{R}P_R$ in a vector current.
3. `InteractionOrder -> {NP, 1}` on `ct`, `ctL`, `ctR` — they enter a vertex once each, at NP order 1.
4. `PDG -> 32` — the conventional PDG code for a $Z'$.
5. The hard-coded `Width -> {WV1, 229.31}` at `MV1 = 1500` GeV is an exact numerical check.
   For $\mathcal{L}\supset V_{1\mu}\bar t\gamma^\mu(c_LP_L+c_RP_R)t$,
   $$\Gamma(V_1\to t\bar t)=\frac{N_c M}{24\pi}\sqrt{1-4x}\Big[(c_L^2+c_R^2)(1-x)+6\,c_Lc_R\,x\Big],
   \qquad x=\frac{m_t^2}{M^2}.$$
   With $N_c=3$, $M=1500$ GeV, $m_t\simeq173$ GeV, $c_L=0$, $c_R=2$ this gives
   $\Gamma\simeq229.2$ GeV, matching the stored `229.31` GeV. So the width was computed from a
   **top-only** vector coupling with exactly these parameters, and $t\bar t$ is the only open channel.

The removed term is therefore

$$
\boxed{\;\mathcal{L}_{V_1 t t} \;=\; V_{1\,\mu}\;\bar{t}\,\gamma^{\mu}
\Big(c_{L}\,P_{L} \;+\; c_{R}\,P_{R}\Big)\,t\;}
\qquad \text{[inferred; e.g. \texttt{LV1Top}, absent from the file]}
$$

with $P_{L,R}=\tfrac{1}{2}(1\mp\gamma^5)$ (FeynRules `ProjM`/`ProjP`), the colour index of $t$
contracted trivially with $\bar t$ (singlet current, $\delta_{ij}$, since $V_1$ is colourless),
and $c_L=c_t\cos\theta_t$, $c_R=c_t\sin\theta_t$. The term is self-hermitian for real $c_{L,R}$
and real $V_1$, so no `+HC[...]` is required. An overall normalisation convention
(e.g. a global $1/2$, or $\gamma^\mu(c_L P_L + c_R P_R)$ vs. $\gamma^\mu(v-a\gamma^5)$) cannot be
fixed with certainty from the remaining file alone, but the width check above is consistent with
the unit-normalised form written here.

Equivalent vector/axial form:
$$
\mathcal{L}_{V_1tt}=V_{1\mu}\,\bar t\,\gamma^\mu\!\left(g_V + g_A\gamma^5\right)t,
\qquad g_V=\frac{c_R+c_L}{2},\quad g_A=\frac{c_R-c_L}{2}.
$$

---

## 2. Field table

| Symbol | Class | Spin | $SU(3)_C$ | $SU(2)_L$ | $U(1)_Y$ / charge | Self-conjugate | Mass symbol | Mass value | Width |
|---|---|---|---|---|---|---|---|---|---|
| $V_1$ (`V1`, `V[100]`) | vector | 1 | **1** (singlet — no `Indices -> {Index[Colour]}` declared) | **1** (no `Indices -> {Index[SU2W]}`, no `SU2 rep` declared) | 0 (no `QuantumNumbers` block; no electric charge, no hypercharge) | **Yes** (`SelfConjugate -> True`) | `MV1` | 1500. GeV | `WV1` = 229.31 GeV |

Additional declared attributes: `PDG -> 32` (conventional $Z'$ code), `PropagatorType -> Sine`
(wavy/vector line), `PropagatorArrow -> None` (consistent with a real field), `ParticleName -> "V1"`.

No other new particle classes are declared. Because the field is real and neutral under every SM
factor, $V_1$ is a **Standard-Model-singlet massive neutral vector boson** — a $Z'$.

---

## 3. Parameters

### External parameters

| Symbol | LHA block / order | Value | Multiplies | Physical meaning |
|---|---|---|---|---|
| `ct` ($c_t$) | `TOPPHILIC`, 1 | 2. | overall strength of the $V_1\bar t t$ current (via `ctL`, `ctR`) | dimensionless **coupling** of the new vector to the top quark; `InteractionOrder -> {NP,1}` so one power per vertex |
| `thV1` ($\theta_t$) | `TOPPHILIC`, 2 | 1.5707963267948966 $=\pi/2$ | nothing directly; sets the split of $c_t$ between $P_L$ and $P_R$ | **chirality mixing angle**. No `InteractionOrder` (it is a pure angle, not a coupling order). At the default $\pi/2$: $c_L=0$, $c_R=c_t=2$ — a **purely right-handed** top coupling |

Note that `MV1` and `WV1` are not listed in `M$Parameters`; FeynRules creates them automatically
from the `Mass` and `Width` entries of the `V[100]` class.

### Internal (derived) parameters

| Symbol | Definition | Value at defaults | Multiplies | Physical meaning |
|---|---|---|---|---|
| `ctL` ($c_L$) | $c_t\cos\theta_t$ | $0$ | $\bar t\,\gamma^\mu P_L\,t\;V_{1\mu}$ | left-handed (chirality $P_L$) coupling of $V_1$ to the top |
| `ctR` ($c_R$) | $c_t\sin\theta_t$ | $2$ | $\bar t\,\gamma^\mu P_R\,t\;V_{1\mu}$ | right-handed (chirality $P_R$) coupling of $V_1$ to the top |

The polar parametrisation $(c_L,c_R)=c_t(\cos\theta_t,\sin\theta_t)$ keeps
$c_L^2+c_R^2=c_t^2$ fixed while $\theta_t$ scans from purely left-handed ($\theta_t=0$) through
vector-like ($\theta_t=\pi/4$) to purely right-handed ($\theta_t=\pi/2$).

**Both `ctL` and `ctR` are unused in this file** — they appear in no Lagrangian expression. As
written, the model would generate no $V_1$ vertex at all, and `WV1 = 229.31` GeV would be
inconsistent with a completely decoupled, stable $V_1$. This is the strongest internal sign that
an interaction term has been removed from the file.

---

## 4. Physics summary

This is a **top-philic $Z'$ model**: the Standard Model is extended by one real, colour-singlet,
electroweak-singlet, electrically neutral massive spin-1 boson $V_1$ (PDG 32) with
$M_{V_1}=1500$ GeV, described by a Proca kinetic plus mass term. Its parameter sector defines a
single new coupling $c_t=2$ to the top quark, split into chiral pieces
$c_L=c_t\cos\theta_t$ and $c_R=c_t\sin\theta_t$, which at the default $\theta_t=\pi/2$ is a
**purely right-handed** $V_1\bar t_R t_R$ interaction.

Phenomenologically such a state is produced at hadron colliders mainly through
$gg\to t\bar t V_1$ and $pp\to t\bar t V_1$ associated production, or through $tW$/$t$-channel
top loops, since it has no tree-level coupling to light quarks; it decays essentially only to
$t\bar t$ (the stored width $229.31$ GeV is exactly the $t\bar t$ partial width for $c_R=2$,
$c_L=0$ at $M=1500$ GeV), giving four-top ($pp\to t\bar t V_1\to t\bar t t\bar t$) and
$t\bar t$-resonance signatures, and it contributes to $t\bar t$ production at one loop.

**Caveat, repeated for the reader:** the $V_1\bar t t$ interaction itself is *missing* from the
file as given. Only the free Proca Lagrangian is written and assigned to `LTotal`; the coupling
parameters are orphaned. The model as literally encoded describes a stable, completely decoupled
1.5 TeV neutral vector.
