# V12 c3-anchors — round 98

Seat: V12 (verifier, C3 depth). Baseline: r97 closure `9a3d648` (pre-round bytes
via `git show 9a3d648:<path>`). All commands ran from the lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested
agents, no commits, no pushes, no network. Writes: this report and
`.ufo/waves/round-98/seats/V12-scratch/check_anchors.py` (my own implementation).

Target (S4 byte-ownership): `corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md`
(+ `README.md` read as context). Seat claim under test: all 20 anchors in-span by my
own implementation; inherited line numbers preserved; the three new anchors only in
the filing-note section.

Frozen revision verified (stable across ~8 min of re-checks):

```
$ md5sum corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md corpus/fixtures/r98-clerk-filing/fictional-excerpts.md
263403647097bcd6da3cdd524b7c4c73  corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md
c3c0b0005732ff0f1bc5d2387f8075fb  corpus/fixtures/r98-clerk-filing/fictional-excerpts.md
$ sha256sum corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md corpus/fixtures/r98-clerk-filing/README.md
c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba  …claim-excerpt-map.md
32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926  …README.md
```

Both sha256 values match S4's report (sections "Owned and delivered" and D), so the
bytes I verified are S4's declared delivery.

## A. Poll-wait record

- 20:27: `corpus/fixtures/r98-clerk-filing/` absent; `.ufo/waves/round-98/seats/`
  empty. Existence polls every 20 s.
- 20:28:24: directory appeared with 10 files — **r97 placeholder phase**. Detected
  by content, not existence: `cmp` showed `claim-excerpt-map.md` byte-identical to
  r97's map ("MAP == r97 COPY") and `README.md` line 1 still
  `# Round 97 crossing-acknowledgment continuation`. An existence-only poll is
  satisfied by this placeholder; the r96/r97-class hazard is live and I record it.
- 20:28:55: S3's data edits landed (excerpt grew 3410→4187 bytes, 53→64 lines;
  `entities.json` 6 records, `timeline.json` 7, `sources.json` 7).
- 20:30:21: S4's map rewrite landed (12117→15028 bytes).
- 20:30:41 (S4 report): S4's README rewrite landed; observed at my next poll.
- 20:33: `S4-fixture-docs.md` appeared (poll try 4 of that loop, 20 s cadence).
  `S3-fixture-author.md` also present. No ABSENT condition; no stall-escape needed.

## B. Method — own implementation

`.ufo/waves/round-98/seats/V12-scratch/check_anchors.py` (written by me; does not
import `corpus/tools/support_check.py`). It parses the map tables, resolves every
`file.json#/pointer` against the actual fixture JSON, checks each row's exact anchor
as a fixed substring of its declared line span, compares J01–J17 against the r97
baseline map from `9a3d648`, and checks the new rows against the appended section
boundary derived from the r97 excerpt length.

Final run on the frozen revision:

```
$ python3 .ufo/waves/round-98/seats/V12-scratch/check_anchors.py
parsed rows: 20 JSON facts, 2 editorial
declared inventory: (20, 2, 22, 18)
INVENTORY OK: (20, 2, 22, 18)
inherited-matched rows: 17; new rows: ['J18', 'J19', 'J20']
PRESERVED PREFIX OK: lines 1-53 byte-identical to r97
filing section starts at line 54; new headings: [(55, '## Round 98 clerk filing (2026-10-17)')]

ALL CHECKS PASS
MY_EXIT=0
```

The checker also resolves every pointer and requires the resolved `source_id` /
`first_appearance` value to equal the row's in-world source ID; no pointer or
source-ID problem was reported on any of the 20 rows.

## C. Finding 1 — all 20 anchors in-span (own implementation)

20 JSON fact rows and 2 editorial rows parsed; every exact anchor found inside its
declared span; every row's mode `verbatim`; declared inventory
`20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors`
equals the parsed counts. New-row specifics (all inside the filing section):

| ID | pointer | declared span | anchor | anchor's own line |
|---|---|---:|---|---:|
| J18 | `entities.json#/5/first_appearance` (`clerk-maren`) | 60 | `I am Maren, clerk of the Chalk Stair registry` | 60 |
| J19 | `entities.json#/5/claims/0` (`statement`, `source_id`) | 59-60 | `I filed both pending accounts at the Chalk Stair registry.` | 59 |
| J20 | `timeline.json#/6` (six fields) | 55-64 | `Tick 14: I filed both pending accounts at the Chalk Stair registry.` | 59 |

Independent corroboration with the lane's own tool (same revision):

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
… PASS J01–J17 (inherited lines 12/13/17/18/19/20/26/37/48), PASS J18 (line 60),
  PASS J19 and PASS J20 (line 59), PASS S01, PASS S02
RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS                                                          (exit 0)
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations          (exit 0)
```

## D. Finding 2 — inherited line numbers preserved

- Excerpt prefix: my checker requires `fictional-excerpts.md` lines 1–53 to be
  byte-identical to the r97 baseline file; reported `PRESERVED PREFIX OK`.
- Map rows: a second scripted comparison of J01–J17 against the `9a3d648` map
  compared the pointer, in-world source ID, span, and anchor columns:

```
inherited ptr/src/span/anchor differences: NONE (17/17 identical)
r98-only rows: ['J18', 'J19', 'J20']
```

  (The path-qualification column alone changes to `r98-clerk-filing:…` by design;
  my comparison excludes it deliberately.)
- Map positions: J01 is line 22 and J17 is line 38 in both the r98 and r97 maps
  (`grep -n` on each), so the three new rows (lines 39–41) are appended after the
  inherited rows and no inherited row moved.
- No inherited span reaches into the new section (checker condition: all inherited
  span ends ≤ 53; max is J17's 44-53).

## E. Finding 3 — the three new anchors only in the filing-note section

- The new section is lines 55–64 (`## Round 98 clerk filing (2026-10-17)` at line
  55; line 54 is the blank separator after the preserved r97 text).
- Occurrence counts in the delivered excerpt: each new anchor occurs exactly once —
  J18 at line 60, J19 at line 59, J20 at line 59 — and all three occurrences lie in
  55–64; each anchor string is absent from the preserved prefix (lines 1–53), which
  my checker verifies directly.
- The map's prose claim "anchored only in the appended Round 98 clerk filing section
  (lines 55-64)" holds: spans are 60, 59-60, 55-64 respectively, all ≥ 55.

## F. Hazards, notes, bounds

- Placeholder hazard (recorded, not fatal): the fixture directory existed for ~2.5
  min with r97 bytes; existence-only polls would have passed on stale content. I
  content-gated every poll (cmp against r97 files, README title, map size) and
  re-ran the full check on the frozen revision after S4's report landed.
- Transparency on my own tooling: my first checker run reported 17 pointer
  "unresolved" errors — a parsing bug in my scratch (I stripped backticks from the
  whole pointer cell instead of extracting the first backticked token). Fixed in my
  scratch; the delivered map was never implicated, and the corrected run plus
  `support_check.py` agree.
- S4's report hash claims were re-verified by me (both sha256 match), and the map
  md5 was unchanged across all post-delivery checks.
- Bounds: my receipt covers fixed-string anchor containment, span bounds, pointer
  resolution, and inheritance identity. It is lexical preflight only — not
  whole-claim entailment, source authenticity, chronology truth, rights, permission,
  or canon review. The J18/J19/J20 prose paragraphs in the map (no-finding,
  no-verdict, no-reconciliation reading of lines 59–62) are S4's authored reading; I
  re-read them against the section and found them consistent with lines 59–62 and
  64, but that is a reading, not a mechanical check.

## Bottom line

**PASS** — on the frozen revision (map md5 `263403647097bcd6da3cdd524b7c4c73`),
all 20 JSON-fact anchors and both editorial anchors are in-span under my own
implementation; J01–J17 carry spans/anchors/modes/pointers identical to the r97
baseline at the same excerpt and map line numbers; and J18–J20 are anchored only in
the appended filing-note section (lines 59–60 inside 55–64), with
`support_check.py` 20/20 PASS and `check_bible` CLEAN as corroboration.
