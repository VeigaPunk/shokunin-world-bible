# Round 20 independent verifier — declaration/clarification

Verifier role: non-author replay and bounded probe, against report baseline commit `47733bf` (round 19 report commit). No checker, fixture JSON, documentation, or other source files were edited by this verifier. This report is the only file written by this verifier.

## Integrity and replay

- Compared every baseline fixture JSON path from `git ls-tree -r 47733bf`: **244/244 byte-identical** in the current worktree. No baseline JSON path was changed.
- Ran the baseline checker (`git show 47733bf:.shokunin/lore/corpus/fixtures/check_bible.py`) and current checker against the same 49 baseline fixture directories and paths. **49/49** had identical exit status, stdout, and stderr. Using the same paths avoids confusing the expected missing-file diagnostic path with a behavioral difference.
- Replayed the current checker for all **56** fixture directories; **56/56** transcripts (command, exit code, stdout) match the saved `corpus/live/runs/20261012T191902Z/*.txt` outputs exactly. Stderr was also captured; none differed from the saved transcript format (the saved records include stdout and exit only).

## Paired inputs and mixed-edge controls

Inspected actual JSON, not descriptions alone. `r20-valid-order` vs `r20-negative-dependent` differs only in the dependent event tick (1 to -1); `r20-valid-order` vs `r20-negative-prereq` differs only in the prerequisite tick (0 to -1). The valid order case is clean; each negative case retains the appropriate `must be nonnegative` finding and does not add a dependency inversion. `r20-valid-inversion` reports inversion for valid ticks 2 -> 1. `r20-valid-equal` reports inversion for equal valid ticks 1 -> 1 (and independently retains its occupancy collision). These are controlled input differences, not source claims.

`r20-mixed-edges` has valid A tick 2, negative B tick -1, and C tick 1 depending on both. Output retains B's negative-tick violation, suppresses the B→C inversion because one endpoint has invalid time, and reports A→C inversion because both endpoints have valid times (2 is not before 1). Thus the mixed control supports the per-edge eligibility change rather than globally skipping dependency checks when a row has an invalid tick.

## Temporary negative-tick diagnostics probes

Using a copied fixture under `/tmp` and the current checker (no repo fixture changes):

- self-dependency on the negative-tick dependent row: self-dependency diagnostic retained;
- repeated dependency: repeated-dependency diagnostic retained;
- unknown dependency: unknown-event diagnostic retained;
- ambiguous dependency (two rows with the referenced event ID): ambiguous-dependency diagnostic retained on the negative dependent row. The added duplicate row also correctly receives its own duplicate-ID/self/ambiguous findings.

All retain the negative-tick diagnostic as applicable. The ambiguous-ID probe necessarily adds a duplicate event row; its extra duplicate-ID and row-local diagnostics are not attributable to the dependency tick guard.

## Scope and limits

Evidence supports only that the current diff gates timeline inversion comparisons on both endpoint ticks being nonnegative, preserves the tested independent dependency diagnostics, leaves all 49 prior fixture outcomes unchanged, and reproduces all 56 saved current outputs. It does not establish source-text chronology, canon, event occurrence, exhaustive ordering behavior, or the absence of inversions/conflicts outside these tested cases. Suppressed invalid-time comparison is unassessed, not proof of valid chronology. No axis-admission verdict is made here.
