#!/usr/bin/env python3
"""
# validation_benchmark.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Validation-augmented benchmark.

The prior db_benchmark scored agent-generated .fr files ONLY on field-content
fidelity vs the physicist's reference (name-independent signatures). It never
compiled anything. This benchmark runs each agent-generated .fr through the
REAL downstream tool chain now that a licence-free Wolfram Engine + FeynRules +
MadGraph are available:

    agent .fr  --(FeynRules/Wolfram)-->  UFO  --(MadGraph)-->  import model

and reports, per model and in aggregate:
  * compile_ok            : did FeynRules WriteUFO produce a UFO?
  * checks                : FeynRules consistency-check verdicts, read from each
                            check's return value (pass / fail / inconclusive)
  * n_new_particles       : new (BSM) particle classes that reached the UFO
  * madgraph_import_ok    : does MadGraph load the generated UFO?

This is a strictly stronger signal than field F1: a model can have the right
field content yet fail to compile (bad FeynRules syntax) or fail to load in
MadGraph (malformed UFO). Failures are rows, not omissions.

Usage:
    python eval/benchmark_runs/validation_benchmark.py [page1,page2,...]
    python eval/benchmark_runs/validation_benchmark.py --all
"""

from __future__ import annotations

import json
import os
import re
import signal
import subprocess
import sys
import threading
import time
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO))

import config  # noqa: E402
from tools.feynrules.lagrangian_checks import PASS, parse_check_verdicts  # noqa: E402
from tools.frgen.fr_parser import parse_lagrangian_terms  # noqa: E402

DRIVER = REPO / "tools" / "feynrules" / "UFO_generator.wl"
MG5 = Path(config.mg5_path) / "bin" / "mg5_aMC"
SM_FR = REPO / "tools" / "feynrules" / "test_files" / "models" / "SM.fr"
OUTROOT = Path(os.environ.get("VBENCH_OUT", "/tmp/vbench"))

COMPILE_TIMEOUT = int(os.environ.get("VBENCH_COMPILE_TIMEOUT", "420"))
MG5_TIMEOUT = int(os.environ.get("VBENCH_MG5_TIMEOUT", "240"))

# The four checks UFO_generator.wl runs by default. Each passes for the
# Standard Model alone, so a failure is about the model under test.
CHECK_KEYS = ("hermiticity", "kinetic_diagonal", "mass_diagonal", "mass_spectrum")


def all_checks_pass(checks: dict | None) -> bool:
    """True only when every default check returned an affirmative verdict.

    Inconclusive is not a pass, and a check that did not run is not a pass.
    Verdicts stored before 2026-09-13 came from a prose classifier that could
    not report a failure, which is why this is the only definition used.
    """
    checks = checks or {}
    return all(checks.get(k) == PASS for k in CHECK_KEYS)

# A diverse default subset spanning colour reps, spins, and gauge extensions.
DEFAULT_SUBSET = [
    "LeptoQuark", "DMsimp", "B-L-SM", "HeavyN", "Sextets",
    "Top-Philic-Zprime", "Triplets", "VLQ", "Wprime", "GeneralU1",
]


_IDENT_RE = re.compile(r"\b([A-Za-z][A-Za-z0-9$]*)\b")


