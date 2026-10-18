# S4 fixture-docs — round 99

Seat: S4 (producer, byte-ownership). Baseline: r98 closure `4265df5`. All commands ran from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested agents, no commits, no pushes, no network. Writes: the two owned fixture paths below (absolute), this report, and `.ufo/waves/round-99/seats/S4-scratch/` (`poll.log`, `map-namespace-swap.md`, `map-ns.md`, `claim-excerpt-map.md` draft).

Owned and delivered (both rewritten from the r98 placeholder copies S3 left in the new directory):

1. `corpus/fixtures/r99-window-lapse/claim-excerpt-map.md` — 17,119 bytes; sha256 `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d`
2. `corpus/fixtures/r99-window-lapse/README.md` — 6,176 bytes; sha256 `b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049`

## A. Poll-wait record

- 22:00:23: `corpus/fixtures/r99-window-lapse/` absent; `.ufo/waves/round-99/seats/` absent.
- 22:01:09 try=1: directory present, content not ready (`poll.log`: `dir-present content-not-ready`). At 22:01:23 the directory held the r98 placeholder README and map (21:36 mtimes, 5,829 and 15,028 bytes) while `fictional-excerpts.md`, `sources.json`, and `timeline.json` were already the lapse bytes (mtime 22:01:13).
- 22:01:29 try=2: POLL_HIT. Content gate (`grep clerk-lapse-recorded timeline.json` AND `grep clerk-lapse-note sources.json` AND `grep clerk-lapse-note fictional-excerpts.md`) passed. S3's report was absent at the hit.
- 22:03:09: `S3-fixture-author.md` was present (5,069 bytes, mtime 22:01). No ABSENT condition arose and no stall-escape was needed. Same placeholder hazard as r98: an existence-only poll is satisfied by the r98 byte copies of README and claim-excerpt-map. Writes were gated on the lapse markers and re-verified afterwards. S3 data-file mtimes stayed 22:01:13 (`timeline.json`, `sources.json`, `fictional-excerpts.md`) and 21:36:10 (`entities.json`) through the final gate run at 22:03:23.

## B. Map: canonical form, ALL 21 obligations

`claim-excerpt-map.md` declares `**Expected inventory:** 21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors.` and carries 21 canonical `file.json#/pointer` rows in `## JSON facts` (six `first_appearance`, six claims, one relation, eight timeline events).

**20 inherited rows (J01–J20) unchanged modulo namespace.** Row comparison against the r98 map (pointer cell, anchor, span, mode; namespace string swapped back):

```
rows_a=20 rows_b=21
changed_inherited 0 []
line_numbers_identical True
pairs: J01–J20 at map lines 22–41 in both maps
new_rows ['J21']
```

The inherited rows keep identical map line numbers because J21 is appended after them. `map_obligations` compares as a set and PASSes.

**Anchor line numbers unchanged** (`grep -nF` first hit on the r99 excerpt, inside the declared span for every inherited row):

```
J01 span=12 first=12
J02 span=13 first=13
J03 span=12 first=12
J04 span=13 first=13
J05 span=17 first=17
J06 span=12 first=12
J07 span=13 first=13
J08 span=12 first=12
J09 span=13 first=13
J10 span=18 first=18
J11 span=19 first=19
J12 span=12 first=12
J13 span=13 first=13
J14 span=18-20 first=20
J15 span=22-31 first=26
J16 span=33-42 first=37
J17 span=44-53 first=48
J18 span=60 first=60
J19 span=59-60 first=59
J20 span=55-64 first=59
```

**Excerpt is append-only** (inherited bytes preserved):

```
excerpt_prefix_identical True
r98 fictional-excerpts.md 4187 bytes is a byte prefix of the r99 file (5114 bytes)
```

**One new row, pointer `timeline.json#/7`, anchored only in the new lapse section (lines 66-76):**

| ID | pointer | source | span | anchor |
|---|---|---|---:|---|
| J21 | `timeline.json#/7` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `clerk-lapse-note` | 66-76 | `Tick 15: The crossing-window named in the original minute has closed.` |

