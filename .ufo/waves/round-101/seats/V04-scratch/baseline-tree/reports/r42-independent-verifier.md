# Round 42 independent verifier

## Baseline and replay

Pinned baseline: `ba50a55169359c217710a09ed22510023c5be484`. I extracted that commit with `git archive` to an independent temporary root and compared it with the working tree. The baseline contains 94 active fixture directories and 469 JSON paths under `corpus/fixtures`; the root-relative invocation used for each was:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>
```

All 94 executions produced identical raw stdout bytes, raw stderr bytes, and exit status between the archive and current roots. All 469 fixture JSON paths were present on both sides with byte-identical contents; no old fixture JSON was added, removed, or changed. The checker bytes also match exactly. No `r42-*` fixture directory is present in the current fixture tree. This verifies regression preservation against the pinned baseline, not execution of a proposed round-42 test.

## Prior-art check and boundary

The round-3 reviewer explicitly records using temporary copies to test an unsupported field, observing exit 1 with a diagnostic and no crash (`.shokunin/lore/reports/r3-reviewer.md`, “Scope and replay”). The round-3 report also limits the conclusion: allowed selectors are structural pointers; the checker does not verify semantic conflict, source support, or the truth of `why`.

Therefore unsupported-field behavior is prior executed coverage. Round 42 has no durable fixture for the proposed unsupported-`description` case, and no such candidate probe was executed as part of this verification. Do not attribute an observed r42 result to it or present this as new branch coverage.

No files were changed by this verification other than this report.
