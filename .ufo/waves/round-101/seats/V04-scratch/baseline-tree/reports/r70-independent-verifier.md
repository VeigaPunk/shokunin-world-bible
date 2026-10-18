# Round 70 independent verifier

## Scope and method

I independently archived pinned baseline `5ccbffaf4b593dcfa34bf92a8ac351c83a105ab3` from Git with `git archive` into `/tmp/lore-r70-pinned-5ccbffa`. The archived checker and fixture bytes are the baseline; the working-tree checker and seven `r70-*` fixture directories are the candidate. No checker, fixture, README, or LOG changes were made by this verifier.

I compared every file under the pinned `.shokunin/lore/corpus/fixtures` tree to the corresponding working-tree path as raw bytes. Then, from repository-root cwd and using the same root-relative fixture arguments, I ran both checkers on each of the 130 old fixture directories and captured process exit status, stdout bytes, and stderr bytes. I ran the same pinned and candidate checkers against all seven new matched r70 fixture directories, capturing the same raw tuple. The command form was `python3 <checker> .shokunin/lore/corpus/fixtures/<fixture>`.

## Old fixture tree and raw CLI replay

The pinned fixture tree contains 709 files under 130 fixture directories. All 709 old paths still exist in the working tree; the 130 old directory paths also match. Of the old files, 707 are byte-identical. The only two byte differences are the declared candidate targets: `README.md` and `check_bible.py`. The candidate adds 35 paths: five JSON files in each of seven new r70 fixture directories.

For all 130 old fixture directories, the pinned checker and candidate checker produced **130/130 identical tuples** (exit code, raw stdout bytes, raw stderr bytes); there were zero mismatches. All 130 stderr streams were empty. I used identical root-relative fixture arguments for both checkers, avoiding path-dependent loader messages. This establishes old-fixture output preservation for the candidate, not correctness or materiality by itself.

## Seven new matched fixtures: exact old-to-candidate results

All seven stderr streams were empty for both checkers. `r70-absent`, `r70-empty`, and `r70-whitespace` each changed from exit **1** and these three stdout lines:

```text
VIOLATION: contradictions[0].claim_a.event_id: required nonempty string
VIOLATION: contradictions[0].claim_b.event_id: required nonempty string
VIOLATION: contradictions[0]: claim_a and claim_b references must differ
3 violation(s); no canon changed
```

to exit **1** and:

```text
VIOLATION: contradictions[0].claim_a.event_id: required nonempty string
VIOLATION: contradictions[0].claim_b.event_id: required nonempty string
2 violation(s); no canon changed
```

Thus the exact delta in each of those three controls is removal of only the pair-level finding and corresponding count decrement; both local required-ID errors remain.

The other four new fixtures had identical raw tuples under pinned and candidate checkers:

| Fixture | Exit | Exact stdout (stderr empty) |
|---|---:|---|
| `r70-valid-id-invalid-field` | 1 | `VIOLATION: contradictions[0].claim_a.field: expected one of ['depends_on', 'place_id', 'tick']`
`VIOLATION: contradictions[0].claim_b.field: expected one of ['depends_on', 'place_id', 'tick']`
`VIOLATION: contradictions[0]: claim_a and claim_b references must differ`
`3 violation(s); no canon changed` |
| `r70-valid-identical` | 1 | `VIOLATION: contradictions[0]: claim_a and claim_b references must differ`
`1 violation(s); no canon changed` |
| `r70-valid-different` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| `r70-distinct-field` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |

These controls show that the candidate retains the pair finding for equal nonempty IDs even when both fields are invalid, retains it for a valid identical pair, and emits no pair finding for distinct IDs or distinct fields. In particular, this is the event-ID-only gate, not the broader R69 field-validity gate.

## R62 retention

`r62-malformed-side` has the same raw tuple under both checkers: exit **1**, empty stderr, and exact stdout:

```text
VIOLATION: timeline.json: cannot load JSON: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
VIOLATION: contradictions[0].claim_a.field: expected one of ['depends_on', 'place_id', 'tick']
VIOLATION: contradictions[0].claim_b.field: expected one of ['depends_on', 'place_id', 'tick']
VIOLATION: contradictions[0]: claim_a and claim_b references must differ
4 violation(s); no canon changed
```

So the R62 pair warning is retained despite its matching invalid fields; both event IDs are nonempty strings. This independently verifies the required R62 counter-control.

## Limits

The replay verifies file bytes and checker outputs only for the committed 130 old fixtures and seven committed new cases. The new cases cover both IDs absent, both empty, both whitespace-only, matching nonempty IDs with invalid fields, valid identical references, valid different references, and distinct fields. They do not cover a one-invalid/one-usable ID pair or every non-string ID shape. A finite output matrix cannot establish whether editors benefit from seeing the removed pair warning early; as the critic noted, it might prompt a later distinct-pointer repair even when IDs are currently missing. I therefore report the observed exact behavior and preservation, not a demonstrated user-repair or material calibration benefit.

This is solely about structural diagnostics on supplied JSON inputs. It makes no claim about source text, event occurrence, fictional truth, canon, rights, or game mechanics.
