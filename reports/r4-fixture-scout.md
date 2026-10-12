# Round 4 fixture scout — exact display-name collision

## Observed evidence

- `.shokunin/lore/corpus/fixtures/check_bible.py` declares five required JSON sections in `FIELDS`: `sources`, `entities`, `relations`, `timeline`, and `contradictions`. Its entity schema requires `id`, `kind`, `name`, `first_appearance`, and `claims`; it checks entity IDs for duplicates but currently has no displayed-name check.
- `.shokunin/lore/corpus/fixtures/consistent/entities.json` is a positive precedent: records have distinct display names, and both first-appearance and claim citations resolve to the source IDs in `consistent/sources.json`.
- `.shokunin/lore/corpus/fixtures/consistent/{relations,timeline,contradictions}.json` show empty/minimal valid sections; in particular `contradictions.json` is `[]`. `.shokunin/lore/corpus/fixtures/README.md` says the fifth section is required, even for a bible with no asserted contradiction.
- `.shokunin/lore/corpus/fixtures/contradictions/entities.json` demonstrates that different entity IDs carry independent names and in-world citations. Reuse this schema, not its unrelated timeline conflict.

## Recommendation: smallest useful positive/negative pair

Add two isolated fixture directories, for example `name-unique/` and `name-duplicate/`. Each must contain **all five** required JSON files. Keep the source, relations, timeline, and contradiction tables identical across the pair; use one fictional source and empty arrays for relations, timeline, and contradictions. This keeps the sole intended difference in `entities.json` and makes the name rule outcome unambiguous.

Use a minimal source record such as `{"id":"registry","title":"Lantern Harbor Registry, year 12","kind":"fictional municipal record","reliability_note":"in-world fiction; records named residents"}` in both `sources.json` files. Give each entity `first_appearance: "registry"` and a nonempty `claims` array whose `source_id` is `registry` (e.g. statement `"The registry lists this resident."`). These are invented in-world citations, not real-world claims.

- **Positive `name-unique/entities.json`:** two valid records, e.g. `{ "id":"mira", "kind":"character", "name":"Mira", ...cited fields... }` and `{ "id":"niko", "kind":"character", "name":"Niko", ...cited fields... }`. Expect clean/exit 0.
- **Negative `name-duplicate/entities.json`:** same two otherwise-valid records and distinct IDs, but set both `name` values to exactly `"Mira"`. Keep both independently cited. Expect one name-local diagnostic identifying both entity IDs/locations and exit 1; do not merge, rename, or choose a canon winner.

The files `relations.json`, `timeline.json`, and `contradictions.json` should each contain `[]` in both fixtures. Keep `sources.json` byte-identical across the pair. Avoid adding a disambiguation field: the round claim is exact duplicate display names, not aliases, case folding, or exceptions.

## Replay and scope

Run the same checker command against both fixture directories from the repository root. The discriminating evidence is positive exit 0 versus negative exit 1 with only the negative name-collision diagnostic; confirm all five files are present in each. If the checker reports other issues, fix fixture citations/schema rather than broadening the rule. Existing `consistent`, `contradictions`, and alliance fixture outcomes should also remain as regressions, but are not substitutes for this paired test.

This is a recommendation only. I did not create or edit fixture files, checker code, or shared documentation.
