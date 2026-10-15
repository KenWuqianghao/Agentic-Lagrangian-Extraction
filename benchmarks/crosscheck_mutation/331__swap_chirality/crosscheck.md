# Crosscheck: `reconstruction.md` against Cao & Zhang, "Collider Phenomenology of the 3-3-1 Model"

RUN-TAG: XM-CROSS-331__swap_chirality

## 0. Where the paper defines the model

The paper builds an $SU(3)_C \times SU(3)_L \times U(1)_X$ ("331") model. The relevant
definitions are:

| Content | Location in `paper.tex` |
|---|---|
| Three scalar triplets $\rho,\eta,\chi$ and their VEVs $v_1,v_2,v_3$ | Sec. 2.1, Eq. (1) and the VEV equation after it |
| Charge operator $Q=T^3+\beta T^8+X$; $Q_Y=\frac{\sqrt3}{2}\beta+\frac12$, $Q_V=\frac{\sqrt3}{2}\beta-\frac12$ | Sec. 2.1, unnumbered equations after Eq. (1) |
| Higgs potential $V_{Higgs}$ ($\mu_i^2$, $\lambda_i$, $\lambda_{ij}$, $\lambda'_{ij}$, $f=kv_3$) | Eq. `\eqref{VHiggs}` |
| CP-even / CP-odd / charged scalar mass matrices and eigenvalues | Sec. 2.1.1, 2.1.2; summary Eqs. `\eqref{4}`, `\eqref{5}` and the charged-scalar block |
| Gauge Lagrangian, $G_\mu$ matrix, $W^\pm,Y^{\pm Q_Y},V^{\pm Q_V}$ definitions | Sec. 2.2, Eqs. `\eqref{Gmu}`, `\eqref{gaugemass}`, `\eqref{gauge mass}` |
| Gauge boson masses $M_W,M_Y,M_V$ | Eq. `\eqref{MVY}` |
| $Z'$ field, $M_{Z'}^2$ | Eq. `\eqref{ZP}` and the line after Eq. `\eqref{B}`; also Eq. `\eqref{3}` |
| Fermion Lagrangian $\bar\psi^\alpha i D_\mu\gamma^\mu\psi^\alpha$, quark triplets $q_{1L},q_{2L},q_{3L}$, lepton anti-triplets $l_{iL}$ | Sec. 2.3 |
| Heavy fermion charges $Q_D=Q_S=\frac16-\frac{\sqrt3}{2}\beta$, $Q_T=\frac16+\frac{\sqrt3}{2}\beta$, $Q_{E_\ell}=-\frac12+\frac{\sqrt3}{2}\beta$ | Sec. 2.3 and Table `tbl:charge` |
| Yukawa Lagrangian | Sec. 2.4 |
| **All Feynman rules**, including gauge-boson–fermion chiral couplings | Appendix A, Tables `1gauge-2scalars`, `2gauges-1scalar`, `2gauges-2scalars`, `gauges`, `gauge-fermion`, `scalar-fermion` |

**Branch of the model.** The reconstruction sets `beta` $=0.5773502691896258=1/\sqrt3$.
Table `tbl:charge` of the paper for $\beta=+1/\sqrt3$ gives
$Q_{D}=Q_{S}=-1/3$, $Q_T=+2/3$, $Q_{E_\ell}=0$, $Q_V=0$, $Q_Y=+1$,
$Q_{H^{\pm Q_V}}=0$, $Q_{H^{\pm Q_Y}}=+1$, $Q_{H^\pm}=+1$.
Every charge in the reconstruction's field table matches this column. The whole comparison
below therefore uses the $\beta=+1/\sqrt3$ branch.

The decisive table for chirality is Appendix A.3, Table `gauge-fermion`. Its header states
that each vertex is $g_L\gamma^\mu P_L+g_R\gamma^\mu P_R$ with
$P_R=(1+\gamma^5)/2$, $P_L=(1-\gamma^5)/2$ — the same convention the reconstruction uses
for `ProjP` and `ProjM`.

---

