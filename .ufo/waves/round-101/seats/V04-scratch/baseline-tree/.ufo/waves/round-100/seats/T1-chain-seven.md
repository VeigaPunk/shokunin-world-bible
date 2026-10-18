# T1 — chain seven (2026-10-17)

Seat scope: round-100 C1 / coverage. Axes: coverage (r99 pinned; seven clean fixtures), preservation (six prior pins unchanged), freshness/calibration (dated documentation supersessions; no semantics claim). Baseline: `fe1ce46`; live HEAD at the guarded operation: `b5fe472957ab1e4e9c90f5613acc14cd24a288ae` (round-100 declaration). All shell commands below ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`; Python commands used `python3`.

## Delivered changes and ownership

- `corpus/tools/dependency-freeze-contract.json`: written only by the single authorized guarded `--freeze` invocation. Added the r99 pin; no direct edit.
- `corpus/tools/README.md:363`: appended the Round-100 addendum, dated supersession of historical six-fixture wording/revision wording, guarded-operation receipt, seven verification commands, tick-15 negative control, and explicit remaining bounds.
- `SKILL.md:96-102`: only the dependency-freeze registry row was changed: seventh fixture, seven-pin values, dated supersession, AC-4 discharge, and explicit tool-managed revision metadata.
- This exclusive report: `.ufo/waves/round-100/seats/T1-chain-seven.md`.
- Declared per-seat scratch only: `.ufo/waves/round-100/seats/T1-scratch/`. It contains byte copies of `corpus/tools/{dependency_freeze.py,dependency-freeze-contract.json}` and `corpus/fixtures/{r95-crossing-aftermath,r99-window-lapse}/` with each fixture's ten files: `README.md`, `claim-excerpt-map.md`, `contradictions.json`, `entities.json`, `fictional-excerpts.md`, `inspiration-note.md`, `relations.json`, `source-excerpt.md`, `sources.json`, `timeline.json`. Only the scratch r99 `timeline.json` was subsequently edited (the intentional negative control). Self-test temporary subtrees were created and automatically cleaned inside this declared scratch root.

No nested agents, commits, pushes, network, or writes outside these owned paths. The delivered tool and r99 fixture remained untouched. No producer dependency or all-reports poll was needed; the existing r99 artifact was present. No bounded stall-escape was used.

**Important literal-diff qualification:** the contract is not strictly an addition-only text diff: `freeze()` also refreshes its top-level `revision`. The only pin change is the r99 addition; every field of every other pin is identical to `fe1ce46`. Both documentation updates disclose the metadata refresh. I did not hand-edit the contract to erase this guard-produced delta.

## 1. Guarded pin operation

The preflight asserted the current resolved lane root and target, verified that the entire pre-operation contract equaled `git show fe1ce46:corpus/tools/dependency-freeze-contract.json`, and confirmed r99 was absent. Observed preflight output:

```text
ROOT /home/vgpnk/Projects/shokunin/lore-shokunin
TARGET /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r99-window-lapse
CONTRACT /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency-freeze-contract.json
BASELINE contract unchanged; six existing pins; r99 absent
HEAD b5fe472957ab1e4e9c90f5613acc14cd24a288ae
```

Actual guarded command (run once after that successful preflight):

```sh
python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r99-window-lapse
```

Observed stdout, exit 0:

```text
FROZEN r99-window-lapse: events 8; dependency-edges 7; relations 1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
```

## 2. Seven live verification receipts

These seven invocations were first run as independent parallel calls, then replayed concurrently in a Python `ThreadPoolExecutor(max_workers=7)` wrapper that printed each command, actual stdout, and return code. The delivered contract/fixtures, not plans or scratch fixtures, produced all seven receipts:

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
CHAIN 7/7 clean
```

## 3. Schema-2 ten-file payload and existing-pin preservation

Actual diff command:

```sh
git diff fe1ce46 -- corpus/tools/dependency-freeze-contract.json
```

Exit 0; two diff hunks were observed: `@@ -32,7 +32,7 @@` refreshes top-level `revision` from `337f0fa52b02626b7687eedbb2d99fab30446fe4` to `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`; `@@ -554,6 +554,129 @@` appends `pins.r99-window-lapse`. No existing pin's fields occur as changed lines. This matches the writer's `contract["revision"] = revision`; it is disclosed, not hidden as an addition-only diff.

Actual parsed-value/file-digest verification command:

