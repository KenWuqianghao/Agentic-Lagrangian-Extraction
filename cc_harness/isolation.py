"""Run a runtime agent that has a shell without letting it read a stored
answer or change the harness's record of the run.

The agent sees its sandbox, the paths the caller names, and nothing of the
repositories, the stored runs or other runs. It can run the shared toolchain
(FeynRules, MadGraph) but not change it. The harness commands it calls
(the MCP server, the Stop hook) run outside, through a Broker, so their state
is out of the agent's reach. The agent writes only to its sandbox, the
`read_write` paths and what Claude Code and Wolfram need: a write anywhere
else (~/.local, the Wolfram init files) would run outside the sandbox later.

Linux: bubblewrap mounts the host read-only, with empty writable directories
over ~/code, ~/Documents, /tmp, ~/.cache, ~/.claude (only the credentials file
is bound back) and the SECRETS, binds back the named paths, and runs the agent
in its own PID namespace, so every process it starts ends with it. macOS:
sandbox-exec denies reads of the same trees, of the SECRETS, of the repository,
of /tmp and of other runs' sandboxes, and writes outside the sandbox, the named
paths, the user temporary directory, the user caches and Claude Code's
~/.claude; it cannot end leftover processes, so the wolframscript wrapper
records the ones that hold a kernel slot.
"""

from __future__ import annotations

import os
import shlex
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

HOME = Path.home()
MAC = sys.platform == "darwin"
REPO = Path(__file__).resolve().parent.parent
# The chain's three paths on this machine (the Mac keeps them in the home directory).
FEYNRULES = HOME / "feynrules-current" if MAC else HOME / "hep-tools" / "feynrules-current"
MG5 = HOME / "MG5_aMC" if MAC else HOME / "hep-tools" / "MG5_aMC"
WOLFRAMSCRIPT = (
    Path("/opt/homebrew/bin/wolframscript") if MAC else HOME / "hep-tools" / "bin" / "wolframscript"
)
# macOS: without this variable wolframscript opens its config in ~/Library for writing, which
# the sandbox denies; the agent could otherwise point the scorer's wolframscript at a kernel.
WOLFRAM_KERNEL = Path("/Applications/Wolfram Engine.app/Contents/MacOS/WolframKernel")
# The software the scorer shares with the agent. The agent can run it but not change it: a
# setting it saves (MadGraph's auto_convert_model, say) would change every later verdict.
TOOLCHAIN = (FEYNRULES, MG5, Path("/opt/homebrew")) if MAC else (HOME / "hep-tools",)
# Credentials the agent's shell could read and send out. Claude Code's own login stays readable:
# claude runs in the same sandbox.
SECRETS = tuple(
    HOME / p
    for p in (
        ".ssh",
        ".gnupg",
        ".config/gh",
        ".git-credentials",
        ".netrc",
        ".aws",
        ".claude-oauth-token",
    )
)
# After a timeout the agent gets SIGTERM, then SIGKILL if it is still running this much later.
KILL_GRACE = 60

