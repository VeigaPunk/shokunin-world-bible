# Round 28 independent verifier

Independent replay performed against baseline checker extracted from `aaa8d724f5820b07a5cb2d498777306763001441`. No checker or fixture files were changed.

## Reproducible checks

```sh
git show aaa8d724f5820b07a5cb2d498777306763001441:.shokunin/lore/corpus/fixtures/check_bible.py > /tmp/r28-baseline-check.py
for d in .shokunin/lore/corpus/fixtures/*/; do
  [ "${d%/}" = .shokunin/lore/corpus/fixtures/r28-courier-excerpt ] && continue
  python3 /tmp/r28-baseline-check.py "$d" > /tmp/base.out 2>/tmp/base.err; brc=$?
  python3 .shokunin/lore/corpus/fixtures/check_bible.py "$d" > /tmp/current.out 2>/tmp/current.err; crc=$?
  diff -u /tmp/base.out /tmp/current.out; diff -u /tmp/base.err /tmp/current.err; test "$brc" = "$crc"
done
```

The exclusion above uses the corrected path (the verifier draft misspelled `.shokunin` as `.shokhin`); the actual replay enumerated all 78 baseline directories and compared stdout, stderr, and exit status exactly: **78/78 matched; 0 mismatches**.

Baseline JSON inventory and byte checks:

```sh
git ls-tree -r --name-only aaa8d724f5820b07a5cb2d498777306763001441 -- .shokunin/lore/corpus/fixtures | grep '\.json$'
# For each listed path: git show aaa8d724f5820b07a5cb2d498777306763001441:<path>
# compare byte-for-byte with the working-tree file.
```

Result: **389/389** pre-existing JSON paths byte-identical; no missing or differing paths. In `r28-courier-excerpt/`, each of `sources.json`, `entities.json`, `relations.json`, `timeline.json`, and `contradictions.json` is byte-identical to `consistent/`.

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r28-courier-excerpt
```

Observed exit **0**, stdout exactly `CLEAN: schema, citations, relations, timeline; 0 violations
`, stderr empty. `courier-log-excerpt.md` and `relation-clause-map.md` exist. The checker accepts a fixture directory and loads the JSON tables; it does not consume either Markdown file, so this replay verifies neither prose nor clause entailment. Those require human review. The source identifier/reference establishes fixture linkage only; it does not prove source authenticity, a real-world source, or canon/relationship truth.
