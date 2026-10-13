# r64 independent verifier report

## Pinned regression archive and replay

Independent verifier leaf; no children. Archived pinned r63 report commit `3367b22043c55a2e207ca446b916b462e66a0791` with `git archive` to `/tmp/r64-archive-6g71z9zz`, separately from the working tree. Compared the full `.shokunin/lore/corpus` relative-path inventory and raw bytes: **1,298/1,298 paths present in both; zero added, removed, or changed**. All **623 old fixture JSON paths** were byte-identical. Replayed all **125** immediate fixture directories from archive and working-tree roots using identical repo-root-relative argv: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-dir>`. Compared raw stdout, stderr, and exit status tuples: **0/125 mismatches**. No mismatch paths or fixture names.

## Outside-repository matched probes

Probes used a temporary copy of the current `consistent` fixture (`/tmp/`), invoked from the repository root with `python3 .shokunin/lore/corpus/fixtures/check_bible.py <absolute-temp-dir>`. For each, all other four JSON tables were left byte-for-byte untouched; the entities table was varied. Exact output below is stdout; stderr was empty in every case. Exit status is shown. No candidate checker exists; these are active-checker observations only.

- Valid baseline, ID `mira`: **exit 0**, `CLEAN: schema, citations, relations, timeline; 0 violations`.
- Existing referenced ID `mira`, required name changed to empty string: **exit 1**; `VIOLATION: entities[0].name: required nonempty str`; `VIOLATION: relations[0].from: dangling entity 'mira'`; `VIOLATION: timeline[0].entity_id: dangling entity 'mira'`; `VIOLATION: timeline[1].entity_id: dangling entity 'mira'`; `4 violation(s); no canon changed`.
- Existing referenced ID `mira`, required `name` field missing: same **exit 1** and exact four-violation stdout as the invalid-name case.
- Malformed row with absent ID (`ghost`, empty required name): **exit 1**; `VIOLATION: entities[4].name: required nonempty str`; `1 violation(s); no canon changed`.
- Valid duplicate of ID `mira`: **exit 1**; `VIOLATION: entities[4].id: duplicate entities id 'mira'`; `VIOLATION: relations[0].from: ambiguous entity 'mira'`; `VIOLATION: timeline[0].entity_id: ambiguous actor entity 'mira'`; `VIOLATION: timeline[1].entity_id: ambiguous actor entity 'mira'`; `4 violation(s); no canon changed`.
- Successfully loaded empty entities array: **exit 1**; dangling references reported for both relation endpoints (`mira`, `seal`) and both timeline entity/place pairs (`mira`/`harbor`, `mira`/`tower`); `6 violation(s); no canon changed`.
- Wholly unavailable entities table (malformed JSON `{bad json`): **exit 1**; `VIOLATION: entities.json: cannot load JSON: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)`; `1 violation(s); no canon changed`.

**Repair pointer:** restore a valid entity row for `mira` with all required nonempty/type-correct fields (including `name`) to resolve the demonstrated relation/timeline references. A malformed row is excluded from the usable entity index even if it contains the referenced ID, so those pointers are reported dangling. An absent ID produces no reference-specific diagnostic. A valid duplicate ID instead produces ambiguity diagnostics. Loaded-empty makes the table available and enables dangling-reference checks; wholly unavailable JSON suppresses those checks.

## Scope

This verifies pinned corpus/fixture stability and the listed current-checker outputs only. No candidate replay or candidate comparison was possible. No world/canon conclusion is made.
