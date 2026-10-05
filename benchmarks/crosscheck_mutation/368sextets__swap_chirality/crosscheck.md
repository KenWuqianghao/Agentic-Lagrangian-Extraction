# Cross-check: reconstruction vs. paper

Paper: *The phenomenological cornucopia of SU(3) exotica*, Carpenter, Murphy and Tait
(preprint UCI-HEP-TR-2021-26).

## 1. Where the paper defines the model

The paper has two parts. Section II builds a general catalog of colour-sextet
operators (Tables I--IX). Section III picks a small subset of that catalog and
defines the concrete simplified model. The reconstruction describes an
implementation of the **Section III model only**, so the comparison below uses
the Section III equations.

The relevant paper locations are:

* **Eq. \eqref{sFmodel}** (Sec. III, unnumbered `multline` labelled `sFmodel`) --- the
  sextet **fermion** model, for $q \in \{u,d\}$:

  $$
  \mathcal{L} \supset \bar{\Psi}_q(\ii\slashed{D}-m_{\Psi_q})\Psi_q
  + \frac{1}{\Lambda_{\Psi_q}}\big[\kappa_q^I\,\bt{J}^{\,s\,ia}\,
    (\overbar{q^{c}_{R}}_{Ii}\,\sigma^{\mu\nu}\Psi_{qs})\,G_{\mu\nu\,a} + \text{H.c.}\big]
  + \frac{1}{\Lambda_{\Psi_{qB}}^{3}}\big[\kappa_{qB}^I\,\bt{J}^{\,s\,ia}\,
    (\overbar{q^{c}_{R}}_{Ii}\,\Psi_{qs})\,B^{\mu\nu}G_{\mu\nu\,a} + \text{H.c.}\big]
  $$

* **Eq. \eqref{sSmodel}** (Sec. III) --- the sextet **scalar** model, for $q \in \{u,d\}$:

  $$
  \mathcal{L} \supset (D_\mu\Phi_q)^\dagger D^\mu\Phi_q - m^2_{\Phi_q}\Phi_q^\dagger\Phi_q
  + \frac{1}{\Lambda^2_{\Phi_q}}\big[\lambda^{XI}_q\,\bt{J}^{\,s\,ia}\,\Phi_{qs}\,
    (\overbar{q^{c}_{R}}_{Ii}\,\sigma^{\mu\nu}\ell_{\text{R}X})\,G_{\mu\nu\,a} + \text{H.c.}\big]
  $$

* **Table X** (labelled `fields`, Sec. III) --- the quantum numbers of the four new states.
* **Table IX** (labelled `t9`, Sec. II.C) --- the parent operator list for the
  $\boldsymbol{3}\otimes\boldsymbol{6}\otimes\boldsymbol{8}$ invariant.
* **Table I** (labelled `t1`) and **Appendix A**, Eqs. \eqref{Jdef}, \eqref{A16} and
  \eqref{A18} --- the Clebsch-Gordan coefficients $\bt{J}^{\,s\,ia}$, their normalisation,
  and the rewriting used for the FeynRules implementation.
* **Sec. III.A** text (around Figures 3--5) --- the benchmark values of the couplings and
  the cut-off scales.

Two facts from the paper control most of the comparison.

1. **Every** quark bilinear in Eqs. \eqref{sFmodel} and \eqref{sSmodel} is
   $\overbar{q^{c}_{R}}$. This holds for up-type and down-type quarks, and for the
   dimension-5, dimension-6 and dimension-7 operators alike. The paper uses one
   chirality throughout the Section III model.
