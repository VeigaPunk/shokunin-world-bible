# S3 fixture-author — r99-window-lapse

Seat: S3. Exclusive writes: `corpus/fixtures/r99-window-lapse/` (all ten files) and this report. No commits. Baseline blob source: `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`) `corpus/fixtures/r98-clerk-filing/`. Working-tree HEAD at start was `337f0fa` (ahead of the baseline commit); the copy was taken from `git archive 4265df5`, not from the working tree. `git status --short -- corpus/fixtures/r98-clerk-filing` was empty after the copy, so r98 was not touched.

## What changed

Byte-copied all ten r98 files, then modified only three:

- `sources.json`: appended `clerk-lapse-note` (title "Maren's Chalk Stair Lapse Note", kind fictional first-person note). Inherited seven sources unchanged. 7 → 8.
- `timeline.json`: appended `clerk-lapse-recorded`, tick 15, `entity_id` `clerk-maren`, `place_id` `chalk-stair`, `depends_on` `["clerk-filing-open"]`, `source_id` `clerk-lapse-note`. Description records that the crossing-window named in the original minute has closed, the agreement was unfulfilled, no claim was lodged, and the matter stands as a historical open entry. Inherited seven events unchanged. 7 → 8.
- `fictional-excerpts.md`: byte-prefix of the r98 file preserved (including its trailing newline); appended dated section "Round 99 lapse note (2026-10-17)" with the clerk's first-person note (folio 9, lines 1–5). The quoted note asserts no resolution, assigns no blame, and reconciles nothing. The scope sentence states that the section creates no new duty and that the matter stays open. Those denials are negations, not positive assertions of resolution, blame, reconciliation, or a new duty.

Unchanged versus `4265df5:corpus/fixtures/r98-clerk-filing/` (cmp identical): `README.md`, `claim-excerpt-map.md`, `contradictions.json`, `entities.json`, `inspiration-note.md`, `relations.json`, `source-excerpt.md`. Entities remain 6, claims remain 6, relations remain 1, contradictions remain `[]`. No new entity, claim, or relation. README and claim-excerpt-map were left as r98 byte copies on purpose: S4 owns those two files.

Parsed-prefix check: `sources.json[:-1]` and `timeline.json[:-1]` equal the r98 JSON arrays. `fictional-excerpts.md` startswith the r98 bytes plus a newline.

Inventory after the edit: 6 entities / 1 relation / 8 sources / 8 timeline events / 0 contradictions. That is the declared 6/1/8 shape. Census 172→173 was not re-run here (S3 does not own a census script or `corpus/fixtures/README.md`); the new directory is one additional fixture dir, which is the census increment if the r98 count was fixture directories.

## Commands and observed output

Copy (lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`):

```
git rev-parse 4265df5
4265df5e86e4121bde4125b649b89bb1676676a5

mkdir -p corpus/fixtures/r99-window-lapse
git archive 4265df5 corpus/fixtures/r98-clerk-filing | tar -x --strip-components=3 -C corpus/fixtures/r99-window-lapse
```

Post-copy cmp of each of the ten files against working-tree `corpus/fixtures/r98-clerk-filing/<f>`: all ten printed `MATCH`. Post-copy JSON lengths: sources 7, entities 6, relations 1, timeline 7, contradictions 0.

Checker:

```
python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT:0
```

Byte comparison against `git show 4265df5:corpus/fixtures/r98-clerk-filing/<f>`:

```
README.md: identical=True base=5829 now=5829
claim-excerpt-map.md: identical=True base=15028 now=15028
contradictions.json: identical=True base=3 now=3
entities.json: identical=True base=1793 now=1793
inspiration-note.md: identical=True base=1956 now=1956
relations.json: identical=True base=139 now=139
source-excerpt.md: identical=True base=640 now=640
sources.json: identical=False base=2725 now=3293
timeline.json: identical=False base=2552 now=2998
fictional-excerpts.md: identical=False base=4187 now=5114
sources prefix identical True
timeline prefix identical True
excerpt byte-prefix True
excerpt starts with base then newline True
```

`git status --short -- corpus/fixtures/r98-clerk-filing corpus/fixtures/r99-window-lapse` showed only `?? corpus/fixtures/r99-window-lapse/`.

## Not done / follow-up

- S4 still owns README and claim-excerpt-map. Those files still say r98 (20 obligations, 6/1/7, span ending at the clerk-filing section). The 21st map row is not in this seat's write set. Until S4 lands, `support_check` / `map_obligations` against this fixture should be expected to see the inherited r98 map, not 21 rows.
- Census 172→173 not measured by this seat.
- No freeze pin written (S1 owns the freeze tool and contract). A pre-C1 pin that hashed only the five JSON tables would mismatch `sources.json` and `timeline.json` if someone froze r99 before S1's full-file pin exists; that is expected, not a fixture defect.

PASS: r99-window-lapse is 6/1/8 with clerk-lapse-note and tick-15 clerk-lapse-recorded; check_bible CLEAN exit 0; seven inherited files byte-identical to 4265df5 r98; no new entities, claims, or relations.
