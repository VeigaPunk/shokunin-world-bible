#!/bin/bash
# V03 r97 battery capture. Usage: capture.sh <outdir>
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
OUT="${1:?outdir}"
cd "$REPO" || exit 9
mkdir -p "$OUT" || exit 9
run() { # run <label> <args...>
  local label="$1"; shift
  { echo "=== $label ==="; echo "\$ python3 $*"; python3 "$@" 2>&1; echo "EXIT=$?"; echo; } >> "$OUT/battery.txt"
}
: > "$OUT/battery.txt"
echo "REVISION STAMP $(date -Is)" >> "$OUT/battery.txt"
sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json \
  corpus/tools/support_check.py corpus/tools/dependency_freeze.py >> "$OUT/battery.txt"
echo >> "$OUT/battery.txt"

for f in r87-myth-cluster r88-m3-maya-cluster r89-inspiration-paraphrase r93-m2-kojiki-cluster \
         r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment; do
  run "map-$f" corpus/tools/map_obligations.py "corpus/fixtures/$f"
done

run "map-frozen-r93" corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
run "self-test" corpus/tools/map_obligations.py --self-test
run "usage-noargs" corpus/tools/map_obligations.py
run "usage-missing" corpus/tools/map_obligations.py corpus/fixtures/does-not-exist-r97
run "usage-bogus" corpus/tools/map_obligations.py --bogus-flag

for f in r87-myth-cluster r88-m3-maya-cluster r93-m2-kojiki-cluster r94-paired-crossing \
         r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment; do
  run "support-$f" corpus/tools/support_check.py "corpus/fixtures/$f"
done
echo "CAPTURE DONE $(date -Is)" >> "$OUT/battery.txt"
