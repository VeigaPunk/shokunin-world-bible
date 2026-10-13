# Round 70 executor — event-ID-only pair gate

## Change

At the final claim-pair check, require each side to have a nonempty string `event_id` (same predicate as the local required-ID check) before evaluating the existing raw event-ID and raw field equality. The field-validity diagnostics and all other checker logic are unchanged. This is a structural input-ledger condition; it does not establish event existence, sourced support, canon, or a semantic contradiction.

Added seven matched five-table fixtures based on `consistent`: `r70-absent`, `r70-empty`, `r70-whitespace`, `r70-valid-id-invalid-field`, `r70-valid-identical`, `r70-valid-different`, and `r70-distinct-field`. The README documents the cases.

## CLI results

Commands used from repository root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>
```

Each case below had empty stderr.

| Fixture | Exit | Exact stdout |
|---|---:|---|
| `r70-absent` | 1 | See exact output blocks below. |
| `r70-empty` | 1 | See exact output blocks below. |
| `r70-whitespace` | 1 | See exact output blocks below. |
| `r70-valid-id-invalid-field` | 1 | See exact output blocks below. |
| `r70-valid-identical` | 1 | See exact output blocks below. |
| `r70-valid-different` | 0 | See exact output blocks below. |
| `r70-distinct-field` | 0 | See exact output blocks below. |

`r70-absent`, `r70-empty`, and `r70-whitespace` (each):

```text
VIOLATION: contradictions[0].claim_a.event_id: required nonempty string
VIOLATION: contradictions[0].claim_b.event_id: required nonempty string
2 violation(s); no canon changed
```

`r70-valid-id-invalid-field`:

```text
VIOLATION: contradictions[0].claim_a.field: expected one of ['depends_on', 'place_id', 'tick']
VIOLATION: contradictions[0].claim_b.field: expected one of ['depends_on', 'place_id', 'tick']
VIOLATION: contradictions[0]: claim_a and claim_b references must differ
3 violation(s); no canon changed
```

`r70-valid-identical`:

```text
VIOLATION: contradictions[0]: claim_a and claim_b references must differ
1 violation(s); no canon changed
```

`r70-valid-different` and `r70-distinct-field` (each):

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```


The three missing/blank controls retain their independent local required-ID diagnostics and lose only the pair-level finding. A nonempty ID with matching invalid fields still receives the pair finding. The distinct-field control confirms raw field equality remains required.

## R62 and baseline replay

`r62-malformed-side` remains exit 1 with empty stderr and exactly:

```text
VIOLATION: timeline.json: cannot load JSON: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
VIOLATION: contradictions[0].claim_a.field: expected one of ['depends_on', 'place_id', 'tick']
VIOLATION: contradictions[0].claim_b.field: expected one of ['depends_on', 'place_id', 'tick']
VIOLATION: contradictions[0]: claim_a and claim_b references must differ
4 violation(s); no canon changed
```

Replayed all 130 pre-existing fixture directories using both the HEAD checker (baseline) and candidate checker with identical root-relative fixture arguments. **130/130 exit-code, raw stdout-byte, and raw stderr-byte tuples match exactly; zero changed cases.** Baseline outcomes: 25 exit 0, 105 exit 1; every stderr stream empty. The seven new `r70-*` controls were excluded from this 130-case baseline set.

## Limits

These fixtures demonstrate branch behavior and preserve current fixture outputs, including R62. They do not establish that suppressing an unusable-ID pair warning improves editor repair, that any event ID exists, or that the cited fields are supported by source text. No source text, canon, rights, or mechanics were changed or assessed. No LOG/other report edits, commit, push, or merge.
