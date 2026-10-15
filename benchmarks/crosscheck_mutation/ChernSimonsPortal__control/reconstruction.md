# Reconstruction of `sanitized.fr`

## 0. Conventions used below

- Metric $\eta_{\mu\nu} = \mathrm{diag}(+,-,-,-)$. In FeynRules a Lorentz index repeated twice in the same monomial (both written "down", e.g. `X[mu] X[mu]`) is contracted with $\eta^{\mu\nu}$; below such pairs are written with one index raised.
- `Eps[mu,nu,la,rho]` is the rank-4 Levi-Civita symbol $\varepsilon^{\mu\nu\lambda\rho}$ (totally antisymmetric, $\varepsilon^{0123}=+1$ in the FeynRules convention). An overall sign flip of this convention flips the sign of all three portal terms together and is not physical here.
- `del[Phi[rho],la]` $= \partial_\lambda \Phi_\rho$ (the derivative index is the **second** argument).
- `FS[X,mu,nu]` for a self-conjugate, gauge-singlet vector is the abelian field strength $X_{\mu\nu} = \partial_\mu X_\nu - \partial_\nu X_\mu$.
- SM fields and parameters (`A`, `Z`, `W`, `Wbar`, `sw`, `cw`, `sw2`, `MZ`, `MW`, `LSM`) are taken from the SM model file that this file extends. `sw` $=\sin\theta_W$, `cw` $=\cos\theta_W$, `sw2` $=\sin^2\theta_W$.
- FeynRules SM convention: `W[mu]` $= W^+_\mu$ and `Wbar[mu]` $= W^-_\mu$, with $(W^+_\mu)^\dagger = W^-_\mu$.

**Gauge content of the covariant derivative.** There is none to expand: the file contains **no** `DC[...]` and no gauge-index structure. The new field $X$ is a total gauge singlet and its kinetic term uses only ordinary derivatives (through `FS`), so $D_\mu X_\nu \equiv \partial_\mu X_\nu$. All interactions are written **after** electroweak symmetry breaking, directly in the mass-eigenstate basis $(A_\mu, Z_\mu, W^\pm_\mu)$, with the $SU(2)_L\times U(1)_Y$ structure entering only through the explicit $\sin\theta_W$ / $\cos\theta_W$ factors (see the remark at the end of §1.2). The SM covariant derivative itself is unchanged and lives in `LSM`; $X$ does not appear in it.

---

## 1. Lagrangian

### 1.1 `LXkin` — Proca Lagrangian of the new vector

$$
\mathcal{L}_{X\rm kin}
= -\tfrac{1}{4}\,X_{\mu\nu}X^{\mu\nu}
\;+\;\tfrac{1}{2}\,M_X^{2}\,X_\mu X^{\mu},
\qquad
X_{\mu\nu}\equiv \partial_\mu X_\nu-\partial_\nu X_\mu .
$$

A real (self-conjugate) massive spin-1 field with a canonically normalised kinetic term and an explicit, positive-signature Proca mass term. No Higgs mechanism, no Stückelberg field, and no kinetic mixing with $B_{\mu\nu}$ appear.

### 1.2 `LPortalNeutral` — Chern–Simons (Levi-Civita) couplings to the neutral gauge bosons

The `.fr` expression contains two monomials.

**Term 1 ($XZZ$):**

$$
\mathcal{L}_{\rm PortalNeutral}^{(ZZ)}
= -\,c_1\,s_W\,\varepsilon^{\mu\nu\lambda\rho}\,Z_\mu\,X_\nu\,\partial_\lambda Z_\rho
= -\,\tfrac{1}{2}\,c_1\,s_W\,\varepsilon^{\mu\nu\lambda\rho}\,Z_\mu\,X_\nu\,Z_{\lambda\rho},
\qquad Z_{\lambda\rho}\equiv\partial_\lambda Z_\rho-\partial_\rho Z_\lambda .
$$

(The second form follows because $\varepsilon^{\mu\nu\lambda\rho}$ already antisymmetrises $\lambda\rho$. The term does **not** vanish for two identical $Z$ bosons: it is the antisymmetric combination $\varepsilon^{\mu\nu\lambda\rho}X_\nu\,(Z_\mu\partial_\lambda Z_\rho - Z_\rho\partial_\lambda Z_\mu)/2$, i.e. the standard Chern–Simons structure $X\cdot(Z\times\partial Z)$.)

**Term 2 ($XZ\gamma$):**

$$
\mathcal{L}_{\rm PortalNeutral}^{(Z\gamma)}
= +\,c_1\,c_W\,\varepsilon^{\mu\nu\lambda\rho}\,Z_\mu\,X_\nu\,\partial_\lambda A_\rho
= +\,\tfrac{1}{2}\,c_1\,c_W\,\varepsilon^{\mu\nu\lambda\rho}\,Z_\mu\,X_\nu\,F_{\lambda\rho},
\qquad F_{\lambda\rho}\equiv\partial_\lambda A_\rho-\partial_\rho A_\lambda .
$$

