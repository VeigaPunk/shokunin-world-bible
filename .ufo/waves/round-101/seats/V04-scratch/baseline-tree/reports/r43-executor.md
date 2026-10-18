# Round 43 executor — Jorin/Vela sighting

## Artifact and scope

Created `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/` as a clone of `r41-vela-direct-bell`. Every inherited file is byte-identical except `sources.json`, `entities.json`, and `timeline.json`, where the complete inherited row arrays are exact value prefixes and one requested row was appended to each. Inherited `relations.json` and `contradictions.json` are byte-identical; no relation or ledger pair was added. The inherited stale `vela-clause-map.md` remains byte-for-byte unchanged. Added only `jorin-note-excerpt.md` and `jorin-clause-map.md` beyond those JSON appends. Inventory: 12 inherited files, 14 candidate files; only the two named markdown files are additional files.

The Jorin source is marked newly authored, in-world fictional and unverified. The excerpt self-identifies Jorin as registrar, places him at the Lantern Harbor registry doorway, attributes to him seeing Vela on the east steps during what he called Bell-7, and states he did not see who, if anyone, struck a bell. One `jorin` character has exactly one source-cited attributed claim; one `jorin-vela-sighting` event has tick 3 editorial, actor `jorin`, place `harbor`, empty dependencies, a limited attributed description, and source `jorin-note`. The clause map distinguishes Jorin’s doorway scene from Vela’s reported location, states the conditional overlap and unverified occasion/bell/absence limits, and flags the inherited r41 Vela map as stale. No canon or novelty determination is made here.

## Checker runs

Executed from repository root with `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-path>`. Raw captured stdout/stderr and status:

### r41-vela-direct-bell
- stdout: `b'CLEAN: schema, citations, relations, timeline; 0 violations\n'`
- stderr: `b''`
- status: `0`

### r43-jorin-vela-sighting
- stdout: `b'CLEAN: schema, citations, relations, timeline; 0 violations\n'`
- stderr: `b''`
- status: `0`

These checker results establish structural cleanliness only, not excerpt entailment, source authenticity, truth, shared occasion, chronology, bell occurrence, absence, canon, rights, or AI-training permission. No baseline 94-fixture/469-JSON replay was performed by this scoped executor.
