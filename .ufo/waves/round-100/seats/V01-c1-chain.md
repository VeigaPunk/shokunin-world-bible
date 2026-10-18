# V01 — C1 frozen-chain verification (2026-10-17)

Seat: `V01 c1-chain`. Baseline: `fe1ce46`. Observed live HEAD: `b5fe472957ab1e4e9c90f5613acc14cd24a288ae` (round-100 declaration). All commands below ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`; every Python invocation used `python3`.

Axes: **coverage** (exactly seven live clean fixtures), **integrity** (independent r99 ten-file and aggregate SHA-256 recomputation), **non-regression** (every field of all six inherited pins preserved). This report evaluates C1 only, not C2/C3 or whole-round admission.

## Result

- Seven independently executed live verification commands: **7/7 clean**, each exit 0, with every receipt quoted below.
- Contract pins exactly the declared seven fixtures; only `r99-window-lapse` was added; no pins removed.
- Recomputed r99 digests: **10/10 match delivered bytes**, including all five Markdown files. Aggregate digest also matches: `7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e`.
- Every field of all six pre-existing pins is identical to `git show fe1ce46:corpus/tools/dependency-freeze-contract.json`.
- Important qualification: the contract diff is **not literally addition-only**. In addition to the r99 pin, guarded `freeze()` refreshed the top-level `revision` from `337f0fa52b02626b7687eedbb2d99fab30446fe4` to `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`. No other non-pin metadata changed. This is consistent with the delivered writer at `corpus/tools/dependency_freeze.py:441-443` and is disclosed by T1, not concealed as an r99-only textual delta.
- The delivered tool and all seven delivered fixtures remain byte-unchanged from `fe1ce46`; final independent snapshot recheck found **70/70 pinned-file digests matching**.

## Poll-wait and artifact provenance

I first read the round-100 declaration at `LOG.md:3349-3404`, including C1's guarded-freeze-only and unchanged-prior-pins requirements. Preparation found no lane-root `AGENTS.md` (`Read` returned does-not-exist). The initial command `pwd && git status --short && ls .ufo/waves/round-100/seats` exited 2 because the seats directory did not yet exist; it did confirm the correct lane cwd. This absence was not treated as a failed fixture gate or permission to verify a plan.

Actual bounded readiness command:

```sh
python3 -u - <<'PY'
from pathlib import Path
import datetime, json, time
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == root.resolve()
seats = root/'.ufo/waves/round-100/seats'
contract_path = root/'corpus/tools/dependency-freeze-contract.json'
for attempt in range(1, 16):
    reports = sorted(p for p in seats.iterdir() if p.is_file() and p.name.startswith('T1') and p.suffix == '.md') if seats.is_dir() else []
    try:
        contract = json.loads(contract_path.read_bytes())
        pinned = 'r99-window-lapse' in contract.get('pins', {})
    except (OSError, ValueError):
        pinned = False
    artifacts = [root/'corpus/tools/README.md', root/'SKILL.md', contract_path]
    existing = all(p.is_file() for p in artifacts)
    print(f"POLL {attempt}/40 {datetime.datetime.now().astimezone().isoformat(timespec='seconds')} artifacts={existing} r99_pin={pinned} T1_reports={[str(p.relative_to(root)) for p in reports]}", flush=True)
    if existing and pinned and reports:
        print('READY: T1 report and landed contract available', flush=True)
        break
    if attempt < 15:
        time.sleep(20)
else:
    print('POLL-CONTINUE: 15/40 checks exhausted; 25 remain', flush=True)
