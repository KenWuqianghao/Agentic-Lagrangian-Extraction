# Cross-check: `reconstruction.md` against the paper

**RUN-TAG:** XM-CROSS-368sextets__factor2

**Paper:** *The phenomenological cornucopia of SU(3) exotica* — L. M. Carpenter, T. Murphy, T. M. P. Tait (UCI-HEP-TR-2021-26).

---

## 1. Where the paper defines the model

The paper has two parts. Section II builds a general catalog of color-sextet
operators. Section III picks a small subset of that catalog and defines the concrete
simplified model. The reconstruction describes an implementation file, so the correct
target is Section III, not the full catalog.

| Item | Location in `paper.tex` |
| --- | --- |
| Sextet **fermion** model Lagrangian | Sec. III, Eq. `\label{sFmodel}` (the first `multline` in Sec. III, "The sextet fermion models are defined by") |
| Sextet **scalar** model Lagrangian | Sec. III, Eq. `\label{sSmodel}` ("The models for sextet scalars are analogously given by") |
| Field content, hypercharge, lepton number | Sec. III, **Table X** (`\label{fields}`) |
| Parent operator list for both models | Sec. II.C, **Table IX** (`\label{t9}`), invariant **3** ⊗ **6** ⊗ **8** |
| Clebsch-Gordan coefficients **K**, **J** | Appendix A, Eqs. `\label{Kdef}`, `\label{Jdef}`; normalization Eq. `\label{A16}` |
| Rewriting of **J** with ε, **t**₃ and **K̄** | Appendix A, Eq. `\label{A18}`, with the footnote √2 **L**^{ijk} = ε^{ijk} |
| Sextet generators **t**₆ᵃ | Appendix A, Eq. `\label{gen6}` |
| Benchmark coupling and cutoff values | Sec. III.A, text near Figures 3, 4 and 5 |
| Tool chain (FeynRules 2.3.43 → UFO → MG5) | Sec. III, paragraph after Table X |

For reference, the paper's two model Lagrangians are:

Eq. (sFmodel), for q ∈ {u, d}:

> L ⊃ Ψ̄_q(i D̸ − m_{Ψq})Ψ_q
> + (1/Λ_{Ψq}) [ κ_q^I **J**^{s ia} ( (q̄^c_R)_{Ii} σ^{μν} Ψ_{qs} ) G_{μν a} + H.c. ]
> + (1/Λ³_{ΨqB}) [ κ_{qB}^I **J**^{s ia} ( (q̄^c_R)_{Ii} Ψ_{qs} ) B^{μν} G_{μν a} + H.c. ]

Eq. (sSmodel), for q ∈ {u, d}:

> L ⊃ (D_μΦ_q)† D^μΦ_q − m²_{Φq} Φ_q†Φ_q
> + (1/Λ²_{Φq}) [ λ_q^{XI} **J**^{s ia} Φ_{qs} ( (q̄^c_R)_{Ii} σ^{μν} ℓ_{RX} ) G_{μν a} + H.c. ]

### 1.1 The color tensor — a key identity

The reconstruction never uses **J**^{s ia}. It uses the composite tensor

> C^{a,s}_{i₁} = ε^{i₁ i₂ i₃} (T^a)_{i₂ i₄} **K̄**^s_{i₄ i₃}

together with an explicit prefactor −i in front of every interaction term.

Appendix A, Eq. (A18) of the paper states

> **J**^{s ia} = −i √2 **L**^{ijk} [**t**₃^a]_j^l **K̄**^s_{lk},   with  √2 **L**^{ijk} = ε^{ijk}.

Substituting the footnote gives **J**^{s ia} = −i ε^{ijk} [**t**₃^a]_j^l **K̄**^s_{lk}, which is
exactly (−i) × C^{a,s}_{i}. So the reconstruction's −i prefactor is **not** an extra phase
and **not** a normalization guess: the −i together with ε·T·**K̄** reproduces the paper's
**J** exactly, including the √2 factor. The paper itself recommends this route in the last
paragraph of Appendix A, because FeynRules and MadGraph already know ε and **K**, but do
not know **J**. The reconstruction and the paper therefore use the same color structure
with the same normalization.

