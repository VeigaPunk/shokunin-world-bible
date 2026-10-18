# V35 integration-checklist — round 98 (L1 pre-closure checklist)

- Seat: V35 integration-checklist (verifier). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline r97 closure `9a3d648` (pre-round bytes via `git show 9a3d648:<path>`); wave tree uncommitted; HEAD during the round `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb`.
- Writes: this report (absolute path, verified before writing), `.ufo/waves/round-98/scratch/V35/**` (battery, probes, logs) only. No commits, no pushes, no network, no nested agents, no other lane file written.
- Scope: the L1 pre-closure checklist for C1/C2/C3 — every receipt below was measured by me on the frozen revision, not read from a producer report. Producer reports were read afterwards for cross-check only.

## 0. Revision pinned for every measurement (hashes stable ≥ 3 min before and after my runs)

```
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json
1d299c16bf9a0b34526f4a799cdd3117867f6d4d278866b66366b78700d79b84  corpus/tools/README.md
c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba  corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md
32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926  corpus/fixtures/r98-clerk-filing/README.md
1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8  corpus/knowledge/r98-clerk-scope-note.md
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  corpus/fixtures/r98-clerk-filing/entities.json
eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af  corpus/fixtures/r98-clerk-filing/timeline.json
32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3  corpus/fixtures/r98-clerk-filing/sources.json
80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
8e9e1774c1072bd1476d86977804e945301e4583acbfcb80a81b37a2334d4827  corpus/knowledge/r95-aftermath-scope-note.md
a9b51f8ccd78e0dcd8b5e890183068e48cdccd195065c43212211b65ee25f048  corpus/knowledge/r96-response-scope-note.md
```

Baseline receipts measured before any producer landed (pre-state for the before/after pairs): `dependency_freeze --self-test` **16/16** `RESULT PASS` exit 0; chain r88/r94/r95/r96 exit 0 and `r97-crossing-acknowledgment` → `FINDING UNPINNED-FIXTURE … RESULT ERROR` exit 2; `map_obligations --self-test` 25 cases PASS; r97 map 17/17 PASS; `check_bible` r97 CLEAN; census 171 dirs.

## 1. Poll-wait record (20 s cadence; never verified a plan)

- ~20:27 first inspection: no `corpus/fixtures/r98-clerk-filing/`, no producer reports (only `V06-scratch`/`V11-scratch`); S1/S2/S3/S4/S5 artifacts all UNCHANGED vs `9a3d648`.
- 20:28:24 S3's directory appeared with r97 byte-copies (placeholder phase); 20:28:55 S3's authored content landed; 20:29–20:30 S5's addenda and S4's README/map landed; 20:31:20–20:31:30 S1's tool/contract landed, with the contract changing twice more (`3a940a9f… → c435239d… → 153ebc5b…`) while S1 re-froze; the six-pin set appeared at ~20:33.
- Reports: S3 20:31, S4 20:32, S2/S5 20:34, **S1's report `S1-freeze-hygiene.md` landed ~20:36 — absent for the first ~9 minutes of my polling**. I did not verify any plan: all C1/C2/C3 results below were measured against the delivered bytes; the S1-report wait was bounded (my own poll + a targeted 30×20 s watcher) and resolved before I wrote this report. No stall escape was needed and no all-reports poll ever waited on SELF.
- Honest defect in my own first poller: its S1 glob `^S[1-5]` matched the directory name `S1-scratch`, so it printed `ALL5_REPORTS` while S1's report was still absent. Caught by listing `*.md` explicitly; the later watcher used `^S1-.*\.md$`.

## 2. C1 — calibration (dependency_freeze hygiene): **VERIFIED**

**(a) `SELF-TEST-MISMATCH` exits 2 (was 1), pinned as case 17.** My probe copies tool+contract+base fixture into a scratch mirror root, flips `self_test.expected.clean.exit` 0→1 in the mirror contract only, and runs `--self-test`:

```
# delivered revision
SELF-TEST 16/17
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR
--- delivered exit=2 ---
# baseline bytes (git show 9a3d648:…)
SELF-TEST 15/16
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT FAIL
--- baseline exit=1 ---
```

Delivered self-test on the delivered contract: 17 `CASE … ok` lines (16 inherited + `self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok`), `SELF-TEST 17/17` / `RESULT PASS` / exit 0. Case-by-case contract diff vs baseline: `added: ['self_test_mismatch'] dropped: [] changed inherited expectations: [] INHERITED-UNCHANGED: True`.

**(b) Path-less legacy pin migrated in place by `--freeze`.** Scratch mirror, r95 pin's `fixture` key removed:

```
delivered: FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
           FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
           RESULT PASS   exit=0
           post-run pin fixture field: 'corpus/fixtures/r95-crossing-aftermath'
baseline:  FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath:
           pin r95-crossing-aftermath already names None; …   RESULT ERROR   exit=2
           post-run pin fixture field: None
```

The different-path refusal is retained (S1's `post2` probe: `already names 'corpus/fixtures/r95-crossing-aftermath-copy'` → exit 2), so only the path-less class migrates.

**(c) `precedence` text complete.** Delivered contract names the exit-1 findings (`REDUCTION-DETECTED`, `ADDITION-DETECTED`, `ENDPOINT-CHANGE`), the ordered exit-2 checks (`UNPINNED-FIXTURE`/`CONTRACT-INVALID`, `FIXTURE-MISSING`, `PATH-MISMATCH`, `FILE-MISSING`/`MALFORMED-JSON`/`MALFORMED-MODEL`, `DIGEST-MISMATCH`, `INVALID-ARGUMENTS`, `SELF-TEST-MISMATCH`), the `--freeze`-only `SCOPE-REFUSED`, and the legacy-pin migration sentence. All quoted finding IDs match those the tool emits.

**(d) Inherited behavior unchanged.** The four pre-round pins (`r88`, `r94`, `r95`, `r96`) are payload-identical to the baseline contract excluding `revision` (per-file digests, events, relations, counts — verified programmatically); the four pre-round chain digests are byte-identical to the r97 receipts (`15ef230e…`, `2527beb9…`, `d541ae64…`, `d422a9b3…`); `git diff 9a3d648 -- corpus/tools/` touches only the two S1-owned files.

## 3. C2 — coverage (chain extended, V46 discharged): **VERIFIED**

Six-fixture chain, delivered contract, every run `RESULT PASS` exit 0:

```
FREEZE r88-m3-maya-cluster:         events 2/2; dependency-edges 0/0; relations 0/0   DIGEST 15ef230e…
FREEZE r94-paired-crossing:         events 3/3; dependency-edges 2/2; relations 1/1   DIGEST 2527beb9…
FREEZE r95-crossing-aftermath:      events 4/4; dependency-edges 3/3; relations 1/1   DIGEST d541ae64…
FREEZE r96-crossing-response:       events 5/5; dependency-edges 4/4; relations 1/1   DIGEST d422a9b3…
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1   DIGEST 3c922d20…
FREEZE r98-clerk-filing:            events 7/7; dependency-edges 6/6; relations 1/1   DIGEST 59a0f4fa…
```

Pins are path-bound and their per-file digests match the delivered bytes (independently recomputed for both new pins, all five tables each: `per-file digests match: True`). The r97 pin digest equals the digest V46 recorded in its r97 scratch mirror.

**V46's recorded FAIL discharged.** Scratch mirror with the fixture at its pinned path; the tick-13 event's `depends_on` set to `[]` (V46's exact BR-01 mutation, key kept as an empty list):

```
control (unmodified copy): FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
                           RESULT PASS   exit=0
mutated:                   FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5; relations 1/1
                           FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
                           RESULT FAIL   exit=1
```

The r98 edge is load-bearing in the same way: dropping `clerk-filing-open`'s `depends_on` gives `dependency-edges 5/6` / `FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']` / exit 1, while the unmodified fixture exits 0.

## 4. C3 — depth (fourth beat, no finding asserted): **VERIFIED**

Fixture counts on the delivered JSON: **6 entities / 1 relation / 7 events / 7 sources**; new records are `clerk-maren` (`entities.json#/5`, `first_appearance: clerk-filing-note`), `clerk-filing-note` (`sources.json#/6`), `clerk-filing-open` (tick 14, `clerk-maren`, `chalk-stair`, `depends_on: ["acknowledgment-aru-records"]`), and the excerpts' `## Round 98 clerk filing` section (folio 8, "I assert no finding / I reach no verdict and reconcile nothing"). All five JSON tables are inherited-prefix parsed-identical to r97 (`inherited-prefix-identical: True` for entities/relations/timeline/sources/contradictions); `inspiration-note.md` and `source-excerpt.md` are byte-identical to r97; `contradictions.json` stays `[]`.

Map: `**Expected inventory:** 20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors.` and exactly 20 canonical pointer rows (6 `first_appearance` + 6 claims + 1 relation + 7 events). I re-derived the inheritance claim myself: 17 inherited rows differ from r97 **only in the namespace cell** (`r97-crossing-acknowledgment:paired-clock` → `r98-clerk-filing:paired-clock`); `inherited rows identical modulo namespace: True`; new rows are `J18 entities.json#/5/first_appearance`, `J19 entities.json#/5/claims/0`, `J20 timeline.json#/6`.

Receipts (all exit 0):

```
check_bible r98    CLEAN: schema, citations, relations, timeline; 0 violations
map_obligations r98  OBLIGATIONS raw=20 mapped=20
                     INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
                     RESULT PASS
support_check r98    RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
                     SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; MODES 22/22; VALIDATED-ROWS 22/22
                     RESULT PASS
```

Census (full repo-relative sweep of every fixture directory carrying `entities.json`): **CENSUS dirs=172 clean=38 negative=134 other=0 violation_lines=421** — the declared 171→172 with the inherited tuples unchanged (171→172, 37→38, 134, 421; one directory added, zero non-0/1 exits).

**r95 carried-wording repair:** `git diff 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` is exactly `1 insertion, 1 deletion` — one prose sentence ("the new relation encodes…" → "the relation encodes…; the new tick-11 aftermath event records one reported non-arrival on one occasion"). All 25 table rows are byte-identical (`diff` of the `^|` lines: no output); r95 receipts are unchanged (`map_obligations r95` raw=15 mapped=15 PASS; `dependency_freeze r95` digest `d541ae64…` equals the r97 pin, since the map is not a pinned data file).

**S5's notes (cross-checked):** `r98-clerk-scope-note.md` hash matches its report; both correction addenda are pure appends (14 insertions each, 0 deletions). I re-derived their claims independently: `map_obligations.py` `86b52949…`, contract `2142b991…`, `check_bible.py` `ff9fd2aa…`, `support_check.py` `55a5eb27…` all current; the committed `map_obligations.py` history is exactly `cc1df4dc…` (r94), `d1c239cc…` (r95), `2b0ba815…` (r96), `86b52949…` (r97) — so `9224a684…` and `6634e176…` never entered it, as the addenda state; the quoted r95/r96 receipts reproduce (raw=15 / raw=16, support 15/15 / 16/16).

## 5. Integration surface

- **Change set = declared ownership.** `git status --porcelain --untracked-files=all` shows only: `LOG.md`, the r95 map repair, the two knowledge-note addenda, `corpus/tools/README.md`, S1's two files, untracked `corpus/fixtures/r98-clerk-filing/` (10 files), `corpus/knowledge/r98-clerk-scope-note.md`, and `.ufo/waves/round-98/`. No file outside the declared ownership changed; `map_obligations.py`, `map-obligations-contract.json`, `support_check.py`, `boundary_doc_check.py`, `check_bible.py` are byte-unchanged.
- **No commits, no strays in the lane.** `git log --oneline 9a3d648..HEAD` = `dd4df1b` (the r97 closure commit, pre-round); no seat committed. No copy of any lane path exists outside the lane (`find` over the parent tree for `r98-clerk-filing`, `dependency_freeze.py`, `r98-clerk-scope-note.md` → none). No `r94-F01`-class stray write by a lore seat.
- **Unattributed, recorded (not a producer defect):** (1) `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` (105 bytes, 20:30) — a `python3 analyze.py > baseline-analyze.txt` shell-redirect artifact in the parent tree; no lore path in its content, no seat has claimed it (S1, S2 and S3 also recorded it). (2) `v05-self-test-scratch/` (948K, 20:36) at the lane root — gitignored by `*-self-test-*/`, but it sits outside the per-seat scratch convention (`.ufo/waves/round-98/seats/<SEAT>-scratch/`) and **no V05 seat report or seat scratch dir exists in this wave**. Both are closure-sweep items, not claim failures.
- **Regression surface green:** `map_obligations --self-test` PASS (25 cases), `--frozen` r93 snapshot PASS, `boundary_doc_check` CERTIFIED, `boundary_doc_check --self-test` PASS, `discriminate_check` `DISCRIMINATION HELD` exit 0 and the `e97613c` control `REGRESSION-DETECTED` exit 2; r88/r93/r94/r95/r96/r97 map receipts unchanged. Self-test scratch is transient (both `dependency-freeze-self-test-*` dirs had already been cleaned up when I checked) and covered by `.gitignore`.

## 6. Closure worklist (unowned paths; L1 action before commit — none of these is a C1/C2/C3 defect)

1. `SKILL.md:96/98/100` — `dependency_freeze` row still reads "frozen chain … r88-m3-maya-cluster, r94-paired-crossing, r95-crossing-aftermath, r96-crossing-response", "16 cases", "the frozen chain is the declared four fixtures (`r97-crossing-acknowledgment` unpinned)", "a path-less legacy pin cannot be refreshed in place (manual contract edit)". All four clauses are superseded by the delivered revision (six fixtures; 17 cases; both new pins; migration delivered).
2. `corpus/README.md:38` — "rounds 96–97", "16-case persisted self-test", "the r97 fixture is not yet pinned" (and "r88-m3 → r94 → r95 → r96" chain wording).
3. `corpus/fixtures/README.md` — no Round-98 section and no census re-declaration; last declaration is 171/37/134/421 (measured now 172/38/134/421). Also due: the Round-98 dated pin note.
4. `corpus/knowledge/r91-c9-watch.md` — the r97 row ends "Next re-check: r98"; the r98 re-check row (`discriminate_check` held + `e97613c` control) is not yet filed.
5. `SCORECARD.md` — no Round-98 admitted section; `LOG.md` has the round-98 declaration only (no closure entry).
6. Sweep the two unattributed items in §5 (parent-tree `baseline-analyze.txt`; lane-root `v05-self-test-scratch/` with no V05 seat).

## Bottom line

**PASS** — C1 (17/17 self-test with the pinned `self_test_mismatch` case, exit 1→2 proven on baseline vs delivered bytes, path-less legacy pin migrated in place by `--freeze` with the different-path refusal retained, complete `precedence` text, all 16 inherited cases and the four inherited pins unchanged), C2 (r97+r98 pinned by the guarded `--freeze`, chain 6/6 clean with digests, V46's tick-13 mutation now `REDUCTION-DETECTED` exit 1) and C3 (6/1/7/7 counts, inherited records parsed-identical, 20/20 map obligations with 17 inherited rows identical modulo namespace, CLEAN + 20/20/22/22 receipts, census 171→172, r95 repair one prose line with 25 table rows and receipts unchanged) each verify first-hand on the frozen revision `dependency_freeze.py 03d04365…` + contract `153ebc5b…` + r98 fixture; no axis harmed, no strays, no commits; six closure-doc worklist items flagged (all on unowned paths, none a claim defect).