def total_lag_symbol(fr_path: Path) -> tuple[str | None, dict]:
    """The model's grand-total Lagrangian, resolved by reference analysis.

    This used to take the LAST top-level ``L... =`` line in the file. That is
    a guess about file order, and it was wrong for 11 of the 28 benchmark
    models: it selected a sub-Lagrangian, FeynRules compiled that fragment
    alone, and the fragment still passed every Hermiticity / kinetic / mass
    check and imported into MadGraph. Models counted as passing with most of
    their physics missing — VLQ compiled 1 of its 11 Lagrangian terms.

    Instead: build the reference graph over top-level ``L*`` assignments and
    take the **roots**, the terms no other term refers to.

    Exactly one root is the normal case, and it is the total.

    Several roots means the model never declared a single total, and the
    harness genuinely cannot know which is intended. Summing them is NOT a
    safe fallback: roots are independent only as *symbols*, not as physics.
    ChernSimonsPortal defines `LChernSimonsPortal` (symmetric phase, in H and
    the B/Wi field strengths) and `LChernSimonsPortalBroken` (the same
    operator expanded in Z/A/W mass eigenstates) — adding them double-counts
    the interaction. So ambiguity is reported, not resolved, and the model is
    left unscored until someone declares the total. `lag_overrides.json` maps
    page -> symbol for exactly that purpose.

    Returns ``(symbol_or_None, info)``; a None symbol with ``ambiguous`` set
    means "unscoreable", which is different from "failed".
    """
    text = fr_path.read_text(errors="replace")
    try:
        terms = parse_lagrangian_terms(text)
    except Exception as e:                                    # noqa: BLE001
        return None, {"roots": [], "ambiguous": False, "parse_error": str(e)}
    body = {t["name"]: t["expression"] for t in terms if t["name"].startswith("L")}
    if not body:
        return None, {"roots": [], "ambiguous": False}

    referenced: set[str] = set()
    for name, expr in body.items():
        for tok in _IDENT_RE.findall(expr):
            if tok in body and tok != name:
                referenced.add(tok)
    roots = [n for n in body if n not in referenced]

    # what the old positional rule would have picked, kept for the report
    legacy = None
    for line in text.splitlines():
        m = re.match(r"^(L[A-Za-z0-9]*)\s*:?=", line)
        if m:
            legacy = m.group(1)

    roots, dropped = _drop_redundant_roots(roots, body)
    info = {"roots": roots, "legacy_symbol": legacy,
            "n_terms_defined": len(body), "ambiguous": False}
    if dropped:
        info["redundant_roots"] = dropped

    if not roots:                        # every term referenced => cycle
        info.update({"ambiguous": True, "cyclic": True})
        return None, info

    # An explicit human declaration always wins.
    override = _lag_override(fr_path)
    if override:
        info.update({"override": override,
                     "changed_from_legacy": override != legacy})
        return override, info

    if len(roots) > 1:
        info["ambiguous"] = True
        return None, info

    info["changed_from_legacy"] = roots[0] != legacy
    return roots[0], info


_ALIAS_LEFTOVER_RE = re.compile(r"[\s+\-()]")
_ROOT_NAME_PREFERENCE = ("LTot", "LFull", "LBSM", "LTotal")


def _reach(start: str, body: dict) -> set:
    seen, stack = set(), [start]
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)
        for tok in _IDENT_RE.findall(body.get(cur, "")):
            if tok in body:
                stack.append(tok)
    return seen


def _is_pure_alias(name: str, body: dict) -> bool:
    """True when a term is only a sum of other terms, contributing no physics.

    ``LD := LD1 + LD2 + LD3`` is a pure alias. ``LSextet := LSextetKin + LD1 +
    ... + LPot`` is too. Anything with real operators left over after removing
    term names and ``+ - ( )`` is not.
    """
    expr = body.get(name, "")
    for tok in sorted(set(_IDENT_RE.findall(expr)), key=len, reverse=True):
        if tok in body:
            expr = expr.replace(tok, "")
    return not _ALIAS_LEFTOVER_RE.sub("", expr)


def _drop_redundant_roots(roots: list, body: dict) -> tuple[list, list]:
    """Remove roots that are pure aliases adding nothing another root lacks.

    Two real cases in the benchmark, neither of them a guess:
      Sextets   `LD := LD1+LD2+LD3` while `LSextet` already reaches LD1..LD3
      MDMmodel  `LMDMNP` and `LTot` are the same sum written twice
    Dropping these leaves a single genuine total. Roots that carry physics of
    their own, or reach terms no other root reaches, are always kept.
    """
    if len(roots) < 2:
        return roots, []
    reach = {r: _reach(r, body) - {r} for r in roots}
    kept, dropped = list(roots), []
    for r in roots:
        if not _is_pure_alias(r, body):
            continue
        others = [s for s in kept if s != r]
        # covered by a single other root that we are keeping
        covering = next((s for s in others if reach[r] <= reach[s]), None)
        if covering is None:
            continue
        # mutual duplicates: keep the preferred name, drop the other
        if reach[covering] <= reach[r]:
            pref = next((p for p in _ROOT_NAME_PREFERENCE if p in (r, covering)), None)
            if pref == r:
                continue
        kept.remove(r)
        dropped.append({"root": r, "covered_by": covering})
    return (kept or roots), dropped


