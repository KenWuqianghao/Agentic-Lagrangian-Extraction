# Agent benchmark: which model best drives the physics toolkit?

Infrastructure, deliberately model-agnostic. Only Claude has credentials on
this machine today, so the other harnesses are declared with an explicit
reason rather than omitted — a run says "codex: no usage left" instead of
quietly comparing one model against nothing.

```bash
python benchmarks/agent_bench/run.py --list
python benchmarks/agent_bench/run.py --dry-run
python benchmarks/agent_bench/run.py --driver claude_code --tier 1,2
```

## Why it is built this way

**Scoring never asks the model whether it succeeded.** Every case is judged on
an artifact an independent checker can verify: a `.fr` that contains what
FeynRules requires, a number that matches a live archive query. A model that
writes a confident summary and no file scores zero.

**Tool facts come from the tool server, not the harness.** `tool_calls.jsonl`
is written by toolbase and is identical across harnesses, which is what makes
the comparison fair. A harness reporting a call the server never saw is
telling you what it intended. Where the two disagree, the discrepancy is
recorded and the server wins.

**Required-tool coverage is checked separately from the score.** A case
answered without its required tools was answered from memory or from the open
internet. It can still look correct, which is exactly why the check exists.

## Three ways this benchmark lied before the checks existed

All three were caught by running it, not by reasoning about it.

1. **The toolkit was not served at all.** The first run made 4 tool calls,
   produced a plausible answer, and never touched heptapod — it reached
   `arxiv.org` through a generic fetch tool. Fixed by generating an MCP config
   per run that serves only heptapod.

2. **The run inherited the operator's own MCP servers.** Whatever is
   configured for the person running the benchmark leaked into the agent's
   toolbox, turning "how well does this model drive the toolkit" into "how
   resourceful is this model in general". Fixed with `--strict-mcp-config`.

3. **Built-in shortcuts bypassed the toolkit.** A run `curl`'d the archive's
   HTTP API directly, produced the correct number, and would have scored a
   clean pass having never used a single physics tool. Fixed by disallowing
   `Bash`, `WebFetch` and `WebSearch`.

A fourth was an argv bug rather than a lie: `--disallowedTools` is variadic
and swallowed a trailing positional prompt, so the CLI exited immediately and
every case looked like an instant model failure. The prompt goes on stdin.

## Layout

```
trace.py     one normalized event stream, whatever harness produced it
cases.py     tiered tasks, each scored on a verifiable artifact
drivers.py   one adapter per harness, identical signature
run.py       the matrix runner
```

Adding a harness means adding a driver and nothing else. That is the entire
reason the trace schema exists.

## Tiers

| tier | what it tests |
|---|---|
| I | single tool call, deterministic, no external software |
| II | a short chain, still deterministic |
| III | external software in the loop (FeynRules, Wolfram, MadGraph) |
| IV | open-ended: the agent picks its own path to a verifiable artifact |

## Status

Verified working on tiers 1–2 with `claude_code`: the agent uses the real
toolkit (`required=ok`), and the artifact scorers pass. Tier 1 has no scorer
yet and is reported as unscored rather than as a pass.

Not yet done: an orchestral driver (the route to Gemini/Groq/Ollama without a
new harness), a direct-API driver with no coding harness at all, and scorers
for tiers 3–4 beyond "the .fr renders".
