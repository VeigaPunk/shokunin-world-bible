# Round 51 independent verifier: fixture replay

## Scope and pin

This is an independent, non-author verification of the pre-round baseline, not a proposal or canon judgment. Baseline commit: `3ea7d7667b10d43c154f47a2b59c584df11d6d9a`. I extracted that commit with `git archive` into the separate root `/tmp/lore-r51-baseline`; the live comparison root is `/home/vgpnk/Projects/prymeagnt/lore` (HEAD was the pinned commit during inspection). No candidate-map correction was applied or executed here. No statement below establishes bell truth or canon.

## Inventory and bytes

Both roots contain the same 95 immediate fixture directories and the same 474 `*.json` paths, compared as complete sorted relative-path inventories. Every corresponding JSON file is byte-identical (0 differences). The checker `check_bible.py` is byte-identical in both roots; SHA-256: `5a389f1f5c0ccf104d9109f7a4740f398a73d6b372ad82c4e9abb3d4a4052d27` (14,845 bytes).

## Replay

For every one of the 95 fixture directories, I ran the exact same argv, with each root as cwd:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

Captured and compared the raw stdout bytes, raw stderr bytes, and exit status. All 95 pairs matched exactly (0 mismatches). This verifies repeatability of these inputs under the unchanged checker and Python CLI invocation; it is not evidence that any fixture report is true or that the checker decides canon.

## Candidate scope check

The tracked fixture tree has no diff from the baseline and no fixture JSON or checker change; its working-tree status is clean. In particular, this verifier did not find or run any r51 candidate map edit. Thus there is no claim that a suggested correction has been executed or validated here.