def _lag_override(fr_path: Path) -> str | None:
    """Human-declared total for a model, from lag_overrides.json.

    Shape: ``{"<page>": "LTot", ...}``. The page is the benchmark directory
    name, i.e. the first path component under this file's directory.
    """
    path = HERE / "lag_overrides.json"
    if not path.is_file():
        return None
    try:
        table = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    try:
        page = fr_path.resolve().relative_to(HERE.resolve()).parts[0]
    except ValueError:
        return None
    val = table.get(page)
    return val if isinstance(val, str) and val else None


_KERNEL_PATTERN = "Wolfram Player.app/Contents/MacOS/WolframKernel"


def _kernel_pids() -> set:
    """PIDs of the Wolfram Engine kernels running right now."""
    p = subprocess.run(["pgrep", "-f", _KERNEL_PATTERN], capture_output=True, text=True)
    return {int(x) for x in p.stdout.split() if x.strip().isdigit()}


def _kill_stale_kernels(pgid: int | None = None) -> None:
    """Kill the kernels of THIS compile — never another process's.

    wolframscript leaves its kernel behind when the driver is killed, and an
    orphan holds the licence slot and the output pipe, so they must go. Two
    earlier versions of this were both too broad:

      1. ``pkill -9 -f WolframKernel`` killed every Wolfram kernel on the
         machine — a concurrent test suite, a parallel compile, or the
         operator's own Mathematica session.
      2. "every kernel that appeared since I started" is no better when two
         compiles overlap: the first to finish kills the second's kernel,
         and the second reports a compile failure that never happened.

    The compile's own children are identified by process group: the driver is
    started with ``start_new_session=True``, so its kernels inherit its pgid
    and nothing else on the machine shares it.
    """
    if pgid is None:
        return
    p = subprocess.run(["ps", "-A", "-o", "pid=,pgid=,command="],
                       capture_output=True, text=True)
    for line in p.stdout.splitlines():
        parts = line.split(None, 2)
        if len(parts) < 3 or _KERNEL_PATTERN not in parts[2]:
            continue
        try:
            pid, gid = int(parts[0]), int(parts[1])
        except ValueError:
            continue
        if gid != pgid:
            continue
        try:
            os.kill(pid, signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            pass


def _pgid_of(proc) -> int | None:
    """The process group the driver was started in (start_new_session=True)."""
    try:
        return os.getpgid(proc.pid)
    except (ProcessLookupError, PermissionError, AttributeError):
        # The driver has already been reaped; with start_new_session the pgid
        # equals its pid, which is still the right group to sweep.
        return getattr(proc, "pid", None)


def lagrangian_expression(fr: Path, lag: str) -> str:
    """The expression handed to FeynRules for a model whose total is ``lag``.

    FeynRules' Standard Model Lagrangian is ``LSM``. Most benchmark models
    define a BSM-only total, so the SM must be added. Some totals already
    include ``LSM``, directly or through a sub-term; adding it again counts
    every SM term twice, which breaks the mass spectrum and every SM vertex.
    The earlier generator added ``LSM`` unconditionally, so runs whose total
    already included it were checked and compiled with the SM counted twice.
    """
    terms = {t["name"]: t["expression"]
             for t in parse_lagrangian_terms(fr.read_text(errors="replace"))}
    reached: set = set()
    for name in _reach(lag, terms):
        reached.update(_IDENT_RE.findall(terms.get(name, "")))
    return lag if "LSM" in reached else f"LSM + {lag}"


def _run_driver(args: list, timeout: int) -> tuple[str, int, bool, float]:
    """Run UFO_generator.wl; return ``(stdout, exit, timed_out, seconds)``.

    Popen + process-group kill: subprocess.run(timeout=) only kills
    wolframscript, then blocks in communicate() until the orphaned
    WolframKernel children release the output pipe (observed 85 min hang).
    """
    cmd = [config.wolframscript_path, "-f", str(DRIVER),
           f"FeynRulesPath={config.feynrules_path}", *args]
    t0 = time.time()
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         text=True, stdin=subprocess.DEVNULL, start_new_session=True)
    # Wall-clock watchdog beside communicate()'s own timeout: the latter
    # counts monotonic time, which stops while the machine sleeps, so a
    # laptop that dozed off stretched a 3600 s budget to 17471 s. time.time()
    # jumps across sleep; this does not.
    killed = {"by_watchdog": False}

    def _watchdog():
        while p.poll() is None:
            if time.time() - t0 > timeout:
                killed["by_watchdog"] = True
                try:
                    os.killpg(os.getpgid(p.pid), signal.SIGKILL)
                except (ProcessLookupError, PermissionError):
                    pass
                return
            time.sleep(15)
    threading.Thread(target=_watchdog, daemon=True).start()
    try:
        out, _ = p.communicate(timeout=timeout)
        rc = p.returncode
        timed_out = killed["by_watchdog"]
        if timed_out:
            rc = -1
    except subprocess.TimeoutExpired:
        os.killpg(os.getpgid(p.pid), signal.SIGKILL)
        try:
            out, _ = p.communicate(timeout=30)
        except Exception:
            out = ""
        rc = -1
        timed_out = True
    finally:
        _kill_stale_kernels(_pgid_of(p))
    return out or "", rc, timed_out, round(time.time() - t0, 1)


