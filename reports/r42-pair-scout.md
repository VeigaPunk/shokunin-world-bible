# Round 42 pair scout — description selector negative

## Candidate and novelty

Recommendation: **no-go as a calibration candidate**. The clean/negative pair can be made minimally and falsifiably, but the proposed semantic lesson is already substantially covered: r3 reviewer reports a temporary unsupported-ledger-field probe and says endpoints are restricted to allowed event fields (`.shokunin/lore/reports/r3-reviewer.md:15,19`); the checker explicitly allows only `place_id`, `tick`, `depends_on` (`.shokunin/lore/corpus/fixtures/check_bible.py:76-90`); README says the ledger points to event fields and does not copy source text or paraphrase (`.shokunin/lore/corpus/fixtures/README.md:48-54`). R35 further describes these as structured event-field references, not free-form prose (`.shokunin/lore/reports/r35-ledger-scout.md:5-8`).

## Minimal pair design (if retained as a diagnostic only)

Use the exact r35 clean fixture as control. In a copied negative, change only `claim_a.field` in `contradictions.json` from `place_id` to `description`; keep `claim_b`, all event/source rows, `why`, and prose identical. This is a one-field mutation: `description` is a timeline event field in the schema, but not a permitted contradiction-ledger selector (checker gate at `check_bible.py:76-90`; timeline field schema at `check_bible.py:14-21`). Expected negative: exit 1 with `contradictions[0].claim_a.field: expected one of ['depends_on', 'place_id', 'tick']`; clean control remains exit 0. It should reject before dereferencing the selected field, not assert anything about descriptive text.

## Calibration limit and risks

The only potentially sharpened explanation is that an event's human-readable description is not itself a supported machine selector. But this is a narrower restatement of the already-tested unsupported-field gate, not new coverage or demonstrated novel semantic calibration. The checker does not determine whether prose is true, whether two descriptions conflict, or whether `why` is adequate; README expressly limits it to pointers/required text (`fixtures/README.md:51-54`). Avoid claims that event descriptions are forbidden, never useful to an editor, false, or canonically authoritative. A valid source pointer is not proof of attribution/truth (`r35-ledger-scout.md:8,12-14`); preserve both fictional reports without choosing a winner or inferring Bell-7 facts.

## Falsifiable check

Against untouched control and the proposed single-field negative, verify all bytes other than that one JSON scalar are identical; run checker on both. Candidate passes the mechanical prediction only if control is clean and the negative emits the exact field allowlist diagnostic and exits nonzero. Candidate fails if any other file/field changes or that diagnostic differs. Even a mechanical pass does **not** establish incremental calibration: given r3's recorded unsupported-field test and README's explicit field contract, recommend archive/no-go unless an independent reviewer identifies a specific previously unarticulated distinction rather than repeating the gate.
