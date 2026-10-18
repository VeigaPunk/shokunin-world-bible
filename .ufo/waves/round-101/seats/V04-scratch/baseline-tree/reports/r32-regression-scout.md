# Round 32 regression scout — calibration

## Replay scope and evidence

Baseline is the r32 declared work commit `2c6fbbc212bf8d7531849cc33d6ed9b49b6ff1a9` (LOG r32 §1, `.shokunin/lore/LOG.md:497`). Its fixture tree contains **83** fixture directories and **414** JSON files: `git ls-tree -r --name-only 2c6fbbc .shokunin/lore/corpus/fixtures` lists 414 `.json` paths; excluding the README/checker paths leaves 83 fixture dirs. The tracked r32 fixture prefix is empty at the declaration (`LOG.md:497`), so replay must be against that baseline rather than current uncommitted orchestration state. The prior-round reference is r31's source/report pair (`LOG.md:480–485`): duplicate admitted `courier-log` gives eight findings, but it does not test a malformed duplicate source row.

The checker establishes the relevant boundary at `check_bible.py:21–43`: every row is field/type/nonempty validated, and only `valid` rows enter `data[section]`. It then builds source-ID multiplicities from admitted rows at lines 53–56. `source()` reports ambiguous IDs at lines 64–74. Thus a duplicate `sources.json` row with one required field malformed should yield its schema diagnostic but should not increase the count used by references. r26 is a precedent for the same admission pattern on entities, not source rows: its malformed second `seal` row is excluded before entity indexing/counting (`LOG.md:384–389`); the report explicitly avoids claiming malformed screening is novel.

## Regression plan / falsifiable test

Run the exact baseline checker from commit `2c6fbbc` over each of its 83 fixture directories and capture stdout, stderr, and exit status; compare all triples byte-for-byte with the independent baseline replay record. Independently compare the 414 baseline JSON paths byte-for-byte with the replay checkout. Acceptance: 83/83 output triples unchanged and 414/414 JSON files unchanged. A single changed byte, missing path, or exit-code difference falsifies regression safety; count mismatch means the baseline inventory was not reproduced. Do not treat current additional files as baseline.

For the proposed calibration pair, clone the r31 unique-source control and its admitted-duplicate case (the chosen `courier-log` pair described at `LOG.md:485`). Mutate exactly one required field in only the second duplicate source row to the empty string; preserve all other tables/bytes and keep the original valid row and references. Prediction: malformed case exits nonzero and reports that row's `sources[i].title: required nonempty str` (or whichever single selected required string field is deliberately blank), while it does **not** report duplicate source ID or any `ambiguous in-world source 'courier-log'`; the valid admitted-duplicate case still reports ambiguity, and unique control exits 0. Inventory the whole malformed output rather than assuming schema diagnostic is the only one. This is falsified if malformed row contributes to ambiguity count, if a valid control changes, or if any old replay differs. This probes calibration of structural admission, not source truth, canon, or rights.

## Risks and guardrails

- A wrong baseline revision or using the live checker for both sides can mask drift; pin and identify the baseline checker and compare outputs, not only exit codes.
- The r31 pair has multiple legitimate references to `courier-log`; ambiguity appears at multiple paths when admitted. The malformed case should remove only duplicate-induced ambiguity while preserving unrelated diagnostics. Record exact output delta.
- JSON byte comparisons include all tracked JSON paths, not only fixture tables touched by this pair. Keep the regression checkout read-only.
- The r26 entity malformed-row result is analogy only; do not generalize a result to source behavior without replay.
- This is a structural-input calibration test. It does not infer citation support, narrative truth, canon status, ownership, licensing, or permission.
