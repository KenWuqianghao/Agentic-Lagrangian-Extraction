#!/usr/bin/env python3
"""Mutation test of the reverse-Lagrangian crosscheck (option F).

Question: does `reverselagrangian` (blank-slate reconstruction of a .fr, then
a blank-slate comparison against the paper) detect physics defects that the
compile chain passes?

Cases:
  * control  — a stored agent .fr that resolved every physicist predicate;
  * mutant   — the same file with ONE injected defect (drop_eps, flip_charge,
               drop_cutoff, drop_cc, sqrt_swap, factor2, drop_term,
               swap_chirality); one mutation per file;
  * real     — the original agent files that carry the physicist-confirmed
               findings of September 2026 (held-out positives).

Both agent phases are the toolkit's own prompts (tools/reverse/prompts.py) on
the toolkit's own sanitiser. The engine is a Claude Code subagent of the
interactive session (the headless CLIs are logged out), with the tool policy
stated in the prompt and audited from the transcript afterwards.

Usage (from ALE benchmarks/):
  crosscheck_mutation.py prepare-recon --out crosscheck_mutation
  # spawn one subagent per entry of <out>/manifest_recon.json
  crosscheck_mutation.py prepare-cross --out crosscheck_mutation
  # spawn one subagent per entry of <out>/manifest_cross.json
  crosscheck_mutation.py prepare-judge --out crosscheck_mutation
  # spawn one subagent per entry of <out>/manifest_judge.json
  crosscheck_mutation.py audit --out crosscheck_mutation --transcripts-dir <session>/subagents
  crosscheck_mutation.py score --out crosscheck_mutation
"""

from __future__ import annotations

import argparse
import glob
import importlib.util
import json
import os
import re
import shutil
import sys
import types
from pathlib import Path

HERE = Path(__file__).resolve().parent
HEPTAPOD = Path(os.environ.get("HEPTAPOD_REPO", "~/Documents/Github/heptapod")).expanduser()
if not (HEPTAPOD / "tools/reverse/sanitize.py").is_file():
    sys.exit(f"crosscheck_mutation.py: no heptapod checkout at {HEPTAPOD}; set HEPTAPOD_REPO")
TEXT_ROOT = HEPTAPOD / "eval/benchmark_runs"


def _load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, HEPTAPOD / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


fr_parser = _load("fr_parser", "tools/frgen/fr_parser.py")
# sanitize.py imports tools.frgen.fr_parser; the frgen package __init__ pulls
# in orchestral, so register the parser under that name without the package.
for name in ("tools", "tools.frgen"):
    sys.modules.setdefault(name, types.ModuleType(name))
sys.modules["tools.frgen.fr_parser"] = fr_parser
sanitize = _load("sanitize", "tools/reverse/sanitize.py")
prompts = _load("reverse_prompts", "tools/reverse/prompts.py")

# (page, stored run) -> base file. Every base resolved all of its physicist
# predicates in ablation_report*.json, so a defect found in a mutant is the
# mutation, not a pre-existing one.
BASES = {
    "Top-Philic-Zprime": "rerun/v3_notools/s2",
    "EffLRSM": "rerun/v3_notools/s1",
    "GeneralU1": "rerun/v3_notools/s1",
    "368sextets": "rerun/v3_notools/s2",
    "ChernSimonsPortal": "rerun/v3s_notools/s1",
    "pNG": "rerun/v3s_notools/s1",
    "331": "rerun/v3s_tools/s1",
    "Monotops": "rerun/v3s_tools/s1",
}

