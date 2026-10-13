# Round 73 schema scout — minimal r72 clone and Jorin claim

## Scope and evidence

I read the Round 73 declaration in `.shokunin/lore/LOG.md`, the r72 five-table fixture (`corpus/fixtures/r72-vela-slate-claim/{sources,entities,relations,timeline,contradictions}.json`), its Vela slate excerpt/map, the inherited Jorin excerpt/map, relevant Round 72 executor/reviewer/verifier/adjudicator and format/calibration reports, and `corpus/fixtures/check_bible.py`. This is a schema and placement map, not an authored candidate or axis verdict. I changed no fixture, README, checker, LOG, or other report; this report is the sole output.

## Minimal clone and delta

Use all five r72 tables as the base. Preserve inherited rows and, specifically, do not alter `relations.json`, `timeline.json`, or `contradictions.json`. Append just one new fictional, unverified Jorin source in `sources.json`, then append one source-cited claim to the existing `jorin` character's `claims` array in `entities.json`. Do not create another Jorin entity. No event, event pointer, relation, dependency, or contradiction-ledger row is needed or appropriate for this requested claim-only representation.

At the current r72 row positions, `sources.json` has seven rows (new source would be index `/7`); `entities.json` has eight rows and `jorin` is `/7`, with its existing claim at `/7/claims/0` (new claim would be `/7/claims/1`). These are pointers for the inspected r72 baseline; confirm if the clone's rows are changed. The existing `jorin-note` source remains the citation for Jorin's inherited east-steps/Bell-7 sighting, and must not be repurposed as the new slate-wording source. Keep Vela's existing `vela-slate-note` claim and source intact.

The checker requires each source row to have nonempty string `id`, `title`, `kind`, and `reliability_note`; each entity row needs its required fields and valid kind; and each claim needs nonempty `statement` and `source_id`. It resolves claim source IDs against the supplied source index. Thus the new Jorin claim should be explicitly attributed as a report, cite the newly appended unique source ID, and have wording that stays within its eventual excerpt. The checker does not parse excerpts/maps or establish that their wording supports the claim.

## Existing wording and limits for a clause map

`r72-vela-slate-claim/vela-slate-note-excerpt.md` says: “I leaned close to the slate and could read, “KEEP THE EAST GATE CLEAR.” The cramped letters made me wonder if whoever wrote them had been in a hurry. I could not tell who wrote them.” Its map links the exact spans to Vela claim `/6/claims/1` and source `/6` and labels the claim a paraphrase. This is Vela's fictional report, not an authenticated inscription.

Inherited `r72-vela-slate-claim/jorin-note-excerpt.md` instead says Jorin stood at the registry doorway, saw Vela on the east steps “during what I called Bell-7,” and did not see who, if anyone, struck a bell. Its map explicitly says the doorway is not the east steps or registry desk, that the matching Bell-7 label does not establish shared occasion or chronology, and that the existing event's tick is editorial sequence rather than simultaneity evidence. That inherited excerpt does not say Jorin read a slate. Any new excerpt therefore needs its own source and exact clause-to-claim/source pointers; do not treat the inherited sighting as evidence for the new reading.

The proposed editorial comparison should be limited to a difference between the *wording each report attributes to a slate*. Preserve both attributions and leave open whether the accounts concern the same slate/inscription, occasion, or source context. Do not say Jorin saw Vela read it, establish that either line was actually inscribed, or label the accounts a proven contradiction. No shared time, sequence, or event follows from the row order or from the inherited Bell-7 sighting. The declaration supplies no exact proposed Jorin wording, so a scout cannot validate literal quote spans or claim entailment yet.

## Structural boundary

A source plus entity claim can represent the bounded attributed statement without an event row. This deliberately provides no event-indexed retrieval, date, place assignment, or timeline placement for the reported reading. The five-table clone still includes the unchanged inherited timeline and ledger; “no ledger entry” here means no *new* contradiction entry. The checker can establish table/row shape and source-ID membership, not prose fidelity, source truth, slate identity, persistent inscription, chronology, canon, real-world rights, or game mechanics. The declared improvement/falsifiers require later non-author review; this schema map makes no depth, coverage, or calibration finding.
