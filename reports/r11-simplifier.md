# Round 11 simplifier — timeline `place_id` ambiguity guard

## Observed baseline and probes

The current observed checker is `.shokunin/lore/corpus/fixtures/check_bible.py`. In `check()`, schema-valid entity rows are counted into `entity_id_counts` before timeline validation. The timeline place check currently does a dangling test (`row['place_id'] not in entities`) followed by a last-wins kind dereference (`entities[row['place_id']]['kind'] != 'place'`). The `entities` index is overwritten on duplicate IDs; `index('entities')` separately reports the duplicate.

I constructed two temporary probes from `.shokunin/lore/corpus/fixtures/consistent/`: each retained the original rows and changed only duplicate `harbor` entity rows (one `place`, one `character`) and their order. Raw probe directories:

- `/tmp/r11-place-first-g97_nejv`: `harbor` place then character; `python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r11-place-first-g97_nejv` exited 1, reporting duplicate `harbor` and `timeline[0].place_id: not a place 'harbor'`.
- `/tmp/r11-character-first-asz45bgk`: character then place; `python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r11-character-first-asz45bgk` exited 1, reporting only duplicate `harbor`; no timeline place finding.

Thus the declaration's order-dependence premise is confirmed for a place reference with two schema-valid rows. These are temporary scratch probes, not added fixtures.

## Smallest recommendation

In the timeline loop, retain the existing dangling-reference check. For a non-dangling `place_id`, consult the already-computed `entity_id_counts` before dereferencing `entities[place_id]['kind']`:

1. If count is greater than one, append one local finding such as `timeline[i].place_id: ambiguous entity reference 'harbor'` and do not classify its kind.
2. Otherwise, preserve the existing `not a place` check for the unique entity.

This is a narrow branch at the existing place-kind check. It needs no new index, no changes to `index()`, and no new generalized resolver. Keep the duplicate-ID finding; preserve raw rows. Avoid additionally marking `entity_id` or relation endpoints ambiguous in this move: they are outside the stated timeline-place rule. A dangling `place_id` should continue to get only the existing dangling finding, not an ambiguity finding.

## Separate recommendations / controls

- Verify both row orders produce the duplicate-ID finding plus the same ambiguous-place finding; do not expect identical full output order if unrelated diagnostics differ.
- Keep a unique `place` control accepted and a unique non-place control rejected as `not a place`; retain dangling-reference behavior.
- Replay the 20 baseline fixture CLI outputs unchanged apart from no newly added ambiguity case being among those baselines. This report does not claim those replays were run.
- This is structural calibration only. It does not establish canon, resolve conflicting entity rows, or generalize ambiguity semantics to other references.
