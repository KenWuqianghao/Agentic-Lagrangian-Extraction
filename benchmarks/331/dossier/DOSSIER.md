# Model dossier — `331`

**Status: reverse run failed.** The blank-slate reconstruction aborted on an agent transport error. This is an infrastructure failure, not a physics result.

This dossier is not a completed reverse-check review package. It collects what exists for this model so you can read the physics without opening the source files. Where a full review package does exist for a model, it is the `REVIEW.pdf` in that model's directory.

| item | value |
|---|---|
| model | `331` |
| chain status | passed the full chain |
| Lagrangian source | `repair2/final.fr (re-validated)` |
| Lagrangian terms found | 6 |

## Verbatim Lagrangian terms

Quoted unmodified from the `.fr`. These are the terms any reconstruction would have to account for.

### `VHiggs331` (`=`)

```mathematica
mu1sq HC[rho].rho + mu2sq HC[eta].eta + mu3sq HC[chi].chi + lam1 (HC[rho].rho)^2 + lam2 (HC[eta].eta)^2 + lam3 (HC[chi].chi)^2 + lam12 (HC[rho].rho) (HC[eta].eta) + lam13 (HC[rho].rho) (HC[chi].chi) + lam23 (HC[eta].eta) (HC[chi].chi) + lamp12 (HC[rho].eta) (HC[eta].rho) + lamp13 (HC[rho].chi) (HC[chi].rho) + lamp23 (HC[eta].chi) (HC[chi].eta) + Sqrt[2] f331 (Eps[i,j,k] rho[i] eta[j] chi[k] + HC[Eps[i,j,k] rho[i] eta[j] chi[k]])
```

### `LHiggs331` (`=`)

```mathematica
HC[DC[rho, mu]].DC[rho, mu] + HC[DC[eta, mu]].DC[eta, mu] + HC[DC[chi, mu]].DC[chi, mu] - VHiggs331
```

### `LGauge331Mass` (`=`)

```mathematica
1/4 gw^2 vev^2 W[mu] HC[W[mu]] + 1/4 gw^2 (v3^2 + v2^2) Yp[mu] HC[Yp[mu]] + 1/4 gw^2 (v3^2 + v1^2) Vp[mu] HC[Vp[mu]] + 1/2 MZp^2 Zp[mu] Zp[mu]
```

### `LGaugeSelf331` (`=`)

```mathematica
(-I ee) A[mu] W[nu] HC[W[sig]] VVV[mu,nu,sig] + (I am ee/2) A[mu] Vp[nu] HC[Vp[sig]] VVV[mu,nu,sig] + (I ap ee/2) A[mu] Yp[nu] HC[Yp[sig]] VVV[mu,nu,sig] - I Sqrt[3] ee a0/(2 cw sw) Zp[mu] (Vp[nu] HC[Vp[sig]] + Yp[nu] HC[Yp[sig]]) VVV[mu,nu,sig]
```

### `LScalarFermion331` (`=`)

```mathematica
H0 (O331[3,1] ME[ll]/v3 HC[EL[ll]].EL[ll] + O331[2,1] Ml[ll]/v2 HC[LL[ll]].LL[ll]) - I H2 (U331[3,2] ME[ll]/v3 HC[EL[ll]].EL[ll]) - I H3 (U331[3,3] ME[ll]/v3 HC[EL[ll]].EL[ll]) - I H2 (U331[1,2] Md[q]/v1 HC[d[q]].d[q] + U331[2,2] Mu[q]/v2 HC[u[q]].u[q]) - I H3 (U331[1,3] Md[q]/v1 HC[d[q]].d[q] + U331[2,3] Mu[q]/v2 HC[u[q]].u[q])
```

### `LTot` (`:=`)

```mathematica
LGaugeSelf331
```

## The last failure the loop worked on

This is the validation report handed to the repair agent at the start of `repair2/round2` — the problem it was asked to fix. The model **passed** after this round; the report below is the state that was repaired, not the final one.

# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: False
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: hermiticity_fail, mg5_import_fail, mg5_python_traceback