# Original agent files with the physicist-confirmed findings (FINDINGS_2026-09.md).
REAL = {
    "EffLRSM": (
        "model/EffLRSM_gen.fr",
        "Light neutrino written as the bare field `ve` where the paper has "
        "the charge conjugate nu^c (lepton number); and the Z_R coupling "
        "MULTIPLIES by Sqrt[1 - tan^2/kappa^2] where Eq. (8) DIVIDES.",
    ),
    "GeneralU1": (
        "model/GeneralU1_gen.fr",
        "Neutrino Dirac Yukawa contracts LLbar[ii] with Phibar[ii] on a "
        "shared index (no Eps, not an SU(2) singlet); Higgs U(1)_X charge "
        "has the wrong sign (-xH/2 instead of +xH/2).",
    ),
    "368sextets": (
        "model/368sextets_gen.fr",
        "Dimension-5 and -6 sextet operators carry no 1/Lambda, "
        "1/Lambda^2 suppression; couplings absorb the cutoff.",
    ),
}


def _blank_comments(text: str) -> str:
    """Replace every `(* ... *)` comment by spaces so offsets stay valid but
    no operator can match inside a comment."""
    out, depth, i = [], 0, 0
    while i < len(text):
        if text.startswith("(*", i):
            depth += 1
            out.append("  ")
            i += 2
            continue
        if text.startswith("*)", i) and depth:
            depth -= 1
            out.append("  ")
            i += 2
            continue
        out.append(text[i] if depth == 0 or text[i] == "\n" else " ")
        i += 1
    return "".join(out)


def _term_spans(text: str):
    """[(name, start, end)] for every top-level `Lname := ...` statement."""
    text = _blank_comments(text)
    starts = [(m.group(1), m.start()) for m in re.finditer(r"^(L\w+)\s*:=", text, re.M)]
    stops = [m.start() for m in re.finditer(r"^(?:M\$\w+\s*=|L\w+\s*:=)", text, re.M)]
    spans = []
    for name, s in starts:
        nxt = min([x for x in stops if x > s] + [len(text)])
        spans.append((name, s, nxt))
    return spans


def _is_kin(name: str) -> bool:
    return bool(re.search(r"kin|Kin|KIN|free|Free|gauge|Gauge|mass|Mass", name))


# Every operator returns (new_text, term_name, tokens, description) or None.


def op_drop_eps(text):
    for name, s, e in _term_spans(text):
        body = text[s:e]
        m = re.search(r"\s*\*?\s*Eps\[\s*(\w+)\s*,\s*(\w+)\s*\]", body)
        if not m:
            continue
        a, b = m.group(1), m.group(2)
        nb = body[: m.start()] + body[m.end() :]
        nb = re.sub(rf"\b{b}\b", a, nb)

        def _dedupe(mm):
            seen, keep = set(), []
            for v in [x.strip() for x in mm.group(1).split(",")]:
                if v and v not in seen:
                    seen.add(v)
                    keep.append(v)
            return "Block[{" + ", ".join(keep) + "}"

        nb = re.sub(r"Block\[\{([^}]*)\}", _dedupe, nb, count=1)
        return (
            text[:s] + nb + text[e:],
            name,
            [name, "Eps", a],
            f"SU(2) epsilon contraction removed from `{name}`: `Eps[{a}, {b}]` "
            f"dropped and both doublets contracted on the shared index `{a}` "
            "(the term is no longer an SU(2) singlet).",
        )
    return None


def op_flip_charge(text):
    # First non-zero, non-Q quantum number of a new class; fall back to Q.
    for prefer_q in (False, True):
        for m in re.finditer(r"QuantumNumbers\s*->\s*\{([^}]*)\}", text):
            entries = [x.strip() for x in m.group(1).split(",")]
            for i, ent in enumerate(entries):
                mm = re.match(r"(\w+)\s*->\s*(-?[\d/\.]+)\s*$", ent)
                if not mm or mm.group(2) in ("0", "0.", "0/1"):
                    continue
                if (mm.group(1) == "Q") != prefer_q:
                    continue
                q, v = mm.group(1), mm.group(2)
                nv = v[1:] if v.startswith("-") else "-" + v
                entries[i] = f"{q} -> {nv}"
                cls = re.findall(r"ClassName\s*->\s*(\w+)", text[: m.start()])
                cls = cls[-1] if cls else "?"
                new = text[: m.start(1)] + ", ".join(entries) + text[m.end(1) :]
                return (
                    new,
                    cls,
                    [cls, q],
                    f"Quantum number `{q}` of class `{cls}` flipped from {v} to {nv}.",
                )
    return None


