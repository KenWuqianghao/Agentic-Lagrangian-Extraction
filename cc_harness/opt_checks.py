"""The optimisation arm's extra checks (ablation arm `opt`).

Each one names a defect that the stored runs show the chain does not name
(benchmarks/heptapod_ablation/HEPTAPOD_FIXES.md has the evidence). They are
candidates for heptapod upstream; here they run only in the `opt` arm, so the
`full` arm stays the stored harness.

Lint rules, on the .fr text:
  partial_index_fermion   `l[ff]` on a field with indices (spin, generation):
                          the one index goes to the spin slot
  class_outside_list      a class statement that is not an entry of
                          M$ClassesDescription: FeynRules ignores it
  duplicate_mass_parameter  a mass or width named in a class and declared
                          again in M$Parameters: MadGraph rejects the UFO
  shared_lha_block        indexed External parameters on one BlockName
                          without OrderBlock: their UFO entries collide
  nonpositive_order       InteractionOrder with a power below 1: couplings
                          of order '1', which MadGraph rejects

Report sections, on the chain's outputs:
  new particles that are in no UFO vertex; the mass-spectrum rows that
  disagree; the UFO parameter names that are defined twice.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ALE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ALE / "benchmarks"))
import fr_lint  # noqa: E402

SM_PARTICLES = frozenset(json.loads(
    (ALE / "benchmarks" / "heptapod_ablation" / "sm_ufo_particles.json").read_text())["particles"])
# Index counts of the SM.fr fermion classes; the first index is spin.
SM_FERMION_INDICES = {"vl": 2, "l": 2, "uq": 3, "dq": 3, "LL": 3, "lR": 2, "QL": 4, "uR": 3, "dR": 3}


def _finding(rule: str, stage: str, line: int | None, message: str) -> dict:
    return {"rule": rule, "stage": stage, "line": line, "message": message}


def _line(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def _fermion_indices(classes: list[dict]) -> dict:
    """Class name -> number of indices including spin, for the model's own
    fermion classes and SM.fr's."""
    counts = dict(SM_FERMION_INDICES)
    for c in classes:
        name = fr_lint._prop(c["body"], "ClassName")
        if name and c["head"].startswith("F["):
            idx = fr_lint._prop(c["body"], "Indices") or "{}"
            counts[name] = 1 + len(re.findall(r"Index\[", idx))
    return counts


def lint(raw: str) -> list[dict]:
    text = fr_lint.strip_comments(raw)
    out: list[dict] = []
    block = re.search(r"M\$ClassesDescription\s*=\s*\{", text)
    list_end = fr_lint._matching(text, block.end() - 1) if block else -1
    classes = fr_lint._entries(fr_lint._block(text, "ClassesDescription"))
    params = fr_lint._entries(fr_lint._block(text, "Parameters"))

    counts = _fermion_indices(classes)
    use = re.compile(r"(?<![A-Za-z0-9$])(" + "|".join(map(re.escape, counts)) + r")(bar)?\[([^\[\]]*)\]")
    seen = set()
    for term in fr_lint.term_defs(text):
        for m in use.finditer(term["body"]):
            n = len([a for a in m.group(3).split(",") if a.strip()])
            near = term["body"][max(0, m.start() - 2):m.end() + 2]
            if 0 < n < counts[m.group(1)] and "." in near and m.group(0) not in seen:
                seen.add(m.group(0))
                out.append(_finding(
                    "partial_index_fermion", "checks", term["line"] + term["body"].count("\n", 0, m.start()),
                    f"`{m.group(0)}` gives {n} of the {counts[m.group(1)]} indices of `{m.group(1)}`; FeynRules fills "
                    "them from the left and the first is spin, so this index is read as a spin index. The term then "
                    "fails hermiticity or drops out of the UFO. Write the field with no index inside the chain (use "
                    "the class members `e`, `mu`, `ta`, ... or a matrix coupling between two index-free fields), or "
                    "give every index."))

    for m in re.finditer(r"^[ \t]*([SFVUTR]\[\s*\d+\s*\])\s*==\s*\{", text, re.M):
        if not block or not (block.end() <= m.start() <= list_end):
            out.append(_finding(
                "class_outside_list", "checks", _line(text, m.start()),
                f"the class `{m.group(1)}` is a statement outside M$ClassesDescription; FeynRules ignores it, with no "
                "message. Put it inside the M$ClassesDescription list (this is how an SM class such as Phi is "
                "redeclared)."))

    declared = {p["head"]: p for p in params}
    for c in classes:
        for key in ("Mass", "Width"):
            val = fr_lint._prop(c["body"], key) or ""
            for sym in re.findall(r"\{\s*([A-Za-z]\w*)\s*,", val):
                p = declared.get(sym)
                if p and "Internal" not in (fr_lint._prop(p["body"], "ParameterType") or ""):
                    out.append(_finding(
                        "duplicate_mass_parameter", "mg5", _line(text, text.find(sym + " ==")),
                        f"`{sym}` is declared by `{key} -> {{{sym}, ...}}` of class "
                        f"`{fr_lint._prop(c['body'], 'ClassName')}` and again in M$Parameters; the UFO then defines it "
                        "twice and MadGraph stops with \"name ... define multiple time\". Remove the M$Parameters entry."))

    blocks: dict = {}
    for p in params:
        if "External" in (fr_lint._prop(p["body"], "ParameterType") or "") and fr_lint._prop(p["body"], "Indices") \
                and not fr_lint._prop(p["body"], "OrderBlock"):
            blocks.setdefault(fr_lint._prop(p["body"], "BlockName"), []).append(p["head"])
    for name, members in blocks.items():
        if name and len(members) > 1:
            out.append(_finding(
                "shared_lha_block", "mg5", None,
                f"the indexed External parameters {', '.join(members)} share BlockName `{name}`; their components get "
                "the same LHA codes, the UFO defines one name several times, and MadGraph rejects it. Give each "
                "tensor its own BlockName."))

    for p in params:
        order = fr_lint._prop(p["body"], "InteractionOrder") or ""
        if re.search(r",\s*(-\s*\d+|0)\s*\}", order):
            out.append(_finding(
                "nonpositive_order", "warn", _line(text, text.find(p["head"] + " ==")),
                f"`{p['head']}` has InteractionOrder {order}; a product with another parameter can then have order 0, "
                "FeynRules writes the coupling with order '1', and MadGraph rejects it. Check the orders of the couplings "
                "that use it."))
    return out


