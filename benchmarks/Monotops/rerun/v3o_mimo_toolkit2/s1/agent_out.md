All steps finished: `aqVR`/`bqVR` descriptions corrected in `spec.json`, toolkit re-ran clean after each edit, and `./frgen spec.json` was re-run explicitly as the final action.

## Self-audit table (produced before writing `spec.json`, re-verified against the final file)

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4−d) | 1/Λ power (must be d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L/B sum | CC[] where paper writes ψ^c | fraction/root placement checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lkin_sPhi | sPhibar, sPhi (2×DC) | 1+1+1+1=4 | — (coef 1; Mphi in M² term) | 0 | n/a | 0+0=0 | 0+0=0 | singlet | singlet | n/a (no new U(1)) | n/a | n/a | n/a (rule-1 template) | self-conjugate; in LTotal ✓ |
| Lkin_vVec | vVecbar[mu], vVec[mu] (2×FS) | 2+2=4 | — (coef 1; Mvec) | 0 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | n/a | self-conjugate; in LTotal ✓ |
| Lkin_fChi | fChibar, fChi (Ga, DC) | 3/2+1+3/2=4; mass 3/2+3/2+Mchi=4 | — (coef 1; Mchi) | 0 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | n/a | self-conjugate; in LTotal ✓ |
| Lkin_sVarph | sVarphbar, sVarph (2×DC) | 4 | — (coef 1; Mvarphi) | 0 | n/a | +2/3−2/3=0 | +2/3−2/3=0 | singlet | singlet (3⊗3̄) | n/a | n/a | n/a | n/a | self-conjugate; in LTotal ✓ |
| Lkin_sTvarph | sTvarphbar, sTvarph (2×DC) | 4 | — (coef 1; Mtvarphi) | 0 | n/a | −1/3+1/3=0 | −1/3+1/3=0 | singlet | singlet (3⊗3̄) | n/a | n/a | n/a | n/a | self-conjugate; in LTotal ✓ |
| Lkin_vXcol | vXcolbar, vXcol (2×FS) | 4 | — (coef 1; Mxvec) | 0 | n/a | +2/3−2/3=0 | +2/3−2/3=0 | singlet | singlet (3⊗3̄) | n/a | n/a | n/a | n/a | self-conjugate; in LTotal ✓ |
| LphiFC | sPhi, uqbar, uq | 1+3/2+3/2=4 | a0FC, b0FC | 0=4−4 ✓ | n/a | 0+2/3−2/3=0 | 0+2/3−2/3=0 | singlet (uq physical, only Q in SM.fr ⇒ Y=Q) | singlet (colour contracted) | n/a | n/a | n/a | n/a (Eq.(1), LaTeX 185–205, no fraction/root) | HC[...] ✓ |
| LVFC | vVec[mu], uqbar, uq | 1+3/2+3/2=4 | a1FC, b1FC | 0 ✓ | n/a | 0+2/3−2/3=0 | 0+2/3−2/3=0 | singlet | singlet | n/a | n/a | n/a | n/a (Eq.(1)) | HC[...] ✓ |
| Lsvarphq | sVarph, bar[CC[dq]], dq | 1+3/2+3/2=4 | aqSR, bqSR | 0 ✓ | n/a | +2/3−1/3−1/3=0 | +2/3−1/3−1/3=0 | singlet | ε^{ijk} colour singlet (3·3·3) | n/a | n/a | yes | n/a (Eq.(1)) | HC[...] ✓ |
| Lsvarphu | sVarph, uqbar, fChi | 1+3/2+3/2=4 | aSRu, bSRu | 0 ✓ | n/a | +2/3−2/3+0=0 | +2/3−2/3+0=0 | singlet | singlet (3̄·3, shared cc1) | n/a | n/a | n/a | n/a (Eq.(1)) | HC[...] ✓ |
| Ltvarphq | sTvarph, bar[CC[dq]], uq | 1+3/2+3/2=4 | atqSR, btqSR | 0 ✓ | n/a | −1/3−1/3+2/3=0 | −1/3−1/3+2/3=0 | singlet | ε^{ijk} colour singlet | n/a | n/a | yes | n/a (Eq.(1)) | HC[...] ✓ |
| Ltvarphd | sTvarph, dqbar, fChi | 1+3/2+3/2=4 | atSRd, btSRd | 0 ✓ | n/a | −1/3+1/3+0=0 | −1/3+1/3+0=0 | singlet | singlet (3̄·3) | n/a | n/a | n/a | n/a (Eq.(1)) | HC[...] ✓ |
| Lxq | vXcol[mu], bar[CC[dq]], dq | 1+3/2+3/2=4 | aqVR, bqVR | 0 ✓ | n/a | +2/3−1/3−1/3=0 | +2/3−1/3−1/3=0 | singlet | ε^{ijk} colour singlet | n/a | n/a | yes | n/a (Eq.(1)) | HC[...] ✓ |
| Lxu | vXcol[mu], uqbar, fChi | 1+3/2+3/2=4 | aVRu, bVRu | 0 ✓ | n/a | +2/3−2/3+0=0 | +2/3−2/3+0=0 | singlet | singlet (3·3̄, shared cc1) | n/a | n/a | n/a | n/a (Eq.(1)) | HC[...] ✓ |

- Non-fundamental colour representations: **none** — all coloured new states (sVarph, sTvarph, vXcol) are `Colour` fundamentals, so no `AddGaugeRepresentation[...]` row and no `index_decls` are needed.
- `SelfConjugate -> True` classes: **none**; every class (sPhi, vVec, fChi, sVarph, sTvarph, vXcol) is `self_conjugate: false` (Eq.(1) ends with "+ h.c.") and each carries `QuantumNumbers {Q, Y}` (valid only because it is complex).
- Names — classes: sPhi, sPhibar, vVec, vVecbar, fChi, fChibar, sVarph, sVarphbar, sTvarph, sTvarphbar, vXcol, vXcolbar; parameters: a0FC, b0FC, a1FC, b1FC, aqSR, bqSR, aSRu, bSRu, atqSR, btqSR, atSRd, btSRd, aqVR, bqVR, aVRu, bVRu, epsC, Mphi, Mvec, Mchi, Mvarphi, Mtvarphi, Mxvec, Wvarphi, Wtvarphi, Wxvec; indices: Colour, Generation (both built-ins, `index_decls: []`) — none is a Mathematica built-in, a FeynRules symbol, or an SM.fr name (rule 10 ✓).
- Single total Lagrangian: **LTotal** = Lkin_sPhi + Lkin_vVec + Lkin_fChi + Lkin_sVarph + Lkin_sTvarph + Lkin_vXcol + LphiFC + LVFC + Lsvarphq + Lsvarphu + Ltvarphq + Ltvarphd + Lxq + Lxu (all 14 defined terms, no second total, no constant term).
- Reference or cached model file read: **none** (only `paper/1106.6199_source.tex`, `SM.fr`, and the schema/renderer/lint tools).
- Benchmark note: coupling values follow the paper's benchmark exactly (a0FC/a1FC[1,3]=[3,1], aqSR[1,2]=−aqSR[2,1], aSRu[3], aqVR[1,1], aVRu[3], atqSR[1,3]=[2,3], atSRd[1]=[2]=0.1; all b/ã = 0); masses Mphi=300, Mvec=Mchi=50 (scenario I), Mtvarphi=3000 (four-fermion scenario), Mxvec=500, Mvarphi=500 (resonant scenario — the paper quotes Mφ=3 TeV only in the four-fermion scenario, this choice is documented as ambiguous); invisible widths 0, coloured resonance widths `Automatic` (rendered as numeric placeholder, recovered by MadGraph `compute_widths`).

Last `./frgen spec.json`: `SCHEMA OK: 6 particle classes, 17 parameters, Lagrangian terms ['Lkin_sPhi', 'Lkin_vVec', 'Lkin_fChi', 'Lkin_sVarph', 'Lkin_sTvarph', 'Lkin_vXcol', 'LphiFC', 'LVFC', 'Lsvarphq', 'Lsvarphu', 'Ltvarphq', 'Ltvarphd', 'Lxq', 'Lxu', 'LTotal']` / `RENDERED: model.fr (271 lines). You may read it.` / `LINT: no findings.`