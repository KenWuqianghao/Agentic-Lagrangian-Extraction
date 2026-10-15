# Cross-check: `reconstruction.md` against the paper

**Paper:** *Probing TeV scale Top-Philic Resonances with Boosted Top-Tagging at the High Luminosity LHC*
(Kim, Kong, Lee, Mohlabeng; FERMILAB-PUB-16-125-T).

**Reconstruction under review:** `reconstruction.md`, an independent read-out of `sanitized.fr`.

---

## 0. Where the paper defines the model

The full new-physics model of the paper sits in **Section II A ("Setup")**, lines around Eq. (1):

- **Eq. (1) (`\label{v0inttop}`)** — the only Lagrangian the paper writes:

  $$
  \mathcal{L}_{int} \;=\; \bar t\,\gamma_\mu\,(c_L P_L + c_R P_R)\,t\;V_1^\mu
  \;=\; c_t\,\bar t\,\gamma_\mu\,(\cos\theta\,P_L + \sin\theta\,P_R)\,t\;V_1^\mu .
  $$

- **Text below Eq. (1)** — the conventions: $P_{R/L} = (1 \pm \gamma_5)/2$,
  $c_t = \sqrt{c_L^2 + c_R^2}$, $\tan\theta = c_R/c_L$.

- **Eq. (2) (`\label{width}`)** — the decay width:

  $$
  \Gamma(V_1 \to t\bar t) \;=\; \frac{c_t^2 M_{V_1}}{8\pi}\sqrt{1-\frac{4m_t^2}{M_{V_1}^2}}
  \left[\,1 - \frac{m_t^2}{M_{V_1}^2}\Big(1 - 3\sin 2\theta\Big)\right].
  $$

- **Section II A, first sentence** — the field content: "a color singlet vector particle ($V_1$)
  which dominantly couples to top and anti-top".

- **Section II B** — three free parameters $(M_{V_1}, c_t, \theta)$, and the choice
  $\theta = \pi/2$ for the rest of the paper.

- **Section II C, unnumbered equation after Eq. (2)** — the contact operator that follows when
  you integrate out $V_1$ at $\theta = \pi/2$:
  $\tfrac{1}{2}\,\tfrac{c_t^2}{M_{V_1}^2}\,(\bar t_R\gamma_\mu t_R)(\bar t_R\gamma^\mu t_R)$.

- **Section III, first paragraph** — "Our model implementation is based on the Lagrangian of
  Eq. (1) with parameters $M_{V_1}$, $c_t$ and $\theta$." Benchmark: $M_{V_1} = 1.5$ TeV,
  $c_t = 2.0$.

The paper writes **no** kinetic term and **no** mass term for $V_1$. It treats them as understood.

---

