# Four groups on the 16 papers: results and defects (2026-10-07)

Same model (Sonnet 5 in Claude Code), same 16 papers, same scorer, one seed
per group. This note replaces the group comparison in `REPORT.md`; the
retrospective analysis there still stands.

| group | what the agent has | runs |
|---|---|---|
| 1. vanilla (`cc_vanilla`) | a shell and file tools; no heptapod tool, skill, protocol or gate; it runs `wolframscript` and MadGraph itself (`run_vanilla.py`) | new, 2026-10-06, half on the Mac |
| 2. harness (`cc_sonnet_harness`) | lint, validate (budget 10), massbasis, referee, Stop gate, protocol with the SM-override recipe | stored, 2026-09-30 |
| 3. optimised (`cc_sonnet_opt`) | group 2 plus `cc_harness/opt_checks.py` and four prompt notes | new, 2026-10-06 |
| 4. shell + tools (`cc_sonnet_shell`) | group 3 plus a shell, read access to the outputs of its own validate calls, the cut-statement check, and a gate that does not accept a cut statement or a vertex-less new particle | new, 2026-10-07 |

The older "no tools, one shot" arm (2 of 16) is not a baseline for a person
with a computer: with a shell the same model reaches 7.

## Results

| measure | 1. vanilla | 2. harness | 3. optimised | 4. shell + tools |
|---|---|---|---|---|
| model delivered | 16 | 15 | 16 | 16 |
| full chain pass | 7 | 11 | 13 | 14 |
| chain pass, and no cut statement, and every new particle in a UFO vertex | 7 | 8 | 9 | 14 |
| chain pass, and the fresh referee finds nothing physics-changing | 2 | 2 | 3 | 7 |
| chain pass, and every interaction of the paper has a vertex (audit, particle content only) | not audited | not audited | not audited | 7 |
| cost | $78 | $63 | $60 | $70 (two timed-out runs recorded $0) |

Group 4 against group 1, paired on the papers: 7 papers pass the chain only
in group 4 (331, B-L-SM, GeneralU1, MDMmodel, Monotops, SMWeinberg, pSPSS)
and none only in group 1; exact McNemar p = 0.016. On the second row, group 4
against group 3 is 5 against 0, p = 0.0625. Group 4's chain failures:
ALRM_general (compile timeout) and SLQrules (mass_spectrum and import; its
first compile in any group).

Read the second row with care for group 4: its gate checks exactly those two
conditions, so the agent worked against them. The audit
(`results/forensics/group4_shell.md`) asked whether the 14 passes are real:

- None is hollow. Seven hold every interaction of the paper (B-L-SM,
  ChernSimonsPortal, EffLRSM, HeavyN, Top-Philic-Zprime, Wprime, pNG);
  Monotops holds the paper's Eq. 1 and lacks the gluon vertices of its colour
  triplets; six are partial (331, GeneralU1, MDMmodel, NJLComposite,
  SMWeinberg, pSPSS).
- Three reached a condition in a cheap way. 331 added a term the paper does
  not have, `H2^2 H3^2`, "only so H2/H3 have a vertex". SMWeinberg set the
  Goldstone terms to zero after mass_diagonal failed. MDMmodel replaced the
  paper's t-T mixing by diagonal couplings. All three say so in their text.
- The referee count moves the same way as the audit (7 clean against 2, 2
  and 3), and 6 of its 7 clean papers are in the audit's complete set. The
  referee's noise, measured in group 3, still holds.
- Groups 1 to 3 were not audited this way, so the last row cannot be
  compared yet.

Per paper (P pass; "cut" a top-level statement cut at a line end; "inert" a
new particle with no vertex; the failing stage otherwise):

| paper | 1. vanilla | 2. harness | 3. optimised |
|---|---|---|---|
| ChernSimonsPortal | P | P, cut | P |
| EffLRSM | P | P | P |
| HeavyN | P | P | P |
| NJLComposite | P | P | P |
| Top-Philic-Zprime | P | P | P |
| Wprime | P | P | P |
| pNG | P | P | P |
| B-L-SM | hermiticity, mass_spectrum | P | P |
| MDMmodel | mass_spectrum (P when scored as written) | P | mass checks, import |
| pSPSS | three checks | P, cut, inert | P |
| Monotops | compile timeout | P, cut, inert | P, cut, inert |
| 331 | compile | mass_spectrum, import | P, cut |
| GeneralU1 | mass_spectrum, import | kinetic_diagonal | P, cut, inert |
| SMWeinberg | no single total | hermiticity | P, cut |
| ALRM_general | compile | no model | hermiticity |
| SLQrules | compile timeout | compile | compile timeout |

How to read it:

