# Cross-check: `reconstruction.md` vs. the paper

**Paper.** J. H. Kim, K. Kong, S. J. Lee, G. Mohlabeng, *Probing TeV scale Top-Philic Resonances
with Boosted Top-Tagging at the High Luminosity LHC* (FERMILAB-PUB-16-125-T).

**Where the model lives in the paper.**

- Sec. II A (`sec:model`), Eq. (1) (`\label{v0inttop}`): the full interaction Lagrangian, in both the
  $(c_L, c_R)$ form and the $(c_t, \theta)$ form, plus the definitions
  $P_{R/L} = (1 \pm \gamma_5)/2$, $c_t = \sqrt{c_L^2 + c_R^2}$, $\tan\theta = c_R/c_L$.
- Sec. II A, Eq. (2) (`\label{width}`): the analytic width $\Gamma(V_1 \to t\bar t)$.
- Sec. II B (`sec:Production`): the three free parameters $(M_{V_1}, c_t, \theta)$, the choice
  $\theta = \pi/2$ for the whole paper, and the production modes.
- Sec. II C (`sec:constraints`), unnumbered equation after Eq. (2) (the $\frac{1}{2}\frac{c_t^2}{M_{V_1}^2}
  (\bar t_R \gamma_\mu t_R)(\bar t_R \gamma^\mu t_R)$ contact operator): fixes that
  $\theta = \pi/2$ means a **right-handed** top current.
- Sec. III (`sec:simulation`): "Our model implementation is based on the Lagrangian of Eq. (1) with
  parameters $M_{V_1}$, $c_t$ and $\theta$." Benchmark: $M_{V_1} = 1.5$ TeV, $c_t = 2.0$.

The paper writes **only** the interaction term. It never writes a kinetic term, a mass term, a field
table, a width number, or a PDG code. Those parts of the reconstruction have no paper counterpart and
are marked accordingly.

---

