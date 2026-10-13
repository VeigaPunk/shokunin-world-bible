# Round 78 ledger scout — side citation handling

## Disposition

**NO-GO on the proposed checker change, based on this lane’s inspection.** A ledger-side extra `source_id` does not participate in any checker test, source resolution, or finding. Thus the proposed mismatching copied value is not currently diagnosed, but neither is an equal copied value; the checker treats both as inert extra data. This code trace alone does not establish reader confusion or justify giving the extra field new authority.

## Exact active paths

- `.shokunin/lore/corpus/fixtures/check_bible.py:25-32` declares required members/types for each table. A contradiction row requires `id`, `claim_a`, `claim_b`, and `why`; a side is only required to be a `dict` (`:31`). The loader at `:70-76` validates required members and retains valid rows; it does not reject unlisted object members. Therefore a side `source_id` can survive parsing but is not validated as a required field.
- Ledger side validation at `:111-143` reads only `event_id` and `field` (`:119-125`), then checks timeline availability and unique event-ID count (`:127-132`). For a uniquely resolved event it binds `event = events[event_id]` (`:133`), obtains **that event row’s** `event['source_id']` status (`:134`), and reports an unknown event source or an ambiguous event source at the side-local `.source_id` path (`:135-138`). It never reads `side.get('source_id')` or compares side and event values. A unique actual event source produces no ledger-side source diagnostic.
- The event source status comes from the valid `sources.json` rows counted at `:87-101`; `source()` emits unknown/ambiguous messages at `:103-109`. Independently, the ordinary timeline source check calls `source(row['source_id'], location + '.source_id')` at `:280-285` (line-number range for current checker). These checks resolve the event’s source, not a copied side value.
- General row shape/extra-member handling is at `:65-76`: only declared required fields are type/nonempty checked; extra keys are not rejected. The ledger’s same-reference guard (`:139-143`) compares only each side’s `event_id` and `field`, not other keys. No other side-level code path was found.

## Documentation and prior evidence

README `corpus/fixtures/README.md:45-54` documents each side as `{ "event_id": "...", "field": "..." }`, says the event’s own source is the citation, and says the ledger does not copy a source, text, or paraphrase that could disagree. It also limits validation to pointers and required text, not citation truth or semantic `why` correctness. This describes the intended documented shape, but does not explicitly prohibit extra metadata.

`reports/r3-reviewer.md`, “Findings,” already observes that claim-side objects allow extra keys while the documented representation promises event ID and field, and did not regard this as a current correctness issue. The report does not test a conflicting `source_id`, so it is prior evidence for permissive extension fields, not an execution result for this exact mutation. `reports/r7-reviewer.md`, “Reference-site inspection” and “Contradiction-ledger ambiguity probe,” confirms that the ledger resolves source status through the target event and reports ambiguity at `<side>.source_id`; its executed probe is an ambiguous **event** citation, not a copied side citation.

## Limits

This is static code/documentation tracing, not a matched fixture execution or human-reader study. It establishes that extra side `source_id` has no effect on checker outcomes and that the target event’s source controls ledger source resolution. It does not establish that a reader would be misled, that either source supports an assertion, or anything about source authenticity, story truth, canon, chronology, rights, or mechanics. No checker, fixture, README, or LOG changes were made.