- On the chain alone the order is 7, 11, 13.
- A chain pass is not a model. With the two UFO-level conditions the order
  is 7, 8, 9: every vanilla pass is sound on them, 3 of the 11 harness
  passes are not, and 4 of the 13 optimised passes are not. The gain of the
  harness over a shell is then one paper, and of the optimisations one more.
  One seed cannot tell these apart from noise.
- The referee count does not separate the groups (2, 2, 3) and should not be
  the endpoint as it is. Two reasons, both measured. It is noisy: on the 7
  group-3 files that have an in-loop verdict and a fresh one, 4 disagree on
  "physics-changing or not". And about half of what it calls
  physics-changing is not a model error: of the 27 items on the 13 group-3
  passes, 11 are real departures, 2 are terms changed to pass a check, and
  14 are conventions, input values or conflicts inside the paper
  (`results/forensics/group3_opt.md`, section E). It also reads the `.fr`
  text and cannot see a cut statement or a vanished vertex.
- The earlier statement "8 of the 11 harness passes are faithful" used the
  in-loop verdicts of 2026-09-30. With a fresh referee on the same files it
  is 2 of 11. The verdict the agent worked against is not a measurement.

## 4. Shell + tools (`cc_sonnet_shell`): what the shell did and what is wrong

- **The agent used it.** 488 shell commands in 16 runs: 68 read its own
  validation outputs, 64 ran `wolframscript` itself, 78 read the FeynRules
  source. No command reached the network or opened another run.
- **The new checks fired little.** `cut_statement` fired in one run (331, 23
  lines, fixed before the first validation); "no vertex" in two (Monotops,
  pSPSS, fixed at the next call). No delivered file has either defect. As in
  group 3, the prompt text and the agent's own look at the UFO did most of
  the work; no run isolates the two.
- **Defects of the arm:**
  - The agent ends its turn to wait. `Monitor` and `ScheduleWakeup` are in
    its tool list; SLQrules used all 3 gate continuations in 117 s, and the
    gate did nothing for the next 3.4 hours.
  - Three runs hit the 4-hour limit (ALRM_general, NJLComposite, SLQrules).
    The agent's own `wolframscript` waits behind the same kernel lock as the
    validations: 6.6 hours of lock wait over the 16 runs.
  - The MCP client's 1800 s limit ended 5 validate calls.
  - NJLComposite's delivered file is not the one it last validated (the limit
    came during call 7); it passes the score.
  - The gate can be met by adding or removing physics (331, SMWeinberg,
    MDMmodel above). It needs the paper's interactions as the reference, not
    only the model's own particles.
- **A claim of the audit that I could not reproduce.** The audit says rule 3
  of the prompt addendum (`bar[CC[psi]]`) is read by the kernel as `bar[1]`
  and broke the first call of SMWeinberg, Monotops and EffLRSM. In a kernel
  with SM.fr loaded, `bar[CC[l]]` stays `bar[CC[l]]` (run on 2026-10-07). So
  the mechanism is not confirmed; the form may still be wrong inside a Dot
  chain, which was not tested.

## A defect no tool names: statements cut at a line end

In a `.fr` file a top-level expression that is complete at the end of a line
ends there:

```
LTotal := LSM + LKin
  + LYukawa + LGauge;     (* a separate expression; it does nothing *)
```

`LTotal` is `LSM + LKin`. Verified in the kernel (`x := a`, newline, `+ b`,
newline, `+ c;` gives `a`). FeynRules, the four checks and MadGraph accept
the shorter model. `cut_statements.py` finds the pattern in 3 delivered
harness passes and 4 optimised passes, and in none of the 7 vanilla passes.
It is the cause of both "inert" passes of group 3 and of ALRM_general's
hermiticity failure there. It was found by reading the group-3 runs; it is
not in `opt_checks.py` yet.

## Defects of each group

### 1. Vanilla

- **It stops while it waits.** In 8 of the 9 failures the last message is
  "I'll wait for the job". A headless session ends there. For 331,
  GeneralU1, Monotops and SLQrules the agent never saw the result of its
  last run.
- **Its own test is not the scorer.** Every run wrote its own check script
  (all four checks appear in all 16), 13 tried WriteUFO and 10 a MadGraph
  import. pSPSS read "mass terms diagonal" as a mass-spectrum pass.
- **No help with large models.** Monotops and SLQrules do not compile in the
  time limit (SLQrules expands to 19509 terms); 331 and ALRM_general end in a
  kernel recursion error that the agent saw and could not place.
