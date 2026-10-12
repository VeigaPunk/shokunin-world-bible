# Round 3 reviewer — contradiction ledger

## Scope and replay

Read the round-3 declaration/clarification in `.shokunin/lore/LOG.md`, checker and fixture README, decision table, r3 scout/executor reports, and saved run outputs under `corpus/live/runs/20261012T162704Z/`. Independently replayed all five fixture directories using the documented Python command. Results matched the saved run evidence:

| Fixture | Exit | Findings |
|---|---:|---|
| `consistent` | 0 | clean |
| `contradictions` | 1 | original three diagnostics, unchanged |
| `ally-reciprocal` | 0 | clean |
| `ally-one-way` | 1 | original missing-reciprocal diagnostic |
| `contradictions-ledger-malformed` | 1 | one unresolved ledger event plus the original three diagnostics |

Also used temporary copies (no fixture edits) to test a missing ledger file, scalar ledger row, string-valued claim side, and unsupported field. Each exited 1 with a diagnostic and no crash. Existing contradiction and alliance outputs show no observed regression. The required fifth file is an intentional schema change documented in README/LOG; fixtures without asserted pairs explicitly use `[]`.

## Findings

- **No blocking implementation defect found in reviewed/replayed cases.** Ledger rows require `id`, object sides, and nonempty `why`; each side is checked against the allowed event fields and a uniquely occurring timeline event. The event's source ID must resolve. Duplicate event IDs are rejected as pointer targets. Ordinary schema/citation/consistency diagnostics still run; malformed references do not suppress the three seeded findings or choose a winner.
- The contradictory fixture contains two ledger pairs, not three. This matches the post-scout clarification: the dangling `missing-map` relation has no second cited assertion and remains outside the ledger. The third original checker diagnostic is preserved. The round-3 claim should continue to be read with this explicit boundary, not as ledger coverage of every violation.
- **Evidence supports structural pointers/citations, not semantic truth or entailment.** `why` is checked for nonempty text only; the checker does not prove that the two selected fields conflict or that a source supports its event assertion. The README and decision table state these limits accurately. In particular, the dependency pointer is an event's `depends_on` field, not an independently verified source quotation. Do not describe ledger validation as semantic contradiction verification or proof that the citations support the claims.
- The `claim_a`/`claim_b` objects allow extra keys, but the documented representation only promises event ID and field; this is not a meaningful correctness issue for current fixtures. The checker does not enforce the fixture README's narrow statement that two references are distinct except by exact `(event_id, field)` equality; that is the implemented and documented rule.

## Review verdict

For the declared, clarified scope, no crash or regression was observed and the saved evidence replayed. The depth claim is defensible narrowly as adding explicit, source-resolving editorial pointers while retaining the conflicting records and existing diagnostics; it is not evidence of deeper semantic validation. I found no basis to claim exhaustive malformed-input coverage. No files were changed except this report.
