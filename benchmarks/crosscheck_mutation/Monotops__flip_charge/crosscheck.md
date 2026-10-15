# Cross-check: `reconstruction.md` against "Monotops at the LHC"

Paper: J. Andrea, B. Fuks, F. Maltoni, *Monotops at the LHC* (CP3-11-21; IPHC-PHENO-11-03).

## 1. Where the paper defines the model

* **Section "Effective theory for monotops"** names the field content: $\phi$, $\chi$ and $V$ are the
  scalar, fermionic and vector missing-energy states; $\varphi$ and $X$ are scalar and vector fields
  "lying in the fundamental representation of $SU(3)_c$" that give resonant monotop production;
  $\tilde\varphi$ is a second heavy scalar added for the four-fermion interactions.
* **Eq. (1)** (the `\label{eq:lag}` block, the only numbered equation in the paper) gives the full
  effective Lagrangian in terms of **mass eigenstates**, with "+ h.c." written once at the end of the block.
* **The text after Eq. (1)** states the role of each coupling matrix and the symmetry rule: because of
  $\epsilon^{ijk}$, "identical quark couplings to the scalar field $\varphi$ vanish and so do their axial
  couplings to the vector field $X$".
* **Section "Model-independent searches"** fixes the benchmark numbers: all $b$ couplings zero,
  $(a^0_{FC})_{13}=(a^0_{FC})_{31}=(a^1_{FC})_{13}=(a^1_{FC})_{31}=(a^q_{SR})_{12}=-(a^q_{SR})_{21}=(a^{1/2}_{SR})_3=(a^q_{VR})_{11}=(a^{1/2}_{VR})_3=0.1$;
  for the four-fermion limit $(\tilde a^q_{SR})_{\{1,2\}3}=(\tilde a^{1/2}_{SR})_{\{1,2\}}=0.1$ with
  $M_\varphi=M_{\tilde\varphi}=3$ TeV; resonance mass 500 GeV; $m_\chi=50$ (300) GeV for the scalar
  (vector) resonant case; a 300 GeV scalar or a 50 GeV vector invisible state for the flavour-changing case.
