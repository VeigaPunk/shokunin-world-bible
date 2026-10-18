"""Trace which fixture paths the self-test actually passes to each case."""
import importlib.util, subprocess, sys
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "dependency_freeze", "/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

real_run = subprocess.run
calls = []
def traced(cmd, **kw):
    calls.append(cmd)
    return real_run(cmd, **kw)
mod.subprocess.run = traced

base = Path("/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures") / mod.SELF_TEST_BASE
import tempfile
with tempfile.TemporaryDirectory(prefix="v16-trace-") as tmp:
    cases = mod.self_test_cases(Path(tmp), base)
    for case in mod.FROZEN_CASES:
        argv, exp = cases[case]
        print(f"{case:<24} expected_exit={exp} argv={[str(a) for a in argv()]}")
