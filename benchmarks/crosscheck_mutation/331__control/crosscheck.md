# Cross-check: reconstruction of `sanitized.fr` against the paper

**Paper:** Qing-Hong Cao, Dong-Ming Zhang, *Collider Phenomenology of the 3-3-1 Model*
(`paper.tex`, `\title` line 37).
**Reconstruction:** `reconstruction.md`, an independent read of an implementation file that is
not available here.

---

## 1. Where the paper defines the model

| Block | Location in `paper.tex` |
| --- | --- |
| Gauge group and breaking pattern | Sec. 2.1, Eq. after `\be` at line 108 |
| Three Higgs triplets `\rho`, `\eta`, `\chi` and their vevs | Sec. 2.1, Eq. `\label{1}` and the vev equation |
| Charge generator `Q = T^3 + \beta T^8 + X`, `X` charges, `Q_Y`, `Q_V` | Sec. 2.1, Eq. `\label{xqn}` and the `Q_Y/Q_V` equation |
| Higgs Lagrangian and full potential | Sec. 2.1, `\cL_{Higgs}` and Eq. `\label{VHiggs}` |
| Neutral scalar mass matrix and eigenvalues | Sec. 2.1.1, Eq. `\label{Neutral even mass mixing}`, Eq. `\label{U}`, CP-odd matrix |
| Charged scalar mass matrices and eigenvalues | Sec. 2.1.2, the three `M^2_{\pm1}`, `M^2_{\pm Q_Y}`, `M^2_{\pm Q_V}` blocks |
| Gauge Lagrangian, `G_\mu` matrix, gauge boson masses | Sec. 2.2, Eq. `\label{Gmu}`, Eq. `\label{gauge mass}`, Eq. `\label{MVY}` |
| `Z'` definition, `g_Y`, `s_W`, `M_{Z'}` | Sec. 2.2, Eq. `\label{ZP}`, `\label{B}`, and the `m_Z^2`/`M_{Z'}^2` pair |
| Fermion Lagrangian, covariant derivatives, quark and lepton triplets | Sec. 2.3, `\cL_{\rm Fermion}` and the `q_{1L}`, `q_{2L}`, `q_{3L}`, `l_{iL}` equations |
| Exotic fermion charges `Q_D=Q_S`, `Q_T`, `Q_{E_\ell}` | Sec. 2.3 |
| Yukawa Lagrangian | Sec. 2.4, `-\cL^q_{Yuk}`, `-\cL^l_{Yuk}` |
| Charge table for the four `\beta` benchmarks | Sec. 2.5, Table `\label{tbl:charge}` |
| Mass spectrum summary | Sec. 2.5, Eqs. `\label{4}`, `\label{5}`, `\label{3}` |
| Complete Feynman rules | App. A, Tables `1gauge-2scalars`, `2gauges-1scalar`, `2gauges-2scalars`, `gauges`, `gauge-fermion`, `scalar-fermion` |
| Scalar mixing matrices `U` and `O` | App. B |

---

## 2. Which benchmark the file implements

The reconstruction lists `beta = 0.5773502691896258 = 1/\sqrt3`. The paper allows only
`\beta = \pm\sqrt3` and `\pm 1/\sqrt3` (Sec. 2.5). Every charge in the reconstruction agrees with
the `\beta=+1/\sqrt{3}` column of Table `tbl:charge`:

| State | Paper, `\beta=+1/\sqrt3` | Reconstruction |
| --- | --- | --- |
| `D`, `S` | `-1/3` | `-1/3` |
| `T` | `+2/3` | `+2/3` |
| `E_\ell` | `0` | `0` |
| `V` | `0` | `0` |
| `Y` | `+1` | `+1` |
| `H^{\pm Q_V}` | `0` | `0` |
| `H^{\pm Q_Y}` | `+1` | `+1` |
| `H^{\pm}` | `+1` | `+1` |

So the file is the `\beta=+1/\sqrt3` version of the 331 model, written in the mass basis, on top of
an SM file. The reconstruction does not name the model. Its physics content does identify it.

---

## 3. Term-by-term comparison

Compare physics content only. Notation differences are not counted.

