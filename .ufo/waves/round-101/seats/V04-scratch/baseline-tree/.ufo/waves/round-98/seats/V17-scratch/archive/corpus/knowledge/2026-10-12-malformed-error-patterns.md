# Round 5 — observed malformed-bible error patterns

Run every row from the repository root with:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>
```

Each `r5-*` directory is a fresh copy of `consistent/` with exactly the single changed or missing path named below. These are fictional records. The checker is unchanged from baseline report commit `b6ca1e902f2bf08b8acddaef665d9764f8636981`; compare `git diff b6ca1e9 -- .shokunin/lore/corpus/fixtures/check_bible.py`. The raw repo-root CLI outputs and exit statuses were captured in `corpus/live/runs/20261012T164316Z/`.

| Case `<case>` | Only mutation vs `consistent/` | Observed exit | Stable primary diagnostic | Other diagnostics observed |
|---|---|---:|---|---|
| `consistent` | None | 0 | `CLEAN`, zero violations | None |
| `r5-missing-file` | `contradictions.json` omitted | 1 | `contradictions.json: cannot load JSON` (file absent) | None in this low-cascade example |
| `r5-invalid-json` | `contradictions.json` replaced with `{` | 1 | `contradictions.json: cannot load JSON` (parse error) | None in this example |
| `r5-wrong-top-level` | `contradictions.json` replaced with `{}` | 1 | `contradictions.json: expected array` | None in this example |
| `r5-row-shape` | `contradictions.json` replaced with `[7]` | 1 | `contradictions[0]: expected object` | None in this example |
| `r5-invalid-citation` | `relations[0].source_id` set to `absent-source` | 1 | `relations[0].source_id: unknown in-world source 'absent-source'` | None in this example |

These are observations for these exact committed inputs, not a complete classification of malformed bibles. In particular, removing a heavily referenced table such as `entities.json` also triggers downstream dangling-reference diagnostics; one mutated file does not always mean one error. `cannot load JSON` groups file-read and JSON-parse failures, so the two rows share a prefix but are distinct causes. OS path text and JSON parser wording/offsets are not portable assertions. `[7]` tests a non-object row, not every field-shape error. The citation case checks source-ID membership, not whether the source supports a relation or whether it is true. Exit 1 reports an input violation; no canon is repaired or rewritten.

Regression replay on the same checker preserved `contradictions` exit 1/three seeded findings, `ally-reciprocal` exit 0, `ally-one-way` exit 1/missing reciprocal, and `contradictions-ledger-malformed` exit 1/ledger pointer plus three original findings. Outputs are alongside the six rows in the same run directory. This table's calibration claim still requires a named non-author verifier to replay raw fixtures; it does not self-verify.
