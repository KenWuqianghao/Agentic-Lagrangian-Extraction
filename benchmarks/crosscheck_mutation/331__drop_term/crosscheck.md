# Cross-check: `reconstruction.md` against Cao & Zhang, "Collider Phenomenology of the 3-3-1 Model"

RUN-TAG: XM-CROSS-331__drop_term

## 0. Where the paper defines the model

The paper defines the model in Sec. 2 ("The Model"), in four blocks:

| block | location |
|---|---|
| Symmetry breaking, Higgs triplets, VEVs | Sec. 2.1, Eq. (1) and the VEV equation |
| Charge operator and $X$ quantum numbers | Sec. 2.1, Eqs. (xqn), $Q=T^3+\beta T^8+X$ |
| Higgs Lagrangian and potential | Sec. 2.1, $\mathcal{L}_{Higgs}$ and Eq. (VHiggs) |
| Neutral / charged scalar mass matrices and eigenvalues | Sec. 2.1.1, Eq. (Neutral even mass mixing); Sec. 2.1.2 |
| Gauge Lagrangian and gauge masses | Sec. 2.2, $\mathcal{L}_{Gauge}$, Eqs. (0), (Gmu), (gauge mass), (MVY), (ZP), (3) |
| Fermion Lagrangian and representations | Sec. 2.3, $\mathcal{L}_{\rm Fermion}=\bar\psi^\alpha i D_\mu\gamma^\mu\psi^\alpha$ |
| Yukawa Lagrangian | Sec. 2.4, $\mathcal{L}^q_{Yuk}$, $\mathcal{L}^l_{Yuk}$ |
| Charges and full mass spectrum | Sec. 2.5, Table "Electric charges", Eqs. (4), (5), (3), (MVY) |
| All interaction vertices | Appendix A, Tables `1gauge-2scalars`, `2gauges-1scalar`, `2gauges-2scalars`, `gauges`, `gauge-fermion`, `scalar-fermion` |
| Scalar mixing matrices $U$, $O$ | Appendix B, Eqs. (U), (O) |

The reconstruction selects the benchmark $\beta=+1/\sqrt3$. All charges in the
reconstruction match the paper's Table of electric charges for that column:
$Q_{D}=Q_{S}=-1/3$, $Q_T=+2/3$, $Q_{E_\ell}=0$, $Q_V=0$, $Q_Y=+1$,
$Q_{H^{\pm Q_V}}=0$, $Q_{H^{\pm Q_Y}}=+1$, $Q_{H^\pm}=+1$.

The reconstruction is written in the **broken phase**: it adds mass-eigenstate
fields on top of an SM host file. The paper writes the model in the **unbroken
phase** ($SU(3)_C\times SU(3)_L\times U(1)_X$) and then lists the broken-phase
vertices in Appendix A. A broken-phase file is a valid way to encode the same
physics, but only if every Appendix-A vertex is written by hand. The comparison
below uses this rule.

---

## 1. Term-by-term comparison

