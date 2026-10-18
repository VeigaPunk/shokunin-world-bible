# r91-c1-tick-unresolved

Fixture scaffolding only; not sourced story evidence.

Purpose: show that tick ordering is independent of holder identity while a separate chain break remains qualified.

Run from `lore-shokunin/`:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
```

The predecessor's `f3-dup` holder has two raw entity rows and one resolved-index row; the later row compares it with `mira`. Tick `1` follows tick `3`, so the tick is invalid while the identity-dependent chain break stays qualified.

## Expected output with e97613c (exit 1; stderr empty)

Complete stdout:

```text
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); provenance tick 1 must be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed
```

## Expected output with the delivered checker (exit 1; stderr empty)

Complete stdout:

```text
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed
```

Only the tick finding changes: it is integer-only under the delivered checker. The qualified chain-break line must remain byte-for-byte unchanged.
