"""Coverage of the agent's own target list by the UFO it built (arm `cover`).

A chain pass says the file is consistent; it does not say that the paper's
fields and interactions are in the model. The runtime agent cannot see what
it left out, and a gate that only asks for a pass rewards a smaller model.
So the agent writes its target first, `spec.json`, from the paper:

    {"fields":       [{"name": "Zp", "spin": 1, "paper": "Eq. (2)"}],
     "interactions": [{"particles": ["Zp", "tbar", "t"], "paper": "Eq. (3)"}]}

Names are the model's own class or member names (`tbar`/`t~` for the
antiparticle; an SM class such as `l`, `vl`, `uq`, `dq` stands for any of its
members). After every compile this module answers, from the UFO:
  - is every listed field a particle of the UFO;
  - does every listed interaction have a vertex with those particles.
A particle and its antiparticle count as the same leg: the check is about
which fields meet, not about the direction of a line.

The first spec that is validated is recorded; an entry that later disappears
from spec.json is reported, so the list cannot be met by shortening it.
"""

from __future__ import annotations

import itertools
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "benchmarks"))
import fr_lint  # noqa: E402

_ANTI = re.compile(r"(bar|~)$")


def _names(prop: str | None) -> list[str]:
    return re.findall(r"[A-Za-z][A-Za-z0-9$]*[+\-~]*", prop.strip("{} ")) if prop else []


def class_table(*fr_texts: str) -> dict:
    """Class or member name -> the ParticleName strings FeynRules writes to
    the UFO for it. A later file overrides an earlier one (the add-on wins)."""
    table: dict = {}
    for raw in fr_texts:
        text = fr_lint.strip_comments(raw)
        for c in fr_lint._entries(fr_lint._block(text, "ClassesDescription")):
            body = c["body"]
            cls = fr_lint._prop(body, "ClassName")
            if not cls or "True" in (fr_lint._prop(body, "Unphysical") or ""):
                continue
            members = _names(fr_lint._prop(body, "ClassMembers")) or [cls]
            pnames = [
                x.strip('" ')
                for x in re.findall(
                    r'"[^"]*"|[A-Za-z][\w+\-~]*',
                    (fr_lint._prop(body, "ParticleName") or "").strip("{} "),
                )
            ]
            ufo = pnames if len(pnames) == len(members) else members
            table[cls] = set(ufo)
            for m, u in zip(members, ufo):
                table[m] = {u}
    return table


def ufo_families(ufo: Path) -> tuple[dict, list[list[str]]]:
    """UFO particle name (and antiparticle name) -> one family id per
    particle/antiparticle pair; and every vertex as a list of family ids."""
    text = (ufo / "particles.py").read_text(errors="replace")
    var_family, name_family = {}, {}
    for m in re.finditer(r"^(\w+) = Particle\((.*?)^\s*\)?\s*$", text, re.M | re.S):
        var, body = m.group(1), m.group(2)
        name = re.search(r"\bname\s*=\s*'([^']*)'", body)
        anti = re.search(r"\bantiname\s*=\s*'([^']*)'", body)
        var_family[var] = var
        for n in (name, anti):
            if n:
                name_family[n.group(1)] = var
    for a, p in re.findall(r"^(\w+) = (\w+)\.anti\(\)", text, re.M):
        var_family[a] = var_family.get(p, p)
    vertices = []
    for m in re.finditer(
        r"particles\s*=\s*\[([^\]]*)\]", (ufo / "vertices.py").read_text(errors="replace")
    ):
        vertices.append([var_family.get(v, v) for v in re.findall(r"P\.(\w+)", m.group(1))])
    return name_family, vertices


def _families(token: str, table: dict, name_family: dict) -> set:
    """The UFO families a spec token can stand for."""
    base = _ANTI.sub("", token.strip())
    out = set()
    for ufo_name in table.get(base, {base}):
        for cand in (
            ufo_name,
            ufo_name + "~",
            ufo_name.rstrip("+-") + "+",
            ufo_name.rstrip("+-") + "-",
        ):
            if cand in name_family:
                out.add(name_family[cand])
    return out