### 3.1 Vector sector

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| `Z'` kinetic term inside `-\frac14 F^i_{\mu\nu}F^{i\mu\nu}` (Sec. 2.2, Eq. `\label{2}`) | `LZp = -\frac14 Z'_{\mu\nu}Z'^{\mu\nu}` | agree | `Z'` is a Cartan-direction field. It is real and it has no self-coupling. |
| `M^2_{Z'} = (g^2+\beta^2 g_X^2)v_3^2/3` (Sec. 2.2 mass line with `\frac16(g^2+\beta^2g_X^2)v_3^2 Z'^2`, confirmed by Eq. `\label{3}`) | `MZp = \sqrt{(g_w^2+\beta^2 g_X^2)v_3^2/6}` | **disagree** | Factor 2 too small in `M^2`. See D1. |
| `Y^{\pm Q_Y}` kinetic term, non-abelian (Sec. 2.2) | `LYp = -\frac12 Y'^\dagger_{\mu\nu}Y'^{\mu\nu}` with an abelian curl | **disagree** | Normalisation is right. The curl is not. See D7. |
| `M^2_{Y^{\pm Q_Y}} = \frac14 g^2(v_3^2+v_2^2)` (Eq. `\label{MVY}`) | `MYp = \sqrt{g_w^2(v_3^2+v_2^2)/4}` | agree | The paper uses the same `M^2 Y^\dagger Y` normalisation. |
| `V^{\pm Q_V}` kinetic term, non-abelian (Sec. 2.2) | `LVp`, abelian curl | **disagree** | Same defect as `Y'`. See D7. |
| `M^2_{V^{\pm Q_V}} = \frac14 g^2(v_3^2+v_1^2)` (Eq. `\label{MVY}`) | `MVp = \sqrt{g_w^2(v_3^2+v_1^2)/4}` | agree | The `v_1`/`v_2` split is correct: `Y'` takes `v_2`, `V'` takes `v_1`. |
| `V'` is a distinct particle from its antiparticle | `Vp` complex, `Q=0` | agree | The paper gives `V` the odd `Z_2` charge (Sec. 2.6), so `V` is not self-conjugate. |
| `AV^{+Q_V}V^{-Q_V}`, `AY^{+Q_Y}Y^{-Q_Y}`, `ZVV`, `ZYY`, `Z'VV`, `Z'YY`, `V W Y` (Table `gauges`) | none | **missing-in-reconstruction** | All triple gauge vertices are absent. |
| Quartic gauge vertices `AAVV`, `VVVV`, `WWYY`, `VVZZ'`, ... (Table `gauges`) | none | **missing-in-reconstruction** | All quartic gauge vertices are absent. |

