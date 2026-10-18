# Round 10 timeline scout: synchronized archivist witness and Mira departure

## Observed constraints (repository evidence)

- The clean baseline has Mira’s `departure` at tick 1 in `harbor`, followed by `arrival` at tick 2 in `tower`; `arrival.depends_on` contains `departure`. See `.shokunin/lore/corpus/fixtures/consistent/timeline.json`.
- Event rows require `id`, integer `tick`, `entity_id`, `place_id`, list `depends_on`, `description`, and `source_id`; see `FIELDS` and the timeline loop in `.shokunin/lore/corpus/fixtures/check_bible.py`. The checker rejects negative ticks, dangling entity/place IDs, and a `place_id` whose entity kind is not `place`. Timeline source IDs must resolve uniquely.
- Occupancy is keyed by `(entity_id, tick)`. Reusing an entity at a tick is only diagnosed as double-booked when the locations differ; different entities may occupy the same place and tick. This is structural input validation, not proof that the described people were really there.
- Each dependency must be an event-ID string. Unknown and ambiguous target IDs are errors; a unique dependency must have a strictly smaller tick than the dependent event. Thus a same-tick witness event cannot be made a dependency of the same-tick departure (nor vice versa). Duplicate event IDs are errors; contradiction references additionally require exactly one event ID.
- Existing source catalog entries are fictional `courier-log` and `archive-ledger`, described as first-person and municipal records respectively, in `.shokunin/lore/corpus/fixtures/consistent/sources.json`. The round-10 declaration says the baseline has no excerpt text; the schema itself has no excerpt-text field.

## Timeline implications for this proposed beat

Represent the witness’s presence as a distinct timeline event with the archivist as `entity_id`, `harbor` as `place_id`, and the exact same tick as Mira’s departure. This avoids the occupancy collision because the event entities differ, while expressing coincidence at the fixture’s tick granularity. Both event rows need unique IDs and uniquely resolving source IDs. The witness entity must be declared, as must `harbor` (already present in the baseline).

Do not add a `depends_on` edge between the two simultaneous events: strict-earlier validation makes that invalid. Keep the existing `arrival` at a later tick and its dependency on `departure`; any dependency on the witness event is valid only if the chosen witness tick is strictly earlier than arrival. Do not reuse Mira’s ID for the witness event/entity or put either actor at another place at the same tick.

## Recommendations (not observations or canon claims)

1. Use a single named tick for “the departure / witnessed departure” and make the excerpt say the archivist was at the harbor at that moment; do not imply within-tick ordering that the timeline cannot encode.
2. Cite the witness event to an invented registry excerpt that explicitly records the event and place, and cite the departure event to the invented courier excerpt. If the intended point is that the archivist saw Mira leave (not merely that both occupied the harbor), the source wording must directly support the seeing/recording claim. IDs in `source_id` alone do not establish that correspondence.
3. Put invented excerpt text in an appropriate separate artifact/source description or claim text only if the fixture design allows it; do not silently assume `sources.json` currently supports excerpt fields. Ensure every new assertion has an explicit source mapping and is still a fictional author-created account.
4. Keep dependency edges for actual sequence only (e.g. departure before arrival). Same-tick co-presence is a synchronization convention, not a causal edge. If the narrative requires a strict order between witness activity and departure, assign different ticks and order them explicitly instead of treating equal ticks as ordered.

Scope: this is a map of current checker behavior and a modeling recommendation. It does not establish fictional canon, prose truth, or source authenticity.
