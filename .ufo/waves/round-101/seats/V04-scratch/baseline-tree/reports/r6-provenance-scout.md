# Round 6 provenance scout — observed schema and minimal proposal

## Observed in the repository

- The concrete fixture schema is implemented in `.shokunin/lore/corpus/fixtures/check_bible.py`: `FIELDS` requires entity `{id, kind, name, first_appearance, claims}`, relation `{from, to, type, source_id}`, timeline `{id, tick, entity_id, place_id, depends_on, description, source_id}`, and source `{id, title, kind, reliability_note}`. The checker indexes entity IDs and validates relation endpoints and source references; timeline ticks/dependencies are checked for order/inversion. No schema field currently encodes a handoff or acquisition.
- `.shokunin/lore/corpus/fixtures/consistent/entities.json` has item `seal` (`kind: item`), first appearance `courier-log`, and a sourced claim “The seal accompanied Mira.” Its `relations.json` has `mira -> seal`, type `carries`, source `courier-log`. These are sourced assertions, but neither carries a tick nor gives previous/current holders as an ordered chain.
- `consistent/timeline.json` orders Mira’s departure (tick 1) and arrival (tick 2), with event entity/place and source. It does not encode an item movement. `sources.json` gives the cited in-world documents; source IDs are the citation mechanism.
- The checker validates `claims` as a list but does not require provenance subfields within an item claim. In the fixture, prose is therefore not structured acquisition/transfer evidence. `FIELDS` is the explicit required-field map; unrelated extra object properties are not generally rejected, and there is no top-level provenance file in the current fixture layout.

## Recommendation (not observed schema)

For a small, explicit and opt-in representation, add an optional `provenance` list to **item entities only**. Each record should contain `{tick, from_holder, to_holder, source_id}`; holder values are entity IDs, and `from_holder: null` marks an acquisition/origin record (the initial holder is `to_holder`). Later records are transfers. Example:

```json
{
  "tick": 1,
  "from_holder": null,
  "to_holder": "mira",
  "source_id": "courier-log"
}
```

For each item with a nonempty list, order records by `tick` and require each later record’s `from_holder` to equal the immediately preceding record’s `to_holder`; require nonnegative integer ticks, existing holder entity IDs, and a resolvable in-world `source_id` per record. A mismatched predecessor is a chain break at that record, not a reason to rewrite or resolve history. Keep the field optional: absent/empty provenance means “not represented,” not an error, and must not be inferred from claims, `carries` relations, or timeline prose. If conflicting sources assert incompatible holdings, surface that as conflict evidence rather than picking a winner. A valid chain establishes only that the structured, cited records link; it does not prove canon truth or exhaust all provenance semantics.

This is smaller than a new top-level ledger because it adds no required file and keeps provenance on the item it concerns. It is more expressive than reusing `relations.json` (`from/to/type/source_id` lacks time and an explicit acquisition) or the current timeline row (which has time/source but no item-holder transition). The `tick` convention should be aligned with the existing timeline integer tick; uniqueness/tie behavior for same-item, same-tick records should be specified before implementation (e.g. reject ambiguous ties rather than invent ordering).
