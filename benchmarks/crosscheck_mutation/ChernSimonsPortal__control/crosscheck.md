# Cross-check: `reconstruction.md` vs. the paper

**Paper.** I. Antoniadis, A. Boyarsky, S. Espahbodi, O. Ruchayskiy, J. D. Wells,
*Anomaly driven signatures of new invisible physics at the Large Hadron Collider*
(CERN-PH-TH/2009-006).

**Reconstruction under test.** `reconstruction.md`, an independent read-out of a
FeynRules file `sanitized.fr` (the `.fr` file itself was not available to me).

---

## 1. Where the paper defines the model

The paper states the model in two places, and the two statements must be read together.

| What | Where |
|---|---|
| Low-energy Lagrangian: SM + massive vector $X$ | **eq. (39)**, §2: $\mathcal{L} = \mathcal{L}_{SM} - \frac{1}{4g_X^2}\lvert F_X\rvert^2 + \frac{M_X^2}{2}\lvert D\theta_X\rvert^2 + \mathcal{L}_{int}$, with $D\theta_X = d\theta_X + X$ (Stückelberg field $\theta_X$) |
| The three portal vertices, broken phase | **eq. (59)**, §2: $\epsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \partial_\lambda Z_\rho$, $\;\epsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \partial_\lambda \gamma_\rho$, $\;\epsilon^{\mu\nu\lambda\rho} W^+_\mu X_\nu \partial_\lambda W^-_\rho$ |
| Gauge-covariant (D'Hoker–Farhi) form, with the couplings $c_1, c_2$ | **eq. (48)**, §2: $\mathcal{L}_{int} = c_1 \frac{H^\dagger D H}{\lvert H\rvert^2} D\theta_X F_Y + c_2 \frac{H F_W D H^\dagger}{\lvert H\rvert^2} D\theta_X$ |
| Broken-phase form of the first term of (48) | **eq. (15)**, §5: $\mathcal{L}_{XZY} = c_1 (d\theta_Z + Z) F_Y D\theta_X + \mathcal{O}(\partial h / v)$, with $H$ parametrised in **eq. (13)** |
| Feynman rules $\Gamma_{XZZ}$, $\Gamma_{XZ\gamma}$ | **eq. (40)**, §5 |
| Feynman rule $\Gamma_{XW^+W^-}$ | unnumbered equation after eq. (40), §5 |
| Partial widths | **eq. (41)**, §5.2; ratios in **eq. (55)** and **eq. (57)** |
| Rejected $SU(2)$ Chern–Simons route | **eq. (64)**, **eq. (90)** (rejected because it also makes an $X\gamma\gamma$ term, which breaks $U(1)_{em}$) |
| Heavy fermion content (integrated out) | Tables 1–4 (§2, §3, §4), Yukawa terms **eq. (12)**, **eq. (70)**, **eq. (60)** |
| SM fermions carry no $U(1)_X$ charge | §1, second bullet; §2 opening paragraph |

The paper's own normalisation of the neutral operator is not stated once and for all:
eq. (48) and eq. (15) are written in differential-form notation, which fixes the
**structure** but not the overall factor; eq. (40) and eq. (41) fix numbers. Section 3
below shows that eq. (40) and eq. (41) do not agree with each other for the $XZZ$ term.

---

## 2. Term-by-term comparison

Throughout, I write the reconstruction's neutral-portal Lagrangian coefficients as
$g_{ZZ}$, $g_{Z\gamma}$, $g_{WW}$, defined by
$\mathcal{L} \supset g_{ZZ}\,\varepsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \partial_\lambda Z_\rho
+ g_{Z\gamma}\,\varepsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \partial_\lambda A_\rho
+ \big(g_{WW}\,\varepsilon^{\mu\nu\lambda\rho} W^+_\mu X_\nu \partial_\lambda W^-_\rho + \mathrm{h.c.}\big)$.
The reconstruction has $g_{ZZ} = -c_1 s_W$, $g_{Z\gamma} = +c_1 c_W$, $g_{WW} = c_2$.

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| $-\frac{1}{4g_X^2}\lvert F_X\rvert^2$ — kinetic term of the new vector (eq. 39) | §1.1 `LXkin`: $-\frac14 X_{\mu\nu}X^{\mu\nu}$, $X_{\mu\nu}=\partial_\mu X_\nu - \partial_\nu X_\mu$ | **agree** | Same abelian field strength. The paper keeps $1/g_X^2$ out front; the reconstruction is canonically normalised. The two differ only by $X \to g_X X$, which is absorbed into $c_1, c_2$. Convention, not physics. |
| $\frac{M_X^2}{2}\lvert D\theta_X\rvert^2$ with $D\theta_X = d\theta_X + X$ (eq. 39) | §1.1: $+\frac12 M_X^2 X_\mu X^\mu$, and the explicit remark "no Stückelberg field" | **agree** (in unitary gauge) | Setting $\theta_X = 0$ turns the paper's Stückelberg mass into the reconstruction's Proca mass. Same physical content: one massive, real spin-1 state. The reconstruction's flat statement that there is no Stückelberg field describes the `.fr` file, not the paper's construction. |
| $X$ is the $U(1)_X$ gauge field; SM fields carry no $U(1)_X$ charge; $X$ carries no SM charge (§1, §2) | §2 field table: `V[101]`, spin 1, colour singlet, no $SU(2)_L$ index, $Q=0$, `SelfConjugate -> True` | **agree** | Real vector, electrically neutral, colour singlet. Correct for an abelian gauge field written in the mass-eigenstate basis. |
| $\mathcal{L}_{SM}$ (eq. 39) | §1.5: `LSM` added unchanged | **agree** | The paper does not modify the SM sector. No kinetic mixing $X$–$B$ and no $X$–$Z$ mass mixing appear anywhere in the paper; the reconstruction says the same. |
| $\epsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \partial_\lambda Z_\rho$ (eq. 59, first) | §1.2 Term 1: $-c_1 s_W\,\varepsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \partial_\lambda Z_\rho$ | **agree** on structure; **disagree** on coefficient | Operator, index structure and the fact that it does not vanish for identical $Z$'s are all correct. The coefficient is the one real numerical disagreement — see D1 and D2. |
| $\epsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \partial_\lambda \gamma_\rho$ (eq. 59, second); $\Gamma_{XZ\gamma} = c_1 c_W\,\epsilon^{\mu\nu\lambda\rho} k_2$ (eq. 40) | §1.2 Term 2: $+c_1 c_W\,\varepsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \partial_\lambda A_\rho$ | **agree** | Coefficient $c_1 c_W$ matches eq. (40), and it also reproduces eq. (41)'s $\Gamma_{X\to Z\gamma}$ exactly when the width is recomputed from the operator. |
| $\epsilon^{\mu\nu\lambda\rho} W^+_\mu X_\nu \partial_\lambda W^-_\rho$ (eq. 59, third); $\Gamma_{XW^+W^-} = c_2\,\epsilon^{\mu\nu\lambda\rho}(k_2-k_1)_\lambda$ | §1.3 `LPortalCharged`: $c_2\,\varepsilon^{\mu\nu\lambda\rho} W^+_\mu X_\nu \partial_\lambda W^-_\rho$ | **agree** | Reproduces the paper's Feynman rule and eq. (41)'s $\Gamma_{X\to W^+W^-}$ exactly. |
| hermiticity of the charged vertex (implicit; the paper writes a real Lagrangian) | §1.4 `HC[LPortalCharged]`: $c_2^*\,\varepsilon^{\mu\nu\lambda\rho} W^-_\mu X_\nu \partial_\lambda W^+_\rho$, and the combined form $c_2\,\varepsilon^{\mu\nu\lambda\rho} X_\nu (W^+_\mu \partial_\lambda W^-_\rho - W^-_\rho \partial_\lambda W^+_\mu)$ | **agree** | I checked the relabelling: the sign in the combined form is right. The vertex is electrically neutral and hermitian, with $c_2$ real. |
| Relative weight $s_W$ vs. $c_W$ of the two neutral vertices, fixed by $F_Y$ in eq. (48)/(15) | §1.2 compact form: $c_1\,\varepsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \partial_\lambda B_\rho$ with $B = c_W A - s_W Z$ | **agree** on the $s_W:c_W$ split | The reconstruction's re-assembly into a single $X$–$Z$–$B$ operator is exactly eq. (15) ($Z \wedge F_Y \wedge X$). This is the right reading of the paper's covariant form, and it explains the $s_W^2$ and $c_W^2$ in eq. (41). |
| Relative **sign** of the $XZZ$ and $XZ\gamma$ vertices (eq. 40, as printed: both `+`) | §1.2: $-c_1 s_W$ and $+c_1 c_W$, i.e. opposite signs | **disagree** | See D1. The paper is self-contradictory here: eq. (40) prints both with `+`, but eq. (15)'s $F_Y$ with $B = c_W A - s_W Z$ forces opposite signs, as the reconstruction has. |
| $\Gamma_{X\to ZZ} = \frac{c_1^2 s_W^2 M_X^3}{192\pi M_Z^2}(1-4M_Z^2/M_X^2)^{5/2}$ (eq. 41) | §3, first term, identical | **agree** (copied verbatim) | Identical to the paper. But it is *not* what the reconstruction's own $\mathcal{L}$ produces — see D2. |
| $\Gamma_{X\to W^+W^-} = \frac{c_2^2 M_X^3}{48\pi M_W^2}(1-4M_W^2/M_X^2)^{5/2}$ (eq. 41) | §3, second term, identical | **agree** | Also consistent with the reconstruction's own $g_{WW}=c_2$. |
| $\Gamma_{X\to Z\gamma} = \frac{c_1^2 c_W^2 M_X^3}{96\pi M_Z^2}(1-M_Z^2/M_X^2)^3(1+M_Z^2/M_X^2)$ (eq. 41) | §3, third term, identical | **agree** | Also consistent with the reconstruction's own $g_{Z\gamma}=c_1 c_W$. |
| $c_1, c_2$ dimensionless, values free, set to $1$ or $0.1$ in the figures (eq. 48 text; Fig. captions) | §3: both External, block `NPCOUPLINGS`, value $1.0$, order `{NP,1}`, dimensionless | **agree** | Dimension-4 operators, so dimensionless couplings. Correct. |
| $M_X \sim 1$ TeV as the benchmark (§1, §5) | §2/§3: $M_X = 1000.$ GeV | **agree** | The paper scans $M_X$ from $\sim 500$ GeV to $4$ TeV; 1 TeV is a representative point, not a prediction. |
| $X$ couples to $\gamma H$ and $Z H$ through eq. (15) (stated in §5.2, after eq. 41: "also allows interaction of the $X$ boson with $\gamma H$ and $ZH$, which are generically small") | absent; §3 states "No decays to fermions or to the Higgs are included, because the model has no such couplings" | **missing-in-reconstruction** | See D3. The paper's eq. (48) carries $H$ explicitly, so $\mathcal{O}(\partial h/v)$ vertices $X$–$Z$–$h$ and $X$–$\gamma$–$h$ exist. The reconstruction's claim is true of the `.fr` file but not of the paper. |
| Non-abelian part of $F_W$ inside eq. (48), second term | absent; §1.4 notes only the abelian $W$ field strength is used | **missing-in-reconstruction** | See D4. $F_W$ is the full $SU(2)_L$ field strength, so eq. (48) also generates 4-point vertices such as $X W^+ W^- Z$ and $X W^+ W^- \gamma$. |
| Stückelberg / Goldstone fields $\theta_X$, $\theta_Z$, $\theta_\pm$ and the physical Higgs $h$ (eq. 13, eq. 39) | absent (unitary gauge, mass-eigenstate basis) | **missing-in-reconstruction** | Expected for an implementation in unitary gauge. It is the cause of D3, not an independent problem. |
| Heavy chiral fermions $\psi_{1,2}$, $\chi_{1,2}$ and heavy Higgs $\Phi$ (Tables 1–4; eq. 12, 60, 70) | absent | **missing-in-reconstruction** | By design. The paper integrates them out; eq. (39) *is* the low-energy theory. Not a defect. |
| anomaly coefficient $\kappa$ and the charge solution $y_{1,2}(x,y)$ (eq. 92, 93, 95) | absent | **missing-in-reconstruction** | Same reason: these fix $c_1, c_2$ in the UV, and the paper itself treats $c_1, c_2$ as free inputs at low energy. Not a defect. |
| — | `V[101]`, PDG 5000023, `ParticleName -> "X"`, `PropagatorType -> Sine`, `M$InteractionOrderHierarchy` with `NP` at order 1 | **extra-in-reconstruction** | Pure implementation bookkeeping. No counterpart in the paper and none needed. |
| — | §3: $W_X$ as an Internal parameter (total width from the three portal decays) | **extra-in-reconstruction** | The paper gives the three partial widths but never a total-width expression. Summing them is the natural choice. |
| Chirality / conjugation structure | §1.5: no fermions, no `Ga`, no `ProjP`/`ProjM`, no `CC`; the only conjugation is $W^+ \leftrightarrow W^-$ | **agree** | Correct for the paper's low-energy theory. All chirality lives in the heavy sector that is integrated out. The reconstruction's point that every portal vertex is parity-odd is right and matches the paper's spin/angular-analysis discussion in §5.3. |

---

## 3. Disagreements, with severity

### D1 — Relative sign of the $XZZ$ and $XZ\gamma$ vertices — **severity: convention, with a substantive consequence**

The reconstruction has $g_{ZZ} = -c_1 s_W$ and $g_{Z\gamma} = +c_1 c_W$, i.e. opposite
signs. The paper's eq. (40) prints both Feynman rules with a `+` sign (the second line
carries only a `\hphantom{-}` spacer). The paper's own covariant form, eq. (15), uses
$F_Y$ with $B_\rho = c_W A_\rho - s_W Z_\rho$, which forces the opposite relative sign
that the reconstruction has. The sign cancels in all three widths of eq. (41), so it
cannot be settled from the widths.

