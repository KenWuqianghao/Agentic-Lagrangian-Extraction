## Self-audit

### Terms in LTotal

| Term | Fields in monomial | d | Coupling | Coupling dim (4−d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | New U(1) sum | Lepton/Baryon sum | CC[] vs paper | Fraction/root | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LN4kin (kinetic) | n4bar, n4, ∂ | 4 | I/2 | 0 | none | 0 | 0 | n/a (singlet) | n/a (singlet) | none (LNLS: 0) | n4: no QuantumNumbers (Majorana); sum 0 | CC[] not used (Majorana mass as n4bar.n4, not CC[n4bar.n4]) | I/2, −1/2 match paper FR Majorana kinetic form | Self-conjugate: term is real; no HC needed |
| LN4kin (mass) | n4bar, n4 | 3 | Mn4 | 1 | none | 0 | 0 | n/a | n/a | none | 0 | CC[] not used (see above) | −1/2 matches paper's Majorana −½ m ψ̄ψ | Self-conjugate: real |
| LN5kin (kinetic) | n5bar, n5, ∂ | 4 | I/2 | 0 | none | 0 | 0 | n/a | n/a | none | n5: none; sum 0 | not used | I/2 | real |
| LN5kin (mass) | n5bar, n5 | 3 | Mn5 | 1 | none | 0 | 0 | n/a | n/a | none | 0 | not used | −1/2 | real |
| LYuk (vertex) | N1Lbar, LL, PhiNP | 4 | yvn[ff] | 0 = 4−4 | none (NP order via yvn) | 0 | 0 (N1L 0 + LL −1/2 + PhiNP +1/2) | Eps[ii,jj]: LL and PhiNP both unbarred (same conjugation type) | all singlets (N1L, LL, PhiNP: no colour) | LNLS: (−1 for N1L from LeptonNumber) + (+1 LL) + 0 PhiNP = 0; new U(1) none | Lepton: −1 +1 +0 = 0; Baryon: 0 | CC[N1Lbar] used: paper writes \overline{N_1^c}, FR snippet CC[N1Lbar] — matches | Sqrt[2] in yvn and PhiNP definitions matches paper's U_n row 4 / v/√2 placement | +HC[yuk] present |

### Particle classes (kinetic+mass presence)

| Class | Label | Kinetic term | Mass | In LTotal | Notes |
|---|---|---|---|---|---|
| F[100] | n4 | LN4kin (I/2 n4bar.Ga.del) | Mn4 (Internal), in LN4kin | yes (LN4kin) | SelfConjugate→True → no QuantumNumbers; PDG 8000011; width 0 |
| F[101] | n5 | LN5kin | Mn5 (Internal) | yes (LN5kin) | SelfConjugate→True → no QuantumNumbers; PDG 8000012; width 0 |
| F[102] | nL | Unphysical multiplet; free terms inherited from vl (SM LSM) and n4/n5 (LN4kin/LN5kin) | inherited | yes (via LSM/LN4kin/LN5kin) | 5 mass eigenstates: vl[1..3], n4, n5 |
| F[110] | N1L | Unphysical; free terms superseded by n4/n5 (deltaM carried by Mn4/Mn5; avoids double counting) | superseded | yes (via LN4kin/LN5kin) | LeptonNumber −1; used in LYuk |
| F[111] | N2L | Unphysical; free terms superseded likewise | superseded | yes (via LN4kin/LN5kin) | Defined; not in any interaction term (pSPSS only y1) |
| S[100] | PhiNP | Unphysical Higgs; physical H/G0/GP free terms from SM LHiggs | vevNP | yes (via LSM) | Y→1/2; PhiNP[1]=−I GP, PhiNP[2]=(vevNP+H+I G0)/√2 |
| F[11] | LL | Redefined Unphysical (SM class edited), not a new particle; neutrino component = UnCL·nL generates W–l–n4/n5 couplings | n/a (gauge bosons from SM) | yes (via LSM + LYuk) | Y→−1/2 |

- Non-fundamental colour representations: none → AddGaugeRepresentation not needed.
- Name conflicts: none — labels n4, n5, nL, N1L, N2L, PhiNP, LL (redefined), parameters Mmaj, deltaM, theta1–3, damping, vevNP, yvn, Mn4, Mn5, UnCL, index NeutMass/ni all clear of Mathematica/FeynRules/SM.fr built-ins (checked against SM.fr classes/params).
- LTotal := LSM + LN4kin + LN5kin + LYuk — every term defined in model.fr appears; LSM is the SM.fr base.
- Reference files read: paper/2210.10738_source.tex and SM.fr only (no other .fr).
- PhiNP vs paper FR snippet's PhiNPbar: paper snippet would give Y sum = −1; LaTeX H̃† has Y=+1/2, so PhiNP with Eps is used (Y=0), LaTeX authoritative.

model.fr is written