def op_drop_cutoff(text):
    for name, s, e in _term_spans(text):
        body = text[s:e]
        m = re.search(r"/\s*\(?\s*(Lam\w*|Lambda\w*)\s*(\^\s*\d+)?\s*\)?", body)
        if not m:
            continue
        nb = body[: m.start()] + body[m.end() :]
        return (
            text[:s] + nb + text[e:],
            name,
            [name, m.group(1)],
            f"Cutoff factor `{m.group(0).strip()}` removed from `{name}`; the "
            "operator is no longer suppressed by the cutoff and its coefficient "
            "changes mass dimension.",
        )
    return None


def op_drop_cc(text):
    for name, s, e in _term_spans(text):
        body = text[s:e]
        m = re.search(r"CC\[(\w+)\]", body)
        if not m:
            continue
        nb = body[: m.start()] + m.group(1) + body[m.end() :]
        return (
            text[:s] + nb + text[e:],
            name,
            [name, "CC", m.group(1)],
            f"Charge conjugation dropped in `{name}`: `CC[{m.group(1)}]` -> "
            f"`{m.group(1)}` (the fermion-number-violating structure becomes "
            "a fermion-number-conserving one).",
        )
    return None


def op_sqrt_swap(text):
    m = re.search(r"Value\s*->\s*(Sqrt\[[^\]]*\])\s*,", text)
    if m:
        cls = re.findall(r"(\w+)\s*==\s*\{", text[: m.start()])
        cls = cls[-1] if cls else "?"
        new = text[: m.start(1)] + "1/" + m.group(1) + text[m.end(1) :]
        return (
            new,
            cls,
            [cls, "Sqrt"],
            f"Parameter `{cls}`: `{m.group(1)}` replaced by `1/{m.group(1)}` "
            "(a normalisation that divides now multiplies).",
        )
    for name, s, e in _term_spans(text):
        body = text[s:e]
        m = re.search(r"/\s*(Sqrt\[[^\]]*\])", body)
        if not m:
            continue
        nb = body[: m.start()] + " " + m.group(1) + body[m.end() :]
        return (
            text[:s] + nb + text[e:],
            name,
            [name, "Sqrt"],
            f"In `{name}` a factor `/{m.group(1)}` became `*{m.group(1)}`.",
        )
    return None


def op_factor2(text):
    spans = [x for x in _term_spans(text) if not _is_kin(x[0]) and not x[0].startswith("LTot")]
    if not spans:
        return None
    name, s, e = spans[0]
    body = text[s:e]
    m = re.match(r"(L\w+\s*:=\s*)", body)
    rest = body[m.end() :].rstrip()
    trailing = ""
    if rest.endswith(";"):
        rest, trailing = rest[:-1], ";"
    nb = m.group(1) + "2 (" + rest + ")" + trailing + "\n"
    return (
        text[:s] + nb + text[e:],
        name,
        [name, "2"],
        f"Whole term `{name}` multiplied by 2 (coupling normalisation off by a factor of two).",
    )


def op_drop_term(text):
    spans = _term_spans(text)
    tot = [x for x in spans if x[0].startswith("LTot") or x[0] in ("LFull", "LBSM", "Lag")]
    if not tot:
        return None
    tname, ts, te = tot[-1]
    cands = [
        x
        for x in spans
        if x[0] != tname and not _is_kin(x[0]) and re.search(rf"\b{x[0]}\b", text[ts:te])
    ]
    if not cands:
        return None
    name, s, e = cands[-1]
    total = text[ts:te]
    total2 = re.sub(rf"\s*\+\s*{name}\b", "", total, count=1)
    if total2 == total:
        total2 = re.sub(rf"\b{name}\s*\+\s*", "", total, count=1)
    if total2 == total:
        return None
    if s < ts:
        new = text[:s] + text[e:ts] + total2 + text[te:]
    else:
        new = text[:ts] + total2 + text[te:s] + text[e:]
    return (
        new,
        name,
        [name],
        f"Interaction term `{name}` deleted from the model and from the total "
        "Lagrangian (a whole interaction is missing).",
    )


