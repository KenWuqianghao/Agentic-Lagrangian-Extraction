# Crosscheck: `reconstruction.md` against the color-sextet paper

Paper: "The phenomenological cornucopia of SU(3) exotica", Carpenter, Murphy and Tait
(preprint UCI-HEP-TR-2021-26).

## 0. Where the paper defines the model

The paper has two parts. Section II builds a general operator catalog. Section III defines one
concrete simplified model and studies it at the LHC. The reconstruction describes an
implementation file. That file can only match the Section III model. I therefore use Section III
as the reference, and I use the catalog tables only as context.

The load-bearing places in the paper are:

| Item | Where |
| --- | --- |
| Sextet fermion model Lagrangian | Eq. `(sFmodel)`, Sec. III (three lines: kinetic + mass, dipole, $B\!\cdot\!G$) |
| Sextet scalar model Lagrangian | Eq. `(sSmodel)`, Sec. III (two lines: kinetic + mass, leptoquark) |
| Field content and quantum numbers | Table X ("Exotic field content"), Sec. III |
| Operator origin of both models | Table IX, invariant $\boldsymbol{3}\otimes\boldsymbol{6}\otimes\boldsymbol{8}$ |
| Sextet Clebsch-Gordan $\bt{K}$ | Eq. `(Kdef)`, Appendix A; normalisation eq. `(A16)` |
| New Clebsch-Gordan $\bt{J}$ | Eq. `(Jdef)`, Appendix A |
| $\bt{J}$ written with $\bt{K}$, $\bt{L}$ and $t^a_{\boldsymbol 3}$ | Eq. `(A18)` and its footnote, Appendix A |
| Sextet generators $t^a_{\boldsymbol 6}$ (Gell-Mann basis) | Eq. `(gen6)`, Appendix A |
| Benchmark values of couplings and cutoffs | Sec. III.A, text near Figures 3, 4 and 5 |

The two model equations are:

$$
\mathcal{L}\supset\bar\Psi_q(i\slashed{D}-m_{\Psi_q})\Psi_q
+\frac{1}{\Lambda_{\Psi_q}}\big[\kappa^I_q\,\bt{J}^{\,s\,ia}\,(\overline{q^{\rm c}_{\rm R}}_{Ii}\,\sigma^{\mu\nu}\Psi_{qs})\,G_{\mu\nu\,a}+{\rm H.c.}\big]
+\frac{1}{\Lambda^3_{\Psi_{qB}}}\big[\kappa^I_{qB}\,\bt{J}^{\,s\,ia}\,(\overline{q^{\rm c}_{\rm R}}_{Ii}\,\Psi_{qs})\,B^{\mu\nu}G_{\mu\nu\,a}+{\rm H.c.}\big]
$$

$$
\mathcal{L}\supset(D_\mu\Phi_q)^\dagger D^\mu\Phi_q-m^2_{\Phi_q}\Phi_q^\dagger\Phi_q
+\frac{1}{\Lambda^2_{\Phi_q}}\big[\lambda^{XI}_q\,\bt{J}^{\,s\,ia}\,\Phi_{qs}\,(\overline{q^{\rm c}_{\rm R}}_{Ii}\,\sigma^{\mu\nu}\ell_{{\rm R}X})\,G_{\mu\nu\,a}+{\rm H.c.}\big]
$$

with $q\in\{u,d\}$. Eq. `(A18)` gives

$$
\bt{J}^{\,s\,ia}=-i\sqrt{2}\,\bt{L}^{ijk}[t^a_{\boldsymbol 3}]_j^{\ l}\,\bar{\bt{K}}^s_{\ lk},
\qquad \sqrt{2}\,\bt{L}^{ijk}=\epsilon^{ijk}.
$$

So $\bt{J}^{\,s\,ia}=-i\,\epsilon^{ijk}\,[t^a_{\boldsymbol 3}]_j^{\ l}\,(\bt{K}^s_{lk})^*$. This single
identity settles most of the comparison, because it is exactly the color tensor plus the $-i$ that
the reconstruction carries in front of every interaction term.

---

