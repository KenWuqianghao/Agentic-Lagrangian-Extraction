# Model dossier — `VLC_LN`

**Status: reverse run failed.** The blank-slate reconstruction aborted on an agent transport error. Infrastructure, not physics.

This dossier is not a completed reverse-check review package. It collects what exists for this model so you can read the physics without opening the source files. Where a full review package does exist for a model, it is the `REVIEW.pdf` in that model's directory.

| item | value |
|---|---|
| model | `VLC_LN` |
| chain status | passed the full chain |
| Lagrangian source | `repair2/final.fr (re-validated)` |
| Lagrangian terms found | 15 |

## Verbatim Lagrangian terms

Quoted unmodified from the `.fr`. These are the terms any reconstruction would have to account for.

### `PiMat` (`=`)

```mathematica
{{pi0/Sqrt[2] + eta/Sqrt[6] + etaP/Sqrt[3], pip, Kp}, {pipbar, -pi0/Sqrt[2] + eta/Sqrt[6] + etaP/Sqrt[3], K0}, {Kpbar, K0bar, -2 eta/Sqrt[6] + etaP/Sqrt[3]}}
```

### `Umat` (`:=`)

```mathematica
MatrixExp[I Sqrt[2] PiMat/fpi]
```

### `Mmat` (`=`)

```mathematica
{{mL, 0, y PhiSM[1]}, {0, mL, y PhiSM[2]}, {Conjugate[ytil] PhiSMBar[1], Conjugate[ytil] PhiSMBar[2], mN}}
```

### `LUVVLC` (`:=`)

```mathematica
Block[{mu,sp,aa,kin,yuk},
  kin = I L0bar[sp,aa].Ga[mu].DC[L0[sp,aa],mu] +
        I Lmbar[sp,aa].Ga[mu].DC[Lm[sp,aa],mu] +
        I Nvlcbar[sp,aa].Ga[mu].DC[Nvlc[sp,aa],mu];
  yuk = y PhiSM[1] L0bar[sp,aa].ProjM.Nvlc[sp,aa] +
        y PhiSM[2] Lmbar[sp,aa].ProjM.Nvlc[sp,aa] +
        ytil PhiSMBar[1] L0bar[sp,aa].ProjP.Nvlc[sp,aa] +
        ytil PhiSMBar[2] Lmbar[sp,aa].ProjP.Nvlc[sp,aa];
  1/2 (kin + HC[kin]) -
  mL (L0bar[sp,aa].L0[sp,aa] + Lmbar[sp,aa].Lm[sp,aa]) -
  mN Nvlcbar[sp,aa].Nvlc[sp,aa] +
  yuk + HC[yuk]
]
```

### `LChiralFull` (`:=`)

```mathematica
Block[{mu,i}, fpi^2/4 Tr[DC[Umat,mu].DC[HC[Umat],mu]] + (grho fpi^3 Tr[Mmat.Umat] + HC[grho fpi^3 Tr[Mmat.Umat]]) + fpi^2/16 (mEtaP^2/3) (Log[Det[Umat]] - Log[Det[HC[Umat]]])^2 + 3 gw^2 grho^2 fpi^4/(2 (4 Pi)^2) Sum[Tr[Umat.Ta[i].HC[Umat].Ta[i]], {i,1,3}]]
```

### `LKinCompositeScalars` (`:=`)

```mathematica
Block[{mu}, 1/2 del[pi0,mu] del[pi0,mu] + del[pipbar,mu] del[pip,mu] + 1/2 del[eta,mu] del[eta,mu] + 1/2 del[etaP,mu] del[etaP,mu] - mEtaP^2/2 etaP^2]
```

### `LMExpanded` (`:=`)

```mathematica
-mK2^2 (Kpbar Kp + K0bar K0) - mPi3^2/2 (pi0^2 + 2 pip pipbar) - mEta^2/2 eta^2 + (-I Sqrt[2] grho fpi^2 Bcoup (Kpbar PhiSM[1] + K0bar PhiSM[2]) - grho/Sqrt[2] Acoup fpi (Sum[(Kpbar PauliSigma[a,1,jj] + K0bar PauliSigma[a,2,jj]) PhiSM[jj] PiTriplet[a], {a,1,3}, {jj,1,2}] - eta (Kpbar PhiSM[1] + K0bar PhiSM[2])/Sqrt[3]) + HC[-I Sqrt[2] grho fpi^2 Bcoup (Kpbar PhiSM[1] + K0bar PhiSM[2]) - grho/Sqrt[2] Acoup fpi (Sum[(Kpbar PauliSigma[a,1,jj] + K0bar PauliSigma[a,2,jj]) PhiSM[jj] PiTriplet[a], {a,1,3}, {jj,1,2}] - eta (Kpbar PhiSM[1] + K0bar PhiSM[2])/Sqrt[3])])
```

