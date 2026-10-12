# Round 11 test scout — baseline replay and place-reference probes

## Method and baseline replay

I replayed the 20 fixture directories listed below using the round declaration's baseline checker from `git show 4337c6385ed3f00f45d03eb263028ae313507006:.shokunin/lore/corpus/fixtures/check_bible.py` (saved in `/tmp/r11-test-scout/check_bible.py`). For each, the CLI was `python3 /tmp/r11-test-scout/check_bible.py <fixture-copy>`; fixture inputs were copied from `.shokunin/lore/corpus/fixtures/<name>/` to `/tmp/r11-test-scout/<name>/`. All 20 exit codes matched the existing raw run at `.shokunin/lore/corpus/live/runs/20261012T173416Z/<name>.txt`; printed messages matched except expected absolute-vs-relative temp path in `r5-missing-file`'s OS error. The existing raw files retain the repo-root CLI and original observed output.

Cases and exits: `consistent` 0, `contradictions` 1, `ally-reciprocal` 0, `ally-one-way` 1, `contradictions-ledger-malformed` 1, `r5-missing-file` 1, `r5-invalid-json` 1, `r5-wrong-top-level` 1, `r5-row-shape` 1, `r5-invalid-citation` 1, `item-chain-valid` 0, `item-chain-broken` 1, `r7-ally-reverse-ambiguous` 1, `r7-item-ambiguous` 1, `r8-deps-distinct` 0, `r8-deps-anomalous` 1, `r9-dup-low-high` 1, `r9-dup-high-low` 1, `r9-unique-control` 0, `r10-registry-witness` 0. Raw examples: `.shokunin/lore/corpus/live/runs/20261012T173416Z/consistent.txt` says `CLEAN ... 0 violations`; `r9-dup-low-high.txt` and `r9-dup-high-low.txt` each say duplicate timeline `same` and ambiguous dependency `same` (2 violations); `r9-unique-control.txt` says `CLEAN`.

## Direct row-order/control probes

The baseline checker is read-only, so I made probe-only copies of `consistent/` under `/tmp/r11-test-scout/`; no repo fixture or checker was edited. Each probe changed only timeline row 0's `place_id`, and pair cases inserted a second otherwise schema-valid entity row with the same `harbor` ID, source `archive-ledger`, and a character claim. Probe CLI: `python3 /tmp/r11-test-scout/check_bible.py /tmp/r11-test-scout/<probe>`.

- `/tmp/r11-test-scout/pair-place-character`: harbor rows ordered place, then character. Exit 1: `entities[2].id: duplicate entities id 'harbor'` and `timeline[0].place_id: not a place 'harbor'`.
- `/tmp/r11-test-scout/pair-character-place`: same two rows reversed. Exit 1: only `entities[2].id: duplicate entities id 'harbor'`; **the same timeline reference now passes silently**.
- `/tmp/r11-test-scout/unique-place`: existing unique `harbor` place reference, exit 0 / `CLEAN`.
- `/tmp/r11-test-scout/unique-character`: unique `mira` character used as place, exit 1 / `timeline[0].place_id: not a place 'mira'`.
- `/tmp/r11-test-scout/dangling-place`: absent `unlisted` ID as place, exit 1 / `timeline[0].place_id: dangling entity 'unlisted'`.

These reproduce the order-dependent behavior in the declared baseline: `index('entities')` retains the last duplicate row for kind lookup, while duplicate-ID detection separately reports the collision. The existing round-9 pair is not an entity-duplicate pair: both `r9-dup-*` cases duplicate the **timeline event** ID `same`, and so do not exercise this premise.

## Recommendation (not a code change)

Premise confirmed. Keep the proposed scope local to timeline `place_id`: count matching entity rows; when more than one schema-valid row matches, report an ambiguous place reference and do not classify by last-row kind. Preserve the ordinary duplicate-entity-ID finding and both source rows. Pair results should agree independent of row order; retain the unique place / unique non-place / dangling distinctions shown above. Do not extend this finding to other entity-ID consumers based only on these probes. No checker/fixture/shared-doc changes made.