## 1. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| $\bar\Psi_q\,i\slashed{D}\,\Psi_q$, eq. `(sFmodel)` line 1 | `LPsiuFree`, `LPsidFree` kinetic piece $i\bar\Psi_{u,s}\gamma^\mu(D_\mu\Psi_u)_s$ | **agree** | Dirac sextet, covariant derivative in the $\boldsymbol 6$ plus U(1)$_Y$. Paper Table X makes both fermions SU(2)$_L$ singlets, so no $W^\pm$ term. Same in the reconstruction. |
| $-m_{\Psi_q}\bar\Psi_q\Psi_q$, eq. `(sFmodel)` line 1 | $-M_{\Psi u}\bar\Psi_u\Psi_u$, $-M_{\Psi d}\bar\Psi_d\Psi_d$ | **agree** | Dirac mass, no Majorana or chirality-split mass. |
| $(D_\mu\Phi_q)^\dagger D^\mu\Phi_q$, eq. `(sSmodel)` line 1 | `LPhiuFree`, `LPhidFree` kinetic piece | **agree** | Complex scalar sextet. |
| $-m^2_{\Phi_q}\Phi^\dagger_q\Phi_q$, eq. `(sSmodel)` line 1 | $-M^2_{\Phi u}\Phi^\dagger_u\Phi_u$, $-M^2_{\Phi d}\Phi^\dagger_d\Phi_d$ | **agree** | |
| $\dfrac{\kappa^I_q}{\Lambda_{\Psi_q}}\bt{J}^{\,s\,ia}(\overline{q^{\rm c}_{\rm R}}_{Ii}\sigma^{\mu\nu}\Psi_{qs})G_{\mu\nu a}+{\rm H.c.}$, eq. `(sFmodel)` line 2 | `LPsiuG`, `LPsidG`: $-\dfrac{i\kappa^u_f}{\Lambda_{\Psi u}}\varepsilon_{ijk}T^a_{jl}(K^s_{lk})^*\,\overline{(u^c_f)}_i P_R\sigma^{\mu\nu}\Psi_{u,s}G^a_{\mu\nu}+{\rm h.c.}$ | **agree** | Substitute eq. `(A18)`: $\bt{J}=-i\,\varepsilon\,T\,K^*$. The reconstruction's explicit $-i$ is the $-i$ of $\bt{J}$, not an extra factor. Chirality also matches: $\overline{u^c}P_R\sigma^{\mu\nu}\Psi=\overline{(u_{\rm R})^{\rm c}}\sigma^{\mu\nu}\Psi_{\rm R}$, which is the paper's $\overline{q^{\rm c}_{\rm R}}\sigma^{\mu\nu}\Psi_s$. The paper writes no projector on $\Psi$ because the bilinear fixes it. |
| $\dfrac{\kappa^I_{qB}}{\Lambda^3_{\Psi_{qB}}}\bt{J}^{\,s\,ia}(\overline{q^{\rm c}_{\rm R}}_{Ii}\Psi_{qs})B^{\mu\nu}G_{\mu\nu a}+{\rm H.c.}$, eq. `(sFmodel)` line 3 | `LPsiuB`, `LPsidB`: $-\dfrac{i\kappa^{uB}_f}{\Lambda^3_{\Psi uB}}\varepsilon T K^*\,\overline{(u^c_f)}_i P_R\Psi_{u,s}\,B_{\mu\nu}G^{a\mu\nu}+{\rm h.c.}$ | **agree** | No $\sigma^{\mu\nu}$; the two Lorentz indices sit on the two field strengths. The reconstruction says this in words and in the formula. Cutoff power $\Lambda^{-3}$ matches. The cutoff is a separate symbol from the dipole cutoff in both. |
| $\dfrac{\lambda^{XI}_q}{\Lambda^2_{\Phi_q}}\bt{J}^{\,s\,ia}\Phi_{qs}(\overline{q^{\rm c}_{\rm R}}_{Ii}\sigma^{\mu\nu}\ell_{{\rm R}X})G_{\mu\nu a}+{\rm H.c.}$, eq. `(sSmodel)` line 2 | `LPhiuG`, `LPhidG`: $-\dfrac{i\lambda^u_{xf}}{\Lambda^2_{\Phi u}}\varepsilon T K^*\,\Phi_{u,s}\,\overline{(u^c_f)}_i\sigma^{\mu\nu}P_R\ell_x\,G^a_{\mu\nu}+{\rm h.c.}$ | **agree** | Cutoff power $\Lambda^{-2}$ matches. The scalar enters unconjugated ($\Phi_{qs}$, lowered sextet index) in both. Both fermions are right-handed in both texts. |
| Coupling index order $\lambda^{XI}$: $X$ lepton generation, $I$ quark generation (Table IX, eq. `(sSmodel)`) | `lamu[xx, ff]`, first index lepton, second index quark | **agree** | The reconstruction states this explicitly and correctly. |
| $\kappa^I_q$, $\kappa^I_{qB}$ carry one quark generation index (eq. `(sFmodel)`) | `kapu[ff]`, `kapd[ff]`, `kapuB[ff]`, `kapdB[ff]` | **agree** | One sextet couples to all three quark generations. |
| $\bt{J}^{\,s\,ia}=-i\sqrt2\,\bt{L}^{ijk}[t^a_{\boldsymbol 3}]_j^{\ l}\bar{\bt{K}}^s_{\ lk}$, eq. `(A18)`, with $\sqrt2\,\bt{L}^{ijk}=\epsilon^{ijk}$ | $-i\,\varepsilon_{ijk}T^a_{jl}(K^s_{lk})^*$ (the tensor $\mathcal{C}$ times the explicit $-i$) | **agree** | Normalisation and index pattern both match. The paper says this exact rewriting was used so that FeynRules and MadGraph can build $\bt{J}$ from existing objects. |
| $\bt{K}_s^{\ ij}$ symmetric in $i\leftrightarrow j$ (Table I), ${\rm tr}\,\bt{K}_s\bar{\bt{K}}^t=\delta_s^{\ t}$ (eq. `(A16)`) | `K6bar[s,i,j]` symmetric, ${\rm Tr}[K^sK^{t\dagger}]=\delta^{st}$ | **agree** | |
| Sextet generators $t^a_{\boldsymbol 6}$, eq. `(gen6)` | `AddGaugeRepresentation[SU3C -> {T6, Sextet}]`, `T6` | **agree** (unverified numerically) | The reconstruction cannot show the matrices. See disagreement 6. |
| $\Phi_u\sim(\boldsymbol 6,\boldsymbol 1,\tfrac13)$, $L=-1$ (Table X) | $\Phi_u$: $\boldsymbol 6$, SU(2)$_L$ singlet, $Y=Q=+1/3$, $L=-1$ | **agree** | $Q=Y$ holds because $T_3=0$. |
| $\Phi_d\sim(\boldsymbol 6,\boldsymbol 1,\tfrac43)$, $L=-1$ (Table X) | $\Phi_d$: $Y=Q=+4/3$, $L=-1$ | **agree** | |
| $\Psi_u\sim(\boldsymbol 6,\boldsymbol 1,-\tfrac23)$, $L=0$ (Table X) | $\Psi_u$: $Y=Q=-2/3$, $L=0$ | **agree** | |
| $\Psi_d\sim(\boldsymbol 6,\boldsymbol 1,\tfrac13)$, $L=0$ (Table X) | $\Psi_d$: $Y=Q=+1/3$, $L=0$ | **agree** | |
| Benchmark $\kappa^I_u=\kappa^I_d=0.05$, $\Lambda_{\Psi_u}=\Lambda_{\Psi_d}=1$ TeV (Sec. III.A, near Fig. 3) | `kapu`, `kapd` $=0.05$ for all three generations; `LamPsu`, `LamPsd` $=1000$ GeV | **agree** with one caveat | The paper text says "first- and second-generation". Its own footnote near Fig. 6 quotes ${\rm BF}(\Psi_u\to\bar t g)\approx0.21$, which needs a non-zero third-generation coupling. See disagreement 2. |
| Benchmark $\kappa^I_{uB}=0.10$, $\Lambda_{uB}=1$ TeV (Sec. III.A, near Fig. 4) | `kapuB`, `kapdB` $=0.10$; `LamPsuB`, `LamPsdB` $=1000$ GeV | **agree** with one caveat | The paper quotes this benchmark for the up sector only. The down-sector value is an implementation choice. |
| Benchmark $\lambda^{XI}_{u,d}=0.1\,\delta^{XI}$, $\Lambda_{\Phi_u}=\Lambda_{\Phi_d}=1$ TeV (Sec. III.A, near Fig. 5) | `lamu`, `lamd` $=0.1\,\delta_{xf}$; `LamPhu`, `LamPhd` $=1000$ GeV | **agree** | |
| No $\Phi$ quartic and no $|\Phi|^2|H|^2$ portal in eq. `(sSmodel)` | "No quartic self-interaction and no scalar potential beyond the mass terms" | **agree** | Both omit them. Table VI of the paper shows $|\Phi|^4$ exists in the general catalog. See disagreement 5. |
| $\Psi$ mass value and width | `MPSU`, `MPSD`, `MPHU`, `MPHD` $=1000$ GeV; `WPSU`, `WPSD`, `WPHU`, `WPHD` $=10$ GeV | **extra-in-reconstruction** | The paper fixes no default mass; it scans the mass in Figures 2-6. It computes branching fractions, so it does not use a fixed width. See disagreement 1. |
| (not in paper) | Baryon number $B=-1/3$ for all four states | **extra-in-reconstruction** | The reconstruction says the file does not declare $B$, and derives it. The derivation is correct and the conclusion ($B$ and $L$ both conserved, no proton decay) agrees with the paper's Table IX assignments. |
| (not in paper) | PDG codes 9000001/2, 9000011/12; class labels `S[100]`, `S[101]`, `F[100]`, `F[101]`; parameter blocks `SXTCUTOFF`, `KAPU`, ... | **extra-in-reconstruction** | Implementation bookkeeping only. Nothing to check against the paper. |
| (not in paper) | `M$InteractionOrderHierarchy` and the NP order count (NP $=2,3,4$) | **extra-in-reconstruction** | Implementation bookkeeping. The counting is internally consistent with $\Lambda$ carrying `{NP,-1}`. |
| $\bt{J}^{\,s\,ia}(\overline{q^{\rm c}_{\rm R}}_{Ii}\sigma^{\mu\nu}\Psi_s)|H|^2G_{\mu\nu a}$ and $\bt{J}^{\,s\,ia}\Phi_s(\bar L_{{\rm L}X}H\sigma^{\mu\nu}q_{{\rm R}Ii})G_{\mu\nu a}$, Table IX | absent | **missing-in-reconstruction** (expected) | These are catalog rows, not model terms. Eqs. `(sFmodel)` and `(sSmodel)` drop them too, so the reconstruction matches the model the paper actually simulates. |

