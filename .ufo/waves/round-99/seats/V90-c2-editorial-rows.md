# V90 c2-editorial-rows — round 99

Seat: V90 (verifier, c2-editorial-rows). Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). All commands from the lane root with `python3`. Leaf seat: no nested agents, no commits, no pushes, no network. Exclusive writes: this report and `.ufo/waves/round-99/seats/V90-scratch/verify.txt`. Nothing in `corpus/` was written.

Axes checked: (1) the two editorial rows inherited unchanged from the r98 map; (2) the map inventory counts equal `support_check.py`'s receipt exactly (JSON facts 21, editorial rows 2, total 23).

Subject: delivered `corpus/fixtures/r99-window-lapse/claim-excerpt-map.md`, compared to `git show 4265df5:corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md` (working-tree r98 is that blob).

## Poll

Not ABSENT. First look (before 22:02:39) the fixture map was still S3's r98 byte-copy (`15028` bytes, sha256 `c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba`, title `# r98 clerk-filing`). S4's report was absent then. S3's report (`S3-fixture-author.md`) said README and the map were left as r98 copies on purpose.

Delivery used for this verdict (after both the rewritten map and the producer report existed):

- Map mtime `2026-10-17 22:02:39.612249741 -0300`, `17119` bytes, sha256 `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d`. That hash equals the hash S4 claims in `.ufo/waves/round-99/seats/S4-fixture-docs.md`.
- S4 report present: `S4-fixture-docs.md`, mtime `2026-10-17 22:03:54.733612762 -0300`, `9303` bytes. It is a finished producer report (commands, observed receipts, trailing bottom line), not a plan.
- Locked re-check at `2026-10-17T22:20:16-03:00`. Map bytes had not moved since 22:02:39. Transcript: `V90-scratch/verify.txt`.

## Editorial rows inherited unchanged

The whole editorial section is identical to the r98 baseline section, not only the two data rows. r99 lines 44–51 equal r98 baseline lines 43–50 (`editorial_section_identical True`). Two data rows, seven cells each, every cell equal. No third `| S` row.

r99 section (quoted from the delivered file):

```
44|## Editorial rows (2 bounded Spence comparisons; not JSON facts)
45|
46|These rows compare delivered Spence clauses with the fictional design; they do not make Spence an in-world witness, assign cultural meaning, or add canon. `verbatim` describes the English prose delivered in `source-excerpt.md`, not an authenticated K'iche-language text.
47|
48|| ID | Bounded editorial comparison | Source citation | Excerpt path | Line span | R9 delivery mode | Exact anchor |
49||---|---|---|---:|---|---|---|
50|| S01 | Spence's phrase has the narrator call out “Earth”; the fiction's named Chalk Stair is a bounded crossing, not a world-making act. | Lewis Spence (1913), cited above | `source-excerpt.md` | 5 | `verbatim` | `He called out “Earth,”` |
51|| S02 | Spence says solid land appeared; the fiction's chalk stair remains “a crossing, never a map,” a limited design contrast rather than a shared cosmology. | Lewis Spence (1913), cited above | `source-excerpt.md` | 5 | `verbatim` | `and the solid land appeared.` |
```

Cell equality against `4265df5` r98 (and the working-tree r98 file, which is that blob: `wt_r98_equals_4265df5 True`, base sha256 `c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba`):

```
editorial_data_rows r99=2 r98=2
S01 cells=7 equal=True
S02 cells=7 equal=True
```

Unchanged cells on both rows: ID, bounded comparison, citation (`Lewis Spence (1913), cited above`), excerpt path (`source-excerpt.md`), line span (`5`), mode (`verbatim`), exact anchor (`He called out “Earth,”` / `and the solid land appeared.`). Curly quotes included; equality is Python string equality of the section, not a normalized compare.

`source-excerpt.md` in the r99 fixture is byte-identical to r98, so the anchors still hit the same line 5. `support_check` classifies both as editorial, not JSON facts:

```
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
```

Parser: `editorial_ids ['S01', 'S02']`, `parsed_editorial 2`. Scope of "unchanged" is this section only. The rest of the map did change (title, scope, inventory numbers, namespace column, appended J21, timeline prose). That is outside these two rows.

## Inventory line vs support_check receipt

Map declaration (one line, the only `**Expected inventory:**` line):

```
**Expected inventory:** 21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors.
```

`support_check.parse_map` on that file returned `parsed_expected (21, 2, 23, 19)`, `parsed_json 21`, `parsed_editorial 2`, `parsed_total 23`, `sum_ok True`, `counts_match_expected True`.

Locked command and the receipt lines (full stdout is in `V90-scratch/verify.txt`; stderr `''`):

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse ; echo EXIT:$?
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
EXIT:0
```

`receipt_exact_match True` against the literal line `RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23`. No `MISMATCH` suffix. No inventory failure. Exit 0.

The seat brief's shorthand `JSON-FACTS 21; EDITORIAL 2; TOTAL 23` is the same three counts. The tool does not print the tokens `EDITORIAL` or `TOTAL`; `corpus/tools/support_check.py` prints `EDITORIAL-ROWS` and `TOTAL-ROWS` (receipt f-string at lines 360–361). Those tool tokens, with values 21, 2, and 23, are exactly the receipt. The declared inventory and the parsed receipt agree on all three numbers. Distinct anchors 19/19 are consistent and were not part of the three-count claim.

## Not claimed

This seat did not re-check JSON-row inheritance, census, freeze pins, or whole-claim entailment. `support_check` is lexical preflight. S4's own quoted receipt matches this re-run; that agreement is noted, not treated as the evidence. Evidence is the re-run above.

PASS: r99 editorial section (S01, S02, heading, and intro) is identical to `4265df5` r98; receipt is exactly `RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23`, matching the map's 21 / 2 / 23 inventory, exit 0.
