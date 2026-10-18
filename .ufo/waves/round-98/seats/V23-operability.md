# V23 operability — round 98

Seat: V23 (verifier, operability). Lane repo
`/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline r97 closure `9a3d648`;
the wave tree was uncommitted during the round; HEAD `dd4df1b`. All commands ran
from the lane root with `python3` unless a scratch tree's own root is stated.
Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this
report (absolute) and `.ufo/waves/round-98/seats/V23-scratch/` only. No live-tree
file was written by this seat; the delivered tool/contract bytes were re-hashed
before and after the final battery and are unchanged.

**Charge:** after producers, every documented command in the S4 README + S5
notes + tools README addendum runs as written.

## 0. Poll record (content-gated, 20 s cadence, 40 tries)

First poll used existence-only checks and was restarted after the r98 directory
appeared holding byte-identical r97 placeholders (README/map `cmp`-identical to
r97 at 23:28 UTC) — the placeholder class S4's own report warns about. Second
poller gated on content markers (`grep clerk` in the map, `Round 98` in the
README, diff-vs-`9a3d648` for the S5 addenda and tools README, report files):

- S3 tables landed ~23:28:55 UTC (6 entities / 1 relation / 7 events / 7 sources);
- S5 addenda r95/r96 ~23:29; S4 map ~23:30:27; S4 README ~23:30:47;
- S5 `r98-clerk-scope-note.md` ~23:32:47; S2 tools README addendum ~23:33:47;
- reports: S3 23:30:47, S4 23:32:07, S5 23:32:27, S2 23:33:47, S1 23:35:27.
  ALL-PRESENT at try 20 (23:35:27 UTC). No ABSENT condition; no stall-escape
  needed; no all-reports poll ran without SELF subtraction (no all-reports poll
  was needed — my dependency set was the five artifacts + S1/S2/S4/S5 reports).

## 1. S4 README — replay block (verbatim), `corpus/fixtures/r98-clerk-filing/README.md:25-29`

```
python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
  → CLEAN: schema, citations, relations, timeline; 0 violations   exit=0
python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
  → INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
    ANCHORS repeated-references=4; DUPLICATE-ROWS 0
    RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
    SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; MODES 22/22; VALIDATED-ROWS 22/22
    RESULT PASS   exit=0
python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
  → OBLIGATIONS raw=20 mapped=20
    INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
    RESULT PASS   exit=0
```

All three run as written from the lane root; outputs and exit codes match the
README's documented receipt claims. S4's report hashes re-verified on the
delivered bytes: `README.md` sha256 `32efc78f…`, `claim-excerpt-map.md`
`c1099d0e…`.

## 2. S5 notes — documented commands

- `r98-clerk-scope-note.md:51-62` receipts block = the same trio on the r98
  fixture (run above; every cited receipt line reproduced exactly, including
  `DISTINCT-ANCHORS 18/18`, `ANCHORS repeated-references=4`).
- Note prose claim `:64` "the r97 fixture reads `raw=17 mapped=17` / `RESULT
  PASS` exit 0" — reproduced (`OBLIGATIONS raw=17 mapped=17`, `RESULT PASS`,
  exit 0).
- Note prose `:64` "r95/r96 receipts were re-derived at the same revisions and
  are unchanged (`raw=15 mapped=15` and `raw=16 mapped=16`, both RESULT PASS)"
  — reproduced; `support_check` r95 `15/15`/`TOTAL 17/17` and r96 `16/16`/`TOTAL
  18/18` also reproduced, `RESULT PASS` exit 0 both.
- Addenda (r95/r96 knowledge notes), fenced command run verbatim:

```
sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json
# 86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
# 2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
```

Both hashes match the addenda's documented values exactly. The addenda's
`check_bible.py` `ff9fd2aa…` / `support_check.py` `55a5eb27…` claims were
re-measured and hold.

## 3. S2 tools README addendum (`corpus/tools/README.md:230-282`)

### 3a. Six-fixture chain loop (fenced block, verbatim)

Ran verbatim from the lane root; all six print `FREEZE …`, `DIGEST …`,
`RESULT PASS`, exit 0. Added receipts match the documented values:
`FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations
1/1` digest `3c922d20a01bbd3f…`; `FREEZE r98-clerk-filing: events 7/7;
dependency-edges 6/6; relations 1/1` digest `59a0f4fa3d4a47e0…`.

### 3b. `--self-test` (fenced): `SELF-TEST 17/17` / `RESULT PASS`, exit 0. ✓

### 3c. Path-less legacy pin migration (fenced demo)

Reproduced in scratch tree `V23-scratch/mig/` (own tool+contract copy with
`pins.r95-crossing-aftermath.fixture = null`, own r95 fixture copy), run from
that tree's root:

```
(1) verify before migration:
    FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs a repo-relative fixture path
    RESULT ERROR   exit=2
