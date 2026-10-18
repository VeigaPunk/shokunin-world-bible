# V23 — COVERAGE verdict (2026-10-17)

**COVERAGE: improved, bounded — C1 PASS.** The frozen chain grows from six to exactly seven fixtures, with seven independently replayed clean receipts. The previously unfrozen r99 tick-15 edge is pinned; deleting it in V23-owned scratch produces the expected reduction failure. Every field of all six inherited pins is preserved. This is one coverage verdict, not a C2/C3 or overall-round admission.

Axes: coverage (primary), preservation of existing coverage, and calibration of the verdict's byte/semantic bounds. Baseline `fe1ce46`; observed live HEAD `b5fe472957ab1e4e9c90f5613acc14cd24a288ae` (round-100 declaration). All commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`, using `python3` for Python.

## Readiness and C1-seat reconciliation

Read `LOG.md:3317-3319` and `3361-3365`, T1's complete producer report, and all four C1 verifier reports:

- `T1-chain-seven.md:29-43`: the producer's authorized live `python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r99-window-lapse`, exit 0, with the r99 digest reproduced below.
- `V01-c1-chain.md:69-219`: seven live clean receipts, ten independent r99 file hashes, six unchanged inherited pins, and the top-level revision qualification.
- `V02-c1-discharge.md:136-208`: tick-15 removal yields `REDUCTION-DETECTED` exit 1; a non-anchor excerpt edit yields named `DIGEST-MISMATCH` exit 2 while lexical/map gates remain green.
- `V03-c1-negative.md:29-68,90-103`: its `python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/run_negative_battery.py` returned exit 0 with `cases=73`, `runs=146`, `matching_cases=73`, `failed_case_ids=[]`; its quoted tick-15 control agrees with V23's own control below. These broader battery results are attributed to V03, not represented as V23 executions.
- `V04-c1-code-review.md:7-13,158-188`: unchanged executable, exact writer serialization, freeze-scoped documentation changes, and the same revision qualification.

No contradictory C1 finding was present. All reports identify contract SHA-256 `ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5` and checker SHA-256 `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`, matching V23's independently observed snapshot.

The initial seats-directory listing exited 2 because the directory did not yet exist; this was startup absence, not a fixture failure. A bounded Python readiness poll required both the seven-pin/ten-file r99 artifact and a `T1*.md` producer report, sleeping 20 seconds between attempts, maximum 40. Observed completion:

```text
POLL attempt=1/40 artifact=True producer_reports=[]
[attempts 2–8: artifact=True, producer_reports=[]]
POLL attempt=9/40 artifact=True producer_reports=['T1-chain-seven.md']
READY: C1 artifact and T1 producer report exist
```

Only after readiness did V23 execute the independent replays. A separate 20-second/40-attempt report poll completed on attempt 5 with `V01-c1-chain.md`, `V02-c1-discharge.md`, `V03-c1-negative.md`, and `V04-c1-code-review.md` present, after which all four were read in full. This was a first-verifier-group poll, not an all-reports poll; SELF was nevertheless explicitly excluded. No stall-escape was needed. Both polling tasks completed exit 0; none remains running.

## Independent seven-fixture replay

Actual wrapper command, exit 0:

```sh
python3 .ufo/waves/round-100/seats/V23-scratch/replay.py
```

The wrapper uses seven concurrent real CLI subprocesses on the delivered fixtures, not imports or mock calls. Full commands and stdout for the seven calls (all stderr empty):

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
CHAIN 7/7
```

The same wrapper independently compares `git show fe1ce46:corpus/tools/dependency-freeze-contract.json` with the current parsed contract. Observed comparison fields:

```text
new_pin_names: ["r99-window-lapse"]
removed_pin_names: []
unchanged_prior_pins: all six true
other_top_level_changes (excluding pins and revision): []
tool_unchanged_from_fe1ce46: true
R99 counts: dependency_edges=7, entities=6, events=8, relations=1, sources=8
R99 payload_schema_version: 2
R99 terminal edge: {"depends_on": ["clerk-filing-open"], "endpoint": {"entity_id": "clerk-maren", "place_id": "chalk-stair", "tick": 15}}
LIVE_INPUTS_STABLE True
V23_INDEPENDENT_REPLAY PASS
```

The exact commands, full outputs, comparison object, and all 72 input fingerprints are persisted in `V23-scratch/replay.json`; the executable wrapper is `V23-scratch/replay.py`. The wrapper is deliberately one-shot: it refuses to overwrite an existing reconstruction directory. The seven individual live commands remain reusable read-only checks.

## Guarded-result reproduction and regression check

V23 did not run `--freeze` against the delivered contract. In exclusive scratch, it copied the unchanged delivered checker, the baseline six-pin contract from `fe1ce46`, and the r99/r95 fixture bytes. Actual guarded command:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V23-scratch/guarded-reconstruction/corpus/tools/dependency_freeze.py --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V23-scratch/guarded-reconstruction/corpus/fixtures/r99-window-lapse
```

