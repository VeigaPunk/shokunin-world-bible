# Round 14 claim scout — r10 registry witness

Scope: read-only inventory of the existing JSON rows in `.shokunin/lore/corpus/fixtures/r10-registry-witness/`. This maps each explicit assertion/cited event to its existing `source_id`; it does **not** establish that any assertion is true. The current source registry contains metadata for `archive-ledger` and `courier-log`, but supplies no excerpt text for either. Therefore no clause-level support can presently be checked for those IDs. The already supplied `registrar-copy-excerpt.md` is the only excerpt and is explicitly invented fixture text.

## Exact existing claims and cited source IDs

Paths below are relative to the fixture directory. JSON strings are quoted as stored.

| JSON path | Exact assertion / event text | Existing source ID | Wording needed for a proposed excerpt/map (recommendation, not fact) |
|---|---|---|---|
| `entities.json` `$[0].first_appearance` | Mira first appears | `courier-log` | Recommend a bounded log clause identifying Mira / her appearance. |
| `entities.json` `$[0].claims[0].statement` | “Mira carried the blue seal.” | `courier-log` | Recommend wording that Mira carried the blue seal. |
| `entities.json` `$[1].first_appearance` | Lantern Harbor first appears | `archive-ledger` | Recommend a bounded registry clause naming Lantern Harbor. |
| `entities.json` `$[1].claims[0].statement` | “Lantern Harbor has a registry.” | `archive-ledger` | Recommend wording that the harbor has a registry. |
| `entities.json` `$[2].first_appearance` | North Tower first appears | `archive-ledger` | Recommend a bounded registry clause naming North Tower. |
| `entities.json` `$[2].claims[0].statement` | “North Tower has a watch bell.” | `archive-ledger` | Recommend wording that North Tower has a watch bell. |
| `entities.json` `$[3].first_appearance` | Blue Seal first appears | `courier-log` | Recommend a bounded log clause naming the Blue Seal. |
| `entities.json` `$[3].claims[0].statement` | “The seal accompanied Mira.” | `courier-log` | Recommend wording that the seal accompanied Mira. Do not silently upgrade “accompanied” to ownership or carriage unless the separately cited claim says so. |
| `relations.json` `$[0]` (`mira` → `seal`, type `carries`) | Mira carries the seal | `courier-log` | Recommend wording explicitly supporting the carries relation. This is distinct from, though compatible with, “accompanied Mira.” |
| `timeline.json` `$[0].description` | “Mira departs the harbor.” (tick 1; `entity_id=mira`, `place_id=harbor`) | `courier-log` | Recommend wording supporting this departure and harbor location. |
| `timeline.json` `$[1].description` | “Mira reaches the tower.” (tick 2; `entity_id=mira`, `place_id=tower`; depends on `departure`) | `courier-log` | Recommend wording supporting arrival/reaching North Tower. The JSON dependency also orders this event after `departure`; no extra claim about elapsed duration is needed. |

## Already covered separately; do not backfill

These rows cite `registrar-copy`, not either source being investigated. Their wording is present in `registrar-copy-excerpt.md`:

- `entities.json` `$[4].first_appearance` and `$[4].claims[0].statement`: Sella first appears; “Sella is a registrar at Lantern Harbor.”
- `relations.json` `$[1]`: Sella records Mira’s departure.
- `timeline.json` `$[2].description`: at first bell Sella records seeing Mira leave; at Mira’s request she leaves the registry destination blank and keeps the carbon.

That excerpt is fictional fixture text, not recovered evidence and not independent corroboration. In particular, it expressly leaves Mira’s destination blank. Do not use it to assert that Sella’s registry states a destination, or to fill in facts assigned to `courier-log`/`archive-ledger`.

## Source-ID inventory and boundary

- `sources.json` `$[0]`: `archive-ledger` (“Lantern Harbor Registry, year 12”), described as a fictional municipal record recording movements, not omniscient truth. It is cited by the harbor and tower entity first appearances/claims above. No supplied excerpt text currently supports them.
- `sources.json` `$[1]`: `courier-log` (“Courier Mira’s Route Log, year 12”), described as a fictional first-person account. It is cited by Mira and seal first appearances/claims, the carries relation, and the two route events above. No supplied excerpt text currently supports them.

Recommendations in the table are a coverage checklist for newly authored fictional excerpts only. They are not facts observed in either missing source, evidence of source contents, or a claim that the JSON is canonically true. Preserve existing JSON rows and source IDs; do not represent excerpts as recovered originals or independent corroboration.