PY
```

Observed stdout, exit 0:

```text
POLL 1/40 2026-10-17T23:32:23-03:00 artifacts=True r99_pin=True T1_reports=[]
POLL 2/40 2026-10-17T23:32:43-03:00 artifacts=True r99_pin=True T1_reports=[]
POLL 3/40 2026-10-17T23:33:03-03:00 artifacts=True r99_pin=True T1_reports=[]
POLL 4/40 2026-10-17T23:33:23-03:00 artifacts=True r99_pin=True T1_reports=[]
POLL 5/40 2026-10-17T23:33:43-03:00 artifacts=True r99_pin=True T1_reports=[]
POLL 6/40 2026-10-17T23:34:03-03:00 artifacts=True r99_pin=True T1_reports=[]
POLL 7/40 2026-10-17T23:34:23-03:00 artifacts=True r99_pin=True T1_reports=[]
POLL 8/40 2026-10-17T23:34:43-03:00 artifacts=True r99_pin=True T1_reports=[]
POLL 9/40 2026-10-17T23:35:03-03:00 artifacts=True r99_pin=True T1_reports=['.ufo/waves/round-100/seats/T1-chain-seven.md']
READY: T1 report and landed contract available
```

There were eight 20-second sleeps, no stall-escape, and no all-reports poll; SELF subtraction was therefore not applicable. Only after readiness did I read the complete delivered producer report `.ufo/waves/round-100/seats/T1-chain-seven.md` and perform the seven gate replays below.

T1's report at lines 29-43 records its single authorized producer command, `python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r99-window-lapse`, exit 0, `FROZEN r99-window-lapse: events 8; dependency-edges 7; relations 1`, followed by the same digest and a clean receipt. Guarded-operation history is producer attestation; V01 did not observe that subprocess live or re-run `--freeze`. V01's receipt, digest, and baseline comparisons below are independent reads/executions on the delivered artifacts and are consistent with the guarded writer.

## Seven live receipts — complete stdout for every fixture

These seven commands ran as independent concurrent tool calls. Each returned exit 0 with no stderr.

```text
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
EXIT 0

$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
RESULT PASS
EXIT 0

$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
EXIT 0

$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
RESULT PASS
EXIT 0

$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
RESULT PASS
EXIT 0

$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
EXIT 0

$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
EXIT 0
```

## Independent ten-file recomputation, pin census, and preservation

This audit does not import or reuse the gate's hashing/model functions. It independently reads all ten delivered r99 files with `Path.read_bytes()`, computes each SHA-256, reconstructs the aggregate hash, checks the exact pin set, compares every inherited pin field, and checks the tick-15 pin directly.

Actual command:

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib, json, subprocess
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == root.resolve()
path = root/'corpus/tools/dependency-freeze-contract.json'
raw = path.read_bytes()
current = json.loads(raw)
baseline = json.loads(subprocess.check_output(['git', 'show', 'fe1ce46:corpus/tools/dependency-freeze-contract.json']))
expected_names = ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing', 'r99-window-lapse']
expected_files = ['entities.json', 'relations.json', 'timeline.json', 'sources.json', 'contradictions.json', 'README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md']
print('CONTRACT_SHA256', hashlib.sha256(raw).hexdigest())
print('HEAD', subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip())
print('PIN_COUNT', len(current['pins']))
print('PIN_NAMES', sorted(current['pins']))
print('EXACT_SEVEN', sorted(current['pins']) == expected_names)
print('ADDED_PINS', sorted(set(current['pins']) - set(baseline['pins'])))
print('REMOVED_PINS', sorted(set(baseline['pins']) - set(current['pins'])))
for name, pin in baseline['pins'].items():
    observed = current['pins'].get(name, {})
    drift = sorted(key for key in set(pin) | set(observed) if pin.get(key) != observed.get(key))
    print('INHERITED_PIN', name, 'drift_fields=' + json.dumps(drift))
top_changes = sorted(key for key in set(baseline) | set(current) if baseline.get(key) != current.get(key))
print('TOP_LEVEL_CHANGED_FIELDS', top_changes)
print('TOP_LEVEL_REVISION', baseline['revision'], '->', current['revision'])
print('OUTSIDE_PINS_AND_REVISION_UNCHANGED', {k:v for k,v in baseline.items() if k not in {'pins','revision'}} == {k:v for k,v in current.items() if k not in {'pins','revision'}})
pin = current['pins']['r99-window-lapse']
fixture = root/pin['fixture']
print('R99_FIXTURE', pin['fixture'])
print('R99_PAYLOAD_SCHEMA_VERSION', pin['payload_schema_version'])
print('R99_PINNED_FILES_EXACT_ORDER', pin['pinned_files'] == expected_files)
print('R99_FILE_DIGEST_KEYS_EXACT', sorted(pin['files']) == sorted(expected_files))
digests = {}
for name in expected_files:
    data = (fixture/name).read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    digests[name] = digest
    print(f'FILE {name} bytes={len(data)} computed={digest} pinned={pin["files"].get(name)} match={digest == pin["files"].get(name)}')
combined = hashlib.sha256(json.dumps(digests, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()
print('R99_CONTENT_DIGEST', 'computed='+combined, 'pinned='+pin['content_sha256'], 'match='+str(combined == pin['content_sha256']))
timeline = json.loads((fixture/'timeline.json').read_bytes())
terminal = next(row for row in timeline if row['id'] == 'clerk-lapse-recorded')
print('TICK15_DELIVERED', json.dumps({k:terminal[k] for k in ['id','tick','entity_id','place_id','depends_on']}, sort_keys=True))
print('TICK15_PINNED', json.dumps(pin['events']['clerk-lapse-recorded'], sort_keys=True))
print('CONTRACT_STABLE_DURING_AUDIT', path.read_bytes() == raw)
assert sorted(current['pins']) == expected_names
assert all(baseline['pins'][name] == current['pins'].get(name) for name in baseline['pins'])
assert top_changes == ['pins', 'revision']
assert current['revision'] == pin['revision']
assert pin['payload_schema_version'] == 2 and pin['pinned_files'] == expected_files
assert digests == pin['files'] and combined == pin['content_sha256']
assert terminal['tick'] == 15 and terminal['depends_on'] == ['clerk-filing-open']
assert pin['events']['clerk-lapse-recorded'] == {'depends_on': ['clerk-filing-open'], 'endpoint': {'tick': 15, 'entity_id': 'clerk-maren', 'place_id': 'chalk-stair'}}
assert path.read_bytes() == raw
print('AUDIT PASS')
PY
```

