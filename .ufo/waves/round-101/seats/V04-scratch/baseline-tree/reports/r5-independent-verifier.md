# Round 5 independent raw-CLI verifier

Non-author replay of the six decision-table rows and four named regression cases. Ran each command from repository root against the committed raw fixture (no table-derived simulated output). For each, captured stdout and stderr separately and recorded the checker process exit code; stderr was empty in all ten runs. Exact stdout and command are below.

## Raw replay outputs

### `consistent` — CLI exit 0

Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent`

```text
CLEAN: schema, citations, relations, timeline; 0 violations

```

Stderr: *(empty)*


### `r5-missing-file` — CLI exit 1

Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-missing-file`

```text
VIOLATION: contradictions.json: cannot load JSON: [Errno 2] No such file or directory: '.shokunin/lore/corpus/fixtures/r5-missing-file/contradictions.json'
1 violation(s); no canon changed

```

Stderr: *(empty)*


### `r5-invalid-json` — CLI exit 1

Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-invalid-json`

```text
VIOLATION: contradictions.json: cannot load JSON: Expecting property name enclosed in double quotes: line 2 column 1 (char 2)
1 violation(s); no canon changed

```

Stderr: *(empty)*


### `r5-wrong-top-level` — CLI exit 1

Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-wrong-top-level`

```text
VIOLATION: contradictions.json: expected array
1 violation(s); no canon changed

```

Stderr: *(empty)*


### `r5-row-shape` — CLI exit 1

Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-row-shape`

```text
VIOLATION: contradictions[0]: expected object
1 violation(s); no canon changed

```

Stderr: *(empty)*


### `r5-invalid-citation` — CLI exit 1

Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-invalid-citation`

```text
VIOLATION: relations[0].source_id: unknown in-world source 'absent-source'
1 violation(s); no canon changed

```

Stderr: *(empty)*


### `contradictions` — CLI exit 1

Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/contradictions`

```text
VIOLATION: relations[1].to: dangling entity 'missing-map'
VIOLATION: timeline[1].depends_on: timeline inversion 'later' tick 3 not before 'arrival' tick 2
VIOLATION: timeline[2]: double-booked 'mira' at tick 2 in timeline[1] ('tower') and 'harbor'
3 violation(s); no canon changed

```

Stderr: *(empty)*


### `ally-reciprocal` — CLI exit 0

Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/ally-reciprocal`

```text
CLEAN: schema, citations, relations, timeline; 0 violations

```

Stderr: *(empty)*


### `ally-one-way` — CLI exit 1

Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/ally-one-way`

```text
VIOLATION: relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation
1 violation(s); no canon changed

```

Stderr: *(empty)*


### `contradictions-ledger-malformed` — CLI exit 1

Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/contradictions-ledger-malformed`

```text
VIOLATION: contradictions[1].claim_b.event_id: expected exactly one timeline event 'absent-event'
VIOLATION: relations[1].to: dangling entity 'missing-map'
VIOLATION: timeline[1].depends_on: timeline inversion 'later' tick 3 not before 'arrival' tick 2
VIOLATION: timeline[2]: double-booked 'mira' at tick 2 in timeline[1] ('tower') and 'harbor'
4 violation(s); no canon changed

```

Stderr: *(empty)*


## Raw-input mutation check

Compared each malformed case directly with `consistent/` by SHA-256 of every JSON table. The mutations are exactly those claimed: `r5-missing-file` lacks only `contradictions.json`; `r5-invalid-json`, `r5-wrong-top-level`, and `r5-row-shape` differ only in `contradictions.json` (raw contents respectively `'{\n'`, `'{}\n'`, `'[7]\n'`); `r5-invalid-citation` differs only in `relations.json`, with `relations[0].source_id` equal to `absent-source`. Each other table hash matches clean control. The missing file is the one absent path, not an altered substitute.

## Comparison to decision table and regressions

All six measured rows match the decision table's exit codes and stable diagnostic classes: clean control exits 0; missing and invalid JSON report `contradictions.json: cannot load JSON`; wrong top-level reports `expected array`; row shape reports `contradictions[0]: expected object`; bad citation reports the unknown source. No unexpected extra diagnostics. Exact OS/parser-dependent wording is shown above. The four prior regressions also match their stated behavior: contradiction fixture exits 1 with the same three seeded findings; reciprocal allies exit 0; one-way ally exits 1 with missing sourced reciprocal; malformed contradiction ledger exits 1 with the ledger pointer issue plus the same three findings.

## Non-mutation verification

Checker SHA-256 before and after all runs: `0008496a65e6e0696b638a081c78c44cf4e323d7f56441a6105631ecc689769d` (unchanged). SHA-256 manifests for all ten input directories before/after are identical (all 49 present JSON paths unchanged; the one intentionally missing path remains missing). No fixture/table/checker writes were performed by this verifier.

**Result: no mismatch observed.** The result is bounded to these ten raw input cases and this current checker; it does not establish exhaustive malformed-input behavior.
