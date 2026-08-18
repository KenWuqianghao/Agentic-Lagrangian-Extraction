"""
One normalized event stream, whatever harness produced it.

The whole point of this module is that "which model is best at driving the
physics toolkit" is only answerable if a Claude Code run and a Codex run and a
plain API tool-loop all reduce to the SAME record. Everything else in
agent_bench is wiring; this is the part that makes the comparison fair.

Design rule: ground tool facts in toolbase's own ``tool_calls.jsonl`` where it
is available, because that log is written by the tool server and is therefore
identical across harnesses. Use the harness's own stream only for what the
tool server cannot see — turn count, reasoning text, shell commands.

A harness that reports a tool call the tool server never saw is a harness
telling you what it *intended*, not what happened. Preferring the server log
is what stops a chatty model scoring well for narrating tool calls it did not
make.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

SCHEMA = "agent-bench-trace-1.0"

KIND_TOOL_CALL = "tool_call"
KIND_SHELL = "shell"
KIND_MESSAGE = "message"
KIND_ERROR = "error"


@dataclass
class Event:
    """One thing the agent did."""

    seq: int
    kind: str                      # tool_call | shell | message | error
    tool: Optional[str] = None
    args: Optional[Dict[str, Any]] = None
    ok: Optional[bool] = None
    duration_s: Optional[float] = None
    error: Optional[str] = None
    text: Optional[str] = None     # message/reasoning, truncated by the adapter
    source: str = "unknown"        # which log this came from, for auditing

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class Trace:
    """A whole run, normalized."""

    run_id: str
    case_id: str
    driver: str
    model: str
    events: List[Event] = field(default_factory=list)
    wall_seconds: Optional[float] = None
    exit_code: Optional[int] = None
    notes: List[str] = field(default_factory=list)

    # ------------------------------------------------------------- metrics
    @property
    def tool_calls(self) -> List[Event]:
        return [e for e in self.events if e.kind == KIND_TOOL_CALL]

    @property
    def n_tool_calls(self) -> int:
        return len(self.tool_calls)

    @property
    def n_failed_tool_calls(self) -> int:
        return sum(1 for e in self.tool_calls if e.ok is False)

    @property
    def distinct_tools(self) -> List[str]:
        return sorted({e.tool for e in self.tool_calls if e.tool})

    def tool_histogram(self) -> Dict[str, int]:
        out: Dict[str, int] = {}
        for e in self.tool_calls:
            if e.tool:
                out[e.tool] = out.get(e.tool, 0) + 1
        return dict(sorted(out.items(), key=lambda kv: -kv[1]))

    def summary(self) -> Dict[str, Any]:
        return {
            "schema": SCHEMA,
            "run_id": self.run_id,
            "case_id": self.case_id,
            "driver": self.driver,
            "model": self.model,
            "wall_seconds": self.wall_seconds,
            "exit_code": self.exit_code,
            "n_events": len(self.events),
            "n_tool_calls": self.n_tool_calls,
            "n_failed_tool_calls": self.n_failed_tool_calls,
            "distinct_tools": self.distinct_tools,
            "tool_histogram": self.tool_histogram(),
            "notes": self.notes,
        }

    def write(self, path: Path) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(
            {**self.summary(), "events": [e.to_dict() for e in self.events]},
            indent=1), encoding="utf-8")
        return path


# --------------------------------------------------------------- adapters
def from_toolbase_log(lines: Iterable[str], *, since: float = 0.0,
                      until: Optional[float] = None) -> List[Event]:
    """Events from toolbase's ``tool_calls.jsonl``.

    This is the authoritative source for tool facts. ``since``/``until`` slice
    by timestamp, because a shared log file may hold other runs; pass the
    window around the run rather than assuming the file is yours.
    """
    events: List[Event] = []
    seq = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        ts = _num(rec.get("ts") or rec.get("timestamp") or rec.get("time"))
        if ts is not None:
            if ts < since:
                continue
            if until is not None and ts > until:
                continue
        seq += 1
        ok = rec.get("ok")
        if ok is None and "error" in rec:
            ok = not rec.get("error")
        events.append(Event(
            seq=seq, kind=KIND_TOOL_CALL,
            tool=rec.get("tool") or rec.get("tool_name") or rec.get("name"),
            args=rec.get("args") if isinstance(rec.get("args"), dict) else None,
            ok=bool(ok) if ok is not None else None,
            duration_s=_num(rec.get("duration_s") or rec.get("duration")),
            error=rec.get("error") or None,
            source="toolbase",
        ))
    return events


def from_claude_stream_json(lines: Iterable[str],
                            max_text: int = 400) -> List[Event]:
    """Events from ``claude -p --output-format stream-json``.

    Used for what toolbase cannot see. If a toolbase log is also available,
    prefer it for tool facts and keep these only for messages — see
    :func:`merge`.
    """
    events: List[Event] = []
    seq = 0
    pending: Dict[str, Event] = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue

        for block in _content_blocks(rec):
            btype = block.get("type")
            if btype == "tool_use":
                seq += 1
                ev = Event(seq=seq, kind=KIND_TOOL_CALL,
                           tool=block.get("name"),
                           args=block.get("input") if isinstance(
                               block.get("input"), dict) else None,
                           source="claude-stream")
                pending[str(block.get("id"))] = ev
                events.append(ev)
            elif btype == "tool_result":
                ev = pending.get(str(block.get("tool_use_id")))
                if ev is not None:
                    ev.ok = not bool(block.get("is_error"))
                    if block.get("is_error"):
                        ev.error = _flatten_text(block.get("content"))[:300]
            elif btype == "text":
                txt = (block.get("text") or "").strip()
                if txt:
                    seq += 1
                    events.append(Event(seq=seq, kind=KIND_MESSAGE,
                                        text=txt[:max_text],
                                        source="claude-stream"))
    return events


def from_codex_events(lines: Iterable[str],
                      max_text: int = 400) -> List[Event]:
    """Events from codex's ``codex_events.jsonl``."""
    events: List[Event] = []
    seq = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        t = str(rec.get("type") or rec.get("event") or "")
        if "function_call" in t or "tool" in t:
            seq += 1
            args = rec.get("arguments") or rec.get("args")
            if isinstance(args, str):
                try:
                    args = json.loads(args)
                except json.JSONDecodeError:
                    args = {"raw": args[:200]}
            events.append(Event(
                seq=seq, kind=KIND_TOOL_CALL,
                tool=rec.get("name") or rec.get("tool"),
                args=args if isinstance(args, dict) else None,
                source="codex"))
        elif "message" in t or "text" in t:
            txt = _flatten_text(rec.get("content") or rec.get("text"))
            if txt.strip():
                seq += 1
                events.append(Event(seq=seq, kind=KIND_MESSAGE,
                                    text=txt.strip()[:max_text],
                                    source="codex"))
    return events


