#!/bin/bash
# V45 after-state demo battery — runs ONLY after R3's hardened tool is on disk.
# All writes confined to V45-scratch. Real-tree access is read-only (verify/self-test).
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$REPO/.ufo/waves/round-97/seats/V45-scratch
cd "$REPO" || exit 9
LOG=$S/demos-after.log
: > "$LOG"
say() { echo "$@" | tee -a "$LOG"; }
run() { say "\$ $*"; "$@" >>"$LOG" 2>&1; code=$?; say "exit=$code"; return $code; }

say "== V45 after-state battery $(date +%H:%M:%S) =="
say "tool sha256: $(sha256sum corpus/tools/dependency_freeze.py)"
say "contract sha256 BEFORE: $(sha256sum corpus/tools/dependency-freeze-contract.json)"

say "-- A2 controls: real pinned paths must stay PASS --"
run python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
run python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster

say "-- A1 PATH-MISMATCH: byte-identical shadow copies at foreign paths --"
diff -r corpus/fixtures/r96-crossing-response "$S/shadow/r96-crossing-response" >>"$LOG" 2>&1 && say "shadow r96 byte-identical: yes"
diff -r corpus/fixtures/r88-m3-maya-cluster "$S/shadow/r88-m3-maya-cluster" >>"$LOG" 2>&1 && say "shadow r88 byte-identical: yes"
run python3 corpus/tools/dependency_freeze.py "$S/shadow/r96-crossing-response"
run python3 corpus/tools/dependency_freeze.py "$S/shadow/r88-m3-maya-cluster"

say "-- A7 order probe: tampered foreign copy (reindent sources.json, parsed-equal) --"
python3 - <<'PY' >>"$LOG" 2>&1
import json, pathlib
p = pathlib.Path('/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V45-scratch/shadow-tampered/r96-crossing-response/sources.json')
d = json.loads(p.read_text()); p.write_text(json.dumps(d, indent=4) + "\n")
print("reindented, parsed-equal:", json.loads(p.read_text()) == d)
PY
run python3 corpus/tools/dependency_freeze.py "$S/shadow-tampered/r96-crossing-response"

say "-- A6 symlinks (resolve semantics) --"
run python3 corpus/tools/dependency_freeze.py "$S/symlink-real-r96"
run python3 corpus/tools/dependency_freeze.py "$S/symlink-foreign-r96"

say "-- A8 renamed copy at foreign path (name not pinned) --"
run python3 corpus/tools/dependency_freeze.py "$S/shadow/r96-crossing-response-renamed"

say "-- A3 scope guard: --freeze foreign paths must be rejected with NO contract write --"
run python3 corpus/tools/dependency_freeze.py --freeze "$S/shadow/r96-crossing-response"
run python3 corpus/tools/dependency_freeze.py --freeze "$S/shadow/r88-m3-maya-cluster"
say "contract sha256 AFTER freeze-rejects: $(sha256sum corpus/tools/dependency-freeze-contract.json)"

say "-- self-test (TMPDIR redirected: /tmp inodes exhausted) --"
TMPDIR=$S/tmp python3 corpus/tools/dependency_freeze.py --self-test >>"$LOG" 2>&1
say "self-test exit=$?"

say "-- chain 4/4 --"
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
  run python3 corpus/tools/dependency_freeze.py "corpus/fixtures/$f"
done

say "-- A4/A5 fakerepo: freeze acceptance + DIGEST-MISMATCH naming (writes only under scratch) --"
FR=$S/fakerepo-new
rm -rf "$FR"
mkdir -p "$FR/corpus/tools" "$FR/corpus/fixtures" "$FR/elsewhere"
cp corpus/tools/dependency_freeze.py "$FR/corpus/tools/dependency_freeze.py"
cp corpus/tools/dependency-freeze-contract.json "$FR/corpus/tools/dependency-freeze-contract.json"
cp -a corpus/fixtures/r95-crossing-aftermath "$FR/corpus/fixtures/"
cp -a corpus/fixtures/r95-crossing-aftermath "$FR/elsewhere/"
say "\$ python3 \$FR/corpus/tools/dependency_freeze.py --freeze \$FR/corpus/fixtures/r95-crossing-aftermath"
python3 "$FR/corpus/tools/dependency_freeze.py" --freeze "$FR/corpus/fixtures/r95-crossing-aftermath" >>"$LOG" 2>&1
say "exit=$? (freeze acceptance in-scope)"
python3 - <<'PY' >>"$LOG" 2>&1
import json, pathlib
p = pathlib.Path('/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V45-scratch/fakerepo-new/corpus/fixtures/r95-crossing-aftermath/sources.json')
d = json.loads(p.read_text()); p.write_text(json.dumps(d, indent=4) + "\n")
print("fakerepo sources.json reindented, parsed-equal:", json.loads(p.read_text()) == d)
PY
say "\$ verify fakerepo fixture after single-file byte change"
python3 "$FR/corpus/tools/dependency_freeze.py" "$FR/corpus/fixtures/r95-crossing-aftermath" >>"$LOG" 2>&1
say "exit=$? (expect 2 DIGEST-MISMATCH naming sources.json)"
say "\$ --freeze out-of-scope in fakerepo"
python3 "$FR/corpus/tools/dependency_freeze.py" --freeze "$FR/elsewhere/r95-crossing-aftermath" >>"$LOG" 2>&1
say "exit=$? (expect scope rejection)"

say "contract sha256 FINAL: $(sha256sum corpus/tools/dependency-freeze-contract.json)"
say "== battery done =="