### `LKinTriplet` (`:=`)

```mathematica
(I del[pipbar, mu] gw pi0 WiPhys[mu, 1])/(2 Sqrt[2]) - (I del[pip, mu] gw pi0 WiPhys[mu, 1])/(2 Sqrt[2]) - (I del[pi0, mu] gw pipbar WiPhys[mu, 1])/(2 Sqrt[2]) + (I del[pi0, mu] gw pip WiPhys[mu, 1])/(2 Sqrt[2]) + (del[pipbar, mu] gw pi0 WiPhys[mu, 2])/(2 Sqrt[2]) + (del[pip, mu] gw pi0 WiPhys[mu, 2])/(2 Sqrt[2]) - (del[pi0, mu] gw pipbar WiPhys[mu, 2])/(2 Sqrt[2]) - (del[pi0, mu] gw pip WiPhys[mu, 2])/(2 Sqrt[2]) + 1/2 I del[pip, mu] gw pipbar WiPhys[mu, 3] - 1/2 I del[pipbar, mu] gw pip WiPhys[mu, 3]
```

### `LKinK2` (`:=`)

```mathematica
Block[{mu}, DK2Bar[1, mu] DK2[1, mu] + DK2Bar[2, mu] DK2[2, mu]]
```

### `LAnomalyTriplet` (`:=`)

```mathematica
Block[{mu,nu,rho,sig}, NHC g1 gw/(32 Pi^2 fpi) Eps[mu,nu,rho,sig] BFS[rho,sig] (PiTriplet[1] SU2FS[mu,nu,1] + PiTriplet[2] SU2FS[mu,nu,2] + PiTriplet[3] SU2FS[mu,nu,3])]
```

### `LAnomalyEta` (`:=`)

```mathematica
Block[{mu,nu,rho,sig}, -NHC eta/(32 Sqrt[3] Pi^2 fpi) Eps[mu,nu,rho,sig] (gw^2 (SU2FS[mu,nu,1] SU2FS[rho,sig,1] + SU2FS[mu,nu,2] SU2FS[rho,sig,2] + SU2FS[mu,nu,3] SU2FS[rho,sig,3]) + g1^2 BFS[mu,nu] BFS[rho,sig])]
```

### `LEDM` (`:=`)

```mathematica
Block[{mu,nu,rho,sig,a}, -mPi3^2/2 Sum[PiTriplet[a]^2,{a,1,3}] - mEta^2/2 eta^2 + 4 Im[y ytil] grho^2 fpi^3/mK2^2 (Sum[PhiSMBar[i] PauliSigma[a,i,j] PhiSM[j] PiTriplet[a],{a,1,3},{i,1,2},{j,1,2}] - eta Sum[PhiSMBar[i] PhiSM[i],{i,1,2}]/Sqrt[3]) + NHC g1 gw/(32 Pi^2 fpi) Eps[mu,nu,rho,sig] BFS[rho,sig] (PiTriplet[1] SU2FS[mu,nu,1] + PiTriplet[2] SU2FS[mu,nu,2] + PiTriplet[3] SU2FS[mu,nu,3]) - NHC eta/(32 Sqrt[3] Pi^2 fpi) Eps[mu,nu,rho,sig] (gw^2 (SU2FS[mu,nu,1] SU2FS[rho,sig,1] + SU2FS[mu,nu,2] SU2FS[rho,sig,2] + SU2FS[mu,nu,3] SU2FS[rho,sig,3]) + g1^2 BFS[mu,nu] BFS[rho,sig])]
```

### `LRhoff` (`:=`)

```mathematica
1/Sqrt[2] gV (rhop[mu] (vlbar.Ga[mu].ProjM.l + ubar.Ga[mu].ProjM.d + cbar.Ga[mu].ProjM.s + tbar.Ga[mu].ProjM.b) + rhopbar[mu] (lbar.Ga[mu].ProjM.vl + dbar.Ga[mu].ProjM.u + sbar.Ga[mu].ProjM.c + bbar.Ga[mu].ProjM.t)) + 1/2 gV rho0[mu] (vlbar.Ga[mu].ProjM.vl + ubar.Ga[mu].ProjM.u + cbar.Ga[mu].ProjM.c + tbar.Ga[mu].ProjM.t - lbar.Ga[mu].ProjM.l - dbar.Ga[mu].ProjM.d - sbar.Ga[mu].ProjM.s - bbar.Ga[mu].ProjM.b)
```

