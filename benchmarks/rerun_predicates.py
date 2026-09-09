"""
# rerun_predicates.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Deterministic resolution predicates for the findings reviewing physicists
reported on the agent-generated models: the four of August 2026 (Z' free-field
terms, sextet 1/Lambda cutoffs, EffLRSM nu^c, GeneralU1 Eps + Higgs charge),
the EffLRSM Z_R normalisation of September 2026 (root in the denominator),
and the sextet gauge-representation gap the readers found. Each takes the .fr
text and returns (resolved, detail).

They are written against the CONSTRUCT, not the symbol names the original
files happened to use: a regenerated model is free to call its cutoff
``LambPsiu`` and its Yukawa ``LNYukD``. The first version of this module was
name-bound and reported three resolved files as unresolved; that is the
failure mode to avoid here. Predicates are evidence — a physicist reading
the file is the verdict.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# The repo's own balanced-brace .fr parser. Using it rather than regexes over
# the raw text makes these checks independent of LAYOUT as well as of names.
# The renderer emits `  V[100] == {\n    ClassName -> V1,`; an agent writing a
# .fr by hand emits `V[100] == {\n  ClassName       -> V1,`. A regex tuned to
# the first form silently fails the second, which would mark the no-tools
# ablation arm wrong for a difference in whitespace.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from tools.frgen.fr_parser import parse_fr  # noqa: E402

_LIGHT_NU = r"(?:ve|vm|vt|vl)"


def _strip_comments(fr: str) -> str:
    return re.sub(r"\(\*.*?\*\)", "", fr, flags=re.S)


def _classes(fr_text: str, spin: str | None = None) -> List[Dict]:
    """Particle classes, at any indentation. ``spin`` filters by S/F/V/U/T."""
    try:
        classes = parse_fr(fr_text).get("classes") or []
    except Exception:                                       # noqa: BLE001
        return []
    return [c for c in classes if spin is None or c.get("spin_type") == spin]


def _parameters(fr_text: str) -> List[Dict]:
    try:
        return parse_fr(fr_text).get("parameters") or []
    except Exception:                                       # noqa: BLE001
        return []


def _mass_symbol(mass: str | None) -> str | None:
    """``{MV1, 1500.}`` / ``{MV1}`` / ``MV1`` -> ``MV1``; ``0`` -> None."""
    if not mass:
        return None
    m = re.match(r"\s*\{?\s*([A-Za-z][A-Za-z0-9$]*)", mass)
    return m.group(1) if m else None


def _split_top_level_semicolons(s: str) -> List[str]:
    """Split on ``;`` that are OUTSIDE every bracket.

    Splitting on every ``;`` cuts a statement in half whenever the right-hand
    side is a ``Block[{...}, a = ...; b = ...; expr]``, and the half holding
    the physics then no longer starts with ``L... :=`` and is dropped. A real
    model wrote its neutrino Yukawa in exactly that shape and was reported as
    not having one at all.
    """
    out, depth, start = [], 0, 0
    for i, ch in enumerate(s):
        if ch in "[{(":
            depth += 1
        elif ch in "]})":
            depth -= 1
        elif ch == ";" and depth <= 0:
            out.append(s[start:i])
            start = i + 1
    out.append(s[start:])
    return out


def _statements(fr: str) -> List[str]:
    """Top-level Lagrangian assignments ``Name := ...;`` / ``Name = ...;``."""
    body = re.sub(r"\\\s*\n", " ", _strip_comments(fr))
    return [s.strip() for s in _split_top_level_semicolons(body)
            if re.match(r"^\s*L\w*\s*:?=", s)]


def _external_params(fr: str) -> set:
    return {p["name"] for p in _parameters(fr)
            if str(p.get("parameter_type") or "").strip() == "External"}


# ---------------------------------------------------------------- Zprime
def zprime_free_field_terms(fr_text: str) -> Tuple[bool, str]:
    """Every new vector class has a kinetic + mass term summed into the total."""
    vectors = [(c["class_name"], _mass_symbol(c.get("mass")))
               for c in _classes(fr_text, "V")
               if c.get("class_name") and _mass_symbol(c.get("mass"))]
    if not vectors:
        return False, "no new vector class declared"
    stmts = _statements(fr_text)
    names_in_total = set()
    for s in stmts:
        lhs, rhs = re.split(r":?=", s, maxsplit=1)
        names_in_total |= {n for n in re.findall(r"\bL\w*\b", rhs) if n != lhs.strip()}
    for cls, msym in vectors:
        kin = [s for s in stmts if re.search(rf"FS\[\s*{cls}\s*,|del\[\s*{cls}\[", s)]
        mass = [s for s in stmts if re.search(
            rf"{msym}\^2\s*{cls}\[\w+\]\s*{cls}\[\w+\]|{msym}\^2\s*{cls}bar\[", s)]
        if not kin:
            return False, f"no kinetic term for {cls}"
        if not mass:
            return False, f"no {msym}^2 mass term for {cls}"
        lhs = re.split(r":?=", mass[0], maxsplit=1)[0].strip()
        if lhs not in names_in_total:
            return False, f"{lhs} is not summed into a total Lagrangian"
    return True, f"kinetic + mass term for {', '.join(c for c, _ in vectors)}, summed into the total"


# --------------------------------------------------------------- sextets
def sextets_explicit_cutoffs(fr_text: str) -> Tuple[bool, str]:
    """Every operator with a field strength carries 1/<External cutoff>^n."""
    stmts = [s for s in _statements(fr_text) if "FS[" in s]
    if not stmts:
        return False, "no field-strength operator found"
    ext = _external_params(fr_text)
    used, powers = set(), set()
    for s in stmts:
        cuts = [(c, int(n) if n else 1) for c, n in
                re.findall(r"/\s*\(?\s*(\w+)(?:\^(\d))?", s) if c in ext]
        if not cuts:
            lhs = re.split(r":?=", s, maxsplit=1)[0].strip()
            return False, f"{lhs} has FS[...] but no 1/<External cutoff> factor"
        used |= {c for c, _ in cuts}
        powers |= {n for _, n in cuts}
    return True, f"External cutoffs {sorted(used)} with powers {sorted(powers)} on every field-strength operator"


# --------------------------------------------------------------- EffLRSM
def efflrsm_charge_conjugation(fr_text: str) -> Tuple[bool, str]:
    """No bare light-neutrino field on any W_R line (CC[...] or term dropped)."""
    for s in _statements(fr_text):
        if not re.search(r"\bWR(?:bar)?\[", s):
            continue
        # accept CC[vl], CC[vlbar], bar[CC[vl]], anti[CC[vl]]
        stripped = re.sub(rf"CC\[\s*{_LIGHT_NU}(?:bar)?\s*\]", "CCNU", s)
        stripped = re.sub(rf"CC\[\s*{_LIGHT_NU}(?:bar)?\[[^\]]*\]\s*\]", "CCNU", stripped)
        if re.search(rf"(?<![A-Za-z0-9_]){_LIGHT_NU}(?:bar)?(?![A-Za-z0-9_])", stripped):
            lhs = re.split(r":?=", s, maxsplit=1)[0].strip()
            return False, f"{lhs}: a W_R current uses a bare light-neutrino field; paper Eq.(5) needs nu^c"
    return True, "no bare light-neutrino field on any W_R line (CC[...] used or X term dropped)"


# ------------------------------------------------------------- GeneralU1
def generalu1_eps_and_higgs_charge(fr_text: str) -> Tuple[bool, str]:
    """Dirac neutrino Yukawa is Eps-contracted AND the Higgs U(1)_X charge is +xH/2."""
    import sympy as sp
    fr = _strip_comments(fr_text)
    yuk = [s for s in _statements(fr_text)
           if re.search(r"LLbar\[", s) and re.search(r"\.\s*N\w*\[", s) and "Phibar[" in s]
    if not yuk:
        # Distinguish "absent" from "written after electroweak symmetry
        # breaking". A term like `H vlbar.ynu.ProjP.NR` couples the physical
        # Higgs to the light neutrino directly: there is no doublet, so no Eps
        # contraction can exist, and the charged-lepton partner of the vertex
        # is silently dropped. That is a different defect from a missing term,
        # and saying so is the difference between a useful row and a shrug.
        broken = [s for s in _statements(fr_text)
                  if re.search(r"(?<![A-Za-z0-9])H(?![A-Za-z0-9])", s)
                  and re.search(rf"{_LIGHT_NU}bar", s)
                  and re.search(r"\.\s*N\w*(?![A-Za-z0-9])", s)]
        if broken:
            lhs = re.split(r":?=", broken[0], maxsplit=1)[0].strip()
            return False, (f"{lhs}: the Dirac neutrino Yukawa is written in the broken phase "
                           "with the physical H and a light-neutrino field, not as "
                           "LLbar[..,i,..] Phibar[j] Eps[i,j]; the SU(2) partner vertices are lost")
        return False, "no Dirac neutrino Yukawa term (LLbar ... N ... Phibar) found"
    ok_eps = False
    for s in yuk:
        ll = re.search(r"LLbar\[\s*\w+\s*,\s*(\w+)\s*,", s)
        ph = re.search(r"Phibar\[\s*(\w+)\s*\]", s)
        ep = re.search(r"Eps\[\s*(\w+)\s*,\s*(\w+)\s*\]", s)
        if ll and ph and ep and ll.group(1) != ph.group(1) \
                and {ep.group(1), ep.group(2)} == {ll.group(1), ph.group(1)}:
            ok_eps = True
    if not ok_eps:
        return False, "Dirac neutrino Yukawa lacks LLbar[..,i,..] Phibar[j] Eps[i,j]"
    # The Higgs doublet's charge: a parameter whose Description names the
    # Higgs doublet's U(1)X charge and whose Value is symbolic in xH.
    cands = []
    for p in _parameters(fr_text):
        opts = p.get("options") or {}
        desc = (opts.get("Description") or "").strip().strip('"')
        val = (p.get("value") or "").strip()
        if not desc or not val:
            continue
        # The charge of the SM Higgs doublet under the new U(1). Matched by
        # what the parameter IS, not by one phrasing: its value is symbolic in
        # the new-U(1) normalisation xH, and its description says it is a
        # charge of the doublet. Real files call that doublet "the Higgs
        # doublet", "the SM Higgs", or — following SM.fr's own naming — just
        # "the doublet Phi", and a regex for the first two missed the third.
        if (re.search(r"charge", desc, re.I)
                and re.search(r"higgs|(?<![A-Za-z])phi(?![A-Za-z])", desc, re.I)
                # ...but not a FERMION doublet: the quark and lepton doublets
                # are also "doublets" with a charge symbolic in xH, and a
                # match on the word alone picked xQL = xH/6 + xPhi/3.
                and not re.search(r"quark|lepton|fermion|\bQL\b|\bLL\b|\buR\b|\bdR\b|\blR\b|\bNR\b",
                                  desc, re.I)
                and re.search(r"(?<![A-Za-z0-9])xH(?![A-Za-z0-9])", val)):
            cands.append((p["name"], val))
    if not cands:
        return False, "cannot locate the Higgs doublet's U(1)X charge parameter"
    xH = sp.Symbol("xH")
    for name, val in cands:
        try:
            expr = sp.sympify(val.replace("^", "**"))
        except Exception:                                   # noqa: BLE001
            return False, f"{name} has a non-symbolic value {val!r}"
        if sp.simplify(expr - xH / 2) != 0:
            return False, f"{name} = {val}; Yukawa invariance with SM.fr Y(H)=+1/2 requires +xH/2"
    return True, f"Eps-contracted Dirac Yukawa; Higgs U(1)X charge {cands[0][0]} = {cands[0][1]}"


def _root_is_divisor(expr: str, pos: int) -> bool:
    """True if the ``Sqrt[`` starting at ``pos`` sits in a denominator.

    Walks backwards over whitespace: an immediate ``/`` is a denominator. If
    the root is inside a parenthesised group, the group counts instead
    (``1/(k Sqrt[1-x])`` divides). Anything else — ``*``, a name, a bracket,
    the start of the expression — multiplies.
    """
    i = pos - 1
    while i >= 0 and expr[i].isspace():
        i -= 1
    if i < 0:
        return False
    if expr[i] == "/":
        return True
    # inside a parenthesised group? find the unmatched "(" to the left
    depth = 0
    j = i
    while j >= 0:
        ch = expr[j]
        if ch == ")":
            depth += 1
        elif ch == "(":
            if depth == 0:
                k = j - 1
                while k >= 0 and expr[k].isspace():
                    k -= 1
                return k >= 0 and expr[k] == "/"
            depth -= 1
        elif ch in ";\n" and depth == 0:
            return False
        j -= 1
    return False


def _bracket_arg(expr: str, open_pos: int) -> str:
    depth = 0
    for j in range(open_pos, len(expr)):
        if expr[j] == "[":
            depth += 1
        elif expr[j] == "]":
            depth -= 1
            if depth == 0:
                return expr[open_pos + 1:j]
    return expr[open_pos + 1:]


_WEAK_ANGLE = r"\b(sw|cw|tw\w*|tan\w*|theta\w*|thetaW\w*)\b"


def _close_brace(s: str, open_idx: int) -> int:
    """Index of the ``}`` closing the ``{`` at ``open_idx`` (or end of string)."""
    depth = 0
    for j in range(open_idx, len(s)):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return j
    return len(s)


def _param_spans(fr: str) -> Dict[str, Tuple[int, int]]:
    """``{name: (start, end)}`` character spans of each ``name == { ... }``."""
    spans: Dict[str, Tuple[int, int]] = {}
    for m in re.finditer(r"(?<![A-Za-z0-9$])([A-Za-z][A-Za-z0-9$]*)\s*==\s*\{", fr):
        spans[m.group(1)] = (m.start(), _close_brace(fr, m.end() - 1))
    return spans


def _used_as_divisor(fr: str, name: str) -> Tuple[bool, bool]:
    """How a parameter is consumed elsewhere: (divided_somewhere, multiplied_somewhere).

    Uses inside the parameter's own declaration are skipped, so the
    declaration cannot answer the question about itself.
    """
    divided = multiplied = False
    span = _param_spans(fr).get(name)
    for m in re.finditer(rf"(?<![A-Za-z0-9$]){re.escape(name)}(?![A-Za-z0-9$])", fr):
        if span and span[0] <= m.start() <= span[1]:
            continue
        if _root_is_divisor(fr, m.start()):
            divided = True
        else:
            multiplied = True
    return divided, multiplied


def efflrsm_zr_normalisation(fr_text: str) -> Tuple[bool, str]:
    """The overall Z_R coupling DIVIDES by Sqrt[1 - tan^2(thetaW)/kappa^2].

    Paper Eq. (8) is -kappa g / sqrt(1 - (1/kappa)^2 tan^2 thetaW). The
    reviewed file multiplied by the root instead (a flattened ``\\frac`` in
    the PDF text).

    Two spellings are both correct and both occur in real files, so the check
    follows one level of indirection rather than reading the root's position
    alone:

      inline      ``gZRq == { Value -> -kap gw/Sqrt[1 - tw2/kap^2] }``
      by name     ``nZRq == { Value -> Sqrt[1 - tw2/kap^2] }`` and then
                  ``-(kap gw/nZRq) ...`` in the Lagrangian

    In the second form the root's own position is "multiplied", yet the
    physics is right. Reading position alone marked such a file wrong.
    """
    fr = _strip_comments(fr_text)
    spans = _param_spans(fr)
    found, bad = [], []

    def _classify(match_start: int, label: str) -> None:
        found.append(label)
        if _root_is_divisor(fr, match_start):
            return
        # Not divided where it stands. Is it inside the declaration of a
        # parameter that the rest of the file then divides by?
        owner = next((n for n, (a, b) in spans.items() if a <= match_start <= b), None)
        if owner:
            divided, multiplied = _used_as_divisor(fr, owner)
            if divided and not multiplied:
                return
        bad.append(label)

    for m in re.finditer(r"Sqrt\s*\[\s*1\s*-", fr):
        arg = _bracket_arg(fr, fr.index("[", m.start()))
        if not re.search(_WEAK_ANGLE, arg):
            continue
        _classify(m.start(), arg.strip())
    for m in re.finditer(r"\(\s*1\s*-[^()]*\)\s*\^\s*\(?\s*(-?)1/2\s*\)?", fr):
        if not re.search(_WEAK_ANGLE, m.group(0)):
            continue
        found.append(m.group(0))
        if m.group(1) != "-":
            bad.append(m.group(0))
    if not found:
        return False, "no Z_R normalisation root Sqrt[1 - tan^2(thetaW)/kappa^2] found"
    if bad:
        return False, (f"Z_R normalisation multiplies by Sqrt[{bad[0][:60]}]; "
                       "paper Eq.(8) divides by it (root in the denominator)")
    return True, f"Z_R normalisation divides by Sqrt[{found[0][:60]}] ({len(found)} occurrence(s))"


def sextets_gauge_representation(fr_text: str) -> Tuple[bool, str]:
    """Every new colour-representation index (6, 8, 10 or 15 states) that a
    particle carries has an ``AddGaugeRepresentation[SU3C -> {T, index}]``
    line, so the field couples to gluons. Without it FeynRules builds
    charge-violating gluon vertices and the Hermiticity check stalls."""
    fr = _strip_comments(fr_text)
    sizes = {n: int(s) for n, s in re.findall(
        r"IndexRange\[\s*Index\[(\w+)\]\s*\]\s*=\s*(?:NoUnfold\[|Unfold\[)?\s*Range\[(\d+)\]", fr)}
    colour_like = [n for n, s in sizes.items() if s in (6, 8, 10, 15)
                   and n not in ("Colour", "Gluon", "Generation", "SU2D", "SU2W")]
    used = [n for n in colour_like
            if re.search(rf"Indices\s*->\s*\{{[^}}]*Index\[{n}\]", fr)]
    if not used:
        return False, "no new colour-representation index (Range[6]/[8]) declared on a particle"
    reps = {idx: gen for gen, idx in re.findall(
        r"AddGaugeRepresentation\[\s*SU3C\s*->\s*\{\s*(\w+)\s*,\s*(\w+)\s*\}\s*\]", fr)}
    missing = [n for n in used if n not in reps]
    if missing:
        return False, (f"index {missing[0]} (Range[{sizes[missing[0]]}]) is on a particle but there is no "
                       f"AddGaugeRepresentation[SU3C -> {{T, {missing[0]}}}]; the field cannot couple to gluons")
    return True, ", ".join(f"AddGaugeRepresentation[SU3C -> {{{reps[n]}, {n}}}]" for n in used)


PREDICATES = {
    "Top-Philic-Zprime": [("zprime_free_field_terms", zprime_free_field_terms)],
    "368sextets": [("sextets_explicit_cutoffs", sextets_explicit_cutoffs),
                   ("sextets_gauge_representation", sextets_gauge_representation)],
    "EffLRSM": [("efflrsm_charge_conjugation", efflrsm_charge_conjugation),
                ("efflrsm_zr_normalisation", efflrsm_zr_normalisation)],
    "GeneralU1": [("generalu1_eps_and_higgs_charge", generalu1_eps_and_higgs_charge)],
}
