# JDEP1 — Depth judge #1

Seat: JDEP1. Wave: round-87 follow-up (world-bible lane). Fleet root `/home/vgpnk/Projects/shokunin`, repo `lore-shokunin/`.
Mission: judge depth; re-run every row of the C2 decision table against the delivered tree; verify the table covers every provenance-block branch class from `.ufo/waves/round-87/S1.md`'s map; list uncovered classes.
Measured tree: HEAD `2b48ca7` (`2b48ca72033dfd1060b6f81c4cf27ad83deae57f`), clean at start. The checker is unchanged from that commit; the C2 table and I1's probes landed as untracked follow-up files while this audit ran.

Artifacts: this file, `JDEP1-replay.json` (D2-draft row replay), `JDEP1-table-verify.json` (landed-table verification).

---

## Wait-check receipt for I1's landing (as instructed: twice, 60s spacing)

- **Check #1:** `ls -la corpus/knowledge/r87-provenance-chain-decision-table.md` → `No such file or directory`; `ls -d corpus/fixtures/r87-probe-*` → none; `.ufo/waves/round-87/followup/` did not exist. I created the followup dir.
- **Check #2** (60s later): same command → still `No such file or directory`; `r87-probe-*` still absent.
- **Consequence:** absent after both checks, so per my block I audited **D2's patch file against S1 directly** and flagged the gap (Part C below).
- **Late landing:** at `01:43-01:45`, *after* both checks and mid-audit, I1 landed `corpus/fixtures/r87-probe-entry-shape/`, `corpus/fixtures/r87-probe-record-and-chain/`, and then `corpus/knowledge/r87-provenance-chain-decision-table.md`. All three are untracked. The table therefore exists on the working tree and is audited in full in Parts A and B; the D2-draft audit in Part C is retained as the instructed fallback record.

---

## Part A — Every row's receipt re-run against the delivered tree

The landed table pins itself to `2b48ca7` and claims a checker SHA-256. Both claims verify:

```sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin
sha256sum corpus/fixtures/check_bible.py
# 3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237  corpus/fixtures/check_bible.py
git diff --stat -- corpus/fixtures/check_bible.py   # no output — unchanged from HEAD
```

The claimed hash `3ae4134d…b237` equals the observed hash. Table SHA-256: `6455dc14e74e7aab0588f14607dfcc4916d9b8ac39432d565c938625f02074c3`.

**Receipt replay.** The table's "Receipts" section pastes 14 full command outputs. Script `/tmp/JDEP1-receipts.py` extracts each `$ python3 …` block and its `exit=` line, re-runs it, and diffs recorded vs observed:

```sh
python3 /tmp/JDEP1-receipts.py
# RECEIPTS_PARSED=14  FULL_MATCH=14  MISMATCH=0
```

All 14 receipts reproduce **byte-exact with matching exit codes**:

| Fixture | exit | lines |
|---|---|---|
| `consistent` | 0 | 1 |
| `item-chain-valid` | 0 | 1 |
| `r87-chain-unique-valid` | 0 | 1 |
| `item-chain-broken` | 1 | 2 |
| `r87-chain-unique-broken` | 1 | 2 |
| `r7-item-ambiguous` | 1 | 8 |
| `r87-masked-break-to-ambiguous` | 1 | 7 |
| `r87-masked-break-from-ambiguous` | 1 | 7 |
| `r87-probe-entry-shape` | 1 | 3 |
| `r87-probe-record-and-chain` | 1 | 36 |
| `r85-unique-break-control` | 1 | 2 |
| `r85-masked-ambiguous` | 1 | 6 |
| `r61-independent-empty` | 1 | 18 |
| `r61-independent-unavailable` | 1 | 7 |

**Row-cell signatures.** Script `/tmp/JDEP1-signatures.py` extracts every finding-like backticked signature from all 30 row cells and checks it appears in the actual output of the fixture(s) that row cites:

```sh
python3 /tmp/JDEP1-signatures.py
# ROW_LINES=30  FIXTURES_RESOLVED=14
# SIGNATURES_NOT_FOUND_IN_ANY_CITED_FIXTURE_OUTPUT=0
```

**Zero fabricated signatures.** Every `entities[…]`/`sources[…]`/`CLEAN`/`N violation(s)` string quoted in the 30 rows is present in a cited fixture's real output.

**Code anchors.** All 37 distinct `check_bible.py:<line>` anchors were resolved against the delivered source and each points at exactly the claimed logic — entry gate `:171-173`, kind gate `:176-177`, non-array `:178-180`, eligibility `:183`, record-object `:196-197`, key set `:201-203`, tick `:214-216`, holder shapes `:217-222`, dangling `:223-225`/`:234-236`, ambiguous `:226-230`/`:237-241`, notice `:242-245`, C1 origin disclosure `:246-250`, C1 post-stop disclosure `:189-195`, source shape `:251-253`, source status `:254-259`, latch `:260-263`, comparison `:264-273`. The single external reference, `corpus/fixtures/README.md:110-128`, is accurate and on point (it states source status is membership, not support).