### `LRhoTriplet` (`:=`)

```mathematica
grho 1/2 I del[pip, mu] pipbar rho0[mu] - grho 1/2 I del[pipbar, mu] pip rho0[mu] - grho 1/2 I del[pip, mu] pi0 rhopbar[mu] + grho 1/2 I del[pi0, mu] pip rhopbar[mu] + grho 1/2 I del[pipbar, mu] pi0 rhop[mu] - grho 1/2 I del[pi0, mu] pipbar rhop[mu]
```

### `LTot` (`:=`)

```mathematica
LUVVLC + LKinCompositeScalars + LMExpanded + LKinTriplet + LKinK2 + LAnomalyTriplet + LAnomalyEta + LRhoff + LRhoTriplet
```

## The last failure the loop worked on

This is the validation report handed to the repair agent at the start of `repair2/round2` — the problem it was asked to fix. The model **passed** after this round; the report below is the state that was repaired, not the final one.

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
Non diagonal mass term found: (Acoup*eta*fpi*grho*K0bar*vev)/(2*Sqrt[3])
Non diagonal mass term found: (Acoup*fpi*grho*K0bar*pi0*vev)/2
Non diagonal mass term found: -((Acoup*fpi*grho*Kpbar*pip*vev)/Sqrt[2])
Non diagonal mass term found: (eta*fpi*grho*K0*vev*Conjugate[Acoup])/(2*Sqrt[3])
Non diagonal mass term found: (fpi*grho*K0*pi0*vev*Conjugate[Acoup])/2
Non diagonal mass term found: -((fpi*grho*Kp*pipbar*vev*Conjugate[Acoup])/Sqrt[2])
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (vev*y*Lmbar[Index[Spin, sp], Index[HCIndex, aa]] . ProjM . Nvlc[Index[Spin, sp], Index[HCIndex, aa]])/Sqrt[2] + (vev*yt*Lmbar[Index[Spin, sp], Index[HCIndex, aa]] . ProjP . Nvlc[Index[Spin, sp], Index[HCIndex, aa]])/Sqrt[2]
Warning: not numerical value encountered. Unable to decide whether mass term is diagonal
Non diagonal mass term found: (vev*Conjugate[y]*Nvlcbar[Index[Spin, r$3285], Index[HCIndex, aa]] . ProjM . Lm[Index[Spin, r$3285], Index[HCIndex, aa]])/Sqrt[2] + (vev*Conjugate[yt]*Nvlcbar[Index[Spin, r$3287], Index[HCIndex, aa]] . ProjP . Lm[Index[Spin, r$3287], Index[HCIndex, aa]])/Sqrt[2]
```

## FeynRules / Wolfram Engine output (tail)
```
rentz, Ext[1]]] . Lm[Index[Spin, SP$1], Index[HCIndex, 2]] + Lmbar[Index[Spin, SP$1], 3] . Ga[Index[Lorentz, Ext[1]]] . Lm[Index[Spin, SP$1], Index[HCIndex, 3]]" cannot be used for a symbol name. A symbol name must start with a letter followed by letters and numbers.

Symbol::symname: The string "ISUMObjectaI7[Index[Lorentz, Ext[1]]]L0bar[Index[Spin, SP$1], 1] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . L0[Index[Spin, SP$1], Index[HCIndex, 1]] + L0bar[Index[Spin, SP$1], 2] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . L0[Index[Spin, SP$1], Index[HCIndex, 2]] + L0bar[Index[Spin, SP$1], 3] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . L0[Index[Spin, SP$1], Index[HCIndex, 3]]" cannot be used for a symbol name. A symbol name must start with a letter followed by letters and numbers.

General::stop: Further output of Symbol::symname will be suppressed during this calculation.
From kernel 5 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 6 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 7 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 8 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.
From kernel 5 (Local):
Table::iterb: Iterator {Index[Lorentz, Ext[1]], IndexRange[Index[Lorentz]]} does not have appropriate bounds.

General::stop: Further output of Table::iterb will be suppressed during this calculation.
Flavor expansion of the vertices distributed over 8 cores: Dynamic[FR$Count1] / 176
   - Saved vertices in InterfaceRun[ 1 ].

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Y not conserved in vertex {eta, G0, K0bar}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!
Quantum number Y not conserved in vertex {eta, H, K0bar}.

QN::NonConserv: Warning: non quantum number conserving vertex encountered!

