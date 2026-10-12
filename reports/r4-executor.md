# Round 4 executor report — exact duplicate display names

Implemented the exact-name review diagnostic in `corpus/fixtures/check_bible.py`. It compares raw, case-sensitive `name` strings among schema-valid entity rows whose IDs each occur exactly once. For a matching name across distinct IDs, it emits one diagnostic naming both `entities[index]` locations, IDs, and the shared display name. It does not mutate, merge, or normalize records. Duplicate-ID groups are skipped by this rule and retain the existing duplicate-ID diagnostic; malformed rows are excluded by existing schema validation. No aliases, disambiguation fields, whitespace trimming, case folding, or Unicode normalization were added.

## Replay evidence

Replayed all pre-existing fixture directories from the repository root:

| Fixture | Exit | Result |
|---|---:|---|
| `consistent` | 0 | Clean; no name finding |
| `contradictions` | 1 | Same three existing findings: dangling endpoint, timeline inversion, double booking |
| `ally-reciprocal` | 0 | Clean |
| `ally-one-way` | 1 | Existing missing reciprocal finding only |
| `contradictions-ledger-malformed` | 1 | Existing malformed ledger pointer plus the same three underlying findings |

Temporary probes copied `consistent` under `/tmp` (no repository fixture changes):

- Added `entities[4]` with ID `mira-2` and exact name `Mira`: exit 1, diagnostic `entities[0] and entities[4] ... 'mira' and 'mira-2'`; no canon changed.
- Added another `mira` ID: exit 1 with the existing duplicate-ID error only; no name diagnostic for the ambiguous ID group.
- Added ID `mira-lower` with name `mira`: exit 0, confirming case-sensitive matching.

The parent is preparing the dedicated positive/negative fixture pair; this report does not claim its replay. The diagnostic identifies a duplicate display string for human review, not shared identity, erroneous canon, or proof names must be unique. No commit made.
