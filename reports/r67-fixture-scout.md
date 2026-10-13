# Round 67 fixture scout — matched missing-citation pair

## Scope and read-only evidence

Read `.shokunin/lore/LOG.md` Round 67, `/tmp/mission-lore-standing.md`, and the baseline checker at `craft/lore-r1` HEAD `262486d`. I did not edit checker or fixtures. Existing exploratory inputs under `.shokunin/lore/corpus/live/r67-probe/` were already present; I only read and ran them. This report is the only file I wrote.

Relevant behavior in `.shokunin/lore/corpus/fixtures/check_bible.py`: entity row validation checks `claims` is a list, then claim validation requires nonempty `statement` and `source_id` to be strings, but does not require the citation string to be nonblank. For an otherwise valid claim it calls `source()`. `source_status()` returns `unavailable` when `sources.json` did not load, and `source()` emits nothing for that status. Thus a blank citation escapes a claim-local diagnostic if the source table is missing. With a loaded source table, blank `''` instead yields `unknown in-world source ''`; that is a different diagnostic path and should not be mistaken for the proposed required-field check.

## Observed probe results

Ran from repository root:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/live/r67-probe/empty-unavailable
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/live/r67-probe/control-unavailable
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/live/r67-probe/empty-loaded
```

Observed respectively:

- `empty-unavailable`: exit 1; stdout is the one `sources.json: cannot load JSON: [Errno 2] No such file or directory: '.shokunin/lore/corpus/live/r67-probe/empty-unavailable/sources.json'` violation, then `1 violation(s); no canon changed`; stderr empty. No claim-local finding.
- `control-unavailable`: same result with its own `control-unavailable/sources.json` path; no claim-local finding.
- `empty-loaded`: exit 1; `VIOLATION: entities[0].claims[0].source_id: unknown in-world source ''`, then `1 violation(s); no canon changed`; stderr empty.

The unavailable pair's entities differ only at `entities[0].claims[0].source_id`: `''` versus `'courier-log'`; all other JSON content is equal. This confirms the baseline gap without suggesting that absence of an in-world source record proves absence of fictional evidence.

## Minimal matched fixture proposal (do not implement in this report)

Use two fixture directories, for example:

- `.shokunin/lore/corpus/fixtures/r67-claim-source-unavailable-missing/`
- `.shokunin/lore/corpus/fixtures/r67-claim-source-unavailable-control/`

Each contains the same four files copied from `consistent/`: `entities.json`, `relations.json`, `timeline.json`, `contradictions.json`; omit `sources.json` in both. Keep all rows identical to `consistent/` except the first entity claim's `source_id`: empty string in `...-missing/`, `courier-log` in `...-control/`. Do not change the claim statement or any other field. This makes source-index unavailability common-mode and the citation value the only independent variable. `consistent/` is a positive reference but is not a matched control for the missing-source condition because it includes a source table.

Exact replay commands from repository root:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r67-claim-source-unavailable-missing
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r67-claim-source-unavailable-control
```

Expected after the proposed narrow rule, assuming the existing output wording and validation order remain unchanged:

```text
# missing: exit 1
VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: '.shokunin/lore/corpus/fixtures/r67-claim-source-unavailable-missing/sources.json'
VIOLATION: entities[0].claims[0]: expected nonempty statement and source_id
2 violation(s); no canon changed
# stderr: empty

# control: exit 1
VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: '.shokunin/lore/corpus/fixtures/r67-claim-source-unavailable-control/sources.json'
1 violation(s); no canon changed
# stderr: empty
```

The required delta is exactly the negative-only claim-local line, not a new `unknown in-world source ''` line. The source-file load failure remains independently reported in both cases. If fixture paths change, the embedded missing-file path changes accordingly. The `[Errno 2]` text is this host's Python/OS rendering, so replay expectations should compare the diagnostic class/path rather than promise that errno prose is portable across platforms.

## Recommendation and limits

**GO** for these two raw fixtures as the smallest useful falsification pair for the declared calibration claim: they isolate the condition that suppresses the existing `source()` diagnostic, and a nonempty citation control distinguishes the new claim-local required-field finding. The baseline currently gives both cases the same one-error output, so the pair has a measurable before/after result. Keep the rule unconditional for claim `source_id` nonemptiness, and avoid calling `source()` on a blank ID; retain existing unknown/ambiguous checks for nonempty IDs when the index is available.

This is a fixture-design GO, not evidence that an implementation is correct or that the round should be admitted. Replay clean/prior fixtures and have the named non-author verifier confirm stable outcomes before any round verdict. Claim scope is only structural nonemptiness of a claim's citation field. It does not establish source-text support, source authenticity, rights, fictional canon, or game mechanics; nor does an unavailable source table mean the fictional setting lacks evidence.
