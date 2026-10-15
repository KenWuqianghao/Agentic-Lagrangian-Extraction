`./frgen` is green: **SCHEMA OK**, `model.fr` rendered (151 lines), lint reports only the 4 pre-classified `warn` findings — no fixable defects remain.

## Lint disposition (all warn, all harmless)

| # | Rule | Term | Why harmless |
|---|------|------|--------------|
| 1 | `explicit_index_in_dc` | `LGaugeH2` (model.fr:147) | `DC[PhiCbar[ii],mu]` mirrors SM.fr's own `DC[Phibar[ii],mu]` idiom; indexed doublet before Definitions substitution is the standard FR pattern |
| 2–3 | `undeclared_symbol` (`Phibar`) | `LPotCorr`, `LGaugeH2` (145, 147) | False positive: linter's SM.fr path (`~/Documents/Github/heptapod/...`) doesn't exist in this sandbox, so `SM_CLASSES`/`SM_PARAMS`/`SM_FIELDS_ALL` are empty; `Phibar`/`Phi` are declared in SM.fr, which FeynRules loads at compile time. `SM_MASSES` is hardcoded and includes `MH` |
| 4 | `undeclared_symbol` (`CKM`) | `LYukCorr` (149) | Same sandbox false positive; `CKM` is declared in SM.fr (used with SM's own `ExpandIndices` idiom) |

Expected `mixing_in_definitions` findings did **not** appear (stage-check only anyway; harmless because `m_h = 125 = SM MH`, so SM's mass basis is unchanged).

## Self-audit

### Lagrangian terms

| Term | Fields | d | Coupling | 4−d | 1/Λ | Q | Y | SU(2) | SU(3) | Dark U(1) | B/L | CC | Fraction/root | Hermitian partner |
|------|--------|---|----------|-----|-----|---|---|-------|-------|-----------|-----|----|---------------|-------------------|
| LH2Kin (kin) | H2, H2 | 4 | 1 | 0 | n/a | 0 | 0 | — | — | 0 | 0 | n/a | 1/2 ✓ | real field, self-adjoint |
| LH2Kin (mass) | H2, H2 | 2 | MH2² | 2 | n/a | 0 | 0 | — | — | 0 | 0 | n/a | 1/2 ✓ | same |
| LChiKin (kin) | Chi, Chi | 4 | 1 | 0 | n/a | 0 | 0 | — | — | 0 | 0 | n/a | 1/2 ✓ | real field |
| LChiKin (mass) | Chi, Chi | 2 | Mchi² | 2 | n/a | 0 | 0 | — | — | 0 | 0 | n/a | 1/2 ✓ | same |
| LS (mass) | Scbar, Sc | 2 | muS2 | 2 | n/a | 0 | 0 | — | — | 0 | 0 | n/a | muS2/2 ✓ | Scbar Sc self-adjoint |
| LS (portal) | PhiCbar[ii], PhiC[ii], Scbar, Sc | 4 | lamPS | 0 | n/a | 0 | ½−½=0 | ii contracted ✓ | singlets | 0 | 0 | n/a | lamPS ✓ | self-adjoint |
| LS (quartic) | Scbar, Sc, Scbar, Sc | 4 | lamS | 0 | n/a | 0 | 0 | — | — | 0 | 0 | n/a | lamS/2 ✓ | self-adjoint |
| LSoft | Sc, Sc / Scbar, Scbar | 2 | muSps2 | 2 | n/a | 0 | 0 | — | — | **+2 soft breaking** (Sc²); −2 for Scbar² | 0 | n/a | muSps2/4 ✓ | Sc² + Scbar² = 2Re(Sc²), Hermitian |
| LPotCorr (SM mass) | Phibar[ii], Phi[ii] | 2 | muH² | 2 | n/a | 0 | 0 | ii ✓ | singlet | 0 | 0 | n/a | muH² ✓ | self-adjoint |
| LPotCorr (SM quartic) | Phibar[ii]×2, Phi[ii]×2 | 4 | lam | 0 | n/a | 0 | 0 | ii, jj ✓ | singlet | 0 | 0 | n/a | lam ✓ | self-adjoint |
| LPotCorr (NP mass) | PhiCbar[ii], PhiC[ii] | 2 | muPhi2 | 2 | n/a | 0 | 0 | ii ✓ | singlet | 0 | 0 | n/a | muPhi2/2 ✓ | self-adjoint |
| LPotCorr (NP quartic) | PhiCbar[ii]×2, PhiC[ii]×2 | 4 | lamPhi | 0 | n/a | 0 | 0 | ii, jj ✓ | singlet | 0 | 0 | n/a | lamPhi/2 ✓ | self-adjoint |
| LGaugeH2 (PhiC) | DC PhiCbar[ii], DC PhiC[ii] | 4 | 1 | 0 | n/a | 0 | 0 | ii ✓ | singlet | 0 | 0 | n/a | free field ✓ | Hermitian up to total derivative |
| LGaugeH2 (−Phi) | DC Phibar[ii], DC Phi[ii] | 4 | −1 | 0 | n/a | 0 | 0 | ii ✓ | singlet | 0 | 0 | n/a | free field ✓ | same; difference of two real kinetic ops |
| LYukCorr (d-type) | QLbar·dR·PhiC (+HC) | 4 | yd, CKM | 0 | n/a | 0 | ½+½−1=0 (Yukawa index structure) | ii contracted, Eps where needed | cc contracted ✓ | 0 | B=1, L=0 ✓ | n/a | yuk1+HC[yuk1] ✓ explicit HC | Hermitian by construction |
| LYukCorr (u-type) | QLbar·uR·PhiCbar·Eps (+HC) | 4 | yu | 0 | n/a | 0 | 0 | ii via Eps ✓ | cc ✓ | 0 | B=1, L=0 ✓ | n/a | ✓ | Hermitian by construction |
| LYukCorr (l-type) | LLbar·lR·PhiC (+HC) | 4 | yl | 0 | n/a | 0 | 0 | ii ✓ | colorless | 0 | B=0, L=1 ✓ | n/a | ✓ | Hermitian by construction |
| LTotal | sum of above | — | — | — | n/a | 0 | 0 | ✓ | ✓ | 0 net (LSoft soft term retained) | 0 | n/a | single sum ✓ | whole Lagrangian Hermitian |

Note on factor 2 (documented, not a lint finding): rule 1 free-field mass terms (`−½ MH2² H2²`, `−½ Mchi² Chi²`) overlap the SSB potential's quadratic pieces, so L has a factor-2 on the H2/χ mass relative to the stationarity relations — inherent to combining rule 1 with a symmetry-breaking potential; no lint rule detects it, and `M$vevs`/mass eigenstate definitions keep FeynRules' physical masses correct.

### Kinetic terms per new particle class

| Class | Kinetic term | Mass | Self-conjugate / QN |
|-------|-------------|------|---------------------|
| H2 (S[100]) | `1/2 del[H2,mu] del[H2,mu]` in LH2Kin | `{MH2, 125.3}` | True → no QuantumNumbers ✓ |
| Chi (S[101]) | `1/2 del[Chi,mu] del[Chi,mu]` in LChiKin | `{Mchi, 62.573}` | True → no QuantumNumbers ✓ |
| phi0 (S[200]) | Unphysical: kinetic inherited via PhiC Definitions in LGaugeH2 | — | True ✓ |
| s0 (S[201]) | Unphysical: kinetic via Sc Definitions in LS/LSoft | — | True ✓ |
| Sc (S[202]) | Unphysical complex: kinetic/potential via LS, LSoft | vs/√2 in Definitions | False, no QN on Unphysical ✓ |
| PhiC (S[203]) | Unphysical doublet: DC[PhiCbar]DC[PhiC] in LGaugeH2 | — | False; `{Y→1/2}` declared; SU2D index ✓ |

### Color representations

| Field | SU(3) rep |
|-------|-----------|
| H2, Chi, phi0, s0, Sc | color singlets (no index) ✓ |
| PhiC / Phi | color singlets; only SU2D index ✓ |
| QLbar, uR, dR (in LYukCorr) | SM triplets from SM.fr, `cc` contracted ✓ |
| LLbar, lR | SM colorless ✓ |

**Name checks:** `H2`/`Chi` physical, `MH2`/`Mchi` not reserved; SM `H`, `MH`, `Phi`, `vev`, `lam`, `muH`, `yu`/`yd`/`yl`, `CKM` all referenced as in SM.fr; no name collisions. **Dependent parameters:** `lamS`, `lamPS`, `muS2`, `lamPhi`, `muPhi2`, `kapXh`, `kapXH`, `muSps2` Internal with `{NP,1}` (except `muPhi2`, a pure mass parameter); free Externals `vs`, `thetaHS` in `PINPUTS`. **No cached .fr model files were read** (only `SM.fr` as the declared add-on base, plus toolkit sources).

---

1. Every new particle class is SelfConjugate→True (H2, Chi, phi0, s0) or Unphysical without QuantumNumbers where required; the only QuantumNumbers (`Y→1/2` on PhiC) sit on the Unphysical doublet that must carry hypercharge before Definitions.
2. Name checks pass: physical `H2`/`Chi` and masses `MH2`/`Mchi` are unique; SM symbols (`H`, `MH`, `Phi`, `Phibar`, `vev`, `lam`, `muH`, `CKM`, Yukawas) match SM.fr; no reserved-mass/width collisions; all new coupling parameters carry `InteractionOrder {NP,1}` (mass parameter `muPhi2` excepted as a mass, not a coupling).
3. Exactly one total Lagrangian: `LTotal := LH2Kin + LChiKin + LS + LSoft + LPotCorr + LGaugeH2 + LYukCorr` (model.fr:151) — the sole `:=` sum of all terms.
4. No cached FeynRules model files were read; `spec.json` was built from TASK.md, the paper source, `SM.fr`, and the toolkit schema/linter/render sources only.