# Round 9 critic — duplicate-target order and dependency cascades

## Verdict: claim falsified against the observed checker

The current `.shokunin/lore/corpus/fixtures/check_bible.py` builds `events` with `index('timeline')`, which overwrites duplicate IDs with the last row. It separately counts `event_id_counts`, but the timeline dependency loop consults `events[dep]` without consulting that count. Thus the declared ambiguity guard is absent in the observed working tree and row-order invariance fails.

### Probe 1: duplicate target row order changes dependency conclusion

I copied the valid `consistent` fixture into temporary directories (not repo fixtures), replacing its timeline with duplicate target rows `same` at ticks 1 and 5, plus `consumer` at tick 3 with `depends_on: ["same", "same"]`. The paired timelines differ only by reversing the two `same` rows; consumer and all other fixture files stay fixed. Commands were `python3 .shokunin/lore/corpus/fixtures/check_bible.py <temp>/caseFalse` and the corresponding `caseTrue`.

Forward output:
```
VIOLATION: timeline[1].id: duplicate timeline id 'same'
VIOLATION: timeline[2].depends_on: timeline inversion 'same' tick 5 not before 'consumer' tick 3
VIOLATION: timeline[2].depends_on[1]: repeated dependency 'same'
3 violation(s); no canon changed
```

Reversed output:
```
VIOLATION: timeline[1].id: duplicate timeline id 'same'
VIOLATION: timeline[2].depends_on[1]: repeated dependency 'same'
2 violation(s); no canon changed
```

The first ordering asserts an inversion against the last target; the reversed ordering silently treats the dependency as earlier. No `ambiguous dependency event` diagnostic appears. The repeated second prerequisite does not repeat the tick lookup, but does not prevent the first lookup from making an arbitrary choice.

### Probe 2: duplicate IDs plus self/duplicate prerequisites cascade

I made two timeline rows both ID `same`, ticks 1 and 5, each with `depends_on: ["same", "same"]`, and reversed their row order. This is deliberately malformed input, but useful for checking the promised local diagnostics and cascades.

Tick-1-first output included `timeline[0].depends_on: timeline inversion 'same' tick 5 not before 'same' tick 1`; reversed output instead included `timeline[1].depends_on: timeline inversion 'same' tick 1 not before 'same' tick 5`. Both outputs also emit self-dependency at each raw list index and repeated-dependency at `[1]`, plus one duplicate-ID finding. Totals were 9 vs 8 findings. Thus dependency-list diagnostics exist per occurrence, but last-wins lookup adds an order-sensitive inversion cascade atop self and duplicate-target findings. The input and full output can be reconstructed from the recipe above; probes were outside the repository.

### Existing unique-ID behavior / cascade boundary

`.shokunin/lore/corpus/fixtures/r8-deps-anomalous/timeline.json` has `arrival` depending twice on earlier `departure` and on itself. Its observed logic emits the repeated-entry finding, one inversion-free lookup for `departure`, and the self finding plus self tick inversion. This is the intended R8 rule (one lookup per distinct dependency ID), but it shows self-dependency is not just a single diagnostic: it deliberately cascades into a generic inversion. The source at `r8-deps-distinct/timeline.json` is the clean paired baseline. Keep this distinction explicit: repeated-prerequisite suppression is already present; ambiguous target handling is not.

## Recommendations (not implementation)

1. For each distinct dependency ID, use the valid timeline-row count before any tick comparison. If count is greater than one, emit one `ambiguous dependency event` at the depending list entry and skip tick comparison; do not let the last-wins map choose a row. Keep duplicate-ID findings and raw repeat-index findings.
2. Decide explicitly whether self-dependency should additionally emit generic inversion. Current R8 contract says retain the old inversion, so avoid changing that while addressing ambiguity. With duplicate event IDs, ensure the ambiguity finding does not get hidden by a self/inversion cascade.
3. Replay both target-row permutations with a unique-ID consumer, and separately duplicate/self prerequisite probes. Compare the set of findings after normalizing row locations only; require the same conclusion and no arbitrary tick claim. Keep malformed duplicate event ID concerns separate from uniquely resolved dependency semantics.

No source, checker, fixture, or shared documentation was edited. Only this report is intended as the artifact.
