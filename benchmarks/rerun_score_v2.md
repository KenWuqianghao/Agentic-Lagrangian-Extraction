# Sandboxed rerun `v2` vs the original fleet

| model | original run | field F1 orig | field F1 sandboxed | QN F1 sandboxed | fields (gen/ref) | read paper | tainted | status |
|---|---|---|---|---|---|---|---|---|
| 331 | clean | 0.20 | 0.41 | 0.41 | {'reference': 38, 'generated': 21, 'reference_raw': 58, 'generated_raw': 21}/38 | True | False | scored |
| ALRM_general | clean | 0.52 | 0.61 | 0.42 | {'reference': 16, 'generated': 23, 'reference_raw': 30, 'generated_raw': 23}/16 | True | False | scored |
| topBSM | OWN REFERENCE READ | 1.00 | — | — | {'reference': 0, 'generated': 0, 'reference_raw': 0, 'generated_raw': 0}/0 | True | False | scored_no_new_fields |
| ChernSimonsPortal | OWN REFERENCE READ | 1.00 | 0.12 | 0.12 | {'reference': 1, 'generated': 16, 'reference_raw': 1, 'generated_raw': 16}/1 | True | False | scored |
| DMsimp | OWN REFERENCE READ | 0.67 | 0.67 | 0.89 | {'reference': 4, 'generated': 5, 'reference_raw': 4, 'generated_raw': 5}/4 | True | False | scored |
| EffLRSM | clean | 1.00 | 1.00 | 1.00 | {'reference': 3, 'generated': 3, 'reference_raw': 3, 'generated_raw': 3}/3 | True | False | scored |
| GeneralU1 | other reference read | 0.50 | 0.50 | 0.50 | {'reference': 15, 'generated': 5, 'reference_raw': 41, 'generated_raw': 5}/15 | True | False | scored |
| HeavyN | OWN REFERENCE READ | 1.00 | 1.00 | 1.00 | {'reference': 3, 'generated': 3, 'reference_raw': 3, 'generated_raw': 3}/3 | True | False | scored |
| HNLs | OWN REFERENCE READ | 0.98 | — | — | —/— | True | False | render_failed |
| B-L-SM | clean | 0.62 | 0.75 | 0.75 | {'reference': 10, 'generated': 6, 'reference_raw': 30, 'generated_raw': 6}/10 | True | False | scored |
| MDMmodel | OWN REFERENCE READ | 0.62 | 0.71 | 0.71 | {'reference': 9, 'generated': 5, 'reference_raw': 35, 'generated_raw': 5}/9 | True | False | scored |
| Monotops | OWN REFERENCE READ | 1.00 | 1.00 | 1.00 | {'reference': 6, 'generated': 6, 'reference_raw': 6, 'generated_raw': 6}/6 | True | False | scored |
| pNG | OWN REFERENCE READ | 0.86 | 0.75 | 0.75 | {'reference': 3, 'generated': 5, 'reference_raw': 29, 'generated_raw': 5}/3 | True | False | scored |
| Sextets | OWN REFERENCE READ | 1.00 | 0.67 | 0.67 | {'reference': 3, 'generated': 6, 'reference_raw': 3, 'generated_raw': 6}/3 | True | False | scored |
| 368sextets | OWN REFERENCE READ | 1.00 | 1.00 | 1.00 | {'reference': 4, 'generated': 4, 'reference_raw': 4, 'generated_raw': 4}/4 | True | False | scored |
| SLQrules | clean | 0.78 | 1.00 | 1.00 | {'reference': 14, 'generated': 14, 'reference_raw': 14, 'generated_raw': 14}/14 | True | False | scored |
| pSPSS | clean | 0.22 | 1.00 | 1.00 | {'reference': 6, 'generated': 6, 'reference_raw': 32, 'generated_raw': 6}/6 | True | False | scored |
| SMWeinberg | OWN REFERENCE READ | 1.00 | 1.00 | 1.00 | {'reference': 1, 'generated': 1, 'reference_raw': 1, 'generated_raw': 1}/1 | True | False | scored |
| Top-Philic-Zprime | clean | 1.00 | 1.00 | 1.00 | {'reference': 1, 'generated': 1, 'reference_raw': 1, 'generated_raw': 1}/1 | True | False | scored |
| Triplets | OWN REFERENCE READ | 1.00 | 0.00 | 0.00 | {'reference': 1, 'generated': 3, 'reference_raw': 1, 'generated_raw': 3}/1 | True | False | scored |
| VLQ | OWN REFERENCE READ | 0.40 | 0.27 | 0.00 | {'reference': 4, 'generated': 11, 'reference_raw': 24, 'generated_raw': 11}/4 | True | False | scored |
| LeptoQuark | OWN REFERENCE READ | 0.00 | 0.00 | 0.44 | {'reference': 6, 'generated': 3, 'reference_raw': 6, 'generated_raw': 3}/6 | True | False | scored |
| Wprime | clean | 0.67 | 0.67 | 0.67 | {'reference': 1, 'generated': 2, 'reference_raw': 1, 'generated_raw': 2}/1 | True | False | scored |
| MSSMD | OWN REFERENCE READ | 0.50 | 0.27 | 0.30 | {'reference': 39, 'generated': 6, 'reference_raw': 60, 'generated_raw': 6}/39 | True | False | scored |
| CHEIDI | OWN REFERENCE READ | 1.00 | 0.22 | 0.22 | {'reference': 1, 'generated': 8, 'reference_raw': 1, 'generated_raw': 8}/1 | True | False | scored |
| HiggsCharacterisation | OWN REFERENCE READ | 1.00 | 1.00 | 1.00 | {'reference': 3, 'generated': 3, 'reference_raw': 3, 'generated_raw': 3}/3 | True | False | scored |
| NJLComposite | clean | 0.80 | 0.50 | 0.50 | {'reference': 18, 'generated': 6, 'reference_raw': 18, 'generated_raw': 6}/18 | True | False | scored |
| VLC_LN | OWN REFERENCE READ | 0.61 | 0.31 | 0.61 | {'reference': 4, 'generated': 9, 'reference_raw': 30, 'generated_raw': 9}/4 | True | False | scored |

## Summary

- **n_candidates**: 28
- **n_scored**: 26
- **n_read_paper**: 28
- **n_contaminated**: 0
- **mean_field_f1_sandboxed**: 0.632
- **mean_field_f1_original_same_models**: 0.73
- **mean_field_f1_sandboxed_where_original_clean**: 0.771
- **mean_field_f1_original_where_original_clean**: 0.646
- **mean_field_f1_sandboxed_where_original_read_own_ref**: 0.561
- **mean_field_f1_original_where_original_read_own_ref**: 0.791