## 1. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| $\bar t\,\gamma_\mu\,(c_L P_L + c_R P_R)\,t\,V_1^\mu$ — Eq. (1), first line | `LV1Top` $= (c_L\,\bar t\gamma^\mu P_L t + c_R\,\bar t\gamma^\mu P_R t)V_\mu$ | **agree** | Same operator, same overall sign, same $+1$ coefficient. Colour singlet current $\bar t_i \ldots t_i$ in both. |
| $c_t\,\bar t\,\gamma_\mu(\cos\theta\,P_L + \sin\theta\,P_R)\,t\,V_1^\mu$ — Eq. (1), second line | `ctL` $= c_t\cos\theta_t$ on `ProjM`, `ctR` $= c_t\sin\theta_t$ on `ProjP` | **agree** | $\cos\theta$ goes with the **left** projector and $\sin\theta$ with the **right** one in both. No chirality swap. |
| $P_{R/L} = (1 \pm \gamma_5)/2$ — Eq. (1), text below | `ProjM` $=P_L=\tfrac12(1-\gamma_5)$, `ProjP` $=P_R=\tfrac12(1+\gamma_5)$ | **agree** | The stated FeynRules convention is the standard one and matches the paper's definition. |
| $c_t = \sqrt{c_L^2+c_R^2}$, $\tan\theta = c_R/c_L$ — Eq. (1), text below | $c_L = c_t\cos\theta_t$, $c_R = c_t\sin\theta_t$ (so $c_L^2+c_R^2=c_t^2$, $c_R/c_L=\tan\theta_t$) | **agree** | The two parameterisations are algebraically identical. |
| $\theta = \pi/2$ is the right-handed limit — Sec. II C contact operator $(\bar t_R\gamma_\mu t_R)^2$, and footnote on ATLAS | Benchmark $\theta_t = \pi/2 \Rightarrow c_L = 0$, $c_R = 2$, "purely right-handed", $g_V = -g_A = 1$ | **agree** | Both put the whole coupling on $t_R$ at $\theta=\pi/2$. Limits at $\theta=0$ (pure left) and $\theta=\pi/4$ (pure vector) also follow from the paper's definitions. |
| Chiral decomposition $g_V$, $g_A$ (implicit in Eq. (1); used in Eq. (2)) | $g_V = (c_L+c_R)/2$, $g_A = (c_L-c_R)/2$ in the form $\gamma^\mu(g_V - g_A\gamma_5)$ | **agree** | Sign convention differs from the common $(g_V+g_A\gamma_5)$ form, but the reconstruction is internally consistent and reproduces Eq. (1). |
| Colour-singlet vector particle $V_1$ — Sec. II A, first sentence; Sec. I ("color singlet vector resonance") | `V1` = `V[100]`, spin 1, no colour index, $Q=0$ | **agree** | Neutral, colourless, spin 1. |
| $V_1$ couples to $t$ and $\bar t$ only; all other couplings neglected — Sec. I, Sec. II A | Single interaction term, top quark only; SM sector untouched | **agree** | Paper says "dominantly"/"primarily" and then neglects the rest; the file realises the strict limit. See disagreement D3. |
| Free parameters $(M_{V_1}, c_t, \theta)$ — Sec. II B | External: `ct`, `thV1`; mass `MV1` from the particle class | **agree** | Same three physical inputs. |
| Benchmark $M_{V_1} = 1.5$ TeV, $c_t = 2.0$, $\theta = \pi/2$ — Sec. II B, Fig. 2, Tables V–VIII | `MV1` $=1500.$ GeV, `ct` $=2.$, `thV1` $=1.5707963\ldots$ | **agree** | Numbers match the paper's illustrative point. |
| $\Gamma(V_1\to t\bar t) = \frac{c_t^2 M_{V_1}}{8\pi}\sqrt{1-\frac{4m_t^2}{M_{V_1}^2}}\big[1-\frac{m_t^2}{M_{V_1}^2}(1-3\sin 2\theta)\big]$ — Eq. (2) | Fixed number `WV1` $= 229.31$ GeV, no formula | **agree** (numerically) | Eq. (2) at $M=1500$ GeV, $c_t=2$, $\theta=\pi/2$, $m_t=172$ GeV gives $229.3$ GeV. The reconstruction's $\Gamma/M \simeq 0.153$ also matches the paper's estimate $\Gamma/M\approx c_t^2/8\pi$. But the analytic formula itself is absent; see D2. |
| No new gauge group; Eq. (1) is written as a stand-alone interaction — Sec. II B ("we do not consider any underlying or fundamental theory which might generate Eq. (1)") | No `M$GaugeGroups`, no `DC[...]`; abelian `FS`, explicit Proca mass | **agree** | Both treat $V_1$ as a non-gauge massive vector added by hand. |
| (no counterpart — paper writes only $\mathcal L_{int}$) | `LV1Kin` $= -\frac14 F^V_{\mu\nu}F^{V\mu\nu} + \frac12 M_{V_1}^2 V_\mu V^\mu$ | **extra-in-reconstruction** | Standard Proca normalisation for a real vector; required for any simulation, implied but never written by the paper. |
| (no counterpart) | `SelfConjugate -> True` | **extra-in-reconstruction** | The paper never says $V_1$ is real. A real field is the natural reading of a neutral $t\bar t$ resonance and is consistent with the $-1/4$, $+1/2$ normalisation. |
| (no counterpart) | PDG 32, `PropagatorType -> Sine`, `PropagatorArrow -> None` | **extra-in-reconstruction** | Bookkeeping and drawing only; no physics content. |
| (no counterpart) | `M$InteractionOrderHierarchy` QCD=1, QED=2, NP=1; couplings carry `{NP,1}` | **extra-in-reconstruction** | Implementation bookkeeping. Consistent with the paper's tree-level four-top and one-loop counting. |
| Axial limit $\theta = 3\pi/4$, where loop production $gg\to V_1 j$ and $gg\to V_1 \to t\bar t$ are largest — Sec. II B item 1, Sec. II C | Not mentioned; the reconstruction lists $\theta = 0, \pi/4, \pi/2$ only | **missing-in-reconstruction** | Only a phenomenology remark. The reconstruction's parameterisation does reproduce $c_V = 0$ at $\theta = 3\pi/4$. |
| Four-top rate is independent of $\theta$; loop rate is not — Sec. II B item 2, footnote in Sec. II C | Not mentioned | **missing-in-reconstruction** | Phenomenology, not Lagrangian content. |
| Contact operator $\frac12\frac{c_t^2}{M_{V_1}^2}(\bar t_R\gamma_\mu t_R)(\bar t_R\gamma^\mu t_R)$ — Sec. II C | Not mentioned | **missing-in-reconstruction** | This is the $M_{V_1}\to\infty$ limit of Eq. (1), not a separate term of the model. |
| Eq. (1) is hermitian as written (no `+h.c.` in the paper) | "the term is hermitian only in the special case $\theta_t = \pi/4$" | **disagree** | See D1. The coefficient structure the reconstruction writes is still correct. |

