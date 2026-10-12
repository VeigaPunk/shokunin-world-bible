# Round 6 simplifier: optional explicit item-transfer records

## Observed in the repository

- `.shokunin/lore/corpus/fixtures/check_bible.py` currently requires five JSON arrays: `sources`, `entities`, `relations`, `timeline`, and `contradictions` (`FIELDS`). There is no item-transfer section or holder field.
- The clean bible's `seal` item in `corpus/fixtures/consistent/entities.json` has a cited first appearance and the claim “The seal accompanied Mira.” A separate `relations.json` row says Mira `carries` the seal, with `courier-log` as source. Neither row establishes a transfer sequence or a prior holder.
- Existing `timeline.json` records cite events about Mira's location. The checker uses ticks/dependencies for ordering and occupancy, but does not derive item possession from descriptions, character presence, or relations.
- The checker currently reports missing required files as input errors. Making transfer data optional therefore means an absent transfer file must be explicitly exempted from required-table loading; otherwise unrelated existing bibles fail.

## Recommendation (not implemented)

Use one optional `item_transfers.json` array, loaded as empty when the file is absent. Do not change the existing five-table contract. Each explicit record is a cited assertion with only:

- `item_id`: existing entity whose kind is `item`;
- `from_holder` and `to_holder`: existing entity IDs (not inferred from prose);
- `tick`: nonnegative local integer ordering records for that item;
- `source_id`: resolvable in-world source.

Validate only chains represented by this table. For each item's records in tick order, require each later record's `from_holder` to equal the previous record's `to_holder`; report a local chain-break at the later record otherwise. Do not require an item to have any transfer records, and do not infer a starting holder from `first_appearance`, claims, `carries` relations, timeline descriptions, or gameplay.

A transfer list alone cannot establish whether its first `from_holder` is the item's true prior holder. To avoid claiming that it does, treat the first cited row as the explicit assertion of that transfer's prior holder, and check only continuity between successive recorded transfers. If the round's stronger phrase “from a cited acquisition/previous transfer” is mandatory, add an explicit acquisition record (item, holder, tick, source) as the chain seed; then require a transfer's first predecessor to match that acquisition. That is semantically stronger but adds a record kind and validation rule, so it is not the minimal option.

## Boundary

This is a schema recommendation, not observed checker behavior or canon. No files other than this report were changed. This convention checks consistency among explicit cited records; it does not prove a source's truth, complete provenance, or possession between records.
