# V28 — verdict-operability (round 98)

Seat: V28 verdict-operability. Exclusive write scope: this report plus
`.ufo/waves/round-98/seats/V28-scratch/` (all absolute under the lane repo
`/home/vgpnk/Projects/shokunin/lore-shokunin`; the session cwd is the parent repo).
No product file written, no commit, no push, no network, no nested agents. All
commands run from the lane root with `python3` (3.14.7). Baseline: r97 closure
`9a3d648` (HEAD `dd4df1b` during the round; wave tree uncommitted). One
operability verdict.

Task as seated: after the producers land, run **every documented command in the
round's new documentation surfaces** (S2's tools README Round-98 addendum, S4's
r98 fixture README, S5's r98 knowledge note and the two dated correction addenda)
exactly as written, check the 0/1/2 exit contracts, and additionally probe the
round's operability-bearing C1/C2 behaviors (SELF-TEST-MISMATCH exit class,
legacy-pin migration, six-fixture chain, V46 discharge). Never verify a plan.

## 0. Poll-wait, landing order, frozen revision

Own poll (`V28-scratch/poll.sh`, 20 s cadence, 40 tries) watching the five
producer reports plus the r98 fixture files and the r98 knowledge note. Recorded
landings (local time -03 unless marked):

| Artifact | Landed |
|---|---|
| r98 fixture 10-file tree (S3 byte copy of r97, placeholder README/map) | 20:28 |
| S3 data edits (`clerk-maren`, `clerk-filing-open`, `clerk-filing-note`, excerpt section) | 20:28:55 |
| S4 `claim-excerpt-map.md` (20 rows) / `README.md` rewrites | 20:30 / 20:30:41 |
| S1 `dependency_freeze.py` final (`03d04365…`) | 20:31:49 |
| S1 `dependency-freeze-contract.json` final (`153ebc5b…`; two earlier revisions observed and discarded) | 20:33:36 |
| S2 `corpus/tools/README.md` final (`1d299c16…`) | 20:34:06 |
| S5 r95/r96 correction addenda (20:28); r98 knowledge note (20:32) | 20:28–20:32 |
| Reports: S3 20:31 · S4 20:32 · S5 20:33 · S2 20:34 · S1 20:35:38 | |

**Poll result: ALL-PRESENT at try 23 of 40 (23:35:38 UTC / 20:35:38 local) —
S1's report was the last item; no ABSENT condition, no stall escape needed.**
No artifact was verified before it existed; S1's contract moved during the wait
(observed by this seat at `c435239d…` then final `153ebc5b…`; S2's report records
two earlier revisions) and every receipt below was run against the final
revision. Endgame convention honoured: the poll waited on the five producer
reports only — not on SELF, not on all seats.

Frozen revision for every receipt below (sha256; re-verified **after** the whole
battery — `hashes-before-clean.txt` vs `hashes-after-clean.txt` → `HASHES-IDENTICAL`):

```
1d299c16bf9a0b34526f4a799cdd3117867f6d4d278866b66366b78700d79b84  corpus/tools/README.md
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8  corpus/knowledge/r98-clerk-scope-note.md
8e9e1774c1072bd1476d86977804e945301e4583acbfcb80a81b37a2334d4827  corpus/knowledge/r95-aftermath-scope-note.md
a9b51f8ccd78e0dcd8b5e890183068e48cdccd195065c43212211b65ee25f048  corpus/knowledge/r96-response-scope-note.md
db2d8e5d… / 32ee15b1… / eb24e084… / 29e384bf…  r98 {entities,sources,timeline}.json / fictional-excerpts.md
c1099d0e… / 32efc78f…  r98 claim-excerpt-map.md / README.md
```

These match the producers' own cited revisions (S1: `03d04365…`/`153ebc5b…`; S2:
`1d299c16…`; S5: r98 note `1162262c…`; S3: `80440d61…`, r98 JSONs). Transcripts:
`V28-scratch/{battery-final.txt, delivered-chain.txt, probes-output.txt,
before-probes.txt, extra-probes.txt, v46-crosschecks.txt, final-probes.txt,
envvar-probe.txt, preflight-receipts.txt}` — no pipelines in the harnesses
wherever a tool exit code mattered (after the r96 lesson that `cmd | tail` masks
the tool's exit with `tail`'s).

## 1. Documented-command replay — run exactly as written

