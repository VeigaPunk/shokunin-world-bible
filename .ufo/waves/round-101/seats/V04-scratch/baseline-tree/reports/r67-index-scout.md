# Round 67 index scout — unavailable-source diagnostics

## Scope
Read-only inspection of `.shokunin/lore/corpus/fixtures/check_bible.py` and temporary inputs under `/tmp`. No checker, fixture, README, LOG, or corpus files were changed. The temporary directories were removed by `TemporaryDirectory` on exit. This report does not assert anything about source text, canon, rights, or game mechanics.

## Code observations
At `.shokunin/lore/corpus/fixtures/check_bible.py`, `FIELDS['entities']` requires `claims` to be a list. In the entity claim loop, the condition rejects a claim when it is not a dict, its `statement` is not a nonempty string, or `source_id` is not a string. It does **not** reject `source_id == ''` or whitespace-only strings. In the `else` branch, it calls `source(claim['source_id'], label + '.source_id')`.

`source_status()` returns `unavailable` when `sources_available` is false. The `source()` helper emits errors only for `unknown` and `ambiguous`, so an empty or whitespace `source_id` produces no claim-local finding when `sources.json` cannot load. The loader separately emits a global `sources.json: cannot load JSON: ...` diagnostic. When the index is available, an empty ID instead receives the claim-local `unknown in-world source ''` finding. Thus the gap is conditional on unavailable source index and concerns validation of required input shape, not a conclusion that evidence is absent from the fictional world.

## Reproduction
The following temporary probes ran the repository checker via Python (no repository files modified):

```text
python .shokunin/lore/corpus/fixtures/check_bible.py <temporary-directory>
```

For each probe, `entities.json` contained a valid entity with one nonempty statement and source ID respectively `""`, `"   "`, or `"known"`; `sources.json` contained invalid JSON (`{ invalid index`); relations/timeline/contradictions were valid empty arrays. All three runs returned exit 1, stderr empty, and exactly this stdout (with the per-run temp path):

```text
VIOLATION: sources.json: cannot load JSON: Expecting property name enclosed in double quotes: line 1 column 3 (char 2)
1 violation(s); no canon changed
```

No claim-local diagnostic appeared, including for empty/whitespace IDs. This establishes behavior for an invalid/unloadable index. A separate probe omitted `sources.json` entirely and used `source_id: ""`; exit 1, stderr empty, stdout was only the loader's `sources.json: cannot load JSON: [Errno 2] No such file or directory: '<temporary-path>/sources.json'` plus `1 violation(s); no canon changed`. This establishes the missing-index case too.

The checked-in `.shokunin/lore/corpus/fixtures/` inventory contains 125 fixture directories (as stated in Round 67 declaration); my scan found no entity claim with an empty/whitespace string source ID and no fixture directory lacking `sources.json`. The existing fixture corpus therefore does not itself exercise this combination. The reproduction is synthetic and supports only the diagnosed code-path behavior.

## Assessment
**GO for the declared calibration move, narrowly.** A claim-level nonempty `source_id` check independent of index availability would distinguish a malformed/missing citation field from the separate inability to consult the source index. The present checker does not already report that claim-local defect in the reproduced unavailable-index cases, so the declared falsifier (“existing behavior already reports that required-field defect”) is not met. Keep the existing global index-load error and source-identity checks for nonempty IDs; do not convert index unavailability into an unknown-source judgment. A matched negative/control fixture pair and independent replay are still needed to establish improvement and no regressions before admission.

Bounded axis view: calibration is plausibly improved by making a required field's empty value observable despite a separate unavailable dependency. Depth and coverage appear unchanged by the narrowly specified check, but this scout did not implement or replay a candidate and cannot establish either axis as improved or verify regression stability. This is not a final round adjudication.
