#!/bin/bash
# V28 (late-bookkeeper) reconciliation suite. Read-only against the corpus;
# writes only inside .v28-scratch/.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
SCRATCH="$(pwd)/.ufo/waves/round-101/seats/.v28-scratch"

echo "== C1: contract pin census =="
python3 - <<'EOF'
import json, subprocess
d = json.load(open('corpus/tools/dependency-freeze-contract.json'))
pins = d['pins']
print('pins:', len(pins), list(pins.keys()))
print('r100-docket-review present:', 'r100-docket-review' in pins)
base = json.loads(subprocess.run(
    ['git', 'show', 'HEAD:corpus/tools/dependency-freeze-contract.json'],
    capture_output=True, text=True).stdout)
changed = [k for k in base['pins'] if pins.get(k) != base['pins'][k]]
print('baseline pins with changed fields:', changed or 'NONE')
print('revision baseline:', base.get('revision'), '-> now:', d.get('revision'))
EOF

echo "== C1: eight-fixture chain verify =="
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath \
         r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing \
         r99-window-lapse r100-docket-review; do
  out=$(python3 corpus/tools/dependency_freeze.py "corpus/fixtures/$f" 2>&1); rc=$?
  echo "$f exit=$rc :: $(echo "$out" | tail -n 1)"
done

echo "== C3: self-test run =="
python3 corpus/tools/dependency_freeze.py --self-test > "$SCRATCH/selftest.out" 2>&1
echo "selftest exit=$?"
tail -n 4 "$SCRATCH/selftest.out"

echo "== C3: case census + new case expectations =="
python3 - <<'EOF'
import json
d = json.load(open('corpus/tools/dependency-freeze-contract.json'))
exp = d['self_test']['expected']
print('case count:', len(exp))
known = {'addition_edge_phantom','clean','digest_tamper','event_endpoint_change',
         'event_removed','invalid_arguments','malformed_json','markdown_tamper',
         'missing_fixture','missing_timeline','path_mismatch','reduction_edge_drop',
         'relation_added','relation_endpoint_flip','relation_removed','scope_refused',
         'self_test_mismatch','unpinned_fixture'}
for k in sorted(exp):
    if k not in known:
        print('NEW CASE:', k, json.dumps(exp[k], sort_keys=True))
EOF

echo "== C1/C3 doc updates (README + SKILL) =="
grep -n "19 case\|19/19\|repoint" corpus/tools/README.md | head -n 8
grep -n "19 case\|19/19\|r101" SKILL.md | head -n 8

echo "== C2: knowledge file receipt =="
ls -la corpus/knowledge/r101-r10-register-first-entry.md 2>&1
sha256sum corpus/knowledge/r101-r10-register-first-entry.md 2>/dev/null

echo "== tool file hashes (vs baseline fb9bb9ff/ea012b9c/c99217cd/09b2949a) =="
sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json \
          corpus/tools/README.md SKILL.md
echo "== RECONCILE-DONE =="