*A human should check* whether eq. (40)'s $XZZ$ line is missing a minus sign, because
the relative sign is physical: it shows up in interference between the $ZZ$ and $Z\gamma$
channels, for example in $Z\gamma \to X \to ZZ$ and in multi-boson final states.

### D2 — Magnitude of the $XZZ$ coefficient — **severity: substantive**

Three statements about the $XZZ$ normalisation exist and no two agree:

- **Paper eq. (40):** $\Gamma_{XZZ} = \tfrac12 c_1 s_W\,\epsilon^{\mu\nu\lambda\rho}(k_2-k_1)_\lambda$, i.e. $\lvert g_{ZZ}\rvert = \tfrac12 c_1 s_W$.
- **Reconstruction §1.2:** $\lvert g_{ZZ}\rvert = c_1 s_W$.
- **Paper eq. (41):** implies $\lvert g_{ZZ}\rvert = c_1 s_W/\sqrt{2}$.

I derived the third number as follows. I recomputed all three partial widths from a
generic vertex $g\,\varepsilon^{\mu\nu\lambda\rho} V^1_\mu X_\nu \partial_\lambda V^2_\rho$,
keeping the leading term in $M_V/M_X$. Only one final-state boson can be longitudinal at
such a vertex (the paper says the same in §5.1). The results are
$\Gamma_{W^+W^-} = g_{WW}^2 M_X^3/(48\pi M_W^2)$,
$\Gamma_{Z\gamma} = g_{Z\gamma}^2 M_X^3/(96\pi M_Z^2)$ and
$\Gamma_{ZZ} = g_{ZZ}^2 M_X^3/(96\pi M_Z^2)$ (the last one already includes the
identical-particle factor $1/2$). The first two reproduce eq. (41) **exactly** with
$g_{WW}=c_2$ and $g_{Z\gamma}=c_1 c_W$ — which validates both the method and those two
lines of the reconstruction. The third gives $c_1^2 s_W^2 M_X^3/(96\pi M_Z^2)$ from the
reconstruction's $g_{ZZ}=c_1 s_W$, i.e. **twice** eq. (41)'s $192\pi$ result. The paper's
$192\pi$ looks like the identical-particle factor $1/2$ applied twice.