### 1.1 S4 r98 fixture README replay block (README:25–29)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations                  EXIT=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS                                                                  EXIT=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS                                                                  EXIT=0
```

README count claims reproduce: README:3 "6 entities / 1 relation / 7 events / 7
sources" → parsed counts `6 1 7 7` (S3 report §B, re-read this pass); README:21
"20 source-attributed JSON pointer obligations" → `raw=20 mapped=20`; the map's
`**Expected inventory:** 20 / 2 / 22 / 18` → the support_check INVENTORY line.
The README is no longer the r97 placeholder: sha `32efc78f…` vs r97's
`d9387b7d…`; the map sha `c1099d0e…` vs r97's `49d4834e…`.

### 1.2 S5 r98 knowledge-note receipts block (note:51–61) and the r97 retained replay

Same three commands; every quoted receipt line matches verbatim (§1.1 and below).
The r97 fixture replay block (r97 README:25–29) reproduces:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
CLEAN: … 0 violations                                                         EXIT=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15
… RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19 / RESULT PASS        EXIT=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17 / INVENTORY 17/17; 2/2; 19/19 / RESULT PASS      EXIT=0
```

The note's census claim reproduces: `ls -d corpus/fixtures/*/ | wc -l` → **172**
(171 at r97 closure; +1 for r98-clerk-filing). No fabricated receipt found.

### 1.3 S5 dated addenda receipts (r95/r96 notes)

```
sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json
  86b52949… / 2142b991…        (matches both addenda; check_bible ff9fd2aa…, support_check 55a5eb27… also current)
r95: check_bible CLEAN EXIT=0 · support_check 15/15; 2/2; 17/17 PASS EXIT=0 · map_obligations raw=15 mapped=15 PASS EXIT=0
r96: check_bible CLEAN EXIT=0 · support_check 16/16; 2/2; 18/18 PASS EXIT=0 · map_obligations raw=16 mapped=16 PASS EXIT=0
```

The r95 receipts are unchanged by S3's one-line map repair (the changed line is
prose in `## Timeline normalization and scope`, not a data row, not the
`**Expected inventory:**` line — `git diff` shows exactly 1 insertion / 1
deletion; map sha `30281ff1…` → `80440d61…`; the freeze pin `d541ae64…` is over
the five JSON tables and still verifies PASS).

### 1.4 S2 tools README Round-98 addendum

Chain loop exactly as written (README Round-98 addendum block):

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath \
         r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
    python3 corpus/tools/dependency_freeze.py "corpus/fixtures/$f"; echo "$f exit=$?"; done