**Compact (pre-EWSB) form.** Using $B_\rho = c_W A_\rho - s_W Z_\rho$, the two monomials combine exactly into one hypercharge-field term:

$$
\mathcal{L}_{\rm PortalNeutral}
= c_1\,\varepsilon^{\mu\nu\lambda\rho}\,Z_\mu\,X_\nu\,\partial_\lambda B_\rho
= \tfrac{1}{2}\,c_1\,\varepsilon^{\mu\nu\lambda\rho}\,Z_\mu\,X_\nu\,B_{\lambda\rho}.
$$

So the single new neutral coupling is $X$–$Z$–$B$, written out in the photon/$Z$ basis. This fixes the relative sign and the $s_W$ vs. $c_W$ weights seen in the file, and it is the origin of the $s_W^2$ and $c_W^2$ factors in the width (§3).

This structure is real and hermitian by itself (all three fields are real), which is why no `HC` is added for it.

### 1.3 `LPortalCharged` — Chern–Simons coupling to the charged gauge bosons

$$
\mathcal{L}_{\rm PortalCharged}
= c_2\,\varepsilon^{\mu\nu\lambda\rho}\,W^{+}_{\mu}\,X_\nu\,\partial_\lambda W^{-}_{\rho}.
$$

### 1.4 `HC[LPortalCharged]` — hermitian conjugate

$$
\mathcal{L}_{\rm PortalCharged}^{\dagger}
= c_2^{*}\,\varepsilon^{\mu\nu\lambda\rho}\,W^{-}_{\mu}\,X_\nu\,\partial_\lambda W^{+}_{\rho}.
$$

With $c_2$ real (it is declared External with a real value), the sum of §1.3 and §1.4 is

$$
\mathcal{L}_{\rm PortalCharged}+{\rm h.c.}
= c_2\,\varepsilon^{\mu\nu\lambda\rho}\,X_\nu\Big(W^{+}_{\mu}\,\partial_\lambda W^{-}_{\rho}\;-\;W^{-}_{\rho}\,\partial_\lambda W^{+}_{\mu}\Big),
$$

an electrically neutral, hermitian $XW^+W^-$ vertex. Note this uses the *abelian* part of the $W$ field strength only; the term is not $SU(2)_L$ covariant on its own, as expected for a Chern–Simons/Wess–Zumino operator written after EWSB.

### 1.5 `LTotal` — the full model

$$
\mathcal{L}_{\rm Total}
= \mathcal{L}_{\rm SM}
+ \mathcal{L}_{X\rm kin}
+ \mathcal{L}_{\rm PortalNeutral}
+ \mathcal{L}_{\rm PortalCharged}
+ \mathcal{L}_{\rm PortalCharged}^{\dagger}.
$$

**Chirality / conjugation summary.** There are no fermions, no `Ga`, no `ProjP`/`ProjM`, no `CC` and no Yukawa-type structures anywhere in the file, so there is nothing chiral to specify. The only conjugation is the charged-current $W^+\leftrightarrow W^-$ one in §1.4. All Lorentz contractions are through $\eta_{\mu\nu}$ and the single $\varepsilon^{\mu\nu\lambda\rho}$ per portal term; every portal vertex is therefore parity-odd in structure (an $\varepsilon$-tensor triple-gauge vertex), unlike the $\varepsilon$-free SM triple-gauge vertices.

---

## 2. Field table

| Symbol | Class | Spin | $SU(3)_C$ | $SU(2)_L$ | $U(1)$ charge | Self-conjugate | Mass | Width | PDG |
|---|---|---|---|---|---|---|---|---|---|
| $X_\mu$ | `V[101]` | 1 (vector) | singlet (no `Indices -> {Index[Colour]}`) | not declared → singlet (mass-eigenstate field, post-EWSB) | $Q=0$ (no `QuantumNumbers` declared); hypercharge undeclared → 0 | **Yes** (`SelfConjugate -> True`, so $X_\mu$ is real, $X^\dagger_\mu = X_\mu$) | $M_X = 1000.$ GeV | $W_X$, Internal (§3) | 5000023 |

Only one new particle class is declared. Display settings: `ParticleName -> "X"`, `PropagatorType -> Sine` (wavy/sine propagator line, i.e. drawn as a gauge boson), `PropagatorArrow -> None` (consistent with a real field). All other fields ($A$, $Z$, $W^\pm$, and everything in `LSM`) are the unmodified SM fields.

---

## 3. Parameters

### New external parameters

