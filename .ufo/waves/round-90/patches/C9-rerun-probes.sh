#!/usr/bin/env bash
set -euo pipefail

repo=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../../../.." && pwd)
cd "$repo"
baseline_commit=e97613cc276f5fa9cac49ff1900798cf6863c020
patch_path=.ufo/waves/round-90/patches/X1-c1.patch
expected_patch_sha256=6d37eccfb913155aabd6e4e883870eab68676920dca1142d6d4482ae79316223
patch_sha256=$(sha256sum "$patch_path" | awk '{print $1}')
[[ "$patch_sha256" == "$expected_patch_sha256" ]]
printf 'baseline_commit=%s\npatch_sha256=%s\n' "$baseline_commit" "$patch_sha256"

scratch=$(mktemp -d /tmp/lore-r90-C9.XXXXXX)
trap 'rm -rf -- "$scratch"' EXIT
git archive --format=tar "$baseline_commit" corpus/fixtures/check_bible.py | tar -xf - -C "$scratch"
patch --fuzz=0 -p1 -d "$scratch" < "$patch_path"
candidate="$scratch/corpus/fixtures/check_bible.py"
candidate_sha256=$(sha256sum "$candidate" | awk '{print $1}')
expected_candidate_sha256=12866e734beb0e8fdfb641e9dab7cdaae7518fc0fdb8749a5e086981a0d1ae18
[[ "$candidate_sha256" == "$expected_candidate_sha256" ]]
printf 'candidate_checker_sha256=%s\n' "$candidate_sha256"

base_fixture="$repo/corpus/fixtures/r89-fn2-unresolved-chain-break"
probe_root="$scratch/probes"
python3 - "$base_fixture" "$probe_root" <<'PY'
from copy import deepcopy
import json
from pathlib import Path
import sys

base = Path(sys.argv[1])
probe_root = Path(sys.argv[2])
original = json.loads((base / 'entities.json').read_text(encoding='utf-8'))
cases = {
    'chain-unresolved': None,
    'tick-relevant-unresolved': ((3, None, 'f3-dup'), (1, 'f3-dup', 'harbor')),
    'null-from-chain': ((0, None, 'mira'), (1, None, 'harbor')),
    'unrelated-duplicate-tick': ((3, None, 'mira'), (1, 'mira', 'mira')),
}
for name, provenance in cases.items():
    rows = deepcopy(original)
    if provenance is not None:
        item = next(row for row in rows if row['id'] == 'f3-seal')
        for record, (tick, from_holder, to_holder) in zip(item['provenance'], provenance):
            record['tick'] = tick
            record['from_holder'] = from_holder
            record['to_holder'] = to_holder
    directory = probe_root / name
    directory.mkdir(parents=True)
    for section in ('sources', 'relations', 'timeline', 'contradictions'):
        (directory / f'{section}.json').symlink_to(base / f'{section}.json')
    (directory / 'entities.json').write_text(json.dumps(rows, indent=2) + '\n', encoding='utf-8')
PY

for name in chain-unresolved tick-relevant-unresolved null-from-chain unrelated-duplicate-tick; do
    printf '\n=== %s ===\n' "$name"
    if python3 "$candidate" "$probe_root/$name"; then
        rc=0
    else
        rc=$?
    fi
    printf 'exit=%s\n' "$rc"
done
patch_sha256_after=$(sha256sum "$patch_path" | awk '{print $1}')
[[ "$patch_sha256_after" == "$expected_patch_sha256" ]]
printf '\npatch_sha256_after=%s\n' "$patch_sha256_after"
