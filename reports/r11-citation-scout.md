# Round 11 citation and naming scout

## Observed evidence

- The active checker at `.shokunin/lore/corpus/fixtures/check_bible.py` indexes entity records by `id` in `index('entities')` (duplicate IDs emit `duplicate entities id ...`); later timeline references use those IDs. A row with a duplicated ID overwrites the earlier dictionary value for that key. The timeline `place_id` check currently reads `entities[row['place_id']]['kind']` after only a presence check, so it classifies the last indexed row. This is identifier resolution, not display-name comparison.
- The active sample `.shokunin/lore/corpus/fixtures/consistent/entities.json` has `harbor` / `Lantern Harbor` / `place`. `name` is display text; entity IDs are the keys used by relation endpoints and timeline `entity_id`/`place_id`. No display-name uniqueness rule is in the active checker.
- In-world citations are a separate namespace: entity `first_appearance` and claim `source_id`, relation/event `source_id` resolve against source record `id`s in `sources.json`. The active checker counts duplicate source IDs and says `ambiguous in-world source`; e.g. `.shokunin/lore/corpus/fixtures/r7-item-ambiguous/sources.json` duplicates `archive-ledger`, and `.shokunin/lore/corpus/live/runs/20261012T170333Z/r7-item-ambiguous.txt` records citation ambiguity findings. A citation-ID collision is not an entity-ID collision and neither is a display-name homonym.
- Raw CLI probe, from repository root: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent` exits 0 (`CLEAN`).
- The historical exact-display-name experiment is preserved under `.shokunin/lore/corpus/live/rejected-r4/`. CLI `python3 .shokunin/lore/corpus/live/rejected-r4/check_bible.py .shokunin/lore/corpus/live/rejected-r4/name-duplicate` exits 1 with `duplicate display name 'Mira' for distinct entity IDs 'mira-one' and 'mira-two'; review, do not merge`; the paired `name-unique` command exits 0. Saved outputs are `.shokunin/lore/corpus/live/runs/20261012T163450Z/name-duplicate.txt` and `name-unique.txt`. `.shokunin/lore/corpus/fixtures/README.md` explicitly says the exact-name detector was rejected because it wrongly emitted a hard violation for legitimate homonyms. These archived probes are not active behavior.

## Bounded interpretation

A repeated entity **ID** is a structural key collision: references to that ID cannot unambiguously select one entity row. Distinct IDs with the same display `name` are not duplicate entity records; they may be legitimate homonyms and the rejected experiment demonstrates the calibration risk of treating them as invalid. Duplicate source IDs make citations ambiguous in the source namespace. Do not conflate these cases or claim that a repeated ID proves the rows describe the same in-world person/place.

## Recommendations (not changes)

1. Describe the proposed round-11 finding narrowly as: “`timeline[i].place_id` refers to an entity ID occurring in multiple schema-valid entity rows; report an ambiguous entity-ID reference and skip place-kind classification for that reference.” Keep the ordinary duplicate-ID diagnostic and raw records. Avoid “duplicate entity” as a merge instruction or a claim about identity.
2. Preserve unique-ID behavior: a single entity row with kind `place` passes the place-kind test; a single non-place remains `not a place`; an absent ID remains dangling. Do not broaden to every entity-ID consumer without separate evidence/scope.
3. State explicitly that equal display names are allowed, and source citations resolve by `source_id` against sources—not by entity name. Do not revive the rejected exact-name hard error. Any name-based alias/homonym review would be a different, non-blocking policy and is not supported by this round's evidence.
4. Avoid language implying a citation establishes the entity's real identity, source truth, or canon; this check concerns input-key ambiguity only.
