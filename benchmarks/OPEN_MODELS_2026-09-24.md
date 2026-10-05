# Toolkit vs bare harness on open-weights models (2026-09-24)

Question: does the toolkit help an agent extract a FeynRules model from a
paper when the agent is an open-weights model in an open-source harness?

**Update 2026-09-28 (read first).** The MiMo result below (15 of 16 files
against 7 of 16, p = 0.008) did not reproduce and is withdrawn: the same v1
toolkit arm, re-run on 8 papers where it had produced 8 of 8 files, produced
0 of 8. The fixed toolkit (v2, section "Round 2") gave Nemotron 3 Ultra its
first full-chain pass (ChernSimonsPortal, 1 of 15).

Short answer (2026-09-24): the toolkit did not make any open model pass the full chain
(0 of 62 valid runs, both arms). For MiMo v2.6 Flash, the toolkit is the
difference between producing a model file and producing nothing: 15 of 16
papers against 7 of 16 (paired exact test p = 0.008). For Nemotron 3 Ultra
there is no measurable effect. After the compile, both models hit the same
wall as Sonnet in September: Hermiticity, the mass basis and the MadGraph
import.

## Setup

| item | value |
|---|---|
| harness | opencode 1.18.25 (MIT), `opencode run --format json`, isolated `HOME`, no user config, skills or plugins |
| models | `opencode/mimo-v2.6-flash-free` (Xiaomi MiMo v2.6 Flash), `opencode/nemotron-3-ultra-free` (NVIDIA Nemotron 3 Ultra). Both are open weights, served free by opencode Zen |
| papers | the 16 scorable single-model papers of ABLATION_2026-09-17, LaTeX source |
| prompt | the v3s prompts of the same arm type. Only the file paths, the OUTPUT line and the SANDBOX note change |
| budget | 60 min per run, 128k output tokens per step, up to 3 "continue" nudges in the same session when a run stops before its deliverable exists |
| seeds | 1 |
| scoring | the corrected chain (heptapod-dev main 4bcbcf2): compile (900 s timeout, as in September), 4 FeynRules checks, MadGraph import. Serial, one Wolfram kernel |

Two arms. They differ only in the toolkit:

- **hand**: the sandbox holds the paper and `SM.fr`. The agent writes
  `model.fr` itself.
- **toolkit**: the sandbox also holds the schema, the renderer, the lints and
  one command, `./frgen spec.json`. The command validates the JSON against
  the schema, renders `model.fr`, and lints it. The agent writes the spec and
  may run the command as often as it likes. The harness re-renders the final
  spec with a clean copy of the toolkit.

Both arms use the same opencode permission config: read, write and edit
inside the sandbox; shell only for `./frgen`; no web; no path outside the
sandbox. The free tier refuses a request whose tool list lacks the shell
tool, so the hand arm also has the shell tool. There is no `./frgen` in its
sandbox.

Note the difference from September: the September "tools" arm had the schema
and renderer only, one shot, with no lint and no feedback loop. This toolkit
arm has the feedback loop.

## Results

| model | arm | valid runs | `.fr` produced | compiled | MG5 import | 4 checks pass | full chain | field F1 |
|---|---|---|---|---|---|---|---|---|
| Nemotron 3 Ultra | hand | 15 | 11 | 5 | 0 | 1 | **0** | 0.59 |
| Nemotron 3 Ultra | toolkit | 15 | 11 | 6 | 1 | 0 | **0** | 0.73 |
| MiMo v2.6 Flash | hand | 16 | 7 | 5 | 2 | 2 | **0** | 0.66 |
| MiMo v2.6 Flash | toolkit | 16 | **15** | 9 | 4 | 2 | **0** | 0.65 |
| Sonnet 5 (Sep 17) | hand | 16 | 15 | 11 | 4 | 4 | **2** | 0.66 |
| Sonnet 5 (Sep 17) | schema one-shot | 16 | 15 | 13 | 7 | 3 | **2** | 0.67 |

Paired exact (McNemar) tests, toolkit against hand, on the same papers:

