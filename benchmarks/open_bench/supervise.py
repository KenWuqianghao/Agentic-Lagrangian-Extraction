#!/usr/bin/env python3
"""Finish one arm on the opencode free tier across rate-limit windows.

    supervise.py --model mimo --arm toolkit2 [--jobs 2] [--hours 36]

Loop until every page has a run.json that did not hit the rate limit:
probe the model with a one-line request; when it answers, prepare and run the
pages still missing (open_bench.py run skips finished pages); move every
rate-limited run to s<seed>_infra<N> so it is retried; when the probe is
refused, wait 30 minutes. Uses the same environment as open_bench.py.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import open_bench as ob  # noqa: E402


def probe(model: str) -> bool:
    d = ob.OC_HOME / "probe"
    d.mkdir(parents=True, exist_ok=True)
    env = dict(
        os.environ,
        PWD=str(d),
        HOME=str(ob.OC_HOME),
        XDG_CONFIG_HOME=str(ob.OC_HOME / ".config"),
        XDG_DATA_HOME=str(ob.OC_HOME / ".local/share"),
        XDG_CACHE_HOME=str(ob.OC_HOME / ".cache"),
        OPENCODE_DISABLE_CLAUDE_CODE="1",
    )
    try:
        p = subprocess.run(
            [
                str(ob.OPENCODE),
                "run",
                "--pure",
                "--format",
                "json",
                "--dir",
                str(d),
                "-m",
                ob.MODELS[model],
                "Reply with the single word OK.",
            ],
            cwd=d,
            env=env,
            capture_output=True,
            text=True,
            timeout=300,
            stdin=subprocess.DEVNULL,
        )
    except subprocess.TimeoutExpired:
        return False
    return '"reason":"stop"' in p.stdout and not ob.RATE_LIMIT.search(p.stdout)


def clean_done(page: str, model: str, arm: str, seed: int) -> bool:
    run = ob.rundir(page, model, arm, seed) / "run.json"
    return run.is_file() and not json.loads(run.read_text()).get("rate_limited")


def archive_rate_limited(model: str, arm: str, seed: int) -> list[str]:
    moved = []
    for page in ob.PAGES16:
        rd = ob.rundir(page, model, arm, seed)
        run = rd / "run.json"
        if run.is_file() and json.loads(run.read_text()).get("rate_limited"):
            n = 1
            while (rd.parent / f"s{seed}_infra{n}").exists():
                n += 1
            rd.rename(rd.parent / f"s{seed}_infra{n}")
            moved.append(page)
    return moved


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, choices=sorted(ob.MODELS))
    ap.add_argument("--arm", required=True, choices=["hand", "toolkit", "toolkit2"])
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--jobs", type=int, default=2)
    ap.add_argument("--hours", type=float, default=36)
    a = ap.parse_args()
    deadline = time.time() + a.hours * 3600
    while time.time() < deadline:
        todo = [p for p in ob.PAGES16 if not clean_done(p, a.model, a.arm, a.seed)]
        if not todo:
            print(f"[supervise] {a.model} {a.arm}: all {len(ob.PAGES16)} pages done", flush=True)
            return 0
        if not probe(a.model):
            print(
                f"[supervise] {time.strftime('%H:%M')} {a.model}: probe refused, "
                f"{len(todo)} pages left; waiting 30 min",
                flush=True,
            )
            time.sleep(1800)
            continue
        print(
            f"[supervise] {time.strftime('%H:%M')} {a.model}: probe ok, running "
            f"{len(todo)} pages: {','.join(todo)}",
            flush=True,
        )
        pages = ",".join(todo)
        cli = [sys.executable, str(HERE / "open_bench.py")]
        subprocess.run(
            cli
            + [
                "prepare",
                "--model",
                a.model,
                "--arm",
                a.arm,
                "--pages",
                pages,
                "--seed",
                str(a.seed),
            ],
            check=True,
        )
        subprocess.run(
            cli
            + [
                "run",
                "--model",
                a.model,
                "--arm",
                a.arm,
                "--pages",
                pages,
                "--seed",
                str(a.seed),
                "--jobs",
                str(a.jobs),
            ]
        )
        moved = archive_rate_limited(a.model, a.arm, a.seed)
        if moved:
            print(f"[supervise] rate-limited, archived for retry: {','.join(moved)}", flush=True)
    print(f"[supervise] {a.model} {a.arm}: deadline reached", flush=True)
    return 1


if __name__ == "__main__":
    sys.exit(main())
