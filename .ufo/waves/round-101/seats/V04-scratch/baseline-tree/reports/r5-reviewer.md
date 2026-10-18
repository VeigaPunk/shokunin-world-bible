# Round 5 independent reviewer replay

## Scope and method

I independently inspected the committed raw fixture directories and ran the exact checker command from the repository root for all six new rows and all four requested prior regression fixtures. I did not use the author table as the source of measured outputs. Per the task's write restriction, this report is my only created artifact; I did not modify fixtures, checker, or run artifacts.

The clean control contains `entities.json`, `relations.json`, `timeline.json`, `sources.json`, and `contradictions.json`. For each `r5-*` directory, comparing names and bytes against `consistent/` found exactly the declared difference: missing `contradictions.json`; changed `contradictions.json` in the invalid-JSON, wrong-top-level, and row-shape cases; changed `relations.json` in invalid-citation. All other present files matched byte-for-byte. The literal malformed values/field are consistent with the table: `{`, `{}`, `[7]`, and `relations[0].source_id = absent-source` respectively. No unexpected file was present.

`git diff --exit-code b6ca1e902f2bf08b8acddaef665d9764f8636981 -- .shokunin/lore/corpus/fixtures/check_bible.py` returned 0. Checker SHA-256 before/after replay was `0008496a65e6e0696b638a081c78c44cf4e323d7f56441a6105631ecc689769d`.

## Measured CLI outcomes

Command for each case: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>`.

| Case | Exit | Observed output class / count | Match |
|---|---:|---|---|
| `consistent` | 0 | `CLEAN`; 0 violations | Yes |
| `r5-missing-file` | 1 | `contradictions.json: cannot load JSON`; 1 violation | Yes |
| `r5-invalid-json` | 1 | `contradictions.json: cannot load JSON`; 1 violation | Yes |
| `r5-wrong-top-level` | 1 | `contradictions.json: expected array`; 1 violation | Yes |
| `r5-row-shape` | 1 | `contradictions[0]: expected object`; 1 violation | Yes |
| `r5-invalid-citation` | 1 | `relations[0].source_id: unknown in-world source 'absent-source'`; 1 violation | Yes |

All printed the ordinary final summary (`CLEAN` or `N violation(s); no canon changed`); no stderr or traceback was observed. The table's bounded classes and counts are accurate for these exact fixtures. Missing-file and parser-specific text remain environment-dependent as documented.

## Prior fixture replay

| Case | Exit | Measured stable findings | Match to declared outcomes |
|---|---:|---|---|
| `contradictions` | 1 | 3: dangling `missing-map`; timeline inversion (`later` tick 3 not before `arrival` tick 2); double-booked `mira` at tick 2 | Yes |
| `ally-reciprocal` | 0 | Clean, 0 violations | Yes |
| `ally-one-way` | 1 | 1: `allied_with` faction relation lacks sourced reciprocal relation | Yes |
| `contradictions-ledger-malformed` | 1 | 4: ledger `absent-event` pointer plus the same three findings as `contradictions` | Yes |

## Reviewer judgment and limits

The decision table is accurate against raw fixtures and the checker; the five malformed cases are isolated as claimed, and prior outcomes replayed as declared. I found no cascade in these deliberately low-cascade malformed cases. The table itself correctly warns that this does not generalize: the one-file mutation premise does not imply one diagnostic for a referenced table (as the prior scout's missing-entities experiment showed). `[7]` establishes only a non-object row case, and the citation row establishes source-ID membership only.

No overclaim appears in the current measured table or its explicit limitations. It would be an overclaim to call the table exhaustive, claim all malformed inputs avoid cascades/crashes, or say citations are supported/true. Independent replay supports the narrow reproducibility and prior-outcome claims. This assessment is limited to CLI output observed in this environment; host-specific parser wording and absolute paths are not portable contracts.
