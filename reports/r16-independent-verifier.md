# Round 16 independent verifier

Role: non-author replay and integrity check. Scope was read-only against the checker and fixtures; I wrote only this report. Baseline is commit `3995486def3c9fceb95449362f6e8dab8cc130f7`.

## Integrity and baseline

- Hashed `corpus/fixtures/check_bible.py` and every `corpus/fixtures/**/*.json` immediately before and after replay: **165 files** (checker + 164 JSON files), SHA-256 maps identical. Checker SHA-256 both times: `bf2061b5c6f4e5f67f6c6f8dfbe31b0141c9541e259fe4ddf333aebef92b19b6`.
- Compared all **144 JSON paths** in the baseline commit’s fixture tree with current bytes; all hashes match. Four new r16 fixture directories contribute 20 JSON files; none are baseline paths.
- Extracted baseline checker with `git show 3995486def3c9fceb95449362f6e8dab8cc130f7:.shokunin/lore/corpus/fixtures/check_bible.py` and replayed both checker versions against all **33** current fixture directories, capturing stdout, stderr, and exit code separately as bytes.
- All **29** earlier fixtures exactly match between baseline and current checker: stdout bytes, stderr bytes, and exit status all equal. They also exactly match saved earlier CLI transcripts under `corpus/live/runs/20261012T181828Z/` (including the parsed exit code and stdout; prior transcripts show no stderr). No differences.

## Four new fixture outcomes

All commands were run as `python3 <checker> .shokunin/lore/corpus/fixtures/<fixture>`; the following are exact current-checker stdout, with stderr empty and exit status **1** in each case.

- `r16-missing-first`: `VIOLATION: timeline[0].place_id: dangling entity 'unlisted'
1 violation(s); no canon changed
` — no definite double-booked finding.
- `r16-missing-place`: `VIOLATION: timeline[1].place_id: dangling entity 'unlisted'
1 violation(s); no canon changed
` — no definite double-booked finding.
- `r16-mixed-three`: `VIOLATION: timeline[1].place_id: dangling entity 'unlisted'
VIOLATION: timeline[2]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
2 violation(s); no canon changed
` — the missing-place middle event does not mask the known harbor/tower pair.
- `r16-valid-places`: `VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
` — known-place control still reports double-booking.

Baseline/current differences occur only in the intended assertions for the missing-place cases: baseline additionally reports a double-booked finding against raw key `unlisted` in `r16-missing-first`, `r16-missing-place`, and `r16-mixed-three`. The valid-place control is byte-identical between versions.

## Limits

This verifies checker CLI behavior and fixture integrity, not narrative truth or source claims. It establishes only the declared count-zero-place behavior. Duplicate/ambiguous IDs and uniquely resolved non-place IDs were not changed or adjudicated here.
