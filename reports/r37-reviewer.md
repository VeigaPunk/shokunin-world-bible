# Round 37 non-author reviewer — ledger endpoint duplicate

## Verdict: PASS (bounded)

I independently compared both r37 fixture copies with `r35-bell7-conflict`, inspected the r9 duplicate fixtures, and ran the checker on each r37 fixture from the repository root:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r37-ledger-unique
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r37-ledger-ambiguous
```

The unique control exits 0, stdout exactly `CLEAN: schema, citations, relations, timeline; 0 violations`, stderr empty. The ambiguous fixture exits 1, stderr empty, and has exactly these two stdout diagnostics:

```text
VIOLATION: timeline[4].id: duplicate timeline id 'tarin-envelope-observation'
VIOLATION: contradictions[0].claim_a.event_id: expected exactly one timeline event 'tarin-envelope-observation'
2 violation(s); no canon changed
```

The ninth inherited file set from r35 is unchanged in the unique fixture. In the ambiguous fixture only `timeline.json` differs from r35. Its original four rows are retained in order and unchanged; an identical copy of original row `timeline[2]` is appended at index 4. Thus the schema-valid `tarin-envelope-observation` ID occurs twice, while `sella-bell7-presence` occurs once. `contradictions.json` and both event-field endpoints are unchanged: claim_a points at `tarin-envelope-observation.place_id`, claim_b at `sella-bell7-presence.place_id`. The source registry, both cited excerpts, and the clause/manual maps are also byte-identical to r35. This confirms the duplicate is the sole fixture change and the copy preserves the original row and citations.

Round 9's `r9-dup-low-high` / `r9-dup-high-low` fixtures already exercise generic duplicate timeline IDs and ambiguous dependency lookup (`consumer.depends_on: ["same"]`), including row-order variation. They do not contain a contradiction ledger endpoint. R37 therefore demonstrates a distinct input branch: exact-one cardinality validation when a ledger endpoint targets an ID duplicated in timeline. The observed claim_a endpoint diagnostic accompanies the global duplicate-ID diagnostic; claim_b remains uniquely represented. No last-row or first-row selection is justified. (The checker may build a last-wins internal ID index, but the ledger cardinality guard rejects this endpoint before treating it as unique.)

## Limits

This is structural checker/fixture evidence only. It does not establish that either fictional testimony is true or false, that the narrative reports are semantically incompatible, that their occasion/identity assumptions hold, or that canon has been resolved. A clean unique-pointer result is not proof of source-text truth; this duplicate case only makes claim_a ambiguous as a structured pointer. No inference about testimony or canon is made.
