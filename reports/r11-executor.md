# Round 11 executor report — timeline place-ID ambiguity

## Change
Added a local timeline `place_id` guard in `corpus/fixtures/check_bible.py`, using the existing `entity_id_counts`. A count greater than one emits `timeline[i].place_id: ambiguous place entity {id!r}` and skips last-wins kind lookup. A unique ID retains the existing not-a-place check; an absent ID retains the existing dangling check. The existing duplicate-entity-ID finding and all entity rows remain intact. No other code paths changed.

## Paired fixtures
Ran both existing row-order fixtures:
- `r11-place-character`: duplicate-ID report for `harbor` and `timeline[0].place_id: ambiguous place entity 'harbor'`.
- `r11-character-place`: same two conclusions.
Controls:
- `r11-unique-nonplace`: `timeline[0].place_id: not a place 'mira'`.
- `r11-dangling-place`: `timeline[0].place_id: dangling entity 'unlisted'`.

## Baseline replay
Loaded checker source with `git show 4337c63:.shokunin/lore/corpus/fixtures/check_bible.py` and ran it and the modified checker against each of the 20 existing non-r11 fixture directories. All 20 matched exactly in stdout, stderr, and exit status (including the clean/violation status). Thus the change did not alter prior fixture outputs.

## Scope and limits
This is only a local input-structure finding for timeline place references whose IDs occur in multiple schema-valid entity rows. It does not resolve identity or canon, and makes no claim about relations, timeline actors, occupancy, provenance, homonyms, or source truth. No fixtures or docs changed by this executor; no commit made.
