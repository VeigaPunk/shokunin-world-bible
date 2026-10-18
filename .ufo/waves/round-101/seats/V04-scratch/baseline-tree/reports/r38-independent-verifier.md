# Round 38 independent verifier

## Baseline replay

I extracted the fixture tree from baseline report commit `ceb6ea7c2c609dfc332218ceb14f04994f5c28c6` with `git archive` into `/tmp/r38base`. It contains 90 prior fixture directories and 449 prior JSON paths. For each directory I ran the same root-relative argv, `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-dir>`, once with the archived baseline tree as cwd and once with the working tree as cwd. All 90 raw stdout byte strings, stderr byte strings, and exit statuses matched exactly. All 449 archived JSON files matched their corresponding working-tree bytes exactly. The temporary archive is outside the repository.

## Independent r38 run

I ran both fixture commands independently from the repository root. The unique control produced stdout `CLEAN: schema, citations, relations, timeline; 0 violations
`, empty stderr, exit 0. The ambiguous fixture produced exactly:

```text
VIOLATION: sources[4].id: duplicate sources id 'sella-bell7-note'
VIOLATION: contradictions[0].claim_b.source_id: ambiguous in-world source 'sella-bell7-note'
VIOLATION: timeline[3].source_id: ambiguous in-world source 'sella-bell7-note'
3 violation(s); no canon changed
```

Its stderr was empty and exit status 1. Thus the complete output includes the collateral timeline reference; it is not limited to the ledger finding.

## Fixture / prior-art boundary

The nine inherited files are `clause-map.md`, `contradictions.json`, `entities.json`, `manual-clause-pointer-map.md`, `relations.json`, `sella-bell7-note-excerpt.md`, `sources.json`, `tarin-note-excerpt.md`, and `timeline.json`. The unique control matches all nine r35 files byte-for-byte. Comparing negative to control, only `sources.json` differs: exactly one copied Sella source object is appended at index 4. The source ID `sella-bell7-note` occurs once in control and twice in negative. All four timeline event IDs occur exactly once in each fixture; both contradiction event pointers are unchanged and unique. `claim_a` still refers to the unique Tarin source; the Sella endpoint `claim_b.source_id` becomes ambiguous, as does `timeline[3].source_id`.

Prior-art limits matter: r7's reviewer reported a temporary, uncommitted `claim_a` ambiguity probe using duplicated `archive-ledger`; this is not first coverage of ledger source ambiguity as a general checker branch. This fixture is durable Bell-7 `claim_b` counterpart coverage, with uniquely resolving event IDs and the listed source-row collateral. It does not establish a new checker rule, choose between duplicate source rows, establish either account's truth, or adjudicate canon. No checker changes were made.
