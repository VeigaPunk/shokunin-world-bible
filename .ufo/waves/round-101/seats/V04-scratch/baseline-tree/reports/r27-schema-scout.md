# Round 27 schema scout — admitted entity constraints

## Evidence and scope

- The round targets one combined relation case: a single `relations[0]` whose `from` and `to` each name a duplicated admitted entity ID, compared with a target-only duplicate control (`.shokunin/lore/LOG.md:405-406`). This is structural diagnostic coverage only; it does not establish relation truth or entity identity.
- The schema admits a relation only when all required fields have their exact declared types and nonblank string values; admitted rows enter `data[section]` (`.shokunin/lore/corpus/fixtures/check_bible.py:8-14,31-43`, as at baseline `afe5ed5`). Thus malformed entity rows are not included in `entity_id_counts`; the ambiguity rule concerns schema-valid records, not every raw JSON occurrence.
- Entity ID counting increments once per admitted entity row (`check_bible.py:119-121`). Duplicate diagnostics are emitted by `index('entities')` for each later occurrence (`check_bible.py:45-51,57-59`).
- For each admitted relation, the checker visits both endpoint fields independently and emits either dangling or ambiguous at that endpoint (`check_bible.py:123-130`). If both IDs are duplicated, code shape predicts two endpoint-local ambiguity diagnostics in addition to entity duplicate-ID diagnostics. This has not been empirically replayed; the LOG explicitly says the simultaneous case lacks non-author replay (`LOG.md:405`).
- The later alliance rule skips relations if either endpoint ID is ambiguous (`check_bible.py:210-218`). The relation row is not removed or resolved; endpoint diagnostics remain the evidence of ambiguity.

## Risks / limits

- The dict returned by `index` is last-wins (`check_bible.py:45-51`), so an endpoint present in it is not itself evidence of uniqueness. The relation loop's independent count guard is essential. Do not characterize duplicate rows as selected or their relationship as canonical.
- Duplicate diagnostics depend on schema admission: an invalid duplicate-looking entity row does not increment the admitted count (`check_bible.py:31-43,119-121`). Avoid claims about raw-file duplicate counts.
- A both-duplicated relation may produce additional findings from other consumers if it is `allied_with`; use a non-alliance relation type and unique source ID to isolate the pair. No truth, directionality, or source-text support follows from this structural test.
- Error ordering follows checker iteration: entity duplicate-ID findings occur during indexing, then relation endpoint checks iterate `from` before `to` (`check_bible.py:45-51,123-130`). Tests should assert required diagnostic presence/count rather than accidentally treat order as semantics.

## Proposed coverage test

Use a clean-control-derived pair with one unchanged relation `mira -> seal`, a unique source ID, and a non-alliance relation type. In both fixtures add a second schema-valid entity row for `seal`; in the both case additionally add a second schema-valid `mira` row. Assert target-only has exactly one `relations[0].to: ambiguous entity 'seal'` and no `relations[0].from` ambiguity; both case has exactly one ambiguity at each endpoint, plus the expected duplicate entity-ID findings. Keep relation bytes otherwise identical and ensure unique IDs/control fixture is clean. Replay all prior fixtures and compare their stdout/exit markers and JSON path bytes against baseline, as the LOG requires (`LOG.md:406`). This proposes a test only; no canon or relation-truth assertion.
