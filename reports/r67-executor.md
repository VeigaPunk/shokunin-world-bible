# Round 67 executor — nonempty claim citation field

## Change

- In `corpus/fixtures/check_bible.py`, the existing entity-claim structural guard now rejects `source_id` strings whose `.strip()` is empty. It retains the existing `expected nonempty statement and source_id` location/message, and calls source membership resolution only for nonblank IDs.
- Added five matched fixtures: unavailable-index control, empty ID, whitespace ID; loaded-index empty-ID negative and nonempty clean control. The four-table unavailable fixtures share every file except the claim `source_id`; their `sources.json` is absent. Loaded pair is copied from `consistent/` except the claim source ID.
- Added a concise Round 67 README subsection documenting required field presence versus index lookup and the evidentiary boundary.

## Raw checker replay

Commands were run from repository root with:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>
```

All runs had empty stderr. Raw exit status and stdout:

- `r67-claim-source-unavailable-control` — exit **1**:
  ```text
  VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: '.shokunin/lore/corpus/fixtures/r67-claim-source-unavailable-control/sources.json'
  1 violation(s); no canon changed
  ```
- `r67-claim-source-unavailable-empty` — exit **1**:
  ```text
  VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: '.shokunin/lore/corpus/fixtures/r67-claim-source-unavailable-empty/sources.json'
  VIOLATION: entities[0].claims[0]: expected nonempty statement and source_id
  2 violation(s); no canon changed
  ```
- `r67-claim-source-unavailable-whitespace` — exit **1**:
  ```text
  VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: '.shokunin/lore/corpus/fixtures/r67-claim-source-unavailable-whitespace/sources.json'
  VIOLATION: entities[0].claims[0]: expected nonempty statement and source_id
  2 violation(s); no canon changed
  ```
- `r67-claim-source-loaded-empty` — exit **1**:
  ```text
  VIOLATION: entities[0].claims[0]: expected nonempty statement and source_id
  1 violation(s); no canon changed
  ```
- `r67-claim-source-loaded-control` — exit **0**:
  ```text
  CLEAN: schema, citations, relations, timeline; 0 violations
  ```

The unavailable control retains only the loader diagnostic; empty and whitespace values add the structural claim finding. No `unknown in-world source` conclusion is emitted for an empty ID, and no result here establishes source membership, source-text support, fictional-world evidence/absence, truth, canon, or rights. This is executor replay only; no claim of full-corpus independent regression verification or axis admission.

No commit, push, or merge.
