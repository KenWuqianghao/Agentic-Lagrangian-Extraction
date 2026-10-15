# Model dossier — `HNLs`

**Status: never cleared the chain.** A stack of layered semantic UFO leaks: `Mass -> N4` against an undefined `MN4`, `NoUnfold[..]` inside index ranges, a bare `NP` interaction order. Each was fixed once the diagnostics named it, but the stack outlasted the round budget.

This dossier is not a completed reverse-check review package. It collects what exists for this model so you can read the physics without opening the source files. Where a full review package does exist for a model, it is the `REVIEW.pdf` in that model's directory.

| item | value |
|---|---|
| model | `HNLs` |
| chain status | did not pass |
| Lagrangian source | `repair3/round3/model.fr (last attempt)` |
| Lagrangian terms found | 15 |

## Why this model matters to you

The loop could not get this model through the chain. It is included so the picture is the whole benchmark, not only the successes. The Lagrangian below is the best attempt the loop produced; treat it as a draft that is known not to validate.

## Verbatim Lagrangian terms

Quoted unmodified from the `.fr`. These are the terms any reconstruction would have to account for.

### `Mesons` (`=`)

```mathematica
True
```

### `LHeavyNMajoranaMass` (`:=`)

```mathematica
Block[{sp,ii,jj,ff1,ff2}, -Sum[yN[ff1,ff2] LLbar[sp,ii,ff1].NR[sp,ff2] Phibar[jj] Eps[ii,jj],{ff1,1,3},{ff2,1,1}] - MN4/2 Sum[NRcbar[sp,ff1].NR[sp,ff1],{ff1,1,1}] + HC[-Sum[yN[ff1,ff2] LLbar[sp,ii,ff1].NR[sp,ff2] Phibar[jj] Eps[ii,jj],{ff1,1,3},{ff2,1,1}]]]
```

### `LHeavyNDiracMass` (`:=`)

```mathematica
Block[{sp,ii,jj,ff1,ff2}, -Sum[yN[ff1,ff2] LLbar[sp,ii,ff1].NR[sp,ff2] Phibar[jj] Eps[ii,jj],{ff1,1,3},{ff2,1,1}] - MN4 Sum[NLbar[sp,ff1].NR[sp,ff1],{ff1,1,1}] + HC[-Sum[yN[ff1,ff2] LLbar[sp,ii,ff1].NR[sp,ff2] Phibar[jj] Eps[ii,jj],{ff1,1,3},{ff2,1,1}] - MN4 Sum[NLbar[sp,ff1].NR[sp,ff1],{ff1,1,1}]]]
```

### `LHeavyNMass` (`:=`)

```mathematica
Block[{sp}, -MN4 N4bar[sp].N4[sp]]
```

### `LHeavyNEW` (`:=`)

```mathematica
Block[{mu,sp,sp2,sp3,ii,jj,kk,ll,aa}, gw/Sqrt[2] W[mu] Sum[Conjugate[PMNS[aa,ii]] vlbar[jj,ii].Ga[mu,jj,kk].ProjM[kk,ll].l[ll,aa],{aa,1,3},{ii,1,4}] + gw/(4*cw) Z[mu] Sum[Sum[Conjugate[PMNS[aa,ii]] PMNS[aa,jj],{aa,1,3}] vlbar[sp,ii].Ga[mu,sp,sp2].ProjM[sp2,sp3].vl[sp3,jj],{ii,1,4},{jj,1,4}] + HC[gw/Sqrt[2] W[mu] Sum[Conjugate[PMNS[aa,ii]] vlbar[jj,ii].Ga[mu,jj,kk].ProjM[kk,ll].l[ll,aa],{aa,1,3},{ii,1,4}]]]
```

### `LHadrPseudoscalarChargedCore` (`:=`)

