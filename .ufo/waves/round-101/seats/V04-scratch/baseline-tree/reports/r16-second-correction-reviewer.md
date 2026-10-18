# Round 16 second-correction review — non-author

## Scope

I inspected the second correction record, both earlier rejection/review artifacts, the four round-16 fixture inputs, the fixture README, checker, and current raw outputs. I made no source or fixture edits. This review is limited to the replacement description `Fixture input: Mira's place is unspecified at tick 7.` and the requested four-case replay.

## Description judgment

The phrase avoids both previously identified claims, with an important scope distinction. “Fixture input:” explicitly frames the sentence as a description of the test input, not as quoted or reported content from `courier-log`; the fact that the row separately has `source_id: "courier-log"` does not override that explicit framing. It also names no known place (Harbor, Tower, or otherwise), and does not say that `unlisted` resolves to any location. In context, “Mira's place is unspecified” describes the place field of this fixture row, not all possible records about Mira at tick 7: the control events still identify their own `harbor` and `tower` IDs.

The description is somewhat less precise than `Fixture input row: place_id is unlisted (unresolved).` because it omits the key itself and could be read broadly if detached from its row. In its actual timeline-row context, however, the prefix and the row's `place_id: "unlisted"` make the intended scope clear. I find it sufficiently clear to remove the first correction review's source-attestation concern and the original known-place contradiction. It is fixture prose, not evidence about the fictional source or canon.

## Four-case replay

Ran the checker on each current fixture. Results match the expected narrow behavior:

- `r16-valid-places`: reports `mira` double-booked between `harbor` and `tower`.
- `r16-missing-place`: reports dangling `unlisted`; no double-booking assertion.
- `r16-missing-first`: reports dangling `unlisted`; no double-booking assertion.
- `r16-mixed-three`: reports dangling middle `unlisted` and retains the known `harbor`/`tower` double-booking.

The unresolved row is withheld from the different-resolved-place comparison; its actual location and any conflict involving it remain unassessed, not disproved. The checker does not read descriptions or infer source-text support from the source ID. The correction report supplies first-to-second hashes; the correction verifier directly confirmed second-correction hashes and matching 33 saved CLI transcripts. As that verifier notes, the pre-correction hashes for these newly added fixtures cannot be independently reconstructed from baseline bytes. This provenance limitation remains; the replay establishes current reproducibility, not pre-correction provenance.

## Residual limitations

The behavior is not a general resolved-place rule. A uniquely identified wrong-kind entity (for example `mira`) still gets a “not a place” diagnostic but can enter raw-ID occupancy comparison; duplicate/ambiguous place IDs likewise still get their diagnostic and can enter the comparison. These are explicitly documented as out of scope and should not be hidden by the narrow admission. Suppressing a zero-match location does not establish that no real conflict exists. The selected mixed-three case shows the known pair survives in this event order, not general pairwise semantics for every arrangement.

## Recommendation

**Admit the second correction for fresh readjudication; recommend the round's narrow calibration move, with no axis claim beyond calibration improved, depth and coverage unchanged, and no harm found in the reviewed evidence.** The fixture-scoped wording now avoids both the concrete known-place misdescription and an attribution that the courier-log text attests the missing ID. Keep the duplicate-place and wrong-kind occupancy limitations, unresolved-conflict uncertainty, and unrecoverable pre-correction hash provenance explicit. This is not a source-truth, canon, or general location-resolution claim.
