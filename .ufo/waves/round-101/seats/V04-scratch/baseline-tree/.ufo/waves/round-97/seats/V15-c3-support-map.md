# V15 — c3-support-map (round 97)

**Seat:** V15 `c3-support-map` (verifier)
**Scope:** C3/depth — run `support_check.py` and `map_obligations.py` on the delivered
`corpus/fixtures/r97-crossing-acknowledgment/` (expected `17/17; 2/2; 19/19` PASS and `raw=17
mapped=17` PASS), and re-run both on the repaired `corpus/fixtures/r96-crossing-response/` to
confirm the r96 receipts are unchanged by R4's cosmetic repair (quote old vs new).
**Report path (exclusive):** `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V15-c3-support-map.md`
**Baseline:** r96 closure `f3e09f9`. All commands run from the lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.
**Scratch:** `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V15-scratch/`
(absolute lane path; no repo file outside this report and that scratch dir was written by this
seat — `git status --porcelain` shows only `M LOG.md`, the producers' paths, and untracked
`.ufo/waves/round-97/`).

## 0. Poll-wait record (R5)

Target = R5's `corpus/fixtures/r97-crossing-acknowledgment/{README.md,claim-excerpt-map.md}` plus
R5's producer report. Poller `.ufo/waves/round-97/seats/V15-scratch/poll.sh` (20 s cadence, 40
tries) logged to `V15-scratch/poll.log`:

| Time | Observation |
|---|---|
| 18:42:40 (try 1) | r97 dir absent (`files=0/2`, `report=none`) |
| 18:44:20 (try 6) | `files=2/2` — but the two files were byte-copies of r96's (`claim-excerpt-map.md` sha `e851f068…` = r96 *post-repair*; `README.md` `ff52ced4…` = r96's), i.e. R5's copy bases |
| 18:49:05 | map became `49d4834e…`; 18:49:30 README became `d9387b7d…` |
| 18:51:40 (try 28) | `READY` — `report=.ufo/waves/round-97/seats/R5-fixture-docs.md` |

Verification started only after the producer report existed (first receipt 18:51:45). The
mid-flight state seen at try 6–27 was **not** verified: at that moment the r97 map still declared
`16 JSON facts; 18 total mapped rows` with rows J01–J16 and no `J17`, and R5's report was absent;
verifying it would have produced a false FAIL against an unfinished artifact. Nothing was verified
before it existed and nothing was fabricated. Fixture bytes were re-hashed before and after every
probe and are stable (section 1).

## 1. Revisions verified

Fixture `corpus/fixtures/r97-crossing-acknowledgment/` (sha256; stable 18:45:07 → 18:52:20):

| File | sha256 | bytes |
|---|---|---:|
| `claim-excerpt-map.md` | `49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f` | 12117 |
| `README.md` | `d9387b7d73264dfc6c01d27cc6bf24c58ef6bdb4461d2ae8fbfdb6376d9e019f` | 5304 |
| `timeline.json` | `73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b` | 2173 |
| `sources.json` | `438fb513a62496c41179ead3ea2a55a69ff4ce1fd191c3a7ebccb10651a8dc73` | 2235 |
| `entities.json` | `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` | 1449 |
| `relations.json` | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` | 139 |
| `contradictions.json` | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | 3 |
| `fictional-excerpts.md` | `8ba491cb249dd57f6aee8ca216133b07c06287c0240be658ea2e68da0cf5703c` | 3410 |
| `inspiration-note.md` | `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` | 1956 |
| `source-excerpt.md` | `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` | 640 |

Both R5-declared hashes (`claim-excerpt-map.md` `49d4834e…`, `README.md` `d9387b7d…`) reproduce.
The five byte-copy tables and the two byte-copy prose files are sha-identical to r96 (matches
R4/R5).

Tool revisions bracketing the receipts (18:51:45 → 18:52:20, unchanged across that window):

- `support_check.py` `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c` — same
  revision as r96's delivery and as my 18:42 pre-repair baseline.
- `map_obligations.py` `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9` — R1's
  in-tree revision; it had moved from `2b0ba815…` (the r96 delivered revision) by 18:51.
- `map-obligations-contract.json` `2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41`
  — R2's in-tree revision; had moved from `97b76bb8…`.

## 2. Required command 1 — `support_check.py` on r97 (expected PASS)

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J02: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J03: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J04: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J05: source-support; mode=verbatim; anchor=found; 17:> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.
PASS J06: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J07: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J08: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J09: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J10: source-support; mode=verbatim; anchor=found; 18:> After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.
PASS J11: source-support; mode=verbatim; anchor=found; 19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
PASS J12: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J13: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J14: source-support; mode=verbatim; anchor=found; 20:> Their tick-10 decision depends on both ninth-bell entries: Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court. After agreeing to share stewardship for this crossing only, they chalked one temporary route mark together at the midpoint.
PASS J15: source-support; mode=verbatim; anchor=found; 26:> Tick 11: I waited at the Chalk Stair through the agreed bell.
PASS J16: source-support; mode=verbatim; anchor=found; 37:> Tick 12: I was at Salt Court through the same agreed bell.
PASS J17: source-support; mode=verbatim; anchor=found; 48:> Tick 13: I received Evin's response at the Chalk Stair.
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19
RESULT PASS
exit=0
```

