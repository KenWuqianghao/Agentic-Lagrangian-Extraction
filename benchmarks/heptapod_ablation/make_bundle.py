#!/usr/bin/env python3
"""A zip of every group's result and agent trace for every paper, with one score table.

    make_bundle.py OUT.zip

Per run: the delivered model (`model/`), the agent's last message (`agent_out.md`), the full
trace (`agent_stream.jsonl`, `tool_calls.jsonl`), the task and protocol it had, each validate
call's report, the scored UFO and the scorer's verdict. `scores.csv` has one row per run.
"""

from __future__ import annotations

import csv
import io
import json
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "hillclimb"))
import ref_score as R  # noqa: E402

RUNS = HERE / "runs"
STORED = Path.home() / "code/heptapod/eval/benchmark_runs"
HARNESS_UFO = Path("/tmp/claude-exp/rescore_cc")
GROUPS = [   # folder in the zip, runs root, variant, what the agent had
    ("1a_vanilla_run1", RUNS, "cc_vanilla", "shell only; 2 h limit; not told the scorer's two interface rules"),
    ("1b_vanilla_run2", RUNS, "cc_vanilla_v2", "shell only; 2 h limit; 3-4 agents queued for one kernel"),
    ("1c_vanilla_fair", RUNS, "cc_vanilla_fair", "shell only; 4 h limit, two kernel slots (seed 1: 8 papers of run 2 that did "
                                                 "not time out + the 5 rerun papers)"),
    ("2_harness_0930", STORED, "cc_sonnet_harness", "heptapod tools, protocol, stop gate; no shell (stored 2026-09-30)"),
    ("3_optimised", RUNS, "cc_sonnet_opt", "harness + more lint rules + 'a new particle with no vertex is not a pass'"),
    ("4_shell_tools", RUNS, "cc_sonnet_shell", "optimised + a shell: reads its own UFO and logs, runs wolframscript"),
    ("5_plus", RUNS, "cc_sonnet_plus", "shell_tools + gauge recipes + chain-head lint (6 papers)"),
    ("x_cover", RUNS, "cc_hc1_cover", "shell_tools + a target list (spec.json) the UFO must cover (6 papers)"),
    ("6a_haiku55_vanilla", RUNS, "cc_haiku_vanilla", "as 1c_vanilla_fair, model claude-haiku-5-5"),
    ("6b_haiku55_shell_tools", RUNS, "cc_haiku_shell", "as 4_shell_tools, model claude-haiku-5-5"),
    ("7a_sonnet55_vanilla", RUNS, "cc_sonnet55_vanilla", "as 1c_vanilla_fair, model claude-sonnet-5-5; ALRM_general and "
                                                         "MDMmodel are a second attempt after a 4 h timeout"),
    ("7b_sonnet55_shell_tools", RUNS, "cc_sonnet55_shell", "as 4_shell_tools, model claude-sonnet-5-5; ALRM_general and "
                                                           "MDMmodel are a second attempt after a 4 h timeout"),
]
SKIP_DIRS = {"__pycache__"}
SKIP_FILES = {"sandbox_path.txt", "command.json", "mcp.json", "settings.json"}
EMAIL = re.compile(rb"[\w.+-]+@[\w-]+(\.[\w-]+)+")
README = """# heptapod ablation: results and agent traces

Groups 1 to 5 and x use claude-sonnet-5. Groups 6 and 7 use claude-haiku-5-5 and claude-sonnet-5-5.

One folder per group, then per paper, then per seed (`s1`, `s2`, ...).

{groups}

In each run folder:
- `model/<paper>_gen.fr`      the delivered FeynRules model
- `agent_out.md`              the agent's last message
- `agent_stream.jsonl`        the full trace (every message and tool call, Claude Code stream-json)
- `tool_calls.jsonl`          the heptapod tool calls (harness groups)
- `prompt.txt`, `protocol.md` the task and the system-prompt protocol the agent had
- `validation/call<k>/`       each validate_model call: summary.json, the report, the UFO, the FeynRules log
- `score_ufo/`                particles.py and vertices.py of the UFO the scorer built
- `validation_hepval.json`    the scorer's verdict on the delivered model (the six chain items)
- `run.json`                  time, cost, token counts, timeout flag

`scores.csv`: one row per run. `metric` = vertex-kind F1 against the reference model when the scored
chain passes, else 0 (`ref_score.py`, with the three reference label fixes); `metric_raw` is the same
without the fixes. Papers with no usable reference have an empty metric. `reference_models/` holds how
each reference was compiled.

Every email address in the run files is replaced with `<email>`.
"""


def main() -> int:
    out = Path(sys.argv[1])
    rows = []
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for folder, root, variant, _what in GROUPS:
            for pdir in sorted(root.iterdir()):
                for sdir in sorted((pdir / "rerun" / variant).glob("s*")):
                    if not (sdir / "run.json").is_file():
                        continue
                    paper, seed = pdir.name, sdir.name
                    for f in sorted(sdir.rglob("*")):
                        if f.is_file() and not (set(f.relative_to(sdir).parts) & SKIP_DIRS) and f.name not in SKIP_FILES:
                            z.writestr(f"{folder}/{paper}/{seed}/{f.relative_to(sdir)}", EMAIL.sub(b"<email>", f.read_bytes()))
                    alt = HARNESS_UFO / paper / "call1" / "round0" / "UFO"
                    ufo = alt if root == STORED and not (sdir / "score_ufo" / "vertices.py").is_file() else None
                    if ufo and ufo.is_dir():
                        for name in ("particles.py", "vertices.py"):
                            if (ufo / name).is_file():
                                z.write(ufo / name, f"{folder}/{paper}/{seed}/score_ufo/{name}")
                    agent = json.loads((sdir / "run.json").read_text()).get("agent") or {}
                    s, raw = R.score_run(sdir, paper, ufo), R.score_run(sdir, paper, ufo, fixed=False)
                    rows.append({"group": folder, "variant": variant, "paper": paper, "seed": seed,
                                 "chain_pass": s["chain"], "metric": s.get("metric"), "metric_raw": raw.get("metric"),
                                 "f1": s.get("f1"), "precision": s.get("precision"), "recall": s.get("recall"),
                                 "minutes": round((agent.get("seconds") or 0) / 60), "timed_out": bool(agent.get("timed_out")),
                                 "cost_usd": round(agent.get("cost_usd") or 0, 2)})
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
        z.writestr("scores.csv", buf.getvalue())
        z.writestr("README.md", README.format(groups="\n".join(f"- `{f}`: {what}" for f, _r, _v, what in GROUPS)))
        z.write(HERE / "hillclimb" / "ref_score.py", "ref_score.py")
        for how in sorted((HERE / "hillclimb" / "ref_ufo").glob("*/how.json")):
            z.write(how, f"reference_models/{how.parent.name}/how.json")
            for name in ("particles.py", "vertices.py"):
                if (how.parent / "UFO" / name).is_file():
                    z.write(how.parent / "UFO" / name, f"reference_models/{how.parent.name}/UFO/{name}")
    print(json.dumps({"zip": str(out), "runs": len(rows), "mb": round(out.stat().st_size / 1e6, 1)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
