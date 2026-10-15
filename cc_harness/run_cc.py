#!/usr/bin/env python3
"""Run Claude Code (headless `claude -p`) as the extraction agent, with the
heptapod chain in its loop, on the benchmark papers; then score it like every
other arm.

    run_cc.py check                               # claude -p answers? (login)
    run_cc.py run   --variant cc_sonnet_harness --pages pNG --model claude-sonnet-5
    run_cc.py score --variants cc_sonnet_harness --pages all
    run_cc.py report --variants v3s_notools,pi_qwen_harness,cc_sonnet_harness --pages all

`--arm` selects an ablation arm (common.ARMS): which MCP tools exist and what
validate_model shows. The default, `full`, is the harness described here.
`--draft-from VARIANT` starts the agent from a stored first draft of that
variant (its first validated file, else its delivered file) instead of an
empty directory: arms then differ only in the feedback on the same file.

One agent per paper, in its own sandbox (a temp dir with the paper, SM.fr and
the model.fr it writes; nothing else):

  --tools Read,Write,Edit,Glob,Grep     the only built-in tools
  --disallowedTools Bash,WebFetch,...   and a deny list, belt and braces
  --mcp-config (strict)                 only heptapod-tools: lint_model,
                                        validate_model, massbasis, review_model
  --settings                            the hooks: PreToolUse sandbox guard,
                                        Stop gate (no finishing with a failing
                                        model, at most 3 continuations)
  --setting-sources ''                  none of the operator's CLAUDE.md, hooks
                                        or settings reach the agent
  --append-system-prompt-file           prompts/protocol.md

The task prompt is pi_harness/run_pi.py's harness prompt (the v3 task text,
paper path, sandbox note, v3 addendum), on stdin. Directories follow
run_pi.py (RUNS/<page>/rerun/<variant>/s<k>/); `score` is run_pi's scorer
(hepval, pristine heptapod-dev main driver, serial), so every arm has one
scorer.
"""

from __future__ import annotations

import argparse
import contextlib
import json
import os
import shlex
import shutil
import statistics
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "pi_harness"))
import common as C  # noqa: E402
import isolation  # noqa: E402
import run_pi  # noqa: E402

RUNS = run_pi.RUNS
PROTOCOL = HERE / "prompts" / "protocol.md"
AGENT_TIMEOUT = int(os.environ.get("CC_AGENT_TIMEOUT", str(4 * 3600)))
BUILTIN_TOOLS = "Read,Write,Edit,Glob,Grep"
DISALLOWED = "Bash,WebFetch,WebSearch,Task,Agent,NotebookEdit"
# The stored runs that drafts come from; RUNS may be a fresh tree (runs_root.sh).
DRAFT_RUNS = Path(
    os.environ.get("CC_DRAFT_RUNS", Path.home() / "Documents/Github/heptapod/eval/benchmark_runs")
)
DRAFT_NOTE = """\
DRAFT: model.fr in the working directory is a first draft of this model from an earlier
attempt. It does not pass the chain. Check it against the paper, repair it, and hand in the
repaired model.fr. You may change or rewrite any part of it."""


def _pages(arg: str) -> list[str]:
    return [p for p in (run_pi.SINGLE_MODEL if arg == "all" else arg).split(",") if p]


def cmd_check(args) -> int:
    """A minimal `claude -p` with the absolute path: is the CLI logged in?"""
    r = subprocess.run(
        [
            "perl",
            "-e",
            "alarm 180; exec @ARGV",
            C.CLAUDE,
            "-p",
            "--model",
            args.model,
            "--output-format",
            "json",
            "Reply with the single word OK",
        ],
        capture_output=True,
        text=True,
        cwd=tempfile.gettempdir(),
        stdin=subprocess.DEVNULL,
    )
    try:
        out = json.loads(r.stdout)
    except json.JSONDecodeError:
        out = {}
    ok = r.returncode == 0 and not out.get("is_error") and "OK" in (out.get("result") or "")
    print(
        json.dumps(
            {
                "claude": C.CLAUDE,
                "model": args.model,
                "exit": r.returncode,
                "logged_in": ok,
                "result": (out.get("result") or r.stdout or r.stderr)[:300],
            },
            indent=1,
        )
    )
    return 0 if ok else 1


