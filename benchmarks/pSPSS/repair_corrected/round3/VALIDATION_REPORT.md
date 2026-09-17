# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- FeynRules check `hermiticity`: fail
- FeynRules check `kinetic_diagonal`: fail
- FeynRules check `mass_diagonal`: fail
- FeynRules check `mass_spectrum`: inconclusive
- MadGraph import: False
- Heuristic error tags: hermiticity_fail, kinetic_diagonal_fail, mass_diagonal_fail, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd

## FeynRules check `hermiticity`: fail
The Lagrangian is not Hermitian: FeynRules found residual terms in L - HC[L]. Almost always a term is missing its conjugate -- add `+ HC[...]` around the offending interaction, or write the conjugate out explicitly. (Checking for hermiticity by calculating the Feynman rules contained in L-HC[L]. If the lagrangian is hermitian, then the number of vertices should be zero. Starting Feynman rule calculation. Expanding the Lagrangian... Expanding the indices over 8 cores Collecting the different structures that enter the vertex. 90 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$F)

## FeynRules check `kinetic_diagonal`: fail
Kinetic terms are not diagonal: two fields mix at quadratic order, so the fields in the Lagrangian are not mass eigenstates. Rotate them to the mass basis, or declare the mixing so FeynRules can do it. (Neglecting all terms with more than 2 particles. Non diagonal kinetic term found: I Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 4]]] n4bar[Index[Spin, r$18048]] . del[vm[Index[Spin1]], Index[Lorentz, mu]] Ga[0, r$18048, Index[Spin2]] Ga[Index[Lorentz, mu], Index[Spin, i$35538], Index[Spin, j$35538]] Un[Index[Neutrino, 4], Index[Neutrino, 2]] + I Conjugate[Un[Index[Neutrino, 5], Index[Neutrino)

## FeynRules check `mass_diagonal`: fail
Mass terms are not diagonal: the mass matrix mixes fields, so the declared particles are not mass eigenstates. Diagonalise the mass matrix, or declare the mixing. (Warning: not numerical value encountered. Unable to decide whether mass term is diagonal Non diagonal mass term found: -(Mmaj Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 5]]] Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]] n4bar[Index[Spin, r$18055]] . n5[Index[Spin, sp1]] . Ga[0] Ga[0, r$18055, sp1]) - Mmaj Conjugate[Ga[0, r$18048, sp1]] n4bar[Index[Spin, r$18048]] . n5[Index[Spin, sp1)

## FeynRules check `mass_spectrum`: inconclusive
The mass spectrum could not be computed. This usually means the mass terms are not diagonal -- see that result. (Neglecting all terms with more than 2 particles. Warning: not numerical value encountered. Unable to decide whether mass term is diagonal Non diagonal mass term found: -(Mmaj Conjugate[Un[Index[Neutrino, 4], Index[Neutrino, 5]]] Conjugate[Un[Index[Neutrino, 5], Index[Neutrino, 4]]] n4bar[Index[Spin, r$18055]] . n5[Index[Spin, sp1]] . Ga[0] Ga[0, r$18055, sp1]) - Mmaj Conjugate[Ga[0, r$18048, sp1]])

## FeynRules / Wolfram Engine output (tail)
```
[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]}}.
From kernel 3 (Local):
Take::take: Cannot take positions 2 through 2 in {{1, -I Un4x1 Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[2]]] L$Ga[0, r$18050, sp1] L$IndexDelta[Index[Spin, Ext[Index[Spin, b]]], Index[Spin, Ext[Index[Spin, a]]]] L$IndexDelta[Index[Spin, Ext[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]]], Index[Spin, Ext[PRIVATE`TurnFermionicIndexDeltas[[2]]]]] yvn[Index[Generation, Ext[2]]] /. Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]}}.
From kernel 4 (Local):
Take::take: Cannot take positions 2 through 2 in {{1, -I Un4x1 Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[2]]] L$Ga[0, r$18050, sp1] L$IndexDelta[Index[Spin, Ext[Index[Spin, b]]], Index[Spin, Ext[Index[Spin, a]]]] L$IndexDelta[Index[Spin, Ext[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]]], Index[Spin, Ext[PRIVATE`TurnFermionicIndexDeltas[[2]]]]] yvn[Index[Generation, Ext[2]]] /. Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]}}.
From kernel 5 (Local):
Take::take: Cannot take positions 2 through 2 in {{1, -I Un4x1 Eps[Index[SU2D, Ext[3]], Index[SU2D, Ext[2]]] L$Ga[0, r$18050, sp1] L$IndexDelta[Index[Spin, Ext[Index[Spin, b]]], Index[Spin, Ext[Index[Spin, a]]]] L$IndexDelta[Index[Spin, Ext[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]]], Index[Spin, Ext[PRIVATE`TurnFermionicIndexDeltas[[2]]]]] yvn[Index[Generation, Ext[2]]] /. Rule[Ext[PRIVATE`dummylist[{{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[1], a]]], {{CC[vebar], 1}, {LL, 2}, {Phibar, 3}}[[PRIVATE`hold[Ext[2], b]]]], opt___], Ext[P$IndexDelta[Index[Spin, Ext[1]], Index[Spin, a]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]}}.

