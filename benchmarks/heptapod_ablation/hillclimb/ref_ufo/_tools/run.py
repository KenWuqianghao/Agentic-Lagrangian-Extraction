#!/usr/bin/env python3
"""Compile one reference model to a UFO, check the UFO, write <paper>/how.json
and refresh STATUS.md.

    run.py PAPER --files A.fr[,B.fr] --load-sm true|false [--sm-file X] --lag EXPR
           --evidence TXT [--notes TXT] [--extra K=V ...] [--multi] [--no-compile]
    run.py status        # rewrite STATUS.md from the how.json files

A relative --files name is read from REFERENCE_CACHE/PAPER/. --multi loads
several files through compile_multi.wl; otherwise the single-file heptapod
driver compiles the model. --no-compile records the UFO and the log of an
earlier compile again (for example with corrected notes).

External trees (environment):
    REFERENCE_CACHE  the FeynRules database models (default: heptapod's eval/reference_cache)
    FEYNRULES_PATH   FeynRules (set by ~/hep-tools/env.sh)
    HEPVAL_ROOT      the heptapod-dev validator checkout that holds UFO_generator.wl
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
MULTI = TOOLS / "compile_multi.wl"
REF = Path(
    os.environ.get(
        "REFERENCE_CACHE", Path.home() / "Documents/Github/heptapod/eval/reference_cache"
    )
)
FR = Path(os.environ.get("FEYNRULES_PATH", Path.home() / "hep-tools/feynrules-current"))
VALIDATOR = Path(
    os.environ.get("HEPVAL_ROOT", Path.home() / "Documents/Github/hep-pr/validator-main")
)
DRIVER = VALIDATOR / "tools/feynrules/UFO_generator.wl"
ORDER = (
    "ChernSimonsPortal,Top-Philic-Zprime,Wprime,HeavyN,EffLRSM,SMWeinberg,Monotops,"
    "NJLComposite,331,ALRM_general,B-L-SM,GeneralU1,MDMmodel,SLQrules,pNG,pSPSS"
).split(",")
UFO_FILES = ("particles.py", "vertices.py", "couplings.py", "parameters.py")
# By UFO variable name: FeynRules gives the SM ghosts codes 90000xx that collide with model codes.
SM_NAMES = frozenset(
    "a Z W__plus__ W__minus__ g ghA ghZ ghWp ghWm ghG ve vm vt e__minus__ e__plus__ mu__minus__ "
    "mu__plus__ ta__minus__ ta__plus__ u c t d s b H h G0 G__plus__ G__minus__".split()
)


def is_sm(name: str) -> bool:
    return name.replace("__tilde__", "") in SM_NAMES


def check(ufo: Path) -> dict:
    res = {"ok": False, "n_particles": 0, "n_vertices": 0, "problems": []}
    for f in UFO_FILES:
        p = ufo / f
        if not p.is_file():
            res["problems"].append("missing " + f)
            continue
        try:
            compile(p.read_text(errors="replace"), str(p), "exec")
        except SyntaxError as e:
            last = str(e).strip().splitlines()[-1][:200]
            res["problems"].append(f"does not parse: {f}: {last}")
    if any(p.startswith("missing") for p in res["problems"]):
        return res
    ptxt = (ufo / "particles.py").read_text()
    named = re.findall(r"^(\w+)\s*=\s*Particle\(pdg_code\s*=\s*-?\d+", ptxt, re.M)
    res["n_particles"] = len(re.findall(r"^\w+\s*=\s*Particle\(", ptxt, re.M))
    res["bsm_particles"] = sorted(n for n in named if not is_sm(n) and "__tilde__" not in n)
    vtxt = (ufo / "vertices.py").read_text()
    res["n_vertices"] = len(re.findall(r"=\s*Vertex\(", vtxt))
    verts = [re.findall(r"P\.(\w+)", v) for v in re.findall(r"particles\s*=\s*\[([^\]]*)\]", vtxt)]
    bsm = [names for names in verts if any(not is_sm(n) for n in names)]
    res["n_bsm_vertices"] = len(bsm)
    res["example_bsm_vertex"] = bsm[0] if bsm else None
    if not bsm:
        res["problems"].append("no vertex with a non-SM particle")
    res["ok"] = not res["problems"]
    return res


def status() -> None:
    rows = [
        "# Reference UFO compiles",
        "",
        "| paper | ok | load_sm | lagrangian | particles | vertices | BSM vertices | seconds "
        "| notes |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for p in ORDER:
        hp = ROOT / p / "how.json"
        if not hp.is_file():
            rows.append(f"| {p} | Not started | | | | | | | |")
            continue
        h = json.loads(hp.read_text())
        notes = h["notes"].replace("|", "/").replace("\n", " ")
        rows.append(
            f"| {p} | {'ok' if h['ok'] else 'FAILED'} | {h['load_sm']} | `{h['lagrangian']}` "
            f"| {h['n_particles']} | {h['n_vertices']} | {h.get('n_bsm_vertices', '')} "
            f"| {h['seconds']} | {notes} |"
        )
    (ROOT / "STATUS.md").write_text("\n".join(rows) + "\n")


def compile_command(a: argparse.Namespace, files: list[str], ufo: Path) -> list[str]:
    if a.multi:
        return [
            "wolframscript",
            "-f",
            str(MULTI),
            f"FeynRulesPath={FR}",
            "ModelFiles=" + ",".join(files),
            f"OutputDir={ufo}",
            f"Lagrangian={a.lag}",
            *a.extra,
        ]
    return [
        "wolframscript",
        "-f",
        str(DRIVER),
        f"FeynRulesPath={FR}",
        f"ModelPath={files[0]}",
        f"OutputDir={ufo}",
        "Checks=false",
        "AddDecays=false",
        f"LoadSM={a.load_sm}",
        f"Lagrangian={a.lag}",
        *a.extra,
    ]


def main() -> int:
    if sys.argv[1:] == ["status"]:
        status()
        return 0
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("paper")
    ap.add_argument("--files", required=True, help="comma-separated .fr files")
    ap.add_argument("--load-sm", required=True, choices=("true", "false"))
    ap.add_argument(
        "--sm-file",
        help="the SM file to record in how.json (default: FeynRules' SM.fr if --load-sm)",
    )
    ap.add_argument("--lag", default="", help="the total Lagrangian expression")
    ap.add_argument("--evidence", default="")
    ap.add_argument("--notes", default="")
    ap.add_argument("--extra", nargs="*", default=[], help="more K=V arguments for the driver")
    ap.add_argument("--multi", action="store_true", help="compile through compile_multi.wl")
    ap.add_argument("--no-compile", action="store_true")
    a = ap.parse_args()
    d = ROOT / a.paper
    d.mkdir(parents=True, exist_ok=True)
    ufo, log, hp = d / "UFO", d / "compile.log", d / "how.json"
    files = [f if f.startswith("/") else str(REF / a.paper / f) for f in a.files.split(",")]
    load_sm = a.load_sm == "true"
    prev = json.loads(hp.read_text()).get("attempts", []) if hp.is_file() else []
    # A --no-compile record with a Lagrangian replaces the record of that compile.
    if a.no_compile and prev and a.lag:
        prev = prev[:-1]
    secs, rc, cmd = 0, None, None
    if not a.no_compile:
        shutil.rmtree(ufo, ignore_errors=True)
        cmd = compile_command(a, files, ufo)
        t = time.time()
        with open(log, "a") as fh:
            fh.write(f"\n===== attempt {len(prev) + 1}: {' '.join(cmd)}\n")
            fh.flush()
            rc = subprocess.call(
                ["timeout", "-k", "20", "3600", *cmd],
                stdout=fh,
                stderr=subprocess.STDOUT,
                cwd=d,
            )
            secs = round(time.time() - t)
            fh.write(f"\n===== exit code {rc}, {secs} s\n")
    res = (
        check(ufo)
        if ufo.is_dir()
        else {"ok": False, "n_particles": 0, "n_vertices": 0, "problems": ["no UFO directory"]}
    )
    tail = []
    if log.is_file():
        text = log.read_text(errors="replace")
        if a.no_compile:
            m = re.findall(r"===== exit code (\S+), (\d+) s", text)
            if m:
                rc = int(m[-1][0]) if m[-1][0].lstrip("-").isdigit() else None
                secs = int(m[-1][1])
            cm = re.findall(r"===== attempt \d+: (.*)", text)
            cmd = cm[-1] if cm else None
        tail = [ln.rstrip() for ln in text.splitlines() if ln.strip()][-8:]
    ok = bool(res["ok"] and rc == 0 and any("[INFO] Done." in ln for ln in tail))
    att = {
        "lagrangian": a.lag,
        "load_sm": load_sm,
        "model_files": files,
        "extra": a.extra,
        "seconds": secs,
        "exit_code": rc,
        "ok": ok,
        "problems": res["problems"],
    }
    how = {
        "model_files": files,
        "load_sm": load_sm,
        "sm_file": a.sm_file or (str(FR / "Models/SM/SM.fr") if load_sm else None),
        "lagrangian": a.lag,
        "seconds": secs,
        "ok": ok,
        "n_particles": res["n_particles"],
        "n_vertices": res["n_vertices"],
        "n_bsm_vertices": res.get("n_bsm_vertices", 0),
        "bsm_particles": res.get("bsm_particles", []),
        "example_bsm_vertex": res.get("example_bsm_vertex"),
        "evidence": a.evidence,
        "notes": a.notes,
        "extra_args": a.extra,
        "command": cmd,
        "problems": res["problems"],
        "last_log_lines": [] if ok else tail,
        "attempts": [*prev, att],
    }
    hp.write_text(json.dumps(how, indent=1))
    status()
    keys = ("ok", "seconds", "n_particles", "n_vertices", "n_bsm_vertices", "bsm_particles")
    print(json.dumps({k: how[k] for k in (*keys, "example_bsm_vertex", "problems")}))
    if not ok:
        print("\n".join(tail))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
