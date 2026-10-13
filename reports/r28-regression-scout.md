# Round 28 regression scout — exact 78/389 replay plan

## Evidence and replay contract

- `.shokunin/lore/LOG.md:422` records baseline work/report commits `55fe508fec502fef5bf6a1f6f81aa93ba5a9529c` / `aaa8d724f5820b07a5cb2d498777306763001441` and the missing committed excerpt. `.shokunin/lore/LOG.md:423` defines the falsifiable depth move and explicitly requires all 78 prior fixture stdout/stderr/exit results and 389 prior JSON path bytes unchanged.
- `.shokunin/lore/LOG.md:424` prescribes a new fixture, followed by independent non-author review and verification; no existing fixture should be edited.
- `.shokunin/lore/corpus/fixtures/consistent/sources.json:9-12` establishes the `courier-log` ID and its in-world, first-person-fiction boundary. `.shokunin/lore/corpus/fixtures/consistent/relations.json:2-7` contains the single `mira -> seal` `carries` relation citing that source. This is setup context, not evidence that prose proves the relation.

## Exact replay proposal

1. Use the baseline commit in a disposable worktree or temporary checkout. Enumerate the 78 fixture cases and capture each invocation's exact argv, cwd, exit status, stdout bytes, and stderr bytes. Store a manifest keyed by fixture-relative path, not traversal order. Include the exact set of 389 JSON relative paths and their raw bytes (or SHA-256 plus byte length, with hashes computed from raw bytes).
2. Run the same harness against the candidate tree, excluding only the newly added r28 fixture from the old-fixture set. Compare path sets exactly, then compare each old fixture's argv and exit/stdout/stderr bytes; compare the 389 old JSON paths and raw bytes exactly. Report additions separately; do not weaken or regenerate the baseline from the candidate.
3. Run the new fixture checker on its own and require exit 0. Keep its source excerpt/map in the new fixture only. Have a named non-author reviewer independently trace each mapped statement to an exact excerpt clause and the one relation record; separately inspect that unsupported excerpt clauses are marked out of scope.
4. Record command lines, baseline revision, counts, and per-comparison pass/fail in the verifier report. A mismatch, missing/extra old path, changed old byte, or nonzero new-fixture result falsifies the replay claim; stop for investigation rather than updating expected output.

## Risks / falsifiers

- Fixture discovery may be order-sensitive or recursive; an added fixture could shift output. Preserve per-case invocations and compare by path, while also checking the aggregate harness behavior.
- A checker-wide command that includes the new fixture is not a substitute for proving the 78 old cases unchanged. Keep old-set and new-fixture results distinct.
- Text entailment is a human review obligation, not established by exit 0, IDs, citations, or matching strings. The source is explicitly fictional and first-person (`sources.json:9-12`); do not claim real-source truth, canonical relationship truth, or broader narrative support.
- Comparing parsed JSON rather than raw bytes can miss formatting/content changes. Compare raw bytes for all 389 baseline paths.
- The baseline counts and commits are LOG claims until independently reproduced. If the baseline checkout does not yield exactly 78 fixture outcomes and 389 JSON paths, report the discrepancy; do not silently adjust the target.

## Falsifiable check

Independent verifier checks out `55fe508fec502fef5bf6a1f6f81aa93ba5a9529c`, records the 78-case stdout/stderr/exit manifest and 389 raw JSON path-byte inventory, then repeats against the candidate tree. Pass iff every old case/path is present with exact corresponding bytes and outcomes, no old JSON path differs, counts are exactly 78 and 389, and the new fixture independently exits 0; otherwise fail with the first path/case and byte or outcome delta. A separate non-author reviewer must confirm the narrow clause-to-record map by inspection. This tests regression preservation and one constructed excerpt only, not general prose verification.
