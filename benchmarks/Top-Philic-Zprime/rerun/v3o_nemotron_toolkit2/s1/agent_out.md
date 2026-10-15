**Self-audit table:**

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (4-d) | 1/Lambda power (d-4 or n/a) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) charge sum | L/B sum | CC[] used | fraction/root checked | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L_V1_kin_mass | V1, FS[V1] | 4 | 1 (implicit) | 0 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | n/a | self-conjugate (real vector) |
| L_V1_int | uqbar[3], uq[3], V1 | 4 | ct | 0 | n/a | 0 | 0 | singlet | δ_cc (color singlet) | n/a | 0 | n/a | n/a (cos/sin) | self-conjugate (ψ̄γᵘP_{L/R}ψ hermitian) |
| LTotal | sum of above | — | — | — | — | — | — | — | — | — | — | — | — | — |

- Kinetic+mass term for V1 exists and is in LTotal: **YES**  
- Non-fundamental colour representations: **none** (V1 is colour singlet)  
- SelfConjugate→True classes with no QuantumNumbers: **V1** (Q=0, zero charge allowed)  
- Name collision check: **V1, MV1, ct, theta, WV1, L_V1_kin_mass, L_V1_int, LTotal, TOPPHILIC** — none conflict with Mathematica/FeynRules/SM.fr names  
- Single total Lagrangian: **LTotal = L_V1_kin_mass + L_V1_int**  
- Reference/cached model file read: **none** (only paper LaTeX source and SM.fr read)

```
./frgen spec.json
SCHEMA OK: 1 particle classes, 2 parameters, Lagrangian terms ['L_V1_kin_mass', 'L_V1_int', 'LTotal']
RENDERED: model.fr (66 lines). You may read it.
LINT: no findings.
```