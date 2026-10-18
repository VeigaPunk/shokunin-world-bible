#!/bin/bash
# V48 fakerepo builder: mirror <tool-src> and <contract-src> into a scratch fake repo root,
# copy a fixture into scope. Usage: mkrep.sh <dest-root> <tool-src> <contract-src> <fixture-name> [<fixture-src-dir>]
set -e
DEST="$1"; TOOL="$2"; CONTRACT="$3"; FIX="$4"; FIXSRC="${5:-/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/$4}"
R=/home/vgpnk/Projects/shokunin/lore-shokunin
mkdir -p "$DEST/corpus/tools" "$DEST/corpus/fixtures"
cp "$TOOL" "$DEST/corpus/tools/dependency_freeze.py"
cp "$CONTRACT" "$DEST/corpus/tools/dependency-freeze-contract.json"
cp -r "$FIXSRC" "$DEST/corpus/fixtures/$FIX"
echo "FAKEREPO $DEST ready: $(ls "$DEST/corpus/fixtures/")"