---

## 2. Disagreements, with severity

I found no disagreement in any Lagrangian term. Every operator, coefficient structure, cutoff
power, chirality, charge and lepton number matches. The items below are gaps between the paper
and the implementation, or claims the reconstruction adds on its own.

1. **Default masses (1 TeV) and widths (10 GeV).** Severity: **convention**.
   A human should check whether the simulation used the hard-coded 10 GeV width or an automatic
   width, because the paper derives its branching fractions from the couplings and a wrong width
   changes every cross section that goes through a resonance.

2. **Third-generation couplings.** Severity: **convention**.
   A human should check whether $\kappa^3_q$ and $\kappa^3_{qB}$ are meant to be 0.05 and 0.10 or
   zero, because the paper's benchmark text says "first- and second-generation" while its own
   branching-fraction footnote needs a non-zero top coupling.

3. **Down-sector $B\!\cdot\!G$ benchmark.** Severity: **cosmetic**.
   A human should confirm that $\kappa^I_{dB}=0.10$ is an assumed value, because the paper gives
   this benchmark only for the up sector.

4. **The claim that a gluon field strength is mandatory.** Severity: **cosmetic**.
   The reconstruction says colour alone forbids any $\bar q\,\Psi$ or $\bar q\,\ell\,\Phi$ term
   without a gluon. A human should note that the paper's Table VIII gives a gluon-free operator
   $\bt{K}_s^{\ ij}\Phi^{\dagger s}(\overline{q^{\rm c}_{\rm R}}_{Ii}q_{{\rm R}Jj})$ for a sextet
   scalar with $Y\in\{-\tfrac23,\tfrac13,\tfrac43\}$, which includes both $Y_{\Phi_u}$ and
   $Y_{\Phi_d}$; lepton number ($L=-1$), not colour, is what removes it here. The conclusion
   (no such term in this model) is right; the stated reason is incomplete.

