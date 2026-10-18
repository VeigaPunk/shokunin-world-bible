# Round 43 independent verifier

## Baseline replay

Pinned baseline: `e810eb0bd6a7019502c6172feed0520db4a58048`. I checked out that commit in a separate detached Git worktree at `/tmp/lore-r43-base`; the candidate root is the current `lore` worktree. The baseline contains **94 fixture directories and 469 fixture JSON paths**. For each baseline fixture, I ran the identical root-relative command from each root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

All 94 baseline replays had byte-identical raw stdout, byte-identical raw stderr, and identical exit status across roots (94/94). All 469 baseline JSON files are present and byte-identical in the candidate; the checker file bytes also match. The candidate adds one fixture directory, `r43-jorin-vela-sighting`, containing five JSON files, so total candidate inventory is 95 directories / 474 JSON paths. No baseline JSON path was removed or changed.

## r41-to-r43 fixture comparison

Compared `r41-vela-direct-bell` from the pinned baseline to `r43-jorin-vela-sighting` from the candidate. The r41 fixture has 12 files; r43 has 14. Every inherited markdown file is byte-identical. The only two added files are `jorin-note-excerpt.md` and `jorin-clause-map.md`. `relations.json` and `contradictions.json` are byte-identical, so no relationship or contradiction-ledger row was appended. In `sources.json`, `entities.json`, and `timeline.json`, the full r41 arrays are exact value prefixes; each has exactly one appended Jorin row (`jorin-note`, `jorin`, and `jorin-vela-sighting`, respectively). Thus the modification is limited to the claimed source/entity/timeline additions plus the two markdown additions. This comparison does not treat checker cleanliness as source truth.

## Target checker calls

Ran the two target calls independently with the same argv, once from each respective root:

| Root / fixture | stdout bytes | stderr bytes | exit |
|---|---|---|---:|
| baseline / `r41-vela-direct-bell` | `CLEAN: schema, citations, relations, timeline; 0 violations\n` | empty | 0 |
| candidate / `r43-jorin-vela-sighting` | `CLEAN: schema, citations, relations, timeline; 0 violations\n` | empty | 0 |

These are structural checker results only; they establish neither source authenticity nor factual truth, shared occasion, chronology, canon, or absence of an event.

No source files or fixtures were edited by this verifier. This report is the sole file written.
