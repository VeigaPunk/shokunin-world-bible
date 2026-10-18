# R54 replay clarifier: archived baseline versus live corpus

## Scope and method

This is an independent baseline-corpus replay only. I used `git archive 585a00f1b5c22001bb590a55276f0c22193ca305 .shokunin/lore/corpus` to extract the pinned corpus into a separate temporary root, then compared it with the live `.shokunin/lore/corpus`. The two repositories were used as distinct working directories; no candidate was built or run. This does not make a canon claim.

## Corpus comparison

- Relative corpus files: **1,149 archived and 1,149 live**; all relative paths and bytes match (0 missing, extra, or differing files).
- Fixture directories: **95** in each corpus.
- Fixture JSON files: **474**; archived and live contents total **230,650 bytes** and match byte-for-byte.
- `fixtures/check_bible.py`: **14,845 bytes** in each root, byte-identical.

## Replay

For every one of the 95 fixture directories, I ran this same argv separately with each root as cwd:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<name>
```

Compared the raw `(stdout bytes, stderr bytes, exit code)` tuples case-by-case. There were **190 executions total** (95 per root), with **0 / 95 tuple mismatches**. Both roots produced exit code 0 for 24 cases and exit code 1 for 71 cases; corresponding raw output bytes were identical in every case. Exit code 1 cases are preserved as observed, not interpreted as a replay discrepancy.

## Conclusion

The pinned archive and live corpus are byte-identical for the compared corpus tree, and their checker replays match exactly across all fixture directories. This replay is limited to baseline corpus equivalence and does not validate or evaluate a candidate.