def draft_file(page: str, variant: str) -> Path:
    """The first file a stored run had validated, or the file it delivered."""
    d = DRAFT_RUNS / page / "rerun" / variant / "s1"
    for f in (d / "validation" / "call1" / "model.fr", d / "model" / f"{page}_gen.fr"):
        if f.is_file():
            return f
    raise FileNotFoundError(f"no stored draft for {page} in {variant} under {DRAFT_RUNS}")


def make_sandbox(page: str, rundir: Path, draft: Path | None = None) -> Path:
    """The paper and SM.fr (and the draft, as model.fr), nothing else; outside
    the repo (a sandbox path that names the repo invites reads through the
    real path)."""
    sb = Path(tempfile.mkdtemp(prefix=f"cc-{page}-")).resolve()
    paper = run_pi.paper_file(page)
    dst = sb / "eval" / "benchmark_runs" / page / "text" / paper.name
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(paper, dst)
    shutil.copy2(run_pi.SM_FR, sb / "SM.fr")
    if draft:
        shutil.copy2(draft, sb / "model.fr")
    (rundir / "sandbox_path.txt").write_text(str(sb))
    return sb


SHELL_NOTE = """\
SANDBOX: the working directory contains the paper (under eval/benchmark_runs/), SM.fr (the
Standard Model file this add-on is loaded on top of: take field names, index conventions and
hypercharges from it), and what you write. You have a shell: wolframscript, FeynRules
($FEYNRULES_PATH) and MadGraph ($MG5_PATH) are installed. Do not use the network."""


def cc_env(rundir: Path, sandbox: Path, args) -> dict:
    """The settings that the MCP server and the hooks read from their environment."""
    return {
        "CC_SANDBOX": str(sandbox),
        "CC_RUNDIR": str(rundir),
        "CC_VALIDATE_BUDGET": str(args.validate_budget),
        "CC_REVIEW_BUDGET": str(args.review_budget),
        "CC_MAX_CONTINUATIONS": str(args.max_continuations),
        "CC_AGENT_MODEL": args.model,
        "CC_REVIEW_MODEL": args.review_model or args.model,
        "CC_PYTHON": sys.executable,
        "CC_ARM": args.arm,
        # The validator's settings (compile time limit, tree, lock) must be
        # the runner's: the MCP server does not get them any other way.
        **{k: v for k, v in os.environ.items() if k.startswith("HEPVAL_")},
    }


def harness_commands() -> dict[str, list[str]]:
    """What a shell arm's Broker serves: the MCP server and the Stop hook."""
    py = sys.executable
    return {
        "mcp": [py, str(HERE / "heptapod_mcp.py")],
        "stop": [py, str(HERE / "hooks" / "stop_gate.py")],
    }


def write_configs(rundir: Path, args, env: dict, broker: isolation.Broker | None = None) -> None:
    """settings.json, mcp.json and protocol.md. A shell arm reaches its MCP
    server and Stop hook through `broker`, because inside its sandbox it could
    change their state."""
    py = sys.executable
    arm = C.arm(args.arm)
    if arm.shell and broker is None:
        raise ValueError("a shell arm needs a Broker")
    # With a shell the PreToolUse guard cannot confine anything: isolation.py does.
    hooks = (
        {}
        if arm.shell
        else {
            "PreToolUse": [
                {
                    "matcher": "*",
                    "hooks": [
                        {
                            "type": "command",
                            "command": f"{py} {HERE / 'hooks' / 'pretool_guard.py'}",
                        }
                    ],
                }
            ]
        }
    )
    if "validate_model" in arm.tools:
        # The gate asks for a validate_model verdict; without the tool there is none to ask for.
        stop = broker.shell_command("stop") if arm.shell else shlex.join(harness_commands()["stop"])
        hooks["Stop"] = [{"hooks": [{"type": "command", "command": stop}]}]
    denied = ["WebFetch", "WebSearch", "Task", "Agent"] + ([] if arm.shell else ["Bash"])
    settings = {"env": env, "permissions": {"deny": denied}, "hooks": hooks}
    if not arm.tools:
        servers = {}
    elif arm.shell:
        proxy = broker.command("mcp")
        servers = {C.SERVER_NAME: {"type": "stdio", "command": proxy[0], "args": proxy[1:]}}
    else:
        mcp = harness_commands()["mcp"]
        servers = {C.SERVER_NAME: {"type": "stdio", "command": mcp[0], "args": mcp[1:], "env": env}}
    (rundir / "settings.json").write_text(json.dumps(settings, indent=1))
    (rundir / "mcp.json").write_text(json.dumps({"mcpServers": servers}, indent=1))
    (rundir / "protocol.md").write_text(
        C.render_protocol(
            PROTOCOL.read_text(),
            arm,
            args.validate_budget,
            args.max_continuations,
            rundir=str(rundir),
        )
    )


