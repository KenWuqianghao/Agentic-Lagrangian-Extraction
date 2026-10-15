# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- FeynRules check `hermiticity`: fail
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: pass
- FeynRules check `mass_spectrum`: pass
- MadGraph import: False
- Heuristic error tags: hermiticity_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd

## FeynRules check `hermiticity`: fail
The Lagrangian is not Hermitian: FeynRules found residual terms in L - HC[L]. Almost always a term is missing its conjugate -- add `+ HC[...]` around the offending interaction, or write the conjugate out explicitly. (Checking for hermiticity by calculating the Feynman rules contained in L-HC[L]. If the lagrangian is hermitian, then the number of vertices should be zero. Starting Feynman rule calculation. Expanding the Lagrangian... Expanding the indices over 8 cores Collecting the different structures that enter the vertex. 6 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$Fe)

## FeynRules / Wolfram Engine output (tail)
```
]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 3 (Local):
ReplaceAll::reps: {Rule[Ext[lbar[Index[Spin, a]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . NR1, opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 4 (Local):
ReplaceAll::reps: {Rule[Ext[lbar[Index[Spin, a]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . NR1, opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 6 (Local):
ReplaceAll::reps: {Rule[Ext[lbar[Index[Spin, a]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . NR1, opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 8 (Local):
ReplaceAll::reps: {Rule[Ext[lbar[Index[Spin, a]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . NR1, opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of `1` is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing. will be suppressed during this calculation.

Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.

Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.

General::stop: Further output of Rule::argrx will be suppressed during this calculation.
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
ReplaceAll::reps: {Rule[Ext[lbar[Index[Spin, a]] . L$Ga[0] . L$Ga[Index[Lorentz, Ext[1]]] . NR1, opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 2 (Local):
ReplaceAll::reps: {Rule[Ext[lbar[Index[Spin, a]] . L$Ga[0] . L$Ga[Index[Lorentz, Ext[1]]] . NR1, opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 3 (Local):
ReplaceAll::reps: {Rule[Ext[lbar[Index[Spin, a]] . L$Ga[0] . L$Ga[Index[Lorentz, Ext[1]]] . NR1, opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 4 (Local):
ReplaceAll::reps: {Rule[Ext[lbar[Index[Spin, a]] . L$Ga[0] . L$Ga[Index[Lorentz, Ext[1]]] . NR1, opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 5 (Local):
ReplaceAll::reps: {Rule[Ext[lbar[Index[Spin, a]] . L$Ga[0] . L$Ga[Index[Lorentz, Ext[1]]] . NR1, opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of `1` is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing. will be suppressed during this calculation.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/198 .

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
_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/EffLRSM/validation/call2/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/EffLRSM/validation/call2/round0/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
el not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/EffLRSM/validation/call2/round0/UFO
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

## UFO Python syntax error — `UFO/couplings.py` line 694: unterminated string literal (detected at line 694)
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
  692 | GC_171 = Coupling(name = 'GC_171',
  693 |                   value = 'ReplaceAll(-0.5*(ee*complex(0,1)*kappaRell*Dot(lbar(-1),Gamma(0),Gamma(1),NR1)*complexconjugate(Ymix1x1)*Gamma(0,r$18608,1))/(sw*cmath.sqrt(2)) - (ee*complex(0,1)*kappaRell*Dot(lbar(-2),Gamma(0),Gamma(1),Gamma5(),NR1)*complexconjugate(Ymix1x1)*Gamma(0,r$18609,1))/(2.*sw*cm
  694 |                   order = {'                       1                                                                                                                                    I                                                                                                                   
  695 |                     (-(-) I) ee kappaRell Conjugate[Ymix1x1] lbar[Index[Spin, Int[1]]] . L$Ga[0] . L$Ga[Index[Lorentz, Ext[1]]] . NR1 L$Ga[0, r$18608, 1]   - ee kappaRell Conjugate[Ymix1x1] lbar[Index[Spin, Int[2]]] . L$Ga[0] . L$Ga[Index[Lorentz, Ext[1]]] . L$Ga[5] . NR1 L$Ga[0, r$18609, 1]   - ee 
  696 |                        2                                                                                                                                    2                                                                                                                                          2    
```

## UFO Python syntax error — `UFO/parameters.py` line 90: positional argument follows keyword argument
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
   88 |                     texname = '\\text{Ymix1x1}',
   89 |                     lhablock = 'EFFLRSM',
   90 | ClassAttributeCreation[lhacode, PYList[{1, 1} /. 8], 20]<>)
   91 | 
   92 | Xmix1x1 = Parameter(name = 'Xmix1x1',
```

## UFO Python syntax error — `UFO/vertices.py` line 580: closing parenthesis ')' does not match opening parenthesis '[' on line 577
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
  578 |               color = [ '1' ],
  579 |               lorentz = [ L.<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1 ],
  580 |               couplings = {(0,-1 + PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1):C.GC_171})
  581 | 
  582 | V_96 = Vertex(name = 'V_96',
```

## UFO direct-import error (the REAL reason MadGraph rejects this UFO — MadGraph's own message misreports the location)
Fix the .fr declaration that produced this; the UFO is regenerated from model.fr each round.
```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    __import__('UFO')
    ~~~~~~~~~~^^^^^^^
  File "/Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/EffLRSM/validation/call2/round0/UFO/__init__.py", line 2, in <module>
    import particles
  File "/Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/EffLRSM/validation/call2/round0/UFO/particles.py", line 8, in <module>
    import parameters as Param
  File "/Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/EffLRSM/validation/call2/round0/UFO/parameters.py", line 90
    ClassAttributeCreation[lhacode, PYList[{1, 1} /. 8], 20]<>)
                                                   ^
SyntaxError: positional argument follows keyword argument

```
