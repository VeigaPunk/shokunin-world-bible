## Work performed

Axes: **freeze identity**, **census/receipt parity**, **boundary replay and code anchors**, and **M2 failure-contract behavior**. I checked the committed HEAD separately from the visible worktree candidate; the claimed r92 integration is not at HEAD. I made no tracked-file edits, commit, or push. Scratch copies were under `/tmp` and removed.

## Before → after measurements

**Freeze identity (blocking precondition).** Exact command:

```sh
git log --oneline -3 && git status --short --branch && printf '\nHEAD=' && git rev-parse HEAD && printf '\ntracked_diff_paths:\n' && git diff --name-only HEAD
```

Observed:

```text
396c568 lore r91: closure — verdicts ruled (all improved, bounded; doc harm repaired by deferral), round record
c2ab3d0 lore r91: C3 R8/R10 r91 edge decisions (failed-gate disposition, withhold precedence, source_id namespace) + the r89 paraphrase demo's Inventory line (missed from the work commit)
6332115 lore r91: C1 discriminating fixtures + C9 watch, C2 hardened support command, C3 edge decisions, boundary-doc reconstruction — work wave (33 luna-max seats)
## main...origin/main [ahead 13]
 M corpus/fixtures/README.md
 M corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md
 M corpus/knowledge/holder-assessment-boundary.md
 M corpus/knowledge/r88-sourced-inspiration-decision-table.md
 M corpus/knowledge/r91-c9-watch.md
 M corpus/tools/support_check.py
?? .ufo/waves/poll_wait.sh
?? .ufo/waves/round-92/

HEAD=396c568cbf86bba2c4b7a4ce8bd69fc38bb33d1f

tracked_diff_paths:
corpus/fixtures/README.md
corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md
corpus/knowledge/holder-assessment-boundary.md
corpus/knowledge/r88-sourced-inspiration-decision-table.md
corpus/knowledge/r91-c9-watch.md
corpus/tools/support_check.py
```

**(a) Fixture census vs B1: PASS on HEAD.** Exact command was `PYTHONDONTWRITEBYTECODE=1 python3 -I - <<'PY' ... PY` from `lore-shokunin/`; it sorted direct `corpus/fixtures` directories, ran `python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<name>` for each, computed `{exit, stdout_sha256, violation_count}`, and compared every row to `.ufo/waves/round-92/patches/B1-tuples.json`. The delivered checker's working file hash was also compared with `git show HEAD:corpus/fixtures/check_bible.py`.

Observed:

```text
HEAD=396c568
fixture_dirs=166 B1_rows=166
exit_counts={0: 32, 1: 134} violation_lines=421
stderr_nonempty=0
checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 head_checker_equal=True
missing=0 extra=0 tuple_mismatches=0
mismatch_paths=[]
```

**(b) Support receipts: FAIL on HEAD; PASS on worktree candidate.** For HEAD, the exact snapshot was made with `git archive --format=tar HEAD corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r89-inspiration-paraphrase | tar -xf - -C <scratch>`. In that scratch root, ran:

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase
```

HEAD observed summary lines:

```text
r87: INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22
     SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); RESULT PASS; exit=0
r88: INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 0/0; TOTAL-ROWS 10/10; DISTINCT-ANCHORS 6/6
     WARN: unreferenced excerpt declaration: source-excerpt.md (mode=verbatim)
     RESULT PASS WITH WARNINGS; exit=0
paraphrase: INVENTORY JSON-FACTS 1/1; EDITORIAL-ROWS 0/0; TOTAL-ROWS 1/1; DISTINCT-ANCHORS 1/1
            SOURCE-SUPPORT 0/0; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); RESULT PASS; exit=0
scratch_cleaned=true
```

The same exact CLI commands from the checkout root against the visible worktree candidate produced:

```text
$ python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS

$ python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12; DISTINCT-ANCHORS 8/8
RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12
SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 12/12; VALIDATED-ROWS 12/12
RESULT PASS

