# Crosscheck: `reconstruction.md` against the Effective LRSM paper

RUN-TAG: XM-CROSS-EffLRSM__swap_chirality

Paper: *Automated Neutrino Jet and Top Jet Predictions at Next-to-Leading-Order with
Parton Shower Matching in Effective Left-Right Symmetric Models*
(Mattelaer, Mitra, Ruiz; IPPP-16-102, CP3-16-51).

## 1. Where the paper defines the model

The paper defines the model in Sec. II, "Effective Left-Right Symmetric Model"
(`\label{sec:theory}`). The relevant places are:

| Location | Content |
| --- | --- |
| Sec. II, first paragraph | Field content: SM states, $W_R^\pm$ and $Z_R$ **aligned with their mass eigenstates**, and three heavy Majorana neutrinos $N_i$ **aligned with the RH chiral states**. |
| Eq. (`chcurrent`), Sec. II | $W_R$ charged current to quarks. |
| Unnumbered equation after Eq. (`chcurrent`) — the $\mathcal{L}_{W_R-\ell-\nu/N}$ equation | $W_R$ charged current to leptons, with the mixing matrices $X_{\ell m}$ and $Y_{\ell m'}$. |
| Equation for $\vert Y\vert^2$ and $\vert X\vert^2$, Sec. II | Scaling of the lepton mixings. |
| Eq. (`eq:lrsmNuMixing`) | Default numerical choice: $\vert Y_{eN}\vert=\vert Y_{\mu N_2}\vert=\vert Y_{\tau N_3}\vert=1$, all other $Y$ and all $X$ set to zero. |
| Table I (`tb:qNumbers`) | $T_L^{3,f}$, $T_R^{3,f}$ and $Q^f$ for every chiral fermion. |
| Eq. (`neucurrent`) | $Z_R$ neutral current, with the $1/\sqrt{1-(1/\kappa_R^f)^2\tan^2\theta_W}$ normalisation. |
| The two equations after Eq. (`neucurrent`) | $g_L^{Z_R,f}=(T_L^{3,f}-Q^f)\tan^2\theta_W/\kappa_R^{f\,2}$ and $g_R^{Z_R,f}=T_R^{3,f}-\tan^2\theta_W Q^f/\kappa_R^{f\,2}$. |
| Partial-width equations, Sec. II | LO $\Gamma(W_R\to q\bar q')$, $\Gamma(W_R\to tb)$, $\Gamma(W_R\to \ell N_{m'})$, $\Gamma(Z_R\to f\bar f)$. |
| Eq. (`eq:massRelationship`), Eq. (`eq:lrsmInputs`), Table II (`tb:lrsmParam`) | $M_{Z_R}\simeq1.7\,M_{W_R}$; benchmark $M_{W_R}=3$ TeV, $m_{N_1}=m_t=173.3$ GeV, $m_{N_2},m_{N_3}=10^{12}$ GeV; total widths $\Gamma_{W_R}=84.3$ GeV, $\Gamma_{Z_R}=114$ GeV, $\Gamma_{N_1}=2.12\times10^{-8}$ GeV. |
| Sec. II C (`sec:modelLimits`) | The model has no LRSM scalar sector; non-Abelian $W_R$ and $Z_R$ self-interactions and their couplings to SM bosons are **ill-defined** and absent. |
| App. C (`app:GenCuts`) | Heavy-neutrino PDG code 9900012. App. A uses the names `wr+`, `wr-`, `zr`, `n1`. |

The paper writes no explicit kinetic or mass terms for $W_R$, $Z_R$ or $N$. It states the
field content and the interaction terms only.

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| Gauge group and effective character: SM + mass-eigenstate $W_R^\pm,Z_R$ + 3 Majorana $N_i$; non-Abelian $V_R$ interactions ill-defined (Sec. II intro, Sec. II C) | §0 and §4: effective Proca fields, no `DC[...]`, no adjoint `FS`, no $V_R$ self-couplings; SM covariant derivative only | **agree** | The reconstruction's "not a gauged $SU(2)_R\times U(1)_{B-L}$" reading matches Sec. II C exactly. |
| $\mathcal{L}_{W_R\text{-}q\text{-}q'}=\frac{-\kappa_R^q g}{\sqrt2}\,\overline{u}_i V^{\rm CKM'}_{ij}\,W^+_{R\mu}\gamma^\mu \mathbf{P_R}\,d_j+\text{H.c.}$ (Eq. `chcurrent`) | `LWRq`: $-\frac{\kappa_R^q g}{\sqrt2}\,\overline{u}_i (V^R_{\rm CKM})_{ij}\gamma^\mu \mathbf{P_L}\,d_j\,W_{R\mu}+\text{h.c.}$ | **disagree** | **Chirality is flipped.** The paper uses the RH projector $P_R$ (it defines $P_{R(L)}=\tfrac12(1\pm\gamma^5)$ right below Eq. `chcurrent`). The reconstruction uses `ProjM` $=P_L$. Prefactor, $\sqrt2$, RH CKM matrix and the h.c. all agree. |
| $V^{\rm CKM'}_{ij}$: RH CKM matrix, taken diagonal with unit entries (`diagonalCKM.rst`, Sec. II) | `VCKMR`, $3\times3$, `Unitary -> True`, set to $\mathbb{1}$ | **agree** | Same object, same default. |
| $\kappa_R^q\in\mathds{R}$: overall normalisation of the $W_R$ quark coupling (Sec. II) | `kapRq`, external, `LRSMINPUTS` 1, value $1.0$, order `{NP,1}` | **agree** | The reconstruction's gloss $\kappa_R^q=g_R/g_L$ is an interpretation; the paper calls it only "an overall normalization". |
| $\mathcal{L}_{W_R\text{-}\ell\text{-}\nu/N}=\frac{-\kappa_R^\ell g}{\sqrt2}\big[\sum_m\overline{\nu^c_m}X_{\ell m}+\sum_{m'}\overline{N_{m'}}Y_{\ell m'}\big]W^+_{R\mu}\gamma^\mu P_R\,\ell^-+\text{H.c.}$ | `LWRl`: $-\frac{\kappa_R^\ell g}{\sqrt2}\big[\overline{N_i}(Y_N)_{ij}\gamma^\mu P_R\ell_j+\overline{\nu^c_i}(X_N)_{ij}\gamma^\mu P_R\ell_j\big]W_{R\mu}+\text{h.c.}$ | **agree** | Both pieces, both projectors $P_R$, the charge conjugation $\overline{\nu^c}$, the prefactor and the h.c. all match. Only the index order of $X$ and $Y$ is transposed (paper: lepton index first). |
| $\kappa_R^\ell\in\mathds{R}$, independent of $\kappa_R^q$ (Sec. II) | `kapRl`, external, `LRSMINPUTS` 2, value $1.0$ | **agree** | |
| $\vert Y_{eN}\vert=\vert Y_{\mu N_2}\vert=\vert Y_{\tau N_3}\vert=1$, all other $Y$ zero; $\vert X_{\ell m}\vert=0$ (Eq. `eq:lrsmNuMixing`) | `YN` $=\mathbb{1}$, `XN` $=0$ | **agree** | Same defaults. The paper also says the defaults can be changed by not loading the restriction files. |
| $\mathcal{L}_{Z_R\text{-}f\text{-}f}=\frac{-\kappa_R^f g}{\sqrt{1-(1/\kappa_R^f)^2\tan^2\theta_W}}\,\overline{f}Z_{R\mu}\gamma^\mu(g_L^{Z_R,f}P_L+g_R^{Z_R,f}P_R)f$ (Eq. `neucurrent`) | `LZRq` and `LZRl`, each $-\frac{\kappa_R g}{n_{Z_R}}[\,g_L\bar f\gamma^\mu P_L f+g_R\bar f\gamma^\mu P_R f\,]Z_{R\mu}$ | **agree** | Same sign, same structure. The split into a quark term and a lepton term reflects the two different $\kappa_R^f$; the paper uses one equation with $f$-dependent $\kappa_R^f$. |
| Normalisation $\sqrt{1-(1/\kappa_R^f)^2\tan^2\theta_W}$ (Eq. `neucurrent`) | `nZRq` $=\sqrt{1-\tan^2\theta_W/\kappa_R^{q\,2}}$, `nZRl` likewise; `tw2` $=s_W^2/c_W^2$ | **agree** | Identical. |
| $g_L^{Z_R,f}=(T_L^{3,f}-Q^f)\tan^2\theta_W/\kappa_R^{f\,2}$; $g_R^{Z_R,f}=T_R^{3,f}-\tan^2\theta_W Q^f/\kappa_R^{f\,2}$ | Master formula $g^f_{L,R}=T_{3R}^f-(Q_f-T_{3L}^f)\tan^2\theta_W/\kappa_R^2$ | **agree** | The single formula reproduces both paper formulas, because $T_{3R}=0$ for left-chiral fields and $T_{3L}=0$ for right-chiral fields (Table I). |
| $g_L^{Z_R,u}$ from Table I: $(\tfrac12-\tfrac23)\tan^2\theta_W/\kappa_R^{q2}=-\tfrac16\tan^2\theta_W/\kappa_R^{q2}$ | `gLZRu` $=-\tfrac16\tan^2\theta_W/\kappa_R^{q2}$ | **agree** | |
| $g_R^{Z_R,u}=\tfrac12-\tfrac23\tan^2\theta_W/\kappa_R^{q2}$ | `gRZRu` $=\tfrac12-\tfrac23\tan^2\theta_W/\kappa_R^{q2}$ | **agree** | |
| $g_L^{Z_R,d}=(-\tfrac12+\tfrac13)\tan^2\theta_W/\kappa_R^{q2}=-\tfrac16\tan^2\theta_W/\kappa_R^{q2}$ | `gLZRd` $=-\tfrac16\tan^2\theta_W/\kappa_R^{q2}$ | **agree** | |
| $g_R^{Z_R,d}=-\tfrac12+\tfrac13\tan^2\theta_W/\kappa_R^{q2}$ | `gRZRd` $=-\tfrac12+\tfrac13\tan^2\theta_W/\kappa_R^{q2}$ | **agree** | |
| $g_L^{Z_R,e}=(-\tfrac12+1)\tan^2\theta_W/\kappa_R^{\ell2}=+\tfrac12\tan^2\theta_W/\kappa_R^{\ell2}$ | `gLZRe` $=+\tfrac12\tan^2\theta_W/\kappa_R^{\ell2}$ | **agree** | |
| $g_R^{Z_R,e}=-\tfrac12+\tan^2\theta_W/\kappa_R^{\ell2}$ | `gRZRe` $=-\tfrac12+\tan^2\theta_W/\kappa_R^{\ell2}$ | **agree** | |
| $g_L^{Z_R,\nu}=(\tfrac12-0)\tan^2\theta_W/\kappa_R^{\ell2}$; $\nu_L$ couples to $Z_R$ through $B-L$ (Sec. II, and $\Gamma(Z_R\to\nu_e\nu_e)=2.78$ GeV in Table II) | `gLZRv` $=+\tfrac12\tan^2\theta_W/\kappa_R^{\ell2}$ | **agree** | |
| $g_R^{Z_R,N}=T_R^{3,N}-0=+\tfrac12$ (Table I, $Q^{N}=0$); $\Gamma(Z_R\to N_1N_1)=10.2$ GeV (Table II) | `gRZRn` $=+\tfrac12$ | **agree** | |
| No $g_R^{Z_R,\nu}$ and no $g_L^{Z_R,N}$: Table I gives $T_R^{3,\nu_L}=0$, $Q^{\nu_L}=0$ and $T_L^{3,N_R}=0$, $Q^{N_R}=0$, so both vanish | §1: "no right-handed light-neutrino term and no left-handed $N$ term" | **agree** | The reconstruction reaches the same conclusion from the file. |
| $M_{W_R}=3000$ GeV, $\Gamma_{W_R}=84.3$ GeV (Eq. `eq:lrsmInputs`, Table II) | `MWR` $=3000$, `WWR` $=84.3$ | **agree** | |
| $M_{Z_R}=5070$ GeV, $\Gamma_{Z_R}=114$ GeV (Table II; consistent with $M_{Z_R}\simeq1.7M_{W_R}$, Eq. `eq:massRelationship`) | `MZR` $=5070$, `WZR` $=114$ | **agree** | |
| $m_{N_1}=m_t=173.3$ GeV, $m_{N_2}=m_{N_3}=10^{12}$ GeV, $\Gamma_{N_1}=2.12\times10^{-8}$ GeV (Eq. `eq:lrsmInputs`, Table II) | `mn1` $=173.3$, `mn2`,`mn3` $=10^{12}$, `Wn1` $=2.12\times10^{-8}$, `Wn2`,`Wn3` $=0$ | **agree** | |
| Heavy neutrino PDG code 9900012 (App. C, `cuts.f` snippet); names `n1`, `wr+`, `wr-`, `zr` (App. A) | PDG 9900012 / 9900014 / 9900016; `WR` 9900024, `ZR` 9900023; members `n1,n2,n3` | **agree** | Only 9900012 and the particle names appear in the paper; the rest is not contradicted. |
| Three $N_i$ are Majorana and aligned with the RH chiral states (Sec. II intro; Keung–Senjanović signature, Sec. I) | `NR` self-conjugate, `F[100]`, 3 generations, gauge singlet | **agree** | |
| No explicit $W_R$ kinetic or mass term in the paper | `LWRkin` $=-\tfrac12 W^\dagger_{R\mu\nu}W_R^{\mu\nu}+M_{W_R}^2 W^\dagger_{R\mu}W_R^\mu$ (Abelian field strength, complex-field normalisation) | **extra-in-reconstruction** | Required for a propagating massive field, and consistent with Sec. II C (no non-Abelian $W_R$ terms). The paper does not state it, so it cannot be confirmed from the paper. |
| No explicit $Z_R$ kinetic or mass term in the paper | `LZRkin` $=-\tfrac14 Z_{R\mu\nu}Z_R^{\mu\nu}+\tfrac12 M_{Z_R}^2 Z_{R\mu}Z_R^\mu$ | **extra-in-reconstruction** | Same remark. Real-field normalisation is correct for a neutral self-conjugate vector. |
| No explicit $N$ kinetic or Majorana mass term in the paper | `LNkin` $=\sum_i[\tfrac i2\overline{N_i}\gamma^\mu\partial_\mu N_i-\tfrac12 M_{N_i}\overline{N_i}N_i]$ | **extra-in-reconstruction** | Standard Majorana normalisation; the masses match Eq. (`eq:lrsmInputs`). Not written in the paper. |
| Not in the paper | `M$InteractionOrderHierarchy = {{QCD,1},{QED,2},{NP,1}}`, new order `NP` on $\kappa_R^{q,\ell}$ | **extra-in-reconstruction** | Pure implementation bookkeeping. The paper's MG5 commands in App. A do not use an `NP` order restriction, so nothing conflicts. |
| SM sector with Goldstone couplings in Feynman gauge, new terms in Unitary gauge (Sec. III A) | "All SM fields come from the imported `LSM`" | **agree** | The reconstruction does not report the gauge choice, but it does not contradict it. |
| LO partial widths $\Gamma(W_R\to q\bar q')$, $\Gamma(W_R\to tb)$, $\Gamma(W_R\to\ell N)$, $\Gamma(Z_R\to f\bar f)$ (Sec. II) | Not reconstructed (they are derived, not implemented) | **missing-in-reconstruction** | Expected: FeynRules computes widths from the Lagrangian; the paper says "We have checked our model against these analytic results." |

## 3. Disagreements, with severity

1. **Chirality of the $W_R$ quark current — SUBSTANTIVE.**
   Eq. (`chcurrent`) uses $P_R$. The reconstruction has `ProjM` $=P_L$ in `LWRq`.
   *What a human should check:* open the implementation file and read the projector in the
   $W_R$–$u$–$d$ term; if it is `ProjM`, the file does not implement Eq. (`chcurrent`), and
   every $W_R$ quark vertex has the wrong handedness.

   Impact, for the reviewer's judgement: the LO partial widths in Sec. II do not change,
   because they are quadratic in the coupling and the quarks are treated as massless. So a
   width table check cannot catch this. What does change is every spin observable and every
   interference: the polar distribution of $j_1$ in the reconstructed $W_R$ frame
   (Fig. `effLRSMnlo_pp_wr_Xjet_cosThStar`), the top polarisation in $W_R\to tb$ that feeds
   the top-jet study in Sec. IV C, and interference with the SM $W$ (which the paper
   switches off for simplicity, but which Sec. III B says can be turned on). A $P_L$ quark
   current also makes $\kappa_R^q$ no longer the ratio $g_R/g_L$ that the $Z_R$ sector
   assumes through $T_R^{3,f}$.

2. **Internal chirality mismatch inside the reconstructed model — SUBSTANTIVE (same root
   cause).**
   The reconstructed $W_R$ lepton current uses $P_R$ and the whole $Z_R$ sector is built on
   $T_R^{3,f}$, while the reconstructed quark current uses $P_L$. The paper is uniformly
   right-handed in both sectors.
   *What a human should check:* whether this asymmetry is a single-line defect in the quark
   term or a deliberate variant model; the reconstruction itself flags the asymmetry twice
   (§1 "Chirality note" and §4), so the reconstruction is faithfully reporting what it read.

3. **Index order of $X$ and $Y$ — CONVENTION.**
   The paper writes $X_{\ell m}$ and $Y_{\ell m'}$ with the charged-lepton flavour first.
   The reconstruction writes $(X_N)_{ij}$ and $(Y_N)_{ij}$ with the neutrino index first.
   *What a human should check:* nothing numerically, because the defaults are $\mathbb{1}$
   and $0$; but confirm the transpose before anyone sets a non-diagonal $Y$ or $X$.

4. **$\kappa_R^f$ read as $g_R/g_L$ — COSMETIC.**
   The paper calls $\kappa_R^{q,\ell}$ "an overall normalization for the $W_R$ interaction
   strength" and never writes $\kappa_R=g_R/g_L$.
   *What a human should check:* that the added interpretation, and the derived claim about a
   lower bound $\kappa_R>\tan\theta_W$, are treated as the reconstruction's commentary, not
   as a statement of the paper.

5. **Proca kinetic and mass terms, and the Majorana $N$ kinetic term — COSMETIC.**
   The paper never writes them; the reconstruction supplies them.
   *What a human should check:* that the normalisations in the file are the ones the
   reconstruction reports ($-\tfrac12|W_{R\mu\nu}|^2+M^2|W_R|^2$ for the charged complex
   field, $-\tfrac14 Z^2+\tfrac12 M^2Z^2$ for the neutral real field, $\tfrac12$ factors for
   Majorana $N$), since a wrong factor there rescales every $W_R$ or $Z_R$ rate.

## 4. Overall assessment

The reconstruction tracks the paper closely almost everywhere. The $Z_R$ sector is an exact
match: the prefactor and its $\sqrt{1-(1/\kappa_R^f)^2\tan^2\theta_W}$ normalisation, the
master formula for the chiral coefficients, and all ten numerical coefficients
(`gLZRu`, `gRZRu`, `gLZRd`, `gRZRd`, `gLZRe`, `gRZRe`, `gLZRv`, `gRZRn`, plus the two absent
couplings) reproduce Eq. (`neucurrent`) together with Table I, entry by entry. The $W_R$
lepton current matches in every element, including the $\overline{\nu^c}$ conjugation, both
mixing matrices and their defaults from Eq. (`eq:lrsmNuMixing`). Every mass, width, PDG code
and input value matches Eq. (`eq:lrsmInputs`) and Table II. The effective, non-gauged reading
of the model agrees with Sec. II C. The single clear conflict is the chiral projector in the
$W_R$ quark current: the paper's Eq. (`chcurrent`) is right-handed ($P_R$), the reconstruction
reports a left-handed one ($P_L`$). This one term is load-bearing, because the paper's whole
subject is right-handed currents, and because the defect is invisible in the width cross-check
the paper itself performed. The reconstruction does not hide the problem; it flags the
asymmetry as internally inconsistent and says it is reporting the file as written. A human
reviewer therefore has two separate questions to settle: whether the implementation file
really carries `ProjM` in that term, and, if so, whether that is a defect in the file or a
defect in the reconstruction's reading of it.
