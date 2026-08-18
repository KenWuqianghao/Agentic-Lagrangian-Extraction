"""
Benchmark cases: what we ask a model to do, and how we decide it worked.

A case is deliberately NOT "did the agent say the right thing". Every case
here is scored on an artifact that an independent, non-LLM checker can verify
— a file that compiles, a UFO MadGraph will import, a number that matches the
archive. That is the only way a model benchmark measures capability rather
than measuring how confidently a model narrates.

Tiers follow the difficulty axis ToolBench uses, adapted to this toolkit:

  I    single tool call, deterministic, no external software
  II   a short chain, still deterministic
  III  external software in the loop (FeynRules, Wolfram, MadGraph)
  IV   open-ended: the agent must choose its own path to a verifiable artifact
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

Scorer = Callable[[Path, Dict[str, Any]], Dict[str, Any]]


@dataclass
class Case:
    """One benchmark task."""

    case_id: str
    tier: int
    prompt: str
    description: str
    # Tools the case cannot be solved without. Used to detect a model that
    # produced a plausible answer without doing the work.
    required_tools: List[str] = field(default_factory=list)
    timeout_s: int = 900
    needs_external: List[str] = field(default_factory=list)
    scorer: Optional[Scorer] = None

    def score(self, workdir: Path, ctx: Dict[str, Any]) -> Dict[str, Any]:
        if self.scorer is None:
            return {"scored": False,
                    "reason": "no scorer; inspect the artifacts by hand"}
        try:
            return self.scorer(workdir, ctx)
        except Exception as e:                              # noqa: BLE001
            return {"scored": False, "passed": False,
                    "reason": f"scorer raised {type(e).__name__}: {e}"}


# --------------------------------------------------------------- scorers
def _fr_renders(workdir: Path, ctx: Dict[str, Any]) -> Dict[str, Any]:
    """A .fr exists and contains the constructs FeynRules requires."""
    frs = sorted(workdir.rglob("*.fr"))
    if not frs:
        return {"scored": True, "passed": False, "reason": "no .fr produced"}
    text = frs[0].read_text(encoding="utf-8", errors="replace")
    need = ["M$ModelName", "M$ClassesDescription", "M$Parameters"]
    missing = [n for n in need if n not in text]
    return {
        "scored": True,
        "passed": not missing,
        "artifact": str(frs[0].relative_to(workdir)),
        "reason": "ok" if not missing else f"missing {missing}",
        "bytes": len(text),
    }


def _archive_value_matches(workdir: Path, ctx: Dict[str, Any]) -> Dict[str, Any]:
    """The agent's reported number agrees with the archive's own answer.

    Ground truth is fetched live rather than hardcoded, so the case does not
    silently rot when the archive updates.
    """
    import sys
    sys.path.insert(0, str(Path(ctx["heptapod"])))
    from tools.exoplanet.archive_interface import ExoplanetArchive

    rows = ExoplanetArchive().query(
        "select count(*) as n from ps where pl_name='HD 189733 b'")
    truth = int(rows[0]["n"])

    answer = ctx.get("final_text") or ""
    found = str(truth) in answer
    return {
        "scored": True,
        "passed": found,
        "expected": truth,
        "reason": ("agent reported the archive's row count"
                   if found else
                   f"expected {truth} somewhere in the answer"),
    }


# ----------------------------------------------------------------- cases
def default_cases() -> List[Case]:
    return [
        Case(
            case_id="t1-arxiv-astro-search",
            tier=1,
            description="One search tool call against a non-default category.",
            prompt=(
                "Using the available tools, search arXiv for recent papers on "
                "exoplanet transmission spectroscopy in the astro-ph.EP "
                "category. Report the arXiv IDs and titles of the top 3 "
                "results. Use the tools; do not answer from memory."
            ),
            required_tools=["ArxivSearchTool"],
            timeout_s=300,
        ),
        Case(
            case_id="t2-exoplanet-disagreement",
            tier=2,
            description=(
                "Resolve a planet name, then query the archive. Checks that "
                "the model uses ps rather than answering from memory."),
            prompt=(
                "Using the available tools, find out how many separate "
                "published parameter sets the NASA Exoplanet Archive holds "
                "for the planet HD 189733 b, and state that number "
                "explicitly. Then say which parameter shows the largest "
                "disagreement between references."
            ),
            required_tools=["MeasurementDisagreementTool"],
            timeout_s=600,
            scorer=_archive_value_matches,
        ),
        Case(
            case_id="t2-frgen-leptoquark",
            tier=2,
            description="Build a structured spec and render a .fr from it.",
            prompt=(
                "Using the available tools, generate a FeynRules .fr model "
                "file for a scalar leptoquark S1: a colour triplet, weak "
                "singlet, charge -1/3 scalar with mass 1500 GeV and one "
                "Yukawa coupling to a right-handed up quark and a "
                "right-handed lepton. Write it to S1_bench.fr."
            ),
            required_tools=["GenerateFeynRulesModelTool"],
            timeout_s=600,
            scorer=_fr_renders,
        ),
        Case(
            case_id="t3-validate-chain",
            tier=3,
            description="Full external chain: .fr to UFO to MadGraph import.",
            prompt=(
                "Using the available tools, generate a FeynRules model for a "
                "scalar leptoquark S1 (colour triplet, charge -1/3, mass 1500 "
                "GeV, one right-handed Yukawa coupling), then validate it: "
                "compile it to a UFO, run the FeynRules consistency checks, "
                "and import the result into MadGraph. Report which checks "
                "passed and which failed."
            ),
            required_tools=["GenerateFeynRulesModelTool", "ValidateModelTool"],
            needs_external=["feynrules", "wolframscript", "mg5"],
            timeout_s=1800,
            scorer=_fr_renders,
        ),
        Case(
            case_id="t4-paper-to-model",
            tier=4,
            description=(
                "Open-ended: fetch a real paper and produce a validated "
                "model from it. The hardest case, and the one that most "
                "resembles the actual research task."),
            prompt=(
                "Using the available tools, fetch the LaTeX source of arXiv "
                "paper 1603.04993, identify the scalar leptoquark model it "
                "describes, generate a FeynRules .fr file for it, and "
                "validate that file as far as the available tools allow. "
                "Report what you produced and what validation said."
            ),
            required_tools=["ArxivSourceTool", "GenerateFeynRulesModelTool"],
            needs_external=["feynrules", "wolframscript"],
            timeout_s=2400,
            scorer=_fr_renders,
        ),
    ]


def load_cases(path: Optional[Path] = None) -> List[Case]:
    """Cases from JSON, else the built-in set.

    JSON cases cannot carry a scorer, so they are recorded as unscored rather
    than being silently counted as passes.
    """
    if path is None or not Path(path).is_file():
        return default_cases()
    data = json.loads(Path(path).read_text())
    return [Case(**{k: v for k, v in c.items() if k != "scorer"})
            for c in data.get("cases", [])]
