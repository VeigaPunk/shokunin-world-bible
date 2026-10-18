# Round 60 pair-scout — entity table unavailable vs loaded controls

## Independent calibration verdict: **GO, narrowly**

**Path:** propose withholding only entity-reference conclusions that require lookup in `entities.json` when that table is unavailable (missing/unreadable/invalid JSON/wrong top-level shape). Keep the direct table-load diagnostic and checks not dependent on entity membership or kind. A successfully loaded empty or partial entity array is different: lookup is available and IDs absent from it may still be reported dangling. This is a proposed diagnostic-calibration policy, not a claim that any entity does or does not exist in the fictional world. I found no basis for expanding it to unavailable sources/timeline tables.

## Observed evidence (not proposed behavior)

- The loader catches a table-load error and assigns `rows = []`, then stores an empty `data[section]` and runs all cross-table checks (`.shokunin/lore/corpus/fixtures/check_bible.py:38-63`). `index('entities')` indexes only retained valid rows (`:65-71`); `entity_id_counts` counts only retained entity rows (`:125-127`).
- Relations report missing endpoints by `entity_id not in entities` (`check_bible.py:119-123`); timeline reports both entity and place references the same way (`:226-230`). Thus current code conflates unavailable table (represented as empty) with successfully loaded empty/partial table for these checks.
- I used temporary copies of `consistent/` outside the repository and changed only `entities.json`. Invalid JSON produced the file parse diagnostic plus six dangling findings: relation from `mira`, to `seal`, and timeline actor/place references `mira`, `harbor`, `mira`, `tower`. A valid empty `[]` produced the six dangling findings but no load diagnostic. A valid one-row partial table containing `mira` instead produced dangling findings for `seal`, `harbor`, and `tower`, while its unrelated `first_appearance` citation also failed because my temporary row used nonexistent `book-1`. These are observed checker outputs, not source/canon claims; the partial probe is illustrative, not a clean matched fixture.
- Prior art confirms the broad unavailable-table behavior: r5 loader scout observed absent, invalid-JSON, and nonarray `entities.json` each followed by six dangling findings (`reports/r5-loader-scout.md`, especially its Observations); r59 nested duplicate unload produced six dangling findings (`reports/r59-axis-adjudicator.md`, candidate table). R5's five malformed controls preserve existing primary output (`reports/r5-axis-adjudicator.md`), but do not establish suppression policy.
- Current code's other entity-dependent decisions include provenance holder checks (`check_bible.py:170-190`), alliance faction-kind eligibility (`:212-222`), and timeline occupancy/place-kind comparisons (`:226-251`). Broad suppression must be carefully limited to conclusions requiring entity lookup; the provenance chain has additional independent structural checks. A simple `entities=[]` or missing-membership guard is not a principled way to represent unavailable state.

## Proposed decision table

| entities.json state | Entity membership / kind-dependent conclusion | Independent work |
|---|---|---|
| Unavailable: load failure, malformed JSON, or non-array | Withhold dangling/unknown/ambiguous entity identity and kind conclusions that depend on this table; do not call them clean or absent. | Keep the load/shape diagnostic; preserve entity-row-independent schema and checks over successfully loaded tables, including source and timeline checks that do not require entity lookup. |
| Successfully loaded empty array | Report referenced IDs as dangling, because an available table contains no matching row. | Run all checks normally. |
| Successfully loaded partial array | Report IDs absent from the loaded array as dangling; resolve present unique/duplicate IDs under existing rules. Do not assume partial means exhaustive beyond the checker’s stated table semantics. | Run all checks normally, including other table diagnostics. |

## Risks and falsifier

Material benefit is calibration: a failed load is not evidence of an empty entity table, so suppressing only derivative absence/kind claims avoids presenting a known unavailable input as known absence. Main regression risk is overbroad suppression: it could hide independent structural errors (e.g. malformed timeline fields, invalid dependency references) or the established useful findings on a genuinely loaded empty/partial table. A second risk is erasing evidence from valid rows if implementation discards a partially parseable file; current JSON parsing is whole-file, so such a file is unavailable, not partially loaded.

**Falsifier:** a documented checker input contract that defines failed entity-table loads as an empty table for diagnostic purposes, or a paired regression showing that the proposed availability distinction suppresses a useful independent finding / changes results for a successfully loaded empty or partial table. Before implementation, require matched unavailable-vs-empty-vs-partial fixtures and replay of all prior outputs; classify every output delta. The r59 nested duplicate case is a known expected delta only if the narrow policy is adopted and independently verified.

**Axes:** Calibration proposed improved; depth unchanged; coverage unchanged. This is a GO for a scoped candidate/review, not admission of a checker change. No fixture/checker/README/LOG was edited. No inference about source text, actual world absence, canon, rights, or permission follows.
