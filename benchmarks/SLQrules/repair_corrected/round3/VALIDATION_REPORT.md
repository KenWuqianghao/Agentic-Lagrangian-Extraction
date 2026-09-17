# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- FeynRules check `hermiticity`: fail
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: fail
- FeynRules check `mass_spectrum`: inconclusive
- MadGraph import: False
- Heuristic error tags: hermiticity_fail, mass_diagonal_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd

## FeynRules check `hermiticity`: fail
The Lagrangian is not Hermitian: FeynRules found residual terms in L - HC[L]. Almost always a term is missing its conjugate -- add `+ HC[...]` around the offending interaction, or write the conjugate out explicitly. (Checking for hermiticity by calculating the Feynman rules contained in L-HC[L]. If the lagrangian is hermitian, then the number of vertices should be zero. Starting Feynman rule calculation. Expanding the Lagrangian... Expanding the indices over 8 cores Collecting the different structures that enter the vertex. 80 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$F)

## FeynRules check `mass_diagonal`: fail
Mass terms are not diagonal: the mass matrix mixes fields, so the declared particles are not mass eigenstates. Diagonalise the mass matrix, or declare the mixing. (Warning: not numerical value encountered. Unable to decide whether mass term is diagonal Non diagonal mass term found: Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 1]]] lbar[Index[Spin, r$18754]] . HC[ProjR] . HC[Qbar[1, 2, aa$18126]] Ga[0, r$18754, 1] R2p23hatbar[Index[Colour, aa$18126]] + Conjugate[Y2LR[Index[Generation, 2], Index[Generation, 1]]] lbar[Index[Spin, r$18754]] . HC[ProjR])