The check is visible in a ratio that is free of any overall normalisation: the
reconstruction's Lagrangian gives $\Gamma_{Z\gamma}/\Gamma_{ZZ} = c_W^2/s_W^2 \approx 3.3$,
whereas the paper's eq. (55) states $2 c_W^2/s_W^2 \approx 6.7$. Likewise the
reconstruction's Lagrangian gives $\Gamma_{W^+W^-}/\Gamma_{ZZ} = 2 c_2^2/(s_W^2 c_1^2)$,
whereas the paper's eq. (57) states $4 c_2^2/(s_W^2 c_1^2)$.

*A human should check* the $XZZ$ normalisation directly — fix one convention for $c_1$,
then recompute the $XZZ$ Feynman rule and $\Gamma_{X\to ZZ}$ from it, and decide whether
the reconstruction's $-c_1 s_W$, the paper's eq. (40) $\tfrac12 c_1 s_W$, or neither, is
the intended coefficient. This also decides whether the `.fr` file's Internal width
parameter (copied verbatim from eq. 41) is consistent with the `.fr` file's own
`LPortalNeutral`, which by my calculation it is not, by a factor of 2.

### D3 — Missing $X$–$Z$–$h$ and $X$–$\gamma$–$h$ vertices — **severity: substantive (small in rate)**

