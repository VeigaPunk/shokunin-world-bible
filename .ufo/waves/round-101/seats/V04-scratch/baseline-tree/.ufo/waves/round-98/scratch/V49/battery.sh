#!/bin/bash
# V49 final coverage battery — run only after S1's contract pins r97+r98 land.
set -u
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-98/scratch/V49
cd "$R" || exit 1

echo "== revisions =="
sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/fixtures/r97-crossing-acknowledgment/timeline.json corpus/fixtures/r98-clerk-filing/timeline.json
git rev-parse HEAD

echo
echo "== chain 6/6 (delivered tool, delivered fixtures) =="
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
  echo "--- $f ---"
  python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f
  echo "exit=$?"
done

echo
echo "== independent recompute of all pins =="
python3 "$S/recompute.py" "$R"
echo "recompute-exit=$?"

echo
echo "== mirror reproducibility: delivered pins == guarded --freeze on identical copies =="
rm -rf "$S/mirror2"
mkdir -p "$S/mirror2/corpus/tools" "$S/mirror2/corpus/fixtures"
cp corpus/tools/dependency_freeze.py "$S/mirror2/corpus/tools/"
cp corpus/tools/dependency-freeze-contract.json "$S/mirror2/corpus/tools/"
for fx in r97-crossing-acknowledgment r98-clerk-filing; do cp -r corpus/fixtures/$fx "$S/mirror2/corpus/fixtures/"; done
python3 "$S/mirror2/corpus/tools/dependency_freeze.py" --freeze "$S/mirror2/corpus/fixtures/r97-crossing-acknowledgment"; echo "mirror-freeze-r97-exit=$?"
python3 "$S/mirror2/corpus/tools/dependency_freeze.py" --freeze "$S/mirror2/corpus/fixtures/r98-clerk-filing"; echo "mirror-freeze-r98-exit=$?"
python3 - "$R" "$S" <<'PY'
import json, sys
R, S = sys.argv[1], sys.argv[2]
d = json.load(open(f"{R}/corpus/tools/dependency-freeze-contract.json"))["pins"]
m = json.load(open(f"{S}/mirror2/corpus/tools/dependency-freeze-contract.json"))["pins"]
for k in ("r97-crossing-acknowledgment", "r98-clerk-filing"):
    same = d[k] == m[k]
    print(f"PIN-REPRODUCIBILITY {k}: {'EXACT-MATCH' if same else 'DIFF'}")
    if not same:
        for f in sorted(set(d[k]) | set(m[k])):
            if d[k].get(f) != m[k].get(f):
                print("  field", f, "delivered:", str(d[k].get(f))[:120], "mirror:", str(m[k].get(f))[:120])
PY

echo
echo "== discharge probe: tick-13 edge drop under the delivered pins (mirror2) =="
python3 - <<'PY'
import json, hashlib, subprocess, sys, shutil
from pathlib import Path
R = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
S = R / ".ufo/waves/round-98/scratch/V49"
M = S / "mirror2"
fx = M / "corpus/fixtures/r97-crossing-acknowledgment"
p = fx / "timeline.json"
tl = json.loads(p.read_text())
for r in tl:
    if r["id"] == "acknowledgment-aru-records":
        r["depends_on"] = [d for d in r["depends_on"] if d != "response-evin-salt-court"]
p.write_text(json.dumps(tl, indent=2) + "\n")
print("mutated r97 timeline sha256:", hashlib.sha256(p.read_bytes()).hexdigest())
r = subprocess.run([sys.executable, str(M / "corpus/tools/dependency_freeze.py"), str(fx)], capture_output=True, text=True)
print(f"exit={r.returncode}"); print(r.stdout + r.stderr)
PY

echo
echo "== discharge probe: r98 tick-14 edge drop under the delivered pins (mirror2) =="
python3 - <<'PY'
import json, hashlib, subprocess, sys
from pathlib import Path
R = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
S = R / ".ufo/waves/round-98/scratch/V49"
M = S / "mirror2"
fx = M / "corpus/fixtures/r98-clerk-filing"
p = fx / "timeline.json"
tl = json.loads(p.read_text())
for r in tl:
    if r["id"] == "clerk-filing-open":
        r["depends_on"] = [d for d in r["depends_on"] if d != "acknowledgment-aru-records"]
p.write_text(json.dumps(tl, indent=2) + "\n")
print("mutated r98 timeline sha256:", hashlib.sha256(p.read_bytes()).hexdigest())
r = subprocess.run([sys.executable, str(M / "corpus/tools/dependency_freeze.py"), str(fx)], capture_output=True, text=True)
print(f"exit={r.returncode}"); print(r.stdout + r.stderr)
PY

echo
echo "== stray check (working tree vs HEAD dd4df1b) =="
git status --porcelain
