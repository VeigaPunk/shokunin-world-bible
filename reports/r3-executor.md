# Round 3 executor report — required contradiction ledger

## Implementation

`check_bible.py` now treats `contradictions.json` as a universal fifth required JSON-array section. Each row requires a unique `id`, object-valued `claim_a` / `claim_b`, and nonempty `why`. A claim side is `{event_id, field}`; permitted fields are `place_id`, `tick`, and `depends_on`. Each event reference must resolve to exactly one timeline row whose `source_id` resolves in `sources.json`. Identical references are rejected. Ledger ID duplicates use the checker's standard duplicate-ID diagnostic. The standard loader still emits `cannot load JSON` for a missing file.

The validator checks structure and references only. It does not decide whether claims contradict, assess whether citations support them, alter rows, or infer a second side for the dangling `missing-map` relation. The two existing ledger rows point to the timeline claims; that dangling relation remains outside the ledger.

## Existing case replay

Ran once from repository root after the fifth files were present:

| Fixture | Exit | Result |
|---|---:|---|
| `consistent` | 0 | Clean |
| `contradictions` | 1 | Original three findings preserved: dangling `missing-map`, `arrival` dependency inversion against `later`, and Mira double-booked at tick 2 (`tower` / `harbor`); no ledger finding |
| `ally-reciprocal` | 0 | Clean |
| `ally-one-way` | 1 | Original missing reciprocal alliance finding |
| `contradictions-ledger-malformed` | 1 | Ledger-local unresolved `absent-event` reference plus the original three contradiction-fixture findings (4 total) |

## Malformed-input probes

Temporary copies of `consistent` were probed; repository fixtures were not changed. Missing `contradictions.json` exits 1 with `contradictions.json: cannot load JSON` (including the OS missing-file detail). A scalar ledger row exits 1 with `contradictions[0]: expected object`. A string in `claim_a` exits 1 with a row-local required-dict diagnostic. Invalid fields exit 1 with a side-local allowed-fields diagnostic; identical invalid references additionally produce the distinct-reference diagnostic. Replacing a timeline row with a string exits 1 with `timeline[0]: expected object`. All probes completed without a crash. Diagnostics may be multiple when one malformed input violates multiple checks; malformed base rows are skipped rather than dereferenced.

These tests establish malformed-shape handling for the probed cases, not exhaustive malformed-input coverage. A resolvable row citation is only pointer resolution, not proof of source support or truth. No canon was rewritten.