def _verdicts(out: str) -> dict:
    """``{check name: "pass" | "fail" | "inconclusive"}`` from generator stdout."""
    return {c["name"]: c["verdict"] for c in parse_check_verdicts(out)}


def compile_to_ufo(page: str, fr: Path, lag: str, outdir: Path) -> dict:
    outdir.parent.mkdir(parents=True, exist_ok=True)
    if outdir.exists():
        subprocess.run(["rm", "-rf", str(outdir)], capture_output=True)
    expr = lagrangian_expression(fr, lag)
    out, rc, timed_out, dt = _run_driver(
        [f"ModelPath={fr}", f"OutputDir={outdir}", "Checks=true", "AddDecays=false",
         "LoadSM=true", f"Lagrangian={expr}"],
        COMPILE_TIMEOUT)
    (outdir.parent / "compile.log").write_text(out)
    ufo_files = [f for f in ("particles.py", "parameters.py", "couplings.py",
                             "vertices.py", "lorentz.py")
                 if (outdir / f).is_file()]
    # Exit 2 is the generator's own verdict that WriteUFO left an incomplete UFO.
    compile_ok = rc == 0 and "[INFO] Done." in out and (outdir / "particles.py").is_file()
    protected_errs = len(re.findall(r"ISUMObject|IndexRange\[Index\[Spin\]\]", out))
    return {
        "compile_ok": compile_ok,
        "lagrangian_expression": expr,
        "timed_out": timed_out,
        "exit": rc,
        "seconds": dt,
        "ufo_files": ufo_files,
        "checks": _verdicts(out),
        "protected_symbol_errors": protected_errs,
        "log_tail": out[-1200:] if not compile_ok else "",
    }


def run_lagrangian_checks(fr: Path, lag: str, log_path: Path,
                          timeout: int = COMPILE_TIMEOUT) -> dict:
    """FeynRules' consistency checks alone, without writing a UFO.

    Returns ``{"checks", "lagrangian_expression", "exit", "timed_out",
    "seconds"}``; stdout goes to ``log_path`` so every verdict has its
    evidence on disk.
    """
    log_path.parent.mkdir(parents=True, exist_ok=True)
    expr = lagrangian_expression(fr, lag)
    out, rc, timed_out, dt = _run_driver(
        [f"ModelPath={fr}", f"OutputDir={log_path.parent / 'checks_only_UFO'}",
         "Checks=true", "ChecksOnly=true", "LoadSM=true", f"Lagrangian={expr}"],
        timeout)
    log_path.write_text(out)
    return {"checks": _verdicts(out), "lagrangian_expression": expr,
            "exit": rc, "timed_out": timed_out, "seconds": dt}


