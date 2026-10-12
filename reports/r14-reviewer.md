# Round 14 independent reviewer — excerpt / assertion audit

## Scope and raw replay

I inspected the raw fixture at `.shokunin/lore/corpus/fixtures/r10-registry-witness/` (all five JSON files and all three excerpt files), the executor's clause map, and the round-14 LOG declaration/clarification. I replayed the fixture directly:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokuhin/lore/corpus/fixtures/r10-registry-witness
CLEAN: schema, citations, relations, timeline; 0 violations
```

(The actual command used the repository path `.shokunin/lore/corpus/fixtures/r10-registry-witness`.) This is a structural checker result; it does not inspect Markdown excerpts or establish prose support. I make no claim about the 28-fixture replay from this single-fixture run.

## Clause-by-clause assertion audit

All quoted excerpt clauses below are verbatim. “Corresponds” means only that newly authored prose was tailored to the existing fixture row; it is not independent evidence.

| Existing assertion (raw JSON selector) | Corresponding supplied wording | Assessment / limit |
|---|---|---|
| `entities.json` `$[0].first_appearance` = `courier-log` | Courier: “I am Mira.” | In-fiction narrator labels herself Mira. Does not establish identity, literal historical first appearance, or source independence. `first_appearance` is a source/index assignment here. |
| `entities.json` `$[0].claims[0]`: “Mira carried the blue seal.” (`courier-log`) | “At local tick 1, I leave Lantern Harbor carrying the blue seal.” | Corresponds to carrying at departure. No ownership or custody before/after the stated moment. |
| `entities.json` `$[1].first_appearance` = `archive-ledger`; `$[1].claims[0]`: “Lantern Harbor has a registry.” | Archive: “Lantern Harbor has a registry.” | Exact wording correspondence for the claim; source assignment is not proof of historical first appearance. |
| `entities.json` `$[2].first_appearance` = `archive-ledger`; `$[2].claims[0]`: “North Tower has a watch bell.” | Archive: “North Tower has a watch bell.” | Exact wording correspondence; same first-appearance limit. |
| `entities.json` `$[3].first_appearance` = `courier-log`; `$[3].claims[0]`: “The seal accompanied Mira.” | “I am Mira.” + “At local tick 1, I leave Lantern Harbor carrying the blue seal.” | The passage depicts the seal accompanying the narrator at tick 1; it does not establish origin or broader duration. |
| `entities.json` `$[4].first_appearance` = `registrar-copy`; `$[4].claims[0]`: “Sella is a registrar at Lantern Harbor.” | Existing registrar excerpt: “At first bell at Lantern Harbor, I, Sella, registrar there, recorded seeing Mira leave.” | Supported only by the pre-existing, explicitly invented excerpt—not either new excerpt. Source assignment is not literal historical-first proof. |
| `relations.json` `$[0]`: `mira` carries `seal` (`courier-log`) | “At local tick 1, I leave Lantern Harbor carrying the blue seal.” | Corresponds to carrying then; does not imply legal possession or extended custody. |
| `relations.json` `$[1]`: Sella `records_departure` of Mira (`registrar-copy`) | Existing registrar excerpt: “... recorded seeing Mira leave.” | Existing excerpt wording corresponds. Not a new excerpt assertion; no destination established. |
| `timeline.json` `$[0]`: departure, tick 1, Mira, harbor (`courier-log`) | “At local tick 1, I leave Lantern Harbor carrying the blue seal.” | Explicitly states the row's tick and place/departure. Does not state a route. |
| `timeline.json` `$[1]`: arrival, tick 2, Mira, tower (`courier-log`) | “At local tick 2, I reach North Tower.” | Explicitly states the row's tick and endpoint. No travel duration, path, or intervening event. |
| `timeline.json` `$[2]`: registry entry, tick 1, Sella, harbor (`registrar-copy`) | Existing registrar excerpt: “At first bell at Lantern Harbor, I, Sella, registrar there, recorded seeing Mira leave. At Mira’s request, I left the registry destination blank and kept the carbon.” | Existing excerpt maps to the entry, observation, and blank destination. **“First bell” is not stated to equal fixture tick 1**; the JSON tick is not a conversion proved by that phrase. Blank destination remains unknown. |

The new archive excerpt has no corresponding relation or timeline rows; appropriately, it asserts neither Mira's destination nor chronology, Sella's omission, or corroboration. The courier excerpt contains only narrator identification, tick-1 departure/carrying, and tick-2 arrival. I found no new event, intermediate route, relation, uncertainty qualification, or other substantive world detail. The executor's map is materially accurate when read with its stated boundaries, although its “Supports” column should be understood as editorial wording correspondence, not evidentiary validation.

## Axis judgment

- **Depth: unchanged.** These excerpts make existing row assertions easier to read as in-world prose, but all their lore content is a restatement of those rows. The route remains only two already-asserted endpoints and their ticks. New files, clause mapping, and clearer prose are useful traceability/documentation, not a richer account or added lore. The post-scout clarification itself correctly says not to count restatement as depth.
- **Coverage: unchanged.** No new rule class, assertion type, or checker behavior was added.
- **Calibration: unchanged, narrowly.** The explicit “newly authored ... (not recovered evidence)” labels, source-ID convention, existing source reliability limits, and tick/first-appearance caveats reduce the risk of mistaking backfilled prose for independent evidence. They do not make the excerpts independent. If later presented without these caveats as source validation, that would harm calibration; that is not what the reviewed files currently say.

**Recommendation:** do not admit this as a depth axis improvement. The checker result is clean but is not a prose review or reason to change that verdict. This is a bounded legibility/traceability improvement only; no canon truth or independent corroboration has been demonstrated.
