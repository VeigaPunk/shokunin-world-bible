# Round 33 independent verifier

Independent replay against baseline `56f924458673e86cd82588ceb7818c1cdaad44a8`.

## Reproduction

From repository root, extract the baseline checker and run it against all fixture directories present at the baseline:

```sh
git show 56f924458673e86cd82588ceb7818c1cdaad44a8:.shokunin/lore/corpus/fixtures/check_bible.py > /tmp/r33-baseline-checker.py
# For each of the 84 fixture directories enumerated from baseline JSON paths:
python /tmp/r33-baseline-checker.py .shokunin/lore/corpus/fixtures/<fixture>
python .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>
```

Captured each command's raw stdout, stderr, and exit status; all **84/84** triples match exactly. Compared every tracked baseline JSON path's current bytes with `git show <baseline>:<path>`: **419/419 unchanged**. This includes the baseline `consistent/` fixture.

For the new fixture:

```sh
python .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r33-tarin-envelope
```

Observed exit **0**, stdout exactly `CLEAN: schema, citations, relations, timeline; 0 violations
`, stderr empty. Parsed-array comparison with baseline `consistent/`: all old rows preserved in order; additions are exactly **1 source**, **2 entities**, **1 timeline event**. `relations.json` and `contradictions.json` are byte-identical to `consistent/` (both `cmp` succeeded).

## Scope / caveats

The checker establishes schema/reference consistency only, not that the excerpt is true or that its claims are canon. The new prose and clause map are present and internally align the excerpt phrases to the added Tarin/Sella/event rows; the event's tick 3 is identified as local metadata, not observed or absolute time. This mechanical verifier cannot independently establish prose entailment or fictional-world truth; that requires the separate manual reviewer. No inference about envelope contents, ownership, recipient, motive, Blue Seal/carbon/route-strip connection, real-world rights, or AI-training permission follows from this replay.