## 1. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| $\bar t\,\gamma_\mu(c_L P_L + c_R P_R)\,t\,V_1^\mu$ — the interaction, Eq. (1) | **Absent** from `LTotal`. Written only in §1b as an inference, clearly marked "NOT present in the file". | **missing-in-reconstruction** | This is the whole model of the paper. The reconstruction reports that the implementation file holds only the free Proca part. The *inferred* form in §1b is identical to Eq. (1), field by field. |
| $c_L = c_t\cos\theta$, $c_R = c_t\sin\theta$ (from $c_t=\sqrt{c_L^2+c_R^2}$, $\tan\theta = c_R/c_L$, below Eq. (1)) | `ctL = ct Cos[thV1]`, `ctR = ct Sin[thV1]` (§3, internal parameters) | **agree** | Same polar parametrisation. The paper's two relations fix $(c_L,c_R)=c_t(\cos\theta,\sin\theta)$ up to one overall sign. |
| $P_{R/L} = (1\pm\gamma_5)/2$ (below Eq. (1)) | $P_{L,R} = \tfrac12(1\mp\gamma_5)$, FeynRules `ProjM`/`ProjP` (§1b) | **agree** | Identical operators, only the order of writing differs. |
| Chirality structure: $P_L$ pairs with $c_L$, $P_R$ pairs with $c_R$ (Eq. (1)) | Same pairing (§1b, §3) | **agree** | No left/right swap. |
| Lorentz structure: vector current $\gamma_\mu$, no tensor or scalar piece (Eq. (1)) | $\gamma^\mu$ only (§1b) | **agree** | The equivalent $g_V + g_A\gamma_5$ form given in §1b is the correct rewrite, $g_{V,A} = (c_R \pm c_L)/2$. |
| Colour structure: $V_1$ is a colour singlet, so the top current is a colour singlet (Section II A) | Colour singlet current, $\delta_{ij}$ (§1b, §2 field table) | **agree** | |
| Coupling to light quarks or other SM fields: none (Section I, Section II A — "top-philic") | No such term; no SM field declared (§1.3, §4) | **agree** | Both the paper and the file couple $V_1$ to the top only. |
| Overall normalisation of the vertex — unit coefficient, fixed twice: by Eq. (1) itself and by the contact operator $\tfrac12 c_t^2/M_{V_1}^2 (\bar t_R\gamma t_R)^2$ (Section II C) | §1b writes the unit-normalised form, but says the normalisation "cannot be fixed with certainty" | **agree** | The written term is right. Only the stated confidence is too low; the paper removes the ambiguity. See D3. |
| Hermiticity: no $+\mathrm{h.c.}$ in Eq. (1) — the current is self-hermitian and $V_1$ is real | "The term is self-hermitian for real $c_{L,R}$ and real $V_1$, so no `+HC[...]` is required" (§1b) | **agree** | |
| $V_1$ is a real (self-conjugate) vector — implied by Eq. (1) with no h.c., and by the contact operator | `SelfConjugate -> True` (§2) | **agree** | The paper never says "real" in words, but Eq. (1) only makes sense for a real $V_1$. |
| $\Gamma(V_1\to t\bar t)$, Eq. (2) | $\Gamma = \frac{N_c M}{24\pi}\sqrt{1-4x}\big[(c_L^2+c_R^2)(1-x) + 6c_Lc_R x\big]$ (§1b) | **agree** | Algebraically the same. Put $N_c=3$ and $c_Lc_R = \tfrac12 c_t^2\sin2\theta$ and the bracket becomes $c_t^2[1-x(1-3\sin2\theta)]$, and the prefactor becomes $c_t^2M/8\pi$. Note that the paper's Eq. (2) already carries $N_c=3$ inside its $1/8\pi$. |
| $t\bar t$ is the only decay channel in the TeV range (Section II B) | "$t\bar t$ is the only open channel" (§1b, §4) | **agree** | |
| $M_{V_1} = 1.5$ TeV benchmark (Section III, Fig. 2, all cut-flow tables) | `MV1` mass value $1500$ GeV (§2) | **agree** | |
| $c_t = 2.0$ benchmark (Section III, all cut-flow tables) | `ct` external value $2.$ in block `TOPPHILIC` (§3) | **agree** | |
| $\theta = \pi/2$, fixed "for the rest of discussion" (Section II B, item 2) | `thV1 = 1.5707963267948966` $=\pi/2$ (§3) | **agree** | Both then give $c_L=0$, $c_R=2$: a purely right-handed top coupling. Confirmed by Section II C, which speaks of $\bar t_R\gamma t_R$ at $\theta=\pi/2$. |
| Stored width $229.31$ GeV | `Width -> {WV1, 229.31}` (§2), re-derived in §1b | **agree** | Eq. (2) at $M=1500$ GeV, $c_t=2$, $\theta=\pi/2$, $m_t=172$ GeV gives $229.3$ GeV. The number is the paper's own formula at the paper's own benchmark. |
| Kinetic term of $V_1$: **not written** in the paper | $-\tfrac14 V_{1\mu\nu}V_1^{\mu\nu}$, abelian field strength (§1.1) | **agree** | Implied, not stated. A propagating massive vector needs it, and the paper's Fig. 1 diagrams use a $V_1$ propagator. |
| Mass term of $V_1$: **not written** in the paper, but $M_{V_1}$ is a declared free parameter (Section II B) | $+\tfrac12 M_{V_1}^2 V_{1\mu}V_1^\mu$ (§1.2) | **agree** | The $1/2$ is the right normalisation for a real field, and matches `SelfConjugate -> True`. |
| Electroweak quantum numbers of $V_1$: the paper says only "color singlet" | $SU(2)_L$ singlet, $U(1)_Y$ charge $0$, electrically neutral (§2) | **agree** | Consistent with a neutral $t\bar t$ resonance. The paper does not state this, so it is an implementation choice, not a paper statement. See D1. |
| Covariant derivative of $V_1$: not discussed | $D_\mu V_{1\nu} = \partial_\mu V_{1\nu}$ (§1.4) | **agree** | Follows from the singlet assignment. |
| `PDG -> 32`, `PropagatorType -> Sine`, `PropagatorArrow -> None`, `ParticleName` | Listed in §2 | **extra-in-reconstruction** | Implementation metadata. The paper fixes none of it. No physics content. |
| Production modes: loop $pp\to V_1 + j$ and off-shell $gg\to V_1\to t\bar t$; tree-level $t\bar tV_1$, $tWV_1$, $tjV_1$ (Section II B) | "$gg\to t\bar tV_1$ and $pp\to t\bar tV_1$ associated production, or through $tW$/$t$-channel top loops" (§4) | **disagree** | The reconstruction mixes the tree-level channels with the loop channel. See D2. Phenomenology only; no Lagrangian term depends on it. |
| Axial limit $\theta = 3\pi/4$, where loop production is largest (Section II B, Section II C) | §3 lists $\theta=0$, $\pi/4$, $\pi/2$ only | **missing-in-reconstruction** | A gap in the discussion, not in the model. The parametrisation given does reproduce $c_L=-c_R$ at $3\pi/4$. |

