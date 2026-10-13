# Round 78 probe-scout — copied ledger-side `source_id`

## Disposition

**GO for a narrowly scoped calibration review; NO-GO for checker or fixture change on this probe alone.** On the active checker, adding a side-level `source_id` equal to the pointed event’s source, a mismatching source, a non-string value, or no side field at all all produce exactly the same clean result. The ledger side currently treats only `event_id` and `field` as operative; source resolvability is derived from the uniquely matched timeline row. Thus this probe establishes that a conflicting copied citation is silently ignored by current validation, not that readers are in fact misled or that a diagnostic is warranted. A prospective policy should not promote side metadata into a second citation authority without separate materiality review.

## Method and exact matched inputs

Read active `.shokunin/lore/LOG.md` Round 78 declaration, `corpus/fixtures/check_bible.py`, `corpus/fixtures/README.md` Round 3, and prior reports `r3-reviewer.md`, `r3-axis-adjudicator.md`, `r7-reviewer.md`, `r63-prior-scout.md`, `r62-scribe.md`, and `r39-executor.md`.

I copied the nine files of `corpus/fixtures/r35-bell7-conflict/` into six separate directories under `/tmp/r78-probe-_arusju5/`; all are outside the repository and were run against the current repository checker. The baseline ledger `claim_a` is `{ "event_id": "tarin-envelope-observation", "field": "place_id" }`; its unique event row cites `tarin-note`. The `claim_b` and all other input files are unchanged except for the explicitly described controls below.

- `correct`: add `"source_id": "tarin-note"` to `claim_a` only.
- `mismatched`: add `"source_id": "sella-bell7-note"` to `claim_a` only.
- `absent`: leave the side field absent (byte-equivalent input to the r35 control).
- `malformed`: add `"source_id": 17` to `claim_a` only.
- `unresolved-event`: change only `claim_a.event_id` to `missing-event`; no copied `source_id`.
- `unresolved-event-source`: change `claim_a.source_id` to `missing-tarin-note` and the pointed event’s `timeline[2].source_id` to that same absent ID. This checks ordinary event-citation resolution with the side copy matching the input event; compared with the matched correct variant, only the side copy and target event source value differ. It is not a control for the checker’s side-field validation.

Command form for every run (same checker and matched source directory; absolute temp path):
`python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r78-probe-_arusju5/<case>`

## Exact raw behavior

For each of `correct`, `mismatched`, `absent`, and `malformed`: **exit 0**, stderr empty, stdout exactly:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

For `unresolved-event`: **exit 1**, stderr empty, stdout exactly:

```text
VIOLATION: contradictions[0].claim_a.event_id: expected exactly one timeline event 'missing-event'
1 violation(s); no canon changed
```

For `unresolved-event-source`: **exit 1**, stderr empty, stdout exactly:

```text
VIOLATION: contradictions[0].claim_a: event 'tarin-envelope-observation' has no resolvable source_id
VIOLATION: timeline[2].source_id: unknown in-world source 'missing-tarin-note'
2 violation(s); no canon changed
```

The final control demonstrates that even when the side copy equals an unresolved event source, the existing diagnostic is attached to the ledger side because the checker reads the target event’s `source_id`, plus the normal timeline citation diagnostic. It does not validate the copy.

## Prior-art and limits

README Round 3 documents side references as `{event_id, field}` and explicitly says the event’s source is its citation; the ledger does not copy a source. The active code confirms that: it retrieves `events[event_id]`, derives `event_source_status` from `event['source_id']`, and never reads `side['source_id']`. Extra side members pass because the checker validates required members but does not reject unknown ones. R3 reviewer’s temporary malformed-side probes concerned non-object sides, bad event IDs, and unsupported fields, not a copied source member. R7’s source probes concern ambiguous IDs at actual source-reference sites, not inert side metadata. R39 tested an unresolved source on the target event, not a side copy. R63 documents that extra members are generally permissive; this probe is not a novel general unknown-key policy.

This is only exact behavior on six copies of one fixture under one checker version. No corpus, checker, README, fixture, LOG, or other file was edited. No source text was authenticated or semantically compared. These outcomes do not establish what an ordinary reader would infer, whether policy should forbid extensions, or any source truth, story fact, canon, rights, chronology, or game-mechanics conclusion. Any next decision needs non-author assessment of realistic reader confusion and of the benefit/cost of rejecting only a contradictory optional copy while preserving arbitrary unrelated extension fields.
