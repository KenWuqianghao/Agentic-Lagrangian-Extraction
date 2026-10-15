#!/usr/bin/env python3
"""
End-to-end run of the whole loop, one stage per bundle, on a real paper.

    literature -> extract -> frgen -> feynrules/validate -> reverse
                                                        \\-> limits (ADS)

Every stage calls the actual registered tool, not a helper, so this exercises
what an agent would exercise. Results are written to e2e_result.json.

Usage:
    python e2e_run.py [--skip-reverse] [--skip-extract]
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

REPO = Path("/Users/kenwu/Documents/Github/heptapod")
sys.path.insert(0, str(REPO))
os.chdir(REPO)

SANDBOX = Path(sys.argv[sys.argv.index("--sandbox") + 1]) if "--sandbox" in sys.argv \
    else Path("/tmp/e2e_loop")
SANDBOX.mkdir(parents=True, exist_ok=True)

ARXIV_ID = "1603.04993"          # scalar leptoquark S1, has arXiv source
MODEL_NAME = "S1_LQ_E2E"

RESULTS: list[dict] = []

# Tools declare external paths and the agent command as StateFields. Under
# toolbase these are injected from the toolkit config; instantiating a tool
# directly means passing them explicitly, or the tool fails validation before
# it ever runs.
import config as _cfg                                       # noqa: E402
STATE = {
    "feynrules_path": _cfg.feynrules_path,
    "wolframscript_path": _cfg.wolframscript_path,
    "mg5_path": _cfg.mg5_path,
}
BLANK_AGENT = getattr(_cfg, "blank_agent_cmd", None)
ADS_TOKEN = getattr(_cfg, "ads_token", None)


def stage(name: str, note: str = ""):
    def deco(fn):
        def wrapped(*a, **kw):
            print(f"\n{'='*70}\n[{name}] {note}\n{'='*70}", flush=True)
            t0 = time.time()
            try:
                ok, detail = fn(*a, **kw)
                err = None
            except Exception as e:                          # noqa: BLE001
                ok, detail, err = False, {}, f"{type(e).__name__}: {e}"
            dt = round(time.time() - t0, 1)
            RESULTS.append({"stage": name, "ok": bool(ok), "seconds": dt,
                            "detail": detail, "error": err})
            print(f"[{name}] {'PASS' if ok else 'FAIL'} ({dt}s)"
                  + (f" — {err}" if err else ""), flush=True)
            return ok, detail
        return wrapped
    return deco


# ---------------------------------------------------------------- 1. literature
@stage("literature", f"fetch LaTeX e-print for arXiv:{ARXIV_ID}")
def run_literature():
    from tools.literature.literature_tools import ArxivSourceTool
    out = json.loads(ArxivSourceTool(
        arxiv_id=ARXIV_ID, output_dir="paper",
        base_directory=str(SANDBOX))._run())
    if out.get("status") != "ok":
        return False, out
    tex = out.get("main_tex_path") or out.get("tex_path")
    n = out.get("chars") or out.get("n_chars") or 0
    print(f"  main tex: {tex}   ({n} chars)")
    return True, {"tex_path": tex, "chars": n,
                  "keys": sorted(out)[:12]}


# ------------------------------------------------------------------ 2. extract
@stage("extract", "paper text -> structured FeynRulesModel (Ollama)")
def run_extract(tex_rel):
    from tools.extract.extract_tool import ExtractLagrangianTool
    p = SANDBOX / tex_rel
    text = p.read_text(encoding="utf-8", errors="replace")[:24000]
    out = json.loads(ExtractLagrangianTool(
        paper_text=text, model_name=MODEL_NAME,
        base_directory=str(SANDBOX))._run())
    if out.get("status") != "ok":
        return False, {k: out.get(k) for k in ("status", "error")}
    spec = out.get("model_json") or out.get("model")
    n_p = out.get("n_particles") or 0
    n_par = out.get("n_parameters") or 0
    print(f"  particles={n_p} parameters={n_par}")
    (SANDBOX / "spec.json").write_text(
        spec if isinstance(spec, str) else json.dumps(spec))
    # status=ok only means the call returned. A model with no particles is
    # not an extraction, and letting it count as a pass would hide the
    # failure behind a downstream compile error.
    return bool(n_p > 0), {"n_particles": n_p, "n_parameters": n_par,
                           "extracted_model_name": (json.loads(spec).get("model_name")
                                                    if isinstance(spec, str) else None)}


# -------------------------------------------------------------------- 3. frgen
@stage("frgen", "structured spec -> FeynRules .fr")
def run_frgen(spec_json=None):
    from tools.frgen.frgen_tool import GenerateFeynRulesModelTool
    from tools.frgen.frmodel import (FeynRulesModel, IndexDecl, LagrangianTerm,
                                     MassSpec, ModelInfo, Parameter, ParticleClass)
    if spec_json is None:
        # Deterministic reference spec, so the chain below is exercised even
        # when the LLM stage is skipped or its output is unusable.
        model = FeynRulesModel(
            model_name=MODEL_NAME,
            info=ModelInfo(authors=["E2E"], version="1.0.0", date="05.08.2026",
                           institutions=["HEPTAPOD"], emails=[]),
            interaction_order_hierarchy=[("NP", 2)],
            index_decls=[IndexDecl(name="Colour", range_kind="NoUnfold", size=3)],
            parameters=[Parameter(name="yRR11", parameter_type="External",
                                  block_name="BSMINPUTS", complex=False,
                                  interaction_order=("NP", 1), value="0.5",
                                  description="S1-e-u Yukawa")],
            particles=[ParticleClass(
                spin_type="S", class_index=100, class_name="S1",
                self_conjugate=False, indices=["Colour"],
                mass=MassSpec(sym="MS1", value="1500."),
                width=MassSpec(sym="WS1", value="Automatic"),
                quantum_numbers={"Q": "-1/3"}, particle_name="S1",
                antiparticle_name="S1~", full_name="Scalar leptoquark S1",
                propagator_label="S1", propagator_type="ScalarDash",
                propagator_arrow="None")],
            lagrangian_terms=[
                LagrangianTerm(name="LkinS1", delayed=False, expression=(
                    "Block[{mu,aa}, ExpandIndices[DC[S1bar[aa],mu] DC[S1[aa],mu]"
                    " - MS1^2 * HC[S1].S1]]")),
                LagrangianTerm(name="L1YukRRNonHC", delayed=True, expression=(
                    "Block[{sp, aa}, yRR11 * anti[CC[uR]][sp, 1, aa]"
                    ".lR[sp, 1] * HC[S1][aa]]")),
                LagrangianTerm(name="L1YukRR", delayed=True,
                               expression="L1YukRRNonHC + HC[L1YukRRNonHC]"),
                LagrangianTerm(name="LBSM", delayed=False,
                               expression="LkinS1 + L1YukRR"),
            ])
        spec_json = model.model_dump_json()
    out = json.loads(GenerateFeynRulesModelTool(
        model_json=spec_json, output_path=f"{MODEL_NAME}.fr",
        base_directory=str(SANDBOX))._run())
    if out.get("status") != "ok":
        return False, out
    print(f"  wrote {out['fr_path']}  particles={out['n_particles']} "
          f"parameters={out['n_parameters']}")
    return True, {"fr_path": out["fr_path"], "n_particles": out["n_particles"],
                  "n_parameters": out["n_parameters"]}


# ----------------------------------------------------------------- 4. validate
@stage("validate", "compile .fr -> UFO, FeynRules checks, MadGraph import")
def run_validate(fr_rel):
    from tools.validate.validate_tool import ValidateModelTool
    out = json.loads(ValidateModelTool(
        model_path=fr_rel, physics_checks=True, madgraph_check=True,
        timeout_sec=900, base_directory=str(SANDBOX), **STATE)._run())
    # The tool reports {"status", "passed", "checks":[{name,passed,detail}]}.
    checks = out.get("checks") or []
    named = {c["name"]: bool(c.get("passed")) for c in checks
             if isinstance(c, dict) and "name" in c}
    for n, p in named.items():
        print(f"    {'PASS' if p else 'FAIL':4} {n}")
    ok = bool(out.get("passed")) and all(named.values())
    return ok, {"status": out.get("status"), "passed": out.get("passed"),
                "n_checks": len(named),
                "n_failed": sum(1 for v in named.values() if not v),
                "checks": named}


# ------------------------------------------------------------------ 5. reverse
@stage("reverse", "blank-slate reconstruction + review package (claude CLI)")
def run_reverse(fr_rel):
    from tools.reverse.reverse_tool import ReverseLagrangianTool
    out = json.loads(ReverseLagrangianTool(
        model_path=fr_rel, action="reconstruct", output_dir="review",
        timeout_sec=900, base_directory=str(SANDBOX),
        blank_agent_cmd=BLANK_AGENT)._run())
    print(f"  agent: {BLANK_AGENT}")
    pkg = out.get("review_package") or out.get("review_md")
    print(f"  status={out.get('status')} package={pkg}")
    recon = SANDBOX / "review" / "reconstruction.md"
    n = len(recon.read_text(errors="replace")) if recon.is_file() else 0
    print(f"  reconstruction.md: {n} chars")
    return bool(n > 200), {"status": out.get("status"), "package": pkg,
                           "reconstruction_chars": n}


# ------------------------------------------------------------------- 6. limits
@stage("limits", "model -> ADS experimental-limit search -> extracted bounds")
def run_limits():
    from tools.literature.limits_tools import (ExtractConstraintsTool,
                                               FindExperimentalLimitsTool)
    found = json.loads(FindExperimentalLimitsTool(
        model_name="S1_LQ_RR", particle_names=["S1"], rows_per_query=6,
        ads_token=ADS_TOKEN)._run())
    if found.get("note"):
        print(f"  note: {found['note']}")
    papers = found.get("papers") or []
    print(f"  keywords={found.get('keywords')}  papers={len(papers)}")
    for p in papers[:3]:
        print(f"    {p['year']}  {(p['title'] or '')[:58]}")

    # Read bounds out of the abstracts we just found.
    blob = "\n\n".join((p.get("abstract") or "") for p in papers)
    (SANDBOX / "abstracts.txt").write_text(blob, encoding="utf-8")
    got = json.loads(ExtractConstraintsTool(
        text_path="abstracts.txt", base_directory=str(SANDBOX))._run())
    n = got.get("n_records", 0)
    print(f"  extracted {n} candidate bounds")
    for r in (got.get("limits") or [])[:4]:
        rng = (f"{r.get('range_low')}-{r.get('range_high')}"
               if r["kind"] == "exclusion_range" else r["value"])
        print(f"    [{r['kind']}] {rng} {r['unit'] or ''}")
    return bool(papers), {"n_papers": len(papers), "n_bounds": n,
                          "keywords": found.get("keywords"),
                          "note": found.get("note"),
                          "errors": found.get("errors"),
                          "top_papers": [{"year": p["year"], "title": p["title"],
                                          "citations": p["citation_count"]}
                                         for p in papers[:5]],
                          "sample": (got.get("limits") or [])[:5]}


def main() -> int:
    print(f"sandbox: {SANDBOX}")
    fr_rel = None

    ok, lit = run_literature()
    tex = lit.get("tex_path") if ok else None

    spec = None
    if ok and tex and "--skip-extract" not in sys.argv:
        ok_x, _ = run_extract(tex)
        if ok_x and (SANDBOX / "spec.json").is_file():
            spec = (SANDBOX / "spec.json").read_text()

    ok_g, gen = run_frgen(spec)
    if ok_g:
        fr_rel = gen["fr_path"]

    if fr_rel:
        run_validate(fr_rel)
        if "--skip-reverse" not in sys.argv:
            run_reverse(fr_rel)

    run_limits()

    out = SANDBOX / "e2e_result.json"
    passed = sum(1 for r in RESULTS if r["ok"])
    out.write_text(json.dumps(
        {"stages": RESULTS, "passed": passed, "total": len(RESULTS),
         "arxiv_id": ARXIV_ID, "model_name": MODEL_NAME}, indent=1))
    print(f"\n{'='*70}\nEND TO END: {passed}/{len(RESULTS)} stages passed")
    for r in RESULTS:
        print(f"  {'PASS' if r['ok'] else 'FAIL'}  {r['stage']:12} {r['seconds']:>7.1f}s"
              + (f"  {r['error']}" if r["error"] else ""))
    print(f"wrote {out}")
    return 0 if passed == len(RESULTS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
