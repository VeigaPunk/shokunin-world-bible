# Round 83 source scout — Vela wording and non-sighting scope

## Exact source text and pointers

The relevant authored excerpts are in three controlled fixtures:

- `corpus/fixtures/r40-vela-listener/vela-note-excerpt.md`: “I, Vela, stood on the Lantern Harbor east steps and heard two strokes I took to be the registry bell during Bell-7, the sole seventh-watch registry-bell sounding on the seventh day of Embermonth, year 12. I did not see Sella or an envelope.”
- `corpus/fixtures/r41-vela-direct-bell/vela-note-excerpt.md` and `corpus/fixtures/r43-jorin-vela-sighting/vela-note-excerpt.md`: same location, occasion and final non-sighting clause, but the auditory clause is “heard the registry bell strike twice.” These r41/r43 copies retain the same non-sighting wording as r40.

In each fixture the Vela claim is `entities.json`, character `vela`, `claims[0]`: “Vela reports hearing two strokes she took to be the registry bell during Bell-7 and reports not seeing Sella or an envelope.” The corresponding `timeline.json` event is `vela-listening-report` (actor `vela`, `place_id: harbor`, `tick: 3`, source `vela-note`): “Vela reports hearing two strokes she took to be the registry bell during Bell-7; she reports that she did not see Sella or an envelope.” The r41/r43 excerpts strengthen the bell wording but **do not change these JSON strings**. `sources.json` labels `vela-note` a newly authored, fictional, unverified report. `vela-clause-map.md` in r40 and `strength-contrast-map.md` in r41/r43 explicitly treat the final clause as a report-level non-sighting, not proof of absence. The r41/r43 inherited clause map is not a reliable exact quotation of their stronger bell wording; see the local strength contrast maps and the actual excerpt.

## Does the existing record encode two separate non-sightings?

At ordinary English reading, “I did not see Sella or an envelope” conventionally reports that Vela saw neither Sella nor an envelope. The claim and event repeat that coordinated negative in attributed prose. So an editor may reasonably read it as two targets of one non-sighting report—not as a positive sighting of either.

But the fixture does **not** encode two separately addressable propositions/fields. Each JSON record contains one free-text sentence with the same “not seeing X or Y” coordination; there is no distinct `did_not_see_sella` / `did_not_see_envelope` field, separately sourced claim, or checker rule that resolves scope. The clause map likewise describes the phrase collectively as limiting Vela’s reported sighting. Thus “both separately encoded” is too strong as a structural claim: both targets occur in a single, ordinary-language negative, whose likely distributive reading is manual semantics, not machine-validated atomization.

The round-83 contrast is semantically intelligible: “I did not see Sella with an envelope” ordinarily denies seeing the *combined scene* (Sella-with-envelope), and does not by itself deny seeing Sella alone or an envelope alone. The current “Sella or an envelope” wording ordinarily covers either target separately. This would be a distinction between the scope of Vela’s attributed report, not a discovery that either target was actually seen or absent. However, because both JSON strings remain unstructured summaries and the checker validates structure/pointers rather than prose meaning, neither phrase yields a machine-enforced pair of independent absence claims. A careful editorial response to a joint-only variant would be to qualify/withhold any separate envelope non-sighting inference rather than call the existing rows false.

## Limits and provenance

The excerpts are explicitly authored fictional reports; source IDs, entity/event pointers and checker-clean status establish fixture attribution/structure only—not authenticity, independent corroboration, what happened in the fictional world, or canon. The quoted Bell-7/date/sole-ringing phrases are character-attributed claims, not authenticated chronology; local tick 3 does not prove simultaneity or a shared occasion. Vela’s report does not settle Tarin/Sella’s ledger or establish Sella/envelope presence or absence as world fact. Nothing here determines real-world rights or reuse permission, and no game mechanics are implicated.

**Source-scout conclusion:** likely distinct ordinary-language readings exist between separate-target non-sighting and a joint-scene non-sighting, but the present JSON expresses the former only as one coordinated free-text report; it does not separately model the two propositions. Any calibration gain therefore needs to be demonstrated as a useful human editorial decision, not claimed as checker coverage or formal semantic encoding.
