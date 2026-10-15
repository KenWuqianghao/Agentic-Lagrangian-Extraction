# Cross-check: `reconstruction.md` against the paper

**Paper.** Antoniadis, Boyarsky, Espahbodi, Ruchayskiy, Wells,
*Anomaly driven signatures of new invisible physics at the Large Hadron Collider*
(CERN-PH-TH/2009-006).

**RUN-TAG:** XM-CROSS-ChernSimonsPortal__factor2

---

## 1. Where the paper defines the model

| Item | Location in `paper.tex` |
|---|---|
| Low-energy Lagrangian (SM + massive vector $X$ + interactions) | eq. (39), §2 |
| The three portal vertex structures in the broken phase | eq. (59), §2 |
| Gauge-covariant form of the portal ($c_1$, $c_2$) | eq. (48), §2 |
| Broken-phase form of the first portal term | eq. (15), §5 |
| Feynman rules $\Gamma_{XZZ}$, $\Gamma_{XZ\gamma}$, $\Gamma_{XW^+W^-}$ | eq. (40) and the unnumbered equation after it, §5 |
| Partial decay widths of $X$ | eq. (41), §5.2 |
| Width ratios (internal consistency of eq. 41) | eq. (55), eq. (57) |
| Heavy fermion sector that generates the portal | §3, §4; Tables 1–4; eq. (60), eq. (70) |
| Rejected non-abelian Chern-Simons route | eq. (64), eq. (90) and the text after them |

