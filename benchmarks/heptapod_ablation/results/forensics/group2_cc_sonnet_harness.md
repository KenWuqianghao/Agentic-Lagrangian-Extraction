# cc_sonnet_harness: failure forensics (16-paper run, 2026-09-30)

Read-only analysis. No kernel, MadGraph or agent was run. `R/<paper>` = `/home/deck/code/heptapod/eval/benchmark_runs/<paper>/rerun/cc_sonnet_harness/s1`. `cK` = `validation/call<K>`.
Each statement has a tag: **[OBS]** = quoted from a file, **[INF]** = my inference from observed facts (not tested by a run).

## Cross-paper findings (read these first)

1. **[OBS] The pSPSS pass has no heavy-neutrino vertex in the UFO.** `R/pSPSS/c10/round0/UFO/vertices.py` has 0 vertices with `P.n4` or `P.n5`; `couplings.py` has 0 `VlN` couplings (36 at call 9). The check passed because the terms disappeared (`terms=532` -> `terms=496`), not because they became hermitian.
2. **[OBS] The NJLComposite "pass at call 6" is an 8-line probe file**: `LTotal := LSM;` with no classes. Calls 5-8 are bisection probes, not candidate models.
3. **[OBS/INF] A class declared outside `M$ClassesDescription` is silently ignored.** GeneralU1 puts `S[11] == {ClassName -> Phi ...};` at top level in all 8 compiled calls; this is the kinetic_diagonal failure. 331 had the same defect in calls 2-3 and the same symptom; it went away when the block moved into the list.
4. **[OBS] The mass_spectrum report gives no rows.** The driver writes `detail=` empty; `agent_report.md` has 0 occurrences of `derived` or `ghW` (331 c3/c8/c9/c10, ALRM maxout c9). The rows are in `compile.log` only.
5. **[OBS/INF] Ghost masses fail after a correct Phi override.** 331 and ALRM maxout: only `ghWp/ghWm/ghZ` disagree at the end. Cause is SM.fr `LGhost` (`doublet = {..., Phi[2]} /. MR$Definitions /. vev -> 0`): a redeclared `Phi[2]` with `v1` in place of `vev` is not set to zero.
6. **[OBS] The MadGraph tail shows the retry error, not the first error.** `UFOError : invalid syntax (object_library.py, line 268)` appears after MG5 `auto_convert_model`; `object_library.py` is byte-identical (md5 `f9a6cc89...`) to the one in a passing run. The first error (`name MH2 define multiple time`) is in `MG5_debug` only.
7. **[OBS] Lint was silent on every root cause below** except SLQrules `ambiguous_total` (calls 5-6). `l[ff]` (pSPSS, SMWeinberg), `uqbar[3, cc]` (MDMmodel), shared `BlockName` (Monotops), missing `ClassMembers` (331, NJL), stray class (GeneralU1), `{NP,-1}` (MDMmodel): no finding.

---

## SLQrules — compile fails in 10 of 10 calls

