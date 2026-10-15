# Cross-check: `reconstruction.md` against the paper

RUN-TAG: XM-CROSS-Top-Philic-Zprime__factor2

Paper: "Probing TeV scale Top-Philic Resonances with Boosted Top-Tagging at the High
Luminosity LHC" (Kim, Kong, Lee, Mohlabeng; FERMILAB-PUB-16-125-T).

## 1. Where the paper defines the model

The full model definition is short. It sits in Section II ("A Top-Philic Resonance:
Simplified Model"), Subsection II.A ("Setup"), plus two later statements.

- **Field content.** Section II.A, first sentence: "We consider a color singlet vector
  particle ($V_1$) which dominantly couples to top and anti-top." Section V repeats this:
  "a color singlet vector resonance, $V_1$". No other new state is introduced.
- **Interaction Lagrangian.** Eq. (1) (label `v0inttop`):

  $$
  \mathcal{L}_{int}
  = \bar t\,\gamma_\mu (c_L P_L + c_R P_R)\, t\, V_1^\mu
  = c_t\,\bar t\,\gamma_\mu (\cos\theta\,P_L + \sin\theta\,P_R)\, t\, V_1^\mu .
  $$

- **Conventions and parameters.** Text after Eq. (1): $P_{R/L} = (1 \pm \gamma_5)/2$,
  $c_t = \sqrt{c_L^2 + c_R^2}$, $\tan\theta = c_R/c_L$.
- **Free parameters.** Section II.B: "There are three free parameters, the vector
  resonance mass ($M_{V_1}$), the overall coupling strength ($c_t$) and the chirality
  ($\theta$)."
- **Decay width.** Eq. (2) (label `width`):

  $$
  \Gamma(V_1 \to t\bar t)
  = \frac{c_t^2 M_{V_1}}{8\pi}\sqrt{1 - \frac{4 m_t^2}{M_{V_1}^2}}
    \left[1 - \frac{m_t^2}{M_{V_1}^2}\left(1 - 3\sin 2\theta\right)\right].
  $$

- **Chirality choice.** Section II.B, item 2: "We set $\theta = \frac{\pi}{2}$ for the rest
  of discussion in this paper." Section II.C confirms the meaning: the ATLAS contact
  interaction "for the right-handed top quark (corresponding to $\theta = \pi/2$ in our
  case)".
- **Benchmark point.** Figure 2 caption, Tables VI, VIII and IX: $M_{V_1} = 1.5$ TeV and
  $c_t = 2.0$.
- **Normalization cross-check.** Eq. (3), obtained by integrating out $V_1$ at
  $\theta = \pi/2$:

  $$
  \frac{1}{2}\frac{c_t^2}{M_{V_1}^2}\,
  (\bar t_R \gamma_\mu t_R)(\bar t_R \gamma^\mu t_R).
  $$

- **Implementation statement.** Section III: "Our model implementation is based on the
  Lagrangian of Eq. (1) with parameters $M_{V_1}$, $c_t$ and $\theta$."

