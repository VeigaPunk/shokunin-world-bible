# Round 46 citation scout — person identification and bounds

## Finding

**No-go on treating this as a novel calibration axis move; preserve as a useful caveat, not a new rule.** The person-referent question is real: a source sentence can report seeing someone whom the speaker only took to be Vela, while a record names Vela. But the candidate is already the inverse of r41’s explicit tentative-versus-direct identification contrast. r41 changes Vela’s identification of a sound; r46 would change Jorin’s identification of a person. The referent differs, but the epistemic operation and expected treatment (fixed record remains compatible yet loses source precision) are substantially the same. This is a serious novelty challenge, not evidence that the candidate is false.

## Evidence (path:line)

- `.shokunin/lore/LOG.md:771-773` describes the proposed single-clause change from “I saw Vela” to “I saw someone I took to be Vela,” while leaving five JSON tables unchanged; it expressly identifies r41 as prior art and makes novelty a gate. (Use the Round 46 section near the end of the file; line numbering may shift.)
- `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/jorin-note-excerpt.md:1` currently says “I saw Vela standing…”; the source does **not** say “someone I took to be Vela.”
- `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/jorin-clause-map.md:5-8` aligns that clause to a claimed sighting, says overlap is conditional on same place/occasion, and explicitly says it does not verify Vela’s report. Its narrator/role clause is only self-identification, not external identity/employment verification (`:5`).
- `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/entities.json:~last entry` has ID `jorin`, whose claim says Jorin reports seeing **Vela** on the east steps, cited to `jorin-note`; there is no separate person entity or uncertainty marker. `timeline.json:50-57` likewise describes Jorin seeing Vela and assigns actor `jorin`, place `harbor`, tick 3. These are fixed editorial rows, not independent confirmation.
- `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/strength-contrast-map.md` is inherited r41 contrast text, not an r43-specific map; it states r40 “I took to be” versus r41 direct “the registry bell,” and that unchanged JSON stays logically compatible but loses epistemic precision. Do not cite it as a map of the proposed person wording.
- `.shokunin/lore/corpus/fixtures/r34-tarin-hearsay/modality-contrast-map.md:1-10` already distinguishes a source reporting hearsay from fixed rows claiming direct sight, while cautioning that mismatch does not make the record false. This is additional precedent for source/record mismatch, albeit not tentative personal identification.

## Bound distinctions

1. **Source wording:** In the hypothetical, Jorin reports a visual encounter and his tentative identification of the encountered person. It does not directly identify that person as Vela. The tentativeness is about *who the person was*, not whether Jorin saw someone.
2. **Citation/record support:** `jorin-note` can cite Jorin’s account, but a citation pointer does not upgrade “someone I took to be Vela” into direct source identification of Vela. The fixed `vela` subject ID / Vela-named claim and timeline description would overstate what that excerpt directly identifies. At most the report is compatible with Vela being the person; it is not established false or logically incompatible. An editorial map may label the proposed alignment as tentative, but must not imply a uniquely resolved identity.
3. **Canon/world fact:** Neither the existing excerpt nor the hypothetical authenticates Jorin, Vela, the sighting, or the identification. There is no objective evidence the person was not Vela. Nor does a matching Bell-7 label establish a shared occasion, simultaneity, or a bell sounding (`jorin-clause-map.md:8-10`). No canon conclusion follows.

## Risks / novelty challenge

The strongest novelty objection is that r41 already teaches the exact calibration lesson: distinguish a tentative source identification from a direct one; unchanged JSON may remain logically compatible while overstating or under-preserving the source’s epistemic precision. Swapping *sound* for *person* is a useful instance but may not materially improve calibration as a distinct general rule. r34 additionally covers mismatch between source modality and direct-observation records. The counterargument is narrower: person identity is a distinct subject-resolution problem, and an entity ID can encode a stronger identity claim than the narrator warrants. That distinction may merit a regression case only if a reviewer can state a different expected decision than the r41 precedent, rather than merely rephrase its outcome.

Do not claim the source directly identifies Vela under the hypothetical; do not claim it proves a non-Vela; do not merge Jorin’s occasion with Vela’s account; do not claim canon. “No objective non-Vela, shared occasion or canon” is the evidence boundary, not a conclusion that the tentative person was different.

## Falsifiable gate

**Go only if** an independent reviewer, blind to the proposed expected result, explains a materially distinct person-ID decision (not just the r41 tentative/direct calibration rule), and can specify a reproducible record consequence that preserves uncertainty without declaring fixed JSON false. **No-go** if the only outcome is “compatible but source overstates certainty,” already demonstrated by r41, or if the case requires asserting a different person, shared occasion, or canon. This scout recommends no-go absent that distinct outcome.