---

## 2. Disagreements

**D1 — Hermiticity claim about $\bar t\gamma^\mu P_{L,R} t$. Severity: substantive (reasoning, not coefficients).**
The reconstruction states that $(\bar t\gamma^\mu P_L t)^\dagger = \bar t\gamma^\mu P_R t$ and concludes that
Eq. (1) is hermitian only when $c_L = c_R$. This is wrong: $\gamma^0 (\gamma^\mu P_L)^\dagger \gamma^0 = \gamma^\mu P_L$,
so each chiral current is self-adjoint and Eq. (1) needs no `+HC[...]` for real $c_L$, $c_R$ — which is why the
paper writes it without one. *A human should check this line of the reconstruction and delete the warning, so
that the absent `HC` is not later reported as an implementation defect.*

**D2 — Width stored as a fixed number instead of Eq. (2). Severity: convention.**
`WV1 = 229.31` GeV reproduces Eq. (2) exactly at the shipped point ($M=1.5$ TeV, $c_t=2$, $\theta=\pi/2$,
$m_t \simeq 172$ GeV), but it is a constant in the file, while the paper scans $c_t$ and $M_{V_1}$ over the whole
$(M_{V_1}, c_t)$ plane in Figs. 3, 11 and 12. *A human should check that the width is recomputed (auto-width or a
re-derived value) at every scan point, not left at 229.31 GeV.*

**D3 — "couples only to the top quark" vs. "couples primarily to the top quark". Severity: cosmetic.**
The paper keeps small couplings to light quarks in words and then neglects them; the file sets them to zero.
*A human should confirm that the strict top-only limit is intended for the simulated samples.*

**D4 — Phenomenology statements without a paper source. Severity: cosmetic.**
The reconstruction adds a peak–dip interference line shape in $gg\to t\bar t$ and a "$\sim 100\%$ branching
ratio to $t\bar t$" statement. The paper discusses off-shell $gg \to V_1 \to t\bar t$ and two-body decay above
threshold, but not the line shape. *A human should treat these as the reconstruction's own commentary.*

**D5 — Model-level caveat (not a mismatch between the two documents). Severity: convention.**
The paper calls Eq. (1) "renormalizable", while both documents describe a massive non-gauge vector with a
chiral (non-conserved) current. *A human should note that this is a property of the paper's simplified model,
which the reconstruction copies faithfully, and not a reconstruction error.*

No disagreement was found in field content, representations, charges, chirality assignment, conjugation, or
coefficient structure.

---

## 3. Overall assessment

The reconstruction reproduces the paper's model Lagrangian, Eq. (1) of Sec. II A, term by term: one colour- and
charge-neutral spin-1 state coupled to a top-quark current only, with independent left- and right-handed
strengths written as $c_L = c_t\cos\theta$ and $c_R = c_t\sin\theta$ on the projectors $P_L$ and $P_R$
respectively. The projector convention, the definitions $c_t=\sqrt{c_L^2+c_R^2}$ and $\tan\theta=c_R/c_L$, the
right-handed reading of $\theta=\pi/2$ (confirmed independently by the contact operator in Sec. II C), and the
benchmark values $M_{V_1}=1.5$ TeV, $c_t=2.0$ all match. The stored width, 229.31 GeV, reproduces Eq. (2) at
that benchmark to three digits, which is an independent numerical confirmation that the chirality angle enters
the implementation the same way as in the paper. The parts of the reconstruction with no paper counterpart —
the Proca kinetic and mass terms, `SelfConjugate`, the PDG code and the NP interaction order — are standard
choices needed to simulate Eq. (1), and none of them changes the physics content. The one clear defect is the
hermiticity paragraph, which misstates the adjoint of a chiral vector current and would, if believed, send a
reviewer looking for a missing `+HC` that Eq. (1) does not need; the second point worth attention is the
hard-coded width against the paper's parameter scans. Both are matters for the human reviewer to settle.
