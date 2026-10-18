#!/bin/bash
# V35 round-98 L1 pre-closure checklist battery. Run from repo root.
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin
OUT=.ufo/waves/round-98/scratch/V35/battery-out
mkdir -p "$OUT"
run() { name=$1; shift; "$@" > "$OUT/$name.txt" 2>&1; rc=$?; echo "$name exit=$rc"; }

echo "== A. C1 calibration: dependency_freeze =="
run c1-selftest python3 corpus/tools/dependency_freeze.py --self-test
tail -3 "$OUT/c1-selftest.txt"
run c1-r88 python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
run c1-r94 python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
run c1-r95 python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
run c1-r96 python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
run c1-r97 python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
run c1-r98 python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing

echo "== B. C2 coverage: six-fixture chain + V46 discharge =="
run c2-map-r98 python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
run c2-support-r98 python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing

echo "== C. C3 depth: r98 fixture =="
run c3-check-bible-r98 python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
run c3-check-bible-r97 python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
run c3-map-r97 python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
run c3-map-r95 python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath

echo "== D. other gates (regression surface) =="
run d-map-selftest python3 corpus/tools/map_obligations.py --self-test
run d-map-frozen python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
run d-boundary python3 corpus/tools/boundary_doc_check.py
run d-boundary-selftest python3 corpus/tools/boundary_doc_check.py --self-test
run d-discriminate python3 corpus/tools/discriminate_check.py
run d-discriminate-hist python3 corpus/tools/discriminate_check.py --checker e97613c

echo "== E. census =="
python3 - <<'EOF' > "$OUT/census.txt" 2>&1
import subprocess
from pathlib import Path
root = Path(".")
dirs = sorted(d for d in (root/"corpus/fixtures").iterdir() if d.is_dir() and (d/"entities.json").exists())
clean = neg = other = lines = 0
bad = []
for d in dirs:
    r = subprocess.run(["python3", "corpus/fixtures/check_bible.py", str(d)], capture_output=True, text=True)
    if r.returncode == 0: clean += 1
    elif r.returncode == 1: neg += 1
    else: other += 1; bad.append(str(d))
    lines += sum(1 for l in r.stdout.splitlines() if l.startswith("VIOLATION:"))
print(f"CENSUS dirs={len(dirs)} clean={clean} negative={neg} other={other} violation_lines={lines}")
if bad: print("OTHER_DIRS:", bad)
EOF
echo "census: $(cat "$OUT/census.txt")"

echo "== F. git surface =="
git status --porcelain > "$OUT/git-status.txt" 2>&1
git log --oneline -1 >> "$OUT/git-status.txt" 2>&1
wc -l "$OUT/git-status.txt"
echo done
