#!/bin/bash
# V35 adjudicator closure battery — run from repo root on the final revision.
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin
OUT=.ufo/waves/round-97/seats/V35-scratch/battery-out
mkdir -p "$OUT"
run() { name=$1; shift; "$@" > "$OUT/$name.txt" 2>&1; echo "$name exit=$?"; }

echo "== C1 map_obligations =="
run c1-selftest python3 corpus/tools/map_obligations.py --self-test
run c1-r97 python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
run c1-r96 python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
run c1-r95 python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
run c1-r94 python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
run c1-r88 python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster
run c1-r93 python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster
run c1-r87-failclosed python3 corpus/tools/map_obligations.py corpus/fixtures/r87-myth-cluster
run c1-r89-failclosed python3 corpus/tools/map_obligations.py corpus/fixtures/r89-inspiration-paraphrase
run c1-frozen-r93 python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93

echo "== C2 dependency_freeze =="
run c2-selftest python3 corpus/tools/dependency_freeze.py --self-test
for fx in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
  run c2-chain-$fx python3 corpus/tools/dependency_freeze.py corpus/fixtures/$fx
done

echo "== C3 depth =="
run c3-check-bible python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
run c3-support python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment

echo "== other gates =="
run gate-boundary python3 corpus/tools/boundary_doc_check.py
run gate-boundary-selftest python3 corpus/tools/boundary_doc_check.py --self-test
run gate-discriminate python3 corpus/tools/discriminate_check.py
run gate-discriminate-hist python3 corpus/tools/discriminate_check.py --checker e97613c

echo "== census =="
python3 - <<'EOF' > "$OUT/census.txt" 2>&1
import subprocess
from pathlib import Path
root = Path(".")
dirs = sorted(d for d in (root/"corpus/fixtures").iterdir() if d.is_dir() and (d/"entities.json").exists())
clean = neg = other = lines = 0
for d in dirs:
    r = subprocess.run(["python3", "corpus/fixtures/check_bible.py", str(d)], capture_output=True, text=True)
    if r.returncode == 0: clean += 1
    elif r.returncode == 1: neg += 1
    else: other += 1
    lines += sum(1 for l in r.stdout.splitlines() if l.startswith("VIOLATION:"))
print(f"CENSUS dirs={len(dirs)} clean={clean} negative={neg} other={other} violation_lines={lines}")
EOF
echo "census: $(cat "$OUT/census.txt")"

echo "== pins =="
run pins-check-bible sha256sum corpus/fixtures/check_bible.py
echo "== git surface =="
git status --porcelain > "$OUT/git-status.txt" 2>&1
git diff --stat HEAD >> "$OUT/git-status.txt" 2>&1
echo done
