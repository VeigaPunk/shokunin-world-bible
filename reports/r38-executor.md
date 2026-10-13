# Round 38 executor — Bell-7 ledger source-unique/ambiguous pair

## Scope and construction

Created only `corpus/fixtures/r38-ledger-source-unique/`, `corpus/fixtures/r38-ledger-source-ambiguous/`, and this executor report. Both fixtures are copies of `r35-bell7-conflict`; the unique control retains all nine inherited files byte-for-byte. The ambiguous variant changes only `sources.json`: it appends at `sources[4]` a byte-for-byte-equivalent JSON object copied from the existing `sella-bell7-note` row. The original four source rows remain in order, with no excerpt, event, or ledger edits. The duplicate is an input alias, not a second witness.

Byte comparison across all nine inherited file names: the unique fixture has no differing files from r35; the ambiguous fixture differs from the unique fixture only in `sources.json`. The source row rises from four to five; `sella-bell7-note` count is 1 in the control and 2 in the negative. There are four timeline events in each, with each event ID count exactly 1. The contradiction ledger keeps its original event pointers: `claim_a=tarin-envelope-observation`, `claim_b=sella-bell7-presence`; thus `claim_a` source `tarin-note` remains unique, and both event pointers remain unique.

## Checker replay: complete raw output

Command for each fixture: `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-directory>`.

### Unique control

```text
stdout (exit 0):
CLEAN: schema, citations, relations, timeline; 0 violations

stderr (empty, 0 bytes):

exit status: 0
```

### Ambiguous source

```text
stdout (exit 1):
VIOLATION: sources[4].id: duplicate sources id 'sella-bell7-note'
VIOLATION: contradictions[0].claim_b.source_id: ambiguous in-world source 'sella-bell7-note'
VIOLATION: timeline[3].source_id: ambiguous in-world source 'sella-bell7-note'
3 violation(s); no canon changed

stderr (empty, 0 bytes):

exit status: 1
```

Collateral inventory is complete: besides the duplicate row and ledger `claim_b.source_id` finding, `timeline[3].source_id` is ambiguous because that Sella event cites the same source ID. No `claim_a` ambiguity or event-ID finding occurs. The temporary r7 reviewer probe already exercised ledger source ambiguity on `claim_a` using `archive-ledger`; this fixture contributes only a committed Bell-7 `claim_b` counterpart, not first coverage of ledger source ambiguity as a class, a new checker rule, or a canon winner. Structural source identity ambiguity does not establish either account’s truth or choose a source row.
