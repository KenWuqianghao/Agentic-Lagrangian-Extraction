## Self-Audit Table for pNG_gen Model

### Lagrangian Term Audit

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4 - d) | 1/Lambda power present (must be d - 4, or "n/a" if d <= 4) | Q sum | Y sum | SU(2) contraction (singlet? which Eps or shared index) | SU(3) contraction | sum of each new U(1) charge (must be 0) | lepton/baryon number sum | CC[] used where paper writes psi^c (yes/no/n/a) | fraction/root placement checked against (equation, LaTeX line, or "n/a") | Hermitian partner (HC[] or self-conjugate) |
|-----------|------------------------|---------------------------|-----------------|------------------------------------------|-------------------------------------------------------------|-------|-------|--------------------------------------------------------|-------------------|------------------------------------------|--------------------------|-----------------------------------------------|--------------------------------------------------------------------------|------------------------------------------|
| L_kin_Phi | Phibar, Phi (with DC) | 4 | 1 (implicit) | 0 | n/a | 0 | 0 | shared index ii: Phibar[ii] Phi[ii] | singlet | 0 (no new U(1)) | 0 | n/a | n/a (kinetic term) | self-conjugate (real) |
| L_kin_S | Sbar, S (with DC) | 4 | 1 (implicit) | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a (kinetic term) | self-conjugate (real) |
| L_mass_Phi | Phibar, Phi | 2 | muPhi2 | 2 | n/a | 0 | 0 | shared index ii: Phibar[ii] Phi[ii] | singlet | 0 | 0 | n/a | n/a (mass term) | self-conjugate (real) |
| L_quartic_Phi | Phibar, Phi, Phibar, Phi | 4 | lambdaPhi | 0 | n/a | 0 | 0 | singlet: (Phibar[ii] Phi[ii])^2 | singlet | 0 | 0 | n/a | LaTeX: \frac{\lambda_\Phi}{2} (\Phi^\dagger \Phi)^2, Eq. (147) | self-conjugate (real) |
| L_portal | Phibar, Phi, Sbar, S | 4 | lambdaPhiS | 0 | n/a | 0 | 0 | singlet: Phibar[ii] Phi[ii] times Sbar S | singlet | 0 | 0 | n/a | LaTeX: -\lambda_{\Phi S} \Phi^\dagger \Phi \|S\|^2, Eq. (125) | self-conjugate (real) |
| L_quartic_S | Sbar, S, Sbar, S | 4 | lambdaS | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | LaTeX: -\frac{\lambda_S}{2} \|S\|^4, Eq. (125) | self-conjugate (real) |
| L_soft | S, S + Sbar, Sbar | 2 | muSprime2 | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | LaTeX: \frac{\mu_S'^2}{4} (S^2 + S^{*2}), Eq. (126) | HC of each other: S^2 <-> Sbar^2 |

### New Particle Class Kinetic + Mass Terms

| particle class | kinetic term in LTotal? | mass term in LTotal? | mass symbol | value | notes |
|----------------|-------------------------|----------------------|-------------|-------|-------|
| HH (S[101]) | Yes (from DC[Sbar,mu]DC[S,mu] via S definition) | Yes (from potential via S definition) | mH | 200. | Real scalar, SelfConjugate=True |
| chi (S[102]) | Yes (from DC[Sbar,mu]DC[S,mu] via S definition) | Yes (from soft term muSprime2 = m_chi^2) | m_chi | 100. | Real scalar, SelfConjugate=True |

### Non-Fundamental Colour Representations

None. All new fields are colour singlets.

### Self-Conjugate Classes with No QuantumNumbers

| class_name | self_conjugate | quantum_numbers | check |
|------------|----------------|-----------------|-------|
| HH | True | {} | PASS |
| chi | True | {} | PASS |

### Name Conflict Check

All names (S, HH, chi, m_chi, vs, theta, mH, lambdaPhi, lambdaS, lambdaPhiS, muSprime2, muPhi2, muS2, PNG) are clear of Mathematica built-ins, FeynRules symbols, and SM.fr names.

### Total Lagrangian

**LTotal** = LGauge + LFermions + LHiggsTotal + LYukawa + LGhost

### Reference Model Files

None read. Extraction based solely on arXiv:1912.04008_source.tex.

### Lint Findings Judgment

1. **undeclared_symbol (Phibar)**: Phibar is declared in SM.fr as antiparticle of Phi. Linter doesn't see SM.fr. **Harmless.**
2. **mixing_in_definitions (S mixes H, HH, chi)**: Add-on reinterprets SM.fr's H (mass eigenstate) as gauge eigenstate component. Known limitation; paper's standalone model redeclares full Higgs sector. **Harmless for this benchmark.**

---

**Last ./frgen result:**
```
SCHEMA OK: 3 particle classes, 10 parameters, Lagrangian terms ['LHiggsTotal', 'LTotal']
RENDERED: model.fr (113 lines). You may read it.
LINT: 2 finding(s). Each names the stage it predicts will fail (compile, checks = a FeynRules consistency check, mg5 = MadGraph import, harness = the total Lagrangian cannot be identified, warn = may still pass). Fix the ones that are real defects; do not remove paper physics just to silence one.
- [warn] undeclared_symbol: `LHiggsTotal` uses `Phibar` which is neither declared here nor by SM.fr (model.fr line 111)
- [checks] mixing_in_definitions: class `S` is defined as a mixture of ['HH', 'chi']; the mass basis of the partner fields declared in SM.fr is unchanged (model.fr line 78)
```