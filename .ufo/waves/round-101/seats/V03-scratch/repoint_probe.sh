#!/usr/bin/env bash
# V03 repointed-edge probe: mirror delivered tool+contract+fixture into a scratch
# root, repoint clerk-review-first-passage's depends_on to a different valid
# earlier event, verify against the mirrored pin. Args: MIRROR_ROOT SRC_FIXTURE NEW_DEP
set -u
MIRROR="$1"; SRC="$2"; NEWDEP="$3"
ROOTM="$MIRROR/root"
rm -rf "$ROOTM"
mkdir -p "$ROOTM/corpus/tools" "$ROOTM/corpus/fixtures"
cp /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py "$ROOTM/corpus/tools/"
cp /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency-freeze-contract.json "$ROOTM/corpus/tools/"
cp -r "$SRC" "$ROOTM/corpus/fixtures/$(basename "$SRC")"
python3 - "$ROOTM/corpus/fixtures/$(basename "$SRC")/timeline.json" "$NEWDEP" <<'PY'
import json, sys
p, newdep = sys.argv[1], sys.argv[2]
t = json.loads(open(p, encoding='utf-8').read())
for rec in t:
    if rec['id'] == 'clerk-review-first-passage':
        old = rec['depends_on']
        assert old and old != [newdep], f"unexpected current depends_on: {old}"
        rec['depends_on'] = [newdep]
        print(f"EDIT clerk-review-first-passage depends_on {old} -> [\"{newdep}\"]")
open(p, 'w', encoding='utf-8').write(json.dumps(t, indent=2) + '\n')
PY
echo "--- run on mirror ---"
python3 "$ROOTM/corpus/tools/dependency_freeze.py" "$ROOTM/corpus/fixtures/$(basename "$SRC")"
echo "exit=$?"
