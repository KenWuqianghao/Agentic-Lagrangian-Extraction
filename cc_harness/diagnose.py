"""Agent-facing diagnostics for one validation row. No Wolfram, no MadGraph.

Three things the scoring report does not say, rebuilt from what the
diagnostic driver (wl/UFO_generator_diag.wl) and the UFO leave on disk:

* hermiticity: each non-zero vertex of ``L - HC[L]`` (fields + coefficient)
  and the named Lagrangian block that holds those fields;
* mass_diagonal: the off-diagonal mass terms and the tadpoles, with their
  coefficients and numerical values;
* MadGraph import: the UFO object that broke (parameter, coupling, particle),
  its expression, and the .fr lines that define it.

Every function takes plain values and returns plain values, so the tests run
on stored logs and UFO snippets.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Optional

_HERM = re.compile(r"^HEPTAPOD-HERM\|i=(\d+)\|fields=([^|]*)(?:\|unreduced=([^|]*))?\|expr=(.*)$", re.M)
_HERMBLOCK = re.compile(r"^HEPTAPOD-HERMBLOCK\|block=([^|]*)\|contents=(.*)$", re.M)
_MASSTERM = re.compile(r"^HEPTAPOD-MASSTERM\|fields=([^|]*)\|coefficient=([^|]*)\|numeric=(.*)$", re.M)
_TADPOLE = re.compile(r"^HEPTAPOD-TADPOLE\|field=([^|]*)\|coefficient=([^|]*)\|numeric=(.*)$", re.M)


def parse_diag_lines(log: str) -> dict:
    herm = [{"i": int(i), "fields": [f for f in fs.split(",") if f],
             "unreduced": [f for f in (un or "").split(",") if f], "expr": e.strip()}
            for i, fs, un, e in _HERM.findall(log)]
    blocks: Dict[str, Optional[List[List[str]]]] = {}
    for b, c in _HERMBLOCK.findall(log):
        c = c.strip()
        blocks[b] = None if c == "TIMEOUT" else [x.split() for x in c.split(";") if x.strip()]
    mass = [{"fields": fs.split(","), "coefficient": c.strip(), "numeric": n.strip()}
            for fs, c, n in _MASSTERM.findall(log)]
    tad = [{"field": f, "coefficient": c.strip(), "numeric": n.strip()}
           for f, c, n in _TADPOLE.findall(log)]
    return {"herm": herm, "blocks": blocks, "massterms": mass, "tadpoles": tad}


def _conj(name: str) -> str:
    return name[:-3] if name.endswith("bar") else name + "bar"


def localize_herm(herm: List[dict], blocks: Dict[str, Optional[List[List[str]]]]) -> List[dict]:
    """Attach to each non-hermitian vertex the blocks whose expanded terms
    carry the same field multiset, or its conjugate (the missing partner of
    a term shows up with the conjugated fields)."""
    def norm(fs):
        # Self-conjugate fields (Z, a Majorana N) have no `bar` partner, so a
        # conjugated key can name a field that does not exist; the field set
        # without `bar` still identifies the block.
        return tuple(sorted(f[:-3] if f.endswith("bar") else f for f in fs))
    exact = {b: {tuple(sorted(fc)) for fc in (c or [])} for b, c in blocks.items()}
    loose = {b: {norm(fc) for fc in (c or [])} for b, c in blocks.items()}
    out = []
    for v in herm:
        key = tuple(sorted(v["fields"]))
        ckey = tuple(sorted(_conj(f) for f in v["fields"]))
        hit = sorted(b for b, cs in exact.items() if key in cs or ckey in cs)
        if not hit:
            hit = sorted(b for b, cs in loose.items() if norm(v["fields"]) in cs)
        if not hit and v.get("unreduced"):
            # An unreduced vertex lumps many terms together, so its field list
            # is a union: take the blocks with terms whose fields all lie in
            # it, most such terms first.
            vs = set(norm(v["fields"]))
            # Count only terms that carry one of the vertex's own legs (the
            # boson of a current): a kinetic or mass term of the fermions in
            # the chain is a subset too, and says nothing.
            legs = set(norm([f for f in v["fields"] if f not in v["unreduced"]]))
            score = {b: sum(1 for fc in cs if len(fc) >= 2 and set(fc) <= vs and (not legs or set(fc) & legs))
                     for b, cs in loose.items()}
            hit = [b for b, n in sorted(score.items(), key=lambda x: (-x[1], x[0])) if n > 0][:3]
        out.append({**v, "blocks": hit})
    return out


# ------------------------------------------------------------------ MadGraph
_UFO_OBJ = re.compile(r"^(\w+)\s*=\s*(Parameter|Coupling|Particle|Vertex|Lorentz|CouplingOrder|Decay)\(")
_UFO_FRAME = re.compile(r'File "[^"]*/UFO/(\w+\.py)", line (\d+)')
_NAME_ERR = re.compile(r"NameError: name '([^']+)' is not defined")
_PY_WORDS = {"name", "value", "texname", "lhablock", "lhacode", "nature", "type", "order",
             "complex", "cmath", "cos", "sin", "tan", "sqrt", "pi", "real", "imag", "conjugate",
             "abs", "exp", "log", "True", "False", "None", "Parameter", "Coupling", "Particle",
             "Vertex", "Lorentz", "external", "internal", "P", "C", "L", "particles", "color",
             "lorentz", "couplings", "spin", "mass", "width", "pdg_code", "charge", "antiname",
             "GhostNumber", "LeptonNumber", "Y", "Q", "propagating", "line", "Param", "ZERO",
             "ReplaceAll", "Dot", "Gamma", "Identity", "ProjM", "ProjP", "Index", "PYList",
             "ClassAttributeCreation", "Spin", "Lorentz", "Ext", "Int", "I", "ee", "cw", "sw",
             "vev", "gw", "g1", "gs", "complexconjugate"}


# FeynRules words that also appear, mangled, in a broken UFO line
# (`ConvertSpinToString[0]<>F<>...`): they name no model symbol.
_FR_HEADS = {"F", "S", "V", "U", "T", "W", "R", "PRIVATE", "ConvertSpinToString", "PartNameMG",
             "CreateObjectParticleName", "MakeIdenticalFermions", "anti", "Module", "Block"}


def _ufo_object(lines: List[str], lineno: int) -> tuple[Optional[str], int, int]:
    """(object name, start, end) of the top-level UFO object around a line."""
    i = min(max(lineno - 1, 0), len(lines) - 1)
    start = None
    for k in range(i, -1, -1):
        m = _UFO_OBJ.match(lines[k])
        if m:
            start = k
            name = m.group(1)
            break
    if start is None:
        return None, i, i
    end = start + 1
    while end < len(lines) and not re.match(r"^\w+\s*=", lines[end]):
        end += 1
    return name, start, end


def _fr_symbols(fr_text: str) -> dict:
    params = set(re.findall(r"^\s*(\w+)\s*==\s*\{", fr_text, re.M))
    classes = set(re.findall(r"ClassName\s*->\s*(\w+)", fr_text))
    members = set()
    for m in re.findall(r"ClassMembers\s*->\s*\{([^}]*)\}", fr_text):
        members |= {x.strip() for x in m.split(",") if x.strip()}
    pnames = {}
    for cls_block in re.finditer(r"ClassName\s*->\s*(\w+)(.*?)(?=ClassName\s*->|\Z)", fr_text, re.S):
        cls, body = cls_block.group(1), cls_block.group(2)
        for key in ("ParticleName", "AntiParticleName"):
            m = re.search(key + r'\s*->\s*(\{[^}]*\}|"[^"]*")', body)
            if m:
                for nm in re.findall(r'"([^"]*)"', m.group(1)):
                    pnames[nm] = cls
    return {"params": params, "classes": classes, "members": members, "particle_names": pnames}


SM_FR = Path.home() / "Documents/Github/heptapod/tools/feynrules/test_files/models/SM.fr"


def _sm_member_class() -> Dict[str, str]:
    """SM.fr particle and member names -> the class the add-on writes (ve -> vl)."""
    if not SM_FR.is_file():
        return {}
    t = SM_FR.read_text(errors="replace")
    out: Dict[str, str] = {}
    for m in re.finditer(r"ClassName\s*->\s*(\w+)(.*?)(?=\s[FSVUWT]\[\d+\]\s*==|\Z)", t, re.S):
        cls, body = m.group(1), m.group(2)
        out[cls] = cls
        mm = re.search(r"ClassMembers\s*->\s*\{([^}]*)\}", body)
        for mem in (mm.group(1).split(",") if mm else []):
            out[mem.strip()] = cls
        for nm in re.findall(r'ParticleName\s*->\s*(?:\{([^}]*)\}|"([^"]*)")', body):
            for x in re.findall(r'"([^"]*)"', nm[0]) or [nm[1]]:
                out.setdefault(x.strip(), cls)
    return out


_SM_MAP = _sm_member_class()


def _fr_candidates(ident: str, sym: dict) -> List[str]:
    """.fr symbols a UFO identifier can come from: itself, a tensor parameter
    whose component it is (yM1x2 -> yM, VlN1 -> VlN), or the class behind a
    particle name (ve~ -> vl member ve)."""
    out = []
    for s in (ident, ident.replace("__tilde__", "~").rstrip("~")):
        if s in sym["params"] or s in sym["classes"] or s in sym["members"]:
            out.append(s)
        if s in sym["particle_names"]:
            out.append(sym["particle_names"][s])
    base = ident.replace("__tilde__", "").replace("__minus__", "").replace("__plus__", "")
    if base in _SM_MAP:
        out.append(_SM_MAP[base])
    m = re.match(r"^([A-Za-z]\w*?)(\d+(?:x\d+)*)$", ident)
    if m and m.group(1) in sym["params"]:
        out.append(m.group(1))
    return list(dict.fromkeys(out))


def _vertex_particles(ufo_dir: Path, coupling: str) -> List[str]:
    vf = ufo_dir / "vertices.py"
    if not vf.is_file():
        return []
    txt = vf.read_text(errors="replace")
    parts = []
    for blk in re.split(r"\n(?=V_\d+\s*=\s*Vertex\()", txt):
        if re.search(rf"\bC\.{re.escape(coupling)}\b", blk):
            # Up to the end of the particles line: a corrupted UFO nests
            # brackets inside it (P.<>CreateObjectParticleName[PartNameMG[ve[...]]]).
            m = re.search(r"particles\s*=\s*\[(.*?)\]\s*,\s*\n", blk, re.S)
            if m:
                parts += re.findall(r"P\.(\w+)", m.group(1))
                parts += re.findall(r"PartNameMG\[(?:anti\[)?([A-Za-z]\w*)", m.group(1))
    return [x for x in dict.fromkeys(parts) if x not in ("CreateObjectParticleName", "MakeIdenticalFermions", "anti")]


def _fr_lines(fr_text: str, symbols: List[str], limit: int = 6) -> List[dict]:
    """.fr lines that declare or use the symbols, declarations first, then the
    Lagrangian lines that mention the most of them."""
    lines = fr_text.splitlines()
    decl, use = [], []
    for n, ln in enumerate(lines, 1):
        s = ln.strip()
        if not s or s.startswith("(*"):
            continue
        hits = [x for x in symbols if re.search(rf"\b{re.escape(x)}(bar)?\b", ln)]
        if not hits:
            continue
        if any(re.match(rf"^\s*{re.escape(x)}\s*==\s*\{{", ln) or
               re.search(rf"ClassName\s*->\s*{re.escape(x)}\b", ln) for x in hits):
            decl.append({"line": n, "text": ln.rstrip(), "symbols": hits, "kind": "declaration"})
        else:
            use.append({"line": n, "text": ln.rstrip(), "symbols": hits, "kind": "use"})
    use.sort(key=lambda d: (-len(d["symbols"]), d["line"]))
    # A parameter declaration is shown whole: an LHA or index error lives in
    # one of its options (OrderBlock, Indices, Value), not on the head line.
    for d in decl:
        if re.match(r"^\s*\w+\s*==\s*\{", d["text"]):
            blk, depth = [], 0
            for ln in lines[d["line"] - 1:d["line"] + 14]:
                blk.append(ln.rstrip())
                depth += ln.count("{") - ln.count("}")
                if depth <= 0:
                    break
            d["block"] = "\n".join(blk)
    return (decl + use)[:limit]


def mg5_backtrace(row: dict, fr_text: str) -> List[dict]:
    """Each UFO location that broke the import, the UFO object there, its
    text, and the .fr lines behind it."""
    ufo_dir = Path(row.get("ufo_dir") or "")
    locs = [(e["file"], int(e["line"]), e.get("msg", "")) for e in row.get("ufo_syntax_errors") or []]
    tb = (row.get("ufo_import_error") or "") + "\n" + (row.get("mg5_debug_tail") or "")
    frames = _UFO_FRAME.findall(row.get("ufo_import_error") or "")
    if frames:
        f, ln = frames[-1]
        locs.append((f, int(ln), (tb.strip().splitlines() or [""])[-1][:200]))
    name_errs = _NAME_ERR.findall(tb)
    sym = _fr_symbols(fr_text)
    out, seen = [], set()
    for f, ln, msg in locs:
        if (f, ln) in seen:
            continue
        seen.add((f, ln))
        uf = ufo_dir / f
        lines = uf.read_text(errors="replace").splitlines() if uf.is_file() else []
        obj, a, b = _ufo_object(lines, ln) if lines else (None, 0, 0)
        text = "\n".join(lines[a:b])[:1800] if lines else ""
        bad_line = lines[ln - 1] if 0 < ln <= len(lines) else ""
        words = lambda t: [w for w in re.findall(r"\b[A-Za-z]\w*\b", t)
                           if w not in _PY_WORDS and not w.startswith(("GC_", "L_", "V_"))]
        # The broken line's own identifiers first: in a Particle object the
        # break is one attribute (a quantum number named B_L), not the particle.
        idents = list(dict.fromkeys(name_errs + words(bad_line) + ([obj] if obj else []) + words(text)))
        particles = _vertex_particles(ufo_dir, obj) if obj and obj.startswith("GC_") else []
        cands: List[str] = []
        for t in idents + particles:
            cands += _fr_candidates(t, sym)
        # Anything else that is a word of the .fr: quantum-number keys, index names.
        for t in name_errs + words(bad_line):
            if len(t) < 2 or t in _FR_HEADS:
                continue
            if t not in cands and re.search(rf"(?<![\w$]){re.escape(t)}(?![\w$])", fr_text):
                cands.append(t)
        cands = list(dict.fromkeys(cands))
        m_err = _NAME_ERR.search(tb)
        if m_err and f == "particles.py":
            msg = m_err.group(0)
        out.append({"ufo_file": f, "ufo_line": ln, "message": msg, "ufo_object": obj,
                    "ufo_text": text, "vertex_particles": particles,
                    "fr_symbols": cands, "fr_lines": _fr_lines(fr_text, cands)})
    return out


# ------------------------------------------------------------------ report
def render_sections(row: dict, log: str, fr_text: str) -> str:
    d = parse_diag_lines(log)
    parts: List[str] = []
    checks = row.get("checks") or {}
    if checks.get("hermiticity") == "fail":
        blocks = {b: c for b, c in d["blocks"].items() if b != row.get("lag_symbol")}
        herm = localize_herm(d["herm"], blocks)
        parts += ["## Hermiticity: the non-zero vertices of L - HC[L]",
                  "Each row is a vertex that does not cancel against its conjugate. The usual "
                  "cause is a term without its `+ HC[...]` partner, or a complex coefficient on "
                  "a self-conjugate combination. `block` is the named Lagrangian term in model.fr "
                  "whose expanded terms carry these fields (or their conjugates).", ""]
        if not herm:
            parts.append("(the driver returned no vertex list)")
        for v in herm[:25]:
            parts.append(f"- vertex {v['i']}: fields {' '.join(v['fields'])}; "
                         f"block: {', '.join(v['blocks']) or 'not located'}")
            if v.get("unreduced"):
                parts.append(f"  UNREDUCED: FeynRules could not strip {', '.join(v['unreduced'])} from this "
                             "vertex; its coefficient still holds a spinor chain (Ga[0] from the conjugate). "
                             "The usual cause is an explicit spin or flavour index on the spinors of that "
                             "chain (see lint rule explicit_spin_in_chain); write the chain with implicit "
                             "indices (`Xbar.Ga[mu].ProjP.Y`).")
            parts.append(f"  coefficient: `{v['expr'][:500]}`")
        if len(herm) > 25:
            parts.append(f"- ... {len(herm) - 25} more vertices")
        parts.append("")
    if checks.get("mass_diagonal") == "fail" and (d["massterms"] or d["tadpoles"]):
        parts += ["## Mass matrix: the off-diagonal entries the check found", "",
                  "| fields | coefficient in the Lagrangian | numerical value |", "|---|---|---|"]
        for m in d["massterms"][:30]:
            parts.append(f"| {' '.join(m['fields'])} | `{m['coefficient'][:300]}` | {m['numeric']} |")
        if d["tadpoles"]:
            parts += ["", "Tadpoles (terms linear in one field: the vev is not at a minimum of "
                      "the potential until these vanish):", "",
                      "| field | coefficient | numerical value |", "|---|---|---|"]
            for t in d["tadpoles"][:10]:
                parts.append(f"| {t['field']} | `{t['coefficient'][:300]}` | {t['numeric']} |")
        parts.append("")
    if row.get("compile_ok") and not row.get("madgraph_import_ok"):
        bt = mg5_backtrace(row, fr_text)
        if bt:
            parts += ["## MadGraph import: where the UFO breaks, and the model.fr lines behind it", ""]
            for e in bt:
                parts.append(f"### `UFO/{e['ufo_file']}` line {e['ufo_line']}"
                             + (f", object `{e['ufo_object']}`" if e["ufo_object"] else "")
                             + (f": {e['message']}" if e["message"] else ""))
                parts += ["```", e["ufo_text"][:1200] or "(line not found)", "```"]
                if e["vertex_particles"]:
                    parts.append(f"Vertex particles using this coupling: {', '.join(e['vertex_particles'])}")
                if e["fr_lines"]:
                    parts.append("model.fr lines:")
                    for x in e["fr_lines"]:
                        parts.append(f"- line {x['line']} ({x['kind']}): `{x['text'].strip()[:240]}`")
                        if x.get("block"):
                            parts += ["  ```", *["  " + b for b in x["block"].splitlines()], "  ```"]
                else:
                    parts.append("model.fr lines: none matched the symbols "
                                 + (", ".join(e["fr_symbols"]) or "(no model symbol in this object)"))
                parts.append("")
    return "\n".join(parts).rstrip() + ("\n" if parts else "")


def stage_reached(row: dict, all_checks_pass) -> str:
    """The furthest stage of the chain: compile, checks, mg5, or pass."""
    if row.get("full_pass"):
        return "pass"
    if not row.get("compile_ok"):
        return "compile"
    if not all_checks_pass(row.get("checks")):
        return "checks"
    return "mg5"
