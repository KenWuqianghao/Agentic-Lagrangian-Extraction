# Cross-check: `reconstruction.md` against the paper

RUN-TAG: XM-CROSS-368sextets__drop_term

Paper: *The phenomenological cornucopia of SU(3) exotica* — Carpenter, Murphy, Tait (UCI-HEP-TR-2021-26).

## 1. Where the paper defines the model

The reconstruction describes the simplified models of **Section III** ("Sextets at the LHC"), not
the full operator catalog of Section II. The relevant sources in `paper.tex` are:

| Item | Paper location |
|---|---|
| Sextet **fermion** model (kinetic + mass, dim-5 $qG$ operator, dim-7 $qBG$ operator) | Eq. `\eqref{sFmodel}`, lines 857–859 |
| Sextet **scalar** model (kinetic + mass, dim-6 $q\ell G$ leptoquark operator) | Eq. `\eqref{sSmodel}`, lines 861–863 |
| Field content and quantum numbers ($\mathcal{G}_{\rm SM}$, $L$) | Table X (`\label{fields}`), lines 1142–1162 |
| Parent operator list for the invariant $\boldsymbol{3}\otimes\boldsymbol{6}\otimes\boldsymbol{8}$ | Table IX (`\label{t9}`), lines 820–843 |
| Clebsch-Gordan coefficients $\bt{J}^{\,s\,ia}$, explicit matrices | Eq. `\eqref{Jdef}`, lines 1386–1410 |
| $\bt{J}$ written with $\varepsilon$, $\bt{t}_3^a$ and $\bar{\bt{K}}$ (the form used for FeynRules) | Eq. `\eqref{A18}`, lines 1421–1424 |
| $\bt{K}_s^{\ ij}$ matrices | Eq. `\eqref{Kdef}`, lines 1366–1383 |
| Benchmark couplings, cutoffs and generation ranges | Sec. III.A text, lines 1184, 1191, 1197 |

The two model equations are, in the paper's notation, for $q \in \{u,d\}$:

$$
\mathcal{L} \supset \bar\Psi_q(\mathrm{i}\slashed{D}-m_{\Psi_q})\Psi_q
+\frac{1}{\Lambda_{\Psi_q}}\big[\kappa_q^I\,\bt{J}^{\,s\,ia}(\overline{q^{\rm c}_{\rm R}}_{Ii}\,\sigma^{\mu\nu}\Psi_{qs})G_{\mu\nu\,a}+\text{H.c.}\big]
+\frac{1}{\Lambda^3_{\Psi_{qB}}}\big[\kappa_{qB}^I\,\bt{J}^{\,s\,ia}(\overline{q^{\rm c}_{\rm R}}_{Ii}\,\Psi_{qs})B^{\mu\nu}G_{\mu\nu\,a}+\text{H.c.}\big]
$$

$$
\mathcal{L} \supset (D_\mu\Phi_q)^\dagger D^\mu\Phi_q-m^2_{\Phi_q}\Phi_q^\dagger\Phi_q
+\frac{1}{\Lambda^2_{\Phi_q}}\big[\lambda_q^{XI}\,\bt{J}^{\,s\,ia}\,\Phi_{qs}(\overline{q^{\rm c}_{\rm R}}_{Ii}\,\sigma^{\mu\nu}\ell_{{\rm R}X})G_{\mu\nu\,a}+\text{H.c.}\big]
$$

**Colour tensor.** Eq. `\eqref{A18}` gives $\bt{J}^{\,s\,ia}=-\mathrm{i}\sqrt{2}\,\bt{L}^{ijk}[\bt{t}^a_3]_j^{\ l}\bar{\bt{K}}{}^s_{\ lk}$,
and the footnote there gives $\sqrt{2}\,\bt{L}^{ijk}=\epsilon^{ijk}$. Therefore

$$
\bt{J}^{\,s\,ia}=-\mathrm{i}\,\epsilon^{ijk}\,[\bt{t}^a_3]_j^{\ l}\,\bar{\bt{K}}{}^s_{\ lk}.
$$

