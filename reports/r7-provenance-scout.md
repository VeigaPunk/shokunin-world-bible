# Round 7 provenance scout — duplicate-source item transfer judgment

## Scope and method

Read-only probe; no checker, fixture, or shared-doc changes. I inspected `corpus/fixtures/check_bible.py`, the round-6 `item-chain-valid` and `item-chain-broken` fixtures, then copied each fixture under `/tmp` and appended a duplicate source record while keeping the referenced `source_id` unchanged. CLI used:

```text
python3 /home/vgpnk/Projects/prymeagnt/lore/.shokunin/lore/corpus/fixtures/check_bible.py <temporary-fixture-dir>
```

Temporary paths shown below are the concrete probe paths from this run. These inputs were disposable copies; repository fixtures were not altered.

## Observed behavior

Baseline clean and broken chain controls:

- `.shokunin/lore/corpus/fixtures/item-chain-valid`: exit 0, stdout `CLEAN: schema, citations, relations, timeline; 0 violations`, stderr empty.
- `.shokunin/lore/corpus/fixtures/item-chain-broken`: exit 1, stdout `VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'` and `1 violation(s); no canon changed`; stderr empty.

Copied valid chain, duplicate cited `archive-ledger` at `/tmp/r7-prov-m095465x/item-chain-valid-archive-ledger`:

```text
VIOLATION: sources[2].id: duplicate sources id 'archive-ledger'
1 violation(s); no canon changed
```
Exit 1, stderr empty. Copy with duplicate `courier-log` at `/tmp/r7-prov-m_we2abr/item-chain-valid-courier-log` produced the same duplicate-ID-only pattern for `courier-log`.

Copied broken chain, duplicate cited `archive-ledger` at `/tmp/r7-prov-zzu8buxc/item-chain-broken-archive-ledger`:

```text
VIOLATION: sources[2].id: duplicate sources id 'archive-ledger'
VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'
2 violation(s); no canon changed
```
Exit 1, stderr empty. Copy with duplicate `courier-log` at `/tmp/r7-prov-d625lifu/item-chain-broken-courier-log` likewise produced the duplicate-ID violation plus the same chain-break finding.

The current implementation (`check_bible.py`) creates `sources` through `index('sources')`; `index` reports duplicates but overwrites the prior row with the last row. The provenance loop's `source(source_id, ...)` checks only membership (`source_id not in sources`). It therefore emits no local ambiguous-source diagnostic for a provenance citation. It continues to evaluate chain shape/order even when one or more provenance citations resolve only to duplicate IDs. A duplicate record copied from its original row does not change titles/notes in these probes; this probes duplicate-ID ambiguity, not evidence-text conflict.

## Risk and proposed handling (not implemented)

- **Observed risk:** a duplicate ID does not currently stop item-chain judgment. With the broken-chain fixture, the chain-break output is unchanged and co-reported with duplicate-ID. The checker cannot establish which duplicate source record was meant. This can read as a provenance assertion being citation-qualified when it is not uniquely resolved.
- **Cascade risk:** if round 7 changes generic source membership to “unique IDs only,” merely gating each record locally may create several extra missing/ambiguous-source findings for all fields citing that ID; independent structural chain diagnostics could also be misread as source-backed. The current probe shows the existing duplicate diagnostic is global (at `sources[2]`), not repeated at each item record.
- **Proposal:** keep source-ID duplication as one defining diagnostic, and mark a provenance record's citation as ambiguous locally (or otherwise expose the ambiguity at its reference) without calling it “unknown.” For chain judgment, consider a three-state distinction: uniquely cited and shape-valid; structurally inspectable but citation-ambiguous; unknown/malformed. Preserve structural chain findings only if they are explicitly labeled as source-independent asserted-record structure; otherwise gate source-dependent judgments while continuing safe shape checks. Avoid turning one duplicate source into unbounded repeated cascades across all records. This is a design proposal, not observed checker behavior.
- **Boundary:** no text-support or canon-truth conclusion is possible from the fixture's `sources.json`; this probe tests ID resolution and checker diagnostics only. A valid sequence under duplicate source IDs is not evidence that either duplicate document supports it.
