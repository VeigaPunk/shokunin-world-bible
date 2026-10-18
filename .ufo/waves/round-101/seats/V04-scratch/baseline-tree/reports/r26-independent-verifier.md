# Round 26 independent verifier report

## Result

Independent replay passed. The baseline checker and current checker produced byte-identical stdout and stderr and identical exit codes for all 75 pre-existing fixture directories. All 374 pre-existing JSON paths are byte-identical to baseline `f44e7281a5438dc86e4fd8a03b19476e4cce7371`. The sole new fixture directory, `r26-to-malformed/`, contains five JSON paths.

## Commands and observations

From the repository root, I extracted the baseline checker and replayed the exact fixture directories named by the baseline tree:

```sh
git show f44e7281a5438dc86e4fd8a03b19476e4cce7371:.shokunin/lore/corpus/fixtures/check_bible.py > /tmp/r26-baseline-check.py
# For each of the 75 pre-existing fixture directories:
python3 /tmp/r26-baseline-check.py .shokunin/lore/corpus/fixtures/<fixture>
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>
```

The comparison used `(stdout bytes, stderr bytes, return code)` tuples: **75 directories, 0 mismatches**. Directory names were enumerated with `git ls-tree -d --name-only f44e7281a5438dc86e4fd8a03b19476e4cce7371:.shokunin/lore/corpus/fixtures` and limited to existing directories in the working tree.

For each JSON path in the baseline fixture tree, comparison was `git show f44e7281a5438dc86e4fd8a03b19476e4cce7371:<path>` against the working-tree file bytes: **374 paths, 0 changed**. `r26-to-malformed/` adds five JSON files and none were baseline paths.

Target replay:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r26-to-malformed
stdout: VIOLATION: entities[4].name: required nonempty str
        1 violation(s); no canon changed
stderr: (empty)
exit: 1

python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r25-to-ambiguous
stdout: VIOLATION: entities[4].id: duplicate entities id 'seal'
        VIOLATION: relations[0].to: ambiguous entity 'seal'
        2 violation(s); no canon changed
stderr: (empty)
exit: 1

python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r25-to-unique
stdout: CLEAN: schema, citations, relations, timeline; 0 violations
stderr: (empty)
exit: 0
```

The five filenames in `r26-to-malformed/` are `sources.json`, `entities.json`, `relations.json`, `timeline.json`, and `contradictions.json`. Byte comparisons against `r25-to-ambiguous/` show the four non-entity files identical. Parsed entity rows differ only at index 4: its `name` changes from `Seal in courier ledger` to `""`; the raw duplicate row remains present with the same `id`, `kind`, `first_appearance`, and `claims`. The malformed run emits exactly the required-name diagnostic, with neither duplicate-ID nor `relations[0].to` ambiguity diagnostic. The r25 admitted duplicate still emits both duplicate-ID and target-ambiguity diagnostics; unique control remains clean.

## Scope and limits

This verifies checker behavior and fixture bytes, not lore truth, citation contents, canon, or whether the malformed raw row denotes a real entity. The lack of an ambiguity finding means only that this checker excludes the invalid row from its admitted-entity index; it does not establish a unique real-world target. Baseline replay covers the 75 directories present at the named baseline, not the newly added fixture. No checker or other production source was changed as part of this verification.
