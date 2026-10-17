#!/bin/bash
# V22 c3-tamper matrix — runs entirely inside V22 scratch workspace.
set -u
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-96/seats/V22-c3-tamper.scratch
W=$S/ws
T=$W/corpus/tools/dependency_freeze.py
CHAIN="r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response"

mkdir -p $S/pristine
for d in $CHAIN; do
  rm -rf $S/pristine/$d
  cp -r $R/corpus/fixtures/$d $S/pristine/$d
done
mkdir -p $S/muts

echo "### T0 verify-clean on ws copies"
for d in $CHAIN; do
  echo "== T0 $d =="
  python3 $T $W/corpus/fixtures/$d; echo "EXIT=$?"
done

echo
echo "### T1 non-edge byte tamper: r96 sources.json one character (title)"
rm -rf $S/muts/t1; mkdir -p $S/muts/t1; cp -r $S/pristine/r96-crossing-response $S/muts/t1/
python3 - "$S/muts/t1/r96-crossing-response/sources.json" <<'PY'
import sys, pathlib
p = pathlib.Path(sys.argv[1]); t = p.read_text()
t2 = t.replace("Evin's Salt Court Response Note", "Evin's Salt Court Response note", 1)
assert t2 != t, "replacement failed"
p.write_text(t2)
PY
sha256sum $S/muts/t1/r96-crossing-response/sources.json
echo "== T1 =="
python3 $T $S/muts/t1/r96-crossing-response; echo "EXIT=$?"

echo
echo "### T2 non-edge byte tamper: r94 timeline.json description only (inventory-neutral)"
rm -rf $S/muts/t2; mkdir -p $S/muts/t2; cp -r $S/pristine/r94-paired-crossing $S/muts/t2/
python3 - "$S/muts/t2/r94-paired-crossing/timeline.json" <<'PY'
import sys, pathlib
p = pathlib.Path(sys.argv[1]); t = p.read_text()
t2 = t.replace("south bell at Salt Court", "South bell at Salt Court", 1)
assert t2 != t, "replacement failed"
p.write_text(t2)
PY
sha256sum $S/muts/t2/r94-paired-crossing/timeline.json
echo "== T2 =="
python3 $T $S/muts/t2/r94-paired-crossing; echo "EXIT=$?"

echo
echo "### T3 edge tamper (BR-01): r94 drop evin-ninth-bell from tick-10 depends_on"
rm -rf $S/muts/t3; mkdir -p $S/muts/t3; cp -r $S/pristine/r94-paired-crossing $S/muts/t3/
python3 - "$S/muts/t3/r94-paired-crossing/timeline.json" <<'PY'
import sys, json, pathlib
p = pathlib.Path(sys.argv[1]); data = json.loads(p.read_text())
for r in data:
    if r["id"] == "paired-crossing-decision":
        r["depends_on"] = [d for d in r["depends_on"] if d != "evin-ninth-bell"]
p.write_text(json.dumps(data, indent=2) + "\n")
PY
echo "== T3 =="
python3 $T $S/muts/t3/r94-paired-crossing; echo "EXIT=$?"

echo
echo "### T5b boundary: markdown-only edit (README append) — expect not covered by JSON digest"
rm -rf $S/muts/t5b; mkdir -p $S/muts/t5b; cp -r $S/pristine/r94-paired-crossing $S/muts/t5b/
printf '\n<!-- V22 boundary probe: markdown not digested -->\n' >> $S/muts/t5b/r94-paired-crossing/README.md
echo "== T5b =="
python3 $T $S/muts/t5b/r94-paired-crossing; echo "EXIT=$?"

echo
echo "### T4 freeze-on-copy then verify (last: rewrites ws contract)"
rm -rf $S/muts/t4; mkdir -p $S/muts/t4; cp -r $S/muts/t1/r96-crossing-response $S/muts/t4/
echo "== T4 freeze tampered r96 copy =="
python3 $T --freeze $S/muts/t4/r96-crossing-response; echo "EXIT=$?"
echo "== T4 verify after freeze =="
python3 $T $S/muts/t4/r96-crossing-response; echo "EXIT=$?"
rm -rf $S/muts/t4b; mkdir -p $S/muts/t4b; cp -r $S/pristine/r94-paired-crossing $S/muts/t4b/
echo "== T4b freeze pristine r94 copy =="
python3 $T --freeze $S/muts/t4b/r94-paired-crossing; echo "EXIT=$?"
echo "== T4b verify after freeze =="
python3 $T $S/muts/t4b/r94-paired-crossing; echo "EXIT=$?"

echo
echo "### DONE"