---

## 2. Disagreements, with severity

**D1. Electroweak quantum numbers are asserted, not derived from the paper.**
*Severity: convention (with a physics caveat).*
The paper says only "color singlet". The reconstruction adds $SU(2)_L$ singlet and $Y=0$. That is
the standard reading, but note that a strict electroweak-singlet $V_1$ with $c_L\neq 0$ couples to
$t_L$ alone and not to $b_L$, which breaks $SU(2)_L$. The paper accepts this: it says it does "not
consider any underlying or fundamental theory which might generate Eq. (1)". At the benchmark
$\theta=\pi/2$ the point is moot, because $c_L=0$.
*A human should check that the benchmark keeps $\theta=\pi/2$, or that any $c_L\neq 0$ run is
understood as a simplified model that is not $SU(2)_L$ invariant.*

**D2. The production-mode summary in §4 is garbled.**
*Severity: cosmetic.*
The paper separates one-loop production ($pp\to V_1+j$, and off-shell $gg\to V_1\to t\bar t$) from
tree-level $V_1$-strahlung ($t\bar tV_1$, $tWV_1$, $tjV_1$). The reconstruction writes
"$gg\to t\bar tV_1$ ... or through $tW$/$t$-channel top loops", which blends the two.
*A human should ignore this for model validation; it touches no Lagrangian term.*

**D3. The reconstruction understates how well the vertex normalisation is fixed.**
*Severity: cosmetic.*
§1b says an overall factor "cannot be fixed with certainty from the remaining file alone". That is
true of the file, but the paper fixes it twice over: Eq. (1) is written with unit coefficient, and
the contact operator $\tfrac12 c_t^2/M_{V_1}^2(\bar t_R\gamma_\mu t_R)(\bar t_R\gamma^\mu t_R)$ in
Section II C is exactly what a unit-coefficient real-vector exchange gives.
*A human should confirm that the restored FeynRules term carries coefficient 1, not $1/2$.*

**D4. The interaction term is absent from the implementation file.**
*Severity: substantive — but it is a finding about the file, not an error by the reconstruction.*
The paper's entire model is Eq. (1). The reconstruction reports that `LTotal := LV1Kin` holds only
the Proca kinetic and mass terms, and that `ct`, `thV1`, `ctL`, `ctR` are declared but used
nowhere. As encoded, the model gives no $V_1$ vertex, so it can produce none of the paper's
results, and the stored width $229.31$ GeV contradicts a decoupled, stable $V_1$.
*A human should open the implementation file and confirm that no `LV1Top`-style term exists, then
restore $V_1^\mu\,\bar t\gamma_\mu(c_LP_L + c_RP_R)t$ and re-run one benchmark cross section.*

**D5. The axial point $\theta = 3\pi/4$ is not mentioned.**
*Severity: cosmetic.*
The paper singles out $\theta=3\pi/4$ as the axial limit, where loop production and the $t\bar t$
bound are strongest. The reconstruction lists only $0$, $\pi/4$ and $\pi/2$.
*A human should check that any scan over $\theta$ still covers the axial region.*

---

## 3. Overall assessment

On every point of physics that the paper states, the reconstruction and the paper line up. The
field content matches: one real, colour-singlet, electrically neutral, massive spin-1 boson at
1.5 TeV that couples to the top quark alone. The coupling structure matches: a vector current
$\gamma^\mu$ with a left/right split $c_L = c_t\cos\theta$, $c_R = c_t\sin\theta$, the same
projector convention, the same colour-singlet contraction, no extra hermitian conjugate, and the
same numerical benchmark $c_t = 2$, $\theta = \pi/2$, $M_{V_1} = 1500$ GeV. The width formula
quoted in the reconstruction is algebraically identical to the paper's Eq. (2) once $N_c = 3$ and
$c_Lc_R = \tfrac12 c_t^2\sin2\theta$ are inserted, and it reproduces the stored 229.31 GeV. The
free Proca terms that the reconstruction reports are the standard, and necessary, completion of a
Lagrangian the paper chose not to write out. The one substantive gap is not a mismatch between the
two documents but a gap inside the implementation file itself: the $V_1\bar t t$ interaction — the
entire content of the paper's Eq. (1) — is not present in the file, and the reconstruction says so
plainly and repeatedly, then infers the removed term correctly from the orphaned parameters, the
`TOPPHILIC` block name, the PDG code and the stored width. The remaining differences are wording
in the phenomenology paragraph, an unstated electroweak assignment, and an overly cautious remark
about a normalisation the paper in fact pins down. A human reviewer should focus on restoring and
re-validating the interaction term, and should decide separately whether a reconstruction that
correctly reports a missing term counts as a faithful reconstruction of the paper's model.