## FeynRules check `mass_spectrum`: inconclusive
The mass spectrum could not be computed. This usually means the mass terms are not diagonal -- see that result. (Neglecting all terms with more than 2 particles. Warning: not numerical value encountered. Unable to decide whether mass term is diagonal Non diagonal mass term found: Conjugate[Y2LR[Index[Generation, 1], Index[Generation, 1]]] lbar[Index[Spin, r$18754]] . HC[ProjR] . HC[Qbar[1, 2, aa$18126]] Ga[0, r$18754, 1] R2p23hatbar[Index[Colour, aa$18126]] + Conjugate[Y2LR[Index[Generation, 2], Index[Genera)

## FeynRules / Wolfram Engine output (tail)
```
qbar[Index[Spin, 3], 3] . ProjL . LL[Index[Spin, 3], 1] Eps[Index[SU2D, Ext[1]], 1] IndexDelta[Index[Colour, Ext[1]], Index[Colour, 3]] Y2RL[Index[Generation, 3], Index[Generation, 3]] + uqbar[Index[Spin, 3], 3] . ProjL . LL[Index[Spin, 3], 2] Eps[Index[SU2D, Ext[1]], 2] IndexDelta[Index[Colour, Ext[1]], Index[Colour, 3]] Y2RL[Index[Generation, 3], Index[Generation, 3]]" cannot be used for a symbol name. A symbol name must start with a letter followed by letters and numbers.

General::stop: Further output of Symbol::symname will be suppressed during this calculation.
From kernel 4 (Local):
Table::iterb: Iterator {Index[Colour, Ext[1]], NoUnfold[{1, 2, 3}]} does not have appropriate bounds.
From kernel 4 (Local):
Table::iterb: Iterator {Index[Colour, Ext[1]], NoUnfold[{1, 2, 3}]} does not have appropriate bounds.
From kernel 5 (Local):
Table::iterb: Iterator {Index[Colour, Ext[1]], NoUnfold[{1, 2, 3}]} does not have appropriate bounds.
From kernel 6 (Local):
Table::iterb: Iterator {Index[Colour, Ext[1]], NoUnfold[{1, 2, 3}]} does not have appropriate bounds.
From kernel 7 (Local):
Table::iterb: Iterator {Index[Colour, Ext[1]], NoUnfold[{1, 2, 3}]} does not have appropriate bounds.

General::stop: Further output of Table::iterb will be suppressed during this calculation.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 154
   - Saved vertices in InterfaceRun[ 1 ].
Quantum number Y not conserved in vertex {Phi, R2bar}.
Quantum number Y not conserved in vertex {Phi, R2tbar, S1}.
Quantum number Y not conserved in vertex {Phibar, R2}.
Quantum number Y not conserved in vertex {Phibar, R2t, S1bar}.
Quantum number Q not conserved in vertex {R2t, R2t, S1m13hat}.
Quantum number Q not conserved in vertex {R2tbar, R2tbar, S1m13hatbar}.
Quantum number Q not conserved in vertex {R2, R2t, S1tm43hat}.
Quantum number Q not conserved in vertex {Phi, R2, S1m13hat, S1tm43hat}.
Quantum number Y not conserved in vertex {Phi, R2, S1m13hat, S1tm43hat}.
Quantum number Q not conserved in vertex {R2, R2tbar, S1m13hatbar, S1tm43hat}.
Quantum number Q not conserved in vertex {R2bar, R2tbar, S1tm43hatbar}.
Quantum number Q not conserved in vertex {Phibar, R2bar, S1m13hatbar, S1tm43hatbar}.
Quantum number Y not conserved in vertex {Phibar, R2bar, S1m13hatbar, S1tm43hatbar}.
Quantum number Q not conserved in vertex {R2bar, R2t, S1m13hat, S1tm43hatbar}.
Quantum number Q not conserved in vertex {Phibar, R2, S1m13hat, S3}.
Quantum number Y not conserved in vertex {Phibar, R2, S1m13hat, S3}.
Quantum number Q not conserved in vertex {Phi, R2t, S1m13hat, S3}.
Quantum number Y not conserved in vertex {Phi, R2t, S1m13hat, S3}.
Quantum number Q not conserved in vertex {Phi, R2, S1tm43hat, S3}.
Quantum number Y not conserved in vertex {Phi, R2, S1tm43hat, S3}.
Quantum number Q not conserved in vertex {R2, R2bar, S1m13hatbar, S3}.
Quantum number Q not conserved in vertex {R2t, R2tbar, S1m13hatbar, S3}.
Quantum number Q not conserved in vertex {R2bar, R2t, S1tm43hatbar, S3}.
Quantum number Q not conserved in vertex {S1m13hatbar, S1m13hatbar, S3, S3}.
Quantum number Y not conserved in vertex {Phibar, R2, S3, S3}.
Quantum number Y not conserved in vertex {Phi, R2t, S3, S3}.
Quantum number Q not conserved in vertex {Phi, R2bar, S1m13hatbar, S3bar}.
Quantum number Y not conserved in vertex {Phi, R2bar, S1m13hatbar, S3bar}.
Quantum number Q not conserved in vertex {Phibar, R2tbar, S1m13hatbar, S3bar}.
Quantum number Y not conserved in vertex {Phibar, R2tbar, S1m13hatbar, S3bar}.
Quantum number Q not conserved in vertex {Phibar, R2bar, S1tm43hatbar, S3bar}.
Quantum number Y not conserved in vertex {Phibar, R2bar, S1tm43hatbar, S3bar}.
Quantum number Q not conserved in vertex {R2, R2bar, S1m13hat, S3bar}.
Quantum number Q not conserved in vertex {R2t, R2tbar, S1m13hat, S3bar}.
Quantum number Q not conserved in vertex {R2, R2tbar, S1tm43hat, S3bar}.
Quantum number Q not conserved in vertex {S1m13hat, S1m13hat, S3bar, S3bar}.
Quantum number Q not conserved in vertex {S1m13hatbar, S3, S3, S3bar}.
Quantum number Y not conserved in vertex {Phi, R2bar, S3bar, S3bar}.
Quantum number Y not conserved in vertex {Phibar, R2tbar, S3bar, S3bar}.
Quantum number Q not conserved in vertex {S1m13hat, S3, S3bar, S3bar}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/224 .
    - Writing files.

StringJoin::string: String expected at position 2 in P.<>CreateObjectParticleName[PartNameMG[Phibar]].

StringJoin::string: String expected at position 2 in P.<>CreateObjectParticleName[PartNameMG[Phi]].

StringJoin::string: String expected at position 2 in P.<>CreateObjectParticleName[PartNameMG[R2bar]].

General::stop: Further output of StringJoin::string will be suppressed during this calculation.
Done!
[INFO] UFO complete: particles.py, vertices.py, couplings.py, parameters.py, coupling_orders.py all present.
[INFO] Done.

```

## MadGraph import output (tail)
```
/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /private/tmp/repair_corrected/SLQrules/round2/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_corrected/SLQrules/round2/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
h_interface.py", line 5837, in do_import
    raise self.InvalidCmd('UFO model not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /tmp/repair_corrected/SLQrules/round2/UFO
You can also type "set auto_convert_model T" to automatically convert all python2 module to be python3 compatible in the future.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/kenwu/MG5_aMC/madgraph/interface/extended_cmd.py", line 1570, in onecmd
    return self.onecmd_orig(line, **opt)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/madgraph/interface/extended_cmd.py", line 1519, in onecmd_orig
    return func(arg, **opt)
  File "/Users/kenwu/MG5_aMC/madgraph/interface/master_interface.py", line 281, in do_import
    self.cmd.do_import(self, *args, **opts)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/madgraph/interface/madgraph_interface.py", line 5893, in do_import
    self.import_command_file(args[1])
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/madgraph/interface/extended_cmd.py", line 1718, in import_command_file
    self.exec_cmd(line, precmd=True)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/madgraph/interface/extended_cmd.py", line 1599, in exec_cmd
    stop = Cmd.onecmd_orig(current_interface, line, **opt)
  File "/Users/kenwu/MG5_aMC/madgraph/interface/extended_cmd.py", line 1519, in onecmd_orig
    return func(arg, **opt)
  File "/Users/kenwu/MG5_aMC/madgraph/interface/master_interface.py", line 281, in do_import
    self.cmd.do_import(self, *args, **opts)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/madgraph/interface/madgraph_interface.py", line 5835, in do_import
    raise err
  File "/Users/kenwu/MG5_aMC/madgraph/interface/madgraph_interface.py", line 5819, in do_import
    self._curr_model = import_ufo.import_model(args[1], prefix=prefix,
                       ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
        complex_mass_scheme=self.options['complex_mass_scheme'],
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        options=options)
        ^^^^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
Fail to write options with error No model currently active, please import a model!
```

## UFO Python syntax error — `UFO/lorentz.py` line 15: cannot assign to literal here. Maybe you meant '==' instead of '='?
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
   13 | 
   14 | 
   15 | 1 = Lorentz(name = '1',
   16 |             spins = [],
   17 |             structure = '1')
```

## UFO Python syntax error — `UFO/vertices.py` line 217: invalid syntax
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
  215 | 
  216 | V_35 = Vertex(name = 'V_35',
  217 |               particles = [ P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]], P.<>CreateObjectParticleName[PartNameMG[R2bar]], P.<>CreateObjectParticleName[PartNameMG[R2]] ],
  218 |               color = [ '1' ],
  219 |               lorentz = [ L.SSSS1 ],
```

## UFO direct-import error (the REAL reason MadGraph rejects this UFO — MadGraph's own message misreports the location)
Fix the .fr declaration that produced this; the UFO is regenerated from model.fr each round.
```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    __import__('UFO')
    ~~~~~~~~~~^^^^^^^
  File "/tmp/repair_corrected/SLQrules/round2/UFO/__init__.py", line 2, in <module>
    import particles
  File "/tmp/repair_corrected/SLQrules/round2/UFO/particles.py", line 393, in <module>
    mass = Param.m1m13hat,
           ^^^^^^^^^^^^^^
AttributeError: module 'parameters' has no attribute 'm1m13hat'

```
