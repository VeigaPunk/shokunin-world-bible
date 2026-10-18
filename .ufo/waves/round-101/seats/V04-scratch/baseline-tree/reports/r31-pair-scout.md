# Round 31 pair scout — generic relation source ambiguity

## Smallest controlled pair (proposal, not implemented)

Use `corpus/fixtures/consistent/` as the template for two sibling cases. Keep all five JSON tables otherwise byte-identical. Keep `relations[0]` exactly `{from: mira, to: seal, type: carries, source_id: courier-log}` in both. The control retains its one `courier-log` row; the probe appends one second, distinct fictional source row whose `id` is also `courier-log` (do not replace or collapse either row). This is the smallest meaningful input delta: one added source row, leaving the relation itself unchanged. The existing consistent source ledger has one `courier-log` at `corpus/fixtures/consistent/sources.json:8-13`; the relation is at `corpus/fixtures/consistent/relations.json:2-7`.

The checker counts source rows at `corpus/fixtures/check_bible.py:54-57`; `source_status` distinguishes unknown/unique/ambiguous at `:64-66`, and `source()` emits the location-specific ambiguity at `:68-74`. Relations call it generically at `:123-130`, independent of relation type. Thus expected proposed control: exit 0. Expected probe: `relations[0].source_id: ambiguous in-world source 'courier-log'` plus legitimate ambiguity findings from other references to that same ID, and the duplicate-source-ID finding. Do not promise relation-only output: the base entities and timeline also cite courier-log (`consistent/entities.json:4-11, 17-24, 31-38`; `consistent/timeline.json:2-19`). Inventory exact output in implementation/review.

## Prior art, novelty, and risk

This extends coverage narrowly to a controlled, non-alliance (`carries`) relation using a duplicated citation ID; it is not evidence that ambiguous relation citations were wholly untested. Round 7 already has a reverse `allied_with` relation citing duplicated `harbor-compact` (`corpus/fixtures/r7-ally-reverse-ambiguous/relations.json:9-14`; duplicated rows `.../sources.json:2-11`). Its prior fixture scout reports that probe and checker behavior in `reports/r7-fixture-scout.md` under “Observed repository evidence” (especially the reverse ambiguity probe); do not re-label it as generic/carries coverage.

The extra row tests input identity ambiguity only. It does not establish which fictional record is intended, what either record says, whether Mira carried the seal, canon truth, or citation rights. Risk: duplicating a source used by several tables causes multiple valid diagnostics and may tempt reviewers to claim an isolated relation behavior from a noisy result. Mitigation: retain all original rows and files, explicitly enumerate all expected findings, and compare the unchanged control.

## Test / acceptance

Run `check_bible.py` separately on both fixture directories. Confirm control exit 0; probe reports ambiguity at `relations[0].source_id` in addition to expected findings, without treating the relation as false or resolving either record. Diff every file: only probe `sources.json` may differ, by exactly the appended row. Regression requirement from round declaration: all 81 prior fixture stdout/stderr/exit tuples and 404 prior JSON path bytes unchanged. This proposal changes no checker rule and asserts no canon truth.
