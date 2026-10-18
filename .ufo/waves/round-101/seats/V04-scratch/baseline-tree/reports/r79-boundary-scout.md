# Round 79 boundary scout — r72/r73 slate linkage limits

## Scope

Report-only review of the Round 79 declaration and the existing Round 72/73 declarations, fixtures, and relevant scout/reviewer/adjudicator evidence. The requested boundary is whether r72/r73 support a shared slate, event, timeline, or relation, and how to word any link safely. I made no edits to LOG, corpus, fixtures, or checker; this report is the only file written. No external sources were consulted.

## What the rows and prose actually establish

- **R72 Vela report:** `corpus/fixtures/r72-vela-slate-claim/vela-slate-note-excerpt.md` says Vela leaned close and could read “KEEP THE EAST GATE CLEAR,” wondered whether cramped letters meant the writer was hurried, and could not tell who wrote them. Its source row `vela-slate-note` labels this an invented, unverified first-person report. The appended Vela entity claim cites that source. The clause map distinguishes reported reading, tentative inference, and limit. R72 deliberately adds no slate entity, timeline event/tick/place/dependency, relation, or contradiction entry; the inherited timeline/relations/contradictions remain the r43 rows.
- **R73 Jorin report:** `corpus/fixtures/r73-jorin-slate-claim/jorin-slate-note-excerpt.md` says Jorin was sent to copy a gate notice, read “KEEP THE EAST GATE OPEN” on a slate at the east steps, and did not see who put it there. The new `jorin-slate-note` source and Jorin entity claim represent this as a separate invented, unverified report. R73 appends no event: `timeline.json`, `relations.json`, and `contradictions.json` are unchanged from r72. Its editorial comparison accurately compares two *reported wordings* and explicitly leaves slate/inscription identity, reading time, and source relationship unresolved.
- **Inherited Jorin sighting is not the reading:** `jorin-note-excerpt.md` says Jorin saw Vela on the east steps during what he called Bell-7. It does not mention a slate, words, or either reading. Its event `jorin-vela-sighting` is an existing location-sighting report, not a slate-reading event. Neither the matching place words nor Bell-7 label links that sighting to Jorin’s separate slate report. R72/R73 adjudication likewise treats the Bell-7 sighting and slate readings as unlinked.

Thus the safely supported connection is only a **documentary/editorial comparison** between two distinct attributed reports that use the word “slate” and report different wording. The records do not establish one physical object, one inscription, one notice, persistence/change, a common occasion, common authorship, a witness relationship, or any temporal ordering. “At the east steps” in Jorin’s r73 report does not supply a time or identify Vela’s report’s slate. Repetition of “gate” or the same setting is not identity evidence.

## Linkage risks and safe boundaries

1. **Shared slate / changing inscription:** Calling this “the same slate,” “the notice changed from CLEAR to OPEN,” or “before/after versions” would add an unsupported object identity and sequence. Even “the same notice” overstates the evidence: the excerpts say “slate” and “gate notice,” but do not connect the described items. Do not call the different text a contradiction; the reports could concern separate slates, notices, or occasions.
2. **Shared event / eyewitness chain:** Saying “Jorin saw Vela read it,” “Jorin later read Vela’s slate,” or that both readings occurred in one scene/event is unsupported. The old Jorin report only says he saw Vela standing at east steps during his Bell-7 label. No source says he witnessed a reading, spoke to Vela, or saw the same object.
3. **Timeline / chronology:** No slate-reading event, tick, date, dependency, or ordering exists in r72/r73. The fixture’s existing tick-3 labels are local sequence labels and do not establish simultaneous occurrence or date. Jorin’s “during what I called Bell-7” belongs to his inherited sighting report, not the added reading report. Do not attach the new Jorin claim to `jorin-vela-sighting`, infer Bell-7 timing, say either reading preceded/followed the other, or use absence of timeline rows as proof the readings did not happen.
4. **Relation / source relation:** No relation row links Vela and Jorin, either to a slate, or the reports to each other. A shared-occasion, witnessed-by, authored-by, copied-from, or source-dependence relation would be invented. Different `source_id`s are citation pointers to separate fictional report rows; they do not prove independent witnesses, source independence, or corroboration.
5. **Object, maker, placement, and truth:** Neither excerpt authenticates slate existence, inscription, wording, placement, persistence, writer, placer, or provenance. Vela’s inference about hurried letters remains her speculation, not an authored fact; neither speaker identifies a writer/placer. No canon conclusion follows.

## Safe wording

Prefer:

> “Vela’s r72 fictional report says she could read ‘KEEP THE EAST GATE CLEAR’ on a slate (`vela-slate-note`). Jorin’s separately cited r73 fictional report says he read ‘KEEP THE EAST GATE OPEN’ on a slate (`jorin-slate-note`). These are different reported wordings; the records do not establish whether they concern the same slate/inscription or occasion, when either reading occurred, or any relationship between the reports. Neither establishes an inscription change or direct contradiction.”

If shorter wording is needed: **“Two separately attributed fictional reports give different slate wording; shared object, occasion, chronology, and source relationship are unresolved.”** Avoid “the slate,” “the changed inscription,” “Jorin’s later reading,” “Vela’s/Jorin’s version of the same notice,” “corroborates,” and “contradicts” unless new evidence explicitly supports the intended link.

## Checker and evidence boundary

`check_bible.py` validates JSON shape and, among other structural checks, whether an entity claim’s `source_id` resolves uniquely to a `sources.json` ID. This citation-ID check only tests a fixture-local pointer. It does not read or compare excerpt/clause-map Markdown, prove a claim is entailed by prose, establish source authenticity or truth, identify two described objects/events as the same, validate chronology or relation semantics, or establish canon. The clause maps and editorial comparison are human editorial aids, not checker-verified facts. A clean checker result is not evidence that either invented report is true or that their accounts agree.

This report concerns repository-invented fiction and structural citation behavior only. It makes no finding about real source-text truth/authenticity, canon, rights/licensing, or game mechanics. “Fictional,” “newly authored,” and a resolvable citation ID do not by themselves establish rights or permission.
