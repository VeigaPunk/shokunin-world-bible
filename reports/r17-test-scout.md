# Round 17 test scout — raw replay and probe results

Role: read-only test scout. This report is the only file written. I did not change the checker, fixtures, shared docs, or commit.

## Raw CLI replay: 33 baseline fixtures

Ran each command as `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>` and recorded stdout findings and exit code. Compared all results to saved transcripts in `corpus/live/runs/20261012T182817Z/`: **33/33** match exactly in stdout, stderr, and exit code. The 29 pre-r16 fixtures also match their original baseline transcripts; the four r16 fixture outputs match the round-16 corrected run. Read-only replay SHA-256 check covered 165 files (checker + 164 JSON files), with no changes.

| Fixture | Exit | Raw CLI findings (stdout, omitting `VIOLATION:` prefix) |
|---|---:|---|
| `ally-one-way` | 1 | relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation |
| `ally-reciprocal` | 0 | CLEAN |
| `consistent` | 0 | CLEAN |
| `contradictions` | 1 | relations[1].to: dangling entity 'missing-map'; timeline[1].depends_on: timeline inversion 'later' tick 3 not before 'arrival' tick 2; timeline[2]: double-booked 'mira' at tick 2 in timeline[1] ('tower') and 'harbor' |
| `contradictions-ledger-malformed` | 1 | contradictions[1].claim_b.event_id: expected exactly one timeline event 'absent-event'; relations[1].to: dangling entity 'missing-map'; timeline[1].depends_on: timeline inversion 'later' tick 3 not before 'arrival' tick 2; timeline[2]: double-booked 'mira' at tick 2 in timeline[1] ('tower') and 'harbor' |
| `item-chain-broken` | 1 | entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira' |
| `item-chain-valid` | 0 | CLEAN |
| `r10-registry-witness` | 0 | CLEAN |
| `r11-character-place` | 1 | entities[2].id: duplicate entities id 'harbor'; timeline[0].place_id: ambiguous place entity 'harbor' |
| `r11-dangling-place` | 1 | timeline[0].place_id: dangling entity 'unlisted' |
| `r11-place-character` | 1 | entities[2].id: duplicate entities id 'harbor'; timeline[0].place_id: ambiguous place entity 'harbor' |
| `r11-unique-nonplace` | 1 | timeline[0].place_id: not a place 'mira' |
| `r12-ambiguous-actor` | 1 | entities[4].id: duplicate entities id 'mira'; timeline[0].entity_id: ambiguous actor entity 'mira'; timeline[1].entity_id: ambiguous actor entity 'mira' |
| `r12-unique-actor` | 1 | timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower' |
| `r13-missing-actor` | 1 | timeline[0].entity_id: dangling entity 'unlisted'; timeline[1].entity_id: dangling entity 'unlisted' |
| `r13-unique-actor` | 1 | timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower' |
| `r15-carbon-followup` | 0 | CLEAN |
| `r16-missing-first` | 1 | timeline[0].place_id: dangling entity 'unlisted' |
| `r16-missing-place` | 1 | timeline[1].place_id: dangling entity 'unlisted' |
| `r16-mixed-three` | 1 | timeline[1].place_id: dangling entity 'unlisted'; timeline[2]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower' |
| `r16-valid-places` | 1 | timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower' |
| `r5-invalid-citation` | 1 | relations[0].source_id: unknown in-world source 'absent-source' |
| `r5-invalid-json` | 1 | contradictions.json: cannot load JSON: Expecting property name enclosed in double quotes: line 2 column 1 (char 2) |
| `r5-missing-file` | 1 | contradictions.json: cannot load JSON: [Errno 2] No such file or directory: '.shokunin/lore/corpus/fixtures/r5-missing-file/contradictions.json' |
| `r5-row-shape` | 1 | contradictions[0]: expected object |
| `r5-wrong-top-level` | 1 | contradictions.json: expected array |
| `r7-ally-reverse-ambiguous` | 1 | sources[2].id: duplicate sources id 'harbor-compact'; relations[1].source_id: ambiguous in-world source 'harbor-compact'; relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation |
| `r7-item-ambiguous` | 1 | sources[2].id: duplicate sources id 'archive-ledger'; entities[1].first_appearance: ambiguous in-world source 'archive-ledger'; entities[1].claims[0].source_id: ambiguous in-world source 'archive-ledger'; entities[2].first_appearance: ambiguous in-world source 'archive-ledger'; entities[2].claims[0].source_id: ambiguous in-world source 'archive-ledger'; entities[3].provenance[1].source_id: ambiguous in-world source 'archive-ledger'; entities[3].provenance[2].source_id: ambiguous in-world source 'archive-ledger' |
| `r8-deps-anomalous` | 1 | timeline[1].depends_on[1]: repeated dependency 'departure'; timeline[1].depends_on[2]: self dependency 'arrival'; timeline[1].depends_on: timeline inversion 'arrival' tick 2 not before 'arrival' tick 2 |
| `r8-deps-distinct` | 0 | CLEAN |
| `r9-dup-high-low` | 1 | timeline[1].id: duplicate timeline id 'same'; timeline[2].depends_on[0]: ambiguous dependency event 'same' |
| `r9-dup-low-high` | 1 | timeline[1].id: duplicate timeline id 'same'; timeline[2].depends_on[0]: ambiguous dependency event 'same' |
| `r9-unique-control` | 0 | CLEAN |

## Temporary paired schedule probes (current checker; no repository fixtures created)

Constructed three temporary fixture copies from `r16-valid-places`, replacing only `timeline.json` with same-tick rows for actor `mira` (each event cites existing `courier-log`). The exact CLI outcomes:

- **wrong-kind**, rows `[harbor, mira]` (where `mira` is uniquely a character): exit 1; `timeline[1].place_id: not a place 'mira'`; **and** `timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'mira'`.
- **valid**, rows `[harbor, tower]` (both unique places): exit 1; `timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'`.
- **mixed**, rows `[harbor, mira, tower]`: exit 1; the wrong-kind finding and its definite comparison above, plus `timeline[2]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'`.

The existing 33-case suite also contains kind/ID boundary controls: `r11-unique-nonplace` reports `not a place 'mira'`; `r11-place-character` and `r11-character-place` report ambiguous `harbor` (duplicate ID); r16 missing-place controls report dangling and no double-booking, while `r16-valid-places` and `r16-mixed-three` retain known harbor/tower conflict. These controls distinguish the unique wrong-kind case from duplicate and count-zero cases.

## Recommendations (not changes)

1. The paired probe reproduces the declared defect: current guard admits `place_id_count != 0`, so a unique wrong-kind ID is still treated as an occupancy location after the separate `not a place` finding. If round-17 claim is upheld, require exactly one resolved entity **and** kind `place` before occupancy comparison/update; preserve the `not a place` finding.
2. Keep `r11-unique-nonplace` as a negative/non-place control; retain the two-ID-order ambiguous controls, the valid `[harbor,tower]` conflict control, and the `[harbor,mira,tower]` mixed schedule. Current mixed probe already shows a valid known-pair finding coexists with wrong-kind double-booking; after any checker edit verify only the latter is withheld.
3. Replay the same 33 fixture CLI outputs byte-for-byte after a code change. In particular, do not weaken r16 missing-place behavior or the known harbor/tower findings in `r16-mixed-three`.
4. These are checker-input findings, not proof of narrative truth, actual location, or absence/presence of an in-world conflict. No citation establishes that the temporary schedule describes canon.