NO_GAUGE_GROUPS = "SM add-on => no M$GaugeGroups block; "
GAUGE_GROUPS_ALLOWED = (
    "SM add-on: SM.fr declares the SM gauge groups; add an M$GaugeGroups block only for a gauge "
    "group that the paper adds (see the protocol); "
)


def task_prompt(page: str, arm: C.Arm, draft: bool = False) -> str:
    """run_pi's harness prompt; an arm without validate_model has no verdict
    to summarise, a run that starts from a draft is told so, and the shell
    arm is not told that it has no shell."""
    prompt = run_pi.build_prompt(page, "harness")
    if arm.shell:
        if run_pi.SANDBOX_NOTE not in prompt:
            raise ValueError("task prompt: the sandbox note is not where it was")
        prompt = prompt.replace(run_pi.SANDBOX_NOTE, SHELL_NOTE)
    if arm.recipes:
        if NO_GAUGE_GROUPS not in prompt:
            raise ValueError("task prompt: the gauge-group rule is not where it was")
        prompt = prompt.replace(NO_GAUGE_GROUPS, GAUGE_GROUPS_ALLOWED)
    if "validate_model" not in arm.tools:
        tail = " and the last validate_model verdict."
        if tail not in prompt:
            raise ValueError("task prompt: the validate_model sentence is not where it was")
        prompt = prompt.replace(tail, ".")
    return prompt + ("\n" + DRAFT_NOTE + "\n" if draft else "")


def agent_cmd(
    rundir: Path, model: str, arm: C.Arm, sandbox: Path | None = None, ctl: Path | None = None
) -> list[str]:
    """The claude command line; a shell arm's runs in isolation and reads its run directory
    and the Broker's directory `ctl` but cannot write them."""
    if arm.shell:
        cmd = [
            C.CLAUDE,
            "-p",
            "--output-format",
            "stream-json",
            "--verbose",
            "--model",
            model,
            "--setting-sources",
            "",
            "--settings",
            str(rundir / "settings.json"),
            "--mcp-config",
            str(rundir / "mcp.json"),
            "--strict-mcp-config",
            "--permission-mode",
            "bypassPermissions",
            "--append-system-prompt-file",
            str(rundir / "protocol.md"),
            # The wait tools let a headless agent end its turn "to wait"; the session then ends.
            "--disallowedTools",
            "WebFetch,WebSearch,Task,Agent"
            + (",Monitor,ScheduleWakeup,CronCreate" if arm.feedback == "cover" else ""),
        ]
        from hepval import STATE  # the kernel lock the wrapper and hepval share

        return isolation.isolate(cmd, sandbox, read_only=(rundir, ctl), read_write=(STATE,))
    return [
        C.CLAUDE,
        "-p",
        "--output-format",
        "stream-json",
        "--verbose",
        "--model",
        model,
        "--setting-sources",
        "",
        "--settings",
        str(rundir / "settings.json"),
        "--mcp-config",
        str(rundir / "mcp.json"),
        "--strict-mcp-config",
        "--tools",
        BUILTIN_TOOLS,
        "--allowedTools",
        ",".join((BUILTIN_TOOLS, *C.mcp_tool_names(arm))),
        "--permission-mode",
        "dontAsk",
        "--append-system-prompt-file",
        str(rundir / "protocol.md"),
        # Variadic: it must come last, and the prompt goes on stdin.
        "--disallowedTools",
        DISALLOWED,
    ]


