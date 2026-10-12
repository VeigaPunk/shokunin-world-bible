# Round 20 fixture scout — dependency endpoints with negative ticks

## Scope

Scout-only result. Baseline was declared as commit `47733bfa36216a28c639fd8d5dc891fb4d8de3f5`; I extracted `.shokunin/lore/corpus/fixtures/check_bible.py` with `git show 47733bf:...` into `/tmp/r20-check_bible-baseline.py` and ran its raw CLI against temporary copies of the `consistent` fixture. No repository checker or fixture was changed. Fixture descriptions below are explicitly input-scoped; they do not state what a cited source says or establish fictional-world chronology.

## Raw CLI observations (baseline)

Every probe had two uniquely identified events (`prereq`, `dependent`), known entity/place IDs, the same existing source IDs, and a single `dependent.depends_on = ["prereq"]`. The CLI was `python /tmp/r20-check_bible-baseline.py <temporary-fixture-directory>`; stderr was empty in all six runs.

| Probe | Input ticks `(prereq, dependent)` | Exit | Exact stdout |
|---|---:|---:|---|
| negative dependent | `(0, -1)` | 1 | `VIOLATION: timeline[1].tick: must be nonnegative`<br>`VIOLATION: timeline[1].depends_on: timeline inversion 'prereq' tick 0 not before 'dependent' tick -1`<br>`2 violation(s); no canon changed` |
| valid dependent control | `(0, 1)` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| negative prerequisite | `(-1, 0)` | 1 | `VIOLATION: timeline[0].tick: must be nonnegative`<br>`1 violation(s); no canon changed` |
| valid prerequisite control | `(0, 1)` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| valid-to-valid inversion control | `(2, 1)` | 1 | `VIOLATION: timeline[1].depends_on: timeline inversion 'prereq' tick 2 not before 'dependent' tick 1`<br>`1 violation(s); no canon changed` |
| both endpoints negative | `(-2, -1)` | 1 | `VIOLATION: timeline[0].tick: must be nonnegative`<br>`VIOLATION: timeline[1].tick: must be nonnegative`<br>`2 violation(s); no canon changed` |

In each valid pair, the only changed field is the corresponding endpoint tick. Event descriptions are identical input-only text: “Fixture input: prerequisite tick field is provided; this prose does not report source-text chronology.” and “Fixture input: dependent tick and dependency fields are provided; this prose does not report source-text chronology.” No fixture description asserts chronology.

## Recommendations (not baseline observations)

- Minimal negative-dependent pair: `(0,-1)` versus `(0,1)`. Retain negative tick validation in the first; the present baseline additionally emits inversion, while the valid control is clean.
- Minimal negative-prerequisite pair: `(-1,0)` versus `(0,1)`. Baseline reports only the prerequisite’s negative-tick defect in the former and no error in the latter. This makes clear the current false-confidence risk: a dependency involving an invalid endpoint can pass the ordering check without a definite ordering result.
- Preserve `(2,1)` as a valid-to-valid inversion control; it must still report inversion. Optionally retain `(-2,-1)` to check invalid-tick diagnostics survive when both endpoints are invalid.
- A bounded candidate behavior is: retain tick errors and dependency ID diagnostics, but do not compare ordering for a uniquely resolved dependency when either endpoint tick is negative. Do not call that dependency satisfied, chronologically impossible, or canonically false. Keep unknown/ambiguous/self/repeated dependency handling intact. This scout did not test those classes.
- The two “valid prerequisite” / “valid dependent” examples have identical tick inputs `(0,1)` and therefore are one shared control, not independent evidence. Existing source IDs only exercise citation presence/resolution; they do not attest tick values, order, or event truth.
