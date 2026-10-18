# V03 c1-selftest — round 98

- Seat: **V03 c1-selftest** (verifier). Lane repo
  `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline r97 closure `9a3d648`
  (pre-round bytes via `git show 9a3d648:<path>`); wave tree uncommitted; HEAD
  during the round `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb`.
- Claim under test: **C1 (calibration)** — `dependency_freeze` self-test/contract
  hygiene. Focus: `--self-test` 17/17 PASS on the delivered revision; two
  expectations hand-derived independently; `corpus/` hash-stable around runs;
  BR-05 pattern respected (self-test scratch at repo root, gitignored).
- Wrote only this report (absolute path) and
  `.ufo/waves/round-98/scratch/V03/` (declared scratch). Leaf seat: no nested
  agents, no commits, no pushes, no network, no other lane file written.

## 0. Poll-wait record (20 s cadence; artifacts AND producer reports)

Artifact poll (background, `git diff 9a3d648 -- corpus/tools/{dependency_freeze.py,dependency-freeze-contract.json}`):

```
S1-LANDED try=13 diff-lines=34/27 at 20:31:28
```

Producer-report poll (background, S1 report + 2-consecutive stable hash pair):

```
try=1 t=20:33:28 S1rep=0 hashpair=d8f2f30dbab7144abfa6f9a2b3cb5161 stable=0
try=2 t=20:33:48 S1rep=0 hashpair=7a7a963b94c8363a01e44aca13edbf53 stable=0
try=3 t=20:34:08 S1rep=0 hashpair=7a7a963b94c8363a01e44aca13edbf53 stable=1
...
try=7 t=20:35:28 S1rep=1 hashpair=7a7a963b94c8363a01e44aca13edbf53 stable=5
S1-REPORT+STABLE
```

`S1-freeze-hygiene.md` (254 lines) landed at 20:35:28; the tool+contract hash
pair was stable from 20:33:48 through the final run at 20:35:49. Never verified a
plan; no stall escape needed; no all-reports poll needed (endgame convention not
triggered for this seat). **S1's report is present.**

Final revision locked for all final-revision evidence below:

```
corpus/tools/dependency_freeze.py              sha256 03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  mtime 20:31:49
corpus/tools/dependency-freeze-contract.json   sha256 153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  mtime 20:33:36
```

S1 wrote in stages (tool `1a01fd17…` @20:31:30 → `03d04365…` @20:31:49; contract
`3a940a9f…` @20:31:20, 4 pins → `c435239d…` @~20:32:4x, 6 pins → `153ebc5b…`
@20:33:36). My first full self-test ran at 20:32:44 on pair (`03d04365…`,
`c435239d…`); the final-revision comparison below proves the only difference
between the two contracts is `provenance_note` — `self_test`, `precedence`, and
all six pins are byte-identical (pristine copy of `c435239d…` archived at
`.ufo/waves/round-98/scratch/V03/handrun-delivered/reduction/corpus/tools/`).

## 1. C1(a) — pre-state vs delivered `--self-test`

Pre-state, baseline bytes (`git show 9a3d648:…` copied into
`.ufo/waves/round-98/scratch/V03/` mirrors; raw logs kept):

```
$ python3 corpus/tools/dependency_freeze.py --self-test          # baseline, exit=0
SELF-TEST 16/16
RESULT PASS

$ (mirror, baseline bytes, self_test.expected.clean.exit corrupted 0 -> 1)
  python3 <mirror>/corpus/tools/dependency_freeze.py --self-test
