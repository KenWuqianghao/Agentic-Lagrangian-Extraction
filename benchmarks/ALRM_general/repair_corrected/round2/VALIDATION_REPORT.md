# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: FAILED (TIMED OUT — the compile exceeded the time limit; the model may need simplification of redundant/expanded terms, without changing the physics)
- FeynRules check `hermiticity`: not reached
- FeynRules check `kinetic_diagonal`: not reached
- FeynRules check `mass_diagonal`: not reached
- FeynRules check `mass_spectrum`: not reached
- MadGraph import: not reached
- Heuristic error tags: compile_timeout, selfconjugate_quantum_numbers

## FeynRules / Wolfram Engine output (tail)
```
15.
[WARN] Wolfram >= 14 detected. FeynRules 2.3.49 requires the Commutator/MatrixSymbol unprotect patch (FeynRules PR #6) on this kernel; without it the UFO export produces malformed output.
[INFO] Loading via explicit file: /Users/kenwu/feynrules-current/FeynRules.m
 - FeynRules - 
Version: 2.3.49 (*29 September 2021).
Authors: A. Alloul, N. Christensen, C. Degrande, C. Duhr, B. Fuks
 
Please cite:
    - Comput.Phys.Commun.185:2250-2300,2014 (arXiv:1310.1921);
    - Comput.Phys.Commun.180:1614-1641,2009 (arXiv:0806.4194).
 
http://feynrules.phys.ucl.ac.be
 
The FeynRules palette can be opened using the command FRPalette[].
[INFO] Loading SM from: /Users/kenwu/feynrules-current/Models/SM/SM.fr
From kernel 3 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 4 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 5 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 1 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 2 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 4 (Local):
ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.
From kernel 5 (Local):
ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.

General::stop: Further output of Warning: Selfconjugated fields should not carry quantumnumbers. will be suppressed during this calculation.
From kernel 1 (Local):
ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.
From kernel 3 (Local):
ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.
From kernel 8 (Local):
ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.

General::stop: Further output of ToExpression::argb will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of LoadModel::QN will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of LoadModel::QN will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of LoadModel::QN will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of LoadModel::QN will be suppressed during this calculation.
From kernel 8 (Local):
General::stop: Further output of LoadModel::QN will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
From kernel 4 (Local):
Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.
From kernel 5 (Local):
Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.
From kernel 1 (Local):
Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.
From kernel 3 (Local):
Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.
From kernel 4 (Local):
Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.

General::stop: Further output of Length `1` of dimension `2` in `3` is incommensurate with length `4` of dimension 1 in `5`. will be suppressed during this calculation.
Merging model-files...
This model implementation was created by
Mariana Frank
Benjamin Fuks
Ozer Ozdal
Model Version: 1.0
For more information, type ModelInformation[].

   - Loading particle classes.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

General::stop: Further output of LoadModel::QN will be suppressed during this calculation.

ToExpression::argb: ToExpression called with 0 arguments; between 1 and 3 arguments are expected.

General::stop: Further output of ToExpression::argb will be suppressed during this calculation.
   - Loading gauge group classes.
   - Loading parameter classes.

Model ALRM_general_gen loaded.

Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.

Inner::incom: Length 1 of dimension 1 in {Index[SU2D]} is incommensurate with length 2 of dimension 1 in {2, 2}.
[INFO] Lagrangian: LSM + LTot
[INFO] Running consistency checks: hermiticity, kinetic_diagonal, mass_diagonal, mass_spectrum

```
