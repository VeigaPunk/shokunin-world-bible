# Round 5 simplifier — evidence-preserving fixtures

## Observations

- The active checker is `.shokunin/lore/corpus/fixtures/check_bible.py`; `check()` loads exactly five JSON tables (`sources`, `entities`, `relations`, `timeline`, `contradictions`). Its CLI prints `VIOLATION:` diagnostics and returns 1 if any exist; clean input prints `CLEAN:` and returns 0. No checker change is needed to exercise the five LOG-listed cases.
- `.shokunin/lore/corpus/fixtures/consistent/` is already the clean five-file baseline. The current fixture README runs it using `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent`.
- I independently probed mutations made on temporary copies of that baseline, without changing tracked fixtures. Example invocation shape was `python3 .shokunin/lore/corpus/fixtures/check_bible.py "$tmp"`; mutations were (a) remove `sources.json`, (b) replace it with `{`, (c) replace it with `{}` and (d) replace `entities.json` with `[null]`, and (e) change `entities[0].first_appearance` to `missing-source`. All exited 1. Diagnostic classes were respectively `cannot load JSON` (plus expected downstream unknown-source diagnostics), `cannot load JSON` (plus downstream unknown-source diagnostics), `expected array` (plus downstream diagnostics), `entities[0]: expected object` (plus dangling-reference diagnostics), and `unknown in-world source` (one violation). Clean baseline exited 0.
- Loader errors include host-specific paths / parser offsets. Reproducible table assertions should match exit code and stable diagnostic class/subject, not literal absolute paths or JSON parser wording. Missing/invalid `sources.json` necessarily causes secondary unknown-source errors; those are observed behavior, not separate mutations.

## Recommendation

Keep the clean baseline as the sole full fixture. For each malformed case, commit a tiny *one-file mutation recipe* (for example JSON patch/input or a short declarative manifest) and use a shell/Python runner to copy the baseline to a temporary directory, apply exactly that mutation, invoke the existing checker, and record output/exit status. This avoids five redundant copies of four unchanged tables while retaining independently replayable, one-aspect evidence. Keep the runner and mutation inputs under the round-5 corpus scratch/fixture scope; do not add checker branches or alter active checker behavior. A second option—five complete copied directories—is simpler to invoke but duplicates unchanged canon data and increases drift risk.

The five mutations should each be applied to a fresh baseline copy, never cumulatively. Retain the exact invocation and raw stdout/stderr/status per case (or have the runner capture them) so the decision table is replay evidence, not merely an asserted expected result. If the round's contract requires committed raw fixture directories rather than deterministic recipes, prefer full snapshots; that is an evidence-contract choice, not a checker limitation.

## Scope

No tracked checker, fixture, or shared documentation was edited for this scout. No claim is made that these five probes exhaust malformed-input behavior.
