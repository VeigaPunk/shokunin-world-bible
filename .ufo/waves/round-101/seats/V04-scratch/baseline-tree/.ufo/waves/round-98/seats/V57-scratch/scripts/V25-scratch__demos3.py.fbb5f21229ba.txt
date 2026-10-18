#!/usr/bin/env python3
"""V25 final comparisons: K1 untampered baseline rows, K2 contract inherited-pin equality,
K3 expectation-drop fail-closed, K4 path-less verify fail-closed, K5 body-diff, K6 stray stat."""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

SCRATCH = Path(__file__).resolve().parent
FROZEN = (SCRATCH / "frozen-r98").resolve()
WORK = SCRATCH / "work"
BASELINE = SCRATCH / "baseline"
TOOL = FROZEN / "corpus/tools/dependency_freeze.py"
CONTRACT = FROZEN / "corpus/tools/dependency-freeze-contract.json"


def run(argv, cwd=None):
    r = subprocess.run([sys.executable, *argv], capture_output=True, text=True, cwd=cwd)
    return r.returncode, r.stdout, r.stderr


def case_rows(text):
    rows = {}
    for l in text.splitlines():
        mm = re.match(r"CASE (\w+): exit=(\d+) expected=(\d+) findings=(\[.*\]) (ok|MISMATCH)", l)
        if mm:
            rows[mm.group(1)] = (int(mm.group(2)), mm.group(3), mm.group(4), mm.group(5))
    return rows


# K1: untampered baseline self-test in a fresh mirror
d = WORK / "baseline-clean"
if d.exists():
    shutil.rmtree(d)
(d / "corpus/tools").mkdir(parents=True)
(d / "corpus/fixtures").mkdir(parents=True)
shutil.copy2(BASELINE / "corpus/tools/dependency_freeze.py", d / "corpus/tools/dependency_freeze.py")
shutil.copy2(BASELINE / "corpus/tools/dependency-freeze-contract.json", d / "corpus/tools/dependency-freeze-contract.json")
shutil.copytree(FROZEN / "corpus/fixtures/r95-crossing-aftermath", d / "corpus/fixtures/r95-crossing-aftermath")
code, out, err = run([str(d / "corpus/tools/dependency_freeze.py"), "--self-test"], cwd=d)
(SCRATCH / "baseline" / "selftest-out-clean.txt").write_text(out)
brows = case_rows(out)
drows = case_rows((WORK / "selftest-frozen.txt").read_text())
diff = {k: (brows.get(k), drows.get(k)) for k in sorted(set(brows) | set(drows)) if brows.get(k) != drows.get(k)}
print(f"K1 untampered baseline --self-test exit={code} rows={len(brows)}; delivered rows={len(drows)}; differing={json.dumps(diff)}")
print(f"K1 baseline tail: {[l for l in out.splitlines() if l.startswith('SELF-TEST') or l.startswith('RESULT')]}")

# K2: contract equality for inherited pins + sections
bc = json.loads((BASELINE / "corpus/tools/dependency-freeze-contract.json").read_text())
dc = json.loads(CONTRACT.read_text())
for name in sorted(bc["pins"]):
    same = bc["pins"][name] == dc["pins"].get(name)
    print(f"K2 inherited pin {name} identical={same}")
print(f"K2 exit_codes equal: {bc['exit_codes'] == dc['exit_codes']}")
print(f"K2 self_test.base_fixture equal: {bc['self_test']['base_fixture'] == dc['self_test']['base_fixture']}")
print(f"K2 scope equal: {bc['scope'] == dc['scope']}")
print(f"K2 data_files/required_files equal: {bc['data_files'] == dc['data_files'] and bc['required_files'] == dc['required_files']}")
print(f"K2 pins added={sorted(set(dc['pins']) - set(bc['pins']))} removed={sorted(set(bc['pins']) - set(dc['pins']))}")
print(f"K2 top-level keys added={sorted(set(dc) - set(bc))} removed={sorted(set(bc) - set(dc))}")

# K3: drop the self_test_mismatch expectation -> fail closed
d = WORK / "demo-drop-expectation"
if d.exists():
    shutil.rmtree(d)
(d / "corpus/tools").mkdir(parents=True)
(d / "corpus/fixtures").mkdir(parents=True)
shutil.copy2(TOOL, d / "corpus/tools/dependency_freeze.py")
c = json.loads(CONTRACT.read_text())
del c["self_test"]["expected"]["self_test_mismatch"]
(d / "corpus/tools/dependency-freeze-contract.json").write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\n")
shutil.copytree(FROZEN / "corpus/fixtures/r95-crossing-aftermath", d / "corpus/fixtures/r95-crossing-aftermath")
code, out, err = run([str(d / "corpus/tools/dependency_freeze.py"), "--self-test"], cwd=d)
print(f"K3 dropped expectation --self-test exit={code} out={out.strip().splitlines()}")

# K4: verify on a path-less pin (delivered tool) -> fail closed CONTRACT-INVALID
d = WORK / "demo-verify-legacy"
if d.exists():
    shutil.rmtree(d)
(d / "corpus/tools").mkdir(parents=True)
(d / "corpus/fixtures").mkdir(parents=True)
shutil.copy2(TOOL, d / "corpus/tools/dependency_freeze.py")
c = json.loads(CONTRACT.read_text())
del c["pins"]["r95-crossing-aftermath"]["fixture"]
(d / "corpus/tools/dependency-freeze-contract.json").write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\n")
shutil.copytree(FROZEN / "corpus/fixtures/r95-crossing-aftermath", d / "corpus/fixtures/r95-crossing-aftermath")
code, out, err = run([str(d / "corpus/tools/dependency_freeze.py"), "corpus/fixtures/r95-crossing-aftermath"], cwd=d)
print(f"K4 path-less verify exit={code} out={out.strip().splitlines()}")

# K5: self_test_cases body diff (baseline vs delivered)
bsrc = (BASELINE / "corpus/tools/dependency_freeze.py").read_text()
dsrc = TOOL.read_text()
bstart, bend = bsrc.index("def self_test_cases("), bsrc.index("def run_self_test(")
dstart, dend = dsrc.index("def self_test_cases("), dsrc.index("def run_self_test(")
bbody, dbody = bsrc[bstart:bend], dsrc[dstart:dend]
print(f"K5 baseline body lines={bbody.count(chr(10))} delivered body lines={dbody.count(chr(10))}")
print(f"K5 delivered body startswith baseline body: {dbody.startswith(bbody.rstrip(chr(10)))}")
added = dbody[len(bbody.rstrip(chr(10))):]
print(f"K5 appended block lines={added.count(chr(10))}; starts with: {added.strip().splitlines()[0][:80] if added.strip() else '(none)'}")

# K6: parent stray stat (read-only)
p = Path("/home/vgpnk/Projects/shokunin/baseline-analyze.txt")
if p.exists():
    st = p.stat()
    print(f"K6 parent stray exists: size={st.st_size} mtime={st.st_mtime}")
else:
    print("K6 parent stray absent")
