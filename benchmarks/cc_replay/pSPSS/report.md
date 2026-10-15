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
 "seconds": 251.6,
 "lock_wait_seconds": 84.1,
 "t_kernel_start": 1790744834.17,
 "t_kernel_end": 1790745086.47,
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
The Lagrangian is not Hermitian: FeynRules found residual terms in L - HC[L]. Almost always a term is missing its conjugate -- add `+ HC[...]` around the offending interaction, or write the conjugate out explicitly. (Checking for hermiticity by calculating the Feynman rules contained in L-HC[L]. If the lagrangian is hermitian, then the number of vertices should be zero. Starting Feynman rule calculation. Expanding the Lagrangian... Expanding the indices over 8 cores Collecting the different structures that enter the vertex. 28 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$F)

## Hermiticity: the non-zero vertices of L - HC[L]
Each row is a vertex that does not cancel against its conjugate. The usual cause is a term without its `+ HC[...]` partner, or a complex coefficient on a self-conjugate combination. `block` is the named Lagrangian term in model.fr whose expanded terms carry these fields (or their conjugates).

- vertex 1: fields W n4 ta n5 e mu; block: not located
  UNREDUCED: FeynRules could not strip n4, ta, n5, e, mu from this vertex; its coefficient still holds a spinor chain (Ga[0] from the conjugate). The usual cause is an explicit spin or flavour index on the spinors of that chain (see lint rule explicit_spin_in_chain); write the chain with implicit indices (`Xbar.Ga[mu].ProjP.Y`).
  coefficient: `(I*ee*(Conjugate[UnCL[Index[Generation, 3], Index[Neutrino, 4]]]*n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . ta[Index[Spin, SP$1]] + Conjugate[UnCL[Index[Generation, 1], Index[Neutrino, 5]]]*n5[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . e[Index[Spin, SP$1]] + Conjugate[UnCL[Index[Generation, 2], Index[Neutrino, 5]]]*n5[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . mu[Index[Spin, SP$1]] + Conjugate[UnCL[Index[Generation, 3], Index[Neutrino, 5]]]*n5[Inde`
- vertex 2: fields Wbar ebar n4 n5 mubar tabar; block: not located
  UNREDUCED: FeynRules could not strip ebar, n4, n5, mubar, tabar from this vertex; its coefficient still holds a spinor chain (Ga[0] from the conjugate). The usual cause is an explicit spin or flavour index on the spinors of that chain (see lint rule explicit_spin_in_chain); write the chain with implicit indices (`Xbar.Ga[mu].ProjP.Y`).
  coefficient: `(I*ee*(ebar[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . n4[Index[Spin, SP$1]]*UnCL[Index[Generation, 1], Index[Neutrino, 4]] - ebar[Index[Spin, SP$1]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . ProjP . n4[Index[Spin, SP$1]]*UnCL[Index[Generation, 1], Index[Neutrino, 4]] + ebar[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . n5[Index[Spin, SP$1]]*UnCL[Index[Generation, 1], Index[Neutrino, 5]] - ebar[Index[Spin, SP$1]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . Proj`
- vertex 3: fields Z n4 n5 ve vm vt vebar vmbar vtbar; block: not located
  UNREDUCED: FeynRules could not strip n4, n5, ve, vm, vt, vebar, vmbar, vtbar from this vertex; its coefficient still holds a spinor chain (Ga[0] from the conjugate). The usual cause is an explicit spin or flavour index on the spinors of that chain (see lint rule explicit_spin_in_chain); write the chain with implicit indices (`Xbar.Ga[mu].ProjP.Y`).
  coefficient: `((I/4)*ee*(thetasq*n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . n4[Index[Spin, SP$1]] + I*thetasq*n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . n5[Index[Spin, SP$1]] + 2*Conjugate[UnCL[Index[Generation, 1], Index[Neutrino, 4]]]*n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . ve[Index[Spin, SP$1]] + 2*Conjugate[UnCL[Index[Generation, 2], Index[Neutrino, 4]]]*n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . vm[Index[Spin, SP$1]] + 2*Conjugate`

## MadGraph import: where the UFO breaks, and the model.fr lines behind it