```mathematica
Block[{ii,jj,ff1,ff2}, Sum[I*Sqrt[2]*Gf*fpi*CKM[1,1] Pipbar PMNS[ff2,ff1] yl[ff2,ff2] vev/Sqrt[2] lbar[ii,ff2].ProjM[ii,jj].vl[jj,ff1] - I*Sqrt[2]*Gf*fpi*CKM[1,1] Pipbar PMNS[ff2,ff1] numass[ff1,ff1] lbar[ii,ff2].ProjP[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,3}] + Sum[I*Sqrt[2]*Gf*fK*CKM[1,2] Kpbar PMNS[ff2,ff1] yl[ff2,ff2] vev/Sqrt[2] lbar[ii,ff2].ProjM[ii,jj].vl[jj,ff1] - I*Sqrt[2]*Gf*fK*CKM[1,2] Kpbar PMNS[ff2,ff1] numass[ff1,ff1] lbar[ii,ff2].ProjP[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,3}] + Sum[I*Sqrt[2]*Gf*fD*CKM[2,1] Ddbar PMNS[ff2,ff1] yl[ff2,ff2] vev/Sqrt[2] lbar[ii,ff2].ProjM[ii,jj].vl[jj,ff1] - I*Sqrt[2]*Gf*fD*CKM[2,1] Ddbar PMNS[ff2,ff1] numass[ff1,ff1] lbar[ii,ff2].ProjP[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,3}] + Sum[I*Sqrt[2]*Gf*fDs*CKM[2,2] Dsbar PMNS[ff2,ff1] yl[ff2,ff2] vev/Sqrt[2] lbar[ii,ff2].ProjM[ii,jj].vl[jj,ff1] - I*Sqrt[2]*Gf*fDs*CKM[2,2] Dsbar PMNS[ff2,ff1] numass[ff1,ff1] lbar[ii,ff2].ProjP[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,3}]]
```

### `LHadrPseudoscalarNeutral` (`:=`)

```mathematica
Block[{ii,jj,ff1,ff2,ff3}, Sum[-I/2*Gf*fpi Pi0 Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] numass[ff2,ff2] vlbar[ii,ff1].ProjP[ii,jj].vl[jj,ff2] + I/2*Gf*fpi Pi0 Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] numass[ff1,ff1] vlbar[ii,ff1].ProjM[ii,jj].vl[jj,ff2],{ff1,1,4},{ff2,1,4},{ff3,1,3}] + Sum[-I/2*Gf*feta Eta Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] numass[ff2,ff2] vlbar[ii,ff1].ProjP[ii,jj].vl[jj,ff2] + I/2*Gf*feta Eta Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] numass[ff1,ff1] vlbar[ii,ff1].ProjM[ii,jj].vl[jj,ff2],{ff1,1,4},{ff2,1,4},{ff3,1,3}] + Sum[-I/2*Gf*fetap Etap Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] numass[ff2,ff2] vlbar[ii,ff1].ProjP[ii,jj].vl[jj,ff2] + I/2*Gf*fetap Etap Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] numass[ff1,ff1] vlbar[ii,ff1].ProjM[ii,jj].vl[jj,ff2],{ff1,1,4},{ff2,1,4},{ff3,1,3}]]
```

### `LHadrPseudoscalarCharged` (`:=`)

```mathematica
LHadrPseudoscalarChargedCore + HC[LHadrPseudoscalarChargedCore]
```

### `LHadrVectorNeutral` (`:=`)

