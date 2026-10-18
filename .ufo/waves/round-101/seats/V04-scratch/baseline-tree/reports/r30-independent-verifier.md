# Round 30 independent verifier

## Reproduction

From the repository root, extract the baseline checker and run the verification script below. The baseline commit is `533e36712a3acefe7aa2ccb7e03f44aeb20efdbd`.

```sh
git show 533e36712a3acefe7aa2ccb7e03f44aeb20efdbd:.shokunin/lore/corpus/fixtures/check_bible.py > /tmp/check-bible-r30-baseline.py
python3 /tmp/r30check.py
```

`/tmp/r30check.py` enumerates fixture directories from `git ls-tree -r --name-only <baseline> -- .shokunin/lore/corpus/fixtures`, runs both the extracted checker and current checker on each directory, and compares the `(stdout, stderr, returncode)` tuples exactly. It then compares every baseline JSON path's working-tree bytes against `git show <baseline>:<path>`, compares the five JSON files in r28/r29/r30, and runs current checker on each new textual fixture.

## Results

- All **80** baseline fixture directories produced exact stdout, stderr, and exit-code matches between extracted baseline checker and current checker.
- All **399** baseline fixture JSON paths are byte-identical to baseline.
- The five JSON tables (`entities.json`, `relations.json`, `sources.json`, `timeline.json`, `contradictions.json`) in r28, r29, and r30 are byte-identical across all three fixtures.
- Current checker on `r28-courier-excerpt`, `r29-near-miss`, and `r30-explicit-negation` exited **0** each, printed exactly `CLEAN: schema, citations, relations, timeline; 0 violations
`, and emitted empty stderr.

## Scope and limits

This verifies structural checker behavior, byte preservation, and the stated fixture comparisons; it does not validate Markdown prose or the manual clause-to-relation interpretation. In particular, the contrast among r28 positive wording, r29 unsupported proximity, and r30 explicit negation is not checker output. The textual-conflict interpretation is conditional on editorial ID and same-proposition/occasion alignment; it does not establish canon truth, resolve the relation, or make claims beyond the excerpt's scope. This verification does not establish correctness for untested fixtures, platforms, or semantic readings.
