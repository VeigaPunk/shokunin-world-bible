# Round 60 independent verifier report

## Pinned baseline and preservation

Archived commit `d76619452cea837eeb95b1196683b29175b0c98a` to `/tmp/lore-r59-pin`. Ran all **99** baseline fixture directories twice, once with the archived checker and once with the working-tree checker, using identical root-relative argv: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<directory>`. Compared raw `(stdout bytes, stderr bytes, exit status)` tuples. **98/99 were identical.** The sole changed old output was:

- `r59-nested-duplicate`: archived checker: exit 1, stderr empty, stdout had the duplicate `entities.json` member `source_id` load violation, six dangling-reference diagnostics (`relations[0].from` mira, `.to` seal, `timeline[0].entity_id` mira, `.place_id` harbor, `timeline[1].entity_id` mira, `.place_id` tower), then `7 violation(s); no canon changed`. Working checker: exit 1, stderr empty, stdout had the same duplicate-member load violation followed immediately by `1 violation(s); no canon changed`. Thus the only removed old diagnostics are the six dangling-reference lines and the count changes 7→1.

Archived corpus has **494 JSON files**. Every old JSON path remains present and byte-identical; zero changed or removed. The full old fixture tree differs only at `check_bible.py` and `README.md` (both changed). The current tree adds **20 JSON files**: five each in `r60-empty`, `r60-partial`, `r60-unavailable`, and `r60-unavailable-independent`. No conclusions about canon/source authority are made.

## Matched candidate replay

Copied each of the four current `r60-*` candidate directories byte-for-byte into the archived tree (outside tracked worktree), then ran old/current checker against that same copied input with the identical argv above. All have empty stderr and exit 1. The raw stdout text and violation counts:

- `r60-empty`: both emit dangling `relations[0].from` mira, `relations[0].to` seal, `timeline[0].entity_id` mira, `timeline[0].place_id` harbor, `timeline[1].entity_id` mira, `timeline[1].place_id` tower; **6**.
- `r60-partial`: both emit dangling `relations[0].to` seal, `timeline[0].place_id` harbor, `timeline[1].place_id` tower; **3**.
- `r60-unavailable`: archived emits `entities.json: cannot load JSON: Expecting property name enclosed in double quotes: line 1 column 3 (char 2)`, then the six dangling diagnostics listed for `r60-empty`; **7**. Current emits only the same JSON load error; **1**.
- `r60-unavailable-independent`: archived emits that same entities JSON load error, the six dangling diagnostics, `timeline[0].tick: must be nonnegative`, `timeline[1].source_id: unknown in-world source 'absent'`, and `timeline[1].depends_on: unknown event 'missing'`; **10**. Current emits the JSON load error and those last three independent diagnostics, omitting the six dangling diagnostics; **4**.

In each case the terminal summary is `<count> violation(s); no canon changed`. The three fixtures with loaded empty/partial entities and unavailable-independent have identical non-entity diagnostics between checker versions; thus their non-entity table diagnostics are byte-for-byte stable. `r60-unavailable` likewise retains the JSON error and changes only entity-dependent fallout.

## Regression fixtures

Ran the five pinned `r5-*` controls with both checker versions and identical root-relative argv. All ten runs match exactly (exit 1, empty stderr): `r5-missing-file` missing contradictions input (1 violation); `r5-invalid-json` contradictions JSON decode error (1); `r5-wrong-top-level` contradictions expected array (1); `r5-row-shape` contradictions[0] expected object (1); `r5-invalid-citation` unknown source `absent-source` (1).
