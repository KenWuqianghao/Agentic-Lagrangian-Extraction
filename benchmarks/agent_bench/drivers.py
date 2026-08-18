"""
Harness adapters. One signature, so the model is the only variable.

    run(case, workdir, model) -> Trace

Adding a harness means adding a driver here and nothing else. That is the
whole reason the trace schema exists.

Only the Claude driver is implemented against a real CLI today, because that
is the only harness this machine has credentials for. The others are declared
with an explicit ``unavailable`` result rather than omitted, so a run reports
"codex: no credentials" instead of quietly comparing one model against
nothing.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import time
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional

from .trace import (
    Event, KIND_ERROR, Trace, discrepancy, from_claude_stream_json,
    from_codex_events, from_toolbase_log, merge,
)

TOOLBASE_LOG = Path.home() / ".toolbase" / "logs" / "tool_calls.jsonl"

HEPTAPOD = Path("/Users/kenwu/Documents/Github/heptapod")
MCP_SERVER = HEPTAPOD / "scripts" / "serve_lagrangian_mcp.py"
VENV_PY = HEPTAPOD / ".venv" / "bin" / "python"


def write_mcp_config(workdir: Path) -> Path:
    """An MCP config serving ONLY the heptapod toolkit.

    Two failures this prevents, both observed in a real run before it existed:
    the agent had no heptapod tools at all and answered by hitting the arXiv
    HTTP API directly, and it inherited the operator's own MCP servers. Either
    one turns "how well does this model drive the toolkit" into "how
    resourceful is this model in general", which is a different question with
    a flattering answer.

    Paired with --strict-mcp-config so nothing from the user's environment
    leaks in.
    """
    cfg = {"mcpServers": {"heptapod": {
        "command": str(VENV_PY),
        "args": [str(MCP_SERVER)],
        "env": {"PYTHONPATH": str(HEPTAPOD)},
    }}}
    path = workdir / "mcp_config.json"
    path.write_text(json.dumps(cfg, indent=1), encoding="utf-8")
    return path


class DriverUnavailable(RuntimeError):
    """This harness cannot run here — missing binary, or no credentials."""


def _toolbase_events(since: float, until: float) -> List[Event]:
    """Tool facts from the shared toolbase log, sliced to this run's window.

    The log is shared, so the window matters: without it a second concurrent
    run would be attributed to this one.
    """
    if not TOOLBASE_LOG.is_file():
        return []
    try:
        with open(TOOLBASE_LOG, "r", encoding="utf-8", errors="replace") as fh:
            return from_toolbase_log(fh, since=since, until=until)
    except OSError:
        return []


class Driver:
    """Base: name yourself, say whether you can run, then run."""

    name = "base"

    def available(self) -> Optional[str]:
        """None if usable, else the reason it is not."""
        return f"{self.name} driver not implemented"

    def run(self, case, workdir: Path, model: str) -> Trace:
        raise DriverUnavailable(self.available() or self.name)


class ClaudeCodeDriver(Driver):
    """`claude -p --output-format stream-json`, headless.

    Tool facts come from the toolbase log when one exists; the stream is used
    for messages and as a fallback when it does not.
    """

    name = "claude_code"

    def available(self) -> Optional[str]:
        if not shutil.which("claude"):
            return "claude CLI not on PATH"
        if not MCP_SERVER.is_file():
            return f"heptapod MCP server not found at {MCP_SERVER}"
        if not VENV_PY.is_file():
            return f"heptapod venv python not found at {VENV_PY}"
        return None

    def run(self, case, workdir: Path, model: str) -> Trace:
        reason = self.available()
        if reason:
            raise DriverUnavailable(reason)

        workdir.mkdir(parents=True, exist_ok=True)
        run_id = f"{case.case_id}-{self.name}-{uuid.uuid4().hex[:8]}"
        mcp_cfg = write_mcp_config(workdir)
        cmd = ["claude", "-p", "--output-format", "stream-json", "--verbose",
               "--mcp-config", str(mcp_cfg),
               # Without this the run inherits the operator's own MCP servers
               # and can solve the case with tools the toolkit never provided.
               "--strict-mcp-config",
               # And without THIS the agent reaches for its own Bash and
               # WebFetch instead. Observed: a run curl'd the archive's HTTP
               # API directly, produced the correct number, and would have
               # scored a clean pass having never touched the toolkit. The
               # benchmark measures driving these tools, so the shortcuts
               # have to be closed.
               "--disallowedTools", "Bash,WebFetch,WebSearch"]
        if model:
            cmd += ["--model", model]
        # The prompt goes on stdin, NOT as a positional. --disallowedTools is
        # variadic, so a trailing positional is swallowed as another tool name
        # and the CLI then exits with "Input must be provided either through
        # stdin or as a prompt argument" — a 2-second run that looks like a
        # model failure and is actually an argv bug.

        t0 = time.time()
        try:
            proc = subprocess.run(
                cmd, cwd=str(workdir), capture_output=True, text=True,
                timeout=case.timeout_s, input=case.prompt)
            out, err, code = proc.stdout, proc.stderr, proc.returncode
            timed_out = False
        except subprocess.TimeoutExpired as e:
            out = (e.stdout or "") if isinstance(e.stdout, str) else ""
            err = (e.stderr or "") + f"\ntimed out after {case.timeout_s}s"
            code, timed_out = 124, True
        t1 = time.time()

        (workdir / "harness_stdout.jsonl").write_text(out, encoding="utf-8")
        if err:
            (workdir / "harness_stderr.txt").write_text(err, encoding="utf-8")

        stream = from_claude_stream_json(out.splitlines())
        server = _toolbase_events(t0, t1)

        notes: List[str] = []
        if server:
            note = discrepancy(server, stream)
            if note:
                notes.append(note)
            events = merge(server, stream)
        else:
            notes.append("no toolbase log found; tool facts come from the "
                         "harness stream, which reports intent rather than "
                         "what the tool server actually executed")
            events = stream

        if timed_out:
            events.append(Event(seq=len(events) + 1, kind=KIND_ERROR,
                                error=f"timeout after {case.timeout_s}s",
                                source=self.name))
            notes.append("run hit the case timeout")

        return Trace(run_id=run_id, case_id=case.case_id, driver=self.name,
                     model=model or "default", events=events,
                     wall_seconds=round(t1 - t0, 1), exit_code=code,
                     notes=notes)


class CodexDriver(Driver):
    """`codex exec`. Present so the matrix is honest about what is missing."""

    name = "codex"

    def available(self) -> Optional[str]:
        if not shutil.which("codex"):
            return "codex CLI not on PATH"
        return ("codex CLI present but this account has no usage left; "
                "verified by a run that returned 'You've hit your usage limit'")


class OrchestralDriver(Driver):
    """In-process orchestral agent — the route to non-Anthropic models.

    heptapod already ships orchestral demos, so this is where Gemini, Groq
    and Ollama arrive without a new harness. Needs a provider key.
    """

    name = "orchestral"

    def available(self) -> Optional[str]:
        try:
            import orchestral  # noqa: F401
        except Exception:                                   # noqa: BLE001
            return "orchestral not importable"
        if not any(os.environ.get(k) for k in
                   ("OPENAI_API_KEY", "GEMINI_API_KEY", "GROQ_API_KEY")):
            return "no provider key set (OPENAI_API_KEY / GEMINI_API_KEY / GROQ_API_KEY)"
        return "driver not implemented yet"


DRIVERS: Dict[str, Driver] = {
    d.name: d for d in (ClaudeCodeDriver(), CodexDriver(), OrchestralDriver())
}


def availability() -> Dict[str, Any]:
    """What can actually run here, and why not for the rest."""
    return {name: {"available": d.available() is None,
                   "reason": d.available()}
            for name, d in DRIVERS.items()}