2. Eq. \eqref{A18} gives
   $\bar{\bt{J}}_{s\,ai} = \ii\sqrt{2}\,\bt{K}_s^{\ kl}[\bt{t}^a_{\boldsymbol 3}]_l^{\ j}\bar{\bt{L}}_{ijk}$
   with $\sqrt{2}\,\bar{\bt{L}}_{ijk}=\epsilon_{ijk}$. The paper says plainly that it
   builds $\bt{J}$ this way inside FeynRules, because FeynRules and MadGraph5
   already carry $\bt{K}$ and the Levi-Civita symbol. This explains the
   $\varepsilon\,T^a\,\bar{K}$ tensor and the explicit factor $\ii$ that the
   reconstruction reports.

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| $\bar{\Psi}_u(\ii\slashed{D}-m_{\Psi_u})\Psi_u$, Eq. \eqref{sFmodel} with $q=u$ | `LPsiuFree` (§1.1) | **agree** | Dirac sextet, weak singlet, $Y=-2/3$; covariant derivative carries $\bt{t}^a_{\boldsymbol 6}$ and hypercharge only. |
| $\bar{\Psi}_d(\ii\slashed{D}-m_{\Psi_d})\Psi_d$, Eq. \eqref{sFmodel} with $q=d$ | `LPsidFree` (§1.2) | **agree** | $Y=+1/3$, matches Table X. |
| $(D_\mu\Phi_u)^\dagger D^\mu\Phi_u - m^2_{\Phi_u}\Phi_u^\dagger\Phi_u$, Eq. \eqref{sSmodel} with $q=u$ | `LPhiuFree` (§1.3) | **agree** | Complex sextet scalar, $Y=+1/3$, matches Table X. |
| $(D_\mu\Phi_d)^\dagger D^\mu\Phi_d - m^2_{\Phi_d}\Phi_d^\dagger\Phi_d$, Eq. \eqref{sSmodel} with $q=d$ | `LPhidFree` (§1.4) | **agree** | $Y=+4/3$, matches Table X. |
| $\frac{\kappa_u^I}{\Lambda_{\Psi_u}}\bt{J}^{\,s\,ia}(\overbar{u^{c}_{R}}_{Ii}\sigma^{\mu\nu}\Psi_{us})G_{\mu\nu\,a}+$H.c., Eq. \eqref{sFmodel} (also Table IX, row "Dirac $\Psi_s$", first entry) | `LPsiuG` (§1.5) with $P_L$: $\overbar{(u_L)^{c}}\,\sigma^{\mu\nu}\Psi_{u,L}$ | **disagree** | **Chirality.** The paper uses the right-handed quark $\overbar{q^{c}_{R}}$. The file uses the left-handed projector. Colour tensor, $\sigma^{\mu\nu}$, $1/\Lambda$ power, generation index and h.c. all agree. This is the single substantive difference. |
| $\frac{\kappa_d^I}{\Lambda_{\Psi_d}}\bt{J}^{\,s\,ia}(\overbar{d^{c}_{R}}_{Ii}\sigma^{\mu\nu}\Psi_{ds})G_{\mu\nu\,a}+$H.c., Eq. \eqref{sFmodel} | `LPsidG` (§1.6) with $P_R$ | **agree** | Right-handed, as the paper states. This term is the direct partner of `LPsiuG` and shows the file's own reference chirality. |
| $\frac{\kappa_{uB}^I}{\Lambda^3_{\Psi_{uB}}}\bt{J}^{\,s\,ia}(\overbar{u^{c}_{R}}_{Ii}\Psi_{us})B^{\mu\nu}G_{\mu\nu\,a}+$H.c., Eq. \eqref{sFmodel} (also Table IX, second Dirac entry) | `LPsiuB` (§1.7) with $P_R$ | **agree** | Scalar bilinear, no $\sigma^{\mu\nu}$; the two Lorentz indices sit on $B_{\mu\nu}$ and $G^{a\,\mu\nu}$; cut-off enters as $1/\Lambda^3$. All correct. |
| $\frac{\kappa_{dB}^I}{\Lambda^3_{\Psi_{dB}}}\bt{J}^{\,s\,ia}(\overbar{d^{c}_{R}}_{Ii}\Psi_{ds})B^{\mu\nu}G_{\mu\nu\,a}+$H.c., Eq. \eqref{sFmodel} | `LPsidB` (§1.8) with $P_R$ | **agree** | Same structure for the down-type partner. |
| $\frac{\lambda^{XI}_u}{\Lambda^2_{\Phi_u}}\bt{J}^{\,s\,ia}\Phi_{us}(\overbar{u^{c}_{R}}_{Ii}\sigma^{\mu\nu}\ell_{\text{R}X})G_{\mu\nu\,a}+$H.c., Eq. \eqref{sSmodel} (also Table IX, row "Scalar $\Phi_s$", first entry) | `LPhiuG` (§1.9) with $\sigma^{\mu\nu}P_R$ | **agree** | Right-handed charged lepton and right-handed quark, $1/\Lambda^2$, coupling index order (lepton first, quark second) all match $\lambda^{XI}_u$. |
| $\frac{\lambda^{XI}_d}{\Lambda^2_{\Phi_d}}\bt{J}^{\,s\,ia}\Phi_{ds}(\overbar{d^{c}_{R}}_{Ii}\sigma^{\mu\nu}\ell_{\text{R}X})G_{\mu\nu\,a}+$H.c., Eq. \eqref{sSmodel} | `LPhidG` (§1.10) | **agree** | Same structure for the down-type leptoquark. |
| Colour tensor $\bt{J}^{\,s\,ia}$, Table I and Eqs. \eqref{Jdef}, \eqref{A18} | $\mathcal{C}^{a,s}_{i_1}=\varepsilon_{i_1i_2i_3}(T^a)_{i_2i_4}(\bar{K}^{s})_{i_4i_3}$, with an explicit prefactor $-\ii$ (§0, §1.5--§1.10) | **agree** | This is Eq. \eqref{A18} written out, with $\sqrt{2}\,\bt{L}=\epsilon$ absorbed. The paper itself says it builds $\bt{J}$ from $\bt{K}$, $\bt{t}^a_{\boldsymbol 3}$ and $\epsilon$ for exactly this reason. The overall sign of $\ii$ and the index height ($\bt{J}$ vs. $\bar{\bt{J}}$) differ; see the convention item in §3. |
| Sextet colour representation, Eq. \eqref{gen6} ($\bt{t}^a_{\boldsymbol 6}$, Gell-Mann basis) | `AddGaugeRepresentation[SU3C -> {T6, Sextet}]` (§0) | **agree** | The new states get their QCD interaction from the $\boldsymbol 6$ generators, as the paper requires. |
| $\Phi_u\sim(\boldsymbol 6,\boldsymbol 1,\tfrac13)$, $L=-1$; Table X | $\Phi_u$: $\boldsymbol 6$, $SU(2)_L$ singlet, $Y=+1/3$, $L=-1$ (§2) | **agree** | |
| $\Phi_d\sim(\boldsymbol 6,\boldsymbol 1,\tfrac43)$, $L=-1$; Table X | $\Phi_d$: $Y=+4/3$, $L=-1$ (§2) | **agree** | |
| $\Psi_u\sim(\boldsymbol 6,\boldsymbol 1,-\tfrac23)$, $L=0$; Table X | $\Psi_u$: $Y=-2/3$, no lepton number (§2) | **agree** | |
| $\Psi_d\sim(\boldsymbol 6,\boldsymbol 1,\tfrac13)$, $L=0$; Table X | $\Psi_d$: $Y=+1/3$, no lepton number (§2) | **agree** | |
| Benchmark $\kappa_u^I=\kappa_d^I=0.05$, $\Lambda_{\Psi_u}=\Lambda_{\Psi_d}=1$ TeV; Sec. III.A (text at Figure 3) | `kapu`, `kapd` $=0.05$ for three generations; `LamPsu`, `LamPsd` $=1000$ GeV (§3.1, §3.2) | **agree** | The paper states the benchmark for $I\in\{1,2\}$, but later quotes $\text{BF}(\Psi_u\to\bar{t}g)\approx0.21$, which needs a third-generation coupling. The file sets all three equal. See the cosmetic item in §3. |
| Benchmark $\kappa_{uB}^I=0.10$, $\Lambda_{uB}=1$ TeV; Sec. III.A (text at Figure 4) | `kapuB`, `kapdB` $=0.10$; `LamPsuB`, `LamPsdB` $=1000$ GeV (§3.1, §3.2) | **agree** | The file adds the matching down-type values, which the paper implies but does not print. |
| Benchmark $\lambda^{XI}_{u,d}=0.1\,\delta^{XI}$, $\Lambda_{\Phi_u}=\Lambda_{\Phi_d}=1$ TeV; Sec. III.A (text at Figure 5) | `lamu`, `lamd` $=0.1\,\delta_{xf}$; `LamPhu`, `LamPhd` $=1000$ GeV (§3.1, §3.2) | **agree** | Diagonal in the lepton-quark generation pair, as the paper specifies. |
| Sextet masses $m_{\Psi}$, $m_{\Phi}$ scanned over Figures 2--6 | `MPSU`, `MPSD`, `MPHU`, `MPHD` $=1000$ GeV (§3.3) | **agree** | A default point inside the paper's scan range, not a claim about the model. |
| (no widths given in the paper) | `WPSU`, `WPSD`, `WPHU`, `WPHD` $=10$ GeV (§3.3) | **extra-in-reconstruction** | Placeholder widths needed by the Monte Carlo tools. Cosmetic. |
| (no coupling-order bookkeeping in the paper) | `M$InteractionOrderHierarchy = {{QCD,1},{QED,2},{NP,1}}`, `NP` $=-1$ per $\Lambda$ and $+1$ per $\kappa,\lambda$ (§3.4) | **extra-in-reconstruction** | FeynRules and MadGraph5 bookkeeping. Cosmetic. |
| (no PDG codes in the paper) | PDG 9000001, 9000002, 9000011, 9000012 (§2) | **extra-in-reconstruction** | Implementation detail. Cosmetic. |
| (baryon number not stated in the paper; Table X gives $L$ only) | $B=-1/3$ for all four states, inferred from the interactions (§2) | **extra-in-reconstruction** | A correct inference, not a claim from the paper. |
| Table IX, third Dirac entry: $\bt{J}^{\,s\,ia}(\overbar{q^{c}_{R}}_{Ii}\sigma^{\mu\nu}\Psi_s)|H|^2G_{\mu\nu\,a}$ | not present | **missing-in-reconstruction** | Expected. Eq. \eqref{sFmodel} does not include this operator, so the model does not use it. Not a defect. |
| Table IX, second scalar entry: $\bt{J}^{\,s\,ia}\Phi_s(\bar{L}_{\text{L}X}H\sigma^{\mu\nu}q_{\text{R}Ii})G_{\mu\nu\,a}$ | not present | **missing-in-reconstruction** | Expected. Eq. \eqref{sSmodel} keeps only the $\ell_{\text{R}}$ operator. Not a defect. |
| Section II catalog, Tables I--VIII (other colour invariants, e.g. $\boldsymbol3\otimes\boldsymbol3\otimes\boldsymbol{\bar6}$ diquark operators) | not present | **missing-in-reconstruction** | Expected. The Section III model is built only on $\boldsymbol 3\otimes\boldsymbol 6\otimes\boldsymbol 8$. Not a defect. |

