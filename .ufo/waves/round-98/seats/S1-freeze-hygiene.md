# S1 freeze-hygiene — round 98

- Seat: S1 freeze-hygiene (producer, byte-ownership). Lane repo
  `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline r97 closure `9a3d648`
  (pre-round bytes via `git show 9a3d648:<path>`); the wave tree is uncommitted;
  HEAD during the round `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb`. All commands
  ran from the lane root with `python3`.
- Owned and delivered: `corpus/tools/dependency_freeze.py`
  (sha256 `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`) and
  `corpus/tools/dependency-freeze-contract.json`
  (sha256 `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`).
- Writes: those two files, this report (absolute path), and
  `.ufo/waves/round-98/seats/S1-scratch/`. Leaf seat: no nested agents, no
  commits, no pushes, no network. No other lane file written.

## 0. Poll-wait record (20 s cadence, 40 tries max; never verify a plan)

- ~20:30 first inspection: `corpus/fixtures/r98-clerk-filing/` JSON present
  (mtimes 20:28:24–20:28:55; 6 entities / 1 relation / 7 events / 7 sources,
  tick-14 `clerk-filing-open` depends on `acknowledgment-aru-records`), no
  producer reports in `.ufo/waves/round-98/seats/` (only V15's report).
- 20:31–20:32: `S3-fixture-author.md` and `S4-fixture-docs.md` present → my only
  dependency (S3's fixture + report) satisfied; both freezes ran ~20:33 against
  the on-disk final JSON.
- 20:34: all four other producer reports on disk (`S2-tools-docs.md`,
  `S3-fixture-author.md`, `S4-fixture-docs.md`, `S5-knowledge-notes.md`); S2's
  README round-98 addendum (`corpus/tools/README.md:230-282`) matches my receipts.
- Endgame convention: no all-reports poll was ever needed (my dependency was S3
  alone, satisfied); no stall escape required; no wait exceeded the budget.

## 1. C1(a) — `SELF-TEST-MISMATCH` exits 2, pinned as self-test case 17

Pre-state, quoted from the baseline bytes (`git show 9a3d648:…` copied into
`.ufo/waves/round-98/seats/S1-scratch/preselftest/`, persisted expectation for
`clean` corrupted to `exit: 1`):

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE clean: exit=0 expected=1 findings=[] MISMATCH
…
SELF-TEST 15/16
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT FAIL
EXIT=1
```

Delivered change (`git diff 9a3d648 -- corpus/tools/dependency_freeze.py`):

```
-        emit(1, [("SELF-TEST-MISMATCH", f"cases failed: {sorted(failures)}")])
-        return 1
+        emit(2, [("SELF-TEST-MISMATCH", f"cases failed: {sorted(failures)}")])
+        return 2
```

plus the persisted 17th case `self_test_mismatch`: a mirror root whose contract
copy corrupts the `clean` expectation, run through `--self-test`; expected exit 2
with `SELF-TEST-MISMATCH` (`self_test.expected.self_test_mismatch`). The nested
replay of that case (marked by `DEPENDENCY_FREEZE_SELF_TEST_CHILD` on every case
subprocess) gets the corrupted mirror without the base fixture, so it fails
closed on `FIXTURE-MISSING` before it can replay the case — the corruption
cannot recurse without bound.

Post-state on the delivered bytes:

```
$ python3 corpus/tools/dependency_freeze.py --self-test
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
SELF-TEST 17/17
RESULT PASS
EXIT=0
```

All 16 inherited cases print `ok` (unchanged); `FROZEN_CASES` grew 16 → 17 by
append; the contract's expectation set is exactly the 17 implemented cases.

## 2. C1(b) — a path-less legacy pin is migrated in place by `--freeze`

Scratch mirrors `.ufo/waves/round-98/seats/S1-scratch/{pre,post,post2}/` (tool +
contract + `corpus/fixtures/r95-crossing-aftermath`; the r95 pin's `fixture` key
removed in pre/post, pointed at `corpus/fixtures/r95-crossing-aftermath-copy` in
post2):

