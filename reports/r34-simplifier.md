# Round 34 simplifier — smallest negative artifact

## Minimum fixture-only proposal

Use a separate `.shokunin/lore/corpus/fixtures/r34-tarin-hearsay/` directory copied from `r33-tarin-envelope/`. Preserve all five JSON tables byte-for-byte; change only the excerpt sentence to: “I, Tarin, heard that Sella placed an unlabeled paper envelope on the Lantern Harbor registry desk.” Retain the existing clause map only if it is revised to mark the proposition as hearsay; do not describe the wording as Tarin witnessing placement. This is the smallest controlled negative: one prose modality substitution, with source IDs and structured assertions held fixed. The excerpt is at `r33-tarin-envelope/tarin-note-excerpt.md:1`; the r33 character claims say “reports seeing” / “reports that Sella placed” (`entities.json:51-70`), and its event says “reports seeing” (`timeline.json:23-29`).

## Calibration boundary and risks

The altered sentence supports that Tarin says they heard an assertion about Sella; it does not support Tarin directly seeing the placement. It does not establish whether the placement happened, whether the hearsay is true, or that any r33 JSON assertion is canonically false. Because the cloned JSON remains unchanged, structural checker success would not validate the prose/claim fit; the intentional mismatch is the negative test. Avoid converting “heard that” into a false-world finding, or inferring envelope contents, ownership, recipient, motive, canon, or rights/provenance. A weaker risk is over-reading the map as checker evidence: it is manual review material only.

## Falsifiable check

A non-author reviewer compares the unchanged r33 claims/event with the changed excerpt and must classify r33 as direct-observation wording conditional on its authored source, but r34 only as hearsay—not direct-sighting support—and must not call the hearsay false or the JSON false. If the reviewer accepts r34 as direct sighting, or rejects the distinction without textual grounds, the calibration claim fails. Verify the only semantic change is the excerpt sentence and both fixtures remain structurally accepted; unchanged JSON tables must compare byte-for-byte. No prior-fixture regression claim is made by this proposal.

Scope: report only; no fixture, checker, README, LOG, or commit changes.
