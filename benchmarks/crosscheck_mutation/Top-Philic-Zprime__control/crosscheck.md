# Cross-check: `reconstruction.md` against the paper

**Paper:** *Probing TeV scale Top-Philic Resonances with Boosted Top-Tagging at the High
Luminosity LHC* (FERMILAB-PUB-16-125-T), Kim, Kong, Lee, Mohlabeng.

**Reconstruction:** `reconstruction.md`, an independent read-out of `sanitized.fr`.

---

## 1. Where the paper defines the model

The paper puts the complete model in **Section II ("A Top-Philic Resonance: Simplified
Model")**. The relevant places are:

| Location | Content |
|---|---|
| Sec. II A, first sentence | "We consider a color singlet vector particle ($V_1$) which dominantly couples to top and anti-top." |
| **Eq. (1)** (`\label{v0inttop}`), Sec. II A | The interaction Lagrangian, in two equivalent forms. |
| Text after Eq. (1) | $P_{R/L} = (1 \pm \gamma_5)/2$, $c_t = \sqrt{c_L^2 + c_R^2}$, $\tan\theta = c_R/c_L$. |
| **Eq. (2)** (`\label{width}`), Sec. II A | $\Gamma(V_1 \to t\bar t)$, and the limit $\Gamma/M_{V_1} \approx c_t^2/8\pi$. |
| Sec. II B, item 2 | "We set $\theta = \pi/2$ for the rest of discussion in this paper." |
| Sec. II B, paragraph 3 | The three free parameters: $M_{V_1}$, $c_t$, $\theta$. |
| **Eq. (3)**, Sec. II C | The contact operator obtained by integrating $V_1$ out at $\theta = \pi/2$. |
| Sec. III, first paragraph | "Our model implementation is based on the Lagrangian of Eq. (1) with parameters $M_{V_1}$, $c_t$ and $\theta$." |
| Sec. IV, Tables VI, VIII, X | Benchmark point $M_{V_1} = 1.5$ TeV, $c_t = 2.0$. |

Paper Eq. (1) reads

$$
\mathcal{L}_{int} \;=\; \bar t\,\gamma_\mu\,(c_L P_L + c_R P_R)\,t\,V_1^\mu
\;=\; c_t\,\bar t\,\gamma_\mu\,(\cos\theta\,P_L + \sin\theta\,P_R)\,t\,V_1^\mu .
$$

The paper writes **no** kinetic term and **no** mass term. It gives only the interaction.

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Colour-singlet spin-1 field $V_1$ (Sec. II A, first sentence; Sec. V) | `V1` = `V[100]`, spin 1, no colour index | **agree** | Same field content: one new vector, no colour. |
| $V_1$ electrically neutral, $SU(2)_L$ singlet (implicit: $V_1 \to t\bar t$, Sec. II B) | $Q = 0$, $Y = 0$, no `SU2W` index | **agree** | The paper never states the electroweak numbers. They follow from the neutral $t\bar t$ current in Eq. (1). |
| $V_1$ real / self-conjugate (implicit: single $V_1^\mu$ in a hermitian Eq. (1)) | `SelfConjugate -> True`, `PropagatorArrow -> None` | **agree** | Consistent. The paper does not say it in words. |
| One new field only; no new fermion, no new scalar (Sec. II A, Sec. II B) | Only `V1` added; SM top taken from the base model | **agree** | |
| Eq. (1), form 1: $\bar t\,\gamma_\mu (c_L P_L + c_R P_R)\, t\, V_1^\mu$ | `LV1Top` $= \bar t\,\gamma^\mu(c_L P_L + c_R P_R)\,t\,V_\mu$ | **agree** | Same Dirac structure, same chirality split, same index contraction. Index height is notation only. |
| Eq. (1), form 2: $c_t(\cos\theta P_L + \sin\theta P_R)$ | `ctL` $= c_t\cos\theta_t$, `ctR` $= c_t\sin\theta_t$ | **agree** | Identical parameterisation. |
| $P_{R/L} = (1 \pm \gamma_5)/2$ (after Eq. (1)) | `ProjM` $= P_L = (1-\gamma_5)/2$, `ProjP` $= P_R = (1+\gamma_5)/2$ | **agree** | |
| $c_t = \sqrt{c_L^2 + c_R^2}$, $\tan\theta = c_R/c_L$ (after Eq. (1)) | $c_L = c_t\cos\theta_t$, $c_R = c_t\sin\theta_t$ | **agree** | The two statements are inverses of each other. |
| Overall coefficient of the bilinear = 1 (Eq. (1): no $1/2$, no $i$, no $g$) | Coefficient = 1 | **agree** | Normalisation matches, so $c_t$ means the same number in both. |
| Hermiticity: Eq. (1) written with no $+\,{\rm h.c.}$ | No `HC`; each bilinear separately hermitian | **agree** | Correct reasoning: $V_\mu$ real and $c_{L,R}$ real. |
| Flavour-diagonal $t$–$\bar t$ current (Eq. (1)) | No `CC`; top number conserved | **agree** | |
| Colour contraction $\bar t_i \dots t_i$ (implicit, $V_1$ colour singlet) | $\delta_{ij}$, implicit sum | **agree** | |
| Kinetic term $-\tfrac14 V_{\mu\nu}V^{\mu\nu}$ — **not written in the paper** | `LV1Kin`: $-\tfrac14 V_{\mu\nu}V^{\mu\nu}$, abelian $V_{\mu\nu} = \partial_\mu V_\nu - \partial_\nu V_\mu$ | **extra-in-reconstruction** | Physically required for a propagating vector, and implied by the paper's use of a $V_1$ propagator. The paper simply omits it. |
| Mass term $+\tfrac12 M_{V_1}^2 V_\mu V^\mu$ — **not written in the paper** | `LV1Kin` mass term, Proca form | **extra-in-reconstruction** | The paper uses $M_{V_1}$ as a free parameter everywhere, so the term is implied. Normalisation $\tfrac12$ is the right one for a real field. |
| No underlying gauge theory: "we ... do not consider any underlying or fundamental theory which might generate Eq. (1)" (Sec. II B) | Mass put in by hand; $V_1$ is not a gauge field; any $U(1)'$ is implicit | **agree** | |
| No $V_1$ self-interaction, no $V_1$–gauge-boson coupling (implicit in Eq. (1)) | Abelian field strength, no self-interaction | **agree** | |
| Three free parameters $M_{V_1}$, $c_t$, $\theta$ (Sec. II B) | `MV1`, `ct`, `thV1` external | **agree** | The reconstruction adds `WV1`, which the paper derives instead (see next row). |
| Eq. (2): $\Gamma(V_1 \to t\bar t) = \frac{c_t^2 M_{V_1}}{8\pi}\sqrt{1-\frac{4m_t^2}{M_{V_1}^2}}\,[1-\frac{m_t^2}{M_{V_1}^2}(1-3\sin 2\theta)]$ | `WV1` $= 229.31$ GeV | **agree** | Numerical check: at $M_{V_1}=1500$ GeV, $c_t=2$, $\theta=\pi/2$ ($\sin 2\theta = 0$), $m_t = 172$ GeV, Eq. (2) gives $229.31$ GeV. Exact match. |
| $\Gamma/M_{V_1} \approx c_t^2/8\pi$ for $m_t \ll M_{V_1}$ (after Eq. (2)) | $\Gamma/M \approx 0.15$ | **agree** | $c_t^2/8\pi = 0.159$ at $c_t = 2$. |
| $\theta = \pi/2$ for the whole paper (Sec. II B, item 2) | `thV1` default $= \pi/2$ | **agree** | |
| $\theta = \pi/2$ is the purely right-handed point (Sec. II C: ATLAS "contact interaction for the right-handed top quark ... corresponding to $\theta = \pi/2$ in our case") | $c_L = 0$, $c_R = 2$, purely right-handed | **agree** | |
| Benchmark $M_{V_1} = 1.5$ TeV, $c_t = 2.0$ (Sec. IV, Tables VI, VIII, X; Fig. 2) | `MV1` $= 1500$ GeV, `ct` $= 2$ | **agree** | |
| Axial limit at $\theta = \tfrac34\pi$ (Sec. II B item 1, Sec. II C) | Reconstruction names $\theta_t = \pi/4$ as the pure-vector point; does not name the axial point | **agree** | Consistent: $\theta = \pi/4 \Rightarrow g_A = 0$; $\theta = 3\pi/4 \Rightarrow g_V = 0$. The axial point is simply not mentioned. |
| Vector/axial form $\gamma^\mu(g_V + g_A\gamma_5)$ — not in the paper | $g_V = (c_R+c_L)/2$, $g_A = (c_R-c_L)/2$ | **extra-in-reconstruction** | The algebra is correct. See disagreement D1 for a sign slip in the worked example. |
| Eq. (3): contact operator $\frac12\frac{c_t^2}{M_{V_1}^2}(\bar t_R\gamma_\mu t_R)(\bar t_R\gamma^\mu t_R)$ | absent | **missing-in-reconstruction** | Expected. Eq. (3) is a derived low-energy limit used only to compare with ATLAS, not part of the model file. |
| "couples primarily to the top quark and weakly to the light quarks (top-philic), such that we can ignore all the other couplings" (Sec. I) | "couples **only** to the top quark" | **agree** | Same working model. The paper's light-quark couplings are set to zero in practice. |
| Tree production $t\bar t V_1$, $tWV_1$, $tjV_1$, with $V_1 \to t\bar t$ (Sec. II B item 2) | "$pp \to t\bar t V_1$, $pp \to t V_1$ with an extra top, four-top" | **agree** | Narrative only, not a Lagrangian term. The reconstruction does not name $tWV_1$ separately. |
| Loop production: on-shell $pp \to V_1 + j$, and **off-shell** $gg \to V_1 \to t\bar t$ (Sec. II B item 1) | "loop-level $gg \to V_1$ production and $V_1 \to gg,\ \gamma\gamma$ decays through the top loop" | **disagree** | See disagreement D2. |
| $V_1$ decays essentially to $t\bar t$ above $2m_t$ (Sec. II B) | Same | **agree** | |
| PDG code, `ParticleName`, `PropagatorLabel`, `PropagatorType`, LHA block `TOPPHILIC`, `InteractionOrder -> {NP,1}`, `M$InteractionOrderHierarchy` | present | **extra-in-reconstruction** | Implementation metadata. The paper has no counterpart and needs none. |

---

## 3. Disagreements

### D1. Sign slip in the worked $g_V$, $g_A$ example — severity: **convention**

Section 3 of the reconstruction contradicts itself in one sentence: it writes
"$g_V = -g_A = 1$ in the $(g_V + g_A\gamma_5)$ basis... explicitly $g_V = g_A = 1$ with the
sign convention $g_V = (c_R+c_L)/2$, $g_A = (c_R-c_L)/2$." With $c_L = 0$ and $c_R = 2$ the
second statement is the correct one ($g_V = g_A = 1$); the first is wrong.

*Human check:* confirm that the intended relative sign of $g_A$ is $+$ for a purely
right-handed coupling, and delete the "$g_V = -g_A$" clause.

### D2. Loop-level claims violate the Landau–Yang theorem — severity: **substantive**

The reconstruction's physics summary says $V_1$ "induces loop-level $gg \to V_1$ production
and $V_1 \to gg,\ \gamma\gamma$ decays through the top loop." A massive spin-1 particle
cannot couple to two on-shell massless gauge bosons in a symmetric colour state
(Landau–Yang). The paper is careful about exactly this point: it lists on-shell loop
production only as $pp \to V_1 + j$, and $gg \to V_1 \to t\bar t$ only as an **off-shell**
contribution (Sec. II B, item 1). $V_1 \to \gamma\gamma$ is never mentioned in the paper.

*Human check:* confirm that the loop-level statements are removed or restated as
$pp \to V_1 + j$ and off-shell $gg \to V_1^* \to t\bar t$. This is narrative text, not a
Lagrangian term, so it does not change the implemented model.

### D3. "Broad resonance" wording — severity: **cosmetic**

The reconstruction calls $V_1$ "a broad resonance" at $\Gamma/M \approx 0.15$. The paper
states "$V_1$ must be a narrow resonance, if it weakly couples to a top pair" (after
Eq. (2)). The two statements are not in conflict, because the paper's statement is
conditional on a small $c_t$, while the benchmark uses $c_t = 2$.

*Human check:* none needed; only confirm that no narrow-width approximation is assumed
downstream at $c_t = 2$.

### D4. Width treated as an independent input — severity: **convention**

The reconstruction lists `WV1` as an external parameter. In the paper the width is a
prediction of Eq. (2) from $(M_{V_1}, c_t, \theta)$. The stored value $229.31$ GeV happens
to be exactly the Eq. (2) value at the benchmark, so there is no numerical conflict at the
default point.

*Human check:* confirm that `WV1` is recomputed whenever $c_t$, $\theta$ or $M_{V_1}$ is
changed away from the benchmark; a fixed width would be wrong elsewhere in the scan of
Figs. 8 and 9.

### D5. Electroweak quantum numbers are inferred, not stated — severity: **cosmetic**

The reconstruction asserts $SU(2)_L$ singlet, $Y = 0$, $Q = 0$ from the absence of index
declarations. The paper states only "color singlet vector particle". The assignment is the
only one consistent with Eq. (1) and with $V_1 \to t\bar t$, but it is an inference.

*Human check:* note that Eq. (1) with $c_L \neq c_R$ is not $SU(2)_L$ invariant on its own,
since $t_L$ sits in a doublet with $b_L$. This is accepted simplified-model practice and the
paper calls Eq. (1) "renormalizable" in that spirit; no action is needed unless the model is
used above the electroweak scale in a gauge-invariant setting.

---

## 4. Overall assessment

On the physics that the paper actually writes down, the reconstruction and the paper match
term by term. The interaction Lagrangian is identical in field content, chirality
structure, projector convention, colour and Dirac contraction, hermiticity, and overall
normalisation; the $(c_L, c_R) \leftrightarrow (c_t, \theta)$ parameterisation in the
reconstruction is the exact inverse of the relations the paper gives after Eq. (1); and the
default values $M_{V_1} = 1500$ GeV, $c_t = 2$, $\theta = \pi/2$ reproduce the paper's
benchmark point, with the stored width $229.31$ GeV equal to Eq. (2) evaluated there. The
kinetic and Proca mass terms in the reconstruction have no written counterpart in the paper,
but they are required for a propagating massive vector and carry the standard real-field
normalisation, so they are additions of substance rather than of conflict. The only items
that need a human eye are outside the Lagrangian itself: a self-contradicting sign in the
worked $g_V$/$g_A$ example, a loop-level production and decay claim that the Landau–Yang
theorem forbids and that the paper deliberately phrases differently, and the treatment of
the width as an independent input rather than as a derived quantity. The pass/fail decision
is left to the human reviewer.
