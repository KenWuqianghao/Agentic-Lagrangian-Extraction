# Crosscheck: `reconstruction.md` against the paper

RUN-TAG: XM-CROSS-EffLRSM__factor2

Paper: *Automated Neutrino Jet and Top Jet Predictions at Next-to-Leading-Order with Parton
Shower Matching in Effective Left-Right Symmetric Models* (Mattelaer, Mitra, Ruiz;
IPPP-16-102, CP3-16-51).

## 1. Where the paper defines the model

The full model definition is in Sec. II, "Effective Left-Right Symmetric Model", and in
Sec. III.A, "Model Implementation". The relevant places are:

| Item | Location in `paper.tex` |
|---|---|
| Field content: SM + $W_R^\pm$ + $Z_R$ + three heavy Majorana $N_i$ | Sec. II, first paragraph |
| $W_R$ charged current, quarks | Eq. (`chcurrent`), Sec. II |
| $W_R$ charged current, leptons | the unnumbered display just after Eq. (`chcurrent`) ($\mathcal{L}_{W_R-\ell-\nu/N}$) |
| Mixing-matrix scaling and benchmark values | Eq. (`eq:lrsmNuMixing`) |
| Chiral charges $T_L^3$, $T_R^3$, $Q$ | Table `tb:qNumbers` |
| $Z_R$ neutral current | Eq. (`neucurrent`), Sec. II |
| $g_L^{Z_R,f}$, $g_R^{Z_R,f}$ definitions | the two displays just after Eq. (`neucurrent`) |
| LO partial widths | the width displays after the $g_{L,R}$ definitions |
| Benchmark masses | Eq. (`eq:lrsmInputs`) and Eq. (`eq:massRelationship`) |
| Masses and total widths | Table `tb:lrsmParam` |
| No new gauge self-interactions | Sec. II.C, "Limitations of the Effective Left-Right Symmetric Model" |
| Gauge to implement in, and the FeynRules workflow | Sec. III.A |
| Heavy-neutrino PDG code 9900012 | App. C, `cuts.f` listing |