## 3. Disagreements, with severity

**1. Chirality of `LPsiuG` --- severity: substantive.**

The paper writes the dimension-5 chromomagnetic dipole with the right-handed
quark bilinear $\overbar{u^{c}_{R}}\,\sigma^{\mu\nu}\Psi_u$ in Eq. \eqref{sFmodel},
and Table IX lists the same structure. The reconstruction reports the projector
$P_L$, giving $\overbar{(u_L)^{c}}\,\sigma^{\mu\nu}\Psi_{u,L}$.

Three independent checks point the same way:

* The down-type partner `LPsidG` uses $P_R$, and the paper treats $u$ and $d$
  identically ("for $q\in\{u,d\}$").
* The dimension-7 operator `LPsiuB` couples the *same* two fields $u$ and
  $\Psi_u$ and uses $P_R$.
* All four remaining interaction terms in the file use $P_R$.

So `LPsiuG` is the only left-handed structure among the six interactions. The
reconstruction noticed this by itself and said so in its §1.12, but it reported
the file as written and did not correct it. The disagreement is therefore between
the implementation and the paper, not inside the reconstruction.

*What a human should check:* open the model file, find the `LPsiuG` term, and
confirm whether the first projector is `ProjM` where Eq. \eqref{sFmodel} requires
`ProjP`; then check whether any cross section or branching fraction in the paper
was produced with the left-handed version.

