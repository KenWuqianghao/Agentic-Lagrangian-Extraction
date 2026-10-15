# What to change in heptapod, ranked

Source: heptapod-dev `origin/main` at 26ca74b (v2.16.0), read only, compared
with the stored `cc_sonnet_harness` and `pi_qwen_harness` runs. The scoring
driver (4bcbcf2) and `origin/main` have the same `tools/feynrules`,
`tools/frgen` and `tools/ufo` (the diff is empty), so a statement about the
scorer's driver is a statement about the released one.

Labels: **RUN** = confirmed by a run of the chain on this machine on
2026-10-06 (files named). **STORED** = read from the stored logs by a script
or a quoted line. **INFERRED** = not tested.

"Flips" is the number of the 16 papers that the change can move to the
primary endpoint of `DESIGN.md` (chain pass, clean referee, every new
particle in a vertex). The stored harness run has 7 of 16 on that endpoint.
Every flip count is an estimate from one seed.

## The nine papers that miss the endpoint, and why

| paper | stored result | cause | label |
|---|---|---|---|
| Monotops | chain pass, referee clean | no new particle has a vertex: the UFO has the Standard Model's 163 vertices. Quark fields written with two of three indices (`uqbar[ff, cc]`) | STORED (`score` UFO of call 6) |
| pSPSS | chain pass, referee: 1 physics-changing | no vertex has `n4` or `n5`. `l[ff]`: one index on a two-index field goes to the spin slot | STORED |
| SMWeinberg | hermiticity fails in 10 of 10 calls | the same `l[ff]`; 16 unreduced vertices | STORED |
| MDMmodel | chain pass, referee: 2 physics-changing | 8 calls on a coupling of order `'1'` (`InteractionOrder -> {NP, -1}`); then `uqbar[3, cc]` broke the import and the agent removed the paper's term | STORED |
| NJLComposite | chain pass, referee: 2 physics-changing | a three-generation class without `ClassMembers` aborts the load with no class named; 4 of 10 calls were probe files; the agent cut the model to one generation | STORED |
| GeneralU1 | kinetic_diagonal fails in 8 calls | the `Phi` redeclaration is a statement after `M$ClassesDescription`, not an entry in it: FeynRules ignores it | RUN (`results/GeneralU1_class_inside.json`, `sm_override/` E) |
| 331 | mass_spectrum and import fail | ghost masses after a `Phi` override with a second vev; 14 masses declared twice; compile at 805 s of a 900 s limit | STORED (mass rows), INFERRED (ghost mechanism) |
| SLQrules | compile fails in 10 of 10 calls | `RecursionLimit` in `ExpandIndices`; one of 19 blocks fails alone, `LQKin` (`DC[Phi1bar, mu][cc]`) | RUN for the block (`results/compile_bisect_SLQrules.json`); INFERRED for the construct |
| ALRM_general | no model | the response hit the 64000-token output cap before the first write | STORED; not a heptapod matter |

## Changes in heptapod (upstream)

### 1. A gate for "the new physics is not in the UFO"

- Evidence. STORED: the chain passes Monotops and pSPSS (Sonnet) and
  Monotops and Top-Philic-Zprime (Qwen) with new particles that no vertex
  contains. 2 of the 11 stored harness passes and 2 of the 4 stored pi passes
  are of this kind. The referee did not see it: it reads the `.fr`.
- What exists. `FeynRulesToUFO` and `ValidateUFOModel` return
  `vertex_inventory` with a `new_physics` count, and `ValidateUFOModel` says
  "No interaction content is verified". The data is there; nothing fails.
- Change. In `ValidateUFOModel`, add a check `new_particles_interact`: every
  declared new particle is in at least one physical vertex; fail and name
  the particles otherwise. In the driver, print the term count of each named
  block before and after index expansion, so a block that expands to nothing
  is named.
- Flips: 0 at once; it removes 2 false passes and turns them into failures
  the loop can work on. With change 2 it is the difference between "pass"
  and "model" for Monotops and pSPSS.