$ python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase
INVENTORY JSON-FACTS 1/1; EDITORIAL-ROWS 0/0; TOTAL-ROWS 1/1; DISTINCT-ANCHORS 1/1
RECEIPT JSON-FACTS 1; EDITORIAL-ROWS 0; TOTAL-ROWS 1
SOURCE-SUPPORT 0/0; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1; VALIDATED-ROWS 1/1
RESULT PASS
```

Thus the intended worktree state has all three requested receipts, but it is not the current HEAD.

**(c) Boundary replay and anchors: FAIL as a freeze check.** The current HEAD document is the old 549-line baseline, not the r92 re-derivation. The visible worktree target is 413 lines and has an odd number of Markdown fence markers (`3`), with no receipt block for any of the six requested cases. Exact snapshot/receipt scan observed:

```text
HEAD_doc_lines=549 fenced_blocks=7
HEAD receipt wrappers present: r85-masked-ambiguous=yes; r85-isolated-ambiguous=yes; r85-harbor-repro=yes; r90-c1-three-causes=no; r89-fn2-unresolved-chain-break=yes; r89-fn2-control=yes
worktree_doc_lines=413 fenced_blocks=1 fence_markers=3 odd_fence_count=1
worktree receipt wrappers present: all six absent (0/6)
```

I still ran all six exact checker calls from the repo root and compared stdout bytes, exit, and empty stderr to the old HEAD document's r85/FN-2 receipts and the prior r90 F1 receipt. Every runtime comparison matched, but the r90 receipt is in `.ufo/waves/round-90/F1.md`, not in the boundary document, and none of these receipts is in the current worktree target:

```sh
python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous
```

```text
VIOLATION: entities[5].id: duplicate entities id 'vault'
VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'vault'
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'vault' at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'vault' at entities[3].provenance[1]
4 violation(s); no canon changed
exit=1 stderr_bytes=0 exact_match_to_HEAD_receipt=true stdout_sha256=757cc1308914ffe5968464c3e9b3fbffef70b040ba89e5f3b0aa1a4186d489c1
```

```sh
python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/r85-isolated-ambiguous
```

```text
VIOLATION: entities[5].id: duplicate entities id 'vault'
VIOLATION: entities[3].provenance[2].to_holder: ambiguous entity 'vault'
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'vault' at entities[3].provenance[2]
3 violation(s); no canon changed
exit=1 stderr_bytes=0 exact_match_to_HEAD_receipt=true stdout_sha256=3e50866af53011ee465ac9126f37ce098420ba64360a1f5283f13340eb4904ad
```

```sh
python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/r85-harbor-repro
```

```text
VIOLATION: entities[4].id: duplicate entities id 'harbor'
VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'harbor'
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'harbor' at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'harbor' at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2].from_holder: ambiguous entity 'harbor'
VIOLATION: timeline[0].place_id: ambiguous place entity 'harbor'
6 violation(s); no canon changed
exit=1 stderr_bytes=0 exact_match_to_HEAD_receipt=true stdout_sha256=5c5b5955d87f87797c2389ee1ef7dc67f04392fa407521aa0a77b79c6bb6e54d
```

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r90-c1-three-causes
```

```text
VIOLATION: entities[0].provenance[0].tick: required nonnegative integer
VIOLATION: entities[0].provenance[0].to_holder: dangling entity 'r90-c1-three-causes-absent-holder'
VIOLATION: entities[0].provenance[0].source_id: unknown in-world source 'r90-c1-three-causes-absent-source'
VIOLATION: entities[0].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (invalid tick); holder reference to_holder 'r90-c1-three-causes-absent-holder' absent from raw entities and absent from the resolved index; source reference 'r90-c1-three-causes-absent-source' absent from raw sources and absent from the resolved index at entities[0].provenance[0]
4 violation(s); no canon change
exit=1 stderr_bytes=0 exact_match_to_round90_F1_receipt=true stdout_sha256=97723e8fe516a9086834a678a394a7b454ddcb05f87a8a9025149b16bd892148
```

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-fn2-unresolved-chain-break
```

```text
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
2 violation(s); no canon changed
exit=1 stderr_bytes=0 exact_match_to_HEAD_receipt=true stdout_sha256=66ed1438c6d1af003492d29569492ec0990e5b01b041fba1b4e21147eab4327a
```

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-fn2-control
```

```text
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'f3-dup', got 'mira'
1 violation(s); no canon changed
exit=1 stderr_bytes=0 exact_match_to_HEAD_receipt=true stdout_sha256=4283f6955f40d49f6036ad61f55ab94e682cdb3c475af73c3d8350920cf06951
```

**Anchor resolution against the delivered checker.** The checker hash is the required `ff9fd2aa…` and matches HEAD. A targeted content check was run with `PYTHONDONTWRITEBYTECODE=1 python3 -I - <<'PY' ... PY` over the null guard/detail, relation ambiguity, to/from holder ambiguity, tick comparison, qualified chain comparison, and first-record spans. Observed:

```text
null_guard: 169-170 PASS
identity_detail: 171-175 PASS
relation_ambiguity: 184-184 PASS
to_holder_ambiguity: 277-277 PASS
from_holder_ambiguity: 290-290 PASS
tick_integer_comparison: 323-326 PASS
qualified_chain_comparison: 330-335 PASS
first_record_comparison: 339-341 PASS
critical_content_anchors=8/8
```

The old HEAD boundary document's own code-anchor check is **1/2**, not a pass: its explicit historical `5eb9451` span `212-224` resolves in that historical checker, but its unqualified current relation anchor `check_bible.py:182` resolves to AST-derived delivered span `184-184`:

```text
historical_ref=5eb9451:corpus/fixtures/check_bible.py:212-224 derived_span=(212, 224) PASS=True
current_ref=corpus/fixtures/check_bible.py:182 derived_relation_ambiguity_span=[(184, 184)] PASS=False
anchor_result=1/2
```

This is targeted source-content evidence, not a full B3 catalog certification. `tools/certify_boundary_doc.py` is absent.

**(d) M2 failure contract: FAIL on HEAD; PASS on worktree candidate.** On scratch copies of the r87 cluster, checker, and maps, exact candidate commands were:

```sh
/usr/bin/python3 /tmp/lore-r92-SF1-M2-y02ihc9v/worktree/corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster --map /tmp/lore-r92-SF1-M2-y02ihc9v/worktree-missing_inventory.md
/usr/bin/python3 /tmp/lore-r92-SF1-M2-y02ihc9v/worktree/corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster --map /tmp/lore-r92-SF1-M2-y02ihc9v/worktree-map_error.md
```

Observed candidate results:

```text
missing-inventory: exit=1; stdout='RESULT FAIL\n'; stderr='FAIL: map must contain exactly one expected inventory declaration\n'
map-error: exit=2; stdout='RESULT ERROR\n'; stderr='FAIL: map table row has a different number of cells than its header\n'
```

The exact same scratch probes with `git show HEAD:corpus/tools/support_check.py` yielded:

```text
missing-inventory: exit=2; stdout=''; stderr='FAIL: map must contain exactly one expected inventory declaration\n'
map-error: exit=2; stdout=''; stderr='FAIL: map table row has a different number of cells than its header\n'
scratch_cleaned=true
```

## Findings & named debt

- **Freeze failure:** HEAD remains `396c568` (r91 closure), not the claimed r92 WORK integration. Six tracked integration targets are dirty. The current worktree results must not be represented as HEAD verification.
- **PASS:** the pinned 166-directory census exactly matches B1 (zero missing, extra, or changed tuples).
- **FAIL on HEAD / PASS in worktree:** r87 and paraphrase receipts pass on both snapshots; r88-m3 on HEAD is still 10+0 with the unreferenced-excerpt WARN, while the worktree candidate is 10+2 PASS without WARN.
- **FAIL on HEAD/worktree freeze artifact:** the HEAD document is the old version; the dirty worktree document is malformed (one unmatched fence) and contains none of the six requested receipts. The six runtime probes themselves matched their old/external reference outputs. The current HEAD's unqualified relation anchor is stale (`182` vs `184`).
- **FAIL on HEAD / PASS in worktree:** the M2 candidate produces the required exit/RESULT contract on scratch copies; HEAD still produces exit 2 with no terminal RESULT for both tested cases.
- Named debt is integration/commit and a new post-integration boundary replay/certification. No tracked files were changed by SF1.

## Handoff

- Deliverables: `.ufo/waves/round-92/followup/SF1.md` and `.ufo/waves/round-92/followup/SF1-freeze.json`.
- Overall result: **FAIL — the requested r92 freeze is not the current HEAD.** Preserve the integration changes, finish/commit them in the integration seat, then rerun SF1 against that new HEAD.
- No commit/push. Temporary scratch directories were cleaned; only the two permitted SF1 follow-up artifacts were written.
