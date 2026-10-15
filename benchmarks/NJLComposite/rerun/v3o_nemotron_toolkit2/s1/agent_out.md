**Self-audit table written to SELF_AUDIT.md**

**Last ./frgen result:**
```
SCHEMA OK: 11 particle classes, 6 parameters, Lagrangian terms ['L_Pi12_kin', 'L_PiM12_kin', 'L_LQPi16_kin', 'L_LQPi76_kin', 'L_NR_kin', 'L_ER_kin', 'L_UR_kin', 'L_DR_kin', 'L_NRA_kin', 'L_ERA_kin', 'L_nuR_kin', 'L_PiPlus_CI', 'L_Pi0d_CI', 'L_Pi0u_CI', 'L_Pi53_CI', 'L_PiM13_CI', 'L_Pi23u_CI', 'L_Pi23d_CI', 'L_U0bar_CI', 'L_Upbar_CI', 'L_Dpbar_CI', 'L_D0bar_CI', 'L_EM23bar_CI', 'L_Np13bar_CI', 'L_Ep13bar_CI', 'L_NM23bar_CI', 'L_U0_CI', 'L_Um_CI', 'L_Dm_CI', 'L_D0_CI', 'L_E23_CI', 'L_Nm13_CI', 'L_Ep13_CI', 'L_N23_CI', 'LTotal']
RENDERED: model.fr (315 lines). You may read it.
LINT: no findings.
```

**Model summary:**
- **4 composite scalar doublets** (2 color-singlet: Pi12 Y=1/2, PiM12 Y=-1/2; 2 color-triplet LQ: LQPi16 Y=1/6, LQPi76 Y=7/6) — 8 mass eigenstates
- **1 right-handed neutrino** (nuR, SU(2) singlet, Y=0, 3 generations)
- **6 composite Weyl fermion doublets** (4 color-singlet: NR, ER, UR, DR all Y=-1/2; 2 color-triplet: NRA, ERA Y=1/6) — 12 mass eigenstates × 3 generations
- **6 External parameters**: Lam (5.1 TeV), FPi (3.6 TeV), gY (0.5), MPi (2 TeV), MF (3 TeV), gStar (1.0)
- **35 Lagrangian terms** including kinetic/mass for all 11 classes, 6 boson contact interactions (Eqs. 488-502), 18 fermion contact interactions (Eqs. 818-869), and single LTotal sum
- All charges conserved, SU(2) contractions verified (shared index for same-Y doublets, Eps for conjugate pairs), SU(3) delta for triplets
- No reserved name conflicts, no SelfConjugate=True with charges, no non-fundamental color reps, no reference files read