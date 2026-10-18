# V08 c1-negative-rerun — round 99

Seat: V08 c1-negative-rerun (verifier). Lane `/home/vgpnk/Projects/shokunin/lore-shokunin`. Commands from the lane root or a scratch mirror, `python3` only. No commits, no pushes, no network, no nested agents. Writes: this report and `.ufo/waves/round-99/seats/V08-scratch/` only.

Axes for this seat: class coverage (every listed exit class), ID stability (twice each), evidence fidelity (quoted commands and outputs), non-interference (scratch mirrors only).

Delivered revision, snapshotted at POLL_HIT and unchanged at the end of the battery and again at report time:

- `corpus/tools/dependency_freeze.py` sha256 `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`
- `corpus/tools/dependency-freeze-contract.json` sha256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`
- contract `schema_version` 2, `payload_schema_version` 2
- pins: `r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`, `r97-crossing-acknowledgment`, `r98-clerk-filing` (no `r99-window-lapse`)
- producer report: `.ufo/waves/round-99/seats/S1-full-file-pins.md`

Baseline control bytes from `git archive 4265df5e86e4121bde4125b649b89bb1676676a5`: tool `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`, contract `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`.

## 1. Poll-wait

20 s cadence. Hit required an `S1-*.md` or `S1.md` report plus three consecutive identical tool+contract shas. A report was not treated as optional.

```
POLL_START 2026-10-17 22:03:58 -03
try=1  t=22:03:58 report=none tool=changed contract=same    toolsha=1728ed89… ctsha=153ebc5b…
try=2  t=22:04:18 report=none tool=changed contract=changed toolsha=1728ed89… ctsha=73b28933…
try=3  t=22:04:38 report=none tool=changed contract=changed toolsha=1728ed89… ctsha=8f9c1f53…
try=12 t=22:07:38 report=none tool=changed contract=changed toolsha=6f81f8be… ctsha=8f9c1f53…
try=15 t=22:08:38 report=none tool=changed contract=changed toolsha=6f81f8be… ctsha=8f9c1f53…
```

The first poller was killed by this seat's 300 s tool timeout after try 15 (not a protocol miss of the producer). Resume:

```
POLL_RESUME 2026-10-17 22:30:00 -03 from_try=16 reason=prior-poller-killed-at-tool-timeout-after-try-15
try=16 t=22:30:00 report=none toolsha=6f81f8be… ctsha=8c2561b0…
try=40 t=22:38:00 report=none toolsha=6f81f8be… ctsha=8c2561b0…
POLL_ABSENT tries=40
```

Stall-escape, recorded: at 22:43 the tool sha had moved to `fb9bb9ff…` (mtime 22:38:11, 11 s after try 40) and `S1-scratch` had new directories. Producer still writing, so absence was not inferred from the exhausted budget.

```
STALL_ESCAPE_START 2026-10-17 22:50:55 -03 tries=41-60 reason=producer-still-writing-at-try-40 tool_mtime_after_deadline
escape try=41 t=22:50:55 report=…/seats/S1-full-file-pins.md toolsha=fb9bb9ff… ctsha=8c2561b0…
STAB i=41 sha=67d630b3… stable=0
STAB i=42 sha=67d630b3… stable=1
STAB i=43 sha=67d630b3… stable=2
POLL_HIT try=43 report=…/seats/S1-full-file-pins.md tool=fb9bb9ff… contract=8c2561b0…
POLL_STABLE sha=67d630b30cd0622820006fb5679462341b8d5224b8d6730dde9937f5654f1f05
```

No final battery run was taken before that hit. Full poll log: `.ufo/waves/round-99/seats/V08-scratch/poll.log`.

## 2. Method

Harness `.ufo/waves/round-99/seats/V08-scratch/battery.py`. Each case is a fresh mirror: tool and contract copied under `corpus/tools/`, fixture copied to the pin's repo-relative path, so `ROOT` is the mirror and the live tree is not mutated. Every case ran twice. Pass required exit, finding-ID list, and (for digest rows) the mutated filename in the finding detail, with no traceback. Full transcript: `V08-scratch/after/log.txt` and `after/summary.json`.

Subject for the required matrix: `r95-crossing-aftermath` (self-test base). Clean control on the snapshot matched S1's r95 digest `97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710`.

57/57 rows `MATCH`, run1 stdio byte-identical to run2 (`bad=0` from `summary.json`). Live tool and contract shas at battery end and at report time equal the POLL_HIT shas (`DRIFT tool=False contract=False`). `LANE_SELF_TEST_RESIDUE []`.

## 3. Before (baseline `4265df5`, scratch only)

Same first-word removal later used on the delivered tool. Five markdown edits stayed invisible; a JSON newline was already `DIGEST-MISMATCH`. Twice each, stdio identical.

```
$ python3 …/before/cases/md-fictional-excerpts.md/corpus/tools/dependency_freeze.py …/corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
EXIT=0
FINDINGS=[]
```

Same exit 0 / same digest / empty findings for `README.md`, `claim-excerpt-map.md`, `inspiration-note.md`, `source-excerpt.md`.

```
$ python3 …/before/cases/json-timeline/corpus/tools/dependency_freeze.py …/corpus/fixtures/r95-crossing-aftermath
FINDING DIGEST-MISMATCH: content digest c7c29b5e… != pin d541ae64…; changed: timeline.json (sha256 3c0faad6… -> bd64e666…); fixture bytes changed outside the frozen inventory
RESULT ERROR
EXIT=2
```

This is a different prose edit from S1's J14 sentence swap. It shows the old freeze did not see a markdown byte edit. It does not re-test `support_check`.

## 4. Delivered matrix (r95 mirror, twice each)

Tool path pattern: `python3 V08-scratch/after/cases/<case>/corpus/tools/dependency_freeze.py <args>`. Run1 stdout below; run2 byte-identical in every row.

**Exit 1 — REDUCTION / ADDITION / ENDPOINT**

```
$ …/reduction_edge_drop/…/dependency_freeze.py …/corpus/fixtures/r95-crossing-aftermath
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
EXIT=1

