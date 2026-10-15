# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: FAILED
- FeynRules check `hermiticity`: not reached
- FeynRules check `kinetic_diagonal`: not reached
- FeynRules check `mass_diagonal`: not reached
- FeynRules check `mass_spectrum`: not reached
- MadGraph import: not reached
- Heuristic error tags: wolfram_aborted

## FeynRules / Wolfram Engine output (tail)
```
[INFO] Wolfram $VersionNumber = 15.
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
Merging model-files...
This model implementation was created by
Andreas Crivellin
Luc Schnell
Model Version: 1.0
For more information, type ModelInformation[].

   - Loading particle classes.
   - Loading gauge group classes.
   - Loading parameter classes.

Model SLQrules_gen loaded.
[INFO] Lagrangian: LSM + LBSM
[INFO] Running consistency checks: hermiticity, kinetic_diagonal, mass_diagonal, mass_spectrum

Inner::incom: Length 2 of dimension 1 in {SU2D, Generation} is incommensurate with length 1 of dimension 1 in {Index[SU2D, 1]}.

Inner::incom: Length 2 of dimension 1 in {SU2D, Generation} is incommensurate with length 1 of dimension 1 in {Index[SU2D, 1]}.

Inner::incom: Length 2 of dimension 1 in {SU2D, Generation} is incommensurate with length 1 of dimension 1 in {Index[SU2D, 1]}.

General::stop: Further output of Inner::incom will be suppressed during this calculation.

Global`D$18429::shdw: Symbol D$18429 appears in multiple contexts {Global`, System`}; definitions in context Global` may shadow or be shadowed by other definitions.

Global`E$18429::shdw: Symbol E$18429 appears in multiple contexts {Global`, System`}; definitions in context Global` may shadow or be shadowed by other definitions.

Sum::vloc: The variable FieldExpand[a$18429] cannot be localized so that it can be assigned to numerical values.

Sum::vloc: The variable FieldExpand[a$18429] cannot be localized so that it can be assigned to numerical values.

Sum::vloc: The variable FieldExpand[a$18429] cannot be localized so that it can be assigned to numerical values.

General::stop: Further output of Sum::vloc will be suppressed during this calculation.
$Aborted
GetFC::Head: Wrong Head in FC.

```
