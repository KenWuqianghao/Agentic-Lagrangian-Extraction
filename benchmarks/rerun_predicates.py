"""
# rerun_predicates.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Deterministic resolution predicates for the four findings a reviewing
physicist reported on the agent-generated models (August 2026). Each takes
the .fr text and returns (resolved, detail).

They are written against the CONSTRUCT, not the symbol names the original
files happened to use: a regenerated model is free to call its cutoff
``LambPsiu`` and its Yukawa ``LNYukD``. The first version of this module was
name-bound and reported three resolved files as unresolved; that is the
failure mode to avoid here. Predicates are evidence — a physicist reading
the file is the verdict.
"""

from __future__ import annotations

import re
from typing import List, Tuple

_LIGHT_NU = r"(?:ve|vm|vt|vl)"


def _strip_comments(fr: str) -> str:
    return re.sub(r"\(\*.*?\*\)", "", fr, flags=re.S)


def _statements(fr: str) -> List[str]:
    """Top-level Lagrangian assignments ``Name := ...;`` / ``Name = ...;``."""
    body = re.sub(r"\\\s*\n", " ", _strip_comments(fr))
    out = []
    for s in body.split(";"):
        s = s.strip()
        if re.match(r"^L\w*\s*:?=", s):
            out.append(s)
    return out


def _external_params(fr: str) -> set:
    return set(re.findall(
        r"^  (\w+) == \{(?:(?!^  \}).)*?ParameterType\s*->\s*External",
        _strip_comments(fr), re.S | re.M))


# ---------------------------------------------------------------- Zprime
def zprime_free_field_terms(fr_text: str) -> Tuple[bool, str]:
    """Every new vector class has a kinetic + mass term summed into the total."""
    fr = _strip_comments(fr_text)
    vectors = re.findall(
        r"^  V\[\d+\] == \{\s*ClassName -> (\w+).*?Mass -> \{(\w+)", fr, re.S | re.M)
    if not vectors:
        return False, "no new vector class declared"
    stmts = _statements(fr_text)
    names_in_total = set()
    for s in stmts:
        lhs, rhs = re.split(r":?=", s, 1)
        names_in_total |= {n for n in re.findall(r"\bL\w*\b", rhs) if n != lhs.strip()}
    for cls, msym in vectors:
        kin = [s for s in stmts if re.search(rf"FS\[\s*{cls}\s*,|del\[\s*{cls}\[", s)]
        mass = [s for s in stmts if re.search(
            rf"{msym}\^2\s*{cls}\[\w+\]\s*{cls}\[\w+\]|{msym}\^2\s*{cls}bar\[", s)]
        if not kin:
            return False, f"no kinetic term for {cls}"
        if not mass:
            return False, f"no {msym}^2 mass term for {cls}"
        lhs = re.split(r":?=", mass[0], 1)[0].strip()
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
            lhs = re.split(r":?=", s, 1)[0].strip()
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
            lhs = re.split(r":?=", s, 1)[0].strip()
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
    for m in re.finditer(r"^  (\w+) == \{(.*?)^  \}", fr, re.S | re.M):
        name, body = m.group(1), m.group(2)
        d = re.search(r'Description -> "([^"]*)"', body)
        v = re.search(r"Value -> ([^,\n]+)", body)
        if d and v and re.search(r"higgs doublet|SM Higgs", d.group(1), re.I) \
                and "charge" in d.group(1).lower() and "xH" in v.group(1):
            cands.append((name, v.group(1).strip()))
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


PREDICATES = {
    "Top-Philic-Zprime": [("zprime_free_field_terms", zprime_free_field_terms)],
    "368sextets": [("sextets_explicit_cutoffs", sextets_explicit_cutoffs)],
    "EffLRSM": [("efflrsm_charge_conjugation", efflrsm_charge_conjugation)],
    "GeneralU1": [("generalu1_eps_and_higgs_charge", generalu1_eps_and_higgs_charge)],
}
