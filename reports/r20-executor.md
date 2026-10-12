# Round 20 executor — dependency inversion with invalid ticks

## Change

At baseline `47733bfa36216a28c639fd8d5dc891fb4d8de3f5`, after a dependency ID uniquely resolves, the checker compared the prerequisite raw tick against the dependent raw tick without requiring either tick to be in the supported nonnegative domain. I changed only that comparison guard in `corpus/fixtures/check_bible.py`: it now compares for inversion only when both endpoint ticks are `>= 0`. The unique-ID branch, tick diagnostics, indexed events/raw ticks, and per-edge loop remain in place. Self, repeated, unknown, and ambiguous ID checks remain before the guard; no `continue` was added. Occupancy and all other logic are unchanged.

## Baseline replay

I extracted the checker directly from `git show 47733bf:.shokunin/lore/corpus/fixtures/check_bible.py` into `/tmp/r20-baseline-check.py` and replayed each of the 49 saved CLI transcripts in `.shokunin/lore/corpus/live/runs/20261012T190807Z/` against both that baseline checker and the working-tree checker, from the repository root. For every case, baseline and current each matched the saved exit code, stdout bytes, and empty stderr exactly: **49/49 baseline exact; 49/49 current exact; 0 mismatches**. The replay transcript corpus contains the 45 earlier cases plus four r19 cases. The comparison includes exit status, stdout, and stderr. This establishes unchanged behavior on those 49 inputs, not all possible bibles.

## Round-20 fixture CLI observations

Command for each row: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<name>`. Exact stdout follows; stderr was empty for all seven.

| Fixture | Exit | Exact stdout |
|---|---:|---|
| `r20-both-negative` | 1 | `VIOLATION: timeline[0].tick: must be nonnegative`
`VIOLATION: timeline[1].tick: must be nonnegative`
`2 violation(s); no canon changed` |
| `r20-mixed-edges` | 1 | `VIOLATION: timeline[1].tick: must be nonnegative`
`VIOLATION: timeline[2].depends_on: timeline inversion 'r20-valid-a' tick 2 not before 'r20-valid-c' tick 1`
`2 violation(s); no canon changed` |
| `r20-negative-dependent` | 1 | `VIOLATION: timeline[1].tick: must be nonnegative`
`1 violation(s); no canon changed` |
| `r20-negative-prereq` | 1 | `VIOLATION: timeline[0].tick: must be nonnegative`
`1 violation(s); no canon changed` |
| `r20-valid-equal` | 1 | `VIOLATION: timeline[1]: double-booked 'mira' at tick 1 in timeline[0] ('tower') and 'harbor'`
`VIOLATION: timeline[1].depends_on: timeline inversion 'r20-prereq' tick 1 not before 'r20-dependent' tick 1`
`2 violation(s); no canon changed` |
| `r20-valid-inversion` | 1 | `VIOLATION: timeline[1].depends_on: timeline inversion 'r20-prereq' tick 2 not before 'r20-dependent' tick 1`
`1 violation(s); no canon changed` |
| `r20-valid-order` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |

In particular, the negative-dependent/prerequisite and both-negative fixtures retain their tick diagnostics but no longer emit inversion findings. The mixed-edges fixture still checks its separate valid-to-valid edge and reports its inversion, demonstrating the loop continues per edge. Equal, strictly inverted, and ordered nonnegative controls retain the inversion or clean result expected by their inputs.

## Scope and limits

This is a checker-input-domain guard, not a chronology or canon ruling. A withheld comparison does not mean a dependency is satisfied, that events did or did not occur, or that no conflict exists. Fixture tick/source values are not evidence that an in-world source attests chronology. The replay and seven fixture outputs are finite behavior checks. I changed no fixtures, docs, log, commit, or files other than the checker and this report.
