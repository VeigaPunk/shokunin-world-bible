# Round 33 schema scout — minimal cited character/event

## Minimal shape

Use the existing five-table shape; do not add schema fields or a relation. Copy `consistent/` unchanged into a separate fixture, then append one source, one character entity and one timeline row. This is the smallest existing-schema representation of the proposed observation: `entities` rows already carry `id`, `kind`, `name`, `first_appearance`, and source-cited claims (`corpus/fixtures/consistent/entities.json:3-11`); events already carry `id`, local `tick`, `entity_id`, `place_id`, `depends_on`, `description`, and `source_id` (`corpus/fixtures/consistent/timeline.json:3-10`).

Suggested added records:

- `sources.json`: `{ "id": "tarin-note", "title": "Tarin’s harbor note, year 12", "kind": "fictional first-person note", "reliability_note": "Newly authored fictional excerpt for this fixture; Tarin reports an observation, not omniscient truth." }`. The precedent makes source-ID/title/kind/note explicit and marks the text invented, not recovered (`corpus/fixtures/r10-registry-witness/sources.json:15-19`; `corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md:1-5`).
- `entities.json`: `{ "id": "tarin", "kind": "character", "name": "Tarin", "first_appearance": "tarin-note", "claims": [{"statement":"Tarin reports seeing Sella place an unlabeled paper envelope on the Lantern Harbor registry desk.","source_id":"tarin-note"}] }`. This follows the minimal character row and required cited claim pattern (`corpus/fixtures/r10-registry-witness/entities.json:50-61`). `first_appearance` is a source index in this fixture, not a claim about historical first appearance (r23 explicitly warns of this convention: `corpus/fixtures/r23-note-class/witnessed-absence-clause-map.md:18`).
- `timeline.json`: `{ "id":"tarin-envelope-observation", "tick":3, "entity_id":"tarin", "place_id":"harbor", "depends_on":[], "description":"Tarin reports seeing Sella place an unlabeled paper envelope on the Lantern Harbor registry desk.", "source_id":"tarin-note" }`. Event field pattern follows baseline (`corpus/fixtures/consistent/timeline.json:3-10`). Tick 3 and no dependency avoid asserting ordering against equal-tick Sella registry row; ticks are invented local sequence labels, not absolute dates (`corpus/fixtures/README.md:23-25`).

The excerpt should be a single first-person sentence, e.g. “I, Tarin, saw Sella place an unlabeled paper envelope on the Lantern Harbor registry desk.” Map “I, Tarin” → speaker/entity; “Sella place” → reported action and named participant; “unlabeled paper envelope” → description only; “Lantern Harbor registry desk” → location. No envelope entity or contents assertion is needed. Clause-by-clause manual maps are precedent, not checker behavior (`corpus/fixtures/r23-note-class/witnessed-absence-clause-map.md:1-3,10-16`).

## Risks / bounds

- The schema can cite an invented source ID but cannot establish that excerpt text entails the row. Round 10 explicitly limits checking to structure/reference identity, not entailment, corroboration, witness honesty or canon (`LOG.md:140-141`); round 23 likewise says checker does not read the manual map (`LOG.md:345-347`). Require a non-author to quote the exact sentence against each assertion.
- Do not infer envelope contents, ownership, recipient, destination, Blue Seal connection, motive, or causal role. The proposal supports only Tarin’s reported sighting of Sella placing an unlabeled envelope; it does not establish the world fact independently.
- Avoid a `saw/observed` relation: no such relation is needed in the existing schema, and adding one expands assertions beyond the one event. Do not add an envelope entity merely to encode an object mentioned in the event.
- Character `first_appearance` means indexed source in these examples, not globally earliest appearance; do not present it as chronology.

## Falsifiable check

On a separate `consistent`-derived fixture, the checker should exit 0 with exactly one new `sources` row, one new `entities` row and one new `timeline` row; all additions cite resolvable `tarin-note`, actor/place resolve uniquely, and tick/dependencies satisfy the local timeline rules. A non-author reviewer must be able to map every positive clause above to the exact invented sentence and reject any claim about envelope contents/owner/destination/Blue Seal. The new fixture fails this check if it needs another assertion to make the observation intelligible, if any clause lacks direct wording support, or if it implies an envelope fact not in the sentence. This tests a bounded authored-fiction observation class, not canon truth or real-world evidence.
