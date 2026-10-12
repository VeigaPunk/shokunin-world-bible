# Round 7 independent reviewer replay

No repository source/fixture edits were made. Temporary probes were cloned under `/tmp/lore-r7-*` with Python `shutil.copytree`, mutated in temporary copies, and invoked through `subprocess.run`.

## Raw fixture replay

From the repository root I ran, for each of the 14 raw fixture directories:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>
```

| Case | Exit | Observed result |
|---|---:|---|
| consistent | 0 | clean |
| contradictions | 1 | 3: dangling relation endpoint; timeline inversion; double-booking |
| ally-reciprocal | 0 | clean |
| ally-one-way | 1 | one missing sourced reciprocal |
| contradictions-ledger-malformed | 1 | 4: malformed ledger event reference plus the same 3 baseline contradictions |
| r5-missing-file | 1 | missing contradictions.json |
| r5-invalid-json | 1 | JSON parse error in contradictions.json |
| r5-wrong-top-level | 1 | contradictions.json expected array |
| r5-row-shape | 1 | contradictions[0] expected object |
| r5-invalid-citation | 1 | relations[0].source_id unknown |
| item-chain-valid | 0 | clean |
| item-chain-broken | 1 | one provenance chain break at entities[3].provenance[2] |
| r7-ally-reverse-ambiguous | 1 | duplicate source ID + ambiguous reverse reference + missing reciprocal finding |
| r7-item-ambiguous | 1 | duplicate archive-ledger ID + five ambiguous ordinary references + two ambiguous provenance references (7 total) |

The fixtures `r7-ally-reverse-ambiguous` and `r7-item-ambiguous` contain respectively 3 and 7 violations. Raw JSON was read directly from their `sources.json`, `entities.json`, `relations.json`, `timeline.json`, and `contradictions.json`; both fixtures retain both duplicate source records.

## Reference-site inspection

Inspected the entire `check_bible.py`, especially lines 45–74, 88–123, 145–220, and 225–233. `index('sources')` reports a repeated ID and overwrites the dictionary slot (last wins), but the `sources` dictionary is not otherwise used for source qualification. `source_id_counts` over valid source rows is the operative status map; `source_status` returns unknown/unique/ambiguous. `source()` emits a local unknown/ambiguous diagnostic.

All source-reference paths:

- contradiction ledger: each valid claim side resolves a unique timeline event, then checks that event's source status; ambiguous status calls `source(..., <side>.source_id)`, while unknown emits the separate “event ... has no resolvable source_id” wording;
- entity `first_appearance` and each valid claim `source_id` call `source()`;
- every relation `source_id` calls `source()`;
- every structurally well-formed provenance record `source_id` calls `source()`; unknown source invalidates the record and breaks subsequent chain checking; ambiguous source is diagnosed but record remains structurally valid and chain checks can proceed with explicit “input-structural finding, not sourced-canon” labels;
- every timeline `source_id` calls `source()`;
- alliance reciprocal qualification is the exceptional non-diagnostic query: reverse relation qualifies only if its source status is unique. The outer relation still gets its normal source diagnostic.

`source_status` handles identity qualification consistently at these sites; there is no last-wins source-row selection feeding the checks. Caveat: source rows that fail required-field validation are excluded from `data['sources']`, so the count is among valid source rows only.

## Additional adversarial probes (temporary copies)

1. **Unique alternative reverse witness.** Cloned raw `r7-ally-reverse-ambiguous`, appended reverse relation `bell-wardens -> quay-guild` with `source_id: separate-compact`, and ran the checker on that temp directory. Exit 1, exactly two findings: duplicate `harbor-compact` ID and ambiguous source on the original reverse relation. The original forward relation no longer gets a missing-reciprocal cascade. This confirms a unique alternative witness qualifies.
2. **Unrelated duplicate source.** Cloned `consistent`, appended two rows with a new duplicated ID `unused-dup` that no reference uses, then ran checker. Exit 1 with only the duplicate-ID finding; no cascade. (A separate duplicate of cited `archive-ledger` gives duplicate-ID plus four ambiguous reference findings, as expected; it does not affect `courier-log` citations, relation, or timeline.)
3. **Duplicate source used by broken chain.** Cloned `item-chain-broken`, appended duplicate `archive-ledger` row, then ran checker. Exit 1, eight total: duplicate, six local ambiguous source references (two ordinary entity refs and two each provenance refs), plus the existing chain break with explicit `input-structural finding, not sourced-canon` qualification. The source ambiguity does not suppress or recast explicit holder/tick mismatch.
4. **Contradiction-ledger ambiguity probe.** Cloned `consistent`; duplicated `archive-ledger`, made `departure` cite it, and added a ledger entry with claim sides `departure.place_id` and `arrival.place_id`. Exit 1, seven total: duplicate, the local `contradictions[0].claim_a.source_id` ambiguity, two entity first-appearance ambiguities, two entity claim ambiguities, and timeline[0] ambiguity. There is no additional generic “no resolvable source” finding for that side.

## Cascade assessment

The substantive potential false cascade is alliance: an ambiguous reverse edge cannot witness reciprocity, so the forward edge receives “lacks a sourced reciprocal.” This is policy-consistent for the raw r7 fixture (only ambiguous reverse exists) and appropriately disappears with the distinct unique reverse probe. Do not interpret it as proof that the alliance is false; it is a qualification failure, not canon resolution.

The duplicate in the item fixture causes seven reference-local findings, which is intentionally the stated round-7 policy, though multiple findings for the same duplicated ID are noisy by design. The broken-chain finding is not a false source-truth cascade: it checks the explicitly listed holder values and labels itself independent of sourced canon. In the contradiction ledger, an ambiguous event source yields a single local side-source diagnostic, not extra absence/unknown diagnostics. No false cascade observed beyond the expected alliance qualification diagnostic when no unique alternative witness is supplied.

Limit: probes test checker behavior and reference identity counts, not whether any source text supports its cited claims or whether lore claims are true.