**Result: the landed table is fully reproducible on the delivered tree.** Unlike D2's draft, every row is re-pointed at a durable in-tree fixture — no `/tmp`-only dependency survives.

---

## Part B — Coverage against S1's branch map

S1's "Branch map" (`S1.md:10-25`) plus the adjacent section (`S1.md:27-30`) enumerate the provenance block's classes. Mapping each to the landed table:

| # | S1 class (`S1.md`) | Landed row | Covered |
|---|---|---|---|
| 1 | absent `provenance` property, silent `continue` (10) | 1 (`consistent`) | yes |
| 2 | wrong entity kind, `only valid on item entities` (11) | 3 (`r61-independent-empty`) | yes |
| 3 | non-array provenance (12) | 4 (`r87-probe-entry-shape`) | yes |
| 4 | initial gate: eligible item + unavailable sources (13) | 6 (`r61-independent-unavailable`) | yes |
| 5 | initial gate: duplicate own item ID (13) | 5 (`r87-probe-entry-shape`) | yes |
| 6 | non-object record (14) | 7 (`r87-probe-record-and-chain` r0) | yes |
| 7 | object with wrong key set (15) | 8 (r1 missing, r10 extra) | yes |
| 8 | tick validation, bool + negative (16) | 9 (r2, r3) | yes |
| 9 | holder field shape, `from_holder` + `to_holder` (17) | 10, 11 (r4, r5) | yes |
| 10 | holder identity: dangling, both directions (18) | 12 (r6, r7) | yes |
| 11 | holder identity: ambiguous `to_holder` alone (18) | 13 (`r87-masked-break-to-ambiguous`) | yes |
| 12 | holder identity: ambiguous `from_holder` alone (18) | 13 (`r87-masked-break-from-ambiguous`) | yes |
| 13 | ambiguous-holder disclosure + latch (19) | 14, 15 | yes |
| 14 | source field shape, blank/non-string (20) | 16 (r8) | yes |
| 15 | source status `unknown` (20) | 17 (r9, rope r7) | yes |
| 16 | source status `unavailable`, per-record (20) | 6 (implicit) | yes |
| 17 | source status `ambiguous` (20) | 18 (anvil r1, r2) | yes |
| 18 | ambiguous-source prefix on a chain finding (20,24) | 19 (anvil r2) | yes |
| 19 | any invalid record → reset + latch (21) | 26 (rope r7→r8) | yes |
| 20 | comparison gate skipped after a stop (22) | 27, 28 | yes |
| 21 | first eligible record, non-null `from_holder` (23) | 20 (rope r0) | yes |
| 22 | later records: equal / decreasing tick (24) | 21, 22 (rope r1, r3) | yes |
| 23 | later records: holder discontinuity (24) | 23 (rope r4) | yes |
| 24 | later records: both comparisons fail (24) | 24 (rope r6) | yes |
| 25 | comparison finding does not latch (24) | 25 (rope r4 then r5) | yes |
| 26 | successful record state update (25) | 30 (positive control) | yes |
| 27 | **adjacent `allied_with` / shared `source_status()` boundary** (27-30) | — | **no** |

**Explicitly uncovered class:**

1. **Adjacent `allied_with` interaction** (S1 `27-30`). S1 gives it a dedicated section: the alliance pass shares `source_status()` (`check_bible.py:97-101`) and does not read or mutate provenance state (`check_bible.py:275-293`), and "no active fixture combines an item chain/holder with an alliance edge". The landed table has no row and no boundary statement for it. This is a genuine class in S1's map, so I list it as uncovered. Severity **low**, with the caveat that the table is titled *Provenance-chain* decision table and the alliance pass is explicitly non-interacting — a single boundary row ("the alliance pass neither reads nor mutates provenance state; shared `source_status()` semantics") would close it.

**One class outside S1's map that the table also omits** (reported because C1 introduced it after S1 was written):

2. **Malformed record after the ambiguity stop.** C1 emits the disclosure at `check_bible.py:189-195` *before* the `isinstance(record, dict)` gate at `:196`. A non-object record after the stop therefore yields **both** the disclosure and `expected object`. Verified on the delivered checker with a scratch probe built from the landed `r87-masked-break` shape (`/tmp/JDEP1-scratch/post-stop-nonobject`):
   ```text
   VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'vault', from_holder 'vault' first occurred at entities[3].provenance[1]
   VIOLATION: entities[3].provenance[2]: expected object
   7 violation(s); no canon changed
   ```
   Row 28 covers "record-local checks continue after the stop" for a *well-formed* record; the malformed-after-stop interaction is not isolated. Low severity.

