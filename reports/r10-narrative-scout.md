# Round 10 narrative scout — Mira route witness extension

## Observations

- The round-10 declaration in `.shokunin/lore/LOG.md` asks for a separate cited micro-bible that preserves the existing route and adds an archivist/registry witness to Mira’s departure.
- `.shokunin/lore/corpus/fixtures/consistent/` currently has four entities (`mira`, `harbor`, `tower`, `seal`), one `carries` relation, and two events: `departure` (Mira at harbor, tick 1) and `arrival` (Mira at tower, tick 2, depending on `departure`).
- Its `sources.json` defines `courier-log` as a first-person fictional route log and `archive-ledger` as a fictional municipal record that records movements, not omniscient truth. The files do not contain excerpt text for either record.
- `.shokunin/lore/corpus/fixtures/check_bible.py` requires each new source/entity/relation/event to use its defined fields and checks source-ID resolution, entity endpoints, place kind, and event ordering/occupancy. It does not test whether prose supports a claim or whether a source is true.

## Recommendation (not existing canon or observed fact)

Build a separate fixture by copying the clean Mira route and adding one fictional source, one registrar entity, one explicitly sourced relation, and one registrar event. Preserve all existing rows unchanged. This gives the second perspective a specific institutional act and a traceable record rather than merely adding an entity or repeating the departure sentence.

Proposed source row:

```json
{
  "id": "registrar-copy",
  "title": "Sella’s Harbor Register carbon, year 12",
  "kind": "fictional handwritten register excerpt",
  "reliability_note": "authored in-world excerpt for this fixture; Sella records what she entered, not omniscient truth"
}
```

Proposed excerpt, labeled as invented fixture text (not recovered evidence):

> First bell, year 12: I, Sella, registrar at Lantern Harbor, entered that courier Mira departed for North Tower carrying the blue seal. I kept the carbon in the harbor register.

Proposed additions and exact assertion-to-excerpt mapping:

| Proposed row/field | Exact assertion | Supporting excerpt text |
|---|---|---|
| `entities.json`: new `registrar` entity `name` | The character is named Sella. | “I, Sella” |
| `entities.json`: `registrar.first_appearance` = `registrar-copy`; claim | Sella is a registrar at Lantern Harbor. | “registrar at Lantern Harbor” |
| `relations.json`: `registrar` → `mira`, type `records_departure`, `source_id: registrar-copy` | Sella records Mira’s departure. | “I … entered that courier Mira departed” |
| `timeline.json`: new event `registry-entry`, tick 1, `entity_id: registrar`, `place_id: harbor`, `depends_on: []`, `source_id: registrar-copy` | At first bell, Sella enters a register record of Mira’s departure for North Tower with the blue seal. | “First bell, year 12”; “entered that courier Mira departed for North Tower carrying the blue seal” |
| `timeline.json`: event description | Sella keeps the carbon in the harbor register. | “I kept the carbon in the harbor register.” |

For the entity row, use a claim statement such as `Sella is a registrar at Lantern Harbor.` with `source_id: registrar-copy`; the first-appearance citation also uses `registrar-copy`. For the event, use an explicit description such as `Sella enters a register entry that Mira departed for North Tower carrying the blue seal, and keeps the carbon.` The event’s placement at harbor and tick 1 align the authored scene with the existing departure, without claiming that the checker verifies witness accuracy. The proposed excerpt says “first bell” rather than assigning tick 1; the fixture’s tick is an ordering convention, not a converted clock time.

This is intentionally limited to one new witness, one sourced relationship, one event, and one short excerpt. Do not imply the new excerpt validates the pre-existing `courier-log` or `archive-ledger` claims; it is authored fiction that independently asserts the overlap. Keep the source’s reliability note explicit, and leave contradictions/reporting policy unchanged.