This is exactly the tensor the reconstruction writes, including the explicit factor $-\mathrm{i}$ that it
carries in front of every interaction term. The two forms are the same object, not merely proportional.

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| $\bar\Psi_u(\mathrm{i}\slashed D-m_{\Psi_u})\Psi_u$, Eq. `sFmodel` line 1 with $q=u$; $\Psi_u\sim(\boldsymbol6,\boldsymbol1,-\tfrac23)$, Table X | `LPsiuFree`: $\mathrm{i}\bar\Psi_u\gamma^\mu D_\mu\Psi_u-M_{\Psi_u}\bar\Psi_u\Psi_u$, $Y=-\tfrac23$ | **agree** | Sextet colour, $SU(2)_{\rm L}$ singlet, Dirac, $Y=-2/3$: all match Table X. $D_\mu$ expansion (gluon in $T_6$, no $W^\pm$) follows from the representation. |
| $\bar\Psi_d(\mathrm{i}\slashed D-m_{\Psi_d})\Psi_d$, Eq. `sFmodel` with $q=d$; $\Psi_d\sim(\boldsymbol6,\boldsymbol1,\tfrac13)$, Table X | `LPsidFree`, $Y=+\tfrac13$ | **agree** | Same as above. |
| $(D_\mu\Phi_u)^\dagger D^\mu\Phi_u-m^2_{\Phi_u}\Phi_u^\dagger\Phi_u$, Eq. `sSmodel` with $q=u$; $\Phi_u\sim(\boldsymbol6,\boldsymbol1,\tfrac13)$, $L=-1$, Table X | `LPhiuFree`, $Y=+\tfrac13$, $L=-1$ | **agree** | Complex scalar sextet, no quartic and no Higgs portal in either. |
| $(D_\mu\Phi_d)^\dagger D^\mu\Phi_d-m^2_{\Phi_d}\Phi_d^\dagger\Phi_d$, Eq. `sSmodel` with $q=d$; $\Phi_d\sim(\boldsymbol6,\boldsymbol1,\tfrac43)$, $L=-1$, Table X | `LPhidFree`, $Y=+\tfrac43$, $L=-1$ | **agree** | |
| $\frac{\kappa_u^I}{\Lambda_{\Psi_u}}\bt{J}^{\,s\,ia}(\overline{u^{\rm c}_{\rm R}}_{Ii}\sigma^{\mu\nu}\Psi_{us})G_{\mu\nu a}+$ H.c., Eq. `sFmodel` line 2; Table IX row 3 | `LPsiuG`: $-\mathrm{i}\frac{\kappa^u_f}{\Lambda_{\Psi_u}}\epsilon_{ijk}(T^a)_{jl}\bar K^s_{lk}\,\overline{u^{\rm c}_f}P_R\sigma^{\mu\nu}\Psi_u G^a_{\mu\nu}+$ h.c. | **agree** | Colour tensor equals $\bt{J}^{\,s\,ia}$ including the $-\mathrm{i}$ and the $\sqrt2$ (Eq. `A18`). Chirality matches: $\overline{u^{\rm c}}P_R=\overline{(u_{\rm R})^{\rm c}}$, which is the paper's $\overline{q^{\rm c}_{\rm R}}$. Dimension 5, one power of $\Lambda$. One quark generation index. |
| $\frac{\kappa_d^I}{\Lambda_{\Psi_d}}\bt{J}^{\,s\,ia}(\overline{d^{\rm c}_{\rm R}}_{Ii}\sigma^{\mu\nu}\Psi_{ds})G_{\mu\nu a}+$ H.c., Eq. `sFmodel` line 2 with $q=d$ | `LPsidG` | **agree** | Identical structure in the down sector. |
| $\frac{\kappa_{uB}^I}{\Lambda^3_{\Psi_{uB}}}\bt{J}^{\,s\,ia}(\overline{u^{\rm c}_{\rm R}}_{Ii}\Psi_{us})B^{\mu\nu}G_{\mu\nu a}+$ H.c., Eq. `sFmodel` line 3; Table IX row 4 | `LPsiuB`: $-\mathrm{i}\frac{\kappa^{Bu}_f}{\Lambda^3_{\Psi_uB}}\,\epsilon(T^a)\bar K\,\overline{u^{\rm c}_f}P_R\Psi_u\,B_{\mu\nu}G^{a\mu\nu}+$ h.c. | **agree** | No $\sigma^{\mu\nu}$ in the bilinear; the two Lorentz indices sit on the two field strengths. Dimension 7, $1/\Lambda^3$. A separate cutoff symbol from the dim-5 one, as in the paper. See disagreement D2 for the reconstruction's chirality remark. |
| $\frac{\kappa_{dB}^I}{\Lambda^3_{\Psi_{dB}}}\bt{J}^{\,s\,ia}(\overline{d^{\rm c}_{\rm R}}_{Ii}\Psi_{ds})B^{\mu\nu}G_{\mu\nu a}+$ H.c., Eq. `sFmodel` line 3 with $q=d$ | `LPsidB` | **agree** | |
| $\frac{\lambda_u^{XI}}{\Lambda^2_{\Phi_u}}\bt{J}^{\,s\,ia}\Phi_{us}(\overline{u^{\rm c}_{\rm R}}_{Ii}\sigma^{\mu\nu}\ell_{{\rm R}X})G_{\mu\nu a}+$ H.c., Eq. `sSmodel` line 2 with $q=u$; Table IX row 1 | `LPhiuG`: $-\mathrm{i}\frac{\lambda^u_{xf}}{\Lambda^2_{\Phi_u}}\epsilon(T^a)\bar K\,\Phi_u\,\overline{u^{\rm c}_f}\sigma^{\mu\nu}P_R\ell_x G^a_{\mu\nu}+$ h.c. | **agree** | $\Phi_u$ enters unconjugated, index down, as in the paper. Two generation indices, lepton first. Dimension 6, $1/\Lambda^2$. Projector position relative to $\sigma^{\mu\nu}$ is immaterial, as the reconstruction states. |
| $\frac{\lambda_d^{XI}}{\Lambda^2_{\Phi_d}}\bt{J}^{\,s\,ia}\Phi_{ds}(\overline{d^{\rm c}_{\rm R}}_{Ii}\sigma^{\mu\nu}\ell_{{\rm R}X})G_{\mu\nu a}+$ H.c., Eq. `sSmodel` line 2 with $q=d$ (the equation is stated "for $q\in\{u,d\}$"; $\Lambda_{\Phi_d}$ and $\lambda_d^{XI}$ are used in the benchmark at line 1197 and in Fig. 5) | **absent** — `LTotal` has no `LPhidG`; `lamd` and `LamPhd` are declared but unused | **missing-in-reconstruction** | This is the one term of the Section III model that the reconstruction does not carry. See D1. |
| $\Psi_u,\Psi_d$ carry $L=0$; $\Phi_u,\Phi_d$ carry $L=-1$ (Table X) | Field table: $L=-1$ for both scalars; $L$ "not declared" for the fermions | **agree** | Values match. The fermion $L=0$ is implicit in the file rather than declared. |
| Benchmark: $\kappa_u^I=\kappa_d^I=0.05$, $\kappa_{uB}^I=0.10$ for $I\in\{1,2\}$; $\lambda^{XI}_{u,d}=0.1\,\delta^{XI}$; all $\Lambda=1$ TeV (lines 1184, 1191, 1197) | Same numbers, but $\kappa$ set for $f=1,2,3$; $\lambda=0.1\,\delta_{xf}$; all $\Lambda=1000$ GeV | **agree** (with a caveat) | Structure and values match. The generation range differs; see D3. |
| Sextet masses scanned over a range in Figs. 2–6; no fixed value in the Lagrangian | `MPHU`=`MPHD`=`MPSU`=`MPSD`=1000 GeV, widths 10 GeV | **agree** (defaults only) | Numerical defaults of an implementation file, not model content. See D4. |
| Table IX also lists $(q\Psi)|H|^2G$ (dim 7) and $(\bar L_{\rm L}H\sigma^{\mu\nu}q_{\rm R})\Phi G$ (dim 7) | absent | — | Not a defect. Eqs. `sFmodel` and `sSmodel` deliberately keep only a subset of Table IX ("taken with light modification from Table IX", line 864). The reconstruction matches that subset. |
| — | PDG codes 9000001/9000002/9000011/9000012, propagator types, `InteractionOrder` and `NP` counting | — | Implementation bookkeeping. The paper states no values for these, so they cannot be checked against it. |

