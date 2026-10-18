# S5 — knowledge-notes (round 98)

Seat: S5 knowledge-notes. Exclusive write scope per seat spec:
`corpus/knowledge/r98-clerk-scope-note.md` (delivered, 72 lines, sha256
`1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8`) plus dated correction
addenda appended to `corpus/knowledge/r95-aftermath-scope-note.md` and
`corpus/knowledge/r96-response-scope-note.md` (delivered, 14 insertions each, 0 deletions).
No other writes; no commits; no pushes; no network. Scratch: none outside this report (all
checks were inline `python3`/shell in the lane tree, read-only).

Baseline: r97 closure `9a3d648` (HEAD at seat time `dd4df1b`). All commands from the lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin`; every write used an absolute path under the lane
and was re-verified by `git status` (see Hygiene).

## Poll-wait record (artifact-based, never verified a plan)

- Seat start ~`20:27-03:00`: `corpus/fixtures/r98-clerk-filing/` did not exist; `.ufo/waves/round-98/seats/`
  held only verifier scratch dirs.
- Poll 1 (20 s × 40, background): `FOUND at try 3 2026-10-17T20:28:31-03:00` — directory existed with
  10 entries. **Intermediate state observed honestly:** at 20:28 all 10 files were r97 byte-copies
  (`cmp` IDENTICAL for entities/sources/timeline/fictional-excerpts/README/map), i.e. S3's copy step
  had landed but not its authored content; no receipt was run against that state.
- Poll 2 (content-aware: `clerk-maren` in entities, `clerk-filing-open` in timeline,
  `clerk-filing-note` in sources, `Tick 14` in excerpts, `Round 98` in README, `clerk-filing` in map):
  `CONTENT-READY at try 7 2026-10-17T20:30:52-03:00` — S3's four content files landed ~20:29-20:30,
  S4's `README.md` + `claim-excerpt-map.md` landed at 20:30.
- Producer reports were not used as a gate: S3/S4 reports were absent at content-ready time and
  appeared later (present at final check). ENDGAME CONVENTION honoured trivially — no poll waited on
  reports at all, and no poll waited on SELF.
- No stall escape was needed; total wait ~4 minutes.

## What the note records

`corpus/knowledge/r98-clerk-scope-note.md` opens with `source:` / `verified-at:` / `recheck:` /
`citation-convention:` metadata, then:

1. **The class — institutional filing record asserting no finding** (named as the **fourth beat** of
   the crossing arc: r95 Aru's reported non-performance → r96 Evin's second account → r97 Aru's
   acknowledgment → r98 the harbor clerk's filing). A named office-holder's own first-person record
   that he filed both pending accounts and recorded the matter OPEN, asserting no finding, reaching
   no verdict, reconciling nothing. Distinguished from the r97 acknowledgment class (participant
   receipt vs non-participant institutional act) and from the r35 ledger-pair class (no contradiction
   asserted; `contradictions.json` stays `[]`).
2. **Supporting records (exact)** — `clerk-filing-note` (`sources.json#/6`, id at `:39`, reliability
   note `:42`); note text `fictional-excerpts.md:55-64` (quoted `:59-62`); new entity `clerk-maren`
   (`entities.json#/5`, id at `:63`, `first_appearance` `:66`, claim `:69-70`); event `clerk-filing-open`
   (`timeline.json#/6`, id at `:66`; tick 14, `entity_id: clerk-maren`, `place_id: chalk-stair`,
   `depends_on: ["acknowledgment-aru-records"]`, description `:73`); inherited tick-13 row
   `timeline.json#/5` parsed-equal to r97; inherited crossing-only relation `relations.json#/0`
   byte-identical to r97; map rows J18/J19/J20 at `claim-excerpt-map.md:39/40/41` with bounded
   readings at `:62/:64/:66`.
3. **Bounds** — clerk's filing only; no finding / no resolution truth; no winner and no new duty;
   first-appearance bound (office wording is the note's own attributed self-description, not identity
   proof); editorial tick/ID alignments (tick 14, event ID, `depends_on` edge, single actor slot);
   checker validates structure, not testimony; no contradiction created (tick-14 does not revise
   tick-11..13).
