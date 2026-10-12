# Round 12 independent reviewer — checker diff, raw replay, and critic caveat

## Scope and verdict

I independently reviewed the checker diff, the 26 saved round-12 CLI records, the critic's caveat, and the changed README/decision-table language. I replayed all 26 fixture commands and ran additional temporary probes. The narrow implementation matches the declared clarification: for each timeline row whose actor ID has multiple schema-valid entity rows, it emits an ambiguity finding and skips only that row's occupied-slot comparison/update. It retains raw rows, duplicate-ID diagnostics, and unrelated timeline checks. This avoids asserting a definite same-actor conflict, but it does **not** establish that no real conflict exists; identity and conflict remain indeterminate. The implementation is scoped and coherent, with a modest output-noise concern noted below.

## Diff review

In `check_bible.py`, `ambiguous_actor` is derived from `entity_id_counts` (which counts schema-valid entity rows), after dangling-reference checks. The occupancy `slot` lookup and update are both inside `if not ambiguous_actor:`; other timeline checks continue. This is the right narrow boundary for the LOG clarification. The duplicate entity finding and event rows are not removed. A malformed duplicate is excluded from that count, as intended.

The added fixture pair supports the comparison: `r12-unique-actor` yields one `double-booked` finding; `r12-ambiguous-actor` yields the duplicate-ID finding and two actor-ambiguity findings, with no `double-booked`. The fixture README and decision table correctly state that this means no *definite* same-actor inference, not that a real conflict is absent or impossible. The corpus README lists both fixtures and the new run directory. The critic's warning that duplicate rows might describe one actor is therefore addressed by the current language; avoid shortening this to “no occupancy conflict.”

## Replay evidence

Ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>` for every `*.txt` under `corpus/live/runs/20261012T175244Z/` (26 fixtures). For all 26, current exit code, stdout bytes, and stderr bytes matched the corresponding saved record; no drift. The two new cases both exit 1, stderr empty. Exact outputs:

```text
r12-unique-actor:
VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed

r12-ambiguous-actor:
VIOLATION: entities[4].id: duplicate entities id 'mira'
VIOLATION: timeline[0].entity_id: ambiguous actor entity 'mira'
VIOLATION: timeline[1].entity_id: ambiguous actor entity 'mira'
3 violation(s); no canon changed
```

I also extracted `check_bible.py` from baseline commit `954a1b712590f9b89aed6757e72a8bd4af5c8848` and compared it to the current checker on each of the 24 pre-round-12 fixture directories. All 24 outputs, stderr, and exit codes match exactly. The sole difference among all current fixture directories is the intended `r12-ambiguous-actor` result.

## Additional probes (temporary copies; no fixture files changed)

- Two ambiguous `mira` events at the **same** tick and **same** place: duplicate-ID finding plus one `ambiguous actor entity` finding per event; no `double-booked`. This is logically consistent with “skip only occupancy,” though it reveals that the checker reports actor ambiguity even when there is no differing-place comparison to suppress.
- A malformed duplicate `mira` entity row (missing required fields) plus same-tick/different-place events: malformed-field findings and the old `double-booked` remain; no ambiguous-actor finding. The malformed row does not count as a valid identity candidate.
- A mixed valid schedule with duplicated `mira` and unique `kestrel`, each appearing at two different places on the same tick: `mira` gets duplicate-ID plus two ambiguity findings and no definite double-booking; `kestrel` still gets `double-booked`. This demonstrates the skip is actor-ID-local and does not disable other actors' checks.
- Two dangling `unlisted` actor rows at same tick/different places: two dangling findings **and** the prior `double-booked` finding remain. This is the documented limitation, not evidence that a conflict is absent; zero valid entity rows are not handled by the new ambiguity guard.

## Caveat / possible noise

As the critic observed, duplicate rows have two plausible interpretations: duplicate descriptions of one actor (where a true conflict may exist) or distinct actors with a colliding ID (where the old assertion may be false). Neither can be resolved from this schema. The new result properly withholds a *definite* actor-level assertion while preserving this uncertainty. It also emits one ambiguity finding for every affected event even when the events share a place or have different ticks and no occupancy comparison would conflict. That is a small potential noise cost, but it is explicit, local, and the declared rule says each affected timeline row gets the finding; I found no broader checker change or changed prior fixture output.

**Reviewer conclusion:** round-12 evidence supports the stated calibration move, provided its result remains described as indeterminate identity / no definite same-actor inference—not as proof that occupancy conflict is absent. No harm found in the reviewed legacy fixtures or the mixed unique/ambiguous probe. No source, fixture, or documentation files were changed by this review.
