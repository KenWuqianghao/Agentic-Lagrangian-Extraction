# Model dossier — `B-L-SM`

**Status: reverse run failed.** The blank-slate reconstruction aborted on an agent transport error (connection reset). Infrastructure, not physics.

This dossier is not a completed reverse-check review package. It collects what exists for this model so you can read the physics without opening the source files. Where a full review package does exist for a model, it is the `REVIEW.pdf` in that model's directory.

| item | value |
|---|---|
| model | `B-L-SM` |
| chain status | passed the full chain |
| Lagrangian source | `repair2/final.fr (re-validated)` |
| Lagrangian terms found | 9 |

## Verbatim Lagrangian terms

Quoted unmodified from the `.fr`. These are the terms any reconstruction would have to account for.

### `LZpKin` (`:=`)

```mathematica
Block[{mu,nu}, -1/4 FS[Zp,mu,nu] FS[Zp,mu,nu]]
```

### `LChi` (`:=`)

```mathematica
Block[{mu,ii}, ExpandIndices[(del[HC[Chi],mu] - I*2*g1p*Zp[mu]*HC[Chi])*(del[Chi,mu] + I*2*g1p*Zp[mu]*Chi) - muChi2*HC[Chi]*Chi - lambda2BL*(HC[Chi]*Chi)^2 - lambda3BL*(Phibar[ii]*Phi[ii])*(HC[Chi]*Chi), FlavorExpand -> SU2D]]
```

### `LBLCurrent` (`:=`)

```mathematica
Block[{mu}, ExpandIndices[-g1p*Zp[mu]*(1/3 QLbar.Ga[mu].QL + 1/3 uRbar.Ga[mu].uR + 1/3 dRbar.Ga[mu].dR - LLbar.Ga[mu].LL - lRbar.Ga[mu].lR - nuRbar.Ga[mu].nuR), FlavorExpand -> {SU2D, Generation, Colour}]]
```

### `YMRRules` (`=`)

```mathematica
{YMRMat[1,1] -> YMR1x1, YMRMat[1,2] -> YMR1x2, YMRMat[1,3] -> YMR1x3, YMRMat[2,1] -> YMR2x1, YMRMat[2,2] -> YMR2x2, YMRMat[2,3] -> YMR2x3, YMRMat[3,1] -> YMR3x1, YMRMat[3,2] -> YMR3x2, YMRMat[3,3] -> YMR3x3}
```

### `YNURules` (`=`)

```mathematica
{YNUMat[1,1] -> YNU1x1, YNUMat[1,2] -> YNU1x2, YNUMat[1,3] -> YNU1x3, YNUMat[2,1] -> YNU2x1, YNUMat[2,2] -> YNU2x2, YNUMat[2,3] -> YNU2x3, YNUMat[3,1] -> YNU3x1, YNUMat[3,2] -> YNU3x2, YNUMat[3,3] -> YNU3x3}
```

### `LNuYukNonHC` (`:=`)

```mathematica
Block[{sp,ff1,ff2}, ExpandIndices[-YNUMat[ff1,ff2] (LLbar[sp,1,ff1].nuR[sp,ff2] (Phibar[2] - vev/Sqrt[2]) - LLbar[sp,2,ff1].nuR[sp,ff2] Phibar[1]) - 1/2 YMRMat[ff1,ff2] anti[CC[nuR]][sp,ff1].nuR[sp,ff2] Chi, FlavorExpand -> Generation] /. YNURules /. YMRRules]
```

### `LNuYuk` (`:=`)

```mathematica
LNuYukNonHC + HC[LNuYukNonHC]
```

### `LScalarDiag` (`:=`)

```mathematica
Block[{mu}, ca*sa*del[H,mu]*del[H2,mu] - ca*sa*muChi2*H*H2 - ca*sa*lambda3BL*vev^2*H*H2/2 + ca*lambda3BL*vev*xBL*H*H2 - 3*ca*sa*lambda2BL*xBL^2*H*H2]
```

### `LTot` (`:=`)

