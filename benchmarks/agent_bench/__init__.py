"""
Model-agnostic benchmark for agents driving the HEPTAPOD physics toolkit.

The question is "which model is best at actually doing the physics work",
which is only answerable if every harness reduces to the same record and
every case is scored on an artifact rather than on the model's own account
of itself. Those two constraints are the design.

    trace.py    one normalized event stream, whatever harness produced it
    cases.py    the tasks, tiered, each scored on a verifiable artifact
    drivers.py  one adapter per harness, identical signature
    run.py      the matrix runner

Only Claude has credentials on this machine today. Other harnesses are
declared with an explicit unavailable-reason rather than omitted, so a run
says "codex: no usage left" instead of quietly comparing one model to
nothing.
"""

from .cases import Case, default_cases
from .drivers import DRIVERS, availability
from .trace import Event, Trace

__all__ = ["Case", "default_cases", "DRIVERS", "availability", "Event", "Trace"]