### 3.2 Fermion sector

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| `q_{1L}=(u,d,D)_L`, `q_{2L}=(c,s,S)_L` triplets (Sec. 2.3) | `D`, `S` as `SU(2)_L`-singlet colour triplets, `Y=-1/3` | agree | Correct after `SU(3)_L \to SU(2)_L`. |
| `q_{3L}=(b,-t,T)_L` anti-triplet (Sec. 2.3) | `T` as `SU(2)_L`-singlet colour triplet, `Y=+2/3` | agree | The quantum numbers are right, but no `T` interaction is kept. See next rows. |
| `l_{iL}=(\ell,-\nu_\ell,E_\ell)_L` anti-triplets (Sec. 2.3) | `EL` colour and charge singlets, `Y=0` | agree | `Q_{E}=0` at `\beta=+1/\sqrt3`. |
| `i\bar\psi\gamma^\mu D_\mu\psi` for `D`, `S`, `T` (Sec. 2.3); `\bar DDA`, `\bar TTA`, `\bar DDZ`, `\bar TTZ` (Table `gauge-fermion`) | `LDQ`, `LSQ`, `LTQ` with `DC` | agree | `Y=Q`, `T^3=0` reproduces the photon and `Z` vertices of the table. |
| `\bar E_\ell E_\ell A`, `\bar E_\ell E_\ell Z` with `a_-=\sqrt3\beta-1=0` (Table `gauge-fermion`) | `LEL` with `\partial_\mu` only | agree | Both vertices vanish at `\beta=+1/\sqrt3`, so `\partial_\mu` is correct here. |
| Vector-like Dirac masses from `y^J\bar q\chi J_R`, `y^E\bar l\chi^* E_R` (Sec. 2.4) | `-M_D\bar DD`, `-M_S\bar SS`, `-M_T\bar TT`, `-M_{E_\ell}\bar E_\ell E_\ell` | agree | The paper says heavy fermion masses are free (Sec. 2.5). 1000 GeV matches the paper's own figures. |
| `\bar D u Y^{+Q_Y}`, `g_L=-ie/(\sqrt2 s_W)`, `g_R=0` (Table `gauge-fermion`) | `\frac{g_w}{\sqrt2}\bar u\gamma^\mu P_L D\,Y'_\mu` + h.c. | agree | `e/s_W=g_w`. Purely left-handed. Sec. 6.1 states the coupling is `g/\sqrt2`. |
| `\bar S c Y^{+Q_Y}`, same coupling | `\frac{g_w}{\sqrt2}\bar c\gamma^\mu P_L S\,Y'_\mu` + h.c. | agree | |
| `\bar D d V^{+Q_V}`, `g_L=-ieV_{ud}/(\sqrt2 s_W)` (Table `gauge-fermion`) | `\frac{g_w}{\sqrt2}\bar d\gamma^\mu P_L D\,V'_\mu` + h.c. | **disagree** | The CKM factor `V_{ud}` is dropped. See D5. |
| `\bar S s V^{+Q_V}`, `g_L=-ieV_{cs}/(\sqrt2 s_W)` | `\frac{g_w}{\sqrt2}\bar s\gamma^\mu P_L S\,V'_\mu` + h.c. | **disagree** | The CKM factor `V_{cs}` is dropped. See D5. |
| `\bar t T V^{+Q_V}`, `g_L=-ie/(\sqrt2 s_W)` (Table `gauge-fermion`; also Sec. 6.2, `T\to tV`) | none | **missing-in-reconstruction** | See D3. |
| `\bar T b Y^{-Q_Y}`, `g_L=-ieV_{tb}/(\sqrt2 s_W)` (Table `gauge-fermion`; also `T\to bY`) | none | **missing-in-reconstruction** | See D3. |
| `\bar\ell E_\ell Y^{+Q_Y}`, `g_L=-ie/(\sqrt2 s_W)` (Table `gauge-fermion`) | none | **missing-in-reconstruction** | See D4. |
| `\bar\nu_\ell E_\ell V^{+Q_V}`, `g_L=-ie/(\sqrt2 s_W)` (Table `gauge-fermion`) | none | **missing-in-reconstruction** | See D4. |
| `Z'` couplings to `e,\mu,\tau,\nu,u,c,t,d,s,b` (Table `gauge-fermion`) | none | **missing-in-reconstruction** | See D6. This is the whole of Sec. 4. |
| `Z'` couplings to `D`, `S`, `T`, `E_\ell` (Table `gauge-fermion`) | none | **missing-in-reconstruction** | See D6. |
| SM Yukawa terms and the CKM matrix (Sec. 2.4) | none | missing-in-reconstruction | Expected: these live in the SM file the module is loaded with. |

