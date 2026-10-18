#!/usr/bin/env python3
"""V18 probe driver: fresh scratch copy -> mutation -> gate run (x2).

Usage:
  probe.py clean   <fixture_name>
  probe.py mutate  <fixture_name> <mode> [args...]

Runs corpus/tools/dependency_freeze.py against the scratch copy twice and
prints exit codes + verbatim stdout for each run.
"""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
TOOL = ROOT / "corpus" / "tools" / "dependency_freeze.py"
SCRATCH = ROOT / ".ufo" / "waves" / "round-96" / "V18-scratch"
sys.path.insert(0, str(SCRATCH))
import mutate  # noqa: E402


def fresh_copy(fixture_name):
    src = ROOT / "corpus" / "fixtures" / fixture_name
    parent = SCRATCH / "scratch-root"
    parent.mkdir(parents=True, exist_ok=True)
    dst = parent / fixture_name  # preserve basename in case the pin is keyed by it
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    return dst


def run_gate(d, label):
    cmd = ["python3", str(TOOL), str(d)]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT))
    print(f"--- {label} exit={r.returncode}")
    print(f"$ {' '.join(cmd)}")
    out = (r.stdout or "") + (r.stderr or "")
    print(out.rstrip() if out.strip() else "(no output)")
    return r.returncode, out


if __name__ == "__main__":
    mode = sys.argv[1]
    fixture = sys.argv[2]
    d = fresh_copy(fixture)
    if mode == "mutate":
        m = sys.argv[3]
        args = sys.argv[4:]
        if m == "phantom":
            mutate.phantom(str(d), args[0], args[1])
        elif m == "flip":
            mutate.flip(str(d))
        elif m == "endpoint":
            mutate.endpoint(str(d), args[0], args[1])
        elif m == "delete":
            mutate.delete(str(d), args[0])
        elif m == "reduce":
            mutate.reduce_edge(str(d), args[0], args[1])
        elif m == "texttamper":
            mutate.texttamper(str(d), args[0])
        else:
            raise SystemExit(f"unknown mode {m}")
    print(f"=== fixture={fixture} mode={mode} dir={d}")
    codes = []
    outs = []
    for i in (1, 2):
        c, o = run_gate(d, f"run{i}")
        codes.append(c)
        outs.append(o)
    print(f"=== SUMMARY fixture={fixture} mode={mode} exits={codes} identical_output={outs[0] == outs[1]}")