```
$ (pre, 9a3d648 bytes) python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs a repo-relative fixture path
RESULT ERROR            EXIT=2
$ (pre) python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r95-crossing-aftermath
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pin r95-crossing-aftermath already names None; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR            EXIT=2
$ (post, delivered bytes) python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r95-crossing-aftermath
MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS             EXIT=0
$ (post) python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
RESULT PASS             EXIT=0
$ (post2) python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r95-crossing-aftermath
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pin r95-crossing-aftermath already names 'corpus/fixtures/r95-crossing-aftermath-copy'; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR            EXIT=2
```

The refusal for a pin that already names a different nonempty path is unchanged;
only the path-less class (absent/`null`/empty `fixture`) migrates.

## 3. C1(c) — contract `precedence` names the full exit-2 order and finding IDs

Delivered text (`corpus/tools/dependency-freeze-contract.json`):

> semantic inventory findings decide first (exit 1: REDUCTION-DETECTED,
> ADDITION-DETECTED, ENDPOINT-CHANGE); a content digest change the frozen
> inventory does not model exits 2 (DIGEST-MISMATCH). Exit-2
> (could-not-evaluate) checks run in this order and the first failing check
> decides: UNPINNED-FIXTURE (no pin for the fixture name) or CONTRACT-INVALID
> (unreadable contract or invalid pin), FIXTURE-MISSING (fixture directory
> absent), PATH-MISMATCH (invoked path differs from the pin's recorded path),
> FILE-MISSING / MALFORMED-JSON / MALFORMED-MODEL (model build), DIGEST-MISMATCH
> (inventory clean, bytes changed outside the frozen inventory),
> INVALID-ARGUMENTS (CLI usage), SELF-TEST-MISMATCH (--self-test observed
> outcome differs from the persisted case expectation); --freeze additionally
> raises SCOPE-REFUSED (target outside corpus/fixtures/**, or a same-named
> in-scope target that would rewrite an existing pin's recorded path). A
> path-less legacy pin is migrated in place by --freeze instead of refused.

## 4. C2 — chain extended to six fixtures; V46's recorded FAIL discharged

Freeze receipts (delivered contract, guarded `--freeze`):

```
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r97-crossing-acknowledgment
FROZEN r97-crossing-acknowledgment: events 6; dependency-edges 5; relations 1
DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
RESULT PASS             EXIT=0
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r98-clerk-filing
FROZEN r98-clerk-filing: events 7; dependency-edges 6; relations 1
DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
RESULT PASS             EXIT=0
```

Chain 6/6 (all `RESULT PASS`, exit 0):

```
r88-m3-maya-cluster          DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279
r94-paired-crossing          DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
r95-crossing-aftermath       DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
r96-crossing-response        DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
r97-crossing-acknowledgment  DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6
r98-clerk-filing             DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
```

The four pre-round digests are byte-identical to the r97 contract's pins (r95's
digest unchanged by S3's map repair — the map is not a pinned data file, matching
S3's `receipt-freeze-r95-after-repair.txt`). The r97 pin's digest equals the
bytes V46 froze in its r97 scratch mirror (`.ufo/waves/round-97/seats/V46-cross-gates.md`
§4: `DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6`).
The r98 pin carries `clerk-filing-open` → `depends_on: ['acknowledgment-aru-records']`,
endpoint `{tick: 14, entity_id: clerk-maren, place_id: chalk-stair}`.

V46 discharge — scratch mirror carrying byte-identical copies of the delivered
tool and contract (contract sha256 `153ebc5b…` equal on both sides) and the r97
fixture at its pinned path; the mutation reproduces V46's exact bytes:

```
$ python3 <mirror>/mutate.py corpus/fixtures/r97-crossing-acknowledgment <S1-scratch>/r97-depdropped acknowledgment-aru-records response-evin-salt-court
event=acknowledgment-aru-records before=['response-evin-salt-court'] after=[]
$ sha256sum <S1-scratch>/r97-depdropped/timeline.json
37a425b97af658d71b8dc8904f43fd75859905bac326489a71adb67004004eb1   # equals V46's recorded sha
$ diff -u corpus/fixtures/r97-crossing-acknowledgment/timeline.json <S1-scratch>/r97-depdropped/timeline.json
@@ -56,9 +56,7 @@
     "tick": 13, "entity_id": "aru", "place_id": "chalk-stair",
-    "depends_on": [
-      "response-evin-salt-court"
-    ],
+    "depends_on": [],
$ python3 <mirror>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r97-crossing-acknowledgment   # intact
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
RESULT PASS             EXIT=0
$ python3 <mirror>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r97-crossing-acknowledgment   # mutated
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5; relations 1/1
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
RESULT FAIL             EXIT=1
```

V46's bar is now met against the delivered pin: the r97 tick-13 edge is frozen
and the drop is caught as BR-01 (`REDUCTION-DETECTED`, edge count 4/5). The other
three gates on the same mutated bytes stay green, as V46 recorded:

```
check_bible.py     CLEAN: schema, citations, relations, timeline; 0 violations      EXIT=0
support_check.py   … 17/17; 2/2; 19/19 / RESULT PASS                                EXIT=0
map_obligations.py OBLIGATIONS raw=17 mapped=17 / RESULT PASS                       EXIT=0
```

Same-named mutated copy at a foreign path with the delivered tool still exits 2
`PATH-MISMATCH` (the r97 guard, unchanged).

## 5. Inherited behavior and boundaries

- 16 inherited self-test cases: all `ok` in the 17/17 run above; no case removed
  or re-pointed; the same-named-elsewhere refusal retained (post2 above).
- Chain behavior: the four pre-round fixtures verify at their r97 pins with
  identical digests; the two new pins are additive.
- Bounds: pins cover the five JSON tables only (fixture Markdown unpinned, as at
  r97); the migration covers path-less pins only; BR-01's markdown/prose half
  remains open; `--self-test` scratch stays at the repo root (gitignored
  `*-self-test-*/`, BR-05 residual unchanged).

## 6. Write audit

- Final `git status --porcelain` shows, besides my two owned files, only other
  seats' declared paths (`r95-crossing-aftermath/claim-excerpt-map.md`,
  `r95-aftermath-scope-note.md`, `r96-response-scope-note.md`,
  `corpus/tools/README.md`, `LOG.md`, untracked `r98-clerk-filing/`,
  `r98-clerk-scope-note.md`, `.ufo/waves/round-98/`). `git diff 9a3d648 --
  corpus/tools/` lists only `dependency_freeze.py` and
  `dependency-freeze-contract.json`; `map_obligations.py`,
  `map-obligations-contract.json`, `support_check.py`, `boundary_doc_check.py`
  are byte-unchanged. `__pycache__/` is gitignored.
- Not mine, recorded: S3's report item D5 notes an untracked `baseline-analyze.txt`
  in `/home/vgpnk/Projects/shokunin` (the r94-F01 stray-write class) written by an
  unattributed seat; I wrote nothing outside the lane.

## Bottom line

**PASS** — C1(a) `SELF-TEST-MISMATCH` exits 2 and is pinned as persisted case 17
(pre-state exit 1 vs delivered exit 2 both quoted; 16 inherited cases unchanged);
C1(b) a path-less legacy pin migrates in place via `--freeze` (`MIGRATED …` then
PASS; the different-path refusal retained); C1(c) the contract precedence text
names the full exit-2 order and finding IDs; C2 pins r97 (`3c922d20…`) and r98
(`59a0f4fa…`) through the guarded `--freeze`, the chain verifies 6/6 clean, and
V46's discharge reproduces on its exact mutation bytes (`REDUCTION-DETECTED`,
exit 1; other gates green); `--self-test 17/17` `RESULT PASS` exit 0 on the
delivered revision.
