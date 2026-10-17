#!/bin/bash
# V05 drift compare: baseline tool vs delivered tool on FROZEN fixture copies, byte-identical stdout+exit expected.
set -u
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-97/seats/V05-scratch
cd $R
BASE=$S/baseline/map_obligations.py
POST=$R/corpus/tools/map_obligations.py
FR=$S/frozen-fixtures
rm -rf $FR; mkdir -p $FR
cp -r "$S/dual-ref" "$S/dual-ref-colon" $FR/
for f in r87-myth-cluster r88-m3-maya-cluster r96-crossing-response; do
  cp -r "corpus/fixtures/$f" $FR/
done
FAIL=0
for f in "$FR/dual-ref" "$FR/dual-ref-colon" "$FR/r87-myth-cluster" "$FR/r88-m3-maya-cluster" "$FR/r96-crossing-response"; do
  b=$(python3 "$BASE" "$f" 2>&1); be=$?
  p=$(python3 "$POST" "$f" 2>&1); pe=$?
  if [ "$b" = "$p" ] && [ "$be" = "$pe" ]; then
    echo "IDENTICAL exit=$be $f"
  else
    FAIL=1
    echo "DRIFT $f"
    echo "--- baseline exit=$be"; echo "$b"
    echo "--- post exit=$pe"; echo "$p"
  fi
done
exit $FAIL
