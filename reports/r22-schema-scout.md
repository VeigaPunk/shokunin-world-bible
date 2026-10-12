# Round 22 schema scout — dependency member types and safety

## Raw observation (baseline `cc92ece` checker source)

The timeline required-field screen uses exact `type(row[field]) is expected` checks. `depends_on` must therefore be a Python `list` (JSON array); a non-list outer value, missing field, or row with any other invalid required field is diagnosed and excluded from `data["timeline"]`, so it never reaches dependency traversal. Each admitted row has a nonempty string `id` and a list-valued `depends_on`, but the schema screen does not validate the list's members.

At traversal, `all(isinstance(dep, str) for dep in row['depends_on'])` is the sole member screen. If even one member is non-string, the checker adds exactly one `...depends_on: expected event-id strings` error and immediately `continue`s. It does not inspect any member in that row. Consequently a string sibling's self, repeated, unknown, ambiguous, or inversion condition is masked too. This path does not establish that the bad member is satisfied or absent.

If every member is a string, traversal is safe for the subsequent `seen_dependencies` set, `event_id_counts.get(dep, 0)`, and `events[dep]` lookup: strings are hashable, and unknown/duplicate IDs are checked before event lookup. The self check runs for every occurrence before duplicate handling. The first occurrence is looked up; a later occurrence emits repeated-dependency and does not repeat the ID lookup/inversion test. A self edge can additionally be repeated if it recurs.

JSON permits array elements of null, boolean, number, string, array, or object. All except strings fail `isinstance(dep, str)`. In particular, nested JSON arrays and objects decode as Python `list` and `dict`, which are unhashable. Under the current list-wide guard they cannot reach `set.add`, `.get`, or key access, so the current branch is safe from unhashable-key exceptions. Processing an unfiltered dict/list with existing lookups would raise `TypeError`; a safe partial-recovery implementation must type-filter each member before *any* set membership/addition or dictionary lookup. `bool`/numbers are hashable but still invalid IDs and must not be treated as IDs.

## Recommendation (not an observed result)

If adopting the declared round-22 per-string recovery, retain one list-level malformed-member diagnostic, then skip each non-string member before all ID comparisons/set/dictionary operations while traversing string members in original order. Preserve existing string behavior (including self-before-dedup and first-occurrence lookup) and do not coerce invalid values to strings. This is a control-flow recommendation only; it does not demonstrate a coverage gain, calibration safety, or canon/source-text chronology. Raw paired CLI and saved-output replay remain necessary evidence for those claims.
