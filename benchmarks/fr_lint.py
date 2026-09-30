#!/usr/bin/env python3
"""Deterministic lints for an agent-written FeynRules add-on (.fr) file.

Every rule encodes one construct that broke a compile, a FeynRules check or a
MadGraph import in the benchmark (prompt_addendum_v3.txt rules 9-15 and the
repair-loop taxonomy). A lint runs in milliseconds on the text; the compile it
predicts takes up to 900 s.

Each finding carries the STAGE it predicts:
  compile  - FeynRules will not load or will not finish the model
  checks   - the model loads but a consistency check fails
  mg5      - the UFO is written but MadGraph rejects it
  harness  - the validation harness cannot pick the total Lagrangian
  warn     - FeynRules warns; the run may still pass

Library: ``lint_text(text) -> list[Finding]``. CLI: ``fr_lint.py file.fr``.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set

HEPTAPOD = Path.home() / "Documents/Github/heptapod"
SM_FR = HEPTAPOD / "tools/feynrules/test_files/models/SM.fr"

# Mathematica built-ins and FeynRules symbols a class, parameter or index must
# not be named after (rule 10).
FR_SYMBOLS = {"HC", "CC", "FS", "DC", "del", "Eps", "Ga", "ProjP", "ProjM", "T",
              "Sig", "PauliSigma", "IndexDelta", "ME", "Index", "Indices", "Mass",
              "Width", "Value", "Unphysical", "Abelian"}
PROTECTED = {"N", "C", "D", "E", "I", "K", "O", "Pi", "Gamma", "Beta", "Zeta",
             "Sqrt", "Exp", "Log", "Sin", "Cos", "Tan", "Re", "Im", "Conjugate",
             "Sum", "Block", "Module", "Table", "If", "Which"}

# Names SM.fr declares: classes, class members, parameters, gauge groups, indices.
_SM_TEXT = SM_FR.read_text() if SM_FR.is_file() else ""
SM_CLASSES: Set[str] = set(re.findall(r"ClassName\s*->\s*(\w+)", _SM_TEXT))
SM_MEMBERS: Set[str] = set()
for _m in re.findall(r"ClassMembers\s*->\s*\{([^}]*)\}", _SM_TEXT):
    SM_MEMBERS |= {x.strip() for x in _m.split(",") if x.strip()}
_i = _SM_TEXT.find("M$Parameters")
SM_PARAMS: Set[str] = set(re.findall(r"^\s*(\w+)\s*==\s*\{", _SM_TEXT[_i:], re.M)) if _i >= 0 else set()
SM_GAUGE = {"U1Y", "SU2L", "SU3C"}
SM_INDICES = {"Generation", "Colour", "Gluon", "SU2D", "SU2W", "Lorentz", "Spin",
              "Spin1", "Spin2", "Sextet"}
SM_FIELDS_ALL = SM_CLASSES | SM_MEMBERS | {c + "bar" for c in SM_CLASSES | SM_MEMBERS}
SM_MASSES = {"MZ", "MW", "MH", "Me", "MMU", "MTA", "MU", "MC", "MT", "MD", "MS", "MB",
             "WZ", "WW", "WH", "WT"}

FR_BUILTINS = {"HC", "CC", "FS", "DC", "del", "Eps", "Ga", "ProjP", "ProjM", "T",
               "PauliSigma", "IndexDelta", "ME", "Sqrt", "Exp", "Log", "Sin", "Cos",
               "Tan", "I", "Pi", "Sum", "Block", "Module", "ExpandIndices",
               "FlavorExpand", "True", "False", "bar", "anti", "left", "right",
               "Conjugate", "Re", "Im", "Abs", "Sig", "Ta", "T6", "K6", "K6bar",
               "K3", "K3bar", "f", "dSUN", "Dot", "Times", "Plus", "Power",
               "Automatic", "Internal", "External", "Unfold", "NoUnfold", "Range",
               "Index", "Lorentz", "Spin", "Colour", "Gluon", "Generation",
               "SU2D", "SU2W", "Sextet", "IndexStyle", "MakeIdenticalFermions",
               "Expand", "Simplify", "ProjPlus", "ProjMinus", "FR$", "vev"}


@dataclass
class Finding:
    rule: str
    stage: str  # compile | checks | mg5 | harness | warn
    message: str
    line: Optional[int] = None


# ------------------------------------------------------------------ parsing

def strip_comments(text: str) -> str:
    out, depth, i = [], 0, 0
    while i < len(text):
        if text.startswith("(*", i):
            depth += 1
            i += 2
            continue
        if text.startswith("*)", i) and depth:
            depth -= 1
            i += 2
            continue
        if depth == 0:
            out.append(text[i])
        elif text[i] == "\n":
            out.append("\n")
        i += 1
    return "".join(out)


def _matching(text: str, open_idx: int) -> int:
    depth = 0
    pairs = {"{": "}", "[": "]", "(": ")"}
    closes = set(pairs.values())
    for j in range(open_idx, len(text)):
        ch = text[j]
        if ch in pairs:
            depth += 1
        elif ch in closes:
            depth -= 1
            if depth == 0:
                return j
    return len(text) - 1


def _block(text: str, name: str) -> str:
    m = re.search(rf"M\${name}\s*=\s*\{{", text)
    if not m:
        return ""
    end = _matching(text, m.end() - 1)
    return text[m.end():end]


def _entries(block: str) -> List[Dict]:
    """Top-level `Head == { ... }` entries of a M$ block."""
    out = []
    for m in re.finditer(r"(\w+(?:\[\s*\d+\s*\])?)\s*==\s*\{", block):
        end = _matching(block, m.end() - 1)
        body = block[m.end():end]
        out.append({"head": m.group(1), "body": body, "pos": m.start()})
    return out


def _prop(body: str, key: str) -> Optional[str]:
    m = re.search(rf"\b{key}\s*->\s*", body)
    if not m:
        return None
    rest = body[m.end():]
    if rest.startswith("{"):
        return rest[: _matching(rest, 0) + 1]
    mm = re.match(r"[^,}\n]+", rest)
    return mm.group(0).strip() if mm else None


def _is_kin_name(name: str) -> bool:
    return bool(re.search(r"kin|Kin|KIN|free|Free|Gauge|gauge", name))


def term_defs(text: str) -> List[Dict]:
    starts = [(m.group(1), m.start()) for m in re.finditer(r"^(L\w+)\s*:?=", text, re.M)]
    stops = [m.start() for m in re.finditer(r"^(?:M\$\w+\s*=|L\w+\s*:?=|\w+\s*=\s*\{)", text, re.M)]
    out = []
    for name, s in starts:
        e = min([x for x in stops if x > s] + [len(text)])
        out.append({"name": name, "body": text[s:e], "line": text[:s].count("\n") + 1})
    return out


def _line_of(text: str, needle: str) -> Optional[int]:
    i = text.find(needle)
    return text[:i].count("\n") + 1 if i >= 0 else None


# -------------------------------------------------------------------- lints

def lint_text(raw: str) -> List[Finding]:
    text = strip_comments(raw)
    F: List[Finding] = []
    classes = _entries(_block(text, "ClassesDescription"))
    params = _entries(_block(text, "Parameters"))
    terms = term_defs(text)
    term_names = {t["name"] for t in terms}
    term_bodies = "\n".join(t["body"] for t in terms)

    class_names, class_idx = {}, {}
    for c in classes:
        cn = _prop(c["body"], "ClassName")
        if cn:
            class_names[cn] = c
            mi = re.match(r"(\w+)\[\s*(\d+)\s*\]", c["head"])
            if mi:
                class_idx[cn] = (mi.group(1), int(mi.group(2)))
    param_names = {p["head"]: p for p in params}
    index_decls = dict(re.findall(r"IndexRange\[\s*Index\[(\w+)\]\s*\]\s*=\s*([^;\n]+)", text))

    # --- rule 10: names -------------------------------------------------
    for name in list(class_names) + list(param_names) + list(index_decls):
        if name in FR_SYMBOLS:
            F.append(Finding("feynrules_symbol_name", "compile",
                             f"`{name}` is a FeynRules symbol", _line_of(text, name)))
        elif name in PROTECTED:
            F.append(Finding("protected_name", "warn",
                             f"`{name}` is a Mathematica built-in (loads with a warning; renaming is safer)",
                             _line_of(text, name)))
    for name in class_names:
        if name in SM_CLASSES or name in SM_MEMBERS:
            F.append(Finding("sm_class_redeclared", "warn",
                             f"class `{name}` is already declared by SM.fr (doubly-defined class)",
                             _line_of(text, f"ClassName -> {name}")))
    for name in param_names:
        if name in SM_PARAMS or name in SM_MASSES:
            F.append(Finding("sm_parameter_redeclared", "warn",
                             f"parameter `{name}` is already declared by SM.fr", _line_of(text, name)))
    for cn, c in class_names.items():
        for key in ("ParticleName", "AntiParticleName"):
            v = _prop(c["body"], key)
            names = re.findall(r'"([^"]*)"', v) if v else []
            if v and any(re.search(r"[\'`\s!@#%^&*()=\[\]{}|\\;:<>?/,]", nm) for nm in names):
                F.append(Finding("bad_particle_name", "mg5",
                                 f"class `{cn}`: {key} {v} is not a valid UFO identifier", _line_of(text, v)))
        if cn in class_idx and class_idx[cn][1] < 100:
            F.append(Finding("low_class_index", "warn",
                             f"class `{cn}` uses index {class_idx[cn][0]}[{class_idx[cn][1]}]; SM.fr uses the low indices",
                             _line_of(text, c["head"])))
        for m in re.finditer(r"ClassMembers\s*->\s*\{([^}]*)\}", c["body"]):
            for mem in [x.strip() for x in m.group(1).split(",") if x.strip()]:
                if mem in SM_MEMBERS or mem in SM_CLASSES:
                    F.append(Finding("sm_member_redeclared", "compile",
                                     f"class member `{mem}` of `{cn}` collides with an SM.fr name",
                                     _line_of(text, mem)))
    if "$" in re.sub(r"M\$\w+", "", text):
        for m in re.finditer(r"\b\w*\$\w*", text):
            if not re.match(r"^(M|MR|FR)\$", m.group(0)):
                F.append(Finding("dollar_in_name", "mg5", f"`{m.group(0)}` contains `$` (invalid Python)",
                                 text[:m.start()].count("\n") + 1))
                break

    # --- rule 11: interaction orders --------------------------------------
    hierarchy = _block(text, "InteractionOrderHierarchy")
    orders_declared = set(re.findall(r"\{\s*(\w+)\s*,\s*-?\d+\s*\}", hierarchy))
    for pn, p in param_names.items():
        body = p["body"]
        ptype = (_prop(body, "ParameterType") or "External").strip()
        io = _prop(body, "InteractionOrder")
        used = re.search(rf"\b{re.escape(pn)}\b", term_bodies) is not None
        is_mass = any(re.search(rf"Mass\s*->\s*\{{\s*{re.escape(pn)}\b", c["body"]) or
                      re.search(rf"Width\s*->\s*\{{\s*{re.escape(pn)}\b", c["body"])
                      for c in classes) or re.match(r"^(M|W)[A-Z]", pn) and not io
        if io:
            oname = re.findall(r"\{\s*(\w+)\s*,", io)
            for o in oname:
                if o not in orders_declared and o not in ("QCD", "QED"):
                    F.append(Finding("order_not_in_hierarchy", "warn",
                                     f"parameter `{pn}` uses InteractionOrder `{o}` not listed in M$InteractionOrderHierarchy",
                                     _line_of(text, pn)))
    ordered = {pn for pn, p in param_names.items() if _prop(p["body"], "InteractionOrder")}
    internal = {pn for pn, p in param_names.items()
                if (_prop(p["body"], "ParameterType") or "External").strip() == "Internal"}
    # an Internal parameter inherits the orders of the parameters in its Value
    for pn in list(internal):
        val = _prop(param_names[pn]["body"], "Value") or ""
        if any(re.search(rf"\b{re.escape(o)}\b", val) for o in ordered):
            ordered.add(pn)
    for t in terms:
        if _is_kin_name(t["name"]):
            continue
        used_params = {pn for pn in param_names if re.search(rf"\b{re.escape(pn)}\b", t["body"])}
        sm_couplings = {"ee", "gw", "gs", "g1", "yl", "yu", "yd", "lam", "CKM"}
        if used_params and not (used_params & ordered) and not \
                any(re.search(rf"\b{c}\b", t["body"]) for c in sm_couplings) and \
                not any(re.search(rf"\b(DC|FS)\[", t["body"]) for _ in [0]):
            F.append(Finding("missing_interaction_order", "mg5",
                             f"`{t['name']}`: none of its parameters ({', '.join(sorted(used_params))}) carries an InteractionOrder",
                             t["line"]))

    # --- rule 12: pattern rules on tensor parameters -----------------------
    for pn, p in param_names.items():
        if re.search(r"\w+\[[^\]]*_[^\]]*\]\s*:?->", p["body"]) or "_?NumericQ" in p["body"]:
            F.append(Finding("pattern_rule_definition", "mg5",
                             f"parameter `{pn}` uses a pattern rule in Definitions/Value; FeynRules exports it verbatim as a UFO name",
                             _line_of(text, pn)))
    for cn, c in class_names.items():
        d = _prop(c["body"], "Definitions") or ""
        if re.search(r"\w+\[[^\]]*_[^\]]*\]\s*:>", d) and not re.search(r"\w+\[[^\]]*_\s*[,\]]", d):
            pass  # `X[mu_] :> ...` is the normal FeynRules idiom; leave it

    # --- rule 13: explicit indices ------------------------------------------
    for t in terms:
        b = t["body"]
        for m in re.finditer(r"DC\[\s*(\w+)\[([^\]]*)\]\s*,", b):
            fld = m.group(1)
            c = class_names.get(fld)
            idx = (_prop(c["body"], "Indices") or "") if c else ""
            if c and re.search(r"Colour|Sextet|Gluon|Octet|Col", idx):
                F.append(Finding("explicit_index_in_dc", "compile",
                                 f"`{t['name']}`: covariant derivative on `{fld}` with an explicit colour-type index", t["line"]))
            else:
                F.append(Finding("explicit_index_in_dc", "warn",
                                 f"`{t['name']}`: covariant derivative on an explicitly indexed field `{fld}`", t["line"]))
            break
        if re.search(r"Index\[\s*Generation\s*,\s*\w+\s*\]\s*,\s*Index\[\s*Generation", b) or \
                re.search(r"\w+\[\s*Generation\s*,\s*\w+\s*\]", b):
            F.append(Finding("nested_generation_index", "compile",
                             f"`{t['name']}`: nested generation index", t["line"]))
        m = re.search(r"\b(\w+)\[\s*(ff\d?|gen\d?|ii\d?)\s*,\s*(ff\d?|gen\d?|jj\d?)\s*\]\s*\w+bar\[", b)
        if m and m.group(1) in param_names:
            F.append(Finding("explicit_flavour_sum", "mg5",
                             f"`{t['name']}`: flavour matrix `{m.group(1)}` with explicit generation indices instead of matrix form",
                             t["line"]))

    # --- rule 14: one declared total ---------------------------------------
    roots = []
    for t in terms:
        if not any(re.search(rf"\b{t['name']}\b", u["body"]) for u in terms if u is not t):
            roots.append(t["name"])
    if terms and not roots:
        F.append(Finding("no_total_lagrangian", "harness", "no Lagrangian symbol is a root (circular or empty)", None))
    elif len(roots) > 1:
        F.append(Finding("ambiguous_total", "harness",
                         f"{len(roots)} root Lagrangian symbols: {', '.join(roots)}", None))
    elif roots and roots[0] not in ("LTotal", "LTot", "LFull", "LBSM", "LNP", "Lag", "LagTot"):
        F.append(Finding("total_not_named_ltotal", "warn", f"the single root is `{roots[0]}`, not LTotal", None))
    field_tokens = set(class_names) | {c + "bar" for c in class_names} | SM_FIELDS_ALL
    for c in classes:
        for m in re.finditer(r"ClassMembers\s*->\s*\{([^}]*)\}", c["body"]):
            field_tokens |= {x.strip() for x in m.group(1).split(",") if x.strip()}
    for t in terms:
        rhs = t["body"].split("=", 1)[-1]
        if re.search(r"\bL\w+\b", rhs) and any(re.search(rf"\b{u['name']}\b", rhs) for u in terms if u is not t):
            continue  # a sum of other terms
        if not any(re.search(rf"\b{re.escape(f)}\b", rhs) for f in field_tokens):
            F.append(Finding("fieldless_term", "mg5", f"`{t['name']}` contains no field", t["line"]))

    # --- rule 15: declarations -----------------------------------------------
    for cn, c in class_names.items():
        sc = (_prop(c["body"], "SelfConjugate") or "").strip()
        qn = _prop(c["body"], "QuantumNumbers")
        if sc == "True" and qn and re.search(r"->\s*-?[1-9]", qn):
            F.append(Finding("selfconjugate_with_qn", "warn",
                             f"class `{cn}` is SelfConjugate and carries QuantumNumbers {qn}",
                             _line_of(text, f"ClassName -> {cn}")))
        if sc == "True" and _prop(c["body"], "AntiParticleName"):
            pass
    # Majorana mass normalisation
    for cn, c in class_names.items():
        if (_prop(c["body"], "SelfConjugate") or "").strip() == "True" and c["head"].startswith("F"):
            mm = re.search(r"Mass\s*->\s*\{\s*(\w+)", c["body"])
            if not mm:
                continue
            M = mm.group(1)
            pat = re.compile(rf"(-?\s*(?:1/2|0\.5|\(1/2\))?\s*\*?\s*{M}\b[^;]{{0,40}}{cn}bar\s*\.\s*{cn}\b)")
            for t in terms:
                for hit in pat.finditer(t["body"]):
                    if not re.search(r"1/2|0\.5", hit.group(1)):
                        F.append(Finding("majorana_mass_no_half", "checks",
                                         f"`{t['name']}`: Majorana mass term for `{cn}` without the 1/2",
                                         t["line"]))
    # undeclared symbols in terms (conservative: capitalised identifiers used as fields)
    declared = set(class_names) | {c + "bar" for c in class_names} | set(param_names) | \
        SM_FIELDS_ALL | SM_PARAMS | SM_MASSES | FR_BUILTINS | set(term_names) | set(index_decls) | \
        {"If", "Which", "Table", "KroneckerDelta", "Transpose", "Inverse", "ArcTan", "Sec", "Csc",
         "Cot", "Abs", "MatrixExp", "DiagonalMatrix", "IdentityMatrix", "Sum", "Product"}
    for c in classes:
        for key in ("Mass", "Width"):
            v = _prop(c["body"], key) or ""
            declared |= set(re.findall(r"\b([A-Za-z]\w*)\b", v)) - {"Internal", "External", "Automatic"}
    for c in classes:
        for m in re.finditer(r"ClassMembers\s*->\s*\{([^}]*)\}", c["body"]):
            for mem in [x.strip() for x in m.group(1).split(",") if x.strip()]:
                declared |= {mem, mem + "bar"}
        for m in re.finditer(r"Unphysical\s*->\s*True", c["body"]):
            pass
    for t in terms:
        b = re.sub(r'"[^"]*"', "", t["body"])
        locals_ = set()
        for m in re.finditer(r"(?:Block|Module)\[\s*\{([^}]*)\}", b):
            locals_ |= {x.strip().split("=")[0].strip() for x in m.group(1).split(",")}
        for m in re.finditer(r"\b([A-Za-z]\w*)\b", b):
            s = m.group(1)
            if s in declared or s in locals_ or s == t["name"] or len(s) < 2:
                continue
            if re.match(r"^(mu|nu|rho|sig|la|lam|al|be|sp|ss|ii|jj|kk|ll|ff|gg|cc|aa|bb|tt|rr|xx|yy|zz)\d*$", s):
                continue
            if s in ("ExpandIndices", "FlavorExpand", "Index", "Sqrt", "HC"):
                continue
            if s[0].isupper() and re.search(rf"\b{re.escape(s)}\s*[\[.]", b):
                F.append(Finding("undeclared_symbol", "warn",
                                 f"`{t['name']}` uses `{s}` which is neither declared here nor by SM.fr",
                                 t["line"]))
                break

    # --- rule 9: non-fundamental colour representations -----------------------
    for iname, rng in index_decls.items():
        if re.search(r"Range\[\s*6\s*\]", rng) and "AddGaugeRepresentation" not in text:
            F.append(Finding("sextet_without_representation", "warn",
                             f"index `{iname}` has range 6 but there is no AddGaugeRepresentation", _line_of(text, iname)))

    # --- mass mixing written into Definitions (the dominant check failure) ----
    phys_new = {cn for cn, c in class_names.items() if (_prop(c["body"], "Unphysical") or "").strip() != "True"}
    for cn, c in class_names.items():
        d = _prop(c["body"], "Definitions") or ""
        if not d:
            continue
        fields_in = {s for s in re.findall(r"\b([A-Za-z]\w*)\b", d) if s in phys_new or s in SM_CLASSES}
        fields_in -= {cn}
        if len(fields_in) >= 2 and re.search(r"\b(sa|ca|sin|cos|Sin|Cos|s\w*|c\w*)\w*\b", d):
            F.append(Finding("mixing_in_definitions", "checks",
                             f"class `{cn}` is defined as a mixture of {sorted(fields_in)}; the mass basis of the partner fields declared in SM.fr is unchanged",
                             _line_of(text, f"ClassName -> {cn}")))
    F += _mg5_leak_rules(text, classes, params)
    return F


# Constructs that compile, pass the checks and then leak unevaluated
# Mathematica into the UFO, so MadGraph cannot import it (the three pi Qwen
# runs that failed only at `import model`: B-L-SM, Wprime, HeavyN).
_SPIN_CHAIN = re.compile(
    r"\b(\w+bar)\[\s*([A-Za-z]\w*)\s*(?:,[^\[\]]*)?\]"            # Xbar[sp, ...]
    r"(?:\s*\.\s*(?:Ga|ProjP|ProjM)(?:\[[^\[\],]*\])?)+"              # .Ga[mu].ProjM (no spin args)
    r"\s*\.\s*(\w+)\[\s*\2\s*[,\]]")                                   # . Y[sp, ...]


def _mg5_leak_rules(text: str, classes: List[Dict], params: List[Dict]) -> List[Finding]:
    F: List[Finding] = []
    # A name with an underscore is a Mathematica pattern (B_L is "a B with
    # head L"), not a symbol. As a quantum number it becomes an attribute of
    # every UFO particle, `B_L = (B_L)[A]`, and particles.py raises NameError.
    for m in re.finditer(r"QuantumNumbers\s*->\s*\{([^}]*)\}", text):
        for key in re.findall(r"([A-Za-z]\w*)\s*->", m.group(1)):
            if "_" in key:
                F.append(Finding("pattern_symbol_name", "mg5",
                                 f"quantum number `{key}` contains `_`, which makes it a Mathematica "
                                 f"pattern; FeynRules writes it into particles.py as `{key} = ({key})[...]` "
                                 f"and the UFO does not import. Rename it without the underscore (e.g. "
                                 f"`{key.replace('_', '')}`)", text[:m.start()].count("\n") + 1))
    names = [(_prop(c["body"], "ClassName") or "", "class") for c in classes]
    names += [(p["head"], "parameter") for p in params]
    names += [(n, "index") for n in re.findall(r"IndexRange\[\s*Index\[(\w+)\]", text)]
    for mem in re.findall(r"ClassMembers\s*->\s*\{([^}]*)\}", text):
        names += [(x.strip(), "class member") for x in mem.split(",") if x.strip()]
    for nm, kind in names:
        if "_" in nm:
            # Warning only: parameter names like aSRh_u passed the whole chain
            # (Monotops, pi Qwen harness); only the quantum-number key breaks.
            F.append(Finding("pattern_symbol_name", "warn",
                             f"{kind} name `{nm}` contains `_`, which makes it a Mathematica pattern "
                             f"rather than a symbol; rename it", _line_of(text, nm)))
    # A tensor parameter gets one LHA code per component from its indices. An
    # explicit OrderBlock on it is written unevaluated into parameters.py
    # (`lhacode = PYList[{1} /. 7]`), which is not Python.
    for p in params:
        body = p["body"]
        idx = _prop(body, "Indices")
        if idx and re.search(r"Index\[", idx) and re.search(r"\bOrderBlock\s*->", body):
            F.append(Finding("tensor_orderblock", "mg5",
                             f"parameter `{p['head']}` has Indices and an OrderBlock; FeynRules numbers "
                             f"the components of a tensor itself, and the explicit OrderBlock is written "
                             f"unevaluated into parameters.py. Remove the OrderBlock line",
                             _line_of(text, f"{p['head']} ==")))
    # `Xbar[sp].Ga[mu].Y[sp, ff]`: the same explicit spin index on both ends of
    # a chain with a Dirac matrix between them. The index should be implicit
    # (`Xbar.Ga[mu].Y`) or carried through the matrix (`Ga[mu, sp1, sp2]`).
    # FeynRules leaves the chain unevaluated and the coupling in couplings.py
    # holds `ReplaceAll(... Dot(...) ...)`.
    for m in _SPIN_CHAIN.finditer(text):
        F.append(Finding("explicit_spin_in_chain", "mg5",
                         f"`{m.group(1)}[{m.group(2)}]` and `{m.group(3)}[{m.group(2)}, ...]` carry the "
                         f"same explicit spin index with a Dirac matrix between them; drop the explicit "
                         f"spin index (`{m.group(1)}.Ga[mu].{m.group(3)}`) or thread it through the matrix",
                         text[:m.start()].count("\n") + 1))
    return F


def lint_file(path: str) -> List[Finding]:
    return lint_text(Path(path).read_text(errors="replace"))


if __name__ == "__main__":
    for p in sys.argv[1:]:
        fs = lint_file(p)
        print(json.dumps({"file": p, "findings": [asdict(f) for f in fs]}, indent=1))
