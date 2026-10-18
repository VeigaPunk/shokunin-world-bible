# Round 24 executor report

Implemented a relation-local ambiguous entity endpoint diagnostic in `corpus/fixtures/check_bible.py`. The checker counts the same structurally admitted entity rows used by downstream rules. For each relation endpoint, zero indexed rows keeps the prior dangling diagnostic; one row passes unchanged; more than one emits `relations[i].from/to: ambiguous entity ID`. The existing duplicate-ID error, source validation, and all downstream last-row index behavior remain unchanged. No canon row is resolved.

## Commands and results

From repository root, ran:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r12-ambiguous-actor
```

Exit 1; emitted existing duplicate entity ID, the new `relations[0].from: ambiguous entity 'mira'`, and the two existing ambiguous actor findings (4 total). The unique `to: seal` endpoint gets no ambiguity finding.

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r12-unique-actor
```

Exit 1 with its pre-existing `double-booked` finding (1 total); no relation endpoint ambiguity. Note: this fixture is an occupancy case, not a clean whole-bible control; the declared unique relation endpoint remains unambiguous.

Regression command used for each of the 73 existing fixture directories:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>
```

Compared stdout, stderr, and exit code against the pre-edit `HEAD` checker extracted with `git show HEAD:.shokunin/lore/corpus/fixtures/check_bible.py` and run as `/tmp/check_bible_r24_baseline.py`. Exactly two fixture outputs changed, each by only the intended additional line and a +1 total: `r12-ambiguous-actor` (3→4) and `r21-ambiguous-actor` (4→5). All other 71 outputs were identical. No fixture JSON was modified or added.

No canon resolution, source-text claim, or game-mechanics inference is made.
