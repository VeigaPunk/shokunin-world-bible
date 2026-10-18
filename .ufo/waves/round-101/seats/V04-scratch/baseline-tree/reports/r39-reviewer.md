# Round 39 — non-author reviewer

**Result: pass on execution and scope; coverage gain is narrowly supported, not a new checker behavior.** I made no fixture or checker edits.

## Independent checks

Compared the nine files in `r35-bell7-conflict/`, `r39-ledger-source-unique/`, and `r39-ledger-source-missing/`. The control matches r35 byte-for-byte in all nine files. The negative matches in eight; only `timeline.json` differs. Its sole semantic change is `timeline[3].source_id`: `sella-bell7-note` → `missing-sella-note`. The Sella event ID `sella-bell7-presence` is unchanged and unique, as are both ledger event pointers; `sources.json`, both excerpts, and `contradictions.json` are unchanged. The authored Sella source text remains present; only the event's new citation ID is absent from the source table.

I independently ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture>` from the repository root:

| Fixture | Exit | stdout | stderr |
|---|---:|---|---|
| `r39-ledger-source-unique` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` | empty |
| `r39-ledger-source-missing` | 1 | `VIOLATION: contradictions[0].claim_b: event 'sella-bell7-presence' has no resolvable source_id`
`VIOLATION: timeline[3].source_id: unknown in-world source 'missing-sella-note'`
`2 violation(s); no canon changed` | empty |

These are the complete outputs: exactly two findings, no collateral diagnostics. The second is the timeline-local unknown-ID finding; the first is the ledger-side consequence for the same uniquely resolved event whose source status is zero matches.

## Prior-art distinction and adjudication boundary

`reports/r7-reviewer.md:38` describes both ledger source-status paths: an unknown source produces “event ... has no resolvable source_id,” while an ambiguous source calls the local source diagnostic. That description is not evidence of an executed unknown-source probe. At line 52, the executed temporary probe duplicated `archive-ledger` and observed **ambiguous** `claim_a.source_id` (two matching rows), plus other affected source references. It did not observe zero matches. Thus r39's bounded novelty claim—an executed, unique event endpoint with **unknown/zero-source status**, contrasted with prior executed ambiguous status—is supported by the cited record. This exercises an existing branch, not new checker behavior. It does not prove no unrecorded/private test ever covered it.

The missing citation means the ledger's B endpoint is not structurally source-qualified in this input. It does not erase or disprove the Sella excerpt, establish that testimony is false, resolve the reported Bell-7 conflict, or determine canon. These are input-structure findings only.

## Collateral and risk

No unexpected collateral findings appeared in either run. The expected timeline diagnostic accompanies the ledger diagnostic because both validate the same event-source defect; they are distinct locations, not evidence of two separate missing source rows. The mutation changes one value (25 bytes at the byte-diff level) and leaves all other eight files byte-identical. Risk is limited: these fixtures demonstrate the checker's existing zero-source status path for a ledger endpoint; they do not validate source-text support or semantic claims. The fixture pair is useful regression evidence, but not a new rule or truth/canon test.