1. **Root cause: not determined from the logs.** [OBS] `R/SLQrules/c10/round0/compile.log:28` `Thread::tdlen: Objects of unequal length in {} + {4 Index[SU2W, PRIVATE`a$18652]} + {4 Index[SU2W, PRIVATE`a$18654]} + {Index[SU2W, ...], Index[SU2W, ...]}` then `TerminatedEvaluation[RecursionLimit]`. The log stops before `[INFO] Lagrangian:`, so the failure is in the driver's `ExpandIndices[LTotal]`.
   - [OBS] The message is identical in calls 1, 2, 3, 4, 9, 10. Ruled out by the agent's own edits: the `Phi3` class with `Index[SU2W]` (removed at call 3), `Wi[mu,3]` (removed at call 4), the full quartic sector (removed from `LTotal` at call 10). At call 10 `SU2W` occurs in comments only.
   - [INF, leading candidate, not tested] `LQKin` / `LQKinPhi3` use `DC[Phi1bar,mu][cc] DC[Phi1,mu][cc]`, `DC[Phi2bar,mu][ii,cc] ...` (5 uses at c1, 10 at c4-c10). SM.fr uses `DC[Phibar[ii],mu]`. FeynRules `Core/Initialisation.m:390` evaluates `DC[field_, mu_]` for a bare class name, so `[cc]` is applied to a `Plus[...]`. This form is in all 10 snapshots; no other arm has this error (`grep tdlen` hits only this arm).
2. **Report: symptom only.** It shows the two log lines. No block, no line number.
3. **Lint: no.** Findings were `explicit_flavour_sum (line 384)` and `mixing_in_definitions`; none on `DC[...][...]`.
4. **Agent response.** c2: hand-written Phi3 kinetic term (kept `DC[X,mu][cc]`). c3: removed the SU2W class (228 lines). c4: `Wi[mu,3]` -> `cw Z + sw A`. c5-c8: four bisection attempts on the quartic sector, **all rejected before compile** as `no_lagrangian_symbol` ([OBS] `c5/summary.json`: `"roots": ["LQQuartic", "LTotal"], "ambiguous": true`; the report says "It found none"). c9: restored. c10: quartic removed, same error. Not fixed. Final text blames the environment ("not a defect I could locate in `model.fr`").
5. **Compile type: crash, not timeout.** [OBS] `timed_out=False`, `exit=0`, 41.5-61.3 s. Calls 5-8: no kernel run (`seconds=None`, 0.012 s).

## 331 — final: mass_spectrum fail + MadGraph fail

Distinct failures, in order:
- **c1 compile abort (16.4 s, exit 0, not timeout).** [OBS] `LoadModel::PartName: The number of particles names for MG must correspond to the number of particles in the clas.` Cause [OBS diff c1->c2]: class `lHE` had 3 particle names and no `ClassMembers -> {EHe,EHm,EHt}`. Report: symptom only (no class name). Lint: no. Fixed at c2.
- **c2-c3 kinetic_diagonal.** [OBS] `Non diagonal kinetic term found: c12 s12 del[G0, ...] del[H0, ...]`. Cause: `S[11] == {ClassName -> Phi...}` at top level (c2 line 313, list closes at 310; 0 `Doubly defined` warnings). Moved into the list at c4 (7 warnings); check passes from c5. Report: symptom + generic "MAY be benign" text. Lint: no.
- **c3-c4 hermiticity (Zp quark vertices).** [OBS] `(QZpQmat[1,2] - QZpQmat[2,1])`: a tensor parameter with zero off-diagonal entries that FeynRules keeps symbolic. Report named vertices, `block: LZpCurrent` (c3), `not located` (c4). Agent response at c5: replaced the matrix by one averaged coupling, [OBS] `"the paper's genuine non-universality (Q12 vs Q3) is dropped here for tractability"`. This weakens the physics; it is still in the final model (line 194-198).
- **c4-c7 compile timeout.** [OBS] `timed_out=True`, `exit=-1`, 900.1-900.2 s. Successful compiles take 713.6-807.7 s, so the margin is ~90 s. c5/c6: all three checks had passed, then killed. [OBS] c5->c6 diff is 0 lines: one call re-ran an identical file. c7 is different: [OBS] `Part::partw: Part 4 of {Index[SU2D], Index[Generation], Index[Colour]} does not exist` from a fermion-like class declared as `S[113]`; fixed to `F[113]` at c8. Report: "TIMED OUT ... may need simplification"; no time per stage.
- **c8 MadGraph.** `V_345` malformed. [OBS] compile.log `{{EHmbar, 1}, {EHm, 2}, {Zp, 3}}` with `Ga[..., SP$1, SP$1]`: from `lHEbar[sp,ff].Ga[mu,sp,sp].lHE[sp,ff]`. Report named `V_345` and pointed at line 309 (Zp declaration) and unrelated `Sqrt` lines: wrong lines. Agent still fixed it at c9 (`lHEbar.Ga[mu].lHE`).
- **c9 MadGraph.** [OBS] report: `UFO/parameters.py line 143, object bpar ... value = 1/Sqrt(3)` + `line 81 (declaration)`. Named exactly; fixed at c10.
- **c10 + final MadGraph.** [OBS] `mg5.log:80`-area `InvalidModel: name MH2 define multiple time`. [OBS] `UFO/parameters.py` has 14 names twice (MH2, MH3, MH0, MHp, MHqy, MHqv, MQD, MQS, MQT, MEH, MZp, MYb, MVpr, WEH). Cause [INF]: the mass is declared in `M$Parameters` (line 103 `MH2 == {ParameterType -> External...}`) and again by the class (`Mass -> {MH2,1500.}`, line 216). The report named the UFO object (in the raw `MG5_debug` block, first seen at c10), not the model lines. No call left.
- **mass_spectrum (c8, c9, c10, final).** [OBS] `c10/round0/compile.log`:
  `HEPTAPOD-MASS|particle=ghWm|derived=94.65634075707756|declared=79.82435974619784|agrees=False`
  `HEPTAPOD-MASS|particle=ghWp|derived=94.65634075707756|declared=79.82435974619784|agrees=False`
  `HEPTAPOD-MASS|particle=ghZ|derived=108.13095859289017|declared=91.1876|agrees=False`
  All other rows agree (W 79.824, Z 91.1876, t 172, b 4.7, new states). [INF] (94.656/79.824)^2 = 1.406 = (vev + v1)/vev with v1 = 100: finding 5. At c3 (no override yet) the ghosts agreed and `d, s, t, W, Z` disagreed (t derived 423.5; W 108.13) — a different, earlier defect, fixed by c8.
  Report: [OBS] one sentence, no rows. Agent's final text: `"mass_spectrum still fails (magnitude unknown — the diagonstic detail wasn't returned in the last report)"`.

## GeneralU1 — final: kinetic_diagonal fail

1. **Root cause.** [OBS] `R/GeneralU1/c10/model.fr:271` `S[11] == {` ... `Definitions -> { Phi[1] -> -I GP, Phi[2] -> (vev + ca*H - sa*h2 + I G0)/Sqrt[2] }` `};` is a top-level statement. `M$ClassesDescription` closes at line 81. Same in calls 3-10. [OBS] compile.log has 0 `Doubly defined particle classes` warnings (B-L-SM, where the override works, has 7). [INF] The redeclaration has no effect; `Phi` keeps SM.fr's `(vev + H + I G0)/Sqrt[2]`; the doublet gives no H-h2 cross term; the singlet term gives `+ca sa`.
2. **Exact text (item 6).** [OBS] `Non diagonal kinetic term found: ca sa del[H, Index[Lorentz, mu]] del[h2, Index[Lorentz, mu]]` (calls 3-9; index `nu` at c10). The coefficient is a product of mixing-angle parameters, but it is **not a symbolic false positive**: a false positive has the form `(ca^2 + sa^2 - 1)`. Here the two cross terms (`-ca sa` doublet, `+ca sa` singlet) cancel for every angle if both are present. It is also **not a kinetic-mixing term of the paper**. It is a real defect of the file.
3. **Report: symptom only.** The term is quoted. The text says a mixing-angle coefficient "MAY be benign" and to check "if the term that should have cancelled it is absent altogether" — correct direction, no pointer to `Phi`.
4. **Lint: no.** c10 lint has 1 finding, `explicit_index_in_dc (line 290)`. [OBS] `sm_class_redeclared` is absent; in 331 it appears only after the class is inside the list. Its absence was the signal, and nothing reported it.
5. **Agent response.** Six rewrites of the *singlet* term (c3-5 `PhiS` class; c6 by hand; c7 `Expand[]`; c8 inside `ExpandIndices`; c9 `DC[PhiS,mu]`; c10 separate block + `Simplify`). All off target. Not fixed. Final text: "all producing the identical uncancelled residual".
6. **Earlier failures.** c1-c2 compile abort, 17.8 / 15.7 s, exit 0: [OBS] `LoadModel::Mass: Wrong mass assignment.` (c1: `{MN1,Internal}` in a mass list; c2: missing `ClassMembers -> {n1,n2,n3}`). Fixed at c3. c3 hermiticity (`yNmat` complex Majorana Yukawa) fixed at c4. mass_diagonal fixed at c6.

## SMWeinberg — hermiticity fail in 10 of 10 calls

1. **Vertices (item 7).** [OBS] The same 16 vertices are in calls 1-7 and 10: `G0,GP,Nmaj,l` / `GP,H,Nmaj,l` / `GP,Nmaj,l` / 5 x `(G0|H),Nmaj,vl,vlbar` / `GP,lbar,l` / 3 x `GPbar,...,lbar,Nmaj` / `GPbar,lbar` / `W,Nmaj,l` / `Wbar,lbar,Nmaj` / `Z,Nmaj,vl,vlbar`. All 16 have a non-empty `unreduced=` field. All are in the one block `LNint` (the model has only `LNkin` and `LNint`, so the block name does not localise).
2. **Root cause, layer 1: unreduced chains, not missing HC.** [OBS] `c1/model.fr` `Nmajbar.Ga[mu].ProjM.l[ff]` with `ExpandIndices[dl + HC[dl], ...]`: `+ HC[...]` **is present**. [OBS] c5 (`Sum[..., {ff,1,3}]`) gives `Nmaj . ProjM . (l[Index[Spin, 1]] + l[Index[Spin, 2]] + l[Index[Spin, 3]])`: the one index `ff` is in the **spin slot** of `l`. Same construct as pSPSS.
3. **Layer 2: truly non-hermitian terms, seen only in c8-c9.** With index-free fields (c9, per-flavour, no `HC[]`) the vertices reduce, and 47 remain. [OBS] `fields=Nmaj,e,W|unreduced=|expr=(I*ee*TensDot[Ga[...], Ga[5]]...)/(Sqrt[2]*sw)`: a gamma5 residual. [INF] The hand-written conjugate is `ebar.Ga[mu].ProjP.Nmaj`; the conjugate of `Nmajbar.Ga[mu].ProjM.e` is `ebar.Ga[mu].ProjM.Nmaj`. Also [OBS] `Nmaj,e,GP` residuals with `ProjM` from the `CC[e].ProjM.Nmaj` terms; cause of these: not determined.
4. **Report.** Named the cause class: [OBS] `UNREDUCED: FeynRules could not strip Nmaj, l ... The usual cause is an explicit spin or flavour index on the spinors of that chain (see lint rule explicit_spin_in_chain); write the chain with implicit indices`. It did not say that `l[ff]` puts `ff` in the spin slot. The header still says "The usual cause is a term without its `+ HC[...]` partner".
5. **Lint: no.** [OBS] `lint: no findings` in calls 1, 8, 10 (the report cites a lint rule that did not fire).
6. **Agent response.** c2-c4: conjugate order and `CC[]` forms. c5-c6: explicit `Sum`. c7: coupling vector `kl[ff]`. c8-c9: index-free fields (on target for layer 1) but with hand-written conjugates in place of `HC[]`, which exposed layer 2. c10: went back to `l[ff] kl[ff]` (16 uses). Never tried index-free fields **with** `HC[dl]`. Not fixed. Final text calls it "a known-class FeynRules kernel limitation".

## ALRM_general — no model

- **Original arm.** [OBS] `R/ALRM_general/run.json` `ok: False`; `agent_out.md`: `API Error: Claude's response exceeded the 64000 output token maximum`. [OBS] stream `result`: `num_turns: 9`, `outputTokens: 281778`, `thinkingTokens: 281063`; last iteration `output_tokens: 64000`. Tool calls: 4 x `Read`, 1 x `Glob`; **no `Write`**. Root cause: one response used the full 64k cap on thinking before the first file write. No report, no lint, no Stop event.
- **`cc_sonnet_harness_maxout`** (`.../rerun/cc_sonnet_harness_maxout/s1`). c1-c8 compile fail, 18-26 s, exit 0, not timeout: [OBS] `Power::infy: Infinite expression 1/0 encountered`, `HEPTAPOD-LAGRANGIAN|...|terms=0`, `$Aborted`. The construct that gives `1/0`: **not determined** (the report shows the message only; lint has 8 unrelated findings). Cleared at c9 by a 123-line cut (removed `th23`, `thA2`, `phA2`, `szeta/czeta`, `ydN`, unphysical doublets). c9 mass_spectrum: [OBS] `ghWm derived=112.237 declared=79.824`, `ghZ 128.21 vs 91.19`, `W 77.987 vs 79.824`, `Z 89.089 vs 91.188`, and `b, d, s derived=If[Im[NumericalValue[Md]] ...` (unevaluated). c10: [OBS] `Syntax::com ... (line 200 of model.fr)`: a trailing comma before `};` after the last parameter (87.4 s, exit 0). File edited again after c10; never validated.

## pSPSS — pass at call 10 (10 calls)

1. **Root cause of calls 1-7, 9.** [OBS] `c1/model.fr:211` `n4bar.Ga[mu].ProjM.l[ff]` (and `vl[ff]`): `ff` fills the spin slot. Same 4 unreduced vertices in every call: `H,vlbar,n4,n5,vl` / `W,n4,l,n5` / `Wbar,lbar,n4,n5` / `Z,vlbar,n4,n5,vl`. `+ HC[...]` present from c1.
2. **Report.** UNREDUCED text as for SMWeinberg (cause class named, with the term as `vlbar[Index[Spin, a]]`). The MadGraph section was specific: [OBS] c2 `UFO/couplings.py line 690, object GC_170` ... `line 202 (use): -gw/Sqrt[2] (VlN4[ff] n4bar.Ga[mu].ProjM.l[ff] + ...) W[mu]` and `Vertex particles using this coupling: W__plus__` (a one-particle vertex).
3. **Lint: no.** `lint: no findings` in calls 1, 5, 7, 9, 10.
4. **Agent response.** c2-c4: moved `ExpandIndices` / split terms. c5: swapped order (`lbar[ff]...n4`). c6: hand-written conjugate with `ProjP`. c7: `CC[n4][sp]` with explicit `sp`. c8: `VlN4c` parameters; compile fail 17.4 s, exit 1 ([OBS] `Syntax::com ... line 135`: stray comma). c10: one named block per half-term, each in its own `ExpandIndices`. **`l[ff]` is still in the passing file** (`c10/model.fr:222-238`).
5. **Why it passed.** [OBS] `terms=496` (532 before); UFO vertices 163 (199 before); the 36 lost are the `[ P.H ]` x12, `[ P.W__minus__ ]` x6, `[ P.W__plus__ ]` x6, `[ P.Z ]` x12 one-particle vertices. No n4/n5 vertex exists in any call's UFO. Why the terms evaluate to nothing at c10: not determined. The referee read the `.fr` text and did not see this (`review/review1.md`: "heavy-sector mixing ... correctly implemented").

## NJLComposite — pass at call 10 (10 calls)

1. **Calls 1-5, 7: real compile aborts, not timeouts.** [OBS] 15.3-18.6 s, `timed_out=False`, `exit=0`, tag `wolfram_aborted`; `LoadModel::PartName: The number of particles names for MG must correspond to the number of particles in the clas.` Cause [OBS `c1/model.fr:61-73`]: class `N1` with `Indices -> {Index[Generation]}`, `ParticleName -> {"n1e","n1m","n1t"}` and no `ClassMembers` (0 `ClassMembers` in any snapshot). c3 also had `Syntax::com ... line 173`.
2. **Why it continued after call 6.** Snapshot sizes: 332, 332, 228, 332, **37, 8, 26, 23**, 332, 316 lines. c6 is `LTotal := LSM;` only: a probe to see if the harness worked at all. c7 = probe with one 3-generation fermion class (fails: confirms the cause). c8 = probe with one scalar class (passes). So c6/c8 passes are empty probes and c7 is a real, intended failure. 4 of 10 calls were spent on probes.
3. **c9: real MadGraph failure.** [OBS] `InvalidModel: name MPi define multiple time` (mass in `M$Parameters` and in `Mass -> {MPi, ...}`; same mechanism as 331). The report's `MG5_debug` block named `MPi`; fixed at c10 by deleting the `MPi` / `MPiLQ` parameter entries.
4. **Report / lint for the abort.** Symptom only (log line, no class). Lint: 3 unrelated findings.
5. **Fix.** At c9 the agent removed the generation index instead of adding `ClassMembers`: [OBS] `c10/model.fr:6` "representative first generation; see note at bottom on the multi-generation scope cut". `FlavorIndex` count 14 -> 4. The pass is for a one-generation model.

## MDMmodel — in-loop pass at call 9, final edit unvalidated (10 calls)

1. **c1, c2, (c3-c6), c7, c8 MadGraph.** [OBS] `mg5.log`: `InvalidModel: Some couplings have '1' order.` [OBS] `c1/round0/UFO/couplings.py:68-70` `GC_15 ... value = '-(ca*complex(0,1)*fS*kappa)', order = {'1':1}` (6 such couplings). Cause [OBS `c1/model.fr:44-47`]: `fS == { ... InteractionOrder -> {NP, -1}` with `kappa` at `{NP, 1}`: net order 0. Fixed at c9 by deleting that one line (3-line diff).
2. **Report.** Symptom only: the MG sentence in the raw `MG5_debug` block; no `GC_15`, no model line. The compile log had `Warning: Non positive interaction order` (shown, not linked). Lint: no (4 unrelated findings).
3. **Agent response.** c2: other edits. c3-c6: added matrix Yukawas `dyHttMat` -> new hermiticity failures ([OBS] `Conjugate[dyHttMat[2,2]] - dyHttMat[2,2]`, later `dyHttMat[1,2] - dyHttMat[2,1]`: symbolic tensor entries), a 4-call detour. c7: removed them. c9: pass.
4. **c10.** Agent added the t-t' term back as `- dyHtt H uqbar[3, cc].uq[3, cc]` (`c10/model.fr:278`): numeric `3` in the spin slot. [OBS] `mg5.log:63` `WrongFermionFlow: Not coherent Incoming/outcoming fermion flow`, masked by MG5's own `NameError: name 'helas' is not defined`. The report shows the `NameError` only (0 hits for `WrongFermionFlow`). Lint `numeric_spin_slot` did not fire. Final file = c9 + a comment (3-line diff): the paper's Eq. 15-16 correction is not in the scored model.

## Monotops — pass at call 6 (5 x MadGraph fail)

1. **Root cause.** [OBS] `c5/model.fr:145-304`: every indexed External parameter has `BlockName -> MTOPCPL` (14 uses), no `OrderBlock`. [OBS] `c5/round0/UFO/parameters.py`: 12 names are duplicated (`aHVR1` is written 6 times), e.g. `aHVR1 ... lhablock 'MTOPCPL', lhacode [ 1 ]`. MG: `InvalidModel: name b12VR1 define multiple time` (c1), `bHVR1` (c2-c4), `aHVR1` (c5): always the tensor declared last.
2. **Report.** Named the UFO object in the raw `MG5_debug` block. Did not say the cause (shared block) or a model line. Lint: `no findings`.
3. **Agent response.** c2: renamed parameters (`a0FC` -> `aFCs`). c3: `Base + HC[Base]` rewrite ("to avoid duplicate UFO declarations"). c4: symmetrised bilinears. c5: swapped declaration order of `aHVR`/`bHVR` — the error then named `aHVR1`, which showed it follows the last declaration. c6: one `BlockName` per tensor (`MTOP01`, `MTOP02`, ...): pass. Four off-target calls, fixed at c6.

---

## Summary table

| paper | failing stage | root cause (1 line) | report named it? | lint named it? | agent fixed it? (call #) | information that was needed |
|---|---|---|---|---|---|---|
| SLQrules | compile (crash, 41-61 s, exit 0) | not determined; candidate [INF] `DC[Phi1bar,mu][cc]` form in `LQKin` (all 10 snapshots) | symptom-only | no | no | which named block fails in `ExpandIndices` (per-block evaluation); permission to bisect (4 calls lost to `no_lagrangian_symbol`) |
| 331 (mass_spectrum) | checks | SM `LGhost` + redeclared `Phi` with `v1`: ghost masses x sqrt((vev+v1)/vev) | symptom-only (no rows) | no | no | the 3 `HEPTAPOD-MASS` rows; note that ghosts come from `LGhost` |
| 331 (MadGraph) | mg5 | masses declared in `M$Parameters` and in class `Mass -> {MH2,...}` -> `name MH2 define multiple time` | symptom-only (UFO name, raw traceback, first at call 10) | no | no (seen at last call) | first MG error instead of retry error; model lines 103 + 216 |
| 331 (timeouts c4-c7) | compile timeout (900 s, exit -1) | compile needs ~805 s of a 900 s limit; c7 also `S[113]` for a fermion class | symptom-only | no | yes (8), by dropping Z' non-universality | time per stage; higher limit |
| GeneralU1 | checks: kinetic_diagonal | `S[11] == {... Phi ...};` outside `M$ClassesDescription`: override ignored; residual `ca sa del[H] del[h2]` is real | symptom-only | no | no | "class Phi was not redeclared (0 merge warnings)"; which block gives the cross term |
| SMWeinberg | checks: hermiticity | `l[ff]` / `vl[ff]`: `ff` in the spin slot -> 16 unreduced vertices; behind it, hand-written conjugates with `ProjP` | yes, as a class ("explicit spin or flavour index"); not the slot | no | no | "`l[ff]` = `l[Index[Spin, ff]]`; write `l` and keep `HC[dl]`" |
| ALRM_general | no model | one response used 64000 output tokens on thinking before any `Write` | n/a | n/a | no | larger cap, or a rule to write the file in parts |
| ALRM (maxout) | compile, then mass_spectrum + mg5 | `1/0` in `LTotal`: not determined; then ghost masses, W/Z off 2.3 %, unevaluated `Md` | symptom-only | no | partly (9) by deleting 123 lines | which block gives `1/0`; mass rows |
| pSPSS | hermiticity x8, then pass | `l[ff]` spin slot; pass at 10 only because the 36 n4/n5 terms vanished from the UFO | yes, as a class; MG section showed line 202 | no | no — vacuous pass (10) | same as SMWeinberg; a check that new particles have vertices |
| NJLComposite | compile abort x6 (15-19 s), mg5 x1 | 3-generation class without `ClassMembers`; then `MPi` declared twice | symptom-only; `MPi` named at c9 | no | yes (9-10), by cutting to one generation | class name + "add `ClassMembers`"; a free bisection path |
| MDMmodel | mg5 x5 (+4 hermiticity detour) | `fS` with `InteractionOrder -> {NP,-1}` -> coupling `order = {'1':1}`; c10: `uqbar[3, cc]` | symptom-only | no | yes (9); c10 regression reverted without a call | coupling `GC_15` + parameters `fS`, `kappa` and their orders; `WrongFermionFlow` line |
| Monotops | mg5 x5 | all tensor parameters share `BlockName -> MTOPCPL` -> duplicated UFO parameters | symptom-only (UFO name) | no | yes (6) | "N tensors share one LHA block"; lines of the `BlockName` entries |