### `UFO/couplings.py` line 642, object `GC_158`: unterminated string literal (detected at line 642)
```
GC_158 = Coupling(name = 'GC_158',
                  value = 'ReplaceAll((ee*complex(0,1)*UnCL1x4*Dot(n4(-1),Gamma(1),ProjM,e(-1)))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UnCL2x4*Dot(n4(-1),Gamma(1),ProjM,mu(-1)))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UnCL3x4*Dot(n4(-1),Gamma(1),ProjM,ta(-1)))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UnCL1x5*Dot(n5(-1),Gamma(1),ProjM,e(-1)))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UnCL2x5*Dot(n5(-1),Gamma(1),ProjM,mu(-1)))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UnCL3x5*Dot(n5(-1),Gamma(1),ProjM,ta(-1)))/(sw*cmath.sqrt(2)),Rule(Ext(Dot(n4(-1),Gamma(1),ProjM,e(-1)),Pattern(opt,BlankNullSequence())),Ext(List,opt),Ext(Slot(2),Pattern(opt,BlankNullSequence())),Ext(Slot(3),opt),Ext(2,Pattern(opt,BlankNullSequence())),Ext(Slot(3),opt)))',
                  order = {'                    I ee UnCL1x4 n4[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . e[Index[Spin, Int[1]]]   I ee UnCL2x4 n4[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . mu[Index[Spin, Int[1]]]   I ee UnCL3x4 n4[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . ta[Index[Spin, Int[1]]]   I ee UnCL1x5 n5[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]
```
Vertex particles using this coupling: W__minus__
model.fr lines:
- line 148 (declaration): `UnCL == {`
  ```
    UnCL == {
      ParameterType    -> Internal,
      BlockName        -> PSPSS,
      Indices          -> {Index[Generation], Index[Neutrino]},
      InteractionOrder -> {NP, 1},
      Value            -> {
        UnCL[1, 1] -> 1 - thetasq/2,  UnCL[1, 2] -> -theta1 theta2/2,  UnCL[1, 3] -> -theta1 theta3/2,  UnCL[1, 4] -> -I theta1/Sqrt[2],  UnCL[1, 5] -> theta1/Sqrt[2],
        UnCL[2, 1] -> -theta2 theta1/2,  UnCL[2, 2] -> 1 - thetasq/2,  UnCL[2, 3] -> -theta2 theta3/2,  UnCL[2, 4] -> -I theta2/Sqrt[2],  UnCL[2, 5] -> theta2/Sqrt[2],
        UnCL[3, 1] -> -theta3 theta1/2,  UnCL[3, 2] -> -theta3 theta2/2,  UnCL[3, 3] -> 1 - thetasq/2,  UnCL[3, 4] -> -I theta3/Sqrt[2],  UnCL[3, 5] -> theta3/Sqrt[2]
      },
      Description      -> "upper 3x5 block U'_CL of U_n (active-sterile mixing matrix, paper eq.(29)), used for the index contraction of the mixed W and Z couplings"
    }
  ```
- line 168 (declaration): `ClassName       -> n4,`
- line 180 (declaration): `ClassName       -> n5,`
- line 288 (use): `(UnCL[ff1, 4] lbar[sp, ff1].Ga[mu].ProjM.n4[sp] + UnCL[ff1, 5] lbar[sp, ff1].Ga[mu].ProjM.n5[sp]) Wbar[mu]`
- line 289 (use): `+ (Conjugate[UnCL[ff1, 4]] n4bar[sp].Ga[mu].ProjM.l[sp, ff1] + Conjugate[UnCL[ff1, 5]] n5bar[sp].Ga[mu].ProjM.l[sp, ff1]) W[mu]`
- line 299 (use): `+ I thetasq/2 n4bar[sp].Ga[mu].ProjM.n5[sp]`

### `UFO/vertices.py` line 616, object `V_101`: closing parenthesis ')' does not match opening parenthesis '[' on line 613
```
V_101 = Vertex(name = 'V_101',
               particles = [ P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[3]], P.W__minus__, P.<>CreateObjectParticleName[PartNameMG[3]] ],
               color = [ '1' ],
               lorentz = [ L.<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1 ],
               couplings = {(0,-1 + PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1):C.GC_158})

```
model.fr lines:
- line 158 (use): `Description      -> "upper 3x5 block U'_CL of U_n (active-sterile mixing matrix, paper eq.(29)), used for the index contraction of the mixed W and Z couplings"`
- line 288 (use): `(UnCL[ff1, 4] lbar[sp, ff1].Ga[mu].ProjM.n4[sp] + UnCL[ff1, 5] lbar[sp, ff1].Ga[mu].ProjM.n5[sp]) Wbar[mu]`
- line 289 (use): `+ (Conjugate[UnCL[ff1, 4]] n4bar[sp].Ga[mu].ProjM.l[sp, ff1] + Conjugate[UnCL[ff1, 5]] n5bar[sp].Ga[mu].ProjM.l[sp, ff1]) W[mu]`

## compile log, distinct lines (tail)
```
x[Spin, SP$1]] cannot be used as a part specification.
Inner::incom: Length 0 of dimension 1 in {} is incommensurate with length 1 of dimension 1 in {ebar[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . n4[Index[Spin, SP$1]]}.
Inner::normal: Nonatomic expression expected at position 3 in Inner[PRIVATE`TurnFermionicIndexDeltas, ebar[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . n4[Index[Spin, SP$1]], List].
ReplaceAll::reps: {Rule[Ext[ebar[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . n4[Index[Spin, SP$1]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
Part::pkspec1: The expression n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . n4[Index[Spin, SP$1]] cannot be used as a part specification.
Inner::incom: Length 0 of dimension 1 in {} is incommensurate with length 1 of dimension 1 in {n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . n4[Index[Spin, SP$1]]}.
Inner::normal: Nonatomic expression expected at position 3 in Inner[PRIVATE`TurnFermionicIndexDeltas, n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . n4[Index[Spin, SP$1]], List].
ReplaceAll::reps: {Rule[Ext[n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . n4[Index[Spin, SP$1]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
MapAt::partw: Part {1} of PRIVATE`TurnFermionicIndexDeltas does not exist.
MapAt::partw: Part {1} of List does not exist.
MapAt::partw: Part {1} of 1 does not exist.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
ReplaceAll::reps: {Rule[Ext[n4[Index[Spin, SP$1]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . e[Index[Spin, SP$1]], opt___], Ext[List, opt], Ext[#2, opt___], Ext[#3, opt], Ext[2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/202 .
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
  
