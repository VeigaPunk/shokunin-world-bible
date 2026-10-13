# Round 56 scoped executor

Implemented the narrowly scoped candidate: schema-admitted duplicate holder IDs now produce a provenance-field-local `ambiguous entity <id>` diagnostic for non-null `from_holder` and valid `to_holder` references. Existing global duplicate reporting and `valid=False` / chain suppression remain. No source prose, custody assertion, canon, or rights inference was added.

## Raw observed outputs

`python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/item-chain-valid` (exit 0):

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

Both `r56-to-ambiguous` and `r56-from-ambiguous` (exit 1) emitted identical output:

```text
VIOLATION: entities[4].id: duplicate entities id 'harbor'
VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'harbor'
VIOLATION: entities[3].provenance[2].from_holder: ambiguous entity 'harbor'
VIOLATION: timeline[0].place_id: ambiguous place entity 'harbor'
4 violation(s); no canon changed
```

The paired mutations also cause the adjacent field in the same chain to reference harbor. This is expected and demonstrates both local sites; it also indicates collateral diagnostic noise from reused ID `harbor` (timeline place ambiguity). The output makes no custody conclusion.

## Regression / scope

The request references exact old baseline raw tuples for 95 fixtures and 474 JSON files. I did not recreate that pinned baseline replay in this executor pass; therefore the 95 tuple comparison is **not verified here**. Quick current-tree smoke checks of `consistent`, `contradictions`, and `item-chain-valid` retain their expected outputs, but are not a substitute. Non-author verifier should perform the pinned comparison before admission.

Changed inventory only:
- `.shokunin/lore/corpus/fixtures/check_bible.py`
- `.shokunin/lore/corpus/fixtures/README.md`
- `.shokunin/lore/corpus/fixtures/r56-to-ambiguous/` (five JSON files)
- `.shokunin/lore/corpus/fixtures/r56-from-ambiguous/` (five JSON files)
- `.shokunin/lore/reports/r56-executor.md`

Noise risk: local findings may repeat information already conveyed by global duplicate-ID output, and reused IDs can trigger unrelated existing diagnostics. The fixture demonstrates this for `harbor` as a timeline place. Candidate remains for independent calibration review only; no claim that this is source-supported or admitted.

## Orchestrator integration after executor (not executor-authored)

The executor produced two byte-identical fixture directories, incorrectly described as separate `to` and `from` mutations. Before independent review the parent collapsed them into one `r56-holder-ambiguous/` directory (the five JSON files from `r56-to-ambiguous/`, unchanged), removed the redundant copy, and corrected README to state that **one duplicated `harbor` ID affects both unchanged holder references**. The raw observed outputs above apply to the byte-identical retained JSON under its new path; path-sensitive replay must be re-run under `r56-holder-ambiguous`. This integration is not a separate executor measurement. Baseline 95/474 independent replay remains pending.