4. **Precedent cross-reference** — `r97-acknowledgment-scope-note.md` (immediate predecessor);
   **r10 registry-witness** (`corpus/fixtures/r10-registry-witness/`, registrar-copy excerpt, `registry-entry`
   at `timeline.json#/2`, `records_departure` at `relations.json#/1`; limits documented at
   `corpus/fixtures/README.md:209-210` and `2026-10-12-lore-decision-table.md:112` — "does **not**
   assert a different destination or settle whether Sella's report is true", "authored second
   perspective, not external corroboration or canon resolution"); r95/r96 notes; r23 report-not-proof
   row (`2026-10-12-lore-decision-table.md:226-230`).
5. **Receipts, same-round adjacent change, path/line checks, limits** — below.

## The two correction addenda (historical text unrewritten)

Append-only sections dated `2026-10-17, round 98, S5 knowledge-notes seat`; `git diff` shows
14 insertions / 0 deletions per file.

**r95 note** — records that the receipts paragraph's pin `map_obligations.py` `9224a684…` is stale:
it was an in-flight intermediate during round 95 and never entered committed history (committed
revisions: `cc1df4dc…` r94 `abbc3e0`, `d1c239cc…` r95 `dcb2d92`, `2b0ba815…` r96 `f3e09f9`,
`86b52949…` r97 `9d25df9`). Current delivered at addendum run time `2026-10-17T20:28:35-03:00`:
`map_obligations.py` `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9`, contract
`map-obligations-contract.json` `2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41`.
Instructs re-derivation on next touch.

**r96 note** — records both stale pins: `map_obligations.py` `6634e176…` (in-flight during r96, never
committed; r96 closure delivered `2b0ba815…`) and the contract `8173bb97…` (which is
`corpus/tools/map-obligations-contract.json` at its **r95** revision, commit `dcb2d92`; r96 closure
delivered `97b76bb8…`). Also notes `d1c239cc…` is the r95 revision — historical, not current. Current
delivered hashes as above. Instructs re-derivation on next touch.

Both addenda state that round 98's C1 work owns `dependency_freeze.py` /
`dependency-freeze-contract.json`, not the map-obligations tool or its contract.

## Receipts (measured this pass, from the lane root)

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
# CLEAN: schema, citations, relations, timeline; 0 violations   exit 0
python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
# INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
# ANCHORS repeated-references=4; DUPLICATE-ROWS 0
# RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
# SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; MODES 22/22; VALIDATED-ROWS 22/22
# RESULT PASS   exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
# OBLIGATIONS raw=20 mapped=20 / INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22 / RESULT PASS   exit 0
```

Tool revisions at the 20:31-03:00 receipt run: `check_bible.py` `ff9fd2aa…`, `support_check.py`
`55a5eb27…`, `map_obligations.py` `86b52949…` (contract `2142b991…`). Re-run at 20:32:51-03:00 after
S1's C1 files landed (`dependency_freeze.py` `03d04365…`, `dependency-freeze-contract.json`
`c435239d…`): the four checker hashes above were unchanged and the r98 battery re-passed identically.
Predecessor fixtures re-derived at the same revisions this pass, all `RESULT PASS` exit 0:
r95 `raw=15 mapped=15` (re-run **after** S3's r95 map repair), r96 `raw=16 mapped=16`,
r97 `raw=17 mapped=17`.

## Verification and hygiene checks

- **Cited-line verification (python3, this pass):** 38 cited `path:line` targets in the new note were
  checked programmatically (line content contains the expected substring) — all resolve; the one
  reported "mismatch" was an artifact of my checker splitting the phrase "does **not** assert a
  different destination" across `corpus/fixtures/README.md:209-210`, which the note cites as a range.
  All other cited paths (`corpus/knowledge/r97-acknowledgment-scope-note.md`,
  `corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md`,
  `corpus/fixtures/r35-bell7-conflict/contradictions.json`, …) exist.
- **Inheritance (python3):** `r98 entities.json[:5] == r97 entities.json`,
  `r98 sources.json[:6] == r97 sources.json`, `r98 timeline.json[:6] == r97 timeline.json` → `True`;
  `contradictions.json`/`inspiration-note.md`/`relations.json`/`source-excerpt.md` byte-identical to
  r97 (`cmp`); map rows J01-J17 identical modulo the namespace column (0 other diffs), J18-J20 the
  only new rows.
- **Census:** `ls -d corpus/fixtures/*/ | wc -l` = **172** (171 at r97 closure) — matches C3.
- **Stray-write guard (r94-F01 class):** all writes were absolute under
  `/home/vgpnk/Projects/shokunin/lore-shokunin/`; `find /home/vgpnk/Projects/shokunin -maxdepth 3 -name
  "r98-clerk-scope-note.md" -not -path "*/lore-shokunin/*"` → empty; final `git status --porcelain`
  shows my three files exactly (`M` r95 note, `M` r96 note, `?? corpus/knowledge/r98-clerk-scope-note.md`)
  plus S1/S3/S4 artifacts and `LOG.md`.
- **r95 repair cross-check:** `git diff` on `r95-crossing-aftermath/claim-excerpt-map.md` = 1 insertion
  / 1 deletion at line 49 only; r95 receipts unchanged by it (re-run).

## Not my axis / limits

- This is an author-seat knowledge note and addenda, not independent verification, admission, or a
  non-author review; it does not authenticate fictional sources or adjudicate any character.
- C1 (self-test 17, path-less pin migration, precedence text) and C2 (six-fixture chain, V46
  discharge) are other seats' claims; I verified only that the checker revisions I cite are current
  and that the r95/r96/r97/r98 fixtures pass at them. I did not run the freeze tool.
- S1's C1 files landed at 20:32 (`dependency_freeze.py` `03d04365…`, contract `c435239d…`) and S2's
  `corpus/tools/README.md` landed by my final check (20:33:49); neither affects the checker revisions
  cited above, and the r98 battery was re-run green at the final state (fixture mtimes ≤ 20:30:41).

## Bottom line

**PASS** — `corpus/knowledge/r98-clerk-scope-note.md` names the institutional-filing class (fourth
beat) with exact records, bounds, and the r97/r10 cross-references, and the r95/r96 notes carry
append-only dated addenda correcting their stale tool pins to the measured current hashes; r98
receipts 20/20 facts / 22/22 rows / 20 mapped obligations, `check_bible` CLEAN, all exit 0.
