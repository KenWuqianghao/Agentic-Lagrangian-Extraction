# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- FeynRules check `hermiticity`: pass
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: fail
- FeynRules check `mass_spectrum`: inconclusive
- MadGraph import: True
- Heuristic error tags: mass_diagonal_fail

## FeynRules check `mass_diagonal`: fail
Mass terms are not diagonal: the mass matrix mixes fields, so the declared particles are not mass eigenstates. Diagonalise the mass matrix, or declare the mixing. (Warning: not numerical value encountered. Unable to decide whether mass term is diagonal Non diagonal mass term found:)

## FeynRules check `mass_spectrum`: inconclusive
The mass spectrum could not be computed. This usually means the mass terms are not diagonal -- see that result. (Neglecting all terms with more than 2 particles. Warning: not numerical value encountered. Unable to decide whether mass term is diagonal Non diagonal mass term found:)

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
From kernel 1 (Local):
IntOrder::Overwrite: Warning: Conflicting definitions for InteractionOrder Hierachy found for QCD. Last definition is kept.
From kernel 3 (Local):
IntOrder::Overwrite: Warning: Conflicting definitions for InteractionOrder Hierachy found for QCD. Last definition is kept.
From kernel 4 (Local):
IntOrder::Overwrite: Warning: Conflicting definitions for InteractionOrder Hierachy found for QCD. Last definition is kept.
From kernel 5 (Local):
IntOrder::Overwrite: Warning: Conflicting definitions for InteractionOrder Hierachy found for QCD. Last definition is kept.
From kernel 6 (Local):
IntOrder::Overwrite: Warning: Conflicting definitions for InteractionOrder Hierachy found for QCD. Last definition is kept.

General::stop: Further output of Warning: Conflicting definitions for InteractionOrder `1` found for `2`. Last definition is kept. will be suppressed during this calculation.
Merging model-files...

IntOrder::Overwrite: Warning: Conflicting definitions for InteractionOrder Hierachy found for QCD. Last definition is kept.

IntOrder::Overwrite: Warning: Conflicting definitions for InteractionOrder Hierachy found for QED. Last definition is kept.
This model implementation was created by
Zack Sullivan
Model Version: 1.0
For more information, type ModelInformation[].

   - Loading particle classes.
   - Loading gauge group classes.
   - Loading parameter classes.

Model Wprime_gen loaded.
[INFO] Lagrangian: LSM + LBSM
[INFO] Running consistency checks: hermiticity, kinetic_diagonal, mass_diagonal, mass_spectrum
HEPTAPOD-CHECK|scope=model|name=hermiticity|verdict=pass|detail=Checking for hermiticity by calculating the Feynman rules contained in L-HC[L]. If the lagrangian is hermitian, then the number of vertices should be zero. Starting Feynman rule calculation. Expanding the Lagrangian... Expanding the indices over 8 cores Collecting the different structures that enter the vertex. No vertices found. 0 vertices obtained. The lagrangian is hermitian.
HEPTAPOD-CHECK|scope=model|name=kinetic_diagonal|verdict=pass|detail=Neglecting all terms with more than 2 particles. All kinetic terms are diagonal.
HEPTAPOD-CHECK|scope=model|name=mass_diagonal|verdict=fail|detail=Warning: not numerical value encountered. Unable to decide whether mass term is diagonal Non diagonal mass term found:                                                                                                                                                                                                                                                                                          
HEPTAPOD-CHECK|scope=model|name=mass_spectrum|verdict=inconclusive|detail=Neglecting all terms with more than 2 particles. Warning: not numerical value encountered. Unable to decide whether mass term is diagonal Non diagonal mass term found:                                                                                                                                                                                                                                         
[INFO] UFO output: /tmp/repair_corrected/Wprime/round0/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
98 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 98.
93 vertices obtained.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 93
   - Saved vertices in InterfaceRun[ 1 ].
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/163 .
    - Writing files.
Done!
[INFO] UFO complete: particles.py, vertices.py, couplings.py, parameters.py, coupling_orders.py all present.
[INFO] Done.

```