* **The paper never writes a number for the electric charge** of $\varphi$, $\tilde\varphi$ or $X$, and it
  never writes the kinetic terms of the new fields. Both follow from Eq. (1) and from the stated colour
  representation. The charges follow from electric-charge conservation of each term in Eq. (1), with
  $Q_u=+2/3$, $Q_d=-1/3$, $Q_\chi=0$, and $Q(\overline{d^c})=-1/3$:
  * $\epsilon^{ijk}\varphi_i\,\bar d^c_j\,d_k$ and $\varphi_i\,\bar u^i\chi$ both need $Q_\varphi=+2/3$;
  * $\epsilon^{ijk}\tilde\varphi_i\,\bar d^c_j\,u_k$ and $\tilde\varphi_i\,\bar d^i\chi$ both need $Q_{\tilde\varphi}=-1/3$;
  * $\epsilon^{ijk}X_{\mu,i}\,\bar d^c_j\gamma^\mu d_k$ and $X_{\mu,i}\,\bar u^i\gamma^\mu\chi$ both need $Q_X=+2/3$.
  Section "Beyond the Standard Model Explorations" confirms this independently: it identifies $\varphi$ with
  an $R$-parity-violating up squark, $\bar d\bar s\to\tilde u_i\to t\tilde\chi^0_1$, and $X$ with a vector
  leptoquark, $\bar d\bar d\to V\to t\bar\nu$. Both initial states carry $+2/3$.

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| $\lag_{SM}$ (Eq. (1), first line) | absent from `LTotal` (§1) | missing-in-reconstruction | `LTotal` holds only the new fields and the new vertices. A FeynRules file normally loads the SM part separately, so this is probably outside the reconstructed file. |
| $\phi\,\bar u[a^0_{FC}+b^0_{FC}\gamma_5]u$ (Eq. (1)) | `Lphiu`: $\phi[a^0_{ij}\bar u^a_i u_{ja}+b^0_{ij}\bar u^a_i\gamma^5 u_{ja}]$ | agree | Same field content, same colour-diagonal contraction, same scalar plus pseudo-scalar structure, same flavour-matrix index order. See the h.c. row below. |
| $V_\mu\,\bar u[a^1_{FC}\gamma^\mu+b^1_{FC}\gamma^\mu\gamma_5]u$ (Eq. (1)) | `LVu` | agree | Same vector plus axial-vector structure, colour-diagonal, flavour matrices. |
| $\epsilon^{ijk}\varphi_i\,\bar d^c_j[a^q_{SR}+b^q_{SR}\gamma_5]d_k$ (Eq. (1)) | `LvphiDiquark` | agree | Charge conjugation, $\epsilon$ colour contraction and $\{1,\gamma^5\}$ structure all match. The reconstruction derives that $a^q$ and $b^q$ are antisymmetric in flavour; this reproduces the paper's statement that identical-quark couplings to $\varphi$ vanish. |
| $\varphi_i\,\bar u^i[a^{1/2}_{SR}+b^{1/2}_{SR}\gamma_5]\chi$ (Eq. (1)) | `LvphiChi` | agree | Up-type quark, one flavour index, colour index contracted with $\varphi$. Matches the paper's description of $a^{1/2}_{SR}$. |
| $\epsilon^{ijk}\tilde\varphi_i\,\bar d^c_j[\tilde a^q_{SR}+\tilde b^q_{SR}\gamma_5]u_k$ (Eq. (1)) | `LvphitDiquark` | agree | Down-type plus up-type pair, so no flavour (anti)symmetry rule applies. The reconstruction says the same. |
| $\tilde\varphi_i\,\bar d^i[\tilde a^{1/2}_{SR}+\tilde b^{1/2}_{SR}\gamma_5]\chi$ (Eq. (1)) | `LvphitChi` | agree | Down-type quark with $\chi$, as in the paper. |
| $\epsilon^{ijk}X_{\mu,i}\,\bar d^c_j[a^q_{VR}\gamma^\mu+b^q_{VR}\gamma^\mu\gamma_5]d_k$ (Eq. (1)) | `LXDiquark` | agree | The reconstruction derives $a^{qV}$ symmetric and $b^{qV}$ antisymmetric. This reproduces the paper's statement that axial couplings of identical quarks to $X$ vanish. |
| $X_{\mu,i}\,\bar u^i[a^{1/2}_{VR}\gamma^\mu+b^{1/2}_{VR}\gamma^\mu\gamma_5]\chi$ (Eq. (1)) | `LXChi` | agree | Same structure. |
| "+ h.c." at the end of Eq. (1) | explicit `HC` on the six coloured terms only; none on `Lphiu` and `LVu` (§1) | disagree | A literal reading of Eq. (1) applies h.c. to every new term. With the paper's own benchmark ($a^0$, $a^1$ real and symmetric) that doubles the $\phi\bar u u$ and $V_\mu\bar u\gamma^\mu u$ vertices. The file instead relies on $a^0$, $a^1$ hermitian and $b^0$ anti-hermitian. |
| Colour representation of $\varphi$, $\tilde\varphi$, $X$: fundamental $SU(3)_c$ (Sec. "Effective theory") | colour triplet, one `Index[Colour]` each (§2) | agree | The $\epsilon$ contraction of $\mathbf 3\otimes\mathbf 3\otimes\mathbf 3$ and the singlet $\varphi\,\bar u$ contraction both work with the triplet assignment. |
| $Q_\varphi=+2/3$, fixed by both $\varphi$ terms in Eq. (1) and by the RPV up-squark reading in Sec. "Beyond the Standard Model Explorations" | declared `Q -> -2/3` (§2 field table) | **disagree** | Sign flip. The reconstruction detects the same problem on its own and states that both interaction terms need $+2/3$. It then continues with $Q_\varphi=+2/3$ for the physics discussion. |
| $Q_{\tilde\varphi}=-1/3$, fixed by both $\tilde\varphi$ terms in Eq. (1) | $-1/3$ (§2) | agree | |
| $Q_X=+2/3$, fixed by both $X$ terms in Eq. (1) | $+2/3$ (§2) | agree | |
| $\chi$: neutral colour-singlet fermion carrying the missing energy (Sec. "Effective theory", Fig. 1) | Dirac singlet, $Q=0$, `Lchikin` (§1, §2) | agree | The paper does not choose Dirac or Majorana. Dirac is consistent with Eq. (1), which has no $\chi$–$\chi$ conjugation. |
| $\phi$, $V$: neutral colour-singlet invisible boson states (Sec. "Effective theory") | real scalar and real Proca vector, $Q=0$, singlet (§1, §2) | agree | Zero widths match the paper's "long-lived or decaying invisibly" state. |
| Kinetic and mass terms of the new fields (implied, not written) | `Lphikin`, `LVkin`, `Lchikin`, `Lvphikin`, `Lvphitkin` (§1) | extra-in-reconstruction | These terms are needed and their normalisations and signs are the standard ones. No conflict with the paper. |
| Kinetic term of the coloured vector $X$ (implied; $X$ is a colour triplet) | `LXkin` built from the plain curl $\partial^\mu X^\nu-\partial^\nu X^\mu$ (§1) | disagree | Not QCD-covariant. The reconstruction flags this itself and says the $g_s\,G\,X^\dagger X$ vertex is missing. |
| $SU(2)_L$ and hypercharge: Lagrangian written "in terms of mass eigenstates" (Sec. "Effective theory") | no $SU(2)_L$ representation and no hypercharge declared (§0, §2) | agree | Both treat the model as a broken-phase effective parametrisation. The paper says the flavour-changing terms come from the weak sector, but it does not write an $SU(2)_L$-invariant form either. |
| Benchmark couplings: all $b=\tilde b=0$; nine $a$ entries $=0.1$ with $(a^q_{SR})_{12}=-(a^q_{SR})_{21}$; four-fermion set $(\tilde a^q_{SR})_{\{1,2\}3}=(\tilde a^{1/2}_{SR})_{\{1,2\}}=0.1$ (Sec. "Model-independent searches") | parameter table in §3 | agree | Every non-zero entry and every zero entry matches, including the antisymmetric sign of $(a^q_{SR})_{21}$. |
| Benchmark masses: resonance 500 GeV; $m_\chi=50$ or 300 GeV or 0; $M_\phi=300$ GeV; $M_V=50$ GeV; four-fermion limit $M_\varphi=M_{\tilde\varphi}=3$ TeV | $M_\varphi=M_X=500$ GeV, $M_\phi=300$, $M_V=50$, $M_\chi=50$, $M_{\tilde\varphi}=3000$ GeV (§2) | agree | The file holds one default card, not five scenarios. $M_\chi=50$ GeV is scenario I; the vector-resonant (300 GeV) and four-fermion (massless) values need a different card, as does $M_\varphi=3$ TeV for the four-fermion limit. |
| Resonance widths (not given; the paper assumes BR$(\varphi,X\to t\chi)=1$) | $W_\varphi=W_X=50$ GeV, $W_{\tilde\varphi}=300$ GeV (§2) | extra-in-reconstruction | Fixed at 10 % of the mass. The paper's analysis is insensitive to this choice. |
| PDG codes, LHA block `MONOTOP`, `InteractionOrder {NP,1}` | §3 | extra-in-reconstruction | Implementation bookkeeping. The paper says nothing about it. |

