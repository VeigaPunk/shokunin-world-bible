#!/bin/bash
# V40 build-mirror: copies the DELIVERED working-tree bytes into a mirror at $1
# (tool + contract + the six chain fixtures), then saves pristine base copies.
set -eu
M="$1"
SRC=/home/vgpnk/Projects/shokunin/lore-shokunin
rm -rf "$M"
mkdir -p "$M/corpus/tools" "$M/corpus/fixtures"
cp "$SRC/corpus/tools/dependency_freeze.py" "$M/corpus/tools/dependency_freeze.py"
cp "$SRC/corpus/tools/dependency-freeze-contract.json" "$M/corpus/tools/dependency-freeze-contract.json"
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
  cp -r "$SRC/corpus/fixtures/$f" "$M/corpus/fixtures/$f"
done
cp "$M/corpus/tools/dependency_freeze.py" "$M/base-tool.py"
cp "$M/corpus/tools/dependency-freeze-contract.json" "$M/base-contract.json"
sha256sum "$M/corpus/tools/dependency_freeze.py" "$M/corpus/tools/dependency-freeze-contract.json"