The paper's eq. (48) is written with the Higgs doublet, and the paper states after
eq. (41) that eq. (15) "also allows interaction of the $X$ boson with $\gamma H$ and
$ZH$". These come from the $\mathcal{O}(\partial h / v)$ remainder in eq. (15). The
reconstruction has no Higgs field in any portal term and says the model has no Higgs
couplings at all.

*A human should check* whether the `.fr` file was meant to implement the full eq. (48)
(with $h$) or only the pure gauge-boson limit of eq. (59). The paper calls these vertices
"generically small", so the omission is probably deliberate, but it should be recorded as
a deliberate truncation rather than as a property of the model.

### D4 — Non-abelian part of $F_W$ dropped — **severity: substantive**

The second term of eq. (48) contains $F_W$, the full $SU(2)_L$ field strength. Its
non-abelian piece, together with $D H$, generates 4-point vertices ($X W^+ W^- Z$,
$X W^+ W^- \gamma$) alongside the trilinear $X W^+ W^-$ of eq. (59). The reconstruction
keeps only the abelian part and says so explicitly in §1.4, correctly noting that the
term is then not $SU(2)_L$ covariant on its own.

*A human should check* whether the missing quartic vertices matter for the paper's own
phenomenology, in particular for vector-boson fusion $W^+W^- \to X$ (eq. 100) where a
4-point contact term can contribute at the same order.

