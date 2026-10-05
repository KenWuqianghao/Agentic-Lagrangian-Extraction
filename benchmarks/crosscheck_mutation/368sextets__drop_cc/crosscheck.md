# Cross-check: `reconstruction.md` against the paper

RUN-TAG: XM-CROSS-368sextets__drop_cc

Paper: *The phenomenological cornucopia of SU(3) exotica*, L. M. Carpenter, T. Murphy,
T. M. P. Tait (preprint UCI-HEP-TR-2021-26).

## 1. Where the paper defines the model

The paper defines the simplified models in Section III ("Sextets at the LHC"):

- **Eq. \eqref{sFmodel}** (the `multline` labelled `sFmodel`) — the sextet **fermion** model:

  $$\mathcal{L}\supset \bar{\Psi}_q(\mathrm{i}\slashed{D}-m_{\Psi_q})\Psi_q
  +\frac{1}{\Lambda_{\Psi_q}}\big[\kappa_q^{I}\,\bt{J}^{\,s\,ia}\,(\overline{q^{c}_{R}}_{Ii}\,\sigma^{\mu\nu}\Psi_{qs})\,G_{\mu\nu\,a}+\text{H.c.}\big]
  +\frac{1}{\Lambda^{3}_{\Psi_qB}}\big[\kappa_{qB}^{I}\,\bt{J}^{\,s\,ia}\,(\overline{q^{c}_{R}}_{Ii}\,\Psi_{qs})\,B^{\mu\nu}G_{\mu\nu\,a}+\text{H.c.}\big]$$

  for $q\in\{u,d\}$.

- **Eq. \eqref{sSmodel}** — the sextet **scalar** model:

  $$\mathcal{L}\supset (D_\mu\Phi_q)^{\dagger}D^{\mu}\Phi_q-m^{2}_{\Phi_q}\Phi_q^{\dagger}\Phi_q
  +\frac{1}{\Lambda^{2}_{\Phi_q}}\big[\lambda_q^{XI}\,\bt{J}^{\,s\,ia}\,\Phi_{qs}\,(\overline{q^{c}_{R}}_{Ii}\,\sigma^{\mu\nu}\ell_{RX})\,G_{\mu\nu\,a}+\text{H.c.}\big].$$

- **Table X** (label `fields`) — the field content and quantum numbers:
  $\Phi_u\sim(\boldsymbol{6},\boldsymbol{1},\tfrac13)$, $\Phi_d\sim(\boldsymbol{6},\boldsymbol{1},\tfrac43)$, both with $L=-1$;
  $\Psi_u\sim(\boldsymbol{6},\boldsymbol{1},-\tfrac23)$, $\Psi_d\sim(\boldsymbol{6},\boldsymbol{1},\tfrac13)$, both with $L=0$.

- **Table IX** — the parent operator list for the invariant $\boldsymbol{3}\otimes\boldsymbol{6}\otimes\boldsymbol{8}$,
  with couplings $\kappa_I/\Lambda_\Psi$, $\kappa_I/\Lambda_\Psi^3$ and $\lambda^X_I/\Lambda_\Phi^2$.

- **Appendix A**, Eqs. \eqref{Kdef}, \eqref{Jdef} and \eqref{A18} — the Clebsch-Gordan coefficients
  $\bt{K}_s^{\ ij}$ and $\bt{J}^{\,s\,ia}$, and the identity that lets a public tool build $\bt{J}$
  from objects it already has:
  $\bt{J}^{\,s\,ia}=-\mathrm{i}\sqrt{2}\,\bt{L}^{ijk}[\bt{t}^{a}_{\boldsymbol{3}}]_j^{\ l}\,\bar{\bt{K}}{}^{s}_{\ lk}$,
  with $\sqrt{2}\,\bt{L}^{ijk}=\epsilon^{ijk}$.

