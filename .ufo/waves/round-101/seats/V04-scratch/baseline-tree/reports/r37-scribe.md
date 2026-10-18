# Round 37 scribe — decision table and exact commands

Scope: decision aid for the declared coverage probe, not a checker or canon interpretation. Round 37 specifies one duplicated `tarin-envelope-observation` row while retaining ledger `bell7-location-reports` (`.shokunin/lore/LOG.md:366-368`). No fixture, checker, LOG, README, or commit changes are made here.

## Decision table

| Timeline rows matching a ledger pointer `event_id` | Checker result | What can be concluded |
|---|---|---|
| None | At each affected `claim_*.event_id`, `expected exactly one timeline event '<id>'`; no event source lookup for that pointer. | Pointer is unresolved, not evidence that the reported assertion is false or absent. |
| Exactly one | Pointer resolves to that row; then its source reference is checked for missing/ambiguous source ID. | Structural pointer resolution only. It does not validate `why`, prose semantics, report truth, or canon. |
| More than one | Global `timeline[i].id: duplicate timeline id '<id>'`, plus `expected exactly one timeline event '<id>'` at each ledger endpoint that names it. Pointer resolution skips source lookup for that endpoint. | Endpoint identity is ambiguous. Do not choose first/last row, erase either testimony, conclude testimony false, or resolve a canon winner. Other uniquely resolving endpoint may still resolve independently. |

The branch is explicit in `check_bible.py`: timeline indexing reports duplicates but overwrites the map (`.shokunin/lore/corpus/fixtures/check_bible.py:45-51,58-62`); ledger endpoint cardinality is independently counted and requires exactly one before lookup (`:77-100`, especially `:92-100`). Do not mistake the overwritten `events[id]` row for a valid ledger resolution: the count guard prevents that.

## Exact commands

Run from repository root; both paths below are the declared control/candidate names, not yet asserted to exist (`.shokunin/lore/LOG.md:366-368`):

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r37-bell7-ledger-unique
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r37-bell7-ledger-duplicate
```

Expected control: exit 0, `CLEAN: schema, citations, relations, timeline; 0 violations`. Expected candidate includes the timeline duplicate diagnostic and ledger-local `contradictions[0].claim_a.event_id: expected exactly one timeline event 'tarin-envelope-observation'`; enumerate all additional findings from actual output rather than assuming only these. The declared negative expectation and regression bounds are in `.shokunin/lore/LOG.md:366-368` (88 previous CLI tuples; 439 prior JSON paths).

## Precedent and limits

Round 9 duplicates timeline ID `same` in both row orders, and shows order must not select a dependency target (`.shokunin/lore/corpus/fixtures/r9-dup-low-high/timeline.json:1-29`; high/low counterpart `.shokunin/lore/corpus/fixtures/r9-dup-high-low/timeline.json`). It has `contradictions: []`, however, so does not exercise the two-sided ledger endpoint case (`r9-dup-low-high/contradictions.json:1`). R37 is distinct in testing the ledger guard, not in discovering duplicate timeline IDs (`LOG.md:365-368`). R35 supplies the positive pair: Tarin and Sella event IDs and the two `place_id` pointers (`.shokunin/lore/corpus/fixtures/r35-bell7-conflict/timeline.json:20-46`; `contradictions.json:1-9`).

Risks: duplicate rows generate independent downstream checks (citations, occupancy, dependencies); any extra messages must be inventoried, not conflated with the endpoint cardinality result. Duplicate ID does not establish two real actors, two true events, or which row should be selected. Tarin's event place is his reported observation scene, not proof he occupies Sella's place (`r35-bell7-conflict/contradictions.json:9`). The checker reads JSON, not source excerpts or ledger prose (`check_bible.py:18-27,275-288`); a valid pointer is not semantic validation. Neither duplicate identity nor a clean control proves a testimony false/true, chooses canon, or resolves source reliability. In particular, endpoint ambiguity does not invalidate the accounts as narrative testimony; it means this ledger assertion cannot identify a unique event row.

## Falsifiable check

Run both commands above and retain stdout/stderr/exit. The claim is falsified if unique control is not clean; if candidate lacks both a duplicate-timeline-ID finding and the ledger-local exactly-one finding for `claim_a`; if the checker resolves the duplicated pointer by array order; or if any candidate findings are omitted from the report. Confirm the other ledger endpoint remains independently assessed, and inspect the full diagnostics for collateral changes. Separately compare all 88 prior fixture CLI tuples and 439 prior JSON paths byte-for-byte against the declared baseline (`LOG.md:366-368`); any delta must be specifically explained, not waved away. This is coverage of an ambiguous ledger endpoint only: no source-text falsity, testimony erasure, or canon resolution follows.
