# Round 18 scribe — bounded documentation draft

## Raw observations (not recommendations)

- Round-18 declaration in `LOG.md` identifies baseline report commit `82701ce7680fb062a345e379057c8a097c1539e6` and says duplicate/ambiguous `place_id` values can still enter occupancy as raw IDs.
- Current checker code confirms the relevant condition: `comparable_place = place_id_count != 1 or ... kind == 'place'`; when the actor count is one and `place_id_count != 0`, the raw place ID can reach occupancy. For a repeated ID, matching duplicate rows produce the existing ambiguous-place diagnostic earlier in the same pass.
- Existing docs state round-16 absent-ID and round-17 unique-wrong-kind behavior, and explicitly leave duplicate/ambiguous place IDs as a limitation. The docs do not yet establish round-18 fixture outcomes or admission.
- No round-18 reports/fixtures were present at time of this draft. Thus the paired cases below are proposed wording only; they are not observed checker results.

## Proposed bounded decision-table row (use only after evidence/review)

| Place-ID matches among required-field-screened entity rows | Proposed occupancy decision | Evidence and boundary |
|---|---|---|
| More than one | Keep duplicate-ID and `ambiguous place entity` findings and preserve the raw timeline row; do not compare or insert it as a **definite uniquely resolved place** for occupancy. | Proposed paired cases: unique `tower` + duplicate-ID `harbor` should withhold that definite comparison regardless of event order; unique `tower` + unique `harbor` control should retain the existing `double-booked` finding. Cite exact fixture paths and replay receipts only after they exist and a non-author verifies them. This does not resolve the entity, establish actual locations, or prove there is no conflict. |

## Proposed README paragraph (conditional)

For a timeline `place_id` matching multiple required-field-screened entity rows, retain the ambiguous-place and duplicate-ID findings and the event row, but do not use the raw ID as a uniquely resolved place in definite occupancy comparisons. A unique-place control remains necessary to show that the rule still reports the tested known-place pair. Any withheld comparison is **unassessed**, not evidence that no conflict exists. This is a local input-identity rule; it does not choose between duplicate rows, establish source-text support, or resolve canon. Refer to the round-18 fixtures and independent replay only after they are present and verified.

## Caveats for the final wording

1. Keep round-18 claims conditional until paired fixture results, order controls, and independent replay are actually available. Do not turn the declaration's prediction into an observed outcome.
2. State the index scope precisely: required-field-screened rows, and count greater than one. Do not generalize to display-name collisions, all entity-resolution questions, or malformed rows.
3. Preserve round-16 count-zero behavior and round-17 count-one wrong-kind behavior; this proposed row covers only duplicate/ambiguous place IDs. Do not imply duplicate actors or other fields are covered.
4. A withheld checker comparison is uncertainty, not proof of no real-world/in-world conflict. A retained `double-booked` diagnostic is an input-level checker result, not narrative truth.
5. Source-ID resolution, fixture descriptions, and diagnostic labels do not prove that an in-world source text supports an assertion. Avoid attributing fixture prose to `courier-log` or another cited source.
6. The proposed `tower`/`harbor` paired example and row-order behavior must be replaced with actual, verified paths/results or omitted. A selected finite schedule does not establish exhaustive pairwise detection.
7. Do not update README/table or claim round-18 admission from this draft. Final disposition and axis verdict belong to the independent adjudication and append-only LOG process.
