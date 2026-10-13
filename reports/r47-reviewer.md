# Round 47 non-author reviewer — intake-slip depth decision

## Decision: NO-GO

The unbuilt invented intake slip does not demonstrate material object-centered depth beyond existing records without relying on a bridge the proposal expressly disallows. A separate report that an envelope lay on the registry desk, with no depositor entry, is a potentially distinct *documentary detail*, but it does not establish that the described object is Tarin’s envelope or that the slip and Tarin concern the same Bell-7 occasion. Without either link, the comparison is two generic attributed reports at a shared named location—not an object-specific evidentiary relation. The blank depositor field adds a local record limitation, not an identity, placement, or absence fact. This is insufficient for the declared depth claim.

This is an independent review of the proposal, not an execution result. No candidate fixture was constructed or run; no checker output or regression replay is claimed.

## Precedent and source comparison

- **R10** (`reports/r10-reviewer.md`; `corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md`) already represents an invented registry record, a recorded observation, and intentionally blank registry information. That precedent makes “it is an intake slip” or “it leaves a field blank” insufficient novelty on its own.
- **R23** (`reports/r23-reviewer.md`; `corpus/fixtures/r23-note-class/sella-absence-note-excerpt.md`) already distinguishes an authored, speaker-bounded non-finding from proof of world absence. “Depositor not recorded on this slip” is narrower, but similarly document-bounded; it cannot mean no depositor existed or no one placed an envelope.
- **R33** (`corpus/fixtures/r33-tarin-envelope/tarin-note-excerpt.md:1`, and its `clause-map.md`) already has Tarin report seeing Sella place an unlabeled paper envelope at the registry desk. The map cautions that the envelope is not separately identified. A second envelope-at-desk statement does not make the two referents identical.
- **R35** (`corpus/fixtures/r35-bell7-conflict/manual-clause-pointer-map.md`; `contradictions.json`) preserves attributed, conditional accounts around Bell-7. The label and local tick do not authenticate or synchronize occasions; the existing ledger concerns the Sella-location conflict, not a verified envelope identity.
- **R43** (`corpus/fixtures/r43-jorin-vela-sighting/` and `jorin-clause-map.md`) shows that another authored sighting and a Bell-7 label do not establish a common occasion or corroboration. It supplies no envelope identity relation.

The proposed slip can be cited to support only its own authored wording: its writer reports envelope-presence at the desk and reports that the slip contains no depositor entry. A feasible `sources.json` reference, item row, or reporter-attributed event would be an editorial representation of that report. A structurally valid source citation is not proof the prose entails every mapped field, that the document existed or is authentic, that accounts are independent, or that the envelope is the same one. In particular, shared noun (“envelope”), place (“registry desk”), or writer-supplied “Bell-7” cannot supply the missing object/occasion key.

## Axis judgment and risks

- **Depth: unchanged / rejected.** No material, distinct object-centered relation survives removal of same-envelope and same-occasion assumptions. A format change, one more source, and one more presence row are not depth by themselves. The unrecorded depositor may add a bounded detail, but its relation to Tarin’s report is not grounded beyond co-location and generic description.
- **Coverage: unchanged.** No checker rule or detectable validation class is added by the proposal.
- **Calibration: unchanged.** Stating limits is prudent, but it does not demonstrate a calibration improvement. Main risk is false precision: treating a feasible citation or CLEAN checker result as semantic verification, or converting “not recorded” into objective absence.

Other risks: attributing the envelope to Sella or any depositor; treating Bell-7 as a shared/verified event; conflating an event actor with a depositor or mover; presenting authored fiction as recovered corroboration or canon. These inferences would overstate the source.

## Falsifier / reconsideration bar

Reconsider only if exact proposed excerpt clauses and a source-to-field map let a non-author identify a concrete narrative function that remains materially useful when the envelope identity and Bell-7 occasion are both unknown—and that is more than another report plus a blank field. Any purported function that fails when either identity/occasion assumption is withheld, or any row that asserts unsupported actor, depositor, same-object, same-event, truth, or canon, falsifies the case. A structural citation/checker pass cannot satisfy this bar; it establishes only the implemented structural/reference checks, not textual entailment or verified object linkage.
