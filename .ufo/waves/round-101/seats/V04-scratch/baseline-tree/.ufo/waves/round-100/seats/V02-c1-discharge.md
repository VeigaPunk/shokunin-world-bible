# V02 — C1 r99-bound discharge (2026-10-17)

Axes: **coverage** (the formerly unfrozen tick-15 edge is covered), **calibration** (full-file byte detectability, not semantic truth), **adjacency** (isolated negative controls; no producer-byte writes).

Scope: independently verify the r99 recorded bound at `LOG.md:3317-3319` / round-100 C1 at `LOG.md:3361-3365`. This is a V02-scoped verdict, not an all-claims admission or an independent replay of all seven fixtures.

## Readiness and isolation

The artifact and producer report were both present before any verification replay. Seven numbered artifact probes were made, separated by `sleep 20`; the first matched producer report was on probe 7: `.ufo/waves/round-100/seats/T1-chain-seven.md`. The report was read in full and ended PASS. The r99 pin was present at every numbered probe. No bounded stall-escape or all-reports poll was needed (therefore no SELF-subtraction case).

Declared scratch, resolved beneath the lane root before creation:

`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V02-c1-discharge-scratch/`

Three mirrors (`clean/`, `edge-drop/`, `prose-edit/`) contain byte copies of `corpus/tools/{dependency_freeze.py,dependency-freeze-contract.json}` and the ten files under `corpus/fixtures/r99-window-lapse/`. The copies were prepared while waiting; all verification commands below ran after T1's report appeared. Post-copy assertions verified the copied tools/contracts against the delivered bytes. Each mirror preserves `corpus/fixtures/r99-window-lapse` relative to its own copied checker root; no path guard or pin was modified.

All shell commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` and used `python3`. No `--freeze` was invoked by this verifier. No nested agents, commits, pushes, or network calls.

## Baseline and delivered snapshot audit

Actual baseline command:

```sh
python3 - <<'PY'
import json, subprocess
baseline = subprocess.run(['git', 'show', 'fe1ce46:corpus/tools/dependency-freeze-contract.json'], check=True, capture_output=True, text=True)
contract = json.loads(baseline.stdout)
print('BASELINE fe1ce46 pins=' + str(len(contract['pins'])))
print('BASELINE r99-window-lapse pinned=' + str('r99-window-lapse' in contract['pins']))
PY
```

Observed stdout, exit 0:

```text
BASELINE fe1ce46 pins=6
BASELINE r99-window-lapse pinned=False
```

Actual delivered/scratch comparison command:

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib, json, subprocess
lane = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
scratch = lane / '.ufo/waves/round-100/seats/V02-c1-discharge-scratch'
contract_path = lane / 'corpus/tools/dependency-freeze-contract.json'
contract_raw = contract_path.read_bytes()
contract = json.loads(contract_raw)
baseline = json.loads(subprocess.run(['git', 'show', 'fe1ce46:corpus/tools/dependency-freeze-contract.json'], check=True, capture_output=True, text=True).stdout)
print('delivered_contract_sha256=' + hashlib.sha256(contract_raw).hexdigest())
print('pin_count=' + str(len(contract['pins'])))
print('added_pin_names=' + repr(sorted(set(contract['pins']) - set(baseline['pins']))))
print('other_six_pins_unchanged=' + str(all(contract['pins'][name] == pin for name, pin in baseline['pins'].items())))
pin = contract['pins']['r99-window-lapse']
print('r99_payload_schema_version=' + str(pin['payload_schema_version']))
print('r99_pinned_file_count=' + str(len(pin['files'])))
print('r99_tick15_pin=' + json.dumps(pin['events']['clerk-lapse-recorded'], sort_keys=True))
for case in ('clean', 'edge-drop', 'prose-edit'):
    root = scratch / case
    tool_equal = (root / 'corpus/tools/dependency_freeze.py').read_bytes() == (lane / 'corpus/tools/dependency_freeze.py').read_bytes()
    contract_equal = (root / 'corpus/tools/dependency-freeze-contract.json').read_bytes() == contract_raw
    fixture = root / 'corpus/fixtures/r99-window-lapse'
    changed = [name for name in pin['pinned_files'] if (fixture / name).read_bytes() != (lane / pin['fixture'] / name).read_bytes()]
    print(case + ': tool_byte_identical=' + str(tool_equal) + '; contract_byte_identical=' + str(contract_equal) + '; changed_fixture_files=' + repr(changed))
    assert tool_equal and contract_equal
    assert changed == {'clean': [], 'edge-drop': ['timeline.json'], 'prose-edit': ['fictional-excerpts.md']}[case]
print('SNAPSHOT isolation assertions PASS')
PY
```