## FeynRules check `hermiticity` output
```
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
10 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 10.

Part::partw: Part 1 of {} does not exist.

Part::partw: Part 1 of {} does not exist.

Part::partw: Part 1 of {} does not exist.

General::stop: Further output of Part::partw will be suppressed during this calculation.
5 vertices obtained.
The lagrangian appears not to be hermitian.
Non vanishing terms during the Feynman rule calculation for L - HC[L]:
{{{A, 1}, {Vp, 2}, {Vpbar, 3}}, -1/2*(am*ebar . Ga[0]*ME[Index[Lorentz, α], Index[Lorentz, Ext[1]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[2]]]*VVV[mu, nu, sig])}
{{{A, 1}, {W, 2}, {Wbar, 3}}, ebar . Ga[0]*ME[Index[Lorentz, α], Index[Lorentz, Ext[1]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[2]]]*VVV[mu, nu, sig]}
{{{A, 1}, {Yp, 2}, {Ypbar, 3}}, -1/2*(ap*ebar . Ga[0]*ME[Index[Lorentz, α], Index[Lorentz, Ext[1]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[2]]]*VVV[mu, nu, sig])}
{{{Vp, 1}, {Vpbar, 2}, {Zp, 3}}, (Sqrt[3]*a0*ebar . Ga[0]*ME[Index[Lorentz, α], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[2]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[1]]]*VVV[mu, nu, sig])/(2*cw*sw)}
{{{Yp, 1}, {Ypbar, 2}, {Zp, 3}}, (Sqrt[3]*a0*ebar . Ga[0]*ME[Index[Lorentz, α], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[2]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[1]]]*VVV[mu, nu, sig])/(2*cw*sw)}
HEPTAPOD-CHECK-ERROR
```

## FeynRules check `kinetic_terms` output
```
Neglecting all terms with more than 2 particles.
All kinetic terms are diagonal.
```

## FeynRules check `mass_spectrum` output
```
Neglecting all terms with more than 2 particles.
All mass terms are diagonal.
Getting mass spectrum.
Checking for less then 0.1% agreement with model file values.
```

## FeynRules / Wolfram Engine output (tail)
```
 name.
From kernel 1 (Local):
LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.
From kernel 2 (Local):
LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.
From kernel 3 (Local):
LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.

General::stop: Further output of In FeynRules mode, all class members should be given a mass name. will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.
From kernel 6 (Local):
General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.
From kernel 7 (Local):
General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
Merging model-files...
This model implementation was created by
Codex extraction from Cao and Zhang, arXiv:1611.09337
Model Version: 1.0.0
For more information, type ModelInformation[].

   - Loading particle classes.

LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.

LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.

LoadModel::FAMass: In FeynRules mode, all class members should be given a mass name.

General::stop: Further output of LoadModel::FAMass will be suppressed during this calculation.
   - Loading gauge group classes.
   - Loading parameter classes.

Model 331_gen loaded.
[INFO] Total Lagrangian: LSM + LTot
[INFO] Running FeynRules consistency checks.
HEPTAPOD-CHECK-BEGIN: hermiticity
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
10 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 10.

Part::partw: Part 1 of {} does not exist.

Part::partw: Part 1 of {} does not exist.

Part::partw: Part 1 of {} does not exist.

General::stop: Further output of Part::partw will be suppressed during this calculation.
5 vertices obtained.
The lagrangian appears not to be hermitian.
Non vanishing terms during the Feynman rule calculation for L - HC[L]:
{{{A, 1}, {Vp, 2}, {Vpbar, 3}}, -1/2*(am*ebar . Ga[0]*ME[Index[Lorentz, α], Index[Lorentz, Ext[1]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[2]]]*VVV[mu, nu, sig])}
{{{A, 1}, {W, 2}, {Wbar, 3}}, ebar . Ga[0]*ME[Index[Lorentz, α], Index[Lorentz, Ext[1]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[2]]]*VVV[mu, nu, sig]}
{{{A, 1}, {Yp, 2}, {Ypbar, 3}}, -1/2*(ap*ebar . Ga[0]*ME[Index[Lorentz, α], Index[Lorentz, Ext[1]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[2]]]*VVV[mu, nu, sig])}
{{{Vp, 1}, {Vpbar, 2}, {Zp, 3}}, (Sqrt[3]*a0*ebar . Ga[0]*ME[Index[Lorentz, α], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[2]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[1]]]*VVV[mu, nu, sig])/(2*cw*sw)}
{{{Yp, 1}, {Ypbar, 2}, {Zp, 3}}, (Sqrt[3]*a0*ebar . Ga[0]*ME[Index[Lorentz, α], Index[Lorentz, Ext[3]]]*ME[Index[Lorentz, β], Index[Lorentz, Ext[2]]]*ME[Index[Lorentz, γ], Index[Lorentz, Ext[1]]]*VVV[mu, nu, sig])/(2*cw*sw)}
HEPTAPOD-CHECK-ERROR
HEPTAPOD-CHECK-END: hermiticity
HEPTAPOD-CHECK-BEGIN: kinetic_terms
Neglecting all terms with more than 2 particles.
All kinetic terms are diagonal.
HEPTAPOD-CHECK-END: kinetic_terms
HEPTAPOD-CHECK-BEGIN: mass_spectrum
Neglecting all terms with more than 2 particles.
All mass terms are diagonal.
Getting mass spectrum.
Checking for less then 0.1% agreement with model file values.
HEPTAPOD-CHECK-END: mass_spectrum
[INFO] UFO output: /tmp/repair_bench2/331/round1/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
41 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 41.
31 vertices obtained.
Flavor expansion of the vertices: Dynamic[FR$Count1] / 31
   - Saved vertices in InterfaceRun[ 1 ].
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/75 .
    - Writing files.
Done!
[INFO] Done.


```

