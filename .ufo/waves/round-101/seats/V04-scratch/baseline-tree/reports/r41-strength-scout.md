# Round 41 strength scout — Vela’s epistemic wording

## Assessment

The proposed edit tests a source-to-record strength mismatch, not whether the registry bell objectively rang. In r40 Vela says she “heard two strokes I took to be the registry bell,” explicitly marking bell identification as her interpretation; the excerpt does not establish bell origin (`.shokunin/lore/corpus/fixtures/r40-vela-listener/vela-note-excerpt.md:1`; map at `.../vela-clause-map.md:9-10`). The proposed r41 clause “heard the registry bell strike twice” is a more direct report that the sound was the registry bell (`.shokunin/lore/LOG.md:680`). It is still Vela’s attributed report, not independent or objective proof that the bell rang.

If r41 changes only that excerpt clause while retaining the r40 claim/event statements (“two strokes she took to be the registry bell”) unchanged (`.shokunin/lore/corpus/fixtures/r40-vela-listener/entities.json:81`; `.../timeline.json:46`), the record underrepresents the stronger wording. That is a plausible calibration mismatch: the fixed JSON remains logically compatible with the stronger excerpt (hearing the bell strike twice entails hearing two strokes), but it no longer faithfully preserves Vela’s direct identification. Do not call the JSON false or the excerpt objectively true. A careful reviewer can say “the source more strongly identifies the sound; record uses weaker, tentative attribution,” without resolving world truth.

## Novelty and precedent

R34 changed “saw” to “heard that,” separating direct visual observation from hearing a proposition; unchanged `reports seeing` fields then lacked direct-sighting support (`.shokunin/lore/LOG.md:531-532`; `.shokunin/lore/reports/r34-modality-scout.md`, “Calibration claim”). R41 is distinct in kind: it changes the strength of a reporter’s identification of an auditory source, not sensory modality versus hearsay. R36 changes an explicit date and withdraws same-occasion support, while copied event/ledger rationale becomes unsupported by changed prose (`.shokunin/lore/LOG.md:574-576`; `.shokunin/lore/reports/r36-date-scout.md`, “Risks”). R41 does not withdraw logical compatibility: “registry bell strike twice” is consistent with “two strokes she took to be the registry bell.” Its possible novelty is fidelity/calibration of epistemic strength, not contradiction or a stronger factual conclusion.

## Risks

- Overstate “directly asserts” as proof of the objective bell/source. It is only Vela’s stronger assertion in an unverified fictional excerpt.
- Overstate fixed JSON as incompatible or false. Its weaker tentative wording can remain logically true under the stronger excerpt; the defect is under-description / failure to represent the excerpt’s confidence, not necessary contradiction.
- Treat this as a mere paraphrase or as already proven calibration improvement. The contrast is subtle, and R34/R36 also test prose-to-record mismatch; novelty requires an independent reviewer to reliably identify this specific strength asymmetry.
- Conflate “two strokes” with “twice”: the proposed clause asserts two strikes of the identified bell; it still does not establish independent count, timing, occasion, or external source authentication.
- The unchanged non-sighting, date, tick, and other reports do not establish absence, chronology, corroboration, or canon.

## Falsifiable check

Compare the exact r40 and proposed r41 excerpts and confirm the sole changed clause is `heard two strokes I took to be the registry bell` → `heard the registry bell strike twice`, with all five JSON tables byte-identical. Give a non-author reviewer both exact excerpts and the unchanged Vela claim/event, asking separately (1) what Vela’s excerpt reports about source identification, (2) what the JSON records about her identification, and (3) whether the JSON is logically compatible with the excerpt. Expected: tentative identification in r40; direct/stronger identification in r41; tentative wording in the record; compatibility may remain, but source-to-record strength fidelity is reduced. The candidate is falsified as a useful calibration probe if reviewers find no meaningful strength difference, cannot distinguish it from r34 modality or r36 date support, or are led to declare objective ringing / JSON falsity. Checker success is irrelevant to this semantic judgment.