The paper's model at LHC energies is: the Standard Model, plus one massive
vector $X$, plus the D'Hoker-Farhi (generalized Chern-Simons) portal terms.
The heavy fermions of §3 and §4 are integrated out. The SM fermions carry no
$U(1)_X$ charge, so $X$ has no tree-level fermion coupling.

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| $\mathcal{L}_{SM}$ (eq. 39) | `LSM` inside `LTotal` (§1.4) | **agree** | Both keep the SM unchanged. |
| $-\dfrac{1}{4g_X^2}\lvert F_X\rvert^2$ (eq. 39) | $-\tfrac14 X_{\mu\nu}X^{\mu\nu}$, $X_{\mu\nu}=\partial_\mu X_\nu-\partial_\nu X_\mu$ (§1.1) | **agree** | Same abelian field strength. The paper keeps $1/g_X^2$ outside; the reconstruction uses a canonically normalized field. This is a rescaling $X\to g_X X$, not a physics change. |
| $\dfrac{M_X^2}{2}\lvert D\theta_X\rvert^2$ with $D\theta_X=d\theta_X+X$ (eq. 39) | $+\tfrac12 M_X^2 X_\mu X^\mu$ (§1.1) | **agree** | The paper uses a Stückelberg field $\theta_X$; the reconstruction uses the unitary gauge $\theta_X=0$. Both give a Proca field. The $\tfrac12$ and the relative sign are correct for a real vector. See disagreement D4 for what the unitary gauge removes. |
| $X$ is the $U(1)_X$ gauge boson; SM fields are neutral under $U(1)_X$ (§2, intro) | $X$ = `V[101]`, spin 1, colour singlet, weak singlet, $Y=0$, $Q=0$, `SelfConjugate -> True` (§2) | **agree** | A $U(1)$ gauge field is real and electrically neutral. The reconstruction's field table matches. |
| SM fermions are not charged under $U(1)_X$; no $q\bar q\to X\to f\bar f$ (§1, §5.1) | no fermion couplings, no `ProjP`/`ProjM`, no `Ga`, no `CC` (§1.4) | **agree** | No chirality structure exists in either model. The absence of chiral projectors is correct, not an omission. |
| $M_X \sim 1$ TeV benchmark; $c_1=c_2=1$ benchmark (§5.1, §5.3, Fig. 2 caption) | $M_X = 1000$ GeV, $c_1=c_2=1.0$ (§2, §3) | **agree** | Numerical benchmark values match the paper's choice. |
| $\epsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \partial_\lambda Z_\rho$ (eq. 59) | $-2\,c_1 s_W\,\epsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \partial_\lambda Z_\rho$ (§1.2) | **disagree** | Tensor structure and index slot order match eq. (59) exactly. The coefficient does not: see D1. |
| $\epsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \partial_\lambda \gamma_\rho$ (eq. 59) | $+2\,c_1 c_W\,\epsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \partial_\lambda A_\rho$ (§1.2) | **disagree** | Structure matches. Coefficient is a factor 2 too large: see D1. |
| $\epsilon^{\mu\nu\lambda\rho} W^+_\mu X_\nu \partial_\lambda W^-_\rho$ (eq. 59) | $c_2\,\epsilon^{\mu\nu\lambda\rho} W^+_\mu X_\nu \partial_\lambda W^-_\rho$ (§1.3) | **agree** | Structure and coefficient match. |
| Hermiticity of the charged portal (implicit in eq. 48, which is a real action) | `HC[LPortalCharged]` $= c_2^*\,\epsilon^{\mu\nu\lambda\rho} W^-_\mu X_\nu \partial_\lambda W^+_\rho$ (§1.3) | **agree** | The paper lists the structure only, not the conjugate. A real Lagrangian needs the h.c. term. The reconstruction adds it correctly. |
| One coupling $c_1$ for the whole neutral sector; $\theta_W$ splits it into $c_1 s_W$ ($ZZX$) and $c_1 c_W$ ($Z\gamma X$) (eq. 48, eq. 15, eq. 40) | $c_1$ multiplies $(-s_W Z_\rho + c_W A_\rho)$, i.e. the relative split is $s_W : c_W$ (§1.2, §3) | **agree** | The relative weight of the two neutral vertices is correct. Only the common factor is wrong (D1). |
| $F_Y$ in eq. (15) is the hypercharge field strength, so the neutral portal is built on $B_\rho$ | $\mathcal{L} = 2c_1\,\epsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \partial_\lambda B_\rho$, using $B = c_W A - s_W Z$ (§1.2) | **agree** | The relative minus sign between the $ZZX$ and $Z\gamma X$ terms follows from $F_Y$. The reconstruction gets this right. The paper prints both vertices of eq. (40) with a plus sign; see D2. |
| $\Gamma_{XW^+W^-}^{\mu\nu\rho} = c_2\,\epsilon^{\mu\nu\lambda\rho}(k_2-k_1)_\lambda$ (after eq. 40) | vertex "proportional to $\epsilon^{\alpha\nu\lambda\beta}(p_2-p_1)_\lambda$" from $c_2$ plus h.c. (§1.3) | **agree** | The two Wick contractions of the $c_2$ term and its h.c. combine to exactly $c_2\,\epsilon^{\alpha\nu\lambda\beta}(k_2-k_1)_\lambda$. Normalization matches the paper. |
| $\Gamma_{XZZ}^{\mu\nu\rho} = \tfrac12 c_1 s_W\,\epsilon^{\mu\nu\lambda\rho}(k_2-k_1)_\lambda$ (eq. 40) | vertex from $-2c_1 s_W\,\epsilon Z X \partial Z$, i.e. $-2c_1 s_W\,\epsilon^{\alpha\nu\lambda\beta}(k_2-k_1)_\lambda$ (§1.2) | **disagree** | Magnitude is 4 times the paper's, and the sign is opposite. See D1 and D2. |
| $\Gamma_{XZ\gamma}^{\mu\nu\rho} = c_1 c_W\,\epsilon^{\mu\nu\lambda\rho} k_{2\rho}$ (eq. 40) | vertex from $+2c_1 c_W\,\epsilon Z X \partial A$ | **disagree** | Magnitude is 2 times the paper's. The free index $\rho$ on $k_2$ in eq. (40) is a typographical slip for $\lambda$; the reconstruction's $\lambda$ placement is the consistent one. |
| $\Gamma_{X\to ZZ} = \dfrac{c_1^2 s_W^2 M_X^3}{192\pi M_Z^2}\left(1-\frac{4M_Z^2}{M_X^2}\right)^{5/2}$ (eq. 41) | first term of `WX` (§3) | **agree** | Copied term for term, including the $\beta^5$ threshold factor. |
| $\Gamma_{X\to W^+W^-} = \dfrac{c_2^2 M_X^3}{48\pi M_W^2}\left(1-\frac{4M_W^2}{M_X^2}\right)^{5/2}$ (eq. 41) | second term of `WX` (§3) | **agree** | Identical. |
| $\Gamma_{X\to Z\gamma} = \dfrac{c_1^2 c_W^2 M_X^3}{96\pi M_Z^2}\left(1-\frac{M_Z^2}{M_X^2}\right)^{3}\left(1+\frac{M_Z^2}{M_X^2}\right)$ (eq. 41) | third term of `WX` (§3) | **agree** | Identical. |
| Total width = sum of the three two-body widths; no $X\to f\bar f$ (eq. 41, §5.2) | `WX` is the sum of the same three channels (§3) | **agree** | Channel list matches. |
| $X$ also couples to $\gamma H$ and $Z H$, "generically small" (text after eq. 41); $\mathcal{O}(\partial h/v)$ terms in eq. (15) | no $X$–Higgs term anywhere | **missing-in-reconstruction** | See D4. |
| $\theta_X$ Stückelberg pseudo-scalar, $D\theta_X = d\theta_X + X$ (eq. 39, eq. 48) | no pseudo-scalar field | **missing-in-reconstruction** | See D4. Equivalent in unitary gauge, but the covariant form is lost. |
| Covariant portal $c_1\frac{H^\dagger DH}{\lvert H\rvert^2}D\theta_X F_Y + c_2\frac{H F_W DH^\dagger}{\lvert H\rvert^2}D\theta_X$ (eq. 48) | only the broken-phase mass-eigenstate form | **missing-in-reconstruction** | See D4. The broken-phase content is the part the paper uses for phenomenology, so this is a scope limit, not an error. |
| Heavy fermions $\psi_{1,2},\chi_{1,2}$ and heavy Higgs $\Phi$ (§3, §4, eq. 60, eq. 70, Tables 1–4) | absent | **agree** | Correct. These states sit above the LHC reach and are integrated out; eq. (39) is the theory below their masses. |
| $\epsilon^{\mu\nu\lambda\rho} X_\mu \gamma_\nu \partial_\lambda \gamma_\rho$ is rejected because it breaks electromagnetic $U(1)$ (text after eq. 64) | no $\epsilon\,A X \partial A$ operator (§3) | **agree** | Both models exclude the operator. The reconstruction gives a different reason (it says the operator vanishes for two on-shell photons). See D3. |
| Non-abelian CS term $\omega_{\nu\lambda\rho}(A^a)$ (eq. 90) inside eq. (64) | absent | **agree** | The paper rejects this route. Its absence is correct. |
| no paper counterpart | `M$InteractionOrderHierarchy` `{QCD,1},{QED,2},{NP,1}`; PDG code 5000023; `WX` declared `Internal`; propagator labels | **extra-in-reconstruction** | Implementation bookkeeping only. No physics claim to check. |

