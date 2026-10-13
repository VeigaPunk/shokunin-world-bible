# Round 34 modality scout — seeing versus hearing

## Calibration claim

A direct-sighting assertion requires a source that reports the witness saw the act. A source that says the witness heard that the act occurred supports only the witness’s report of hearing a proposition; it does not support the separate claim that the witness saw the act. That difference is evidentiary modality, not a finding that the act did not happen. Do not treat hearsay as direct observation, and do not treat lack of direct-sighting support as proof of falsity.

## Evidence and boundary

- The r34 round declaration describes r33’s excerpt as “I, Tarin, saw Sella place...” and notes that the cited character/event rows say Tarin **reports seeing** (`.shokunin/lore/LOG.md:531`).
- Exact r33 prose is one sentence: “I, Tarin, saw Sella place an unlabeled paper envelope on the Lantern Harbor registry desk” (`.shokunin/lore/corpus/fixtures/r33-tarin-envelope/tarin-note-excerpt.md:1`). The verb is “saw,” not “heard [that]”.
- The manual map expressly scopes “saw” to Tarin’s reported observation and says it does not independently verify the world event; it treats IDs as editorial alignments and tick 3 as an arbitrary local label (`.shokunin/lore/corpus/fixtures/r33-tarin-envelope/clause-map.md:7-12`).
- The source metadata calls Tarin’s note a fictional first-person note, reporting his observation rather than omniscient truth (`.shokunin/lore/corpus/fixtures/r33-tarin-envelope/sources.json:15-18`).
- Both new character claims preserve that attribution: Tarin “reports seeing” and Tarin “reports that Sella placed” the envelope (`.shokunin/lore/corpus/fixtures/r33-tarin-envelope/entities.json:51-60,63-71`). The event likewise says “Tarin reports seeing” and cites `tarin-note` (`.shokunin/lore/corpus/fixtures/r33-tarin-envelope/timeline.json:23-29`).
- The r34 hypothesis explicitly holds r33’s five JSON tables fixed and changes only the excerpt sentence to “I, Tarin, heard that Sella placed...” (`.shokunin/lore/LOG.md:532`). This isolates the modality cue; the changed excerpt no longer entails `reports seeing` even though the structural JSON and source ID remain unchanged. The log says both cases structurally exit 0; structural acceptance is not prose support (`.shokunin/lore/LOG.md:532`).
- The checker’s prose limitation and the need for manual evidence review are recorded in the r33 observation policy (`.shokunin/lore/LOG.md:518-519`). Thus no checker result can decide this distinction.

## Risks

1. Lexical substitution may be overgeneralized: “heard” can describe acoustic perception of the act itself, but this controlled near-miss specifically says “heard **that** Sella placed,” a reported proposition. The contrast must stay tied to the exact wording.
2. Retaining `reports seeing` JSON after changing its sole prose excerpt creates an unsupported assertion, not an established false one. Do not say Sella did not place the envelope, or that Tarin’s hearsay is false.
3. A clean checker exit may be mistaken for entailment; it checks structure/references, not the excerpt’s modality.
4. Do not infer source reliability, independent corroboration, contents/recipient/ownership of the envelope, timing beyond fixture-local tick, or canon from either wording.

## Falsifiable check

Give a non-author reviewer the r33 excerpt/map and a prose-only near-miss with the excerpt changed exactly as specified in `.shokunin/lore/LOG.md:532`, while keeping all five JSON tables byte-identical. Without seeing a preferred verdict, ask the reviewer to classify whether the source supports (a) Tarin reports seeing the placement, (b) Tarin reports hearing the proposition that Sella placed it, or (c) neither; require a cited verb/phrase and prohibit a truth/falsity verdict about the placement. The calibration claim fails if the reviewer accepts the near-miss as direct-sighting support, calls the placement false solely because it is hearsay, or cannot distinguish the two phrasings. Expected: r33 supports (a), near-miss supports (b) only. Structural checker status is recorded separately and is not the criterion.