### 3.3 Scalar sector

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| `(D_\mu\rho)^\dagger(D^\mu\rho)+(D_\mu\eta)^\dagger(D^\mu\eta)+(D_\mu\chi)^\dagger(D^\mu\chi)` (Sec. 2.1, Eq. `\label{0}`) | free kinetic terms for the seven physical scalars | agree in part | The mass-basis kinetic and mass terms are right. Everything the covariant derivative generates beyond them is absent. See D8. |
| `V_{Higgs}` with `\mu_i^2`, `\lambda_{1,2,3}`, `\lambda_{12,13,23}`, `\lambda'_{12,13,23}`, `\sqrt2 f\epsilon_{ijk}\rho^i\eta^j\chi^k` (Eq. `\label{VHiggs}`) | no potential; `\lambda_3`, `\lambda'_{ij}`, `f` appear only inside mass formulas | **missing-in-reconstruction** | No scalar self-interaction of any kind. See D8. |
| `M^2_{H_2}=\frac{v^2}{v_1v_2}fv_3` (Eq. `\label{4}`) | `MH2 = \sqrt{(v_{\rm SM}^2/(v_1v_2))fv_3}` | agree | |
| `M^2_{H_3}=2\lambda_3 v_3^2` (Eq. `\label{5}`) | `MH3 = \sqrt{2\lambda_3 v_3^2}` | agree | |
| `M^2_{H_0}=(\frac{v_1v_2}{v_3}+\frac{v_1v_3}{v_2}+\frac{v_2v_3}{v_1})f` (Eq. `\label{5}` block) | `MH0`, same expression | agree | |
| `M^2_{H^\pm}=\frac{2fv_3+\lambda'_{12}v_1v_2}{2v_1v_2}v^2` (Sec. 2.1.2 and Sec. 2.5) | `MHpm`, same expression | agree | |
| `M^2_{H^{\pm Q_Y}}=\frac{2fv_1+\lambda'_{23}v_2v_3}{2v_2v_3}(v_2^2+v_3^2)` | `MHQY`, same expression | agree | Built from the 2-3 vev pair, as the reconstruction says. |
| `M^2_{H^{\pm Q_V}}=\frac{2fv_2+\lambda'_{13}v_1v_3}{2v_1v_3}(v_1^2+v_3^2)` | `MHQV`, same expression | agree | Built from the 1-3 vev pair. |
| `v^2=v_1^2+v_2^2=(246\,{\rm GeV})^2` (Sec. 2.1.1) | `v2 = \sqrt{v_{\rm SM}^2-v_1^2}` | agree | The `W` mass constraint is enforced the same way. |
| `f=kv_3`, `k\sim O(1)` (Sec. 2.1) | `f = k v_3`, `k=1` | agree | |
| `H^\pm` and `H^{\pm Q_Y}` photon and `Z` couplings (Tables `1gauge-2scalars`, `gauges`) | from `DC` with `Y=Q=+1` | agree | The abelian part is reproduced. |
| 125 GeV Higgs `h` and the CP-even mixing matrix `U` (Eq. `\label{U}`, App. B) | none | **missing-in-reconstruction** | The SM `h` stays unrotated, so all `\kappa` shifts of Sec. 3 are absent. See D8. |
| CP-odd mixing matrix `O` (App. B) | none | **missing-in-reconstruction** | See D8. |
| Charged-scalar mixing angles `c_{12},s_{12},c_{23},s_{23},c_{13},s_{13}` (Eqs. `\label{sc23}`, `\label{sc13}`) | none | **missing-in-reconstruction** | Every `V`, `Y` and `T` decay width in Secs. 5 and 6 uses them. |
| Goldstone bosons `G_Z`, `G_{Z'}`, `G^\pm`, `G^{\pm Q_Y}`, `G^{\pm Q_V}` | none | agree | The paper's Feynman rules are in unitary gauge (App. A), so this is consistent. |
| `VSS` couplings, Table `1gauge-2scalars` | none | **missing-in-reconstruction** | See D8. |
| `VVS` couplings, Table `2gauges-1scalar` | none | **missing-in-reconstruction** | See D8. |
| `VVSS` couplings, Table `2gauges-2scalars` | none | **missing-in-reconstruction** | See D8. |
| Scalar-fermion couplings, Table `scalar-fermion` | none | **missing-in-reconstruction** | Removes `T\to tH^{Q_V}`, `D\to`scalar modes, and all `H_{0,2,3}` decays. |

### 3.4 Parameters

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| `\beta` fixed to one of four values (Sec. 2.5) | `beta = 1/\sqrt3` external | agree | Selects the `\beta=+1/\sqrt3` model. |
| `g_X` fixed by `g_Y=gg_X/\sqrt{g^2+\beta^2g_X^2}` (Sec. 2.2) | `gX = 0.5` free external input | **disagree** | `g_X` is derived, not free. See D2. |
| `v_1` at the weak scale (Sec. 2.1) | `v1 = 173.95` GeV external | agree | Close to the paper's own `v_1=v_2=174` GeV benchmark (Fig. `vbr`). |
| `v_3 \gg v_{1,2}`, 2 TeV used throughout Sec. 3 | `v3 = 2000` GeV external | agree | |
| `\lambda_3`, `\lambda'_{12}`, `\lambda'_{13}`, `\lambda'_{23}` | four external inputs, all 0.1 | agree | Same role as in Eq. `\label{VHiggs}`. |
| `\lambda_1`, `\lambda_2`, `\lambda_{12}`, `\lambda_{13}`, `\lambda_{23}`, `\mu_i^2` (Eq. `\label{VHiggs}`) | none | **missing-in-reconstruction** | They set `m_h` and the `U` matrix. |
| Computed widths of `Z'`, `V`, `Y`, `D`, `S`, `T` (Figs. `zpwidth`, `vbr`, `Tbr`) | all widths are 1 GeV placeholders | disagree | Cosmetic for the Lagrangian. See D11. |

### 3.5 Extra terms

No row is **extra-in-reconstruction**. Every term the reconstruction reports has a counterpart in
the paper. The file is a strict subset of the paper's model, plus the two coefficient problems
below.