---

## 3. Disagreements

### D1. Overall factor 2 on the neutral portal — **substantive**

The reconstruction multiplies the complete neutral portal by 2:
$\mathcal{L} = 2c_1\,\epsilon\,Z X \partial B$. The paper gives this operator with a
single power of $c_1$ (eq. 48, eq. 15), and its Feynman rules (eq. 40) fix the
normalization as $\Gamma_{XZ\gamma} = c_1 c_W\,\epsilon\,k_2$. The factor 2
therefore doubles both neutral amplitudes and multiplies the $ZZ$ and $Z\gamma$
partial widths by 4. The mismatch is also internal to the reconstruction: its
own `WX` copies eq. (41) verbatim, with plain $c_1^2 s_W^2$ and $c_1^2 c_W^2$
numerators, which only holds if the neutral portal carries no extra factor 2.
The charged portal carries no such factor and matches
$\Gamma_{XW^+W^-} = c_2\,\epsilon(k_2-k_1)$ exactly, so the two sectors are
normalized against each other incorrectly. The reconstruction flags this itself
in its §5.2.
*Human check:* confirm that the implementation file has no leading `2` on
`LPortalNeutral`, and recompute the $ZZ$ and $Z\gamma$ branching ratios against
eq. (41) and Fig. 5.

### D2. Sign and normalization of the $XZZ$ vertex against eq. (40) — **convention, with one substantive part**

Two separate points sit in this row.