```mathematica
Block[{mu,nu,ii,jj,kk,ff1,ff2,ff3}, -1/8 FS[rho0,mu,nu] FS[rho0,mu,nu] + Mrho0^2/4 rho0[mu] rho0[mu] - Sum[1/2*Gf*frho*(1-2*sw^2) rho0[mu] Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] vlbar[ii,ff1].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff2],{ff1,1,4},{ff2,1,4},{ff3,1,3}] -1/8 FS[omega,mu,nu] FS[omega,mu,nu] + Mom^2/4 omega[mu] omega[mu] + Sum[1/2*Gf*fomega*(2/3*sw^2) omega[mu] Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] vlbar[ii,ff1].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff2],{ff1,1,4},{ff2,1,4},{ff3,1,3}] -1/8 FS[phimeson,mu,nu] FS[phimeson,mu,nu] + Mphi^2/4 phimeson[mu] phimeson[mu] + Sum[1/2*Sqrt[2]*Gf*fphi*(1/2 - 2/3*sw^2) phimeson[mu] Conjugate[PMNS[ff3,ff1]] PMNS[ff3,ff2] vlbar[ii,ff1].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff2],{ff1,1,4},{ff2,1,4},{ff3,1,3}]]
```

### `LHadrVectorChargedCore` (`:=`)

```mathematica
Block[{mu,nu,ii,jj,kk,ff1,ff2}, -1/4 FS[rhobar,mu,nu] FS[rho,mu,nu] + Mrho^2/2 rhobar[mu] rho[mu] - Sum[Sqrt[2]*Gf*frho*CKM[1,1] PMNS[ff2,ff1] lbar[ii,ff2].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff1] rhobar[mu],{ff1,1,4},{ff2,1,3}] -1/4 FS[Kstarbar,mu,nu] FS[Kstar,mu,nu] + MKstar^2/2 Kstarbar[mu] Kstar[mu] - Sum[Sqrt[2]*Gf*fKstar*CKM[1,2] PMNS[ff2,ff1] lbar[ii,ff2].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff1] Kstarbar[mu],{ff1,1,4},{ff2,1,3}]]
```

### `LHadrVectorChargedInteractions` (`:=`)

```mathematica
Block[{mu,ii,jj,kk,ff1,ff2}, -Sum[Sqrt[2]*Gf*frho*CKM[1,1] PMNS[ff2,ff1] lbar[ii,ff2].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff1] rhobar[mu],{ff1,1,4},{ff2,1,3}] - Sum[Sqrt[2]*Gf*fKstar*CKM[1,2] PMNS[ff2,ff1] lbar[ii,ff2].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff1] Kstarbar[mu],{ff1,1,4},{ff2,1,3}]]
```

### `LHadrVectorCharged` (`:=`)

```mathematica
LHadrVectorChargedCore + HC[LHadrVectorChargedInteractions]
```

### `LHadrSemileptonicCore` (`:=`)

```mathematica
Block[{mu,ii,jj,kk,ff1,ff2}, -Sum[2*Sqrt[2]*Gf*CKM[1,2]*fplusK0Pi[ff1,ff2]*I del[Pipbar,mu] K0bar PMNS[ff2,ff1] lbar[ii,ff2].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff1],{ff1,1,4},{ff2,1,2}] + Sum[Sqrt[2]*Gf*CKM[1,2]*(fplusK0Pi[ff1,ff2]-fminusK0Pi[ff1,ff2])*vev/Sqrt[2] Pipbar K0bar PMNS[ff2,ff1] yl[ff2,ff2] lbar[ii,ff2].ProjM[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,2}] - Sum[Sqrt[2]*Gf*CKM[1,2]*(fplusK0Pi[ff1,ff2]-fminusK0Pi[ff1,ff2]) Pipbar K0bar PMNS[ff2,ff1] numass[ff1,ff1] lbar[ii,ff2].ProjP[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,2}] - Sum[2*Gf*CKM[1,2]*fplusKPi0[ff1,ff2]*I del[Pi0,mu] Kpbar PMNS[ff2,ff1] lbar[ii,ff2].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff1],{ff1,1,4},{ff2,1,2}] + Sum[Gf*CKM[1,2]*(fplusKPi0[ff1,ff2]-fminusKPi0[ff1,ff2])*vev/Sqrt[2] Pi0 Kpbar PMNS[ff2,ff1] yl[ff2,ff2] lbar[ii,ff2].ProjM[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,2}] - Sum[Gf*CKM[1,2]*(fplusKPi0[ff1,ff2]-fminusKPi0[ff1,ff2]) Pi0 Kpbar PMNS[ff2,ff1] numass[ff1,ff1] lbar[ii,ff2].ProjP[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,2}] - Sum[2*Sqrt[2]*Gf*CKM[2,2]*fplusDK[ff1,ff2]*I del[Kpbar,mu] D0bar PMNS[ff2,ff1] lbar[ii,ff2].Ga[mu,ii,jj].ProjM[jj,kk].vl[kk,ff1],{ff1,1,4},{ff2,1,2}] + Sum[Sqrt[2]*Gf*CKM[2,2]*(fplusDK[ff1,ff2]-fminusDK[ff1,ff2])*vev/Sqrt[2] Kpbar D0bar PMNS[ff2,ff1] yl[ff2,ff2] lbar[ii,ff2].ProjM[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,2}] - Sum[Sqrt[2]*Gf*CKM[2,2]*(fplusDK[ff1,ff2]-fminusDK[ff1,ff2]) Kpbar D0bar PMNS[ff2,ff1] numass[ff1,ff1] lbar[ii,ff2].ProjP[ii,jj].vl[jj,ff1],{ff1,1,4},{ff2,1,2}]]
```