This identity matters for the table below: wherever the reconstruction writes
"−i (κ/Λ) ε T **K̄** …", read "(κ/Λ) **J** …".

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| Ψ̄_u(i D̸ − m_{Ψu})Ψ_u — Eq. (sFmodel), line 1 | §1.1 `LPsiuFree` = i Ψ̄_u γ^μ (D_μΨ_u) − M_{Ψu} Ψ̄_u Ψ_u | **agree** | Same Dirac kinetic and mass term. D_μ uses **t**₆ᵃ (Eq. gen6) and Y = −2/3. |
| Ψ̄_d(i D̸ − m_{Ψd})Ψ_d — Eq. (sFmodel), line 1 | §1.2 `LPsidFree` | **agree** | Same, with Y = +1/3. |
| (D_μΦ_u)†D^μΦ_u − m²_{Φu}Φ_u†Φ_u — Eq. (sSmodel), line 1 | §1.3 `LPhiuFree` | **agree** | Complex scalar, sextet, Y = +1/3. |
| (D_μΦ_d)†D^μΦ_d − m²_{Φd}Φ_d†Φ_d — Eq. (sSmodel), line 1 | §1.4 `LPhidFree` | **agree** | Same, Y = +4/3. |
| Covariant derivative D_μ on a sextet, SU(2)_L singlet — implied by Table X and Eq. (sFmodel)/(sSmodel) | §0 "Covariant derivative": ∂_μ − i g_s G^a (t₆^a) − i g₁ Y B_μ | **agree** | Gluon in the sextet rep, hypercharge with Q = Y, no W± coupling. Consistent with (**6**, **1**, Y) in Table X. |
| (1/Λ_{Ψu}) κ_u^I **J**^{s ia} (ū^c_R σ^{μν} Ψ_us) G_{μν a} + H.c. — Eq. (sFmodel), line 2 | §1.5 `LPsiuG`, **multiplied by an overall factor 2** | **disagree** | Color tensor, chirality, conjugation, σ^{μν}, G^a_{μν}, flavour index and 1/Λ power all agree. The **overall factor of 2 is not in the paper**. See disagreement D1. |
| (1/Λ_{Ψd}) κ_d^I **J**^{s ia} (d̄^c_R σ^{μν} Ψ_ds) G_{μν a} + H.c. — Eq. (sFmodel), line 2 with q = d | §1.6 `LPsidG`, no factor 2 | **agree** | Exact match, including the −i·ε·T·**K̄** = **J** identity. |
| (1/Λ³_{ΨuB}) κ_{uB}^I **J**^{s ia} (ū^c_R Ψ_us) B^{μν} G_{μν a} + H.c. — Eq. (sFmodel), line 3 | §1.7 `LPsiuB` | **agree** | No σ^{μν}; the two field strengths carry the contracted Lorentz indices; 1/Λ³. Matches Table IX row 2 of the Dirac block. |
| (1/Λ³_{ΨdB}) κ_{dB}^I **J**^{s ia} (d̄^c_R Ψ_ds) B^{μν} G_{μν a} + H.c. — Eq. (sFmodel), line 3 with q = d | §1.8 `LPsidB` | **agree** | Exact mirror of the up-type term. |
| (1/Λ²_{Φu}) λ_u^{XI} **J**^{s ia} Φ_us (ū^c_R σ^{μν} ℓ_{RX}) G_{μν a} + H.c. — Eq. (sSmodel), line 2 | §1.9 `LPhiuG` | **agree** | Φ_u unconjugated with a lowered sextet index; lepton generation index first in λ^{XI} = `lamu[xx,ff]`; right-handed lepton; 1/Λ². |
| (1/Λ²_{Φd}) λ_d^{XI} **J**^{s ia} Φ_ds (d̄^c_R σ^{μν} ℓ_{RX}) G_{μν a} + H.c. — Eq. (sSmodel), line 2 with q = d | §1.10 `LPhidG` | **agree** | Exact mirror of the up-type term. |
| Chirality: every quark enters as q̄^c_R, every lepton as ℓ_{RX} — Eqs. (sFmodel), (sSmodel), Table IX | §0 and §1.11: `ProjP` → P_R everywhere; `CC[uqbar]` P_R = conjugate of the right-handed quark | **agree** | The paper's middle block of Table IV gives the same bilinear class, χ̄^c_R Γ χ'_R. |
| **J**^{s ia} — Appendix A Eq. (Jdef), rewritten in Eq. (A18) | §0: −i × ε^{i₁i₂i₃}(T^a)_{i₂i₄} **K̄**^s_{i₄i₃} | **agree** | Identical after the paper's own √2 **L** = ε footnote. See §1.1 above. |
| Φ_u ~ (**6**, **1**, 1/3), L = −1 — Table X | §2: `S[100]` Phiu, sextet, SU(2) singlet, Y = Q = +1/3, L = −1 | **agree** | |
| Φ_d ~ (**6**, **1**, 4/3), L = −1 — Table X | §2: `S[101]` Phid, Y = Q = +4/3, L = −1 | **agree** | |
| Ψ_u ~ (**6**, **1**, −2/3), L = 0 — Table X | §2: `F[100]` Psiu, Dirac, Y = Q = −2/3, lepton number not declared | **agree** | An undeclared lepton number in FeynRules means L = 0, which is the Table X value. |
| Ψ_d ~ (**6**, **1**, 1/3), L = 0 — Table X | §2: `F[101]` Psid, Dirac, Y = Q = +1/3, lepton number not declared | **agree** | |
| κ_u^I = κ_d^I = 0.05, Λ_{Ψu} = Λ_{Ψd} = 1 TeV — Sec. III.A, benchmark for Figure 3 | §3.1, §3.2: `kapu` = `kapd` = {0.05, 0.05, 0.05}, `LamPsu` = `LamPsd` = 1000 | **agree** (with a caveat) | The Figure 3 text says "∀ I ∈ {1,2}", but the Sec. III.B footnote quotes BF(Ψ_u → t̄g) ≈ 0.21, which needs a non-zero third-generation coupling. See disagreement D2. |
| κ_{uB}^I = 0.10, Λ_{uB} = 1 TeV — Sec. III.A, benchmark for Figure 4 | §3.2: `kapuB` = `kapdB` = {0.10, 0.10, 0.10}, `LamPsuB` = `LamPsdB` = 1000 | **agree** (with the same caveat) | The paper states the value only for the up-type case; the file sets the down-type one equal, which is a consistent extension. |
| λ_{u,d}^{XI} = 0.1 δ^{XI}, Λ_{Φu} = Λ_{Φd} = 1 TeV — Sec. III.A, benchmark for Figure 5 | §3.2: `lamu` = `lamd` = 0.1 δ_{xf}, `LamPhu` = `LamPhd` = 1000 | **agree** | Diagonal in generation space, so no lepton-flavour violation, as the paper states. |
| Sextet masses are scanned over in Figures 2–6; no fixed value is part of the model | §2: `MPHU` = `MPHD` = `MPSU` = `MPSD` = 1000 GeV; widths 10 GeV | **extra-in-reconstruction** | Default numbers in the implementation file. The paper fixes no mass and quotes no width. See disagreement D3. |
| — | §2: PDG codes 9000001, 9000002, 9000011, 9000012; propagator and particle-name settings | **extra-in-reconstruction** | Pure bookkeeping. The paper has no such assignment. |
| — | §3: `InteractionOrder` counting {QCD,1}, {QED,2}, {NP,1}; cutoffs at NP = −1 | **extra-in-reconstruction** | Pure MG5 bookkeeping. Harmless, but it is not paper physics. |
| — | §2: inferred baryon number B(Ψ_u) = B(Ψ_d) = B(Φ_u) = B(Φ_d) = −1/3 | **extra-in-reconstruction** | The reconstruction labels this an inference, not a declaration. Table X lists only L. The inference is self-consistent. |
| (qΨ)\|H\|²G, a dimension-7 operator — Table IX, last Dirac row | absent | **agree** | The paper lists it in the catalog but leaves it out of Eq. (sFmodel). The file leaves it out too, so the two agree. |
| (ℓ̄q)ΦG with L_{LX} H — Table IX, second scalar row | absent | **agree** | Also catalog-only; not in Eq. (sSmodel). |
| Operators of the invariant **3** ⊗ **3** ⊗ **6̄** (sextet diquarks) — Table VIII | absent | **agree** | Section III deliberately uses only the **3** ⊗ **6** ⊗ **8** invariant. |
| Scalar self-coupling, Higgs portal | absent (§1.3 states so) | **agree** | Eq. (sSmodel) contains none either. |

