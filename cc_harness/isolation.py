"""Run a runtime agent that has a shell without letting it read a stored
answer, and make its Wolfram runs wait for the one kernel.

Linux: bubblewrap hides ~/code, ~/Documents and /tmp, then binds back only
what the caller names. macOS: sandbox-exec denies reads under ~/Documents,
~/code, ~/Desktop and ~/Downloads (binds are not possible there, so a run
that needs files from those trees must not use it).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

HOME = Path.home()
MAC = sys.platform == "darwin"
# The chain's three paths on this machine (the Mac keeps them in the home directory).
FEYNRULES = HOME / "feynrules-current" if MAC else HOME / "hep-tools" / "feynrules-current"
MG5 = HOME / "MG5_aMC" if MAC else HOME / "hep-tools" / "MG5_aMC"
WOLFRAMSCRIPT = (
    Path("/opt/homebrew/bin/wolframscript") if MAC else HOME / "hep-tools" / "bin" / "wolframscript"
)

WRAPPER = """#!{python}
# The licence runs {slots} Wolfram kernels at a time; wait for a slot (hepval takes them the same way).
import fcntl, os, sys, time
while True:
    for i in range({slots}):
        fd = os.open("{lock}." + str(i), os.O_RDWR | os.O_CREAT)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            os.close(fd)
            continue
        os.set_inheritable(fd, True)          # the slot is held as long as wolframscript runs
        os.execv("{real}", ["{real}", *sys.argv[1:]])
    time.sleep(2)
"""

# macOS: sandbox-exec does not end what a run leaves behind, and `ps` hides the environment, so the
# wrapper stays as the parent and records each wolframscript it starts (its own process group, kernel
# and subkernels included) in `.bin/pids`; kill_recorded() ends them when the run is over.
WRAPPER_TRACKED = """#!{python}
import fcntl, os, signal, subprocess, sys, time
def slot():
    while True:
        for i in range({slots}):
            fd = os.open("{lock}." + str(i), os.O_RDWR | os.O_CREAT)
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                return fd
            except BlockingIOError:
                os.close(fd)
        time.sleep(2)
fd = slot()
p = subprocess.Popen(["{real}", *sys.argv[1:]], start_new_session=True)
with open("{pids}", "a") as f:
    f.write(str(p.pid) + "\\n")
def forward(sig, _frame):
    try:
        os.killpg(p.pid, sig)
    except ProcessLookupError:
        pass
for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
    signal.signal(s, forward)
sys.exit(p.wait())
"""


def kill_recorded(sandbox: Path) -> None:
    """End every wolframscript the tracked wrapper started in this sandbox."""
    import signal

    pids = sandbox / ".bin" / "pids"
    for pid in pids.read_text().split() if pids.is_file() else ():
        try:
            os.killpg(int(pid), signal.SIGKILL)
        except (ProcessLookupError, PermissionError, ValueError):
            pass


def write_wolframscript_wrapper(sandbox: Path, lock: Path) -> Path:
    """`<sandbox>/.bin/wolframscript`: put `<sandbox>/.bin` first on PATH."""
    (sandbox / ".bin").mkdir(exist_ok=True)
    w = sandbox / ".bin" / "wolframscript"
    w.write_text(
        (WRAPPER_TRACKED if MAC else WRAPPER).format(
            python=sys.executable,
            lock=lock,
            real=WOLFRAMSCRIPT,
            pids=sandbox / ".bin" / "pids",
            slots=os.environ.get("HEPVAL_KERNEL_SLOTS", "2"),
        )
    )
    w.chmod(0o755)
    return w.parent


def isolate(
    cmd: list[str], sandbox: Path, read_only: tuple = (), read_write: tuple = (), hidden: tuple = ()
) -> list[str]:
    """`cmd` in a view of the machine without the repositories and stored
    runs. `read_only` and `read_write` paths under the hidden trees come back
    (Linux only); `hidden` files inside them are replaced by an empty file."""
    if MAC:
        profile = (
            "(version 1)(allow default)"
            f'(deny file-read* (subpath "{HOME / "Documents"}") (subpath "{HOME / "code"}")'
            f' (subpath "{HOME / "Desktop"}") (subpath "{HOME / "Downloads"}"))'
        )
        return ["sandbox-exec", "-p", profile, *cmd]
    binds = [x for p in read_only for x in ("--ro-bind", str(p), str(p))]
    binds += [x for p in read_write for x in ("--bind", str(p), str(p))]
    binds += [x for p in hidden for x in ("--ro-bind", "/dev/null", str(p))]
    return [
        "bwrap",
        "--bind",
        "/",
        "/",
        "--dev",
        "/dev",
        "--proc",
        "/proc",
        "--tmpfs",
        str(HOME / "code"),
        "--tmpfs",
        str(HOME / "Documents"),
        "--tmpfs",
        "/tmp",
        "--tmpfs",
        str(HOME / ".claude" / "projects"),
        "--bind",
        str(sandbox),
        str(sandbox),
        *binds,
        "--chdir",
        str(sandbox),
        "--die-with-parent",
        *cmd,
    ]
