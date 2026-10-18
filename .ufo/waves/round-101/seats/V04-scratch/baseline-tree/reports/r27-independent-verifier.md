# Round 27 independent verifier

Baseline: `bb4c6c971faeaed48c7dbdf57ceb90fcfc873a21`. I ran the baseline checker saved from that commit and the current checker against every baseline fixture directory, comparing stdout bytes, stderr bytes, and exit status:

```text
baseline fixture directories: 76
exact stdout/stderr/exit matches: 76
mismatches: 0
```

I compared each of the 379 baseline JSON paths byte-for-byte with the working tree: `379/379` identical, `0` changed.

Reproducer (from repository root):

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r27-target-only
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r27-both-ambiguous
```

Exact observed outputs (stderr empty):

```text
$ target-only
VIOLATION: entities[4].id: duplicate entities id 'seal'
VIOLATION: relations[0].to: ambiguous entity 'seal'
2 violation(s); no canon changed
exit: 1

$ both-ambiguous
VIOLATION: entities[4].id: duplicate entities id 'seal'
VIOLATION: entities[5].id: duplicate entities id 'mira'
VIOLATION: relations[0].from: ambiguous entity 'mira'
VIOLATION: relations[0].to: ambiguous entity 'seal'
VIOLATION: timeline[0].entity_id: ambiguous actor entity 'mira'
VIOLATION: timeline[1].entity_id: ambiguous actor entity 'mira'
6 violation(s); no canon changed
exit: 1
```

The pair comparison found only `entities.json` differs; the other four JSON files are byte-identical. The both-case adds the admitted `mira` entity row. The two timeline actor ambiguities are collateral findings against pre-existing timeline rows that reference `mira`, and are included in the exact six-finding count. These fixture outputs establish checker behavior only: no canon, identity resolution, entity uniqueness, or relation truth is inferred.
