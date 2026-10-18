# Round 5 fixture scout — isolated malformed-input probes

## Observed evidence

- The standing round-5 claim in `.shokunin/lore/LOG.md` calls for one untouched clean baseline and one minimally changed copy per error class: missing file, invalid JSON, wrong top-level type, row shape, and invalid citation. The active checker is `.shokunin/lore/corpus/fixtures/check_bible.py`; it loops over five required tables in `FIELDS`: `sources.json`, `entities.json`, `relations.json`, `timeline.json`, and `contradictions.json`.
- The fixture root is `.shokunin/lore/corpus/fixtures/`. The baseline `consistent/` has all five files. In particular, `contradictions.json` is `[]`, `relations.json` has one well-formed `mira -> seal` row citing `courier-log`, and `sources.json` defines that source.
- I ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent` from the repository root; observed exit 0 and `CLEAN: schema, citations, relations, timeline; 0 violations`.
- The checker reports load failures as `<file>: cannot load JSON: ...`; a parsed non-array as `<file>: expected array`; non-object array members as `<section>[<index>]: expected object`; unresolved citation references as `unknown in-world source ...`. The checker continues after these errors, so a mutation to a heavily referenced table can create secondary diagnostics. A low-cascade target is preferable for loader/schema probes.

## Recommendation: five isolated raw fixture copies

Create six directories under `.shokunin/lore/corpus/fixtures/`: keep `consistent/` as the baseline and add `r5-missing-file/`, `r5-invalid-json/`, `r5-wrong-top-level/`, `r5-row-shape/`, and `r5-invalid-citation/`. For each new directory, begin with byte-for-byte copies of all five files in `consistent/`; make only the stated mutation below. Record hashes or run `diff -ru` against `consistent/` so the changed path(s) are explicit. Each CLI invocation uses the same command shape from the repository root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-missing-file
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-invalid-json
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-wrong-top-level
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-row-shape
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-invalid-citation
```

| Probe | Exact affected path relative to repo root | One-aspect mutation | Expected diagnostic class (prediction from code; must be measured before publishing a decision table) |
|---|---|---|---|
| Baseline | none; `.shokunin/lore/corpus/fixtures/consistent/` | untouched | exit 0, `CLEAN` |
| Missing file | `.shokunin/lore/corpus/fixtures/r5-missing-file/contradictions.json` | Remove this file only; the other four tables remain verbatim copies. | exit 1, `contradictions.json: cannot load JSON` (file-not-found); likely final `1 violation(s)` |
| Invalid JSON | `.shokunin/lore/corpus/fixtures/r5-invalid-json/contradictions.json` | Replace the contents only with invalid JSON, e.g. `{`. | exit 1, `contradictions.json: cannot load JSON` (JSON decode); likely final `1 violation(s)` |
| Wrong top-level type | `.shokunin/lore/corpus/fixtures/r5-wrong-top-level/contradictions.json` | Replace valid `[]` with `{}`. | exit 1, `contradictions.json: expected array`; likely final `1 violation(s)` |
| Row shape | `.shokunin/lore/corpus/fixtures/r5-row-shape/contradictions.json` | Replace valid `[]` with `[7]` (valid JSON array containing a non-object row). | exit 1, `contradictions[0]: expected object`; likely final `1 violation(s)` |
| Invalid citation | `.shokunin/lore/corpus/fixtures/r5-invalid-citation/relations.json` | In the existing single relation only, change `source_id` from `courier-log` to an absent ID such as `absent-source`; leave all other fields and files unchanged. | exit 1, `relations[0].source_id: unknown in-world source 'absent-source'`; likely final `1 violation(s)` |

Using `contradictions.json` for the four loader/shape cases avoids cascaded unknown-source, dangling-reference, or timeline errors. These are independent sibling copies from the clean baseline, not a chain in which each mutation inherits the previous defect. The malformed cases should have nonzero exits; do not describe exact full output or error counts as observed until the CLI results are recorded verbatim.

## Validation / boundaries

For each sibling, verify only the listed path differs from `consistent/` (with `contradictions.json` absent in the missing-file case), and preserve the baseline directory unchanged. Replay each exact command, recording exit status and relevant diagnostic; distinguish the missing-file and parse-error subtypes even though both use the `cannot load JSON` prefix. Also replay existing regression commands in `.shokunin/lore/corpus/fixtures/README.md` before claiming preserved outcomes. These five probes sample these error patterns; they are not exhaustive malformed-input coverage, and they do not establish anything about canon.

Recommendations only: I did not create or change fixture copies, checker code, decision table, or shared docs. This report is the only file written.
