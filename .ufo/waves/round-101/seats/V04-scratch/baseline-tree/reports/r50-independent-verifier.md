# Round 50 independent verifier

## Baseline and method

Baseline is report commit `6f89824ef85812b3f366fd90b8a06458dd8af0c6` (HEAD at verification). I extracted its `git archive` into an independent temporary root (`/tmp/tmp.gFeQ47TV4n`); the working tree was used as the current root. For every fixture directory, I ran the identical argument vector from each root:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>
```

The checker path and fixture argument are root-relative; `cwd` was each respective root. Captured raw stdout, raw stderr, and exit code were compared byte-for-byte for every run.

## Replay result

- 95 fixture directories, containing 474 JSON paths, were replayed.
- All 95 comparisons were exact: no stdout, stderr, or exit-code differences.
- Both roots yielded 24 exit-0 and 71 exit-1 results.
- Checker bytes are identical (SHA-256 `5a389f1f5c0ccf104d9109f7a4740f398a73d6b372ad82c4e9abb3d4a4052d27`).

## Corpus inventory and byte audit

Recursive corpus inventory at baseline and current each contains 1,149 files. The path sets are identical: no additions or deletions. Of the 1,149 paths, exactly one file differs: `fixtures/README.md`. Its baseline SHA-256 is `c0252ed2308abb2f6f4865091d926c7d94cdadd5e564a7851df79c12d7ddc53c`; current SHA-256 is `9db3195ccebca979a75130581099c65f334e5502e53adca523c96e8c07c69ac4`.

The only diff revises the prose around the Jorin/Vela map history and interpretation (baseline lines 906–908; current lines 906–910). All remaining bytes match, including every JSON file, maps, excerpts, and strength maps. The Python checker validates fixture structure/consistency; it cannot validate README prose or establish whether its account is true. No prose correctness is claimed by this replay.
