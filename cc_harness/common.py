"""Shared paths, state and path guard for the Claude Code harness.

The MCP server, both hooks and the runner read the same environment:

  CC_SANDBOX          the agent's working directory; the only tree a tool may touch
  CC_RUNDIR           where logs, validation outputs and state go (outside the sandbox)
  CC_VALIDATE_BUDGET  validate_model calls per run (default 10)
  CC_REVIEW_BUDGET    review_model calls per run (default 2)
  CC_MAX_CONTINUATIONS  Stop-gate blocks per run (default 3)
  CC_REVIEW_MODEL     model for the referee (default: CC_AGENT_MODEL)
  CC_AGENT_MODEL      model of the agent under test
  CC_ARM              ablation arm (ARMS below; default "full")
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import time
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALE = HERE.parent
HEPVAL = Path(os.environ.get("CC_HEPVAL", ALE / "pi_harness" / "hepval.py"))
CLAUDE = os.environ.get("CC_CLAUDE_BIN", str(Path.home() / ".local/bin/claude"))
PYTHON = os.environ.get("CC_PYTHON", "python3")
SERVER_NAME = "heptapod-tools"
TOOLS = ("lint_model", "validate_model", "massbasis", "review_model")


@dataclass(frozen=True)
class Arm:
    """One ablation arm: the MCP tools the agent has, and what validate_model
    shows it. The chain always runs in full and its verdicts go to
    summary.json; `feedback` only selects the agent's view:

      none     no validate_model
      compile  whether FeynRules wrote a UFO, and the log when it did not
               (a generic compile loop: no checks, no MadGraph import)
      import   compile, plus whether MadGraph imports the UFO, with its
               output when it does not (a generic build-and-load loop)
      checks   the verdicts and prose heptapod-dev main returns: compile, the
               four checks, MadGraph import
      diag     checks plus the ALE diagnostic sections (non-hermitian vertices
               by block, mass-matrix entries, MadGraph back-trace)
      opt      diag plus the optimisation checks of opt_checks.py: more lint
               rules, new particles without a vertex (not a pass), the
               disagreeing mass rows, UFO parameters defined twice
      real     opt plus statements cut at a line end (not a pass)
      cover    real plus the coverage of the agent's own target list,
               spec.json, by the UFO (an uncovered entry is not a pass)

    `shell`: the agent also has Bash, can read the outputs of its validate
    calls (UFO, FeynRules log) and can run wolframscript and MadGraph itself.
    The run is isolated by isolation.py, not by the PreToolUse guard.
    """
    tools: tuple
    feedback: str
    shell: bool = False


ARMS = {
    "none": Arm((), "none"),
    "compile": Arm(("validate_model",), "compile"),
    "import": Arm(("validate_model",), "import"),
    "heptapod": Arm(("validate_model",), "checks"),
    "diag": Arm(("validate_model",), "diag"),
    "lint": Arm(("lint_model", "validate_model"), "diag"),
    "massbasis": Arm(("lint_model", "validate_model", "massbasis"), "diag"),
    "full": Arm(TOOLS, "diag"),
    "opt": Arm(TOOLS, "opt"),
    "shell": Arm(TOOLS, "real", shell=True),
    "cover": Arm((*TOOLS, "review_spec"), "cover", shell=True),
}


def arm(name: str | None = None) -> Arm:
    return ARMS[name or os.environ.get("CC_ARM", "full")]


def mcp_tool_names(a: Arm) -> tuple:
    return tuple(f"mcp__{SERVER_NAME}__{t}" for t in a.tools)


_BLOCK = re.compile(r"<!--if (!?)(\w+)-->(.*?)<!--end-->", re.S)


def render_protocol(template: str, a: Arm, validate_budget: int, max_continuations: int, rundir: str = "") -> str:
    """The system-prompt protocol for an arm: a block `<!--if X-->...<!--end-->`
    stays when X holds (`!X`: when it does not). X is a tool name, `tools`
    (the arm has any), `generic` (a build report without check verdicts),
    `import` (that report includes the MadGraph import), `checks` (the agent
    sees check verdicts), `checks_plain` (verdicts without the diagnostic
    sections) or `diag`. The SM-override recipe is outside every block: all arms get it."""
    flags = {*a.tools, *(["tools"] if a.tools else []),
             {"import": "import", "checks": "checks_plain", "diag": "diag", "opt": "opt", "real": "opt", "cover": "opt"}.get(a.feedback, "")}
    if a.feedback in ("opt", "real", "cover"):
        flags.add("diag")
    if a.feedback in ("checks", "diag", "opt", "real", "cover"):
        flags.add("checks")
    if a.feedback == "cover":
        flags.add("cover")
    if a.shell:
        flags.add("shell")
    if a.feedback in ("compile", "import"):
        flags.add("generic")
    if a.feedback != "compile" and a.tools:
        flags.add("imports_shown")
    text = _BLOCK.sub(lambda m: m.group(3) if (m.group(2) in flags) != bool(m.group(1)) else "", template)
    names = [f"`{t}`" for t in a.tools]
    tool_list = names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1] if names else ""
    return (text.replace("{tool_list}", tool_list).replace("{validate_budget}", str(validate_budget))
            .replace("{rundir}", rundir)
            .replace("{max_continuations}", str(max_continuations)))


def env_int(name: str, default: int) -> int:
    try:
        return int(os.environ.get(name, default))
    except ValueError:
        return default


def sandbox() -> Path:
    return Path(os.environ["CC_SANDBOX"]).resolve()


def rundir() -> Path:
    p = Path(os.environ["CC_RUNDIR"]).resolve()
    p.mkdir(parents=True, exist_ok=True)
    return p


def inside(path: str, root: Path, cwd: Path | None = None) -> tuple[bool, Path]:
    """Resolve ``path`` the way a file tool would (relative to cwd, symlinks
    followed; a new file is checked through its directory) and say whether it
    lies in ``root``."""
    p = Path(os.path.expanduser(path))
    if not p.is_absolute():
        p = (cwd or root) / p
    # Collapse `..` first: `new/../../etc` must not pass through a directory
    # that does not exist yet.
    p = Path(os.path.normpath(str(p)))
    try:
        real = p.resolve(strict=True)
    except (FileNotFoundError, RuntimeError, OSError):
        parent = p.parent
        while not parent.exists() and parent != parent.parent:
            parent = parent.parent
        real = Path(os.path.normpath(str(parent.resolve() / p.relative_to(parent))))
    try:
        real.relative_to(root)
        return True, real
    except ValueError:
        return False, real


def sha(path: Path) -> str | None:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


STATE = "cc_state.json"


def load_state(rd: Path) -> dict:
    f = rd / STATE
    if f.is_file():
        try:
            return json.loads(f.read_text())
        except json.JSONDecodeError:
            pass
    return {"validations": 0, "reviews": 0,
            "validate_budget": env_int("CC_VALIDATE_BUDGET", 10),
            "review_budget": env_int("CC_REVIEW_BUDGET", 2),
            "last_validation": None, "review_log": []}


def save_state(rd: Path, state: dict) -> None:
    tmp = rd / (STATE + ".tmp")
    tmp.write_text(json.dumps(state, indent=1, default=str))
    tmp.replace(rd / STATE)


def log(rd: Path, name: str, rec: dict) -> None:
    with open(rd / name, "a") as fh:
        fh.write(json.dumps({"t": round(time.time(), 3), **rec}, default=str) + "\n")