def parse_stream(lines: list[str]) -> dict:
    tools: list[str] = []
    seen_msgs: dict = {}
    results, init = [], {}
    final = ""
    for line in lines:
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        t = ev.get("type")
        if t == "system" and ev.get("subtype") == "init":
            init = {
                "model": ev.get("model"),
                "tools": ev.get("tools"),
                "mcp_servers": ev.get("mcp_servers"),
                "permission_mode": ev.get("permissionMode"),
            }
        elif t == "assistant":
            m = ev.get("message") or {}
            for b in m.get("content") or []:
                if b.get("type") == "tool_use":
                    tools.append(b.get("name"))
                elif b.get("type") == "text" and b.get("text", "").strip():
                    final = b["text"]
            if m.get("id") and m.get("usage"):
                seen_msgs[m["id"]] = m["usage"]
        elif t == "result":
            results.append(ev)
    # The result event carries the session's cumulative usage; per-message
    # usage in the stream is a partial snapshot (output_tokens of 2 or 17).
    last = results[-1] if results else {}
    ru = last.get("usage") or {}
    usage = {
        k: int(ru.get(k) or 0)
        for k in (
            "input_tokens",
            "cache_creation_input_tokens",
            "cache_read_input_tokens",
            "output_tokens",
        )
    }
    usage["thinking_tokens"] = int(
        (ru.get("output_tokens_details") or {}).get("thinking_tokens") or 0
    )
    usage["input_total"] = (
        usage["input_tokens"]
        + usage["cache_creation_input_tokens"]
        + usage["cache_read_input_tokens"]
    )
    usage["per_result_event"] = [
        {
            k: (r.get("usage") or {}).get(k)
            for k in ("input_tokens", "cache_read_input_tokens", "output_tokens")
        }
        for r in results
    ]
    return {
        "tools": tools,
        "usage": usage,
        "n_api_calls": len(seen_msgs),
        "cost_usd": float(last.get("total_cost_usd") or 0),
        "result_usage": last.get("usage"),
        "num_turns": last.get("num_turns"),
        "duration_ms": last.get("duration_ms"),
        "is_error": last.get("is_error"),
        "result_subtype": last.get("subtype"),
        "n_result_events": len(results),
        "final_text": last.get("result") or final,
        "init": init,
        # A session that ends on an API error (the 64k output cap, a
        # transport error) never reaches the Stop hook.
        "api_error": (last.get("result") or "")[:300] if last.get("is_error") else None,
    }


def run_agent(page: str, seed: int, args) -> dict:
    rundir = RUNS / page / "rerun" / args.variant / f"s{seed}"
    if (rundir / "run.json").is_file() and not args.force:
        prev = json.loads((rundir / "run.json").read_text())
        if (prev.get("agent") or {}).get("ok"):
            print(f"[cc] skip {page} s{seed}: done", flush=True)
            return prev
    if rundir.exists():
        shutil.rmtree(rundir)
    rundir.mkdir(parents=True)
    draft = draft_file(page, args.draft_from) if args.draft_from else None
    sandbox = make_sandbox(page, rundir, draft)
    arm = C.arm(args.arm)
    prompt = task_prompt(page, arm, draft=bool(draft))
    (rundir / "prompt.txt").write_text(prompt)
    env_cc = cc_env(rundir, sandbox, args)
    env = {
        **os.environ,
        **env_cc,
        # validate_model can hold the tool call for one queued compile plus
        # its own (2 x 900 s): the default MCP tool timeout is far shorter.
        "MCP_TOOL_TIMEOUT": str(3 * 3600 * 1000),
        "MCP_TIMEOUT": "60000",
    }
    if arm.shell:
        from hepval import LOCK

        wrapper_dir = isolation.write_wolframscript_wrapper(sandbox, LOCK)
        env.update(
            {
                "PATH": f"{wrapper_dir}:{os.environ['PATH']}",
                "FEYNRULES_PATH": str(isolation.FEYNRULES),
                "MG5_PATH": str(isolation.MG5),
            }
        )
    if args.max_output_tokens:
        env["CLAUDE_CODE_MAX_OUTPUT_TOKENS"] = str(args.max_output_tokens)
    broker = (
        isolation.Broker(
            harness_commands(), {**os.environ, **env_cc}, rundir / "harness_stderr.txt"
        )
        if arm.shell
        else contextlib.nullcontext()
    )
    print(f"[cc] {args.variant} {page} s{seed} ...", flush=True)
    t0 = time.time()
    with (
        broker,
        open(rundir / "agent_stream.jsonl", "w") as out,
        open(rundir / "agent_stderr.txt", "w") as err,
    ):
        ctl = broker.dir if arm.shell else None
        write_configs(rundir, args, env_cc, broker if arm.shell else None)
        cmd = agent_cmd(rundir, args.model, arm, sandbox, ctl)
        (rundir / "command.json").write_text(json.dumps(cmd, indent=1))
        rc, timed_out = isolation.run(cmd, sandbox, env, prompt, out, err, AGENT_TIMEOUT)
    return finalize(page, seed, args, rundir, sandbox, rc, round(time.time() - t0, 1), timed_out)