def count_new_particles(outdir: Path) -> int:
    """Particles in the generated UFO minus the plain-SM baseline count."""
    pf = outdir / "particles.py"
    if not pf.is_file():
        return 0
    txt = pf.read_text(errors="replace")
    total = len(re.findall(r"=\s*Particle\(", txt))
    # SM UFO has ~ (17 physical + goldstones/ghosts). Report raw; SM baseline
    # subtraction is approximate, so we also keep the raw count in the row.
    return total


def madgraph_import(outdir: Path, workdir: Path) -> dict:
    if not MG5.is_file():
        return {"madgraph_import_ok": False, "reason": "mg5_aMC not found"}
    workdir.mkdir(parents=True, exist_ok=True)
    cmdfile = workdir / "mg5_import.txt"
    cmdfile.write_text(f"import model {outdir}\ndisplay particles\n")
    try:
        p = subprocess.run([str(MG5), str(cmdfile)], capture_output=True, text=True,
                           timeout=MG5_TIMEOUT, stdin=subprocess.DEVNULL, cwd=str(workdir))
        out = (p.stdout or "") + "\n" + (p.stderr or "")
        (workdir / "mg5.log").write_text(out)
    except subprocess.TimeoutExpired:
        return {"madgraph_import_ok": False, "reason": "timeout"}
    fatal = ("Traceback (most recent call last)" in out
             or "InvalidCmd" in out
             or re.search(r"Command \".*\" interrupted with error", out))
    loaded = re.search(r"Current model contains (\d+) particles", out)
    ok = bool(loaded) and not fatal
    return {
        "madgraph_import_ok": ok,
        "mg5_particles": int(loaded.group(1)) if loaded else None,
        "lepton_number_violation": "violating the charge: LeptonNumber" in out,
        "mg5_tail": out[-800:] if not ok else "",
    }


def run_one(page: str) -> dict:
    fr = HERE / page / "model" / f"{page}_gen.fr"
    row: dict = {"page": page, "fr": str(fr.relative_to(REPO)) if fr.is_file() else None}
    if not fr.is_file():
        row["status"] = "missing_fr"
        return row
    lag, lag_info = total_lag_symbol(fr)
    row["lag_symbol"] = lag
    row["lag_resolution"] = lag_info
    if not lag:
        # Unscoreable is not the same as failed: the model may be perfectly
        # good, but it never says which symbol is its total Lagrangian, so
        # there is nothing defensible to compile.
        row["status"] = ("ambiguous_lagrangian_symbol" if lag_info.get("ambiguous")
                         else "no_lagrangian_symbol")
        return row
    outdir = OUTROOT / page / f"{page}_UFO"
    comp = compile_to_ufo(page, fr, lag, outdir)
    row.update(comp)
    if comp["compile_ok"]:
        row["n_particles_ufo"] = count_new_particles(outdir)
        row.update(madgraph_import(outdir, OUTROOT / page / "mg5run"))
        row["status"] = "compiled"
    else:
        row["status"] = "compile_failed" if not comp["timed_out"] else "compile_timeout"
    return row


