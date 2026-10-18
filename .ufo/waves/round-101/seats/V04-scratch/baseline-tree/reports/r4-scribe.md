# Round 4 scribe — proposed decision-table wording

## Observed scope

The round-4 claim in `.shokunin/lore/LOG.md` is an exact, case-sensitive duplicate display-name check across entities with distinct IDs. It explicitly excludes case folding, aliases, transliteration, and any assertion that duplicate names cannot occur in canon. In `.shokunin/lore/corpus/fixtures/check_bible.py`, entity records require a nonempty string `name`; `index('entities')` diagnoses repeated IDs, while no current pass compares display names. The sample names and their `first_appearance` source IDs are in `.shokunin/lore/corpus/fixtures/consistent/entities.json`; the fixture README describes citations as in-world records, not proof of truth.

## Suggested decision-table rows

| Input condition | Decision / output | Evidence and boundary |
|---|---|---|
| Two otherwise valid entity records have different `id` values and exactly equal `name` strings | Report a name-collision violation identifying both entity locations, IDs, and the shared name. Preserve both records and IDs; do not merge, rename, or select canon. | Positive duplicate-name fixture to be added for this round; baseline clean example is `corpus/fixtures/consistent/entities.json`. |
| Entity names differ by case or spelling (for example, `Mira` and `mira`) | No finding under this exact-match rule. | Exact string equality only; no case folding, normalization, transliteration, or fuzzy matching. |
| Repeated entity ID, missing/invalid name, or invalid entity record | Leave to existing ID/schema diagnostics; do not count the record as a distinct-ID name-collision pair. | `corpus/fixtures/check_bible.py` already reports duplicate entity IDs and required-field errors. Do not broaden this round's claim to define how malformed records affect name indexing. |
| A duplicate name has different first-appearance citations, or shares the same citation | The collision rule still reports the exact duplicate; it does not decide whether the sources establish identity, intentional homonymy, or a canon contradiction. | `first_appearance` is required and checked for source resolution, but the checker does not assess source meaning or name-specific support. |

## Recommendation and limits

Keep the check purely diagnostic and limited to exact equality among distinct entity IDs. Do not add a disambiguation field in this round: the round-4 claim makes no such field necessary, and an unvalidated override would weaken the narrow rule. If a later design adds one, document its schema and require an in-world source citation rather than treating it as silent conflict resolution.

The new paired fixtures should demonstrate one exact duplicate across distinct IDs (violation) and one clean comparison (no violation), then replay the pre-existing clean and contradictory cases to show prior outcomes remain. This tests the stated coverage move; it does not establish that duplicate names are invalid in the fictional canon, cover aliases or Unicode normalization, or measure source reliability. Any positive-case names and sources are invented fixture data, not claims about real-world naming conventions.