def _covered(legs: list[set], vertices: list[list[str]]) -> bool:
    n = len(legs)
    for v in vertices:
        if len(v) != n:
            continue
        if any(all(v[i] in legs[p[i]] for i in range(n)) for p in itertools.permutations(range(n))):
            return True
    return False


def load_spec(path: Path) -> tuple[dict | None, str]:
    if not path.is_file():
        return None, (
            "spec.json does not exist. Write it from the paper before the model: every new field "
            "and every interaction term (see the protocol)."
        )
    try:
        spec = json.loads(path.read_text())
        fields = [f["name"] for f in spec["fields"]]
        inter = [list(i["particles"]) for i in spec["interactions"]]
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        return (
            None,
            f"spec.json is not in the required form ({type(e).__name__}: {e}). See the protocol.",
        )
    if not fields or not inter:
        return None, "spec.json lists no field or no interaction."
    return {"fields": fields, "interactions": inter}, ""


def check(spec: dict, ufo: Path, model_fr: str, sm_fr: str) -> dict:
    table = class_table(sm_fr, model_fr)
    name_family, vertices = ufo_families(ufo)
    missing_fields = [f for f in spec["fields"] if not _families(f, table, name_family)]
    missing, unknown = [], []
    for legs in spec["interactions"]:
        fams = [_families(t, table, name_family) for t in legs]
        if not all(fams):
            unknown.append(
                {"particles": legs, "not_in_ufo": [t for t, f in zip(legs, fams) if not f]}
            )
        elif not _covered(fams, vertices):
            missing.append(legs)
    return {
        "fields": len(spec["fields"]),
        "interactions": len(spec["interactions"]),
        "missing_fields": missing_fields,
        "missing_interactions": missing,
        "unknown_particles": unknown,
        "complete": not (missing_fields or missing or unknown),
    }


def removed_entries(first: dict, now: dict) -> dict:
    """Entries of the first validated spec that are not in the current one."""

    def key(legs: list[str]) -> tuple:
        return tuple(sorted(_ANTI.sub("", t) for t in legs))

    now_keys = {key(i) for i in now["interactions"]}
    return {
        "fields": [f for f in first["fields"] if f not in now["fields"]],
        "interactions": [i for i in first["interactions"] if key(i) not in now_keys],
    }


def report(result: dict, removed: dict) -> str:
    out = [
        "## Coverage of spec.json by the UFO",
        f"{result['fields']} fields and {result['interactions']} interactions are listed.",
    ]
    if result["complete"] and not (removed["fields"] or removed["interactions"]):
        return "\n".join(
            out
            + [
                "Every listed field is a particle of the UFO and every listed interaction has a "
                "vertex.",
                "",
            ]
        )
    for f in result["missing_fields"]:
        out.append(f"- field `{f}` is listed and is not a particle of the UFO")
    for u in result["unknown_particles"]:
        out.append(
            f"- interaction {u['particles']}: {u['not_in_ufo']} is not a particle of the UFO (use "
            "the model's class or member names)"
        )
    for i in result["missing_interactions"]:
        out.append(f"- interaction {i} is listed and no vertex of the UFO has these particles")
    for f in removed["fields"]:
        out.append(
            f"- field `{f}` was in the spec at the first validation and is gone from spec.json"
        )
    for i in removed["interactions"]:
        out.append(
            f"- interaction {i} was in the spec at the first validation and is gone from spec.json"
        )
    out += [
        "",
        "The model is not done while this list is not empty. A missing vertex means the term did "
        "not reach the UFO: expand that Lagrangian block alone with wolframscript and look at what "
        "it gives. Remove a spec entry only when the paper does not have it, and say so in your "
        "summary.",
        "",
    ]
    return "\n".join(out)
