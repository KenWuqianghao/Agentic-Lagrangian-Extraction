Fixed the `LGG2` bracket (missing `]` closing `Block`), re-ran `./frgen spec.json`: schema OK, `model.fr` rendered (77 lines), lint clean.

## Self-audit

| term | fields in the monomial | d | coupling symbol | coupling dim (= 4−d) | 1/Λ power (d−4, or n/a) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sums | lepton/baryon sum | CC[] for ψ^c | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LNkin | `NMbar.Ga[mu].del[NM,mu]`; `NMbar.NM` | 4; 4 | 1; `mN` | 0; 1 (=4−4; =4−3) | n/a (1/Λ absorbed in `mN`) | 0 | 0 | singlet, no open SU(2) index | none (singlet) | n/a (no new gauge group) | 0 as summed; N carries no QuantumNumbers, paper assigns it none (Majorana mass is the ΔL=2 source, line 97) | n/a (Majorana bilinear) | −1/2 mN NMbar.NM per Majorana rule; `mN` vs eq:heavyNMass (line 188) | self-conjugate |
| LNW | `W[mu] NMbar.Ga[mu].ProjM.l[ff]` | 4 | `gw/Sqrt[2]` | 0 | n/a | +1(W)−1(l)+0 = 0 | 0 (SM.fr declares no Y on physical W/l; NM none) | singlet (physical fields, ProjM = P_L) | none | n/a | +1 (L(l)=1; N carries none, paper assigns none) | no (paper writes ℓ⁻) | ΔL line 366; eq:lagCC line 177 | `HC[…]` |
| LNZ | `Z[mu] NMbar.Ga[mu].ProjM.vl[ff]` | 4 | `gw/(2*cw)` | 0 | n/a | 0 | 0 | singlet | none | n/a | +1 (L(vl)=1) | no | ΔL line 368 | `HC[…]` |
| LNH | `H NMbar.ProjM.vl[ff]`; `H*H…` | 4 (H¹); 5 (H²) | `gw*mN/(2*MW)`; `gw^2*mN/(8*MW^2)` | 0; −1 = 4−5 | n/a; 1/Λ¹ absorbed in `mN` (Description: absorbed 1/Lambda, mass dim 1, GeV) | 0 | 0 | singlet | none | n/a | +1 (L(vl)=1) | no | ΔL line 370 (1/2·1/4 = 1/8 ✓) | `HC[…]` |
| LNGP | `GP*(NMbar.ProjM.l + bar[CC[l]].ProjM.NM)`; ×(1+gw H/(2 MW)) | 4 (GP¹); 5 (GP·H) | `gw*mN/(2*Sqrt[2]*MW)`; `gw^2*mN/(4*Sqrt[2]*MW^2)` | 0; −1 = 4−5 | n/a; 1/Λ¹ absorbed in `mN` | +1+0−1 = 0; +1−1+0 = 0 | 0 | singlet | none | n/a | +1 both pieces (L(N) undeclared) | **yes** (paper `\bar{\ell^c}P_L N`) | ΔL line 372 (1/2·1/2 = 1/4, Sqrt[2] placement ✓) | `HC[…]` |
| LNG0 | `G0*NMbar.ProjM.vl[ff]` ×(1+gw H/(2 MW)) | 4 (G0¹); 5 (G0·H) | `gw*mN/(2*MW)`; `gw^2*mN/(4*MW^2)` | 0; −1 = 4−5 | n/a; 1/Λ¹ absorbed in `mN` | 0 | 0 | singlet | none | n/a | +1 (L(vl)=1) | no | ΔL line 374 (1/2·1/2 = 1/4 ✓) | `HC[…]` |
| LGG1 | `2 GP GP bar[CC[l]].ProjM.l[ff2]`; `G0 G0 NMbar.ProjM.vl[ff]` | 5; 5 | `gw^2*mN/(8*MW^2)` | −1 = 4−5 | 1/Λ¹ absorbed in `mN` (Description) | +2−1−1 = 0; 0 | 0 | singlet | none | n/a | +2 (ΔL=2 G⁺G⁺ piece); +1 | **yes** (paper `\bar{\ell^c}P_L \ell'`) | ΔL line 376 (factor 2 kept ✓) | `HC[…]` |
| LGG2 | `G0 GP (NMbar.ProjM.l + bar[CC[l]].ProjM.NM)` | 5 | `gw^2*mN/(4*Sqrt[2]*MW^2)` | −1 = 4−5 | 1/Λ¹ absorbed in `mN` (Description) | 0+(+1)+0−1 = 0; +1−1+0 = 0 | 0 | singlet | none | n/a | +1 each piece | **yes** (paper `\bar{\ell^c}P_L N`) | ΔL line 379 (1/(4√2) ✓) | `HC[…]` |
| LTotal | sum of the 8 terms | n/a | — | — | n/a | 0 | 0 | — | — | n/a | — | — | n/a | n/a |

- New-particle row: class `NM` (F[100], SelfConjugate) — kinetic + Majorana mass exist in `LNkin` (model.fr:61) and are summed in `LTotal` (model.fr:77) ✓.
- Non-fundamental colour representation rows: **none** — `NM` is a colour singlet (no `Index[Colour]`), so no `AddGaugeRepresentation[…]` is needed ✓.
- `SelfConjugate -> True` classes: `NM` only; it carries no `QuantumNumbers` ✓ (model.fr:48–58).
- Names chosen — class: `NM`; parameters: `Lambda`, `Cll`, `mN`, `wN`; indices: none new (reuses SM.fr's `Index[Generation]`); blocks/orders: `NUPHYSICS`, `QCD`/`QED`/`NP`. None is a Mathematica built-in (`N` avoided by rule 10), a FeynRules symbol, or an SM.fr-declared name (SM.fr declares none of `NM`/`Lambda`/`Cll`/`mN`/`wN`; `gw`, `cw`, `MW`, `vev`, `W`, `Z`, `H`, `G0`, `GP`, `vl`, `l` are SM.fr's own names, deliberately reused) ✓.
- Single total Lagrangian: `LTotal := LNkin + LNW + LNZ + LNH + LNGP + LNG0 + LGG1 + LGG2` (model.fr:77), summing exactly the 8 emitted terms ✓.
- Y-sum note: SM.fr declares `Y` only on unphysical classes (`LL`, `lR`, …); no physical field used here nor `NM` carries a declared `Y`, so every Y sum is 0 — equivalently each term descends from the hypercharge-invariant Weinberg operator (eq:dim5Lag, source lines 107–111).
- Reference or cached model file read: **none** (only `paper/2012.09882_source.tex` and the workspace's provided `SM.fr`).

Last `./frgen spec.json`: `SCHEMA OK: 1 particle classes, 4 parameters, Lagrangian terms ['LNkin', 'LNW', 'LNZ', 'LNH', 'LNGP', 'LNG0', 'LGG1', 'LGG2', 'LTotal']` / `RENDERED: model.fr (77 lines)` / `LINT: no findings.`