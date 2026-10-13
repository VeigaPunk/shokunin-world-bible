# Round 49 independent verifier report

## Scope and method

Baseline: `d3eac97c3c8ff8c58f6900bf119cfa30c7c7935d` (also the current `HEAD`). I extracted that commit with `git archive` into a separate root (`/tmp/r49base`), rather than relying on the working tree. The current tree had unrelated uncommitted report/log changes; I did not modify or use them as baseline.

I enumerated fixture directories under `.shokunin/lore/corpus/fixtures` in each root. Both contain exactly 95 directories, with no path additions or omissions. The fixture tree contains 474 JSON paths on each side; all paths match and every corresponding JSON file is byte-identical. The checker file `check_bible.py` is byte-identical.

For every one of the 95 fixture directories, I ran the same argv from each root, with that root as cwd:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<directory>
```

I compared raw stdout bytes, raw stderr bytes, and exit status. Result: **0 mismatches out of 95**.

## Round-49 admission check

Neither baseline nor current fixture enumeration contains an r49 fixture directory. I found no r49 candidate among the fixture directories. The parent task's other r49 scout reports are outside this fixture tree and were not treated as corpus inputs.

## Boundary / provenance note

The active fixtures document round 6 as the existing explicit item-provenance chain (`item-chain-valid` / `item-chain-broken`). The separate carbon-followup fixture is round 15; its README describes it as an authored fictional note and explicitly says it does not identify the mark as Mira's Blue Seal. I found no basis here to treat a new “carbon proposal” as built or admitted coverage. This report claims only artifact equality and deterministic replay at the stated baseline; it does not claim source truth, canon, or checker completeness.