---

## 4. Disagreements, with severity

**D1. `M_{Z'}` is a factor `\sqrt2` too small. Severity: substantive.**
The paper writes the mass term as `\frac16(g^2+\beta^2g_X^2)v_3^2 Z'^2_\mu`. For a real vector this
equals `\frac12 M^2 Z'^2`, so `M^2_{Z'}=(g^2+\beta^2g_X^2)v_3^2/3`. Eq. `\label{3}` confirms it:
using `g_Y=gg_X/\sqrt{g^2+\beta^2g_X^2}` one gets `c_W^2/[1-(1+\beta^2)s_W^2]=(g^2+\beta^2g_X^2)/g^2`,
so Eq. `\label{3}` is the same `/3` result. The file uses `/6`, that is 581 GeV instead of 821 GeV
for `g_w=0.65`, `g_X=0.5`, `v_3=2` TeV.
*A human should read the `MZp` line in the `.fr` file and decide whether the real-field factor `1/2`
was dropped.*

**D2. `g_X` is treated as a free input. Severity: substantive.**
In the paper `g_X` is fixed once `g` and `s_W` are known: `g_X = g\,s_W/a_0` with
`a_0=\sqrt{1-(1+\beta^2)s_W^2}` (Sec. 2.2 and App. A). For `\beta=1/\sqrt3` this gives
`g_X \simeq 0.376`. The value 0.5 implies `s_W^2\simeq0.331`, which contradicts the `s_W` of the SM
file the module is loaded onto.
*A human should check whether `gX` should be an internal parameter derived from `sw` and `beta`.*

**D3. No third-generation exotic current. Severity: substantive.**
Table `gauge-fermion` gives `\bar t T V^{+Q_V}` and `\bar T b Y^{-Q_Y}`, both with `g/\sqrt2` and
`P_L`. The file has no `T` interaction at all, so `T` is stable in it. The paper builds its whole
`T\bar T` analysis (Sec. 6) on these two vertices.
*A human should confirm the `.fr` file really omits the `T` current, and add `t`-`T`-`V'` and
`b`-`T`-`Y'` if it does.*

**D4. No heavy lepton currents. Severity: substantive.**
Table `gauge-fermion` gives `\bar\ell E_\ell Y^{+Q_Y}` and `\bar\nu_\ell E_\ell V^{+Q_V}`, again with
`g/\sqrt2` and `P_L`. The file leaves `E_\ell` fully inert, so the dark matter and `\ell^+\ell^-+\met`
signatures of Sec. 5.3 cannot be produced.
*A human should check whether the lepton block was deliberately removed or lost.*

**D5. The CKM factors in the `V'` currents are dropped. Severity: substantive, small in size.**
The paper attaches `V_{ud}` to `\bar D d V^{+Q_V}` and `V_{cs}` to `\bar S s V^{+Q_V}`, while the
`Y'` currents carry no CKM factor. The file uses a bare `g_w/\sqrt2` for all four. The size change is
about 2.5 percent, but the flavour structure is gone, and with it any off-diagonal current.
*A human should check whether the down-type currents in the `.fr` file should carry `CKM[...]`.*

**D6. No `Z'` couplings to matter. Severity: substantive.**
Table `gauge-fermion` lists `Z'` couplings to every SM fermion and to `D`, `S`, `T`, `E_\ell`, with
separate `g_L` and `g_R`. The file has none, so its `Z'` is stable and cannot be produced. Sections 4
and 6 of the paper depend entirely on these couplings.
*A human should check whether the `Z'` interaction block exists elsewhere in the implementation.*

**D7. `Y'` and `V'` kinetic terms use an abelian curl. Severity: substantive.**
In the paper `Y` and `V` are `SU(3)_L` gauge fields, so `-\frac14 F^i_{\mu\nu}F^{i\mu\nu}` gives the
`AYY`, `ZYY`, `Z'YY`, `AVV`, `ZVV`, `Z'VV`, `VWY` vertices and all quartics of Table `gauges`. The
file uses `\partial_\mu X_\nu-\partial_\nu X_\mu`, so the `Q=+1` field `Y'` has no photon coupling.
This also removes diagrams (a), (b) and (c) of Fig. `vypair`, which the paper needs for the unitarity
cancellation of Sec. 5.1.1.
*A human should decide whether these vertices must be added by hand, since `FeynRules` cannot
generate them from an undeclared group.*