| model | stage | toolkit only | hand only | p |
|---|---|---|---|---|
| MiMo | `.fr` produced | 8 | 0 | **0.008** |
| MiMo | compiled | 5 | 1 | 0.22 |
| MiMo | MG5 import | 3 | 1 | 0.63 |
| Nemotron | `.fr` produced | 2 | 2 | 1.0 |
| Nemotron | compiled | 3 | 2 | 1.0 |

"Valid runs" leaves out pSPSS for Nemotron in both arms: those runs ended on
provider errors (503 "Service temporarily overloaded", 504 "Upstream idle
timeout") before any file existed. Seven other Nemotron runs failed the same
way at first. They were retried once, and the retry counts. The failed
attempts are kept as `s1_infra1`.

Per-paper cells: `open_bench/report.md`. Raw rows: `open_bench/report.json`.

## What the toolkit changed

**MiMo: the toolkit gets a file written.** MiMo reasons for a very long time
before it writes a large file. In the hand arm, 13 of 16 runs hit the
60-minute limit, and 9 of them never wrote `model.fr`. One step alone used
87k reasoning tokens in 26 minutes and wrote nothing. In the toolkit arm, the
agent writes a JSON spec, runs `./frgen`, and edits the spec. 15 of 16 runs
left a spec on disk, and 15 of 16 ran `./frgen` at least once. This is the
one significant effect in the study. It is an effect on *finishing*, not on
correctness: the compile and MadGraph gains (9 vs 5, 4 vs 2) are not
significant at n = 16.

**Nemotron: the toolkit swaps one error class for another.** Nemotron used
the tool less: it ran `./frgen` in 9 of 16 toolkit runs, and 2 runs left a
spec that it never checked. The compile failures show the swap:

| cause | Nemotron hand | Nemotron toolkit |
|---|---|---|
| unquoted LaTeX in `TeX -> \chi` (syntax error) | 3 | 0 (the renderer quotes it) |
| no total Lagrangian, or two candidates | 2 | 1 (the one run that never ran `./frgen`) |
| mass/width value FeynRules rejects (`Width -> {W, Auto}` twice, `Mass -> {MZp, MZp}` once) | 0 | **3** (the schema accepts any string) |
| compile timeout | 0 | 1 |

The renderer removes a whole class of syntax error, and the lint catches the
missing total when the agent runs it. The schema lets a new class through.
The field F1 rises from 0.59 to 0.73, but the pass counts do not move.

**After the compile, nothing changes.** Every compiled file in both arms
fails at least one of Hermiticity, the mass basis, the mass spectrum or the
MadGraph import. These are the same classes that decide the Sonnet result.
Two examples: `mass_diagonal` fails on HeavyN and MDMmodel (the neutrino and
singlet mass mixing of OPTIONS_2026-09-22 section 1). On Wprime, MadGraph
stops with `name VLq1x1 define multiple time`, because two External tensors
(`VLq`, `VRp`) share one LHA block, so their entries collide (corrected
2026-09-24; the first version of this note blamed a separately declared
component).

## Toolkit gaps these runs found

Each gap let a defect through the schema and the lint, and FeynRules or
MadGraph then rejected the file:

1. **Mass/width value.** `MassSpec.value` accepts any string. FeynRules reads
   only a number or `Internal` (the renderer also maps `Automatic`), so allow
   only those (3 Nemotron compile failures).
2. **Bracket balance.** A Lagrangian string with unbalanced brackets passes
   the schema (SLQrules MiMo toolkit: "unexpected end of file"). A balance
   check on every `expression` costs nothing.
3. **External block collisions.** Two External parameters on one LHA entry
   (two same-rank tensors in one block, or a one-index tensor on a scalar's
   OrderBlock). The UFO defines one name twice and MadGraph rejects it
   (`VLq`/`VRp` in `WPCOUP`). Corrected 2026-09-24: first written as "a
   tensor plus a separately declared component".
4. **SelfConjugate with QuantumNumbers.** FeynRules warns. Corrected
   2026-09-24: every case in the data is a zero charge (`Q -> 0`), and a
   Top-Philic-Zprime file with `Q -> 0` passed the full chain, so this is not
   a failure cause. The fix rejects only non-zero charges on real fields,
   which are physically wrong.
5. **The loop is optional.** The toolkit helps only when the agent calls it.
   Nemotron skipped `./frgen` in 7 of 16 runs. A harness hook that runs
   `frgen` on every write of `spec.json` removes that choice.

## Caveats

- n = 16 papers, 1 seed. The only significant result is MiMo's `.fr`
  produced. Everything else is inside the noise, as in September.
- Free-tier serving. Nemotron's provider failed often (503/504). MiMo's
  catalog output cap is 32k, and its reasoning filled that cap before the
  first write on every smoke run. The endpoint served a 95.7k-token step when
  asked, so both models ran at 128k. A pilot at the default 32k cap was
  discarded; its partial data showed the same direction (the MiMo toolkit
  arm produced files on ALRM_general and 331, and the hand arm did not).
- The 60-minute limit decides the MiMo result. With no time limit, the hand
  arm might write more files. The limit is the same in both arms.
- Local open models were not tried. The Mac has 16 GB and its swap was
  full; the only local model (qwen2.5:14b) has a 32k context, which is too
  short for the papers plus `SM.fr`.
- The harness is different from September's (opencode against Claude Code
  subagents), so the Sonnet rows are a reference, not a controlled arm.
