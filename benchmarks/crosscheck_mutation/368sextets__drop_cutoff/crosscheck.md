# Cross-check: `reconstruction.md` against "The phenomenological cornucopia of SU(3) exotica"

**Paper.** L. M. Carpenter, T. Murphy, T. M. P. Tait, preprint UCI-HEP-TR-2021-26.
**Reconstruction.** Independent read of an implementation file (`sanitized.fr`). The implementation
file was not available for this check.

---

## 1. Where the paper defines the model

The paper has two parts. Section II is a general operator catalog. Section III defines the
concrete model. Only Section III is the model to compare against.

| Location in `paper.tex` | Content |
|---|---|
| Sec. III, eq. `\label{sFmodel}` (line 857) | Sextet **fermion** Lagrangian, for $q\in\{u,d\}$: kinetic + mass, the $\sigma^{\mu\nu}G$ dipole with prefactor $1/\Lambda_{\Psi_q}$, and the $B^{\mu\nu}G_{\mu\nu a}$ operator with prefactor $1/\Lambda^3_{\Psi_qB}$ |
| Sec. III, eq. `\label{sSmodel}` (line 861) | Sextet **scalar** Lagrangian: kinetic + mass, and the leptoquark dipole with prefactor $1/\Lambda^2_{\Phi_q}$ |
| Table X, `\label{fields}` (line 1142) | Quantum numbers: $\Phi_u(\boldsymbol{6},\boldsymbol{1},\tfrac13)$, $\Phi_d(\boldsymbol{6},\boldsymbol{1},\tfrac43)$, both $L=-1$; $\Psi_u(\boldsymbol{6},\boldsymbol{1},-\tfrac23)$, $\Psi_d(\boldsymbol{6},\boldsymbol{1},\tfrac13)$, both $L=0$ |
| Table IX, `\label{t9}` (line 820) | The parent operator list for the invariant $\boldsymbol{3}\otimes\boldsymbol{6}\otimes\boldsymbol{8}$, with the cutoff power of each operator stated in the "Coupling" column |
| App. A, eq. `\label{Jdef}` (line 1386) | Explicit values of the Clebsch-Gordan coefficients $\bt{J}^{\,s\,ia}$ |
| App. A, eq. `\label{A18}` (line 1421) | $\bt{J}^{\,s\,ia} = -\ii\sqrt{2}\,\bt{L}^{ijk}[\bt{t}^a_{\boldsymbol{3}}]_j^{\ l}\bar{\bt{K}}{}^s_{\ lk}$, with $\sqrt{2}\,\bt{L}^{ijk}=\epsilon^{ijk}$. The paper states that this identity is the way to build the model in FeynRules, because FeynRules has no native $\bt{J}$. |

Note on references: the labels in this `.tex` sit after `\begin{table*}` / `\begin{multline}`, so
printed numbers are not recoverable from the source. This document cites labels and line numbers.

