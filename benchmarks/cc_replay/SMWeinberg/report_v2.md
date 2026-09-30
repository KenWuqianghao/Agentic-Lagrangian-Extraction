{
 "call": 2,
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
 "seconds": 79.7,
 "lock_wait_seconds": 0.0,
 "t_kernel_start": 1790745265.56,
 "t_kernel_end": 1790745345.86,
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
The Lagrangian is not Hermitian: FeynRules found residual terms in L - HC[L]. Almost always a term is missing its conjugate -- add `+ HC[...]` around the offending interaction, or write the conjugate out explicitly. (Checking for hermiticity by calculating the Feynman rules contained in L-HC[L]. If the lagrangian is hermitian, then the number of vertices should be zero. Starting Feynman rule calculation. Expanding the Lagrangian... Expanding the indices over 8 cores Collecting the different structures that enter the vertex. 60 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$F)

## Hermiticity: the non-zero vertices of L - HC[L]
Each row is a vertex that does not cancel against its conjugate. The usual cause is a term without its `+ HC[...]` partner, or a complex coefficient on a self-conjugate combination. `block` is the named Lagrangian term in model.fr whose expanded terms carry these fields (or their conjugates).

- vertex 1: fields Nnubar e G0 GP; block: LG0GP
  coefficient: `((I/4)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(Sqrt[2]*MW^2*sw^2)`
- vertex 2: fields Nnubar e GP H; block: LNGP
  coefficient: `(ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(4*Sqrt[2]*MW^2*sw^2)`
- vertex 3: fields Nnubar e GP; block: LNGP
  coefficient: `(ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(2*Sqrt[2]*MW*sw)`
- vertex 4: fields Nnubar mu G0 GP; block: LG0GP
  coefficient: `((I/4)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(Sqrt[2]*MW^2*sw^2)`
- vertex 5: fields Nnubar mu GP H; block: LNGP
  coefficient: `(ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(4*Sqrt[2]*MW^2*sw^2)`
- vertex 6: fields Nnubar mu GP; block: LNGP
  coefficient: `(ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(2*Sqrt[2]*MW*sw)`
- vertex 7: fields Nnubar ta G0 GP; block: LG0GP
  coefficient: `((I/4)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(Sqrt[2]*MW^2*sw^2)`
- vertex 8: fields Nnubar ta GP H; block: LNGP
  coefficient: `(ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(4*Sqrt[2]*MW^2*sw^2)`
- vertex 9: fields Nnubar ta GP; block: LNGP
  coefficient: `(ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(2*Sqrt[2]*MW*sw)`
- vertex 10: fields Nnubar ve G0; block: LNG0
  coefficient: `((I/4)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW^2*sw^2)`
- vertex 11: fields Nnubar ve G0 H; block: LNG0
  coefficient: `(ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(4*MW^2*sw^2)`
- vertex 12: fields Nnubar ve H; block: LNh
  coefficient: `((-1/4*I)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW^2*sw^2)`
- vertex 13: fields Nnubar ve G0; block: LNG0
  coefficient: `(ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(2*MW*sw)`
- vertex 14: fields Nnubar ve H; block: LNh
  coefficient: `((-1/2*I)*ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW*sw)`
- vertex 15: fields Nnubar vm G0; block: LNG0
  coefficient: `((I/4)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW^2*sw^2)`
- vertex 16: fields Nnubar vm G0 H; block: LNG0
  coefficient: `(ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(4*MW^2*sw^2)`
- vertex 17: fields Nnubar vm H; block: LNh
  coefficient: `((-1/4*I)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW^2*sw^2)`
- vertex 18: fields Nnubar vm G0; block: LNG0
  coefficient: `(ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(2*MW*sw)`
- vertex 19: fields Nnubar vm H; block: LNh
  coefficient: `((-1/2*I)*ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW*sw)`
- vertex 20: fields Nnubar vt G0; block: LNG0
  coefficient: `((I/4)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW^2*sw^2)`
- vertex 21: fields Nnubar vt G0 H; block: LNG0
  coefficient: `(ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(4*MW^2*sw^2)`
- vertex 22: fields Nnubar vt H; block: LNh
  coefficient: `((-1/4*I)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW^2*sw^2)`
- vertex 23: fields Nnubar vt G0; block: LNG0
  coefficient: `(ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(2*MW*sw)`
- vertex 24: fields Nnubar vt H; block: LNh
  coefficient: `((-1/2*I)*ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW*sw)`
- vertex 25: fields ebar Nnu G0 GPbar; block: LG0GP
  coefficient: `((-1/4*I)*ee^2*MNu*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(Sqrt[2]*MW^2*sw^2)`
- ... 35 more vertices

## MadGraph import: where the UFO breaks, and the model.fr lines behind it

### `UFO/parameters.py` line 42, object `Cll1x1`: positional argument follows keyword argument
```
Cll1x1 = Parameter(name = 'Cll1x1',
                   nature = 'external',
                   type = 'complex',
                   value = 0.,
                   texname = '\\text{Cll1x1}',
                   lhablock = 'NUPHYSICS',
ClassAttributeCreation[lhacode, PYList[{1, 1} /. 2], 19]<>)

```
model.fr lines:
- line 56 (declaration): `Cll == {`
  ```
    Cll == {
      ParameterType    -> External,
      BlockName        -> NUPHYSICS,
      OrderBlock       -> 2,
      Indices          -> {Index[Generation], Index[Generation]},
      Value            -> {
        Cll[1, 1] -> 0., Cll[1, 2] -> 0., Cll[1, 3] -> 0.,
        Cll[2, 1] -> 0., Cll[2, 2] -> 1., Cll[2, 3] -> 0.,
        Cll[3, 1] -> 0., Cll[3, 2] -> 0., Cll[3, 3] -> 0.
      },
      InteractionOrder -> {NP, 1},
      Description      -> "Weinberg operator Wilson coefficients C5^{ll'} (dimensionless), paper Eq.(dim5Lag); benchmark C5^{mu mu} = 1, all others 0"
    },
  ```
- line 62 (use): `Cll[1, 1] -> 0., Cll[1, 2] -> 0., Cll[1, 3] -> 0.,`
- line 63 (use): `Cll[2, 1] -> 0., Cll[2, 2] -> 1., Cll[2, 3] -> 0.,`
- line 64 (use): `Cll[3, 1] -> 0., Cll[3, 2] -> 0., Cll[3, 3] -> 0.`
- line 75 (use): `Value         -> Abs[Cll[1, 1] + Cll[1, 2] + Cll[1, 3] + Cll[2, 1] + Cll[2, 2] + Cll[2, 3] + Cll[3, 1] + Cll[3, 2] + Cll[3, 3]] vev^2/Lambda,`

## compile log, distinct lines (tail)
```
utation: Dynamic[FR$FeynmanRules] / 220.
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
  
