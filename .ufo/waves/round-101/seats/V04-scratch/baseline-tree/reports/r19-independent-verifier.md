# Round 19 independent verifier report

## Scope and method

Independent verification only; no checker, fixture, documentation, or shared-log edits. I used baseline report commit `9ee1e6eb18b7813a6fe2eda175d891b5d7f55308`, extracted its checker to `/tmp/r19-independent-baseline-check.py`, and ran the baseline and working-tree checkers from the repository root. Baseline checker SHA-256: `8ad6848022410e8c8519e0fffde55c4e96bab594fdc6895574c0eb7efe11997e`; current checker SHA-256: `9ab0679201218b45f006847be27c972fe244ba1b9577fe82483b233238ae27e`.

## Fixture integrity and replay

- Enumerated the baseline commit's tracked `.json` paths under `.shokunin/lore/corpus/fixtures`: **224 paths**. Compared each baseline `git show` byte stream with its working-tree file: **224/224 byte-identical**, no missing or changed paths. This checks those fixture JSON files only, not all repository files.
- Replayed each of the **45 pre-round-19** saved CLI cases in `corpus/live/runs/20261012T185657Z/` against both baseline and current checkers. For every case, baseline and current each matched the saved exit code, stdout bytes, and stderr bytes, and matched each other: **45/45 exact**, no mismatches.
- Replayed all **49** saved transcripts in `corpus/live/runs/20261012T190807Z/` against the current checker: **49/49 exact** on exit code, stdout, and stderr. The 45 earlier cases and four r19 cases all matched; stderr was empty throughout.

## Paired fixtures and controls

The `r19-negative-tick` and `r19-valid-tick` directories differ only in `timeline.json`; all other JSON files are byte-identical. Their two rows have the same actor (`mira`), distinct uniquely indexed place IDs (`tower`, `harbor`), and otherwise matching fields; both ticks change from `-1` to `9`. Baseline output for the negative pair includes both `must be nonnegative` findings **and** `double-booked` at tick -1. Current output retains the two invalid-tick findings and withholds only that negative-tick double-booking. Both baseline and current retain the positive-control tick-9 double-booking.

The `r19-valid-around-negative` and `r19-negative-first-valid` controls also differ only in `timeline.json`. They place a valid tick-9 known-place pair around or after a negative-tick row. Both checkers retain the negative row's `must be nonnegative` diagnostic and the valid tick-9 `double-booked` finding across the invalid row. This confirms the tested valid pair is not suppressed by an intervening negative row or by a negative first row.

I additionally made a temporary, uncommitted dependency probe by adding a dependency from the accepted negative-tick event to the later tick-9 event in `r19-valid-around-negative`. Baseline and current outputs were byte-identical: both retained the negative tick diagnostic and the existing timeline-inversion diagnostic (`tick 9 not before tick -1`), as well as the valid tick-9 pair's booking finding. The temporary probe was removed. This checks one negative-tick dependency case, not the full dependency policy.

## Limits

These results establish bounded checker behavior on the enumerated fixture inputs and CLI runs. Byte identity is limited to the 224 baseline-tracked fixture JSON paths; no claim is made about other files' integrity. The paired fixtures isolate ticks in their timeline files, but their descriptions explicitly describe fixture input, not source-text claims. `source_id`, entity IDs, and place IDs do not attest that a source says an event occurred or that a place assignment is canon. Withholding a definite occupancy finding for a negative tick does not establish impossibility, absence of an in-world conflict, or canon-falsehood. The controls do not prove all nonnegative scheduling behavior or all dependency behavior.