- Effort: half a day (the inventory is computed already); one test with a
  UFO whose new particle has no vertex. The ALE scorer needs the same check
  (2 hours; `retro.particles_without_vertex` is the prototype).

### 2. An index-count check for fermion fields

- Evidence. RUN (`results/HeavyN_partial_index.json`): the stored HeavyN
  model passes the full chain; with its charged current rewritten as
  `VlN[ff] Nhbar.Ga[mu].ProjM.l[ff]`, and nothing else changed, hermiticity
  fails, the import fails, and no vertex has `Nh` and `W`. The stored lint
  has no finding on that file. STORED, by `index_count_replay.py`: an SM fermion in a Dot chain
  with some but not all of its indices is in 35 of the 102 compiled in-loop
  snapshots of the two loop arms. 32 of the 35 fail hermiticity or have a
  vertex-less new particle; the other 3 are MDMmodel files whose import
  fails. The stored lint is silent on 31 of the 35. Papers: SMWeinberg,
  pSPSS, Monotops, MDMmodel (Sonnet); EffLRSM, MDMmodel, Monotops,
  SMWeinberg, Top-Philic-Zprime (Qwen).
- What exists. Nothing in heptapod: it has no lint for `.fr` text. Its
  skill does not mention the spin slot. The ALE lint has the rule for a
  numeric index only (`numeric_spin_slot`).
- Change. A preflight in `ValidateLagrangian` (pure Python on the `.fr`
  text, before the kernel starts): a field of a class with n indices, used in
  a Dot chain with 0 < k < n indices. Message: "`l[ff]` is
  `l[Index[Spin, ff]]`; write `l[s, ff]` or no index". One entry in
  `skills/feynrules/references/pitfalls.md`.
- Flips: up to 4 (SMWeinberg to a pass; pSPSS and Monotops from vacuous to
  real; MDMmodel keeps its term). A realistic count is 2: SMWeinberg has a
  second defect behind this one (hand-written conjugates), and MDMmodel has
  two more referee findings. INFERRED: no repaired paper model was run.
- Effort: one day, with a replay test on the stored snapshots.

### 3. Correct the SM-override text in the skill, and support the override

