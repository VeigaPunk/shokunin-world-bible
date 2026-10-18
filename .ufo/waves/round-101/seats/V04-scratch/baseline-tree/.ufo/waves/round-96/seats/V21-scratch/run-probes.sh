#!/usr/bin/env bash
# V21 c3-fail-closed probe harness. Run from lane repo root.
# Basename-pinned design: pin lookup uses the fixture dir's basename, so
# cases needing a pinned lookup use a dir named exactly r94-paired-crossing.
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
TOOL=corpus/tools/dependency_freeze.py
SC=.ufo/waves/round-96/seats/V21-scratch
CASES=$SC/cases

rm -rf "$CASES"; mkdir -p "$CASES"

# malformed timeline, pinned basename
mkdir -p "$CASES/malformed-tl"
cp -r corpus/fixtures/r94-paired-crossing "$CASES/malformed-tl/r94-paired-crossing"
printf '[{"id": "aru-ninth-bell", "tick": 9,' > "$CASES/malformed-tl/r94-paired-crossing/timeline.json"

# missing timeline file, pinned basename
mkdir -p "$CASES/no-timeline"
cp -r corpus/fixtures/r94-paired-crossing "$CASES/no-timeline/r94-paired-crossing"
rm "$CASES/no-timeline/r94-paired-crossing/timeline.json"

# digest-only tamper (valid JSON, unmodeled content change), pinned basename
mkdir -p "$CASES/digest-tamper"
cp -r corpus/fixtures/r94-paired-crossing "$CASES/digest-tamper/r94-paired-crossing"
python3 - "$CASES/digest-tamper/r94-paired-crossing/timeline.json" <<'EOF'
import sys
p = sys.argv[1]
t = open(p, encoding="utf-8").read()
open(p, "w", encoding="utf-8").write(t.replace("south bell at Salt Court", "South bell at Salt Court", 1))
EOF

# missing dir with a pinned basename: $CASES/missing-dir/r94-paired-crossing (not created)

run() {
  label="$1"; shift
  echo "### $label"
  echo "\$ $*"
  out=$("$@" 2>&1); rc=$?
  echo "$out"
  echo "[exit=$rc]"
  echo
}

echo "=== V21 fail-closed sweep $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
echo "tool sha256: $(sha256sum $TOOL | cut -d' ' -f1)"
echo "contract sha256: $(sha256sum corpus/tools/dependency-freeze-contract.json | cut -d' ' -f1)"
echo

# P0 positive controls
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
  run "P0 positive control $f" python3 "$TOOL" "corpus/fixtures/$f"
done

# P1 unpinned fixture dir (exists, has timeline.json, not in chain)
run "P1 unpinned r93-m2-kojiki-cluster" python3 "$TOOL" corpus/fixtures/r93-m2-kojiki-cluster

# P2 malformed timeline JSON (pinned basename, corrupted bytes)
run "P2 malformed timeline" python3 "$TOOL" "$CASES/malformed-tl/r94-paired-crossing"

# P3 missing fixture dir (pinned basename, nonexistent path)
run "P3a missing dir pinned-name" python3 "$TOOL" "$CASES/missing-dir/r94-paired-crossing"
run "P3b missing dir unpinned-name" python3 "$TOOL" corpus/fixtures/does-not-exist-r96

# P4 usage errors
run "P4a no args" python3 "$TOOL"
run "P4b unknown flag" python3 "$TOOL" --bogus corpus/fixtures/r94-paired-crossing
run "P4c freeze without dir" python3 "$TOOL" --freeze
run "P4d two dirs" python3 "$TOOL" corpus/fixtures/r94-paired-crossing corpus/fixtures/r95-crossing-aftermath
run "P4e self-test plus fixture" python3 "$TOOL" --self-test corpus/fixtures/r94-paired-crossing
run "P4f freeze plus fixture" python3 "$TOOL" corpus/fixtures/r94-paired-crossing --freeze corpus/fixtures/r94-paired-crossing

# P5 non-chain fixture with no pins
run "P5a non-chain consistent" python3 "$TOOL" corpus/fixtures/consistent
run "P5b non-chain item-chain-valid" python3 "$TOOL" corpus/fixtures/item-chain-valid

# E1 extra: missing timeline file under a pinned basename
run "E1 missing timeline file" python3 "$TOOL" "$CASES/no-timeline/r94-paired-crossing"
# E2 extra: unmodeled content change (digest mismatch)
run "E2 digest-only tamper" python3 "$TOOL" "$CASES/digest-tamper/r94-paired-crossing"

echo "=== post-sweep contract sha256: $(sha256sum corpus/tools/dependency-freeze-contract.json | cut -d' ' -f1) ==="
