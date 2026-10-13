# Round 66 regression scout — R59 README calibration

## Scope and pinned baseline

Independent regression scout; no fixture, checker, README, LOG, or historical report was edited. HEAD is the pinned r65 report commit `b5d370b571e406a7befe2d98718eb665fcf3c977` (work commit `e5f69e7e09f19711371dc4d36886b180374ced41`); current inventory is 125 fixture directories and 623 fixture JSON paths. Worktree had the round declaration in LOG and other scout reports; README had no diff. This task's allowed prospective change is README-only. R65 independently recorded a full-corpus pin of 1,298 paths/raw bytes, 623/623 old JSON bytes, and 125/125 old CLI stdout/stderr/exit tuples; this scout did not repeat that archived comparison. The present direct output below was freshly run against HEAD.

## Exact discrepancy and current output

Active `corpus/fixtures/README.md`, Round 59, presently says: “Other files are still checked; as shown by `r59-nested-duplicate/`, unloading an entity table can consequently produce dangling-reference findings in other tables. Those are consequences of missing loaded rows, not proof that entities are absent.” This follows a present-tense description of the checker and does not date the listed six findings as creation-time behavior. The sentence accurately explains the R59-era output but is stale as a description of current behavior.

Fresh command at HEAD:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r59-nested-duplicate
```

Exit 1, stderr empty; stdout exactly:

```text
VIOLATION: entities.json: duplicate object member 'source_id'; cannot load JSON
1 violation(s); no canon changed
```

The fixture's nested repeated member makes entities.json unavailable. R59 executor `reports/r59-executor.md` records the historical candidate output for the same fixture: loader diagnostic plus six dangling-reference findings (relations from mira/to seal; timeline entity mira/place harbor and entity mira/place tower), total seven. R60 executor `reports/r60-executor.md` says current `r59-nested-duplicate` output is the loader diagnostic only, summary 1; R60 axis-adjudicator independently pinned/replayed and reports this as the intentional delta. README Round 60 explicitly states that an unavailable entity index does not yield dangling/ambiguous/kind or derived occupancy/alliance conclusions, while retaining independent checks. Thus facts are documented correctly in the later section, but the R59 anecdote itself is not marked as historical or cross-linked to the changed behavior.

## Materiality decision: GO, narrowly, for README clarification

Recommendation: GO for a small README-only correction that labels the R59 six-cascade example as historical creation-time behavior, cites the R59 executor as historical output, and points to Round 60/current behavior. Do not alter R59 executor or other old reports. R60 exists later in the same document and accurately describes current behavior, so the risk is bounded and the exact sentence says the findings “can consequently” arise rather than explicitly claiming every current run does. Nevertheless, a reader reaching the R59 section for the fixture's named output sees it in present tense, without a date/version marker, and can reasonably expect six dangling-reference findings from the current runnable command. The actual output is one loader finding. This is a reproducible discrepancy in an active how-to/behavior README, not a demand to reconcile history or merely correct an inconsequential count. A brief local pointer avoids changing historical narrative and improves the operator's expected diagnosis/output. This is a calibration improvement; it does not change fixtures/checker or assert world absence.

## Falsifier / regression constraint

The GO would be falsified if R59 were already explicitly labeled historical in context, or if the named R59 example did not give a reader a reasonable expectation of current output. It is not so labeled: the section describes the current checker, then says other files “are still checked” and gives the nested fixture as demonstration; its creation-time status is only inferable by navigating to an old executor report. R60's later policy text mitigates but does not make the R59 example precise. Any accepted wording must distinguish historical seven-finding output from current one-finding output, cross-reference Round 60, and retain the caveat that historical dangling findings reflect unloaded rows rather than world absence. No old report/fixture/checker/LOG edits; no source-prose, canon, rights, or permission inference. No README diff was made by this scout.