- The free tier may log prompts. The inputs are public arXiv sources and the
  GPL toolkit files.

## Files

- `open_bench/open_bench.py`: sandbox, prompts, opencode runner, audit,
  nudges, serial validation.
- `open_bench/frgen_cli.py`: the `./frgen` command (schema + renderer + lint).
- `open_bench/report.py`: this table, Fisher tests, per-paper cells.
- `<page>/rerun/v3o_{mimo,nemotron}_{hand,toolkit}/s1/`: TASK.md, the full
  JSON event stream, tool calls, audit, spec, `.fr`, validation, predicates.

## Round 2 (2026-09-25 to 09-28): the gaps fixed, and a control

The four schema fixes are committed in heptapod-dev (`35e2bb3`, local branch
`frgen/schema-gaps`). Gap 5 is an opencode plugin (`open_bench/frgen_hook.js`)
that runs `./frgen` after every write or edit of `spec.json` and appends the
report to that tool result. Arm `toolkit2` = toolkit + both. Replay of the
new schema on 104 stored specs the old schema accepted: 14 rejected, all 14
failed the chain, none that passed was rejected.

| model | arm | valid runs | `.fr` produced | compiled | MG5 import | 4 checks pass | full chain |
|---|---|---|---|---|---|---|---|
| Nemotron 3 Ultra | hand | 15 | 11 | 5 | 0 | 1 | 0 |
| Nemotron 3 Ultra | toolkit | 15 | 11 | 6 | 1 | 0 | 0 |
| Nemotron 3 Ultra | toolkit2 | 15 | 15 | 8 | 2 | 2 | **1** |
| MiMo v2.6 Flash | hand | 16 | 7 | 5 | 2 | 2 | 0 |
| MiMo v2.6 Flash | toolkit | 16 | 15 | 9 | 4 | 2 | 0 |
| MiMo v2.6 Flash | toolkit2 | 16 | 3 | 2 | 0 | 0 | 0 |

- Nemotron toolkit2 against hand: files 15 vs 11 (Fisher p = 0.10), compiled
  8 vs 5 (p = 0.46). The pass is ChernSimonsPortal: 4/4 checks, MadGraph
  import, clean audit. Excluded for provider errors: SLQrules.
- MiMo toolkit2 collapsed to 3 of 16 files. In 11 of 16 runs the hour ended
  inside one long generation, as in the hand arm (13 of 16). Provider speed
  was normal (small steps: median 1.5 s).
- **Control (2026-09-28).** The v1 toolkit arm (old schema, `--pure`, no hook)
  re-run as seed 2 on ALRM_general, EffLRSM, GeneralU1, NJLComposite,
  SLQrules, Wprime, pNG and HeavyN: **0 of 8** files, against 8 of 8 on
  2026-09-24. So the toolkit2 changes did not cause the drop. MiMo either
  varies this much between runs or the free endpoint changed the model; the
  data cannot separate the two. The September-24 MiMo result is withdrawn.
- The free tier rate-limited both models from the evening of 2026-09-24 into
  2026-09-25. The driver now stops a run at the first 429 and
  `open_bench/supervise.py` retries it when the quota returns; 4 cut runs
  are kept as `s1_infra1`.