**`INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15`,
`SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; MODES 19/19; VALIDATED-ROWS 19/19`, `RESULT PASS`,
exit 0** — matches the claim exactly, and the map's own declaration
(`**Expected inventory:** 17 JSON facts; 2 editorial rows; 19 total mapped rows; 15 distinct
excerpt anchors`) is satisfied. `stderr` empty. The 16 inherited `PASS` lines are byte-identical to
the r96 receipt (same anchors, same line numbers 12/13/17/18/19/20/26/37); the only new line is
`J17 … 48:> Tick 13: I received Evin's response at the Chalk Stair.`, whose anchor line 48 lies
inside J17's declared span `44-53`. Re-run at 18:52:20 with identical output.

## 3. Required command 2 — `map_obligations.py` on r97 (expected raw=17 mapped=17 PASS)

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS
exit=0
```

**`raw=17 mapped=17`, `RESULT PASS`, exit 0** — matches the expectation, with no `FINDING` line
(no `inventory_mismatch`, no `dual_pointer`, no `schema_drift` false positive on the canonical r97
map). `stderr` empty.

Independent recount from the raw tables (not via the tool):
`r96: first_appearance=5 claims=5 relations=1 timeline=5 total=16` →
`r97: first_appearance=5 claims=5 relations=1 timeline=6 total=17`; entities 5, relations 1,
contradictions 0, sources 6. New records are exactly `timeline.json#/5`
`acknowledgment-aru-records` (actor `aru`, place `chalk-stair`, `depends_on
["response-evin-salt-court"]`, tick 13, `source_id` `aru-acknowledgment-note`) and
`sources.json#/5` `aru-acknowledgment-note`; the r96 prefixes are element-identical
(`t[:5]==t96`, `s[:5]==s96`), and `entities.json` / `relations.json` / `contradictions.json` are
value-identical to r96.

`python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment` →
`CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0 (corroboration; C3's gate is
V13's seat).

Parser-level inheritance (using the tools' own parsers, `support_check.parse_map`):
`inv96 (16, 2, 18, 14)` → `inv97 (17, 2, 19, 15)`; the 16 inherited rows are **parse-value
identical** on id/kind/mode/anchor/path/span (`inh96 == inh97 → True`); the only extra row in r97
is `J17`; J17's pointer token is `timeline.json#/5`. `fictional-excerpts.md` r96 (2588 B, 42 lines)
is a strict byte-prefix of r97's (3410 B, 53 lines); the appended section is lines 43–53.

## 4. r96 post-repair re-runs — receipts UNCHANGED (old vs new)

R4's repair landed at 18:43:42 (`claim-excerpt-map.md` `5093d72e…` → `e851f068…`, +130 B). This
seat captured the r96 receipt **before** the repair landed (18:42:36) and again after, so the
"unchanged" claim is measured against real bytes on both sides, not only against r96's report.

**`support_check.py` on r96 — old vs new:**

```
--- OLD (pre-repair, map sha 5093d72e…, tools map_obligations 2b0ba815… / contract 97b76bb8…) ---
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS
exit=0
--- NEW (post-repair, map sha e851f068…, tools 86b52949… / 2142b991…) ---
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS
exit=0
```

**`map_obligations.py` on r96 — old vs new:**

```
--- OLD (pre-repair) ---          --- NEW (post-repair) ---
OBLIGATIONS raw=16 mapped=16      OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; ...   INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS                       RESULT PASS
exit=0                            exit=0
```

Machine-checked equality (`.ufo/waves/round-97/seats/V15-scratch/{r96-pre-repair.txt,
r96-post-repair.txt,r96-post-repair-currenttools.txt}`, 30 receipt lines each):

- pre-repair (old tools) vs post-repair (current tools): `IDENTICAL: True`
- post-repair (old tools) vs post-repair (current tools): `IDENTICAL: True`

So the receipts are unchanged both **across the repair** and **across the tool revision churn**
(`map_obligations.py` `2b0ba815…` → `86b52949…`, contract `97b76bb8…` → `2142b991…`), i.e. the
"unchanged" result is not an artefact of one tool revision. This also agrees with r96's recorded
receipt (V10, map sha `5093d72e…`): `INVENTORY … 16/16; 2/2; 18/18; 14/14` + `raw=16 mapped=16`,
both PASS.

### 4a. The repair is cosmetic — diff and data-row check

`diff -u` of the pre-repair snapshot (`V15-scratch/r96-map-prerepair.md`, byte-identical to
`git show f3e09f9:corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` = `5093d72e…`) vs the
repaired file = **exactly two hunks**:

1. line 44, editorial-table delimiter `|---|---|---|---|---|---:|---|---|` (8 cells) →
   `|---|---|---|---|---:|---|---|` (7 cells), now matching its 7-cell header and 7-cell data rows
   (verified by cell count: L43 header 7, L44 delimiter 7, L45/L46 data 7);
2. line 50, the stale sentence `The new relation encodes only the agreement for this crossing, not
   perpetual performance or alliance.` → `The new tick-12 event encodes only Evin's second account
   of the same crossing occasion; it asserts no reconciliation, selects no winner between the
   accounts, and adds no duty beyond this crossing, not perpetual performance or alliance.`

All 23 non-delimiter table rows are **byte-identical** before/after (`data rows pre 23 post 23
identical: True`), as are the other nine files of the fixture (`git diff --name-only --
corpus/fixtures/r96-crossing-response/` lists only `claim-excerpt-map.md`; `git diff --stat` = `1
file changed, 2 insertions(+), 2 deletions(-)`). The repaired map's JSON-facts table delimiter
(L21, 8 cells) and its header/data rows (8 cells) are consistent and were not touched.

Note (context, not a finding): `support_check.py` skips delimiter rows (`support_check.py:107-109`)
*before* its cell-count check (`:110`), so an 8-cell delimiter under a 7-cell header never reached
the receipts — the repair's receipt-neutrality is therefore expected, but it was still measured
rather than assumed, and the receipts are byte-identical.

## 5. Limitations / not verified here

- The receipts are lexical/map-declared preflight (row inventory, fixed-string anchors, spans, R9
  modes, pointer↔row binding). Whole-claim entailment, the acknowledgment bound ("dispute
  preserved unresolved"), and canon truth are manual/adversarial reviews — other seats' scope
  (e.g. V13 checker, V14 inherited equality, V19 repair scope).
- My receipts are bracketed to `support_check.py` `55a5eb27…`, `map_obligations.py` `86b52949…`,
  contract `2142b991…` at 18:52:20. R1/R2 were still writing during the round (R5 flags the same);
  if either revision moves again, sections 2–4 must be re-run at closure. The r96 half of the
  result is already revision-robust (identical under both revisions observed).
- `corpus/fixtures/README.md`'s census text (170) vs the on-disk 171 dirs is R4/R5's noted,
  read-only item; not assessed here.
- R3's `dependency_freeze.py` re-freeze of the r96 fixture is outside this seat and was not run.

## Bottom line

**PASS** — `corpus/fixtures/r97-crossing-acknowledgment` verifies as claimed: `support_check`
`INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15` +
`SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; MODES 19/19; VALIDATED-ROWS 19/19` `RESULT PASS`
exit 0, and `map_obligations` `raw=17 mapped=17` + `RESULT PASS` exit 0, with J17
`timeline.json#/5` anchored at line 48 inside its span 44-53, 16 inherited rows parse-value
identical, and `check_bible` CLEAN exit 0; R4's r96 repair is cosmetic (two hunks: 8→7-cell
delimiter, tick-12-event rewording; 23/23 data rows byte-identical) and the r96 `support_check` +
`map_obligations` receipts are byte-identical before vs after the repair and across the tool
revision churn (`2b0ba815…`→`86b52949…`).
