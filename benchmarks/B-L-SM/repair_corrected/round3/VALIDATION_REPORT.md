# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- FeynRules check `hermiticity`: pass
- FeynRules check `kinetic_diagonal`: fail
- FeynRules check `mass_diagonal`: fail
- FeynRules check `mass_spectrum`: inconclusive
- MadGraph import: False
- Heuristic error tags: selfconjugate_quantum_numbers, kinetic_diagonal_fail, mass_diagonal_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd

## FeynRules check `kinetic_diagonal`: fail
Kinetic terms are not diagonal: two fields mix at quadratic order, so the fields in the Lagrangian are not mass eigenstates. Rotate them to the mass basis, or declare the mixing so FeynRules can do it. (Neglecting all terms with more than 2 particles. Non diagonal kinetic term found: -(ca sa del[H, Index[Lorentz, mu]] del[H2, Index[Lorentz, mu]]))

## FeynRules check `mass_diagonal`: fail
Mass terms are not diagonal: the mass matrix mixes fields, so the declared particles are not mass eigenstates. Diagonalise the mass matrix, or declare the mixing. (Non diagonal mass term found:                                             2                     ca H H2 lambda3BL sa vev                                                          2 ca H H2 muChi2 sa + ------------------------- - ca H H2 lambda3BL vev xBL + 3 ca H H2 lambda2BL sa xBL                                 2 Non diagonal mass term found:   vev N1bar[Index[Spin, r$18612]] . ve[Index[Spin, r$)

## FeynRules check `mass_spectrum`: inconclusive
The mass spectrum could not be computed. This usually means the mass terms are not diagonal -- see that result. (Neglecting all terms with more than 2 particles. Non diagonal mass term found:                                             2                     ca H H2 lambda3BL sa vev                                                          2 ca H H2 muChi2 sa + ------------------------- - ca H H2 lambda3BL vev xBL + 3 ca H H2 lambda2BL sa xBL                                 2 Non diagonal mass term found:   ve)

## FeynRules / Wolfram Engine output (tail)
```
 N1}.
Quantum number LeptonNumber not conserved in vertex {G0, vebar, N2}.
Quantum number LeptonNumber not conserved in vertex {G0, vebar, N3}.
Quantum number LeptonNumber not conserved in vertex {G0, vmbar, N1}.
Quantum number LeptonNumber not conserved in vertex {G0, vmbar, N2}.
Quantum number LeptonNumber not conserved in vertex {G0, vmbar, N3}.
Quantum number LeptonNumber not conserved in vertex {G0, vtbar, N1}.
Quantum number LeptonNumber not conserved in vertex {G0, vtbar, N2}.
Quantum number LeptonNumber not conserved in vertex {G0, vtbar, N3}.
Quantum number LeptonNumber not conserved in vertex {H, vebar, N1}.
Quantum number LeptonNumber not conserved in vertex {H, vebar, N2}.
Quantum number LeptonNumber not conserved in vertex {H, vebar, N3}.
Quantum number LeptonNumber not conserved in vertex {H, vmbar, N1}.
Quantum number LeptonNumber not conserved in vertex {H, vmbar, N2}.
Quantum number LeptonNumber not conserved in vertex {H, vmbar, N3}.
Quantum number LeptonNumber not conserved in vertex {H, vtbar, N1}.
Quantum number LeptonNumber not conserved in vertex {H, vtbar, N2}.
Quantum number LeptonNumber not conserved in vertex {H, vtbar, N3}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
From kernel 1 (Local):
ReplaceAll::reps: {yM} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 2 (Local):
ReplaceAll::reps: {yM} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 3 (Local):
ReplaceAll::reps: {yM} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 4 (Local):
ReplaceAll::reps: {yM} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 5 (Local):
ReplaceAll::reps: {yM} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of `1` is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing. will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of ReplaceAll::reps will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of ReplaceAll::reps will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of ReplaceAll::reps will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of ReplaceAll::reps will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of ReplaceAll::reps will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
From kernel 1 (Local):
ReplaceAll::reps: {yM} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 2 (Local):
ReplaceAll::reps: {yM} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 3 (Local):
ReplaceAll::reps: {yM} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 4 (Local):
ReplaceAll::reps: {yM} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 5 (Local):
ReplaceAll::reps: {yM} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of `1` is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing. will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of ReplaceAll::reps will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of ReplaceAll::reps will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of ReplaceAll::reps will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of ReplaceAll::reps will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of ReplaceAll::reps will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/201 .
    - Writing files.
Warning: Non positive interaction order QED.
                This might reduce the efficiency of certain matrix element generators.
                See logfile for more details.
Done!
[INFO] UFO complete: particles.py, vertices.py, couplings.py, parameters.py, coupling_orders.py all present.
[INFO] Done.

```

## MadGraph import output (tail)
```
dels/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /private/tmp/repair_corrected/B-L-SM/round2/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_corrected/B-L-SM/round2/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
aph_interface.py", line 5837, in do_import
    raise self.InvalidCmd('UFO model not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /tmp/repair_corrected/B-L-SM/round2/UFO
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

## UFO Python syntax error — `UFO/parameters.py` line 498: invalid syntax
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
  496 |                 texname = '\\text{x}')
  497 | 
  498 | yM1x2 /. yM = Parameter(name = 'yM1x2 /. yM',
  499 |                         nature = 'internal',
  500 |                         type = 'real',
```

## UFO direct-import error (the REAL reason MadGraph rejects this UFO — MadGraph's own message misreports the location)
Fix the .fr declaration that produced this; the UFO is regenerated from model.fr each round.
```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    __import__('UFO')
    ~~~~~~~~~~^^^^^^^
  File "/tmp/repair_corrected/B-L-SM/round2/UFO/__init__.py", line 2, in <module>
    import particles
  File "/tmp/repair_corrected/B-L-SM/round2/UFO/particles.py", line 8, in <module>
    import parameters as Param
  File "/tmp/repair_corrected/B-L-SM/round2/UFO/parameters.py", line 498
    yM1x2 /. yM = Parameter(name = 'yM1x2 /. yM',
           ^
SyntaxError: invalid syntax

```