5. **No scalar potential.** Severity: **cosmetic**.
   A human should note that a renormalisable $|\Phi|^4$ term and a $|\Phi|^2|H|^2$ portal are
   allowed by all symmetries and appear in the paper's own Table VI, but neither the paper's
   eq. `(sSmodel)` nor the file includes them. The two texts agree; the omission is the paper's.

6. **Basis of the sextet objects.** Severity: **substantive, but unresolvable from these two
   files**.
   Eq. `(A18)` holds in the Gell-Mann basis, with $t^a_{\boldsymbol 6}$ given by eq. `(gen6)` and
   $\bt{K}_s$ by eq. `(Kdef)`. A human should check that the file's `T6` and `K6bar` are those
   matrices in that basis, because the reconstruction can only report the symbol names. If the
   file's `T6` follows a different basis or a different generator ordering, every colour factor
   changes while the written Lagrangian still looks correct.

7. **Index heights and the $-i$ placement.** Severity: **cosmetic**.
   The reconstruction folds the $-i$ of eq. `(A18)` into the coupling prefactor and writes the
   rest as a real tensor $\mathcal{C}$. A human should confirm that the file contracts
   $\bar{\bt{K}}^s$ (upper $s$, that is the $\boldsymbol{\bar 6}$ index of $\bt{J}$) with the
   lowered sextet index of $\Psi_s$ or $\Phi_s$, and not the other way round, since $\bt{K}$ is
   real in this basis and the conjugation therefore leaves no numerical trace.

