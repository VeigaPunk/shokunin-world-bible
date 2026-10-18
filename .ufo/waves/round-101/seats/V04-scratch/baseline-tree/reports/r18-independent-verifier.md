# Round 18 independent verifier report

## Scope and method

Non-author verification only; no source or fixture edits. Baseline commit: `82701ce7680fb062a345e379057c8a097c1539e6` (HEAD at inspection). Extracted its checker to `/tmp/r18-baseline-checker.py`. Ran byte comparisons of each fixture JSON path tracked at that commit against the working tree; ran baseline and current checker on all non-r18 fixture directories; then replayed all saved run outputs against the current CLI. Examined all six r18 fixture directories and their CLI output. No claim is made from the absent test-scout report.

## Byte integrity and replay

- The baseline commit has **194 tracked fixture `.json` paths**. All 194 working-tree files are byte-identical to `82701ce`; **0 differences**.
- Baseline checker versus current checker: **39/39 non-r18 fixture directories** had identical exit code, stdout bytes, and stderr bytes.
- Saved `corpus/live/runs/20261012T185657Z/` contains **45** `.txt` transcripts. I parsed each transcript's recorded command and `exit_code` header, and compared its remaining stdout with a fresh current CLI invocation, including empty stderr. **45/45** matched exactly (exit, stdout, stderr).
- The 45 replay means all saved baseline and r18 outputs under that run match current behavior. Separately, the 39-case baseline-vs-current comparison independently confirms unchanged transcripts against the baseline checker.

## Six r18 fixtures and paired difference

The positive control `r18-unique-pair` exits 1 with one `double-booked` finding for unique `tower` / `harbor`. Its negative pair `r18-duplicate-pair` differs in exactly one fixture file: `entities.json` appends one complete entity row `{id: harbor, kind: place, name: Fixture duplicate place, first_appearance: archive-ledger, claims: []}`. `contradictions.json`, `relations.json`, `sources.json`, and `timeline.json` are byte-identical. The appended row makes the `harbor` ID ambiguous; output retains duplicate-ID and ambiguous-place findings but suppresses double-booking.

- `r18-duplicate-reverse` reverses the two timeline rows: retains duplicate-ID and ambiguous-place findings, with no double-booking.
- `r18-mixed-kind` uses a duplicate `harbor` row of `kind: character`; it retains duplicate-ID and ambiguous-place findings, with no double-booking.
- `r18-duplicate-first-known` exercises ambiguous / known / known sequence: reports ambiguity and retains a `tower`/`quay` double-booking.
- `r18-known-through-ambiguous` exercises known / ambiguous / known: reports ambiguity and retains a `tower`/`quay` double-booking.

All six current CLI invocations exited 1 with empty stderr. Every event description says it is fixture input and makes no source-text location assertion. The paired output distinction is reproducible and order-insensitive for the two-event ambiguous case. The preservation cases show that this checker still compares the two distinct, uniquely indexed IDs in those rows.

## Evidence limits

This is a checker-behavior result on these JSON inputs, not verification that a source document says the event occurred, or that `harbor`, `tower`, or `quay` is an actual event location. IDs and source IDs are fixture references, not source-text attestation. Suppressing a comparison for an ambiguous ID does not establish there was no real-world/in-world location conflict; the retained unique-ID `double-booked` finding likewise establishes only the checker’s ID-level result, not narrative canon. I did not claim independent source-text review, test-scout completion, or verification beyond the enumerated 194 files, 39 baseline cases, 45 saved outputs, and six fixtures.
