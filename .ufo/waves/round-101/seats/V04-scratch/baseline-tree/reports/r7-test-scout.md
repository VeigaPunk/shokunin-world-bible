# Round 7 test scout — replay matrix

Scope: map old fixture coverage and probe duplicate source-ID behavior from the current working tree. This is a scout report, not checker/fixture modification. **Observed** means run against the current `check_bible.py`; **proposed** means a replay expectation for the round-7 change, not an observed result after that change.

## Observed old-fixture replay

At repo root I ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>` for the listed cases. Captured output is also present at `.shokunin/lore/corpus/live/runs/20261012T165220Z/` for the unchanged old matrix (cases without a round-6 addition have the earlier capture `.shokunin/lore/corpus/live/runs/20261012T164316Z/`). Results:

| Fixture | Exit | Observed diagnostic/result |
|---|---:|---|
| `consistent` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| `contradictions` | 1 | 3 violations: dangling `missing-map`, timeline inversion, double-booked Mira |
| `ally-one-way` | 1 | `relations[0] ... lacks a sourced reciprocal relation` |
| `ally-reciprocal` | 0 | `CLEAN ... 0 violations` |
| `contradictions-ledger-malformed` | 1 | 4 violations: absent contradiction event plus the three `contradictions` findings |
| `item-chain-valid` | 0 | `CLEAN ... 0 violations` |
| `item-chain-broken` | 1 | `entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'` |
| `r5-invalid-citation` | 1 | unknown in-world source `absent-source` |
| `r5-invalid-json` | 1 | `contradictions.json: cannot load JSON` (JSON parse error) |
| `r5-missing-file` | 1 | `contradictions.json: cannot load JSON` (missing file) |
| `r5-row-shape` | 1 | `contradictions[0]: expected object` |
| `r5-wrong-top-level` | 1 | `contradictions.json: expected array` |

Exact saved CLI transcripts for these outcomes are the named `<case>.txt` files under the run directories above. This preserves baseline assertions: source uniqueness change should not alter the old matrix.

## Observed duplicate-source witness probes (current checker)

I made temporary copies of two existing fixtures under `/tmp/lore-r7-probes-q94a6mvw/` and appended one copy of the first source record to each `sources.json` (retaining all existing rows/references). These probes were not committed fixtures and the temporary directory was removed after the run.

| Temporary probe derived from | New duplicate | Command result observed |
|---|---|---|
| `ally-reciprocal` | second `harbor-compact` record | Exit 1, only `VIOLATION: sources[1].id: duplicate sources id 'harbor-compact'`; **no** alliance finding; duplicate-ID source still qualifies as the reciprocal witness. |
| `item-chain-valid` | second `archive-ledger` record | Exit 1, only `VIOLATION: sources[2].id: duplicate sources id 'archive-ledger'`; **no** provenance citation finding; duplicate-ID source still qualifies for the transfer records. |

The exact commands used were `python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r7-probes-q94a6mvw/duplicate-alliance` and the corresponding `/duplicate-provenance`. Current `check_bible.py` constructs `sources = index('sources')`, where duplicate IDs emit an error but the later row overwrites the map; alliance witness uses `candidate['source_id'] in sources`; item provenance calls `source(source_id, ...)`, which likewise only checks dictionary membership. This is the concrete baseline behavior, not a claim about a future implementation.

## Proposed replay matrix for the change

Keep the twelve old rows above as regression controls. Add durable, minimal cases once the executor integrates them (or construct raw copies in a verifier scratch area):

1. **Unique-source positive controls:** existing `ally-reciprocal` and `item-chain-valid` remain exit 0 and retain their current clean line.
2. **Duplicate source alone:** use a duplicate record ID and no reference to that duplicated ID. Expect exit 1 for the duplicate ID only; establishes that duplicate records remain present and the checker still reports the base violation.
3. **Duplicate alliance witness:** start with `ally-reciprocal`; duplicate the `harbor-compact` source ID while leaving both reciprocal relations intact and cited to it. Expect exit 1 with duplicate-ID finding plus a local finding that the would-be reverse relation is not a qualified, unambiguous sourced witness. Do not expect the duplicate relation or source record to be deleted/selected.
4. **Duplicate provenance witness:** start with `item-chain-valid`; duplicate `archive-ledger`, which is cited by provenance records at `entities[3].provenance[1:3]`. Expect exit 1 with duplicate-ID finding and local ambiguous-source findings for those records; do not report a chain break merely because the citation is ambiguous unless the implementation's declared diagnostic contract explicitly does so.
5. **No false cascade control:** duplicate an unrelated source ID while retaining an otherwise valid uniquely cited alliance/provenance witness. Proposed expectation: duplicate ID is reported, but unrelated unique witness behavior is retained. This tests that ambiguity is scoped to the duplicated identifier rather than poisoning every witness.

For each new durable row, record exact input mutation (changed `sources.json` plus any other changed file), command, exit status and complete stdout/stderr. Compare pre/post fixture manifests and checker hash in the independent verification phase; the probes above are only exploratory current-state runs and do not establish post-change integrity.

Limits: IDs are resolution keys; these checks cannot establish whether a source text supports a claim, whether a witness is true in-world, or whether the two records are legitimate distinct documents. The scout probes only exercise alliance reciprocity and item provenance, not every source-reference site.
