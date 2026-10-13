# Round 84 pair scout — matched event-ID control

## Scope and method

I read the Round 84 declaration in `.shokunin/lore/LOG.md` and inspected `check_bible.py`, the `consistent` baseline fixture, and relevant prior reports: R9, R11–R13, R16/R19, R37, R52, and R70. I made two temporary clones under `/tmp/r84-pair-scout-cne_j1sy/`, outside the repository. Each clone copied all five JSON files from `.shokunin/lore/corpus/fixtures/consistent`; only `timeline.json` was replaced with the two rows below. Thus both inherit the exact baseline sources, entities, relations, and empty contradictions array. No repo corpus or checker was changed.

The controlled difference is only the second row's `id`: `pair-event-b` in the distinct-ID control, `pair-event-a` in the duplicate-ID case. Both rows have the same actor (`mira`), nonnegative local tick (`7`), and different uniquely typed places (`harbor`, `tower`). Both source IDs resolve uniquely in the inherited source list. These are schema-valid row fields; they are invented test inputs, not verified testimony.

Exact replacement timeline inputs:

```json
[
  {
    "id": "pair-event-a",
    "tick": 7,
    "entity_id": "mira",
    "place_id": "harbor",
    "depends_on": [],
    "description": "Mira is recorded at harbor.",
    "source_id": "courier-log"
  },
  {
    "id": "pair-event-b",
    "tick": 7,
    "entity_id": "mira",
    "place_id": "tower",
    "depends_on": [],
    "description": "Mira is recorded at tower.",
    "source_id": "archive-ledger"
  }
]
```

For the duplicate-ID clone, the second row above has exactly this one substitution: `"id": "pair-event-a"` (instead of `"id": "pair-event-b"`).

## Raw root-relative CLI results

Commands were run from the repository root with stdout and stderr redirected separately. The displayed `exit` is the command's actual checker exit status.

Distinct IDs:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r84-pair-scout-cne_j1sy/distinct
```

- Exit: `1`
- stdout:
  ```text
  VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
  1 violation(s); no canon changed
  ```
- stderr: empty

Duplicated ID:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r84-pair-scout-cne_j1sy/duplicated
```

- Exit: `1`
- stdout:
  ```text
  VIOLATION: timeline[1].id: duplicate timeline id 'pair-event-a'
  VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
  2 violation(s); no canon changed
  ```
- stderr: empty

## Observation and limit

The predicted condition is reproduced narrowly: duplicate event ID adds its own finding, but the checker still emits the same definite-looking `double-booked` output. In the inspected occupancy branch, the same-actor/tick comparison depends on unique actor and place IDs and a nonnegative tick; it does not gate on event-ID uniqueness. The distinct-ID control has the same booking finding. Therefore this matched pair does **not** show that event-ID ambiguity currently changes the booking calculation or gives a different immediate repair action. A likely structural repair for the duplicate case is to disambiguate/fix the event IDs; whether the two raw location/tick rows independently warrant a booking warning despite that duplicate label is the unresolved policy question, not settled by these outputs.

Prior art bounds novelty: R9 and R37 exercise duplicate event IDs in dependency/ledger endpoint resolution; R11–R13 and R16/R19 cover actor/place identity and occupancy gates; R52 considers source ambiguity and booking; R70 concerns a separate contradiction-pair equality gate. In particular, duplicate event IDs here are not duplicate actor IDs or ambiguous place IDs. The current output proves only what this checker reports for these supplied JSON rows. It does not establish source-text support, actual co-location, chronology, a fictional-world fact, canon, rights, or mechanics. This scout provides a matched probe, not an axis verdict or implementation recommendation.