The paper gives no explicit kinetic or mass term for $W_R$, $Z_R$ or $N$. It only states
that the new vectors are aligned with their mass eigenstates, that the $N_i$ are Majorana,
and that the new terms are implemented in the Unitary gauge.

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| $W_R^\pm$, $Z_R$: massive vectors aligned with mass eigenstates (Sec. II, para. 1); no explicit kinetic term written | `LWRkin` $=-\tfrac12 W^-_{R\mu\nu}W_R^{+\mu\nu}+M_{W_R}^2W^-_{R\mu}W_R^{+\mu}$; `LZRkin` $=-\tfrac14 Z_{R\mu\nu}Z_R^{\mu\nu}+\tfrac12 M_{Z_R}^2 Z_{R\mu}Z_R^\mu$ (§1.1, §1.2) | agree | Standard Proca normalisation for one complex and one real vector. The paper does not write these terms, so they are implied, not quoted. Abelian field strengths carry no self-coupling, which matches Sec. II.C. |
| Non-Abelian $W_R$, $Z_R$ interactions and their couplings to SM bosons are "ill-defined" and not modelled (Sec. II.C) | No `DC` anywhere; new vectors are not gauge fields; no triple or quartic self-couplings (§0, §4) | agree | The reconstruction reads this as a property of the model, which is what Sec. II.C states. |
| Three heavy Majorana neutrinos $N_i$, aligned with the RH chiral states, SM singlets, charged only under $SU(2)_R\otimes U(1)_{B-L}$ (Sec. I, Sec. II) | `F[100] NR`, `SelfConjugate -> True`, `Index[Generation]`, no colour, no $SU(2)_L$ rep, $Q=0$ (§2) | agree | Majorana nature, three generations and singlet status all match. |
| Majorana mass of $N$ (implied by "Majorana neutrinos" plus $m_{N}$ in Eq. (`eq:lrsmInputs`)) | `LNkin` $=\tfrac{i}{2}\overline{N_f}\gamma^\mu\partial_\mu N_f-\tfrac12 M_{N_f}\overline{N_f}N_f$ (§1.3) | agree | The $\tfrac12$ factors are the standard Majorana normalisation. The paper writes no such term. |
| $\mathcal{L}_{W_R-q-q'}=\dfrac{-\kappa_R^q g}{\sqrt{2}}\,\overline{u}_i V^{\rm CKM'}_{ij}W^+_{R\mu}\gamma^\mu P_R d_j+{\rm H.c.}$ — Eq. (`chcurrent`) | $\mathcal{L}^q_{W_R}= \mathbf{2}\left[-\dfrac{\kappa_R^q g_w}{\sqrt2}\overline{u}_i (V^R_{\rm CKM})_{ij}\gamma^\mu P_R d_j W^+_{R\mu}+{\rm h.c.}\right]$ (§1.4) | **disagree** | Field content, chirality ($P_R$), flavour structure and the $-\kappa_R^q g/\sqrt2$ factor all match, but the reconstruction multiplies the whole term, h.c. included, by an overall **2**. See D1. |
| $\mathcal{L}_{W_R-\ell-\nu/N}=\dfrac{-\kappa_R^\ell g}{\sqrt2}\left[\sum_m\overline{\nu^c_m}X_{\ell m}+\sum_{m'}\overline{N_{m'}}Y_{\ell m'}\right]W^+_{R\mu}\gamma^\mu P_R\,\ell^-+{\rm H.c.}$ (display after Eq. (`chcurrent`)) | $-\dfrac{\kappa_R^\ell g_w}{\sqrt2}\left[\overline{N}_i (Y_N)_{ij}+\overline{\nu^c_i}(X_N)_{ij}\right]\gamma^\mu P_R \ell_j W^+_{R\mu}+{\rm h.c.}$ (§1.5) | agree | Both currents present, both with $P_R$, both with the same prefactor and no extra factor. The matrix index order differs: the paper writes $X_{\ell m}$, $Y_{\ell m'}$ (lepton index first); the reconstruction writes $(X_N)_{ij}$, $(Y_N)_{ij}$ with the neutrino index first. See D2. |
| No prefactor 2 on the lepton charged current (same display) | No prefactor on `LWRl` (§1.5) | agree | The lepton term is normalised as the paper writes it. This makes the quark-term factor 2 an asymmetry inside the reconstruction as well. |
| $|Y_{eN}|=|Y_{\mu N_2}|=|Y_{\tau N_3}|=1$, all other $Y$ and all $X$ zero — Eq. (`eq:lrsmNuMixing`) | $Y_N=\mathbb{1}_{3\times3}$, $X_N=0_{3\times3}$ (§3.2) | agree | Same benchmark point. The light-neutrino right-handed current is present in the Feynman rules but switched off numerically, which matches "at TeV collider scales ... light neutrino mixing can be taken to zero". |
| RH CKM matrix $V^{\rm CKM'}$, taken diagonal with unit entries (Sec. II, after Eq. (`chcurrent`)) | `VCKMR` $=\mathbb{1}_{3\times3}$, `Unitary -> True` (§3.2) | agree | Same assumption. The paper notes it comes from the `diagonalCKM.rst` restriction. |
| $\kappa_R^q,\kappa_R^\ell\in\mathds{R}$, independent normalisations of the quark and lepton $W_R$ couplings (Sec. II) | `kapRq`, `kapRl`, external, real, default 1., block `LRSMINPUTS` (§3.1) | agree | Two independent real inputs, as the paper requires. Default 1. matches the benchmark $\kappa_R^{q,\ell}=1$. |
| $\mathcal{L}_{Z_R-f-f}=\dfrac{-\kappa_R^f g}{\sqrt{1-(1/\kappa_R^f)^2\tan^2\theta_W}}\,\overline{f}Z_{R\mu}\gamma^\mu(g_L^{Z_R,f}P_L+g_R^{Z_R,f}P_R)f$ — Eq. (`neucurrent`) | `LZRq` $=-\dfrac{\kappa_R^q g_w}{n^q_{Z_R}}[\,\dots]Z_{R\mu}$ and `LZRl` $=-\dfrac{\kappa_R^\ell g_w}{n^\ell_{Z_R}}[\,\dots]Z_{R\mu}$, with $n_{Z_R}=\sqrt{1-t_W^2/\kappa_R^2}$ (§1.6, §1.7) | agree | Same prefactor. The paper's single sum over $f$ is split into a quark part and a lepton part, because $\kappa_R^q$ and $\kappa_R^\ell$ differ. No factor 2 and no mixing matrix on either part. |
| $g_L^{Z_R,f}=(T_L^{3,f}-Q^f)\tan^2\theta_W/\kappa_R^{f\,2}$ (display after Eq. (`neucurrent`), with Table `tb:qNumbers`) | $g_L^u=g_L^d=-\tfrac16 t_W^2/\kappa_R^{q2}$; $g_L^e=g_L^\nu=+\tfrac12 t_W^2/\kappa_R^{\ell2}$ (§3.2) | agree | All four values reproduce the paper: $u$: $\tfrac12-\tfrac23=-\tfrac16$; $d$: $-\tfrac12+\tfrac13=-\tfrac16$; $e$: $-\tfrac12+1=+\tfrac12$; $\nu$: $\tfrac12-0=+\tfrac12$. The reconstruction's equivalent form $g_L^f=-Y_{f_L}t_W^2/\kappa_R^2$ follows from $Q=T_L^3+Y$. |
| $g_R^{Z_R,f}=T_R^{3,f}-Q^f\tan^2\theta_W/\kappa_R^{f\,2}$ (same display, with Table `tb:qNumbers`) | $g_R^u=\tfrac12-\tfrac23 t_W^2/\kappa_R^{q2}$; $g_R^d=-\tfrac12+\tfrac13 t_W^2/\kappa_R^{q2}$; $g_R^e=-\tfrac12+t_W^2/\kappa_R^{\ell2}$; $g_R^N=\tfrac12$ (§3.2) | agree | All four values reproduce the paper, including $g_R^N=T_R^{3,N}=+\tfrac12$ with $Q^N=0$. |
| $\nu_L$ and $N_R$ both carry $B-L$ and so both couple to $Z_R$ (Sec. II, after Table `tb:qNumbers`); Table `tb:qNumbers` has no right-handed light $\nu$ and no left-handed $N$ | Light $\nu$ couples only through $P_L$; $N$ couples only through $P_R$; $g_L^N$ and $g_R^\nu$ absent (§1.7) | agree | Correct: $T_L^{3,N_R}=0$ and $Q^N=0$ give $g_L^{Z_R,N}=0$, and the model has no right-handed light neutrino. |
| $\tan^2\theta_W$ from SM inputs, Eq. (`eq:smInputs`) | `tw2` $=s_w^2/c_w^2$, internal (§3.2) | agree | Derived, not a new input. |
| SM sector fully supported, implemented with Goldstone couplings in the Feynman gauge (Sec. II.C, Sec. III.A) | $\mathcal{L}_{\rm SM}$ imported unchanged; SM fields and $g_w,s_w,c_w$ not redefined (§0, §1.8) | agree | Same structure. |
| $M_{W_R}=3$ TeV, $m_{N_1}=m_t=173.3$ GeV, $m_{N_2}=m_{N_3}=10^{12}$ GeV — Eq. (`eq:lrsmInputs`) | `MWR` $=3000.$, `mn1` $=173.3$, `mn2` $=$ `mn3` $=10^{12}$ (§2) | agree | Exact match, including the deliberate decoupling of $N_2$ and $N_3$. |
| $M_{Z_R}=\sqrt{2\cos^2\theta_W/\cos2\theta_W}\,M_{W_R}\approx1.7\,M_{W_R}$ — Eq. (`eq:massRelationship`); Table `tb:lrsmParam` gives 5070 GeV | `MZR` $=5070.$ (§2) | agree | $5070/3000=1.69$, consistent with Eq. (`eq:massRelationship`). |
| Total widths $\Gamma_{W_R}=84.3$ GeV, $\Gamma_{Z_R}=114$ GeV, $\Gamma_{N_1}=2.12\times10^{-8}$ GeV — Table `tb:lrsmParam` | `WWR` $=84.3$, `WZR` $=114.$, `Wn1` $=2.12\times10^{-8}$, `Wn2` $=$ `Wn3` $=0$ (§2) | agree | The stored widths match the paper's table. They do **not** match the factor-2 quark current; see D1. |
| Heavy neutrino PDG code 9900012 (App. C, `cuts.f`) | `9900012 / 9900014 / 9900016` for $N_{1,2,3}$ (§2) | agree | Only 9900012 appears in the paper. The other two follow the same PDG convention. |
| Particle names `wr+`, `wr-`, `zr`, `n1` used in the MG5 commands (App. A) | `wr+` with $Q=+1$, `zr`, `n1,n2,n3` (§0, §2) | agree | Names and charge assignment match the paper's usage. |
| PDG codes of $W_R$, $Z_R$ | 9900024 ($W_R$), 9900023 ($Z_R$) (§2) | extra-in-reconstruction | The paper never states these codes. They follow the standard convention, but the paper gives nothing to check them against. |
| $N\to\ell^\pm W_R^{\mp*}\to\ell^\pm q\overline{q'}$, branching fraction 100 % (Sec. IV.C, Fig. `fig:Decay`) | Same decay chain described in §4 | agree | Follows from the Lagrangian, not an independent term. |
| $M$\$`InteractionOrderHierarchy` = {QCD,1}, {QED,2}, {NP,1}; only $\kappa_R^{q,\ell}$ carry NP (§3.3) | — | extra-in-reconstruction | Bookkeeping needed by FeynRules and MG5. The paper does not discuss interaction orders. |
| LO and NLO partial-width formulas, $r_i^{V_R}=m_i^2/M_{V_R}^2$ (displays before Table `tb:lrsmParam`) | — | missing-in-reconstruction | These are analytic cross-checks in the paper, not Lagrangian terms. A `.fr` file is not expected to contain them. |
| LRSM scalar sector (bidoublet, triplets); LRSM Higgs masses 15–20 TeV and decoupled (Sec. II.C) | Absent | agree | The paper states the effective model has no LRSM scalars. Their absence is correct. |

## 3. Disagreements

**D1 — Overall factor 2 on the quark $W_R$ charged current. Severity: substantive.**
Eq. (`chcurrent`) has the coefficient $-\kappa_R^q g/\sqrt2$ and no extra factor; the
reconstruction's `LWRq` multiplies the whole term and its h.c. by 2, giving
$-\sqrt2\,\kappa_R^q g$. The vertex is then twice as large, and every $W_R$ rate from
quarks is four times as large. The paper's own numbers settle which normalisation it
intends: with $\alpha=1/127.940$ and $\sin^2\theta_W=0.23126$ (Eq. (`eq:smInputs`)), the
paper's formula $\Gamma(W_R\to q\overline{q'})=N_c|V|^2\kappa_R^{q2}g^2M_{W_R}/48\pi$ gives
25.4 GeV per light-quark channel, which reproduces the 50.7 GeV and 25.2 GeV entries and
the 84.3 GeV total of Table `tb:lrsmParam`. With the factor 2, the quark partial widths
would each grow by four, and the $W_R$ total width would be about 312 GeV instead of
84.3 GeV. The reconstruction keeps `WWR` $=84.3$, so the file would also be internally
inconsistent. **A human should check the `LWRq` definition in the implementation file for a
stray overall 2 (or a `2 (tmp + HC[tmp])` where `tmp + HC[tmp]` is meant), and confirm that
the $W_R\to q\overline{q'}$ partial width computed from the model equals 25.4 GeV per
channel.**

**D2 — Index order of the leptonic mixing matrices $X$ and $Y$. Severity: convention.**
The paper writes $\overline{\nu^c_m}X_{\ell m}$ and $\overline{N_{m'}}Y_{\ell m'}$, so the
first index is the charged-lepton flavour and the second is the neutrino index. The
reconstruction writes $(X_N)_{ij}$ and $(Y_N)_{ij}$ with the first index on the barred
neutrino field and the second on the charged lepton, that is, the transpose. At the
benchmark point this has no effect, because $Y_N$ is the identity and $X_N$ is zero.
**A human should check the index order before using any non-diagonal $X$ or $Y$, because
a transpose changes which $N_i$ pairs with which $\ell_j$ once the matrices are
off-diagonal.**

**D3 — $W_R$ and $Z_R$ PDG codes are not verifiable from the paper. Severity: cosmetic.**
The reconstruction reports 9900024 and 9900023. The paper states only 9900012, for the
heavy neutrino. **A human should confirm 9900024 and 9900023 against the public UFO file,
since App. A refers to the states only by the names `wr+`, `wr-` and `zr`.**

**D4 — Majorana bookkeeping in the $Z_R$–$N$–$N$ term. Severity: convention.**
The reconstruction writes $g_R^N\overline{N}\gamma^\mu P_R N$, in the same generic form as
Eq. (`neucurrent`). For a self-conjugate field the vector part of this current vanishes and
only the axial part survives, so the effective vertex differs from the naive Dirac case by
a fixed factor. The paper's generic notation carries the same ambiguity, so this is not a
mismatch between the two documents. **A human should check the $\Gamma(Z_R\to N_1N_1)=10.2$
GeV entry of Table `tb:lrsmParam` against the model, because that number fixes the
convention.**

## 4. Overall assessment

The reconstruction and the paper describe the same model over almost the whole Lagrangian.
The field content, the Majorana nature and generation structure of $N$, the chirality and
flavour structure of both $W_R$ charged currents, the $Z_R$ prefactor
$1/\sqrt{1-t_W^2/\kappa_R^2}$, all eleven $Z_R$ chiral charges, the two independent real
inputs $\kappa_R^q$ and $\kappa_R^\ell$, the identity RH CKM matrix, the benchmark masses
and the three stored widths all agree with Eqs. (`chcurrent`), (`neucurrent`),
(`eq:lrsmNuMixing`), (`eq:lrsmInputs`) and Tables `tb:qNumbers` and `tb:lrsmParam`. The
reconstruction's reading of the new vectors as non-gauged Proca fields with no
self-interaction also matches Sec. II.C. One item stands apart from this agreement: the
overall factor 2 on the quark $W_R$ current, which the paper's Eq. (`chcurrent`) does not
carry and which the paper's own width table contradicts by a factor of about 3.7 in the
$W_R$ total width. The reconstruction itself flags this factor twice, in §1.4 and §4, and
reports it as written rather than silently normalising it away, which is the right
behaviour for a reconstruction; it does not, however, weigh it against the paper. The other
three items are matters of convention or of information the paper does not contain. The
decision on whether the factor 2 is an error in the implementation file, an error in the
reconstruction, or an intended deviation from the published normalisation belongs to the
human reviewer.