### D5 — Kinetic-term normalisation and the Stückelberg field — **severity: cosmetic**

The paper writes $-\frac{1}{4g_X^2}\lvert F_X\rvert^2 + \frac{M_X^2}{2}\lvert d\theta_X + X\rvert^2$;
the reconstruction writes the canonical Proca form and states that there is no Stückelberg
field and no Higgs mechanism. These describe the same physical state after choosing
unitary gauge and rescaling $X \to g_X X$.

*A human should check* only that the $1/g_X^2$ rescaling has been absorbed consistently
into **both** $c_1$ and $c_2$, so that the two portal couplings are still measured in the
same units.

### D6 — Default benchmark point sits outside the narrow-width regime — **severity: cosmetic (but worth a note)**

The reconstruction's defaults are $c_1 = c_2 = 1$ and $M_X = 1000$ GeV, and §4 describes
the signature as a "narrow-to-broad diboson resonance". With the paper's own numerical
form of eq. (41) ($\Gamma_{W^+W^-} \approx c_2^2 \cdot 1.03$ TeV, $\Gamma_{Z\gamma} \approx c_1^2 \cdot 307$ GeV,
$\Gamma_{ZZ} \approx c_1^2 \cdot 45$ GeV, all at $M_X = 1$ TeV), that point gives
$\Gamma_X \approx 1.4$ TeV $> M_X$. The paper's LHC figure uses $c_1 = c_2 = 0.1$.

*A human should check* whether the shipped default card is meant as a physically usable
benchmark; if so, smaller $c_i$ would keep the resonance interpretation and the effective
description valid.

### D7 — Index typo in the paper — **severity: cosmetic, no action on the reconstruction**

Paper eq. (40) writes $\Gamma_{XZ\gamma} \propto \epsilon^{\mu\nu\lambda\rho} {k_2}_\rho$,
with $\rho$ already used as a free index. It should read ${k_2}_\lambda$. The
reconstruction's index placement is the correct one. No change is needed on the
reconstruction side.

---

## 4. Overall assessment

The reconstruction identifies the right model. It picks out all three Chern–Simons portal
operators of eq. (59), assigns them to the correct fields, gets the field content right
(one heavy, real, electrically neutral, colour-singlet spin-1 state with no fermion, no
Higgs and no mixing couplings), gets the hermitian conjugation of the charged vertex
right, and — a genuine piece of insight rather than transcription — re-assembles the two
neutral monomials into the single hypercharge operator $c_1\,\varepsilon\,Z X \partial B$,
which is exactly the broken-phase content of the paper's eq. (15). Its statements about
chirality, parity-odd vertex structure, the longitudinal $1/M_V^2$ growth and the
anomaly-induced origin of the operators all track the paper. Two of the three partial
widths it quotes are reproduced exactly by its own Lagrangian coefficients, which is
strong evidence that $g_{Z\gamma} = c_1 c_W$ and $g_{WW} = c_2$ are correct. The open
items are concentrated in one place and in two omissions: the $XZZ$ normalisation, where
the reconstruction, the paper's Feynman rule (eq. 40) and the paper's width (eq. 41) give
three mutually inconsistent coefficients and the paper cannot arbitrate between them; the
relative sign of the two neutral vertices, where the reconstruction follows the paper's
covariant form and contradicts the paper's printed Feynman rule; and two operators that
the covariant eq. (48) contains but the reconstruction does not — the $\mathcal{O}(\partial h/v)$
$X$–$Z$–$h$ and $X$–$\gamma$–$h$ vertices that the paper mentions explicitly, and the
non-abelian part of $F_W$ with its associated quartic vertices. A reviewer should settle
the $XZZ$ factor first, since it propagates into the branching ratios of eq. (55) and
eq. (57) and therefore into every rate the model predicts.
