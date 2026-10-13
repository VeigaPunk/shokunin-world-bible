# Round 47 scribe — manual clause/source/object comparison

## Evidence boundary

This is a proposed object-specific comparison, not evidence that the proposed slip exists in-world beyond its authored fixture text. The r47 declaration calls it newly authored fictional material and explicitly withholds depositor identity, object identity, occasion identity, support for Sella's placement, source authentication, and canon (`LOG.md:788-790`). No checker output can establish those semantic facts: prior r43 evidence calls its clean result structural and non-authenticating (`LOG.md:726,730-734`).

## Manual clause-to-record table

| Proposed clause / field | Evidentiary source | Narrow support / limit |
|---|---|---|
| “an unlabeled paper envelope lay on the Lantern Harbor registry desk” | Proposed newly authored intake-slip excerpt; source metadata row `registry-intake-slip`; item row `envelope` and cited entity claim | The slip's writer reports desk-presence of an envelope. It does not identify that object with the envelope Tarin reports, and does not assert who placed it. This is source-text support conditional on the editorial source-to-row mapping, not external verification. |
| “during what I called Bell-7” | Same proposed excerpt | Only the writer's label. It does not establish that the slip and Tarin refer to the same ringing or occasion. Bell-7/date wording is treated as fictional source claim, not an authenticated time. |
| “the depositor was not recorded” | Same proposed excerpt; corresponding item/claim or event wording, if represented | Supports only the writer's report that the slip lacks a depositor entry. It does not prove there was no depositor, that Sella was absent, or that Tarin's reported placement occurred. |
| `first_appearance: registry-intake-slip` (if used on item) | Proposed source ID | Fixture index/reference, not a historical first appearance and not proof of object's identity across reports. |
| event actor/source/place/tick (if an event is retained) | Proposed excerpt/source, with Jorin only if the slip text itself makes him its reporter | Actor must represent the person/reporting perspective actually named by prose; do not set the envelope as mover. Harbor is a broad editorial place alignment only where prose specifies the desk. Tick is local ordering, never Bell-7 conversion or simultaneity. |
| Comparison with Tarin's account | `r33-tarin-envelope/tarin-note-excerpt.md:1`; r35's mapped Bell-7 clause at `r35-bell7-conflict/manual-clause-pointer-map.md:9` | Tarin reports seeing Sella place an unlabeled paper envelope at the desk. The proposed slip separately reports desk presence and missing depositor record. Similar descriptors and location do not establish same envelope, occasion, depositor, placement, or corroboration. |

## Cross-account decision

**Go only** for a narrowly labeled editorial juxtaposition: two attributed fictional accounts concern an envelope-like object at the same named desk, with the slip reporting no depositor entry; identity, shared Bell-7 occasion, and any link to Sella remain unknown. It may offer a distinct record-shaped uncertainty (presence reported, entry's depositor blank) rather than simply another character witness, but it is a fragile depth claim and should be rejected if the actual excerpt/rows merely duplicate Tarin's assertion or imply identity/common occasion. The declared falsifier is explicit in `LOG.md:790`: no identification of the envelopes/occasions and no support that Sella placed it.

**No-go** if the proposed excerpt says or the table implies “the same envelope,” “same occasion,” “Sella deposited/placed it,” or treats the unrecorded depositor as proof nobody placed it. Do not create a contradiction pair: the slip does not conflict with Tarin's report and cannot resolve r35's conditional Sella-location ledger. A structurally clean checker run, if later made, checks schema/reference rules only; it cannot validate prose, provenance, source truth, rights, or canon.

## Axis assessment (distinct axes)

- **Depth: unproven / conditional candidate.** Potential gain is a source-attributed documentary absence-of-entry attached to reported object-presence, compared with Tarin's direct placement report. This is more than a row/source count only if the bounded contrast is preserved and reviewer finds the record-shaped uncertainty narratively material. Not yet an observed or admitted gain from this scribe analysis.
- **Coverage: unchanged.** No checker rule or input-validation case is proposed; no branch coverage claim follows from the new fictional text.
- **Calibration: unchanged.** No decision threshold, structural diagnostic, or source-truth criterion is tested. The table explicitly prevents overreading but is not a checker calibration result.

## Falsifiable acceptance test

A non-author reviewer can falsify the proposed depth move by tracing each eventual new JSON assertion to the exact authored clause and finding unsupported assertions, an implied same-envelope/same-occasion bridge, depositor attribution, or no material distinction from another witness row. Acceptance requires a manual clause/source map with those limits, exact alignment of excerpt and rows, and an independent finding that the documentary non-entry detail adds material narrative information. Reject if any such implication is present or the distinction is only additional row count. No source authentication, rights grant, canon fact, or real-world corroboration is claimed.