### 1.1 Gauge sector

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Gauge group $SU(3)_C\times SU(3)_L\times U(1)_X$ (Sec. 2, Sec. 2.1 breaking chain) | no new gauge group; $SU(3)_C\times SU(2)_L\times U(1)_Y$ of the host SM file | **disagree** | Broken-phase choice. It is acceptable only with hand-written vertices, which are absent. |
| $\mathcal{L}_{Gauge}=-\frac14 F^i_{\mu\nu}F^{i\mu\nu}-\frac14 B_{\mu\nu}B^{\mu\nu}$ (Sec. 2.2) — kinetic normalisation of the mass eigenstates | $-\frac14 F^{Z'}F^{Z'}$; $-\frac12 F^{Y\dagger}F^{Y}$; $-\frac12 F^{V\dagger}F^{V}$ | **agree** | Real field gets $-1/4$, complex fields get $-1/2$. This is the correct Proca normalisation. |
| Non-abelian part of $F^i_{\mu\nu}$ → triple gauge vertices $AVV$, $AYY$, $ZVV$, $ZYY$, $Z'VV$, $Z'YY$, $V^-W^+Y^+$ (Table `gauges`) | none | **missing-in-reconstruction** | `FS[V,mu,nu]` is the free abelian field strength, so no self-coupling is produced. |
| Quartic gauge vertices $AAVV$, $AAYY$, $VVVV$, $YYYY$, $WWZZ$, $VVZZ'$, ... (Table `gauges`) | none | **missing-in-reconstruction** | Same cause. |
| $\gamma Y^{+Q_Y}Y^{-Q_Y}=\frac{i}{2}a_+e = ie$ for $\beta=+1/\sqrt3$ (Table `gauges`) | none; $Y^\pm$ has an ordinary derivative | **disagree** | The reconstruction itself flags this. A field with $Q=+1$ must couple to the photon. |
| $Z V^{+Q_V}V^{-Q_V}=-\frac{ie(1+a_-s_W^2)}{2c_Ws_W}$, non-zero at $\beta=+1/\sqrt3$ (Table `gauges`) | none; $V^0$ has $Q=0$ and an ordinary derivative | **disagree** | $V^0$ is electrically neutral here but still carries weak isospin, so $ZVV$ does not vanish. |
| $M^2_{W^\pm}=\frac{g^2}{4}v^2$ (Eq. MVY) | not declared (host SM) | **agree** | Correctly left to the host file. |
| $M^2_{Y^{\pm Q_Y}}=\frac{g^2}{4}(v_3^2+v_2^2)$ (Eq. MVY) | `MYp` $=\sqrt{g_w^2(v_3^2+v_2^2)/4}$ | **agree** | Exact match, including which VEV pairs with which boson. |
| $M^2_{V^{\pm Q_V}}=\frac{g^2}{4}(v_3^2+v_1^2)$ (Eq. MVY) | `MVp` $=\sqrt{g_w^2(v_3^2+v_1^2)/4}$ | **agree** | Exact match. |
| $M^2_{Z'}=\frac13(g^2+\beta^2g_X^2)v_3^2$ — from $\mathcal{L}^{mass}_{Gauge}\supset\frac16(g^2+\beta^2g_X^2)v_3^2Z'^2_\mu$ with $\frac12M^2Z'^2$ normalisation; identical to Eq. (3) after substituting $g_Y$ | `MZp` $=\sqrt{(g_w^2+\beta^2g_X^2)v_3^2/6}$ | **disagree** | $M^2$ is a factor **2 too small**. The file appears to read the Lagrangian coefficient $1/6$ as the mass itself and drop the $\frac12$ of the Proca mass term. |
| $M^2_{Z'}$ sub-leading piece $\frac{g^4+2\beta^2g^2g_X^2+\beta^2(\beta^2+3)g_X^4}{6(g^2+\beta^2g_X^2)}v^2$ (Sec. 2.2, same equation), i.e. the $v_1^2$ and $v_2^2$ terms of the expanded $M^2_{Z'}$ | absent | **missing-in-reconstruction** | This is a complete term of the paper's $M_{Z'}$ formula, and it is the single clearest candidate for a dropped term. |
| $M^2_{Z'}=\frac{4c_W^2}{3[1-(1+\beta^2)s_W^2]}M^2_{Y(V)}+\mathcal{O}(v_1^2)$ (Eq. zpvy) | not satisfied by `MZp`, `MYp`, `MVp` as written | **disagree** | Consequence of the factor 2. The relation holds exactly with $M^2_{Z'}=A v_3^2/3$, and fails by 2 with $A v_3^2/6$. |
| $g_Y=\frac{gg_X}{\sqrt{g^2+\beta^2g_X^2}}$ (Sec. 2.2), so $g_X$ is **fixed** by $g$, $s_W$ and $\beta$ | `gX` declared external, value $0.5$ | **disagree** | With SM inputs and $\beta=1/\sqrt3$, the paper gives $g_X\simeq0.38$. The value $0.5$ implies $s_W^2\simeq0.33$. |
| $Z'_\mu=-s_{331}W^8_\mu+c_{331}X_\mu$, real neutral (Eq. ZP) | `Zp`, `SelfConjugate -> True`, $Q=0$ | **agree** | |
| $\beta=\pm\sqrt3,\pm1/\sqrt3$; $Q=T^3+\beta T^8+X$ (Sec. 2.1, Sec. 2.5) | `beta` $=1/\sqrt3$, same charge operator described | **agree** | One of the paper's four benchmarks. |