The paper never writes the kinetic term or the mass term of $V_1$. It treats $V_1$ as a
massive vector with a free mass, so a Proca kinetic and mass term is implied.

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| $\bar t\,\gamma_\mu (c_L P_L + c_R P_R)\, t\, V_1^\mu$ — Eq. (1) | $2\big[c_L\,\bar t\gamma^\mu P_L t + c_R\,\bar t\gamma^\mu P_R t\big] V_\mu$ | **disagree** | Same fields, same chirality structure, same flavor content. The reconstruction carries an extra overall factor 2. Every $V_1 t\bar t$ vertex is doubled, so every rate is 4 times too large. The reconstruction flags this itself. |
| Left-handed piece $c_L\,\bar t\gamma_\mu P_L t\,V_1^\mu$ — Eq. (1) | $c_L\,\bar t\gamma^\mu P_L t\,V_\mu$ (`ctL`, `ProjM`) | **agree** | Field content, chirality and index structure match. Only the prefactor differs (row above). |
| Right-handed piece $c_R\,\bar t\gamma_\mu P_R t\,V_1^\mu$ — Eq. (1) | $c_R\,\bar t\gamma^\mu P_R t\,V_\mu$ (`ctR`, `ProjP`) | **agree** | Same as above. |
| $P_{R/L} = (1 \pm \gamma_5)/2$ — text after Eq. (1) | `ProjM` $= P_L = (1-\gamma_5)/2$, `ProjP` $= P_R = (1+\gamma_5)/2$ | **agree** | Projector assignment is identical. No chirality swap. |
| $c_L = c_t\cos\theta$, $c_R = c_t\sin\theta$ — second line of Eq. (1) | `ctL` $= c_t\cos\theta_t$, `ctR` $= c_t\sin\theta_t$ | **agree** | The reconstruction reproduces the paper's angular parametrization exactly. |
| $c_t = \sqrt{c_L^2 + c_R^2}$, $\tan\theta = c_R/c_L$ — text after Eq. (1) | "It sets the magnitude $\sqrt{c_L^2 + c_R^2} = c_t$" | **agree** | Consistent inverse relation. |
| $V_1$ is a color-singlet vector — Section II.A, Section V | `V[100]`, spin 1, $SU(3)_C$ singlet, $SU(2)_L$ singlet, $Y = 0$ | **agree** | The reconstruction derives the singlet assignment from the absent `Indices` entries. This matches the paper. |
| $V_1$ is a real (self-conjugate) field — implied by the hermitian form of Eq. (1) | `SelfConjugate -> True`, no `HC` needed | **agree** | The paper does not say "real" in words. A neutral current times a single $V_1^\mu$ is hermitian only if $V_1$ is real, so the two are consistent. |
| Coupling is to the top quark only, flavor diagonal — Section I and Section II.A | Only $t$ appears; current is flavor diagonal and color diagonal | **agree** | The paper drops all other couplings by assumption ("we can ignore all the other couplings except for the one with tops"). |
| Three free parameters $M_{V_1}$, $c_t$, $\theta$ — Section II.B | `MV1`, `ct`, `thV1` | **agree** | Same parameter set, same roles. |
| Benchmark $M_{V_1} = 1.5$ TeV — Figure 2, Tables VI, VIII, IX | `MV1` $= 1500.$ GeV | **agree** | Values match. |
| Benchmark $c_t = 2.0$ — Figure 2, Tables VI, VIII, IX | `ct` $= 2.0$ | **agree** | Values match. |
| $\theta = \pi/2$ — Section II.B item 2 | `thV1` $= 1.5707963267948966$ | **agree** | Equals $\pi/2$ to machine precision. |
| Purely right-handed limit at $\theta = \pi/2$ — Section II.C (ATLAS comparison) | $c_L = 0$, $c_R = 2$ at the stored values | **agree** | The reconstruction reaches the same physical conclusion as the paper. |
| $\Gamma(V_1 \to t\bar t)$ — Eq. (2) | `WV1` $= 229.31$ GeV (stored number, plus an approximate formula) | **agree** | Eq. (2) with $c_t = 2$, $M_{V_1} = 1500$ GeV, $m_t = 172$ GeV and $\theta = \pi/2$ gives $229.3$ GeV. The stored width matches the paper exactly. Note the stored width therefore belongs to the Lagrangian **without** the factor 2. |
| $\Gamma/M_{V_1} \approx c_t^2/(8\pi)$ for $m_t \ll M_{V_1}$ — text after Eq. (2) | $\Gamma/M \approx 0.15$ | **agree** | $c_t^2/(8\pi) = 0.159$ at $c_t = 2$. The paper calls $V_1$ narrow only for small $c_t$; the reconstruction calls the benchmark broad. Both statements are true at their own coupling values. |
| Contact interaction $\frac{1}{2}\frac{c_t^2}{M_{V_1}^2}(\bar t_R\gamma_\mu t_R)(\bar t_R\gamma^\mu t_R)$ — Eq. (3) | no counterpart | **missing-in-reconstruction** | This is a derived low-energy limit, not a term of the model file. Its coefficient $\tfrac12 c_t^2/M^2$ is a second, independent confirmation that Eq. (1) has no factor 2. |
| Proca kinetic and mass term (not written in the paper; implied by "massive vector") | $-\frac14 V_{\mu\nu}V^{\mu\nu} + \frac12 M_{V_1}^2 V_\mu V^\mu$ | **extra-in-reconstruction** | Required for any working implementation, and in the standard real-vector normalization. The paper gives no equation to compare against, so only the normalization convention can be judged. It is correct for a real vector. |
| no counterpart in the paper | PDG code 32, `PropagatorType -> Sine`, `PropagatorArrow -> None`, `ParticleName` | **extra-in-reconstruction** | Bookkeeping and display settings only. No physics content. |
| no counterpart in the paper | `M$InteractionOrderHierarchy` with `{NP, 1}` per vertex | **extra-in-reconstruction** | Counting convention for the generator. The paper does not discuss coupling-order counting. |