```
$ grep -nF -- "Tick 15: The crossing-window named in the original minute has closed." corpus/fixtures/r99-window-lapse/fictional-excerpts.md
70:> Tick 15: The crossing-window named in the original minute has closed.
```

That hit is inside span 66-76 and is not inside any inherited span. The row's path-qualified namespace is `r99-window-lapse:clerk-lapse-note`. The map's timeline paragraph names the edge `clerk-lapse-recorded` depends on `clerk-filing-open`, and the J21 paragraph names the no-resolution / no-blame / no-reconciliation sentence at excerpt line 74. The delivered event (S3) is tick 15, `entity_id` `clerk-maren`, `place_id` `chalk-stair`, `depends_on` `["clerk-filing-open"]`, `source_id` `clerk-lapse-note`.

Parsed counts on the delivered JSON at gate time: entities 6, relations 1, timeline 8, sources 8, contradictions 0. Timeline prefix versus r98 was identical (7 inherited events, then the appended lapse event).

## C. Gates on the delivered r99 bytes (final run 22:03:23, after the README bound-phrase edit)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
bible_exit=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01 … PASS J20 (inherited lines 12/13/17/18/19/20/26/37/48/59/60)
PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
PASS S01; PASS S02
RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
support_exit=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
map_exit=0
```

An earlier run at 22:02 (before the two README phrase edits) produced the same three receipts and the same exit codes. The README edits do not change map rows; the map sha256 above is unchanged across those edits.

## D. README

Line 3 states `6 entities / 1 relation / 8 events / 8 sources`. Line 11 states the lapse bound: the window closed per the original minute's terms; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry and the matter stays open; nothing is resolved; no blame; no reconciliation; it closes no one. Line 21 states 21 source-attributed JSON pointer obligations (20 inherited rows carried unchanged plus the new tick-15 lapse event, pointer `timeline.json#/7`). Lines 25-29 are the three replay commands against `corpus/fixtures/r99-window-lapse`. It is not the r98 placeholder:

```
r98 README sha256 32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926 (5,829 bytes; still the placeholder at poll-hit)
delivered README sha256 b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049 (6,176 bytes)
```

## E. Cross-checks, contradictions, bounds

- S3's report (section "Not done / follow-up") says README and claim-excerpt-map still say r98 (20 obligations, 6/1/7) and that `support_check` / `map_obligations` should be expected to see the inherited r98 map. That was true at S3's report time (their cmp showed both files identical to `4265df5` r98, and at poll-hit both were still the 21:36 placeholders). It is stale for the delivered tree: both files were rewritten by this seat (map 22:02:39, README 22:03, final sha256s above) and the gates in section C were run on those bytes. No action taken on S3's files.
- S3's delivered event matches the declared shape this map rows against: `clerk-lapse-recorded`, tick 15, actor `clerk-maren`, place `chalk-stair`, `depends_on: ["clerk-filing-open"]`, source `clerk-lapse-note`. Excerpt quote lines 70-74 match the anchors named in J21's paragraph. I did not rewrite any S3 file.
- Bounds of my receipts: `support_check` and `map_obligations` are lexical preflight and one-to-one mapping checks, not whole-claim entailment, source authenticity, chronology truth, rights, permission, or canon review. The J21 prose paragraph is my authored reading of the appended section (lines 66-76); a verifier should re-read that section against it. Census 172→173 was not measured by this seat (not in the owned write set). Freeze pinning of the new Markdown is S1's contract, not verified here.
- Row order: J21 is appended after the inherited rows so every inherited row keeps its r98 map line number; the tools compare as sets and PASS.

## Bottom line

**PASS** — r99 `claim-excerpt-map.md` carries all 21 canonical pointer rows, the 20 inherited rows identical modulo namespace at unchanged map line numbers with anchors verified by `grep -nF` at the same excerpt line numbers, and the new row `timeline.json#/7` anchored only in the appended lapse section (lines 66-76, hit at line 70); README states the 6/1/8 counts, 8 sources, 21 obligations, the lapse bound (window closed per the original minute's terms; matter stays open; nothing resolved), and the replay commands; on the delivered bytes `check_bible` is CLEAN (exit 0), `support_check` is 21/21 PASS (exit 0), and `map_obligations` is raw=21 mapped=21 PASS (exit 0).
