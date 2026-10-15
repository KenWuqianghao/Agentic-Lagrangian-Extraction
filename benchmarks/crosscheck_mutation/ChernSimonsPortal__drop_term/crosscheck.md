# Cross-check: reconstruction vs. paper

RUN-TAG: XM-CROSS-ChernSimonsPortal__drop_term

Paper: *Anomaly driven signatures of new invisible physics at the Large Hadron
Collider* (Antoniadis, Boyarsky, Espahbodi, Ruchayskiy, Wells; CERN-PH-TH/2009-006).

## 1. Where the paper defines the model

The paper gives the model at two levels.

**High-energy level.** Section 3 and Section 4 define heavy chiral fermions
$\psi_{1,2},\chi_{1,2}$ and a heavy Higgs $\Phi$, with charges in
Table 2 (`tab:2ferm`), Table 4 (`tab:su2`) and Table 5 (`tab:su2ex`), and Yukawa
terms in eq. (70) and eq. (60). These fields cancel the mixed anomalies. They are
heavy (about 10 TeV or more) and the paper integrates them out.

**Low-energy level — this is what an implementation file must contain.**

- eq. (39): $\mathcal{L} = \mathcal{L}_{SM} - \frac{1}{4g_X^2}|F_X|^2
  + \frac{M_X^2}{2}|D\theta_X|^2 + \mathcal{L}_{int}$, with $\theta_X$ the
  Stueckelberg pseudo-scalar and $D\theta_X = d\theta_X + X$.
- eq. (59): the three interaction vertices, written in mass eigenstates:
  $\epsilon^{\mu\nu\lambda\rho}Z_\mu X_\nu\partial_\lambda Z_\rho$,
  $\epsilon^{\mu\nu\lambda\rho}Z_\mu X_\nu\partial_\lambda \gamma_\rho$,
  $\epsilon^{\mu\nu\lambda\rho}W^+_\mu X_\nu\partial_\lambda W^-_\rho$.
- eq. (48): the covariant form,
  $\mathcal{L}_{int} = c_1\frac{H^\dagger DH}{|H|^2}D\theta_X F_Y
  + c_2\frac{H F_W DH^\dagger}{|H|^2}D\theta_X$.
- eq. (15): the broken-phase form of the first term,
  $\mathcal{L}_{XZY} = c_1 (d\theta_Z + Z) F_Y D\theta_X + \mathcal{O}(\partial h/v)$.
- eq. (40) and the display just after it: the vertices
  $\Gamma_{XZZ} = \frac{1}{2}c_1 s_W \epsilon^{\mu\nu\lambda\rho}(k_{2\lambda}-k_{1\lambda})$,
  $\Gamma_{XZ\gamma} = c_1 c_W \epsilon^{\mu\nu\lambda\rho}k_{2\rho}$ (the index
  on $k_2$ is a typo for $\lambda$), and
  $\Gamma_{XW^+W^-} = c_2\,\epsilon^{\mu\nu\lambda\rho}(k_{2\lambda}-k_{1\lambda})$.
- eq. (41): the three partial widths $X\to ZZ$, $X\to W^+W^-$, $X\to Z\gamma$;
  ratios in eq. (55) and eq. (57).
- Text after eq. (64): the operator
  $\epsilon^{\mu\nu\lambda\rho}X_\mu\gamma_\nu\partial_\lambda\gamma_\rho$ is
  forbidden, because it breaks electromagnetic gauge invariance.