| Symbol | Type | Block | Value | Interaction order | Mass dimension | What it multiplies | Physical meaning |
|---|---|---|---|---|---|---|---|
| $c_1$ | External | `NPCOUPLINGS`, index 1 | $1.0$ | `{NP,1}` | dimensionless | `LPortalNeutral`: both the $XZZ$ term ($-c_1 s_W$) and the $XZ\gamma$ term ($+c_1 c_W$); equivalently the single $XZB$ term | Neutral Chern–Simons portal coupling of $X$ to the hypercharge/neutral sector. One parameter controls $XZZ$ and $XZ\gamma$ together, with their ratio fixed by the weak mixing angle. |
| $c_2$ | External | `NPCOUPLINGS`, index 2 | $1.0$ | `{NP,1}` | dimensionless | `LPortalCharged` and its h.c.: the $XW^+W^-$ vertex | Charged Chern–Simons portal coupling of $X$ to the $W$ sector. |
| $M_X$ | External (created by the `Mass -> {MX, 1000.}` declaration of `V[101]`) | `MASS` (default) | $1000.$ GeV | — | mass | $\tfrac12 M_X^2 X_\mu X^\mu$ in `LXkin` | Pole mass of the new vector: a 1 TeV state. |

Both portal operators are dimension 4, hence $c_1$ and $c_2$ are dimensionless; no new mass scale beyond $M_X$ is introduced. `M$InteractionOrderHierarchy` adds `NP` at order 1 alongside `QCD` (1) and `QED` (2), so each portal vertex counts as one power of `NP`.

### New internal parameter

| Symbol | Type | Expression |
|---|---|---|
| $W_X$ | Internal | total width of $X$, computed at tree level from the three portal decays |

$$
\Gamma_X \;=\;
\underbrace{\frac{c_1^{2}s_W^{2}M_X^{3}}{192\pi M_Z^{2}}\left(1-\frac{4M_Z^{2}}{M_X^{2}}\right)^{5/2}}_{X\to ZZ}
\;+\;
\underbrace{\frac{c_2^{2}M_X^{3}}{48\pi M_W^{2}}\left(1-\frac{4M_W^{2}}{M_X^{2}}\right)^{5/2}}_{X\to W^{+}W^{-}}
\;+\;
\underbrace{\frac{c_1^{2}c_W^{2}M_X^{3}}{96\pi M_Z^{2}}\left(1-\frac{M_Z^{2}}{M_X^{2}}\right)^{3}\left(1+\frac{M_Z^{2}}{M_X^{2}}\right)}_{X\to Z\gamma}.
$$

Reading of the three pieces:

- The $\beta^{5}$ threshold factors $(1-4M_V^2/M_X^2)^{5/2}$ are the two-identical-mass phase-space behaviour of a derivative ($\varepsilon$-tensor) vertex.
- The $s_W^2$ weight tracks the $-c_1 s_W$ coupling of the $XZZ$ term; the $c_W^2$ weight tracks the $+c_1 c_W$ coupling of the $XZ\gamma$ term — exactly the split of the single $XZB$ operator.
- The $X\to Z\gamma$ factor $(1-M_Z^2/M_X^2)^3(1+M_Z^2/M_X^2)$ is the one-massless/one-massive two-body form.
- The $1/M_V^2$ in each term comes from the longitudinal polarisations of the final-state gauge bosons, i.e. the operators grow with energy — the usual sign that this is an effective description valid below some higher cut-off.
- No decays to fermions or to the Higgs are included, because the model has no such couplings.

No other new parameters are declared; $s_W$, $c_W$, $s_W^2$, $M_Z$ and $M_W$ are SM inputs.

---

## 4. Physics summary

This is a minimal "Chern–Simons portal": one heavy (1 TeV), electrically neutral, colour-singlet, self-conjugate spin-1 state $X_\mu$ added to the Standard Model with a Proca kinetic term, and coupled to the SM **only** through two dimension-4 Levi-Civita triple-gauge-boson operators — $c_1\,\varepsilon\,Z X \partial B$ (which splits into $XZZ$ and $XZ\gamma$) and $c_2\,\varepsilon\,W^+ X \partial W^-$ plus its hermitian conjugate. There are no couplings to quarks, leptons or the Higgs, no mass mixing with the $Z$, and no kinetic mixing, so the electroweak sector is otherwise untouched; such $\varepsilon$-tensor vertices are the structure that anomaly-induced (Wess–Zumino / Green–Schwarz) terms leave behind when heavy anomalous fermions are integrated out.

Phenomenologically, $X$ can only be produced from gauge bosons — vector-boson fusion ($WW\to X$, $ZZ/Z\gamma\to X$) and associated production with a $W$, $Z$ or photon — and it decays to $W^+W^-$, $ZZ$ and $Z\gamma$ with branching ratios fixed by $c_1$, $c_2$ and $\theta_W$. It therefore shows up as a narrow-to-broad diboson resonance at $\sim 1$ TeV whose angular distributions carry the parity-odd $\varepsilon$-tensor signature, distinguishing it from a conventional $Z'$ or a spin-2 graviton.
