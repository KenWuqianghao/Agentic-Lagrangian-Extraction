"""Tests for isolation.py: the Broker, the timeout, and what a sandboxed agent
can change. The sandbox tests need bubblewrap and skip without it."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import isolation  # noqa: E402

PY = sys.executable
needs_bwrap = pytest.mark.skipif(
    isolation.MAC or not shutil.which("bwrap"), reason="needs bubblewrap"
)


def test_the_proxy_joins_the_caller_to_a_command_run_by_the_broker(tmp_path):
    upper = [PY, "-c", "import sys; sys.stdout.write(sys.stdin.read().upper())"]
    with isolation.Broker({"up": upper}, {}, tmp_path / "log") as broker:
        out = subprocess.run(broker.command("up"), input="call", capture_output=True, text=True)
    assert out.stdout == "CALL"


def test_an_agent_that_ignores_sigterm_is_killed_after_the_grace(tmp_path, monkeypatch):
    monkeypatch.setattr(isolation, "KILL_GRACE", 1)
    stubborn = "import signal, time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(60)"
    t0 = time.time()
    with open(tmp_path / "out", "w") as out:
        rc, timed_out = isolation.run([PY, "-c", stubborn], tmp_path, None, "", out, out, 1)
    assert timed_out and rc != 0 and time.time() - t0 < 10


def _in_sandbox(sb: Path, script: str, **kw) -> str:
    cmd = isolation.isolate(["sh", "-c", script], sb, **kw)
    with open(sb / "out", "w") as out:
        isolation.run(cmd, sb, None, "", out, out, 30)
    return (sb / "out").read_text()


@needs_bwrap
def test_a_process_the_agent_detaches_ends_with_the_agent(tmp_path):
    sb = tmp_path / "sb"
    sb.mkdir()
    # The agent exits only once the detached process runs in its own session.
    _in_sandbox(sb, f"setsid sh -c 'touch {sb}/started; sleep 2; touch {sb}/late' & sleep 1")
    time.sleep(3)
    assert (sb / "started").exists()
    assert not (sb / "late").exists()


@needs_bwrap
def test_the_agent_reads_but_cannot_change_its_run_directory(tmp_path):
    sb, rundir = tmp_path / "sb", tmp_path / "run"
    sb.mkdir()
    rundir.mkdir()
    (rundir / "cc_state.json").write_text('{"validations": 3}')
    out = _in_sandbox(
        sb,
        f"cat {rundir}/cc_state.json; echo '{{}}' > {rundir}/cc_state.json || echo denied",
        read_only=(rundir,),
    )
    assert '"validations": 3' in out and "denied" in out
    assert (rundir / "cc_state.json").read_text() == '{"validations": 3}'


@needs_bwrap
def test_the_agent_runs_the_shared_toolchain_but_cannot_change_it(tmp_path, monkeypatch):
    sb, tools = tmp_path / "sb", tmp_path / "hep-tools"
    sb.mkdir()
    tools.mkdir()
    (tools / "mg5_configuration.txt").write_text("auto_convert_model = True")
    monkeypatch.setattr(isolation, "TOOLCHAIN", (tools,))
    out = _in_sandbox(
        sb,
        f"cat {tools}/mg5_configuration.txt; "
        f"echo 'auto_convert_model = False' > {tools}/mg5_configuration.txt || echo denied",
    )
    assert "= True" in out and "denied" in out
    assert (tools / "mg5_configuration.txt").read_text() == "auto_convert_model = True"


@needs_bwrap
def test_the_agent_writes_its_sandbox_but_no_other_host_path(tmp_path):
    # /var/tmp stands for ~/.local and the Wolfram init files: the user can write it and no
    # empty directory covers it.
    sb, host = tmp_path / "sb", Path(tempfile.mkdtemp(dir="/var/tmp"))
    sb.mkdir()
    try:
        out = _in_sandbox(
            sb, f"echo x > {sb}/model.fr && echo wrote; echo x > {host}/claude || echo denied"
        )
        assert "wrote" in out and "denied" in out
        assert (sb / "model.fr").is_file() and not (host / "claude").exists()
    finally:
        shutil.rmtree(host)


@needs_bwrap
def test_the_agent_cannot_read_the_hosts_credentials(tmp_path, monkeypatch):
    sb, home = tmp_path / "sb", Path(tempfile.mkdtemp(dir="/var/tmp"))
    sb.mkdir()
    (home / ".ssh").mkdir()
    (home / ".ssh" / "id_ed25519").write_text("PRIVATE KEY")
    (home / ".netrc").write_text("password hunter2")
    monkeypatch.setattr(isolation, "SECRETS", (home / ".ssh", home / ".netrc", home / ".aws"))
    try:
        out = _in_sandbox(sb, f"cat {home}/.ssh/id_ed25519 {home}/.netrc; echo done")
        assert "done" in out and "PRIVATE KEY" not in out and "hunter2" not in out
    finally:
        shutil.rmtree(home)
