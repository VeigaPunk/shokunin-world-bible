#!/usr/bin/env python3
"""V25 delivered-revision demos for C1 (dependency_freeze hygiene).

Usage: python3 demos.py <frozen_root> <workdir>
frozen_root = dir containing corpus/tools/{dependency_freeze.py,dependency-freeze-contract.json}
              and corpus/fixtures (symlink ok)
workdir     = scratch dir for demo copies
"""
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

FROZEN = Path(sys.argv[1]).resolve()
WORK = Path(sys.argv[2]).resolve()
TOOL = FROZEN / "corpus/tools/dependency_freeze.py"
CONTRACT = FROZEN / "corpus/tools/dependency-freeze-contract.json"
BASELINE = Path(__file__).resolve().parent / "baseline/corpus/tools"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def run(argv, cwd=None):
    r = subprocess.run([sys.executable, *argv], capture_output=True, text=True, cwd=cwd)
    return r.returncode, r.stdout, r.stderr


def fresh(name):
    d = WORK / name
    if d.exists():
        shutil.rmtree(d)
    (d / "corpus/tools").mkdir(parents=True)
    (d / "corpus/fixtures").mkdir(parents=True)
    shutil.copy2(TOOL, d / "corpus/tools/dependency_freeze.py")
    shutil.copy2(CONTRACT, d / "corpus/tools/dependency-freeze-contract.json")
    shutil.copytree(FROZEN / "corpus/fixtures/r95-crossing-aftermath",
                    d / "corpus/fixtures/r95-crossing-aftermath")
    return d


def contract(d):
    return json.loads((d / "corpus/tools/dependency-freeze-contract.json").read_text())


def save_contract(d, c):
    (d / "corpus/tools/dependency-freeze-contract.json").write_text(
        json.dumps(c, indent=2, ensure_ascii=False) + "\n")


print(f"FROZEN tool sha256={sha(TOOL)}")
print(f"FROZEN contract sha256={sha(CONTRACT)}")

# --- section A: persisted case set + contract expectations delta ---
src = TOOL.read_text()
m = re.search(r"FROZEN_CASES = \((.*?)\)", src, re.S)
delivered_cases = re.findall(r'"([a-z_]+)"', m.group(1))
bsrc = (BASELINE / "dependency_freeze.py").read_text()
bm = re.search(r"FROZEN_CASES = \((.*?)\)", bsrc, re.S)
baseline_cases = re.findall(r'"([a-z_]+)"', bm.group(1))
print(f"\nA delivered FROZEN_CASES n={len(delivered_cases)} added={sorted(set(delivered_cases)-set(baseline_cases))} "
      f"removed={sorted(set(baseline_cases)-set(delivered_cases))}")
dc = contract(FROZEN)
bc = json.loads((BASELINE / "dependency-freeze-contract.json").read_text())
dexp, bexp = dc.get("self_test", {}).get("expected", {}), bc["self_test"]["expected"]
print(f"A contract expected n={len(dexp)} added={sorted(set(dexp)-set(bexp))} removed={sorted(set(bexp)-set(dexp))}")
shared_changed = sorted(k for k in set(dexp) & set(bexp) if dexp[k] != bexp[k])
print(f"A inherited expected entries changed vs baseline: {shared_changed}")

# --- section B: delivered --self-test on frozen root ---
code, out, err = run([str(TOOL), "--self-test"], cwd=FROZEN)
print(f"\nB frozen --self-test exit={code}")
tail = [l for l in out.splitlines() if l.startswith("SELF-TEST") or l.startswith("RESULT") or l.startswith("FINDING")]
print("B tail:", tail)
open(WORK / "selftest-frozen.txt", "w").write(out)

# --- section C: tampered-expectation mirror => SELF-TEST-MISMATCH exit 2 ---
d = fresh("demo-mismatch")
c = contract(d)
c["self_test"]["expected"]["clean"]["exit"] = 1
save_contract(d, c)
code, out, err = run([str(d / "corpus/tools/dependency_freeze.py"), "--self-test"], cwd=d)
lines = [l for l in out.splitlines() if "MISMATCH" in l or l.startswith("SELF-TEST ") or l.startswith("FINDING") or l.startswith("RESULT")]
print(f"\nC tampered-expectation --self-test exit={code}")
for l in lines:
    print("C ", l)
print("C traceback in output:", "Traceback" in (out + err))

# --- section D: legacy path-less pin migrated by --freeze ---
d = fresh("demo-legacy")
c = contract(d)
del c["pins"]["r95-crossing-aftermath"]["fixture"]
save_contract(d, c)
code, out, err = run([str(d / "corpus/tools/dependency_freeze.py"), "--freeze", "corpus/fixtures/r95-crossing-aftermath"], cwd=d)
print(f"\nD path-less pin --freeze exit={code}")
print("D out:", out.strip().splitlines())
after = contract(d)
print("D pin fixture after:", repr(after["pins"]["r95-crossing-aftermath"].get("fixture")))

# --- section E: path-bearing pin still guarded (same-named copy elsewhere) ---
d = fresh("demo-guard")
alt = d / "corpus/fixtures/elsewhere/r95-crossing-aftermath"
shutil.copytree(d / "corpus/fixtures/r95-crossing-aftermath", alt)
code, out, err = run([str(d / "corpus/tools/dependency_freeze.py"), "--freeze", "corpus/fixtures/elsewhere/r95-crossing-aftermath"], cwd=d)
print(f"\nE path-bearing pin, same-named copy elsewhere --freeze exit={code}")
print("E out:", out.strip().splitlines())

# --- section F: precedence text ---
print("\nF baseline precedence:", repr(bc.get("precedence")))
print("F delivered precedence:", repr(dc.get("precedence")))

# --- section G: inherited-16 executed comparison (delivered case rows vs baseline rows) ---
def case_rows(text):
    rows = {}
    for l in text.splitlines():
        mm = re.match(r"CASE (\w+): exit=(\d+) expected=(\d+) findings=(\[.*\]) (ok|MISMATCH)", l)
        if mm:
            rows[mm.group(1)] = (int(mm.group(2)), mm.group(3), mm.group(4), mm.group(5))
    return rows


drows = case_rows((WORK / "selftest-frozen.txt").read_text())  # section B run, saved
bout = (Path(__file__).resolve().parent / "baseline/selftest-out.txt").read_text()
brows = case_rows(bout)
diff = {k: (brows.get(k), drows.get(k)) for k in sorted(set(brows) | set(drows)) if brows.get(k) != drows.get(k)}
print(f"\nG per-case rows baseline n={len(brows)} delivered n={len(drows)} differing={json.dumps(diff)}")
