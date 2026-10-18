# V119 c2-map-anchors-3 — round 99

Seat: V119 (verifier, third anchor pass). Method required to differ from V13/V41: acceptance is a half-open **byte-offset window**, not `grep -nF` line membership. This seat did not read V13 or V41 reports. Baseline: r98 closure `4265df5`. Commands from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf: no nested agents, no commits, no pushes, no network. Writes: this report and `.ufo/waves/round-99/seats/V119-scratch/byte_window_anchors.py` only.

The 21 under test are the JSON-fact rows J01–J21 in `corpus/fixtures/r99-window-lapse/claim-excerpt-map.md`. Editorial S01–S02 were measured the same way and are not part of the 21.

## Poll record (20 s cadence)

| Time (local, -03) | Observation |
|---|---|
| 22:02:31 try 1 | Map still the r98 byte copy: 15028 bytes, sha256 `c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba`, header `# r98 clerk-filing…`, `J21` absent. Only producer report present: `S3-fixture-author.md`. Not verified. |
| 22:02:42 | Same map identity. Scratch checker written; not run against the placeholder. |
| 22:03:28 try 2 (after `sleep 20`) | Map rewritten: 17119 bytes, sha256 `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d`, header `# r99 window-lapse…`, `J21` present. S4 report still absent. |
| 22:05:08 | `S4-fixture-docs.md` present (9303 bytes, mtime 22:03). Its claimed map sha256 matches the bytes under test. |
| 22:07:21 | Re-hash unchanged. S3 and S4 reports both present. No further map edit. |

No ABSENT, no stall-escape. S5's knowledge files are outside this seat's artifact set and were not waited on. The placeholder map was not treated as the delivered revision.

## Method

A declared line span `L–M` becomes the half-open byte window covering those 1-based lines, newline byte included in the line it terminates. Two independent scanners, same offsets:

1. `V119-scratch/byte_window_anchors.py` — walk the file for `\r\n` / `\n` / `\r`, slice `raw[start:end]`, require `anchor.encode("utf-8")` as a contiguous substring, and require every whole-file `find` hit to lie inside that window.
2. A second pass that indexes only `0x0A` (no CRLF branch) and derives `hit_line` by counting newlines strictly before the hit offset.

Neither pass calls `grep`, `support_check`, or line-number membership as the acceptance test. Files are LF-only (`\r` absent in the map, `fictional-excerpts.md`, and `source-excerpt.md`).

## Commands and observed output

Delivered identity at verification time:

```
sha256sum corpus/fixtures/r99-window-lapse/claim-excerpt-map.md \
          corpus/fixtures/r99-window-lapse/fictional-excerpts.md \
          corpus/fixtures/r99-window-lapse/source-excerpt.md
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  claim-excerpt-map.md
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  fictional-excerpts.md
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
```

`fictional-excerpts.md` is 5114 bytes, 76 `0x0A`. `git show 4265df5:corpus/fixtures/r98-clerk-filing/fictional-excerpts.md` is 4187 bytes and is a strict prefix; the next byte is `0x0A`. Prefix equality: `startswith r98 bytes True`.

Second-pass result (0x0A index; `FAILS 0`):

```
OK J01 window=[379:434] hit=389 hit_line=12 span=12-12 file_occ=1 anchor_len=43
OK J02 window=[434:484] hit=444 hit_line=13 span=13-13 file_occ=1 anchor_len=38
OK J03 window=[379:434] hit=389 hit_line=12 span=12-12 file_occ=1 anchor_len=43
OK J04 window=[434:484] hit=444 hit_line=13 span=13-13 file_occ=1 anchor_len=38
OK J05 window=[593:678] hit=595 hit_line=17 span=17-17 file_occ=1 anchor_len=82
OK J06 window=[379:434] hit=381 hit_line=12 span=12-12 file_occ=1 anchor_len=52
OK J07 window=[434:484] hit=436 hit_line=13 span=13-13 file_occ=1 anchor_len=47
OK J08 window=[379:434] hit=405 hit_line=12 span=12-12 file_occ=1 anchor_len=27
OK J09 window=[434:484] hit=458 hit_line=13 span=13-13 file_occ=1 anchor_len=24
OK J10 window=[678:761] hit=680 hit_line=18 span=18-18 file_occ=1 anchor_len=80
OK J11 window=[761:848] hit=763 hit_line=19 span=19-19 file_occ=1 anchor_len=84
OK J12 window=[379:434] hit=389 hit_line=12 span=12-12 file_occ=1 anchor_len=43
OK J13 window=[434:484] hit=444 hit_line=13 span=13-13 file_occ=1 anchor_len=38
OK J14 window=[678:1116] hit=850 hit_line=20 span=18-20 file_occ=1 anchor_len=265
OK J15 window=[1117:1845] hit=1379 hit_line=26 span=22-31 file_occ=1 anchor_len=61
OK J16 window=[1846:2588] hit=2107 hit_line=37 span=33-42 file_occ=1 anchor_len=58
OK J17 window=[2589:3410] hit=2861 hit_line=48 span=44-53 file_occ=1 anchor_len=55
OK J18 window=[3738:3817] hit=3740 hit_line=60 span=60-60 file_occ=1 anchor_len=45
OK J19 window=[3668:3817] hit=3679 hit_line=59 span=59-60 file_occ=1 anchor_len=58
OK J20 window=[3411:4187] hit=3670 hit_line=59 span=55-64 file_occ=1 anchor_len=67
OK J21 window=[4188:5114] hit=4444 hit_line=70 span=66-76 file_occ=1 anchor_len=69
FAILS 0
r98 excerpt bytes 4187
J21 window 4188 5114 equals append region True
```

