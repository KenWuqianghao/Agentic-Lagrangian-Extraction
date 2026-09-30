# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- FeynRules check `hermiticity`: fail
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: pass
- FeynRules check `mass_spectrum`: pass
- MadGraph import: False
- Heuristic error tags: hermiticity_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd

## FeynRules check `hermiticity`: fail
The Lagrangian is not Hermitian: FeynRules found residual terms in L - HC[L]. Almost always a term is missing its conjugate -- add `+ HC[...]` around the offending interaction, or write the conjugate out explicitly. (Checking for hermiticity by calculating the Feynman rules contained in L-HC[L]. If the lagrangian is hermitian, then the number of vertices should be zero. Starting Feynman rule calculation. Expanding the Lagrangian... Expanding the indices over 8 cores Collecting the different structures that enter the vertex. 60 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$F)

## FeynRules / Wolfram Engine output (tail)
```
=True
HEPTAPOD-MASS|particle=e|derived=0.0005110000000000001|declared=0.000511|agrees=True
HEPTAPOD-MASS|particle=mu|derived=0.10566000000000003|declared=0.10566|agrees=True
HEPTAPOD-MASS|particle=ta|derived=1.7770000000000006|declared=1.777|agrees=True
HEPTAPOD-MASS|particle=c|derived=1.2700000000000002|declared=1.27|agrees=True
HEPTAPOD-MASS|particle=t|derived=172.00000000000003|declared=172.|agrees=True
HEPTAPOD-MASS|particle=u|derived=0.002550000000000001|declared=0.00255|agrees=True
HEPTAPOD-MASS|particle=W|derived=79.82435974619786|declared=79.82435974619784|agrees=True
HEPTAPOD-MASS|particle=Z|derived=91.18760000000003|declared=91.1876|agrees=True
HEPTAPOD-CHECK|scope=model|name=mass_spectrum|verdict=pass|detail=
HEPTAPOD-HERMBLOCK|block=LFreeN|contents=Nnu Nnubar
HEPTAPOD-HERMBLOCK|block=LG0GP|contents=e G0 GP Nnubar;G0 GP mu Nnubar;G0 GP Nnubar ta
HEPTAPOD-HERMBLOCK|block=LGG0|contents=G0 G0 Nnubar ve;G0 G0 Nnubar vm;G0 G0 Nnubar vt
HEPTAPOD-HERMBLOCK|block=LNG0|contents=G0 H Nnubar ve;G0 H Nnubar vm;G0 H Nnubar vt;G0 Nnubar ve;G0 Nnubar vm;G0 Nnubar vt
HEPTAPOD-HERMBLOCK|block=LNGP|contents=e GP H Nnubar;GP H mu Nnubar;GP H Nnubar ta;e GP Nnubar;GP mu Nnubar;GP Nnubar ta
HEPTAPOD-HERMBLOCK|block=LNW|contents=e Nnubar W;mu Nnubar W;Nnubar ta W
HEPTAPOD-HERMBLOCK|block=LNZ|contents=Nnubar ve Z;Nnubar vm Z;Nnubar vt Z
HEPTAPOD-HERMBLOCK|block=LNh|contents=H H Nnubar ve;H H Nnubar vm;H H Nnubar vt;H Nnubar ve;H Nnubar vm;H Nnubar vt
[INFO] UFO output: /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/SMWeinberg/validation/call2/round0/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
220 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 220.
193 vertices obtained.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 193
   - Saved vertices in InterfaceRun[ 1 ].
Quantum number LeptonNumber not conserved in vertex {G0, GP, Nnubar, e}.
Quantum number LeptonNumber not conserved in vertex {G0, GP, Nnubar, mu}.
Quantum number LeptonNumber not conserved in vertex {G0, GP, Nnubar, ta}.
Quantum number LeptonNumber not conserved in vertex {GP, H, Nnubar, e}.
Quantum number LeptonNumber not conserved in vertex {GP, H, Nnubar, mu}.
Quantum number LeptonNumber not conserved in vertex {GP, H, Nnubar, ta}.
Quantum number LeptonNumber not conserved in vertex {GP, Nnubar, e}.
Quantum number LeptonNumber not conserved in vertex {GP, Nnubar, mu}.
Quantum number LeptonNumber not conserved in vertex {GP, Nnubar, ta}.
Quantum number LeptonNumber not conserved in vertex {G0, G0, Nnubar, ve}.
Quantum number LeptonNumber not conserved in vertex {G0, G0, Nnubar, vm}.
Quantum number LeptonNumber not conserved in vertex {G0, G0, Nnubar, vt}.
Quantum number LeptonNumber not conserved in vertex {G0, H, Nnubar, ve}.
Quantum number LeptonNumber not conserved in vertex {G0, H, Nnubar, vm}.
Quantum number LeptonNumber not conserved in vertex {G0, H, Nnubar, vt}.
Quantum number LeptonNumber not conserved in vertex {H, H, Nnubar, ve}.
Quantum number LeptonNumber not conserved in vertex {H, H, Nnubar, vm}.
Quantum number LeptonNumber not conserved in vertex {H, H, Nnubar, vt}.
Quantum number LeptonNumber not conserved in vertex {G0, Nnubar, ve}.
Quantum number LeptonNumber not conserved in vertex {G0, Nnubar, vm}.
Quantum number LeptonNumber not conserved in vertex {G0, Nnubar, vt}.
Quantum number LeptonNumber not conserved in vertex {H, Nnubar, ve}.
Quantum number LeptonNumber not conserved in vertex {H, Nnubar, vm}.
Quantum number LeptonNumber not conserved in vertex {H, Nnubar, vt}.
Quantum number LeptonNumber not conserved in vertex {W, Nnubar, e}.
Quantum number LeptonNumber not conserved in vertex {W, Nnubar, mu}.
Quantum number LeptonNumber not conserved in vertex {W, Nnubar, ta}.
Quantum number LeptonNumber not conserved in vertex {Z, Nnubar, ve}.
Quantum number LeptonNumber not conserved in vertex {Z, Nnubar, vm}.
Quantum number LeptonNumber not conserved in vertex {Z, Nnubar, vt}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/193 .
    - Writing files.

StringJoin::string: String expected at position 1 in ClassAttributeCreation[lhacode, PYList[{1, 1} /. 2], 19]<>).


StringJoin::string: String expected at position 1 in ClassAttributeCreation[lhacode, PYList[{1, 2} /. 2], 19]<>).


StringJoin::string: String expected at position 1 in ClassAttributeCreation[lhacode, PYList[{1, 3} /. 2], 19]<>).


General::stop: Further output of StringJoin::string will be suppressed during this calculation.
Done!
[INFO] UFO complete: particles.py, vertices.py, couplings.py, parameters.py, coupling_orders.py all present.
[INFO] Done.

```