1. *Sign (convention).* The reconstruction has $-s_W$ on the $ZZX$ term and
   $+c_W$ on the $Z\gamma X$ term. This relative minus is exactly what
   $B = c_W A - s_W Z$ gives, and eq. (15) says the field strength is the
   hypercharge $F_Y$. The paper prints both lines of eq. (40) with a plus sign.
   The overall sign of $c_1$ is not observable, but the *relative* sign of the
   two neutral vertices is, because both contribute to the same three-gauge-boson
   amplitudes with an off-shell $X$.
2. *Factor (substantive).* Taking the paper's charged vertex as the
   normalization anchor, the paper's own $\Gamma_{XZZ} = \tfrac12 c_1 s_W\,
   \epsilon(k_2-k_1)$ of eq. (40) and its $\Gamma_{X\to ZZ}$ of eq. (41) do not
   sit on the same normalization: eq. (41), combined with the $W^+W^-$ width and
   the identical-particle factor, implies an effective $ZZX$ Lagrangian
   coefficient of about $c_1 s_W/\sqrt2$, while eq. (40) states $\tfrac12 c_1 s_W$.
   The reconstruction's value, $2c_1 s_W$, is larger than either.

*Human check:* fix the sign convention of $\epsilon^{\mu\nu\lambda\rho}$ and of
$B_\rho$ once, then rederive $\Gamma_{XZZ}$ and $\Gamma_{X\to ZZ}$ from a single
Lagrangian, and decide which of eq. (40) and eq. (41) sets the model's
normalization.

### D3. Reason given for the absence of $\epsilon\,A X \partial A$ — **cosmetic**

The reconstruction says the $\gamma\gamma X$ operator is absent because it would
vanish for two on-shell photons. The paper gives a stronger reason: the operator
is not gauge invariant under electromagnetic $U(1)$, which is why the route of
eq. (64) is rejected. The Lagrangians agree; only the stated reason differs.
*Human check:* no model change needed; correct the wording if the note is reused.

### D4. Stückelberg field, covariant portal and the $X$–Higgs vertices — **substantive (scope)**

The reconstruction works in unitary gauge and keeps only the mass-eigenstate
operators. It therefore drops three things the paper carries: the pseudo-scalar
$\theta_X$ and the combination $D\theta_X = d\theta_X + X$ (eq. 39); the
$SU(2)\times U(1)_Y\times U(1)_X$ covariant form of eq. (48); and, as a direct
consequence, the $X\gamma H$ and $XZH$ vertices, plus the
$\mathcal{O}(\partial h/v)$ terms of eq. (15). The paper calls these Higgs
couplings "generically small", so the omission is defensible for the diboson
analysis. It is still a real difference in field content and in the operator
basis.
*Human check:* decide whether the intended scope is the broken-phase diboson
model only. If $X h$ final states matter, the covariant operator of eq. (48)
must be implemented, not the three vertices of eq. (59).

---

## 4. Overall assessment

The reconstruction identifies the correct model. Field content, gauge
representations, self-conjugacy, the absence of fermion and chirality structure,
the three Levi-Civita portal operators of eq. (59) with the correct index slot
order, the $s_W$ versus $c_W$ split of the neutral sector, the hypercharge
($B_\rho$) origin of that split, the Hermitian completion of the charged portal,
the benchmark values $M_X = 1$ TeV and $c_1=c_2=1$, and all three partial widths
of eq. (41) match the paper. The charged portal even matches the paper's Feynman
rule normalization term for term. One clear defect stands out against this
background: an overall factor 2 multiplies the neutral portal, which the paper
does not have, which contradicts the paper's eq. (40) and eq. (48), and which is
inconsistent with the reconstruction's own width expression copied from eq. (41).
The reconstruction reports this conflict itself and argues the factor is
spurious. The remaining differences are of two kinds: a normalization and sign
question in the $ZZX$ vertex that the paper itself leaves unclear between eq. (40)
and eq. (41), and the deliberate restriction to the broken phase, which removes
the Stückelberg field and the small $X$–Higgs couplings. A human reviewer should
resolve the factor 2 first, because it changes two of the three branching ratios
by a factor 4, then settle the $\epsilon$-tensor and $ZZX$ normalization
convention, and finally confirm that the broken-phase scope is intended.