- **The task text missed two scorer rules** (my error, not the agent's): the
  scorer adds `LSM` when `LTotal` does not name it, and it needs one unused
  top-level `L` term. B-L-SM, MDMmodel, GeneralU1 and SMWeinberg wrote a full
  Lagrangian from SM.fr's pieces or left a second root. Scored as written
  (`intent_score.py`), MDMmodel passes (8 of 16); SMWeinberg and GeneralU1
  then pass all four checks and fail the import; B-L-SM fails hermiticity.
- **Strength.** No pass is hollow: no cut statement and no inert particle
  in the 7. The agent looks at its own UFO.
- The runs on one machine shared its one Wolfram kernel; a 21-minute
  Monotops job blocked two others.

### 2. Harness (`cc_sonnet_harness`)

- **Hollow passes.** Monotops and pSPSS pass with no new-particle vertex;
  ChernSimonsPortal passes with a cut statement. The loop optimises the
  chain's verdict, and the verdict cannot see these.
- **Failures the report did not place** (`RETRO.md`,
  `results/forensics/group2_cc_sonnet_harness.md`): SMWeinberg and pSPSS,
  a field with a partial index list (`l[ff]`), 10 calls each; GeneralU1, the
  `Phi` redeclaration outside `M$ClassesDescription`, 8 calls; SLQrules, one
  block of 19 that does not expand, 10 calls; 331, ghost masses with no mass
  rows in the report, and 14 masses declared twice.
- **Budget spent on probing.** NJLComposite used 4 of 10 calls on probe
  files and then cut the model to one generation.
- **Physics weakened to pass.** MDMmodel dropped the paper's top-partner
  term; 331 replaced a matrix coupling by an average.

### 3. Optimised (`cc_sonnet_opt`)

What changed against group 2: 331, GeneralU1 and SMWeinberg pass the chain;
pSPSS passes with real vertices; ALRM_general delivers a model; MDMmodel
fails.

- **The prompt notes did the work, not the lint rules.** In 331, GeneralU1,
  SMWeinberg and pSPSS the agent wrote the file the right way from the first
  call. `class_outside_list`, `duplicate_mass_parameter` and
  `shared_lha_block` never fired in 16 runs. `partial_index_fermion` fired
  in 3 runs, each before the first validation, and was fixed each time. This
  is an inference from the files: the runs have no control with the notes
  and without the rules.
- **The "no vertex" check works and is not enough.** It fired in 7 runs and
  cleared in 4. GeneralU1 and Monotops ended with it still firing after 10
  calls: the cause was a cut statement, and the report's hint pointed at
  partial indices, the wrong place.
- **Defects of the new checks themselves:**
  - "no vertex" tests `name` and `name__tilde__` only; a particle with its
    own antiparticle name is a false alarm (8 of ALRM_general's 9 firings).
  - "UFO parameters defined twice" prints 20 names with no count of the
    rest and gives two causes; neither was Monotops' cause, and the agent
    spent 7 calls on it.
  - "no vertex" led NJLComposite to invent a coupling for a singlet that
    the paper leaves without one.
  - `nonpositive_order` fired on SM.fr's own `aEWM1` once.
- **MDMmodel stopped early.** It kept the paper's term, answered each of
  the 3 Stop-gate blocks with "this needs a decision from you" and no tool
  call, and was released with 7 validate calls unused. The gate has no rule
  for an agent that refuses to continue.
- **Still not solved:** SLQrules (compile over the limit), the mass mixing
  in MDMmodel and SLQrules that the agent does not rotate, and the cut
  statements.

## What follows for heptapod

In the order the three groups support:

1. Detect cut statements (new; `cut_statements.py` is the prototype). It is
   behind 7 hollow or failing results across groups 2 and 3.
2. Fail a model whose new particle has no vertex, with the antiparticle name
   handled and without a guess at the cause.
3. Put the four "silent mistakes" in the skill text. They moved three
   papers without any tool firing.
4. Say which block does not expand (`compile_bisect.py`), for SLQrules-size
   models.
5. Replace "referee says no physics-changing item" as an endpoint. Use the
   UFO: compare vertices with the paper's couplings, as hepbench does.

## Limits

- One seed per group. Differences of one or two papers are not established.
- Group 4's checks and notes were written after reading the failures of groups 2 and 3 on these papers; its gain is in-sample.
- Group 2 ran on 2026-09-30 on the Mac with Claude Code 2.1.282; groups 1
  and 3 on 2026-10-06 with 2.1.290 and 2.1.291. The scorer reproduces all 15
  stored group-2 scores on this machine.
- Group 1's task text is short and differs from the harness task text; the
  two scorer rules above were missing from it.
- Group 3 was written after reading group 2's failures on the same 16
  papers, so its gain on these papers is in-sample.
- The design-A repair experiment was stopped at 59 of 108 runs on the
  user's direction; its runs are kept in `runs/` and are not analysed here.
