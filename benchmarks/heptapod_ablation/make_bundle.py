#!/usr/bin/env python3
"""A zip of the final comparison for physicists: per model and paper, the agent's .fr files, the
ground-truth .fr and a readable trace of each run.

    make_bundle.py OUT.zip

Layout: <model>/<paper>/ holds ground_truth_<file>.fr and, per group and seed, <group>_s<k>_model.fr
and <group>_s<k>_trace.md. Top level: README.md and scores.csv (one row per run).
"""

from __future__ import annotations

import csv
import io
import json
import re
import sys
import time
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "hillclimb"))
import ref_score as R  # noqa: E402

RUNS = HERE / "runs"
PAPERS = ("HeavyN", "Top-Philic-Zprime", "pNG", "SMWeinberg", "EffLRSM", "B-L-SM", "MDMmodel", "Monotops",
          "Wprime", "pSPSS", "GeneralU1", "331", "ALRM_general")   # the 13 papers with a usable reference
MODELS = [   # folder, (group, variant) pairs, seeds
    ("sonnet-5", (("tools", "cc_sonnet_shell"), ("vanilla", "cc_vanilla_fair")), (1, 2, 3)),
    ("haiku-5.5", (("tools", "cc_haiku_shell"), ("vanilla", "cc_haiku_vanilla")), (1, 2, 3)),
    ("sonnet-5.5", (("tools", "cc_sonnet55_shell"), ("vanilla", "cc_sonnet55_vanilla")), (1,)),
]
EMAIL = re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+")
README = """# heptapod tools against vanilla: models and agent traces

Layout: `<model>/<paper>/`
- `ground_truth_<file>.fr`   the reference model from the FeynRules model database
- `<group>_s<k>_model.fr`    the model the agent delivered
- `<group>_s<k>_trace.md`    the agent's work: task, its messages, every tool call and result, the
                             stop-gate messages, and its final summary

Models: `sonnet-5` (claude-sonnet-5, seeds 1 to 3), `haiku-5.5` (claude-haiku-5-5, seeds 1 to 3),
`sonnet-5.5` (claude-sonnet-5-5, seed 1). 13 papers, 182 runs.

Groups:
- `tools`: Claude Code + the heptapod tools (lint_model, validate_model, massbasis, review_model) +
  a protocol + a stop gate + a shell. The stop gate sends the agent back (at most 3 times) when it
  tries to stop with a model that did not pass validate_model.
- `vanilla`: the same Claude Code with a shell only. It runs FeynRules and MadGraph itself and
  decides itself when to stop.
- Same for both: the task text, FeynRules 2.3.49, MadGraph 3.7.3, a 4-hour limit, no network. The
  agent writes an add-on loaded on top of FeynRules' SM.fr.

Score (`scores.csv`, column `score`):
1. Gate: the delivered model must pass FeynRules compile, hermiticity, diagonal kinetic terms,
   diagonal mass terms, the mass spectrum (declared against derived masses) and MadGraph import.
   One failure gives 0.
2. Each vertex with at least one new particle becomes a "kind": Standard Model particles by PDG code
   with the generation removed, new particles by (spin, charge, colour). Ghosts and Goldstones are
   left out.
3. Score = F1 between the agent's set of kinds and the ground truth's set.
The score does not compare coupling values or signs. Three label errors of the ground truth are
corrected in the scorer only, not in the files here: Monotops (colour of phic and tphic), B-L-SM
(the Higgs has PDG code 9900025), 331 (beta is a free symbol; the 4 values of the paper are tried).
GeneralU1's ground truth is the database file with one quoting fix so that it compiles.

Notes:
- `delivered = False` in scores.csv: the agent left no model.fr; there is no `_model.fr` file.
- sonnet-5.5 ALRM_general and MDMmodel: the first attempt hit the 4-hour limit in both groups; the
  files are the second attempt.
- Every email address in the files is replaced with `<email>`.
"""


def fence(text: str, lang: str = "") -> str:
    n = max([3] + [len(m) + 1 for m in re.findall(r"`{3,}", text)])
    return f"{'`' * n}{lang}\n{text.rstrip()}\n{'`' * n}\n"


def result_text(content) -> str:
    if isinstance(content, str):
        return content
    return "\n".join(b.get("text", "") if b.get("type") == "text" else f"[{b.get('type')} block]" for b in content or [])


