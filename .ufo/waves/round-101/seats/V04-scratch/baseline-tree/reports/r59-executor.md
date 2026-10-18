# Round 59 executor — parser-boundary candidate

## Scope and implementation

Changed only the checker, four new fixture directories, fixture README, and this report. The loader passes `unique_object` as `json.loads(..., object_pairs_hook=...)`. Every JSON object at every nesting level is checked; a repeat raises `DuplicateMemberError` and the owning table is set to `[]`, matching the existing unloadable-file handling. The diagnostic is stable and file-level: `duplicate object member '<name>'; cannot load JSON`. No row/index/path is fabricated. Syntax errors retain the pre-existing `cannot load JSON: ...` path. This is a candidate parser policy, not a statement about story facts or what duplicate names mean in an upstream producer.

## Candidate fixture inventory and outputs

Each new directory contains exactly five JSON tables (`sources.json`, `entities.json`, `relations.json`, `timeline.json`, `contradictions.json`), cloned from `consistent/`, with the indicated mutation only:

- `r59-duplicate-harbor-tower/`: timeline arrival tick changed to 1, dependencies emptied, duplicate `place_id` ordered harbor then tower.
- `r59-duplicate-tower-harbor/`: same changes, duplicate order tower then harbor.
- `r59-unique-control/`: originally byte-copy of the five consistent tables, single tower choice. **Parent integration before non-author review:** corrected this control to the same arrival tick 1 and empty dependency list as both duplicate variants, retaining one `place_id: tower`. Its current double-booked output was rerun below; the original executor description and raw CLEAN output were for the prior different-tick control, not the current fixture state.
- `r59-nested-duplicate/`: duplicate nested `claims[].source_id` in `entities.json`; other four tables unchanged.

Ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<name>` from repository root. Exact stdout and exit status (stderr empty in each run):

```text
r59-duplicate-harbor-tower (1):
VIOLATION: timeline.json: duplicate object member 'place_id'; cannot load JSON
1 violation(s); no canon changed

r59-duplicate-tower-harbor (1):
VIOLATION: timeline.json: duplicate object member 'place_id'; cannot load JSON
1 violation(s); no canon changed

r59-unique-control (0):
CLEAN: schema, citations, relations, timeline; 0 violations

r59-nested-duplicate (1):
VIOLATION: entities.json: duplicate object member 'source_id'; cannot load JSON
VIOLATION: relations[0].from: dangling entity 'mira'
VIOLATION: relations[0].to: dangling entity 'seal'
VIOLATION: timeline[0].entity_id: dangling entity 'mira'
VIOLATION: timeline[0].place_id: dangling entity 'harbor'
VIOLATION: timeline[1].entity_id: dangling entity 'mira'
VIOLATION: timeline[1].place_id: dangling entity 'tower'
7 violation(s); no canon changed
```

The nested probe demonstrates an explicit cost of unloading a whole table: independent cross-file checks cascade. These dangling messages reflect no loaded entity rows, not world absence. The two target duplicates no longer produce an occupancy choice; the unique control remains clean.

## Old checker and regression limits

Pre-candidate current checker behavior was directly observed by r59 scouts on temporary copies: with arrival tick 1 and `depends_on=[]`, duplicate harbor-then-tower exited 1 with a `double-booked` finding; tower-then-harbor exited 0 CLEAN. The parent LOG records this pair. The regression scout reports zero duplicate-member files among the 474 active fixture JSON files and baseline 95 fixture directories. The existing r5 matrix covers missing file, invalid syntax, wrong top-level type, row shape, and invalid citation, but not duplicate object members; parser wording/offsets were not treated as portable.

I did **not** run the pinned 95-case raw stdout/stderr/exit replay, nor compare all 474 fixture JSON bytes against a pinned archive. The pinned archive was not found locally during this scoped execution. Therefore preservation of all 95 old tuples is unverified; this report is not an admission verdict. The candidate's likely deltas on any duplicate-bearing external input, and cascades from unloadable tables, remain risks. No other corpus files were changed.

No source text, actual location, canon, rights, or permission is asserted. No commit made.

## Parent integration correction (after executor)

The equal-tick unique control now retains the single `tower` place and correctly exits **1** with `VIOLATION: timeline[1]: double-booked 'mira' at tick 1 in timeline[0] ('harbor') and 'tower'` followed by `1 violation(s); no canon changed`. The original CLEAN output above was observed **before** the control correction and must not be read as current. README now describes the matched control. No candidate-old 95-case replay is claimed by this report.
