# Round 67 regression scout — baseline inventory and replay plan

## Scope and state observed

Read `.shokunin/lore/LOG.md` Round 67 and `/tmp/mission-lore-standing.md`. At inspection, `git rev-parse --short HEAD` returned `262486d`; this matches the round declaration. `git status --short` showed the orchestrator's modified LOG, `corpus/live/r67-probe/`, and other scouts’ reports. I did not modify any of those. Existing fixture inventory: 125 directories under `.shokunin/lore/corpus/fixtures/`; Round 67's declaration records 623 JSON files at baseline. Checker: `.shokunin/lore/corpus/fixtures/check_bible.py`.

The declared candidate concerns an entity claim whose `source_id` is empty/whitespace while `sources.json` cannot be loaded. This is specifically about required citation data and checker diagnostics, not fictional-world evidence.

## Baseline raw CLI replay

I ran the checker once against each of the 125 fixture directories, preserving each stdout and stderr in `/tmp/r67-baseline-<fixture-name>.out` and `.err` (outside the repository). The invocation form was:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-name>
```

Observed stdout categories: 24 start `CLEAN:` and 101 start `VIOLATION:`. This is exit classification from the runner (`$?`), not a claim that every violating fixture is expected to fail for the Round 67 rule. Example output:

```text
$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent
CLEAN: schema, citations, relations, timeline; 0 violations
exit 0

$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r61-direct-unavailable
VIOLATION: sources.json: cannot load JSON: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
1 violation(s); no canon changed
exit 1
```

Relevant fixture comparison already present:

- `corpus/fixtures/r61-direct-unavailable/{sources,entities,relations,timeline,contradictions}.json`: `sources.json` is `{invalid json`; entity claim values remain ordinary nonempty strings. Raw output has only the sources load failure, no claim-local diagnostic.
- `corpus/fixtures/r61-direct-empty/`: source index is `[]`; output reports unknown source references, including `entities[0].claims[0].source_id`, not a required-nonempty-field finding.
- `corpus/fixtures/r61-independent-unavailable/`: unavailable index plus unrelated deliberate defects; it is not a clean isolated control.
- `corpus/fixtures/consistent/`: clean output, exit 0.

This replay establishes ordinary fixture regression baseline and illustrates unavailable-index behavior, but does **not** test the candidate defect: these fixtures do not pair unavailable `sources.json` with an empty/whitespace claim `source_id`. The orchestrator's separate untracked `corpus/live/r67-probe/` was visible but was not used or modified in this report.

## Non-author replay plan (after any candidate implementation)

1. A non-author obtains the exact candidate commit and records `git rev-parse HEAD`, `git status --short`, Python version, and checker path. Confirm the 125 committed fixtures match the declared baseline; exclude `corpus/live/` scratch from the fixture corpus.
2. Run the same command over all 125 fixture directories, capturing **raw stdout, stderr, and exit status** per directory. Compare byte-for-byte against pre-change baseline artifacts if available; otherwise use the baseline invocation above and its saved outputs, noting these `/tmp` files are local to this scout's environment and may not transfer. Do not equate “all old failures still fail” with identical output.
3. Replay a matched minimal pair supplied by the executor: both have valid entity arrays and one claim with nonempty statement; control has a valid nonempty claim source ID, negative case has `""` or whitespace. Set `sources.json` unavailable in both (e.g. absent, if the test is meant to exercise unavailability; specify which failure mode). Capture raw tuples. Require the negative to add exactly the claim-local `expected nonempty statement and source_id` finding, with no `unknown in-world source` for the empty ID; control must not receive that finding. Keep other files/data byte-identical.
4. Also replay the negative with a loaded source table to ensure the requirement does not depend on index state, then run `consistent` as clean control. Review changes in raw output, not just exit codes; distinguish pre-existing sources load errors from newly added diagnostics.
5. Report exact commands, commit, fixture hashes or diffs, raw artifact locations, and any deviations. A failure, missing artifact, environment mismatch, changed unrelated diagnostic, or non-isolated pair is NO-GO pending explanation.

## Scout assessment

**GO, narrowly, to implement and independently test the declared required-field check**, because current code inspection shows claim validation only tests `source_id` is a string (not `.strip()`), then calls `source()` whose membership check returns `unavailable` without an error when the source table cannot load. The current 125-fixture replay cannot falsify the specific hypothesis because no baseline fixture covers the minimal empty-ID/unavailable-index case. Treat this as a testable validation gap, not established user impact or evidence that any fictional-world source is absent.

**NO-GO for a final round claim until** the matched pair and full raw-output replay pass under a non-author, and the result is shown not to harm coverage/depth or change unrelated findings. This scout makes no claim about canon, source-text support/authenticity, rights, or game mechanics.
