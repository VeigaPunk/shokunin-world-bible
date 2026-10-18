# Round 20 test scout — saved CLI replay and invalid-dependency probes

Role: read-only test scout. I wrote only this report; no checker, fixture, shared document, or commit was changed. Paired probes were copied from the clean `consistent/` bible into temporary `/tmp` directories and changed only `timeline.json`. Probe files are scratch data, not repository fixtures.

## Raw observations

### Saved-output replay

Re-ran all 49 fixture commands recorded in `.shokunin/lore/corpus/live/runs/20261012T190807Z/` against the working-tree checker. Compared exit code and stdout with the saved transcript for each case. **49/49** exit codes and stdout matched exactly; no differences. The re-run produced no stderr. This establishes replay agreement with those saved outputs on the current checker, not comparison to an independently executed baseline revision.

### Dependency endpoint probes

Probe source: `consistent/`; IDs remain `departure` (row 0) and `arrival` (row 1). The first row is the prerequisite and second depends on `departure`. Each case changes only the two ticks and dependency list in `timeline.json`; all other files/fields remain as copied.

| Temporary case | Ticks (departure, arrival) | `arrival.depends_on` | Exit | Exact stdout findings (without `VIOLATION:` prefix) |
|---|---:|---|---:|---|
| invalid prerequisite endpoint | `(-1, 2)` | `['departure']` | 1 | `timeline[0].tick: must be nonnegative`; `1 violation(s); no canon changed` |
| invalid dependent endpoint | `(0, -1)` | `['departure']` | 1 | `timeline[1].tick: must be nonnegative`; `timeline[1].depends_on: timeline inversion 'departure' tick 0 not before 'arrival' tick -1`; `2 violation(s); no canon changed` |
| valid-endpoint inversion | `(2, 1)` | `['departure']` | 1 | `timeline[1].depends_on: timeline inversion 'departure' tick 2 not before 'arrival' tick 1`; `1 violation(s); no canon changed` |
| valid ordered control | `(0, 1)` | `['departure']` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |

All four had empty stderr. The command outputs show that a uniquely indexed endpoint with a negative tick is still used in the comparison: a negative dependent endpoint generated an inversion finding; a negative prerequisite endpoint did not generate inversion because `-1 < 2`. Valid-to-valid inversion remains reported, and the valid ordered pair is clean. The invalid tick diagnostic remains in each negative case.

## Recommendations (not observations)

- The probes support testing a narrow guard that withholds only the definite inversion comparison when either uniquely resolved endpoint has a negative tick, while retaining invalid-tick diagnostics and raw IDs/references. They do not establish that the dependency is satisfied or that events did/did not occur.
- Preserve the valid-to-valid inversion and ordered controls. Before claiming preservation of other behavior, test missing, duplicate/ambiguous, self, and repeated dependency IDs on both sides of the guard.
- Fixture ticks and source IDs are input data; the CLI does not validate source-text support, chronology in canon, or event truth. The finite replay does not establish behavior outside these cases.