## 3. Disagreements

**D1. The $\Phi_d$ leptoquark operator is missing.**
Severity: **substantive**.
Eq. `\eqref{sSmodel}` defines the scalar model for both $q=u$ and $q=d$, and Sec. III.A uses
$\lambda^{XI}_{u,d}$ and $\Lambda_{\Phi_d}=1$ TeV in the benchmark for Fig. 5 (line 1197). The
reconstruction reports no `LPhidG` in `LTotal` and two unused parameters, `lamd` and `LamPhd`. With
the term absent, $\Phi_d$ has only gauge interactions, it does not decay, and the $\Phi_d+\ell$
production and $\bar d\,\ell\,g$ signature of Fig. 5 cannot be generated.
What a human should check: open the implementation file and confirm whether `LPhidG` truly does not
exist (and is not added to `LTotal` under another name), because the reconstruction had no access to
a second opinion; if it is truly absent, decide whether the file, and any result produced with it,
covers the down-type scalar at all.

**D2. Chirality gloss on the dimension-7 operator is wrong.**
Severity: **cosmetic** (commentary only; the written term is correct).
Section 1.3 of the reconstruction says the scalar bilinear $\overline{u^{\rm c}}P_R\Psi_u$ "pairs the
right-handed quark with the left-handed component of $\Psi_u$", and calls the $\sigma^{\mu\nu}$
operators "chirality preserving" by contrast. Both statements are incorrect: $P_R$ stands to the left
of $\Psi_u$ in the reconstruction's own formula, so it selects $\Psi_{u{\rm R}}$, and the scalar and
tensor bilinears have the *same* chirality structure, $\overline{(u_{\rm R})^{\rm c}}\,\Psi_{u{\rm R}}$.
The term itself, and the paper's $(\overline{q^{\rm c}_{\rm R}}\Psi_s)$, agree.
What a human should check: ignore the prose and confirm the projector placement in the source line for
`LPsiuB`/`LPsidB`; the derived Feynman rules should show the same quark chirality as `LPsiuG`.

