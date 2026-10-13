# Round 27 pair-scout: target-only vs both-endpoint duplicate fixture

## Evidence

- `.shokunin/lore/LOG.md:404-407` declares the coverage axis and asks for a controlled pair: same `mira -> seal` relation, both IDs duplicated in one case versus only `seal` duplicated in control; desired ambiguity paths are `from` and `to` versus `to` only. It also requires prior fixture outcomes and JSON path bytes to remain unchanged.
- `.shokunin/lore/corpus/fixtures/check_bible.py:45-50` counts duplicate IDs in the section index while retaining an entry for the repeated ID; `.shokunin/lore/corpus/fixtures/check_bible.py:118-129` independently checks each relation endpoint against entity ID counts and emits a field-specific ambiguous-entity finding.
- `.shokunin/lore/corpus/fixtures/r25-to-unique/entities.json:1-50` and `r25-to-unique/relations.json:1-8` provide the target-only control pattern; `r25-to-ambiguous/entities.json:1-57` and `r25-to-ambiguous/relations.json:1-8` show the matched control with duplicated `seal` and unchanged relation. Both fixtures keep the same base entities and relation; duplicate entity is appended.

## Proposed paired fixture difference

Use a new matched pair rather than editing existing fixtures. Keep each pair's `relations.json` identical, containing exactly the single existing-shaped `mira -> seal` relation with its same type and source ID. In each `entities.json`, preserve the common baseline rows and append a second row with `id: "seal"` to the target-only control. In the both-endpoint case, additionally append a second row with `id: "mira"`; change no other fields or files. This makes the sole treatment difference the additional duplicate `mira` row. Prefer clone-derived data from the existing r25 target-only fixture, preserving all unrelated fixture files byte-for-byte.

## Proposed test and coverage oracle

Run the existing checker on both new fixture directories. Require the both-duplicate case to contain exactly one `relations[0].from: ambiguous entity 'mira'` and exactly one `relations[0].to: ambiguous entity 'seal'` finding, plus the expected duplicate-ID diagnostics for `mira` and `seal`. Require the target-only control to contain exactly one `relations[0].to: ambiguous entity 'seal'`, no `relations[0].from` ambiguity, and the expected duplicate-ID diagnostic for `seal`. Compare all other prior fixture outputs and their JSON relative-path inventory byte-for-byte with baseline; no checker edit is part of this test.

## Risks / limits

- Adding duplicate rows can trigger duplicate-ID diagnostics and any other checks that inspect entity rows; assert the complete output, not only the two endpoint lines. Repeated claims or kind-specific checks may create noise if the duplicate rows are copied carelessly; use minimal copies consistent with existing entity schema.
- The control must differ only by absence of the extra `mira` row; otherwise findings cannot be attributed to the additional endpoint ambiguity.
- This is a structural coverage test of independently evaluated endpoint fields. It does not establish canon, whether the relation is true, or which duplicate entity is intended. Do not interpret fixture labels or sample prose as a resolution.