def merge(authoritative: List[Event], supplementary: List[Event]) -> List[Event]:
    """Tool facts from the tool server; everything else from the harness.

    Where both describe tool calls, the server wins outright rather than
    being deduplicated heuristically: a harness can claim a call the server
    never received, and silently trusting that would reward a model for
    narrating work it did not do. The discrepancy is recorded rather than
    hidden.
    """
    tools = [e for e in authoritative if e.kind == KIND_TOOL_CALL]
    others = [e for e in supplementary if e.kind != KIND_TOOL_CALL]
    out = tools + others
    for i, e in enumerate(out, 1):
        e.seq = i
    return out


def discrepancy(authoritative: List[Event],
                supplementary: List[Event]) -> Optional[str]:
    """A note when the harness and the tool server disagree on call count."""
    a = sum(1 for e in authoritative if e.kind == KIND_TOOL_CALL)
    b = sum(1 for e in supplementary if e.kind == KIND_TOOL_CALL)
    if a == b:
        return None
    return (f"harness reported {b} tool calls, tool server recorded {a}; "
            f"scoring uses the tool server")


# ----------------------------------------------------------------- helpers
def _num(v: Any) -> Optional[float]:
    try:
        return float(v) if v is not None else None
    except (TypeError, ValueError):
        return None


def _content_blocks(rec: Dict[str, Any]) -> List[Dict[str, Any]]:
    msg = rec.get("message") if isinstance(rec.get("message"), dict) else rec
    content = msg.get("content")
    if isinstance(content, list):
        return [b for b in content if isinstance(b, dict)]
    return []


def _flatten_text(content: Any) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return " ".join(
            b.get("text", "") for b in content
            if isinstance(b, dict) and b.get("type") == "text")
    return ""
