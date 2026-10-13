# Round 72 format scout — source + entity claim without event

## Scope and evidence

I read the Round 72 declaration in `.shokunin/lore/LOG.md`, the r43 fixture tables and Vela/Jorin excerpts and clause maps, Round 71 executor/reviewer/verifier/adjudicator reports and relevant schema/clause scouts, and `.shokunin/lore/corpus/fixtures/check_bible.py`. This is a format/adequacy audit only; I did not edit corpus, checker, LOG, or any other report.

The declaration requests a five-table r43-derived fixture with one new fictional first-person Vela source and **one cited claim on the existing Vela entity**, but explicitly no timeline event, relation, dependency, or contradiction. Round 71 tested a related slate-reading report with source + entity claim + timeline event; the reviewer found narrow depth potential, while the adjudicator rejected that candidate because `tick: 4` ordered it after inherited tick-3 accounts without support. The Round 72 form intentionally removes that shared-timeline placement.

## Schema and checker

An entity claim has the required shape `{ "statement": <nonempty string>, "source_id": <nonempty string> }`. The checker validates the claim's two strings and resolves `source_id` against a uniquely indexed source row. It does **not** require the entity claim to correspond to a timeline event. `first_appearance` is separately required and source-resolved; for existing Vela it should remain the inherited `vela-note`, not be rewritten to the new report merely because it is newly added.

Accordingly, a new source row plus one appended Vela claim is structurally adequate to preserve an attributed proposition such as “Vela reports that she read … and tentatively inferred …” without inventing a shared tick, event place, or sequence. Keep the wording explicitly as Vela’s report; source `reliability_note` can label it newly authored, fictional, and unverified. The source ID proves only a local citation link. An excerpt and clause map remain necessary for human audit of what Vela actually says and for separating reported reading from inference; the checker does not read them.

## Adequacy and limits

**Adequate for this bounded lore record, with a deliberate loss of event structure.** Source + entity claim can represent an attributed character-level claim without a timeline event; the checker does not make a timeline event a prerequisite. This is a better fit than forcing an unsupported tick when the record is not to assert relative chronology. It is not equivalent to a sourced event record: with no event, the tables do not encode when or where the reported reading occurred, nor a distinct event occurrence. Do not smuggle those details into the statement as objective fact or treat absence of an event as an assertion that no reading happened. If the intended product requirement is specifically an event-indexed chronology, entity claim alone would not satisfy that different requirement.

For the declared task, map the exact excerpt clause(s) to the appended `entities.json` claim pointer and its new `sources.json` row. Keep the claim scoped to what the excerpt reports and preserve uncertainty around maker inference. The source/claim/map combination is an auditable attribution record, not independent corroboration, authenticated slate text, or verification of the scene. No timeline placement means no event-ID/tick/place/dependency trace in the fixture; this is an intentional representational limit, not a checker defect.

## Verdict boundary

Format: **GO** for one appended, source-cited claim on existing `vela` with no timeline row, provided the claim is explicitly attributed and the excerpt/map trace it. The structural checker can establish schema and source-ID membership only. This audit makes no judgment that the prose materially deepens Vela, and no conclusion about source truth, canon, rights, or game mechanics.