Complete observed stdout, exit 0:

```text
FROZEN r99-window-lapse: events 8; dependency-edges 7; relations 1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
```

Wrapper observation: `GUARDED_RECONSTRUCTION_BYTE_IDENTICAL True`. The full reproduced contract, including tool-managed revision metadata, equals the delivered contract byte-for-byte. This independently establishes consistency with the guarded writer; the historical claim that T1 used only that route remains producer attestation, not retrospective observation of its subprocess.

Actual isolated self-test command:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V23-scratch/guarded-reconstruction/corpus/tools/dependency_freeze.py --self-test
```

Observed exit 0, eighteen `CASE ... ok` lines, including `markdown_tamper`, followed by:

```text
SELF-TEST 18/18
RESULT PASS
```

Complete eighteen-case output is in `replay.json`. The delivered code and contract are byte-identical to this mirror. A direct live-root self-test was not run because its temporary trees would fall outside V23's exclusive write scope; all self-test writes here stayed in the owned mirror and were cleaned automatically.

## Independent tick-15 control and explicit unpinned bound

After the clean reconstruction and self-test, V23 used `Read` then `Edit` only on its scratch `r99-window-lapse/timeline.json`, changing the terminal `clerk-lapse-recorded.depends_on` from `["clerk-filing-open"]` to `[]`. Actual command:

```sh
python3 .ufo/waves/round-100/seats/V23-scratch/guarded-reconstruction/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/V23-scratch/guarded-reconstruction/corpus/fixtures/r99-window-lapse
```

Complete observed stdout, exit 1:

```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 6/7; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-lapse-recorded lost depends_on ['clerk-filing-open']
RESULT FAIL
```

This intentional failure discharges the r99 recorded unfrozen-edge bound. It is not a delivered-fixture failure. Semantic precedence explains the absence of `DIGEST-MISMATCH`. The scratch mirror is intentionally left in this red-control state; the clean replay record predates that mutation. A subsequent live snapshot comparison printed `POST-NEGATIVE_LIVE_INPUT_CHANGES []`.

Actual bound probe:

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r100-docket-review
```

Complete observed stdout, exit 2:

```text
FINDING UNPINNED-FIXTURE: no pin for 'r100-docket-review' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing', 'r99-window-lapse'])
RESULT ERROR
```

This is an explicit bound, not a C1 failure: C1 declares seven fixtures through r99, not an eighth r100 pin.

## Final preservation and snapshot audit

Actual commands:

```sh
git diff --exit-code fe1ce46 -- corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r94-paired-crossing corpus/fixtures/r95-crossing-aftermath corpus/fixtures/r96-crossing-response corpus/fixtures/r97-crossing-acknowledgment corpus/fixtures/r98-clerk-filing corpus/fixtures/r99-window-lapse
git diff --check -- corpus/tools/dependency-freeze-contract.json corpus/tools/README.md SKILL.md
```

Both exited 0 with empty stdout/stderr. `git diff fe1ce46 -- corpus/tools/dependency-freeze-contract.json` had exactly the r99 addition and the top-level revision refresh, not an inherited-pin change. **Do not describe the entire JSON diff as addition-only.** The guarded writer refreshes `revision` from `337f0fa52b02626b7687eedbb2d99fab30446fe4` to `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`. This is disclosed in the delivered README:389 and SKILL.md:99; no corrective hand-edit is appropriate.

Actual final read-only audit command:

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib,json,subprocess
root=Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
assert Path.cwd().resolve()==root
scratch=root/'.ufo/waves/round-100/seats/V23-scratch'
report=root/'.ufo/waves/round-100/seats/V23-verdict-coverage.md'
assert report.resolve()==report and report.parent.resolve()==root/'.ufo/waves/round-100/seats'
assert not report.exists()
record=json.loads((scratch/'replay.json').read_text())
changed=[rel for rel,digest in record['input_fingerprints'].items() if hashlib.sha256((root/rel).read_bytes()).hexdigest()!=digest]
assert not changed
current=json.loads((root/'corpus/tools/dependency-freeze-contract.json').read_text())
baseline=json.loads(subprocess.check_output(['git','show','fe1ce46:corpus/tools/dependency-freeze-contract.json']))
assert [key for key in sorted(current) if current[key]!=baseline[key]]==['pins','revision']
assert all(current['pins'][name]==pin for name,pin in baseline['pins'].items())
pin_matches=0
for pin in current['pins'].values():
    for name,digest in pin['files'].items():
        assert hashlib.sha256((root/pin['fixture']/name).read_bytes()).hexdigest()==digest
        pin_matches+=1
