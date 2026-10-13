# Round 83 independent verifier — final candidate state

## Pin and method

I independently archived baseline `e9324f6e4657ad2cdddbe3f38e4749d51cc30cb1` with `git archive` into `/tmp/r83-independent-e9324f6/.shokunin/lore/corpus`. I compared file paths and raw bytes against the current worktree and ran each fixture checker from both the archive root and repository root. Commands were root-relative and stdout/stderr were captured separately as bytes; no normalization was applied. This report is the only file I created.

## Prior corpus preservation

The archived baseline contains 1,356 corpus files. Every baseline path remains in the worktree. The only changed prior corpus file is the declared `fixtures/README.md` addition for Round 83; its other prior content is retained with the new entry appended. All other 1,355 prior corpus paths are byte-identical. The sole 12 added corpus paths are the files in `fixtures/r83-vela-joint-nonsighting/`; there are no other added corpus paths. The active checker is byte-identical to the pin, SHA-256 `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`.

I independently replayed all 132 baseline fixtures. Their exact `(exit status, stdout bytes, stderr bytes)` tuples match archive-to-worktree for **132/132**: 27 exit 0 and 105 exit 1, with no mismatches. The compact JSON tuple ledger SHA-256 is `bdd1ed6253070e583b3631fd52d9af71ae6a05f85b83ea60474d707f442f8f7e`.

## Candidate clone and raw checker tuples

The r83 fixture has 12 files: the 11 r40 files plus `scope-contrast-map.md`. Comparing inherited paths against r40 shows only two byte changes: `vela-note-excerpt.md` and `vela-clause-map.md`. The five JSON files (`sources.json`, `entities.json`, `relations.json`, `timeline.json`, `contradictions.json`) are byte-identical to r40, as are all other inherited files. The candidate README entry says the same.

The reviewer flagged a stale r40 heading in the cloned clause map. The parent corrected it to `# Clause map — r83 Vela joint non-sighting report` before the candidate bytes and checker tuples below were captured; this report verifies the corrected final worktree bytes, not the pre-correction state.

From repository root, separately captured raw CLI results for

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r40-vela-listener
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r83-vela-joint-nonsighting
```

are:

| Fixture | Exit | stdout bytes (UTF-8 display) | stderr bytes |
|---|---:|---|---|
| r40 | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations\n` | empty |
| r83 | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations\n` | empty |

Thus checker output is structurally identical; it does not establish prose support or semantic correctness.

## Git scope and limits

At inspection, the only tracked modifications were `.shokunin/lore/LOG.md` and `.shokunin/lore/corpus/fixtures/README.md`. Untracked work consisted of the declared Round 83 report set and the r83 fixture directory; no checker, config, or unrelated project paths appeared. The log is the declared Round 83 coordination artifact, not part of my edits. I made no other file edits and did not commit, push, merge, or spawn agents.

The excerpt and records are authored fiction and unverified. Byte preservation, fixture replay, and checker CLEAN establish neither source authenticity nor truth, fictional-world canon, real-world rights, or game mechanics. The unchanged JSON/parity also cannot decide whether the altered prose is adequately supported; this is preservation and structural evidence only, not an axis verdict.
