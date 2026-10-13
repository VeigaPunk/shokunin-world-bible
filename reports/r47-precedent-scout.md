# Round 47 precedent scout

## Judgment: NO-GO on material depth novelty

An intake slip can supply another attributed documentary form, but the proposed content does not add a distinct evidence relation beyond already represented presence, report provenance, and absence-of-record language. A new source title or row is not depth by itself. The proposal should not be implemented as an asserted cross-account object match.

## Precedent comparison

| Precedent | What is actually represented | Implication for proposed slip |
|---|---|---|
| r10 | `corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md:1-5` labels the excerpt invented fiction and says Sella recorded seeing Mira leave while leaving destination blank. `sources.json` identifies it as a fictional handwritten register; `timeline.json` has a `registry-entry` event sourced to it. | Already exercises documentary/carbon provenance, witness attribution and an intentionally blank record. A new registry document is not, without a novel relation, depth. |
| r23 | `corpus/fixtures/r23-note-class/sella-absence-note-excerpt.md:1-7` is newly authored fiction; Sella reports looking for a named strip and not finding it, explicitly not proving world-absence. `timeline.json` maps this as a sourced report. | Already represents narrow record/search absence and the distinction between non-finding and fact. “Depositor not recorded” resembles this known absence-of-record class. |
| r33 | `corpus/fixtures/r33-tarin-envelope/tarin-note-excerpt.md:1` says Tarin saw Sella place an unlabeled envelope on the registry desk. `clause-map.md:7-13` aligns reporter, reported sighting, Sella, envelope, and desk, while saying this is only reported observation. | The exact object, desk, attribution, and observation content are already present. A second invented report that an envelope lay there is repetition unless it supports a carefully bounded *same-object* or independently meaningful cross-account relation—which these facts do not establish. |
| r35 | `corpus/fixtures/r35-bell7-conflict/tarin-note-excerpt.md:1-3`; `manual-clause-pointer-map.md:3,9-17` add a named occasion and retain conflicting Sella-attributed reports conditionally, while expressly leaving object identity/ownership and authentication unresolved. | Occasion qualification and conditional cross-account comparison are prior art. A slip saying “during Bell-7” does not independently identify the same event; it is another authored claim. |
| r43 | `corpus/fixtures/r43-jorin-vela-sighting/jorin-note-excerpt.md:1`; `jorin-clause-map.md` (search excerpt clauses) treats Jorin’s claimed sighting and Bell-7 label as attributed, conditional on common place/occasion, and not corroboration. `timeline.json` records reporter Jorin, broad scene Harbor, source Jorin note. | A second account and same occasion label do not prove common occasion or corroboration. The same epistemic limit applies more strongly to an envelope at a desk. |

## Distinct depth assessment

**Depth: unchanged / candidate not admitted.** “Documentary slip” is a medium/class label; an attributed object-presence row would reuse existing sourced event/claim representation (r10/r33), while “depositor not recorded” reuses an absence-of-record/report limit (r10/r23). If the slip merely says an unlabeled envelope was on the desk, its novel contribution is one more in-world assertion, not a demonstrated new documentary or witness capability. If it explicitly cross-compares with Tarin, it must not imply the same envelope or occasion. That leaves no supported new relation to map.

The apparent report is not independent corroboration: it is newly invented in-world text, not recovered/authenticated evidence. An envelope-at-desk report does not identify its depositor, prove it is Tarin’s envelope, establish a common occasion, support that Sella placed it, or settle canon, rights, or truth. “No depositor recorded” states a limit of the slip’s record only; it does not prove no depositor, Sella’s absence, or Tarin’s accuracy.

## Falsifiable go/no-go

**No-go** unless an independently reviewable source clause supplies a specific, non-inferential relation that is absent from r10/r23/r33/r35/r43, and a clause-to-field map can encode that relation without assuming depositor identity, envelope identity, shared occasion, or source authenticity. A proposed test would fail this criterion if reviewers cannot point to that relation in exact source text, or if the mapping makes any of those unsupported bridges. Merely adding a slip/source/item/event, reporting “depositor not recorded,” or obtaining a CLEAN structural check is not a pass. If reconsidered, compare against controls that preserve Tarin’s report and do not turn a shared label/location into same-envelope evidence.

No fixture/checker/README/LOG change is recommended. No checker result is asserted. Calibration and coverage unchanged; depth unchanged. This is a novelty assessment, not a judgment that either fictional report is true or false.