def op_swap_chirality(text):
    for name, s, e in _term_spans(text):
        body = text[s:e]
        if "ProjP" in body:
            nb = body.replace("ProjP", "ProjM", 1)
            return (
                text[:s] + nb + text[e:],
                name,
                [name, "ProjM", "ProjP"],
                f"First `ProjP` in `{name}` changed to `ProjM` (a right-handed "
                "current became left-handed).",
            )
        if "ProjM" in body:
            nb = body.replace("ProjM", "ProjP", 1)
            return (
                text[:s] + nb + text[e:],
                name,
                [name, "ProjM", "ProjP"],
                f"First `ProjM` in `{name}` changed to `ProjP` (a left-handed "
                "current became right-handed).",
            )
    return None


OPERATORS = {
    "drop_eps": op_drop_eps,
    "flip_charge": op_flip_charge,
    "drop_cutoff": op_drop_cutoff,
    "drop_cc": op_drop_cc,
    "sqrt_swap": op_sqrt_swap,
    "factor2": op_factor2,
    "drop_term": op_drop_term,
    "swap_chirality": op_swap_chirality,
}


def _paper_tex(page: str) -> Path:
    texs = sorted((TEXT_ROOT / page / "text").glob("*_source.tex"))
    if texs:
        return texs[0]
    txts = sorted((TEXT_ROOT / page / "text").glob("*.txt"))
    if not txts:
        raise FileNotFoundError(f"no paper text for {page}")
    return txts[0]


def build_cases() -> list:
    cases = []
    for page, run in BASES.items():
        frs = sorted(glob.glob(str(HERE / page / run / "model" / "*.fr")))
        if not frs:
            print(f"[prepare] {page}: no base .fr under {run}", file=sys.stderr)
            continue
        base = Path(frs[0]).read_text()
        cases.append(
            {
                "id": f"{page}__control",
                "page": page,
                "kind": "control",
                "source": frs[0],
                "operator": None,
                "term": None,
                "tokens": [],
                "defect": None,
                "text": base,
            }
        )
        for opname, fn in OPERATORS.items():
            res = fn(base)
            if res is None:
                continue
            new, term, tokens, desc = res
            if new == base or sanitize.sanitize_fr(new)[0] == sanitize.sanitize_fr(base)[0]:
                continue  # the change landed in a comment: not a mutant
            cases.append(
                {
                    "id": f"{page}__{opname}",
                    "page": page,
                    "kind": "mutant",
                    "source": frs[0],
                    "operator": opname,
                    "term": term,
                    "tokens": tokens,
                    "defect": desc,
                    "text": new,
                }
            )
    for page, (rel, desc) in REAL.items():
        p = HERE / page / rel
        if p.is_file():
            cases.append(
                {
                    "id": f"{page}__real",
                    "page": page,
                    "kind": "real",
                    "source": str(p),
                    "operator": "physicist_finding",
                    "term": None,
                    "tokens": [],
                    "defect": desc,
                    "text": p.read_text(),
                }
            )
    return cases


RECON_POLICY = (
    "RUN-TAG: {tag}\n\n"
    "Your working directory for this task is {sandbox}. It contains exactly one "
    "file, sanitized.fr. Tool policy: use only the Read tool, and only on files "
    "under {sandbox}; then use the Write tool exactly once to write your document "
    "to {output}. No shell, no search, no web, no other files or directories. "
    "After writing, reply with the single line DONE.\n\n"
)

