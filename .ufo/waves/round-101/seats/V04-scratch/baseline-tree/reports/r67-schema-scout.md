# Round 67 schema scout — claim citation requirement

## Scope and result
Read-only inspection of the active checker and the round-67 probe inputs. **Recommendation: GO, narrowly**, for the declared claim-local nonempty `source_id` validation. The existing row schema requires an entity `claims` value to be a list, but the nested claim validator does not enforce a nonblank citation. When `sources.json` is unavailable, this allows a claim with an empty citation to receive no claim-local diagnostic. The existing source-table loader error remains; this is not a claim that the entire input passes cleanly.

## Exact code evidence
Path: `.shokunin/lore/corpus/fixtures/check_bible.py` (active tree at baseline HEAD `262486d719ff1690c41b48dd1d0413305c396cdb`).

- Lines 25–32: `FIELDS['entities']` at line 27 requires only that `claims` be a `list`; nested claims are not declared in `FIELDS`.
- Lines 41–76: parser validates required row fields and admits a row only when those fields pass. In particular, `claims` itself passes as a list; nested claim citation semantics are deferred.
- Lines 58–62: `sources_available` is set only if `sources.json` loads as an array.
- Lines 97–109: `source_status()` returns `'unavailable'` at lines 97–101 when the table is unavailable. `source()` emits diagnostics only for `'unknown'` and `'ambiguous'` (lines 103–109), so it emits none for unavailable.
- Lines 145–154: claims are visited at lines 149–150. The condition at line 151 checks that `source_id` is a string, but not that it is nonempty/stripped. An empty-string claim therefore takes the `else` at 153 and calls `source('', ...)` at 154; with unavailable sources, that call emits no claim-local error. With a loaded source table, an empty ID instead produces the existing `unknown in-world source ''` finding.

## Reproduction observed
Command, run from repository root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/live/r67-probe/empty-unavailable
```

Observed exit 1 and output:

```text
VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: '.shokunin/lore/corpus/live/r67-probe/empty-unavailable/sources.json'
1 violation(s); no canon changed
```

The input `.shokunin/lore/corpus/live/r67-probe/empty-unavailable/entities.json` has `entities[0].claims[0].source_id` equal to `""`; its `sources.json` is absent. There is no `entities[0].claims[0]` finding. The matched control `.shokunin/lore/corpus/live/r67-probe/control-unavailable/` has the same claim with `source_id: "courier-log"` and the same missing source table; it emits only the loader error as well. The loaded-table contrast `.shokunin/lore/corpus/live/r67-probe/empty-loaded/` has an empty source ID and a valid `sources.json`; it emits `entities[0].claims[0].source_id: unknown in-world source ''` (plus summary). This confirms the gap is specifically the unavailable-index path, not a general absence of all checker findings.

Command sequence used for all three:

```sh
for d in empty-unavailable control-unavailable empty-loaded; do
  echo ===$d===
  python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/live/r67-probe/$d
  echo EXIT:$?
done
```

## Decision and bounds
GO is supported because the source-local omission is directly observable, and the control demonstrates a nonempty claim citation does not get an invented membership conclusion when its table is unavailable. The proposed validation should report only the required-field defect (`expected nonempty statement and source_id`) at the claim location; it should not call the ID unknown when the source index is unavailable. Existing membership checks can continue when a table is loaded.

This only validates presence/nonblankness of an input citation identifier. It cannot establish source text, support, authenticity, fictional-world evidence or absence, truth, canon, rights, or game mechanics. A nonblank ID is not evidence that the cited source supports the claim. Empty and whitespace-only values should be treated alike if the declared rule says nonempty after stripping; the existing row-level string validation uses `.strip()` at checker line 72, but nested claim validation currently does not.

No checker, fixture, README, LOG, or other file was changed by this scout. No commit or push.
