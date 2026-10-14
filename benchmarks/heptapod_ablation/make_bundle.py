#!/usr/bin/env python3
"""A zip of the final comparison: tools group and vanilla on three models, with the agent traces
and one score table.

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
PAPERS = ("HeavyN", "Top-Philic-Zprime", "pNG", "SMWeinberg", "EffLRSM", "B-L-SM", "MDMmodel", "Monotops",
          "Wprime", "pSPSS", "GeneralU1", "331", "ALRM_general")   # the 13 papers with a usable reference
GROUPS = [   # model folder, group folder, variant, seeds
    ("sonnet-5", "tools", "cc_sonnet_shell", (1, 2, 3)),
    ("sonnet-5", "vanilla", "cc_vanilla_fair", (1, 2, 3)),
    ("haiku-5.5", "tools", "cc_haiku_shell", (1, 2, 3)),
    ("haiku-5.5", "vanilla", "cc_haiku_vanilla", (1, 2, 3)),
    ("sonnet-5.5", "tools", "cc_sonnet55_shell", (1,)),
    ("sonnet-5.5", "vanilla", "cc_sonnet55_vanilla", (1,)),
]
SKIP_DIRS = {"__pycache__"}
SKIP_FILES = {"sandbox_path.txt", "command.json", "mcp.json", "settings.json"}
EMAIL = re.compile(rb"[\w.+-]+@[\w-]+(\.[\w-]+)+")
README = """# heptapod tools against vanilla: results and agent traces

Start with `quick_en.html` (or `quick_zh.html`): the result, how the score is computed, and the
workflow figures (also in `figures/`). Open it in a browser.

Layout: `<model>/<group>/<paper>/<seed>/`, one folder per run, 182 runs.

- Models: `sonnet-5` (claude-sonnet-5, seeds 1 to 3), `haiku-5.5` (claude-haiku-5-5, seeds 1 to 3),
  `sonnet-5.5` (claude-sonnet-5-5, seed 1).
- Groups: `tools` = Claude Code + the heptapod tools (lint_model, validate_model, massbasis,
  review_model) + protocol + stop gate + a shell. `vanilla` = the same Claude Code with a shell only.
- Same for both groups: the task text, FeynRules 2.3.49, MadGraph 3.7.3, a 4-hour limit, 2 Wolfram
  kernels and 2 agents per machine, no network.
- sonnet-5.5, ALRM_general and MDMmodel: the first attempt hit the 4-hour limit in both groups; these
  folders hold the second attempt.

In each run folder:
- `model/<paper>_gen.fr`      the delivered FeynRules model
- `agent_out.md`              the agent's last message
- `agent_stream.jsonl`        the full trace (every message and tool call, Claude Code stream-json)
- `prompt.txt`                the task the agent had (`protocol.md`: the tools group's protocol)
- `tool_calls.jsonl`          the heptapod tool calls (tools group)
- `validation/call<k>/`       each validate_model call: the report, the UFO, the FeynRules log (tools group)
- `stop_gate_log.jsonl`       each stop-gate decision (tools group)
- `score_ufo/`                particles.py and vertices.py of the UFO the scorer built
- `validation_hepval.json`    the scorer's verdict on the delivered model (the six chain items)
- `run.json`                  time, cost, token counts, timeout flag

`scores.csv`: one row per run. `metric` = vertex-kind F1 against the reference model when the scored
chain passes, else 0. `reference_models/<paper>/UFO/` holds the reference UFO, and `ref_score.py` the
scorer (it needs hepbench's `checks.py` to run).

Every email address in the run files is replaced with `<email>`.
"""


def main() -> int:
    out = Path(sys.argv[1])
    rows = []
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for model, group, variant, seeds in GROUPS:
            for paper in PAPERS:
                for k in seeds:
                    sdir = RUNS / paper / "rerun" / variant / f"s{k}"
                    if not (sdir / "run.json").is_file():
                        raise SystemExit(f"missing run: {sdir}")
                    base = f"{model}/{group}/{paper}/s{k}"
                    for f in sorted(sdir.rglob("*")):
                        if f.is_file() and not (set(f.relative_to(sdir).parts) & SKIP_DIRS) and f.name not in SKIP_FILES:
                            z.writestr(f"{base}/{f.relative_to(sdir)}", EMAIL.sub(b"<email>", f.read_bytes()))
                    agent = json.loads((sdir / "run.json").read_text()).get("agent") or {}
                    s = R.score_run(sdir, paper)
                    rows.append({"model": model, "group": group, "paper": paper, "seed": k,
                                 "chain_pass": s["chain"], "metric": s.get("metric"), "f1": s.get("f1"),
                                 "precision": s.get("precision"), "recall": s.get("recall"),
                                 "minutes": round((agent.get("seconds") or 0) / 60), "timed_out": bool(agent.get("timed_out")),
                                 "cost_usd": round(agent.get("cost_usd") or 0, 2)})
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
        z.writestr("scores.csv", buf.getvalue())
        z.writestr("README.md", README)
        z.write(HERE / "hillclimb" / "ref_score.py", "ref_score.py")
        for page in ("quick_en.html", "quick_zh.html"):
            z.write(HERE / page, page)
        for fig in sorted((HERE / "figures").glob("workflow_*.png")):
            z.write(fig, f"figures/{fig.name}")
        for paper in PAPERS:
            ref = HERE / "hillclimb" / "ref_ufo" / paper
            z.write(ref / "how.json", f"reference_models/{paper}/how.json")
            for name in ("particles.py", "vertices.py"):
                z.write(ref / "UFO" / name, f"reference_models/{paper}/UFO/{name}")
    print(json.dumps({"zip": str(out), "runs": len(rows), "mb": round(out.stat().st_size / 1e6, 1)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