### `LHadrSemileptonic` (`:=`)

```mathematica
LHadrSemileptonicCore + HC[LHadrSemileptonicCore]
```

### `LTot` (`:=`)

```mathematica
LHeavyNMass + LHeavyNEW + LHadrPseudoscalarCharged + LHadrPseudoscalarNeutral + LHadrVectorNeutral + LHadrVectorCharged + LHadrSemileptonic
```

## The last failure the loop worked on

This is the validation report handed to the repair agent at the start of `repair3/round3` — the problem it was asked to fix. The model still did not pass after this round.

# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- Hermiticity check: True
- Kinetic-terms check: True
- Mass-spectrum check: True
- MadGraph import: False
- Heuristic error tags: duplicate_particle_names, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd

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
, Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 4 (Local):
ReplaceAll::reps: {Rule[Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 5 (Local):
ReplaceAll::reps: {Rule[Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 8 (Local):
ReplaceAll::reps: {Rule[Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.
From kernel 2 (Local):
ReplaceAll::reps: {Rule[Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt], Ext[#2, opt___], Ext[#3, opt]]} is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing.

General::stop: Further output of `1` is neither a list of replacement rules nor a valid dispatch table and so cannot be used for replacing. will be suppressed during this calculation.
From kernel 8 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad Multpad + Multpad Index[Neutrinos, Ext[1]], 0].
From kernel 8 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad Multpad + Multpad NoUnfold[{1, 2, 3, 4}], 0].
From kernel 8 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad Multpad + Multpad Index[Neutrinos, Ext[2]], 0].
From kernel 8 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.

Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].

Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + NoUnfold[{1, 2, 3, 4}], 0].

Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[2]], 0].

General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 8 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].
From kernel 1 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].
From kernel 2 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].
From kernel 3 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].
From kernel 4 (Local):
Complement::normal: Nonatomic expression expected at position 2 in Complement[Addpad + Index[Neutrinos, Ext[1]], 0].

General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 8 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 1 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of Complement::normal will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/400 .

StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.

StringJoin::string: String expected at position 2 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.
    - Writing files.

StringJoin::string: String expected at position 1 in PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1.

General::stop: Further output of StringJoin::string will be suppressed during this calculation.

Part::partw: Part 3 of {{NP, 1}, {NP, 0}} does not exist.
Done!
[INFO] Done.

```

## MadGraph import output (tail)
```
MG5_aMC/models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "$MG5_PATH/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "$MG5_PATH/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
Command "import /private/tmp/repair_bench3/HNLs/round2/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench3/HNLs/round2/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.