Benchmark values, from Sec. III.A (lines 1184, 1191, 1197): $\kappa_u^I=\kappa_d^I=0.05$,
$\kappa_{uB}^I=0.10$, $\lambda^{XI}_{u,d}=0.1\,\delta^{XI}$, and every cutoff $=1\,\mathrm{TeV}$.

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Colour structure $\bt{J}^{\,s\,ia}$ (App. A, `Jdef`), built as $-\ii\,\epsilon^{ijk}[\bt{t}^a_{\boldsymbol 3}]_j^{\ l}\bar{\bt{K}}{}^s_{\ lk}$ (App. A, `A18`) | $-i\,\mathcal{C}^{a,s}_{\,i}=-i\,\varepsilon_{i_1i_2i_3}T^a_{i_2i_4}(\bar K^s)_{i_4i_3}$, §0 and §1 | **agree** | Index chain and the factor $-i$ match `A18` exactly. The $-i$ is part of $\bt{J}$, not an extra phase. The reconstruction reads $\bar K$ and $\varepsilon$ as undefined externals (§5.2); the paper confirms they come from the FeynRules sextet machinery. |
| $\bar\Psi_q(\ii\slashed{D}-m_{\Psi_q})\Psi_q$, $q=u$ (`sFmodel`, line 1 of the multline) | `LPsiuFree`: $i\bar\Psi_u\gamma^\mu(D_\mu\Psi_u)-M_{\Psi_u}\bar\Psi_u\Psi_u$, $Y=-\tfrac23$ | **agree** | Dirac field, colour $\boldsymbol 6$, weak singlet, $Y=-\tfrac23$. Matches Table X. |
| Same, $q=d$ (`sFmodel`) | `LPsidFree`, $Y=+\tfrac13$ | **agree** | Matches Table X. |
| $(D_\mu\Phi_q)^\dagger D^\mu\Phi_q-m^2_{\Phi_q}\Phi^\dagger_q\Phi_q$, $q=u$ (`sSmodel`, line 1) | `LPhiuFree`, $Y=+\tfrac13$ | **agree** | Matches Table X. No potential beyond the mass term, in the paper and in the file. |
| Same, $q=d$ (`sSmodel`) | `LPhidFree`, $Y=+\tfrac43$ | **agree** | Matches Table X. |
| $\dfrac{1}{\Lambda_{\Psi_u}}[\kappa_u^I\,\bt{J}^{\,s\,ia}(\overbar{u^{\rm c}_{\rm R}}_{Ii}\sigma^{\mu\nu}\Psi_{us})G_{\mu\nu a}+\text{H.c.}]$ (`sFmodel`, line 2; Table IX row "$(q\Psi)G$", coupling $\kappa_I/\Lambda_\Psi$) | `LPsiuG`: $-i\,\kappa^u_f\,\mathcal{C}^{a,s}_{i_1}\overline{u^{\rm c}_{f,i_1}}P_R\sigma^{\mu\nu}\Psi_{u,s}G^a_{\mu\nu}+\text{h.c.}$, **with no $1/\Lambda_{\Psi_u}$** | **disagree** | Field content, chirality, colour tensor and Lorentz structure all agree. The cutoff $1/\Lambda_{\Psi_u}$ that the paper requires is absent. The reconstruction reports this itself in §5.1 and says `LamPsu` is declared but used nowhere. See D1. |
| $\dfrac{1}{\Lambda_{\Psi_d}}[\kappa_d^I\,\bt{J}^{\,s\,ia}(\overbar{d^{\rm c}_{\rm R}}_{Ii}\sigma^{\mu\nu}\Psi_{ds})G_{\mu\nu a}+\text{H.c.}]$ (`sFmodel`, line 2) | `LPsidG`: same structure, **with** $\kappa^d_f/\Lambda_{\Psi_d}$ | **agree** | This is the correct partner of the term above, and it shows the intended form. |
| $\dfrac{1}{\Lambda^3_{\Psi_uB}}[\kappa_{uB}^I\,\bt{J}^{\,s\,ia}(\overbar{u^{\rm c}_{\rm R}}_{Ii}\Psi_{us})B^{\mu\nu}G_{\mu\nu a}+\text{H.c.}]$ (`sFmodel`, line 3; Table IX, coupling $\kappa_I/\Lambda^3_\Psi$) | `LPsiuB`: $-i\,(\kappa^{uB}_f/\Lambda^3_{\Psi_uB})\,\mathcal{C}\,\overline{u^{\rm c}}P_R\Psi_u\,B_{\mu\nu}G^{a\mu\nu}+\text{h.c.}$ | **agree** | No $\sigma^{\mu\nu}$, scalar fermion bilinear, two field strengths contracted together, cutoff power 3. All match. Mass dimension 7, as the paper states. |
| $\dfrac{1}{\Lambda^3_{\Psi_dB}}[\kappa_{dB}^I\,\ldots]$ (`sFmodel`, line 3) | `LPsidB` | **agree** | Same as above for the down sector. |
| $\dfrac{1}{\Lambda^2_{\Phi_u}}[\lambda^{XI}_u\,\bt{J}^{\,s\,ia}\Phi_{us}(\overbar{u^{\rm c}_{\rm R}}_{Ii}\sigma^{\mu\nu}\ell_{{\rm R}X})G_{\mu\nu a}+\text{H.c.}]$ (`sSmodel`, line 2; Table IX row "$(q\ell)\Phi G$", coupling $\lambda^X_I/\Lambda^2_\Phi$) | `LPhiuG`: $-i\,(\lambda^u_{xf}/\Lambda^2_{\Phi_u})\,\mathcal{C}\,\Phi_{u,s}\,\overline{u^{\rm c}_{f}}\sigma^{\mu\nu}P_R\ell_x\,G^a_{\mu\nu}+\text{h.c.}$ | **agree** | Cutoff power 2. Index order $\lambda^{XI}$ (lepton first, quark second) matches `lamu[xx,ff]`. One $P_R$ fixes both the quark and the lepton to be right-handed, because $[\sigma^{\mu\nu},\gamma_5]=0$. This reproduces the paper's $(\overbar{q^{\rm c}_{\rm R}}\ldots\ell_{{\rm R}X})$. |
| $\dfrac{1}{\Lambda^2_{\Phi_d}}[\lambda^{XI}_d\,\ldots]$ (`sSmodel`, line 2) | `LPhidG` | **agree** | Same as above for the down sector. |
| Lepton number: $L(\Phi_{u,d})=-1$, $L(\Psi_{u,d})=0$ (Table X, `fields`) | §2 field table: $L(\Phi)=-1$, $L(\Psi)$ not declared, read as 0 | **agree** | Values match. The reconstruction notes $L$ is not declared for $\Psi$; 0 is the FeynRules default and is the paper's value. |
| Weak representation: all four states are $\mathrm{SU}(2)_{\rm L}$ singlets (Table X, and eq. `sextet_numbers`, line 750) | §0 and §2: no `Index[SU2W]`, so $Q=Y$ | **agree** | Consistent. $D_\mu$ then holds only the gluon and $B$ terms, as the reconstruction states. |
| Benchmark $\kappa_u^I=\kappa_d^I=0.05$, $\Lambda_{\Psi_u}=\Lambda_{\Psi_d}=1\,$TeV (Sec. III.A, line 1184) | `kapu`, `kapd` $=0.05$ for all three generations; all $\Lambda=1000$ GeV | **agree** | The paper text writes $\forall\,I\in\{1,2\}$, but its own branching fractions need a third-generation coupling. See D3. |
| Benchmark $\kappa_{uB}^I=0.10$, $\Lambda_{uB}=1\,$TeV (Sec. III.A, line 1191) | `kapuB`, `kapdB` $=0.10$; $\Lambda=1000$ GeV | **agree** | |
| Benchmark $\lambda^{XI}_{u,d}=0.1\times\delta^{XI}$, $\Lambda_{\Phi_u}=\Lambda_{\Phi_d}=1\,$TeV (Sec. III.A, line 1197) | `lamu`, `lamd` diagonal $0.1$, off-diagonal 0; $\Lambda=1000$ GeV | **agree** | Flavour-diagonal, so no lepton-flavour violation. Matches the paper. |
| Sextet masses: the paper scans $m_\Psi$, $m_\Phi$ (Figs. 2–6) | `MPHU`, `MPHD`, `MPSU`, `MPSD` $=1000$ GeV | **agree** | A default inside the scan range. The paper does not fix one mass. |
| Widths: the paper computes branching fractions, e.g. ${\rm BF}(\Psi_u\to\bar u g)\approx0.26$ (Sec. III.B, line 1211) | `WPHU`, `WPHD`, `WPSU`, `WPSD` $=10$ GeV, fixed | **extra-in-reconstruction** | The paper needs computed widths. A fixed 10 GeV is a placeholder value. See D2. |
| PDG codes | 9000001, 9000002, 9000011, 9000012 | **extra-in-reconstruction** | Bookkeeping only. The paper says nothing about PDG codes. |
| Baryon number | Not declared; the reconstruction infers $B=-\tfrac13$ for all four states | **extra-in-reconstruction** | The paper does not assign $B$ either. The inference is sound and harmless. |
| Table IX also lists $(\overbar{q^{\rm c}_{\rm R}}\sigma^{\mu\nu}\Psi_s)|H|^2G$ and $(\bar L_{{\rm L}X}H\sigma^{\mu\nu}q_{{\rm R}I})\Phi_s G$ | Absent | **agree** (not a defect) | The paper's Sec. III says the model takes the Table IX operators "with light modification". Eqs. `sFmodel` and `sSmodel` do not contain these two. Their absence is correct. |

---

## 3. Disagreements

**D1. `LPsiuG` has no $1/\Lambda_{\Psi_u}$. Severity: substantive.**
The paper's eq. `sFmodel` puts $1/\Lambda_{\Psi_q}$ in front of the dipole operator for **both**
$q=u$ and $q=d$, and Table IX gives the coupling as $\kappa_I/\Lambda_\Psi$. The reconstruction
reports the factor present for $d$ and absent for $u$. Three consequences follow.

* The term has mass dimension 5, not 4. The Lagrangian is not dimensionally homogeneous.
* The $u$ vertex is too large by one power of $\Lambda_{\Psi_u}$. At the paper's benchmark
  $\Lambda_{\Psi_u}=1000$ GeV, any rate driven by this vertex is wrong by about $10^6$.
* The vertex carries NP order 1 instead of NP order 2. A MadGraph run with an `NP` coupling-order
  cut would then treat the $u$ and $d$ sectors differently.

*What a human should check:* open the implementation file at the `LPsiuG` definition and confirm
whether `/LamPsu` is really missing; then confirm whether this file is the one that produced
Figures 3, 4 and 6, because Figure 6 is a limit plot in the $(m_{\Psi_u},\Lambda_{\Psi_u})$ plane
and depends on exactly this factor.

**D2. Fixed 10 GeV widths. Severity: convention.**
The paper quotes branching fractions for $\Psi_u$ (line 1211 and its footnote) and applies a
branching fraction of about 0.26 to the dijet limit. Those numbers need widths computed from the
model, not a hard-coded 10 GeV.