CROSS_POLICY = (
    "RUN-TAG: {tag}\n\n"
    "Your working directory for this task is {sandbox}. It contains exactly two "
    "files, paper.tex and reconstruction.md. Tool policy: use only the Read tool, "
    "and only on files under {sandbox} (paper.tex is long: read it completely, in "
    "chunks with offset and limit); then use the Write tool exactly once to write "
    "your document to {output}. No shell, no search, no web, no other files or "
    "directories. After writing, reply with the single line DONE.\n\n"
)


def _rewrite_final(p: str, output: str) -> str:
    return p.replace(
        "Your final message must be the complete markdown document and nothing else.",
        f"Write the complete markdown document to {output}.",
    )


def prepare_recon(args):
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    cases = build_cases()
    manifest = []
    for c in cases:
        d = out / c["id"]
        d.mkdir(exist_ok=True)
        (d / "model.fr").write_text(c["text"])
        san, rep = sanitize.sanitize_fr(c["text"])
        (d / "sanitized.fr").write_text(san)
        (d / "sanitizer_report.json").write_text(json.dumps(rep, indent=2))
        meta = {k: v for k, v in c.items() if k != "text"}
        (d / "case.json").write_text(json.dumps(meta, indent=2))
        sb = d / "recon_sandbox"
        if sb.exists():
            shutil.rmtree(sb)
        sb.mkdir()
        shutil.copyfile(d / "sanitized.fr", sb / "sanitized.fr")
        output = d / "reconstruction.md"
        if output.is_file() and not args.force:
            continue
        tag = f"XM-RECON-{c['id']}"
        prompt = RECON_POLICY.format(tag=tag, sandbox=sb, output=output) + _rewrite_final(
            prompts.RECONSTRUCT_PROMPT, str(output)
        )
        (d / "prompt_recon.txt").write_text(prompt)
        manifest.append(
            {"id": c["id"], "tag": tag, "sandbox": str(sb), "output": str(output), "prompt": prompt}
        )
    (out / "manifest_recon.json").write_text(json.dumps(manifest, indent=2))
    (out / "cases.json").write_text(
        json.dumps([{k: v for k, v in c.items() if k != "text"} for c in cases], indent=2)
    )
    kinds = {}
    for c in cases:
        kinds[c["kind"]] = kinds.get(c["kind"], 0) + 1
    print(
        f"[prepare-recon] {len(cases)} cases {kinds}; {len(manifest)} to run "
        f"-> {out / 'manifest_recon.json'}"
    )
    return 0


def prepare_cross(args):
    out = Path(args.out).resolve()
    cases = json.loads((out / "cases.json").read_text())
    manifest = []
    for c in cases:
        d = out / c["id"]
        recon = d / "reconstruction.md"
        if not recon.is_file() or not recon.read_text().strip():
            print(f"[prepare-cross] {c['id']}: no reconstruction.md, skipped", file=sys.stderr)
            continue
        sb = d / "cross_sandbox"
        # A run may be in flight on an existing sandbox; rebuild it only with --force.
        if not sb.exists() or args.force:
            if sb.exists():
                shutil.rmtree(sb)
            sb.mkdir()
            shutil.copyfile(_paper_tex(c["page"]), sb / "paper.tex")
            shutil.copyfile(recon, sb / "reconstruction.md")
        output = d / "crosscheck.md"
        if output.is_file() and not args.force:
            continue
        tag = f"XM-CROSS-{c['id']}"
        prompt = CROSS_POLICY.format(tag=tag, sandbox=sb, output=output) + _rewrite_final(
            prompts.CROSSCHECK_PROMPT, str(output)
        )
        (d / "prompt_cross.txt").write_text(prompt)
        manifest.append(
            {"id": c["id"], "tag": tag, "sandbox": str(sb), "output": str(output), "prompt": prompt}
        )
    (out / "manifest_cross.json").write_text(json.dumps(manifest, indent=2))
    print(f"[prepare-cross] {len(manifest)} to run -> {out / 'manifest_cross.json'}")
    return 0


