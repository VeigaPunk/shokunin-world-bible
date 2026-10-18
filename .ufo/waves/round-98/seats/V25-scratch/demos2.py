#!/usr/bin/env python3
"""V25 extra probes: H tool-side reversion, I contract-side flip, J chain digests, L path-less-elsewhere bound."""
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


# --- H: tool-side reversion of the exit-2 change (pin load-bearing) ---
d = fresh("demo-revert")
t = d / "corpus/tools/dependency_freeze.py"
src = t.read_text()
old = '        emit(2, [("SELF-TEST-MISMATCH", f"cases failed: {sorted(failures)}")])\n        return 2'
new = '        emit(1, [("SELF-TEST-MISMATCH", f"cases failed: {sorted(failures)}")])\n        return 1'
assert old in src, "reversion anchor not found"
t.write_text(src.replace(old, new))
code, out, err = run([str(t), "--self-test"], cwd=d)
rows = [l for l in out.splitlines() if l.startswith("CASE self_test_mismatch") or l.startswith("SELF-TEST ") or l.startswith("FINDING") or l.startswith("RESULT")]
print(f"H tool-reverted --self-test exit={code}")
for l in rows:
    print("H ", l)

# --- I: contract-side flip of the self_test_mismatch expectation ---
d = fresh("demo-flip")
c = contract(d)
c["self_test"]["expected"]["self_test_mismatch"]["exit"] = 1
save_contract(d, c)
code, out, err = run([str(d / "corpus/tools/dependency_freeze.py"), "--self-test"], cwd=d)
rows = [l for l in out.splitlines() if l.startswith("CASE self_test_mismatch") or l.startswith("SELF-TEST ") or l.startswith("FINDING") or l.startswith("RESULT")]
print(f"\nI contract-flipped --self-test exit={code}")
for l in rows:
    print("I ", l)

# --- J: chain 6/6 with the frozen delivered tool, digests vs baseline ---
print("\nJ chain on frozen delivered tool:")
for f in ("r88-m3-maya-cluster", "r94-paired-crossing", "r95-crossing-aftermath",
          "r96-crossing-response", "r97-crossing-acknowledgment", "r98-clerk-filing"):
    code, out, err = run([str(TOOL), str(FROZEN / "corpus/fixtures" / f)], cwd=FROZEN)
    digest = re.search(r"DIGEST (\w+)", out)
    print(f"J {f} exit={code} digest={digest.group(1) if digest else '?'}")

# --- L: path-less pin + same-named copy elsewhere -> migration binds foreign path ---
d = fresh("demo-legacy-elsewhere")
alt = d / "corpus/fixtures/elsewhere/r95-crossing-aftermath"
shutil.copytree(d / "corpus/fixtures/r95-crossing-aftermath", alt)
c = contract(d)
del c["pins"]["r95-crossing-aftermath"]["fixture"]
save_contract(d, c)
code, out, err = run([str(d / "corpus/tools/dependency_freeze.py"), "--freeze", "corpus/fixtures/elsewhere/r95-crossing-aftermath"], cwd=d)
after = contract(d)
print(f"\nL path-less pin + foreign same-named copy --freeze exit={code}")
print("L out:", out.strip().splitlines())
print("L pin fixture after:", repr(after["pins"]["r95-crossing-aftermath"].get("fixture")))
