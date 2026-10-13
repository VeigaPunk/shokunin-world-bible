# Round 39 scribe — unknown versus ambiguous ledger source

## Decision table

| Event pointer | Event `source_id` count in valid `sources` rows | Ledger-side result | Meaning |
|---|---:|---|---|
| Exactly one timeline event | 0 (unknown) | `contradictions[i].claim_{a,b}: event '<id>' has no resolvable source_id` | The selected event cannot be linked to any valid source row. It is not evidence the event or testimony is false. |
| Exactly one timeline event | 1 (unique) | No source-status diagnostic at that ledger side | Structural source linkage only; not excerpt support or authenticity. |
| Exactly one timeline event | >1 (ambiguous) | `contradictions[i].claim_{a,b}.source_id: ambiguous in-world source '<id>'` | A duplicate identifier prevents a unique source selection; no row is chosen. |
| 0 or >1 timeline events | Any | `.event_id: expected exactly one timeline event '<id>'`; source-status check is skipped | Event identity failure precedes source classification. Do not conflate unknown event with unknown source. |

## Evidence and novelty boundary

Checker control flow explicitly validates event cardinality before looking up its event source (`corpus/fixtures/check_bible.py:92-100`); status counts distinguish zero/one/multiple valid source rows (`:53-66`). Unknown produces the ledger-specific message, whereas ambiguous calls the ordinary local source diagnostic (`:97-100`). The generic source helper likewise distinguishes unknown from ambiguous (`:68-74`).

The r7 reviewer documented an actual temporary ledger ambiguity probe on `claim_a`, including duplicate `archive-ledger`, and explicitly contrasts the unknown wording (`reports/r7-reviewer.md`, “Contradiction-ledger ambiguity probe” and “Reference-site inspection”). R38's source scout describes the same two branches and unique-event prerequisite (`reports/r38-source-scout.md`, first bullet); R38 adjudicator rejected source-ambiguity coverage as already reached by r7 (`reports/r38-axis-adjudicator.md`, Coverage row). Therefore **ambiguity is already tested**. The LOG r39 declaration claims no prior unknown-source ledger probe, but a repository-report search finds prior references to the checker branch, not an executed unknown-source ledger probe; r7's probe is explicitly ambiguous, not unknown. This candidate is not safely novel until temporary probes outside reports are ruled out. Do not claim new checker behavior from a fixture alone.

## Candidate and falsifiable check

A bounded candidate is a clean r35-derived control and a negative differing only in the unique `sella-bell7-presence` timeline event's `source_id`, changed to absent ID `missing-sella-note`. Preserve event IDs, sources, excerpts, and ledger sides. Expected negative: the ledger `claim_b` gets the exact no-resolvable-source finding above, while the timeline reference independently gets its unknown-source finding. Inventory the full output; no source row should be inferred or substituted. Falsify the candidate if the control is not clean, the event pointer is not unique, the exact ledger-side unknown-source finding is absent, it instead says ambiguous, or any unplanned file changes. If any prior temporary or committed probe already exercised this unknown ledger branch, classify coverage unchanged/reject rather than repeat r38's novelty error.

## Risks / limits

Unknown is not ambiguity: zero matches says no valid row resolves the identifier; multiple matches say identity cannot be uniquely selected. Invalid source rows may be excluded from valid source counts (`check_bible.py:53-66`), so malformed rows need separate accounting. The timeline may independently report the same missing ID; that is collateral visibility, not a second witness. Neither result establishes whether Sella was present, whether the excerpt supports the event, whether either report is authentic, or which account is canon. Checker diagnostics are structural reference checks only.
