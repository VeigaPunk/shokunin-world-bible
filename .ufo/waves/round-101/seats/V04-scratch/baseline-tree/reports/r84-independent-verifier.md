# Round 84 independent verifier

## Scope and pin

Independently verified the declared archive pin `596f70e417c794f6d09279ee26cf9a03dd17eea9` (`HEAD` matched), extracted its `.shokunin/lore/corpus` with `git archive`, and compared it with the worktree corpus. I also independently recreated the matched distinct/duplicate event-ID probe in temporary directories outside the repository. No repository input, checker, configuration, or other report was changed; this report is the only file written.

## Corpus preservation

- Pinned archive: **1,368** corpus files; worktree: **1,368**.
- Relative path sets: exact; raw-byte matches: **1,368/1,368**; missing, extra, or changed files: **0**.
- Pinned active checker SHA-256: `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`.

## Prior fixture replay

Enumerated all **133** fixture directories in the pinned corpus. From both the extracted archive root and repository root, ran each fixture with the root-relative command:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

Compared unnormalized `(exit status, stdout bytes, stderr bytes)` results: **133/133 exact matches**; **28** exited 0 and **105** exited 1. No mismatches. This is pinned-baseline replay, not an interpretation of the diagnostics.

## Independently recreated matched pair

Copied the `consistent` fixture's five JSON files to two temporary copies outside the repository and replaced only `timeline.json` with two schema-valid rows. Both rows had actor `mira`, tick `7`, places `harbor` and `tower`, and source IDs `courier-log` and `archive-ledger`. The sole controlled difference was second row ID: `pair-event-b` (distinct control) versus `pair-event-a` (duplicate case). Each command ran from the repository root with stdout/stderr captured separately:

Distinct IDs — exit **1**; stdout bytes decode to:

```text
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
```

stderr: **empty**.

Duplicate ID — exit **1**; stdout bytes decode to:

```text
VIOLATION: timeline[1].id: duplicate timeline id 'pair-event-a'
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
2 violation(s); no canon changed
```

stderr: **empty**.

Thus the duplicate adds its own ID diagnostic; the same booking diagnostic remains in both outputs. This confirms the pair scout's raw-channel results independently. In combination with the checker-scout's code-path inspection, the probe supports that occupancy compares admitted rows by actor/tick and place, independently of event-ID uniqueness. It does not prove which editorial policy is correct. The proposed suppression/qualification move has no demonstrated distinct safe repair in this pair; the critic and editor scout explain why suppressing the finding risks hiding an independently actionable input-field conflict. This evidence supports the provisional **NO-GO** for this calibration hypothesis, not a final axis adjudication.

## Limits

All fixture prose and test values are invented and unverified. Structural schema/citation pointers and checker diagnostics do not establish source support or truth, an in-world event or location, chronology, canon, rights, or mechanics. Local tick `7` is not a real date. No commit, push, merge, or candidate implementation was made.
