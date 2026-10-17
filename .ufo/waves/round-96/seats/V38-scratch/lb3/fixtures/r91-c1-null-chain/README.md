# r91-c1-null-chain

Fixture scaffolding only; not sourced story evidence.

Purpose: discriminate the null-holder identity repair. The predecessor resolves uniquely to `mira`; the later record uses `from_holder: null`.

Run from `lore-shokunin/`:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
```

This fixture copies `item-chain-valid` and changes only the seal's provenance records to two valid, source-resolving rows. The only intentional defect is the null `from_holder` on the second row.

## Expected output with e97613c (exit 1; stderr empty)

Complete stdout:

```text
VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)
1 violation(s); no canon changed
```

## Expected output with the delivered checker (exit 1; stderr empty)

Complete stdout:

```text
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None
1 violation(s); no canon changed
```

The changed finding must be definite and say `got None`; a silent revert to e97613c restores the hedged output above.