## 3. Disagreements, with severity

1. **Electric charge of $\varphi$ is $-2/3$ instead of $+2/3$ — substantive.**
   A human should check the `QuantumNumbers -> {Q -> ...}` line of the `vphi` class against Eq. (1): both
   $\varphi$ vertices and the paper's own RPV up-squark reading need $+2/3$, so the declared value breaks
   electric-charge conservation and flips the sign of the $\varphi$–photon coupling.
2. **The $X$ kinetic term uses the plain curl, not the QCD covariant derivative — substantive.**
   A human should check whether `FS[X,mu,nu]` was meant to be a covariant field strength, because as written
   the colour-triplet vector $X$ has no gluon coupling from its kinetic term, which changes its production rate.
3. **Scope of the "+ h.c." in Eq. (1) — convention, with a possible factor of 2.**
   A human should decide whether the paper's h.c. covers the $\phi$ and $V$ flavour-changing terms; if it
   does, the file's `Lphiu` and `LVu` vertices are a factor of 2 too small for the benchmark values used in
   Table I.
4. **No Standard Model part inside `LTotal` — convention.**
   A human should confirm that the model file loads the SM FeynRules model beside this one, because Eq. (1)
   starts from $\lag_{SM}$.
5. **Single default mass card — cosmetic.**
   A human should check that the benchmark cards for the vector-resonant ($m_\chi=300$ GeV), four-fermion
   ($m_\chi=0$, $M_\varphi=3$ TeV) and flavour-changing scenarios exist somewhere outside the model file.
6. **Widths fixed by hand at 10 % of the mass — cosmetic.**
   A human should confirm the widths are recomputed per scenario, since the paper instead assumes a unit
   branching ratio to $t\chi$.
7. **Direction of the resonant initial state in the reconstruction's §4 summary — cosmetic.**
   The reconstruction writes $d\,s\to\varphi$ and $d\,d\to X$, while the paper writes $\bar d_i\bar d_j\to S$
   or $V$; these are conjugate processes, so a human only needs to check that the prose is not read as a
   charge statement.

## 4. Overall assessment

The reconstruction reproduces the operator content of Eq. (1) closely. All ten interaction terms are
present, with the same fields, the same charge conjugation on the diquark bilinears, the same $\epsilon^{ijk}$
colour contraction, the same scalar/pseudo-scalar and vector/axial-vector coefficient pairs, and the same
flavour index placement. The derived flavour (anti)symmetry rules match the paper's own statement about the
$\epsilon^{ijk}$ tensor, and every benchmark coupling value, including the antisymmetric sign of
$(a^q_{SR})_{21}$, matches the paper. The differences fall into two groups. The first group is bookkeeping
that the paper does not fix: kinetic terms, widths, PDG codes, LHA block, and a single default mass card
instead of five scenarios. The second group holds two physics items — the declared electric charge of
$\varphi$, which has the opposite sign to the value that Eq. (1) requires, and the non-covariant field
strength of the coloured vector $X$ — plus one ambiguity about how far the "+ h.c." of Eq. (1) reaches. The
reconstruction raises the charge problem and the $X$ field-strength problem by itself and marks the charge as
an internal inconsistency of the implementation file, so the reader is told where to look. A human reviewer
should decide whether the charge sign is a defect of the implementation or of the reconstruction, since the
reconstruction had no access to the paper.
