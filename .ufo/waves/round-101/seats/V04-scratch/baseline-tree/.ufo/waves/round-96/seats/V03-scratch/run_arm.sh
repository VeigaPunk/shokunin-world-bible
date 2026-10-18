#!/bin/bash
# usage: run_arm.sh <arm-name>  -> run --self-test inside the arm, capture stdout+exit
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
ARM=$REPO/.ufo/waves/round-96/seats/V03-scratch/arms/$1
cd "$ARM" || exit 9
python3 map_obligations.py --self-test > "$ARM/out.txt" 2> "$ARM/err.txt"
echo "exit=$?"
echo "--- stdout ---"; cat "$ARM/out.txt"
echo "--- stderr (bytes=$(wc -c < "$ARM/err.txt")) ---"; cat "$ARM/err.txt"