Observed stdout, exit 0:

```text
delivered_contract_sha256=ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
pin_count=7
added_pin_names=['r99-window-lapse']
other_six_pins_unchanged=True
r99_payload_schema_version=2
r99_pinned_file_count=10
r99_tick15_pin={"depends_on": ["clerk-filing-open"], "endpoint": {"entity_id": "clerk-maren", "place_id": "chalk-stair", "tick": 15}}
clean: tool_byte_identical=True; contract_byte_identical=True; changed_fixture_files=[]
edge-drop: tool_byte_identical=True; contract_byte_identical=True; changed_fixture_files=['timeline.json']
prose-edit: tool_byte_identical=True; contract_byte_identical=True; changed_fixture_files=['fictional-excerpts.md']
SNAPSHOT isolation assertions PASS
```

The delivered checker hash was independently printed before report creation: `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c` (the report-path preflight also reproduced the contract hash above). T1 discloses the guarded writer's top-level revision refresh; this seat's preservation assertion concerns every field of the six existing **pins**, not an addition-only textual contract diff.

## 1. Delivered r99 and unchanged scratch are clean

Actual command:

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
```

Complete stdout and observed exit:

```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
observed_exit=0
```

Actual unchanged-scratch command:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V02-c1-discharge-scratch/clean/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V02-c1-discharge-scratch/clean/corpus/fixtures/r99-window-lapse
```

Complete stdout and observed exit:

```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
observed_exit=0
```

Actual structural command on the delivered fixture:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
```

Complete stdout and observed exit:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
observed_exit=0
```

## 2. Tick-15 edge-drop control detects the formerly unfrozen edge

Using `Read` then `Edit` on the **scratch** `edge-drop/corpus/fixtures/r99-window-lapse/timeline.json`, changed only the `clerk-lapse-recorded` event's `depends_on` from `["clerk-filing-open"]` to `[]`. The actor, place, tick 15, event ID, source, prose, and every other parsed field stayed unchanged; the specificity assertion below checks this against `fe1ce46`.

Actual command:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V02-c1-discharge-scratch/edge-drop/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V02-c1-discharge-scratch/edge-drop/corpus/fixtures/r99-window-lapse
```

Complete stdout and observed exit:

```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 6/7; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-lapse-recorded lost depends_on ['clerk-filing-open']
RESULT FAIL
observed_exit=1
```

This intentional red result is the required discharge evidence. It is not a delivered-fixture failure. Semantic-inventory precedence is visible: the edge loss produces exit 1 and no `DIGEST-MISMATCH`.

## 3. The ten-file payload catches an r99 fictional-excerpts edit

Using `Read` then `Edit` on **scratch** `prose-edit/corpus/fixtures/r99-window-lapse/fictional-excerpts.md:76`, changed only `and that the matter stands as a historical open entry.` to `and that the matter stands as a historical OPEN entry.` in the final explanatory Scope paragraph. No quoted excerpt or map anchor was changed. The entire JSON inventory is unchanged.

Actual command:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V02-c1-discharge-scratch/prose-edit/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V02-c1-discharge-scratch/prose-edit/corpus/fixtures/r99-window-lapse
```

Complete stdout and observed exit:

```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
FINDING DIGEST-MISMATCH: content digest 7d57b4ed45c9f193e137c07fc9d85564529e9ad52146656a445f457039bdc9a4 != pin 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e; changed: fictional-excerpts.md (sha256 fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d -> d56462d895e0fcd61195ad4a1873d8eb2ebef01e539336890d3089c2f2e83287); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
observed_exit=2
```