r88 … events 2/2; 0/0; 0/0   DIGEST 15ef230e…  RESULT PASS  exit=0
r94 … events 3/3; 2/2; 1/1   DIGEST 2527beb9…  RESULT PASS  exit=0
r95 … events 4/4; 3/3; 1/1   DIGEST d541ae64…  RESULT PASS  exit=0
r96 … events 5/5; 4/4; 1/1   DIGEST d422a9b3…  RESULT PASS  exit=0
r97 … events 6/6; 5/5; 1/1   DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6  RESULT PASS  exit=0
r98 … events 7/7; 6/6; 1/1   DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133  RESULT PASS  exit=0
```

The two added receipts match the addendum's quoted digests (`3c922d20a01bbd3f…`,
`59a0f4fa3d4a47e0…`); the four pre-round digests equal the r97 pins.

```
$ python3 corpus/tools/dependency_freeze.py --self-test
… 17 × "CASE <case>: exit=<0|1|2> expected=<…> findings=[…] ok" …
SELF-TEST 17/17
RESULT PASS                                                                  EXIT=0
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 25/25 pinned … RESULT PASS                                   EXIT=0
```

The 17 printed cases match the persisted contract set exactly; the 16 inherited
expectations are byte-identical to `git show 9a3d648:…` (case-by-case python
compare: added `['self_test_mismatch']`, dropped `[]`, changed `[]`); the four
inherited pins are byte-identical to the r97 contract. The addendum's `--freeze`
migration code block is documented as a scratch-tree demo; reproduced on a mirror
root (§2.2) — the delivered tree was never re-frozen by this seat.

## 2. C1 operability probes (before/after, mirror roots only)

### 2.1 `SELF-TEST-MISMATCH` exit class

Before, on the pinned baseline bytes (`git show 9a3d648:…` into a mirror; contract
copy with `self_test.expected.clean.exit` flipped 0→1):

```
CASE clean: exit=0 expected=1 findings=[] MISMATCH
SELF-TEST 15/16
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT FAIL                                                                  EXIT=1
```

After, same flipped contract against the delivered tool:

```
CASE clean: exit=0 expected=1 findings=[] MISMATCH
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
SELF-TEST 16/17
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR                                                                 EXIT=2
```

Both match the README addendum's quoted before/after verbatim; the exit-1→exit-2
change is load-bearing and the 17th case is exercised by the delivered self-test.

### 2.2 Path-less legacy pin migration

Before (baseline tool, `pins.r95-crossing-aftermath.fixture = null`):

```
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pin r95-crossing-aftermath already names None; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR                                                                 EXIT=2
```

After (delivered tool, same mirror):

```
MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
RESULT PASS                                                                  EXIT=0
post: migrated fixture value = 'corpus/fixtures/r95-crossing-aftermath'
re-verify after migration → FREEZE 4/4; 3/3; 1/1 / RESULT PASS               EXIT=0
```

Bounds confirmed on the same revision: plain verify before migration → `FINDING
CONTRACT-INVALID: pin r95-crossing-aftermath needs a repo-relative fixture path`
EXIT=2; a pin recording a *different* path → `SCOPE-REFUSED … already names
'corpus/fixtures/foreign/r95-crossing-aftermath'` EXIT=2 (r97 guard retained).

### 2.3 Contract `precedence` text

Delivered text names the exit-1 findings (`REDUCTION-DETECTED`,
`ADDITION-DETECTED`, `ENDPOINT-CHANGE`), the full exit-2 order (`UNPINNED-FIXTURE`
/ `CONTRACT-INVALID` → `FIXTURE-MISSING` → `PATH-MISMATCH` → `FILE-MISSING` /
`MALFORMED-JSON` / `MALFORMED-MODEL` → `DIGEST-MISMATCH` → `INVALID-ARGUMENTS` →
`SELF-TEST-MISMATCH`), the `--freeze` `SCOPE-REFUSED` class, and the migration
rule. Checked against the delivered code path order: `verify()` = `pin_for` →
`is_dir` → `bind_path` → `build_model` → `compare`/digest; `freeze()` raises
`scope_guard`/same-named-elsewhere first; `INVALID-ARGUMENTS` in `main`;
`SELF-TEST-MISMATCH` only in `run_self_test`. Consistent; every named ID exists in
the tool.

## 3. C2 operability probes

- Chain 6/6 as written (§1.4): all PASS exit 0, digests match the pins; delivered
  contract carries exactly six pins (four inherited byte-identical to the r97
  contract, two added).
- V46 discharge, reproduced on a scratch mirror with the delivered tool+contract:
  dropping `acknowledgment-aru-records.depends_on: ["response-evin-salt-court"]`
  gives `FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5` /
  `FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on
  ['response-evin-salt-court']` / `RESULT FAIL` **EXIT=1**; the unmodified mirror
  copy is PASS exit 0. The r97 pin's digest `3c922d20…` equals the digest V46
  recorded in its r97 scratch mirror (`round-97/seats/V46-cross-gates.md:101`).
  The same mutation on the r98 tick-14 edge
  (`clerk-filing-open` losing `acknowledgment-aru-records`) also gives
  `REDUCTION-DETECTED` exit 1. On the mutated r97 bytes the other three gates stay
  green, as S1 §4 claims: `check_bible` CLEAN exit 0; `support_check` 17/17 PASS
  exit 0; `map_obligations` `raw=17 mapped=17` PASS exit 0.

## 4. Exit contract 0/1/2 on the claimed paths

| Path (as documented) | Documented | Observed exit | Terminal line |
|---|---|---|---|
| r98 fixture (S4 README, S5 note) | 0 | 0 | `RESULT PASS` / `CLEAN` |
| r97 retained replay | 0 | 0 | `RESULT PASS` |
| r95 / r96 addendum receipts | 0 | 0 | `RESULT PASS` |
| chain ×6 (`dependency_freeze`) | 0 | 0 | `RESULT PASS` (6/6) |
| `dependency_freeze --self-test` | 0 | 0 | `RESULT PASS` (17/17) |
| `map_obligations --self-test` | 0 | 0 | `RESULT PASS` (25/25) |
| flipped-expectation self-test, before / after | 1 / 2 | 1 / 2 | `RESULT FAIL` / `RESULT ERROR` |
| `--freeze` on a path-less pin, before / after | 2 / 0 | 2 / 0 | `SCOPE-REFUSED` / `MIGRATED … RESULT PASS` |
| verify a path-less pin (before migration) | 2 | 2 | `CONTRACT-INVALID` |
| `--freeze` a same-named-elsewhere pin | 2 | 2 | `SCOPE-REFUSED` |
| r97/r98 edge mutation (freeze) | 1 | 1 | `REDUCTION-DETECTED` |

Usage probes: `--self-test` combined with a fixture → `INVALID-ARGUMENTS` exit 2
(covered by the persisted `invalid_arguments` case). cwd-independence probe: run
from `/tmp` with absolute paths → `FREEZE r88-m3-maya-cluster … RESULT PASS` exit
0 (ROOT resolves from the script path).

## 5. Preservation and residue

- `git status --porcelain` identical before and after the whole battery
  (`git-status-before-battery.txt` vs `-after-battery.txt`, `diff` clean): ` M`
  LOG.md, r95 map, r95/r96 notes, tools README, dependency_freeze.py, contract;
  `??` r98 fixture, r98 note, `.ufo/waves/round-98/`. No corpus modification by
  this seat; every probe ran on mirror roots under `V28-scratch/probes/`.
- Frozen hashes re-verified identical after all runs (§0). No leftover self-test
  scratch from this seat: transient `*-self-test-*` dirs observed mid-wave were
  concurrent seats' in-flight runs and cleaned themselves; the only resident
  match is `v05-self-test-scratch` (another seat's declared scratch). Both tools'
  self-test scratch lands at the repo root and is gitignored (`*-self-test-*/`) —
  the documented r94 BR-05 residual, unchanged.
- Stray check (r94-F01 class): `find /home/vgpnk/Projects/shokunin -maxdepth 4
  -name 'r98-clerk-*' -not -path '*/lore-shokunin/*'` → empty. The parent-repo
  stray `baseline-analyze.txt` (105 bytes, mtime 20:30, content a captured
  `python3: can't open file …/analyze.py` error) is recorded by S1 §6 and S3 §D5;
  not written by this seat, left untouched.