WRAPPER = """#!{python}
# The licence runs {slots} Wolfram kernels at a time; wait for a slot
# (hepval takes them the same way).
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

# macOS: sandbox-exec does not end what a run leaves behind, and `ps` hides the environment, so
# the wrapper stays as the parent and records each wolframscript it starts (its own process group,
# kernel and subkernels included) in `.bin/pids`; kill_recorded() ends them when the run is over.
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
    cmd: list[str], sandbox: Path, read_only: tuple = (), read_write: tuple = ()
) -> list[str]:
    """`cmd` in a view of the machine without the repositories, the stored runs
    and other runs: the sandbox, plus `read_only` and `read_write` paths."""
    if MAC:
        tmp = sandbox / ".tmp"
        tmp.mkdir(exist_ok=True)
        hidden = (
            HOME / "Documents",
            HOME / "code",
            HOME / "Desktop",
            HOME / "Downloads",
            HOME / ".claude" / "projects",
            REPO,
            Path("/tmp").resolve(),
            *SECRETS,
        )

        def paths(ps):
            return " ".join(f'(subpath "{Path(p).resolve()}")' for p in ps)

        # Wolfram does not start without the user temporary directory, so only the sandboxes
        # of other runs in it are hidden.
        user_tmp = Path(tempfile.gettempdir()).resolve()
        others = f'(regex #"^{user_tmp}/(cc|vanilla)-")'
        writable = (sandbox, *read_write, user_tmp, HOME / "Library" / "Caches", HOME / ".claude")
        profile = (
            "(version 1)(allow default)"
            f"(deny file-read* {paths(hidden)} {others})"
            f"(allow file-read* {paths((sandbox, *read_only, *read_write))})"
            '(deny file-write* (subpath "/"))'
            f'(allow file-write* {paths(writable)} (subpath "/dev")'
            f' (literal "{HOME / ".claude.json"}"))'
            f"(deny file-write* {paths((*TOOLCHAIN, *read_only))} {others})"
            f"(allow file-write* {paths((sandbox,))})"
        )
        # Claude Code keeps its own files under /tmp unless CLAUDE_CODE_TMPDIR names a place.
        return [
            "sandbox-exec",
            "-p",
            profile,
            "/usr/bin/env",
            f"TMPDIR={tmp}",
            f"CLAUDE_CODE_TMPDIR={tmp}",
            f"WolframKernel={WOLFRAM_KERNEL}",
            *cmd,
        ]
    binds = [x for p in (*TOOLCHAIN, *read_only) for x in ("--ro-bind", str(p), str(p))]
    binds += [x for p in read_write for x in ("--bind", str(p), str(p))]
    for p in SECRETS:
        if p.is_dir():
            binds += ["--tmpfs", str(p)]
        elif p.exists():
            binds += ["--ro-bind", "/dev/null", str(p)]
    # Claude Code refreshes its login in this file; the rest of ~/.claude stays out of reach.
    creds = HOME / ".claude" / ".credentials.json"
    if creds.is_file():
        binds += ["--bind", str(creds), str(creds)]
    return [
        "bwrap",
        "--ro-bind",
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
        str(HOME / ".cache"),
        "--tmpfs",
        str(HOME / ".claude"),
        "--bind",
        str(sandbox),
        str(sandbox),
        *binds,
        "--chdir",
        str(sandbox),
        "--unshare-pid",
        "--die-with-parent",
        *cmd,
    ]


def run(
    cmd: list[str], sandbox: Path, env: dict, prompt: str, out, err, timeout: float
) -> tuple[int, bool]:
    """Run the agent with `prompt` on stdin until it exits or `timeout` seconds
    pass, then end every process it left. Returns the exit code and whether the
    timeout ended it."""
    p = subprocess.Popen(
        cmd,
        cwd=str(sandbox),
        env=env,
        stdin=subprocess.PIPE,
        stdout=out,
        stderr=err,
        start_new_session=True,
        text=True,
    )
    p.stdin.write(prompt)
    p.stdin.close()
    timed_out = False
    try:
        rc = p.wait(timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        _killpg(p.pid, signal.SIGTERM)
        try:
            rc = p.wait(KILL_GRACE)
        except subprocess.TimeoutExpired:
            _killpg(p.pid, signal.SIGKILL)
            rc = p.wait()
    _killpg(p.pid, signal.SIGKILL)
    kill_recorded(sandbox)
    return rc, timed_out


def _killpg(pgid: int, sig: int) -> None:
    # macOS gives EPERM, not ESRCH, for a group whose processes have all exited.
    try:
        os.killpg(pgid, sig)
    except (ProcessLookupError, PermissionError):
        pass


PROXY = """import socket, sys, threading
s = socket.socket(socket.AF_UNIX)
s.connect(sys.argv[1])
def up():
    while chunk := sys.stdin.buffer.read1(65536):
        s.sendall(chunk)
    s.shutdown(socket.SHUT_WR)
threading.Thread(target=up, daemon=True).start()
while chunk := s.recv(65536):
    sys.stdout.buffer.write(chunk)
    sys.stdout.buffer.flush()
"""


class Broker:
    """Harness commands for a sandboxed agent, run outside the sandbox.

    Each command listens on a Unix socket in a directory that the agent can
    read but not write. The agent's side runs `command(name)`, a proxy that
    joins its stdin and stdout to a new process of that command started here.
    The agent can call the command, as it can call a tool, but it cannot change
    the command's code or the files it keeps.
    """

    def __init__(self, commands: dict[str, list[str]], env: dict, log: Path):
        # Under /tmp: a socket path has at most 104 bytes on macOS.
        self.dir = Path(tempfile.mkdtemp(prefix="cc-ctl-", dir="/tmp"))
        (self.dir / "proxy.py").write_text(PROXY)
        self.env = env
        self.log = log
        self.children: list[subprocess.Popen] = []
        self.listeners: list[socket.socket] = []
        self.threads: list[threading.Thread] = []
        self.closed = threading.Event()
        for name, cmd in commands.items():
            s = socket.socket(socket.AF_UNIX)
            s.bind(str(self.dir / f"{name}.sock"))
            s.listen()
            s.settimeout(1)
            self.listeners.append(s)
            self.threads.append(threading.Thread(target=self._serve, args=(s, cmd), daemon=True))
            self.threads[-1].start()

    def command(self, name: str) -> list[str]:
        return [sys.executable, str(self.dir / "proxy.py"), str(self.dir / f"{name}.sock")]

    def shell_command(self, name: str) -> str:
        return shlex.join(self.command(name))

    def _serve(self, listener: socket.socket, cmd: list[str]) -> None:
        while not self.closed.is_set():
            try:
                conn, _ = listener.accept()
            except TimeoutError:
                continue
            conn.setblocking(True)
            with conn, open(self.log, "a") as err:
                self.children.append(
                    subprocess.Popen(
                        cmd,
                        stdin=conn,
                        stdout=conn,
                        stderr=err,
                        env=self.env,
                        start_new_session=True,
                    )
                )

    def __enter__(self) -> Broker:
        return self

    def __exit__(self, *exc) -> None:
        self.closed.set()
        for t in self.threads:
            t.join()
        for s in self.listeners:
            s.close()
        for c in self.children:
            _killpg(c.pid, signal.SIGKILL)
            c.wait()
        shutil.rmtree(self.dir)
