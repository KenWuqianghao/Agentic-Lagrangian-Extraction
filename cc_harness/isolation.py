"""Run a runtime agent that has a shell without letting it read a stored
answer, and make its Wolfram runs wait for the one kernel.

Linux: bubblewrap hides ~/code, ~/Documents and /tmp, then binds back only
what the caller names. macOS: sandbox-exec denies reads under ~/Documents,
~/code, ~/Desktop and ~/Downloads (binds are not possible there, so a run
that needs files from those trees must not use it).
"""

from __future__ import annotations

import sys
from pathlib import Path

HOME = Path.home()
MAC = sys.platform == "darwin"
# The chain's three paths on this machine (the Mac keeps them in the home directory).
FEYNRULES = HOME / "feynrules-current" if MAC else HOME / "hep-tools" / "feynrules-current"
MG5 = HOME / "MG5_aMC" if MAC else HOME / "hep-tools" / "MG5_aMC"
WOLFRAMSCRIPT = Path("/opt/homebrew/bin/wolframscript") if MAC else HOME / "hep-tools" / "bin" / "wolframscript"

WRAPPER = """#!{python}
# One Wolfram kernel at a time on this machine (licence limit); wait for it.
import fcntl, os, sys
fd = os.open("{lock}", os.O_RDWR | os.O_CREAT)
fcntl.flock(fd, fcntl.LOCK_EX)
os.set_inheritable(fd, True)          # the lock lives as long as wolframscript does
os.execv("{real}", ["{real}", *sys.argv[1:]])
"""


def write_wolframscript_wrapper(sandbox: Path, lock: Path) -> Path:
    """`<sandbox>/.bin/wolframscript`: put `<sandbox>/.bin` first on PATH."""
    (sandbox / ".bin").mkdir(exist_ok=True)
    w = sandbox / ".bin" / "wolframscript"
    w.write_text(WRAPPER.format(python=sys.executable, lock=lock, real=WOLFRAMSCRIPT))
    w.chmod(0o755)
    return w.parent


def isolate(cmd: list[str], sandbox: Path, read_only: tuple = (), read_write: tuple = (), hidden: tuple = ()) -> list[str]:
    """`cmd` in a view of the machine without the repositories and stored
    runs. `read_only` and `read_write` paths under the hidden trees come back
    (Linux only); `hidden` files inside them are replaced by an empty file."""
    if MAC:
        profile = ('(version 1)(allow default)'
                   f'(deny file-read* (subpath "{HOME / "Documents"}") (subpath "{HOME / "code"}")'
                   f' (subpath "{HOME / "Desktop"}") (subpath "{HOME / "Downloads"}"))')
        return ["sandbox-exec", "-p", profile, *cmd]
    binds = [x for p in read_only for x in ("--ro-bind", str(p), str(p))]
    binds += [x for p in read_write for x in ("--bind", str(p), str(p))]
    binds += [x for p in hidden for x in ("--ro-bind", "/dev/null", str(p))]
    return ["bwrap", "--bind", "/", "/", "--dev", "/dev", "--proc", "/proc",
            "--tmpfs", str(HOME / "code"), "--tmpfs", str(HOME / "Documents"), "--tmpfs", "/tmp",
            "--tmpfs", str(HOME / ".claude" / "projects"),
            "--bind", str(sandbox), str(sandbox), *binds,
            "--chdir", str(sandbox), "--die-with-parent", *cmd]