SELF-TEST 15/16
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT FAIL
exit=1                                            # <-- the old exit-1 behavior
```

Delivered, frozen revision:

```
$ python3 corpus/tools/dependency_freeze.py --self-test          # 153ebc5b contract
CASE clean: exit=0 expected=0 findings=[] ok
...  (16 further CASE lines, each `ok`)
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
SELF-TEST 17/17
RESULT PASS
exit=0                                            # 17/17, 17 `ok` lines counted
```

`FROZEN_CASES` grew 16→17 by **append** (`self_test_mismatch` last, observed as
the 17th CASE line); the contract `self_test.expected` has exactly the 17
implemented case names. The 16 inherited cases print `ok` unchanged. The same
run was also executed on the `c435239d…` contract (20:32:44): identical `17/17`
— the staged rewrites did not change the self-test section.

The 17th case mechanism (read at `corpus/tools/dependency_freeze.py:516-527,
549-550`): a mirror root whose contract copy corrupts `clean` to `exit: 1`, run
through `--self-test`; every case subprocess carries
`DEPENDENCY_FREEZE_SELF_TEST_CHILD=1`, so a nested replay gets the corrupted
mirror **without** the base fixture and fails closed on `FIXTURE-MISSING` before
it can replay the case — bounded, no runaway recursion. Empirically: the case
completes `ok` and my direct tampered-mirror run finishes in ~1 s.

## 2. Hand-derived expectations (2) and hand-runs

**HD-1 — `clean` expectation, derived from first principles (not the tool's
harness).** Independently recomputed the r95 pin payload from the fixture bytes
(python3: per-file sha256, then `sha256(json.dumps(per_file, sort_keys=True,
separators=(",",":")))`, then counts):

```
hand per-file == pin per-file : True   (entities 026af0…, relations c27925…, timeline 3c0faa…,
                                        sources fd9e30…, contradictions 37517e…)
hand content  d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
pin  content  d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9  -> match
hand counts events=4 edges=3 relations=1 entities=5 sources=4 == pin counts  -> match
```

With pin == bytes, `clean` (verify r95 at its pinned path) must exit 0 with no
findings — which the run confirms (`CASE clean: exit=0 … ok`, receipt
`events 4/4; dependency-edges 3/3; relations 1/1`).

**HD-2 — `self_test_mismatch` expectation (exit 2, `SELF-TEST-MISMATCH`),
hand-run outside the tool's harness.** I built my own mirror (tool + contract +
r95 fixture), corrupted only `self_test.expected.clean.exit` 0→1, and ran
`--self-test` directly:

```
$ python3 <V03 mirror>/corpus/tools/dependency_freeze.py --self-test
SELF-TEST 16/17
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR
exit=2
```

The persisted expectation (`self_test.expected.self_test_mismatch` = exit 2,
`["SELF-TEST-MISMATCH"]`) matches observed behavior; pre-state the same scenario
exited 1 (section 1). This is the exact calibration move C1(a) claims.

**Hand-runs of two further pinned expectations (bonus, on the final revision):**

```
B (edge `evin-ninth-bell` dropped by hand from paired-crossing-decision):
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 2/3; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL      exit=1        # matches pinned reduction_edge_drop {exit 1, [REDUCTION-DETECTED]}