**D3. Generation range of the default $\kappa$ values.**
Severity: **convention**.
The paper's benchmark sets $\kappa_q^I$ and $\kappa_{qB}^I$ for $I\in\{1,2\}$ only (lines 1184, 1191).
The reconstruction reports the same values for all three generations. The paper is not fully
self-consistent here either: the footnote at line 1211 quotes ${\rm BF}(\Psi_u\to\bar t\,g)\approx0.21$,
which needs a non-zero third-generation coupling.
What a human should check: decide which benchmark the param card is meant to reproduce, because the
branching fractions used for the dijet limits in Fig. 6 depend on it.

**D4. Fixed masses and widths.**
Severity: **convention**.
The file fixes all four masses to 1000 GeV and all widths to 10 GeV. The paper treats the sextet mass
as a free parameter and computes the width from the couplings.
What a human should check: confirm the width is recomputed (for example by MadGraph `--auto_widths`)
before any cross-section or branching-fraction number is quoted, since a hard-coded 10 GeV width is
not consistent with the couplings.

**D5. Fermion lepton number and baryon number are not declared.**
Severity: **cosmetic**.
Table X assigns $L=0$ to $\Psi_u,\Psi_d$; the file leaves $L$ undeclared for them, and the
reconstruction infers $B=-1/3$ for all four states, which the paper does not state.
What a human should check: whether the undeclared quantum numbers matter for the intended MadGraph
runs (they normally do not, but they remove a useful consistency check).

## 4. Overall assessment

The reconstruction tracks the paper's Section III simplified models closely. All four new states carry
the colour, weak and hypercharge assignments of Table X, and the lepton numbers match. The four
fermionic operators reproduce Eq. `\eqref{sFmodel}` term for term, and the surviving scalar operator
reproduces the $q=u$ half of Eq. `\eqref{sSmodel}`. The colour structure is the strongest point of
agreement: the tensor $-\mathrm{i}\,\epsilon_{ijk}(T^a)_{jl}\bar K^s_{lk}$ used in every interaction is
not merely proportional to the paper's $\bt{J}^{\,s\,ia}$ but equal to it, including the factor
$-\mathrm{i}\sqrt2$ of Eq. `\eqref{A18}` after $\sqrt2\,\bt{L}^{ijk}=\epsilon^{ijk}$ is inserted. This
is also the construction the paper says it used for FeynRules, which makes the match meaningful rather
than accidental. The operator dimensions and their cutoff powers ($1/\Lambda$, $1/\Lambda^2$,
$1/\Lambda^3$), the separate $B_{\mu\nu}G^{\mu\nu}$ cutoff, the charge-conjugate right-handed quark in
every bilinear, and the generation-index structure of $\kappa$ and $\lambda$ all agree. One term of the
model is not present: the down-type scalar leptoquark operator, whose two parameters are declared but
unused. That single gap is the only substantive difference; the remaining items are numerical defaults,
undeclared quantum numbers, and one incorrect sentence of commentary that does not affect the terms as
written. The decision on whether this reconstruction is acceptable belongs to the human reviewer.
