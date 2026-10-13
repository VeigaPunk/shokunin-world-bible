# Round 52 pair scout — ambiguous event citations and occupancy wording

## Scope and observed control flow

Read-only scout; no checker, fixture, README, LOG, or commit edits. The round-52 hypothesis in `LOG.md` is specifically an unqualified `double-booked` diagnostic when event source IDs are ambiguous, not a proposal to suppress the collision or decide canon.

The active checker counts source rows at `corpus/fixtures/check_bible.py:53-66`; `source_status()` distinguishes unknown/unique/ambiguous, and `source()` reports local ambiguity at `:68-74`. In the timeline loop, it independently calls `source(row['source_id'], location + '.source_id')` at `:242`, then uses actor uniqueness, valid place, and nonnegative tick to gate occupancy at `:245-252`. The collision message at `:248-250` does not branch on the event source status. Thus ambiguous-source diagnostics and a raw field collision can coexist. This does not show that either event occurred, that its citation supports the location, or that canon conflicts.

## Minimal discriminating pair (proposal, not executed)

Copy `fixtures/consistent/` to two temporary directories outside the repository. In each, use two schema-valid timeline rows, unique event IDs, same uniquely represented actor `mira`, same nonnegative tick, distinct uniquely represented places `harbor` and `tower`, empty dependencies, and otherwise identical fields. Use an existing uniquely represented source ID on both rows in the control. In the variant, change only the second row's `source_id` to a new ID which has **two schema-valid source rows**; retain those duplicate rows and every input row. Ensure the duplicate source ID is not otherwise cited. These are artificial checker inputs, not evidence in the fictional world.

Expected current behavior in both cases: one `double-booked` diagnostic; the variant additionally has the duplicate-source finding and second-row local ambiguous-source finding. Expected candidate behavior under the declared hypothesis: preserve that same raw collision (and all local diagnostics); only the variant collision wording is explicitly qualified as “input-structural finding, not sourced-canon.” Control wording and status remain exactly unchanged. Do not call the collision a sourced contradiction, and do not select a duplicate source row.

## Prior-art boundary and risks

Round 7 already applies the phrase “input-structural finding, not sourced-canon” to item provenance chain errors when an ambiguous source is present (`reports/r7-executor.md`; checker `:145-206`), while retaining independent structural chain checks. It does **not** qualify timeline occupancy; the r7 axis adjudicator explicitly says unique source resolution is not source-text support, reliability, historical truth, or canon (`reports/r7-axis-adjudicator.md`). This is a close wording precedent, not proof that every input-structural diagnostic needs that label.

Round 12 separates actor identity uncertainty from occupancy: its ambiguous actor guard avoids asserting a definite same-actor collision (`reports/r12-axis-adjudicator.md`). The present candidate is different: actor identity, place, and tick are unique/valid; only event source identity is ambiguous. Round 21's paired occupancy probes treat distinct-place same-actor/tick rows as input findings and explicitly deny source-text/canon conclusions (`reports/r21-citation-scout.md`). Round 22 likewise says ordering findings concern input fields, not chronology or canon, and citation ID alone attests none (`reports/r22-axis-adjudicator.md`). These prior qualifications may make added wording redundant/noisy. `fixtures/README.md`'s r43 section also stresses that checker/citation does not establish reported-location truth or canon; prose context elsewhere cannot establish the probe's event facts.

Key risk either way: suppressing or masking `double-booked` would erase the visible input-field collision and conflate source identity with actor/place/tick structure. Conversely, qualifying all collisions or unique-source collisions would broaden scope without evidence. A uniquely resolved source ID still does not prove that source prose supports the row; ambiguous ID neither proves nor disproves fictional location, source prose, or canon. Unknown IDs are out of this pair's scope and should not be silently grouped with ambiguous IDs.

## Falsifiable go/no-go

**Go** only if paired raw CLI runs establish the predicted distinction, the proposed wording can be limited to the ambiguous-source variant while retaining every diagnostic and collision, and a non-author replay verifies unique-source control output/status unchanged plus all pinned baseline regressions unchanged (or documents each affected legacy tuple). The calibration claim must identify a reader-relevant misreading of the current definite-looking collision as sourced/canonical and show the qualifier prevents it without hiding the input collision. If prior explicit boundaries already prevent that misreading, or the qualifier obscures the structural finding, **no-go**: calibration unchanged/harmed, no checker move.

No truth inference is warranted under either outcome. This report records a proposed experiment, not a probe result, implementation, checker output, or axis verdict.
