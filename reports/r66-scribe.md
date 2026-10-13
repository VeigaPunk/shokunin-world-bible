# Round 66 scribe — current vs creation-time R59 wording

## Evidence

The active fixture README’s Round 59 paragraph presently says: “Other files are still checked; as shown by `r59-nested-duplicate/`, unloading an entity table can consequently produce dangling-reference findings in other tables. Those are consequences of missing loaded rows, not proof that entities are absent.” It then directs readers to `../../reports/r59-executor.md` for “raw candidate output and replay limits.” The phrasing reports the old behavior as a present-tense capability and does not identify its checker version or that the example is superseded.

That wording was accurate when R59 was created. `reports/r59-executor.md` records exact creation-time candidate output for `r59-nested-duplicate/`: duplicate `source_id` load error, six dangling findings (`relations[0].from` mira, `relations[0].to` seal, `timeline[0].entity_id` mira, `timeline[0].place_id` harbor, `timeline[1].entity_id` mira, `timeline[1].place_id` tower), total 7, exit 1, empty stderr. The report explicitly says those cascades reflected no loaded entity rows, not world absence. The R60 executor report records the admitted change: unavailable entity index suppresses entity-reference conclusions. It states that current replay of this same old fixture retains only the duplicate-member load diagnostic and summary 1, exit 1, with empty stderr.

I independently ran the active checker against the active fixture from repository root. Actual current stdout is exactly:

```text
VIOLATION: entities.json: duplicate object member 'source_id'; cannot load JSON
1 violation(s); no canon changed
```

Exit status 1; stderr empty. Thus the old six reference messages no longer occur. README Round 60, below Round 59, already clearly says unavailable `entities.json` does not call references dangling, ambiguous, or wrong kind. That materially reduces likely confusion for readers of the full section, but does not make the R59 example clearly historical when encountered alone or in search/snippet use.

## Wording proposal and calibration verdict

**MATERIAL calibration GO, narrow.** The README is the active fixture guide and its R59 example is an operational, reproducible fixture, not merely an archival report. In isolation it implies a current cascade that current CLI output disproves. The discrepancy can mislead an operator about what diagnostics to expect or whether the R60 gate is active. R60’s correct later explanation is a mitigating cross-reference, not a reason to leave an internally contradictory active example. Keep the R59 parser/duplicate-order facts and old reports untouched; amend only the stale cascade sentence to label the seven-finding result as creation-time behavior and point directly to R60/current output.

Suggested replacement for the relevant two sentences (not applied):

> In the R59 creation-time run, unloading an entity table in `r59-nested-duplicate/` produced six dangling-reference findings in other tables (seven total including the load error; see `../../reports/r59-executor.md`). This is historical behavior: under the current R60 rule, unavailable `entities.json` suppresses those entity-index-dependent findings; rerunning this fixture now emits only `VIOLATION: entities.json: duplicate object member 'source_id'; cannot load JSON` and `1 violation(s); no canon changed` (exit 1; stderr empty). See [Round 60](#round-60-unavailable-entity-index) for the current rule. Neither result establishes fictional-world absence.

This preserves the essential historical fact while distinguishing current behavior, points to the existing R60 policy, and avoids rewriting old reports or implying an entity is absent. No change to checker, fixture, LOG or canon is recommended/authorized by this scribe task.

## Falsifier / limits

NO-GO would be appropriate if the R59 prose already labelled its cascade as historical or the R60 cross-reference made the current result explicit in the R59 paragraph; it does neither. The risk is modest because the R60 section is adjacent and sound, so keep the edit minimal; a long duplicate explanation would add little. This verdict is about calibration of active documentation, not checker correctness, depth, coverage, source-text support, fictional truth, canon, chronology, or rights. No files other than this report were changed.
