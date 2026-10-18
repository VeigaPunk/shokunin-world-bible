# Round 34 critic — modality calibration

## Assessment

The proposed negative control is directionally valid: the r33 excerpt's “saw” supports Tarin's reported visual observation, while “heard that” conveys acquisition of a proposition from another speaker/channel and does not support direct sight. It is a near-miss for the *evidence modality*, not counterevidence that Sella did not place the envelope. Do not label its underlying placement claim false or even necessarily unsupported in the wider corpus; only unsupported as direct-sighting evidence.

## Calibration risks

- JSON-preserving pair is useful: r33 `tarin-note-excerpt.md:1` says “I, Tarin, saw Sella place...” whereas its entity claims explicitly encode “Tarin reports seeing” and “Tarin reports that Sella placed...” (`entities.json:57-70`); event likewise states “Tarin reports seeing” (`timeline.json:23-29`). If only the prose changes to “heard that,” those assertions become mismatched to that excerpt as direct observation. The checker cannot reveal this: LOG r34 explicitly notes prose is ignored (`LOG.md:531-532`).
- “Heard that” can mean a report was received, but leaves the original informant, whether the informant personally witnessed anything, transmission chain, time, and reliability unstated. It neither entails that the informant saw the act nor rules that out. Therefore classify as *hearsay/secondhand assertion; no direct-sighting support*, not “no eyewitness existed” or “Sella did not place it.”
- Exact one-sentence substitution controls lexical modality but the test can be overfit to the verbs “saw/heard.” A future prose variant (“Tarin was told…”, “word reached Tarin…”) should receive the same no-direct-sight judgment; conversely a statement that names an actual observer does not automatically become Tarin's direct observation.
- Keep the assessment bounded to the changed excerpt and fixed citation ID. Preserve the distinction between excerpt support, editorial ID alignment, and truth/canon. Existing copied claims unrelated to Tarin remain baseline, not newly supported by the replacement note.

## Falsifiable check

Blind a non-author to the expected result and present the r33 excerpt/rows and the proposed heard-that excerpt with the same JSON rows. For each, require separate answers: (1) does this excerpt support Tarin reporting *directly seeing* the placement? (2) does it report a placement assertion reaching Tarin by some non-specified route? (3) does it establish whether the placement actually occurred? Pass calibration only if r33 gets yes/yes/not established, while the near-miss gets no/yes/not established; fail if the near-miss is treated as direct observation, as denial of the event, or as adjudication of hearsay truth. Check the event/entity language—not just a prose label—and verify the unchanged rows/citations do not silently convert the near-miss into eyewitness evidence. Both checker passes, if run, prove structural validity only, not these judgments (`LOG.md:531-532`).

No envelope contents, recipient, owner, Blue Seal/carbon/route-strip link, canon truth, or rights/game-mechanics conclusion follows.