```mathematica
LZpKin + LChi + LBLCurrent + LNuYuk + LScalarDiag
```

## The last failure the loop worked on

This is the validation report handed to the repair agent at the start of `repair2/round3` — the problem it was asked to fix. The model **passed** after this round; the report below is the state that was repaired, not the final one.

# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: True
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: mg5_import_fail, mg5_python_traceback

## FeynRules check `hermiticity` output
```
Checking for hermiticity by calculating the Feynman rules contained in L-HC[L].
If the lagrangian is hermitian, then the number of vertices should be zero.
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
No vertices found.
0 vertices obtained.
The lagrangian is hermitian.
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
ctrum
[INFO] UFO output: /tmp/repair_bench2/B-L-SM/round2/UFO  (AddDecays -> False)
 --- Universal FeynRules Output (UFO) v 1.1 ---
Starting Feynman rule calculation.
Expanding the Lagrangian...
Expanding the indices over 8 cores
Collecting the different structures that enter the vertex.
162 possible non-zero vertices have been found -> starting the computation: Dynamic[FR$FeynmanRules] / 162.
157 vertices obtained.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 157
   - Saved vertices in InterfaceRun[ 1 ].

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number LeptonNumber not conserved in vertex {GP, N1bar, e}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number LeptonNumber not conserved in vertex {GP, N2bar, e}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
Quantum number LeptonNumber not conserved in vertex {GP, N3bar, e}.
Quantum number LeptonNumber not conserved in vertex {GP, N1bar, mu}.
Quantum number LeptonNumber not conserved in vertex {GP, N2bar, mu}.
Quantum number LeptonNumber not conserved in vertex {GP, N3bar, mu}.
Quantum number LeptonNumber not conserved in vertex {GP, N1bar, ta}.
Quantum number LeptonNumber not conserved in vertex {GP, N2bar, ta}.
Quantum number LeptonNumber not conserved in vertex {GP, N3bar, ta}.
Quantum number LeptonNumber not conserved in vertex {G0, N1bar, ve}.
Quantum number LeptonNumber not conserved in vertex {H, N1bar, ve}.
Quantum number LeptonNumber not conserved in vertex {G0, N2bar, ve}.
Quantum number LeptonNumber not conserved in vertex {H, N2bar, ve}.
Quantum number LeptonNumber not conserved in vertex {G0, N3bar, ve}.
Quantum number LeptonNumber not conserved in vertex {H, N3bar, ve}.
Quantum number LeptonNumber not conserved in vertex {G0, N1bar, vm}.
Quantum number LeptonNumber not conserved in vertex {H, N1bar, vm}.
Quantum number LeptonNumber not conserved in vertex {G0, N2bar, vm}.
Quantum number LeptonNumber not conserved in vertex {H, N2bar, vm}.
Quantum number LeptonNumber not conserved in vertex {G0, N3bar, vm}.
Quantum number LeptonNumber not conserved in vertex {H, N3bar, vm}.
Quantum number LeptonNumber not conserved in vertex {G0, N1bar, vt}.
Quantum number LeptonNumber not conserved in vertex {H, N1bar, vt}.
Quantum number LeptonNumber not conserved in vertex {G0, N2bar, vt}.
Quantum number LeptonNumber not conserved in vertex {H, N2bar, vt}.
Quantum number LeptonNumber not conserved in vertex {G0, N3bar, vt}.
Quantum number LeptonNumber not conserved in vertex {H, N3bar, vt}.
Quantum number LeptonNumber not conserved in vertex {GPbar, ebar, N1}.
Quantum number LeptonNumber not conserved in vertex {GPbar, ebar, N2}.
Quantum number LeptonNumber not conserved in vertex {GPbar, ebar, N3}.
Quantum number LeptonNumber not conserved in vertex {GPbar, mubar, N1}.
Quantum number LeptonNumber not conserved in vertex {GPbar, mubar, N2}.
Quantum number LeptonNumber not conserved in vertex {GPbar, mubar, N3}.
Quantum number LeptonNumber not conserved in vertex {GPbar, tabar, N1}.
Quantum number LeptonNumber not conserved in vertex {GPbar, tabar, N2}.
Quantum number LeptonNumber not conserved in vertex {GPbar, tabar, N3}.
Quantum number LeptonNumber not conserved in vertex {G0, vebar, N1}.
Quantum number LeptonNumber not conserved in vertex {H, vebar, N1}.
Quantum number LeptonNumber not conserved in vertex {G0, vebar, N2}.
Quantum number LeptonNumber not conserved in vertex {H, vebar, N2}.
Quantum number LeptonNumber not conserved in vertex {G0, vebar, N3}.
Quantum number LeptonNumber not conserved in vertex {H, vebar, N3}.
Quantum number LeptonNumber not conserved in vertex {G0, vmbar, N1}.
Quantum number LeptonNumber not conserved in vertex {H, vmbar, N1}.
Quantum number LeptonNumber not conserved in vertex {G0, vmbar, N2}.
Quantum number LeptonNumber not conserved in vertex {H, vmbar, N2}.
Quantum number LeptonNumber not conserved in vertex {G0, vmbar, N3}.
Quantum number LeptonNumber not conserved in vertex {H, vmbar, N3}.
Quantum number LeptonNumber not conserved in vertex {G0, vtbar, N1}.
Quantum number LeptonNumber not conserved in vertex {H, vtbar, N1}.
Quantum number LeptonNumber not conserved in vertex {G0, vtbar, N2}.
Quantum number LeptonNumber not conserved in vertex {H, vtbar, N2}.
Quantum number LeptonNumber not conserved in vertex {G0, vtbar, N3}.
Quantum number LeptonNumber not conserved in vertex {H, vtbar, N3}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/201 .
    - Writing files.
Warning: Non positive interaction order QED.
                This might reduce the efficiency of certain matrix element generators.
                See logfile for more details.
Done!
[INFO] Done.


```

