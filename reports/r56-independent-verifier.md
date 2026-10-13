# Round 56 independent verifier

## Method and results

Pinned the r55 baseline at `0170e88e7706f77a10348c9896bdb9913ff4c490` in a separate detached worktree (`/tmp/r55-archive-13ynqk7f`). Used identical argv from each repository root for each of the 95 baseline fixture directories: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>`. Compared raw stdout bytes, stderr bytes, and exit status. All **95/95 tuples match exactly**, including failures.

All **474/474** old fixture JSON files are byte-identical (230,650 bytes in each corpus). Baseline checker vs current checker has an exact **two-line** unified diff, both insertions:

```diff
@@ -176,0 +177 @@
+                errors.append(f'{record_label}.to_holder: ambiguous entity {to_holder!r}')
@@ -184,0 +186 @@
+                    errors.append(f'{record_label}.from_holder: ambiguous entity {from_holder!r}')
```

Corpus inventory by relative path and file size: exactly `README.md` and `check_bible.py` are changed (50,234→51,139 bytes; 14,845→15,035 bytes), and the only new paths are the five expected JSON files under `r56-holder-ambiguous/` (`sources`, `entities`, `relations`, `timeline`, `contradictions`). No old paths are missing and no other additions/changes were found.

## New behavior checks

Current `r56-holder-ambiguous` command exits 1 and emits exactly:

```text
VIOLATION: entities[4].id: duplicate entities id 'harbor'
VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'harbor'
VIOLATION: entities[3].provenance[2].from_holder: ambiguous entity 'harbor'
VIOLATION: timeline[0].place_id: ambiguous place entity 'harbor'
4 violation(s); no canon changed
```

Current and baseline `item-chain-valid` each exit 0 with identical raw stdout (`CLEAN: schema, citations, relations, timeline; 0 violations\n`) and empty stderr. Its holder chain remains clean; no suppression or chain-wide claim was observed. The ambiguous fixture demonstrates the two new ambiguous-holder diagnostics alongside duplicate-ID and ambiguous-place diagnostics; it does not establish broader provenance/canon semantics.

No files other than this report were written by this verifier in the repository; no commit made.
