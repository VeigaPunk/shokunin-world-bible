# Round 17 critic — wrong-kind place occupancy

## Observed raw CLI (current checkout)

I did not modify fixtures or checker. No `r17-*` fixture directories existed in this checkout during this review, so the round-17 paired controls are not yet independently replayable here. These are the available related raw results:

```text
$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r11-unique-nonplace
VIOLATION: timeline[0].place_id: not a place 'mira'
1 violation(s); no canon changed

$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r16-valid-places
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed

$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r16-mixed-three
VIOLATION: timeline[1].place_id: dangling entity 'unlisted'
VIOLATION: timeline[2]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
2 violation(s); no canon changed

$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r16-missing-place
VIOLATION: timeline[1].place_id: dangling entity 'unlisted'
1 violation(s); no canon changed
```

The current checker reports a unique wrong-kind ID as `not a place` but still admits its raw ID into occupancy (`actor_id_count == 1 and place_id_count != 0`). The r11 wrong-kind raw row is `place_id: "mira"`; its description says “Mira departs the harbor.” Its cited source ID is `courier-log`, whose fixture source metadata identifies a personal log but supplies no excerpt establishing this event wording. Thus the fixture prose does not describe the raw place ID, and the citation ID alone does not repair that mismatch or establish canon.

## Critique / recommendations (not observed behavior)

- The narrow proposed suppression is logically calibrated if it excludes only a uniquely indexed, non-`place` `place_id` from occupancy comparison and insertion, while preserving `not a place` and the raw timeline row. It should not imply the event has no actual location or that a real conflict is absent: the conflict involving that row remains **unassessed**.
- Verify the intended controls with fresh fixtures, including wrong-kind before, between, and after two valid different places for the same uniquely identified actor/tick. The known valid pair must still be reported irrespective of wrong-kind event order. Compare the full old fixture corpus byte-for-byte/output-for-output, not only the new examples.
- Correct any fixture prose/source mismatch before using it as evidence. A fixture description that says “harbor” while `place_id` points to the character `mira` overstates or contradicts the structured input. Use explicit fixture-scoped wording for the intentionally malformed row; do not imply `courier-log` contains or attests the prose unless its excerpt actually does.
- Duplicate/ambiguous place IDs remain an independent unresolved case. Current `place_id_count > 1` reports `ambiguous place entity`, but `place_id_count != 0` still lets that ID participate in raw occupancy comparisons. The wrong-kind guard does not fix that behavior; do not claim all ambiguous-place occupancy is calibrated or resolved. A repeated ambiguous ID versus a uniquely valid place can still yield a raw-ID `double-booked` conclusion whose entity identity is not established.
- A unique wrong-kind entity may itself have a schema-invalid kind, or be a legitimate non-place kind; in either case, `not a place`/schema findings describe input classification, not event truth. Avoid concluding more than “different resolved place IDs” from checker output.
