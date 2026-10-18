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

## Correction addendum (2026-10-18, round 102, freshness seat U2)

The baseline-report commit pin in the paragraph above is **dangling on the delivered revision**: `b6ca1e902f2bf08b8acddaef665d9764f8636981` does not resolve in any accessible object store as of 2026-10-18 — `git cat-file -t b6ca1e902f2bf08b8acddaef665d9764f8636981` fails in this repository (`git log --all --format=%H | grep -c b6ca1e9` = 0) and in the parent project repo at `/home/vgpnk/Projects/shokunin` (`fatal: git cat-file: could not get object info`). The note predates this lane's own repository layout — it was committed here in r5 (`60f4956`, 2026-10-12) while still addressing repo-root paths `.shokunin/lore/…`, i.e. the pre-split layout — so the cited commit most likely lived in the parent project's history before the lane split and was not carried into this repository's object store. The historical comparison `git diff b6ca1e9 -- .shokunin/lore/corpus/fixtures/check_bible.py` is therefore no longer runnable as written; this supersedes only that comparison instruction and the "unchanged from" framing that depends on it. The note's factual content is unaffected and was re-verified fresh on the delivered revision (checker sha256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`): all six rows reproduce exactly —

```text
consistent            exit 0  CLEAN: schema, citations, relations, timeline; 0 violations
r5-missing-file       exit 1  VIOLATION: contradictions.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r5-missing-file/contradictions.json'
r5-invalid-json       exit 1  VIOLATION: contradictions.json: cannot load JSON: Expecting property name enclosed in double quotes: line 2 column 1 (char 2)
r5-wrong-top-level    exit 1  VIOLATION: contradictions.json: expected array
r5-row-shape          exit 1  VIOLATION: contradictions[0]: expected object
r5-invalid-citation   exit 1  VIOLATION: relations[0].source_id: unknown in-world source 'absent-source'
```

The preserved raw r5-era captures at `corpus/live/runs/20261012T164316Z/` still exist in-tree. History above remains unrewritten.

Regression replay on the same checker preserved `contradictions` exit 1/three seeded findings, `ally-reciprocal` exit 0, `ally-one-way` exit 1/missing reciprocal, and `contradictions-ledger-malformed` exit 1/ledger pointer plus three original findings. Outputs are alongside the six rows in the same run directory. This table's calibration claim still requires a named non-author verifier to replay raw fixtures; it does not self-verify.