def main() -> int:
    argv = sys.argv[1:]
    if argv and argv[0] == "--all":
        cands = json.loads((HERE / "db_candidates.json").read_text())["candidates"]
        pages = [c["page"] for c in cands]
    elif argv:
        pages = [p for a in argv for p in a.split(",") if p]
    else:
        pages = DEFAULT_SUBSET

    print(f"[vbench] {len(pages)} models | compile_timeout={COMPILE_TIMEOUT}s "
          f"mg5_timeout={MG5_TIMEOUT}s | out={OUTROOT}", flush=True)
    rows = []
    for i, page in enumerate(pages, 1):
        print(f"[vbench] ({i}/{len(pages)}) {page} ...", flush=True)
        row = run_one(page)
        tag = row.get("status")
        extra = ""
        if tag == "compiled":
            extra = (f"  checks={row.get('checks')}  parts={row.get('n_particles_ufo')}"
                     f"  mg5={row.get('madgraph_import_ok')}  ({row.get('seconds')}s)")
        print(f"[vbench]     -> {tag}{extra}", flush=True)
        rows.append(row)
        (HERE / "validation_benchmark_report.json").write_text(
            json.dumps({"rows": rows}, indent=2))

    # Aggregates
    n = len(rows)
    compiled = [r for r in rows if r.get("status") == "compiled"]
    def _rate(pred):
        m = [r for r in compiled if pred(r)]
        return (len(m), len(compiled))
    herm = _rate(lambda r: (r.get("checks") or {}).get("hermiticity") == PASS)
    allchk = _rate(lambda r: all_checks_pass(r.get("checks")))
    mg5ok = _rate(lambda r: r.get("madgraph_import_ok"))
    agg = {
        "n_models": n,
        "n_compiled": len(compiled),
        "compile_rate": round(len(compiled) / n, 3) if n else 0,
        "hermiticity_pass": herm[0],
        "all_checks_pass": allchk[0],
        "madgraph_import_ok": mg5ok[0],
        "n_compile_failed": sum(1 for r in rows if r.get("status") == "compile_failed"),
        "n_compile_timeout": sum(1 for r in rows if r.get("status") == "compile_timeout"),
    }
    report = {"aggregate": agg, "rows": rows}
    (HERE / "validation_benchmark_report.json").write_text(json.dumps(report, indent=2))

    lines = [
        "# Validation-augmented benchmark — agent .fr → FeynRules/Wolfram UFO → MadGraph",
        "",
        "Each agent-generated `.fr` (from the field-content benchmark) is compiled "
        "to a UFO with the free Wolfram Engine + FeynRules, physics-checked, and "
        "imported into MadGraph 3.7.2. This measures whether the agent's model "
        "**actually works in the real tool chain**, not just whether its field "
        "content matches a reference.",
        "",
        f"**Aggregate over {n} models:** compiled **{agg['n_compiled']}/{n}** "
        f"({agg['compile_rate']:.0%}); Hermiticity-pass {herm[0]}/{herm[1]}; "
        f"all-checks-pass {allchk[0]}/{allchk[1]}; "
        f"MadGraph-import-ok {mg5ok[0]}/{mg5ok[1]}; "
        f"compile-failed {agg['n_compile_failed']}, timeout {agg['n_compile_timeout']}.",
        "",
        "| Model | Lag symbol | Compile | Herm | Kin diag | Mass diag | Spectrum | UFO parts | MG5 load | LNV | secs | Status |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    def _b(v):
        return "✓" if v is True else ("✗" if v is False else "—")

    def _v(v):
        return {"pass": "✓", "fail": "✗", "inconclusive": "?"}.get(v, "—")
    for r in rows:
        c = r.get("checks") or {}
        lines.append(
            f"| {r['page']} | {r.get('lag_symbol','—')} | {_b(r.get('compile_ok'))} | "
            + " | ".join(_v(c.get(k)) for k in CHECK_KEYS) + " | "
            f"{r.get('n_particles_ufo','—')} | "
            f"{_b(r.get('madgraph_import_ok'))} | {_b(r.get('lepton_number_violation'))} | "
            f"{r.get('seconds','—')} | {r.get('status')} |")
    lines += [
        "",
        "## Notes",
        "- `Compile` = FeynRules `WriteUFO` produced `particles.py` and printed Done.",
        "- Checks are FeynRules' own consistency routines. Each verdict is read "
        "from the routine's return value (`tools/feynrules/lagrangian_checks.py`), "
        "not its printed prose. `?` means inconclusive; `—` means the check did not run.",
        "- `MG5 load` = MadGraph `import model` succeeded (UFO auto-converted to "
        "Python3 as needed) and reported a particle count with no fatal error.",
        "- `LNV` = MadGraph flagged a lepton-number-violating interaction "
        "(expected/correct for leptoquark and Majorana-neutrino models).",
        "- `AddDecays=False`: FeynRules' auto-decay routine is disabled (broken "
        "under Wolfram ≥ 15); decay widths are left to MadGraph's `compute_widths`.",
    ]
    (HERE / "validation_benchmark_report.md").write_text("\n".join(lines) + "\n")
    print("\n[vbench] " + json.dumps(agg), flush=True)
    print("[vbench] report: eval/benchmark_runs/validation_benchmark_report.{json,md}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
