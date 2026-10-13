.shokunin/lore Round 24 independent verifier

Scope and method
----------------
Independent replay of all 73 existing fixture directories with the current checker and the baseline checker at `d0e1c73b28fdf971c41cb095d709bfcd9edeffbc`. No fixture/checker files were edited by this verifier. I extracted the baseline script to `/tmp/check_bible_r24_baseline.py`; reproducible commands from repository root:

```sh
git show d0e1c73b28fdf971c41cb095d709bfcd9edeffbc:.shokunin/lore/corpus/fixtures/check_bible.py > /tmp/check_bible_r24_baseline.py
for d in .shokunin/lore/corpus/fixtures/*/; do
  python3 /tmp/check_bible_r24_baseline.py "$d" > /tmp/r24-old.out 2> /tmp/r24-old.err; old=$?
  python3 .shokunin/lore/corpus/fixtures/check_bible.py "$d" > /tmp/r24-new.out 2> /tmp/r24-new.err; new=$?
  # Compare these three observations for each directory: stdout, stderr, and status.
  diff -u /tmp/r24-old.out /tmp/r24-new.out || true
  diff -u /tmp/r24-old.err /tmp/r24-new.err || true
  printf '%s old=%s new=%s\n' "$d" "$old" "$new"
done
```

Actual replay compared captured `(stdout, stderr, exit status)` tuples, not just the displayed shell summary. Result: 73/73 directories executed with each checker. Exactly two output tuples differ; both exit 1 under both checkers and stderr remains empty.

Changed outputs
---------------

- `r12-ambiguous-actor`: baseline has 3 violations; current has 4. Sole added line: `VIOLATION: relations[0].from: ambiguous entity 'mira'`. Existing duplicate-ID and two actor-ambiguity lines are unchanged; total is +1. `to: seal` is unique and gains no finding.
- `r21-ambiguous-actor`: baseline has 4 violations; current has 5. Sole added line: `VIOLATION: relations[0].from: ambiguous entity 'mira'`. Existing duplicate-ID, two actor-ambiguity findings, and malformed dependency finding are unchanged; total is +1.

The other 71/73 cases have byte-identical stdout, stderr, and exit status. This includes `r12-unique-actor`, whose relation endpoint remains unique and whose full baseline/current output is identical. That fixture is not a clean whole-bible case: both versions exit 1 for its pre-existing `double-booked 'mira' at tick 7` finding. The whole-bible clean control, `consistent/`, is unchanged and exits 0 with `CLEAN: schema, citations, relations, timeline; 0 violations`.

Fixture JSON identity
---------------------
At the baseline commit, `git ls-tree -r` enumerates 364 tracked fixture JSON paths. Comparing every path and byte content against the working tree found 364/364 present and byte-identical, zero changed, zero missing, and zero added JSON paths. The current directory inventory remains 73 fixture directories. Checker/README/log/report files are outside that JSON identity check.

Caveats
-------
This verifies checker behavior on the existing fixture corpus, not whether any relation is true in source text or canon. The new line reports endpoint ambiguity from duplicate entity rows; it does not resolve or select one row. `r12-unique-actor`'s pre-existing occupancy violation means “unique endpoint” is the supported assertion, not “clean fixture.” No production or fixture edits were made for this report.
