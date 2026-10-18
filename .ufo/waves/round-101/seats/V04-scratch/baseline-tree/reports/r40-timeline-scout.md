# Round 40 timeline scout — actor, place, tick, and source mapping

## Scope and precedent

Read-only audit of the r40 proposed Vela account against r35, and the r14/r23 precedent reports and fixture. No fixture/checker/LOG/README edits, no commit, and no children spawned. I treat timeline/source rows as editorial structure, not proof that reported events occurred.

r35’s relevant rows are `timeline.json:23-29` (`tarin-envelope-observation`: Tarin, harbor, tick 3, source `tarin-note`) and `:32-38` (`sella-bell7-presence`: Sella, tower, tick 3, source `sella-bell7-note`). Both excerpts describe Bell-7, but r35 review notes the same-occasion interpretation is not independently established by matching editorial tick/label. The r35 source table has separate note IDs at `sources.json:15-25`; the Tarin and Sella event IDs and references are distinct, not duplicate bookings.

## Proposed Vela mapping

For the proposed wording, “I, Vela, stood on the Lantern Harbor east steps and heard two strokes I took to be the registry bell … I did not see Sella or an envelope,” the minimal coherent mapping is:

| Clause | Candidate field | Scope / risk |
|---|---|---|
| “I, Vela” | `timeline.entity_id` = Vela entity ID; claim and excerpt source both identify Vela | Attribute as Vela’s report; do not add Vela as actor to Tarin/Sella rows. |
| “stood on the Lantern Harbor east steps” | `place_id` = existing `harbor` if the steps are within that entity; otherwise define a distinct place and map consistently | Do not silently imply the steps equal registry desk or whole harbor. Existing `harbor` row names Lantern Harbor (`entities.json:15-23`). |
| “heard two strokes I took to be the registry bell” | description + Vela claim, both attributed to the new Vela source; avoid an objective bell event unless separately evidenced | Keep perceptual identification explicitly Vela’s interpretation; do not source-map as objective registry-bell sounding. |
| “during Bell-7” / `tick: 3` | event’s chosen editorial tick 3, with Bell-7 phrase retained as the report’s claimed occasion | Tick 3 is already occupied by Tarin and Sella rows, but this is not a schema-level booking conflict: rows are separate reports and no uniqueness constraint follows from the observed fixture. Nor does equal tick prove simultaneous observation or common referent. |
| “I did not see Sella or an envelope” | Vela’s negative visual report in the same source-attributed event/claim | Narrow to Vela’s seeing; not proof Sella/envelope absent, and not contradiction of Tarin’s seeing or Sella’s report. |
| source | one new unique `sources.json` ID, used consistently in Vela excerpt, entity claim and event | Do not reuse `tarin-note` or `sella-bell7-note`; avoid a second timeline event for the same Vela utterance unless the prose actually distinguishes events. |

No double-booking is established merely by the existing rows sharing tick 3. But a single Vela observation row at tick 3 adds a third editorially co-indexed report and can misleadingly look like a synchronizing witness. Avoid wording such as “at the same instant,” “as Tarin saw,” or “the bell rang” as narrator-level fact; the supplied candidate already limits bell identification to what Vela took it to be. Do not add a Vela→Sella relation or ledger endpoint: the report neither sees Sella nor the envelope.

## Precedent and risks

- r14 reviewer’s audit distinguishes source/index assignment from evidence: matching JSON row and backfilled excerpt is correspondence, not independent support (`reports/r14-reviewer.md`, “Clause-by-clause assertion audit” and “Axis judgment”). This warns against treating a tailored Vela source as corroboration of r35.
- r23 reviewer accepts a tick-3 Sella@harbor follow-up after departure, but explicitly reads `depends_on` as order only, “not a clock,” and the report as speaker-bounded (`reports/r23-reviewer.md`, clause map and timeline audit). Its `timeline.json:23-31` maps one report to Sella/harbor/source `sella-absence-note`; it does not make tick 3 a global instant or establish absence as world fact.
- r35 itself makes the attribution/place split visible: Tarin is the event actor at harbor, while Sella is the reported subject of his envelope observation (`timeline.json:23-29`); Sella’s separately sourced presence row is actor Sella at tower (`:32-38`). Vela’s actor should be Vela, not Sella, and the Harbor place only locates Vela’s reported hearing.
- Main risk: interpreting three tick-3 rows as independent contemporaneous corroboration or using the “registry bell” label to establish an objective bell occurrence. Second risk: flattening “did not see” into a factual absence or into a direct challenge to Tarin/Sella. Source-ID reuse or duplicate rows would also blur whose account each event represents.

## Falsifiable check

Inspect the eventual fixture’s Vela excerpt, `sources.json`, `entities.json`, and `timeline.json` together. Pass this mapping check only if (1) exactly one new Vela source ID is referenced by Vela’s claim and event and the excerpt is expressly report-framed; (2) exactly one Vela event has `entity_id` Vela, the Harbor/steps place resolved consistently, and chosen tick 3; (3) its description preserves “heard two strokes” and the subjective “took to be” wording plus Vela-bounded non-sighting; (4) Tarin and Sella rows, source IDs, descriptions, and ledger pointers are unchanged; and (5) no objective bell event, Sella/envelope absence fact, shared-instant assertion, duplicate Vela event, or new corroboration relation is introduced. A diff violating any item falsifies alignment/non-double-booking at the claim level. Even a pass establishes only structural/source alignment, not truth, simultaneity, or canon.