*Why it matters.* The chirality flip removes the interference between the
dimension-5 dipole and the dimension-7 $B$-operator, because the two now act on
opposite quark helicities. It also changes the helicity structure of
$\Psi_u \to \bar{u}g$ and of single $\Psi_u$ production, which feeds the dijet
limits in Figure 6. Unpolarised total rates may move little, so a rate-only test
can miss this.

**2. Index height and overall factor $\ii$ of the colour tensor --- severity: convention.**

Eq. \eqref{sFmodel} contracts with $\bt{J}^{\,s\,ia}$. Eq. \eqref{A18} gives
$\bar{\bt{J}}_{s\,ai} = +\ii\,\epsilon_{ijk}[\bt{t}^a_{\boldsymbol 3}]_l^{\ j}\bt{K}_s^{\ kl}$,
while the reconstruction reports the file using $-\ii\,\varepsilon\,T^a\,\bar{K}$.
The two differ by complex conjugation and by the sign of $\ii$. Both $\bt{J}$
and $\bar{\bt{J}}$ appear once the h.c. term is added, and an overall phase can
be absorbed into $\kappa$ or $\lambda$, so this is very likely only a convention
choice.

*What a human should check:* compare the file's tensor against Eq. \eqref{A18}
index by index, and confirm that the normalisation $\tr\bt{J}_s\bar{\bt{J}}^{\,t}=\delta_s^{\ t}$
of Eq. \eqref{A16} holds with the $1/\sqrt{2}$ factors that sit inside
$\bt{K}_2$, $\bt{K}_4$ and $\bt{K}_6$ in Eq. \eqref{Kdef}.