Complete observed stdout, exit 0:

```text
CONTRACT_SHA256 ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
HEAD b5fe472957ab1e4e9c90f5613acc14cd24a288ae
PIN_COUNT 7
PIN_NAMES ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing', 'r99-window-lapse']
EXACT_SEVEN True
ADDED_PINS ['r99-window-lapse']
REMOVED_PINS []
INHERITED_PIN r88-m3-maya-cluster drift_fields=[]
INHERITED_PIN r94-paired-crossing drift_fields=[]
INHERITED_PIN r95-crossing-aftermath drift_fields=[]
INHERITED_PIN r96-crossing-response drift_fields=[]
INHERITED_PIN r97-crossing-acknowledgment drift_fields=[]
INHERITED_PIN r98-clerk-filing drift_fields=[]
TOP_LEVEL_CHANGED_FIELDS ['pins', 'revision']
TOP_LEVEL_REVISION 337f0fa52b02626b7687eedbb2d99fab30446fe4 -> b5fe472957ab1e4e9c90f5613acc14cd24a288ae
OUTSIDE_PINS_AND_REVISION_UNCHANGED True
R99_FIXTURE corpus/fixtures/r99-window-lapse
R99_PAYLOAD_SCHEMA_VERSION 2
R99_PINNED_FILES_EXACT_ORDER True
R99_FILE_DIGEST_KEYS_EXACT True
FILE entities.json bytes=1793 computed=db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984 pinned=db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984 match=True
FILE relations.json bytes=139 computed=c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9 pinned=c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9 match=True
FILE timeline.json bytes=2998 computed=2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069 pinned=2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069 match=True
FILE sources.json bytes=3293 computed=8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15 pinned=8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15 match=True
FILE contradictions.json bytes=3 computed=37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 pinned=37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 match=True
FILE README.md bytes=6176 computed=b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049 pinned=b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049 match=True
FILE claim-excerpt-map.md bytes=17119 computed=d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d pinned=d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d match=True
FILE fictional-excerpts.md bytes=5114 computed=fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d pinned=fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d match=True
FILE inspiration-note.md bytes=1956 computed=58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37 pinned=58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37 match=True
FILE source-excerpt.md bytes=640 computed=b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd pinned=b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd match=True
R99_CONTENT_DIGEST computed=7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e pinned=7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e match=True
TICK15_DELIVERED {"depends_on": ["clerk-filing-open"], "entity_id": "clerk-maren", "id": "clerk-lapse-recorded", "place_id": "chalk-stair", "tick": 15}
TICK15_PINNED {"depends_on": ["clerk-filing-open"], "endpoint": {"entity_id": "clerk-maren", "place_id": "chalk-stair", "tick": 15}}
CONTRACT_STABLE_DURING_AUDIT True
AUDIT PASS
```

## Actual Git diff versus fe1ce46

Command:

```sh
git diff --no-ext-diff --unified=3 fe1ce46 -- corpus/tools/dependency-freeze-contract.json
```

Exit 0. The full observed diff has exactly two hunks, with these headers:

```text
@@ -32,7 +32,7 @@
@@ -554,6 +554,129 @@
```

First hunk, complete:

```diff
@@ -32,7 +32,7 @@
     "1": "FAIL",
     "2": "ERROR"
   },
-  "revision": "337f0fa52b02626b7687eedbb2d99fab30446fe4",
+  "revision": "b5fe472957ab1e4e9c90f5613acc14cd24a288ae",
   "pins": {
     "r88-m3-maya-cluster": {
       "fixture": "corpus/fixtures/r88-m3-maya-cluster",
```

Second hunk adds the r99 object after r98, with no removed inherited-pin lines. Representative excerpt of its beginning (not the full hunk):

```diff
@@ -554,6 +554,129 @@
         "entities": 6,
         "sources": 7
       }
+    },
+    "r99-window-lapse": {
+      "fixture": "corpus/fixtures/r99-window-lapse",
+      "revision": "b5fe472957ab1e4e9c90f5613acc14cd24a288ae",
+      "payload_schema_version": 2,
```

An independently executed `git diff --numstat fe1ce46 -- corpus/tools/dependency-freeze-contract.json` returned exit 0, `124\t1\tcorpus/tools/dependency-freeze-contract.json`. The parsed-value audit above covers every field of every inherited pin and every other top-level value, not just the excerpted text.

The initial independent tool-byte check compared delivered bytes against `git show fe1ce46:corpus/tools/dependency_freeze.py` and printed:

```text
TOOL_IDENTICAL_TO_BASELINE corpus/tools/dependency_freeze.py True fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c
```

Final preservation command:

```sh
git diff --exit-code fe1ce46 -- corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r94-paired-crossing corpus/fixtures/r95-crossing-aftermath corpus/fixtures/r96-crossing-response corpus/fixtures/r97-crossing-acknowledgment corpus/fixtures/r98-clerk-filing corpus/fixtures/r99-window-lapse
```

Observed exit 0, empty stdout/stderr: no delivered fixture or gate-code drift.

## Final snapshot and write-scope check

Actual final pre-report command:

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib, json
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
assert Path.cwd().resolve() == root
report = root/'.ufo/waves/round-100/seats/V01-c1-chain.md'
assert report.is_absolute() and report.resolve() == report and report.parent.resolve() == root/'.ufo/waves/round-100/seats'
assert not report.exists()
contract = root/'corpus/tools/dependency-freeze-contract.json'
raw = contract.read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5'
current = json.loads(raw)
for pin in current['pins'].values():
    for name, expected in pin['files'].items():
        assert hashlib.sha256((root/pin['fixture']/name).read_bytes()).hexdigest() == expected
print('FINAL_LIVE_SNAPSHOT contract unchanged; seven fixtures; 70/70 file digests match')
print('REPORT_RESOLVED', report.resolve())
print('REPORT_PARENT_EXISTS', report.parent.is_dir())
print('WRITE_SCOPE_PASS exclusive V01 report only; no scratch created')
PY
```

Observed stdout, exit 0:

```text
FINAL_LIVE_SNAPSHOT contract unchanged; seven fixtures; 70/70 file digests match
REPORT_RESOLVED /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V01-c1-chain.md
REPORT_PARENT_EXISTS True
WRITE_SCOPE_PASS exclusive V01 report only; no scratch created
```

The report-nonexistence assertion was intentionally executed before creation, not a reusable post-creation test.

## Boundaries and touched paths

Only this report was written by V01: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V01-c1-chain.md`. Declared scratch `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V01-c1-chain-scratch/` was unused and not created. No delivered contract, fixture, code, or documentation was changed. No nested agents, commits, pushes, or network calls. No unresolved C1 gate failures remain.

V01 did not run self-test mode because the delivered implementation creates temporary trees outside this seat's exclusive write scope; the seven delivered fixture gates were exercised directly. T1's separate isolated self-test and mutation-control reports are not passed off as V01's own executions. Byte agreement/pinning does not establish dependency semantics, prose entailment, testimony truth, chronology authentication, authenticity, rights, or canon. The new r100 fixture is not one of C1's seven declared pins. r88's extra `symbolism-clause-map.md` remains outside the declared ten-file payload.

PASS — C1 has exactly seven clean live fixtures, all ten independently recomputed r99 digests match, and all six inherited pins are unchanged; guarded-writer top-level revision refresh explicitly qualified.