---

## 3. Overall assessment

The reconstruction and the paper describe the same model. All five distinct interaction terms of
eqs. `(sFmodel)` and `(sSmodel)`, doubled over $q\in\{u,d\}$, appear in the reconstruction with the
same fields, the same conjugation pattern, the same right-handed chirality on both fermions, the
same Lorentz structure ($\sigma^{\mu\nu}$ for the two dipole-type operators, no $\sigma^{\mu\nu}$
for the $B\!\cdot\!G$ operator), the same coupling index structure, and the same cutoff powers
$\Lambda^{-1}$, $\Lambda^{-3}$ and $\Lambda^{-2}$. The four fields carry exactly the hypercharges
and lepton numbers of Table X. The colour tensor is the strongest single point of contact: the
reconstruction's $-i\,\varepsilon_{ijk}T^a_{jl}(K^s_{lk})^*$ is, term for term and factor for
factor, the paper's $\bt{J}^{\,s\,ia}$ as rewritten in eq. `(A18)`, including the $\sqrt2$ that
relates $\bt{L}^{ijk}$ to $\epsilon^{ijk}$; the explicit $-i$ in front of every reconstructed term
is that identity and is not an extra phase. The remaining differences are of two kinds: numerical
defaults that the paper never fixes (masses, widths, PDG codes, parameter blocks, interaction-order
counting), and two commentary claims the reconstruction adds on its own (the derived baryon number,
which is correct, and an over-strong colour argument for why a gluon field strength must appear,
whose conclusion is right for the wrong reason). The one thing this pair of documents cannot
settle is whether the file's `T6` and `K6bar` are the Gell-Mann-basis matrices of eqs. `(gen6)` and
`(Kdef)`, and that is the check most worth a human's time, because eq. `(A18)` is basis dependent
and a basis error would leave the written Lagrangian looking correct while changing every colour
factor.