# ------------------------------------------------------------ the chain's outputs
def particles_without_vertex(ufo: Path) -> list[str]:
    """New particles (not in the UFO of SM.fr alone) that no vertex contains.
    Ghosts are skipped."""
    if not (ufo / "vertices.py").is_file() or not (ufo / "particles.py").is_file():
        return []
    declared = set(re.findall(r"^(\w+) = Particle\(", (ufo / "particles.py").read_text(errors="replace"), re.M))
    used = set(re.findall(r"P\.(\w+)", (ufo / "vertices.py").read_text(errors="replace")))
    return sorted(n for n in declared - SM_PARTICLES
                  if n not in used and n + "__tilde__" not in used and not n.startswith("gh"))


def duplicate_ufo_parameters(ufo: Path) -> list[str]:
    f = ufo / "parameters.py"
    names = re.findall(r"^(\w+) = Parameter\(", f.read_text(errors="replace"), re.M) if f.is_file() else []
    return sorted({n for n in names if names.count(n) > 1})


def mass_rows(log: str) -> list[dict]:
    rows = re.findall(r"^HEPTAPOD-MASS\|particle=([^|]*)\|derived=([^|]*)\|declared=([^|]*)\|agrees=(\w+)", log, re.M)
    return [{"particle": p, "derived": d, "declared": c} for p, d, c, ok in rows if ok != "True"]


def report_sections(row: dict, log: str) -> tuple[str, list[str]]:
    """Extra report text, and the new particles without a vertex (a model
    with any is not a pass in the `opt` arm)."""
    parts: list[str] = []
    ufo = Path(row["ufo_dir"]) if row.get("ufo_dir") else None
    inert = particles_without_vertex(ufo) if ufo and row.get("compile_ok") else []
    if inert:
        parts += ["## New particles that are in no vertex of the UFO",
                  f"{', '.join(inert)}: declared, and no interaction of the model contains them. FeynRules dropped the "
                  "terms that hold them, with no message. The usual cause is a field written with a partial index list "
                  "(lint rule partial_index_fermion) or an index that does not match the class. The chain's checks "
                  "pass such a model; it is not the paper's model. Fix the terms until every new particle has a vertex.", ""]
    rows = mass_rows(log)
    if rows:
        parts += ["## Mass spectrum: the rows that disagree", "", "| particle | mass from the Lagrangian | declared mass |",
                  "|---|---|---|", *[f"| {r['particle']} | {r['derived']} | {r['declared']} |" for r in rows], ""]
        if all(r["particle"].startswith("gh") or r["particle"] in ("G0", "GP") for r in rows):
            parts += ["Only ghost or Goldstone rows disagree. That happens after a Higgs-doublet override that changes "
                      "the vev in Feynman gauge (SM.fr's default). Put `FeynmanGauge = False;` at the top of model.fr: "
                      "the model is then built in unitary gauge and these states are absent.", ""]
    dup = duplicate_ufo_parameters(ufo) if ufo and row.get("compile_ok") else []
    if dup:
        parts += ["## UFO parameters defined more than once",
                  f"{', '.join(dup[:20])}: MadGraph rejects the UFO (\"name ... define multiple time\"). Each is either a "
                  "mass or width named in a class and declared again in M$Parameters (remove that entry), or a "
                  "component of tensors that share one BlockName (give each tensor its own BlockName).", ""]
    return "\n".join(parts), inert