General::stop: Further output of Take::take will be suppressed during this calculation.
From kernel 5 (Local):
Select::normal: Nonatomic expression expected at position 1 in Select[Multpad, MatchColor[#1] & ].
From kernel 5 (Local):
Select::normal: Nonatomic expression expected at position 1 in Select[Multpad, MatchColor[#1] & ].
From kernel 5 (Local):
Complement::normal: Nonatomic expression expected at position 1 in Complement[Multpad, Select[Multpad, MatchColor[#1] & ]].
From kernel 5 (Local):
Select::normal: Nonatomic expression expected at position 1 in Select[Multpad, MatchColor[#1] & ].
From kernel 5 (Local):
Complement::normal: Nonatomic expression expected at position 1 in Complement[Multpad, Select[Multpad, MatchColor[#1] & ]].
From kernel 5 (Local):
Complement::normal: Nonatomic expression expected at position 1 in Complement[Multpad, Select[Multpad, MatchColor[#1] & ]].

Select::normal: Nonatomic expression expected at position 1 in Select[1, MatchColor[#1] & ].

Select::normal: Nonatomic expression expected at position 1 in Select[1, MatchColor[#1] & ].

Complement::normal: Nonatomic expression expected at position 1 in Complement[1, Select[1, MatchColor[#1] & ]].

Select::normal: Nonatomic expression expected at position 1 in Select[1, MatchColor[#1] & ].

General::stop: Further output of Select::normal will be suppressed during this calculation.

Complement::normal: Nonatomic expression expected at position 1 in Complement[1, Select[1, MatchColor[#1] & ]].

Complement::normal: Nonatomic expression expected at position 1 in Complement[1, Select[1, MatchColor[#1] & ]].

General::stop: Further output of Complement::normal will be suppressed during this calculation.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/169 .

StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 2 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 3 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>1.

General::stop: Further output of StringJoin::string will be suppressed during this calculation.
    - Writing files.
Done!
[INFO] UFO complete: particles.py, vertices.py, couplings.py, parameters.py, coupling_orders.py all present.
[INFO] Done.

```

## MadGraph import output (tail)
```
models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /private/tmp/repair_corrected/pSPSS/round2/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_corrected/pSPSS/round2/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
raph_interface.py", line 5837, in do_import
    raise self.InvalidCmd('UFO model not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /tmp/repair_corrected/pSPSS/round2/UFO
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

## UFO Python syntax error — `UFO/vertices.py` line 628: closing parenthesis ')' does not match opening parenthesis '[' on line 625
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
  626 |                color = [ 'Select(1,Function(MatchColor(Slot(1))))' ],
  627 |                lorentz = [ L.<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>S<>PRIVATE`ConvertSpinToString[0]<>3 ],
  628 |                couplings = {(0,0):C.GC_131})
  629 | 
  630 | V_104 = Vertex(name = 'V_104',
```

## UFO direct-import error (the REAL reason MadGraph rejects this UFO — MadGraph's own message misreports the location)
Fix the .fr declaration that produced this; the UFO is regenerated from model.fr each round.
```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    __import__('UFO')
    ~~~~~~~~~~^^^^^^^
  File "/tmp/repair_corrected/pSPSS/round2/UFO/__init__.py", line 6, in <module>
    import vertices
  File "/tmp/repair_corrected/pSPSS/round2/UFO/vertices.py", line 628
    couplings = {(0,0):C.GC_131})
                                ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '[' on line 625

```
