# Correction 2026-09-13: FeynRules check verdicts

Every FeynRules check verdict in this benchmark before 2026-09-13 was a pass unless the check crashed. The prose classifier (`tools/feynrules/wl_checks.py`) returned True on every branch, and none of its failure markers matched what FeynRules prints. Tony Menzo found this while reviewing heptapod-dev #15.

A second defect was in the harness. The old generator always sent `LSM + <total>` to FeynRules. Some models already include `LSM` in their total, so those runs were checked and compiled with every Standard Model term counted twice.

`rescore_checks.py` re-ran only the consistency checks on the same `.fr` and total, with the generator on heptapod `main` and `tools/feynrules/lagrangian_checks.py`. Each verdict now comes from the check's return value, and `LSM` is added only when the total does not already reach it. Every run's log is in its `checks.log`.

The field-content scores and the physicist-finding predicates read the `.fr` text. They do not use these checks and do not change.

## Full chain before and after, per arm

Full chain means compiled, all four default checks pass, and MadGraph imports the UFO.

| arm | runs | re-scored | full chain before | full chain after |
|---|---|---|---|---|
| v1 | 8 | 6 | 2/8 | **2/8** |
| v2 | 31 | 24 | 12/31 | **6/31** |
| v3_notools | 8 | 7 | 6/8 | **4/8** |
| v3_tools | 8 | 6 | 5/8 | **2/8** |

## Repair loop (revalidation_report.json)

| rows | full chain before | full chain after |
|---|---|---|
| 19 | 18 | **9** |

## New verdicts over the re-scored runs

| check | pass | fail | inconclusive | not run |
|---|---|---|---|---|
| hermiticity | 27 | 16 | 0 | 0 |
| kinetic_diagonal | 42 | 1 | 0 | 0 |
| mass_diagonal | 30 | 13 | 0 | 0 |
| mass_spectrum | 28 | 2 | 13 | 0 |

## Runs whose full-chain result changed

| run | before | after | H / Kd / Md / S |
|---|---|---|---|
| EffLRSM/rerun/v3_tools/s1 | True | False | ✓ ✓ ✗ ? |
| GeneralU1/rerun/v3_tools/s2 | True | False | ✗ ✓ ✗ ? |
| Top-Philic-Zprime/rerun/v3_tools/s2 | True | False | ✗ ✓ ✓ ✓ |
| GeneralU1/rerun/v3_notools/s1 | True | False | ✗ ✓ ✗ ? |
| Top-Philic-Zprime/rerun/v3_notools/s1 | True | False | ✗ ✓ ✓ ✓ |
| ChernSimonsPortal/rerun/v2/s1 | True | False | ✓ ✓ ✗ ? |
| LeptoQuark/rerun/v2/s1 | True | False | ✗ ✓ ✓ ✓ |
| MDMmodel/rerun/v2/s1 | True | False | ✓ ✓ ✗ ? |
| Sextets/rerun/v2/s1 | True | False | ✗ ✓ ✓ ✓ |
| VLC_LN/rerun/v2/s1 | True | False | ✓ ✓ ✗ ? |
| pNG/rerun/v2/s1 | True | False | ✓ ✗ ✗ ? |
| revalidation_report.json:B-L-SM | True | False | ✓ ✓ ✓ ✗ |
| revalidation_report.json:EffLRSM | True | False | ✓ ✓ ✗ ? |
| revalidation_report.json:GeneralU1 | True | False | ✓ ✓ ✓ ✗ |
| revalidation_report.json:MDMmodel | True | False | ✗ ✗ ✗ ? |
| revalidation_report.json:Sextets | True | False | ✓ ✓ ✓ ✗ |
| revalidation_report.json:Triplets | True | False | ✓ ✓ ✓ ✗ |
| revalidation_report.json:Wprime | True | False | ✓ ✓ ✗ ? |
| revalidation_report.json:pNG | True | False | ✗ ✓ ✗ ? |
| revalidation_report.json:pSPSS | True | False | ✓ ✗ ✗ ? |

## Runs that had the Standard Model counted twice before

20 of 61 re-scored runs define a total that already contains `LSM`. Their earlier compile and checks used twice the SM Lagrangian. The new verdicts use the total alone. Their UFOs and MadGraph imports were not rebuilt.

- `EffLRSM/rerun/v3_notools/s1`
- `EffLRSM/rerun/v3_notools/s2`
- `GeneralU1/rerun/v3_notools/s1`
- `331/rerun/v2/s1`
- `B-L-SM/rerun/v2/s1`
- `CHEIDI/rerun/v2/s1`
- `ChernSimonsPortal/rerun/v2/s1`
- `EffLRSM/rerun/v2/s2`
- `GeneralU1/rerun/v2/s1`
- `GeneralU1/rerun/v2/s2`
- `HeavyN/rerun/v2/s1`
- `LeptoQuark/rerun/v2/s1`
- `MDMmodel/rerun/v2/s1`
- `SMWeinberg/rerun/v2/s1`
- `Triplets/rerun/v2/s1`
- `pNG/rerun/v2/s1`
- `pSPSS/rerun/v2/s1`
- `topBSM/rerun/v2/s1`
- `revalidation_report.json:HeavyN`
- `revalidation_report.json:SMWeinberg`

`H / Kd / Md / S` is hermiticity, kinetic_diagonal, mass_diagonal, mass_spectrum: ✓ pass, ✗ fail, ? inconclusive. Inconclusive never counts as a pass.
