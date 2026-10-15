SCHEMA OK: 1 particle classes, 2 parameters, Lagrangian terms ['LNKin', 'LNMass', 'LNWbase', 'LNW', 'LNZbase', 'LNZ', 'LNHbase', 'LNH', 'LTotal']
RENDERED: model.fr (70 lines). You may read it.
LINT: no findings.

SELF-AUDIT TABLE
================

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4 - d) | 1/Lambda power present (must be d - 4, or "n/a" if d <= 4) | Q sum | Y sum | SU(2) contraction (singlet? which Eps or shared index) | SU(3) contraction | sum of each new U(1) charge (one column per U(1), must be 0) | lepton/baryon number sum (if the paper assigns them) | CC[] used where paper writes psi^c (yes/no/n/a) | fraction/root placement checked against (equation, LaTeX line, or "n/a") | Hermitian partner (HC[] or self-conjugate) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LNKin | HNbar(3/2), HN(3/2), DC(1) | 4 | 1 (implicit) | 0 | n/a | 0 | 0 (phys basis) | singlet (HN is SU(2) singlet) | singlet (HN is colour singlet) | n/a | 0 (HNbar L=+1, HN L=-1) | n/a | n/a | self-conjugate |
| LNMass | HNbar(3/2), HN(3/2) | 3 | MN | 1 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | n/a | self-conjugate |
| LNWbase | W(1), CC[HNbar](3/2), l(3/2) | 4 | gw/Sqrt[2] * V | 0 | n/a | 0 (W Q=1, HN Q=0, l Q=-1) | 0 (phys basis) | singlet | singlet | n/a | 0 (CC[HNbar] L=-1, l L=+1) | yes (paper N^c -> CC[HN]) | Eq.(224-225), LaTeX 224-225 | HC[LNWbase] in LNW |
| LNW | LNWbase + HC[LNWbase] | 4 | gw/Sqrt[2] * V | 0 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | yes | Eq.(224-225) | self-conjugate (via HC) |
| LNZbase | Z(1), CC[HNbar](3/2), vl(3/2) | 4 | gw/(2*cw) * V | 0 | n/a | 0 (all Q=0) | 0 | singlet | singlet | n/a | 0 (CC[HNbar] L=-1, vl L=+1) | yes (paper N^c -> CC[HN]) | Eq.(226-227), LaTeX 226-227 | HC[LNZbase] in LNZ |
| LNZ | LNZbase + HC[LNZbase] | 4 | gw/(2*cw) * V | 0 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | yes | Eq.(226-227) | self-conjugate (via HC) |
| LNHbase | H(1), CC[HNbar](3/2), vl(3/2) | 4 | gw*MN/(2*MW) * V | 0 | n/a | 0 (all Q=0) | 0 | singlet | singlet | n/a | 0 (CC[HNbar] L=-1, vl L=+1) | yes (paper N^c -> CC[HN]) | Eq.(228), LaTeX 228 | HC[LNHbase] in LNH |
| LNH | LNHbase + HC[LNHbase] | 4 | gw*MN/(2*MW) * V | 0 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | yes | Eq.(228) | self-conjugate (via HC) |

Additional audit rows:
- New particle class HN (F[100]): kinetic term LNKin and mass term LNMass exist and are included in LTotal.
- Non-fundamental colour representations: none (HN is a colour singlet; no AddGaugeRepresentation needed).
- SelfConjugate -> True classes: none (HN has SelfConjugate -> False).
- Name collision check: Class HN, parameters MN, V, index HeavyGeneration, terms LNKin, LNMass, LNWbase, LNW, LNZbase, LNZ, LNHbase, LNH, LTotal — none conflict with Mathematica built-ins, FeynRules symbols (HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM, N, C, D, E, I, K, O), or SM.fr names (H, Phi, Z, W, A, G, ee, gs, gw, sw, cw, vev, MZ, MW, vl, l, uq, dq, LL, QL, uR, dR, lR, Phi).
- Single total Lagrangian: LTotal = LNKin + LNMass + LNW + LNZ + LNH.
- Reference/cached model files read: none (only paper/1602.06957_source.tex and SM.fr were read as instructed).