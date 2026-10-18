# V48 — cross-seat-audit (round 98)

**Seat:** V48 cross-seat-audit (verifier, single-wave round-98 swarm, lore-shokunin lane).
**Scope (verbatim):** *Re-run 6 load-bearing quoted outputs from other seats; REPRODUCED/MISMATCHED.*
**Repo root for every command:** `/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the parent
repo; every path below is absolute or `cd`-anchored there, and every write of this seat used an absolute
path under the lane repo). All commands run from the lane root with `python3`.
**Baseline:** r97 closure `9a3d648`; HEAD during the round `dd4df1b` (r97 SCORECARD closure commit).
**Writes of this seat:** this report and `.ufo/waves/round-98/seats/V48-scratch/**` only. No commits, no
pushes, no network, no nested agents, no writes to any producer-owned path; the delivered
`dependency-freeze-contract.json` was never passed to `--freeze` on the live tree (every freeze probe ran
in a scratch fakerepo).

**STATUS: FINAL — all six audit items re-run independently on the delivered revision: 6 REPRODUCED,
0 MISMATCHED.** Every item was re-run only after the relevant producer report existed on disk (S1–S5 all
present before the first item; ALL-PRESENT at my poll try 21, 20:35:33 local).

## 0. Revision binding

Hashes of the artifacts my re-runs executed against (measured at 20:37–20:39 local; re-hashed after the
probe battery — byte-identical, `BYTES-STABLE-ACROSS-PROBES`):

```
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py            (S1 delivered)
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json (S1 delivered, final)
1d299c16bf9a0b34526f4a799cdd3117867f6d4d278866b66366b78700d79b84  corpus/tools/README.md                       (S2 delivered)
80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md (S3 repaired)
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  corpus/fixtures/r98-clerk-filing/entities.json          (S3)
32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3  corpus/fixtures/r98-clerk-filing/sources.json           (S3)
eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af  corpus/fixtures/r98-clerk-filing/timeline.json          (S3)
29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de  corpus/fixtures/r98-clerk-filing/fictional-excerpts.md  (S3)
32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926  corpus/fixtures/r98-clerk-filing/README.md              (S4)
c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba  corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md   (S4)
1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8  corpus/knowledge/r98-clerk-scope-note.md                (S5)
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py               (unchanged)
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py                (unchanged)
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py              (unchanged)
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json   (unchanged)
```

Every declared delivered hash in S1's, S2's, S3's, S4's, S5's reports matches the file on disk
(S1 declares `03d04365…`/`153ebc5b…`; S2 `1d299c16…`; S3 the four r98 JSON/MD hashes; S4 the two r98 doc
hashes; S5 the note `1162262c…`).

**Contract churn (recorded):** S2's report documents the contract moving `b06275f3…` (r97) → `3a940a9f…`
→ `c435239d…` → `153ebc5b…` while it polled. Every re-run in this report is against the final
`153ebc5b…`/`03d04365…` pair; quotes taken by seats against the interim `c435239d…` are flagged in §4.1.

The wave change set vs `9a3d648` (`git diff --name-only` + untracked) is exactly: `LOG.md` (round
declaration), `SCORECARD.md` (r97 closure commit), the S1/S2/S3/S5 owned paths, and the new
`corpus/fixtures/r98-clerk-filing/` + `corpus/knowledge/r98-clerk-scope-note.md`. No unowned drift.

## 1. Poll-wait record

Protocol: 20 s cadence; no item re-run before the relevant producer report existed on disk; no plan ever
verified. Poller: `.ufo/waves/round-98/seats/V48-scratch/poll.sh` (log quoted):

```
try 5  23:30:13 reports=1  missing: REPORT:S1 REPORT:S2 REPORT:S3 REPORT:S4 REPORT:S5 ART:corpus/knowledge/r98-clerk-scope-note.md
try 8  23:31:13 reports=3  missing: REPORT:S1 REPORT:S2 REPORT:S4 REPORT:S5 ART:corpus/knowledge/r98-clerk-scope-note.md
try 12 23:32:33 reports=7  missing: REPORT:S1 REPORT:S2 REPORT:S5
try 16 23:33:53 reports=15 missing: REPORT:S1 REPORT:S2
try 21 23:35:33 reports=22 missing:
ALL-PRESENT try 21 23:35:33
```

Producer report mtimes: S3 20:31:25, S4 20:32:06, S5 20:34:00, S2 20:34:53, S1 20:35:33. My first
re-run (probe battery) started after 20:35:33. ENDGAME convention: this seat is V48 and no item depended
on V-reports, so the all-producer poll (5/5) needed no SELF subtraction; no stall escape was required.

Cross-seat poll observations absorbed (not fatal): S2's report closed with S1's report **ABSENT** at its
hand-off (S2 verified artifacts by its own probes, not a plan); V11's first poller reported a **false
READY** matching `S4-scratch/` (a directory) and was rewritten to require an `S4*.md` file plus moved
table bytes; S3/S4/V11/V16/S5 all record the **r97-copy placeholder window** (20:28:24–20:30:41) during
which the r98 README/map existed with r97 bytes, i.e. an existence-only poll can be satisfied by a
placeholder. Every item below ran on the final non-placeholder bytes (r98 map `c1099d0e…`, README
`32efc78f…`).

## 2. Audit items

### A1 — C1(a): delivered `--self-test` is 17/17 PASS exit 0 — **REPRODUCED**

Quoted by **S1** (`S1-freeze-hygiene.md` §1, "Post-state on the delivered bytes") and **S2**
(`S2-tools-docs.md`, "Self-test battery"), and by **V03** (`V03-c1-selftest.md`, delivered block):

```
CASE clean: exit=0 expected=0 findings=[] ok
…
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
SELF-TEST 17/17
RESULT PASS
EXIT=0
```

My re-run (command verbatim, repo root, delivered revision `03d04365…`/`153ebc5b…`):

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
rc=0
```

The 17th case is appended (`self_test_mismatch` last), all 16 inherited cases print `ok`, and the
contract's expectation set is exactly the 17 implemented cases. **Verdict: REPRODUCED.**

### A2 — C1(a): `SELF-TEST-MISMATCH` exits 2 (was exit 1) under a perturbed expectation — **REPRODUCED**

Quoted by **S1** §1 (pre-state `RESULT FAIL`/`EXIT=1`; delivered diff hunk `emit(1…)`→`emit(2…)`,
`return 1`→`return 2`), by **S2** ("C1(a) `SELF-TEST-MISMATCH` exits 2", after-block), by **V01**
(`V01-c1-mismatch-pin.md`: `SELF-TEST 16/17` / `FINDING SELF-TEST-MISMATCH` / `RESULT ERROR` / `EXIT=2`),
and by **V03** (pre-state `exit=1  # <-- the old exit-1 behavior`). S2's delivered quote:

```
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
SELF-TEST 16/17
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR
mismatch_exit=2
```

My re-run — scratch fakerepo holding byte-copies of the delivered tool and contract with
`self_test.expected.clean.exit` flipped 0→1 (the delivered contract never modified):

```
$ python3 <V48-scratch/delivered/fakemismatch>/corpus/tools/dependency_freeze.py --self-test
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
SELF-TEST 16/17
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR
rc=2
```

Baseline control — the same flip against the frozen r97 bytes (`git show 9a3d648:…` copied into a
fakerepo), reproducing the "was exit 1" half independently:

```
$ python3 <V48-scratch/base-mismatch/fakerepo>/corpus/tools/dependency_freeze.py --self-test
SELF-TEST 15/16
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT FAIL
rc=1
```

**Verdict: REPRODUCED** — identical terminal pair and exit 2 on the delivered revision; the r97 tool's
exit-1 behavior is real and is what C1(a) closes.

### A3 — C1(b): a path-less legacy pin is migrated in place by `--freeze` — **REPRODUCED**

Quoted by **S1** §2 (pre `SCOPE-REFUSED … already names None` / post `MIGRATED …` + `RESULT PASS`), by
**S2** ("C1(b) legacy path-less pin migrated by `--freeze`"), and by **V02**
(`V02-c1-legacy-migration.md` §2, same migration block plus fresh-process re-verify). S1's delivered
quote:

```
MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS             EXIT=0
```

My re-run — scratch fakerepo with the delivered tool/contract and the r95 fixture, the pin's `fixture`
key removed before the run:

```
$ python3 <V48-scratch/delivered/fakemigrate>/corpus/tools/dependency_freeze.py --freeze <fakerepo>/corpus/fixtures/r95-crossing-aftermath
MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
rc=0
pin fixture now: corpus/fixtures/r95-crossing-aftermath
```

Baseline control — the same path-less pin against the frozen r97 tool:

```
$ python3 <V48-scratch/base-probe/fakerepo>/corpus/tools/dependency_freeze.py --freeze <fakerepo>/corpus/fixtures/r95-crossing-aftermath
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pin r95-crossing-aftermath already names None; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR
rc=2
$ (contract sha256 before vs after)  → CONTRACT-UNCHANGED-BY-REFUSAL
```

The "was manual-only" pre-state (`SCOPE-REFUSED … already names None`) and the delivered migration are
both reproduced; the refusal is read-only (contract byte-unchanged). **Verdict: REPRODUCED.**

### A4 — C2: chain 6/6 clean and the V46 discharge (`REDUCTION-DETECTED` on the r97 tick-13 edge) — **REPRODUCED**

Quoted by **S1** §4 (freeze receipts + chain digest list + V46 discharge block + companion gates), by
**S2** ("C2 chain six fixtures + V46 discharge"), by **V05** (`V05-c2-chain-six.md` §1), and by **V06**
(`V06-c2-v46-discharge.md`: `FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5` /
`FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']`
/ `RESULT FAIL EXIT=1`). S1's chain quote (digests):

```
r88-m3-maya-cluster          DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279
r94-paired-crossing          DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
r95-crossing-aftermath       DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
r96-crossing-response        DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
r97-crossing-acknowledgment  DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6
r98-clerk-filing             DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
```

My re-run — the six verifies on the live tree:

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; done
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0     DIGEST 15ef230e… RESULT PASS  rc=0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1     DIGEST 2527beb9… RESULT PASS  rc=0
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1  DIGEST d541ae64… RESULT PASS  rc=0
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1   DIGEST d422a9b3… RESULT PASS  rc=0
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1  DIGEST 3c922d20… RESULT PASS  rc=0
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1        DIGEST 59a0f4fa… RESULT PASS  rc=0
```

My re-run — the V46 mutation in a scratch fakerepo (delivered tool/contract; the r97 copy's
`acknowledgment-aru-records.depends_on` emptied):

```
$ python3 <fakerepo>/corpus/tools/dependency_freeze.py <fakerepo>/corpus/fixtures/r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5; relations 1/1
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
RESULT FAIL
rc=1
```

Companion gates on the same mutated bytes (S1 §4 quotes these three as still green):

```
check_bible.py      CLEAN: schema, citations, relations, timeline; 0 violations    rc=0
support_check.py    SOURCE-SUPPORT 17/17; … MODES 19/19; VALIDATED-ROWS 19/19 / RESULT PASS  rc=0
map_obligations.py  OBLIGATIONS raw=17 mapped=17 / RESULT PASS                     rc=0
```

**Verdict: REPRODUCED** — six pins verify clean with the quoted digests; the r97 edge drop is caught
exactly (`4/5`, named finding, exit 1) where the other three gates stay green, matching V46's bar.

### A5 — C3: the r98 fixture gates on the delivered bytes — **REPRODUCED**

Quoted by **S3** §C, **S4** §C, **S5** ("Receipts"), **V11** §5 (once delivered), and **V22** §3.
Representative quote (S4 §C):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations          (exit 0)
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS                                                          (exit 0)
```

My re-run (delivered `timeline.json` `eb24e084…`, `entities.json` `db2d8e5d…`, `sources.json`
`32ee15b1…`):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations
rc=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS
rc=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS
rc=0
```

Discrimination replica — **V16**'s mandated probe P1 (drop `depends_on` from `clerk-filing-open`),
re-run on a scratch copy of the delivered fixture:

```
$ python3 corpus/fixtures/check_bible.py <scratch>/r98-clerk-filing
VIOLATION: timeline[6].depends_on: required nonempty list
1 violation(s); no canon changed
rc=1
```

**Verdict: REPRODUCED** — all three gates and the V16 probe output match the quotes character-for-character.

### A6 — C3-repair: the r95 one-sentence repair is receipt-neutral and pin-neutral — **REPRODUCED**

Quoted by **S3** §A (`diff` = `49c49` only; `wc -l` 53/53; sha `80440d61…`), by **V15**
(`V15-c3-r95-repair.md`: `1 1` numstat, single hunk, `DATAROWS-IDENTICAL 17 rows` sha `206fe137…`,
four receipts byte-identical, freeze `DIGEST d541ae64…` PASS), and by **V11** §§2–4 and **V16**
cross-check. V15's data-row quote:

```
$ cmp datarows-pre.txt datarows-post.txt  → DATAROWS-IDENTICAL 17 rows
  sha256 206fe137e8c24d243801eac1ea1ad42e9a5fc321b47f789d2624413c698af6e6  (both sides)
```

My re-run:

```
$ git diff --numstat 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/
1	1	corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
$ git diff -U0 9a3d648 -- …/claim-excerpt-map.md | grep -c '^@@'
1
$ cmp r95-pre-rows.txt r95-post-rows.txt && echo "DATAROWS-IDENTICAL $(wc -l < r95-post-rows.txt) rows"
DATAROWS-IDENTICAL 17 rows
$ sha256sum r95-post-rows.txt
206fe137e8c24d243801eac1ea1ad42e9a5fc321b47f789d2624413c698af6e6  r95-post-rows.txt
$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath   # receipt lines
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS                                                                      rc=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS                                                                      rc=0
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS                                                                      rc=0
```

The data-row block hash reproduces V15's `206fe137…` exactly; one line changed, one hunk, all r95
receipts unmoved, and the unchanged pin still verifies on the repaired tree (the map is not a pinned
data file). **Verdict: REPRODUCED.**

## 3. Extra corroboration (beyond the six, all re-run here)

- **Census** (quoted by V22 §2a and S5): my independent replica over `corpus/fixtures/*/` with
  repo-relative `check_bible.py` arguments →
  `CENSUS dirs=172 clean=38 negative=134 violation_lines=421 non01=0` (r97: 171/37/134/421), matching
  the quoted post-round values. REPRODUCED.
- **S5 addenda receipts** (quoted by S5): r96 `support_check` → `SOURCE-SUPPORT 16/16; … MODES 18/18;
  VALIDATED-ROWS 18/18` / `RESULT PASS` rc=0, `map_obligations` → `raw=16 mapped=16` PASS rc=0; r97
  `map_obligations` → `raw=17 mapped=17` PASS rc=0; r95 addendum values verified under A6. REPRODUCED.
- **C9 checker pair** (quoted by V22 §2d): `discriminate_check.py` → `RESULT: DISCRIMINATION HELD —
  silent-revert check would fail on regression` rc=0; `--checker e97613c` → `REGRESSION-DETECTED on
  r91-c1-null-chain,r91-c1-tick-unresolved` rc=2. REPRODUCED.
- **S2 README addendum** (quoted by S2): `git diff --numstat 9a3d648 -- corpus/tools/README.md` →
  `56 0`; sha `1d299c16…`. REPRODUCED. S5 addenda: `14 0` each; note sha `1162262c…`. REPRODUCED.
- **r98 preservation** (quoted by S3/S4/V16/V45/S5): `contradictions.json` `37517e5f…`,
  `relations.json` `c279254b…`, `inspiration-note.md` `58f5390e…`, `source-excerpt.md` `b5edc2fd…`
  (inherited, unchanged); r98 counts 6 entities / 1 relation / 7 events / 7 sources; event
  `clerk-filing-open` tick 14 at `chalk-stair` with `depends_on ["acknowledgment-aru-records"]` and
  source `clerk-filing-note`. REPRODUCED by hash and by read.

## 4. Observations (not verdicts; reported exactly as seen)

1. **Interim contract hash cited in S5's r98 note.** The delivered note
   `corpus/knowledge/r98-clerk-scope-note.md:64` cites `dependency_freeze.py` `03d04365…` (correct) but
   contract `c435239d…`; the delivered contract is `153ebc5b…` (S2 documents `c435239d…` as the third
   of four contract revisions; the interim bytes are not recoverable in-tree — no S1-scratch contract
   copy hashes `c435239d…`). The sentence is explicitly dated (`…at 20:32:51-03:00`) and is followed by
   "Re-run all three commands and re-measure the tool revisions against the delivered revision before
   citing these receipts", so it is self-guarding; recorded as a stale-interim-hash observation of the
   same class S5's own addenda repair, not a C3 claim failure.
2. **Parent-tree stray (r94-F01 class), unattributed.** `/home/vgpnk/Projects/shokunin/baseline-analyze.txt`
   (105 bytes, mtime 20:30, untracked in the parent repo) containing
   `python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py': [Errno 2] No such file or directory`.
   S2 (cross-seat observations), S3 (D5) and S1 (§6) record it; I confirmed it on disk. Not written by
   this seat; left in place as evidence for the closure sweep.