(2) python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r95-crossing-aftermath
    MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath
    FROZEN … / DIGEST d541ae64… / FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
    RESULT PASS   exit=0
(3) verify after migration: RESULT PASS exit=0
```

Exactly as documented, including the fail-closed pre-migration line.

### 3d. Same-named different-path guard (r97 guard unchanged)

Scratch copy at `corpus/fixtures/sub/r95-crossing-aftermath` (pin names
`corpus/fixtures/r95-crossing-aftermath`): `FINDING SCOPE-REFUSED: --freeze
refuses corpus/fixtures/sub/r95-crossing-aftermath: pin r95-crossing-aftermath
already names 'corpus/fixtures/r95-crossing-aftermath'; …`, `RESULT ERROR`,
exit 2. ✓

### 3e. `SELF-TEST-MISMATCH` exit-code alignment (prose demo, reproduced)

Scratch tree `mismatch/` with the delivered tool + a contract copy whose
`self_test.expected.clean.exit` is flipped 0→1:

```
delivered revision:  SELF-TEST 16/17
                     FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
                     RESULT ERROR   exit=2
r97 revision (git show 9a3d648:… + r97 contract copy, same flip):
                     SELF-TEST 15/16
                     FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
                     RESULT FAIL    exit=1
```

Both match the documented before/after. (First attempt to reproduce the "before"
used the delivered 17-case contract with the old tool; that correctly fails
earlier with `CONTRACT-INVALID: … extra=['self_test_mismatch']` — the strict
set check — so the reproduction was redone with the r97 contract as the
addendum describes.)

### 3f. V46 discharge (prose demo, reproduced)

Scratch tree `v46/` (delivered tool + contract, r97 fixture copy):
control `RESULT PASS` exit 0 (digest `3c922d20…`); with the tick-13 edge
dropped (`acknowledgment-aru-records` losing `depends_on:
["response-evin-salt-court"]`) — `FREEZE r97-crossing-acknowledgment: events
6/6; dependency-edges 4/5; relations 1/1`, `FINDING REDUCTION-DETECTED: event
acknowledgment-aru-records lost depends_on ['response-evin-salt-court']`,
`RESULT FAIL`, exit 1 — the exact documented finding text. Pre-pin state
(r97 tool + r97 contract, tree `prepin/`): `FINDING UNPINNED-FIXTURE … (pinned:
['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath',
'r96-crossing-response'])`, `RESULT ERROR`, exit 2. ✓

### 3g. Contract `precedence` text and the 17th case

`dependency-freeze-contract.json` `precedence` field reproduces the documented
exit-2 order and finding IDs verbatim (`UNPINNED-FIXTURE`/`CONTRACT-INVALID`,
`FIXTURE-MISSING`, `PATH-MISMATCH`, `FILE-MISSING`/`MALFORMED-JSON`/
`MALFORMED-MODEL`, `DIGEST-MISMATCH`, `INVALID-ARGUMENTS`, `SELF-TEST-MISMATCH`,
plus `SCOPE-REFUSED` for `--freeze`) and records the migration sentence. The
self-test expectation set: old 16 → new 17, new-only `self_test_mismatch`
(`exit: 2`, `['SELF-TEST-MISMATCH']`), and the 16 inherited expectations are
byte-equal to the `9a3d648` contract. ✓

### 3h. "Unchanged" claims

- `map_obligations.py --self-test`: `SELF-TEST CASES 25/25 pinned` …
  `RESULT PASS`, exit 0. ✓
- `git diff --name-only 9a3d648 -- corpus/tools/map_obligations.py
  corpus/tools/support_check.py corpus/tools/boundary_doc_check.py
  corpus/tools/map-obligations-contract.json corpus/tools/boundary-doc-contract.json`
  → empty; the three other tools and both other contracts are byte-unchanged. ✓
- **Minor discrepancy (recorded):** the addendum's literal sentence
  "`git diff 9a3d648 -- corpus/tools/` lists only `dependency_freeze.py` and
  `dependency-freeze-contract.json`" does not hold at the delivered revision:
  the same command now also lists `corpus/tools/README.md` — the addendum's own
  file. Self-reference artifact; the sentence's intent (other tool code
  unchanged) is verified above. No command behavior is affected.

## 4. Findings (contradictions are evidence)

1. **F1 (minor, documentation): the addendum's BR-05 parenthetical is false at
   the delivered revision.** `corpus/tools/README.md:232` (r98 addendum first
   paragraph) says the r94 residual BR-05 is "the self-test scratch still lives
   under the repository root and is not gitignored — unchanged in r98". The
   delivered `.gitignore:4` is `*-self-test-*/`, `git check-ignore -v
   dependency-freeze-self-test-probe/ map-obligations-self-test-probe/` returns
   `.gitignore:4:*-self-test-*/`, and the r97 supersession paragraph at
   `README.md:228` in the same file states the scratch is "covered by
   `.gitignore` (`*-self-test-*/`)" — as does the r97 closure record (C-4). The
   stale "not gitignored" phrasing is inherited and recurs at `:103`, `:123`,
   `:179`, `:232` (and the r94-era statement at `:99`); none of those addendum
   openings was updated after r97 discharged the ignore half. The remaining
   BR-05 residual is the scratch *location* (repo root), not its ignore status.
   Bounded: prose only; no documented command or exit code is affected. S2's
   report repeats the same stale phrasing, so the two agree with each other but
   not with the tree.
2. **F2 (minor, documentation): the addendum's `git diff … lists only` sentence
   is self-refuting at the delivered revision** (README.md is itself in the
   path scope). See 3h.
3. **Time-bound, not a defect:** the S5 r98 note's parenthetical "those two
   [dependency_freeze] files still read their r97-closure bytes at this pass's
   measurement" was true at S5's 20:31 measurement but is stale at the
   delivered revision (final bytes `03d04365…`/`153ebc5b…`, S1's report). The
   note itself instructs re-measuring before citing; the note's map_obligations
   hashes remain exact.

## 5. Hygiene / adjacency

- Delivered tool/contract hashes were stable before and after my final battery:
  `dependency_freeze.py` `03d04365cf00903e…`, contract `153ebc5b2092948e…`
  (match S1's report).
- `git status --short` after my runs shows only the declared round change set
  (LOG, r95 map repair, r95/r96 addenda, tools README + two dependency_freeze
  files, new r98 fixture dir, new r98 scope note) — no strays from this seat.
- Repo-root scratch: only `v05-self-test-scratch/` (another seat's; matched by
  `.gitignore:4` and absent from `git status`). My `--self-test` runs leave no
  repo-root residue (temp dirs removed).
- Cross-seat evidence (not mine, already reported by S2): the parent-tree stray
  `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` exists (105 bytes,
  `python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py' …`) —
  the r94-F01 stray class, outside the lane repo; recorded for the closure
  sweep.

## 6. Bounds

This seat verifies that documented commands execute as written and that their
documented outputs/exit codes reproduce; it does not re-adjudicate C1/C2/C3
correctness beyond what those commands expose, does not re-derive the pins, and
did not run `--freeze` against the delivered contract or fixture (all freeze
demos ran in scratch trees with their own tool+contract+fixture copies). F1/F2
are prose-accuracy findings; whether they gate admission is the adjudicator's
call.

**Bottom line: PASS** — every documented command in the S4 README, the S5 notes
and addenda, and the S2 tools README addendum runs as written from the lane
root with the documented outputs and exit codes (trio 20/20 & 22/22 PASS,
self-test 17/17, chain 6/6, migration/SCOPE-REFUSED/mismatch-exit-2/V46 demos
reproduced, sha256sum exact); two minor prose staleness items recorded (F1 the
BR-05 "not gitignored" claim, F2 the "lists only" self-reference).
