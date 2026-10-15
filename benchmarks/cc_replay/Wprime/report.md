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
  "mg5_import_fail",
  "ufo_python_syntax_error",
  "mg5_python_traceback",
  "mg5_invalid_cmd"
 ],
 "seconds": 78.5,
 "lock_wait_seconds": 0.0,
 "t_kernel_start": 1790744444.611,
 "t_kernel_end": 1790744523.718,
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
- Heuristic error tags: mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd

## MadGraph import: where the UFO breaks, and the model.fr lines behind it

### `UFO/parameters.py` line 90, object `WpLeR1`: positional argument follows keyword argument
```
WpLeR1 = Parameter(name = 'WpLeR1',
                   nature = 'external',
                   type = 'complex',
                   value = 1.,
                   texname = '\\text{WpLeR1}',
                   lhablock = 'WPRIME',
ClassAttributeCreation[lhacode, PYList[{1} /. 7], 19]<>)

```
model.fr lines:
- line 128 (declaration): `WpLeR == {`
  ```
    WpLeR == {
      ParameterType    -> External,
      BlockName        -> WPRIME,
      OrderBlock       -> 7,
      Indices          -> {Index[Generation]},
      InteractionOrder -> {NP, 1},
      TeX              -> "V^R_{l nu}",
      Value -> {
        WpLeR[1] -> 1., WpLeR[2] -> 1., WpLeR[3] -> 1.
      },
      Description -> "Couplings of W' to charged leptons and the right-handed neutrino NR; paper: V'_{l nu} is the identity"
    },
  ```
- line 136 (use): `WpLeR[1] -> 1., WpLeR[2] -> 1., WpLeR[3] -> 1.`
- line 251 (use): `gRp Eom CZ WpLeR NRbar.Ga[mu].ProjP.l +`

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
ReplaceAll::reps: {5} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
Merging model-files...
This model implementation was created by
Benchmark automated extraction
Model Version: 1.0
arXiv:hep-ph/0207290
For more information, type ModelInformation[].
   - Loading particle classes.
   - Loading gauge group classes.
   - Loading parameter classes.
Model Wprime_gen loaded.
[INFO] Lagrangian: LTotal
Global`a$::shdw: Symbol a$ appears in multiple contexts {Global`, FeynRules`}; definitions in context Global` may shadow or be shadowed by other definitions.
[INFO] Running consistency checks: hermiticity, kinetic_diagonal, mass_diagonal, mass_spectrum
Neglecting all terms with more than 2 particles.
All mass terms are diagonal.
Getting mass spectrum.
Checking for less then 0.1% agreement with model file values.
[INFO] UFO output: /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/Wprime/validation/call1/round0/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
208 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 208.
181 vertices obtained.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 181
   - Saved vertices in InterfaceRun[ 1 ].
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/181 .
    - Writing files.
StringJoin::string: String expected at position 1 in ClassAttributeCreation[lhacode, PYList[{1} /. 7], 19]<>).
StringJoin::string: String expected at position 1 in ClassAttributeCreation[lhacode, PYList[{2} /. 7], 19]<>).
StringJoin::string: String expected at position 1 in ClassAttributeCreation[lhacode, PYList[{3} /. 7], 19]<>).
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
[1;31mCommand "import /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/Wprime/validation/call1/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/Wprime/validation/call1/round0/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
del not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/Wprime/validation/call1/round0/UFO
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
  