print(f'FINAL_SNAPSHOT {len(record["input_fingerprints"])}/72 live inputs unchanged; {pin_matches}/70 pinned-file digests match')
print('ROOT_CHANGED_FIELDS pins,revision; six inherited pins unchanged')
print('ROOT_REVISION',baseline['revision'],'->',current['revision'])
for name in ['T1-chain-seven.md','V01-c1-chain.md','V02-c1-discharge.md','V03-c1-negative.md','V04-c1-code-review.md']:
    path=report.parent/name
    assert path.is_file()
    print('READ_C1_REPORT_SHA256',name,hashlib.sha256(path.read_bytes()).hexdigest())
print('CONTRACT_SHA256',hashlib.sha256((root/'corpus/tools/dependency-freeze-contract.json').read_bytes()).hexdigest())
print('REPORT_WRITE_RESOLVED',report.resolve())
print('SCRATCH_PERSISTENT_FILES',sum(p.is_file() for p in scratch.rglob('*')))
print('FINAL_READ_ONLY_AUDIT PASS')
PY
```

Complete observed stdout, exit 0:

```text
FINAL_SNAPSHOT 72/72 live inputs unchanged; 70/70 pinned-file digests match
ROOT_CHANGED_FIELDS pins,revision; six inherited pins unchanged
ROOT_REVISION 337f0fa52b02626b7687eedbb2d99fab30446fe4 -> b5fe472957ab1e4e9c90f5613acc14cd24a288ae
READ_C1_REPORT_SHA256 T1-chain-seven.md 0bdb417bdb792fc8f1385c70424a70b06adc5bde472e15238a85987e6076d7b0
READ_C1_REPORT_SHA256 V01-c1-chain.md f1481c4434a3934b157a0d3662bb54643c8a3003ef0b6bffe1ea3ca2b2e2aff1
READ_C1_REPORT_SHA256 V02-c1-discharge.md 8382d7f839bb51c92583ed2be3d340ec46adaf9f36dd7482112222ba2d8c5ed8
READ_C1_REPORT_SHA256 V03-c1-negative.md fb1025cdbe782ea3d043db258087b0f65629e41b4f83d08a07e292e24140d3a2
READ_C1_REPORT_SHA256 V04-c1-code-review.md 44b94d19b92899c729d7624c822c4292cd4fb2fc368a413a3a8b2b940bb7ea02
CONTRACT_SHA256 ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
REPORT_WRITE_RESOLVED /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V23-verdict-coverage.md
SCRATCH_PERSISTENT_FILES 24
FINAL_READ_ONLY_AUDIT PASS
```

The report-nonexistence assertion was run before this report was created and is intentionally not reusable afterward.

## Owned files and remaining bounds

Only this exclusive report and the declared absolute scratch root `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V23-scratch/` were written. Its 24 persistent files are:

- `replay.py` and `replay.json`.
- `guarded-reconstruction/corpus/tools/{dependency_freeze.py,dependency-freeze-contract.json}`.
- `guarded-reconstruction/corpus/fixtures/r95-crossing-aftermath/{README.md,claim-excerpt-map.md,contradictions.json,entities.json,fictional-excerpts.md,inspiration-note.md,relations.json,source-excerpt.md,sources.json,timeline.json}`.
- `guarded-reconstruction/corpus/fixtures/r99-window-lapse/{README.md,claim-excerpt-map.md,contradictions.json,entities.json,fictional-excerpts.md,inspiration-note.md,relations.json,source-excerpt.md,sources.json,timeline.json}`; only this scratch timeline was edited for the red control.

No delivered bytes were changed by V23. No nested agents, commits, pushes, or network. No unresolved C1 execution failure remains. Expected red controls are recorded verbatim rather than suppressed.

Coverage is limited to these seven path-bound snapshots and ten declared files each. r88's extra `symbolism-clause-map.md` remains outside that file set, and r100 is unpinned. Byte agreement and change detection do not establish dependency semantics, prose entailment, testimony truth, chronology authentication, source authenticity, rights, permission, or canon. No C2/C3 verdict or claim of whole-round admission is made.

PASS — COVERAGE improved from six to seven clean frozen fixtures; r99 tick-15 bound discharged; all six inherited pins preserved; guarded revision refresh, unpinned r100, and semantic/non-establishment bounds explicit.