## MadGraph import output (tail)
```
aMC/models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "$MG5_PATH/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "$MG5_PATH/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
Command "import /private/tmp/repair_bench2/B-L-SM/round2/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench2/B-L-SM/round2/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.

```

## MG5_debug (the real MadGraph error)
```
5_aMC/models/import_ufo.py", line 611, in load_model
    self.add_interaction(interaction_info, color_info)
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "$MG5_PATH/models/import_ufo.py", line 1840, in add_interaction
    raise InvalidModel('''Some couplings have \'1\' order.
    This is not allowed in MG.
    Please defines an additional coupling to your model''')
models.import_ufo.InvalidModel: Some couplings have '1' order. 
                    This is not allowed in MG. 
                    Please defines an additional coupling to your model

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
Changed `model.fr` in place by renaming the internal Yukawa tensors `yM` and `ynu` to `YMR` and `YNU` throughout their parameter declarations and neutrino Yukawa terms, which should prevent FeynRules from exporting malformed UFO parameter names like `yM1x2 /. yM`. I also added `LScalarDiag` just before the final `LTot` assignment and included it in `LTot` to cancel the reported residual `H`/`H2` kinetic and mass mixing terms, keeping the declared scalar mass basis diagonal. I could not run the full validation locally because `wolframscript` cannot find a Wolfram kernel here and MadGraph is not on `PATH`.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=76.2

## Attempt 2
What was changed (the agent's own summary):
Changed `model.fr` to replace the problematic internal indexed Yukawa parameters `YMR` and `YNU` with explicit scalar internal component parameters (`YMR1x1` ... `YMR3x3`, `YNU1x1` ... `YNU3x3`) carrying the same formulas and zero entries, plus explicit `NP` interaction order. I then rewired `LNuYukNonHC` through local replacement rules so the operator structure is unchanged but FeynRules exports valid UFO identifiers instead of malformed Mathematica `ReplaceAll` names like `YMR1x2 /. YMR`. `LTot` remains the final top-level assignment. I did not run the full Wolfram/MadGraph validation because that would require tools outside the provided directory.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, mg5_python_traceback, compile_seconds=76.0

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=67.4

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:
