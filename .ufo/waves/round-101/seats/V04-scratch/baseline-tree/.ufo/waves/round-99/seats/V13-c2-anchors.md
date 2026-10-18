# V13 c2-anchors — round 99

Seat: V13 (verifier, C2 depth, anchors). Baseline: r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). Working-tree HEAD at verification was `337f0fa52b02626b7687eedbb2d99fab30446fe4`; the r98 map and excerpt used as the inherited baseline match that commit's blobs (sha256 below). All commands ran from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report and `.ufo/waves/round-99/seats/V13-scratch/` only.

Target (S4 byte-ownership): `corpus/fixtures/r99-window-lapse/claim-excerpt-map.md` (README read as context). Seat claim under test: all 21 anchors in-span by my own implementation; inherited line numbers preserved; the new anchor only in the lapse section.

Axes for this seat: span-containment (every exact anchor inside its declared line span), inheritance (J01–J20 pointer/source/path/span/mode/anchor and map line numbers unchanged), placement (exactly one new JSON-fact anchor, and only inside the appended lapse section).

Frozen revision verified (stable from the map write at 22:02:39 through the post-check `sha256sum -c`; README final at 22:03:19, before the checker run):

```
$ sha256sum corpus/fixtures/r99-window-lapse/claim-excerpt-map.md corpus/fixtures/r99-window-lapse/README.md corpus/fixtures/r99-window-lapse/fictional-excerpts.md
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  corpus/fixtures/r99-window-lapse/README.md
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  corpus/fixtures/r99-window-lapse/fictional-excerpts.md
$ md5sum corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
e7676509c13df358a764580d1f330334  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
$ stat -c '%y %s %n' corpus/fixtures/r99-window-lapse/claim-excerpt-map.md corpus/fixtures/r99-window-lapse/README.md
2026-10-17 22:02:39.612249741 -0300 17119 corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
2026-10-17 22:03:19.512442573 -0300 6176 corpus/fixtures/r99-window-lapse/README.md
```

Both delivered sha256 values match S4's report (section "Owned and delivered"), so the bytes I verified are S4's declared delivery. Post-check `sha256sum -c .ufo/waves/round-99/seats/V13-scratch/frozen-hashes.txt` reported OK for the map, README, excerpt, timeline, entities, sources, and the r98 baseline map and excerpt.

## A. Poll-wait record

Content-gated poll, 20 s cadence, max 40, logged at `.ufo/waves/round-99/seats/V13-scratch/poll.log`. Gate required the map md5 to differ from the r98 placeholder md5 `263403647097bcd6da3cdd524b7c4c73`, README to name the r99 fixture, excerpt to contain `clerk-lapse-note`, timeline to contain `clerk-lapse-recorded`, and an `S4*.md` report under `.ufo/waves/round-99/seats/` (SELF not required).

```
POLL_START 2026-10-17T22:02:08-0300 r98map_md5=263403647097bcd6da3cdd524b7c4c73
TRY 1 22:02:08 map_md5=263403647097bcd6da3cdd524b7c4c73 map_changed=0 readme_hit=0 exc_hit=1 tl_hit=1 s4_reports=none
TRY 2 22:02:28 … map_changed=0 … s4_reports=none
TRY 3 22:02:48 … map_changed=0 … s4_reports=none
TRY 4 22:03:08 map_md5=e7676509c13df358a764580d1f330334 map_changed=1 readme_hit=1 exc_hit=1 tl_hit=1 s4_reports=none
TRY 5 22:03:28 … map_changed=1 … s4_reports=none
TRY 6 22:03:48 … map_changed=1 … s4_reports=none
TRY 7 22:04:08 map_md5=e7676509c13df358a764580d1f330334 map_changed=1 readme_hit=1 exc_hit=1 tl_hit=1 s4_reports=S4-fixture-docs.md,
POLL_HIT try=7 22:04:08
```

