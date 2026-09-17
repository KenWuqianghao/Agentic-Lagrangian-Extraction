# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- FeynRules check `hermiticity`: pass
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: fail
- FeynRules check `mass_spectrum`: inconclusive
- MadGraph import: False
- Heuristic error tags: builtin_symbol_collision, selfconjugate_quantum_numbers, mass_diagonal_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd

## FeynRules check `mass_diagonal`: fail
Mass terms are not diagonal: the mass matrix mixes fields, so the declared particles are not mass eigenstates. Diagonalise the mass matrix, or declare the mixing. (Warning: not numerical value encountered. Unable to decide whether mass term is diagonal Non diagonal mass term found: -(gWRq CKMR[Index[Generation, 1], Index[Generation, 1]] bar[u[Index[Spin, 1], Index[Colour, 1]]] . Ga[Index[Lorentz, mu]] . ProjP . d[Index[Spin, 1], Index[Colour, 1]] WR[Index[Lorentz, mu]]) - gWRq CKMR[Index[Generation, 1], Index[Generation, 2]] bar[u[Index[Spin, 1], Index[Colou)

## FeynRules check `mass_spectrum`: inconclusive
The mass spectrum could not be computed. This usually means the mass terms are not diagonal -- see that result. (Neglecting all terms with more than 2 particles. Warning: not numerical value encountered. Unable to decide whether mass term is diagonal Non diagonal mass term found: -(gWRq CKMR[Index[Generation, 1], Index[Generation, 1]] bar[u[Index[Spin, 1], Index[Colour, 1]]] . Ga[Index[Lorentz, mu]] . ProjP . d[Index[Spin, 1], Index[Colour, 1]] WR[Index[Lorentz, mu]]) - gWRq CKMR[Index[Generation, 1], Index[)

## FeynRules / Wolfram Engine output (tail)
```
m kernel 2 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
From kernel 1 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 2 are expected to be the same.
From kernel 2 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 2 are expected to be the same.
From kernel 3 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 2 are expected to be the same.
From kernel 4 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 2 are expected to be the same.
From kernel 5 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 2 are expected to be the same.

General::stop: Further output of Join::heads will be suppressed during this calculation.
From kernel 1 (Local):
Part::pkspec1: The expression Index[MR$Null] cannot be used as a part specification.
From kernel 2 (Local):
Part::pkspec1: The expression Index[MR$Null] cannot be used as a part specification.
From kernel 3 (Local):
Part::pkspec1: The expression Index[MR$Null] cannot be used as a part specification.
From kernel 4 (Local):
Part::pkspec1: The expression Index[MR$Null] cannot be used as a part specification.
From kernel 5 (Local):
Part::pkspec1: The expression Index[MR$Null] cannot be used as a part specification.

General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 1 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 2 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 3 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 4 (Local):
Part::partw: Part 1 of {} does not exist.
From kernel 5 (Local):
Part::partw: Part 1 of {} does not exist.

General::stop: Further output of Part::partw will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of Part::pkspec1 will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
From kernel 1 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 2 are expected to be the same.
From kernel 2 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 2 are expected to be the same.
From kernel 3 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 2 are expected to be the same.
From kernel 4 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 2 are expected to be the same.
From kernel 5 (Local):
Join::heads: Heads List and IndexRange at positions 1 and 2 are expected to be the same.

General::stop: Further output of Join::heads will be suppressed during this calculation.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/8 .

StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 2 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 3 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.

General::stop: Further output of StringJoin::string will be suppressed during this calculation.
    - Writing files.
Done!
[INFO] UFO complete: particles.py, vertices.py, couplings.py, parameters.py, coupling_orders.py all present.
[INFO] Done.

```

## MadGraph import output (tail)
```
ls/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /private/tmp/repair_corrected/EffLRSM/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_corrected/EffLRSM/round0/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
ph_interface.py", line 5837, in do_import
    raise self.InvalidCmd('UFO model not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /tmp/repair_corrected/EffLRSM/round0/UFO
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

## UFO Python syntax error — `UFO/vertices.py` line 15: invalid syntax. Perhaps you forgot a comma?
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
   13 |              particles = [],
   14 |              color = [ '1' ],
   15 |              lorentz = [ L.1 ],
   16 |              couplings = {(0,0):C.GC_1})
   17 | 
```

## UFO direct-import error (the REAL reason MadGraph rejects this UFO — MadGraph's own message misreports the location)
Fix the .fr declaration that produced this; the UFO is regenerated from model.fr each round.
```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    __import__('UFO')
    ~~~~~~~~~~^^^^^^^
  File "/tmp/repair_corrected/EffLRSM/round0/UFO/__init__.py", line 4, in <module>
    import lorentz
  File "/tmp/repair_corrected/EffLRSM/round0/UFO/lorentz.py", line 15
    1 = Lorentz(name = '1',
    ^
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?

```