- Section 1 and Section 5: the SM fermions carry no $U(1)_X$ charge, so $X$ has
  no direct fermion coupling.

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| $\mathcal{L}_{SM}$ (eq. 39) | `LSM` in `LTotal` | agree | Unmodified SM in both. |
| $-\frac{1}{4g_X^2}|F_X|^2$ (eq. 39) | $-\frac14 X_{\mu\nu}X^{\mu\nu}$ (sec. 1.1) | agree | Same operator. The paper keeps $1/g_X^2$ outside; the file uses a canonical field. The couplings $c_1,c_2$ absorb the rescaling. |
| $\frac{M_X^2}{2}|D\theta_X|^2$ (eq. 39) | $\frac12 M_X^2 X_\mu X^\mu$ (sec. 1.1) | agree | The Proca mass is the unitary-gauge form of the Stueckelberg mass ($\theta_X \to 0$). Same physics for the tree-level signals studied. |
| Stueckelberg field $\theta_X$, $U(1)_X$ gauge group (eq. 39, eq. 69) | no $\theta_X$, `X` declared as a plain vector with no gauge group (sec. 2) | missing-in-reconstruction | Unitary-gauge truncation. It removes the Goldstone and the gauge-group bookkeeping only. |
| $c_1$ neutral portal, covariant form (eq. 48, first term; eq. 15) | $c_1\,\epsilon^{\mu\nu\lambda\rho}Z_\mu X_\nu\partial_\lambda B_\rho$ (sec. 1.2, 1.3, boxed) | agree | Structure matches eq. (15): one $Z$ leg, one hypercharge field strength, one $X$. |
| $\epsilon\,Z X \partial Z$ piece (eq. 59; $\Gamma_{XZZ}$, eq. 40) | $-c_1 s_W\,\epsilon^{\mu\nu\lambda\rho}Z_\mu X_\nu\partial_\lambda Z_\rho$ (sec. 1.2) | disagree | Field content, weak-mixing factor $s_W$ and relative sign all agree (from $B = c_W A - s_W Z$). The normalization does not: see D3 below (possible factor 2 in the vertex). |
| $\epsilon\,Z X \partial\gamma$ piece (eq. 59; $\Gamma_{XZ\gamma}$, eq. 40) | $+c_1 c_W\,\epsilon^{\mu\nu\lambda\rho}Z_\mu X_\nu\partial_\lambda A_\rho$ (sec. 1.3) | agree | Same factor $c_W$ and same sign relative to the $ZZ$ piece. |
| $c_2$ charged portal (eq. 48, second term; eq. 59, third vertex; $\Gamma_{XW^+W^-}$) | **no such term in the file.** `LPortalCharged` is used in `LTotal` but never defined (sec. 1.4) | missing-in-reconstruction | The paper needs this vertex. The file does not contain it. This is the main finding: see D1. |
| hermiticity of the charged portal (eq. 48 is real) | `LTotal := ... + HC[LPortalCharged]` (sec. 1) | disagree | `LTotal` adds only the conjugate half, not the term plus its conjugate: see D2. |
| $X$–$\gamma H$ and $X$–$ZH$ couplings, $\mathcal{O}(\partial h/v)$ (eq. 15 and text after eq. 41) | none; the file has no $X$–Higgs coupling (sec. 1.3, sec. 4) | missing-in-reconstruction | The paper calls these "generically small" and drops them from eq. (41). See D4. |
| no $\epsilon\,X\gamma\partial\gamma$ term (text after eq. 64) | no $\gamma\gamma X$ term (sec. 1.3) | agree | Both exclude it. |
| no $X$ coupling to SM fermions (sec. 1, sec. 5) | no fermion coupling (sec. 1.3, sec. 4) | agree | This is the defining feature of the "invisible" setup. |
| no $X$ coupling to gluons | none | agree | $X$ is a colour singlet in both. |
| $\Gamma_{X\to ZZ} = \frac{c_1^2 s_W^2 M_X^3}{192\pi M_Z^2}(1-4M_Z^2/M_X^2)^{5/2}$ (eq. 41) | first term of `WX` (sec. 3) | agree | Identical, factor for factor. |
| $\Gamma_{X\to W^+W^-} = \frac{c_2^2 M_X^3}{48\pi M_W^2}(1-4M_W^2/M_X^2)^{5/2}$ (eq. 41) | second term of `WX` (sec. 3) | agree | Identical. But the file has no vertex that produces it: see D1. |
| $\Gamma_{X\to Z\gamma} = \frac{c_1^2 c_W^2 M_X^3}{96\pi M_Z^2}(1-M_Z^2/M_X^2)^3(1+M_Z^2/M_X^2)$ (eq. 41) | third term of `WX` (sec. 3) | agree | Identical. |
| $X$ is a massive neutral colour-singlet spin-1 boson, $M_X\sim 1$ TeV (eq. 39, sec. 5) | `V[101]`, spin 1, self-conjugate, neutral, `MX = 1000.` GeV (sec. 2) | agree | The 1 TeV value is the paper's benchmark. |
| $c_1,c_2$ dimensionless and free, benchmarks $c_i=1$ and $c_i=0.1$ (after eq. 48; figs. 6, 7) | `c1`, `c2` external, block `NPCOUPLINGS`, value 1.0 (sec. 3) | agree | Same meaning and same default. |
| heavy fermions $\psi_{1,2},\chi_{1,2}$, heavy Higgs $\Phi$ (tables 2, 4, 5; eq. 60, eq. 70) | absent (sec. 2) | missing-in-reconstruction | By design. eq. (39) is the effective theory below the heavy masses. Not a defect. |
| $\kappa$, the anomaly coefficient (eq. 92, eq. 95) | absent | missing-in-reconstruction | $\kappa$ fixes $c_1,c_2$ from the high-energy charges. A low-energy file does not need it. |
| interaction order `NP` (no paper analogue) | `{NP,1}` on both couplings (sec. 3) | extra-in-reconstruction | Tool bookkeeping only. No physics. |

## 3. Disagreements

**D1. The $XW^+W^-$ term is absent from the implementation. Severity:
substantive.**
The paper requires this vertex three times: eq. (48) second term, eq. (59) third
vertex, and the $\Gamma_{XW^+W^-}$ vertex after eq. (40). The whole $W^+W^-$
phenomenology depends on it (eq. 41, eq. 57, fig. 8), and $W^\pm X$ associated
production is the paper's main discovery channel (sec. 5.3). The file names
`LPortalCharged` in `LTotal` but never defines it, so the model has a $c_2$
parameter and a $c_2$ partial width with no vertex behind them.
*Human check:* confirm that the source file really lacks the definition, then add
$c_2\,\epsilon^{\mu\nu\lambda\rho}W^-_\mu X_\nu\partial_\lambda W^+_\rho$ and
re-derive $\Gamma_{X\to W^+W^-}$ from the restored vertex.

