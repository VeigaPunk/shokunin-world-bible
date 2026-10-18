# V07 c2-refreeze-scope — round 98

- Seat: V07 c2-refreeze-scope (verifier, leaf). Lane repo
  `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline r97 closure `9a3d648`
  (pre-round contract bytes: `git show 9a3d648:corpus/tools/dependency-freeze-contract.json`,
  copied to seat scratch); wave tree uncommitted; HEAD during the round
  `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb` (verified `git rev-parse HEAD`).
- Seat bar: after S1, the contract diff vs `9a3d648` is only the two new pins +
  self-test/expectation changes + precedence text; no other pin touched; the
  r96 pin's revision field unchanged this round.
- Delivered revision under test (measured 20:36, stable since 20:33:36;
  S1-freeze-hygiene.md declares the same):
  - `corpus/tools/dependency-freeze-contract.json` sha256
    `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`
  - `corpus/tools/dependency_freeze.py` sha256
    `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`
- Poll-wait record (20 s cadence, max 40; artifacts AND producer report):
  try=1 (20:28:50) r98 fixture already on disk, contract unchanged; try=9
  (20:31:30) contract changed (interim: precedence + self-test only); try=17–20
  contract settled after the provenance_note extension; try=21 (20:35:30)
  `S1-freeze-hygiene.md` present → READY. No stall escape needed; no all-reports
  poll required (my dependency was S1 alone).
- Writes: this report (absolute path) and `.ufo/waves/round-98/seats/V07-scratch/`
  only. Two ephemeral `/tmp` helper files created early
  (`/tmp/V07-contract-baseline.json`, `/tmp/V07-show-err.txt`) were deleted at
  20:36; nothing in the lane tree outside the scratch dir. Leaf seat: no nested
  agents, no commits, no pushes, no network.

## 1. Contract diff vs 9a3d648 — exact changed-path inventory

Command: `git diff 9a3d648 -- corpus/tools/dependency-freeze-contract.json`
(saved: `V07-scratch/contract-gitdiff-final.txt`), plus a deep JSON-path walk
(`V07-scratch/diff_contract.py`, saved `V07-scratch/final-diff.txt`).

The diff is exactly 4 hunks, 6 changed JSON paths, 0 unexpected beyond those:

| # | hunk | changed JSON path | classification |
|---|------|-------------------|----------------|
| 1 | `@@ -2,7 +2,7 @@` | `precedence` | declared (C1c) |
| 2 | `@@ -19,7 +19,7 @@` | `revision` (top level) | non-pin, freeze-mechanical (see §3) |
| 3 | `@@ -253,6 +253,186 @@` (+180/−0) | `pins.r97-crossing-acknowledgment`, `pins.r98-clerk-filing` | declared (C2) |
| 4 | `@@ -367,8 +547,15 @@` (+8/−1) | `self_test.expected.self_test_mismatch`; `provenance_note` | declared (C1a) / non-pin changelog (see §3) |

No hunk intersects lines 24–252 (the r88/r94/r95/r96 pin blocks) or lines
258–370 (the 16 inherited self-test expectations): those regions are
**byte-identical**, not merely semantically equal.

### 1a. No other pin touched; r96 revision unchanged

From the deep walk on the settled bytes:

```
=== r96 pin revision field ===
baseline r96 revision: 2393934237ea076366f3db6dceeff033edb52ab1
current  r96 revision: 2393934237ea076366f3db6dceeff033edb52ab1
UNCHANGED: True

=== existing pins deep-equality (r88, r94, r95, r96) ===
r88-m3-maya-cluster: byte-identical JSON value: True
r94-paired-crossing: byte-identical JSON value: True
r95-crossing-aftermath: byte-identical JSON value: True
r96-crossing-response: byte-identical JSON value: True
```

### 1b. The two new pins — shape, paths, revisions, independent recomputation

```
r97-crossing-acknowledgment: fixture=corpus/fixtures/r97-crossing-acknowledgment
  revision=dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb
  counts={'events': 6, 'dependency_edges': 5, 'relations': 1, 'entities': 5, 'sources': 6}
r98-clerk-filing: fixture=corpus/fixtures/r98-clerk-filing
  revision=dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb
  counts={'events': 7, 'dependency_edges': 6, 'relations': 1, 'entities': 6, 'sources': 7}
