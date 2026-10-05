## Self-audit table

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4 − d) | 1/Λ power present (must be d − 4, or "n/a" if d ≤ 4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | lepton/baryon number sum | CC[] used | fraction/root placement checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWpkin | FS[Wpbar,mu,nu]·FS[Wp,mu,mu] (d=4); MWp²·Wpbar[mu]·Wp[mu] (monomial d=2, MWp dim 1) | 4 (FS·FS); mass monomial 3 with MWp | implicit 1; MWp | 0; 1 | n/a | (−1)+1=0 | not declared on Wp (same as SM W, SM.fr:157) → 0 | singlet | singlet | n/a | 0 | n/a | n/a (standard kinetic normalization) | self-conjugate (FS·FS and \|Wp\|² real) |
| LNRkin | NRbar.Ga[mu].DC[NR,mu] (d=4); NRbar.NR (d=3) | 4; mass monomial 3 | 1; MNR | 0; 1 | n/a | 0 (neutrino) | not declared → 0 | singlet | singlet | n/a | L: (−1)+1=0 | n/a | n/a | self-conjugate (Dirac kinetic + real mass) |
| LWpq | uqbar.VRp.Ga[mu].ProjP.dq · Wp[mu] /√2 | 4 | gRp (gLp, Cos[zeta], Exp[I omega], 1/√2) | 0 | n/a | (−2/3)+(−1/3)+1=0 | Y not declared on physical uq/dq/Wp → 0 | singlet (physical fields, no SU2 index) | bar–fundamental colour contraction | n/a | 0 | n/a | 1/√2 from LaTeX `\frac{1}{\sqrt{2}}` Eq. lagrangian (source.tex:91) | HC[LWpq] in LWpFerm |
| LWpl | NRbar.Ga[mu].ProjP.l · Wp[mu] /√2 | 4 | gRp | 0 | n/a | 0+(−1)+1=0 | not declared → 0 | singlet | singlet | n/a | L: (−1)+1=0 | n/a | same 1/√2 (source.tex:91) | HC[LWpl] in LWpFerm |
| LWpFerm | LWpq + LWpl + HC[LWpq+LWpl] | inherits 4 from LWpq/LWpl | gRp | 0 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | n/a | explicit HC[...] |
| LTotal | LWpkin + LNRkin + LWpFerm | — | — | — | n/a | — | — | — | — | — | — | — | — | sole root |
| Wp kinetic+mass | LWpkin in LTotal | 4 | — | — | — | — | — | — | — | — | — | — | — | confirmed |
| NR kinetic+mass | LNRkin in LTotal | 4 | — | — | — | — | — | — | — | — | — | — | — | confirmed |
| non-fundamental colour | n/a — no sextet/octet; no `AddGaugeRepresentation[...]` needed | | | | | | | | | | | | | |

- **SelfConjugate → True classes:** none (Wp and NR are both False; no QuantumNumbers on any SelfConjugate class).
- **Names:** classes `Wp`, `NR` (members `ne`,`nm`,`nt`); parameters `gRp`,`gLp`,`zeta`,`omega`,`VRp`,`VLq` (+ auto masses `MWp`,`WWp`,`MNR`); no new index declarations (only SM `Generation`/`Colour`); ParticleNames `Wp`/`Wpbar`, `vre`/`vrm`/`vrt`. None is a Mathematica built-in, FeynRules symbol, or SM.fr name (`Zeta` in PROTECTED is capital; `zeta` is distinct — lint confirms).
- **Single total:** `LTotal := LWpkin + LNRkin + LWpFerm` with `LWpFerm := LWpq + LWpl + HC[LWpq + LWpl]`.
- **Reference/cached model files read:** none (only the paper, SM.fr, schema/renderer/linter, TASK.md).
- **Physics notes:** gRp=0.653 from paper `g²=8 m_W² G_F/√2`, m_W=80.4, G_F=1.16639e-5 (source.tex:197–198); CKM from Eq. ckm (365–371); Γ=16.701 NLO at 500 GeV with leptons (tab:widql, line 520); M′=500 GeV benchmark; M_NR=100. GeV benchmark (paper does not fix m_νR; must be < m_′ for tab:widql); V′_lν identity (line 360) via diagonal ExpandIndices; pure-RH default g_L=0, ζ=0, ω=0; renormalizable (no Λ); no ψ^c; no new U(1); no mass mixing.

**Last `./frgen spec.json`:** `SCHEMA OK: 2 particle classes, 6 parameters, Lagrangian terms ['LWpkin', 'LNRkin', 'LWpq', 'LWpl', 'LWpFerm', 'LTotal']` / `RENDERED: model.fr (114 lines). You may read it.` / `LINT: no findings.`