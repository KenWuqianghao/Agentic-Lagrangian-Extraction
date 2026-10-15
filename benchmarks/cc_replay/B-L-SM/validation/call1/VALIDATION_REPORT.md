# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- FeynRules check `hermiticity`: pass
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: pass
- FeynRules check `mass_spectrum`: pass
- MadGraph import: False
- Heuristic error tags: duplicate_particle_names, mg5_import_fail, ufo_semantic_error, mg5_python_traceback, mg5_invalid_cmd

## FeynRules / Wolfram Engine output (tail)
```
different names.

General::stop: Further output of Warning : All particles should have different names. will be suppressed during this calculation.
Merging model-files...

MergeModels::Particles: Warning: Doubly defined particle classes.
This model implementation was created by
Automated extraction, B-L-SM benchmark
Model Version: 1.0
https://arxiv.org/abs/1811.11452
For more information, type ModelInformation[].

   - Loading particle classes.

LoadModel::Part: Warning : All particles should have different names.

LoadModel::Part: Warning : All particles should have different names.
   - Loading gauge group classes.
   - Loading parameter classes.

Model B-L-SM_gen loaded.
[INFO] Lagrangian: LTotal
HEPTAPOD-GAUGE|feynman=True|source=SM.fr (inherited unless the model overrides it)
HEPTAPOD-LAGRANGIAN|expression=LTotal|symbols=LTotal|terms=907
HEPTAPOD-RESIDUAL|count=0|fields=

Global`a$::shdw: Symbol a$ appears in multiple contexts {Global`, FeynRules`}; definitions in context Global` may shadow or be shadowed by other definitions.
[INFO] Running consistency checks: hermiticity, kinetic_diagonal, mass_diagonal, mass_spectrum
HEPTAPOD-CHECK|scope=model|name=hermiticity|verdict=pass|detail=Checking for hermiticity by calculating the Feynman rules contained in L-HC[L]. If the lagrangian is hermitian, then the number of vertices should be zero. Starting Feynman rule calculation. Expanding the Lagrangian... Expanding the indices over 8 cores Collecting the different structures that enter the vertex. No vertices found. 0 vertices obtained. The lagrangian is hermitian.
HEPTAPOD-CHECK|scope=model|name=kinetic_diagonal|verdict=pass|detail=Neglecting all terms with more than 2 particles. All kinetic terms are diagonal.
HEPTAPOD-CHECK|scope=model|name=mass_diagonal|verdict=pass|detail=All mass terms are diagonal.
Neglecting all terms with more than 2 particles.
All mass terms are diagonal.
Warning: mass term for {G0, G0}seems not to have the correct sign.
Warning: mass term for {GP, GPbar}seems not to have the correct sign.
Getting mass spectrum.
Checking for less then 0.1% agreement with model file values.
HEPTAPOD-MASS|particle=G02|derived=7000.|declared=7000.|agrees=True
HEPTAPOD-MASS|particle=HH|derived=309.9999999999999|declared=310.|agrees=True
HEPTAPOD-MASS|particle=H|derived=124.99999999999906|declared=125.|agrees=True
HEPTAPOD-MASS|particle=ghWm|derived=79.82435974619786|declared=79.82435974619784|agrees=True
HEPTAPOD-MASS|particle=ghWp|derived=79.82435974619786|declared=79.82435974619784|agrees=True
HEPTAPOD-MASS|particle=ghZ|derived=91.18760000000003|declared=91.1876|agrees=True
HEPTAPOD-MASS|particle=N1|derived=1400.|declared=1400.|agrees=True
HEPTAPOD-MASS|particle=N2|derived=1400.|declared=1400.|agrees=True
HEPTAPOD-MASS|particle=N3|derived=1400.|declared=1400.|agrees=True
HEPTAPOD-MASS|particle=b|derived=4.700000000000002|declared=4.7|agrees=True
HEPTAPOD-MASS|particle=d|derived=0.005040000000000001|declared=0.00504|agrees=True
HEPTAPOD-MASS|particle=s|derived=0.10100000000000002|declared=0.101|agrees=True
HEPTAPOD-MASS|particle=e|derived=0.0005110000000000001|declared=0.000511|agrees=True
HEPTAPOD-MASS|particle=mu|derived=0.10566000000000003|declared=0.10566|agrees=True
HEPTAPOD-MASS|particle=ta|derived=1.7770000000000006|declared=1.777|agrees=True
HEPTAPOD-MASS|particle=c|derived=1.2700000000000002|declared=1.27|agrees=True
HEPTAPOD-MASS|particle=t|derived=172.00000000000003|declared=172.|agrees=True
HEPTAPOD-MASS|particle=u|derived=0.002550000000000001|declared=0.00255|agrees=True
HEPTAPOD-MASS|particle=W|derived=79.82435974619786|declared=79.82435974619784|agrees=True
HEPTAPOD-MASS|particle=Z|derived=91.18760000000003|declared=91.1876|agrees=True
HEPTAPOD-MASS|particle=ZP|derived=7000.000000000001|declared=7000.|agrees=True
HEPTAPOD-CHECK|scope=model|name=mass_spectrum|verdict=pass|detail=
[INFO] UFO output: /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/B-L-SM/validation/call1/round0/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
292 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 292.
265 vertices obtained.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 265
   - Saved vertices in InterfaceRun[ 1 ].
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/265 .
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
rt_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/B-L-SM/validation/call1/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/B-L-SM/validation/call1/round0/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
del not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/B-L-SM/validation/call1/round0/UFO
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

## UFO direct-import error (the REAL reason MadGraph rejects this UFO — MadGraph's own message misreports the location)
Fix the .fr declaration that produced this; the UFO is regenerated from model.fr each round.
```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    __import__('UFO')
    ~~~~~~~~~~^^^^^^^
  File "/Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/B-L-SM/validation/call1/round0/UFO/__init__.py", line 2, in <module>
    import particles
  File "/Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/B-L-SM/validation/call1/round0/UFO/particles.py", line 25, in <module>
    B_L = (B_L)[A])
           ^^^
NameError: name 'B_L' is not defined

```