## MadGraph import output (tail)
```
y", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/SMWeinberg/validation/call2/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/SMWeinberg/validation/call2/round0/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/SMWeinberg/validation/call2/round0/UFO
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

## UFO Python syntax error — `UFO/parameters.py` line 42: positional argument follows keyword argument
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
   40 |                    texname = '\\text{Cll1x1}',
   41 |                    lhablock = 'NUPHYSICS',
   42 | ClassAttributeCreation[lhacode, PYList[{1, 1} /. 2], 19]<>)
   43 | 
   44 | Cll1x2 = Parameter(name = 'Cll1x2',
```

## UFO direct-import error (the REAL reason MadGraph rejects this UFO — MadGraph's own message misreports the location)
Fix the .fr declaration that produced this; the UFO is regenerated from model.fr each round.
```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    __import__('UFO')
    ~~~~~~~~~~^^^^^^^
  File "/Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/SMWeinberg/validation/call2/round0/UFO/__init__.py", line 2, in <module>
    import particles
  File "/Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/SMWeinberg/validation/call2/round0/UFO/particles.py", line 8, in <module>
    import parameters as Param
  File "/Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/SMWeinberg/validation/call2/round0/UFO/parameters.py", line 42
    ClassAttributeCreation[lhacode, PYList[{1, 1} /. 2], 19]<>)
                                                   ^
SyntaxError: positional argument follows keyword argument

```
