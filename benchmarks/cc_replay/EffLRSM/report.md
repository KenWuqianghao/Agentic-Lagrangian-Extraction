{
 "call": 1,
 "stage": "checks_failed",
 "full_chain_pass": false,
 "compile_ok": true,
 "checks": {
  "hermiticity": "fail",
  "kinetic_diagonal": "pass",
  "mass_diagonal": "pass",
  "mass_spectrum": "pass"
 },
 "madgraph_import_ok": false,
 "lagrangian_expression": "LTotal",
 "error_tags": [
  "hermiticity_fail",
  "mg5_import_fail",
  "ufo_python_syntax_error",
  "mg5_python_traceback",
  "mg5_invalid_cmd"
 ],
 "seconds": 131.0,
 "lock_wait_seconds": 0.0,
 "t_kernel_start": 1790744523.853,
 "t_kernel_end": 1790744655.607,
 "stage_reached": "checks",
 "driver": "diag"
}

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

## Hermiticity: the non-zero vertices of L - HC[L]
Each row is a vertex that does not cancel against its conjugate. The usual cause is a term without its `+ HC[...]` partner, or a complex coefficient on a self-conjugate combination. `block` is the named Lagrangian term in model.fr whose expanded terms carry these fields (or their conjugates).

- vertex 1: fields WRbar; block: not located
  coefficient: `((-1/2*I)*ee*kappaRell*(Conjugate[Ymix[Index[Generation, 1], Index[Generation, 1]]]*(lbar[Index[Spin, a]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . NR1*Ga[0, r$18639, 1] + lbar[Index[Spin, b]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[5] . NR1*Ga[0, r$18640, 1] - lbar[Index[Spin, c]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . NR1*Ga[0, r$22518, Index[Spin, 1]] - lbar[Index[Spin, d]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[5] . NR1*Ga[0, r$22519, Index[Spin, 1]]) + Conjugate[Ymix[Index[Generation, 2],`
- vertex 2: fields WR; block: not located
  coefficient: `((-1/2*I)*ee*kappaRell*(NR1 . Ga[Index[Lorentz, Ext[1]]] . l[Index[Spin, 1]]*Ymix[Index[Generation, 1], Index[Generation, 1]] + NR1 . Ga[Index[Lorentz, Ext[1]]] . Ga[5] . l[Index[Spin, 1]]*Ymix[Index[Generation, 1], Index[Generation, 1]] - NR1 . Ga[Index[Lorentz, Ext[1]]] . l[Index[Spin, a]]*Ga[0, 1, r$18639]*Ga[0, Index[Spin, b], r$22446]*Ymix[Index[Generation, 1], Index[Generation, 1]] - NR1 . Ga[Index[Lorentz, Ext[1]]] . Ga[5] . l[Index[Spin, c]]*Ga[0, 1, r$18640]*Ga[0, Index[Spin, d], r$2244`

## MadGraph import: where the UFO breaks, and the model.fr lines behind it

### `UFO/couplings.py` line 694, object `GC_171`: unterminated string literal (detected at line 694)
```
GC_171 = Coupling(name = 'GC_171',
                  value = 'ReplaceAll(-0.5*(ee*complex(0,1)*kappaRell*Dot(lbar(-1),Gamma(0),Gamma(1),NR1)*complexconjugate(Ymix1x1)*Gamma(0,r$18639,1))/(sw*cmath.sqrt(2)) - (ee*complex(0,1)*kappaRell*Dot(lbar(-2),Gamma(0),Gamma(1),Gamma5(),NR1)*complexconjugate(Ymix1x1)*Gamma(0,r$18640,1))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*kappaRell*Dot(lbar(-1),Gamma(0),Gamma(1),NR2)*complexconjugate(Ymix2x2)*Gamma(0,r$18641,2))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*kappaRell*Dot(lbar(-2),Gamma(0),Gamma(1),Gamma5(),NR2)*complexconjugate(Ymix2x2)*Gamma(0,r$18642,2))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*kappaRell*Dot(lbar(-1),Gamma(0),Gamma(1),NR3)*complexconjugate(Ymix3x3)*Gamma(0,r$18643,3))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*kappaRell*Dot(lbar(-2),Gamma(0),Gamma(1),Gamma5(),NR3)*complexconjugate(Ymix3x3)*Gamma(0,r$18644,3))/(2.*sw*cmath.sqrt(2)),Rule(Ext(Dot(lbar(-1),Gamma(0),Gamma(1),NR1),Pattern(opt,BlankNullSequence())),Ext(List,opt),Ext(Slot(2),Pattern(opt,BlankNullSequence())),Ext(Slot(3),opt),Ext(2,Pattern(opt,BlankNullSequence())),Ext(Slot(3),opt)))',
                  order = {'                       1                                 
```
Vertex particles using this coupling: wr__plus__
model.fr lines:
- line 95 (declaration): `ClassName       -> NR1,`
- line 107 (declaration): `ClassName       -> NR2,`
- line 119 (declaration): `ClassName       -> NR3,`
- line 166 (declaration): `kappaRell == {`
  ```
    kappaRell == {
      ParameterType    -> External,
      BlockName        -> EFFLRSM,
      OrderBlock       -> 4,
      Value            -> 1.,
      InteractionOrder -> {NP, 1},
      TeX              -> Superscript[kappa, R^l],
      Description      -> "Overall normalization of the WR/ZR coupling to leptons, Eq.(2), Eq.(neucurrent)"
    },
  ```
- line 223 (declaration): `Ymix == {`
  ```
    Ymix == {
      ParameterType    -> External,
      BlockName        -> EFFLRSM,
      OrderBlock       -> 8,
      InteractionOrder -> {NP, 1},
      Indices          -> {Index[Generation], Index[Generation]},
      Value            -> {Ymix[1,1] -> 1, Ymix[1,2] -> 0, Ymix[1,3] -> 0,
                            Ymix[2,1] -> 0, Ymix[2,2] -> 1, Ymix[2,3] -> 0,
                            Ymix[3,1] -> 0, Ymix[3,2] -> 0, Ymix[3,3] -> 1},
      TeX              -> Superscript[Y, N],
      Description      -> "Y_{l m'}: mixing of the heavy neutrino mass eigenstate N_{m'} with the RH state of lepton flavor l, Eq.(lrsmNuMixing); Ymix[N-index, l-index]"
    },
  ```
- line 302 (use): `LNmass := -1/2 MN1 NR1bar.NR1 - 1/2 MN2 NR2bar.NR2 - 1/2 MN3 NR3bar.NR3;`

### `UFO/parameters.py` line 90, object `Ymix1x1`: positional argument follows keyword argument
```
Ymix1x1 = Parameter(name = 'Ymix1x1',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{Ymix1x1}',
                    lhablock = 'EFFLRSM',
ClassAttributeCreation[lhacode, PYList[{1, 1} /. 8], 20]<>)

```
model.fr lines:
- line 223 (declaration): `Ymix == {`
  ```
    Ymix == {
      ParameterType    -> External,
      BlockName        -> EFFLRSM,
      OrderBlock       -> 8,
      InteractionOrder -> {NP, 1},
      Indices          -> {Index[Generation], Index[Generation]},
      Value            -> {Ymix[1,1] -> 1, Ymix[1,2] -> 0, Ymix[1,3] -> 0,
                            Ymix[2,1] -> 0, Ymix[2,2] -> 1, Ymix[2,3] -> 0,
                            Ymix[3,1] -> 0, Ymix[3,2] -> 0, Ymix[3,3] -> 1},
      TeX              -> Superscript[Y, N],
      Description      -> "Y_{l m'}: mixing of the heavy neutrino mass eigenstate N_{m'} with the RH state of lepton flavor l, Eq.(lrsmNuMixing); Ymix[N-index, l-index]"
    },
  ```
- line 229 (use): `Value            -> {Ymix[1,1] -> 1, Ymix[1,2] -> 0, Ymix[1,3] -> 0,`
- line 230 (use): `Ymix[2,1] -> 0, Ymix[2,2] -> 1, Ymix[2,3] -> 0,`
- line 231 (use): `Ymix[3,1] -> 0, Ymix[3,2] -> 0, Ymix[3,3] -> 1},`
- line 233 (use): `Description      -> "Y_{l m'}: mixing of the heavy neutrino mass eigenstate N_{m'} with the RH state of lepton flavor l, Eq.(lrsmNuMixing); Ymix[N-index, l-index]"`
- line 319 (use): `the current is therefore omitted.  Ymix is kept as a parameter`

### `UFO/vertices.py` line 580, object `V_95`: closing parenthesis ')' does not match opening parenthesis '[' on line 577
```
V_95 = Vertex(name = 'V_95',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[3]], P.wr__plus__, P.<>CreateObjectParticleName[PartNameMG[3]] ],
              color = [ '1' ],
              lorentz = [ L.<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1 ],
              couplings = {(0,-1 + PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1):C.GC_171})

```
model.fr lines: none matched the symbols (no model symbol in this object)

## compile log, distinct lines (tail)
```
8 vertices obtained.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 198
   - Saved vertices in InterfaceRun[ 1 ].
Quantum number Q not conserved in vertex {WRbar}.
Quantum number Q not conserved in vertex {WR}.
Preparing Python output.
Part::pkspec1: The expression lbar[Index[Spin, a]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . NR1 cannot be used as a part specification.
Inner::incom: Length 0 of dimension 1 in {} is incommensurate with length 1 of dimension 1 in {lbar[Index[Spin, a]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . NR1}.
Inner::normal: Nonatomic expression expected at position 3 in Inner[PRIVATE`TurnFermionicIndexDeltas, lbar[Index[Spin, a]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . NR1, List].
Join::heads: Heads Inner and List at positions 1 and 2 are expected to be the same.
Function::slotn: Slot number 2 in Ext[#2, opt___] -> Ext[#3, opt] &  cannot be filled from (Ext[#2, opt___] -> Ext[#3, opt] & )[1].
Function::slotn: Slot number 3 in Ext[#2, opt___] -> Ext[#3, opt] &  cannot be filled from (Ext[#2, opt___] -> Ext[#3, opt] & )[1].
Function::slotn: Slot number 3 in Ext[#2, opt___] -> Ext[#3, opt] &  cannot be filled from (Ext[#2, opt___] -> Ext[#3, opt] & )[{WRbar, 1}, 2].
Rule::argrx: Rule called with 6 arguments; 2 arguments are expected.
MapAt::partw: Part {1} of PRIVATE`TurnFermionicIndexDeltas does not exist.
MapAt::partw: Part {1} of List does not exist.
MapAt::partw: Part {1} of 1 does not exist.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
ReplaceAll::reps: {Rule[Ext[lbar[Index[Spin, a]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . NR1, opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
ReplaceAll::reps: {Rule[Ext[lbar[Index[Spin, a]] . L$Ga[0] . L$Ga[Index[Lorentz, Ext[1]]] . NR1, opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/198 .
StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1.
StringJoin::string: String expected at position 2 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1.
StringJoin::string: String expected at position 3 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1.
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
[1;31mCommand "import /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/EffLRSM/validation/call1/round0/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/EffLRSM/validation/call1/round0/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
el not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /Users/kenwu/Documents/Github/Agentic-Lagrangian-Extraction/benchmarks/cc_replay/EffLRSM/validation/call1/round0/UFO
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
  