### 1.2 Scalar sector

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| $\mathcal{L}^{kinetic}_{Higgs}=(D_\mu\rho)^\dagger(D^\mu\rho)+(D_\mu\eta)^\dagger(D^\mu\eta)+(D_\mu\chi)^\dagger(D^\mu\chi)$ (Eq. 0) | kinetic terms for `H2`, `H3`, `H0`, `Hpm`, `HQY`, `HQV` | **agree** (form only) | Real neutral scalars correctly use $\partial_\mu$. Charged scalars use `DC`. See the $Z$-coupling rows below. |
| $V_{Higgs}$: $\mu_1^2,\mu_2^2,\mu_3^2$, $\lambda_1,\lambda_2,\lambda_3$, $\lambda_{12},\lambda_{13},\lambda_{23}$, $\lambda'_{12},\lambda'_{13},\lambda'_{23}$, $\sqrt2f\epsilon_{ijk}\rho^i\eta^j\chi^k+h.c.$ (Eq. VHiggs) | none | **missing-in-reconstruction** | No cubic and no quartic scalar vertex exists. $\lambda_3$ and $\lambda'_{ij}$ survive only inside mass formulas. |
| $\mu_i^2$, $\lambda_1$, $\lambda_2$, $\lambda_{12}$, $\lambda_{13}$, $\lambda_{23}$ as model parameters (Eq. VHiggs) | not declared at all | **missing-in-reconstruction** | Only $\lambda_3$, $\lambda'_{12}$, $\lambda'_{13}$, $\lambda'_{23}$, $k$ are present. |
| $f=kv_3$, $k\sim\mathcal{O}(1)$ (Sec. 2.1) | internal `f` $=k\,v_3$, `k` $=1$ | **agree** | |
| $v^2=v_1^2+v_2^2=(246\ {\rm GeV})^2$ (Sec. 2.1) | internal `v2` $=\sqrt{v^2-v_1^2}$, `v1` $=173.95$ GeV | **agree** | Reproduces the paper's $M_W$ constraint and the benchmark $v_1\simeq v_2\simeq174$ GeV. |
| $m_h^2=\frac{2(\lambda_1v_1^4+\lambda_{12}v_1^2v_2^2+\lambda_2v_2^4)}{v^2}$ (Eq. 4) | absent; $h$ is the host SM Higgs with the SM mass | **missing-in-reconstruction** | The 331 relation for the 125 GeV state is not encoded. |
| $M^2_{H_2}=\frac{v^2}{v_1v_2}fv_3$ (Eq. 4) | `MH2` $=\sqrt{\frac{v^2}{v_1v_2}fv_3}$ | **agree** | |
| $M^2_{H_3}=2\lambda_3v_3^2$ (Eq. 5) | `MH3` $=\sqrt{2\lambda_3v_3^2}$ | **agree** | |
| $M^2_{H_0}=(\frac{v_1v_2}{v_3}+\frac{v_1v_3}{v_2}+\frac{v_2v_3}{v_1})f$ (Eq. 5, CP-odd) | `MH0` identical | **agree** | Equal to the Sec. 2.1.1 form $f(v_1^2v_2^2+v_3^2v_2^2+v_1^2v_3^2)/(v_1v_2v_3)$. |
| $M^2_{H^\pm}=\frac{2fv_3+\lambda'_{12}v_1v_2}{2v_1v_2}v^2$ (Sec. 2.1.2, Sec. 2.5) | `MHpm` identical | **agree** | Correct pairing with $\lambda'_{12}$. |
| $M^2_{H^{\pm Q_Y}}=\frac{2fv_1+\lambda'_{23}v_2v_3}{2v_2v_3}(v_2^2+v_3^2)$ (Sec. 2.1.2, Sec. 2.5) | `MHQY` identical | **agree** | Correct pairing with $\lambda'_{23}$. |
| $M^2_{H^{\pm Q_V}}=\frac{2fv_2+\lambda'_{13}v_1v_3}{2v_1v_3}(v_1^2+v_3^2)$ (Sec. 2.1.2, Sec. 2.5) | `MHQV` identical | **agree** | Correct pairing with $\lambda'_{13}$. |
| Goldstone bosons $G_Z$, $G_{Z'}$, $G^\pm$, $G^{\pm Q_Y}$, $G^{\pm Q_V}$ (Sec. 2.1.1, Sec. 2.1.2) | absent | **agree** | Correct for a unitary-gauge file, which the paper also uses in Appendix A. |
| CP-even mixing matrix $U_{ij}$ (Eq. U, Appendix B) and CP-odd mixing matrix $O_{ij}$ (Appendix B) | absent | **missing-in-reconstruction** | Nearly every Appendix-A vertex carries $U_{ij}$ or $O_{ij}$. |
| $s_{12},c_{12}$; $s_{23},c_{23}$ (Eq. sc23); $s_{13},c_{13}$ (Eq. sc13) | absent | **missing-in-reconstruction** | These angles control the charged-scalar vertices and the heavy-quark decays. |
| $H_2,H_3$ CP-even and $H_0$ CP-odd, all real neutral (Sec. 2.5) | three real self-conjugate neutral scalars | **agree** | The CP quantum number itself is not encoded, but no term in the file needs it. |
| $ZH^+H^-=\frac{ie(p_1-p_2)^\mu(c_W^2-s_W^2)}{2c_Ws_W}$ (Table `1gauge-2scalars`) | `Hpm` declared $SU(2)_L$ singlet with $Y=+1$, giving $-e\tan\theta_W$ | **disagree** | The photon vertex comes out right; the $Z$ vertex does not. $H^\pm$ mixes $\rho^\pm$ and $\eta^\pm$, which carry $T^3=\pm1/2$. |
| $ZH^{+Q_Y}H^{-Q_Y}=\frac{ie(p_1-p_2)^\mu[c_{23}^2(a_+s_W^2-1)+a_+s_{23}^2s_W^2]}{2c_Ws_W}$ (Table `1gauge-2scalars`) | same singlet treatment as `Hpm` | **disagree** | Same cause; the $s_{23},c_{23}$ structure is lost. |
| $ZH^{+Q_V}H^{-Q_V}$, non-zero at $\beta=+1/\sqrt3$ (Table `1gauge-2scalars`) | `HQV` has $Q=Y=0$, so `DC` collapses to $\partial_\mu$ | **disagree** | A state that is electrically neutral still couples to $Z$ here. |
| $VSS$ table: $V^{+Q_V}H^{-Q_V}h$, $W^+H^-h$, $Y^{+Q_Y}H^{-Q_Y}H_0$, $Z'H_2H_0$, ... (Table `1gauge-2scalars`) | none | **missing-in-reconstruction** | |
| $VVS$ table: $VVh$, $YYh$, $ZZ'h$, $Z'Z'H_3$, $AW^+H^-$, ... (Table `2gauges-1scalar`) | none | **missing-in-reconstruction** | These carry the $v_iU_{ij}$ structure used in the Higgs fit. |
| $VVSS$ table: $AAH^+H^-$, $W^+W^-hh$, $Z'Z'H_0H_0$, ... (Table `2gauges-2scalars`) | none | **missing-in-reconstruction** | |
| Higgs trilinear $\lambda_{hhh}=(1+\frac{kv_1v_2U_{31}^2}{m_h^2})\frac{3m_h^2}{v}$ (Sec. 3.3) | none | **missing-in-reconstruction** | Follows from the missing potential. |

### 1.3 Fermion sector

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| $\mathcal{L}_{\rm Fermion}=\bar\psi^\alpha iD_\mu\gamma^\mu\psi^\alpha$ with $q_{1L},q_{2L}$ triplets, $q_{3L}$ anti-triplet, all $l_{L}$ anti-triplets (Sec. 2.3) | Dirac kinetic terms $i\bar\psi\gamma^\mu D_\mu\psi$ for `DQ`, `SQ`, `TQ`, `EL` with the SM covariant derivative only | **disagree** | The SM subgroup part survives. The $SU(3)_L$ structure, and with it the non-universal third generation, is lost. |
| $Q_D=Q_S=\frac16-\frac{\sqrt3}{2}\beta=-\frac13$, $Q_T=+\frac23$ (Sec. 2.3, Table of charges) | `DQ`, `SQ` $Q=Y=-1/3$; `TQ` $Q=Y=+2/3$; colour triplets | **agree** | $Y=Q$ is right for $SU(2)_L$ singlets. |
| $Q_{E_\ell}=-\frac12+\frac{\sqrt3}{2}\beta=0$, three generations (Sec. 2.3) | `EL`, three members, $Q=Y=0$, colourless | **agree** | |
| $\bar DDA=-\frac{i(3\sqrt3\beta-1)e}{6}=-\frac{ie}{3}$, $\bar TTA=+\frac{2ie}{3}$ (Table `gauge-fermion`) | generated automatically by `DC` from $Y=Q$ | **agree** | |
| $\bar DDZ,\ \bar SSZ,\ \bar TTZ$ (Table `gauge-fermion`) | generated by `DC`, $\propto -eQ\tan\theta_W$ | **agree** | Correct for $T^3=0$ singlets, which is what these states are. |
| $\bar E_\ell E_\ell A=\frac{ia_-e}{2}=0$ and $\bar E_\ell E_\ell Z=0$ at $\beta=+1/\sqrt3$ (Table `gauge-fermion`) | $D_\mu\to\partial_\mu$ for `EL` | **agree** | Both sides give no photon and no $Z$ vertex for this $\beta$. |
| $\bar E_\ell E_\ell Z'$, $\bar DDZ'$, $\bar SSZ'$, $\bar TTZ'$ (Table `gauge-fermion`) | none | **missing-in-reconstruction** | |
| $Z'$ couplings to all SM fermions, $\mathcal{L}_f=Z'_\mu\bar f\gamma^\mu(g_LP_L+g_RP_R)f$ (Sec. 4.1, Eq. eq:effcoup; Table `gauge-fermion`) | none | **missing-in-reconstruction** | This removes Drell-Yan $Z'$ production, the whole of Sec. 4, and the $A_{FB}$ study. |
| $\bar Du\,Y^{+Q_Y}$, $\bar Sc\,Y^{+Q_Y}$, $\bar tT\,V^{+Q_V}$, $\bar Dd\,V^{+Q_V}$, $\bar Tb\,Y^{-Q_Y}$, $\bar\ell E_\ell Y^{+Q_Y}$, $\bar\nu_\ell E_\ell V^{+Q_V}$, all with $g_L=-\frac{ie}{\sqrt2s_W}$ and $g_R=0$ (Table `gauge-fermion`) | none | **missing-in-reconstruction** | These are the vertices that make $D,S,T,E_\ell$ decay and that give the $Z_2$-odd sector its phenomenology. |
| Pure left-handed chirality ($g_R=0$) of the $V$ and $Y$ currents (Table `gauge-fermion`) | no chiral projector anywhere in the file | **missing-in-reconstruction** | Not a sign error: the chiral structure has no carrier, because the vertices are absent. |
| $-\mathcal{L}^q_{Yuk}=y^u_{ij}\bar q_{iL}\eta u_{jR}+y^u_{3j}\bar q_{3L}\rho^*u_{jR}+y^d_{ij}\bar q_{iL}\rho d_{jR}+y^d_{3j}\bar q_{3L}\eta^*d_{jR}+y^J_{ik}\bar q_{iL}\chi J_{kR}+y^J_{33}\bar q_{3L}\chi^*J_{3R}+h.c.$ (Sec. 2.4) | none | **missing-in-reconstruction** | |
| $-\mathcal{L}^l_{Yuk}=y^e_{mn}\bar l_{mL}\eta^*e_{nR}+y^E_{mn}\bar l_{mL}\chi^*E_{nR}+h.c.$ (Sec. 2.4) | none | **missing-in-reconstruction** | |
| Scalar-fermion vertices $h\bar E_\ell E_\ell$, $H^{+Q_Y}\bar u D$, $H^{-Q_V}\bar tT$, $H^+\bar tb$, ... (Table `scalar-fermion`) | none | **missing-in-reconstruction** | This removes the $T\to tH^{Q_V}$ mode of Sec. 6.2. |
| Heavy-fermion masses free, "no restriction on them" (Sec. 2.5) | $M_{DQ}=M_{SQ}=M_{TQ}=1000$ GeV, $M_{E_e}=M_{E_\mu}=M_{E_\tau}=1000$ GeV | **agree** | Matches the paper's 1000 GeV benchmark. |
| $y^E_{mn}$ a general $3\times3$ matrix (Sec. 2.4) | diagonal and degenerate by construction | **agree** (benchmark) | The paper also treats the third triplet member as already in its mass eigenstate. |
| Vector-like Dirac nature of $D,S,T$ after SSB | bare Dirac mass, no projector | **agree** | |
| $V_{\rm CKM}=U_L^\dagger V_L$, non-universal $Z'$ couplings, tree-level FCNC (Sec. 2.4, Sec. 1) | none | **missing-in-reconstruction** | |

### 1.4 Extra content in the reconstruction

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| — | PDG codes 4000001–4000015, all widths $=1$ GeV | **extra-in-reconstruction** | Implementation bookkeeping. The paper computes the widths in Secs. 4–6. |
| — | `gX` as an independent `NPINPUTS` entry | **extra-in-reconstruction** | The paper derives $g_X$; see the gauge-sector row above. |

No other content in the reconstruction is absent from the paper. Every
parameter, field and mass formula it lists maps onto a paper object.

---

## 2. Disagreements, with severity

1. **$M_{Z'}^2$ is a factor 2 too small — substantive.**
   The paper's mass term is $\frac16(g^2+\beta^2g_X^2)v_3^2Z'^2_\mu$, and a real
   vector has $\frac12M^2Z'^2_\mu$, so $M^2_{Z'}=\frac13(g^2+\beta^2g_X^2)v_3^2$.
   A human should re-derive `MZp` from Eq. (3) and check it against Eq. (zpvy),
   which the present value violates by exactly 2.

2. **The $v^2$ (that is, $v_1^2$ and $v_2^2$) contribution to $M^2_{Z'}$ is
   absent — substantive.**
   The paper's $Z'$ mass has a second term,
   $\frac{g^4+2\beta^2g^2g_X^2+\beta^2(\beta^2+3)g_X^4}{6(g^2+\beta^2g_X^2)}v^2$.
   A human should check whether this term was present in an earlier version of
   the implementation file, because a single dropped summand in `MZp` explains
   the shape of this defect better than a transcription slip.

3. **The whole interaction sector is absent — substantive.**
   No gauge self-coupling, no fermion current, no Yukawa coupling and no scalar
   potential appears. A human should confirm whether the source file was ever
   meant to carry vertices, or whether a `LTotal` summand was removed.

4. **$Y^{\pm}$ has electric charge $+1$ but no photon coupling — substantive.**
   `FS` gives a free Proca field strength. A human should check the $\gamma YY$,
   $ZYY$ and $Z'YY$ vertices of Table `gauges` against the file.

5. **$V^0$ is neutral but must still couple to $Z$ and $Z'$ — substantive.**
   A human should check $ZV^{+Q_V}V^{-Q_V}$ and $Z'V^{+Q_V}V^{-Q_V}$ in
   Table `gauges`, both non-zero at $\beta=+1/\sqrt3$.

6. **$H^\pm$, $H^{\pm Q_Y}$ and $H^{\pm Q_V}$ are declared $SU(2)_L$ singlets —
   substantive.**
   This gives the right photon vertex but the wrong $Z$ vertex, and it gives no
   $Z$ vertex at all for the neutral $H^{Q_V}$. A human should compare the three
   $ZH^+H^-$ rows of Table `1gauge-2scalars` with the vertices the file makes.

7. **$g_X$ is an external input with value 0.5 — substantive.**
   The paper fixes $g_X$ through $g_Y=gg_X/\sqrt{g^2+\beta^2g_X^2}$. With SM
   inputs this gives $g_X\simeq0.38$ at $\beta=1/\sqrt3$. A human should decide
   whether $g_X$ may float, and if not, make it an internal parameter.

8. **The scalar mixing matrices $U$ and $O$ are absent — substantive.**
   Appendix B defines them and Appendix A uses them everywhere. A human should
   check whether the file was meant to carry them, since without them the
   $h$–$H_2$–$H_3$ system cannot reproduce Sec. 3.

9. **The $SU(3)_L$ representation assignment is not encoded — substantive.**
   The paper's key structural statement is that $q_{3L}$ is an anti-triplet while
   $q_{1L},q_{2L}$ are triplets. That statement drives the tree-level FCNC and the
   difference between $Z'\to t\bar t$ and $Z'\to u\bar u$. A human should check
   whether the file encodes it through explicit non-universal couplings.

10. **`FullName` calls `EL` "heavy charged leptons" while $Q=0$ — cosmetic.**
    At $\beta=+1/\sqrt3$ the paper gives $Q_{E_\ell}=0$, so the quantum numbers
    are right and only the label is wrong. A human should fix the string.

11. **All widths are set to 1 GeV — convention.**
    The paper computes them. A human should replace them with computed widths
    before any rate is quoted.

12. **One benchmark point is hard-coded ($\beta=1/\sqrt3$, $v_1=173.95$,
    $v_3=2000$, $k=1$, $\lambda_3=\lambda'_{ij}=0.1$) — convention.**
    The paper studies four $\beta$ values. A human should check that the
    intended scope is this one benchmark.

---

## 3. Overall assessment

The reconstruction agrees with the paper on everything that concerns particle
content and tree-level mass formulas. The field list is complete and correct for
the $\beta=+1/\sqrt3$ benchmark: three new gauge bosons, three exotic quarks with
the right colour and electric charges, three heavy neutral leptons, three real
neutral scalars, two singly-charged scalars and one complex neutral scalar. Nine
of the paper's mass expressions reproduce exactly, including the pairing of each
$\lambda'_{ij}$ with the right scalar and of each VEV with the right gauge boson,
which is strong evidence that the implementation was built from this paper. The
exception in this block is $M_{Z'}$, which is a factor 2 below the paper's value
and is missing the paper's $v^2$-proportional term; the second point is the most
likely site of a removed summand, and the first may share the same origin. On the
interaction side the two documents do not meet at all: the paper devotes an entire
appendix to six tables of vertices, and the reconstruction reports a Lagrangian
built only from kinetic and mass terms, so the $Z'$ currents, the $V$ and $Y$
charged currents, the Yukawa sector and the scalar potential have no counterpart.
Three further defects follow from the broken-phase encoding rather than from
omission: the charged and neutral scalars and the $V$ and $Y$ vectors are declared
as $SU(2)_L$ singlets with free field strengths, so their photon couplings come out
right while their $Z$ and $Z'$ couplings are wrong or absent. A reviewer should
first establish whether the implementation file was ever intended to carry the
interaction sector, because that single fact decides whether this is one missing
term or a systematically incomplete model.