```

## MG5_debug (the real MadGraph error)
```
madgraph_interface.py", line 5837, in do_import
    raise self.InvalidCmd('UFO model not python3 compatible. You can convert it via the command \nconvert model %s\nYou can also type \"set auto_convert_model T\" to automatically convert all python2 module to be python3 compatible in the future.' % model_path)
madgraph.InvalidCmd: UFO model not python3 compatible. You can convert it via the command 
convert model /tmp/repair_bench3/HNLs/round2/UFO
You can also type "set auto_convert_model T" to automatically convert all python2 module to be python3 compatible in the future.

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

## UFO Python syntax error — `UFO/lorentz.py` line 15: cannot assign to literal here. Maybe you meant '==' instead of '='?
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
   13 | 
   14 | 
   15 | 1 = Lorentz(name = '1',
   16 |             spins = [],
   17 |             structure = '0')
```

## UFO Python syntax error — `UFO/vertices.py` line 2338: closing parenthesis ')' does not match opening parenthesis '[' on line 2335
This generated file is not valid Python, which is why MadGraph's import fails. Find the .fr declaration that produced it and fix THAT (the UFO is regenerated each round).
```
 2336 |                color = [ '1' ],
 2337 |                lorentz = [ L.<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1 ],
 2338 |                couplings = {(0,-1 + PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>1):C.GC_613})
 2339 | 
 2340 | V_389 = Vertex(name = 'V_389',
```

## UFO direct-import error (the REAL reason MadGraph rejects this UFO — MadGraph's own message misreports the location)
Fix the .fr declaration that produced this; the UFO is regenerated from model.fr each round.
```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    __import__('UFO')
    ~~~~~~~~~~^^^^^^^
  File "/tmp/repair_bench3/HNLs/round2/UFO/__init__.py", line 4, in <module>
    import lorentz
  File "/tmp/repair_bench3/HNLs/round2/UFO/lorentz.py", line 15
    1 = Lorentz(name = '1',
    ^
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?

```

## Repair history

What the loop tried, and what each attempt measured.

# Repair history — previous attempts on this model

## Attempt 1
What was changed (the agent's own summary):
Updated `model.fr` in place: fixed the `N4` mass declaration to use the existing `MassN4` parameter, added explicit sums over neutrino mass eigenstates in the `NR`/`NL` unphysical field definitions to prevent FeynRules internals from leaking into UFO Python, corrected the internal `yN` convention to match the declared heavy-neutrino rotation and remove off-diagonal mass residues, removed the unused `LagHeavyN` assignment, and added missing `HC[...]` conjugates for charged pseudoscalar, charged vector interaction, and semileptonic hadronic terms so `LTot` remains the final BSM-only assignment and is Hermitian. Static checks passed for balanced delimiters, final `LTot`, and absence of source-level leaked constructs; I could not run the full Wolfram validation because `wolframscript` has no configured kernel path in this environment.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=duplicate_particle_names, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=4276.7

## Attempt 2
What was changed (the agent's own summary):
Updated `model.fr` to remove the failed `MassN4` alias path: `FR$RmDblExt` no longer remaps `MN4`, the unused internal `MassN4` parameter was removed, and the `N4` class mass now uses the existing external `MN4` directly so the UFO should not emit `value = MassN4`. I also kept the old gauge-basis Dirac block defined above but removed it from final `LTot`, replacing it with a mass-basis `LHeavyNMass := -MN4 N4bar.N4`; this preserves the heavy-neutrino mass while preventing unreduced `LLbar`/`Phibar` and FeynRules `PRIVATE` expressions from leaking into UFO Python. `LTot` remains the last top-level assignment, and I verified balanced delimiters plus no remaining `MassN4` references; full FeynRules validation could not be run because `wolframscript` still has no configured Wolfram kernel path.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=duplicate_particle_names, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=1842.0

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=duplicate_particle_names, mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=380.2

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:
