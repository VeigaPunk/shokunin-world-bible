# Round 89 F1: valid-key multi-cause record

Purpose: pin the valid-key combined-cause path. The sole provenance record has exactly the four required keys and carries two simultaneous latching defects: negative `tick` and `to_holder` resolving to two admitted entity rows. This is intentionally distinct from a shape-invalid record.

## Expected after the C1 fix

- Checker exit: `1` (the duplicate entity ID, invalid tick, and ambiguous holder remain findings).
- The record at `entities[2].provenance[0]` discloses a first-stop summary containing **both** `malformed record (invalid tick)` and `ambiguous holder identity to_holder 'r89-c1-multi-cause-valid-ambiguous-holder'`.
- No cause is omitted or selected by precedence in the combined summary. The baseline checker emits both local findings but its first-stop disclosure names only the invalid tick.

This is fixture scaffolding, not sourced story evidence. The after-state is an expectation for integration replay; F1.md records the unpatched before-state measurement.
