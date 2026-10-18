# Round 39 executor — ledger source missing

## Scope and prior-art boundary

Created only the two controlled fixture directories and this report. The baseline is `r35-bell7-conflict`. `reports/r7-reviewer.md` line 38 describes the unknown-source branch, but line 52's executed temporary probe duplicated `archive-ledger` and observed ambiguous `claim_a.source_id`; it did not execute a zero-source ledger endpoint. Thus this result is narrowly the observed **unknown-source status (zero matching source rows)**, distinct from the already observed ambiguous-source status (two or more rows). It demonstrates no new checker rule and makes no claim that nobody privately tested it.

## Fixture construction and byte inventory

Control `r39-ledger-source-unique/` is a direct copy of the nine files in `r35-bell7-conflict/`. Negative `r39-ledger-source-missing/` is the same copy, with only `timeline.json` changed: `timeline[3].source_id` changes from `sella-bell7-note` to `missing-sella-note`. No source row, excerpt, event ID, or ledger pointer changed. The negative still contains the fictional Sella excerpt; its event citation simply does not resolve.

Inherited-file comparison against r35 (bytes; equality):
- `clause-map.md`: r35=1482; control=1482 (identical=True); negative=1482 (identical=True; changed bytes=0)
- `contradictions.json`: r35=1027; control=1027 (identical=True); negative=1027 (identical=True; changed bytes=0)
- `entities.json`: r35=1689; control=1689 (identical=True); negative=1689 (identical=True; changed bytes=0)
- `manual-clause-pointer-map.md`: r35=4220; control=4220 (identical=True); negative=4220 (identical=True; changed bytes=0)
- `relations.json`: r35=104; control=104 (identical=True); negative=104 (identical=True; changed bytes=0)
- `sella-bell7-note-excerpt.md`: r35=351; control=351 (identical=True); negative=351 (identical=True; changed bytes=0)
- `sources.json`: r35=892; control=892 (identical=True); negative=892 (identical=True; changed bytes=0)
- `tarin-note-excerpt.md`: r35=316; control=316 (identical=True); negative=316 (identical=True; changed bytes=0)
- `timeline.json`: r35=1235; control=1235 (identical=True); negative=1237 (identical=False; changed bytes=25)

The control has all nine inherited files and no additions; negative has all nine and no additions. A focused unified diff confirms only the source_id value above; all four other JSON files and all four prose/markdown files are byte-identical.

## Checker executions (full output)

Command from repository root: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>`.

### Control

Exit: 0  
stdout:
```text
CLEAN: schema, citations, relations, timeline; 0 violations
```
stderr: *(empty)*

### Missing source

Exit: 1  
stdout:
```text
VIOLATION: contradictions[0].claim_b: event 'sella-bell7-presence' has no resolvable source_id
VIOLATION: timeline[3].source_id: unknown in-world source 'missing-sella-note'
2 violation(s); no canon changed
```
stderr: *(empty)*

Exact findings (2): ledger-side `claim_b` event source cannot resolve; timeline event's missing source ID is unknown. No other findings occurred.

## Interpretation boundary

The control ledger B endpoint is structurally source-qualified; the negative retains a unique event pointer but not a resolvable source. The missing event citation does not invalidate, erase, or authenticate Sella's fictional excerpt; it does not prove Sella lied, falsify testimony, resolve the r35 conditional reported incompatibility, or decide canon. The checker reports input structure/status, not source truth. This is executor evidence only; independent review/adjudication remains pending.