```

Both fixture paths are repo-relative and inside `corpus/fixtures/**`; both
revisions equal HEAD during the uncommitted wave (`dd4df1b…`), consistent with
the freeze mechanism (§3). A standalone recomputation of the tool's own digest
scheme (`V07-scratch/recompute_pin.py`, no tool import) compared against each
pin — all five fields match for both pins:

```
=== r97-crossing-acknowledgment (corpus/fixtures/r97-crossing-acknowledgment) ===
  content_sha256: MATCH=True   files: MATCH=True   events: MATCH=True
  relations: MATCH=True   counts: MATCH=True
=== r98-clerk-filing (corpus/fixtures/r98-clerk-filing) ===
  content_sha256: MATCH=True   files: MATCH=True   events: MATCH=True
  relations: MATCH=True   counts: MATCH=True
```

Digests: r97 `3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6`;
r98 `59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133`.
Tool-side end-to-end check on the same bytes:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
RESULT PASS            EXIT=0
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
RESULT PASS            EXIT=0
$ chain r88,r94,r95,r96,r97,r98 → all PASS (6/6)
```

### 1c. Self-test / expectation changes — exactly one added case

```
baseline 16 cases, current 17 cases
added: ['self_test_mismatch']   removed: []   modified: none
self_test_mismatch = {"exit": 2, "finding_ids": ["SELF-TEST-MISMATCH"], "forbid_traceback": true}
```

`FROZEN_CASES` in the delivered tool grew by one appended entry
(`self_test_mismatch`); the tool enforces set equality between
`self_test.expected` and `FROZEN_CASES` (CONTRACT-INVALID otherwise). On the
settled bytes: `python3 corpus/tools/dependency_freeze.py --self-test` →
all 17 cases `ok` (16 inherited + the new one), `SELF-TEST 17/17`, `RESULT
PASS`, exit 0 — including `CASE self_test_mismatch: exit=2 expected=2
findings=['SELF-TEST-MISMATCH'] ok`.

### 1d. Precedence text — complete, and its behavioral claims probed

Delivered text names all three exit-1 IDs (REDUCTION-DETECTED,
ADDITION-DETECTED, ENDPOINT-CHANGE) and every exit-2 finding ID the tool can
emit: UNPINNED-FIXTURE, CONTRACT-INVALID, FIXTURE-MISSING, PATH-MISMATCH,
FILE-MISSING, MALFORMED-JSON, MALFORMED-MODEL, DIGEST-MISMATCH,
INVALID-ARGUMENTS, SELF-TEST-MISMATCH, SCOPE-REFUSED (11/11, cross-checked
against every `fail(...)`/`emit(2, ...)` call site in the tool). The two
behavioral clauses were probed in scratch mirrors carrying the delivered tool
and contract bytes:

```
PROBE A (path-less legacy pin; r98 pin's fixture key removed in the mirror):
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r98-clerk-filing
MIGRATED r98-clerk-filing: path-less legacy pin now names corpus/fixtures/r98-clerk-filing
FROZEN r98-clerk-filing: events 7; dependency-edges 6; relations 1
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
RESULT PASS            EXIT=0   (pin's fixture field after: 'corpus/fixtures/r98-clerk-filing')

PROBE B (same-named in-scope copy at a different path; refusal must stay):
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/moved/r98-clerk-filing
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/moved/r98-clerk-filing: pin r98-clerk-filing
already names 'corpus/fixtures/r98-clerk-filing'; freezing a same-named path elsewhere would
rewrite the delivered pin
RESULT ERROR           EXIT=2
```

## 2. V46-discharge cross-check (supports the C2/refreeze story)

My own reproduction of the V46 mutation on the delivered fixture (scratch
mirror rootC; drop `response-evin-salt-court` from `acknowledgment-aru-records`)
hits V46's exact recorded bytes and is now caught by the frozen pin:

```
$ sha256sum .../r97-crossing-acknowledgment/timeline.json
37a425b97af658d71b8dc8904f43fd75859905bac326489a71adb67004004eb1   # == V46's recorded sha
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5; relations 1/1
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
RESULT FAIL            EXIT=1
```

Also verified: V46's r97 report (`V46-cross-gates.md:101`) quotes DIGEST
`3c922d20…`, identical to the delivered r97 pin; the provenance note's
`37a425b9…` mutation bytes exist on disk in V46's r97 scratch.

## 3. Non-pin changes recorded (outside the literal three-category list)

Two changed paths are not pins and not self-test expectations. Both are
accounted for; the parent should weigh them against the literal "only …"
wording:

- `revision` (top level): `2393934237ea… → dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb`.
  Freeze-mechanical: `freeze()` writes `contract["revision"] = git rev-parse
  HEAD` on every `--freeze`; HEAD during this uncommitted wave is the r97
  close commit `dd4df1b…`. C2 mandates the guarded `--freeze`, so this write
  is inherent to the declared mechanism (same precedent: the r96 pin re-freeze
  at r97 recorded the then-HEAD `2393934…`).
- `provenance_note`: extended with one r98 paragraph. Its checkable claims all
  held in my runs: both pin digests, the `dd4df1b…` revision, chain 6/6, and
  the V46 mutation sha/exit-1 catch (§2). It touches no pin, expectation, or
  verification semantics.

Pin-level scope is exactly as declared: of the 6 changed paths, the only pin
changes are the two new pins; no inherited pin byte moved; the r96 revision
field is unchanged.

## 4. Write audit

`git status --porcelain` (settled revision): modified — `LOG.md`,
`corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md`,
`corpus/knowledge/r95-aftermath-scope-note.md`,
`corpus/knowledge/r96-response-scope-note.md`, `corpus/tools/README.md`,
`corpus/tools/dependency-freeze-contract.json`,
`corpus/tools/dependency_freeze.py`; untracked — `.ufo/waves/round-98/`,
`corpus/fixtures/r98-clerk-filing/`, `corpus/knowledge/r98-clerk-scope-note.md`.
This matches the declared producer byte-ownership map exactly. My writes are
this report plus `V07-scratch/` (baseline/first-change/frozen contract copies,
expected-pin JSONs, diff/compare/recompute scripts, poll log, probes); the two
`/tmp` helper files were removed. (Not mine, recorded from S1/S3 reports: an
untracked `baseline-analyze.txt` in the parent tree.)

## Bottom line

**PASS** — contract diff vs `9a3d648` on the settled revision is exactly the
two declared pins (`r97-crossing-acknowledgment` `3c922d20…`,
`r98-clerk-filing` `59a0f4fa…`, both independently recomputed field-for-field,
revision `dd4df1b…` = HEAD), the one new self-test case (16→17, `--self-test`
17/17 PASS), and the complete precedence text (11/11 exit-2 IDs; migration and
refusal clauses probed true); no other pin touched and the r96 pin revision
field unchanged — with two non-pin changes recorded and accounted for:
top-level `revision` (freeze-mechanical) and `provenance_note` (changelog,
checkable claims verified).