JUDGE_PROMPT = """\
RUN-TAG: {tag}

You are grading the output of an automated physics reviewer. Read exactly two
files with the Read tool, nothing else, no shell, no search:
  {cross}   (the reviewer's term-by-term comparison of a model against a paper)
  {case}    (metadata; the field "defect" describes ONE defect that was
            deliberately injected into the model, or null for a control file)

Answer these questions and write the answer as JSON to {output} with the Write
tool (exactly once), then reply with the single line DONE.

JSON fields:
  "named": "yes" | "partial" | "no" | "n/a"  -- does the reviewer's document
      point at the injected defect? "yes" = a disagree/missing/extra row or a
      listed disagreement describes this specific defect (the right term or
      field AND the right kind of error: sign, factor, missing contraction,
      missing conjugation, missing cutoff, missing term, wrong chirality);
      "partial" = the right term or field is flagged but the stated error is
      different or vague; "no" = not flagged; "n/a" = control file.
  "quote": the sentence or table row that names it (empty if "no").
  "severity": the severity the reviewer gave it (substantive / convention /
      cosmetic / none).
  "other_substantive": number of OTHER disagreements the reviewer marked
      substantive that are not this defect (for a control file: all of them).
  "other_list": one line each for those other substantive disagreements.
  "note": one sentence of your own on whether the reviewer's overall
      assessment would send a physicist to the right place.
"""


def prepare_judge(args):
    out = Path(args.out).resolve()
    cases = json.loads((out / "cases.json").read_text())
    manifest = []
    for c in cases:
        d = out / c["id"]
        cc = d / "crosscheck.md"
        if not cc.is_file():
            continue
        output = d / "judge.json"
        if output.is_file() and not args.force:
            continue
        tag = f"XM-JUDGE-{c['id']}"
        prompt = JUDGE_PROMPT.format(tag=tag, cross=cc, case=d / "case.json", output=output)
        (d / "prompt_judge.txt").write_text(prompt)
        manifest.append({"id": c["id"], "tag": tag, "output": str(output), "prompt": prompt})
    (out / "manifest_judge.json").write_text(json.dumps(manifest, indent=2))
    print(f"[prepare-judge] {len(manifest)} to run -> {out / 'manifest_judge.json'}")
    return 0


