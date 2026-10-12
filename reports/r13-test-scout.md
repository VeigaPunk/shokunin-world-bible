# Round 13 test scout — baseline replay and actor-count probes

## Scope and method

Executed, without edits, the baseline checker extracted from `97f766762ac78ab6bcf6523aadbd2ffa92d4f4f5:.shokunin/lore/corpus/fixtures/check_bible.py` as `/tmp/r13-baseline-check_bible.py`, and the working checker at `.shokunin/lore/corpus/fixtures/check_bible.py`. CLI form in both cases: `python3 CHECKER FIXTURE_DIRECTORY`. The 26 raw fixture directories were enumerated under `.shokunin/lore/corpus/fixtures/` (from `ally-one-way` through `r9-unique-control`). Their stdout, stderr (empty), and exit codes matched exactly: no differences; all 26 comparisons completed.

The disposable probes were generated under `/tmp/r13-mixed-actors-wq2kmt2q/` from `.shokunin/lore/corpus/fixtures/r12-unique-actor/` JSON, adding two valid `shade` entity rows to create a duplicate actor and varying timeline rows. No corpus fixtures were modified. Exact CLI probes and baseline/current results:

- `python3 /tmp/r13-baseline-check_bible.py /tmp/r13-mixed-actors-wq2kmt2q/missing-actor` and `python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r13-mixed-actors-wq2kmt2q/missing-actor` (exit 1, identical stdout):
  ```text
  VIOLATION: entities[5].id: duplicate entities id 'shade'
  VIOLATION: timeline[0].entity_id: dangling entity 'unlisted'
  VIOLATION: timeline[1].entity_id: dangling entity 'unlisted'
  VIOLATION: timeline[1]: double-booked 'unlisted' at tick 7 in timeline[0] ('harbor') and 'tower'
  4 violation(s); no canon changed
  ```
- `... missing` case establishes existing behavior for a zero-match actor: the dangling diagnostics coexist with an occupancy assertion.
- Unique actor probe `python3 CHECKER /tmp/r13-mixed-actors-wq2kmt2q/unique-actor` in both checkers (exit 1, identical):
  ```text
  VIOLATION: entities[5].id: duplicate entities id 'shade'
  VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
  2 violation(s); no canon changed
  ```
- Duplicate actor probe `python3 CHECKER /tmp/r13-mixed-actors-wq2kmt2q/duplicate-actor` in both checkers (exit 1, identical):
  ```text
  VIOLATION: entities[5].id: duplicate entities id 'shade'
  VIOLATION: timeline[0].entity_id: ambiguous actor entity 'shade'
  VIOLATION: timeline[1].entity_id: ambiguous actor entity 'shade'
  3 violation(s); no canon changed
  ```
- Mixed probe `python3 CHECKER /tmp/r13-mixed-actors-wq2kmt2q/mixed` in both checkers (exit 1, identical):
  ```text
  VIOLATION: entities[5].id: duplicate entities id 'shade'
  VIOLATION: timeline[0].entity_id: dangling entity 'unlisted'
  VIOLATION: timeline[1].entity_id: dangling entity 'unlisted'
  VIOLATION: timeline[1]: double-booked 'unlisted' at tick 1 in timeline[0] ('harbor') and 'tower'
  VIOLATION: timeline[3]: double-booked 'mira' at tick 2 in timeline[2] ('harbor') and 'tower'
  VIOLATION: timeline[4].entity_id: ambiguous actor entity 'shade'
  VIOLATION: timeline[5].entity_id: ambiguous actor entity 'shade'
  7 violation(s); no canon changed
  ```

The mixed output confirms behavior is per actor ID: missing `unlisted` currently gets double-booked, unique `mira` gets double-booked, and duplicate `shade` gets local ambiguity without a double-booked finding. All probes use the same two distinct-place events per actor ID. Baseline and working outputs matched on every probe.

Before/after SHA-256 maps of all fixture `*.json` files under `.shokunin/lore/corpus/fixtures/` were identical (129 files each); no fixture changed.

## Recommendations (not findings)

- The declared round-13 claim is not yet realized by the working checker: for zero matching schema-valid entity rows, keep the dangling finding but skip occupancy comparison/update, analogous to duplicate-ID ambiguity handling. Preserve one-match and multi-match behavior.
- Re-run the 26-fixture exact baseline comparison and these three actor-count cases after any implementation. The missing case should lose only the `double-booked` line and associated count; unique actor should retain it; duplicate actor should retain ambiguity.
- These results establish checker diagnostics only. They do not establish whether events refer to the same person, whether a real conflict exists, or any canon fact.
