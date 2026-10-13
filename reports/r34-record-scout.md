# Round 34 record scout — r33 trace

## Scope and calibration axis

The r33 artifact is a small, internally traceable report chain, not independent confirmation that its reported event happened. The relevant calibration distinction is that the text says Tarin **saw** the action, whereas the proposed r34 sentence says Tarin **heard that** it happened. The latter is evidence of a reported assertion reaching Tarin, not direct sight. Do not classify hearsay as an explicit negation or proof the envelope placement is false.

## Claim/event trace

- `tarin-note-excerpt.md:1` (r33 fixture) is the entire newly authored source sentence: “I, Tarin, saw Sella place an unlabeled paper envelope on the Lantern Harbor registry desk.” This supports the text's attribution of a seeing-report to Tarin and the described action, subject to the note's reliability and the editorial entity/place alignments; it does not establish truth beyond that report.
- `sources.json:11-16` registers `tarin-note` as a newly authored fictional first-person note and explicitly cautions it reports Tarin's observation, not omniscient truth. `entities.json:43-51` identifies Tarin with first appearance in that source; its claim says Tarin “reports seeing” the placement. `entities.json:52-60` identifies Sella and phrases her claim as “Tarin reports that Sella placed...” These are attributed claims, not unqualified ground-truth assertions.
- `timeline.json:19-28` adds `tarin-envelope-observation`: actor Tarin, place `harbor`, local tick 3, and an event description repeating “Tarin reports seeing...” The event is explicitly a reported observation. `depends_on: []` and tick 3 do not establish temporal dependency or the event's actual time; `clause-map.md:10-11` says tick 3 is an arbitrary local sequence label.
- `clause-map.md:3-9` maps first-person Tarin, “saw,” Sella, the placement/object description, and registry desk/location. It expressly calls IDs fixture-local alignments (`:5`, `:7`), says the envelope is not separately identified/owned (`:8`), and limits the source's scope (`:13`). Existing registry/courier rows are retained, not corroboration of this placement: `relations.json:1-7` has only Mira carrying the seal; `contradictions.json` is empty.

## Modality contrast and risks

The proposed r34 wording “I, Tarin, heard that Sella placed...” changes the evidence mode: Tarin reports hearing a proposition, not seeing Sella act. If the JSON is held fixed, its `reports seeing` character/event claims no longer follow from that sentence. That mismatch is a calibration failure in the r34 pair, not a reason to call the r33 JSON false. “Heard that” does not identify who told Tarin, their basis, or whether the placement occurred. Conversely, “saw” is a source-level claim of direct observation, not proof the observer is accurate or the world fact true.

Risks to avoid: interpreting either source as omniscient canon; converting a fixture-local ID match or local tick into independently established identity/location/chronology; inferring envelope contents, owner, recipient, destination, motive, Blue Seal/carbon/route-strip connection, or rights/game-mechanics implications. Structural checker success only checks machine-readable structure/references; it cannot validate prose entailment.

## Falsifiable check

Compare r33 and the proposed near-miss while keeping the five JSON tables and source IDs fixed. A non-author reviewer should find that the r33 sentence entails **a report by Tarin of seeing** the placement, and the r33 entity/event rows preserve that attribution; the near-miss entails only **a report by Tarin of hearing an assertion** and must fail acceptance as support for the unchanged direct-sighting wording. It must not be labeled an explicit denial, evidence the placement did not happen, or a reason to mark r33 false. This check is falsified if the reviewer accepts the hearsay sentence as direct-sighting support, or if the r33 claim is rejected despite its literal “saw” wording merely because a report is not independent verification.
