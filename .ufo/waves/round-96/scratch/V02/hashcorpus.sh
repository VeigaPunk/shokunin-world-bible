#!/bin/bash
# usage: hashcorpus.sh <label>
cd /home/vgpnk/Projects/shokunin/lore-shokunin
OUT=.ufo/waves/round-96/scratch/V02/manifest-$1.txt
find corpus -type f -not -path '*/__pycache__/*' | LC_ALL=C sort | xargs sha256sum > "$OUT"
echo "files=$(wc -l < "$OUT") manifest_sha256=$(sha256sum "$OUT" | cut -d' ' -f1)"
echo "pycache_dirs=$(find corpus -type d -name __pycache__ | wc -l)"
