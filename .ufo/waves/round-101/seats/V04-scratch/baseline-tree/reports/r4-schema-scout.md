# Round 4 schema scout: malformed and duplicate entity IDs

## Observed behavior

Inspected `.shokunin/lore/corpus/fixtures/check_bible.py` and replayed temporary copies of `.shokunin/lore/corpus/fixtures/consistent/` (no fixture files were changed).

- Each entity row is first checked against `FIELDS['entities']`: `id`, `kind`, `name`, `first_appearance`, and `claims` must have required types; strings must be nonempty after `.strip()`. A row failing any required-field check is omitted from `data['entities']`, so downstream entity indexing/name checks do not see it. Extra fields are accepted. The check does not normalize IDs or names; comparisons are raw, case-sensitive strings.
- `index('entities')` emits `entities[i].id: duplicate entities id ...` for a repeated valid ID, but then unconditionally assigns `result[id] = row`. Thus the last valid row wins in the entity lookup; the duplicate is not discarded and remains in `data['entities']`. Downstream reference/kind checks can consequently observe the last row. A temporary duplicate `mira` row with a different name produced only the duplicate-ID diagnostic; same name likewise produced only duplicate-ID. This is not an ambiguity-safe index.
- The existing alliance check separately counts IDs over valid entity rows (`entity_id_counts`) and explicitly skips a pair if either endpoint ID occurs other than once, before checking faction kinds. This is a local precedent for not making a semantic decision using an ambiguous duplicate ID. Other passes (relations and timeline) use the last-wins `entities` index and do not make that duplicate-count exclusion.
- Temporary duplicate distinct ID `mira-2` with the same name `Mira` produced no current violation: no duplicate-name rule exists yet. A missing `name` row was excluded from the index and yielded the required-name error plus dangling-reference errors for references to its now-absent ID. This shows malformed rows can create secondary diagnostics; those do not repair the schema error.

Relevant exact paths: `.shokunin/lore/corpus/fixtures/check_bible.py` (`FIELDS`, `check`, nested `index`, alliance `entity_id_counts`); `.shokunin/lore/corpus/fixtures/consistent/entities.json`, `relations.json`, and `timeline.json` (baseline rows/references).

## Recommendations (separate from observations)

1. **For the round-4 exact-name rule, skip any entity whose ID is not unique among schema-valid entity rows.** Only compare names for IDs with count exactly one. Emit the already-existing duplicate-ID error as the actionable diagnosis; do not report a name collision from an ID group whose canonical record is ambiguous. This mirrors the explicit exclusion in the alliance pass and prevents a secondary name result from depending on arbitrary row choice. Preserve the duplicate-ID diagnostic.
2. Compare names exactly and case-sensitively as the round-4 claim specifies; do not trim/normalize beyond the existing nonempty-string validation. Treat only schema-valid rows as candidates. Do not infer aliases or let a collision resolve/merge records.
3. If the implementation instead compares all valid rows (including duplicated IDs), document that it may produce redundant or misleading name diagnostics alongside the duplicate-ID finding. In particular, duplicate-ID rows with different names are not evidence of two unambiguous entities sharing a name.
4. Keep in mind the existing checker has inconsistent duplicate-ID handling across checks: the index is last-wins, whereas alliance reciprocity protects itself with a count. A broader rework of index semantics is outside this round's narrow claim; avoid silently changing those existing behaviors here.

## Probe limits

Probes used only temporary copies of the clean fixture and direct `check()` calls. They establish current code behavior for required-field failure and duplicate entity IDs, not every malformed JSON/type case. No claim is made about intended lore semantics beyond the stated round-4 exact-name rule.