def audit(args):
    """Check every subagent transcript that carries one of our RUN-TAGs: every
    Read/Write path must sit inside that case's sandbox or be its output."""
    out = Path(args.out).resolve()
    cases = json.loads((out / "cases.json").read_text())
    by_tag = {}
    for c in cases:
        d = out / c["id"]
        by_tag[f"XM-RECON-{c['id']}"] = (
            c["id"],
            "recon",
            d / "recon_sandbox",
            d / "reconstruction.md",
        )
        by_tag[f"XM-CROSS-{c['id']}"] = (c["id"], "cross", d / "cross_sandbox", d / "crosscheck.md")
        by_tag[f"XM-JUDGE-{c['id']}"] = (c["id"], "judge", d, d / "judge.json")
    report = {}
    for path in sorted(glob.glob(os.path.join(args.transcripts_dir, "*.jsonl"))):
        lines = Path(path).read_text(errors="replace").splitlines()
        tag = None
        for ln in lines[:5]:
            m = re.search(r"XM-(?:RECON|CROSS|JUDGE)-[\w\-]+", ln) or re.search(
                r"crosscheck_mutation/([\w\-]+)/prompt_(recon|cross|judge)\.txt", ln
            )
            if m:
                tag = (
                    m.group(0)
                    if m.group(0).startswith("XM-")
                    else f"XM-{m.group(2).upper()}-{m.group(1)}"
                )
                break
        if tag is None or tag not in by_tag:
            continue
        cid, phase, sb, output = by_tag[tag]
        tools, problems = [], []
        for ln in lines:
            try:
                ev = json.loads(ln)
            except json.JSONDecodeError:
                continue
            msg = ev.get("message") or {}
            for blk in (msg.get("content") or []) if isinstance(msg.get("content"), list) else []:
                if blk.get("type") != "tool_use":
                    continue
                name = blk.get("name")
                inp = blk.get("input") or {}
                tools.append(name)
                p = inp.get("file_path") or inp.get("path") or ""
                if name == "Read":
                    if Path(p).name in (
                        "prompt_recon.txt",
                        "prompt_cross.txt",
                        "prompt_judge.txt",
                        "case.json",
                        "crosscheck.md",
                    ) and Path(p).resolve().parent in (sb.resolve().parent, sb.resolve()):
                        continue
                    if not Path(p).resolve().is_relative_to(sb.resolve()):
                        problems.append(f"Read outside sandbox: {p}")
                elif name == "Write":
                    if Path(p).resolve() != output.resolve():
                        problems.append(f"Write to unexpected path: {p}")
                else:
                    problems.append(f"tool {name} not allowed")
        report.setdefault(cid, {})[phase] = {
            "transcript": path,
            "n_tools": len(tools),
            "problems": problems,
            "audit_ok": not problems,
        }
    (out / "audit.json").write_text(json.dumps(report, indent=2))
    bad = sum(1 for c in report.values() for ph in c.values() if not ph["audit_ok"])
    print(
        f"[audit] {len(report)} cases with transcripts, {bad} phase(s) with policy problems "
        f"-> {out / 'audit.json'}"
    )
    return 0


VERDICT_RE = re.compile(
    r"\*{0,2}(agree|disagree|missing-in-reconstruction|extra-in-reconstruction)\*{0,2}", re.I
)


def _rows(md: str):
    rows = []
    for ln in md.splitlines():
        if not ln.strip().startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        v = None
        for c in cells:
            m = VERDICT_RE.fullmatch(c.strip("* "))
            if m:
                v = m.group(1).lower()
                break
        if v:
            rows.append({"cells": cells, "verdict": v})
    return rows


def _flags(md: str):
    """Non-agree rows plus the severity list after the table."""
    rows = [r for r in _rows(md) if r["verdict"] != "agree"]
    sev = re.findall(
        r"^\s*(?:[-*]|\d+\.)\s*(.*?(substantive|convention|cosmetic).*)$", md, re.M | re.I
    )
    return rows, [s[0] for s in sev]


