# Round 6 fixture scout — cited transfer-chain pair

## Observed repository evidence

- The active fixture schema is five JSON arrays. `relations.json` rows currently require `from`, `to`, `type`, and `source_id`; `timeline.json` rows require `id`, `tick`, `entity_id`, `place_id`, `depends_on`, `description`, and `source_id` (`corpus/fixtures/check_bible.py`, `FIELDS`). There is no transfer/item-holder field or transfer checker today.
- The clean fixture has item `seal` (`entities.json`, `consistent/`) with cited claim “The seal accompanied Mira.” and a cited `mira -> seal` `carries` relation (`consistent/relations.json`). This demonstrates accompaniment/carrying, not explicitly acquisition or transfer history; it should not be silently treated as an initial ownership record.
- `sources.json` lists two in-world fictional records: `courier-log` (a personal log) and `archive-ledger` (a municipal record that “records movements, not omniscient truth”). The checker only resolves `source_id` against that list; it does not check whether source text supports the asserted record (`check_bible.py`, `source()`; `fixtures/README.md`, citation boundary).
- Current regression observations are preserved in `corpus/live/runs/20261012T164316Z/`: clean `consistent` exits 0 with `CLEAN`; `contradictions` exits 1 with the existing three relation/timeline violations; `ally-reciprocal` exits 0; `ally-one-way` exits 1 with its missing-sourced-reciprocal violation; `r5-invalid-citation` exits 1 with unknown source. The README and round-5 log describe the other malformed-input cases and their stored outputs.

## Recommended fixture pair (not implemented)

Use two new sibling fixture directories copied from `consistent/`, preserving all five baseline tables and changing only the explicit transfer data. Avoid deriving a first holder from `carries`: include an explicit, source-cited acquisition/initial-holder record for `seal` by `mira`, followed by two explicit cited transfers. Keep the same record shape, IDs, sources, ticks, and all other data in both siblings; change only the predecessor (`from`) on the second transfer:

| Record | Valid sibling | Broken sibling |
|---|---|---|
| Initial holder | `seal` acquired/held by `mira`, cited to `courier-log` | identical |
| Transfer 1 | `seal`, `mira` → `harbor`, tick 3, `archive-ledger` | identical |
| Transfer 2 | `seal`, `harbor` → `tower`, tick 4, `archive-ledger` | `seal`, `mira` → `tower`, tick 4, `archive-ledger` |

The valid case has a cited predecessor matching the immediately prior holder and should pass. The broken case must produce one local chain-break diagnostic at transfer 2: expected prior holder `harbor`, asserted predecessor `mira`. Since both fixtures retain all existing clean data, the new rule must not interpret the old `carries` relation as a transfer or fail a bible merely because it has no explicit provenance records. The proposed field/table and acquisition convention are design recommendations, not existing schema or observed behavior; implementation should choose one clear representation and document it. Citation IDs can resolve, but this fixture cannot prove that the fictional source actually supports the transfer statement.

## Unchanged regression cases

Retain and replay existing fixtures without edits: `consistent`, `contradictions`, `ally-reciprocal`, `ally-one-way`, `contradictions-ledger-malformed`, and all `r5-*` cases (`r5-missing-file`, `r5-invalid-json`, `r5-wrong-top-level`, `r5-row-shape`, `r5-invalid-citation`). Preserve the exact prior outcomes, including existing diagnostic text where output preservation is part of the round claim. The raw observed round-5 outputs are in `corpus/live/runs/20261012T164316Z/` for clean, contradictions, reciprocal/one-way, and five malformed cases; round-3/2 outputs are available in their earlier `corpus/live/runs/` snapshots. Do not edit checker or fixtures in this scout lane.
