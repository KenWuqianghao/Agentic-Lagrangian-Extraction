# How much of each Lagrangian actually reached the UFO

**Read this before trusting the pass rate.**

The validation harness chooses each model's total-Lagrangian symbol positionally: it takes the **last** line matching `^L<name> =` in the `.fr`, and compiles `LSM + <that symbol>`.

That is correct only when a model's last `L` assignment really is its total. Where a model defines its total and then defines anything else beginning with `L`, or carries several alternative operator bases, the harness compiles a **fragment** of the model. A fragment can be perfectly Hermitian, pass every FeynRules check and import into MadGraph — so it counts as passing while most of the physics never reached the UFO.

**11 of 28 models are affected, 9 of them among those counted as passing.**

This does not mean those models are wrong. It means the benchmark did not test as much of them as the pass rate implies, and the gap should be closed before the number is quoted anywhere.

## Affected models

| model | source | symbol compiled | L-terms reached | omitted |
|---|---|---|---:|---|
| `VLQ` | one-shot | `L4Mass` | 1/11 | `L4CKM`, `LDBP`, `LDTP`, `LHTP`, `LWBP`, `LWTP`, `LZBP`, `LZTP`, `LyBP`, `LyTP` |
| `HNLs` *(failed anyway)* | one-shot | `LHadrSemileptonic` | 1/8 | `LHadrPseudoscalarCharged`, `LHadrPseudoscalarNeutral`, `LHadrVectorCharged`, `LHadrVectorNeutral`, `LHeavyNDiracMass`, `LHeavyNEW`, `LagHeavyN` |
| `topBSM` | one-shot | `LO1` | 5/23 | `LO0`, `LO0ggfusion`, `LO0ggfusionAxial`, `LO0ggfusionScalar`, `LO0top`, `LS0`, `LS0ggfusion`, `LS0ggfusionAxial`, `LS0ggfusionScalar`, `LS0top`, `LS1`, `LS1dl`, `LS1dr`, `LS1el`, `LS1er`, `LS1nu`, `LS1ul`, `LS1ur` |
| `ALRM_general` *(failed anyway)* | one-shot | `LeffALRM` | 1/4 | `LFALRM`, `LSALRM`, `LYALRM` |
| `331` | repair2 | `LTot` | 2/5 | `LGauge331Mass`, `LHiggs331`, `LScalarFermion331` |
| `DMsimp` | one-shot | `L1DM` | 3/7 | `L0DM`, `L0SM`, `L0SMg`, `L0X` |
| `CHEIDI` | repair2 | `LTot` | 2/4 | `LHEIDI`, `LHEIDIgg` |
| `ChernSimonsPortal` | one-shot | `LChernSimonsPortalBroken` | 1/2 | `LChernSimonsPortal` |
| `MDMmodel` | repair | `LTot` | 4/5 | `LMDMNP` |
| `VLC_LN` | repair2 | `LTot` | 10/12 | `LChiralFull`, `LEDM` |
| `Sextets` | one-shot | `LSextet` | 9/10 | `LD` |

## Worth checking first

- `VLQ` compiled `L4Mass` alone — 1 of 11 terms. Every vector-like quark interaction (`LWTP`, `LZTP`, `LHTP`, `LyTP`, ...) was left out, yet the model passed the full chain.
- `topBSM` compiled `LO1`, reaching 5 of 26 terms. Its cross-check independently flagged 20 substantive disagreements, including that the paper's master EFT Lagrangian was not reproduced — consistent with this.
- `331` compiled `LTot := LGaugeSelf331`, so the Higgs potential, gauge masses and scalar-fermion couplings are all absent.

## The fix

Do not infer the total Lagrangian from file position. Either require the generator to emit a known symbol name, or resolve the root by reference analysis — the term no other term refers to — and fail loudly when that is ambiguous. `UFO_generator.wl` already accepts a `LagName` parameter and already fails when the symbol is undefined; the weakness is purely in how the harness chooses what to pass it.

## Reproducing

```bash
python benchmarks/audit_lagrangian_coverage.py
```
