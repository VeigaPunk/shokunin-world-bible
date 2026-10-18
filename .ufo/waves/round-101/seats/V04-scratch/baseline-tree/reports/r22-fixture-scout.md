# Round 22 fixture scout — mixed dependency and ordering controls

Scope: fixture-only observations and recommendations. No fixture, checker, or shared document was changed. Raw observations below are baseline CLI results from the current `check_bible.py`; all prose in fixture descriptions should describe JSON input fields, not claim story chronology or canon.

## Raw observations (baseline)

I used `r20-valid-inversion` as the basis, copying it to a temporary directory for each CLI probe and changing only the dependent row's `depends_on` list (and, in explicit controls, row order or event IDs). The prerequisite has tick 2; the dependent has tick 1.

| Input | Exit | Finding |
|---|---:|---|
| Clean edge `[`"`r20-prereq`"`]` | 1 | `timeline[1].depends_on: timeline inversion 'r20-prereq' tick 2 not before 'r20-dependent' tick 1` |
| Mixed edge `[`"`r20-prereq`"`, null]` | 1 | `timeline[1].depends_on: expected event-id strings` only; inversion is masked |
| Mixed edge `[null, `"`r20-prereq`"`]` | 1 | Same list-level type finding only; inversion is masked |
| Clean edge, reversed event-row order | 1 | Same inversion, now reported at `timeline[0]` |
| Mixed edge, reversed event-row order | 1 | Same list-level type finding only, now at `timeline[0]`; inversion remains masked |
| Mixed edge renamed consistently to `[`"`alpha`"`, null]` and IDs `alpha`/`beta` | 1 | Same list-level type finding only; no inversion |

The existing empty-list fixture run is clean (exit 0); replacing its dependency list with `[null]` reports the list-level type error. Additional mixed probes (`unknown + null`, `self + null`, repeated known edge + null) all return only the list-level diagnostic, so the current early skip masks those string-member findings as well. These are checker-input observations, not evidence of source-text chronology or canon.

## Fixture recommendations (prose only)

- Keep paired rows identical except for the dependent list: `[`"`r20-prereq`"`]` versus `[`"`r20-prereq`"`, null]`. The expected difference under the declared candidate is an added malformed-member diagnostic while the same string-edge inversion remains visible.
- Add the complementary member order `[null, `"`r20-prereq`"`]` as an order control. This can distinguish member-position dependence from list-wide early-skip behavior.
- Reverse timeline row order in both clean and mixed cases. Preserve stable event IDs and state that only array order changed; location index labels naturally shift.
- Rename both event IDs consistently (prerequisite and dependent) and update the string edge in both pair members. This controls whether observations depend on hard-coded IDs rather than the graph relation.
- Include clean/empty and malformed-only `[null]` controls, plus an ineligible string edge such as an unknown dependency paired with null. Do not treat a malformed member as a satisfied or absent edge.
- Use fixture descriptions such as “Fixture input: dependency and tick fields; no source-text chronology asserted.” Avoid prose like “the prerequisite happens later” as an in-world assertion. The checker result classifies input fields only.

These are design suggestions, not permanent fixtures or an implementation recommendation. In particular, whether to inspect string members despite a malformed list is a policy decision for the round owner; this scout establishes only the baseline masking behavior and useful isolating controls.