3. **Placeholder-window / existence-poll hazard** (recorded by S3 D1, S4 §A, V11 §0, V16 poll, S5 poll):
   between 20:28:24 and S4's rewrites, r98 `README.md`/`claim-excerpt-map.md` existed with r97 bytes, and
   an existence-only poll (V14's log; V11's false READY on `S4-scratch/`) can be satisfied by a
   placeholder or a directory. All six items above were re-run against the final non-placeholder bytes.
4. **Late S1 report absorbed.** S2's report closed with S1's report ABSENT at its hand-off; S1's report
   landed 20:35:33, before my first re-run — the r96/r97 late-landing class recurred and was absorbed
   without a stall escape (my dependency was producers only, all five present at try 21).
5. **No self-test scratch residue** after my runs (`ls -d dependency-freeze-self-test-*` → none);
   `git status --porcelain` shows only the declared ownership set.
6. **Concurrent sibling-lane activity (recorded, not this lane's).** During this seat's run,
   `/home/vgpnk/Projects/shokunin/MANIFEST.json` (mtime 20:38:09) and
   `/home/vgpnk/Projects/shokunin/kotodama-shokunin/{LOG.md,SCORECARD.md}` (mtime 20:37:36) moved —
   path ownership attributes them to the kotodama-shokunin lane (the r97 closure recorded the same
   class, e.g. commit `b0bb880`); read-only metadata checks only, nothing written by this seat.

## Bottom line

**PASS — 6/6 load-bearing quoted outputs from other seats re-run independently: 6 REPRODUCED,
0 MISMATCHED** (S1/S2/V03 self-test 17/17; S1/S2/V01/V03 `SELF-TEST-MISMATCH` exit 2 with an
independently reproduced exit-1 baseline control; S1/S2/V02 path-less pin migration with an
independently reproduced `SCOPE-REFUSED … already names None` baseline control; S1/S2/V05/V06 chain 6/6
plus the V46 `REDUCTION-DETECTED` discharge with companion gates green; S3/S4/S5/V11/V16/V22 r98 gates
`CLEAN` + `raw=20 mapped=20` + `20/20` with the V16 P1 probe replica; S3/V15/V11 r95 one-line repair
with byte-identical data rows `206fe137…` and unmoved receipts/pin). Extra corroboration (census
172/38/134/421, S5 addenda receipts, C9 pair, S2 README) reproduced. Observations in §4 — one interim
contract hash in S5's dated note, one parent-tree stray of the r94-F01 class, the placeholder window,
and the late S1 landing — are recorded exactly; none harms a claimed axis.