The first scanner printed the same 21 windows and the same hit offsets, then `FAILURES 0`. Every hit is inside a `"> "` blockquote body that itself sits inside the declared window. No anchor contains a newline. Each of the 19 distinct anchor strings occurs once in its file (`file_occ=1`). The four repeated references are shared strings, not extra occurrences: J01/J03/J12 share offset 389; J02/J04/J13 share offset 444.

J20's window ends at byte 4187, the r98 prefix boundary. J21's window is exactly the appended region `[4188:5114]` (after the extra newline that becomes blank line 65, which is in neither window). The J21 anchor cannot be an inherited byte.

Inherited row identity versus `4265df5:corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md`, fields `path` / `span` / `anchor` / `mode` for J01–J20 and S01–S02: `INHERITED DRIFT []`. New row only: J21, span `(66, 76)`, anchor `Tick 15: The crossing-window named in the original minute has closed.`, mode `verbatim`, pointer `timeline.json#/7`.

Inside the J21 window, these byte strings are present (exact):

- `The crossing-window named in the original minute has closed.`
- `The agreement was unfulfilled.`
- `No claim was lodged.`
- `The matter stands as a historical open entry.`
- `I record no resolution, assign no blame, and reconcile nothing.`
- `creates no new duty`
- `the matter stays open`

`resolution`, `blame`, and `reconcil` each occur twice in that window, both times inside those negations, not as positive assertions.

Quote bytes: J14's apostrophe in `Aru's` is U+0027 (`0x27`), matching the map anchor. S01's `“Earth,”` is U+201C / U+201D (offsets in `source-excerpt.md`: hit 391, window `[241:447]`, line 5, `file_occ=1`). S02 hit 418, same window. Editorial rows are extra; both passed the same byte test.

JSON pointer walk (first scanner, `POINTER ok` on all 21): each `file.json#/index` resolves, and the named fields exist on object rows. Confirmed targets: entity ids `aru, evin, quiet-rise, salt-court, chalk-stair, clerk-maren`; relation `aru → evin` type `agreed_co_stewardship_for_this_crossing` source `crossing-minute`; timeline length 8, last event `clerk-lapse-recorded` tick 15, `entity_id` `clerk-maren`, `place_id` `chalk-stair`, `depends_on` `["clerk-filing-open"]`, `source_id` `clerk-lapse-note`. Sources length 8, last id `clerk-lapse-note`. Entities 6, relations 1, contradictions `[]`. `sources.json[:-1]` and `timeline.json[:-1]` equal the r98 arrays.

Cross-check only (not this seat's acceptance test):

```
python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; … VALIDATED-ROWS 23/23
RESULT PASS
EXIT:0

python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
EXIT:0
```

`support_check` uses `grep -nF`. Its line hits agree with the byte-derived `hit_line` values above. Agreement is corroboration; the byte windows are the verdict.

## Bounded observation (does not fail an anchor)

Map line 69 says the window "has closed per that minute's terms." The quoted lapse lines, and the J21 anchor, say "named in the original minute has closed." The words `per that minute's terms` are not in the excerpt window. That is editorial strengthening in the scope paragraph, outside the fixed-string anchor contract. The 21 anchors still match.

## Not claimed

This pass does not prove whole-claim entailment, canon truth, or that `depends_on` event ids are literal excerpt syntax. It does not re-run census or the freeze chain.

PASS: all 21 JSON anchors verified inside their declared byte-offset windows, each string once; J21's window is exactly the appended lapse region.