def trace_md(sdir: Path, title: str, score: dict, agent: dict) -> str:
    out = [f"# {title}\n",
           f"Score {score.get('metric')} · check chain {'passed' if score['chain'] else 'failed'} · "
           f"{round((agent.get('seconds') or 0) / 60)} min · ${round(agent.get('cost_usd') or 0, 2)}"
           f"{' · hit the 4-hour limit' if agent.get('timed_out') else ''}\n",
           "## Task\n", fence((sdir / "prompt.txt").read_text(errors="replace"), "text")]
    if (sdir / "protocol.md").is_file():
        out += ["## Protocol (added to the system prompt)\n", fence((sdir / "protocol.md").read_text(errors="replace"), "markdown")]
    out.append("## Trace\n")
    names, step = {}, 0
    for line in (sdir / "agent_stream.jsonl").read_text(errors="replace").splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "assistant":
            for b in ev["message"]["content"]:
                if b.get("type") == "text" and b["text"].strip():
                    step += 1
                    out += [f"### {step}. Agent\n", b["text"].strip() + "\n"]
                elif b.get("type") == "tool_use":
                    step += 1
                    name = b["name"].replace("mcp__heptapod-tools__", "heptapod: ")
                    names[b["id"]] = name
                    inp = b["input"]
                    body = inp["command"] if "command" in inp and set(inp) <= {"command", "description", "timeout"} \
                        else json.dumps(inp, indent=1, ensure_ascii=False)
                    out += [f"### {step}. Tool call: {name}\n", fence(body, "bash" if name == "Bash" else "json")]
        elif ev.get("type") == "user" and isinstance(ev["message"]["content"], list):
            for b in ev["message"]["content"]:
                if b.get("type") == "tool_result":
                    err = " (error)" if b.get("is_error") else ""
                    out += [f"Result of {names.get(b.get('tool_use_id'), 'tool')}{err}:\n", fence(result_text(b.get("content")), "text")]
                elif b.get("type") == "text" and b["text"].startswith("Stop hook feedback"):
                    step += 1
                    out += [f"### {step}. Stop gate (harness)\n", fence(b["text"], "text")]
    final = sdir / "agent_out.md"
    if final.is_file():
        out += ["## Final message\n", final.read_text(errors="replace").strip() + "\n"]
    return "\n".join(out)


def put(z: zipfile.ZipFile, name: str, text: str) -> None:
    info = zipfile.ZipInfo(name, time.localtime()[:6])
    info.compress_type, info.external_attr = zipfile.ZIP_DEFLATED, 0o644 << 16
    z.writestr(info, EMAIL.sub("<email>", text))


def ground_truth(paper: str) -> list[Path]:
    how = json.loads((HERE / "hillclimb" / "ref_ufo" / paper / "how.json").read_text())
    return [Path(f) for f in how["model_files"]]


def main() -> int:
    out = Path(sys.argv[1])
    rows = []
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for model, groups, seeds in MODELS:
            for paper in PAPERS:
                for f in ground_truth(paper):
                    put(z, f"{model}/{paper}/ground_truth_{f.name}", f.read_text(errors="replace"))
                for group, variant in groups:
                    for k in seeds:
                        sdir = RUNS / paper / "rerun" / variant / f"s{k}"
                        agent = json.loads((sdir / "run.json").read_text()).get("agent") or {}
                        frs = sorted((sdir / "model").glob("*.fr"))
                        if len(frs) > 1:
                            raise SystemExit(f"more than one model file: {sdir}")
                        base = f"{model}/{paper}/{group}_s{k}"
                        if frs:
                            put(z, f"{base}_model.fr", frs[0].read_text(errors="replace"))
                        s = R.score_run(sdir, paper)
                        put(z, f"{base}_trace.md", trace_md(sdir, f"{paper} · {model} · {group} · seed {k}", s, agent))
                        rows.append({"model": model, "paper": paper, "group": group, "seed": k, "delivered": bool(frs),
                                     "chain_pass": s["chain"], "score": s.get("metric"), "f1": s.get("f1"),
                                     "precision": s.get("precision"), "recall": s.get("recall"),
                                     "minutes": round((agent.get("seconds") or 0) / 60),
                                     "timed_out": bool(agent.get("timed_out")), "cost_usd": round(agent.get("cost_usd") or 0, 2)})
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
        put(z, "scores.csv", buf.getvalue())
        put(z, "README.md", README)
    print(json.dumps({"zip": str(out), "runs": len(rows), "mb": round(out.stat().st_size / 1e6, 1)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