```sh
python3 - <<'PY'
import hashlib
import json
import subprocess
from pathlib import Path
root = Path.cwd().resolve()
assert root == Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
rel = 'corpus/tools/dependency-freeze-contract.json'
base = json.loads(subprocess.check_output(['git', 'show', 'fe1ce46:' + rel], text=True))
now = json.loads((root / rel).read_text())
assert set(now['pins']) - set(base['pins']) == {'r99-window-lapse'}
assert not (set(base['pins']) - set(now['pins']))
for name, pin in base['pins'].items():
    assert pin == now['pins'][name], name
    print(f'UNCHANGED {name}: every field')
meta_changed = [k for k in sorted(set(base) | set(now)) if k != 'pins' and base.get(k) != now.get(k)]
assert meta_changed == ['revision'], meta_changed
assert now['revision'] == subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
print(f'TOP-LEVEL revision {base["revision"]} -> {now["revision"]} (guarded writer metadata)')
pin = now['pins']['r99-window-lapse']
expected = ['entities.json', 'relations.json', 'timeline.json', 'sources.json', 'contradictions.json', 'README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md']
assert now['schema_version'] == now['payload_schema_version'] == pin['payload_schema_version'] == 2
assert pin['pinned_files'] == expected == now['pinned_files']
assert set(pin['files']) == set(expected)
assert pin['fixture'] == 'corpus/fixtures/r99-window-lapse'
for name in expected:
    actual = hashlib.sha256((root / pin['fixture'] / name).read_bytes()).hexdigest()
    assert actual == pin['files'][name], name
    print(f'R99 FILE {name}: sha256 {actual} matches')
payload = json.dumps(pin['files'], sort_keys=True, separators=(',', ':'))
assert hashlib.sha256(payload.encode()).hexdigest() == pin['content_sha256']
assert pin['counts'] == {'events': 8, 'dependency_edges': 7, 'relations': 1, 'entities': 6, 'sources': 8}
assert pin['events']['clerk-lapse-recorded'] == {'depends_on': ['clerk-filing-open'], 'endpoint': {'tick': 15, 'entity_id': 'clerk-maren', 'place_id': 'chalk-stair'}}
print('R99 SCHEMA 2; declared files 10/10; file hashes 10/10; aggregate digest matches')
print(f'R99 PIN revision {pin["revision"]}; digest {pin["content_sha256"]}; counts {json.dumps(pin["counts"], sort_keys=True)}')
print('R99 TICK-15 edge clerk-lapse-recorded -> clerk-filing-open pinned')
print('DIFF PASS: r99 pin added; six existing pins unchanged; only other change is tool-managed top-level revision')
PY
```

Observed stdout, exit 0:

```text
UNCHANGED r88-m3-maya-cluster: every field
UNCHANGED r94-paired-crossing: every field
UNCHANGED r95-crossing-aftermath: every field
UNCHANGED r96-crossing-response: every field
UNCHANGED r97-crossing-acknowledgment: every field
UNCHANGED r98-clerk-filing: every field
TOP-LEVEL revision 337f0fa52b02626b7687eedbb2d99fab30446fe4 -> b5fe472957ab1e4e9c90f5613acc14cd24a288ae (guarded writer metadata)
R99 FILE entities.json: sha256 db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984 matches
R99 FILE relations.json: sha256 c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9 matches
R99 FILE timeline.json: sha256 2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069 matches
R99 FILE sources.json: sha256 8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15 matches
R99 FILE contradictions.json: sha256 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 matches
R99 FILE README.md: sha256 b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049 matches
R99 FILE claim-excerpt-map.md: sha256 d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d matches
R99 FILE fictional-excerpts.md: sha256 fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d matches
R99 FILE inspiration-note.md: sha256 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37 matches
R99 FILE source-excerpt.md: sha256 b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd matches
R99 SCHEMA 2; declared files 10/10; file hashes 10/10; aggregate digest matches
R99 PIN revision b5fe472957ab1e4e9c90f5613acc14cd24a288ae; digest 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; counts {"dependency_edges": 7, "entities": 6, "events": 8, "relations": 1, "sources": 8}
R99 TICK-15 edge clerk-lapse-recorded -> clerk-filing-open pinned
DIFF PASS: r99 pin added; six existing pins unchanged; only other change is tool-managed top-level revision
```

Report-only QA correction: the first report-integrity `python3 -` script verified all seven quoted live receipts, then found a truncated transcription of the relations digest above. Its output was `REPORT RECEIPTS 7/7 match live verification stdout`, followed by `REPORT MALFORMED SHA256 TOKENS [('c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4a6ff9', 55)]`; it exited 1 on the assertion. I corrected the report to the actual 64-character digest above. Neither the contract nor any fixture was changed by this correction; the original file-hash verification itself was green.

## 4. Tick-15 negative control and isolated regression suite

The scratch mirror was created by copying the delivered tool, contract, and r95/r99 fixtures. The live tool and contract match those mirror copies byte-for-byte; actual verification command:

```sh
python3 - <<'PY'
import hashlib
from pathlib import Path
root = Path.cwd().resolve()
assert root == Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
scratch = root / '.ufo/waves/round-100/seats/T1-scratch'
for name in ['dependency_freeze.py', 'dependency-freeze-contract.json']:
    live = (root / 'corpus/tools' / name).read_bytes()
    assert live == (scratch / 'corpus/tools' / name).read_bytes()
    print(f'BYTE-IDENTICAL {name} sha256 {hashlib.sha256(live).hexdigest()}')
report = root / '.ufo/waves/round-100/seats/T1-chain-seven.md'
assert report.resolve().is_relative_to(root / '.ufo/waves/round-100/seats')
assert not report.exists()
print('RESOLVED REPORT ' + str(report.resolve()))
PY
```

Observed stdout, exit 0 (before report creation; that last nonexistence assertion is intentionally not reusable after creation):

```text
BYTE-IDENTICAL dependency_freeze.py sha256 fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c
BYTE-IDENTICAL dependency-freeze-contract.json sha256 ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
RESOLVED REPORT /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/T1-chain-seven.md
```

Before mutation, actual command:

```sh
python3 .ufo/waves/round-100/seats/T1-scratch/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T1-scratch/corpus/fixtures/r99-window-lapse
```

Observed stdout, exit 0:

```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
```

I used `Read` then `Edit` only on the scratch fixture's `timeline.json`, changing the `clerk-lapse-recorded` event's `depends_on` from `["clerk-filing-open"]` to `[]`. The same actual command then produced exit 1:

```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 6/7; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-lapse-recorded lost depends_on ['clerk-filing-open']
RESULT FAIL
```

This intentional failure is evidence that the formerly unfrozen tick-15 edge is now covered. It is not a delivered-fixture failure; the live seven-fixture replay remained 7/7 clean. As expected from semantic precedence, this mutation prints no `DIGEST-MISMATCH`.

Actual self-test command (byte-identical isolated mirror, so temporary self-test writes stay inside the declared scratch root):

```sh
python3 .ufo/waves/round-100/seats/T1-scratch/corpus/tools/dependency_freeze.py --self-test
```

Observed stdout, exit 0:

```text
CASE clean: exit=0 expected=0 findings=[] ok
CASE reduction_edge_drop: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE addition_edge_phantom: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE event_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE event_endpoint_change: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_endpoint_flip: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE relation_added: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE digest_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
CASE malformed_json: exit=2 expected=2 findings=['MALFORMED-JSON'] ok
CASE missing_timeline: exit=2 expected=2 findings=['FILE-MISSING'] ok
CASE unpinned_fixture: exit=2 expected=2 findings=['UNPINNED-FIXTURE'] ok
CASE missing_fixture: exit=2 expected=2 findings=['FIXTURE-MISSING'] ok
CASE invalid_arguments: exit=2 expected=2 findings=['INVALID-ARGUMENTS'] ok
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
```

The direct live-tree `--self-test` command was not run by this seat: its transient scratch would be outside the seat's declared scratch subtree. The delivered code and contract tested above are byte-identical; the live fixtures were separately exercised directly in section 2.

## 5. Other checks on the delivered revision

Actual commands and observations:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
```

Exit 0, complete stdout:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

```sh
python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
```

Exit 0, complete stdout:

```text
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
```

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
```

Exit 0. Output included all `PASS J01` through `PASS J21` and `PASS S01`/`PASS S02`, with these inventory and terminal receipts (excerpt, not the full per-anchor output):

```text
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
```

```sh
git diff --exit-code fe1ce46 -- corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
```

Exit 0, empty stdout: delivered tool and r99 fixture unchanged from closure.

```sh
git diff --check -- corpus/tools/dependency-freeze-contract.json corpus/tools/README.md SKILL.md
```

Exit 0, empty stdout: no whitespace errors in the three owned tracked deliverables.

```sh
git diff fe1ce46 -- corpus/tools/README.md SKILL.md
```

Exit 0: README is append-only (+60 lines), including the dated Round-100 addendum at line 363; SKILL changes are confined to the dependency-freeze registry at lines 96/99/102. The final documentation/contract assertions printed:

```text
FINAL CONTRACT 7 pins; six prior pins unchanged; non-revision metadata unchanged
FINAL DOC CONTRACT seven registry entries/commands; dated supersession; r99 digest; metadata delta explicit
```

## Boundaries and handoff

C1 coverage is demonstrated on the delivered revision: seven clean chain receipts; r99 ten-file payload schema 2; tick-15 edge pinned and its removal detected; every prior pin preserved. The tool-managed top-level revision refresh is the only non-addition contract delta and needs to remain explicitly qualified if the parent describes the diff. Do not re-freeze the delivered contract merely to verify it.

No claim is made about C2/C3, semantic entailment, testimony truth, chronology authentication, source authenticity, rights, permission, or canon. `r100-docket-review` is not in the frozen set, and r88's `symbolism-clause-map.md` remains outside the ten declared pinned files. Those are bounds, not contradictory green receipts.

PASS — r99 guarded pin added; seven live fixtures clean; six existing pins unchanged; schema-2 ten-file payload and tick-15 reduction detection verified; dated documentation updated; top-level revision refresh disclosed.
