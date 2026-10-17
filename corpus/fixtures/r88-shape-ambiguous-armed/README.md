# Round 88 F1: shape-invalid ambiguous holder arms the stop

Purpose: pin the r87 shape-ambiguous residual with a fixture-local duplicate holder id. Record `[0]` has the ambiguous `to_holder` and an extra key; record `[1]` is shape-valid but its non-null `from_holder` would violate the first-record chain rule if assessed after the malformed record reset.

## Expected after the C1 fix (verified at closure — follow-up seats V2/JCAL3 line-by-line)

- Checker exit: `1` (intentional duplicate entity id and provenance shape violation remain findings).
- The shape-invalid dict at `entities[4].provenance[0]` still reports its exact-key violation and its ambiguous `to_holder` `f1-shape-dup`.
- The ambiguous holder arms the provenance stop despite the shape violation. A disclosure at `[0]` and every later record `[1]` names the record's complete simultaneous causes — `malformed record (unexpected field set); ambiguous holder identity to_holder 'f1-shape-dup'` — with the origin `[0]` (parent precedence amendment, committed with the C1 fix).
- Record `[1]` remains unassessed: do not report its otherwise applicable first-record chain break.

These are post-fix expectations, not measurements against the unpatched checker. The delivered baseline run is recorded in `.ufo/waves/round-88/F1.md`; recheck these expectations against the integrated revision.

Verified on the delivered tree at r88 closure (follow-up seat V2, line-by-line): expectations hold, exit 1, 5 findings.
