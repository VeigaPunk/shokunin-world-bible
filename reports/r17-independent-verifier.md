# Round 17 independent verifier (non-author)

## Scope and integrity

I independently checked the candidate at HEAD `1dd6f27ae89a096c8fb99d2750f35e5118fda5d3` (baseline commit; working tree candidate). I did not edit source code or fixture JSON and did not commit. Before/after SHA-256 checks were made over all fixture JSON present initially (194 files, including the 30 files across six r17 cases) and the checker. All 194 JSON hashes and the checker hash were unchanged during this verification; no fixture JSON was added or deleted by me. The six r17 directories each contain the five standard JSON files.

The baseline commit contains **33** fixture directories and **164** JSON files. For each baseline JSON path, `git show 1dd6f27:<path>` matched the working-tree bytes: **164/164 byte-identical**. The baseline checker was run from the commit bytes extracted with `git show` (SHA-256 `bf2061b5c6f4e5f67f6c6f8dfbe31b0141c9541e259fe4ddf333aebef92b19b6`) against all 33 directories. Baseline-checker and current-checker results matched **33/33** in stdout, stderr, and exit code. The current checker also matched the saved `20261012T184609Z` transcript for **all 39** fixture outputs (33 baseline + six r17): exact stdout, empty stderr, exact exit status.

## Paired fixture review

Inspected the full JSON tables for all six r17 fixture directories. Each has a unique `mira` character and unique `harbor`/`tower` places; timeline rows are tick 7, actor `mira`, source ID `courier-log`, and descriptions explicitly scoped to fixture input without claiming source-text support. The core paired fixtures `r17-valid-places` and `r17-wrong-after` differ in exactly one location: only `timeline[1].place_id` changes from `tower` to `mira`; byte-level unified diff of the five JSON files showed only that one value differs. The wrong-kind ID is indeed uniquely indexed as a character, not a place.

Saved outputs and fresh current replay agree. Valid pair yields a `double-booked` harbor/tower finding. Wrong-after retains `not a place 'mira'` and withholds the occupancy finding. `r17-wrong-before` likewise retains only `not a place`. In three-row cases, wrong-first, wrong-middle, and wrong-last each retain the wrong-kind diagnostic and the distinct known harbor/tower double-booked finding. This demonstrates those three tested input orders, not arbitrary ordering or pairwise completeness.

## Requested unchanged controls

- Duplicate-place-ID probe: added a second `harbor` entity row of kind `character` to an isolated temporary copy of `r17-valid-places`; the checker reported duplicate entity ID, ambiguous place entity, and still the raw-ID harbor/tower `double-booked` finding. This behavior is unchanged by the new guard (`place_id_count == 2` remains eligible); it is an ambiguous-ID limitation, not validated location evidence.
- Wrong-kind order control: the two-event `r17-wrong-before` case (wrong-kind first, valid tower second) reports `not a place` and no occupancy conflict, complementing wrong-after; wrong-first/middle/last three-row controls preserve the known place pair as above.

## Limits

This verifies inputs, checker output, and byte identity only. A unique ID/kind index and a citation ID do not establish what fictional source text says, actual location, canon, or whether an unreported conflict exists. The duplicate-place probe intentionally shows ambiguous IDs can still enter raw-ID occupancy comparison. The tested pair/order cases are finite examples, not proof of general soundness, real-world fact, or game mechanics. `r11-unique-nonplace` is a pre-existing fixture with misleading description and was not used as evidence or changed.

**Verifier result:** requested baseline integrity and output replays pass; paired and ordering evidence is consistent with the narrowly stated round-17 behavior.