## 1. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| $Q=T^3+\beta T^8+X$, $\beta=\pm1/\sqrt3,\pm\sqrt3$ (Sec. 2.1) | `beta` external, $=1/\sqrt3$ | **agree** | Reconstruction reads $\beta$ correctly, including why $1/\sqrt3$ gives SM-like exotic charges. |
| $Q_D=Q_S=-1/3$, colour triplet, from $q_{1L},q_{2L}$ (Sec. 2.3, Table `tbl:charge`) | `DQ`, `SQ`: $Q=Y=-1/3$, **3** of $SU(3)_c$ | **agree** | $SU(2)_L$ singlet with $Y=Q$ is the correct residual assignment for the third triplet component. |
| $Q_T=+2/3$, colour triplet, from anti-triplet $q_{3L}$ (Sec. 2.3) | `TQ`: $Q=Y=+2/3$, **3** | **agree** | |
| $Q_{E_\ell}=0$, three generations, from lepton anti-triplets (Sec. 2.3) | `EL`: $Q=Y=0$, 3 generations, SM singlet | **agree** | Confirms the reconstruction's decision to trust $Q=0$ over the "heavy charged lepton" name string. For $\beta=+1/\sqrt3$ the $E_\ell$ are neutral. |
| $Y^{\pm Q_Y}_\mu$ with $Q_Y=+1$; $V^{\pm Q_V}_\mu$ with $Q_V=0$ (Eq. `\eqref{Gmu}`, Table `tbl:charge`) | `Yp` $Q=+1$ complex; `Vp` $Q=0$ complex | **agree** | $V$ is neutral but not self-conjugate. The reconstruction states this correctly. |
| $Z'_\mu=-s_{331}W^8_\mu+c_{331}X_\mu$, real neutral vector (Eq. `\eqref{ZP}`) | `Zp` real, $-\frac14 Z'_{\mu\nu}Z'^{\mu\nu}+\frac12 M^2 Z'^2$ | **agree** | Normalisation for a real vector is right. |
| $M_{Z'}^2=\frac13(g^2+\beta^2g_X^2)v_3^2$ (line after Eq. `\eqref{B}`: $\mathcal{L}\supset\frac16(g^2+\beta^2g_X^2)v_3^2Z'^2$; equal to Eq. `\eqref{3}`) | `MZp` $=\sqrt{(g^2+\beta^2g_X^2)v_3^2/6}$ | **disagree** | Factor 2 in $M^2$ ($\sqrt2$ in the mass). The paper's Lagrangian coefficient $\frac16 A v_3^2$ equals $\frac12 M^2$, so $M^2=\frac13 A v_3^2$. I checked this against Eq. `\eqref{3}` and it is consistent. |
| $M_{Y^{\pm Q_Y}}^2=\frac14 g^2(v_3^2+v_2^2)$ (Eq. `\eqref{MVY}`) | `MYp` $=\sqrt{g^2(v_3^2+v_2^2)/4}$ | **agree** | |
| $M_{V^{\pm Q_V}}^2=\frac14 g^2(v_3^2+v_1^2)$ (Eq. `\eqref{MVY}`) | `MVp` $=\sqrt{g^2(v_3^2+v_1^2)/4}$ | **agree** | |
| $g_X$ fixed by $g_Y=gg_X/\sqrt{g^2+\beta^2g_X^2}$, i.e. by $g$ and $s_W$ (Sec. 2.2) | `gX` $=0.5$, free external input | **disagree** | With $g\simeq0.652$ and $s_W^2\simeq0.231$ the paper's relation gives $g_X\simeq0.38$, not 0.5. |
| $\mathcal{L}_{Gauge}=-\frac14 F_{\mu\nu}F^{\mu\nu}-\frac14 B_{\mu\nu}B^{\mu\nu}$, non-abelian $SU(3)_L$ strength (Sec. 2.2) | `FS[Yp,...]`, `FS[Vp,...]` = plain curl; masses added by hand | **disagree** | $Y'$ carries $Q=+1$, so its kinetic term must be covariant. The reconstruction flags this itself. |
| $\gamma Y^{+Q_Y}Y^{-Q_Y}=\frac12 i a_+e$ ($=ie$ for $\beta=1/\sqrt3$) (Table `gauges`) | absent | **missing-in-reconstruction** | The charged vector has no photon coupling in the file. |
| $ZY^{+}Y^{-}$, $Z'Y^{+}Y^{-}$, $ZV^{+}V^{-}$, $Z'V^{+}V^{-}$, $V^{-}W^{+}Y^{+}$ and all quartics (Table `gauges`) | absent | **missing-in-reconstruction** | Note $ZV^{+Q_V}V^{-Q_V}=-\frac{ie(1+a_-s_W^2)}{2c_Ws_W}\ne0$: the neutral $V$ still couples to $Z$. |
| $\mathcal{L}_{\rm Fermion}=\bar\psi i D_\mu\gamma^\mu\psi$, Dirac kinetic terms for $D,S,T,E_\ell$ (Sec. 2.3) | `LDQ`, `LSQ`, `LTQ`, `LEL` kinetic terms | **agree** | |
| $\bar DDA=-\frac{i(3\sqrt3\beta-1)e}{6}$, $\bar DDZ=\frac{i(3\sqrt3\beta-1)es_W}{6c_W}$ (Table `gauge-fermion`) | from `DC` with $Q=Y=-1/3$ | **agree** | I evaluated the paper's rules at $\beta=1/\sqrt3$ and they reproduce $eQ$ and $et_WY$ exactly. Same for $T$. |
| $\bar E_\ell E_\ell A$, $\bar E_\ell E_\ell Z\propto a_-=\sqrt3\beta-1$ (Table `gauge-fermion`) | $D_\mu E=\partial_\mu E$ | **agree** | $a_-=0$ at $\beta=+1/\sqrt3$, so both couplings vanish. |
| Heavy fermion Dirac masses from $y^J\bar q\chi J_R$, $y^E\bar l\chi^* E_R$ (Sec. 2.4) | `MDQ`, `MSQ`, `MTQ` $=1000$ GeV; `MEE`,`MEM`,`MET` $=1000$ GeV | **agree** | Paper says heavy fermion masses are unconstrained and uses 1000 GeV as its benchmark. |
| $\bar D\,u\,Y^{+Q_Y}$: $g_L=-\frac{ie}{\sqrt2 s_W}$, $g_R=0$ (Table `gauge-fermion`); also the $P_L\dots P_L$ structure of $A^D$ in Sec. 5.1.1 | $\frac{g}{\sqrt2}\bar u\gamma^\mu P_R D\,Y'_\mu$ + $\frac{g}{\sqrt2}\bar D\gamma^\mu P_L u\,Y'^\dagger_\mu$ | **disagree** | **Chirality.** The paper gives $g_R=0$ for this vertex. The direct term in the file is right-handed. Its own conjugate partner is left-handed, so the block is also not hermitian. |
| $\bar S\,c\,Y^{+Q_Y}$: $g_L=-\frac{ie}{\sqrt2 s_W}$, $g_R=0$ | $\frac{g}{\sqrt2}\bar c\gamma^\mu P_L S\,Y'_\mu$ + h.c. | **agree** | Chirality and strength both match ($e/s_W=g$). |
| $\bar D\,d\,V^{+Q_V}$: $g_L=-\frac{ieV_{ud}}{\sqrt2 s_W}$, $g_R=0$ | $\frac{g}{\sqrt2}\bar d\gamma^\mu P_L D\,V'_\mu$ + h.c., no CKM factor | **agree** (chirality, strength); CKM element **missing-in-reconstruction** | $V_{ud}\simeq0.974$, so the size is close, but the flavour structure is dropped. |
| $\bar S\,s\,V^{+Q_V}$: $g_L=-\frac{ieV_{cs}}{\sqrt2 s_W}$, $g_R=0$ | $\frac{g}{\sqrt2}\bar s\gamma^\mu P_L S\,V'_\mu$ + h.c., no CKM factor | **agree** (chirality, strength); CKM element **missing-in-reconstruction** | Same as the row above. |
| Overall sign $-\frac{ie}{\sqrt2 s_W}$ for every $q$–$J$–$V/Y$ vertex (Table `gauge-fermion`) | $+\frac{g}{\sqrt2}$ | **agree** | A common sign is absorbed by $Y'\to-Y'$, $V'\to-V'$. The file keeps one common sign, as the paper does. |
| $\bar t\,T\,V^{+Q_V}$: $g_L=-\frac{ie}{\sqrt2 s_W}$, $g_R=0$ (Table `gauge-fermion`) | absent | **missing-in-reconstruction** | Removes $T\to tV$ and the $t$-channel $T$ diagram in $VV$ production. |
| $\bar T\,b\,Y^{-Q_Y}$: $g_L=-\frac{ieV_{tb}}{\sqrt2 s_W}$, $g_R=0$ | absent | **missing-in-reconstruction** | Removes $T\to bY$. With the row above, $T$ is completely inert in the file. |
| $\bar e\,E_e\,Y^{+Q_Y}$ (and $\mu,\tau$): $g_L=-\frac{ie}{\sqrt2 s_W}$, $g_R=0$ | absent | **missing-in-reconstruction** | This vertex drives the paper's $pp\to YY\to\ell^+\ell^-+\met$ signature for $\beta=+1/\sqrt3$. |
| $\bar\nu_\ell\,E_\ell\,V^{+Q_V}$: $g_L=-\frac{ie}{\sqrt2 s_W}$, $g_R=0$ | absent | **missing-in-reconstruction** | Drives $V\to\nu E_\ell$, the invisible mode. |
| $Z'$ couplings to all SM fermions, $\bar DDZ'$, $\bar SSZ'$, $\bar TTZ'$, $\bar E_\ell E_\ell Z'$ with non-zero $g_L$ **and** $g_R$ (Table `gauge-fermion`, Eq. `\eqref{eq:effcoup}`, Eq. `\eqref{Zpuu}`) | absent; `Zp` has no interaction at all | **missing-in-reconstruction** | This is the paper's main phenomenology (Drell-Yan $Z'$, $A_{FB}$, $Z'$-mediated heavy-quark pairs). Note these couplings are chiral but **not** purely left-handed. |
| $V_{Higgs}$ with $\mu_i^2,\lambda_1,\lambda_2,\lambda_3,\lambda_{12},\lambda_{13},\lambda_{23},\lambda'_{12},\lambda'_{13},\lambda'_{23},f$ (Eq. `\eqref{VHiggs}`) | only `lam3`, `lampr12`, `lampr23`, `lampr13`, `k` appear, and only inside mass formulas | **missing-in-reconstruction** | No scalar self-interaction is implemented; $\lambda_1,\lambda_2,\lambda_{12},\lambda_{13},\lambda_{23},\mu_i$ never appear. |
| $f=kv_3$, $k\sim O(1)$ (Sec. 2.1) | `f` $=k v_3$, `k` $=1.0$ | **agree** | |
| $v^2=v_1^2+v_2^2=246$ GeV (Sec. 2.1.1) | `v2` $=\sqrt{v_{\rm SM}^2-v_1^2}$ | **agree** | $v_1=173.95$ gives $v_2\simeq174.3$. |
| $M_{H_2}^2=\frac{v^2}{v_1v_2}fv_3$ (Eq. `\eqref{4}`) | `MH2` | **agree** | |
| $M_{H_3}^2=2\lambda_3v_3^2$ (Eq. `\eqref{5}`) | `MH3` | **agree** | |
| $M_{H_0}^2=(\frac{v_1v_2}{v_3}+\frac{v_1v_3}{v_2}+\frac{v_2v_3}{v_1})f$ (Sec. 2.5) | `MH0` | **agree** | The reconstruction also identifies $H_0$ as the CP-odd state, which matches the paper. |
| $M_{H^\pm}^2=\frac{2fv_3+\lambda'_{12}v_1v_2}{2v_1v_2}v^2$ (Sec. 2.5) | `MHpm` | **agree** | |
| $M_{H^{\pm Q_Y}}^2=\frac{2fv_1+\lambda'_{23}v_2v_3}{2v_2v_3}(v_2^2+v_3^2)$ | `MHQY` | **agree** | |
| $M_{H^{\pm Q_V}}^2=\frac{2fv_2+\lambda'_{13}v_1v_3}{2v_1v_3}(v_1^2+v_3^2)$ | `MHQV` | **agree** | |
| $h$ (125 GeV), $m_h^2$, mixing matrices $U$ and $O$, Goldstones $G_Z,G_{Z'},G^\pm,G^{\pm Q_Y},G^{\pm Q_V}$ (Sec. 2.1.1, 2.1.2, App. B) | absent | **missing-in-reconstruction** | $h$ may come from the SM base file, but the three-state mixing that defines $h,H_2,H_3$ is not implemented. |
| $(D_\mu\chi)^\dagger(D^\mu\chi)$ etc. giving $W$, $Z$, $Z'$, $V$, $Y$ couplings to every scalar (Tables `1gauge-2scalars`, `2gauges-1scalar`, `2gauges-2scalars`) | `LHpm`, `LHQY` keep only $\gamma$ and $Z$; `LHQV` keeps nothing | **missing-in-reconstruction** | For example $ZH^{+Q_V}H^{-Q_V}\ne0$ although $Q_V=0$, and $W^+H^{-Q_V}H^{-Q_Y}\ne0$. |
| Scalar–fermion couplings, e.g. $H^{+Q_Y}\bar u D=\sqrt2(\frac{s_{23}m_u}{v_2}P_L+\frac{c_{23}M_D}{v_3}P_R)$ (Table `scalar-fermion`) | absent | **missing-in-reconstruction** | These are genuinely two-chirality couplings in the paper. Their absence removes $T\to tH^{Q_V}$ and the charged-Higgs decay modes. |
| Residual $Z_2$: $Z_2(E_\ell,D,S,T)=-$, $Z_2(Y,V)=-$, $Z_2(H^{\pm Q_Y},H^{\pm Q_V})=-$ (Eqs. `\eqref{eq:odd1}`–`\eqref{eq:odd3}`) | not declared | **missing-in-reconstruction** | The surviving `LNPcc` vertices each join one $Z_2$-even and two $Z_2$-odd states, so the file does not break $Z_2$. It just does not state it. |
| $\mathcal{L}_{total}$ = sum of all sectors | `LTotal` = sum of the 14 blocks | **agree** | The sum is internally consistent with what the file declares. |

No term in the reconstruction describes a field or an interaction that the paper's model
does not contain. I found no **extra-in-reconstruction** item. The $P_R$ term of
row "$\bar D u Y^{+Q_Y}$" is a changed term, not an added one.

---

## 2. Disagreements, with severity

1. **$u$–$D$–$Y'$ chirality is right-handed instead of left-handed.**
   Severity: **substantive**.
   A human should compare the file's `ProjP` in the first `LNPcc` term with Table
   `gauge-fermion`, which gives $g_R=0$ for $\bar D u Y^{+Q_Y}$, and with the $A^D$
   amplitude in Sec. 5.1.1, which uses $P_L$ on both sides.

2. **`LNPcc` is not hermitian.**
   Severity: **substantive**.
   A human should check that the `HC[...]` block and the direct block use the same
   projector; at present one vertex is $P_R$ in one direction and $P_L$ in the other, so
   the Lagrangian is not real and the $u$–$D$–$Y'$ amplitude is not unitary.

3. **$M_{Z'}$ is too small by $\sqrt2$.**
   Severity: **substantive**.
   A human should re-derive $M_{Z'}^2$ from the paper: $\mathcal{L}\supset\frac16(g^2+\beta^2g_X^2)v_3^2Z'^2$
   equals $\frac12M^2Z'^2$, so $M_{Z'}^2=\frac13(g^2+\beta^2g_X^2)v_3^2$, and this agrees
   with Eq. `\eqref{3}`.

4. **$g_X$ is an independent input in the file but is fixed by $g$ and $s_W$ in the paper.**
   Severity: **substantive**.
   A human should decide whether the model file must impose $g_Y=gg_X/\sqrt{g^2+\beta^2g_X^2}$;
   with $g_X=0.5$ the electroweak sector and the $Z'$ mass are not consistent.

5. **CKM elements $V_{ud}$ and $V_{cs}$ are missing from the $D$–$d$–$V'$ and $S$–$s$–$V'$ vertices.**
   Severity: **convention**.
   A human should confirm the file's intent to set $V_L=\mathbb{1}$; the paper instead
   assumes $V_L=V_{\rm CKM}$, $U_L=\mathbb{1}$.

6. **$Y'$ has no photon coupling and no covariant field strength; all three heavy vector masses are hand-written.**
   Severity: **substantive**.
   A human should check whether the file is meant to be a gauge-invariant model or only a
   low-energy effective set of vertices, because a charged vector without a $\gamma Y^+Y^-$
   vertex violates electromagnetic gauge invariance.

7. **$V'$ has no $Z$ or $Z'$ coupling although the paper gives $ZV^+V^-$ and $Z'V^+V^-$ non-zero values.**
   Severity: **substantive**.
   A human should check Table `gauges`: a neutral non-abelian gauge boson still couples to
   $Z$ and $Z'$.

8. **All $Z'$ couplings to fermions are absent, so `Zp` is inert.**
   Severity: **substantive**.
   A human should check Table `gauge-fermion` and Eq. `\eqref{eq:effcoup}`, because $Z'$
   production and decay is the paper's central result and needs both $g_L$ and $g_R$.

9. **Third-generation couplings $t$–$T$–$V'$ and $T$–$b$–$Y'$ are absent, so `TQ` is inert.**
   Severity: **substantive**.
   A human should check the $q_{3L}=(b,-t,T)_L$ anti-triplet of Sec. 2.3 and the
   corresponding rows of Table `gauge-fermion`.

10. **Lepton couplings $e$–$E_\ell$–$Y'$ and $\nu_\ell$–$E_\ell$–$V'$ are absent, so `EL` is inert.**
    Severity: **substantive**.
    A human should check the lepton anti-triplets of Sec. 2.3 and the first and fourth rows
    of Table `gauge-fermion`.

11. **Gauge self-couplings (VVV and VVVV) are absent.**
    Severity: **substantive**.
    A human should check Table `gauges`, because the paper produces $V$ and $Y$ in pairs
    mainly through $\gamma/Z/Z'$ triple gauge vertices.

12. **The whole scalar sector beyond free masses is absent: potential, $h$, mixing matrices $U$ and $O$, gauge–scalar couplings, scalar–fermion couplings.**
    Severity: **substantive**.
    A human should decide whether the file is a deliberate "spectrum-only" subset; if not,
    Eq. `\eqref{VHiggs}`, App. B and Tables `1gauge-2scalars`, `2gauges-1scalar`,
    `2gauges-2scalars`, `scalar-fermion` are all unimplemented.

13. **Benchmark inputs give a $Z'$ far below the paper's own limit.**
    Severity: **substantive** (parameter choice, not Lagrangian structure).
    A human should check that $v_3=2$ TeV with $g_X=0.5$ gives $M_{Z'}\simeq0.6$–$0.8$ TeV,
    while Sec. 4.3 quotes $M_{Z'}\gtrsim3.6$–$4$ TeV for $\beta=+1/\sqrt3$ and uses a 4 TeV
    benchmark.

14. **Overall sign of the $g/\sqrt2$ charged-current block.**
    Severity: **cosmetic**.
    A human can absorb the sign by $Y'\to-Y'$, $V'\to-V'$; the file keeps one common sign,
    as the paper does.

15. **`FullName` says "heavy charged lepton" while $Q=0$.**
    Severity: **cosmetic**.
    A human should confirm the string is a leftover from another $\beta$ branch: Table
    `tbl:charge` gives $Q_{E_\ell}=0$ only for $\beta=+1/\sqrt3$, so the reconstruction's
    reading is right and only the name is wrong.

---

## 3. Overall assessment

The reconstruction identifies the model correctly. It is the $\beta=+1/\sqrt3$ branch of the
331 model of Cao and Zhang, and every electric charge, colour representation, generation
count and scalar mass formula in the reconstruction's tables matches Table `tbl:charge` and
Sec. 2.5 of the paper term for term. Eight of the nine mass formulas reproduce the paper
exactly; only $M_{Z'}$ differs, by a factor $\sqrt2$ that comes from reading the Lagrangian
coefficient $\frac16(g^2+\beta^2g_X^2)v_3^2$ as $M^2$ instead of as $\frac12M^2$. The
reconstruction is also careful and honest about what it reads: it flags the non-hermitian
$u$–$D$–$Y'$ vertex, the missing photon coupling of $Y'$, and the name–charge conflict on
`EL`, and each of those three flags is confirmed by the paper. The one physics
disagreement inside an implemented term is the chirality of the $u$–$D$–$Y'$ coupling: the
paper's Table `gauge-fermion` gives $g_R=0$ for $\bar Du\,Y^{+Q_Y}$, and its $u\bar u\to YY$
unitarity amplitude uses $P_L$ on both sides of the $D$ propagator, so the file's `ProjP`
disagrees with the paper and, as the reconstruction itself notes, breaks hermiticity in
exactly one place. Everything else is a matter of scope: the file implements free kinetic
and mass terms plus four charged-current vertices, while the paper's model also contains the
full $Z'$–fermion couplings, the gauge self-couplings, the third-generation and lepton
$V$/$Y$ vertices, the Higgs potential with its mixing matrices, and all gauge–scalar and
scalar–fermion couplings. Whether that reduced scope is intended, and whether the single
$P_R$ is a typing error or a deliberate change, is for the human reviewer to decide.
