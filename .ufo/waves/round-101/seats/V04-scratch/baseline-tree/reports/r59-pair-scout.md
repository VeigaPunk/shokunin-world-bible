# Round 59 pair scout — swapped duplicate object member probe

## Evidence inspected

- `.shokunin/lore/LOG.md:1008-1021` declares r59 calibration hypothesis and guardrails: raw duplicate member names versus duplicate row IDs, swapped `timeline[1].place_id` values, unique control, old tuple preservation, and no truth/canon/rights inference.
- `corpus/fixtures/check_bible.py:18-43` reads text, calls `json.loads`, then validates decoded rows. No `object_pairs_hook` or raw-member check occurs. `:45-60` separately indexes decoded record IDs and diagnoses duplicate IDs. These are different layers: repeated JSON keys are collapsed before validation; repeated row IDs are checked later.
- `corpus/fixtures/check_bible.py:242-270` performs timeline endpoint/kind/occupancy checks on decoded `entity_id`/`place_id`; last-wins may alter a checker decision, not story fact.
- `consistent/timeline.json:9-17` provides `arrival` with `place_id: tower`; swap in `place_id: harbor` as an alternate valid entity. Keep all other bytes/rows unchanged for the pair.
- `2026-10-12-malformed-error-patterns.md:11-20` records r5 behaviors: malformed JSON gets `cannot load JSON`; wrong top-level array and non-object row have explicit errors; caveat says parser wording/offsets are not portable and cascades can occur.
- `r9-dup-low-high.txt`, `r9-dup-high-low.txt`, `r9-unique-control.txt` (run `20261012T172227Z`) show duplicate timeline row IDs report both duplicate ID and ambiguous dependency independent of order, while unique case is CLEAN. This precedent concerns row IDs, not JSON object members.

## Pair design and expected current raw behavior

Use an isolated temp copy of `consistent/`, change only the second timeline row object, and preserve byte-for-byte valid JSON other than duplicate insertion:

1. duplicate-low-high: `... "place_id": "harbor", "place_id": "tower" ...`
2. duplicate-high-low: `... "place_id": "tower", "place_id": "harbor" ...`
3. unique control: original single `"place_id": "tower"`.

Both values are existing valid places; the JSON text is syntactically accepted. Current Python decoder keeps the later occurrence. Thus duplicate-low-high decodes as tower and should match original CLEAN control; duplicate-high-low decodes as harbor and should produce the checker’s existing occupancy finding for Mira at harbor at both ticks. This is a material order-sensitive, silent raw-input difference, not a finding about whether Mira was actually at either place. Verify exact current raw output with the existing CLI before interpreting; no run was made in this scout.

## Proposed behavior / nested constraint

Proposal for a narrowly scoped parser hook: use `json.loads(..., object_pairs_hook=...)` that preserves pair sequences long enough to detect repeated member names in every object, including nested objects, and raises a dedicated parse/input error rather than returning a last-wins dict. The outer per-file exception path should produce one file-local `cannot load JSON`-style diagnostic (prefer stable wording for duplicate member name, not parser offsets), set that table to empty as existing catch does, and avoid semantic cascade from a chosen duplicate value. Do not claim row indices from a hook: at parse time the hook receives each object’s pairs, not reliably its enclosing JSON path/index. A file-level diagnostic is honest absent a location-tracking parser.

For nested scope, hook naturally sees objects in `entities[].claims[]`, `contradictions[].claim_a/claim_b`, and provenance records too. Duplicate keys there should likewise reject that JSON file, not silently overwrite. But do not emit `timeline[1].place_id` from hook or infer where a nested object resides; object-pairs callback lacks parent path. A top-level duplicate can be reported by key name only if location not implemented. If implementation cannot preserve existing exception handling cleanly, defer nested support explicitly rather than overpromise.

## Calibration verdict

**MATERIAL CALIBRATION GO** for testing/executor consideration, not permission to implement without independent validation. The reciprocal-order pair changes decoded semantics while both source strings are valid and shape-valid, and the unique control isolates duplicate-key ambiguity. Proposed parser rejection makes uncertainty explicit and refuses arbitrary last-wins selection. Calibration is improved only if pair replay confirms current outputs differ, new behavior rejects both duplicate variants without a semantic occupancy choice, and unique control plus all pinned 95 old CLI tuples remain unchanged (or every justified delta is accounted for).

**Falsifier / NO-GO:** if actual pair outputs are order-invariant under checker logic, an established fixture/spec rule explicitly defines last-wins as intended, or rejection creates disproportionate regressions/cascades (including pinned corpus deltas that cannot be justified), then the material calibration claim fails. Also no-go if a hook is presented as having precise nested row locations it cannot know. Old corpus preservation alone does not prove new calibration.

## Risks and boundaries

- Python decoder behavior is implementation detail; a custom hook affects all JSON objects and may reject legitimate existing data if duplicate keys are intentionally tolerated. Scan all 474 JSON paths before adoption.
- One bad file mapped to empty rows can generate downstream dangling/missing-reference noise; report one parse-layer issue and avoid extra downstream diagnostics where feasible, consistent with r5 cascade caveat.
- Comparing full output requires stable control over paths/argv; absolute temp paths can alter exception strings. Compare normalized or repo-root controlled outputs and retain raw capture.
- This concerns duplicate JSON object member names only. It does not conflate duplicate row IDs, determine authored-source support, or infer actual story truth, canon, chronology, rights or permission.

No checker, fixture, README, LOG or commit changes made. Only this report is in scope.
