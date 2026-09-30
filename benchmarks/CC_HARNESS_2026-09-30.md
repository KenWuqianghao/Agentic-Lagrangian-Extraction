# Claude Code with the chain in its loop: 16 papers, Sonnet 5 (2026-09-30)

Question: when Claude Code (Sonnet 5) writes the FeynRules add-on model
itself and can run the scored chain on it while it works (compile, the four
consistency checks, MadGraph import), how many of the 16 single-model
papers reach a full-chain pass? The two arms to beat, scored by the same
code:

- `v3s_notools`: Claude Code, Sonnet 5, no tools, one shot: 2/16;
- `pi_qwen_harness`: Qwen3.8-27B in the pi harness, same tools in the loop:
  4/16 (`PI_HARNESS_2026-09-28.html`).

Code: `cc_harness/` (this note), reusing `pi_harness/hepval.py`,
`run_pi.py`'s prompt, directories and scorer, and `summarize.py`.
Runs: `~/Documents/Github/heptapod/eval/benchmark_runs/<paper>/rerun/cc_sonnet_harness/s1/`.

## What the harness is

Every earlier Claude Code run in this benchmark was one-shot: the agent
wrote the file and stopped, and the harness validated it afterwards. The
repair loop started a new agent per round. Only the pi harness put the
validator inside the agent's loop, and pi cannot run Claude models on the
subscription ("Third-party apps now draw from your extra usage"). The new
parts are therefore an adapter, not a new pipeline:

- **`heptapod_mcp.py`**: an MCP server, `heptapod-tools`, over stdio
  JSON-RPC. Four tools, each a call to `hepval.py`: `lint_model`,
  `validate_model` (budget 10; the report opens with the call number and the
  stage reached: compile, checks, mg5 or pass), `massbasis`, and
  `review_model` (budget 2; a fresh `claude -p` referee in its own sandbox
  with a frozen copy of the model).
- **Sandbox by configuration.** `--tools Read,Write,Edit,Glob,Grep`,
  `--disallowedTools Bash,WebFetch,WebSearch,Task,Agent,NotebookEdit`,
  `--strict-mcp-config`, `--setting-sources ''`, and a PreToolUse hook
  (`hooks/pretool_guard.py`) that denies every path outside the sandbox after
  `..` and symlinks. The sandbox holds the paper, `SM.fr` and the agent's
  `model.fr`.
- **No finishing with a failing model.** A Stop hook (`hooks/stop_gate.py`)
  sends the agent back, with a digest of the last report, while `model.fr` is
  missing, never validated, changed since its last validation, or failed it.
  At most 3 continuations per run; none once the validate budget is spent.
  Every decision is logged with `stop_hook_active`.
- **The prompt** is `run_pi.py`'s harness prompt on stdin, and the protocol
  (`prompts/protocol.md`) is pi's, with the SM-override section verbatim.

## What the reports now say

The validate report had three gaps, each fixed without touching a verdict.

1. **Hermiticity.** The scoring driver reduces `CheckHermiticity`'s return
   value, the Feynman rules of `L - HC[L]`, to pass or fail (`runCheck` ->
   `vHermiticity` in `UFO_generator.wl`) and keeps only the printed prose, cut
   to 400 characters. A copy of the driver (`wl/UFO_generator_diag.wl`; the
   diff against heptapod-dev main 4bcbcf2 is the two check calls and the
   helpers) writes one line per non-zero vertex, its fields and coefficient,
   and the field contents of each named Lagrangian block, so the report says
   which block holds the vertex. A vertex whose coefficient still holds fields
   is one FeynRules could not reduce; the report says so. The copy is used
   only by the in-loop `validate_model` (`hepval validate --diag`); scoring
   keeps the pristine driver.
2. **Mass matrix.** When `mass_diagonal` fails, the same copy writes every
   off-diagonal mass term and every tadpole, with its coefficient and value.
3. **MadGraph import.** The report names the UFO file, line and object that is
   not Python, shows it, and lists the model.fr lines that declare or use the
   symbols in it (tensor parameters by component, particles through SM.fr's
   classes, the vertices that use a broken coupling).

Four constructs behind these failures are visible in the text, so they are
also `fr_lint` rules, each with a unit test. Precision on the 199 stored
models that have a verdict, among compiled files the rule flagged:

| rule | what it catches | flagged and compiled | failed the predicted stage |
|---|---|---|---|
| `pattern_symbol_name` | a quantum number named `B_L` (a Mathematica pattern) | 1 | 1 |
| `tensor_orderblock` | an `OrderBlock` on a parameter with `Indices` | 9 | 9 |
| `explicit_spin_in_chain` | `Xbar[sp].Ga[mu].Y[sp, ff]` | 8 | 7 |
| `numeric_spin_slot` | `l[1]` for the electron: the first index is spin | 4 | 4 (checks) |

The one miss of `explicit_spin_in_chain` is a self-hermitian current with the
full index list on both spinors (Top-Philic Z', pi Qwen harness), which
passes. Underscores in parameter names (`aSRh_u`) passed the chain in a
stored run, so they only warn.

## Replay: the six near-miss models of the pi Qwen harness

Each model failed only one stage. Replayed through the new
`validate_model` (`cc_replay/<paper>/agent_view.md`):

| paper | failed stage | old report | new report points at | fix |
|---|---|---|---|---|
| B-L-SM | MadGraph | "UFO model not python3 compatible" and a traceback | `particles.py` line 25 `B_L = (B_L)[A]`; model.fr lines 252 and 267, `QuantumNumbers -> {B_L -> ...}`; lint `pattern_symbol_name` on both | rename `B_L` |
| HeavyN | MadGraph | the same, plus a syntax error in `couplings.py` | coupling `GC_155` (vertex Z, ve); model.fr line 73, `NLbar[sp].Ga[mu].vl[sp, ff]` (the Z current); the `VlN` tensor declaration; lint `explicit_spin_in_chain` line 73, `tensor_orderblock` line 54 | implicit spin index; drop the OrderBlock |
| Wprime | MadGraph | the same, plus a syntax error in `parameters.py` | parameter `WpLeR1`; the whole `WpLeR == {...}` declaration with `OrderBlock -> 7`; lint `tensor_orderblock` on four tensors | drop the OrderBlocks |
| EffLRSM | hermiticity | generic "add `+ HC[...]`" text, no vertex | unreduced W_R-lepton vertices, block `LWRlepton` first; lint `numeric_spin_slot` lines 325-327, `NR1bar.Ga[mu].l[1]` | `l` with implicit indices, the member name, or all indices |
| SMWeinberg | hermiticity | the same generic text | vertices N e G0 G+ in block `LG0GP`, N e G+ (H) in `LNGP` | `LG0GP` has no `+ HC[...]` |
| pSPSS | hermiticity | the same generic text | unreduced W and Z vertices in blocks `LmixW` and `LmixZ`; lint `explicit_spin_in_chain` on the same lines | implicit spin indices |

For EffLRSM and pSPSS the old advice ("add `+ HC[...]`") was wrong: the
partners were there; the chains could not be reduced.

## Results

(filled in below from `cc_harness/collect.py`)
