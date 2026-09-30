#!/usr/bin/env python3
"""hepval: the deterministic heptapod back end of the pi harness.

The pi extension (extension/heptapod.ts) calls this CLI for every physics
tool, so all FeynRules, MadGraph and sympy work lives in Python next to the
benchmark code it reuses, and the TypeScript side stays a thin adapter.

    hepval.py setup                      create/refresh the validator tree
    hepval.py lint MODEL.fr              fr_lint findings, JSON
    hepval.py validate MODEL.fr --out D  compile + 4 checks + MadGraph import
    hepval.py massbasis SPEC.json        symbolic mass matrix / inverted couplings

The validator tree is a detached worktree of heptapod-dev ``origin/main`` (the
corrected check driver, verdicts from return values) with the benchmark's
``validation_benchmark.py`` and ``repair_benchmark.py`` copied into
``eval/benchmark_runs/``: both compute REPO from their own path, so they must
sit inside the tree they drive. ``config.py`` there carries the three tool
paths and nothing else.

Validation is serial: one Wolfram kernel on this machine. ``validate`` takes an
exclusive flock, then waits until no other WolframKernel runs, before it starts
FeynRules, so concurrent agents and other sessions queue instead of killing
each other's kernels (the 2026-09-09 failure mode).
"""

from __future__ import annotations

import argparse
import fcntl
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import time
import types
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALE = HERE.parent
BENCH = ALE / "benchmarks"
HEPTAPOD = Path.home() / "Documents/Github/heptapod"
HEPTAPOD_DEV = Path.home() / "Documents/Github/heptapod-dev"
VALIDATOR = Path(os.environ.get("HEPVAL_ROOT", Path.home() / "Documents/Github/hep-pr/validator-main"))
STATE = Path(os.environ.get("HEPVAL_STATE", Path.home() / ".cache/ale-pi-harness"))
LOCK = STATE / "wolfram.lock"
# 900 s is what the September ablation used; 600 s turned a slow Monotops
# compile into a timeout on re-scoring.
COMPILE_TIMEOUT = os.environ.get("HEPVAL_COMPILE_TIMEOUT", "900")


