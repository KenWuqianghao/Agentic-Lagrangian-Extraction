{
 "call": 1,
 "stage": "madgraph_failed",
 "full_chain_pass": false,
 "compile_ok": true,
 "checks": {
  "hermiticity": "pass",
  "kinetic_diagonal": "pass",
  "mass_diagonal": "pass",
  "mass_spectrum": "pass"
 },
 "madgraph_import_ok": false,
 "lagrangian_expression": "LTotal",
 "error_tags": [
  "duplicate_particle_names",
  "mg5_import_fail",
  "ufo_semantic_error",
  "mg5_python_traceback",
  "mg5_invalid_cmd"
 ],
 "seconds": 137.2,
 "lock_wait_seconds": 0.0,
 "t_kernel_start": 1790744223.873,
 "t_kernel_end": 1790744361.872,
 "stage_reached": "mg5",
 "driver": "diag"
}

# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- FeynRules check `hermiticity`: pass
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: pass
- FeynRules check `mass_spectrum`: pass
- MadGraph import: False
- Heuristic error tags: duplicate_particle_names, mg5_import_fail, ufo_semantic_error, mg5_python_traceback, mg5_invalid_cmd

## MadGraph import: where the UFO breaks, and the model.fr lines behind it

### `UFO/particles.py` line 25, object `a`: NameError: name 'B_L' is not defined
```
a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0,
             B_L = (B_L)[A])

```
model.fr lines:
- line 252 (use): `QuantumNumbers  -> {B_L -> 2},`
- line 267 (use): `QuantumNumbers   -> {B_L -> -1, LeptonNumber -> 1},`

## compile log, distinct lines (tail)
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
MergeModels::Particles: Warning: Doubly defined particle classes.
LoadModel::Part: Warning : All particles should have different names.
Merging model-files...
This model implementation was created by
Automated extraction, B-L-SM benchmark
Model Version: 1.0
https://arxiv.org/abs/1811.11452
For more information, type ModelInformation[].
   - Loading particle classes.
   - Loading gauge group classes.
   - Loading parameter classes.
Model B-L-SM_gen loaded.
[INFO] Lagrangian: LTotal
Global`a$::shdw: Symbol a$ appears in multiple contexts {Global`, FeynRules`}; definitions in context Global` may shadow or be shadowed by other definitions.
[INFO] Running consistency checks: hermiticity, kinetic_diagonal, mass_diagonal, mass_spectrum
Neglecting all terms with more than 2 particles.
All mass terms are diagonal.
Warning: mass term for {G0, G0}seems not to have the correct sign.
Warning: mass term for {GP, GPbar}seems not to have the correct sign.
Getting mass spectrum.
Checking for less then 0.1% agreement with model file values.
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
  
