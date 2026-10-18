#!/usr/bin/env bash
# V06: build delivered-byte mirrors for the r97 freeze discharge.
# Usage: build_mirror.sh <mirror-root>
set -euo pipefail
cd /home/vgpnk/Projects/shokunin/lore-shokunin
M="$1"
rm -rf "$M"
mkdir -p "$M/corpus/tools" "$M/corpus/fixtures"
cp corpus/tools/dependency_freeze.py "$M/corpus/tools/dependency_freeze.py"
cp corpus/tools/dependency-freeze-contract.json "$M/corpus/tools/dependency-freeze-contract.json"
cp -a corpus/fixtures/r97-crossing-acknowledgment "$M/corpus/fixtures/r97-crossing-acknowledgment"
echo "MIRROR $M built"
