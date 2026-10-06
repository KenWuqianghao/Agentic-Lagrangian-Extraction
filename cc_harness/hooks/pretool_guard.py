#!/usr/bin/env python3
"""PreToolUse hook: the sandbox, enforced by configuration, not by the prompt.

Claude Code sends the tool call as JSON on stdin. The hook denies:
  - any tool that runs code or reaches the network (Bash, WebFetch, WebSearch,
    Task/Agent: a subagent is a second way around the guard);
  - any file tool (Read, Write, Edit, MultiEdit, NotebookEdit, Glob, Grep, LS)
    whose path, after `..` and symlinks, lies outside CC_SANDBOX.
The heptapod MCP tools check their own paths against the same sandbox.

A denial is a JSON permissionDecision on stdout; every decision is appended
to CC_RUNDIR/hook_log.jsonl.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import common as C  # noqa: E402

DENY_TOOLS = {"Bash", "BashOutput", "KillShell", "WebFetch", "WebSearch", "Task", "Agent",
              "PowerShell", "REPL"}
FILE_TOOLS = {"Read", "Write", "Edit", "MultiEdit", "NotebookEdit", "Glob", "Grep", "LS"}
PATH_KEYS = ("file_path", "path", "notebook_path")


def _glob_root(pattern: str) -> str | None:
    """The fixed directory prefix of an absolute or `..` glob pattern."""
    parts = []
    for part in Path(pattern).parts:
        if any(ch in part for ch in "*?[{"):
            break
        parts.append(part)
    return str(Path(*parts)) if parts else None


def decide(event: dict, sandbox: Path) -> tuple[bool, str]:
    tool = event.get("tool_name") or ""
    inp = event.get("tool_input") or {}
    cwd = Path(event.get("cwd") or sandbox)
    if tool in DENY_TOOLS:
        return False, f"{tool} is not available in this harness (no shell, no network, no subagents); use the file tools and the heptapod tools"
    if tool.startswith("mcp__"):
        return tool in C.mcp_tool_names(C.arm()), f"only the {C.SERVER_NAME} MCP tools are available"
    if tool not in FILE_TOOLS:
        return True, "not a file tool"
    paths = [inp[k] for k in PATH_KEYS if isinstance(inp.get(k), str) and inp.get(k)]
    if tool == "Glob" and isinstance(inp.get("pattern"), str):
        root = _glob_root(inp["pattern"])
        if root and (Path(root).is_absolute() or ".." in Path(root).parts):
            paths.append(root)
    if tool == "Grep" and isinstance(inp.get("glob"), str) and ".." in inp["glob"]:
        return False, "a Grep glob may not leave the working directory"
    for p in paths or ["."]:
        ok, real = C.inside(p, sandbox, cwd)
        if not ok:
            return False, f"path {p} is outside the sandbox; only files under {sandbox} exist for this task"
    return True, "inside the sandbox"


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        event = {}
    sb = C.sandbox()
    allow, reason = decide(event, sb)
    try:
        C.log(C.rundir(), "hook_log.jsonl", {"hook": "PreToolUse", "tool": event.get("tool_name"),
                                              "decision": "allow" if allow else "deny", "reason": reason,
                                              "input": event.get("tool_input")})
    except (KeyError, OSError):
        pass
    if not allow:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                                 "permissionDecision": "deny",
                                                 "permissionDecisionReason": reason}}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