**3. Third-generation couplings in the benchmark --- severity: cosmetic.**

The paper states the benchmark as $\kappa_q^I=0.05$ and $\kappa_{qB}^I=0.10$ for
$I\in\{1,2\}$. The file sets all three generations. The paper's own footnote
quotes $\text{BF}(\Psi_u\to\bar{t}g)\approx0.21$, which requires a non-zero
third-generation coupling, so the file is consistent with the paper's numbers
even though it is not consistent with the paper's literal sentence.

*What a human should check:* decide which reading the paper's figures used,
because the branching fractions behind Figure 6 depend on it.

**4. Down-type $B$-operator benchmark values --- severity: cosmetic.**

The paper prints $\kappa_{uB}^I=0.10$ and $\Lambda_{uB}=1$ TeV only for the
up-type case (the text at Figure 4). The file also sets `kapdB` $=0.10$ and
`LamPsdB` $=1000$ GeV. Eq. \eqref{sFmodel} covers both, so this is a reasonable
completion, not a contradiction.

*What a human should check:* confirm that no paper figure assumed a vanishing
down-type $B$-coupling.

## 4. Overall assessment

The reconstruction matches the paper closely on almost every point that carries
physics. The field content is exact: four weak-singlet colour sextets with the
hypercharges and lepton numbers of Table X. The operator content is exact: the
free terms, the dimension-5 dipole, the dimension-7 $B$-operator, and the
dimension-6 leptoquark operator, each for the up-type and the down-type case,
each with the correct power of its own cut-off scale and each with its Hermitian
conjugate. The colour tensor is the FeynRules rewriting of $\bt{J}^{\,s\,ia}$
that the paper itself prescribes in Eq. \eqref{A18}, and the benchmark couplings,
cut-offs and masses reproduce the values quoted in Section III.A. The
reconstruction also adds correct material that the paper does not state, such as
the implied baryon number $B=-1/3$ and the leptoquark reading of $\Phi_{u,d}$,
and its collider summary lines up with the paper's Section III.A and III.B. One
point stands apart from all of this: the dimension-5 dipole `LPsiuG` carries the
left-handed projector, while Eq. \eqref{sFmodel} and Table IX both specify the
right-handed quark bilinear $\overbar{q^{c}_{R}}$ for every operator in the
model, and the five sibling terms in the same file all use the right-handed
projector. The reconstruction flagged this asymmetry itself and chose to report
the file as written rather than repair it, which is the correct behaviour for a
reconstruction; the question of whether the file or the paper should change is
left here for the human reviewer, together with the smaller convention and
benchmark items listed in Section 3 above.