def score(args):
    out = Path(args.out).resolve()
    cases = json.loads((out / "cases.json").read_text())
    results = []
    for c in cases:
        d = out / c["id"]
        cc = d / "crosscheck.md"
        r = dict(c)
        r["has_recon"] = (d / "reconstruction.md").is_file()
        r["has_cross"] = cc.is_file()
        if cc.is_file():
            md = cc.read_text()
            rows, sev = _flags(md)
            r["n_rows"] = len(_rows(md))
            r["n_flagged"] = len(rows)
            r["n_substantive"] = sum(1 for s in sev if re.search(r"substantive", s, re.I))
            # identifiers of any length (quantum numbers Q, Y); not "?" or a bare factor "2"
            toks = [t for t in c["tokens"] if re.fullmatch(r"[A-Za-z_]\w*", t)]
            hit = []
            for row in rows:
                blob = " | ".join(row["cells"])
                if any(re.search(rf"\b{re.escape(t)}\b", blob) for t in toks):
                    hit.append(blob[:300])
            for s in sev:
                if any(re.search(rf"\b{re.escape(t)}\b", s) for t in toks):
                    hit.append(s[:300])
            r["rule_hits"] = hit
            r["rule_detected"] = bool(hit) if c["kind"] == "mutant" else None
        jp = d / "judge.json"
        if jp.is_file():
            try:
                txt = jp.read_text()
                m = re.search(r"\{.*\}", txt, re.S)
                r["judge"] = json.loads(m.group(0) if m else txt)
            except json.JSONDecodeError as e:
                r["judge"] = {"error": str(e)}
        results.append(r)
    (out / "results.json").write_text(json.dumps(results, indent=2))
    mut = [r for r in results if r["kind"] == "mutant" and r.get("has_cross")]
    ctl = [r for r in results if r["kind"] == "control" and r.get("has_cross")]
    real = [r for r in results if r["kind"] == "real" and r.get("has_cross")]
    lines = [
        "# Crosscheck mutation test — rule-based scoring",
        "",
        f"cases scored: {len(mut)} mutants, {len(ctl)} controls, {len(real)} real-finding files",
        "",
    ]
    if mut:
        det = sum(1 for r in mut if r["rule_detected"])
        lines.append(
            "- mutants where a flagged row or severity line names the mutated symbol: "
            f"**{det}/{len(mut)}**"
        )
    if ctl:
        lines.append(
            "- controls: flagged rows / substantive lines per file: "
            + ", ".join(f"{r['page']} {r['n_flagged']}/{r['n_substantive']}" for r in ctl)
        )
    judged = [r for r in results if isinstance(r.get("judge"), dict) and "named" in r["judge"]]
    if judged:
        jm = [r for r in judged if r["kind"] == "mutant"]
        jr = [r for r in judged if r["kind"] == "real"]
        jc = [r for r in judged if r["kind"] == "control"]

        def named(rs):
            n = [r["judge"].get("named") for r in rs]
            return (
                f"yes {n.count('yes')}, partial {n.count('partial')}, no {n.count('no')} "
                f"of {len(rs)}"
            )

        def other_mean(rs):
            total = sum(int(r["judge"].get("other_substantive") or 0) for r in rs)
            return f"{total / max(1, len(rs)):.1f}"

        lines += [
            "",
            "## Judge (subagent reading crosscheck.md against the defect description)",
            "",
            f"- mutants named: {named(jm)}",
            f"- real findings named: {named(jr)}",
            f"- other substantive disagreements per file: mutants mean {other_mean(jm)}, "
            f"controls mean {other_mean(jc)}",
        ]
        by_op = {}
        for r in jm:
            by_op.setdefault(r["operator"], []).append(r["judge"].get("named"))
        lines += ["", "| operator | yes | partial | no |", "|---|---|---|---|"]
        for op, vs in sorted(by_op.items()):
            lines.append(f"| {op} | {vs.count('yes')} | {vs.count('partial')} | {vs.count('no')} |")
    lines += [
        "",
        "| case | kind | operator | term | flagged rows | substantive | rule hit | judge "
        "| other subst. |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in results:
        if not r.get("has_cross"):
            lines.append(
                f"| {r['id']} | {r['kind']} | {r['operator'] or ''} | {r['term'] or ''} "
                "| — | — | no crosscheck | | |"
            )
            continue
        j = r.get("judge") or {}
        lines.append(
            f"| {r['id']} | {r['kind']} | {r['operator'] or ''} | {r['term'] or ''} | "
            f"{r['n_flagged']}/{r['n_rows']} | {r['n_substantive']} | "
            f"{'yes' if r.get('rule_detected') else ('n/a' if r['kind'] != 'mutant' else 'no')} | "
            f"{j.get('named', '')} | {j.get('other_substantive', '')} |"
        )
    (out / "score_rule.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name, fn in (
        ("prepare-recon", prepare_recon),
        ("prepare-cross", prepare_cross),
        ("prepare-judge", prepare_judge),
        ("audit", audit),
        ("score", score),
    ):
        p = sub.add_parser(name)
        p.add_argument("--out", default=str(HERE / "crosscheck_mutation"))
        p.add_argument("--force", action="store_true")
        if name == "audit":
            p.add_argument("--transcripts-dir", required=True)
        p.set_defaults(fn=fn)
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
