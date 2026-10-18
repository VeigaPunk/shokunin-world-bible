# Round 13 critic — missing actor references and occupancy

## Observed raw paths and probes

Read the round-13 declaration in `.shokunin/lore/LOG.md` and the standing brief at `/tmp/mission-lore-standing.md`. Inspected `.shokunin/lore/corpus/fixtures/check_bible.py`, especially schema filtering into `data['entities']`, `entity_id_counts`, the timeline dangling-reference check, and the `occupied` map. The map is keyed by `(row['entity_id'], row['tick'])`; the loop checks `row['entity_id'] not in entities` and emits a dangling finding, but still enters occupancy unless the count is greater than one. Thus a zero-match ID currently gets grouped by its literal string just like a unique ID.

I made temporary copies of `.shokunin/lore/corpus/fixtures/consistent` under `/tmp/lore-r13-critic-n4ivlutu/{missing,unique}`. Each had two valid timeline rows at tick 9, places `harbor` and `tower`, distinct event IDs, empty dependencies, and source `courier-log`. The only intended difference was actor ID: `unlisted` (zero matching entity rows) versus existing unique `mira`. No repository fixture was edited.

Commands:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r13-critic-n4ivlutu/missing
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r13-critic-n4ivlutu/unique
```

Current checker output (exit 1; stderr empty) for `missing`:

```text
VIOLATION: timeline[0].entity_id: dangling entity 'unlisted'
VIOLATION: timeline[1].entity_id: dangling entity 'unlisted'
VIOLATION: timeline[1]: double-booked 'unlisted' at tick 9 in timeline[0] ('harbor') and 'tower'
3 violation(s); no canon changed
```

The `unique` control (exit 1; stderr empty) reports `timeline[1]: double-booked 'mira' at tick 9 in timeline[0] ('harbor') and 'tower'` and one violation. I extracted the declared baseline checker with `git show 97f766762ac78ab6bcf6523aadbd2ffa92d4f4f5:.shokunin/lore/corpus/fixtures/check_bible.py`; it produces the same output and exits for both probes. This confirms the declared behavior, not the intended post-move result.

## Falsification / interpretation

The proposed suppression is **not falsified as a calibration concern**, but the stronger premise “a dangling actor ID means there is no actor-level collision” is false/unsupported. With zero schema-valid entity rows, the checker has no resolved entity target for that reference. The same two raw events are compatible with at least two readings: both events refer to one omitted/mistyped actor who may indeed be at conflicting places, or the identical unresolved token was used for different actors. The schema and citations shown here distinguish neither. The events’ separate IDs mean separate records, not necessarily separate people; identical missing strings do not establish shared identity either.

So baseline `double-booked 'unlisted'` is a potentially spurious same-actor attribution, not proven false in this input. Conversely, suppressing that definite assertion must not be described as proving “no conflict,” clearing the schedule, or showing the events compatible. It makes the identity/conflict conclusion unresolved. A real conflict can be hidden if the output simply drops the collision without preserving an explicit indication that same-actor occupancy could not be assessed. Dangling findings keep the unresolved references visible, but do not by themselves say that occupancy was withheld or that a potential conflict remains unadjudicated.

This probes only two same-tick, different-place events. It does not demonstrate every zero-count case needs an extra per-row warning: if an ID occurs once, there is no pairwise occupancy assertion to suppress. It also does not prove that all repeated dangling tokens refer to the same entity. Keep any suppression bounded to the actor occupancy inference, not other timeline checks.

## Recommendations (not observed behavior)

- If changing count-zero behavior, withhold the **definite** `double-booked` assertion for that unresolved ID, but preserve both dangling-reference findings and all raw events. Describe the result as unresolved identity / no definite same-actor inference—not “no conflict.” Consider a concise local indeterminate-occupancy finding when a same-tick/different-place comparison is actually skipped, so a possible true conflict is not silently lost among dangling diagnostics. This is a recommendation, not a claim about implementation.
- Retain the unique-actor same-tick/different-place control and round-12 duplicated-ID ambiguity behavior. A dangling ID (zero candidates) and duplicate ID (multiple candidates) are distinct causes of unresolved reference; neither is evidence of different actors, and neither warrants selecting identity.
- Keep the test claim structural and modest: output should not assert same-actor collision from unresolved identity; it cannot establish whether the underlying fictional events conflict in-world. Test zero, one, and multiple valid matches separately, and retain the stated exact-output replay for the 26 prior fixtures if behavior is changed.
- Do not infer from this probe that a missing entity row is a valid entity, that a citation authenticates actor identity, or that a source proves either event. No canon, source-truth, or game-mechanics conclusion follows.

No checker, fixture, shared documentation, LOG, or commit was changed. Only this scoped critic report was written.