Everything S1 flags as "no active fixture" (`S1.md:55`) is now covered by the landed table, including both single-direction ambiguous-holder cases, which the landed table closes via the two `r87-masked-break-{to,from}-ambiguous` fixtures.

---

## Part C — D2-draft audit (instructed fallback; superseded by the landing)

Because I1's landing was absent after both wait-checks, I audited `patches/D2-decision-table.md` against S1 directly. That draft is pinned to the **pre-C1 snapshot `28706dc`**; replaying its 30 rows against the delivered checker (`/tmp/JDEP1-replay.py`, using the original probes surviving at `/tmp/r87-D2-28706dc`) gave `MATCH=26 MISMATCH=4`, the 4 mismatches being exactly the ambiguous-holder rows C1 supersedes (`holder-ambiguous-both` 4→6, `earlier-invalid-then-ambiguous` 4→5, `two-ambiguous-records` 5→7, `r85-masked-ambiguous` 3→5). It also had a blocking defect: 26 of its 30 rows pointed at `/tmp`-only `r87-d2-*` fixtures absent from the repo. Full receipts in `JDEP1-replay.json`. **The landed table fixes all of this** — it is re-pinned to `2b48ca7`, every row is re-pointed at a durable fixture, and all ambiguous-holder rows are refreshed to the C1 after-state (rows 14-15, and the `r87-masked-break-*` receipts).

---

## Axis verdicts (per-axis, on the delivered tree at `2b48ca7`, no scalars)

- **Provenance decision table present and reproducible in `corpus/knowledge/`** — **improved**. The file landed (untracked) and is fully reproducible: SHA claim exact, 14/14 receipts byte-exact with matching exits, 0 fabricated row signatures, 37/37 code anchors correct. Baseline: no such file existed at the start of the round. **Named caveat:** the file is *untracked* — not yet committed — so a claim that it "ships in this tree" (its own line 22) is only true of the working tree, not of `HEAD`.
- **Branch-class coverage of the provenance block** — **improved, with one named gap**. 26 of 27 mapped classes covered, including the single-direction ambiguous-holder cases D2's draft missed. Uncovered: the adjacent `allied_with` boundary class (low severity, arguably out of scope). Plus one C1-introduced interaction (malformed record after the stop) not isolated.
- **Reproducible probe fixtures for the provenance classes** — **improved**. `r87-probe-entry-shape` and `r87-probe-record-and-chain` replay exactly as documented (2 and 35 findings). Debt: they do not exercise the wrong-kind or unavailable-sources gates (covered elsewhere in the repo by `r61-independent-*`), and the `r87-probe-record-and-chain` README now correctly points at the landed table file.
- **C1 per-record disclosure behaviour, replayed** — **improved**. `r85-masked-ambiguous` and the two `r87-masked-break-*` fixtures disclose at every record at/after the stop, with correctly formatted single-direction and joint cause strings.
- **No axis harmed** by this delivery on the evidence gathered.

**Verdict recommendation for depth: improved, landable.** The landed table is the first artifact this round that is genuinely re-runnable end-to-end from the repo: every row cites a shipped fixture, every receipt reproduces byte-exact, and coverage spans all but one adjacent S1 class. The depth work is real and verified. Two follow-ups, neither blocking: (a) **commit the file** — it is currently untracked, so nothing has actually landed at `HEAD`; (b) add one boundary row for the adjacent `allied_with` class and, optionally, one for the malformed-record-after-stop interaction.

---

## Handoff

- Outputs: this file plus `JDEP1-replay.json` and `JDEP1-table-verify.json`, all under `.ufo/waves/round-87/followup/`. **No tracked file written, nothing committed, no push, no registry write.** My seat block authorized no named tracked file and none was needed.
- For the parent: the C2 decision table **does exist** on the working tree at `corpus/knowledge/r87-provenance-chain-decision-table.md` and passed a full depth audit — SHA exact, 14/14 receipts byte-exact, 0 fabricated signatures, 37/37 anchors correct, 26/27 S1 classes covered. **It is untracked**, so it has not landed at `HEAD 2b48ca7`; a round-record claim that the table ships requires committing it.
- Uncovered class to record: the adjacent `allied_with` / shared-`source_status()` boundary (S1 `27-30`). Extra finding outside S1's map: malformed-record-after-stop emits both the C1 disclosure and `expected object` (`check_bible.py:189-195` runs before the `:196` object gate).