C (path-less legacy pin, `fixture` key removed; --freeze same path):
MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
RESULT PASS      exit=0        # C1(b) post-state; migrated pin names the repo-relative path
```

## 3. `corpus/` hash-stability around runs

Manifest = `find corpus -type f | sort | xargs sha256sum` (1818 files at first
capture), taken immediately before and after each `--self-test` run:

```
run 1  (c435239d contract):  T0=20:32:44  T1=20:32:45  diff before/after -> empty  CORPUS-STABLE-AROUND-RUN
final  (153ebc5b contract):  T0=20:35:48  T1=20:35:49  diff before/after -> empty  CORPUS-STABLE
```

Tool and contract hashes were identical before and after every run (the
self-test never rewrites the contract or any fixture; its only writes are the
transient temp dir). The first before/after window also proves the staged
contract rewrite happened *before* the window (hash pair stable across it).

## 4. BR-05 pattern — repo-root scratch, gitignored, cleaned up

- `.gitignore:4:*-self-test-*/` → `git check-ignore -v dependency-freeze-self-test-ddfy2cap/`
  printed the match, exit 0.
- Observed live during a run window (my catcher loop, cwd = repo root):
  `dependency-freeze-self-test-1ap90em9` and `dependency-freeze-self-test-czwlna2y`
  appeared at the **repo root** (one mine, one a concurrent seat's — V31's live
  run was also visible in `ps` with its own `dependency-freeze-self-test-_8wr_5yj`
  under its scratch mirror), and all were gone afterwards (`ls -d
  dependency-freeze-self-test-*` → none). Code path: `TemporaryDirectory(prefix="dependency-freeze-self-test-", dir=ROOT)` (`dependency_freeze.py:544`).
- After the final run: `no leftover scratch`; `git status` shows no self-test
  paths. Residual bound unchanged from r97: scratch materialises at the repo
  root (gitignored), not under a tool-owned directory.

## 5. C1(c) cross-check — precedence text covers every finding ID

All 14 finding IDs the tool can emit were extracted from the delivered source
(`fail("…")` and emitted tuples) and each appears in the contract `precedence`
string: REDUCTION-DETECTED, ADDITION-DETECTED, ENDPOINT-CHANGE (exit 1);
UNPINNED-FIXTURE, CONTRACT-INVALID, FIXTURE-MISSING, PATH-MISMATCH, FILE-MISSING,
MALFORMED-JSON, MALFORMED-MODEL, DIGEST-MISMATCH, INVALID-ARGUMENTS,
SELF-TEST-MISMATCH, SCOPE-REFUSED (exit 2). `IDs absent from precedence: []`.
The listed exit-2 order matches the verify path's check order in the code
(contract/unpinned → fixture-missing → path-bind → model build → digest);
`INVALID-ARGUMENTS`/`SELF-TEST-MISMATCH` are mode-level (each invocation takes
one path, so "first failing check decides" holds).

## 6. Cross-checks, boundaries, and observations

- **S1's report matches**: `S1-freeze-hygiene.md` quotes the same delivered
  hashes (`03d04365…`/`153ebc5b…`), the same 17 CASE lines, the same pre-state
  exit-1 mismatch (15/16), and the same `MIGRATED` post-state — reproduced
  independently here.
- **Chain behavior unchanged (C2 context, cheap check):** all six fixtures verify
  `RESULT PASS` exit 0 with receipts `r88 2/2·0/0·0/0, r94 3/3·2/2·1/1, r95
  4/4·3/3·1/1, r96 5/5·4/4·1/1, r97 6/6·5/5·1/1, r98 7/7·6/6·1/1`.
- **Not mine, recorded (adjacency):** `/home/vgpnk/Projects/shokunin/baseline-analyze.txt`
  exists at the parent root (105 B, mtime 20:30) — content is a `python3` error
  line for a missing `analyze.py`; S1's report (§6, via S3's D5) attributes it to
  an unattributed seat (r94-F01 stray-write class). I wrote nothing outside the
  lane; this seat's only writes are this report and `V03/` scratch.
- Raw evidence logs retained under `.ufo/waves/round-98/scratch/V03/`:
  `pre-state-selftest.txt`, `pre-state-mismatch.txt`, `pre-state-legacy.txt`,
  `delivered-selftest.txt`, `final-selftest.txt`, `handrun-delivered/*`,
  `handrun-final/*`, `run1-before/after.txt`, `final-before/after.txt`,
  `scratch-catch.txt`.

## Bottom line

**PASS** — on the frozen revision (`dependency_freeze.py` `03d04365…`,
contract `153ebc5b…`, stable from 20:33:48 through 20:35:49, S1 report present):
`--self-test 17/17 RESULT PASS` exit 0 with the 16 inherited cases `ok` and the
new 17th case `self_test_mismatch` pinned (pre-state tampered-expectation exit 1
vs delivered exit 2 both quoted); two expectations hand-derived independently
(clean pin recomputation; mismatch exit-2 hand-run), plus reduction and
legacy-pin hand-runs reproducing the pinned outcomes; `corpus/` hash-stable
around both runs; BR-05 pattern respected (repo-root `*-self-test-*/` scratch,
gitignored, cleaned up); precedence text covers all 14 finding IDs.
