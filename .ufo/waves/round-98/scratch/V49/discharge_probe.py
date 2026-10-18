#!/usr/bin/env python3
"""V49 discharge probe: build a scratch mirror of the delivered tool+contract+
r97 fixture (and r98), drop the tick-13 edge, run the mirror tool."""
import json, shutil, subprocess, sys, hashlib
from pathlib import Path

R = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
S = R / ".ufo/waves/round-98/scratch/V49"
M = S / "mirror"

if M.exists():
    shutil.rmtree(M)
(M / "corpus/tools").mkdir(parents=True)
(M / "corpus/fixtures").mkdir(parents=True)
shutil.copy2(R / "corpus/tools/dependency_freeze.py", M / "corpus/tools/dependency_freeze.py")
shutil.copy2(R / "corpus/tools/dependency-freeze-contract.json", M / "corpus/tools/dependency-freeze-contract.json")
for fx in ("r97-crossing-acknowledgment", "r98-clerk-filing"):
    src = R / "corpus/fixtures" / fx
    if src.is_dir():
        shutil.copytree(src, M / "corpus/fixtures" / fx)

tool = M / "corpus/tools/dependency_freeze.py"
mutated = M / "corpus/fixtures/r97-crossing-acknowledgment"
tl_path = mutated / "timeline.json"
tl = json.loads(tl_path.read_text(encoding="utf-8"))
before = None
for rec in tl:
    if rec["id"] == "acknowledgment-aru-records":
        before = list(rec["depends_on"])
        rec["depends_on"] = [d for d in rec["depends_on"] if d != "response-evin-salt-court"]
tl_path.write_text(json.dumps(tl, indent=2) + "\n", encoding="utf-8")
after = [rec["depends_on"] for rec in tl if rec["id"] == "acknowledgment-aru-records"][0]
print(f"MUTATION event=acknowledgment-aru-records before={before} after={after}")
print("MUTATED-SHA", hashlib.sha256(tl_path.read_bytes()).hexdigest())

for label, fixture in (("mutated-r97", mutated), ("intact-r97", M / "corpus/fixtures/r97-crossing-acknowledgment")):
    pass  # intact copy is mutated in place; run mutated first, then restore below

# run mutated
r = subprocess.run([sys.executable, str(tool), str(mutated)], cwd=M, capture_output=True, text=True)
print(f"=== mutated r97 exit={r.returncode} ===")
print(r.stdout + r.stderr)

# restore intact from delivered bytes and run control
shutil.rmtree(mutated)
shutil.copytree(R / "corpus/fixtures/r97-crossing-acknowledgment", mutated)
r = subprocess.run([sys.executable, str(tool), str(mutated)], cwd=M, capture_output=True, text=True)
print(f"=== intact r97 exit={r.returncode} ===")
print(r.stdout + r.stderr)

# r98 edge probe: drop acknowledgment-aru-records from clerk-filing-open
m98 = M / "corpus/fixtures/r98-clerk-filing"
if m98.is_dir():
    tl2_path = m98 / "timeline.json"
    tl2 = json.loads(tl2_path.read_text(encoding="utf-8"))
    b2 = None
    for rec in tl2:
        if rec["id"] == "clerk-filing-open":
            b2 = list(rec["depends_on"])
            rec["depends_on"] = [d for d in rec["depends_on"] if d != "acknowledgment-aru-records"]
    tl2_path.write_text(json.dumps(tl2, indent=2) + "\n", encoding="utf-8")
    print(f"MUTATION98 event=clerk-filing-open before={b2} after={[rec['depends_on'] for rec in tl2 if rec['id']=='clerk-filing-open'][0]}")
    r = subprocess.run([sys.executable, str(tool), str(m98)], cwd=M, capture_output=True, text=True)
    print(f"=== mutated r98 exit={r.returncode} ===")
    print(r.stdout + r.stderr)
