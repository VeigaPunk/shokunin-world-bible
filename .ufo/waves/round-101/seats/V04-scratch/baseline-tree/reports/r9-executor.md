# Round 9 executor report — duplicate dependency target guard

## Change

In the timeline dependency lookup, use the existing `event_id_counts` before reading a target tick. A dependency with count 0 retains the existing unknown-event finding; count greater than 1 emits `ambiguous dependency event` at the indexed dependency location and skips tick inference; count 1 retains the existing inversion comparison. The repeat/self checks and their order are unchanged.

## Evidence

Executed with `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture>`:

- `r9-dup-low-high` (duplicate `same` ticks 1 then 5; consumer tick 3): exit 1
  ```
  VIOLATION: timeline[1].id: duplicate timeline id 'same'
  VIOLATION: timeline[2].depends_on[0]: ambiguous dependency event 'same'
  2 violation(s); no canon changed
  ```
- `r9-dup-high-low` (same rows reversed): exit 1, identical findings and count:
  ```
  VIOLATION: timeline[1].id: duplicate timeline id 'same'
  VIOLATION: timeline[2].depends_on[0]: ambiguous dependency event 'same'
  2 violation(s); no canon changed
  ```
- `r9-unique-control` (unique `same` at tick 1, consumer at tick 3): exit 0
  ```
  CLEAN: schema, citations, relations, timeline; 0 violations
  ```

For every pre-existing fixture present at baseline commit `9e1de57` (16 fixture directories), I ran both `/tmp/check_bible_baseline_9e1de57.py` (extracted from that commit) and the edited checker against the same current fixture directory. All 16 had identical exit codes and byte-identical output. This includes `r8-deps-anomalous`; its repeated dependency and self-dependency diagnostics are unchanged. Specifically: `ally-one-way` 1/1; `ally-reciprocal` 0/0; `consistent` 0/0; `contradictions-ledger-malformed` 1/1; `contradictions` 1/1; `item-chain-broken` 1/1; `item-chain-valid` 0/0; `r5-invalid-citation` 1/1; `r5-invalid-json` 1/1; `r5-missing-file` 1/1; `r5-row-shape` 1/1; `r5-wrong-top-level` 1/1; `r7-ally-reverse-ambiguous` 1/1; `r7-item-ambiguous` 1/1; `r8-deps-anomalous` 1/1; `r8-deps-distinct` 0/0.

No fixtures, docs, LOG, or commits were changed by this executor. The only implementation change is `.shokunin/lore/corpus/fixtures/check_bible.py`; this report is the only other path written.
