# Round 11 critic: duplicate harbor reference premise

## Finding

The declared last-wins premise is reproducible. The checked-in baseline `.shokunin/lore/corpus/fixtures/check_bible.py` builds `entities` by repeatedly assigning `result[row['id']] = row` (lines 47–52), then timeline place validation consults `entities[row['place_id']]['kind']` (lines 228–231). `index()` reports the duplicate but retains the final row. Thus the map is order-sensitive even though the duplicate finding is present.

The checked-in round-9 pair is **not** evidence for this claim: `.shokunin/lore/corpus/fixtures/r9-dup-low-high/entities.json` and `r9-dup-high-low/entities.json` each have only one `harbor` entity; their duplicates are timeline event IDs. CLI probes against those fixtures both produce the duplicate timeline ID and ambiguous dependency findings, not an entity-kind result.

## Raw probes

I copied `.shokunin/lore/corpus/fixtures/consistent/` to temporary directories and changed only its `entities.json` to insert a second schema-valid `harbor` row, one `place` and one `character`; the baseline timeline already references `harbor` as a place. Both files remain intact at `/tmp/lore-r11-kbvizzu4/place-then-character/` and `/tmp/lore-r11-kbvizzu4/character-then-place/`.

Commands (exit status and complete stdout):

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r11-kbvizzu4/place-then-character
exit 1
VIOLATION: entities[2].id: duplicate entities id 'harbor'
VIOLATION: timeline[0].place_id: not a place 'harbor'
2 violation(s); no canon changed

python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r11-kbvizzu4/character-then-place
exit 1
VIOLATION: entities[2].id: duplicate entities id 'harbor'
1 violation(s); no canon changed
```

These inputs differ only in the order of the two duplicate rows. The duplicate-ID finding is stable, but the place-reference conclusion flips between `not a place` and no place finding. This falsifies output/conclusion invariance under row permutation and confirms the narrow stated bug. Baseline controls also passed: `python3 .../check_bible.py .shokunin/lore/corpus/fixtures/consistent` and the same command for `r10-registry-witness` each returned exit 0 and `CLEAN`.

## Collateral reference audit (baseline source inspection)

Duplicate entity IDs are already handled differently by other consumers; avoid assuming the timeline fix should globally redefine every reference:

- `relations` (`check_bible.py:118–123`) checks endpoint membership in the last-wins `entities` map only. A duplicate ID still counts as present; it does not report an ambiguous endpoint or inspect endpoint kind there.
- Item provenance (`:125–141`, `:161–184`) counts entity IDs and disables chain checking for a non-unique item ID; holder references with multiple rows set the record invalid without a dangling finding. This is already count-aware, unlike timeline place-kind validation.
- `allied_with` (`:210–216`) skips reciprocal/type checks unless both endpoint IDs are unique, avoiding last-wins faction classification.
- Timeline `entity_id` and `place_id` (`:228–231`) currently report dangling only when absent. `place_id` then uses last-wins kind with no multiplicity guard; this is the demonstrated defect. Occupancy (`:238–243`) keys by entity ID/tick and does not check identity uniqueness.
- Entity claims/first appearances are validated for each raw entity row (`:105–116`); the duplicate finding does not suppress their citation checks. Source and event-ID ambiguity have separate explicit counting logic.

The observed order sensitivity is specifically the timeline `place_id` kind conclusion. Row reordering can also affect diagnostic order/locations in general, so byte-for-byte whole-output invariance is a stronger property than the declaration requires. The desirable invariant here is a stable, explicit ambiguous-place-reference conclusion for either ordering, alongside the existing duplicate-ID report; do not promise whole-output equality unless diagnostics are normalized separately.

## Recommendations (separate from observations)

1. Keep the proposed guard local to timeline `place_id`: if matching valid entity-row count exceeds one, report an input-structural ambiguous place reference and skip last-wins kind classification. Preserve raw rows and the existing duplicate-ID finding.
2. Retain current distinctions for unique place, unique non-place, and dangling ID. Do not broaden this axis move into relation, provenance, allied-relation, or occupancy semantics; those have different existing guards/definitions.
3. Make the paired fixtures actually duplicate `harbor` entity rows. Include the two row orders and controls; the checked-in round-9 timeline-ID fixtures do not test this premise. Assert stable ambiguous-place conclusions, not byte-identical output globally.
