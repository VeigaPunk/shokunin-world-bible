# Round 20 simplifier — negative-endpoint inversion guard

## Raw observations

- The inversion comparison is in the unique-dependency branch of the timeline loop. Once `event_id_counts[dep] == 1`, the current code emits inversion when `events[dep]['tick'] >= row['tick']`. The preceding self, repeated, unknown, and ambiguous-dependency checks are separate branches.
- I copied the `consistent` fixture to temporary directories and changed only the two timeline rows' ticks/dependency lists; no repository fixture or checker was edited. CLI results:
  - prerequisite `departure` at tick 0, dependent `arrival` at -1 with `depends_on: ["departure"]`: `arrival` receives `must be nonnegative` and a definite inversion (`tick 0 not before ... tick -1`).
  - prerequisite at -1, dependent at 0 with the same dependency: only the prerequisite receives `must be nonnegative`; no inversion is emitted.
  - a valid inversion (prerequisite tick 2, dependent tick 1): inversion is emitted.
  - valid ordered dependency (0 then 1): clean.
- The asymmetry is explained by the present one-sided comparison: `0 >= -1` is true, while `-1 >= 0` is false. It compares invalid endpoint ticks as if the checker had a supported chronology.

## Recommendation (not implemented)

Keep the unique-dependency branch and change only its comparison guard to require both endpoint ticks nonnegative before testing their order:

```python
elif (events[dep]['tick'] >= 0 and row['tick'] >= 0
      and events[dep]['tick'] >= row['tick']):
```

This is the smallest local guard: it adds no `continue`, leaves tick diagnostics and raw rows untouched, and does not alter self/repeated/unknown/ambiguous dependency branches. It retains valid-to-valid inversion detection and withholds comparison when either endpoint is negative. It does not treat an invalid tick as proof that a dependency is satisfied or that events did not occur.

I did not edit the checker, fixtures, shared docs, or commit, and did not replay the 49-output baseline; those remain validation tasks for the executor/verifier. These observations establish bounded CLI behavior only, not source chronology or canon truth.
