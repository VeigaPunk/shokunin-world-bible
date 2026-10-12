# Round 18 independent non-author review — calibration recommendation

## Work performed

I inspected the round-18 LOG declaration/clarification, checker, six fixture directories, saved run outputs, relevant documentation, and reports available (executor, critic, scribe, scouts). I independently ran all 45 fixture directories with `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture>` and compared exit code and stdout to the 45 saved transcripts in `corpus/live/runs/20261012T185657Z/`: **45/45 exact matches**. The 39 earlier fixtures also match their saved round-17 transcripts **39/39**. The requested `r18-test-scout` report is absent; I do not attribute replay evidence to that lane. No source edits were made.

## Evidence and fixture design

- `r18-unique-pair` has one `harbor` entity; `r18-duplicate-pair` adds one complete duplicate `harbor` entity. The event rows, order (`tower`, then `harbor`), IDs, source IDs and descriptions otherwise match. CLI goes from `double-booked` to `ambiguous place entity` without `double-booked`; both retain the duplicate-ID finding where applicable. This is a useful paired input, though it is entity-set addition/removal, not a claim that a single event field changed.
- `r18-duplicate-reverse` reverses those two events and still reports ambiguity without `double-booked`; this checks the reverse order.
- `r18-mixed-kind` duplicates `harbor` with a `character` row and likewise reports ambiguity without `double-booked`; it tests mixed-kind ambiguity in one event ordering. The same-kind and mixed-kind rows are not identical cases, and no reverse mixed-kind fixture is present.
- `r18-known-through-ambiguous` has `tower`, ambiguous `harbor`, then `quay`; it reports the known `tower`/`quay` booking while retaining the ambiguous event. `r18-duplicate-first-known` checks the reverse placement of the ambiguous event around known `tower`/`quay` and likewise keeps that known pair. Both add `quay`, a test-only place entity, to make a distinct known-known pair possible around the ambiguous `harbor`; this is correctly labeled as fixture input, not a canon fact.
- The six event descriptions explicitly limit themselves to fixture-input fields and disclaim source-text location assertions. Nonetheless each timeline row has `source_id: courier-log`, and the entities carry source IDs/claims. Those IDs only identify purported sources; no source excerpts are supplied. The fixtures do not show that the courier log supports these event locations, nor do they establish narrative truth. The description discipline avoids the prior direct false implication but cannot turn IDs into source evidence.

The checker change is tightly expressed: occupancy requires exactly one indexed entity row for `place_id` and that row must be kind `place`, in addition to the existing unique actor gate. Ambiguity diagnostics and raw timeline data remain. This is appropriately scoped to count > 1 among indexed/required-field-screened entity rows. It does not resolve the duplicate or prove absence of a conflict.

## Additional probe: malformed excluded row

I copied `r18-unique-pair` to a temporary directory and appended a second `harbor` entity containing only `{ "id": "harbor", "kind": "place" }`, omitting required `name`, `first_appearance`, and `claims`. The checker reported all three malformed-field violations but **also** reported `double-booked` between `tower` and `harbor`; it did not report ambiguous place. The malformed row is excluded from the index/count, so the valid `harbor` remains uniquely indexed. This is consistent with the declared count over screened rows, but demonstrates an important boundary: a malformed duplicate does not trigger this ambiguity suppression. Do not generalize the result to raw duplicate rows or malformed entity data; whether such input should suppress occupancy is a separate policy/question, not covered by this round.

## Saved-output preservation

The current 45 CLI invocations match all 45 saved round-18 transcripts, and all 39 earlier fixture outputs match the corresponding round-17 transcripts. The executor reports an exact 39-case baseline comparison against checker at `82701ce`; I did not independently recreate that comparison from the baseline checker in this review. The current replay confirms stability against the saved output artifacts, not by itself equivalence to arbitrary source revisions or all possible inputs.

## Axis recommendation (not a final adjudication)

- **Calibration: improved, narrowly**, for ambiguous `place_id` values with more than one required-field-screened indexed entity row. Paired unique/duplicate cases and reversed order withhold the definite checker booking while retaining ambiguity diagnostics; unique-place positive control continues to report the tested pair.
- **Depth: unchanged.** This round refines an existing occupancy check; it adds no new lore content or rule class.
- **Coverage: unchanged.** The candidate is a narrower treatment of an already recognized ambiguity limitation, not a new consistency-rule class. Same-kind/mixed-kind and selected schedules add examples, not general coverage proof.
- **Harmed axes: none demonstrated in these fixtures/replays.** This limited observation is not exhaustive regression or a proof that all valid inputs behave soundly.

The strongest warranted conclusion is that the revised checker is less willing to assert a definite ID-based booking when a place ID is ambiguous under its screened index. A withheld comparison is **unassessed**, not evidence that no conflict exists. The selected two- and three-row orders do not prove arbitrary pairwise behavior, hidden-conflict detection, source support, or canon truth. No claim is made about duplicate actors, display-name identity, or malformed excluded duplicates.
