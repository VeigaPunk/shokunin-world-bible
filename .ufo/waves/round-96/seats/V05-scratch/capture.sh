#!/bin/bash
# V05 capture harness. Usage: capture.sh <outdir>
set -u
OUT="$1"
mkdir -p "$OUT"
cd /home/vgpnk/Projects/shokunin/lore-shokunin

run_map() {
  local name="$1"; shift
  python3 corpus/tools/map_obligations.py "$@" > "$OUT/$name.out" 2>&1
  local code=$?
  echo "EXIT=$code" >> "$OUT/$name.out"
}

run_map map-r87 corpus/fixtures/r87-myth-cluster
run_map map-r88 corpus/fixtures/r88-m3-maya-cluster
run_map map-r89 corpus/fixtures/r89-inspiration-paraphrase
run_map map-r93 corpus/fixtures/r93-m2-kojiki-cluster
run_map map-r94 corpus/fixtures/r94-paired-crossing
run_map map-r95 corpus/fixtures/r95-crossing-aftermath
run_map map-r96 corpus/fixtures/r96-crossing-response
run_map map-frozen --frozen .ufo/waves/round-94/frozen/map-obligations-r93
run_map map-usage-noargs
run_map map-usage-missing corpus/fixtures/does-not-exist-r96
run_map map-usage-bogus --bogus-flag corpus/fixtures/r94-paired-crossing
run_map map-selftest --self-test

for f in r87-myth-cluster r88-m3-maya-cluster r93-m2-kojiki-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
  python3 corpus/tools/support_check.py "corpus/fixtures/$f" > "$OUT/support-$f.out" 2>&1
  echo "EXIT=$?" >> "$OUT/support-$f.out"
done

sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/support_check.py > "$OUT/tool-shas.txt"
( cd "$OUT" && sha256sum *.out > manifest.txt )
echo "CAPTURE DONE -> $OUT"