## 3. Disagreements, with severity

1. **Overall factor 2 in the top current (`LV1Top` vs Eq. (1)) — substantive.**
   The paper's Eq. (1) has no prefactor, and $c_L$, $c_R$ are already the full couplings.
   The factor 2 doubles every $V_1 t\bar t$ vertex, so it multiplies the $t\bar t t\bar t$
   signal cross section by 4 and the width by 4. Two independent parts of the paper
   confirm that no factor 2 belongs there: Eq. (2) evaluated at the benchmark gives
   $229.3$ GeV, which equals the stored `WV1` $= 229.31$ GeV, and Eq. (3) gives the
   contact coefficient $\tfrac12 c_t^2/M_{V_1}^2$, which is the tree-level exchange of
   Eq. (1) with unit prefactor.
   *Human should check:* open the implementation file and confirm whether the literal `2`
   in front of the `LV1Top` block is real, then remove it or rescale `ct` by $1/2$.

2. **Unbalanced parentheses in `LV1Top` — substantive (implementation, not physics).**
   The reconstruction reports `2 (Block[{mu}, ExpandIndices[...]];` with the closing `)`
   after the statement terminator. The paper has nothing to compare against here, but a
   definition that does not evaluate produces no vertex at all.
   *Human should check:* run the file in FeynRules and confirm that `LV1Top` evaluates and
   that a $V_1 t\bar t$ vertex is produced.

3. **Missing contact-interaction limit (Eq. (3)) — cosmetic.**
   Eq. (3) is a derived result for the experimental comparison, not a model term, so its
   absence from a file-level reconstruction is expected.
   *Human should check:* nothing to fix; use Eq. (3) only as the normalization test
   described in item 1.

4. **Proca kinetic and mass term present in the reconstruction but absent from the paper
   — convention.**
   The paper never writes the free Lagrangian of $V_1$. The reconstruction uses the
   standard real-vector normalization $-\frac14 V_{\mu\nu}V^{\mu\nu} +
   \frac12 M^2 V_\mu V^\mu$, which gives the correct propagator and the correct pole mass
   $M_{V_1}$.
   *Human should check:* confirm that the generated propagator mass equals the `MV1` used
   in the benchmark tables (1.5 TeV).

5. **Width stored as a fixed number instead of computed — convention.**
   `WV1` is hard-coded. It agrees with Eq. (2) at the benchmark point, but it will be
   wrong at any other $(c_t, \theta, M_{V_1})$ unless the scan recomputes it.
   *Human should check:* whether the scans over $c_t$ and $M_{V_1}$ in Figures 3, 12 and
   13 recompute the width, or reuse the stored value.

6. **"Narrow" versus "broad" wording — cosmetic.**
   The paper says $V_1$ "must be a narrow resonance, if it weakly couples to a top pair".
   The reconstruction calls the benchmark broad, with $\Gamma/M \approx 0.15$. Both follow
   from $\Gamma/M \approx c_t^2/(8\pi)$; they describe different coupling values.
   *Human should check:* nothing; the two statements do not conflict.

## 4. Overall assessment

The reconstruction captures the paper's simplified model closely. The field content is
right: one new heavy, neutral, color-singlet, self-conjugate spin-1 state that couples
only to the top quark. The chirality structure of Eq. (1) is right, the projector
assignment is right, the angular parametrization $c_L = c_t\cos\theta$,
$c_R = c_t\sin\theta$ matches the paper's second line of Eq. (1) and its definition
$\tan\theta = c_R/c_L$, and the stored numerical point ($M_{V_1} = 1.5$ TeV, $c_t = 2.0$,
$\theta = \pi/2$, purely right-handed) is exactly the benchmark the paper uses throughout
Sections II to IV. One difference stands out: the reconstruction reports an explicit
overall factor 2 in front of the top current, which Eq. (1) does not have. The
reconstruction flags this itself and supports the flag with a width argument, and two
independent numbers in the paper point the same way — Eq. (2) reproduces the stored
`WV1` = 229.31 GeV only without the factor, and the contact coefficient of Eq. (3) is the
$\tfrac12 c_t^2/M_{V_1}^2$ of an unmodified Eq. (1). The reconstruction also reports a
parenthesis imbalance in the same definition, which no paper statement can settle. A human
reviewer should read the implementation file directly to confirm both the literal `2` and
the bracket structure, and should decide whether the stored width is recomputed during the
parameter scans.
