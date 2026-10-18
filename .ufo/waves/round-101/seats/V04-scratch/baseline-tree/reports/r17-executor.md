# Round 17 executor evidence

Scope: checker-only narrow guard. Change excludes a count-one non-place `place_id` from occupied-slot comparison and insertion, while retaining `actor_id_count == 1` and `place_id_count != 0`. Existing `not a place` finding is untouched. Duplicate-count place IDs remain comparable as before. No fixtures, docs, LOG, or commits were edited by this executor.

Baseline: `1dd6f27:.shokunin/lore/corpus/fixtures/check_bible.py` (SHA-256 `bf2061b5c6f4e5f67f6c6f8dfbe31b0141c9541e259fe4ddf333aebef92b19b6`). Working checker SHA-256 `cae2dc969c2a28512d957024e6d946585c796684747619f45f39a70022b5b222`.

## Baseline regression replay

Reconstructed each of the 33 fixture directories listed in the baseline commit with `git show` from `1dd6f27`; ran both checker scripts under `python3`, capturing return code, stdout, and stderr. All 33 produced byte-for-byte identical stdout and stderr and identical exit status. Baseline/current exit status by fixture:
- `ally-one-way`: 1
- `ally-reciprocal`: 0
- `consistent`: 0
- `contradictions-ledger-malformed`: 1
- `contradictions`: 1
- `item-chain-broken`: 1
- `item-chain-valid`: 0
- `r10-registry-witness`: 0
- `r11-character-place`: 1
- `r11-dangling-place`: 1
- `r11-place-character`: 1
- `r11-unique-nonplace`: 1
- `r12-ambiguous-actor`: 1
- `r12-unique-actor`: 1
- `r13-missing-actor`: 1
- `r13-unique-actor`: 1
- `r15-carbon-followup`: 0
- `r16-missing-first`: 1
- `r16-missing-place`: 1
- `r16-mixed-three`: 1
- `r16-valid-places`: 1
- `r5-invalid-citation`: 1
- `r5-invalid-json`: 1
- `r5-missing-file`: 1
- `r5-row-shape`: 1
- `r5-wrong-top-level`: 1
- `r7-ally-reverse-ambiguous`: 1
- `r7-item-ambiguous`: 1
- `r8-deps-anomalous`: 1
- `r8-deps-distinct`: 0
- `r9-dup-high-low`: 1
- `r9-dup-low-high`: 1
- `r9-unique-control`: 0

Complete replay comparison: 33/33 exact matches (return code, stdout, stderr); 0 mismatches.

## Round-17 fixture replay

Ran baseline and working checker against all six present `r17-*` fixture directories. Exact captured output follows; stderr was empty in all cases.

### `r17-valid-places`
- Baseline exit: 1; working exit: 1
- Baseline stdout:
```text
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
```
- Working stdout:
```text
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
```
- stderr: empty (both)

### `r17-wrong-after`
- Baseline exit: 1; working exit: 1
- Baseline stdout:
```text
VIOLATION: timeline[1].place_id: not a place 'mira'
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'mira'
2 violation(s); no canon changed
```
- Working stdout:
```text
VIOLATION: timeline[1].place_id: not a place 'mira'
1 violation(s); no canon changed
```
- stderr: empty (both)

### `r17-wrong-before`
- Baseline exit: 1; working exit: 1
- Baseline stdout:
```text
VIOLATION: timeline[0].place_id: not a place 'mira'
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('mira') and 'tower'
2 violation(s); no canon changed
```
- Working stdout:
```text
VIOLATION: timeline[0].place_id: not a place 'mira'
1 violation(s); no canon changed
```
- stderr: empty (both)

### `r17-wrong-first`
- Baseline exit: 1; working exit: 1
- Baseline stdout:
```text
VIOLATION: timeline[0].place_id: not a place 'mira'
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('mira') and 'harbor'
VIOLATION: timeline[2]: double-booked 'mira' at tick 7 in timeline[0] ('mira') and 'tower'
3 violation(s); no canon changed
```
- Working stdout:
```text
VIOLATION: timeline[0].place_id: not a place 'mira'
VIOLATION: timeline[2]: double-booked 'mira' at tick 7 in timeline[1] ('harbor') and 'tower'
2 violation(s); no canon changed
```
- stderr: empty (both)

### `r17-wrong-last`
- Baseline exit: 1; working exit: 1
- Baseline stdout:
```text
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
VIOLATION: timeline[2].place_id: not a place 'mira'
VIOLATION: timeline[2]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'mira'
3 violation(s); no canon changed
```
- Working stdout:
```text
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
VIOLATION: timeline[2].place_id: not a place 'mira'
2 violation(s); no canon changed
```
- stderr: empty (both)

### `r17-wrong-middle`
- Baseline exit: 1; working exit: 1
- Baseline stdout:
```text
VIOLATION: timeline[1].place_id: not a place 'mira'
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'mira'
VIOLATION: timeline[2]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
3 violation(s); no canon changed
```
- Working stdout:
```text
VIOLATION: timeline[1].place_id: not a place 'mira'
VIOLATION: timeline[2]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
2 violation(s); no canon changed
```
- stderr: empty (both)

## Interpretation and limits

The valid-place fixture remains double-booked. All fixtures with a unique non-place location retain the `not a place` finding but no longer emit double-booking comparisons for that row. In wrong-first, a later valid-place conflict is still detected; the retained slot now correctly originates at `timeline[1]`. Baseline replay establishes compatibility on the 33 fixtures existing at commit `1dd6f27`; the six `r17-*` directories were working-tree fixtures and were exercised as found, not assumed to be independently verified or committed. No claims beyond these captured fixtures are made.
