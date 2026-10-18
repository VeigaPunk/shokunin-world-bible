# V08 c2-code-review — round 98

- Seat: V08 c2-code-review (verifier). Lane repo
  `/home/vgpnk/Projects/shokunin/lore-shokunin` (all commands run from that
  root; every write under it, absolute paths). Baseline r97 closure `9a3d648`;
  wave tree uncommitted; `HEAD = dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb`.
- Scope: line-by-line review of S1's `dependency_freeze` diff — (1)
  `SELF-TEST-MISMATCH` exit-code change complete (no path still exits 1), (2)
  path-less-pin migration sound (no scope widening), (3) pin schema consistent
  across the six pins, (4) defects by severity.
- Revision reviewed (frozen for this review, re-checked at endgame):
  `corpus/tools/dependency_freeze.py`
  sha256 `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`
  (mtime 20:31:49), `corpus/tools/dependency-freeze-contract.json`
  sha256 `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`
  (mtime 20:33:36). Pre-round hashes (working tree == baseline at first read):
  py `b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130`,
  contract `27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781`.
- Writes: this report (absolute path) and
  `.ufo/waves/round-98/seats/V08-scratch/` only. Leaf seat: no nested agents,
  no commits, no pushes, no network.

## 0. Poll-wait record

- 20:27–20:31: 12 × 20 s checks — both S1-owned files byte-identical to
  `9a3d648` (`git status --porcelain -- corpus/tools/…` empty), so I reviewed
  the pre-state instead of a plan: the C1 defects were read off the baseline
  bytes (`dependency_freeze.py:544-545` `emit(1,…)`/`return 1`;
  `:359-362` `existing.get("fixture") != fixture_label` → `SCOPE-REFUSED … already
  names None`; contract `precedence` one clause). Baseline battery at that
  moment: `--self-test 16/16 RESULT PASS`, chain 4/4 PASS, r97
  `UNPINNED-FIXTURE` (V46's recorded r97 FAIL reproduced).
- Try 12 (≈20:31): S1 bytes landed. Hash was still moving (py blob
  `6415d74`→`6c0d9e0`→`623b350` between 20:31:30 and 20:31:49), so I waited
  for stability + report: stable at try 2 (03d04365…), `S1-freeze-hygiene.md`
  on disk at 20:35:33. **S1 report PRESENT** (read in full; its receipts
  independently reproduced below).
- Endgame convention: single dependency (S1), satisfied — no all-reports poll
  was needed, no stall escape, no timeout. Endgame re-check at 23:36:55Z: both
  hashes unchanged, `--self-test 17/17 RESULT PASS`, chain 6/6 PASS.

## 1. Diff reviewed

`git diff 9a3d648 -- corpus/tools/dependency_freeze.py` → 6 hunks / 95 lines
(saved `.ufo/waves/round-98/seats/V08-scratch/s1-py-final.diff`);
`… -- corpus/tools/dependency-freeze-contract.json` → 5 hunks / 226 lines
(`s1-contract-final.diff`). Hunk-by-hunk:

| Hunk | Change | Verdict |
|---|---|---|
| py H1 (+7) | docstring "Round-98 hardening" | accurate against code (checked claim by claim) |
| py H2 (+1) | `import os` (alphabetical after `json`) | used at `:546` (`os.environ`) only — no dead import |
| py H3 (+2) | `FROZEN_CASES += "self_test_mismatch"`; `SELF_TEST_CHILD_ENV` const | append-only; 16 inherited entries untouched |
| py H4 (+9/-4) | `freeze()` legacy-pin branch | see §3 |
| py H5 (+13) | `self_test_cases()` case 17 + comment | see §2, defect D3 |
| py H6 (+2/-2) | `env={**os.environ, marker}`; `emit(2,…)`/`return 2` | see §2, defect D2 |
| contract H1 | `precedence` rewritten | see §4, defect D1 |
| contract H2 | `revision` `2393934…`→`dd4df1b…` | matches HEAD |
| contract H3 (+180) | pins `r97-crossing-acknowledgment`, `r98-clerk-filing` added | see §5; four inherited pins byte-identical (no hunk touches them) |
| contract H4 (+7) | `self_test.expected.self_test_mismatch` `{exit 2, SELF-TEST-MISMATCH, forbid_traceback}` | the 16 inherited entries unchanged |
| contract H5 | `provenance_note` + r98 paragraph | claims spot-checked, all true (below) |

## 2. C1(a) — mismatch-exit change complete

**Single emission site; no path still exits 1 for the mismatch class.**

```
$ grep -n "SELF-TEST-MISMATCH" corpus/tools/dependency_freeze.py
19:Round-98 hardening: `SELF-TEST-MISMATCH` exits 2 (the could-not-evaluate class,
572:        emit(2, [("SELF-TEST-MISMATCH", f"cases failed: {sorted(failures)}")])
$ grep -n "emit(1\|return 1\|RESULTS\[1\]" corpus/tools/dependency_freeze.py
345:        emit(1, findings)
346:        return 1
```

Lines 345-346 are `verify()`'s semantic-inventory path (exit 1 by contract);
every other terminal is 0 or 2. Cross-tool parity with `map_obligations.py`
restored (`map_obligations.py:877-879`: `print("RESULT ERROR"); return 2`).
`emit(2,…)` prints `RESULT ERROR`, matching `exit_codes {"2": "ERROR"}`.

**The new case is load-bearing (neutralization).** Mirror with the delivered
contract; only the two changed lines reverted:

```
$ (neutral mirror) python3 corpus/tools/dependency_freeze.py --self-test
exit 1
CASE self_test_mismatch: exit=1 expected=2 findings=['SELF-TEST-MISMATCH'] MISMATCH
SELF-TEST 16/17
FINDING SELF-TEST-MISMATCH: cases failed: ['self_test_mismatch']
RESULT FAIL
```

Delivered revision: `CASE self_test_mismatch: exit=2 expected=2
findings=['SELF-TEST-MISMATCH'] ok`, `SELF-TEST 17/17`, `RESULT PASS`, exit 0;
all 16 inherited cases print `ok` (full log:
`.ufo/waves/round-98/seats/V08-scratch/selftest-out.txt`).

**Case construction is genuine, not vacuous.** The case corrupts the *mirror's*
contract (`expected.clean.exit = 1`) and runs the mirrored tool's `--self-test`;
the child must therefore report `SELF-TEST-MISMATCH` (it is the child's own
`clean` expectation that is corrupted). Verified by running the mirror child by
hand:

```
$ DEPENDENCY_FREEZE_SELF_TEST_CHILD=1 python3 <mirror>/…/dependency_freeze.py --self-test
CASE clean: exit=0 expected=1 findings=[] MISMATCH
… (15 more cases) …
CASE self_test_mismatch: exit=2 expected=2 findings=['FIXTURE-MISSING'] MISMATCH
SELF-TEST 15/17
FINDING SELF-TEST-MISMATCH: cases failed: ['clean', 'self_test_mismatch']
RESULT ERROR            exit 2
```

## 3. C1(b) — migration sound, no scope widening

`freeze()` now refuses only when the existing pin names a *different nonempty*
path; absent/`null`/empty `fixture` migrates. Harness
(`V08-scratch/mig`, `nulls`, `decoy`), all quoted:

```
== A1: path-less legacy pin migrated in place ==
$ python3 <mirror>/corpus/tools/dependency_freeze.py --freeze <mirror>/corpus/fixtures/r95-crossing-aftermath
MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
RESULT PASS             exit 0        # pin.fixture after == 'corpus/fixtures/r95-crossing-aftermath'
== A2: same-named in-scope copy elsewhere still refused ==
$ … --freeze <mirror>/corpus/fixtures/dup/r95-crossing-aftermath
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/dup/r95-crossing-aftermath: pin r95-crossing-aftermath already names 'corpus/fixtures/r95-crossing-aftermath'; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR            exit 2
== A3: path-less legacy pin + out-of-scope target -> refused, no MIGRATED line ==
FINDING SCOPE-REFUSED: --freeze refuses …/V08-scratch/mig/elsewhere/r95-crossing-aftermath …; the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR            exit 2
== A4 (fixture="") and N1 (fixture=null) -> MIGRATED, exit 0 ==
== N2: path-less pin, verify only (no --freeze) -> unchanged pre-existing behavior ==
FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs a repo-relative fixture path
RESULT ERROR            exit 2
```

`scope_guard()` and `validate_pin()` are untouched by the diff; the migration
branch runs *after* `scope_guard(target)` and `build_model(target)`, and the
rewritten pin still goes through `validate_pin` before the write — no check is
bypassed and no scope is widened (guard remains `corpus/fixtures/**`).
Residual corner, defect D4 below.

## 4. C1(c) — precedence text: complete IDs, one ordering inaccuracy (D1)

The tool raises exactly 14 finding IDs
(`fail`/`ToolError`: CONTRACT-INVALID, FILE-MISSING, FIXTURE-MISSING,
INVALID-ARGUMENTS, MALFORMED-JSON, MALFORMED-MODEL, PATH-MISMATCH,
SCOPE-REFUSED, UNPINNED-FIXTURE; `emit`: DIGEST-MISMATCH, SELF-TEST-MISMATCH;
`compare` appends: REDUCTION-DETECTED, ADDITION-DETECTED, ENDPOINT-CHANGE), and
the new `precedence` text names exactly those 14. Coverage is complete.

Ordering: the text lists `INVALID-ARGUMENTS (CLI usage)` *after*
DIGEST-MISMATCH, but CLI-usage errors decide first in fact:

```
$ (corrupt contract: '{ not json') … --self-test --freeze <fixture>
FINDING INVALID-ARGUMENTS: --self-test cannot be combined with a fixture or --freeze
RESULT ERROR            exit 2
$ (same corrupt contract) … <fixture>
FINDING CONTRACT-INVALID: corpus/tools/dependency-freeze-contract.json: Expecting property name enclosed in double quotes: line 1 column 3 (char 2)
RESULT ERROR            exit 2
```

i.e. real order = INVALID-ARGUMENTS → CONTRACT-INVALID → UNPINNED-FIXTURE →
FIXTURE-MISSING → PATH-MISMATCH → FILE-MISSING/MALFORMED-JSON/MALFORMED-MODEL →
DIGEST-MISMATCH (+ SELF-TEST-MISMATCH, and --freeze's SCOPE-REFUSED first).

## 5. C2 — six pins: schema consistent, load-bearing

Programmatic schema check over all six pins (`V08-scratch`, all True):
identical key set `{fixture, revision, content_sha256, files, events, relations,
counts}`; `files` keys exactly the five JSON tables (fixture Markdown unpinned,
as at r97); every event entry `{depends_on, endpoint}` with endpoint
`{tick, entity_id, place_id}`; relations 3-element string triples; `counts`
recomputed from the live fixture equals the pinned counts
(2/0/0/4/2, 3/2/1/5/3, 4/3/1/5/4, 5/4/1/5/5, 6/5/1/5/6, 7/6/1/6/7);
`ALL-SIX-SCHEMA-CONSISTENT: True`, `total pins: 6`.

Chain on the delivered revision (endgame re-run, all `RESULT PASS` exit 0):

```
r88-m3-maya-cluster          DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279
r94-paired-crossing          DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
r95-crossing-aftermath       DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
r96-crossing-response        DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
r97-crossing-acknowledgment  DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6
r98-clerk-filing             DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
```

Independent corroboration (not S1's receipts):

- The r97 pin digest equals the digest of the **pre-round** r97 bytes:
  `git archive 9a3d648 corpus/fixtures/r97-crossing-acknowledgment` → recomputed
  content digest `3c922d20…` (timeline `73063a86…`), byte-equal to the live
  fixture and to V46's r97 record (`.ufo/waves/round-97/seats/V46-cross-gates.md:101`).
- V46's mutation bytes reproduce exactly from the 9a3d648 timeline:
  drop `acknowledgment-aru-records.depends_on` → `json.dumps(indent=2)` →
  sha256 `37a425b97af658d71b8dc8904f43fd75859905bac326489a71adb67004004eb1`
  == V46's recorded sha (`V46-cross-gates.md:44`).
- The two new pins are load-bearing on the round's own edges (scratch mirror,
  delivered tool+contract at pinned paths):

```
P1 r97 tick-13 edge dropped:  FREEZE … dependency-edges 4/5
   FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
   RESULT FAIL   exit 1
P2 r98 tick-14 edge dropped:  FREEZE … dependency-edges 5/6
   FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
   RESULT FAIL   exit 1
P3 r97 restored:              dependency-edges 5/5  RESULT PASS  exit 0
```

- Contract H5 provenance claims verified true (r97 digest, r98 digest, V46
  mutation sha, revision values); `provenance_note` addition is append-only.

## 6. Defects by severity

- **D1 (low, documentation).** `precedence` presents the exit-2 checks as an
  ordered sequence but places `INVALID-ARGUMENTS` after `DIGEST-MISMATCH`;
  empirically it decides first (§4). All 14 IDs are named, so C1(c) is met in
  substance; the order claim is inaccurate for that one ID. Fix: move
  `INVALID-ARGUMENTS` to the head of the enumeration (or mark it as
  out-of-band CLI parsing).
- **D2 (low, robustness; fails closed).** `SELF_TEST_CHILD_ENV`
  (`DEPENDENCY_FREEZE_SELF_TEST_CHILD`) gates case construction on an
  unauthenticated environment variable. If it is present in the ambient
  environment, `--self-test` reports a spurious red on the delivered revision:

```
$ DEPENDENCY_FREEZE_SELF_TEST_CHILD=1 python3 corpus/tools/dependency_freeze.py --self-test
CASE self_test_mismatch: exit=2 expected=2 findings=['FIXTURE-MISSING'] MISMATCH
SELF-TEST 16/17
FINDING SELF-TEST-MISMATCH: cases failed: ['self_test_mismatch']
RESULT ERROR            exit 2
```

  Never a false green (a wrong-reason observation cannot match the persisted
  `finding_ids`), so no admission risk — but the battery's greenness depends on
  an unset ambient variable. Fix options: mark nesting with a dedicated internal
  argv token instead of the environment, or scope the variable name with the
  run's tempdir token.
- **D3 (informational, comment accuracy).** The new case's comment claims the
  nested replay "fails closed on `FIXTURE-MISSING` before it can replay this
  case". Observation shows the nested run *does* replay the case and records its
  own `FIXTURE-MISSING` mismatch (child failure list `['clean',
  'self_test_mismatch']`, §2). The bound actually comes from the grandchild
  failing `run_self_test`'s `base.is_dir()` check before `self_test_cases()` is
  reached; recursion is genuinely bounded (child probe completed in 0.6 s). The
  comment's "cannot recurse without bound" conclusion is right; its mechanism
  sentence is imprecise.
- **D4 (low, dormant corner; declared-bound candidate).** With a path-less
  legacy pin, migration is first-freeze-wins: a same-named in-scope decoy can
  claim the pin, silently re-pointing it (pre-r98 that call refused):

```
$ (path-less r95 pin; decoy at corpus/fixtures/dup/r95-crossing-aftermath)
MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/dup/r95-crossing-aftermath
RESULT PASS             exit 0
```

  Requires a path-less pin *and* a same-named in-scope duplicate; all six live
  pins carry paths, so the branch is dormant. Not a widening of the scope guard.
  Recommend recording it as a declared bound (or requiring the migration to
  re-validate the name against the declared chain set) in closure errata.
- **Informational, by design.** Migration re-pins the *current* bytes, so a
  drifted fixture under a path-less pin silently gets a new baseline (with the
  `MIGRATED` line and no finding). This is the declared C1(b) intent
  ("migrated by `--freeze`; was manual-only"); pre-r98 the same call exited 2
  with zero writes.

## 7. Write audit

- `git status --porcelain` at endgame lists only declared round paths (LOG.md,
  S2's README, S3's r95 map, S5's two knowledge notes, S1's two files, untracked
  `r98-clerk-filing/`, `r98-clerk-scope-note.md`, `.ufo/waves/round-98/`).
- No `dependency-freeze-self-test-*` strays at the repo root after my runs (the
  tool's scratch tempdirs self-clean). One non-V08 root scratch exists,
  `v05-self-test-scratch` (gitignored `*-self-test-*/`, V05-owned) — recorded,
  not touched.
- All V08 writes confined to this report + `.ufo/waves/round-98/seats/V08-scratch/`
  (`s1-py*.diff`, `s1-contract-final.diff`, `selftest-out.txt`, and the
  `chain/ mig/ neutral/ depth/ decoy/ nulls/ v46check/` harness mirrors).
  Nothing written outside the lane.

## Bottom line

**PASS** — mismatch-exit change is complete (single `SELF-TEST-MISMATCH` site at
`:572` exits 2; the only exit-1 site is `verify()`'s semantic path; the new case
17 is load-bearing under neutralization and the battery is 17/17 green);
migration is sound with no scope widening (path-less absent/`null`/empty pins
migrate, different-path and out-of-scope targets still `SCOPE-REFUSED`, guard
and `validate_pin` untouched); the six pins are schema-identical, counts-match
and load-bearing (chain 6/6; r97/r98 edge drops `REDUCTION-DETECTED` exit 1;
r97 digest independently reproduced from the pre-round bytes and V46's mutation
sha reproduced exactly). Four recorded defects, all low/informational and none
harming an axis: D1 precedence-order wording (`INVALID-ARGUMENTS` listed late),
D2 spurious-red when `DEPENDENCY_FREEZE_SELF_TEST_CHILD` is ambient (fails
closed), D3 imprecise nesting comment, D4 path-less-pin first-freeze-wins corner.