- Evidence. RUN, `sm_override/` (six models, `results.json`; each adds a free scalar H2 and tries to put it into the Higgs doublet):

  | model | what it does | H2 vertices | `H2 t t~` | hermiticity | MadGraph import |
  |---|---|---|---|---|---|
  | A | redeclares `S[11] Phi` inside `M$ClassesDescription` (the ALE protocol) | 38 | yes, `i sa yt/sqrt(2)` | pass | ok |
  | B | prepends `Phi[2]` rules, both stored forms, to `MR$Definitions` (the skill's route) | 35 | no | fail | ok |
  | C | neither (control) | 0 | no | pass | ok |
  | D | redeclares the SM parameter `lam` as External | 0 | no | pass | fails: "name lam define multiple time" (the value is the add-on's, written twice) |
  | E | A's block as a statement after the class list | 0 | no | pass | ok |
  | F | A, with `FeynmanGauge = False;` at the top of the add-on | 22 | yes | pass | ok; 97 vertices, 1 ghost vertex (A: 201 and 27) |

  E is the same UFO as the control, and it passes the full chain: a model
  whose override was ignored is not visible to any check.

  The skill (`skills/bsm_model_building/SKILL.md`, "Extending an existing
  model") says: "A class index or parameter name you re-declare does not
  override the existing one — the existing one was read first and it stays."
  With the driver's load order (`LoadModel[SM.fr, add-on]`) that is false for
  a class (A) and for a parameter (D). The route the skill gives instead,
  rules prepended to `MR$Definitions`, left the conjugate field on the SM
  rule in my implementation (B): the model is not hermitian and has no
  `H2 t t~` vertex. Another implementation of that route may work; this one
  shows that it is the fragile one.
  `pitfalls.md` P13 says a diagonality failure with a mixing-angle
  coefficient is a false positive and "Nothing to fix in the model". The
  scored chain fails such a model. With the inverted parametrisation the
  check passes symbolically (pNG and B-L-SM in the stored harness run).
- Change. Rewrite the section: redeclare the class inside
  `M$ClassesDescription`; write the total as `LSM - LHiggs + ...`; do not
  redeclare an SM parameter (use a new name); say what a class statement
  outside the list does (E). Add the inverted parametrisation next to P13.
  In the driver, report the count of "Doubly defined particle classes"
  warnings and the classes merged: zero when the file contains `S[11] ==`
  means the override did not apply. In `frgen`, an `sm_overrides` slot (the
  schema cannot express `Definitions` on an unphysical class now).
- Flips: 1 (GeneralU1). RUN: the stored GeneralU1 file with its `Phi` block moved into the class list, and no other change, passes the full chain here (215 s). The referee and the vertex check were not run on it.
- Effort: skill text half a day; driver line and test half a day; schema
  slot two days.

### 4. Say which block fails to compile

- Evidence. STORED: SLQrules never compiled (10 calls, 32.9M input tokens,
  $11.26); the agent spent 4 of the 10 calls on bisection files that the
  harness rejected. NJLComposite spent 4 of 10 calls on probe files to find
  a class without `ClassMembers`, then cut the model to one generation. 331
  and GeneralU1 lost their first calls to load errors that name no class.
  14 of the 91 stored validate calls ended in a compile failure that the
  log does not localise (8 "other", 6 `RecursionLimit`).
- What exists. The skill says to "compile pieces separately when something
  goes wrong". No tool does it, and each try costs a full call.
- Change. `ValidateLagrangian(localise=true)`: on a failure of the total,
  expand each named block alone and report the blocks that fail, with their
  first kernel message. For `LoadModel::` errors, name the class being
  loaded. Prototype: `compile_bisect.py`. RUN: on the stored SLQrules file it expands 19 blocks one at a time in about 4 minutes of kernel time (7 to 52 s each) and names one, `LQKin`, with the `Thread::tdlen` message; the other 18 expand. No repaired SLQrules file was run.
- Flips: 1 to 2 (NJLComposite with three generations; SLQrules). INFERRED.
- Effort: two days.

### 5. The mass spectrum and the gauge

- Evidence. STORED: 331 ends with three disagreeing rows, all ghosts (ghWm,
  ghWp 94.656 derived against 79.824 declared; ghZ 108.131 against 91.188).
  The agent's last message: "mass_spectrum still fails (magnitude unknown —
  the diagnostic detail wasn't returned in the last report)".
  RUN (`sm_override/` F): `FeynmanGauge = False;` at the top of an add-on
  takes effect with the driver's load order (SM.fr first). `pitfalls.md` P14
  says it does not work "when `SM.fr` is loaded after it"; in heptapod's own
  driver SM.fr is loaded before the add-on, so the entry misleads. That
  unitary gauge clears the 331 ghost rows is INFERRED.
- What exists. The driver prints `HEPTAPOD-MASS` rows and
  `lagrangian_checks.parse_mass_spectrum` returns them; the tools take
  `feynman_gauge`. So upstream is ahead of the ALE wrapper here: the wrapper
  drops the rows and never sets the gauge.
- Change, upstream: when the only disagreeing rows are ghosts or Goldstones,
  say so in the message and point at `feynman_gauge=false`.
- Flips: 1 (331), together with change 6; INFERRED.
- Effort: half a day.

### 6. Static checks of the UFO parameters, before MadGraph

- Evidence. STORED: "name X define multiple time" ended 13 validate calls in
  8 papers, and is the last import error of 331. Two causes: a mass in
  `M$Parameters` and again in the class (the skill's P1), and several tensor
  parameters on one `BlockName` (Monotops, 5 calls; the `frgen/schema-gaps`
  branch rejects it in the schema, not upstream). A coupling of order `'1'`
  (the skill's P2) ended 8 calls of MDMmodel.
- What exists. P1 and P2 are in the skill as text. `ValidateUFOModel`
  returns MadGraph's real error (from `MG5_debug`). No check names the model
  lines.
- Change. In `ValidateUFOModel`, before the import: duplicate names in
  `parameters.py` with the `.fr` lines that declare them; couplings with
  `order = {'1':1}` with their parameters and the orders of each.
- Flips: 0 to 1; it frees budget (13 + 8 of the 91 stored calls).
- Effort: one day.

## In the ALE wrapper, to move upstream

### 7. Located reports for hermiticity and the mass matrix

- Evidence. STORED, `RETRO.md`: all 4 hermiticity fixes and all 4
  mass_diagonal fixes of the stored harness run came after a report that
  located the failure (vertex and block, or the off-diagonal entry). The pi
  arm had the generic text only and ended with hermiticity failing in 4
  delivered models. This is an association in one seed, not an effect:
  design A of `DESIGN.md` (`diag` against `heptapod`) is the test.
- What exists. Upstream returns the verdict and 400 characters of FeynRules'
  printed text for hermiticity, with no vertex and no block.
  `cc_harness/wl/UFO_generator_diag.wl` is the upstream driver plus 88 lines
  (`emitHerm`, `emitMassMix`, `emitBlockContents`); the verdicts are the
  same.
- Change. Take the 88 lines into `UFO_generator.wl`, parse the three line
  types in `lagrangian_checks.py`, return them from `ValidateLagrangian`.
- Flips: counted in the stored 7 already.
- Effort: one day upstream, with the existing unit tests of `diagnose.py`.

### 8. The MadGraph back-trace, the lint, the mass-basis tool

- Back-trace (`diagnose.mg5_backtrace`: UFO file, line, object, and the
  model lines behind it): 4 of the 11 import fixes came after it; the other
  7 came after MadGraph's own message. Move it into `ValidateUFOModel`.
  One day.
- Lint (`fr_lint.py`): it fired with findings before the first validation
  in 8 of 15 runs and accounts for 2 of the 29 in-loop fixes. On the 13
  failing one-shot models it names every failing item of 4 and nothing on
  4. Its effect on the pass count cannot be separated in the stored data.
  Move the precise rules (`ambiguous_total`, `bad_particle_name`,
  `feynrules_symbol_name`, `tensor_orderblock`, `pattern_symbol_name`) and
  change 2 into a `ValidateLagrangian` preflight. Two days.
- `massbasis`: used in 4 of 15 runs (B-L-SM, GeneralU1, MDMmodel, pNG). Two
  of them reach the endpoint; no stored arm has the recipe without the tool,
  so its own effect is not known. Lowest priority.

## In the ALE wrapper only

- Show the `HEPTAPOD-MASS` rows in the validate report (one hour). STORED:
  the agent asked for them.
- Read the first MadGraph error, not the last line: the tail the agent reads
  ends in "invalid syntax (object_library.py, line 268)" for every cause.
  The cause is in `MG5_debug`, which the report does include lower down.
- Accept a bisection file: the harness rejects a file with two root
  Lagrangians (`no_lagrangian_symbol`), which is what a bisecting agent
  writes (SLQrules, calls 5 to 8).
- The scorer needs endpoint condition 3 (change 1).
- The compile limit. RUN (`results/local_rescore_cc_sonnet_harness.json`): On this machine the compile takes 1.5 times as long as on the Mac (median of 15 models, range 1.25 to 1.56). 331 needs 1198 s here (805 s on the Mac), so the default limit of 900 s turns its stored `compiled` into a timeout. With `HEPVAL_COMPILE_TIMEOUT=1350` (900 x 1.5) the limit means here what 900 s meant on the Mac. In the stored run 331 hit the 900 s limit in 4 of its 10 calls.

## Order

1, 2 and 3 first: about three days together, and they touch 5 of the 9
papers that miss the endpoint. 4 and 6 next. 7 after design A says whether
the located reports matter. The expected total, if every inferred flip
held, is 7 + 5 or 6 of 16; one seed supports none of these counts on its
own.
