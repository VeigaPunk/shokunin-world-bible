# Round 6 executor report — optional item provenance

## Implementation

Updated `corpus/fixtures/check_bible.py` only. An entity may include an optional `provenance` property. Its absence (including on an item) is accepted and does not infer history. If present, provenance must be an array on an item entity; each record must have exactly `tick`, `from_holder`, `to_holder`, and `source_id`. `tick` is a nonnegative exact integer (booleans are not integers here); `from_holder` is null or a nonempty ID; `to_holder` and `source_id` are nonempty IDs. Both non-null holder references must resolve to entity IDs, and source IDs must resolve to in-world sources. Each record is checked independently for malformed fields/references, and malformed records are not used as chain evidence. Extra record keys are reported as malformed.

For chain judgment, the item ID and every referenced holder ID must each identify exactly one entity; duplicate-ID entities retain the existing duplicate-ID error and do not participate in chain judgments. On an unambiguous item, the first valid record must have `from_holder: null` (the explicit acquisition). Every later valid record must have a tick strictly greater than the preceding record's tick and a `from_holder` equal to the preceding record's `to_holder`. Tick violations and predecessor mismatches are reported at that record; records are not reordered or modified. A malformed record disables subsequent chain judgment for that item's listed sequence rather than treating it as absent or guessing a predecessor. Provenance on a non-item is reported and not chain-judged.

No checks infer a record from claims, `carries` relations, timeline text, or gameplay; ticks are local provenance ordering markers, not linked to timeline events. A resolvable source pointer is not verification of source content or truth.

## Regression replay

Executed from repository root with `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>`; stderr was empty in every run. Existing cases retained their outcomes: `consistent` and `ally-reciprocal` exit 0; `contradictions` exits 1 with its same three findings (dangling `missing-map`, timeline inversion, and double-booked Mira); `ally-one-way` exits 1 with its existing missing reciprocal finding; `contradictions-ledger-malformed` exits 1 with its existing malformed event reference plus those three findings. The five round-5 malformed cases retain their prior single errors: missing file, invalid JSON, wrong top-level type, non-object row, and unknown citation, respectively.

New paired cases supplied by the parent: `item-chain-valid` exits 0; its initial null-predecessor acquisition and two ordered transfers form a consistent chain. `item-chain-broken` exits 1 with exactly `entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'`. The sibling fixtures differ only in that last `from_holder` value. This tests a local break without resolving which assertion is true.

## Limits

This implements only the declared structural chain convention. It does not verify source semantics, decide conflicts, prove complete history, or establish custody between ticks. No fixtures were edited by this executor.
