# Round 17 fixture scout — wrong-kind / valid controls

## Observed baseline CLI (raw)

Baseline source: `git show 1dd6f27ae89a096c8fb99d2750f35e5118fda5d3:.shokunin/lore/corpus/fixtures/check_bible.py`. Its SHA-256 matches the working checker (`bf2061b5c6f4e5f67f6c6f8dfbe31b0141c9541e259fe4ddf333aebef92b19b6`). I wrote three temporary probe directories under `/tmp/r17-fixture-scout/`, copied the `r16-valid-places` fixture's source/entity files unchanged, and replaced only `timeline.json`. Each command below ran the extracted baseline checker; exit status is shown separately.

Fixture prose is input-scoped: each event description says “Fixture input” and identifies the input `place_id`; the wrong-kind row notes that indexed `mira` is a character. The inherited `source_id` is `courier-log`, but the descriptions do not attribute those place statements to that source.

### `wrong-kind-valid`

Timeline order: known `harbor`, then wrong-kind `mira`.

```text
$ python3 /tmp/r17-baseline-check_bible.py /tmp/r17-fixture-scout/wrong-kind-valid
VIOLATION: timeline[1].place_id: not a place 'mira'
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'mira'
2 violation(s); no canon changed
exit status: 1
```

### `valid-control`

Timeline order: known `harbor`, then known `tower`.

```text
$ python3 /tmp/r17-baseline-check_bible.py /tmp/r17-fixture-scout/valid-control
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
exit status: 1
```

### `known-wrong-known`

Timeline order: known `harbor`, wrong-kind `mira`, known `tower`.

```text
$ python3 /tmp/r17-baseline-check_bible.py /tmp/r17-fixture-scout/known-wrong-known
VIOLATION: timeline[1].place_id: not a place 'mira'
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'mira'
VIOLATION: timeline[2]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
3 violation(s); no canon changed
exit status: 1
```

## Recommendations (not observations)

- Keep the paired wrong-kind/valid case: it shows the current raw-ID behavior and the actual-place positive control with the same actor and tick.
- Keep `known-wrong-known` as the order control. If occupancy is changed to require a unique entity of kind `place`, the expected narrow behavior is `not a place` for the middle event, no definite different-resolved-places finding for that pair, and a retained `harbor`/`tower` finding at the final event.
- Keep fixture descriptions explicitly scoped to fixture input. Avoid saying the courier log “places” Mira at any location: `source_id` reference identity alone does not attest that prose. Do not describe the wrong-kind row as a place or imply its actual location is known.
- These examples test these orders only; they do not establish that every arrangement is covered, what Mira's actual location was, canon truth, or absence of a real conflict.