General::stop: Further output of QN::NonConserv will be suppressed during this calculation.
Quantum number Q not conserved in vertex {eta, GP, Kpbar}.
Quantum number Y not conserved in vertex {eta, GP, Kpbar}.
Quantum number Y not conserved in vertex {G0, K0bar, pi0}.
Quantum number Y not conserved in vertex {H, K0bar, pi0}.
Quantum number Q not conserved in vertex {GP, Kpbar, pi0}.
Quantum number Y not conserved in vertex {GP, Kpbar, pi0}.
Quantum number Q not conserved in vertex {G0, Kpbar, pip}.
Quantum number Y not conserved in vertex {G0, Kpbar, pip}.
Quantum number Q not conserved in vertex {H, Kpbar, pip}.
Quantum number Y not conserved in vertex {H, Kpbar, pip}.
Quantum number Y not conserved in vertex {GP, K0bar, pipbar}.
Quantum number Y not conserved in vertex {eta, G0, K0}.
Quantum number Y not conserved in vertex {eta, H, K0}.
Quantum number Q not conserved in vertex {eta, GPbar, Kp}.
Quantum number Y not conserved in vertex {eta, GPbar, Kp}.
Quantum number Y not conserved in vertex {G0, K0, pi0}.
Quantum number Y not conserved in vertex {H, K0, pi0}.
Quantum number Q not conserved in vertex {GPbar, Kp, pi0}.
Quantum number Y not conserved in vertex {GPbar, Kp, pi0}.
Quantum number Y not conserved in vertex {GPbar, K0, pip}.
Quantum number Q not conserved in vertex {G0, Kp, pipbar}.
Quantum number Y not conserved in vertex {G0, Kp, pipbar}.
Quantum number Q not conserved in vertex {H, Kp, pipbar}.
Quantum number Y not conserved in vertex {H, Kp, pipbar}.
Quantum number Q not conserved in vertex {GP}.
Quantum number Q not conserved in vertex {GPbar}.
Quantum number Q not conserved in vertex {A, pip, W}.
Quantum number Q not conserved in vertex {A, pipbar, Wbar}.
Quantum number Q not conserved in vertex {pip, W, Z}.
Quantum number Q not conserved in vertex {pipbar, Wbar, Z}.
Quantum number Q not conserved in vertex {A, K0bar, Kp, W}.
Quantum number Q not conserved in vertex {K0bar, Kp, W}.
Quantum number Q not conserved in vertex {pi0, pip, W}.
Quantum number Q not conserved in vertex {A, A, pip, W}.
Quantum number Q not conserved in vertex {A, pip, W, Z}.
Quantum number Q not conserved in vertex {A, K0, Kpbar, Wbar}.
Quantum number Q not conserved in vertex {K0, Kpbar, Wbar}.
Quantum number Q not conserved in vertex {pi0, pipbar, Wbar}.
Quantum number Q not conserved in vertex {A, A, pipbar, Wbar}.
Quantum number Q not conserved in vertex {A, pipbar, Wbar, Z}.
Quantum number Q not conserved in vertex {K0bar, Kp, W, Z}.
Quantum number Q not conserved in vertex {pip, W, Z, Z}.
Quantum number Q not conserved in vertex {K0, Kpbar, Wbar, Z}.
Quantum number Q not conserved in vertex {pipbar, Wbar, Z, Z}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/254 .
    - Writing files.
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
Command "import /private/tmp/repair_bench2/VLC_LN/round1/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_bench2/VLC_LN/round1/UFO" with error:
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
models.import_ufo.InvalidModel: name WL define multiple time. Please correct the UFO model!

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
Updated `model.fr` in place: changed eta-prime’s UFO particle name from `eta'` to `etaP` to stop the generated Python string/object-name breakage, and replaced raw `Wi`/`FS[Wi]`/`FS[B]` usage in the exported electroweak scalar kinetic and anomaly terms with explicit physical-field component helpers for `W`, `Wbar`, `A`, and `Z`, preventing unevaluated `Wi` symbols from leaking into UFO vertices. `LTot` remains the final top-level assignment and still uses only defined BSM terms; I could not rerun the full validation because `wolframscript` is installed but has no configured Wolfram kernel path.

Validation outcome AFTER that change: status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, mg5_python_traceback, compile_seconds=76.2

## For reference — the ORIGINAL model's outcome before any repair:
status=compiled, hermiticity=True, kinetic=True, mass=True, madgraph_import=False, tags=mg5_import_fail, ufo_python_syntax_error, mg5_python_traceback, mg5_invalid_cmd, compile_seconds=82.8

## Physicist sign-off

- Reviewed by: ______________________  Date: ____________
- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject
- Notes:
