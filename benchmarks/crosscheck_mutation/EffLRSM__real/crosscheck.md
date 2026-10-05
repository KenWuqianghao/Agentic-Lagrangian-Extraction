# Cross-check: `reconstruction.md` against the paper

RUN-TAG: XM-CROSS-EffLRSM__real

Paper: *Automated Neutrino Jet and Top Jet Predictions at Next-to-Leading-Order with
Parton Shower Matching in Effective Left-Right Symmetric Models*
(Mattelaer, Mitra, Ruiz; preprint IPPP-16-102, CP3-16-51).

## 0. Where the paper defines the model

The paper defines the model in **Sec. II, "Effective Left-Right Symmetric Model"**
(and in Sec. II C for what the model leaves out). The relevant places are:

| Item | Location in `paper.tex` |
| --- | --- |
| Gauge group $SU(3)_c\otimes SU(2)_L\otimes SU(2)_R\otimes U(1)_{B-L}$ | Sec. I, displayed equation after "The model, based on the gauge group" |
| Field content: $W_R^\pm$, $Z_R$ aligned with mass eigenstates, three heavy Majorana $N_i$ aligned with the RH chiral states | Sec. II, first paragraph |
| $W_R$ charged current with quarks | Eq. (`chcurrent`) |
| $W_R$ charged current with leptons ($\nu$ and $N$) | Sec. II, the displayed `eqnarray` for $\mathcal{L}_{W_R-\ell-\nu/N}$ (no label) |
| Lepton mixing defaults $\vert Y\vert=\mathbb{1}$, $\vert X\vert=0$ | Eq. (`eq:lrsmNuMixing`) |
| Chiral quantum numbers $T_L^{3,f}$, $T_R^{3,f}$, $Q^f$ | Table `tb:qNumbers` |
| $Z_R$ neutral current | Eq. (`neucurrent`) |
| Chiral coefficients $g_L^{Z_R,f}$, $g_R^{Z_R,f}$ | the two displayed equations right after Eq. (`neucurrent`) |
| Partial and total widths of $W_R$, $Z_R$ | the `eqnarray` block after Table `tb:qNumbers` |
| Benchmark inputs and $M_{Z_R}$–$M_{W_R}$ relation | Eqs. (`eq:lrsmInputs`), (`eq:massRelationship`) |
| Benchmark masses and widths | Table `tb:lrsmParam` |
| Deliberate omissions (no LRSM scalars, ill-defined $W_R/Z_R$ self-couplings) | Sec. II C |
| Gauge choice, FeynRules/NLOCT setup | Sec. III A |
| Heavy-neutrino PDG code 9900012 | App. C (`cuts.f` snippet) |

The paper prints equation labels, not stable numbers, because the source uses
`revtex4-1` with a counter-reset macro. This document cites the labels.

