# Round 66 drift-scout — R59 README current-output drift

## Independent verdict: NO-GO on material calibration

The active R59 README example is stale if read alone, but current active guidance immediately below corrects it specifically. The factual drift is real; evidence does not show that clarifying the R59 paragraph would materially improve operator decisions beyond the existing R60 rule. Recommend no README/checker/fixture/canon change. This is a calibration verdict, not a claim the stale sentence is factually current.

## Exact present text and output

The active `.shokunin/lore/corpus/fixtures/README.md`, under “Round 59: repeated JSON object member names,” says: “Other files are still checked; as shown by `r59-nested-duplicate/`, unloading an entity table can consequently produce dangling-reference findings in other tables. Those are consequences of missing loaded rows, not proof that entities are absent.” The paragraph links to `../../reports/r59-executor.md` for “raw candidate output and replay limits.” It does not label the cascade as historical, so locally it reads as current fixture behavior.

Current direct command from repository root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r59-nested-duplicate
```

Exit 1, stderr empty; stdout exactly:

```text
VIOLATION: entities.json: duplicate object member 'source_id'; cannot load JSON
1 violation(s); no canon changed
```

There are no six dangling-reference findings. This matches the current R60 policy: README “Round 60: unavailable entity index” says duplicate-member rejection leaves `entities.json` unavailable and the checker does not call references dangling, ambiguous, or wrong-kind. It separately says a successfully loaded empty array does produce dangling results.

## Historical record and calibration assessment

`reports/r59-executor.md` accurately records the creation-time R59 output for this same fixture: the duplicate-member load error plus six dangling findings (relations from `mira`, to `seal`; timeline entity `mira` / places `harbor` and `tower` for both rows), summary `7 violation(s); no canon changed`, exit 1, empty stderr. That report says the findings reflect no loaded entity rows, not world absence. It must remain untouched as historical evidence. `reports/r60-executor.md` records the later entity-index availability gate; `reports/r60-axis-adjudicator.md` independently identifies this fixture as the sole changed old-fixture output in its stated 99-directory replay, with current output reduced from seven findings to one.

The active guide has an internal R59/R60 inconsistency, so a reader stopping at R59 could expect obsolete diagnostics. However R60 is adjacent and expressly covers the duplicate-member/unavailable-table case, describes the current behavior and contrasts loaded-empty input. The likely benefit is cleaner local wording, but no evidence establishes that the inconsistency produces a consequential mistaken repair or expectation. Thus **NO-GO on material calibration**, despite a real present-tense drift. No speculative edit to old reports, checker, fixture, README, or LOG.

## Falsifier and boundaries

Evidence that an operator relying on R59 alone expected or acted on six active dangling findings despite the following R60 rule would falsify this NO-GO materiality judgment. Conversely, if the R59 paragraph already labeled the findings as historical, the factual-drift concern itself would be falsified; it currently does not. Neither old nor current output establishes fictional-world absence, source-text support, canon, or rights. This report does not assert story facts.
