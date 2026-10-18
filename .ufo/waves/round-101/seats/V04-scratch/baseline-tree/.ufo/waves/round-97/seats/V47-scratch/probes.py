#!/usr/bin/env python3
"""V47 independent probes: freeze hardening + C1 before/after loader ratio."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
S = ROOT / ".ufo/waves/round-97/seats/V47-scratch"


def run(args, cwd=ROOT):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def fresh(d):
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    return d


print("== A: foreign-path same-named copy ==")
foreign = fresh(S / "probeA/foreign") / "r94-paired-crossing"
shutil.copytree(ROOT / "corpus/fixtures/r94-paired-crossing", foreign)
rc, so, se = run(["python3", "corpus/tools/dependency_freeze.py", str(foreign)])
print("exit=", rc)
print(so or se)

print("\n== B: --freeze outside corpus/fixtures (scope guard) ==")
target = fresh(S / "probeB/target")
contract_before = sha(ROOT / "corpus/tools/dependency-freeze-contract.json")
rc, so, se = run(["python3", "corpus/tools/dependency_freeze.py", "--freeze", str(target)])
print("exit=", rc)
print(so or se)
print("contract unchanged:", contract_before == sha(ROOT / "corpus/tools/dependency-freeze-contract.json"))

print("\n== C: mirror-root DIGEST-MISMATCH naming ==")
mirror = fresh(S / "probeC/mirror")
(mirror / "corpus/tools").mkdir(parents=True)
shutil.copy2(ROOT / "corpus/tools/dependency_freeze.py", mirror / "corpus/tools/")
shutil.copy2(ROOT / "corpus/tools/dependency-freeze-contract.json", mirror / "corpus/tools/")
shutil.copytree(ROOT / "corpus/fixtures/r94-paired-crossing", mirror / "corpus/fixtures/r94-paired-crossing")
tl = mirror / "corpus/fixtures/r94-paired-crossing/timeline.json"
d = json.loads(tl.read_text())
d[0]["description"] = d[0]["description"] + " [prose drift]"
tl.write_text(json.dumps(d, indent=2) + "\n")
rc, so, se = run(["python3", str(mirror / "corpus/tools/dependency_freeze.py"),
                  "corpus/fixtures/r94-paired-crossing"], cwd=mirror)
print("exit=", rc)
print(so or se)

print("\n== D: C1 loader before/after (23-case contract) ==")
probe = fresh(S / "probeD")
base = json.loads((ROOT / "corpus/tools/map-obligations-contract.json").read_text())
cases = base["self_test"]["cases"]
kept = [c for c in cases if c["id"] not in ("schema_drift", "dual_pointer")]
print("kept cases:", len(kept))
base["self_test"]["cases"] = kept
(probe / "map-obligations-contract.json").write_text(json.dumps(base, indent=2))
subprocess.run(["git", "show", "f3e09f9:corpus/tools/map_obligations.py"],
               cwd=ROOT, stdout=open(probe / "map_obligations_r96.py", "w"))
rc, so, se = run(["python3", str(probe / "map_obligations_r96.py"), "--self-test"])
print("r96 tool + 23-case contract: exit=", rc)
print("\n".join(l for l in so.splitlines() if l.startswith(("SELF-TEST CASES", "RESULT"))) or se)

delivered = fresh(S / "probeD2")
delivered.mkdir(exist_ok=True)
shutil.copy2(probe / "map-obligations-contract.json", delivered / "map-obligations-contract.json")
shutil.copy2(ROOT / "corpus/tools/map_obligations.py", delivered / "map_obligations.py")
rc, so, se = run(["python3", str(delivered / "map_obligations.py"), "--self-test"])
print("delivered tool + 23-case contract: exit=", rc)
print(so or se)

print("\n== E: self-test case counts ==")
for tool, name in [("map_obligations.py", "map"), ("dependency_freeze.py", "freeze")]:
    rc, so, se = run(["python3", f"corpus/tools/{tool}", "--self-test"])
    n_case = sum(1 for l in so.splitlines() if l.startswith(("CASE ", "SELF-TEST PASS")))
    print(f"{name}: exit={rc} case-lines={n_case} result={[l for l in so.splitlines() if l.startswith(('SELF-TEST ', 'RESULT'))]}")

print("\n== strays check ==")
rc, so, se = run(["bash", "-lc", "ls -d corpus/fixtures/dependency-freeze-self-test-* corpus/fixtures/map-obligations-self-test-* 2>/dev/null | wc -l"])
print("stray self-test dirs:", so)
