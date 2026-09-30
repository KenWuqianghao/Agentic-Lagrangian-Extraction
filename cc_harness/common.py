"""Shared paths, state and path guard for the Claude Code harness.

The MCP server, both hooks and the runner read the same environment:

  CC_SANDBOX          the agent's working directory; the only tree a tool may touch
  CC_RUNDIR           where logs, validation outputs and state go (outside the sandbox)
  CC_VALIDATE_BUDGET  validate_model calls per run (default 10)
  CC_REVIEW_BUDGET    review_model calls per run (default 2)
  CC_MAX_CONTINUATIONS  Stop-gate blocks per run (default 3)
  CC_REVIEW_MODEL     model for the referee (default: CC_AGENT_MODEL)
  CC_AGENT_MODEL      model of the agent under test
"""

from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALE = HERE.parent
HEPVAL = Path(os.environ.get("CC_HEPVAL", ALE / "pi_harness" / "hepval.py"))
CLAUDE = os.environ.get("CC_CLAUDE_BIN", str(Path.home() / ".local/bin/claude"))
PYTHON = os.environ.get("CC_PYTHON", "python3")
SERVER_NAME = "heptapod-tools"
TOOLS = ("lint_model", "validate_model", "massbasis", "review_model")
MCP_TOOL_NAMES = tuple(f"mcp__{SERVER_NAME}__{t}" for t in TOOLS)


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
