# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- FeynRules check `hermiticity`: fail
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: pass
- FeynRules check `mass_spectrum`: pass
- MadGraph import: False
- Heuristic error tags: hermiticity_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd

## FeynRules check `hermiticity`: fail
The Lagrangian is not Hermitian: FeynRules found residual terms in L - HC[L]. Almost always a term is missing its conjugate -- add `+ HC[...]` around the offending interaction, or write the conjugate out explicitly. (Checking for hermiticity by calculating the Feynman rules contained in L-HC[L]. If the lagrangian is hermitian, then the number of vertices should be zero. Starting Feynman rule calculation. Expanding the Lagrangian... Expanding the indices over 8 cores Collecting the different structures that enter the vertex. 28 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$F)

## FeynRules / Wolfram Engine output (tail)
```
 Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 4 (Local):
ReplaceAll::reps: {Rule[Ext[n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . e[Index[Spin, SP$1]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 5 (Local):
ReplaceAll::reps: {Rule[Ext[n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . e[Index[Spin, SP$1]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of `1` is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing. will be suppressed during this calculation.
From kernel 1 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 2 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 3 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 4 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
From kernel 5 (Local):
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.

General::stop: Further output of Rule::argrx will be suppressed during this calculation.
From kernel 1 (Local):
ReplaceAll::reps: {Rule[Ext[n4[Index[Spin, SP$1]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . e[Index[Spin, SP$1]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 2 (Local):
ReplaceAll::reps: {Rule[Ext[n4[Index[Spin, SP$1]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . e[Index[Spin, SP$1]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 3 (Local):
ReplaceAll::reps: {Rule[Ext[n4[Index[Spin, SP$1]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . e[Index[Spin, SP$1]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 4 (Local):
ReplaceAll::reps: {Rule[Ext[n4[Index[Spin, SP$1]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . e[Index[Spin, SP$1]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 5 (Local):
ReplaceAll::reps: {Rule[Ext[n4[Index[Spin, SP$1]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . e[Index[Spin, SP$1]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of `1` is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing. will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of Rule::argrx will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of Rule::argrx will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of Rule::argrx will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of Rule::argrx will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of Rule::argrx will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/202 .

StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 2 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 3 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1.

General::stop: Further output of StringJoin::string will be suppressed during this calculation.
    - Writing files.
Done!
[INFO] UFO complete: particles.py, vertices.py, couplings.py, parameters.py, coupling_orders.py all present.
[INFO] Done.

```

## MadGraph import output (tail)
```
port_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/pSPSS/validation/call1/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/pSPSS/validation/call1/round0/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
odel not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/pSPSS/validation/call1/round0/UFO
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

## UFO Python syntax error — `UFO/couplings.py` line 642: unterminated string literal (detected at line 642)
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
  640 | GC_158 = Coupling(name = 'GC_158',
  641 |                   value = 'ReplaceAll((ee*complex(0,1)*UnCL1x4*Dot(n4(-1),Gamma(1),ProjM,e(-1)))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UnCL2x4*Dot(n4(-1),Gamma(1),ProjM,mu(-1)))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UnCL3x4*Dot(n4(-1),Gamma(1),ProjM,ta(-1)))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UnC
  642 |                   order = {'                    I ee UnCL1x4 n4[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . e[Index[Spin, Int[1]]]   I ee UnCL2x4 n4[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . mu[Index[Spin, Int[1]]]   I ee UnCL3x4 n4[Index[Spin, Int[1]]] . L$
  643 | PRIVATE`GetIntOrder[------------------------------------------------------------------------------------------------------ + ------------------------------------------------------------------------------------------------------- + ---------------------------------------------------------------------
  644 |                                                                   Sqrt[2] sw                                                                                               Sqrt[2] sw                                                                                                Sqrt[2] sw             
```

## UFO Python syntax error — `UFO/vertices.py` line 616: closing parenthesis ')' does not match opening parenthesis '[' on line 613
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
  614 |                color = [ '1' ],
  615 |                lorentz = [ L.<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1 ],
  616 |                couplings = {(0,-1 + PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1):C.GC_158})
  617 | 
  618 | V_102 = Vertex(name = 'V_102',
```

## UFO direct-import error (the REAL reason MadGraph rejects this UFO — MadGraph's own message misreports the location)
Fix the .fr declaration that produced this; the UFO is regenerated from model.fr each round.
```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    __import__('UFO')
    ~~~~~~~~~~^^^^^^^
  File "/Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/pSPSS/validation/call1/round0/UFO/__init__.py", line 3, in <module>
    import couplings
  File "/Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/pSPSS/validation/call1/round0/UFO/couplings.py", line 642
    order = {'                    I ee UnCL1x4 n4[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . e[Index[Spin, Int[1]]]   I ee UnCL2x4 n4[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . mu[Index[Spin, Int[1]]]   I ee UnCL3x4 n4[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . ta[Index[Spin, Int[1]]]   I ee UnCL1x5 n5[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . e[Index[Spin, Int[1]]]   I ee UnCL2x5 n5[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . mu[Index[Spin, Int[1]]]   I ee UnCL3x5 n5[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . ta[Index[Spin, Int[1]]]
             ^
SyntaxError: unterminated string literal (detected at line 642)

```