## Findings summary (all failures/absences/edges reported exactly)

1. **F1 — documentation-precision finding (bounded).** The Round-98 addendum's
   "Unchanged" paragraph (and S1 §6, S2 report §Self-test battery) states:
   "`git diff 9a3d648 -- corpus/tools/` lists only `dependency_freeze.py` and
   `dependency-freeze-contract.json`". Measured, `git diff --name-only 9a3d648 --
   corpus/tools/` lists **three** paths — `corpus/tools/README.md`,
   `corpus/tools/dependency-freeze-contract.json`, `corpus/tools/dependency_freeze.py`
   — because the addendum's own README edit is inside that scope. The substantive
   claim holds (`map_obligations.py`, `map-obligations-contract.json`,
   `support_check.py`, `boundary_doc_check.py` are byte-unchanged); the sentence is
   inaccurate only as literally written. Owner: S2 (README) / S1 (report §6).
2. **F2 — self-test hermeticity edge (bounded).** With
   `DEPENDENCY_FREEZE_SELF_TEST_CHILD=1` set in the ambient environment,
   `dependency_freeze.py --self-test` prints `SELF-TEST 16/17` / `FINDING
   SELF-TEST-MISMATCH: cases failed: ['self_test_mismatch']` / `RESULT ERROR`
   exit 2. The variable is the tool's own internal recursion marker, never
   exported to a parent shell by the tool; normal environments cannot set it
   accidentally, so this is a recorded edge, not a defect.
3. **F3 — r97 V27 operability finding resolved (positive).** The r97 seat recorded
   the dependency_freeze README addendum as absent and README:175 as stale
   (14/14, open hazards). The r97 supersession plus the Round-98 addendum now
   document the tool and mark every stale number as superseded; re-verified this
   pass.
4. **F4 — S1 report landing.** S1's report was the last artifact (20:35:38 local,
   poll try 23/40); S2's report had recorded it ABSENT at its own hand-off. No
   verification was done against a plan: every S1 claim above was reproduced
   against the delivered bytes independently.
5. No other documented command failed as written: r98/r97/r95/r96 replays, both
   self-tests, the chain loop, the migration demo (mirror), the before/after
   mismatch demo, and the V46 discharge all reproduce their documented output and
   exit codes on the frozen revision.

## Bottom line

PASS — every documented command in S4's r98 README, S5's r98 note and dated
addenda, and S2's Round-98 tools README addendum runs as written on the frozen
revision (r98 `raw=20 mapped=20` CLEAN/PASS exit 0; r97 17/17, r95 15/15, r96
16/16; self-test 17/17; chain 6/6 with the documented digests; census 172), and
the round's operability-bearing C1/C2 behaviors are independently reproduced —
SELF-TEST-MISMATCH now exits 2 and is pinned (before 15/16 FAIL exit 1 vs after
16/17 ERROR exit 2), path-less legacy pins migrate by `--freeze` (`MIGRATED …`
exit 0; verify-before-migration and different-path refusal both still exit 2),
the contract precedence text matches the code path order, and V46's r97-edge FAIL
is discharged (scratch REDUCTION-DETECTED exit 1, pin digest equal to V46's
recorded scratch digest; r98 edge likewise) — with two bounded findings recorded
(F1 the `git diff` scope sentence is inaccurate as written; F2 the internal
self-test marker env var can force a spurious 16/17 exit 2) and no axis harmed.
