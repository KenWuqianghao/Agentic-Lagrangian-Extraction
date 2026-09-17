# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- FeynRules check `hermiticity`: fail
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: fail
- FeynRules check `mass_spectrum`: inconclusive
- MadGraph import: True
- Heuristic error tags: duplicate_particle_names, hermiticity_fail, mass_diagonal_fail

## FeynRules check `hermiticity`: fail
The Lagrangian is not Hermitian: FeynRules found residual terms in L - HC[L]. Almost always a term is missing its conjugate -- add `+ HC[...]` around the offending interaction, or write the conjugate out explicitly. (Checking for hermiticity by calculating the Feynman rules contained in L-HC[L]. If the lagrangian is hermitian, then the number of vertices should be zero. Starting Feynman rule calculation. Expanding the Lagrangian... Expanding the indices over 8 cores Collecting the different structures that enter the vertex. 21 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$F)

## FeynRules check `mass_diagonal`: fail
Mass terms are not diagonal: the mass matrix mixes fields, so the declared particles are not mass eigenstates. Diagonalise the mass matrix, or declare the mixing. (Warning: not numerical value encountered. Unable to decide whether mass term is diagonal Non diagonal mass term found:                                                                                   2                          2                                                                                                           2                         2           2)

## FeynRules check `mass_spectrum`: inconclusive
The mass spectrum could not be computed. This usually means the mass terms are not diagonal -- see that result. (Neglecting all terms with more than 2 particles. Warning: not numerical value encountered. Unable to decide whether mass term is diagonal Non diagonal mass term found:                                                                                   2                          2                                                                                                           2)

## FeynRules / Wolfram Engine output (tail)
```
ld have different names.
From kernel 7 (Local):
LoadModel::Part: Warning : All particles should have different names.

General::stop: Further output of Warning : All particles should have different names. will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of LoadModel::Part will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of LoadModel::Part will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of LoadModel::Part will be suppressed during this calculation.
From kernel 6 (Local):
General::stop: Further output of LoadModel::Part will be suppressed during this calculation.
From kernel 7 (Local):
General::stop: Further output of LoadModel::Part will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
Merging model-files...

MergeModels::Particles: Warning: Doubly defined particle classes.
This model implementation was created by
Junjie Cao
Yangle He
Peiwen Wu
Mengchao Zhang
Jingya Zhu
Model Version: 1.0
For more information, type ModelInformation[].

   - Loading particle classes.

LoadModel::Part: Warning : All particles should have different names.

LoadModel::Part: Warning : All particles should have different names.

LoadModel::Part: Warning : All particles should have different names.

General::stop: Further output of LoadModel::Part will be suppressed during this calculation.
   - Loading gauge group classes.
   - Loading parameter classes.

Model MDMmodel_gen loaded.
[INFO] Lagrangian: LSM + LMDMNP
[INFO] Running consistency checks: hermiticity, kinetic_diagonal, mass_diagonal, mass_spectrum

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
HEPTAPOD-CHECK|scope=model|name=hermiticity|verdict=fail|detail=Checking for hermiticity by calculating the Feynman rules contained in L-HC[L]. If the lagrangian is hermitian, then the number of vertices should be zero. Starting Feynman rule calculation. Expanding the Lagrangian... Expanding the indices over 8 cores Collecting the different structures that enter the vertex. 21 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$F
HEPTAPOD-CHECK|scope=model|name=kinetic_diagonal|verdict=pass|detail=Neglecting all terms with more than 2 particles. All kinetic terms are diagonal.
HEPTAPOD-CHECK|scope=model|name=mass_diagonal|verdict=fail|detail=Warning: not numerical value encountered. Unable to decide whether mass term is diagonal Non diagonal mass term found:                                                                                   2                          2                                                                                                           2                         2           2                         
HEPTAPOD-CHECK|scope=model|name=mass_spectrum|verdict=inconclusive|detail=Neglecting all terms with more than 2 particles. Warning: not numerical value encountered. Unable to decide whether mass term is diagonal Non diagonal mass term found:                                                                                   2                          2                                                                                                           2              
[INFO] UFO output: /tmp/repair_corrected/MDMmodel/round2/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
145 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 145.
140 vertices obtained.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 140
   - Saved vertices in InterfaceRun[ 1 ].
Quantum number Y not conserved in vertex {sDM, tbar, tp}.
Quantum number Y not conserved in vertex {h, tbar, tp}.
Quantum number Y not conserved in vertex {sDM, tpbar, t}.
Quantum number Y not conserved in vertex {h, tpbar, t}.
Quantum number Y not conserved in vertex {GP, tpbar, d}.
Quantum number Y not conserved in vertex {GP, tpbar, s}.
Quantum number Y not conserved in vertex {GP, tpbar, b}.
Quantum number Y not conserved in vertex {G0, tpbar, t}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/214 .
    - Writing files.
Done!
[INFO] UFO complete: particles.py, vertices.py, couplings.py, parameters.py, coupling_orders.py all present.
[INFO] Done.

```
