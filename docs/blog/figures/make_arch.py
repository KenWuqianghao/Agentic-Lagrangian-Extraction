"""Figure 1 of the blog: the components. Needs rsvg-convert.

python docs/blog/figures/make_arch.py
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "benchmarks/heptapod_ablation/figures"))
from make_figs import MUT, TX, Fig  # noqa: E402

OUT = Path(__file__).resolve().parent

f = Fig(1300, 640, "en")
f.text(40, 42, "The pipeline: from a paper to a validated FeynRules model", 22, TX, "start", True)

# Column 1: inputs
f.box(
    40,
    90,
    270,
    120,
    "neutral",
    "lag-extract (Stage 1)",
    ["INSPIRE · arXiv · NASA ADS search", "ranks papers, fetches LaTeX e-print"],
)
f.box(
    40,
    250,
    270,
    120,
    "neutral",
    "Sandbox inputs",
    ["paper LaTeX source", "FeynRules SM.fr", "no network, no other files"],
)
f.arrow([(175, 210), (175, 250)])
f.text(175, 395, "In the evaluation, the 13 papers", 13, MUT)
f.text(175, 413, "are given; Stage 1 is not scored.", 13, MUT)

# Column 2: harness
f.o.append(
    '<rect x="350" y="80" width="420" height="380" rx="12" fill="none" '
    'stroke="#5aa9e6" stroke-width="2" stroke-dasharray="6 5"/>'
)
f.text(560, 108, "Agent harness: Claude Code, headless", 16, TX, "middle", True)
f.box(
    375, 125, 370, 80, "agent", "Runtime agent", ["reads the paper, writes model.fr, runs a shell"]
)
f.box(
    375,
    220,
    370,
    64,
    "agent",
    "Protocol prompt",
    ["self-audit table first; SM-override recipe"],
    tfs=15,
    lfs=13,
)
f.box(
    375,
    293,
    370,
    74,
    "gate",
    "Stop gate (Stop hook)",
    ["sends the agent back (up to 3 times) while", "the last validation has not passed"],
    tfs=15,
    lfs=13,
)
f.box(
    375,
    376,
    370,
    64,
    "gate",
    "Sandbox guard (PreToolUse hook)",
    ["denies every path outside the run directory"],
    tfs=15,
    lfs=13,
)
f.arrow([(310, 310), (350, 310)])

# Column 3: tools
f.o.append(
    '<rect x="820" y="80" width="440" height="380" rx="12" fill="none" '
    'stroke="#a98bf0" stroke-width="2" stroke-dasharray="6 5"/>'
)
f.text(1040, 108, "heptapod-tools (MCP server)", 16, TX, "middle", True)
f.box(
    845, 125, 390, 64, "tool", "lint_model", ["fixed-rule .fr checks, milliseconds"], tfs=15, lfs=13
)
f.box(
    845,
    203,
    390,
    80,
    "tool",
    "validate_model  (budget 10)",
    ["compile → 4 consistency checks → UFO", "→ MadGraph import, with diagnostics"],
    tfs=15,
    lfs=13,
)
f.box(
    845, 297, 390, 64, "tool", "massbasis", ["sympy mass matrix when scalars mix"], tfs=15, lfs=13
)
f.box(
    845,
    375,
    390,
    64,
    "tool",
    "review_model  (budget 2)",
    ["a fresh agent checks the model vs the paper"],
    tfs=15,
    lfs=13,
)
f.arrow([(770, 220), (820, 220)], color="#8a97a8")
f.arrow([(820, 260), (770, 260)], color="#8a97a8")
f.label(795, 190, "MCP", 12.5, MUT)

# Bottom row: physics back end and outputs
f.box(
    845,
    500,
    390,
    100,
    "neutral",
    "Physics back end",
    [
        "heptapod FeynRules validators (hepval.py)",
        "Wolfram Engine 15 · FeynRules 2.3.49 · MG5 3.7.3",
    ],
    tfs=15,
    lfs=13,
)
f.arrow([(1040, 460), (1040, 500)])

f.box(
    375,
    500,
    370,
    100,
    "good",
    "model.fr",
    ["a FeynRules add-on on top of SM.fr", "delivered only through the stop gate"],
    tfs=16,
    lfs=13,
)
f.arrow([(560, 460), (560, 500)])

f.box(
    40,
    500,
    270,
    100,
    "neutral",
    "Scorer (same for every group)",
    ["6-check gate, then vertex-kind F1", "vs the FeynRules database model"],
    tfs=15,
    lfs=13,
)
f.arrow([(375, 550), (310, 550)])

svg = OUT / "fig1_architecture.svg"
svg.write_text(f.svg())
subprocess.run(
    ["rsvg-convert", "-z", "1.5", "-o", str(OUT / "fig1_architecture.png"), str(svg)], check=True
)
svg.unlink()