def _jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    out = []
    for x in path.read_text().splitlines():
        try:
            out.append(json.loads(x))
        except json.JSONDecodeError:
            pass
    return out


def finalize(
    page: str,
    seed: int,
    args,
    rundir: Path,
    sandbox: Path,
    rc: int,
    secs: float | None,
    timed_out: bool,
) -> dict:
    parsed = parse_stream((rundir / "agent_stream.jsonl").read_text(errors="replace").splitlines())
    if secs is None and parsed.get("duration_ms"):
        # A rebuilt run.json has no runner clock: take the CLI's own wall time.
        secs = round(parsed["duration_ms"] / 1000, 1)
    (rundir / "agent_out.md").write_text(parsed["final_text"] or "")
    fr_dst = rundir / "model" / f"{page}_gen.fr"
    fr_dst.parent.mkdir(parents=True, exist_ok=True)
    src = sandbox / "model.fr"
    delivered = src.is_file()
    if delivered:
        shutil.copy2(src, fr_dst)
    state = C.load_state(rundir)
    hooks = _jsonl(rundir / "hook_log.jsonl")
    denied = [h for h in hooks if h.get("decision") == "deny"]
    gate = _jsonl(rundir / "stop_gate_log.jsonl")
    reviews = []
    for m in (
        sorted((rundir / "review").glob("review*_meta.json"))
        if (rundir / "review").is_dir()
        else []
    ):
        meta = json.loads(m.read_text())
        n = m.name.split("_")[0][6:]
        txt = (
            (rundir / "review" / f"review{n}.md").read_text()
            if (rundir / "review" / f"review{n}.md").is_file()
            else ""
        )
        reviews.append(
            {
                "n": int(n),
                "verdict": C.verdict_line(txt),
                "exit": meta.get("exit"),
                "seconds": meta.get("seconds"),
                "cost_usd": meta.get("total_cost_usd"),
                "usage": meta.get("usage"),
                "reviewed_final_model": meta.get("model_sha") == C.sha(src),
            }
        )
    names = parsed["tools"]
    counts = {n: names.count(n) for n in sorted(set(names))}
    short = {k.replace(f"mcp__{C.SERVER_NAME}__", ""): v for k, v in counts.items()}
    agent = {
        "ok": rc == 0 and delivered and not timed_out,
        "exit": rc,
        "timed_out": timed_out,
        "seconds": secs,
        "engine": "claude-code",
        "claude_bin": C.CLAUDE,
        "claude_version": subprocess.run(
            [C.CLAUDE, "--version"], capture_output=True, text=True
        ).stdout.strip(),
        "model": args.model,
        "review_model": args.review_model or args.model,
        "arm": "harness",
        "ablation_arm": args.arm,
        "draft_from": getattr(args, "draft_from", "") or None,
        "mode": "cc_harness",
        "tool_policy": "enforced (--tools allow-list, --disallowedTools, PreToolUse sandbox guard, "
        "strict MCP)",
        # A denied call never ran, so nothing outside the sandbox was read; the
        # audit is clean only if nothing had to be denied at all.
        "audit_ok": not denied,
        "n_path_denied": sum("outside the sandbox" in str(d.get("reason")) for d in denied),
        "blocked": [
            {"tool": d.get("tool"), "reason": d.get("reason"), "input": d.get("input")}
            for d in denied
        ][:30],
        "n_blocked": len(denied),
        "contaminated": False,
        "read_paper": any(
            "text/" in json.dumps(h.get("input")) for h in hooks if h.get("tool") == "Read"
        ),
        "usage": parsed["usage"],
        "cost_usd": parsed["cost_usd"],
        "n_api_calls": parsed["n_api_calls"],
        "num_turns": parsed["num_turns"],
        "result_subtype": parsed["result_subtype"],
        "is_error": parsed["is_error"],
        "n_result_events": parsed["n_result_events"],
        "api_error": parsed["api_error"],
        "max_output_tokens": getattr(args, "max_output_tokens", None) or "CLI default (64000)",
        "tool_counts": short,
        "n_tool_calls": len(names),
        "n_validate": state.get("validations"),
        "n_review": state.get("reviews"),
        "validate_budget": args.validate_budget,
        "review_budget": args.review_budget,
        "last_inloop": state.get("last_validation"),
        "reviews": reviews,
        "stop_gate": {
            "blocks": sum(g.get("decision") == "block" for g in gate),
            "decisions": [
                {
                    k: g.get(k)
                    for k in ("decision", "why", "stop_hook_active", "continuations_before")
                }
                for g in gate
            ],
        },
        "init": parsed["init"],
    }
    row = {
        "page": page,
        "variant": args.variant,
        "seed": seed,
        "mode": agent["mode"],
        "paper_source": "tex" if run_pi.paper_file(page).name.endswith("_source.tex") else "txt",
        "paper_file": run_pi.paper_file(page).name,
        "agent": agent,
        "render": {"rendered": delivered, "fr": str(fr_dst) if delivered else None},
    }
    (rundir / "run.json").write_text(json.dumps(row, indent=1, default=str))
    u = parsed["usage"]
    print(
        f"[cc]   {page} s{seed}: ok={agent['ok']} delivered={delivered} {secs}s "
        f"validate={state.get('validations')} review={state.get('reviews')} "
        f"gate_blocks={agent['stop_gate']['blocks']} in={u['input_total']:,} "
        f"out={u['output_tokens']:,} ${parsed['cost_usd']:.2f}",
        flush=True,
    )
    return row


