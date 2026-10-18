# Round 63 pair scout — non-finite JSON tokens

## Decision: **GO, narrowly, to evaluate material calibration**

This supports a candidate test, not implementation/admission by itself. The consequential distinction is accepted ignored metadata versus a typed field that rejects the same token. A non-finite literal in an unknown field is currently silently accepted as CLEAN; the same token in `timeline[].tick` is caught by the integer schema. A nested ignored member is also accepted. Therefore schema validation is only effective after Python's decoder has already accepted `NaN`/`Infinity` as values, and unknown keys can bypass type checks. Rejecting these tokens at file parse could make malformed input consistently visible. This is material to input validation only if the project's supported input contract excludes non-finite JSON values; establish that premise before implementation.

## Matched temporary probes (observed)

Used `consistent/` as identical baseline, made isolated copies under `/tmp/lore-r63-pair-*`, changed one value, and ran the unchanged `corpus/fixtures/check_bible.py`.

| Case | Single mutation | Actual result |
|---|---|---|
| clean control | none | exit 0, `CLEAN: ... 0 violations` |
| ignored-key | add `"extra": NaN` to a source object | exit 0, `CLEAN` |
| nested ignored-key | add `"extra": {"v": Infinity}` to an entity claim object | exit 0, `CLEAN` |
| typed tick | set `timeline[1].tick` to `NaN` | exit 1, `required nonempty int` at `timeline[1].tick` |
| typed tick | same field set to `Infinity` | exit 1, same required-int diagnostic |
| valid numeric control | set tick to `2.0` | exit 1, same required-int diagnostic; checker requires exact `int` rather than numeric value generally |

Thus the ignored-key CLEAN outcome contrasts with a typed-field error, but the typed probe does **not** show a non-finite-specific detector: `NaN`, `Infinity`, and ordinary JSON number `2.0` all fail the existing exact-int rule. It is the acceptance through ignored fields—not typed-field behavior—that demonstrates a possible calibration gain. `consistent/` control is valid; all probes were temporary and do not constitute repository fixtures or supported-producer tests. The round-63 LOG also records a parent probe of top-level ignored `sources[0].extra: NaN` yielding CLEAN; my independent probes reproduce it and nested ignored metadata.

## Relevant implementation / precedent

- `corpus/fixtures/check_bible.py:10-23,45`: decoder's `object_pairs_hook=unique_object` rejects duplicate member names, then otherwise uses Python's `json.loads`; it has no `parse_constant` override. The existing exception branch at `:46-53` handles duplicate-member and ordinary decode failures as file-level errors and substitutes empty rows.
- `:25-32,54-57,65-80`: required fields and row schema are checked after decode; unknown members are not rejected, so `extra` is outside the typed schema.
- R59 directly addressed raw duplicate object member names (reports `r59-pair-scout.md`, `r59-prior-scout.md`) and established a general parse hook, not strict JSON-number policy. R5 (`reports/r5-loader-scout.md`, `r5-axis-adjudicator.md`) measured malformed syntax, wrong top-level shapes, and row shapes; it did not test non-finite constants. Python accepts these extensions unless `parse_constant` rejects them. I found no explicit repository policy in reviewed evidence that specifies strict RFC JSON or a producer guarantee; absence of a local policy is not evidence of incompatibility or support.

## Scoped proposition, falsifier, and possible harm

A narrowly scoped candidate is `json.loads(..., parse_constant=reject_nonfinite, object_pairs_hook=unique_object)` (callback raises a dedicated input exception), rejecting exactly `NaN`, `Infinity`, `-Infinity` at any depth. The resulting error should identify the file and token, not claim a row location unavailable to a decoder callback. Existing loader behavior unloads that whole table; this may cause dependent diagnostics (e.g. entity/table availability and timeline/source lookups). Test and bound that cascade; do not silently claim one local finding. Preserve unique-member and valid finite-number behavior. Include NaN/±Infinity at ignored top-level and nested members, and typed fields; finite valid number controls must be chosen mindful that integer schema rejects `2.0` already (test `2`, and a float in an explicitly permitted extension if applicable).

**Falsifier / NO-GO:** authoritative producer/format evidence says these tokens are intentionally supported, or a realistic supported producer emits them and their rejection causes relevant data loss; paired tests show no consequential checker outcome beyond existing typed-field rejection; or whole-file unload causes disproportionate unrelated diagnostics / loses useful independent checks. Also NO-GO if policy is merely assumed from RFC syntax without compatibility evidence. Parent's preliminary declaration anticipated this compatibility gate. A parser-level rejection diagnoses invalid input; it cannot establish story-source truth, actual chronology, event validity, canon, license, rights, or permission. No source prose or canon was changed.

No checker, fixture, README, LOG, or commit edits made. Only this report is in scope.
