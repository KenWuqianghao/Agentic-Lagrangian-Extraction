Now let me produce the self-audit table and final verification.

## Self-Audit Table

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4 - d) | 1/Lambda power present (must be d - 4, or "n/a" if d ≤ 4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | sum of new U(1)_X charge | lepton/baryon number sum | CC[] used where paper writes psi^c | fraction/root placement checked against | Hermitian partner |
|-----------|------------------------|---------------------------|-----------------|------------------------------------------|------------------------------------------------------------|-------|-------|-------------------|-------------------|--------------------------|--------------------------|-----------------------------------|----------------------------------------|-------------------|
| LZpFree (kinetic) | Zp (vector) | 4 | 1 (implicit) | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conjugate |
| LZpFree (mass) | Zp Zp | 2 (Z²) | MZp² | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conjugate |
| LPhiXFree (kinetic) | DCΦX† DCΦX | 4 | 1 (implicit) | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | HC |
| LPhiXFree (mass) | ΦX† ΦX | 2 | MPhiX² | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | HC |
| LNRFree (kinetic) | NR† DC NR | 4 | 1 (implicit) | 0 | n/a | 0 | 0 | singlet | singlet | 0 | L=0 | n/a | n/a | HC |
| LNRFree (mass) | NR† NR | 3 | MNR | 1 | n/a | 0 | 0 | singlet | singlet | 0 | L=0 | n/a | n/a | HC |
| VPotInt (λΦ) | (ΦX†ΦX)² | 4 | lamPhi | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conjugate |
| VPotInt (λ') | (Φ†Φ)(ΦX†ΦX) | 4 | lamPrime | 0 | n/a | 0 | 0 | shared index ii | singlet | 0 | 0 | n/a | n/a | self-conjugate |
| LYukNu | LL† Phibar NR | 4 | Ynu | 0 | n/a | 0 | 0 | shared index ii | singlet | 0 | L=0 | n/a | n/a | HC |
| HC[LYukNu] | NR† Phi LL | 4 | Ynu* | 0 | n/a | 0 | 0 | shared index ii | singlet | 0 | L=0 | n/a | n/a | HC |
| LYukMajorana | ΦX CC[NR†] NR | 4 | YN | 0 | n/a | 0 | 0 | singlet | singlet | 0 | L=0 | yes (paper: N_R^c) | n/a (LaTeX: \bar{N}_R^c) | HC |
| HC[LYukMajorana] | NR† CC[NR] ΦX† | 4 | YN* | 0 | n/a | 0 | 0 | singlet | singlet | 0 | L=0 | yes | n/a | HC |

**Free-field term verification (one row per new class):**
- Zp (V[100]): LZpFree = -1/4 FS² + 1/2 MZp² Zp² included in LNew → LTotal ✓
- PhiX (S[100]): LPhiXFree = DCΦX† DCΦX - MPhiX² ΦX†ΦX included in LNew → LTotal ✓
- NR (F[100]): LNRFree = I NR† DC NR - MNR NR†NR included in LNew → LTotal ✓

**Non-fundamental colour representations:** None (all new fields are SU(3) singlets) ✓

**SelfConjugate → True classes with no QuantumNumbers:**
- Zp (V[100]): SelfConjugate=True, no QuantumNumbers assigned ✓

**Name conflict check:** All class names (PhiX, NR, Zp), parameter names (gX, xH, vPhi, lamPhi, lamPrime, MZp, Ynu, YN, MPhiX, MNR1/2/3, WPhiX, WNR, WZp), and index names use no Mathematica built-ins, FeynRules symbols (N, C, D, E, I, K, O, HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM), or SM.fr names (H, Phi, Z, W, A, G, ee, gs, gw, sw, cw, vev, MZ, MW, etc.). No primes/punctuation in ParticleName/AntiParticleName. Class indices ≥ 100 ✓

**Total Lagrangian:** Single LTotal := LSM + LNew, where LNew = LZpFree + LPhiXFree + LNRFree - VPotInt + LYukNu + HC[LYukNu] + LYukMajorana + HC[LYukMajorana] ✓

**Reference/cached model file read:** None (only paper/2104.10902_source.tex and SM.fr were read) ✓

---

The model.fr file is written and complete.