*What a human should check:* confirm that the run cards set the widths to `auto`, or that the
widths were computed with `compute_widths`, so that the placeholder value never reaches a result.

**D3. Third-generation $\kappa$ set to 0.05. Severity: cosmetic.**
The paper's text says $\kappa_u^I=\kappa_d^I=0.05\ \forall\,I\in\{1,2\}$, which names only the
first two generations. The reconstruction has 0.05 for all three. The paper's own footnote quotes
${\rm BF}(\Psi_u\to\bar t g)\approx0.21$, which needs a non-zero third-generation coupling. The
file therefore agrees with the paper's numbers, and the paper's text is the imprecise side.

*What a human should check:* confirm which generations were switched on in the run cards that
produced the branching fractions on line 1211.

**D4. Projector position differs between term groups. Severity: cosmetic.**
`LPsiuG` and `LPsidG` place $P_R$ to the left of $\sigma^{\mu\nu}$; `LPhiuG` and `LPhidG` place it
to the right. The reconstruction states in §5.3 that the two orders are equal because
$[\sigma^{\mu\nu},\gamma_5]=0$. This is correct, and both orders reproduce the paper's
$\overbar{q^{\rm c}_{\rm R}}$ and $\ell_{{\rm R}X}$.

*What a human should check:* nothing beyond a quick look, unless a FeynRules or UFO convention
changes the sign of a single term.

---

## 4. Overall assessment

The reconstruction and the paper describe the same model. The field content matches Table X state
by state: four colour sextets, all weak singlets, with hypercharges $\tfrac13$, $\tfrac43$,
$-\tfrac23$ and $\tfrac13$, lepton number $-1$ for the scalars and 0 for the fermions. The colour
tensor $-i\,\varepsilon\,T\,\bar K$ in the reconstruction is the paper's $\bt{J}^{\,s\,ia}$, built
by the exact identity the paper gives in Appendix A eq. `A18` for use inside FeynRules, including
the factor $-i$. Nine of the ten Lagrangian terms match the paper in field content, chirality,
conjugation, Lorentz structure and cutoff power, and all six benchmark couplings match the values
in Section III.A. The reconstruction also adds no operator that the paper does not define. The one
substantive difference is D1: the up-type fermion dipole operator carries no $1/\Lambda_{\Psi_u}$,
although the paper's eq. `sFmodel` and Table IX both require it and although the down-type partner
term does carry its own cutoff. The reconstruction found and reported this itself, which raises
confidence in the rest of its reading, but it cannot tell whether the factor is truly absent from
the implementation or was lost somewhere between the file and this document. That question, and
the question of whether the affected figures used this file, need a human with the implementation
file in hand. The remaining differences are placeholders and bookkeeping and carry no physics.
