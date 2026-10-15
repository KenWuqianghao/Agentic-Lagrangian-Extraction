**Self-Audit Table**

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4 - d) | 1/Lambda power present (must be d - 4, or "n/a" if d <= 4) | Q sum | Y sum | SU(2) contraction (singlet? which Eps or shared index) | SU(3) contraction | sum of each new U(1) charge (must be 0) | lepton/baryon number sum | CC[] used where paper writes psi^c (yes/no/n/a) | fraction/root placement checked against (equation, LaTeX line, or "n/a") | Hermitian partner (HC[] or self-conjugate) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LXkin | X, ∂X, X | 4 | (implicit 1) | 0 | n/a | 0 | 0 | singlet (Lorentz only) | singlet | n/a | 0 | n/a | n/a | self-conjugate |
| LXZZ | X, Z, ∂Z, Z | 4 | c1·sw | 0 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | Eq.40 (LaTeX 1259-1263) | self-conjugate |
| LXZγ | X, Z, ∂A, A | 4 | c1·cw | 0 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | Eq.40 (LaTeX 1259-1263) | self-conjugate |
| LXWpWm | X, W+, ∂W-, W- | 4 | c2 | 0 | n/a | 0 (+1-1=0) | 0 | singlet | singlet | n/a | 0 | n/a | Eq.40 (LaTeX 1271-1274) | HC[LXWpWm] |
| LXWpWm_HC | X, W-, ∂W+, W+ | 4 | c2 | 0 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | Eq.40 | HC partner |

**Additional checks:**
- X kinetic+mass term in LTotal: **yes (LXkin)**
- AddGaugeRepresentation for non-fundamental colour: **n/a** (no coloured new fields)
- SelfConjugate→True classes carry no QuantumNumbers: **X has SelfConjugate→True, no QuantumNumbers ✓**
- Class/parameter/index names vs built-ins/SM.fr: **X, MX, c1, c2, LXkin, LXZZ, LXZγ, LXWpWm, LTotal — no conflicts ✓**
- Single LTotal: **LTotal := LXkin + LXZZ + LXZγ + LXWpWm + HC[LXWpWm] ✓**
- Reference/cached model file read: **none** (only paper/0901.0639_source.tex and SM.fr)

model.fr is written.