**D8. The whole scalar interaction sector is absent. Severity: substantive.**
There is no potential (Eq. `\label{VHiggs}`), no mixing matrices `U` and `O` (App. B), no mixing
angles `c_{12}`, `c_{23}`, `c_{13}`, and therefore none of Tables `1gauge-2scalars`,
`2gauges-1scalar`, `2gauges-2scalars` or `scalar-fermion`. The SM Higgs stays unmodified, so the
`\kappa` fits, `R_{Z\gamma}` and `R_{hh}` of Sec. 3 cannot be reproduced.
*A human should decide whether the file was cut down on purpose for one process, or whether the
scalar block is missing.*

**D9. `EL` is named "heavy charged lepton" but declares `Q=0`. Severity: cosmetic.**
The paper settles this: `Q_{E_\ell}=-\frac12+\frac{\sqrt3}{2}\beta = 0` at `\beta=+1/\sqrt3`
(Table `tbl:charge`). The charge is right and the name is a leftover from another `\beta`. The
reconstruction calls this an internal inconsistency; the paper shows it is only a naming problem.
*A human should fix the `FullName` string, not the charge.*

**D10. `H_0` is not marked as CP-odd. Severity: convention.**
In the paper `H_0` is the CP-odd eigenstate (Sec. 2.1.1), while `H_2` and `H_3` are CP-even. The file
declares three real neutral scalars with no CP label. This has no effect while the scalars have no
couplings, but it will matter as soon as they do.
*A human should check the CP assignment before any scalar coupling is added.*

**D11. All widths are 1 GeV placeholders. Severity: cosmetic.**
The paper computes the widths (Figs. `zpwidth`, `vbr`, `Tbr`).
*A human should replace them with `Automatic` or with computed values before any resonance study.*

**D12. `NP` interaction order is declared but never used in a vertex. Severity: convention.**
Only `gX`, `lam3` and the three `lampr*` carry `NP` order, and all of them appear only in mass
formulas. The one real vertex, the `g_w/\sqrt2` current, counts as QED order. In the paper this
coupling is a genuine `SU(3)_L` gauge coupling of weak strength (Sec. 6.1).
*A human should check the order counting used in the MadGraph process definitions.*

**D13. The benchmark point is below the paper's own limit. Severity: substantive, parameter choice.**
With `v_3=2` TeV the file gives `M_{Z'}\simeq0.58` TeV, and 0.82 TeV after D1 is fixed. The paper
excludes `M_{Z'}\lesssim3.6`-4 TeV for `\beta=+1/\sqrt3` from dilepton data (Sec. 4.3) and uses
`M_{Z'}=4` TeV as its benchmark.
*A human should decide whether `v_3=2` TeV is intended, since it was used for the Higgs fit but not
for the `Z'` study.*

---

## 5. Overall assessment

The reconstruction and the paper describe the same model at the level of field content, quantum
numbers and mass formulas. Every new state in the file maps one-to-one onto a state in the paper:
three new vectors, three vector-like colour triplets, three heavy neutral leptons, and seven physical
scalars. All charges match the `\beta=+1/\sqrt3` column of Table `tbl:charge` exactly, the colour and
`SU(2)_L` assignments are right, the exotic quarks are correctly vector-like, and eight of the nine
mass expressions reproduce the paper term for term, including the `v_2`/`v_1` split between `M_{Y'}`
and `M_{V'}` and the vev constraint `v_1^2+v_2^2=v_{\rm SM}^2`. The single interaction term in the
file, the left-handed `g_w/\sqrt2` current, matches Table `gauge-fermion` in chirality, colour
contraction, charge flow and coupling strength, and the reconstruction reads it correctly. The
reconstruction adds nothing that the paper does not contain. Two coefficient problems remain: the
`Z'` mass is a factor `\sqrt2` low against Eq. `\label{3}`, and `g_X` is used as a free input where
the paper fixes it from `s_W`. Beyond those, the gap is one of coverage, not of correctness: the
file carries no scalar potential, no scalar mixing, no `Z'` current, no gauge self-coupling, no
third-generation current and no lepton current, so most of the paper's phenomenology cannot be
generated from it. The reconstruction flags most of these gaps itself and marks them as properties of
the file rather than of its own reading, which makes it straightforward to check against the source.
The remaining question for a reviewer is whether the implementation was cut down on purpose for one
narrow process, and whether D1, D2 and D5 are implementation defects or deliberate convention
choices.
