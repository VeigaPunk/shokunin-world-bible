# Round 25 scribe: bounded endpoint decision table

**Decision scope:** fixture diagnostics for relation endpoint ID multiplicity only. The declared move probes `to` with a duplicate-ID/matched unique-ID pair (and both endpoints only if that paired case is actually warranted). It does not alter checker behavior or settle what the cited fictional text establishes.

| Count of valid entity rows with endpoint ID | Bounded diagnostic expectation | What can be concluded |
|---|---|---|
| 0 | Existing dangling endpoint finding | No valid entity row resolves this ID in the fixture. |
| 1 | No ambiguity finding | This endpoint ID is unique among admitted entity rows. |
| >1 | Relation-local ambiguous entity finding at that endpoint | The ID does not select one entity row; no row is chosen. |

| Probe | Required comparison | Pass condition |
|---|---|---|
| Duplicate `to` | Relation has a duplicated target ID; matched control has unique target and otherwise matched cited relation | Duplicate case yields `.to` ambiguity; control does not. Any duplicate-entity error remains separate. |
| Both endpoints duplicated (conditional) | Include only if a minimal paired fixture can independently exercise both sides | One ambiguity finding per endpoint; no extra semantic inference. |
| Regression | Replay the declared baseline of 73 fixture outputs and 364 prior JSON paths | All 73 prior outputs and all 364 old JSON paths remain byte-identical. |

**Evidence.** Checker admits structurally valid entity rows into `data` (`.shokunin/lore/corpus/fixtures/check_bible.py:32-43`), builds a last-row entity index while reporting duplicate IDs (`:45-51`), and already counts IDs among admitted rows (`:119-121`). Relation checks iterate both `from` and `to`, emitting dangling for zero indexed matches and ambiguity when count exceeds one (`:123-130`). The baseline `consistent` relation has `to: seal` (`.shokunin/lore/corpus/fixtures/consistent/relations.json:2-7`) and one `seal` entity (`consistent/entities.json:39-49`). Existing r12 demonstrates a duplicated `mira` at entity rows beginning lines 2 and 51 and uses it only as `from` (`r12-ambiguous-actor/entities.json:2-12,51-61`; `relations.json:2-7`); it does not prove the `to` case. The round declaration records the 73-fixture/364-path regression bounds (`.shokunin/lore/LOG.md: last Round 25 declaration`).

**Risks / bounds.** A source citation validates only the fixture's source-ID linkage, not real source-text truth or a canonical relation. The matched pair should vary only entity-ID multiplicity/endpoint placement needed for the probe; otherwise a changed output cannot be attributed narrowly. Do not select a duplicate row, add relationship truth, or describe a game mechanic. No checker/fixture edits are part of this scribe task; coverage is not established until non-author replay confirms the declared conditions. Depth and calibration are outside this single coverage move and must not be claimed improved.
