# Round 17 citation scout — identity and truth boundaries

Scope: read-only scout. This report distinguishes what the checked JSON and raw CLI establish from recommendations. No checker, fixture, shared document, or commit was changed.

## Observed from the checker and raw CLI

The checker maintains distinct registries for `entities.id`, `sources.id`, and timeline-event `id`. `timeline.entity_id` and `timeline.place_id` refer to entity IDs; `timeline.source_id` refers to a source ID. The `name` field is a display string, not a lookup key in the checker. Entity-kind validation reads the uniquely indexed entity row's `kind`, not its name or a cited source.

The checker screens required fields/types before adding rows to `data`; only those screened entity rows feed the entity index and `entity_id_counts`. It then reports missing entity references as dangling, duplicate IDs as duplicate/ambiguous, and a unique wrong-kind place reference as `not a place`. For timeline occupancy, its current condition is `actor_id_count == 1 and place_id_count != 0`: thus it compares a unique non-place entity ID as a place ID despite the separate kind diagnostic. This is raw-ID behavior, not evidence that the referenced entity is an actual place.

Raw command used: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>`.

- `r11-unique-nonplace`: exit 1; `timeline[0].place_id: not a place 'mira'`; one violation. No `double-booked` in this fixture because its second event is tick 2, so it does not test a same-tick wrong-kind collision.
- `r11-place-character`: exit 1; duplicate entity ID `harbor` and `timeline[0].place_id: ambiguous place entity 'harbor'`. The duplicate rows have different kinds and different display names; raw ID ambiguity is diagnosed, rather than selecting one row by kind or name.
- `r16-valid-places`: exit 1; a definite raw-ID `double-booked` finding for unique actor `mira`, tick 7, `harbor` and `tower`.
- `r12-unique-actor`: same double-booked finding for the same canonical fixture pattern.

An additional temporary, isolated probe copied `r11-unique-nonplace` to a system temporary directory, added a second distinct place entity ID (`alt-place`) with display name `North Tower`, and made two tick-7 events for actor `mira`, with place IDs `mira` and `alt-place`. CLI output retained `not a place 'mira'` and also emitted `double-booked ... ('mira') and 'alt-place'`. The probe introduced an unrelated dependency-tick violation because it changed the first event's tick without its dependent event; do not use that probe as clean fixture evidence or as a complete test of round-17 controls. It demonstrates current raw ID comparison only.

Citations are checked as source-reference identity: `source_id` must match zero, one, or multiple source rows, producing unknown, unique, or ambiguous status. For a unique source ID, this code does not read or parse the source's supposed text, verify that it states the timeline description, resolve an entity ID from text, or adjudicate whether an event is true in-world. Likewise `name`/`description` prose is not evidence consumed by the occupancy comparison. A passing/unique source reference is not corroboration of the event or the place assignment.

## Recommendations (not observed behavior)

- For the declared round-17 narrow move, base whether an event may participate in a *definite different resolved places* comparison on a unique, valid entity row for `place_id` whose `kind == 'place'`, as well as a unique actor. Preserve the existing `not a place`/dangling/ambiguous findings and raw input. Keep missing-ID round-16 behavior and duplicate-ID behavior separate unless explicitly scoped.
- Test a same-tick unique character place-ID against a known place, two valid unique places as a positive control, and known/wrong-kind/known order as a mixed control. Assert raw CLI output and exit statuses, and ensure event ticks/dependencies do not create unrelated findings. Replay the existing baseline fixtures unchanged.
- Phrase claims narrowly: withholding the checker’s definite resolved-place collision is not proof of no collision, does not infer a location, and does not change canon. A display name that looks like a place and a unique citation source ID do not cure a wrong entity kind or establish in-world truth.
- If source-content corroboration is ever a goal, define a separate evidence model and validation scope; do not treat this ID-reference checker as a source-text verifier or silently turn display names/descriptions into truth.