# ------------------------------------------------------------------ setup
def setup(_args=None) -> int:
    if not (VALIDATOR / "tools/feynrules/UFO_generator.wl").is_file():
        subprocess.run(["git", "-C", str(HEPTAPOD_DEV), "fetch", "-q", "origin"], check=True)
        subprocess.run(["git", "-C", str(HEPTAPOD_DEV), "worktree", "add", "--detach",
                        str(VALIDATOR), "origin/main"], check=True)
    # Only the three tool paths: heptapod's own config.py also holds API keys.
    cfg = (HEPTAPOD / "config.py").read_text()
    keys = ("feynrules_path", "wolframscript_path", "mg5_path")
    lines = [m.group(0) for k in keys
             for m in [re.search(rf"^{k}\s*=\s*.+$", cfg, re.M)] if m]
    if len(lines) != 3:
        raise SystemExit(f"could not read {keys} from {HEPTAPOD / 'config.py'}")
    (VALIDATOR / "config.py").write_text("\n".join(lines) + "\n")
    dst = VALIDATOR / "eval" / "benchmark_runs"
    dst.mkdir(parents=True, exist_ok=True)
    for name in ("validation_benchmark.py", "repair_benchmark.py"):
        shutil.copy2(BENCH / name, dst / name)
    STATE.mkdir(parents=True, exist_ok=True)
    head = subprocess.run(["git", "-C", str(VALIDATOR), "rev-parse", "--short", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    print(json.dumps({"validator": str(VALIDATOR), "head": head, "state": str(STATE)}))
    return 0


def _load_validator():
    """Import repair_benchmark from the validator tree without the heavy
    ``tools`` package __init__ (it pulls orchestral): register the two leaf
    modules the validator needs straight from their files."""
    root = VALIDATOR
    runs = root / "eval" / "benchmark_runs"
    if not (runs / "repair_benchmark.py").is_file():
        raise SystemExit(f"validator tree not set up; run: {sys.argv[0]} setup")
    for name in ("tools", "tools.frgen", "tools.feynrules"):
        sys.modules.setdefault(name, types.ModuleType(name))

    def _load(modname: str, rel: str):
        spec = importlib.util.spec_from_file_location(modname, root / rel)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[modname] = mod
        spec.loader.exec_module(mod)

    _load("tools.frgen.fr_parser", "tools/frgen/fr_parser.py")
    _load("tools.feynrules.lagrangian_checks", "tools/feynrules/lagrangian_checks.py")
    os.environ["VBENCH_COMPILE_TIMEOUT"] = COMPILE_TIMEOUT
    os.environ.setdefault("VBENCH_OUT", str(STATE / "scratch"))
    sys.path.insert(0, str(root))
    sys.path.insert(0, str(runs))
    import repair_benchmark as rb  # noqa: E402
    return rb


# ------------------------------------------------------------------- lint
def unclosed_comments(text: str) -> list[int]:
    """Line numbers of ``(*`` that are never closed. Mathematica comments
    nest, so one missing ``*)`` comments out the rest of the file and
    FeynRules sees no model (seen in a Qwen pNG run: a header line ended in
    ``^T,*`` instead of ``*)``)."""
    stack, line, i, in_str = [], 1, 0, False
    while i < len(text):
        c = text[i]
        if c == "\n":
            line += 1
        elif c == '"' and not stack:
            in_str = not in_str
        elif not in_str and text.startswith("(*", i):
            stack.append(line)
            i += 2
            continue
        elif not in_str and text.startswith("*)", i) and stack:
            stack.pop()
            i += 2
            continue
        i += 1
    return stack


_PAIRS = {"]": "[", "}": "{", ")": "("}


def unbalanced_brackets(text: str) -> list[dict]:
    """Brackets that do not match, outside comments and strings, with line
    numbers. A truncated block (an edit that dropped a closing ``}``) makes
    the rest of the file one statement, so the harness finds no total."""
    stack, bad, line, i, depth_c, in_str = [], [], 1, 0, 0, False
    while i < len(text):
        c = text[i]
        if c == "\n":
            line += 1
        elif depth_c == 0 and c == '"':
            in_str = not in_str
        elif not in_str and text.startswith("(*", i):
            depth_c += 1
            i += 2
            continue
        elif not in_str and depth_c and text.startswith("*)", i):
            depth_c -= 1
            i += 2
            continue
        elif not in_str and depth_c == 0:
            if c in "[{(":
                stack.append((c, line))
            elif c in "]})":
                if stack and stack[-1][0] == _PAIRS[c]:
                    stack.pop()
                else:
                    bad.append({"line": line, "message": f"`{c}` closes "
                                + (f"`{stack[-1][0]}` opened at line {stack[-1][1]}" if stack else "nothing")})
                    if stack:
                        stack.pop()
        i += 1
    bad += [{"line": ln, "message": f"`{c}` opened here is never closed"} for c, ln in stack]
    return bad


def _structure_findings(text: str) -> list[dict]:
    out = [{"rule": "unclosed_comment", "stage": "compile", "line": ln,
            "message": "this `(*` is never closed; comments nest, so everything "
                       "after it is commented out and FeynRules sees no model"}
           for ln in unclosed_comments(text)]
    out += [{"rule": "unbalanced_bracket", "stage": "compile", **b}
            for b in unbalanced_brackets(text)[:6]]
    return out


def lint(args) -> int:
    sys.path.insert(0, str(BENCH))
    import fr_lint  # noqa: E402
    findings = [f.__dict__ for f in fr_lint.lint_file(args.model)]
    findings = _structure_findings(Path(args.model).read_text(errors="replace")) + findings
    for f in findings:
        # The SM-override recipe redeclares Phi on purpose; say when that is fine.
        if f["rule"] == "sm_class_redeclared":
            f["message"] += (" -- allowed only with the SM-override recipe: keep SM.fr's "
                             "names and write the total as LSM - L<replaced SM term> + ...")
    print(json.dumps({"file": args.model, "n": len(findings), "findings": findings}, indent=1))
    return 0


# --------------------------------------------------------------- validate
_NOISE = re.compile(r"^(From kernel \d+ \(Local\):|General::stop: .*)$")


def _dedupe_tail(log: str, limit: int) -> str:
    """The compile-log tail without the per-kernel repeats FeynRules prints
    once per parallel kernel, so the agent sees each distinct message once."""
    seen, out = set(), []
    for line in log.splitlines():
        s = line.strip()
        if not s or _NOISE.match(s) or s in seen:
            continue
        seen.add(s)
        out.append(line)
    text = "\n".join(out)
    return text[-limit:]


DIAG_DRIVER = ALE / "cc_harness" / "wl" / "UFO_generator_diag.wl"


def _use_diag_driver(rb, fr: Path) -> None:
    """In-loop validation for the Claude Code harness: the same checks and
    verdicts, run by a driver copy that also prints the non-hermitian
    vertices, the Lagrangian blocks' field contents and the off-diagonal mass
    terms. Scoring never passes --diag, so the score keeps the pristine
    heptapod-dev main driver."""
    rb.vb.DRIVER = DIAG_DRIVER
    lag, _info = rb.vb.total_lag_symbol(fr)
    terms = {t["name"]: t["expression"]
             for t in rb.vb.parse_lagrangian_terms(fr.read_text(errors="replace"))}
    blocks = sorted(n for n in rb.vb._reach(lag, terms) if n in terms) if lag else []
    orig = rb.vb._run_driver

    def _run(dargs, timeout):
        return orig(list(dargs) + [f"HermBlocks={','.join(blocks)}"], timeout)
    rb.vb._run_driver = _run


def validate(args) -> int:
    rb = _load_validator()
    fr = Path(args.model).resolve()
    if getattr(args, "diag", False):
        _use_diag_driver(rb, fr)
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    rb.OUTROOT = out
    n = len(list(out.glob("call*"))) + 1
    STATE.mkdir(parents=True, exist_ok=True)
    t_wait = time.time()
    with open(LOCK, "w") as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        # The lock orders this harness's calls; other sessions (open_bench,
        # repair loops) start kernels without it. Holding the lock, any live
        # kernel is theirs: wait for it, or the compiles slow each other down.
        while subprocess.run(["pgrep", "-f", "[W]olframKernel"], capture_output=True).returncode == 0:
            time.sleep(10)
        waited = round(time.time() - t_wait, 1)
        t_start = time.time()
        row = rb.validate(f"call{n}", fr, 0)
        t_end = time.time()
    work = out / f"call{n}"
    work.mkdir(parents=True, exist_ok=True)
    shutil.copy2(fr, work / "model.fr")
    report = rb.build_report_md(row, work)
    stage = ("pass" if row.get("full_pass") else
             "no_lagrangian_symbol" if row.get("status") == "no_lagrangian_symbol" else
             "compile_timeout" if row.get("timed_out") else
             "compile_failed" if not row.get("compile_ok") else
             "checks_failed" if not rb.vb.all_checks_pass(row.get("checks")) else
             "madgraph_failed")
    summary = {
        "call": n, "stage": stage, "full_chain_pass": bool(row.get("full_pass")),
        "compile_ok": row.get("compile_ok"), "checks": row.get("checks"),
        "madgraph_import_ok": row.get("madgraph_import_ok"),
        "lagrangian_expression": row.get("lagrangian_expression"),
        "error_tags": row.get("error_tags"), "seconds": row.get("seconds"),
        "lock_wait_seconds": waited,
        # Wall-clock interval the Wolfram kernel was held: intervals of
        # different calls must not overlap (the lock's evidence).
        "t_kernel_start": round(t_start, 3), "t_kernel_end": round(t_end, 3),
        "stage_reached": ("pass" if row.get("full_pass") else "compile" if not row.get("compile_ok")
                          else "checks" if not rb.vb.all_checks_pass(row.get("checks")) else "mg5"),
        "driver": "diag" if getattr(args, "diag", False) else "scoring",
    }
    # The report path stays out of what the agent reads: it lies outside the
    # sandbox. The extension saves the agent's copy as validation/call<n>.md.
    (work / "summary.json").write_text(json.dumps({**summary, "report": str(work / "VALIDATION_REPORT.md"),
                                                   "row": row}, indent=1, default=str))
    # What the agent reads: verdicts, FeynRules' own explanation per failing
    # check, and a de-duplicated log tail. The full report stays on disk.
    head = report.split("## FeynRules / Wolfram Engine output (tail)")[0].rstrip()
    if row.get("full_pass"):
        # build_report_md is written for failing models; say the verdict plainly.
        head = ("# Validation report: FULL CHAIN PASS (compile, all four checks, MadGraph import)\n\n"
                "A pass says the file is consistent FeynRules. It does not say the file is the "
                "paper's model: check that with review_model.")
    body = [json.dumps(summary, indent=1, default=str), "", head]
    if stage == "no_lagrangian_symbol":
        # The generic report says nothing here; say what the harness looked for.
        struct = _structure_findings(fr.read_text(errors="replace"))
        body += ["", "## Why no total Lagrangian was found",
                 "The harness looks for top-level `Name := expr;` statements (outside comments) "
                 "and takes the one no other term uses as the total. It found none."]
        body += [f"- line {f['line']}: {f['rule']}: {f['message']}" for f in struct]
    if not row.get("full_pass"):
        log = Path(row["compile_log"]).read_text(errors="replace") if row.get("compile_log") and Path(row["compile_log"]).is_file() else ""
        if getattr(args, "diag", False):
            sys.path.insert(0, str(ALE / "cc_harness"))
            import diagnose  # noqa: E402
            extra = diagnose.render_sections(row, log, fr.read_text(errors="replace"))
            if extra:
                body += ["", extra.rstrip()]
            log = "\n".join(ln for ln in log.splitlines() if not ln.startswith("HEPTAPOD-"))
        body += ["", "## compile log, distinct lines (tail)", "```", _dedupe_tail(log, 3000), "```"]
        if "## MadGraph import output" in report:
            body += ["", report[report.index("## MadGraph import output"):][:3500]]
    print("\n".join(body))
    return 0


# -------------------------------------------------------------- massbasis
def massbasis(args) -> int:
    """Symbolic quadratic-sector analysis of a real-field potential.

    SPEC (JSON):
      potential      V as a sympy string in gauge-basis symbols (the Lagrangian
                     contains -V). Use ** for powers.
      substitutions  {gauge symbol: expression in mass-basis fields}, e.g.
                     {"phi0": "(vev + ca*h - sa*H2)/sqrt(2)"}
      fields         mass-basis REAL fields, e.g. ["h", "H2"]; split complex
                     fields into real components yourself
      angles         optional {"alpha": ["sa", "ca"]}: sa = sin(alpha),
                     ca = cos(alpha) internally, printed back as sa/ca
      targets        optional {field: mass symbol}: require d2V/dfield2 = M^2
      solve_for      optional parameter names to solve from: vanishing
                     tadpoles, the target diagonal entries, zero off-diagonal
                     entries (the inverted parametrisation)
    Output: tadpoles, the mass-squared matrix d2V/dfi dfj at the vacuum, the
    off-diagonal entries (must vanish for CheckDiagonalMassTerms), and, with
    solve_for, the solution in sympy and Mathematica form plus the residuals
    after substituting it back.
    """
    import sympy as sp
    spec = json.loads(Path(args.spec).read_text()) if Path(args.spec).is_file() else json.loads(args.spec)

    def P(s: str):
        e = sp.sympify(s, locals={"sqrt": sp.sqrt, "I": sp.I})
        return e.subs({x: sp.Symbol(x.name, real=True) for x in e.free_symbols})

    # Angles stay polynomial symbols (s, c) with the ideal s^2 + c^2 - 1: a
    # remainder modulo that ideal is exact and fast, where trigsimp on sin/cos
    # of a symbol took minutes on a two-field potential.
    ideal = [sp.Symbol(s, real=True) ** 2 + sp.Symbol(c, real=True) ** 2 - 1
             for s, c in (spec.get("angles") or {}).values()]
    cvars = [sp.Symbol(c, real=True) for _s, c in (spec.get("angles") or {}).values()]

    def red(e):
        e = sp.together(sp.expand(e))
        num, den = sp.fraction(e)
        for g, c in zip(ideal, cvars):
            gens = sorted(num.free_symbols | {c}, key=lambda x: (x != c, x.name))
            num = sp.reduced(sp.expand(num), [g], *gens)[1] if num.free_symbols else num
            gens = sorted(den.free_symbols | {c}, key=lambda x: (x != c, x.name))
            den = sp.reduced(sp.expand(den), [g], *gens)[1] if den.free_symbols else den
        return sp.factor(sp.cancel(num / den))

    fields = [sp.Symbol(f, real=True) for f in spec["fields"]]
    V = P(spec["potential"])
    subs = {sp.Symbol(k, real=True): P(v) for k, v in (spec.get("substitutions") or {}).items()}
    V = sp.expand(V.subs(subs))
    at0 = {f: 0 for f in fields}
    tad = {str(f): red(sp.diff(V, f).subs(at0)) for f in fields}
    M = [[red(sp.diff(V, fi, fj).subs(at0)) for fj in fields] for fi in fields]
    res = {
        "tadpoles": {k: str(v) for k, v in tad.items()},
        "mass_matrix": {f"{fields[i]},{fields[j]}": str(M[i][j])
                        for i in range(len(fields)) for j in range(i, len(fields))},
        "off_diagonal_nonzero": [f"{fields[i]},{fields[j]}" for i in range(len(fields))
                                 for j in range(i + 1, len(fields)) if M[i][j] != 0],
    }
    unknowns = [sp.Symbol(u, real=True) for u in spec.get("solve_for") or []]
    if unknowns:
        eqs = [e for e in tad.values() if e != 0]
        for f, m in (spec.get("targets") or {}).items():
            i = spec["fields"].index(f)
            eqs.append(M[i][i] - P(m) ** 2)
        eqs += [M[i][j] for i in range(len(fields)) for j in range(i + 1, len(fields))]
        eqs = [sp.numer(sp.together(e)) for e in eqs if e != 0]
        linear = all(sp.Poly(e, *unknowns).total_degree() <= 1 for e in eqs)
        sols = []
        if linear:
            ls = sp.linsolve(eqs, unknowns)
            sols = [dict(zip(unknowns, t)) for t in ls]
        else:
            sols = sp.solve(eqs, unknowns, dict=True)
        if not sols:
            res["solution"] = None
            res["note"] = ("no solution for these unknowns; choose parameters that enter "
                           "the tadpoles and the mass matrix linearly (quartics, mu^2 terms), "
                           "as many unknowns as independent conditions")
        else:
            sol = {k: red(v) for k, v in sols[0].items()}
            free = sorted({str(s) for v in sol.values() for s in v.free_symbols} & {str(u) for u in unknowns})
            Vs = sp.expand(V.subs(sol))
            resid = {
                "tadpoles": [str(red(sp.diff(Vs, f).subs(at0))) for f in fields],
                "off_diagonal": [str(red(sp.diff(Vs, fields[i], fields[j]).subs(at0)))
                                 for i in range(len(fields)) for j in range(i + 1, len(fields))],
                "diagonal_minus_target": {f: str(red(sp.diff(Vs, sp.Symbol(f, real=True), 2).subs(at0) - P(m) ** 2))
                                          for f, m in (spec.get("targets") or {}).items()},
            }
            res["solution"] = {str(k): str(v) for k, v in sol.items()}
            res["solution_mathematica"] = {str(k): sp.mathematica_code(v) for k, v in sol.items()}
            res["residuals_after_solution"] = resid
            res["verified"] = all(r == "0" for r in resid["tadpoles"] + resid["off_diagonal"]
                                  + list(resid["diagonal_minus_target"].values()))
            if free:
                res["underdetermined_in"] = free
            if len(sols) > 1:
                res["n_solutions"] = len(sols)
    print(json.dumps(res, indent=1))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("setup").set_defaults(fn=setup)
    p = sub.add_parser("lint")
    p.add_argument("model")
    p.set_defaults(fn=lint)
    p = sub.add_parser("validate")
    p.add_argument("model")
    p.add_argument("--out", required=True)
    p.add_argument("--diag", action="store_true",
                   help="in-loop diagnostics (cc_harness driver copy): non-hermitian vertices, "
                        "mass matrix, MadGraph back-trace; never used for scoring")
    p.set_defaults(fn=validate)
    p = sub.add_parser("massbasis")
    p.add_argument("spec", help="JSON file or JSON string")
    p.set_defaults(fn=massbasis)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