$ …/reduction_event_removed/…
FINDING REDUCTION-DETECTED: event paired-crossing-decision is missing; 2 frozen dependency edge(s) gone
RESULT FAIL
EXIT=1

$ …/reduction_relation_removed/…
FINDING REDUCTION-DETECTED: relation edge(s) removed: [aru, evin, agreed_co_stewardship_for_this_crossing]
RESULT FAIL
EXIT=1

$ …/addition_edge_phantom/…
FINDING ADDITION-DETECTED: event aru-ninth-bell gained depends_on ['phantom-v08-edge']
RESULT FAIL
EXIT=1

$ …/addition_relation_added/…
FINDING ADDITION-DETECTED: relation edge(s) added: [v08-a, v08-b, v08_unpinned]
RESULT FAIL
EXIT=1

$ …/addition_unpinned_event/…
FINDING ADDITION-DETECTED: unpinned event v08-unpinned-event introduces depends_on ['aru-ninth-bell']
RESULT FAIL
EXIT=1

$ …/endpoint_event/…
FINDING ENDPOINT-CHANGE: event aru-ninth-bell.place_id: 'quiet-rise' -> 'v08-other-place'
RESULT FAIL
EXIT=1

$ …/endpoint_relation_flip/…
FINDING ENDPOINT-CHANGE: relation endpoints changed: removed [aru, evin, agreed_co_stewardship_for_this_crossing]; added [evin, aru, agreed_co_stewardship_for_this_crossing]
RESULT FAIL
EXIT=1
```

Precedence (edge drop plus a README trailing newline) stayed exit 1 and did not emit `DIGEST-MISMATCH`:

```
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
EXIT=1
```

Mirror contract sha unchanged on the semantic rows that recorded it.

**Exit 2 — DIGEST-MISMATCH, JSON class (trailing newline; inventory unchanged)**

Each names only that file. Pin digest `97cffd7b…`.

```
entities.json        changed: entities.json (sha256 026af0bc… -> 3489f303…)
relations.json       changed: relations.json (sha256 c279254b… -> 81114412…)
timeline.json        changed: timeline.json (sha256 3c0faad6… -> bd64e666…)
sources.json         changed: sources.json (sha256 fd9e30e8… -> ab82a3e1…)
contradictions.json  changed: contradictions.json (sha256 37517e5f… -> 5239a775…)
```

Representative:

```
$ …/digest_json_timeline.json/…/dependency_freeze.py …/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest f79cefa3… != pin 97cffd7b…; changed: timeline.json (sha256 3c0faad6… -> bd64e666…); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT=2
```

**Exit 2 — DIGEST-MISMATCH, each Markdown class (first 4-letter word removed)**

```
README.md              removed 'Round'     changed: README.md (sha256 9d27af4a… -> 14b1b48c…)
claim-excerpt-map.md   removed 'crossing'  changed: claim-excerpt-map.md (sha256 80440d61… -> 78591a9d…)
fictional-excerpts.md  removed 'Authored'  changed: fictional-excerpts.md (sha256 0ef6734a… -> 3870e103…)
inspiration-note.md    removed 'Sourced'   changed: inspiration-note.md (sha256 58f5390e… -> 1b061a21…)
source-excerpt.md      removed 'Delivered' changed: source-excerpt.md (sha256 b5edc2fd… -> c1ecd106…)
```

Representative:

```
$ …/digest_md_fictional-excerpts.md/…/dependency_freeze.py …/r95-crossing-aftermath
FINDING DIGEST-MISMATCH: content digest 61db89ac… != pin 97cffd7b…; changed: fictional-excerpts.md (sha256 0ef6734a… -> 3870e103…); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT=2
```

Same ID, exit, and filename-in-detail for the other four. Before, the same class of edit exited 0.

**Exit 2 — other accumulated classes**

```
$ …/file_missing_timeline/…/dependency_freeze.py …/r95-crossing-aftermath
FINDING FILE-MISSING: timeline.json is missing from …/r95-crossing-aftermath
RESULT ERROR
EXIT=2