---

## 3. Disagreements

### D1. Overall factor of 2 in `LPsiuG` — **substantive**

The reconstruction reports that `LPsiuG` is written as `2 (...)` in the file, so every
up-type sextet-fermion chromomagnetic dipole coupling is effectively 2κ_u^f/Λ_{Ψu}, while
the down-type term `LPsidG` has no such factor. The paper defines both charge sectors by
one formula, Eq. (sFmodel) with q ∈ {u, d}, with coefficient 1/Λ_{Ψq} and no numerical
factor. Nothing in Table IX, Table X or Appendix A introduces a 2 for the up-type case.
The factor is hermitian (it multiplies the term and its H.c. together), so it does not
break hermiticity or CP; it is a pure rescaling of the coupling.

The physical effect is large. The amplitude of every vertex from this operator doubles, so
the single-production rate σ(pp → Ψ_u / Ψ̄_u) of Figure 3 and the partial width
Γ(Ψ_u → q̄g) both grow by a factor of about 4. That changes the branching fractions quoted
in the Sec. III.B footnote and moves the excluded region of Figure 6 in the
(m_{Ψu}, Λ_{Ψu}) plane.

*What a human should check:* open the `LPsiuG` definition in the implementation file and
confirm whether the leading `2` is a deliberate choice or a typing error, because the
paper's Eq. (sFmodel) has no factor of 2 and treats u and d identically.

