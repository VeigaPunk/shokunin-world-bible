# Round 28 map scout — clause to relation row

## Exact relation target

- `.shokunin/lore/corpus/fixtures/consistent/relations.json:2-6` is the only relation row: `from=mira`, `to=seal`, `type=carries`, `source_id=courier-log`.
- The source registry identifies `courier-log` as “Courier Mira’s Route Log, year 12” and a first-person fictional log (`sources.json:9-13`). This links the row to an in-world source ID; it is not itself prose evidence.
- Current excerpt gap is explicitly recorded in `.shokunin/lore/LOG.md` (Round 28 declaration): no committed fictional `courier-log` excerpt under `consistent/`. Existing claim at `entities.json:7-11` says “Mira carried the blue seal,” but that is already a structured assertion citing the same source ID, not an independently inspectable clause. The seal claim at `entities.json:43-47` says only “The seal accompanied Mira”; it is not evidence of custody direction or carrying.

## Narrow mapping proposal

For the new fixture's fictional excerpt, select one literal clause whose explicit subject is Mira and whose direct observed action is carrying the Blue Seal (e.g. “I carried the blue seal to the north gate.”). Map only the clause's subject to `from=mira`, object to `to=seal`, and carrying predicate to `type=carries`; cite the exact clause and line in the map. Treat destination/purpose as outside the relation row. Do not use arrival/departure timeline entries (`consistent/timeline.json:2-24`) to infer a carrying event or infer reciprocal ownership, possession duration, delivery, or canonical truth. The example wording is a proposed constructed excerpt, not evidence from existing source text.

## Risks / falsifiable check

Risks: the existing entity claim can create circular-looking corroboration if presented as independent proof; an excerpt mentioning only that the seal accompanied Mira does not entail the directed verb `carries`; relation direction and temporal scope must not be embellished. The checker validates schema/reference consistency, not natural-language entailment.

Falsifiable human check: after a new separate fixture and map exist, a non-author reviewer must quote the exact excerpt line and show independently that its explicit subject/object/action entail precisely `mira -> seal / carries`; reviewer must reject a matched near-miss clause changed to “the seal was near Mira” (no carrying) or “Mira saw the seal carried” (agent differs). Structurally run the checker on the new fixture (expected exit 0), and replay 78 prior fixture stdout/stderr/exit plus 389 prior JSON path bytes exactly. Failure of the entailment contrast, structural check, or byte-identical regression falsifies the declared move. This is a proposed check only; no excerpt, fixture, or checker was changed here, and no claim is made about external source text or canon.