- **Section III.A** — the benchmark values: $\kappa_u^I=\kappa_d^I=0.05$, $\kappa_{uB}^I=0.10$,
  $\lambda^{XI}_{u,d}=0.1\,\delta^{XI}$, and all cut-offs $=1\,\text{TeV}$.

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| $\Phi_u\sim(\boldsymbol{6},\boldsymbol{1},\tfrac13)$, $L=-1$ (Table X) | `S[100] Phiu`, sextet, no $SU(2)_L$ index, $Y=+\tfrac13$, $L=-1$ | agree | Complex scalar, electroweak singlet, so $Q=Y=+\tfrac13$. Same in both. |
| $\Phi_d\sim(\boldsymbol{6},\boldsymbol{1},\tfrac43)$, $L=-1$ (Table X) | `S[101] Phid`, sextet, $Y=+\tfrac43$, $L=-1$ | agree | Same representation, hypercharge and lepton number. |
| $\Psi_u\sim(\boldsymbol{6},\boldsymbol{1},-\tfrac23)$, $L=0$ (Table X) | `F[100] Psiu`, Dirac sextet, $Y=-\tfrac23$, $L$ not declared | agree | An undeclared lepton number is the same as $L=0$. |
| $\Psi_d\sim(\boldsymbol{6},\boldsymbol{1},\tfrac13)$, $L=0$ (Table X) | `F[101] Psid`, Dirac sextet, $Y=+\tfrac13$, $L$ not declared | agree | Same as above. |
| $\bar{\Psi}_q(\mathrm{i}\slashed{D}-m_{\Psi_q})\Psi_q$, $q=u$ (Eq. sFmodel, line 1) | `LPsiuFree` $=\mathrm{i}\bar\Psi_u\gamma^\mu(D_\mu\Psi_u)-M_{\Psi_u}\bar\Psi_u\Psi_u$ | agree | Same Dirac kinetic and mass term, sextet index contracted. |
| $\bar{\Psi}_q(\mathrm{i}\slashed{D}-m_{\Psi_q})\Psi_q$, $q=d$ (Eq. sFmodel, line 1) | `LPsidFree` | agree | Same. |
| $(D_\mu\Phi_q)^{\dagger}D^{\mu}\Phi_q-m^2_{\Phi_q}\Phi_q^{\dagger}\Phi_q$, $q=u$ (Eq. sSmodel, line 1) | `LPhiuFree` | agree | Same scalar kinetic and mass term. |
| $(D_\mu\Phi_q)^{\dagger}D^{\mu}\Phi_q-m^2_{\Phi_q}\Phi_q^{\dagger}\Phi_q$, $q=d$ (Eq. sSmodel, line 1) | `LPhidFree` | agree | Same. |
| Covariant derivative implied by $(\boldsymbol{6},\boldsymbol{1},Y)$ (Table X, Eq. sextet_numbers) | $D_\mu X=\partial_\mu X-\mathrm{i}g_sG^a_\mu T_6^a X-\mathrm{i}g_1Y_XB_\mu X$ | agree | $SU(3)_C$ in the sextet plus $U(1)_Y$, no $SU(2)_L$ part. This matches the singlet assignment. |
| Colour structure $\bt{J}^{\,s\,ia}$ (Table I, Eqs. Jdef, A18) | $\mathcal{K}^{a}_{\ is}=\varepsilon_{i i_2 i_3}(T^a)_{i_2i_4}\bar{K}^{s}_{\ i_4i_3}$ with an explicit $-\mathrm{i}$ in front of every term | agree | Eq. (A18) gives $\bt{J}^{\,s\,ia}=-\mathrm{i}\,\varepsilon^{ijk}[\bt{t}^a_{\boldsymbol{3}}]_j^{\ l}\bar{\bt{K}}{}^s_{\ lk}=-\mathrm{i}\,\mathcal{K}^{a}_{\ is}$. The $-\mathrm{i}$ in the file is exactly this factor, so $-\mathrm{i}\,\mathcal{K}=\bt{J}$. Index order and the position of $\bar{\bt{K}}$ also match. |
| $\dfrac{\kappa_u^{I}}{\Lambda_{\Psi_u}}\bt{J}^{\,s\,ia}(\overline{u^{c}_{R}}_{Ii}\sigma^{\mu\nu}\Psi_{us})G_{\mu\nu a}+\text{H.c.}$ (Eq. sFmodel, line 2, $q=u$) | `LPsiuG` $=-\mathrm{i}\dfrac{\kappa_u^{f}}{\Lambda_{\Psi_u}}\mathcal{K}^{a}_{\ is}\,\overline{u}_{f,i}P_R\sigma^{\mu\nu}\Psi_u^{s}G^{a}_{\mu\nu}+\text{h.c.}$ | **disagree** | The quark field is **not** charge-conjugated in the file. The paper needs $\overline{(u_R)^{c}}$, a $\boldsymbol{3}$ with $Y=+\tfrac23$; the file has $\bar{u}P_R=\overline{u_L}$, a $\bar{\boldsymbol{3}}$ with $Y=-\tfrac23$. Colour, hypercharge, baryon number and chirality all change. Prefactor, $\sigma^{\mu\nu}$, $G^a_{\mu\nu}$ and $1/\Lambda$ power are right. |
| $\dfrac{\kappa_d^{I}}{\Lambda_{\Psi_d}}\bt{J}^{\,s\,ia}(\overline{d^{c}_{R}}_{Ii}\sigma^{\mu\nu}\Psi_{ds})G_{\mu\nu a}+\text{H.c.}$ (Eq. sFmodel, line 2, $q=d$) | `LPsidG` with `CC[dqbar]`, $P_R\sigma^{\mu\nu}$, $G^a_{\mu\nu}$, $\kappa_d^f/\Lambda_{\Psi_d}$ | agree | $\overline{d^{c}}P_R\sigma^{\mu\nu}\Psi_d=\overline{(d_R)^{c}}\sigma^{\mu\nu}\Psi_{d,R}$, which is the paper's bilinear. Dimension 5, so $1/\Lambda^{1}$ is right. |
| $\dfrac{\kappa_{uB}^{I}}{\Lambda^{3}_{\Psi_uB}}\bt{J}^{\,s\,ia}(\overline{u^{c}_{R}}_{Ii}\Psi_{us})B^{\mu\nu}G_{\mu\nu a}+\text{H.c.}$ (Eq. sFmodel, line 3, $q=u$) | `LPsiuB` with `CC[uqbar]`, no $\sigma^{\mu\nu}$, $B_{\mu\nu}G^{a\,\mu\nu}$, $\kappa_u^{B,f}/\Lambda^{3}_{\Psi_uB}$ | agree | Scalar bilinear, the two field strengths contract with each other, separate cut-off symbol, $1/\Lambda^{3}$ for a dimension-7 operator. All match. |
| $\dfrac{\kappa_{dB}^{I}}{\Lambda^{3}_{\Psi_dB}}\bt{J}^{\,s\,ia}(\overline{d^{c}_{R}}_{Ii}\Psi_{ds})B^{\mu\nu}G_{\mu\nu a}+\text{H.c.}$ (Eq. sFmodel, line 3, $q=d$) | `LPsidB` | agree | Same as above with the down-type quark. |
| $\dfrac{\lambda_u^{XI}}{\Lambda^{2}_{\Phi_u}}\bt{J}^{\,s\,ia}\Phi_{us}(\overline{u^{c}_{R}}_{Ii}\sigma^{\mu\nu}\ell_{RX})G_{\mu\nu a}+\text{H.c.}$ (Eq. sSmodel, line 2, $q=u$) | `LPhiuG` with `CC[uqbar]`, $\sigma^{\mu\nu}P_R\ell_x$, $\Phi_u^{s}$, $G^{a}_{\mu\nu}$, $\lambda_u^{xf}/\Lambda^{2}_{\Phi_u}$ | agree | Right-handed up-type quark with right-handed charged lepton, two generation indices, $1/\Lambda^{2}$ for a dimension-6 operator. All match. |
| $\dfrac{\lambda_d^{XI}}{\Lambda^{2}_{\Phi_d}}\bt{J}^{\,s\,ia}\Phi_{ds}(\overline{d^{c}_{R}}_{Ii}\sigma^{\mu\nu}\ell_{RX})G_{\mu\nu a}+\text{H.c.}$ (Eq. sSmodel, line 2, $q=d$) | `LPhidG` | agree | Same as above with the down-type quark. |
| Hermitian conjugate on every interaction (Eqs. sFmodel, sSmodel: "+ H.c.") | `HC[tmp]` on every interaction term | agree | Same. |
| $\kappa_q^{I}$ carries one quark generation index; $\lambda_q^{XI}$ carries lepton $\times$ quark indices (Eqs. sFmodel, sSmodel, Table IX footnote) | `kapu`, `kapd`, `kapuB`, `kapdB` with one index; `lamu`, `lamd` with two | agree | Index structure of the coupling matrices matches. |
| Six separate cut-offs $\Lambda_{\Psi_u},\Lambda_{\Psi_d},\Lambda_{\Psi_uB},\Lambda_{\Psi_dB},\Lambda_{\Phi_u},\Lambda_{\Phi_d}$ (Eqs. sFmodel, sSmodel) | `LamPsu`, `LamPsd`, `LamPsuB`, `LamPsdB`, `LamPhu`, `LamPhd`, all $1000$ GeV | agree | The paper keeps $\Lambda_{\Psi_q}$ and $\Lambda_{\Psi_qB}$ distinct, and the file does too. Benchmark value $1$ TeV matches Section III.A. |
| Benchmark $\kappa_u^I=\kappa_d^I=0.05$, $\kappa_{uB}^I=0.10$ for $I\in\{1,2\}$ (Section III.A) | $0.05$ and $0.10$ for $f=1,2,3$ | agree | Values match. The generation range differs in the text only; the paper's own branching-fraction footnote ($\text{BF}(\Psi_u\to\bar{t}g)\approx0.21$) needs a non-zero third-generation coupling, so the file is the consistent reading. |
| Benchmark $\lambda^{XI}_{u,d}=0.1\,\delta^{XI}$ (Section III.A) | $0.1\,\delta_{xf}$ | agree | Same value and same diagonal texture. |
| No Yukawa term, no Higgs portal, no scalar potential beyond the mass term (Eqs. sFmodel, sSmodel) | "No quartic or trilinear scalar potential terms ... no $\Phi$-Higgs portal" | agree | The paper's simplified model has no such term either. |
| $(q\Psi)|H|^2G$ dimension-7 operator (Table IX, row 3) | — | missing-in-reconstruction | The paper lists this operator in the catalog but leaves it out of Eq. (sFmodel). Its absence from the file is correct for the simplified model. |
| — | `MPHU`/`MPHD`/`MPSU`/`MPSD` $=1000$ GeV, widths $=10$ GeV, PDG codes 9000001/9000002/9000011/9000012 | extra-in-reconstruction | Implementation defaults. The paper scans the sextet mass and quotes no width or PDG code. |
| — | $B(\Phi_{u,d})=B(\Psi_d)=-\tfrac13$ | extra-in-reconstruction | The reconstruction infers baryon number from the interactions. The paper gives only $L$ and the gauge quantum numbers. The inferred values are consistent with the paper's operators. |

