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
 "seconds": 81.7,
 "lock_wait_seconds": 0.0,
 "t_kernel_start": 1790744362.01,
 "t_kernel_end": 1790744444.459,
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

### `UFO/couplings.py` line 630, object `GC_155`: unterminated string literal (detected at line 630)
```
GC_155 = Coupling(name = 'GC_155',
                  value = 'ReplaceAll(-0.5*(ee*complex(0,1)*VlN1*Dot(vebar(-1),Gamma(0),Gamma(1),Gamma(0),NR(-2))*ProjM(-1,-2))/(cw*sw) - (ee*complex(0,1)*VlN2*Dot(vmbar(-1),Gamma(0),Gamma(1),Gamma(0),NR(-2))*ProjM(-1,-2))/(2.*cw*sw) - (ee*complex(0,1)*VlN3*Dot(vtbar(-1),Gamma(0),Gamma(1),Gamma(0),NR(-2))*ProjM(-1,-2))/(2.*cw*sw) - (ee*complex(0,1)*Dot(NRbar(-1),Gamma(1),ve(-2))*complexconjugate(VlN1)*ProjP(-1,-2))/(2.*cw*sw) - (ee*complex(0,1)*Dot(NRbar(-1),Gamma(1),vm(-2))*complexconjugate(VlN2)*ProjP(-1,-2))/(2.*cw*sw) - (ee*complex(0,1)*Dot(NRbar(-1),Gamma(1),vt(-2))*complexconjugate(VlN3)*ProjP(-1,-2))/(2.*cw*sw),Rule(Ext(PRIVATExdummylist(Part(List(List(Z,1)),Dot(vebar(-1),Gamma(0),Gamma(1),Gamma(0),NR(-2))),Part(List(List(Z,1)),PRIVATExhold(SP$1,SP$2))),Pattern(opt,BlankNullSequence())),Ext(Dot(vebar(-1),Gamma(0),Gamma(1),Gamma(0),NR(-2)),opt),Ext(Slot(2),Pattern(opt,BlankNullSequence())),Ext(Slot(3),opt),Ext(2,Pattern(opt,BlankNullSequence())),Ext(Slot(3),opt)))',
                  order = {'                       1                                                                                                                              
```
Vertex particles using this coupling: Z, ve
model.fr lines:
- line 25 (declaration): `ClassName        -> NR,`
- line 54 (declaration): `VlN == {`
  ```
    VlN == {
      ParameterType    -> External,
      Indices          -> {Index[Generation]},
      Value            -> {VlN[1] -> 10.*^-3, VlN[2] -> 0., VlN[3] -> 0.},
      BlockName        -> HNEUTRINO,
      OrderBlock       -> 1,
      InteractionOrder -> {NP, 1},
      TeX              -> Subscript[V, lN],
      Description      -> "Active-heavy neutrino mixing V_lN, Eq. (7) of arXiv:1602.06957"
    }
  ```
- line 73 (use): `-(gw/(2 cw)) Z[mu] Conjugate[VlN[ff]] NLbar[sp].Ga[mu].vl[sp, ff]`
- line 81 (use): `-(mN/vev) Conjugate[VlN[ff]] (H + I G0) NRrbar[sp].vl[sp, ff]`
- line 42 (use): `Definitions    -> { NL[sp1_] :> Module[{sp2}, ProjM[sp1, sp2] NR[sp2]] }`
- line 48 (use): `Definitions    -> { NRr[sp1_] :> Module[{sp2}, ProjP[sp1, sp2] NR[sp2]] }`

### `UFO/parameters.py` line 34, object `VlN1`: positional argument follows keyword argument
```
VlN1 = Parameter(name = 'VlN1',
                 nature = 'external',
                 type = 'complex',
                 value = 0.01,
                 texname = '\\text{VlN1}',
                 lhablock = 'HNEUTRINO',
ClassAttributeCreation[lhacode, PYList[{1} /. 1], 17]<>)

```
model.fr lines:
- line 54 (declaration): `VlN == {`
  ```
    VlN == {
      ParameterType    -> External,
      Indices          -> {Index[Generation]},
      Value            -> {VlN[1] -> 10.*^-3, VlN[2] -> 0., VlN[3] -> 0.},
      BlockName        -> HNEUTRINO,
      OrderBlock       -> 1,
      InteractionOrder -> {NP, 1},
      TeX              -> Subscript[V, lN],
      Description      -> "Active-heavy neutrino mixing V_lN, Eq. (7) of arXiv:1602.06957"
    }
  ```
