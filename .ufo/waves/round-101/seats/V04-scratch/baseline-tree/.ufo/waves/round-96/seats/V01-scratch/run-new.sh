#!/bin/bash
# V01 scratch: run the delivered (NEW) map_obligations against the three mutation variants, twice each.
# Tool copy lives at scratch depth 3 so its ROOT = V01-scratch (self-test tempdirs stay in scratch).
set -u
S=/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats/V01-scratch
NEW=$S/new/tool/map_obligations.py
for run in 1 2; do
  for v in pristine key+row row-only key-only; do
    if [ "$v" = pristine ]; then d=$S/old/corpus/fixtures/r95-crossing-aftermath; else d=$S/mutations/$v; fi
    python3 "$NEW" "$d" > "$S/new-$v-run$run.out" 2>&1
    echo "$?" > "$S/new-$v-run$run.exit"
  done
done
echo "done"
