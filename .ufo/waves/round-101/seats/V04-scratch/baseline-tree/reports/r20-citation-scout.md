# Round 20 citation scout — input time, source text, and canon

## Scope and evidence

Read-only scout of `.shokunin/lore/corpus/fixtures/check_bible.py`, the fixture README and existing timeline examples. Temporary paired probes were created outside the repository from `consistent/`; no fixture, checker, shared document, or canon was changed. The probe descriptions were explicitly input-scoped. The checker was run with the repository's Python 3 interface.

## Raw observations (not recommendations)

- `timeline[].tick` is required to be an exact `int`; negative integers retain a `must be nonnegative` diagnostic. The timeline dependency pass still looks up a uniquely resolved dependency event and compares the raw integers using `events[dep]['tick'] >= row['tick']`. It does not gate comparison on either endpoint's tick validation.
- Temporary input with prerequisite tick `0`, dependent tick `-1`, and the dependent referencing the prerequisite produced both the negative-tick finding and `timeline inversion 'prerequisite' tick 0 not before 'dependent' tick -1`.
- The reversed invalid-endpoint case (prerequisite `-1`, dependent `0`) produced the negative-tick finding and no inversion finding. This follows the raw comparison; it does not establish a valid chronology.
- Valid controls behaved as expected under the present checker: prerequisite `2`, dependent `1` produced inversion; prerequisite `0`, dependent `1` with the dependency produced clean output. These controls show the existing valid-to-valid comparison is active.
- The schema-valid `source_id` is checked for identity/uniqueness, not dereferenced text. `sources.json`'s `courier-log` entry labels itself a fictional personal log; example timeline descriptions are prose fields, but no checker code tests whether a source passage states the description, tick, or dependency. A resolvable source ID therefore does not attest event occurrence, tick, ordering, or support in source text.
- The fixture README frames ticks as an invented world's local sequence, not an absolute date, and dependencies as a local ordering convention. That documentation is project explanation, not source-text evidence for a specific timeline row.

## Recommendations (separate from observations)

- If the round's declared calibration question proceeds, keep any candidate narrowly about withholding the definite inversion comparison when either uniquely identified endpoint has a negative tick. Preserve the negative-tick finding and raw event/dependency data; do not infer the dependency is satisfied, false, or canonically impossible. Keep valid-to-valid ordering and unknown, ambiguous, self, and repeated dependency findings separately observable.
- Pair fixture inputs differing only in the relevant endpoint tick, with both orientations (invalid dependent and invalid prerequisite), plus valid-order and valid-inversion controls. Use descriptions that state only what the fixture input fields contain, not what a cited fictional text says.
- Report the result as checker-input calibration only. Do not claim a source supports either tick or event, that the dependency happened in-world, that chronology is settled, or that a suppressed comparison means no inversion/conflict in canon. Keep source-text review and canon decisions distinct from structural ID/tick checks.

These are scout observations and recommendations only, not an axis verdict or claim that the round is admitted.
