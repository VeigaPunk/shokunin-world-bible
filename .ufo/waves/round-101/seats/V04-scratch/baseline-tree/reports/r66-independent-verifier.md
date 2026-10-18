# r66 independent verifier report

## Pinned archive preservation

Pinned r65 report commit `b5d370b571e406a7befe2d98718eb665fcf3c977` was extracted separately to `/tmp/r66-archive`. Compared the complete `.shokunin/lore/corpus` manifest by repo-relative path and raw bytes: **1,298/1,298 paths match**, with no additions, removals, or byte differences. The pinned corpus contains **623 fixture JSON files** and **125 fixture directories**. Using the same repo-root-relative argv for each directory (`python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<directory>`), compared raw stdout bytes, stderr bytes, and exit status from both roots: **125/125 tuples identical**, zero mismatches.

## Current nested-duplicate behavior

Ran the current checker on `r59-nested-duplicate` with repo-root-relative argv. Exit 1, stderr empty:

```text
VIOLATION: entities.json: duplicate object member 'source_id'; cannot load JSON
1 violation(s); no canon changed
```

The historical r59 independent-verifier report records **7 findings** for this probe under the r59 executor: one duplicate-member load finding followed by six dangling-reference findings because unloading the entities table leaves dependent references unresolved. This is a historical report, not current output. The current checker instead produces one load finding; no candidate replay was performed.

The historical r59 executor commit `9e2887a` contains the same duplicate-unloading policy. Running that archived checker on the fixture directly from `/tmp` reproduced the historical 7-finding output, but that temporary absolute-path invocation is not a current-checker replay and does not establish current behavior; the 7-finding record above is attributed to the historical r59 report.

## Scope

No README candidate exists, so no candidate replay or candidate comparison was performed. No corpus or other repository files were changed by this verification; this report is the sole intended output. These checks make no canon, source-authority, or rights claim.
