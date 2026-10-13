# Round 26 reviewer report

## Independent fixture comparison

Compared the JSON files in `r25-to-ambiguous/` and `r26-to-malformed/` directly. `contradictions.json`, `relations.json`, `sources.json`, and `timeline.json` are byte-identical. `entities.json` differs only in the second `seal` row (`entities[4]`): its `name` changes from `Seal in courier ledger` to the empty string. The raw row remains in the JSON array with its `id`, `kind`, `first_appearance`, and `claims` unchanged. The relation remains the same cited `mira -> seal` row.

## Checker replay and admission

Replayed `python3 .shokunin/lore/corpus/fixtures/check_bible.py` on all three cases. `r26-to-malformed` exits 1, stderr is empty, and stdout is exactly:

```text
VIOLATION: entities[4].name: required nonempty str
1 violation(s); no canon changed
```

`r25-to-ambiguous` exits 1 with empty stderr and exactly the separate duplicate-ID and `relations[0].to: ambiguous entity 'seal'` findings (2 violations). `r25-to-unique` exits 0 with empty stderr and `CLEAN: schema, citations, relations, timeline; 0 violations`.

This matches the checker flow: required fields/nonempty strings are validated at `check_bible.py:32-43`; only valid rows are appended to `data[section]`. Entity ID counts at `:118-121` are computed from those admitted rows, and relation endpoint ambiguity at `:123-129` is reported when that count exceeds one. Thus the malformed second row remains in the raw input and receives its row-local schema violation, but is excluded from admitted entity rows and the duplicate count. The existing admitted-duplicate case still demonstrates the ambiguity diagnostic; the unique case is a clean control.

## Scope and caveat

The observed result supports only this checker's structural admission/counting behavior for this input. Absence of the ambiguity diagnostic is not evidence that the malformed row is false, that its source evidence is absent, or that the seal is unique or canonical. The checker explicitly reports “no canon changed”; no truth or canon inference is warranted.
