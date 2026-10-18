# Round 41 critic — epistemic-strength mismatch and novelty

## Assessment

The proposed substitution is a plausible calibration probe, but its mismatch claim must be stated narrowly. In r40 Vela says she “heard two strokes I took to be the registry bell” (`.shokunin/lore/corpus/fixtures/r40-vela-listener/vela-note-excerpt.md:1`). That wording attributes a tentative identification to Vela. The proposed r41 wording, “heard the registry bell strike twice” (`.shokunin/lore/LOG.md:678`), would instead report the bell as the identified sound source directly. If the Vela claim/event descriptions remain phrased as “took to be,” those fields understate what the altered excerpt says. This is a source-to-record epistemic-strength mismatch, not proof that a real or objective registry bell rang, nor a finding that the unchanged JSON is false.

The stronger excerpt does not by itself establish an objective bell event. It remains Vela's fictional, unverified report. A record that retains the weaker formulation (“took to be”) is logically compatible with the stronger report as a less-specific paraphrase; the defect is loss of fidelity/precision, not contradiction. Thus the round can test whether a reviewer notices the mismatch, but must not describe it as a strict logical incompatibility or unsupported objective fact. Citation IDs and checker success cannot decide this semantic question.

## Novelty against precedents

R34 tested whether “heard that” could be mistaken for Tarin's direct seeing; its policy explicitly retained the JSON and judged direct-sighting support from prose (`LOG.md:531-545`; `.shokunin/lore/reports/r34-critic.md`, “Falsifiable check”). R36 tested a changed explicit date against fixed date-bearing JSON and ledger rationale, withholding same-occasion support (`LOG.md:573-592`; `.shokunin/lore/reports/r36-critic.md`, “Falsifiable check”). R41 is distinct in target: not sensory modality or date identity, but the strength of source identification (tentative interpretation versus direct report of bell source). Yet novelty is modest and not automatic: both prior rounds already establish the general practice of manually assessing prose against fixed structured assertions. The incremental calibration axis is specifically whether a reviewer distinguishes a weaker, compatible record from an exact rendition of stronger prose.

R40's map is explicit that “I took to be” is tentative and does not prove a registry bell rang (`.shokunin/lore/corpus/fixtures/r40-vela-listener/vela-clause-map.md`, rows “heard two strokes” and “I took to be the registry bell”; `.shokunin/lore/reports/r40-scribe.md`, modality row). The new wording removes that hedge but still appears only in an attributed fictional excerpt. It does not prove Bell-7, objective origin, date/time, simultaneity, corroboration, or canon.

## Risks

- **Overclaiming incompatibility:** weaker JSON can remain logically compatible while omitting the stronger distinction. Call it under-specific/mismatched to the excerpt, not false.
- **Objective-source laundering:** the excerpt's direct wording is still a report by Vela, not external confirmation that a bell sounded.
- **False novelty:** merely repeating “prose can mismatch fixed JSON” is not a new axis; the candidate only earns novelty if the reviewer identifies this exact direction of strength shift and compatibility nuance.
- **Retroactive interpretation:** r40 JSON should not be assumed to say more than its fields actually say. Inspect exact Vela claim/event descriptions in the implemented fixture before asserting mismatch.
- **Overreading event vocabulary:** “heard” plus “strike twice” supports Vela's direct report of hearing the registry bell, not mechanism, location, independent witness, or truth.
- **Inherited claims:** non-sighting, Bell-7/date, other accounts, and ledger remain bounded as in r40; no upgrade follows from the wording change.

## Falsifiable check

Compare the exact r40 and proposed r41 excerpts and inspect the unchanged Vela claim and event descriptions. Blind a non-author to the expected result and ask separately: (1) what does Vela's r40 excerpt report about the sound source, and with what certainty? (2) what does the r41 excerpt report? (3) does the fixed JSON contradict r41, or merely fail to preserve its stronger specificity? Calibrated answers should say r40 attributes a tentative identification; r41 directly reports hearing the registry bell strike twice; the weaker record may be logically compatible but is less faithful/under-specific. Fail the candidate if the reviewer calls the JSON objectively false, treats the excerpt as proof of an actual bell, misses the change in epistemic strength, or claims strict incompatibility without textual support. Also verify the only inherited prose change is the intended clause, fixed JSON is byte-identical, and all prior artifacts are preserved as declared; checker cleanliness is structural only. If the exact JSON already states the stronger claim, or the record wording is too ambiguous to establish the proposed under-specificity, the mismatch claim is falsified.

No fixture or checker run is claimed here. No fixture, checker, LOG, README, or commit edits were made.