$ …/malformed_json/…
FINDING MALFORMED-JSON: timeline.json: Expecting property name enclosed in double quotes: line 2 column 1 (char 3)
RESULT ERROR
EXIT=2

$ …/malformed_json_utf8/…
FINDING MALFORMED-JSON: timeline.json is not UTF-8: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
RESULT ERROR
EXIT=2

$ …/scope_refused_outside/…/dependency_freeze.py --freeze …/outside-scope/target
FINDING SCOPE-REFUSED: --freeze refuses …/outside-scope/target (resolves to …/outside-scope/target); the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR
EXIT=2

$ …/scope_refused_root/…/dependency_freeze.py --freeze …/corpus/fixtures
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures itself; the frozen scope is corpus/fixtures/**
RESULT ERROR
EXIT=2

$ …/scope_refused_same_name/…/dependency_freeze.py --freeze …/corpus/fixtures/nested/r95-crossing-aftermath
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/nested/r95-crossing-aftermath: pin r95-crossing-aftermath already names 'corpus/fixtures/r95-crossing-aftermath'; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR
EXIT=2

$ …/path_mismatch/…/dependency_freeze.py …/foreign/r95-crossing-aftermath
FINDING PATH-MISMATCH: pin r95-crossing-aftermath names corpus/fixtures/r95-crossing-aftermath (resolves to …/corpus/fixtures/r95-crossing-aftermath); invoked fixture resolves to …/foreign/r95-crossing-aftermath
RESULT ERROR
EXIT=2

$ …/invalid_none/…/dependency_freeze.py
FINDING INVALID-ARGUMENTS: expected a fixture directory, --freeze DIR, or --self-test
RESULT ERROR
EXIT=2

$ …/invalid_both/…/dependency_freeze.py <fixture> --freeze <fixture>
FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both
RESULT ERROR
EXIT=2

$ …/invalid_selftest/…/dependency_freeze.py --self-test <fixture>
FINDING INVALID-ARGUMENTS: --self-test cannot be combined with a fixture or --freeze
RESULT ERROR
EXIT=2
```

SCOPE-REFUSED rows: mirror contract sha unchanged (`contract_unchanged=True`).

**SELF-TEST-MISMATCH exit 2**

Mirror contract only: `self_test.expected.clean.exit := 1`. Then:

```
$ …/self_test_mismatch/…/dependency_freeze.py --self-test
CASE clean: exit=0 expected=1 findings=[] MISMATCH
CASE reduction_edge_drop: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
… (inherited cases ok, including markdown_tamper: exit=2 findings=['DIGEST-MISMATCH'] ok) …
SELF-TEST 17/18
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR
EXIT=2
```

The corrupted expectation is what failed. The other 17 cases, including `markdown_tamper`, stayed ok. Twice, stdio identical.

## 5. Extras (not required for the class list; all MATCH, twice, stdio identical)

`--freeze` of the canonical r95 path with `README.md` deleted, mirror contract unchanged:

```
FINDING FILE-MISSING: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pinned file(s) missing: README.md
RESULT ERROR
EXIT=2
```

Agrees with S1's missing-`inspiration-note.md` freeze probe (same ID and message shape, different file).

Markdown word-removal sweep on the other five pins (25 rows): every one exit 2 `DIGEST-MISMATCH` naming that file. r88 and r98 digests in the finding match S1's receipts (`acf677a7…`, `5ecf84e1…`). r94/r96/r97 likewise `named=True`. Transcript in `after/log.txt`.

Unpinned eleventh file, after the battery, scratch only. `symbolism-clause-map.md` first `the` → `THE` at offset 65 (1094 bytes both, bytes differ). Twice:

```
$ python3 …/after/cases/extra-symbolism/corpus/tools/dependency_freeze.py …/corpus/fixtures/r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
EXIT=0
```

Agrees with S1: that file is outside the declared ten and an edit is invisible to this gate. Not a failure of the ten-file claim. Recorded bound.

## 6. Agreement with S1

No ID or exit disagreement on the classes this seat ran. r95 clean digest `97cffd7b…`, r88 `acf677a7…`, r98 `5ecf84e1…` match S1's re-verify receipts. Semantic findings still decide first (combined mutation exit 1, no digest finding). `SELF-TEST-MISMATCH` is exit 2. Freeze of a fixture missing a declared pinned file is `FILE-MISSING` and does not rewrite the pin.

Not re-run here, so not confirmed by this seat: S1's 18/18 clean `--self-test` on the live tool, the J14 `support_check` exit 1, and the non-anchor heading edit. Those are S1's receipts, not this matrix.

## 7. Hygiene

Mutations and the self-test temp dirs stayed under `V08-scratch`. Live shas `fb9bb9ff…` / `8c2561b0…` before the battery, after it, and at report time. No `dependency-freeze-self-test-*` residue at the lane root.

**Bottom line: PASS** — on the POLL_HIT revision (`fb9bb9ff…` / `8c2561b0…`, report `S1-full-file-pins.md`), the accumulated negative battery on scratch mirrors exited with stable IDs twice each: REDUCTION/ADDITION/ENDPOINT exit 1; SCOPE-REFUSED, PATH-MISMATCH, FILE-MISSING, MALFORMED-JSON, INVALID-ARGUMENTS, and SELF-TEST-MISMATCH exit 2; DIGEST-MISMATCH exit 2 naming each of the five JSON files and each of the five Markdown files. The same Markdown word-removal was exit 0 on the `4265df5` freeze. Stall-escape recorded (report absent at try 40 while S1 was still writing; hit at escape try 43). Bound: `symbolism-clause-map.md` remains edit-invisible.
