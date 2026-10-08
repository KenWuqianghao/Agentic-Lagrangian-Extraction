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
| 331 | ok | False | `LThree` | 47 | 1897 | 1786 | 1109 | Full model, loaded alone. Total is the file's own LThree. |
| ALRM_general | ok | False | `LVector + LMatter + LHiggs + LYuk + HC[LYuk] + LGhost + LagHEffective` | 33 | 1074 | 1050 | 1609 | Full model, loaded alone. The total is inferred: sum of all pieces the file defines, with HC[LYuk] added because LYuk at :522-528 has no hermitian conjugate. |
| B-L-SM | ok | False | `LBL` | 31 | 291 | 278 | 85 | Full model, loaded alone. Total is the file's own LBL. |
| GeneralU1 | ok | False | `Lfull` | 31 | 462 | 343 | 1110 | Full model, loaded alone. Total is the file's own Lfull. CHANGED REFERENCE COPY: the reference U1XGeneric.fr does not load (Syntax::sntx at line 27) because line 25 closes a string with the typographic quote U+201D. The compile uses GeneralU1/U1XGeneric_quotefix.fr, a copy with that one character replaced by an ASCII quote. Full unified diff: GeneralU1/U1XGeneric_quotefix.diff. The change is inside M$Information (Institutions) and touches no field, parameter or Lagrangian line. Attempt 1 (the reference file as published) failed in 7 s. |
| MDMmodel | ok | False | `LMDM` | 26 | 227 | 64 | 98 | Full model, loaded alone. Total is the file's own LMDM. |
| SLQrules | FAILED | True | `LSM + LQall` | 0 | 0 | 0 | 5091 | FAILED: no UFO in 85 minutes. Add-on, loaded with the SM.fr of the reference directory through _tools/compile_multi.wl. LQall is the file's total for the leptoquark part; adding LSM is inferred. The Lagrangian has 22951 terms after expansion; WriteUFO started and wrote only the static files (no particles.py, vertices.py, couplings.py, parameters.py). 'timeout 3600' did not stop wolframscript, so the process was stopped by pid at 5091 s. No retry, by decision of the coordinator. |
| pNG | ok | False | `LSM + LpNG` | 26 | 103 | 28 | 39 | Full model, loaded alone. Total LSM + LpNG is inferred (file defines both pieces and no total). |
| pSPSS | ok | False | `LpSPSS` | 26 | 129 | 27 | 119 | Full model, loaded alone. Total is the file's own LpSPSS. |
