# Cross-check: `reconstruction.md` against the paper

RUN-TAG: XM-CROSS-GeneralU1__drop_eps

**Paper.** A. Das, P. S. B. Dev, Y. Hosotani, S. Mandal, *Probing the minimal
\(U(1)_X\) model at future electron-positron colliders via fermion
pair-production channels* (preprint OU-HET-1085).

**Reconstruction.** An independent read-out of a FeynRules file
(`sanitized.fr`) that I cannot see.

---

## 1. Where the paper defines the model

All model content sits in Sec. II ("The \(U(1)_X\) Model"), lines 89-215 of
`paper.tex`:

| item | location |
|---|---|
| Gauge group \(SU(3)_C\otimes SU(2)_L\otimes U(1)_Y\otimes U(1)_X\) | Sec. II, first paragraph after Table~\ref{tab1} |
| Field content and \(U(1)_X\) charges | Table~\ref{tab1} (`tab1`); numeric values in Table~\ref{tab2} (`tab2`) |
| Yukawa Lagrangian (5 terms) | Eq.~\ref{LYk} (`LYk`) |
| Scalar potential | unnumbered `align` after Eq.~\ref{LYk} ("The renormalizable Higgs potential…") |
| Vacuum expectation values | unnumbered `align`, \(\langle H\rangle\), \(\langle\Phi\rangle\) |
| \(Z'\) mass | unnumbered `eqnarray` after the VEVs |
| Dirac and Majorana masses | text after the \(Z'\) mass: \(m_{N_\alpha}=\frac{Y_N^\alpha}{\sqrt2}v_\Phi\), \(m_D^{\alpha\beta}=\frac{Y_\nu^{\alpha\beta}}{\sqrt2}v\) |
| Seesaw mass matrix | Eq.~\ref{num} (`num`) |
| \(Z'\) fermion currents | Eq.~\ref{Lag1} (`Lag1`) |
| \(Z'\) partial widths | Eqs.~\ref{2f}, \ref{2v}, \ref{2N} (`2f`, `2v`, `2N`) |
| Benchmarks \(M_{Z'}=7.5\) TeV, \(g'=0.4\), \(x_\Phi=1\) | Sec. II B, text after Fig.~\ref{gp-MZp-1}; Table~\ref{tab3} |

Sections III to VI are collider observables only. They add no new Lagrangian
term. The paper states (Sec. II B) that it takes the FeynRules file of the
model from Ref.~\cite{U1X}, so the file under test is the paper's own file.

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Gauge group \(SU(3)_C\otimes SU(2)_L\otimes U(1)_Y\otimes U(1)_X\) (Sec. II) | same, §0 | **agree** | Same four factors. No kinetic mixing in either document. |
| Field content: \(q_L,u_R,d_R,\ell_L,e_R,N_R\) (3 generations), \(H\), \(\Phi\) (Table 1) | same, §0 and §2; \(N\to\) `F[100]`, \(\Phi\to H_X\) real mode, \(H\to\) `Phi` | **agree** | Three RHN generations, one SM-singlet complex scalar. Colour and isospin reps match line by line. |
| \(x_{q_L}=\frac16 x_H+\frac13 x_\Phi\) (Table 1) | `xqL` \(=x_H/6+x_\Phi/3\) | **agree** | Numeric value \(2/3\) at \(x_H=2\). See §4, item 7: Table 2 of the paper prints \(1/3\) here, which contradicts its own formula. The reconstruction follows the formula. |
| \(x_{u_R}=\frac23 x_H+\frac13 x_\Phi\) (Table 1) | `xuR` | **agree** | |
| \(x_{d_R}=-\frac13 x_H+\frac13 x_\Phi\) (Table 1) | `xdR` | **agree** | |
| \(x_{\ell_L}=-\frac12 x_H-x_\Phi\) (Table 1) | `xlL` | **agree** | |
| \(x_{e_R}=-x_H-x_\Phi\) (Table 1) | `xeR` | **agree** | |
| \(x_{N_R}=-x_\Phi\) (Table 1) | `xnR` | **agree** | |
| \(x_H^{\rm doublet}=-\frac{x_H}{2}\) (Table 1) | `xHd` \(=+x_H/2\) | **agree (convention)** | The paper's \(H\) has its VEV in the **upper** component and couples as \(\overline{q_L}Hu_R\). The file's `Phi` is the standard FeynRules doublet with the VEV in the lower component, so it is the conjugate of the paper's \(H\). The sign flip is exactly that conjugation. Both sets satisfy charge balance in every Yukawa term. \(M_{Z'}\) uses only \(x_{H_d}^2\), so no numeric effect. |
| \(x_\Phi^{\rm singlet}=2x_\Phi\) (Table 1) | `xSc` \(=2x_\Phi\) | **agree** | |
| Charge is a linear combination \(x_HY+x_\Phi(B-L)\); generation independent; anomaly free with 3 RHNs (Sec. II text) | §0 text, same statement | **agree** | One wording slip; see §4, item 5. |
| \(\mathcal{L}^q=-g'(\overline q\gamma^\mu x_{q_L}P_Lq+\overline q\gamma^\mu x_{q_R}P_Rq)Z'_\mu-g'(\overline\ell\gamma^\mu x_{\ell_L}P_L\ell+\overline e\gamma^\mu x_{e_R}P_Re)Z'_\mu\) (Eq.~`Lag1`) | `LZpF`, §1.2 | **agree** | Same overall \(-g'\), same chirality projectors, same charges, flavour diagonal and family universal. The file expands the \(SU(2)_L\) doublets and then applies CKM unitarity, so no flavour-changing neutral current appears. This matches the paper's family-universal assumption. |
| \(Z'\) coupling to \(N_R\): \(g_R^N[g',x_\Phi]\) implied by Eq.~`2N` | \(x_{N_R}\bar N\gamma^\mu P_RN\) inside `LZpF`, §1.2 | **agree** | The paper writes no explicit \(Z'NN\) operator, but Eq.~`2N` requires it with charge \(-x_\Phi\). The file has it. The reconstruction's rewrite as \(\frac{x_{N_R}}{2}\bar N\gamma^\mu\gamma^5N\) is correct for a Majorana field. |
| \(Z'\) gauge kinetic term (implied, never written) | \(-\frac14 Z'_{\mu\nu}Z'^{\mu\nu}\), §1.1 | **agree** | Abelian field strength, no self-coupling. |
| \(M_{Z'}=g'\sqrt{4v_\Phi^2+\frac14x_H^2v^2}\) | `MZp` \(=g_X\sqrt{x_S^2v_X^2+x_{H_d}^2v^2}\), §3 | **agree** | With \(x_S=2x_\Phi=2\) and \(x_{H_d}=x_H/2\) the two expressions are identical. At \(g'=0.4\), \(v_X=9375\) GeV this gives 7.50 TeV, the paper's benchmark. |
| Origin of \(M_{Z'}\): \(|D_\mu\Phi|^2+|D_\mu H|^2\) after symmetry breaking | Proca mass \(+\frac12M_{Z'}^2Z'_\mu Z'^\mu\) put in by hand, §1.1 | **agree (convention)** | The file inserts the value the Higgs mechanism gives. The \(v^2\) piece that would produce \(Z\)-\(Z'\) mass mixing is therefore kept in the mass but not written as a mixing operator. The paper also uses unmixed SM \(Z\) couplings everywhere (Eqs.~`prop-1`, `prop-2`), so both work in the zero-mixing limit. |
| \(-Y_u\overline{q_L}Hu_R-Y_d\overline{q_L}\tilde Hd_R-Y_e\overline{\ell_L}\tilde He_R\) (Eq.~`LYk`, terms 1-3) | inherited from `LSM` in `LTotal`, §1 | **agree** | The file adds the whole SM Lagrangian, so these three terms are present with their SM values. The reconstruction does not re-derive them. Their \(U(1)_X\) charge balance is not enforced by the file, because the \(U(1)_X\) charges are not declared as `QuantumNumbers` (§2 of the reconstruction). |
| \(-Y_N^\alpha\Phi\,\overline{N_R^{\alpha c}}N_R^\alpha+{\rm H.c.}\) (Eq.~`LYk`, term 5) | `LNYuk` \(=-\frac{1}{2\sqrt2}H_X\bar N_i(y_N)_{ij}N_j\), §1.7, plus `LNXKin` mass \(-\frac12\bar N m_N N\), §1.3 | **agree** | The file splits the single paper term into its VEV part (the Majorana mass) and its \(H_X\) part. |
| \(m_{N_\alpha}=\frac{Y_N^\alpha}{\sqrt2}v_\Phi\) (Sec. II text) | `yN` \(={\rm diag}(\sqrt2M_{N_i}/v_X)\), §3 | **agree** | Inverting the file's relation gives \(M_{N_i}=y_{N,i}v_X/\sqrt2\), which is the paper's formula. Diagonal and generation-wise, as in the paper (single index \(\alpha\)). |
| Majorana \(N\) kinetic term (implied) | \(\frac{i}{2}\bar N\gamma^\mu\partial_\mu N\), §1.3 | **agree** | Standard Majorana \(1/2\) normalisation. |
| \(-Y_\nu^{\alpha\beta}\overline{\ell_L^\alpha}HN_R^\beta+{\rm H.c.}\) (Eq.~`LYk`, term 4) | `LNuYuk` \(=-(y_\nu)_{ij}\bar L_L^{a,i}P_RN^j(\Phi^\dagger)_a+{\rm h.c.}\), §1.8 | **disagree** | The doublet indices are contracted **directly**, with no \(\epsilon_{ab}\). In the FeynRules convention the invariant form needs \(\epsilon_{ab}\bar L_L^{a}N_R(\Phi^\dagger)_b\), i.e. \(\tilde\Phi=i\sigma^2\Phi^*\). As written the term is not \(SU(2)_L\) invariant and it couples \(N\) to the **charged** leptons. The paper's term couples \(N\) to the neutrinos. See §4, item 1. |
| \(m_D^{\alpha\beta}=\frac{Y_\nu^{\alpha\beta}}{\sqrt2}v\) (Sec. II text) | absent; the file gives \(\frac{y_\nu}{\sqrt2}(v+h)\,\bar e_LP_RN\) instead, §1.8 | **missing-in-reconstruction** | No neutrino Dirac mass is generated by the file as reconstructed. Direct consequence of the row above. |
| \(\mathcal{M}_\nu=\begin{pmatrix}0&m_D\\m_D^T&m_N\end{pmatrix}\), \(m_\nu\simeq-m_Dm_N^{-1}m_D^T\) (Eq.~`num`) | not realised; the reconstruction says so explicitly, §1.8 and §4 | **missing-in-reconstruction** | The seesaw is a derived result, not a Lagrangian term, but the paper's stated motivation for \(N_R\) does not follow from the file. |
| \(V=-m_h^2(H^\dagger H)+\lambda(H^\dagger H)^2\) | inherited from `LSM` | **agree** | |
| \(m_\Phi^2(\Phi^\dagger\Phi)+\lambda_\Phi(\Phi^\dagger\Phi)^2\) | \(-\lambda_\Phi v_XH_X^3-\frac{\lambda_\Phi}{4}H_X^4\) in `LPotX` (§1.9) plus \(-\frac12M_{H_X}^2H_X^2\) in `LHXKin` (§1.4), with \(M_{H_X}^2=2\lambda_\Phi v_X^2\) | **agree** | The file expands the singlet potential around \(v_X\) and puts the quadratic part in the kinetic block. \(M_{H_X}^2=2\lambda_\Phi v_\Phi^2\) is the correct radial-mode mass for \(\lambda_\Phi(|\Phi|^2-v_\Phi^2/2)^2\). The paper prints \(+m_\Phi^2(\Phi^\dagger\Phi)\); a VEV needs \(m_\Phi^2<0\), so the sign as printed is loose. Both agree once \(m_\Phi^2=-\lambda_\Phi v_\Phi^2\). |
| \(\lambda'(H^\dagger H)(\Phi^\dagger\Phi)\) | \(-\frac{\lambda'}{2}H_X^2(\Phi^\dagger)_a\Phi^a\) only, §1.9 | **disagree** | The linear-in-\(H_X\) part \(\lambda'v_XH_X|\Phi|^2\) is dropped. That is the only source of tree-level \(h\)-\(H_X\) mixing. The paper works "in the limit of small \(\lambda'\)" where this mixing "is negligible", so the omission is aligned with the paper's own approximation, but the paper's potential as written does contain the piece. See §4, item 3. |
| \(|D_\mu\Phi|^2\) contact terms \(Z'Z'\phi\), \(Z'Z'\phi\phi\) (implied by the potential and the covariant derivative) | `LZpHX` \(=g_X^2x_S^2(v_XH_X+\frac12H_X^2)Z'_\mu Z'^\mu\), §1.6 | **agree** | Correct remainder of \(|D_\mu\Phi_X|^2\) with \(\Phi_X=(v_X+H_X)/\sqrt2\) and charge \(x_S\). The paper never writes it, but it follows from the paper's gauge structure. |
| Real scalar \(\phi\) from \(\langle\Phi\rangle=(v_\Phi+\phi)/\sqrt2\) | \(H_X\), `S[100]`, §1.4 and §2 | **agree** | The paper introduces \(\phi\) and then never uses it. The file gives it \(\lambda_\Phi=0.1\), \(M_{H_X}=4.19\) TeV and a width. Those numbers are file-side choices, not paper values. |
| \(\Gamma(Z'\to f\bar f)=N_c\frac{M_{Z'}}{24\pi}(g_L^{f2}+g_R^{f2})\), \(\Gamma(Z'\to\nu\bar\nu)\) (Eqs.~`2f`, `2v`) | `WZp = 1353.` GeV, §2 | **agree** | I checked the number. Summing \(N_c(x_L^2+x_R^2)\) over 3 generations at \(x_H=2,x_\Phi=1\) gives 85. Then \(\Gamma=\frac{7500}{24\pi}(0.4)^2\times85=1353\) GeV. This reproduces the paper's formulas at the paper's benchmark, and it confirms \(x_{q_L}=2/3\) (not the \(1/3\) printed in Table 2). |
| "\(Z'\to NN\) is kinematically disallowed because \(m_N>M_{Z'}\)" (Sec. II A) | \(M_{N_i}=8000\) GeV against \(M_{Z'}=7.50\) TeV, §3 | **agree** | The file's benchmark respects the paper's assumption. The width 1353 GeV also excludes the \(NN\) channel, as the paper does. One prose slip in the reconstruction; see §4, item 6. |
| Benchmarks \(x_\Phi=1\), \(g'=0.4\), \(M_{Z'}=7.5\) TeV, \(x_H\in\{-2,-1,-0.5,0,0.5,1,2\}\) (Sec. II B, Tables 2-3) | `xPhi = 1.0`, `gX = 0.4`, `xH = 2.0`, \(v_X=9375\) GeV, §3 | **agree** | \(v_X=M_{Z'}/(2g')=9375\) GeV reproduces the paper's \(M_{Z'}\simeq2g'v_\Phi\). \(x_H=2\) is one of the paper's seven benchmark values. |
| — (nothing in the paper) | \(y_\nu=10^{-6}\delta_{ij}\), §3 | **extra-in-reconstruction** | The paper sets no \(Y_\nu\) benchmark; it assumes the RHNs decouple from the collider analysis. Harmless, but it is a file-side choice. |
| — (nothing in the paper) | PDG codes, widths `WHX`, `WNXi`, `NP` interaction order, the auxiliary field `NR` (`F[110]`) | **extra-in-reconstruction** | Pure implementation bookkeeping. No physics content to compare. |
| — (nothing in the paper) | statement that no kinetic-mixing term \(-\frac{\epsilon}{2}\hat B_{\mu\nu}\hat Z'^{\mu\nu}\) is present, §0 | **agree** | The paper defines no kinetic mixing either. The reconstruction flags this as a "structural remark", but against this paper it is **not** a defect. |

---

## 3. Quantitative checks I could close

These are consistency tests between the file's numbers (as reported) and the
paper's formulas. All of them pass.

| quantity | paper formula | file numbers | result |
|---|---|---|---|
| \(M_{Z'}\) | \(g'\sqrt{4v_\Phi^2+\frac14x_H^2v^2}\) | \(g_X=0.4\), \(v_X=9375\), \(x_H=2\), \(v=246\) | 7.50 TeV = the paper's benchmark |
| \(v_\Phi\) | \(M_{Z'}\simeq2g'v_\Phi\) | 9375 GeV | consistent |
| \(\Gamma_{Z'}\) | Eqs.~`2f`+`2v`, \(NN\) closed | `WZp = 1353.` GeV | 1353 GeV, exact |
| \(M_{H_X}\) | \(2\lambda_\Phi v_\Phi^2\) from the potential | \(\lambda_\Phi=0.1\), \(v_X=9375\) | 4.19 TeV, as the reconstruction states |
| \(y_N\) | \(m_N=\frac{Y_N}{\sqrt2}v_\Phi\) | \(M_N=8000\), \(v_X=9375\) | \(y_N=1.21\), as the reconstruction states |
| \(m_D\), \(m_\nu\) | \(m_D=\frac{Y_\nu}{\sqrt2}v\), \(m_\nu\simeq m_D^2/m_N\) | \(y_\nu=10^{-6}\), \(M_N=8\) TeV | \(m_D=1.7\times10^{-4}\) GeV, \(m_\nu\approx4\) meV — the right scale, but only for the **corrected** Yukawa term |

---

## 4. Disagreements, with severity

**1. The neutrino Dirac Yukawa has no \(\epsilon_{ab}\). — substantive.**
The paper's Eq.~`LYk` term 4 is \(-Y_\nu\overline{\ell_L}HN_R\), and the paper
uses it to build \(m_D=\frac{Y_\nu}{\sqrt2}v\) and the seesaw of Eq.~`num`. The
file, as reconstructed, contracts \(\bar L_L^{\,a}\) with \((\Phi^\dagger)_a\)
directly. Both carry the \(\bar{\mathbf 2}\) of \(SU(2)_L\), so the product is
not invariant, and in unitary gauge it produces
\(-\frac{y_\nu}{\sqrt2}(v+h)\bar e_LP_RN\): a charged-lepton-to-\(N\) mass, and
no neutrino Dirac mass. A human should open `LNuYuk` in the file and check
whether `Eps[ii,jj]` is present with `Phibar[jj]`. If it is absent, the file
does not implement the paper's Eq.~`LYk`.

**2. The \(U(1)_X\) charge of the Higgs doublet has the opposite sign. — convention.**
The paper's Table 1 gives \(-x_H/2\); the file gives \(+x_H/2\). The paper's
\(H\) takes its VEV in the upper component and couples as \(\overline{q_L}Hu_R\),
so it is the conjugate of the FeynRules doublet. A human should confirm that
the file's `Phi` is the standard SM doublet with the VEV in the lower
component; if so, \(+x_H/2\) is correct and nothing needs changing.

**3. The \(\lambda'v_XH_X|\Phi|^2\) portal term is dropped. — convention.**
The paper's potential contains \(\lambda'(H^\dagger H)(\Phi^\dagger\Phi)\) in
full; the file keeps only the \(H_X^2|\Phi|^2\) piece, so there is no tree-level
\(h\)-\(H_X\) mixing. The paper works in the small-\(\lambda'\) limit where that
mixing is negligible, so the two are compatible in intent. A human should
decide whether the file is meant to be the exact potential or the
zero-mixing limit of it, and record that choice.

**4. The \(Z'\) mass is a Proca term, not a Higgs-mechanism output, and no \(Z\)-\(Z'\) mixing is written. — convention.**
The file inserts \(M_{Z'}\) by hand with the value
\(g_X\sqrt{x_S^2v_X^2+x_{H_d}^2v^2}\), which equals the paper's expression. The
\(x_{H_d}^2v^2\) piece signals \(Z\)-\(Z'\) mass mixing of order \(v^2/v_\Phi^2\),
which neither document writes out. A human should confirm that the intended
use (\(e^+e^-\to f\bar f\) at \(\sqrt s\ll M_{Z'}\), or resonance shapes) does
not need that mixing.

**5. "\(x_\Phi=0\) is pure hypercharge (\(U(1)_R\)-like)" is a mislabel. — cosmetic.**
The paper's Table 2 caption says \(x_H=-2\) is the \(U(1)_R\) case and \(x_H=0\)
is \(B-L\). The reconstruction gets \(x_H=0\leftrightarrow B-L\) right, but
attaches "\(U(1)_R\)-like" to \(x_\Phi=0\), which is pure \(U(1)_Y\), a different
direction. A human should simply correct the wording; no file content is
affected.

**6. The reconstruction's summary says the \(Z'\) decays to \(NN\). — cosmetic.**
The vertex exists, but at the file's own benchmark \(M_N=8\) TeV \(>M_{Z'}=7.5\)
TeV the channel is closed, exactly as the paper assumes, and the file's own
`WZp` value excludes it. A human should read §4 of the reconstruction as
"the vertex is present", not "the channel is open".

**7. The paper's Table 2 prints \(x_{q_L}=1/3\) at \(x_H=2\). — cosmetic, paper-side.**
The defining formula in the same table header gives \(2/3\). The file uses
\(2/3\), and the file's width `WZp = 1353.` GeV only comes out right with
\(2/3\). A human should treat the Table 2 entry as a typo in the paper, not as
a defect in the file.

**8. \(y_\nu=10^{-6}\) is a file-side benchmark with no counterpart in the paper. — cosmetic.**
The paper fixes no \(Y_\nu\) value. A human should confirm the intended
neutrino-mass target before quoting this number as the paper's.

---

## 5. Overall assessment

The reconstruction matches the paper closely on everything that the paper
actually defines. The gauge group, the full field content, all eight
\(U(1)_X\) charges in their \(x_HY+x_\Phi(B-L)\) form, the \(Z'\) neutral current
with its overall \(-g'\) and its left and right projectors, the \(Z'\) mass
formula including the doublet contribution, the Majorana mass and its tie to
\(\langle\Phi\rangle\), and the singlet scalar potential all line up
term by term. Three independent numeric checks close exactly on the paper's
own benchmarks: \(M_{Z'}=7.5\) TeV from \(g'=0.4\) and \(v_\Phi=9375\) GeV, the
total width 1353 GeV from the paper's Eqs.~`2f` and `2v` with the \(NN\)
channel closed, and \(M_N=8\) TeV \(>M_{Z'}\) as Sec. II A assumes. The width
check also settles a small numeric typo in the paper's own Table 2. Against
this, one term does not match the paper: the Dirac Yukawa
\(-Y_\nu\overline{\ell_L}HN_R\) of Eq.~`LYk` appears in the file without the
\(\epsilon_{ab}\) that the FeynRules doublet convention requires, so the
reconstructed operator is not \(SU(2)_L\) invariant and couples \(N\) to charged
leptons instead of neutrinos, removing the neutrino Dirac mass and the seesaw
of Eq.~`num`. The reconstruction identifies this itself, states the correct
invariant form, and shows that the file's own \(y_\nu\) and \(M_N\) values only
make sense with the corrected term, which is good evidence that the intent
matches the paper and the written term does not. The remaining differences
are a doublet-charge sign that follows from \(H\leftrightarrow\tilde H\), a
dropped \(h\)-\(H_X\) portal piece that matches the paper's small-\(\lambda'\)
limit, a hand-inserted \(Z'\) mass with no \(Z\)-\(Z'\) mixing, and two wording
slips. The human reviewer should focus on the \(\epsilon_{ab}\) question first,
since it alone changes physics, and treat the rest as convention or prose.