def cmd_run(args) -> int:
    jobs = [(p, k) for p in _pages(args.pages) for k in range(args.first_seed, args.seeds + 1)]
    with ThreadPoolExecutor(max_workers=max(1, args.parallel)) as ex:
        list(ex.map(lambda j: run_agent(j[0], j[1], args), jobs))
    return 0


def cmd_finalize(args) -> int:
    for page in _pages(args.pages):
        rundir = RUNS / page / "rerun" / args.variant / f"s{args.seed}"
        sandbox = Path((rundir / "sandbox_path.txt").read_text().strip())
        finalize(page, args.seed, args, rundir, sandbox, 0, None, False)
    return 0


def cmd_score(args) -> int:
    """run_pi's scorer, unchanged. run_pi writes validation.json only for
    pi_ variants; the cc arm gets the same copy so ablation_report reads it."""
    rc = run_pi.cmd_score(args)
    for v in args.variants.split(","):
        if not v.startswith("cc_"):
            continue
        for page in _pages(args.pages):
            for k in range(1, args.seeds + 1):
                d = RUNS / page / "rerun" / v / f"s{k}"
                if (d / "validation_hepval.json").is_file():
                    shutil.copy2(d / "validation_hepval.json", d / "validation.json")
    return rc


def cmd_usage(args) -> int:
    """Tokens and wall time per paper, agent plus referee."""
    rows = []
    for page in _pages(args.pages):
        d = RUNS / page / "rerun" / args.variant / "s1"
        if not (d / "run.json").is_file():
            continue
        a = json.loads((d / "run.json").read_text())["agent"]
        rev_in = sum(
            int((r.get("usage") or {}).get(k) or 0)
            for r in a.get("reviews") or []
            for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")
        )
        rows.append(
            {
                "page": page,
                "minutes": round((a.get("seconds") or 0) / 60, 1),
                "input_total": a["usage"]["input_total"],
                "input_uncached": a["usage"]["input_tokens"]
                + a["usage"]["cache_creation_input_tokens"],
                "output": a["usage"]["output_tokens"],
                "referee_input_total": rev_in,
                "cost_usd": round(
                    (a.get("cost_usd") or 0)
                    + sum(float(r.get("cost_usd") or 0) for r in a.get("reviews") or []),
                    2,
                ),
                "validate": a.get("n_validate"),
                "review": a.get("n_review"),
                "gate_blocks": (a.get("stop_gate") or {}).get("blocks"),
            }
        )
    med = (
        {k: statistics.median([r[k] for r in rows]) for k in ("minutes", "input_total", "output")}
        if rows
        else {}
    )
    print(json.dumps({"variant": args.variant, "rows": rows, "median": med}, indent=1))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("--model", default="claude-sonnet-5")
    c.set_defaults(fn=cmd_check)
    r = sub.add_parser("run")
    r.add_argument("--variant", default="cc_sonnet_harness")
    r.add_argument(
        "--arm",
        default="full",
        choices=sorted(C.ARMS),
        help="ablation arm: the MCP tools the agent has and what validate_model shows",
    )
    r.add_argument(
        "--draft-from",
        default="",
        metavar="VARIANT",
        help="start from the stored first draft of this variant (repair design)",
    )
    r.add_argument(
        "--pages", required=True, help="comma-separated, or 'all' for the 16 single-model papers"
    )
    r.add_argument("--model", default="claude-sonnet-5")
    r.add_argument("--review-model", default="")
    r.add_argument("--seeds", type=int, default=1)
    r.add_argument(
        "--first-seed",
        type=int,
        default=1,
        help="run seeds first-seed..seeds: a later batch must not touch the earlier seeds "
        "(a run that failed is run again when its seed is in range)",
    )
    r.add_argument("--parallel", type=int, default=4)
    r.add_argument("--validate-budget", type=int, default=10)
    r.add_argument("--review-budget", type=int, default=2)
    r.add_argument("--max-continuations", type=int, default=3)
    r.add_argument(
        "--max-output-tokens",
        type=int,
        default=0,
        help="CLAUDE_CODE_MAX_OUTPUT_TOKENS for the agent; 0 = the CLI default (64000)",
    )
    r.add_argument("--force", action="store_true")
    r.set_defaults(fn=cmd_run)
    f = sub.add_parser("finalize", help="rebuild run.json after a runner crash")
    f.add_argument("--variant", default="cc_sonnet_harness")
    f.add_argument("--arm", default="full", choices=sorted(C.ARMS))
    f.add_argument("--pages", required=True)
    f.add_argument("--seed", type=int, default=1)
    f.add_argument("--model", default="claude-sonnet-5")
    f.add_argument("--review-model", default="")
    f.add_argument("--validate-budget", type=int, default=10)
    f.add_argument("--review-budget", type=int, default=2)
    f.set_defaults(fn=cmd_finalize)
    s = sub.add_parser("score")
    s.add_argument("--variants", required=True)
    s.add_argument("--pages", required=True)
    s.add_argument("--seeds", type=int, default=1)
    s.add_argument("--force", action="store_true")
    s.set_defaults(fn=cmd_score)
    u = sub.add_parser("usage")
    u.add_argument("--variant", default="cc_sonnet_harness")
    u.add_argument("--pages", default="all")
    u.set_defaults(fn=cmd_usage)
    p = sub.add_parser("report")
    p.add_argument("--variants", required=True)
    p.add_argument("--pages", required=True)
    p.set_defaults(fn=run_pi.cmd_report)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
