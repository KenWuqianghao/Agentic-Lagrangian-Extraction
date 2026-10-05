# Cross-check: `reconstruction.md` against the 331 paper

**Paper:** Qing-Hong Cao and Dong-Ming Zhang, *Collider Phenomenology of the 3-3-1 Model*
(`paper.tex`). Gauge group SU(3)$_C\times$SU(3)$_L\times$U(1)$_X$.

**Reconstruction:** an independent reading of a FeynRules add-on file (`sanitized.fr`).

**Benchmark selected by the reconstruction:** $\beta=+1/\sqrt3$, $v_3=2$ TeV, $v_1=173.95$ GeV,
$k=1$, $g_X=0.5$. All charge comparisons below use the $\beta=+1/\sqrt3$ column of the paper.

---

## 0. Where the paper defines the model

| Content | Location in `paper.tex` |
| --- | --- |
| Scalar triplets $\rho,\eta,\chi$ and their vevs | Sec. 2.1, Eq. (1) |
| Charge generator $Q=T^3+\beta T^8+X$; $X_\rho,X_\eta,X_\chi$; $Q_Y,Q_V$ | Sec. 2.1, Eq. (xqn) and the two lines after it |
| Higgs Lagrangian and potential $V_{Higgs}$ | Sec. 2.1, Eq. (VHiggs) |
| CP-even mass matrix and eigenvalues; mixing matrix $U$ | Sec. 2.1.1, Eq. (Neutral even mass mixing), Eq. (U) |
| CP-odd mass matrix, $M_{H_0}$, mixing matrix $O$ | Sec. 2.1.1; Appendix B |
| Charged-scalar mass matrices and $M_{H^\pm}$, $M_{H^{\pm Q_Y}}$, $M_{H^{\pm Q_V}}$ | Sec. 2.1.2, Eqs. (sc23), (sc13) |
| Gauge Lagrangian, $G_\mu$ matrix, gauge-boson mass terms | Sec. 2.2, Eqs. (Gmu), (gaugemass), (gauge mass) |
| $M_W$, $M_{Y}$, $M_{V}$ | Sec. 2.2, Eq. (MVY) |
| $Z'$ mass term $\frac16(g^2+\beta^2g_X^2)v_3^2Z'^2_\mu$; $Z'$ and $B$ definitions | Sec. 2.2, Eqs. (ZP), (B) and the unnumbered equation after them |
| $M_Z$, $M_{Z'}$ | Sec. 2.2 and Sec. 2.5, Eq. (3) |
| Fermion Lagrangian, covariant derivative, quark and lepton (anti)triplets | Sec. 2.3 |
| Yukawa Lagrangian $\cL^q_{Yuk}$, $\cL^l_{Yuk}$ | Sec. 2.4 |
| Electric charges of all new states | Sec. 2.5, Table (tbl:charge) |
| Scalar masses collected | Sec. 2.5, Eqs. (4), (5) and the charged-scalar block |
| Residual $Z_2$ symmetry, 14 odd states | Sec. 2.6 |
| Full Feynman rules | Appendix A, Tables (1gauge-2scalars), (2gauges-1scalar), (2gauges-2scalars), (gauges), (gauge-fermion), (scalar-fermion) |

A note on scope. The reconstruction describes an **add-on** file. It holds only the new
mass eigenstates, their mass terms and one charged current. The paper defines the **full**
gauge theory. Rows below marked *missing-in-reconstruction* are terms the paper defines and
the file does not contain.

---

## 1. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| $Q=T^3+\beta T^8+X$ (Sec. 2.1, before Eq. (xqn)) | prose says $Q=T_3-\beta T_8+X$ | **disagree** | Sign of the $\beta T^8$ term. The declared charges follow the paper, so only the prose is wrong. |
| $\beta=+1/\sqrt3$ benchmark (Sec. 2.5) | `beta = 0.5773502691896258` | **agree** | Same value. One of the four values the paper studies. |
| $Z'$ kinetic term $-\frac14 F^2$ (Sec. 2.2) | $2\left[-\frac14 Z'_{\mu\nu}Z'^{\mu\nu}\right]=-\frac12 Z'_{\mu\nu}Z'^{\mu\nu}$ | **disagree** | $Z'$ is self-conjugate. The kinetic term is twice the canonical one. See disagreement D1. |
| $Z'$ mass term $\frac16(g^2+\beta^2g_X^2)v_3^2Z'^2_\mu$ (Sec. 2.2) | $2\left[\frac12 M_{Z'}^2Z'^2\right]=M_{Z'}^2Z'^2$ with $M_{Z'}^2=(g^2+\beta^2g_X^2)v_3^2/6$ | **agree** (coefficient only) | The written coefficient matches the paper. The pole mass does not, because the kinetic term is not canonical. See D1. |
| $M_{Z'}^2=\dfrac{c_W^2g^2v_3^2}{3[1-(1+\beta^2)s_W^2]}$, Eq. (3) | `MZp` $=\sqrt{(g^2+\beta^2g_X^2)v_3^2/6}$ | **disagree** | The paper's expression reduces exactly to $(g^2+\beta^2g_X^2)v_3^2/3$. The file gives half of that. See D1. |
| $M_{Y^{\pm Q_Y}}^2=\frac14 g^2(v_3^2+v_2^2)$, Eq. (MVY) | `MYp` $=\sqrt{g^2(v_3^2+v_2^2)/4}$ | **agree** | Complex-vector normalisation $-\frac12|F|^2+M^2|Y|^2$ is the canonical one. |
| $M_{V^{\pm Q_V}}^2=\frac14 g^2(v_3^2+v_1^2)$, Eq. (MVY) | `MVp` $=\sqrt{g^2(v_3^2+v_1^2)/4}$ | **agree** | Same. |
| $Q_Y=\frac{\sqrt3}{2}\beta+\frac12=+1$, Table (tbl:charge) | `Yp` with $Q=+1$, not self-conjugate | **agree** | Correct for $\beta=+1/\sqrt3$. |
| $Q_V=\frac{\sqrt3}{2}\beta-\frac12=0$, Table (tbl:charge) | `Vp` with $Q=0$, not self-conjugate | **agree** | The paper's footnote in Sec. 2.1.2 makes the same point: $Q_V=0$ here, but the state is still distinct from its antiparticle. |
| $AY^{+Q_Y}Y^{-Q_Y}=\frac12 i a_+e$ (Table (gauges)) | none; `Yp` never enters a `DC` | **missing-in-reconstruction** | $Y'$ has $Q=+1$ but no photon coupling. See D2. |
| $ZV^{+Q_V}V^{-Q_V}$, $ZY^{+Q_Y}Y^{-Q_Y}$ (Table (gauges)) | none | **missing-in-reconstruction** | $V'$ and $Y'$ sit in the broken part of SU(3)$_L$, so they carry $T^3=\mp\frac12$. Their $Z$ couplings are not zero even when $Q=0$. See D2. |
| $Z'V^{+Q_V}V^{-Q_V}=Z'Y^{+Q_Y}Y^{-Q_Y}=-\frac{i\sqrt3ea_0}{2c_Ws_W}$ (Table (gauges)) | none | **missing-in-reconstruction** | These drive $VV$ and $YY$ pair production in Sec. 5.1. |
| $V^{-Q_V}W^+Y^{+Q_Y}=\frac{ie}{\sqrt2 s_W}$ (Table (gauges)) | none | **missing-in-reconstruction** | The $W$-$V$-$Y$ vertex follows from $[I_+,V_-]=-U_-$ (Sec. 2.6). |
| All quartic gauge couplings (Table (gauges)) | none | **missing-in-reconstruction** | Same cause: the new vectors are free fields in the file. |
| $q_{1L}=(u,d,D)_L$ triplet, $Q_D=-\frac13$ (Sec. 2.3, Table (tbl:charge)) | `DQ`: colour **3**, $Q=Y=-\frac13$, Dirac mass | **agree** | $D$ is the third member of the triplet, so it is an SU(2)$_L$ singlet with $Y=Q$. The file's assignment is right. |
| $q_{2L}=(c,s,S)_L$, $Q_S=-\frac13$ | `SQ`: colour **3**, $Q=Y=-\frac13$ | **agree** | Same. |
| $q_{3L}=(b,-t,T)_L$ **anti-triplet**, $Q_T=+\frac23$ | `TQ`: colour **3**, $Q=Y=+\frac23$ | **agree** (charge only) | The charge is right. The anti-triplet structure is lost, so all $T$ interactions are gone. See D4. |
| Heavy-quark masses from $y^J\bar q\chi J_R$ (Sec. 2.4); "no restriction on them" (Sec. 2.5) | `MDQ`=`MSQ`=`MTQ`=1000 GeV, external | **agree** | Free Dirac masses are consistent with the paper. The Yukawa origin is not modelled. |
| $\bar DDA$, $\bar TTA$, $\bar DDZ$, $\bar TTZ$ (Table (gauge-fermion)) | from `DC` with $Y=Q$ and no SU(2) index | **agree** | Checked: the table gives $-ieQ$ for the photon and $+ieQs_W/c_W$ for the $Z$, which is the $T^3=0$ result. |
| $\bar DDZ'$, $\bar SSZ'$, $\bar TTZ'$ (Table (gauge-fermion)) | none | **missing-in-reconstruction** | See D3. |
| $l_{\ell L}=(\ell,-\nu_\ell,E_\ell)_L$ anti-triplet, $Q_{E_\ell}=0$ (Sec. 2.3, Table (tbl:charge)) | `EL` $=\{E_e,E_\mu,E_\tau\}$, $Q=Y=0$, colour singlet, free kinetic term | **agree** | $Q_{E_\ell}=-\frac12+\frac{\sqrt3}{2}\beta=0$ at $\beta=+1/\sqrt3$. The file is right; its `FullName` string is stale. |
| $\bar E_\ell E_\ell A/Z$ vertices $\propto a_-=\sqrt3\beta-1=0$ (Table (gauge-fermion)) | zero, because $Q=Y=0$ | **agree** | Both give zero at this $\beta$. |
| $\bar E_\ell E_\ell Z'$ (Table (gauge-fermion)) | none | **missing-in-reconstruction** | Non-zero in the paper. See D3. |
| $\bar Du\,Y^{+Q_Y}$, $g_L=-\frac{ie}{\sqrt2 s_W}$, $g_R=0$ (Table (gauge-fermion)) | $\frac{g}{\sqrt2}\bar u\gamma^\mu P_L D\,Y'_\mu+{\rm h.c.}$ | **agree** | $e/s_W=g$. Strength, chirality and flavour pairing all match. |
| $\bar Sc\,Y^{+Q_Y}$ | $\frac{g}{\sqrt2}\bar c\gamma^\mu P_L S\,Y'_\mu+{\rm h.c.}$ | **agree** | Same. |
| $\bar Dd\,V^{+Q_V}$, $g_L=-\frac{ieV_{ud}}{\sqrt2 s_W}$ | $\frac{g}{\sqrt2}\bar d\gamma^\mu P_L D\,V'_\mu+{\rm h.c.}$ | **disagree** | The CKM factor $V_{ud}$ is absent. See D8. |
| $\bar Ss\,V^{+Q_V}$, $g_L=-\frac{ieV_{cs}}{\sqrt2 s_W}$ | $\frac{g}{\sqrt2}\bar s\gamma^\mu P_L S\,V'_\mu+{\rm h.c.}$ | **disagree** | The CKM factor $V_{cs}$ is absent. See D8. |
| $\bar tT\,V^{+Q_V}$, $g_L=-\frac{ie}{\sqrt2 s_W}$ (Table (gauge-fermion)) | none | **missing-in-reconstruction** | The paper needs it for $T\to tV$ (Sec. 6.2). See D4. |
| $\bar Tb\,Y^{-Q_Y}$, $g_L=-\frac{ieV_{tb}}{\sqrt2 s_W}$ | none | **missing-in-reconstruction** | The paper needs it for $T\to bY$. See D4. |
| $\bar eE_eY^{+Q_Y}$ and the $\mu,\tau$ partners, $g_L=-\frac{ie}{\sqrt2 s_W}$ | none | **missing-in-reconstruction** | See D5. |
| $\bar\nu_\ell E_\ell V^{+Q_V}$, $g_L=-\frac{ie}{\sqrt2 s_W}$ | none | **missing-in-reconstruction** | See D5. |
| $g_R=0$ for every new charged current (Table (gauge-fermion)) | only `ProjM` is used | **agree** | The implemented currents are purely left-handed, as the paper requires. |
| $Z'$ couplings to all SM fermions (Table (gauge-fermion)) | none | **missing-in-reconstruction** | See D3. |
| Three scalar triplets $\rho,\eta,\chi$, Eq. (1) | only the physical mass eigenstates | **missing-in-reconstruction** | The file is a mass-eigenstate description. Acceptable in unitary gauge, but it removes the link to the potential. |
| $V_{Higgs}$ with $\mu_i^2$, $\lambda_i$, $\lambda_{ij}$, $\lambda'_{ij}$, $f$, Eq. (VHiggs) | no potential; $\lambda_3$ and the three $\lambda'_{ij}$ appear only inside mass formulas | **missing-in-reconstruction** | No trilinear or quartic scalar vertices exist. See D7. |
| $f=kv_3$, $k\sim O(1)$ (Sec. 2.1) | `f = k*v3`, $k=1$ | **agree** | Same definition. |
| $v^2=v_1^2+v_2^2=(246~{\rm GeV})^2$ (Sec. 2.1.1) | `v2` $=\sqrt{v^2-v_1^2}$, $v_1=173.95$ | **agree** | $173.95\simeq v/\sqrt2$, i.e. the paper's $v_1=v_2=174$ GeV benchmark of Fig. (vbr)(a). |
| $M_{H_2}^2=\frac{v^2}{v_1v_2}fv_3$, Eq. (4) | `MH2` $=\sqrt{(v^2/(v_1v_2))fv_3}$ | **agree** | Identical. |
| $M_{H_3}^2=2\lambda_3v_3^2$, Eq. (5) | `MH3` $=\sqrt{2\lambda_3v_3^2}$ | **agree** | Identical. |
| $M_{H_0}^2=\left(\frac{v_1v_2}{v_3}+\frac{v_1v_3}{v_2}+\frac{v_2v_3}{v_1}\right)f$, Eq. (5) block | `MH0` with the same three terms | **agree** | Identical. $H_0$ is the CP-odd state. |
| $M_{H^\pm}^2=\frac{2fv_3+\lambda'_{12}v_1v_2}{2v_1v_2}v^2$ | `MHpm` | **agree** | Identical, including the $\lambda'_{12}$ assignment. |
| $M_{H^{\pm Q_Y}}^2=\frac{2fv_1+\lambda'_{23}v_2v_3}{2v_2v_3}(v_2^2+v_3^2)$ | `MHQY` | **agree** | Identical, including the $\lambda'_{23}$ assignment. |
| $M_{H^{\pm Q_V}}^2=\frac{2fv_2+\lambda'_{13}v_1v_3}{2v_1v_3}(v_1^2+v_3^2)$ | `MHQV` | **agree** | Identical, including the $\lambda'_{13}$ assignment. |
| $m_h$ and the SM Higgs $h$, Eq. (4) | not present; $h$ comes from the base model, unmodified | **missing-in-reconstruction** | The paper's Sec. 3 rescales every $h$ coupling by $U_{i1}$. See D7. |
| CP-even mixing matrix $U$, Eq. (U); CP-odd matrix $O$, Appendix B | absent | **missing-in-reconstruction** | Without $U$ and $O$, no scalar couples to anything. See D7. |
| $H^{\pm Q_Y}$ charge $=+1$; $H^{\pm Q_V}$ charge $=0$ (Table (tbl:charge)) | `HQY` $Q=+1$; `HQV` $Q=0$, complex | **agree** | Correct for $\beta=+1/\sqrt3$. |
| $ZH^{+Q_Y}H^{-Q_Y}$, $ZH^{+Q_V}H^{-Q_V}$ (Table (1gauge-2scalars)) | from `DC` with $Y=Q$ | **agree** (decoupling limit) | With $s_{23},s_{13}\to1$ these states are the SU(2)$_L$-singlet third components, so the $-Qs_W/c_W$ form is right. |
| $AH^+H^-=ie(p_1-p_2)^\mu$ (Table (1gauge-2scalars)) | from `DC` with $Q=+1$ | **agree** | Photon coupling is correct. |
| $ZH^+H^-=\frac{ie(c_W^2-s_W^2)}{2c_Ws_W}(p_1-p_2)^\mu$ | from `DC` with $Y=Q=1$, i.e. $-e\,s_W/c_W$ | **disagree** | $H^\pm$ is a mixture of $\rho^\pm$ and $\eta^\pm$, which are SU(2)$_L$ doublet members with $T^3=\mp\frac12$. See D6. |
| $W^+H^-h$, $W^+H^{-Q_V}H^{-Q_Y}$, and the rest of Table (1gauge-2scalars) | none | **missing-in-reconstruction** | No gauge-scalar three-point couplings exist in the file. |
| $VVS$ couplings, Table (2gauges-1scalar) | none | **missing-in-reconstruction** | Includes $W^+W^-h$ and $ZZh$ rescalings that the paper's Sec. 3 constrains. |
| $VVSS$ couplings, Table (2gauges-2scalars) | only the $A$/$Z$ seagulls of `Hpm` and `HQY` | **missing-in-reconstruction** | The new vectors contribute no seagulls. |
| Scalar-fermion couplings, Table (scalar-fermion) | none | **missing-in-reconstruction** | No Yukawa sector at all. See D7. |
| Goldstone states $G_Z$, $G_{Z'}$, $G^\pm$, $G^{\pm Q_Y}$, $G^{\pm Q_V}$ | absent | **agree** | The paper's Feynman rules are in unitary gauge, where the Goldstones are eaten. Their absence is correct. |
| $Z_2$-odd sector: 14 states (Sec. 2.6) | not declared | **missing-in-reconstruction** | Not a Lagrangian term, but it fixes which state is stable. Absent couplings make the point moot in the file. |
| $|M_Y^2-M_V^2|<M_W^2$ (Eq. (deltaM_VY)) | holds automatically from the two mass formulas | **agree** | $M_Y^2-M_V^2=\frac14g^2(v_2^2-v_1^2)$, which is small for $v_1\simeq v_2$. |
| — | `Zp`, `Yp`, `Vp`, `H2`, `H3`, `H0`, `Hpm`, `HQY`, `HQV`, `DQ`, `SQ`, `TQ`, `EL` | **no extra states** | Every field in the file maps onto a state the paper defines. Nothing is extra. |
| — | `M$InteractionOrderHierarchy` with an `NP` counter; PDG codes 4000001–4000015; 1 GeV default widths | **extra-in-reconstruction** | Tool bookkeeping only. It has no physics content and no counterpart in the paper. |

---

## 2. Disagreements, with severity

### D1. The $Z'$ Lagrangian carries an overall factor 2 — **substantive**

The file writes $\mathcal{L}_{Z'}=2\left[-\frac14 Z'_{\mu\nu}Z'^{\mu\nu}+\frac12M_{Z'}^2Z'^2\right]$
with $M_{Z'}^2=(g^2+\beta^2g_X^2)v_3^2/6$.

Two things follow.

1. The **mass coefficient** then reads $M_{Z'}^2Z'^2=\frac16(g^2+\beta^2g_X^2)v_3^2Z'^2$.
   This is exactly the paper's mass term in Sec. 2.2. So the author appears to have copied
   the paper's coefficient correctly.
2. The **kinetic term** is $-\frac12 Z'_{\mu\nu}Z'^{\mu\nu}$, which is twice the canonical
   value for a self-conjugate vector. After the rescaling $Z'\to Z'_c/\sqrt2$ that restores
   $-\frac14F^2$, the mass term becomes $\frac12M_{Z'}^2Z'^2_c$. The pole mass is therefore
   $M_{Z'}=\sqrt{(g^2+\beta^2g_X^2)v_3^2/6}$.

The paper's value is different. Its Eq. (3), $M_{Z'}^2=c_W^2g^2v_3^2/\{3[1-(1+\beta^2)s_W^2]\}$,
reduces algebraically to $M_{Z'}^2=(g^2+\beta^2g_X^2)v_3^2/3$, using
$g_Y=gg_X/\sqrt{g^2+\beta^2g_X^2}$ and the definitions of $s_W,c_W$ in Sec. 2.2. That is twice
the file's $M_{Z'}^2$. With the file's own inputs the numbers are 823 GeV (paper) against
582 GeV (file), a factor $\sqrt2$.

The factor also halves the propagator residue, so any $Z'$ coupling added later would be
misnormalised by $1/\sqrt2$.

*What a human should check:* whether the `2` belongs only on the mass term (which reproduces
the paper) or should be removed together with a change of `MZp` to
$\sqrt{(g^2+\beta^2g_X^2)v_3^2/3}$; only the second choice gives both a canonical kinetic
term and the paper's pole mass.

### D2. $Y'$ and $V'$ have no gauge couplings — **substantive**

The file introduces `Yp` and `Vp` as free massive vectors. They never appear inside a
covariant derivative and no explicit vertex is written for them. The paper's Table (gauges)
gives them a full set: $AY^{+}Y^{-}=\frac12ia_+e$, $ZV^{+}V^{-}$, $ZY^{+}Y^{-}$,
$Z'V^{+}V^{-}$, $Z'Y^{+}Y^{-}$, $V^{-}W^{+}Y^{+}$, plus all the quartics.

Two consequences are serious. First, $Y'$ carries $Q=+1$ but has no photon coupling, so
electromagnetic gauge invariance is broken in the file. Second, $V'$ has $Q=0$ yet its
paper $Z$ coupling $-ie(1+a_-s_W^2)/(2c_Ws_W)$ is non-zero, because $V'$ is a $T^3=-\frac12$
member of the residual SU(2)$_L$, not a singlet.

*What a human should check:* whether the intended scope of the file excluded the diboson
sector, and whether the missing photon coupling of a charged vector invalidates the
$VV$/$YY$ production study of Sec. 5.1 and the unitarity cancellation of Sec. 5.1.1.

### D3. No $Z'$ coupling to any fermion — **substantive**

Table (gauge-fermion) lists $Z'$ couplings to $e,\mu,\tau$, the three neutrinos, $u,c$, $t$,
$d,s$, $b$, $D,S$, $T$ and $E_\ell$, each with separate $g_L$ and $g_R$. The file has none.
The $Z'$ is completely inert.

*What a human should check:* the whole of Sec. 4 (production, width, branching ratios,
dilepton limit, $A_{FB}$) rests on these couplings, so confirm whether the file was ever
meant to cover $Z'$ phenomenology or only the bilepton sector.

### D4. Third-generation currents are absent — **substantive**

The paper puts $q_{3L}=(b,-t,T)_L$ in the anti-triplet, which gives $\bar tT V^{+Q_V}$ and
$\bar TbY^{-Q_Y}$ (Table (gauge-fermion)) and the decays $T\to tV$, $T\to bY$ of Sec. 6.2.
The file's `TQ` has the right charge but no interaction of any kind. The reconstruction
states this plainly.

*What a human should check:* whether the conjugated (anti-triplet) structure was dropped on
purpose; the sign of $t$ in $q_{3L}$ and the placement of $V_{tb}$ both matter when the term
is restored.

### D5. Lepton charged currents are absent — **substantive**

The paper gives $\bar eE_eY^{+Q_Y}$ (and $\mu,\tau$) and $\bar\nu_\ell E_\ell V^{+Q_V}$, both
with $g_L=-ie/(\sqrt2 s_W)$ and $g_R=0$. The file's `EL` has a free kinetic term and a mass
only. The $E_\ell$ dark-matter signatures of Sec. 5.3 and Sec. 6.3, which exist only for
$\beta=+1/\sqrt3$ — the very benchmark chosen here — cannot be produced.

*What a human should check:* whether the leptonic bileptons were left out on purpose, given
that $\beta=+1/\sqrt3$ is the case where $E_\ell$ is a dark-matter candidate.

### D6. $H^\pm$ is treated as an SU(2)$_L$ singlet — **substantive**

The file declares `Hpm` with $Y=Q=+1$ and no SU(2) index, so its $Z$ coupling is
$-e\,s_W/c_W$. The paper's Table (1gauge-2scalars) gives
$ZH^+H^-=ie(c_W^2-s_W^2)/(2c_Ws_W)$, the $T^3=+\frac12$ value, because
$H^\pm=c_{12}\eta^\pm-s_{12}\rho^\pm$ is built from the first two components of the triplets.
With $s_W^2=0.23$ the two numbers differ in size and in sign.

This problem does **not** affect `HQY` and `HQV`: in the decoupling limit those states are
dominantly the third components of $\eta$ and $\rho$, which are genuine SU(2)$_L$ singlets,
so the file's treatment reproduces the paper there.

*What a human should check:* the $ZH^+H^-$ vertex against Table (1gauge-2scalars), and
whether any process in use is sensitive to it.

### D7. No scalar potential, no Yukawa sector, no scalar mixing — **substantive**

Eq. (VHiggs), the mixing matrices $U$ and $O$, and Tables (2gauges-1scalar) and
(scalar-fermion) have no counterpart in the file. Six scalars therefore have no vertices
except the gauge ones. The SM Higgs is unmodified, so the coupling rescalings by $U_{11}$
and $U_{21}$ that the paper constrains in Sec. 3 are not present. The reconstruction says
this itself in its Sec. 4.

*What a human should check:* whether a second file supplies the potential and Yukawas, or
whether the model is intentionally limited to on-shell masses plus one current.

### D8. CKM factors are missing on the down-type currents — **substantive (small numerically)**

The paper attaches $V_{ud}$, $V_{cs}$ and $V_{tb}$ to $\bar DdV^{+Q_V}$, $\bar SsV^{+Q_V}$
and $\bar TbY^{-Q_Y}$, and no CKM factor to $\bar DuY^{+Q_Y}$ and $\bar ScY^{+Q_Y}$. The file
uses $g/\sqrt2$ everywhere. Numerically $V_{ud}\simeq V_{cs}\simeq0.97$, so rates change by a
few percent, but the flavour structure is not the paper's.

*What a human should check:* whether the file assumes $U_L=V_L=\mathbf{1}$; the paper makes
the related choice "$V_L=V_{\rm CKM}$ and $U_L$ the identity" in Sec. 4.1, so the intended
convention should be stated.

### D9. Sign of $\beta T^8$ in the reconstruction's prose — **convention**

The reconstruction writes $Q=T_3-\beta T_8+X$ in its parameter table. The paper writes
$Q=T^3+\beta T^8+X$. Every charge the file declares follows the paper's sign, so this is a
description error, not a model error.

*What a human should check:* nothing in the model; correct the sentence.

### D10. "Every internal mass vanishes as $f\to0$ except `MH3`" — **cosmetic**

This claim in the reconstruction's Sec. 3 is wrong. `MHpm`, `MHQY` and `MHQV` all keep a
$\lambda'_{ij}$ term at $f=0$, exactly as in the paper's charged-scalar mass formulas.
`MH2` and `MH0` do vanish.

*What a human should check:* the sentence only; the formulas themselves match the paper.

### D11. `EL` named a charged lepton while $Q=0$ — **cosmetic**

The reconstruction reports that `EL`'s `FullName` strings say "heavy charged lepton" while
`QuantumNumbers` says $Q=0$. For $\beta=+1/\sqrt3$ the paper's Table (tbl:charge) gives
$Q_{E_\ell}=0$, so the numbers are right and the name is a leftover from another $\beta$.

*What a human should check:* rename the states, so a later reader does not trust the string.

### D12. Interaction-order bookkeeping — **convention**

The reconstruction notes that `gw` carries no `NP` order, so the bilepton currents count as
QED order. The paper makes no statement about counting. This affects MadGraph order
selection only.

*What a human should check:* that the generation commands used for any sample select the
intended orders.

---

## 3. Overall assessment

Everything the file does contain is, with one class of exception, a faithful copy of this
paper at $\beta=+1/\sqrt3$. The four charged-current terms match Table (gauge-fermion) in
strength, chirality and flavour pairing; all six scalar mass formulas, both bilepton mass
formulas, the $v_1^2+v_2^2=v^2$ constraint, $f=kv_3$, and every electric-charge and colour
assignment reproduce the paper exactly, including the two subtle cases where $Q=0$ but the
state is not self-conjugate. The exception is a normalisation problem around the $Z'$: the
explicit factor 2 doubles the kinetic term, which leaves the propagator residue halved and
the pole mass a factor $\sqrt2$ below the paper's Eq. (3), even though the written mass
coefficient reproduces the paper's mass term. Separately, the file is a small subset of the
paper. It is an effective, mass-eigenstate description with one interaction: the whole gauge
structure of SU(3)$_L$ is gone, so the new vectors have no self-couplings and no
electroweak couplings at all, the $Z'$ has no fermion couplings, the third generation and
the leptons have no bilepton currents, and there is neither a scalar potential nor a Yukawa
sector. Whether that subset is a defect or the intended scope of an add-on file is a
judgement about intent that this cross-check cannot make. The two items that are defects
under any reading of the scope are the $Z'$ factor of 2 and the absent photon coupling of
the electrically charged $Y'$.
