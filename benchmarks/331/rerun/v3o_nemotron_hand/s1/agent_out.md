The complete FeynRules model file has been written to `model.fr`. It contains:

- **M$ModelName = "331_gen"**
- **M$Information** with author details from the paper
- **M$InteractionOrderHierarchy** with QCD, QED, NP orders
- **No new indices** needed (all new particles use existing Colour, Generation from SM.fr)
- **M$Parameters** with 80+ parameters: gauge couplings (g331, gX), beta, vevs (v1, v2, v3), Higgs potential parameters (mu1-3, lam1-3, lam12-23, lam12-23p, fparam), mixing angles, masses (Z', V, Y, H2, H3, H0, H±, H±Q_V, H±Q_Y, D, S, T, E_e, E_μ, E_τ), Yukawa couplings, electric/U(1)_X charges
- **M$ClassesDescription** with 15 new particle classes (indices ≥100): Zp, V, Y gauge bosons; H2, H3, H0, H±, H±Q_V, H±Q_Y scalars; Dq, Tq, El fermions; GZp, GVp, GYp Goldstones
- **Lagrangian terms**: kinetic+mass for all new fields, gauge-fermion couplings (V, Y, Z'), gauge self-interactions, scalar-gauge, scalar-fermion (Yukawa) couplings
- **LTotal** summing all terms
- **Self-audit table** with all required verification rows

model.fr is written.