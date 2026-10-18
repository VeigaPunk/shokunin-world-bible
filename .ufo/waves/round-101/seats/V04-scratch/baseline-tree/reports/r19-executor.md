# Round 19 executor report

## Scope and change

Changed only `.shokunin/lore/corpus/fixtures/check_bible.py`: occupied-slot comparison/insertion now requires `row['tick'] >= 0`, in addition to the existing unique-actor and comparable-place guards. The existing negative-tick finding remains before this predicate. No `continue` was added: the timeline row remains indexed and its dependencies are still processed. No fixture, documentation, LOG, or commit was changed by this executor.

Baseline checker extracted from commit `9ee1e6eb18b7813a6fe2eda175d891b5d7f55308` to `/tmp/r19-baseline-check.py`; its SHA-256 is `8ad6848022410e8c8519e0fffde55c4e96bab594fdc6895574c0eb7efe11997e`. Current checker SHA-256: `9ab0679201218b45f006847be27c972fe244ba1b9577fe82483b233238ae27e`.

## Prior CLI replay

Replayed the 45 saved command/transcript pairs from `.shokunin/lore/corpus/live/runs/20261012T185657Z/` against both baseline and current checker. For every case, compared exit code, stdout bytes, and stderr bytes to its saved transcript and compared baseline with current. Result: **45/45** matched the saved output exactly for both checkers; **45/45** baseline/current output tuples were identical. There were no mismatches; stderr was empty in all these invocations. Commands were taken from each transcript header and the checker path substituted with the extracted baseline or current checker.

## Round 19 fixtures

Ran each of the four present `r19-*` fixture directories with baseline and current checker. All exited 1 and had empty stderr. Exact stdout:

- `r19-negative-tick` (baseline):
  ```text
  VIOLATION: timeline[0].tick: must be nonnegative
  VIOLATION: timeline[1].tick: must be nonnegative
  VIOLATION: timeline[1]: double-booked 'mira' at tick -1 in timeline[0] ('tower') and 'harbor'
  3 violation(s); no canon changed
  ```
  Current omits only the `double-booked ... tick -1 ...` line and reports `2 violation(s); no canon changed`.
- `r19-valid-tick` (both):
  ```text
  VIOLATION: timeline[1]: double-booked 'mira' at tick 9 in timeline[0] ('tower') and 'harbor'
  1 violation(s); no canon changed
  ```
- `r19-valid-around-negative` (both):
  ```text
  VIOLATION: timeline[1].tick: must be nonnegative
  VIOLATION: timeline[2]: double-booked 'mira' at tick 9 in timeline[0] ('tower') and 'harbor'
  2 violation(s); no canon changed
  ```
- `r19-negative-first-valid` (both):
  ```text
  VIOLATION: timeline[0].tick: must be nonnegative
  VIOLATION: timeline[2]: double-booked 'mira' at tick 9 in timeline[1] ('tower') and 'harbor'
  2 violation(s); no canon changed
  ```

Thus negative ticks retain their invalid-tick findings but no longer compare/store an occupied slot. Nonnegative same-actor, distinct-known-place conflicts remain. Valid-known pair findings before/after invalid rows remain. This is limited checker behavior on these inputs; it does not establish event truth, impossibility, or absence of an in-world conflict.