Actual lexical-support command on the same tampered scratch fixture:

```sh
python3 corpus/tools/support_check.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V02-c1-discharge-scratch/prose-edit/corpus/fixtures/r99-window-lapse
```

Observed receipt excerpts (the omitted per-row lines were all PASS), exit 0:

```text
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
observed_exit=0
```

Actual obligation-map command on that same fixture:

```sh
python3 corpus/tools/map_obligations.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V02-c1-discharge-scratch/prose-edit/corpus/fixtures/r99-window-lapse
```

Complete stdout and observed exit:

```text
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
observed_exit=0
```

This isolates a non-anchor prose-byte edit caught by the pin while lexical support and map coverage remain green. It establishes byte-change detectability, not that the edited or frozen prose entails the dependency or is true.

## Specificity and preservation checks

Actual command checking the precise negative-control mutations:

```sh
python3 - <<'PY'
from pathlib import Path
import json, subprocess
lane = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
scratch = lane / '.ufo/waves/round-100/seats/V02-c1-discharge-scratch'
base = json.loads(subprocess.run(['git', 'show', 'fe1ce46:corpus/fixtures/r99-window-lapse/timeline.json'], check=True, capture_output=True, text=True).stdout)
edited = json.loads((scratch / 'edge-drop/corpus/fixtures/r99-window-lapse/timeline.json').read_bytes())
expected = json.loads(json.dumps(base))
row = next(row for row in expected if row['id'] == 'clerk-lapse-recorded')
assert row['tick'] == 15 and row['depends_on'] == ['clerk-filing-open']
row['depends_on'] = []
assert edited == expected
print('EDGE CONTROL: parsed baseline equals scratch except tick-15 depends_on [clerk-filing-open] -> []')
original = (lane / 'corpus/fixtures/r99-window-lapse/fictional-excerpts.md').read_text()
prose = (scratch / 'prose-edit/corpus/fixtures/r99-window-lapse/fictional-excerpts.md').read_text()
needle = 'and that the matter stands as a historical open entry.'
assert original.count(needle) == 1
assert prose == original.replace(needle, 'and that the matter stands as a historical OPEN entry.', 1)
print('PROSE CONTROL: only lowercase open -> OPEN on unmapped Scope line 76; quoted excerpt lines unchanged')
print('CONTROL specificity assertions PASS')
PY
```

Complete stdout, exit 0:

```text
EDGE CONTROL: parsed baseline equals scratch except tick-15 depends_on [clerk-filing-open] -> []
PROSE CONTROL: only lowercase open -> OPEN on unmapped Scope line 76; quoted excerpt lines unchanged
CONTROL specificity assertions PASS
```

Actual delivered-preservation command:

```sh
git diff --exit-code fe1ce46 -- corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
```

Exit 0; empty stdout. The delivered checker and r99 fixture remain byte-identical to the closure revision. Every direct Python CLI result above captured `$?` immediately with `rc=$?` and printed it using `python3 -c 'import sys; print("observed_exit=" + sys.argv[1])' "$rc"`; shell assertions required the stated expected status, including the intentional 1/2 negative controls.

## Owned outputs and bounds

Only this report and the declared V02 scratch tree were written. Each of the three mirrors contains these paths: `corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json`, and `corpus/fixtures/r99-window-lapse/{README.md,claim-excerpt-map.md,contradictions.json,entities.json,fictional-excerpts.md,inspiration-note.md,relations.json,source-excerpt.md,sources.json,timeline.json}`. Only the edge-drop timeline and prose-edit excerpt differ from the delivered copies. No producer file, contract pin, or delivered fixture was edited by V02.

No claim is made here about C2/C3 admission, the truth of testimony, chronology authentication, prose entailment, source authenticity, rights, permission, or canon. This seat did not replay the full seven-fixture chain or the general self-test; the narrower C1-bound discharge requested for V02 is fully exercised on the delivered pin and isolated copies.

PASS — r99 is clean; dropping its tick-15 edge produces REDUCTION-DETECTED exit 1, and a fictional-excerpts.md prose edit produces named DIGEST-MISMATCH exit 2 against the delivered schema-2 ten-file pin.