## 3. Disagreements

1. **`LPsiuG` uses a quark that is not charge-conjugated.** *Severity: substantive.*
   A human should check whether the implementation file really contains `uqbar[...]` instead of
   `CC[uqbar][...]` in the up-type chromo-dipole term, because the paper's Eq. (sFmodel) requires
   $\overline{q^{c}_{R}}$ and the term as reported breaks colour, hypercharge, baryon number and
   chirality all at once.

2. **Benchmark generation range: the paper writes $I\in\{1,2\}$, the file sets all three generations.**
   *Severity: cosmetic.*
   A human should confirm which reading was used for the published cross sections, since the paper's
   branching-fraction footnote already implies a non-zero third-generation coupling.

3. **Default masses, widths and PDG codes are not in the paper.** *Severity: cosmetic.*
   A human should confirm that the $1000$ GeV masses and $10$ GeV widths are only placeholder inputs
   for a mass scan, not a physics claim.

4. **Baryon numbers are stated in the reconstruction but not declared in the paper.**
   *Severity: cosmetic.*
   A human should confirm that $B$ is left undeclared on purpose, because the paper tracks only $L$
   and the gauge quantum numbers.

## 4. Overall assessment

The reconstruction and the paper describe the same model almost everywhere. The field content,
the sextet representation, the four hypercharges, the lepton numbers, the electroweak-singlet
assignment, the covariant derivative, the three families of higher-dimensional operators, the
chirality of every quark and lepton, the Lorentz structures ($\sigma^{\mu\nu}G_{\mu\nu}$,
$B_{\mu\nu}G^{\mu\nu}$, $\sigma^{\mu\nu}$ with a right-handed lepton), the powers of the cut-off
scales, the index structure of the coupling matrices and the benchmark numbers all line up with
Eqs. (sFmodel) and (sSmodel) and with Table X. The colour tensor also lines up: the explicit
$-\mathrm{i}\,\varepsilon\,T^{a}\bar{K}^{s}$ written in the file is the paper's
$\bt{J}^{\,s\,ia}$, by the identity in Eq. (A18) of Appendix A, so the factor $-\mathrm{i}$ is
required and not spurious. One term does not line up. The up-type chromo-dipole term `LPsiuG`
reportedly uses the plain quark field where the paper and its three sibling terms use the
charge-conjugated quark. That one change moves the quark from the $\boldsymbol{3}$ to the
$\bar{\boldsymbol{3}}$, breaks electric charge by $4/3$, flips the quark chirality from right to
left, and makes the colour contraction with $\varepsilon_{ijk}$ inconsistent. The reconstruction
itself flags this in its Section 5 and proposes the corrected term, which is identical to the
paper. So the question for the human reviewer is narrow: is this a defect in the implementation
file, or a defect in the reconstruction's reading of that file? Everything else in the document
is an accurate account of the paper's model.
