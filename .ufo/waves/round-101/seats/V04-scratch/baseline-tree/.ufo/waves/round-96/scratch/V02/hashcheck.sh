#!/bin/bash
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
cd "$REPO"
V=.ufo/waves/round-96/scratch/V02
find corpus -type f -not -path '*/__pycache__/*' | LC_ALL=C sort | xargs sha256sum > "$V/corpus.hash.before"
sha256sum corpus/tools/map-obligations-contract.json corpus/tools/map_obligations.py > "$V/contract.hash.before"
echo "stray_before=$(find . -maxdepth 1 -name 'map-obligations-self-test-*' | wc -l)"
git status --porcelain > "$V/gitstatus.before"
python3 corpus/tools/map_obligations.py --self-test > "$V/selftest.out" 2> "$V/selftest.err"
echo "selftest_exit=$?"
find corpus -type f -not -path '*/__pycache__/*' | LC_ALL=C sort | xargs sha256sum > "$V/corpus.hash.after"
sha256sum corpus/tools/map-obligations-contract.json corpus/tools/map_obligations.py > "$V/contract.hash.after"
echo "stray_after=$(find . -maxdepth 1 -name 'map-obligations-self-test-*' | wc -l)"
git status --porcelain > "$V/gitstatus.after"
echo "=== corpus hash diff ==="; diff -q "$V/corpus.hash.before" "$V/corpus.hash.after" && echo CORPUS_HASH_IDENTICAL || echo CORPUS_CHANGED
echo "=== contract+tool hash diff ==="; diff -q "$V/contract.hash.before" "$V/contract.hash.after" && echo CONTRACT_TOOL_HASH_IDENTICAL || echo CONTRACT_TOOL_CHANGED
echo "=== git status diff ==="; diff -q "$V/gitstatus.before" "$V/gitstatus.after" && echo GIT_STATUS_IDENTICAL || { echo GIT_STATUS_CHANGED; diff "$V/gitstatus.before" "$V/gitstatus.after"; }
echo "=== manifest counts ==="; wc -l < "$V/corpus.hash.before"; sha256sum "$V/corpus.hash.before" "$V/corpus.hash.after"
echo "=== stderr bytes ==="; wc -c < "$V/selftest.err"