Placeholder hazard (recorded, not fatal): at 22:01:24 the fixture directory already existed, but `claim-excerpt-map.md` was byte-identical to r98 (`md5 263403647097bcd6da3cdd524b7c4c73`, title `# r98 clerk-filing: canonical claim-to-excerpt map`, inventory 20/2/22/18) while `fictional-excerpts.md` already had the lapse section (76 lines) and `timeline.json` already had `clerk-lapse-recorded`. An existence-only poll would have scored the r98 copy. I did not. S3's report (`S3-fixture-author.md`, present at 22:01) explicitly left README and the map as r98 copies for S4. No ABSENT condition; no stall-escape.

## B. Method — own implementation

`.ufo/waves/round-99/seats/V13-scratch/check_anchors.py` (written by me; does not import `corpus/tools/support_check.py`). It parses both map tables, requires every exact anchor to be a substring of the declared span window and every `grep -nF` hit line to fall inside that span, resolves every `file.json#/pointer` against the fixture JSON (string node must equal the row source ID; object `source_id` must equal the row source ID), compares J01–J20 against the working-tree r98 map on pointer, source ID, excerpt path, span, mode, anchor, and map line number, requires `fictional-excerpts.md` lines 1–64 to equal the r98 excerpt, and requires the single new JSON row's span to start at or after the appended section and its anchor literal to be absent from the preserved prefix.

Parser sanity before the rewrite landed: on the r98 map it parsed 20 JSON facts and 2 editorial rows, inventory `(20, 2, 22, 18)`, J01 at map line 22 through J20 at map line 41, pointers `entities.json#/0/first_appearance` through `timeline.json#/6`.

Final run on the frozen revision (22:04:18, after S4's report; `CHECK_EXIT:0`):

```
$ python3 .ufo/waves/round-99/seats/V13-scratch/check_anchors.py
parsed rows: 21 JSON facts, 2 editorial
declared inventory: (21, 2, 23, 19) (map line 5)
INVENTORY OK: (21, 2, 23, 19)
ROW J01 … span=12-12 grep=[12] outside=[] …
ROW J20 map_line=41 span=55-64 window=True grep=[59] outside=[] own_line=59 ptr=timeline.json#/6 src=clerk-filing-note
ROW J21 map_line=42 span=66-76 window=True grep=[70] outside=[] own_line=70 ptr=timeline.json#/7 src=clerk-lapse-note
ROW S01 map_line=50 span=5-5 window=True grep=[5] outside=[] …
ROW S02 map_line=51 span=5-5 window=True grep=[5] outside=[] …
inherited-matched rows: 20; new rows: ['J21']; dropped: []
PRESERVED PREFIX OK: lines 1-64 byte-identical to r98
lapse section starts at line 65; new headings: [(66, '## Round 99 lapse note (2026-10-17)')]
r99 excerpt lines: 76

ALL CHECKS PASS
RESULT PASS
```

Full per-row lines are in `V13-scratch/check-final.txt`. No pointer or source-ID problem was reported on any of the 21 JSON rows. J21 resolves to `timeline.json#/7`, whose object is:

```
{
  "id": "clerk-lapse-recorded",
  "tick": 15,
  "entity_id": "clerk-maren",
  "place_id": "chalk-stair",
  "depends_on": ["clerk-filing-open"],
  "description": "At the Chalk Stair at tick 15, the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry.",
  "source_id": "clerk-lapse-note"
}
```

That matches the declaration (tick 15, actor `clerk-maren`, place `chalk-stair`, `depends_on: ["clerk-filing-open"]`).

## C. Finding 1 — all 21 anchors in-span (own implementation)

21 JSON fact rows and 2 editorial rows parsed. Every exact anchor is inside its declared span window; every `grep -nF` hit is inside that span; every mode is `verbatim`; declared inventory `21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors` equals the parsed counts. Inherited hit lines (own checker): J01/J03/J06/J08/J12 at 12, J02/J04/J07/J09/J13 at 13, J05 at 17, J10 at 18, J11 at 19, J14 at 20, J15 at 26, J16 at 37, J17 at 48, J18 at 60, J19/J20 at 59. New row:

| ID | pointer | declared span | anchor | anchor's own line |
|---|---|---:|---|---:|
| J21 | `timeline.json#/7` (`clerk-lapse-recorded`, `source_id` `clerk-lapse-note`) | 66-76 | `Tick 15: The crossing-window named in the original minute has closed.` | 70 |

Independent corroboration on the same frozen revision:

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01 … PASS J20; PASS J21 (line 70); PASS S01; PASS S02
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS                                                          (exit 0)
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations          (exit 0)
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS                                                          (exit 0)
```

## D. Finding 2 — inherited line numbers preserved

- Excerpt prefix: my checker requires `fictional-excerpts.md` lines 1–64 to equal the r98 file; reported `PRESERVED PREFIX OK`. The r98 excerpt sha256 `29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de` equals `git show 4265df5:corpus/fixtures/r98-clerk-filing/fictional-excerpts.md`.
- Map rows: an ID-keyed cell comparison of J01–J20 (and S01–S02) against the r98 map, swapping only the path-qualification namespace `r99-window-lapse:` back to `r98-clerk-filing:`, reported `content_diffs=0`. JSON map lines are identical: J01 at line 22 through J20 at line 41 in both maps. Editorial rows S01/S02 moved from map lines 49–50 to 50–51 because J21 was inserted at line 42; their path, span, mode, and anchor cells are unchanged (both still `source-excerpt.md` line 5).
- No inherited span reaches the lapse section (checker condition: inherited span ends ≤ 64; max is J20's 55–64).
- r98 map sha256 `c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba` equals the `4265df5` blob, so the comparison is against the closure baseline, not a drifted working-tree copy.

## E. Finding 3 — the new anchor only in the lapse section

- The appended section starts at line 65 (blank separator). Heading `## Round 99 lapse note (2026-10-17)` is line 66. Excerpt length is 76.
- J21's declared span is 66–76, which starts at the lapse heading and does not enter lines 1–64.
- The anchor literal occurs once in `fictional-excerpts.md`, at line 70, and is absent from lines 1–64 (`anchor_in_lines_1_64 False`). The only other file hit is the map row itself (line 42), which is the declaration, not a second excerpt occurrence.
- Quoted lines inside the span, read directly:

```
70: > Tick 15: The crossing-window named in the original minute has closed.
71: > The agreement was unfulfilled.
72: > No claim was lodged.
73: > The matter stands as a historical open entry.
74: > I record no resolution, assign no blame, and reconcile nothing.
```

- Exactly one new JSON-fact ID (`J21`); dropped inherited IDs: none. J21's map line (42) is after every inherited JSON row (max 41).

## F. Hazards, notes, bounds

- Placeholder hazard, as in section A. Content gate held until the map md5 changed and S4's report existed. The map hash was unchanged from 22:02:39 through the post-check `sha256sum -c`. README moved once after the map write (22:03:19, 6176 bytes, the hash S4 declares); that edit does not change map rows.
- A first ID-agnostic zip of table rows falsely reported S01 colliding with J21. That was my scratch script treating editorial rows (7 cells) as the next JSON row. The ID-keyed rerun reports `content_diffs=0`. The delivered map was not implicated. The failed scratch output is left in `V13-scratch/line-identity.txt` only as the corrected ID-keyed receipt (the broken zip was overwritten).
- S4's report hash claims were re-verified by me (map and README sha256 match).
- Bounds: this receipt is lexical preflight — fixed-string anchor containment, span bounds, pointer resolution, and inheritance identity. It is not whole-claim entailment, source authenticity, chronology truth, rights, permission, or canon review. The J21 prose paragraph in the map (no resolution, no blame, no reconciliation; matter stays open) is S4's authored reading; lines 70–74 and the scope sentence at line 76 are consistent with that reading, but that consistency is a reading, not a mechanical check. Census 172→173 and freeze pinning were not this seat's claim and were not measured here.

## Bottom line

**PASS** — on the frozen revision (map sha256 `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d`, matching S4), all 21 JSON-fact anchors and both editorial anchors are in-span under my own implementation; J01–J20 keep r98 pointers, spans, anchors, modes, and map line numbers, and the excerpt prefix lines 1–64 are byte-identical to the r98 baseline; J21 is the only new anchor and it occurs only in the lapse section (declared span 66–76, sole excerpt hit at line 70), with `support_check.py` 21/21 PASS, `map_obligations` 21/21 PASS, and `check_bible` CLEAN as corroboration.
