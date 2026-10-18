# Round 71 schema scout — minimal r43-derived fixture

## Scope and baseline

This is a schema/placement map only. I read the Round 71 declaration in `.shokunin/lore/LOG.md` (Round 71 section), the five JSON tables and prose maps under `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/`, prior fixture/checker notes below, and `.shokunin/lore/corpus/fixtures/check_bible.py`. I made no fixture, corpus, LOG, checker, or canon edits. The only file written for this task is this report.

The declared clone base is `r43-jorin-vela-sighting/`; its tables are `sources.json`, `entities.json`, `relations.json`, `timeline.json`, and `contradictions.json`. They already hold Vela as character `vela`, broad scene `harbor`, and Jorin's separate attributed report. The existing source prose is in `vela-note-excerpt.md` and `jorin-note-excerpt.md`; their mappings are `vela-clause-map.md` and `jorin-clause-map.md`. The prior Jorin map explicitly says the east steps are not the doorway or registry desk and that tick 3 is editorial, not simultaneity evidence. Avoid changing or relying on the inherited stale `vela-clause-map.md` as an exact r43 quote; the Jorin map documents that limitation.

## Minimal structural delta

Clone all five r43 tables as-is, then append only:

1. one `sources.json` row for the newly authored, explicitly fictional and unverified Vela response;
2. one source-cited claim to the existing `vela` entity in `entities.json` (do not create a duplicate Vela entity);
3. one source-cited report event for Vela in `timeline.json`;
4. no `relations.json` row and no `contradictions.json` row. Preserve all existing rows and text.

Example **structural shape**, with the statement/description required to match the final excerpt exactly in scope (the checker does not test that match):

```json
// sources.json: append
{
  "id": "r71-vela-slate-note",
  "title": "Vela’s east-steps slate note, year 12",
  "kind": "fictional first-person note",
  "reliability_note": "Newly authored fictional, unverified report; records Vela’s account, not omniscient truth."
}

// entities.json: append to the existing entity with id "vela" (not a new entity)
{
  "statement": "Vela reports [precisely quoted/readable slate wording] and distinguishes that observation from her inference about who made it.",
  "source_id": "r71-vela-slate-note"
}

// timeline.json: append
{
  "id": "vela-slate-reading-report",
  "tick": 4,
  "entity_id": "vela",
  "place_id": "harbor",
  "depends_on": [],
  "description": "Vela reports reading [the excerpt’s exact slate wording] at the east steps and separately reports her inference about its maker as uncertain.",
  "source_id": "r71-vela-slate-note"
}
```

The claim belongs in the existing `vela` row's `claims` array; preserve its current `first_appearance: "vela-note"`. The new source ID is cited by both new records and resolves uniquely. The suggested event ID is new; tick 4 is merely a nonnegative fixture-local ordering label, not a time claim. `entity_id=vela` is a resolvable character and `place_id=harbor` is the existing place. Empty dependencies avoid inventing an event dependency. Do not add a relation or a contradiction pointer just to encode the inference: the round declaration asks for one entity claim and one timeline report event, not a ledger assertion.

The bracketed text above is a schema placeholder, **not** authored slate content. The final author must decide on the excerpt and then replace the placeholders with the exact limited attribution it supports; do not commit these illustrative strings as facts. A minimal excerpt/map should identify which quoted words Vela says she could read, which separate statement is her inference about the maker, and what she cannot establish. If the text does not identify a maker, avoid implying it does. No name, signature, handwriting, date, seal, authentication, or provenance should appear in JSON unless the excerpt actually contains that claim—and even then it remains only Vela’s attributed report/inference. The r15 blue-mark account is not evidence of a Blue Seal trace (`.shokunin/lore/corpus/fixtures/r15-carbon-followup/sella-carbon-followup-excerpt.md`, `.shokunin/lore/reports/r15-reviewer.md`); do not connect the slate to the seal.

## Clause-to-row map and checker limits

| Proposed report content | Minimum row mapping | Limits |
|---|---|---|
| Vela identifies herself and reports a slate-reading at the east steps | Existing `entities.json` entity `vela`; new claim cited to `r71-vela-slate-note`. New `timeline.json` event actor `vela`, broad `place_id=harbor`, same source. | IDs are fixture alignment, not identity or location verification. East steps map only to broad harbor; no new place row is needed. |
| Exact words she says she could read | Put only the report-level observation in the claim/event statement/description, with wording traceable to the excerpt. | A readable quotation does not by itself establish who authored, placed, or authenticated the slate or the truth of its message. |
| Her belief/guess about who made it | Keep explicitly attributed as Vela’s inference, distinct from the readable text, in excerpt and mapped statement/description if included. | Inference is not observation or authorship evidence. Do not turn a guess into the claim that the named person made it. If no identity is given in the excerpt, do not add one in the row. |
| Any explicit uncertainty or limit | Map only what the excerpt states; it may be stated in the map as a limit rather than a separate fact claim. | Do not add claims of seal provenance, authenticated time, or resolution of an inherited contradiction. |

A manual clause map is necessary: `check_bible.py` validates required fields/types, unique IDs and source references, entity/place references, and timeline dependencies; it does **not** read Markdown, verify prose-to-row entailment, authenticate the source, or establish truth/canon. Its successful citation check only establishes that the ID exists in the fixture. Existing examples of this boundary include `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/jorin-clause-map.md` and `.shokunin/lore/reports/r43-reviewer.md`.

## Validity and scope checks for a future executor

- Keep the original arrays/rows from all five r43 tables intact; only the three described append operations are needed. The source and event IDs must not collide with inherited IDs.
- Ensure the entity claim is an object with nonempty `statement` and `source_id`; the event has the checker's required nonempty string fields, integer nonnegative `tick`, list `depends_on`, cited source, and resolvable actor/place. The inherited source `vela-note` remains the existing entity's first appearance.
- Run the checker on both the r43 base and new clone, and report its raw output honestly as structural only. A non-author should compare exact excerpt clauses to the one claim and one event and check that all inherited data stays unchanged; a clean checker cannot do that semantic review.
- The declaration sets the separate regression target at 130 prior fixture raw tuples. This schema scout did not run that replay and makes no claim about its result.

This report proposes no source fact, slate text, rights status, fictional-world canon, mechanics, authentication, authorship, or resolved contradiction.