## MadGraph import output (tail)
```
u/MG5_aMC/models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "$MG5_PATH/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "$MG5_PATH/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
Command "import /private/tmp/repair_bench2/331/round1/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench2/331/round1/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.

```

## MG5_debug (the real MadGraph error)
```
"$MG5_PATH/models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "$MG5_PATH/models/import_ufo.py", line 415, in import_full_model
    model = ufo2mg5_converter.load_model()
  File "$MG5_PATH/models/import_ufo.py", line 547, in load_model
    raise InvalidModel("name %s define multiple time. Please correct the UFO model!" \
                                                      % (param.name))
models.import_ufo.InvalidModel: name WT define multiple time. Please correct the UFO model!

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "$MG5_PATH/madgraph/interface/extended_cmd.py", line 1570, in onecmd
    return self.onecmd_orig(line, **opt)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "$MG5_PATH/madgraph/interface/extended_cmd.py", line 1519, in onecmd_orig
    return func(arg, **opt)
  File "$MG5_PATH/madgraph/interface/master_interface.py", line 281, in do_import
    self.cmd.do_import(self, *args, **opts)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "$MG5_PATH/madgraph/interface/madgraph_interface.py", line 5893, in do_import
    self.import_command_file(args[1])
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "$MG5_PATH/madgraph/interface/extended_cmd.py", line 1718, in import_command_file
    self.exec_cmd(line, precmd=True)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "$MG5_PATH/madgraph/interface/extended_cmd.py", line 1599, in exec_cmd
    stop = Cmd.onecmd_orig(current_interface, line, **opt)
  File "$MG5_PATH/madgraph/interface/extended_cmd.py", line 1519, in onecmd_orig
    return func(arg, **opt)
  File "$MG5_PATH/madgraph/interface/master_interface.py", line 281, in do_import
    self.cmd.do_import(self, *args, **opts)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "$MG5_PATH/madgraph/interface/madgraph_interface.py", line 5835, in do_import
    raise err
  File "$MG5_PATH/madgraph/interface/madgraph_interface.py", line 5819, in do_import
    self._curr_model = import_ufo.import_model(args[1], prefix=prefix,
                       ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
        complex_mass_scheme=self.options['complex_mass_scheme'],
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        options=options)
        ^^^^^^^^^^^^^^^^
  File "$MG5_PATH/models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "$MG5_PATH/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "$MG5_PATH/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
Fail to write options with error No model currently active, please import a model!
```

## Repair history

What the loop tried, and what each attempt measured.

# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: added a `VVV` UpValue so `HC[VVV[...]]` reduces to `VVV[...]`, fixing the hermiticity check residue from the triple-gauge terms, and replaced UFO-facing symbolic benchmark values in `beta331` and particle `QuantumNumbers` with their numeric values for `beta331 = 1/Sqrt[3]` so generated Python does not leak `Sqrt[...]`/`beta331` expressions into MadGraph particle charges. `LTot := LGaugeSelf331;` remains the last top-level assignment. I could not rerun the full Wolfram/MadGraph validation because `wolframscript` is installed but has no configured kernel path in this environment.

Validation outcome AFTER that change: status=compiled, hermiticity=False, kinetic=True, mass=True, madgraph_import=False, tags=hermiticity_fail, mg5_import_fail, mg5_python_traceback, compile_seconds=24.9

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=False, kinetic=True, mass=True, madgraph_import=False, tags=hermiticity_fail, mg5_import_fail, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=25.5

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:
