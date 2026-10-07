# Reference UFO compiles

| paper | ok | load_sm | lagrangian | particles | vertices | BSM vertices | seconds | notes |
|---|---|---|---|---|---|---|---|---|
| ChernSimonsPortal | FAILED | True | `` | 0 | 0 | 0 | 0 | Not compiled: the reference file defines no Lagrangian, so there is no published expression to compile. LSM alone gives no vertex with xb. The file is an add-on (uses no SM declaration of its own). |
| Top-Philic-Zprime | ok | True | `LSM + Lv1` | 25 | 76 | 1 | 34 | Add-on. Total LSM + Lv1 is inferred (file has no total). Unitary gauge comes from the file itself. |
| Wprime | ok | True | `LSM + LWprime` | 25 | 199 | 36 | 57 | Add-on. Total LSM + LWprime is inferred (file has no total). |
| HeavyN | ok | True | `LFull` | 27 | 253 | 90 | 65 | Add-on. Total is the file's own LFull. |
| EffLRSM | ok | True | `LagFull` | 29 | 214 | 51 | 59 | Add-on. Total is the file's own LagFull. |
| SMWeinberg | ok | True | `LFull` | 25 | 235 | 60 | 63 | Add-on. Loaded with the sm.fr of the reference directory through _tools/compile_multi.wl (the driver can load only the FeynRules SM.fr). |
| Monotops | ok | True | `LSM + LMono` | 30 | 235 | 72 | 75 | Add-on. Total LSM + LMono is inferred (file has no total). |
| NJLComposite | FAILED | True | `` | 0 | 0 | 0 | 0 | Not compiled: the reference file defines only parameters and scalar classes and no Lagrangian, so there is no published expression to compile. |
| 331 | Not started | | | | | | | |
| ALRM_general | Not started | | | | | | | |
| B-L-SM | ok | False | `LBL` | 31 | 291 | 278 | 85 | Full model, loaded alone. Total is the file's own LBL. |
| GeneralU1 | FAILED | False | `Lfull` | 0 | 0 | 0 | 7 | Full model, loaded alone. Total is the file's own Lfull. |
| MDMmodel | ok | False | `LMDM` | 26 | 227 | 64 | 98 | Full model, loaded alone. Total is the file's own LMDM. |
| SLQrules | FAILED | True | `LSM + LQall` | 0 | 0 | 0 | 5091 | Add-on. Loaded with the SM.fr of the reference directory through _tools/compile_multi.wl. LQall is the file's total for the leptoquark part; adding LSM is inferred. |
| pNG | ok | False | `LSM + LpNG` | 26 | 103 | 28 | 39 | Full model, loaded alone. Total LSM + LpNG is inferred (file defines both pieces and no total). |
| pSPSS | ok | False | `LpSPSS` | 26 | 129 | 27 | 119 | Full model, loaded alone. Total is the file's own LpSPSS. |
