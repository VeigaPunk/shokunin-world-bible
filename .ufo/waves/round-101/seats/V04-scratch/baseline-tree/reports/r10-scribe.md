# Round 10 scribe — bounded source-to-claim table and README wording

## Observations (current baseline)

- The round-10 declaration in `.shokunin/lore/LOG.md` calls for a separate fictional cited micro-bible, adding an archivist/registry witness to Mira’s departure while preserving the original clean route. It requires every added entity claim, relation, and event to carry an in-world source ID and a labeled invented excerpt; it explicitly limits the goal to depth, not checker verification of prose or canon truth.
- `.shokunin/lore/corpus/fixtures/consistent/sources.json` defines `courier-log` as Mira’s fictional first-person route log and `archive-ledger` as a fictional municipal record that records movements but is not omniscient. It contains metadata only, not excerpt text.
- In `.shokunin/lore/corpus/fixtures/consistent/entities.json`, Mira’s “carried the blue seal” claim points to `courier-log`; the harbor registry and North Tower watch bell claims point to `archive-ledger`; the Blue Seal’s “accompanied Mira” claim points to `courier-log`.
- `.shokunin/lore/corpus/fixtures/consistent/relations.json` has Mira `carries` the seal, cited to `courier-log`.
- `.shokunin/lore/corpus/fixtures/consistent/timeline.json` cites `courier-log` for both Mira’s departure from Lantern Harbor (tick 1) and arrival at North Tower (tick 2), with arrival depending on departure.
- `.shokunin/lore/corpus/fixtures/README.md` already says citations resolve to fictional records, checker validates citation identity rather than textual support, and entries are invented. `.shokunin/lore/corpus/README.md` inventories the corpus. No round-10 fixture or round-10 report artifact was present when inspected.

## Bounded decision table (recommendation for a future authored fixture)

| Proposed assertion / row | Proposed in-world witness | Textual check a non-author can make | Bound / do not infer |
|---|---|---|---|
| Mira departs Lantern Harbor (existing `departure` event) | `courier-log`, with the existing event excerpt | Route-log excerpt explicitly says Mira departed Lantern Harbor; compare entity/place and event description | First-person report, not independently established fact |
| Registry witness of the departure (new event or explicitly modeled witness assertion) | A uniquely identified registry excerpt/source, e.g. a new `registry-entry` source rather than silently reusing metadata-only `archive-ledger` | Excerpt identifies Mira and the departure/movement from Lantern Harbor; compare each asserted field against the row | Registry corroborates only what its text states; do not claim omniscience or infer motive |
| New archivist/registrar entity claim, if needed | Same registry source only when its excerpt identifies the person/role | A specific sentence identifies that named role/person and the relevant claim | Do not add an entity merely to increase row count; avoid unsupported biography |
| Any new relation connecting witness/record to Mira or departure | Cite the source whose excerpt states that relation | Check both endpoints and relation meaning against the excerpt | Do not infer friendship, employment, causation, or agreement from co-appearance |
| Existing `arrival` event and `carries` relation | Keep existing `courier-log` citations unless authored excerpt supports a changed citation | Compare the existing cited assertions with their invented route-log excerpt | Do not change or “upgrade” old claims based only on a second perspective about departure |

The source IDs and excerpt contents in this table are a proposal, not observations or established fixture facts. Prefer the smallest coherent addition: one registry record explicitly recording the same departure, and only the minimum witness entity/relation rows required by the chosen schema. If source text and a row disagree or are silent, report the mismatch or narrow/remove the assertion; never resolve it by choosing canon.

## Suggested README wording (recommendation; not applied)

For a round-10 fixture section in `.shokunin/lore/corpus/fixtures/README.md`, append wording along these lines after the fixture’s run instructions and actual paths are known:

> The round-10 cited fixture is a separate fictional example; the original `consistent/` route remains unchanged. Its source excerpts are invented in-world text included so a reader can compare the cited assertions with what each record actually says. A citation identifies a source row; it does not prove that the excerpt is true, complete, unbiased, or canon. The route log is first-person, and the registry supports only the movement details stated in its excerpt. Where an excerpt does not support an assertion, that assertion is not established by this example. The checker checks structure and source-ID resolution, not prose meaning, corroboration, historical truth, or game mechanics.

Use wording consistent with the actual excerpts and fixture paths; do not promise corroboration unless the two excerpts independently state the same bounded detail. Do not alter corpus inventory until an artifact exists. The README recommendations above were not written to shared documentation.