## 1. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| Gauge group $SU(3)_c\otimes SU(2)_L\otimes SU(2)_R\otimes U(1)_{B-L}$ (Sec. I) | Sec. 0, "implied" covariant derivative $D_\mu\supset i g_R T_R^a W^a_{R\mu}+ig_{B-L}\frac{B-L}{2}B^{B-L}_\mu$ | agree | Both say the gauge structure is not written out. The reconstruction infers it from the coupling values. |
| Field content: $W_R^\pm$, $Z_R$, three heavy Majorana $N_i$ (Sec. II, first paragraph) | Sec. 2 field table: `WR` (V[100]), `ZR` (V[101]), `N1,N2,N3` (F[102], Majorana) | agree | Charges, self-conjugation and spin match. $Z_R$ real, $N$ Majorana, $W_R$ charged. |
| $W_R$–quark prefactor $-\kappa_R^q g/\sqrt{2}$, $g=e/\sin\theta_W$ (Eq. `chcurrent`) | `gWRq` $=\kappa_R^q e/(\sqrt2 s_W)$, term carries an explicit minus sign | agree | Same magnitude and same overall sign. |
| $W_R$–quark current $\bar u_i V^{\rm CKM'}_{ij}\gamma^\mu P_R d_j W^+_{R\mu}$ (Eq. `chcurrent`) | `LWRQuarksNonHC`: $V'_{ij}\bar u_i^c\gamma^\mu P_R d_j^c W^+_{R\mu}$ | agree | Pure $P_R$, colour diagonal, up-type barred, down-type unbarred, $W_R^+$. |
| "+ H.c." of Eq. (`chcurrent`) | `LWRQuarks` = noHC + HC, giving the $W_R^-$ current | agree | Correct conjugate structure. |
| $V^{\rm CKM'}$: RH CKM matrix, "related to the SM CKM matrix"; taken diagonal with unit entries (Sec. II) | `CKMR`, $3\times3$ Generation$\times$Generation, identity, `ComplexParameter -> False` | disagree | Value matches the paper's working assumption. The paper does not restrict $V^{\rm CKM'}$ to be real; see D3. |
| $W_R$–lepton prefactor $-\kappa_R^\ell g/\sqrt2$ (Sec. II, $\mathcal{L}_{W_R-\ell-\nu/N}$) | `gWRl` $=\kappa_R^\ell e/(\sqrt2 s_W)$, common to both lepton pieces | agree | One prefactor for the $N$ piece and the $\nu$ piece, as in the paper. |
| Heavy piece $\sum_{m'}\overline{N_{m'}}Y_{\ell m'}W^+_{R\mu}\gamma^\mu P_R\ell^-$ | `LWRLeptonsNonHC`: $Y_{\ell n}\bar N_n\gamma^\mu P_R\ell_\ell W^+_{R\mu}$ | agree | Index order matches: first index = charged-lepton flavour, second = heavy-neutrino flavour. Projector on the charged lepton. |
| Light piece $\sum_m\overline{\nu^c_m}X_{\ell m}W^+_{R\mu}\gamma^\mu P_R\ell^-$ | `LWRLightNuNonHC`: $X_{\ell n}\bar\nu_n\gamma^\mu P_R\ell_\ell W^+_{R\mu}$ | disagree | The paper conjugates the light-neutrino field ($\nu^c$); the reconstruction does not. See D2. |
| "+ H.c." of the lepton current | `LWRLeptons` = both noHC pieces + h.c. | agree | Conjugate terms have $\bar\ell\gamma^\mu P_R N$ and $\bar\ell\gamma^\mu P_R\nu$ with $W_R^-$. |
| $\vert Y_{eN_1}\vert=\vert Y_{\mu N_2}\vert=\vert Y_{\tau N_3}\vert=1$, all other $Y$ and all $X$ zero (Eq. `eq:lrsmNuMixing`) | `YR` = identity, `XL` = zero matrix | agree | Same defaults, same flavour pairing $N_1$–$e$, $N_2$–$\mu$, $N_3$–$\tau$. |
| $Z_R$ current structure $\bar f Z_{R\mu}\gamma^\mu(g_L^{Z_R,f}P_L+g_R^{Z_R,f}P_R)f$, summed over $f$ (Eq. `neucurrent`) | `LZRQuarks`, `LZRLeptons`: same chiral structure, flavour diagonal, generation universal, colour diagonal | agree | No flavour changing neutral current in either. |
| $Z_R$ overall normalization $-\kappa_R^f g\big/\sqrt{1-(1/\kappa_R^f)^2\tan^2\theta_W}$ (Eq. `neucurrent`) | `gZRq`, `gZRl` $=-\kappa_R e/s_W\times\sqrt{1-(s_W/(c_W\kappa_R))^2}$ | disagree | The paper **divides** by the square root; the reconstruction **multiplies** by it. See D1. |
| $g_L^{Z_R,f}=(T_L^{3,f}-Q^f)\tan^2\theta_W/\kappa_R^{f2}$ (after Eq. `neucurrent`) | `gZRuL` $=-\frac16 x_q$, `gZRdL` $=-\frac16 x_q$, `gZRnuL` $=+\frac12 x_\ell$, `gZReL` $=+\frac12 x_\ell$ | agree | Each value reproduces the paper exactly with $x=\tan^2\theta_W/\kappa_R^2$ and Table `tb:qNumbers`. |
| $g_R^{Z_R,f}=T_R^{3,f}-\tan^2\theta_W Q^f/\kappa_R^{f2}$ (after Eq. `neucurrent`) | `gZRuR` $=\frac12-\frac23 x_q$, `gZRdR` $=-\frac12+\frac13 x_q$, `gZReR` $=-\frac12+x_\ell$, `gZRNR` $=+\frac12$ | agree | Each value reproduces the paper exactly. $g_R^{Z_R,N}=\frac12$ because $Q^N=0$. |
| Chiral charge table $T_L^{3,f}$, $T_R^{3,f}$, $Q^f$ (Table `tb:qNumbers`) | Sec. 0 and Sec. 3.2: $T_{3R}=+\frac12$ for $u_R,N_R$, $-\frac12$ for $d_R,e_R$, $0$ for LH fields; $(B-L)=+\frac13$ quarks, $-1$ leptons | agree | The reconstruction uses $(B-L)$ where the paper uses $Q$. The two forms are identical because $Q=T_{3L}+T_{3R}+(B-L)/2$. |
| No $\nu_R$; $\nu_L$ and $N_R$ both carry $B-L$ and couple to $Z_R$ (Sec. II, after Table `tb:qNumbers`) | Light $\nu$ couples through $P_L$ only; $N$ couples through $P_R$ only | agree | Same chirality content. |
| Two independent normalizations $\kappa_R^q$, $\kappa_R^\ell$, both real, same for $W_R$ and $Z_R$ (Sec. II) | `kRquark`, `kRlepton`, real, default $1.0$, used in `gWRq/gZRq` and `gWRl/gZRl` | agree | The reconstruction's remark that independent $\kappa$ values are not a true gauge theory agrees with Sec. II C. |
| $Z_R\to N_1N_1$ allowed, $\Gamma=10.2$ GeV (Table `tb:lrsmParam`) | Sec. 1.5: $Z_R NN$ vertex is purely axial because $N$ is Majorana; `MajoranaPhase -> 1` | agree | The paper does not discuss the axial form, but the vertex exists in both. |
| Benchmark inputs $M_{W_R}=3$ TeV, $m_{N_1}=m_t=173.3$ GeV, $m_{N_2}=m_{N_3}=10^{12}$ GeV (Eq. `eq:lrsmInputs`) | `MWR` $=3000$, `MN1` $=173.3$, `MN2=MN3` $=10^{12}$ GeV | agree | Exact match. |
| Widths $\Gamma_{W_R}=84.3$, $\Gamma_{Z_R}=114$, $\Gamma_{N_1}=2.12\times10^{-8}$ GeV; $M_{Z_R}=5070$ GeV (Table `tb:lrsmParam`) | `WWR` $=84.3$, `WZR` $=114$, `WN1` $=2.12\times10^{-8}$, `MZR` $=5070$ GeV | agree | Exact match. Note the tension with D1: these widths follow from the paper's normalization, not the reconstruction's. |
| $M_{Z_R}=\sqrt{2\cos^2\theta_W/\cos2\theta_W}\,M_{W_R}\approx1.7 M_{W_R}$ (Eq. `eq:massRelationship`) | $M_{Z_R}/M_{W_R}=5070/3000=1.69$ | agree | Same ratio. |
| No LRSM scalar sector; $W_R$, $Z_R$ self-couplings and their couplings to SM bosons are ill-defined (Sec. II C) | Sec. 0 and Sec. 1.6: no `DC[...]`, no `FS[...]`, no scalars, no gauge self-couplings, no $W_L$–$W_R$ or $Z$–$Z_R$ mixing | agree | This is the central "effective" statement, and both texts make it. |
| $W_R$, $Z_R$ aligned with their mass eigenstates (Sec. II, first paragraph) | Sec. 1.6: no $W_R$–$W$ or $Z_R$–$Z$ mixing terms | agree | Same content, different words. |
| SM sector in the Feynman gauge with Goldstone couplings; the new terms in the unitary gauge (Sec. III A) | `FeynmanGauge = False` (unitary gauge, no Goldstone partners for $W_R$, $Z_R$) | disagree | Only the new-state half of the paper's statement is reported. See D4. |
| Heavy-neutrino PDG code 9900012 (App. C) | `N1` PDG 9900012 | agree | Exact match. |
| Five massless quarks assumed; restriction files `massless.rst`, `diagonalCKM.rst` (Sec. II) | not mentioned | missing-in-reconstruction | The reconstruction's identity `CKMR` matches `diagonalCKM.rst`, but the massless-quark restriction is not reported. |
| Analytic $\Gamma(W_R\to q\bar q')$, $\Gamma(W_R\to tb)$, $\Gamma(W_R\to\ell N)$, $\Gamma(Z_R\to f\bar f)$ formulas (Sec. II) | not derived; widths appear only as numerical declarations | missing-in-reconstruction | Expected: widths are external inputs in the implementation file, not Lagrangian terms. No physics is lost. |
| — | PDG codes 9900024 ($W_R$), 9900032 ($Z_R$), 9900014, 9900016 ($N_2$, $N_3$) | extra-in-reconstruction | The paper gives only 9900012 and the MG5 names `wr+`, `wr-`, `zr`, `n1`. The other codes cannot be checked against the paper. |
| — | LHA blocks `BSMINPUTS`, `CKMR`, `HNUMIX`, `LNUMIX`; classes V[100], V[101], F[102]; `InteractionOrder -> {NP,1}`; `M$InteractionOrderHierarchy = {{NP,2},{QCD,1},{QED,2}}` | extra-in-reconstruction | Pure implementation bookkeeping. The paper says nothing about it. Not an error. |
| — | Consistency condition $\kappa_R>\tan\theta_W$ ($g_R>g_Y$) | extra-in-reconstruction | A correct consequence of the square root, but the paper does not state it. |

## 2. Disagreements, with severity

**D1 — $Z_R$ overall normalization: square root in the wrong place. Severity: substantive.**

The paper writes the prefactor as $-\kappa_R^f g\big/\sqrt{1-(1/\kappa_R^f)^2\tan^2\theta_W}$,
that is, the square root is in the **denominator**. The reconstruction writes
`gZRq`, `gZRl` with the square root as a **multiplying** factor. With
$x\equiv\tan^2\theta_W/\kappa_R^2$, the two differ by $(1-x)$. For $\kappa_R=1$ and
$\sin^2\theta_W=0.23126$ (Eq. `eq:smInputs`), $x=0.301$, so the reconstruction's
$Z_R$ coupling is $0.699$ of the paper's, and every $Z_R$ rate is $0.489$ of the
paper's. Three independent checks point the same way. First, the paper's width
formula carries $[1-(1/\kappa_R^f)^2\tan^2\theta_W]$ in the **denominator**.
Second, Table `tb:lrsmParam` gives $\Gamma_{Z_R}=114$ GeV at $M_{Z_R}=5070$ GeV;
the reconstruction's normalization gives about $56$ GeV, yet the reconstruction
quotes `WZR` $=114$ GeV. Third, the exact $SU(2)_R\times U(1)_{B-L}$ result is
$g_R\sqrt{1-x}\,[T_{3R}-\frac{x}{1-x}\frac{B-L}{2}]
=\frac{g_R}{\sqrt{1-x}}[(1-x)T_{3R}-x\frac{B-L}{2}]$; the reconstruction pairs the
**second** bracket with the **first** prefactor, so it is also internally
inconsistent.
*Human check:* open the implementation file, read the `gZRq` and `gZRl`
definitions, and confirm whether the square root divides or multiplies; then
recompute $\Gamma(Z_R\to f\bar f)$ and compare with the 114 GeV total in Table
`tb:lrsmParam`.

**D2 — Light-neutrino field is not conjugated. Severity: convention (can become substantive).**

The paper writes $\overline{\nu^c_m}X_{\ell m}$ in the $W_R$ lepton current. The
reconstruction writes $\bar\nu_n$ with no charge conjugation. If the light
neutrinos are Majorana, $\nu^c=\nu$ and the difference is a phase convention. If
the underlying SM file treats `ve` as a Dirac field, the conjugation decides which
state the $W_R^+$ produces, and therefore the lepton-number flow in
$W_R\to\ell\nu$.
*Human check:* confirm whether `ve` in the base SM model is Majorana or Dirac, and
whether the implementation uses `CC[ve]`; note that `XL` is zero by default, so
this term produces no numbers until a user switches it on.

**D3 — `CKMR` declared real. Severity: convention.**

The paper calls $V^{\rm CKM'}$ the RH CKM matrix and only *assumes* it is diagonal
with unit entries for this study. The reconstruction reports
`ComplexParameter -> False`, which removes RH CP phases from the model, not only
from the benchmark point.
*Human check:* decide whether the public model file is meant to support complex
RH quark mixing after a UFO regeneration, as Sec. II suggests.

**D4 — Gauge choice reported for one half of the model only. Severity: cosmetic.**

Sec. III A states that the SM Lagrangian is implemented with Goldstone couplings
in the Feynman gauge, while Eqs. (`chcurrent`)–(`neucurrent`) are implemented in
the unitary gauge. The reconstruction reports only `FeynmanGauge = False`.
*Human check:* confirm that the global flag in the file is a property of the BSM
fragment and does not silently change the SM half.

**D5 — PDG codes and LHA blocks that the paper does not state. Severity: cosmetic.**

Only 9900012 appears in the paper (App. C). The codes 9900024, 9900032, 9900014
and 9900016, and the block names `BSMINPUTS`, `HNUMIX`, `LNUMIX`, are unverifiable
from the paper.
*Human check:* compare them against the public EffLRSM UFO on the FeynRules
database.

**D6 — Massless-quark restriction not reported. Severity: cosmetic.**

Sec. II says the study assumes five massless quarks and loads `massless.rst`.
*Human check:* confirm that the reconstruction's source file is the unrestricted
model, in which case the omission is correct rather than a miss.

## 3. Overall assessment

The reconstruction and the paper describe the same model over almost all of its
content. The field content, the chirality of every current, the index structure of
the mixing matrices $V^{\rm CKM'}$, $Y$ and $X$, the two independent normalizations
$\kappa_R^q$ and $\kappa_R^\ell$, all eight $Z_R$ chiral charges, the benchmark
masses and widths, the $M_{Z_R}/M_{W_R}$ ratio, and the deliberate omissions (no
scalars, no gauge self-couplings, no $W_L$–$W_R$ mixing) all agree, and the
reconstruction's $(1-x)T_{3R}-x(B-L)/2$ form is an exact rewriting of the paper's
$g_L^{Z_R,f}$ and $g_R^{Z_R,f}$ equations. One item stands apart from the rest:
the $Z_R$ overall normalization, where the paper divides by
$\sqrt{1-(1/\kappa_R)^2\tan^2\theta_W}$ and the reconstruction multiplies by it.
That single placement changes every $Z_R$ rate by a factor of about two at
$\kappa_R=1$, it contradicts the $Z_R$ width formula and the 114 GeV entry in
Table `tb:lrsmParam`, and it is inconsistent with the reconstruction's own chiral
charges, so it is either a real defect in the implementation file or an error made
while reconstructing that one line. The light-neutrino conjugation is the only
other physics-level difference, and it is inert at the default $X=0$. The
remaining items are bookkeeping that the paper never fixes. A human reviewer
should settle D1 first, because it alone decides whether the two documents
describe the same $Z_R$ sector.
