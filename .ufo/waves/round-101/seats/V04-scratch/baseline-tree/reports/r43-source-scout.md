# Round 43 source scout — Jorin wording and attribution

## Finding

Proceed only with a narrow, explicitly attributed report. Jorin's first-person prose should say what Jorin claims to have seen, and the structured claim/event should preserve the same attribution and scope. It can conditionally corroborate Vela's reported east-steps location if editorially aligned character/place IDs and an overlapping occasion are assumed. It cannot establish that Jorin and Vela witnessed the same occasion, that the bell objectively rang, or that Sella/an envelope was absent.

## Source evidence and wording

- The round declaration requires Jorin to report seeing Vela **standing on the Lantern Harbor east steps during what Jorin called Bell-7**, and to say he did not see who, if anyone, struck the bell; it expressly limits corroboration to Vela's reported location and disclaims same occasion, same strokes, objective ringing, Sella/envelope absence, chronology, and canon (`.shokunin/lore/LOG.md:718`).
- Vela's r40 excerpt places her at the east steps and reports hearing strokes she took to be the registry bell, then says she did not see Sella or an envelope (`.shokunin/lore/corpus/fixtures/r40-vela-listener/vela-note-excerpt.md:1`). Its map says east steps map only to broad `harbor`, not registry desk; the sound source is unestablished; Bell-7/date are Vela's unverified occasion claim; and her non-sighting does not prove absence (`.../r40-vela-listener/vela-clause-map.md:7-16`).
- The r41 excerpt strengthens Vela's own identification to “heard the registry bell strike twice” (`.shokunin/lore/corpus/fixtures/r41-vela-direct-bell/vela-note-excerpt.md:1`); its contrast map explicitly treats that as a stronger Vela-attributed claim, not proof of objective ringing, and says unchanged JSON does not establish shared occasion or objective absence (`.../r41-vela-direct-bell/strength-contrast-map.md:3-5`).
- The r33 precedent's first-person “I, Tarin, saw...” supports only a reported observation, with person/place IDs editorial and tick 3 an arbitrary local label (`.shokunin/lore/corpus/fixtures/r33-tarin-envelope/tarin-note-excerpt.md:1`, `.shokunin/lore/corpus/fixtures/r33-tarin-envelope/clause-map.md:7-12`). r10 likewise labels its excerpt fictional/invented, and presents Sella's own recorded account rather than omniscient fact (`.shokunin/lore/corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md:1-5`). These precedents support first-person attribution, not authentication.

### Recommended literal excerpt

> I, Jorin, stood at the Lantern Harbor registry doorway. I saw Vela standing on the Lantern Harbor east steps during what I called Bell-7. I did not see who, if anyone, struck a bell.

This keeps the physical sighting as Jorin's report, preserves the phrase “what I called” as his naming rather than objective bell identification, and states the strike limitation without implying no strike occurred. Do not add “the same Bell-7,” “at the same time,” “I saw/heard the same strokes,” or “Sella and the envelope were absent.” Do not convert east steps to registry desk or assign the bell source. If an event tick is needed, it is fixture-local editorial sequence only, not evidence of simultaneity.

## Attribution requirements for rows/map

- Source excerpt must be explicitly newly authored fictional Jorin first-person text; source metadata/citation ID alone is not evidence authenticity.
- Jorin entity claim: e.g. “Jorin reports seeing Vela standing on the Lantern Harbor east steps during what he called Bell-7; he reports not seeing who, if anyone, struck a bell.” Cite only `jorin-note`.
- Event description must similarly say “Jorin reports seeing...” rather than state “Vela stood...” as narrator fact. Actor `jorin` and place `harbor` should describe the reporter/observation scene, not prove Vela's location independently. Avoid adding a Vela event or changing inherited Vela rows.
- Map exact phrases separately: “I, Jorin” → fixture-local ID alignment; “saw Vela standing” → Jorin's claimed visual observation; “east steps” → broad harbor place alignment, not desk; “during what I called Bell-7” → Jorin's own label, no demonstrated equivalence to Vela's Bell-7; “did not see who, if anyone, struck a bell” → limit of Jorin's sighting, not no-strike or bell-origin assertion. Tick/IDs are editorial. Preserve all inherited Tarin/Sella/Vela claims, event and ledger unchanged.

## Risks / falsifiers

1. **Attribution collapse:** If claim/event removes “Jorin reports” or converts his sighting into an unqualified Vela fact, the wording is overclaimed. Reviewer should reject or repair it.
2. **Occasion conflation:** Shared label text “Bell-7” does not prove Jorin's and Vela's label refers to one ringing; “what I called” deliberately leaves that open. Do not say same occasion or simultaneous corroboration.
3. **Overbroad witness claim:** Jorin's location sighting does not corroborate Vela's heard strokes, bell identification/ringing, or non-sighting concerning Sella/envelope. Explicitly forbid those in map and review.
4. **Arbitrary novelty:** Another witness row alone is not depth. The plausible increment is a separately attributed visual account of Vela's reported location, distinct sensory perspective from Vela's auditory report and Tarin's sighting of Sella's placement. If the adjudicator finds this mere witness-count growth with no material narrative distinction, reject depth admission.
5. **False independence:** “Independent” means a separate authored in-world account/source in the fixture, not verified independence, authenticity, or freedom from shared information. Never infer objective corroboration.

## Falsifiable test and honest novelty assessment

Build a separate r41-derived fixture with unchanged inherited rows and sources, then add only the new Jorin excerpt, source, character claim/event, and clause map. A non-author reviewer must verify every Jorin assertion against the literal excerpt and reject any claim of common occasion, objective bell, Sella/envelope absence, or canon. Structural checker should exit clean, but that result tests only schema/reference validity. Independently replay all 94 baseline CLI stdout/stderr/exit tuples and compare all 469 baseline JSON paths byte-for-byte to the pinned baseline; verify inherited r41 claims/event/ledger unchanged and account for every added row. Fail the depth claim if wording outruns the excerpt, a non-author finds unsupported synchronization/corroboration, or replay changes any prior result.

Novelty is **modest and conditional, not established**: r10 is Sella's own registry account; r33 is Tarin reporting Sella's envelope placement; r40/r41 is Vela's own auditory report. Jorin would add a distinct third-party visual report of Vela's location, not a verified shared observation. The proposal can be a bounded report-level perspective, but an independent adjudicator should reject it if this distinction is not a material depth gain. Coverage/calibration are not targeted and must not be claimed improved.
