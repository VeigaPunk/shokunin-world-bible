# V12 — c2-support-map (round 99)

**Seat:** V12 `c2-support-map` (verifier)
**Scope:** Poll for S4, then run `support_check.py` and `map_obligations.py` on the delivered `corpus/fixtures/r99-window-lapse/` and quote the observed receipts. Expected `map_obligations` `raw=21 mapped=21` PASS.
**Report path (exclusive):** `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V12-c2-support-map.md`
**Baseline:** r98 closure `4265df5`. All commands ran from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.
**Scratch:** `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V12-scratch/` (`poll.sh`, `poll.log`, captured stdout/stderr/exit, hash listings).
**Writes:** this report and that scratch directory only. No commits, no pushes, no network, no nested agents.

**STATUS: COMPLETE — both receipts observed on the delivered bytes. `support_check` RESULT PASS exit 0 (section 2); `map_obligations` raw=21 mapped=21 RESULT PASS exit 0 (section 3). Matches the expected obligation count.**

## 0. Poll-wait record

Target = S4's `corpus/fixtures/r99-window-lapse/{README.md,claim-excerpt-map.md}` moved off the r98 byte-copies, plus an `S4*.md` producer report file (not a scratch directory). Poller `V12-scratch/poll.sh`, 20 s cadence, 40-try cap. Log: `V12-scratch/poll.log`. r98 comparison hashes at poll start: map `c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba`, README `32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926`.

| Time | Observation |
|---|---|
| 22:01:11 (try 1) | fixture present; both S4 files `same-as-r98`; no `S4*.md` report |
| 22:01:31–22:02:51 (tries 2–6) | still `same-as-r98`, reports=none |
| 22:03:11 (try 7) | `map=moved readme=moved`, reports still none |
| 22:03:31–22:03:51 (tries 8–9) | files moved, reports still none |
| **22:04:11 (try 10)** | **READY** — `reports=S4-fixture-docs.md` |

Verification did not start on tries 1–6. Those bytes were the r98 placeholder copies (README 5,829 B, map 15,028 B). Running the tools then would have scored an unfinished artifact. No stall-escape. No ABSENT. Tries used: 10 of 40.

S3's report `S3-fixture-author.md` (5,069 B, mtime 22:01:40) was already present when verification started. It was not this seat's poll gate. By 22:04 the JSON tables that the tools read had also moved off r98 for `sources.json`, `timeline.json`, and `fictional-excerpts.md` (section 1). `entities.json`, `relations.json`, and `contradictions.json` remained byte-identical to r98, which is the preserving-copy shape, not a missing S3 write.

S4 report at verification: `S4-fixture-docs.md`, 9,303 B, mtime 22:03:54, sha256 `61bfdec1f5b7bbcdda653230bb4be1b6c1913683af67e2ae02e4ee46a327f72f`. S4's section C summarizes the same two gates but abbreviates the PASS lines (`PASS J01 … PASS J20`). The quotes below are this seat's full stdout, not a copy of that summary.

## 1. Revisions verified

Fixture sha256, stable across the 22:08:05 run and the 22:11:47 rerun (byte-identical hash listings; sizes from `stat`):

| File | sha256 | bytes | vs r98 |
|---|---|---:|---|
| `claim-excerpt-map.md` | `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d` | 17119 | moved (S4) |
| `README.md` | `b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049` | 6176 | moved (S4) |
| `fictional-excerpts.md` | `fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d` | 5114 | moved |
| `sources.json` | `8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15` | 3293 | moved |
| `timeline.json` | `2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069` | 2998 | moved |
| `entities.json` | `db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984` | 1793 | identical |
| `relations.json` | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` | 139 | identical |
| `contradictions.json` | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | 3 | identical |
| `inspiration-note.md` | `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` | 1956 | identical |
| `source-excerpt.md` | `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` | 640 | identical |

S4's claimed hashes for the two owned files match these measured hashes.

Tool revisions bracketing both receipts (unchanged before/after; same bytes recorded for these two tools at r98):

- `support_check.py` `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c` (17,006 B)
- `map_obligations.py` `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9` (38,693 B)
- `map-obligations-contract.json` `2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41`

Map declaration line (file line 5), which both receipts satisfy:

`**Expected inventory:** 21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors.`

Independent raw recount on the same JSON bytes (not a substitute for the tool): `entities=6 first_appearance=6 claims=6 relations=1 timeline=8 sources=8 contradictions=0`, so `raw_obligations=21`. Last timeline record: `id=clerk-lapse-recorded`, `tick=15`, `entity_id=clerk-maren`, `place_id=chalk-stair`, `depends_on=['clerk-filing-open']`, `source_id=clerk-lapse-note`. Source ids end with `clerk-lapse-note` (8 sources).

## 2. `support_check.py` — full quote

Run at 22:08:05. Rerun at 22:11:47: stdout byte-identical (`cmp`), exit 0 again, stderr still empty.

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
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
PASS J18: source-support; mode=verbatim; anchor=found; 60:> I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN.
PASS J19: source-support; mode=verbatim; anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
PASS J20: source-support; mode=verbatim; anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
exit=0
```

28 stdout lines. `stderr` empty (0 bytes). No `FINDING`, no `WARN`, no `FAIL` line. `RESULT PASS` once. J21's in-span hit is excerpt line 70, inside the map row's declared span 66-76 (`claim-excerpt-map.md` line 42, pointer `timeline.json#/7`).

## 3. `map_obligations.py` — full quote

Same window. Rerun stdout byte-identical, exit 0, stderr empty.

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
exit=0
```

3 stdout lines. `stderr` empty. No `FINDING` line. `RESULT PASS` once. Observed `raw=21 mapped=21` matches the expected count. The independent recount in section 1 is the same 21 (6 first appearances + 6 claims + 1 relation + 8 events).

## 4. Bound

These two receipts are a lexical source-support preflight and a one-to-one pointer comparison. They do not certify entailment, delivery-mode review beyond the declared mode, chronology truth, or the no-resolution/no-blame prose. That prose is in the map (J21 paragraph, file line 69) and was not re-judged here. Census, `check_bible`, and freeze pinning were not this seat's commands.

## Bottom line

PASS — on the delivered `corpus/fixtures/r99-window-lapse/` bytes (map `d2fe20e5…`, verified only after S4's files had moved off the r98 copies and `S4-fixture-docs.md` existed), `support_check` printed `RESULT PASS` exit 0 with `SOURCE-SUPPORT 21/21` and an in-span J21 hit at excerpt line 70, and `map_obligations` printed `OBLIGATIONS raw=21 mapped=21` / `RESULT PASS` exit 0; both reruns were byte-identical and both stderrs were empty.