**D2. `LTotal` adds only `HC[LPortalCharged]`. Severity: substantive.**
eq. (48) is a real Lagrangian, so the charged portal must appear as the term
plus its hermitian conjugate. The line
`LTotal := LSM + LXkin + LPortalNeutral + HC[LPortalCharged]` adds the conjugate
alone. Even after D1 is fixed, this gives a non-hermitian Lagrangian, or the
wrong weight for the $XW^+W^-$ vertex.
*Human check:* decide whether the intended line is `... + LPortalCharged +
HC[LPortalCharged]`, and check the resulting $XWW$ coupling against
$\Gamma_{XW^+W^-} = c_2\epsilon^{\mu\nu\lambda\rho}(k_{2\lambda}-k_{1\lambda})$.

**D3. Possible factor 2 in the $XZZ$ operator normalization. Severity:
substantive (needs verification).**
The file term is $-c_1 s_W\,\epsilon\,Z X \partial Z$. Two Wick contractions of
the identical $Z$ legs give a vertex proportional to
$c_1 s_W\,\epsilon^{\mu\nu\lambda\rho}(k_{2\lambda}-k_{1\lambda})$, which is
twice the paper's eq. (40) value $\frac12 c_1 s_W \epsilon(k_2-k_1)$. The
paper's own ratio eq. (55), $\Gamma_{Z\gamma}/\Gamma_{ZZ} = 2c_W^2/s_W^2$, is
consistent with the $\frac12$ in eq. (40) and with the $XZ\gamma$ coefficient
$c_1 c_W$. The file's `WX` reproduces eq. (41) exactly, so the operator
normalization and the width formula inside the file may disagree by a factor 4
in $\Gamma_{X\to ZZ}$. The paper does not state its wedge-product normalization
for eq. (48) and eq. (15), so this cannot be settled from the text alone.
*Human check:* compute the $XZZ$ Feynman rule from the file with the tool, and
compare it with eq. (40) and with the $ZZ$ term of eq. (41).

**D4. $X$–$ZH$ and $X$–$\gamma H$ couplings are dropped. Severity: convention.**
eq. (48) is written with the full Higgs doublet, so eq. (15) leaves
$\mathcal{O}(\partial h/v)$ terms that couple $X$ to $Z h$ and $\gamma h$. The
file is written after symmetry breaking with no physical Higgs leg, so these are
gone. The paper calls them "generically small".
*Human check:* decide whether the model is meant to be the full covariant
eq. (48) or only the gauge-boson truncation of eq. (59).

**D5. Stueckelberg sector replaced by a Proca mass. Severity: convention.**
eq. (39) carries $\theta_X$ and a $U(1)_X$ gauge symmetry; the file carries a
hard mass and no gauge group.
*Human check:* confirm that unitary gauge is acceptable for the intended
simulations. It is, for tree-level $X$ production and decay into gauge bosons.

**D6. Kinetic normalization $1/g_X^2$ versus canonical. Severity: cosmetic.**
*Human check:* confirm that $c_1,c_2$ in the file are the paper's $c_1,c_2$ for
a canonically normalized $X$, so that the benchmark values $c_i = 1$ and
$c_i = 0.1$ keep their meaning.

**D7. Ordering of the charged-portal fields. Severity: cosmetic.**
The paper writes $\epsilon\,W^+ X\partial W^-$ (eq. 59); the reconstruction's
proposed form is $\epsilon\,W^- X\partial W^+$ plus h.c. The two are the same
operator after the conjugate is added.

## 4. Overall assessment

The reconstruction agrees with the paper on every structural element that the
file actually contains: one new real, neutral, colour-singlet, massive spin-1
boson of about 1 TeV; no coupling to fermions, gluons or the Higgs; no
$\gamma\gamma X$ operator; a single dimension-4 Chern-Simons neutral portal that
collapses to $c_1\,\epsilon\,Z X \partial B$, with the correct $-s_W$ and
$+c_W$ weights and the correct relative sign; two free dimensionless couplings
with the paper's benchmark value; and a total width that reproduces all three
partial widths of eq. (41) factor for factor. The one large gap is the charged
portal. The paper's $c_2$ operator, its $XW^+W^-$ vertex, its $W^+W^-$ partial
width and its main discovery channel ($W^\pm X$ production) all require a term
that the file never defines, and the file compounds this by adding only
`HC[LPortalCharged]` to `LTotal`. The reconstruction detects this gap, states it
clearly, and infers the missing operator correctly from the unused `c2`
parameter and from the $W$ term of `WX`; so the gap is a property of the
implementation file, not an error of the reconstruction. Two further points
deserve a human eye: the possible factor 2 between the file's $XZZ$ operator and
the vertex of eq. (40), which would move $\Gamma_{X\to ZZ}$ by a factor 4 and is
not resolvable from the paper's form-notation alone; and the dropped
$\mathcal{O}(\partial h/v)$ couplings of $X$ to $Zh$ and $\gamma h$.