- line 57 (use): `Value            -> {VlN[1] -> 10.*^-3, VlN[2] -> 0., VlN[3] -> 0.},`
- line 73 (use): `-(gw/(2 cw)) Z[mu] Conjugate[VlN[ff]] NLbar[sp].Ga[mu].vl[sp, ff]`
- line 81 (use): `-(mN/vev) Conjugate[VlN[ff]] (H + I G0) NRrbar[sp].vl[sp, ff]`

### `UFO/vertices.py` line 688, object `V_113`: closing parenthesis ')' does not match opening parenthesis '[' on line 685
```
V_113 = Vertex(name = 'V_113',
               particles = [ P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[ve[Index[Spin, SP$1]]]], P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[3]], P.Z, P.<>CreateObjectParticleName[PartNameMG[3]] ],
               color = [ '1' ],
               lorentz = [ L.<>PRIVATE`ConvertSpinToString[0]<>F<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1 ],
               couplings = {(0,-1 + PRIVATE`ConvertSpinToString[0]<>F<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1):C.GC_155})

```
model.fr lines:
- line 73 (use): `-(gw/(2 cw)) Z[mu] Conjugate[VlN[ff]] NLbar[sp].Ga[mu].vl[sp, ff]`
- line 24 (use): `F[110] == {`
- line 38 (use): `F[111] == {`
- line 44 (use): `F[112] == {`
- line 61 (use): `TeX              -> Subscript[V, lN],`
- line 81 (use): `-(mN/vev) Conjugate[VlN[ff]] (H + I G0) NRrbar[sp].vl[sp, ff]`

## compile log, distinct lines (tail)
```
1}}[[PRIVATE`hold[SP$1, SP$2]]]]} is incommensurate with length 2 of dimension 1 in {vebar[Index[Spin, SP$1]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . NR[Index[Spin, SP$2]], ProjM[Index[Spin, SP$1], Index[Spin, SP$2]]}.
Inner::heads: Heads Dot and PRIVATE`dummylist at positions 3 and 2 are expected to be the same.
Join::heads: Heads Inner and List at positions 1 and 2 are expected to be the same.
Function::slotn: Slot number 2 in Ext[#2, opt___] -> Ext[#3, opt] &  cannot be filled from (Ext[#2, opt___] -> Ext[#3, opt] & )[1].
Function::slotn: Slot number 3 in Ext[#2, opt___] -> Ext[#3, opt] &  cannot be filled from (Ext[#2, opt___] -> Ext[#3, opt] & )[1].
Function::slotn: Slot number 3 in Ext[#2, opt___] -> Ext[#3, opt] &  cannot be filled from (Ext[#2, opt___] -> Ext[#3, opt] & )[{Z, 1}, 2].
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
MapAt::partw: Part {1} of PRIVATE`TurnFermionicIndexDeltas does not exist.
MapAt::partw: Part {1} of 1 does not exist.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
ReplaceAll::reps: {Rule[Ext[PRIVATE`dummylist[{{Z, 1}}[[vebar[Index[Spin, SP$1]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . NR[Index[Spin, SP$2]]]], {{Z, 1}}[[PRIVATE`hold[SP$1, SP$2]]]], opt___], Ext[vebar[Index[Spin, SP$1]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . NR[Index[Spin, SP$2]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
Part::pkspec1: The expression vebar[Index[Spin, SP$1]] . L$Ga[0] . L$Ga[Index[Lorentz, Ext[1]]] . L$Ga[0] . NR[Index[Spin, SP$2]] cannot be used as a part specification.
ReplaceAll::reps: {Rule[Ext[PRIVATE`dummylist[{{Z, 1}}[[vebar[Index[Spin, SP$1]] . L$Ga[0] . L$Ga[Index[Lorentz, Ext[1]]] . L$Ga[0] . NR[Index[Spin, SP$2]]]], {{Z, 1}}[[PRIVATE`hold[SP$1, SP$2]]]], opt___], Ext[vebar[Index[Spin, SP$1]] . L$Ga[0] . L$Ga[Index[Lorentz, Ext[1]]] . L$Ga[0] . NR[Index[Spin, SP$2]], opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/176 .
StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>F<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1.
StringJoin::string: String expected at position 3 in PRIVATE`ConvertSpinToString[0]<>F<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1.
StringJoin::string: String expected at position 4 in PRIVATE`ConvertSpinToString[0]<>F<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1.
    - Writing files.
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
[1;31mCommand "import /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/HeavyN/validation/call1/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/HeavyN/validation/call1/round0/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
del not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/HeavyN/validation/call1/round0/UFO
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
  