### D2. Third-generation couplings switched on — **convention**

The paper's Figure 3 and Figure 4 benchmarks read κ_u^I = κ_d^I = 0.05 and κ_{uB}^I = 0.10
"∀ I ∈ {1,2}", that is, first and second generation only. The file sets all three
generations to the same value. The paper's own Sec. III.B footnote, however, quotes
BF(Ψ_u → t̄g) ≈ 0.21 and BF(Ψ_u → t̄gA) ≈ 0.001, which require a non-zero third-generation
coupling. The file therefore agrees with the branching-fraction discussion and reads as a
superset of the figure text.

*What a human should check:* decide which benchmark the file is meant to reproduce, since a
non-zero κ^3 changes the total width of Ψ_u and hence every branching fraction used for the
Figure 6 limits.

### D3. Fixed 1 TeV masses and 10 GeV widths — **cosmetic**

The paper scans the sextet mass in Figures 2–6 and never fixes it, and never quotes a
width. The file hard-codes 1000 GeV masses and 10 GeV widths. These are ordinary FeynRules
default values that a user overrides in the param card, and MG5 normally recomputes the
width, so this is not a physics claim of the paper.

*What a human should check:* confirm that the analysis scripts override these defaults
rather than using the hard-coded width, especially the 10 GeV value, which is not derived
from the couplings.

### D4. Down-type `kapdB` value not stated in the paper — **cosmetic**

The paper gives κ_{uB}^I = 0.10 for the up-type case only, because Figure 4 shows the
up-type channel. The file sets `kapdB` = 0.10 as well. This is a natural symmetric choice,
but it is a choice, not a quoted paper number.

*What a human should check:* nothing, unless a down-type Ψ_d + γ/Z rate is ever compared
with a paper number.

---

## 4. Overall assessment

The reconstruction describes the same model that Section III of the paper defines. All four
new fields match Table X in spin, color representation, weak representation, hypercharge,
electric charge and lepton number. All six interaction terms match Eqs. (sFmodel) and
(sSmodel) in operator dimension, cutoff power, chirality, charge conjugation, Dirac
structure, field-strength content and flavour-index ordering. The one point that could look
like an error — the explicit −i in front of every interaction term, combined with the
ε·T·**K̄** tensor instead of the paper's **J**^{s ia} — is in fact exactly right: Appendix A,
Eq. (A18) gives **J**^{s ia} = −i√2 **L**^{ijk}[**t**₃^a]_j^l **K̄**^s_{lk} with √2 **L** = ε,
so the file reproduces **J** with the correct normalization, by the very route the paper
recommends in its closing paragraph. The benchmark parameter values also line up with
Section III.A. The single item that does not follow from the paper is the overall factor of
2 on the up-type fermion chromomagnetic dipole term `LPsiuG`: the paper writes one formula
for q ∈ {u, d} with no numerical factor, and the file's own down-type mirror `LPsidG`
carries no such factor, so the up- and down-type sectors are asymmetric in the file and
symmetric in the paper. That factor changes the up-type single-production rate and the
Ψ_u → q̄g width by about a factor of 4, which feeds directly into the Figure 3 cross
sections, the quoted branching fractions and the Figure 6 dijet limits, so it is the item
that deserves the reviewer's attention. The remaining differences — third-generation
couplings switched on, fixed 1 TeV masses, 10 GeV widths, PDG codes and interaction-order
bookkeeping — are implementation defaults that the paper simply does not specify.
