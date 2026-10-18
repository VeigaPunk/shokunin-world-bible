# V04 c1-regression — round 98

- Seat: V04 c1-regression (verifier, read-only on lane bytes; leaf seat).
  Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; all commands run from
  the lane root with `python3`. Baseline r97 closure `9a3d648` (pre-round bytes
  via `git show 9a3d648:<path>`). No commits, no pushes, no network, no nested
  agents.
- Revision verified (equal to S1's own report):
  `corpus/tools/dependency_freeze.py` sha256
  `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`;
  `corpus/tools/dependency-freeze-contract.json` sha256
  `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`.
- Writes: this report (absolute path) and declared scratch
  `.ufo/waves/round-98/seats/V04-scratch/` (mirrors, logs, `final-battery.sh`).
  Nothing else in the lane was written; the delivered tool and contract were
  never mutated by my probes (sha256 checked before/after the battery).

## 0. Poll-wait record (20 s cadence; never verify a plan)

- 20:28 baseline capture: `git diff 9a3d648 -- corpus/tools/` empty for both
  owned files (shas `b06275f3…` / `27273be2…`), so the pre-state runs are on
  baseline bytes; `.ufo/waves/round-98/` did not exist yet.
- 20:29–20:31 polls: no S1 bytes, no producer reports.
- 20:31 first landing: contract declared `self_test_mismatch` but the tool's
  `FROZEN_CASES` did not yet contain it → `--self-test` failed closed,
  `FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=[]
  extra=['self_test_mismatch']`, `RESULT ERROR` exit 2 (mid-write, not counted
  against S1; recorded as a live fail-closed datum).
- 20:32–20:35 polls: tool sha settled at `03d04365…`, contract at `c435239d…`
  then `153ebc5b…`; byte-stability confirmed over consecutive 20 s checks
  (`POLL_STABLE … sha=03d04365…:153ebc5b…`).
- 20:36 S1 report hit: `S1-freeze-hygiene.md` present at exactly the revision
  above (`POLL_HIT … report=S1-freeze-hygiene.md`). No all-reports poll was
  needed, so the r96/r97 endgame subtraction convention did not arise; no stall
  escape required.

## 1. Inherited 16 cases unchanged (IDs and exits)

Baseline reproduction from a clean mirror built out of the baseline bytes
(`.ufo/waves/round-98/seats/V04-scratch/mirror-baseline2/`, tool+contract via
`git show 9a3d648:…`, r95 fixture copied) versus the delivered tree:

```
$ python3 $M/corpus/tools/dependency_freeze.py --self-test   # 9a3d648 bytes
… CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
SELF-TEST 16/16
RESULT PASS                                                  # EXIT=0

$ python3 corpus/tools/dependency_freeze.py --self-test      # delivered
… CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
SELF-TEST 17/17
RESULT PASS                                                  # EXIT=0

$ diff <(grep '^CASE' $M/…baseline-clean.log) <(grep '^CASE' current-selftest.log)
16a17
> CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
```

The diff is exactly one appended line: every inherited `CASE` line (ID, exit,
expected exit, observed finding list, `ok`) is byte-identical. `FROZEN_CASES`
grew 16 → 17 by append; the contract's `self_test.expected` has the 16 inherited
entries JSON-equal to baseline and exactly one added key (`self_test_mismatch`);
`self_test.base_fixture` unchanged.

## 2. Chain behavior pre-S1-pins preserved

The four inherited pins are JSON-identical to the baseline contract
(`pin_equal_to_baseline=True` for r88-m3-maya-cluster, r94-paired-crossing,
r95-crossing-aftermath, r96-crossing-response; `inherited pin set equal: True`),
and all four verify clean at the baseline digests:

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; done
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0      DIGEST 15ef230e…  EXIT=0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1      DIGEST 2527beb9…  EXIT=0
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1   DIGEST d541ae64…  EXIT=0
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1    DIGEST d422a9b3…  EXIT=0
```

All four digests equal the baseline contract's pins (r95's digest unchanged by
S3's map repair — the map is not a pinned data file). Pre-pin state recorded
before S1's C2 landing: `python3 corpus/tools/dependency_freeze.py
corpus/fixtures/r97-crossing-acknowledgment` →
`FINDING UNPINNED-FIXTURE: … (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response'])`
exit 2. The delivered chain is additive: 6/6 PASS (see §7), top-level
`schema_version`, `tool`, `scope`, `data_files`, `required_files`, `exit_codes`
all unchanged.

## 3. Guard / PATH-MISMATCH / DIGEST-MISMATCH classes intact (full negative battery)

Run as one script (`.ufo/waves/round-98/seats/V04-scratch/final-battery.sh`,
log `final-battery.log`) against the delivered bytes:

- **SCOPE-REFUSED (out of scope, real tool/contract)**:
  `--freeze …/V04-scratch/target` → `FINDING SCOPE-REFUSED: --freeze refuses
  …/target …; the frozen scope is corpus/fixtures/** (integration-time operation
  only)` `RESULT ERROR` exit 2 — identical text to baseline.
- **SCOPE-REFUSED (same-named in-scope copy, r97 hardening)**: mirror with
  `corpus/fixtures/nested/r95-crossing-aftermath` and `…/r98-clerk-filing` →
  `FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/nested/r95-crossing-aftermath:
  pin r95-crossing-aftermath already names 'corpus/fixtures/r95-crossing-aftermath';
  freezing a same-named path elsewhere would rewrite the delivered pin` exit 2
  (same for r98), mirror contract sha unchanged.
- **PATH-MISMATCH (real tool, foreign same-name copies)**: r95 →
  `FINDING PATH-MISMATCH: pin r95-crossing-aftermath names corpus/fixtures/r95-crossing-aftermath
  (resolves to …); invoked fixture resolves to …/V04-scratch/foreign/r95-crossing-aftermath`
  exit 2; r98 → same class exit 2.
- **Semantic tamper (mirror, depends_on dropped)**: `FINDING REDUCTION-DETECTED:
  event aftermath-missing-evin lost depends_on ['paired-crossing-decision']`
  `RESULT FAIL` exit 1 (baseline-identical text).
- **Cosmetic tamper (mirror, one trailing newline added)**: `FINDING
  DIGEST-MISMATCH: content digest c7c29b5e… != pin d541ae64…; changed:
  timeline.json (sha256 3c0faad6… -> bd64e666…); fixture bytes changed outside
  the frozen inventory` `RESULT ERROR` exit 2 — the changed file is named, as at
  r97.
- **Strict loader fails closed** (r97 property): deleting one pinned case from a
  mirror contract → `FINDING CONTRACT-INVALID: self-test expectation set
  mismatch; missing=['clean'] extra=[]` exit 2 (also observed live mid-write in
  §0).
- **Real contract untouched**: sha256 `153ebc5b…` before and after the whole
  battery (`CONTRACT_UNCHANGED=yes`).

## 4. C1(a) exit-code change verified before/after

```
# 9a3d648 bytes, mirror contract with clean expectation corrupted to exit 1
SELF-TEST 15/16
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT FAIL            BASELINE_EXIT=1
# delivered bytes, same corruption
SELF-TEST 16/17
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR           POST_EXIT=2
```

The finding ID and message shape are unchanged; only the class moved from 1 to 2
(the could-not-evaluate contract), and case 17 pins it.

## 5. C1(b) path-less legacy pin migration verified

Pre-state on baseline bytes (mirror, `fixture` key deleted):
`FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath:
pin r95-crossing-aftermath already names None; freezing a same-named path
elsewhere would rewrite the delivered pin` exit 2, and verify →
`FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs a repo-relative
fixture path` exit 2; the pin stayed path-less. Delivered bytes:

```
$ python3 $M/corpus/tools/dependency_freeze.py --freeze $M/corpus/fixtures/r95-crossing-aftermath
MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
DIGEST d541ae64…
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
RESULT PASS            FREEZE_EXIT=0
$ python3 $M/corpus/tools/dependency_freeze.py $M/corpus/fixtures/r95-crossing-aftermath
RESULT PASS            VERIFY_EXIT=0        # pin path now 'corpus/fixtures/r95-crossing-aftermath'
```

Guard ordering holds: with the pin still path-less and the fixture copy OUT of
scope, `--freeze …/V04-scratch/foreign/r95-crossing-aftermath` →
`FINDING SCOPE-REFUSED: --freeze refuses .ufo/waves/round-98/seats/V04-scratch/foreign/r95-crossing-aftermath …`
exit 2 with the mirror contract sha unchanged — the migration cannot adopt an
out-of-scope path. The different-nonempty-path refusal is retained (same-named
nested copy, §3).

## 6. C1(c) precedence text coverage (lexical)

Extracted every finding-ID literal from the delivered tool source and checked
membership in the contract `precedence` string:
`tool finding IDs: ['ADDITION-DETECTED', 'CONTRACT-INVALID', 'DIGEST-MISMATCH',
'ENDPOINT-CHANGE', 'FILE-MISSING', 'FIXTURE-MISSING', 'INVALID-ARGUMENTS',
'MALFORMED-JSON', 'MALFORMED-MODEL', 'PATH-MISMATCH', 'REDUCTION-DETECTED',
'SCOPE-REFUSED', 'SELF-TEST-MISMATCH', 'UNPINNED-FIXTURE']`;
`missing from precedence text: []`; the exit-1 clause names all three semantic
IDs; the ordered exit-2 sentence is present. All 14 IDs are named — no exit-2
class the tool can emit is unmentioned.

## 7. New pins are load-bearing (independent of S1's own receipt)

Full chain on the delivered tree: 6/6 `RESULT PASS` exit 0, digests
`15ef230e… / 2527beb9… / d541ae64… / d422a9b3… / 3c922d20… / 59a0f4fa…`. In
mirrors carrying the delivered tool+contract and one fixture copy, stripping
`depends_on` from every event:

```
r97: FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
     (+ aftermath-missing-evin, paired-crossing-decision, response-evin-salt-court)   RESULT FAIL  EXIT=1
r98: FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
     (+ the same three inherited edges)                                              RESULT FAIL  EXIT=1
```

So V46's r97 tick-13 edge is frozen and caught, and the new r98 tick-14 edge is
frozen and caught — the pins, not the fixtures' green gates, carry the claim.

## 8. Findings and bounds (no axis harmed; one bound worth recording)

1. **Bound (new, low severity): the new recursion guard is environment-sensitive.**
   `DEPENDENCY_FREEZE_SELF_TEST_CHILD=1 python3 corpus/tools/dependency_freeze.py
   --self-test` → `FINDING SELF-TEST-MISMATCH: cases failed: ['self_test_mismatch']`
   `RESULT ERROR` exit 2 (`SELF-TEST 16/17`), while a normal run is 17/17 PASS.
   Cause: with the marker already in the ambient environment, the case's mirror
   is built without the base fixture, so the child run fails on
   `FIXTURE-MISSING` instead of the expected `SELF-TEST-MISMATCH`. It fails
   closed (reports FAIL, never a false PASS) and touches nothing but
   `--self-test` under a tool-specific variable that nothing in this lane sets;
   verify/freeze/chain are unaffected. No baseline analogue existed (the marker
   is new), so this is not an inherited regression — recorded as a bound for
   S1/the closure doc pass, not as a FAIL.
2. Bound (declared semantics): a path-less pin has no recorded path to preserve,
   so migration adopts the invoked in-scope path — demonstrated by migrating
   onto `corpus/fixtures/nested/r95-crossing-aftermath` in a mirror. This is
   exactly the declared C1(b) repair (path-less = pre-r97 legacy), and the
   guard keeps it inside `corpus/fixtures/**`.
3. Inherited bounds unchanged: pins cover the five JSON tables only (fixture
   Markdown unpinned); `--self-test` scratch stays at the repo root under the
   gitignored `*-self-test-*/` pattern (no residue from any of my runs).

## 9. Write audit

`git status --porcelain` after my battery shows only producer-owned paths
(`LOG.md`, `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md`,
`corpus/knowledge/r95-aftermath-scope-note.md`,
`corpus/knowledge/r96-response-scope-note.md`, `corpus/tools/README.md`,
`corpus/tools/dependency_freeze.py`,
`corpus/tools/dependency-freeze-contract.json`, untracked
`corpus/fixtures/r98-clerk-filing/`, `corpus/knowledge/r98-clerk-scope-note.md`,
`.ufo/waves/round-98/`). `git diff 9a3d648 -- corpus/tools/` lists only the two
S1-owned files. My only writes are this report and `V04-scratch/`; the delivered
tool and contract shas were `03d04365…`/`153ebc5b…` at the start and end of the
battery. Not mine, recorded: the repo-root `v05-self-test-scratch/` directory
(V05's declared scratch, gitignored by the `*-self-test-*/` pattern) and S3's
report item D5 about an untracked `baseline-analyze.txt` in the parent directory
(the r94-F01 stray class, unattributed; I wrote nothing outside the lane).

## Bottom line

**PASS** — on the delivered revision (`03d04365…`/`153ebc5b…`) the 16 inherited
self-test cases are byte-identical (one appended case, 17/17 PASS), the four
inherited pins are JSON-identical and verify clean at their baseline digests,
the guard/PATH-MISMATCH/DIGEST-MISMATCH/SCOPE-REFUSED/tamper battery reproduces
class-for-class, the C1(a) exit moves 1→2 with the finding preserved, C1(b)
migrates path-less pins behind the scope guard, C1(c) names all 14 finding IDs,
and the r97/r98 pins are load-bearing (REDUCTION-DETECTED exit 1 on stripped
edges); one bounded, fail-closed environment sensitivity of the new self-test
marker is recorded (§8.1).
