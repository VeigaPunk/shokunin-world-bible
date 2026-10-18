# F16 — boundary-doc (FOLLOW-UP verification seat)

Role: leaf verification seat in the round-94 DeepSeek FOLLOW-UP wave. Task: run
`corpus/tools/boundary_doc_check.py` and its `--self-test` on the delivered tree, and
determine whether the r94 additions falsified the boundary-document contract — i.e.
whether any r94 byte is pinned by `corpus/knowledge/holder-assessment-boundary.md` and
whether the document's claims still hold. All commands run from the lane root with
`python3`; no writes outside this report file.

Tree identity at measurement time:

- `git log --oneline -6` → `65a9329 lore r94: declare DeepSeek FOLLOW-UP before dispatch`,
  `abbc3e0 lore r94: checkpoint Luna WORK candidate pending DeepSeek review`,
  `9c2eea3 lore r93: close verified claims and correct historical admission records`.
- `git status --porcelain` → single untracked entry `?? .ufo/waves/round-94/followup/`
  (this wave's own reports); no tracked modification.
- `git rev-parse HEAD:corpus/knowledge/holder-assessment-boundary.md HEAD:corpus/fixtures/check_bible.py`
  → `625148b6f444f0c7c7b0404646c232fca6149a3d`, `20c56dbb90d9f59ca4fb85971154c0774f5ce0d0`;
  `git hash-object` on both working-tree files returns the same two blobs, so the working
  tree bytes equal the committed bytes for the pinned document and checker.

## 1. Required check A — default run

Command: `python3 corpus/tools/boundary_doc_check.py; echo "EXIT=$?"` (observed output, verbatim):

```
Wall time: 0.388 seconds
CHECK pinned inputs: PASS
CHECK receipt replay: PASS
CHECK explicit anchor ranges: PASS
CHECK document structure: PASS
scope=frozen-document drift + receipts + explicit-anchor range + structure; not semantic or AST validation
replay_receipts=3/3
replay_cases=14/14
anchors=2/2
h1_count=1
duplicate_headings=0
instruction_markers=0
CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)
EXIT=0
```

Expected `exit 0` with receipts 3/3, cases 14/14, anchors 2/2 — all observed as expected.
Re-run twice in one shell: both runs produced identical output
(`python3 corpus/tools/boundary_doc_check.py | sha256sum` → `93505918867f02e48355cc5c5f3a5763ccfad3f4a7c86a499f024909a3665fcc`
on both runs), so the verdict is deterministic on this tree.

## 2. Required check B — self-test

Command: `python3 corpus/tools/boundary_doc_check.py --self-test; echo "EXIT=$?"` (observed output, verbatim):

```
Wall time: 1.031 seconds
SELF-TEST PASS anchor_range_control exit=1 findings=['anchor_range'] anchors=1/2 legacy_anchor=check_bible.py:212-224@5eb9451baff217c19d5786405f9b2aa500b7c1b7 baseline_lines=330
SELF-TEST PASS committed_default exit=0 findings=none
SELF-TEST PASS comment_parked_c9 exit=1 findings=['document_drift']
SELF-TEST PASS wrong_bare_anchor exit=1 findings=['document_drift']
SELF-TEST PASS checker_drift exit=1 findings=['checker_drift']
SELF-TEST PASS missing_document exit=1 findings=['document_missing']
SELF-TEST PASS missing_checker exit=1 findings=['checker_missing']
SELF-TEST PASS receipt_drift exit=1 findings=['receipt_drift']
SELF-TEST PASS
EXIT=0
```

All eight controls in `corpus/tools/boundary-doc-contract.json` (`self_test.expected`) matched
their persisted exit/finding expectations, including the negative controls. The
`committed_default` control — the committed document replayed against its committed fixture
inputs — passed at the delivered commit, which is the strongest single signal that the r94
tree does not disturb the pinned pair.

## 3. What r94 actually changed

`git diff --name-only 9c2eea3 abbc3e0 | grep -v "^\.ufo/waves"` (15 paths):

```
LOG.md
SCORECARD.md
corpus/fixtures/r94-paired-crossing/README.md
corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md
corpus/fixtures/r94-paired-crossing/contradictions.json
corpus/fixtures/r94-paired-crossing/entities.json
corpus/fixtures/r94-paired-crossing/fictional-excerpts.md
corpus/fixtures/r94-paired-crossing/inspiration-note.md
corpus/fixtures/r94-paired-crossing/relations.json
corpus/fixtures/r94-paired-crossing/source-excerpt.md
corpus/fixtures/r94-paired-crossing/sources.json
corpus/fixtures/r94-paired-crossing/timeline.json
corpus/knowledge/r94-cross-myth-design-comparison.md
corpus/tools/map-obligations-contract.json
corpus/tools/map_obligations.py
```

`git diff --name-status 9c2eea3 abbc3e0 -- corpus/fixtures/r94-paired-crossing` shows every
r94 fixture file as `A` (added); the two tool files and the knowledge doc are likewise new.

## 4. Parity findings

### P1 — the contract's own pins are unchanged and still match

`cat corpus/tools/boundary-doc-contract.json` pins document sha256
`7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e` and checker sha256
`ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`.
`sha256sum corpus/knowledge/holder-assessment-boundary.md corpus/fixtures/check_bible.py` observed:

```
7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e  corpus/knowledge/holder-assessment-boundary.md
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Both match. Independently, the doc's claim "The checker stayed byte-identical through r91
closure `396c568`" (`holder-assessment-boundary.md:544`) was re-derived:
`git show 396c568:corpus/fixtures/check_bible.py | sha256sum` →
`ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`, i.e. the r91-closure
checker equals the delivered one. The legacy baseline claim
(`check_bible.py:212-224` at `5eb9451…`) was re-derived too:
`git show 5eb9451baff217c19d5786405f9b2aa500b7c1b7:corpus/fixtures/check_bible.py | wc -l`
→ `330`, matching the doc's "330 lines" and the self-test's `baseline_lines=330`.

### P2 — no r94 byte is pinned by the boundary document

The document references no path that r94 touched:

- `grep -c "r94" corpus/knowledge/holder-assessment-boundary.md` → `0` (no occurrence of the round anywhere in the doc).
- `grep -n "corpus/tools" corpus/knowledge/holder-assessment-boundary.md` → no match (exit 1), so the doc does not reference the new `map_obligations.py` / `map-obligations-contract.json` or any other tools path.
- `git diff --name-only 9c2eea3 abbc3e0 -- <every input the doc pins>` returned **no paths** for the full pinned set: `corpus/knowledge/holder-assessment-boundary.md`, `corpus/fixtures/check_bible.py`, `corpus/tools/boundary_doc_check.py`, `corpus/tools/boundary-doc-contract.json`, `corpus/fixtures/README.md`, `corpus/tools/README.md`, `corpus/live/runs/round-85/probe-inputs`, the two r87 direction fixtures, the six r88/r89 durable fixtures, the three FN-2/multi-cause fixtures, `reports/round-1/current-baseline.json`, `reports/round-1/baseline-probes.json`.

Because the doc, the checker, the contract, the README, the probe inputs and all 14 replayed
fixture directories are byte-identical between `9c2eea3` and `abbc3e0`, the checker's verdict
is necessarily unchanged by the r94 additions; the observed exit 0 is therefore not merely
consistent with, but implied by, the unchanged pinned set.

### P3 — the r94 fixture does not arm the doc's provenance recheck

The doc's `recheck:` clause (`holder-assessment-boundary.md:50-59`) requires re-running "any
fixture that combines `provenance` with a duplicated entity id", and its census claims are
revision-qualified ("33 directories carry provenance" at `ca7f9ef`, `:567-568`).

- `grep -rl "provenance" corpus/fixtures/r94-paired-crossing/` → no files matched (exit 1); `grep -c provenance corpus/fixtures/r94-paired-crossing/*.json` → `0` for all five JSON files. The new fixture carries no provenance record at all, so it cannot combine one with a duplicated holder id.
- Measured inventory on the delivered tree: 35 fixture directories contain `provenance` in some `.json` (`for d in corpus/fixtures/*/; do grep -ql provenance "$d"*.json && n=$((n+1)); done` → `dirs_with_provenance=35`). The delta from the doc's r90 number is fully accounted for by r91, which the doc itself already records: `comm -13 <(git ls-tree -d --name-only ca7f9ef corpus/fixtures/) <(current dirs)` lists exactly four directories added since `ca7f9ef` — `r91-c1-null-chain` (provenance), `r91-c1-tick-unresolved` (provenance), `r93-m2-kojiki-cluster` (none), `r94-paired-crossing` (none) — and `holder-assessment-boundary.md:577-578` states "the two additional durable calibration fixtures are `r91-c1-null-chain` and `r91-c1-tick-unresolved`". So the 33→35 change is pre-existing, documented, and revision-scoped, not an r94 falsification.
- Directory counts: `at ca7f9ef: 164  now: 168` — again matching the doc's revision-qualified "164 fixture directories" and SCORECARD's r94 checkpoint line "167→168 directories".

### P4 — doc claims about the fixtures directory still hold

- `holder-assessment-boundary.md:63-64` claims `corpus/fixtures/` contains only `check_bible.py` as a Python file. `ls corpus/fixtures/*.py` → `corpus/fixtures/check_bible.py` only. r94 placed its new tool under `corpus/tools/`, so the claim holds on the delivered tree.
- `:60-66` claims `measure_holder_disclosure.py` is absent; `ls corpus/fixtures/measure_holder_disclosure.py` → `No such file or directory`. Holds.

### P5 — the doc's README line references still resolve

`corpus/fixtures/README.md` is untouched by r94 (absent from the P2 diff list). Its cited
ranges still land on the described content: `sed -n '110,128p'` shows the provenance
discipline text plus the `## Round 7: duplicate source IDs are ambiguous, not qualifying
citations` heading (matching `:590-592`), and `grep -n "^## Round"` puts `## Round 88` at
line 1008 and `## Round 89` at line 1012, matching the doc's `:1008-1011` / `:1012-1015`.

### P6 — the SCORECARD pointer is still live

`holder-assessment-boundary.md:597-598` cites "`SCORECARD.md` fleet-round-1 calibration
declaration (unmeasured tie, falsifiability tie-break)". r94's SCORECARD change is
append-only: `git diff 9c2eea3 abbc3e0 -- SCORECARD.md | grep -c '^-[^-]'` → `0` deleted
lines (the hunk is `@@ -365,3 +365,19 @@`, additions only), and the declaration text still
reads "All inherited axis scores above are unmeasured… Calibration wins the falsifiability
tie-break" (`SCORECARD.md:20-22`, `:50-51`). The pointer resolves to unchanged bytes.

### P7 — independent replay of the document's receipts (not trusting the checker)

I re-derived the 14 pasted cases myself (own script: parse the four fenced `sh` blocks,
extract each loop's case list and base, run each case, require empty stderr, compare to the
next `text` fence byte-for-byte). Observed:

```
loop corpus/live/runs/round-85/probe-inputs (5 cases): byte-identical, stderr empty
loop corpus/fixtures (6 cases): byte-identical, stderr empty
loop corpus/fixtures (3 cases): byte-identical, stderr empty
INDEPENDENT REPLAY: 14/14 cases byte-identical
```

This confirms the doc's "All fourteen pasted case blocks below replay byte-identically
through the delivered checker" (`:41-42`) independently of `boundary_doc_check.py`'s own
replay logic. The fourth `sh` block (the `measure_holder_disclosure.py` command) is not a
fixture loop and was correctly skipped by the checker's parser as well
(`sh block at char 44329: not a fixture loop (skipped)`).

### P8 — the doc's prose claim about the symmetric direction fixtures

`:390-395` states the two in-tree direction fixtures "replay symmetrically" with
`5 violation(s)`. Direct runs observed:

```
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-from-ambiguous
→ VIOLATION: entities[5].id: duplicate entities id 'dup'
  VIOLATION: entities[3].provenance[0].from_holder: ambiguous entity 'dup'
  VIOLATION: entities[3].provenance[0]: … first stop: ambiguous holder identity from_holder 'dup' at entities[3].provenance[0]
  VIOLATION: entities[3].provenance[1]: … (same first stop)
  VIOLATION: entities[3].provenance[2]: … (same first stop)
  5 violation(s); no canon changed            [rc=1]

python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-to-ambiguous
→ same shape with to_holder 'dup', 5 violation(s)   [rc=1]
```

Both match the doc's wording (same shape, records [0]/[1]/[2], 5 violations).

### P9 — anchor coverage boundary (scope note, not a failure)

The checker's `ANCHOR` regex is `\bcheck_bible\.py:(\d+)(?:-(\d+))?\b`
(`corpus/tools/boundary_doc_check.py:35`), so `anchors=2/2` covers exactly two spellings:
the legacy `check_bible.py:212-224` (resolved against the `5eb9451` baseline blob) and the
delivered `check_bible.py:184` (`sed -n '184p'` → `errors.append(f'{location}.{endpoint}:
ambiguous entity {entity_id!r}')`, i.e. the relation-endpoint ambiguity precedent the doc
cites at `:538-539`). The doc's many bare `:NNN` references are *not* machine-checked. I
spot-verified six of them by line-addressed reads against the delivered checker and each
matched its described content: `:208-210` the single disclosure template, `:169-170` the
null guard in `holder_identity_detail`, `:322-326` tick order, `:327-337` chain continuity
with `holder_identity_detail`, `:418-428` CLI/exit behavior. The two anchors are therefore a
lower bound on the doc's checker line references, not the whole set — consistent with the
contract's declared scope.

### P10 — the new r94 fixture is clean under the pinned checker

`python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing` →
`CLEAN: schema, citations, relations, timeline; 0 violations` `[rc=0]`, matching the r94
knowledge doc's structural receipt (`corpus/knowledge/r94-cross-myth-design-comparison.md:27`).
This is context for the pinned checker's behavior on the new input, not a boundary-document
claim; the boundary doc makes no statement about this fixture.

## 5. Limits and residual uncertainty

- The contract's own scope line applies: "frozen-document drift + receipts + explicit-anchor
  range + structure; not semantic or AST validation". Nothing here validates the boundary
  doc's semantics, the fictional content, or the checker's reasoning; it validates byte pins,
  receipt replay, the two declared anchors, and document structure.
- The boundary doc's census numbers (160/164 directories, 33 provenance directories, 13
  duplicated-holder records) are revision-qualified in the document itself; I confirmed the
  deltas are attributable to r91/r93/r94 additions and that r94 contributes no provenance
  bytes, but I did not re-derive the duplicated-holder record count for the delivered tree —
  no r94 byte bears on it.
- The doc's `UNKNOWN / UNMEASURED` line about fixtures outside the listed census combining
  `provenance` with a duplicated holder id (`:636-639`) remains unmeasured; r94's fixture has
  no provenance, so it neither resolves nor contradicts that line.
- I did not modify, regenerate, or re-pin anything; the report is the only file written.

## Bottom line

**PASS** — on the delivered tree (HEAD `65a9329`, WORK candidate `abbc3e0`),
`python3 corpus/tools/boundary_doc_check.py` exits 0 with receipts 3/3, cases 14/14, anchors
2/2 and `--self-test` exits 0 across all eight controls, while the r94 additions add only new
paths (`corpus/fixtures/r94-paired-crossing/`, `corpus/tools/map_obligations.py`,
`corpus/tools/map-obligations-contract.json`, `corpus/knowledge/r94-cross-myth-design-comparison.md`,
plus append-only LOG/SCORECARD edits) and change no byte the boundary document pins — no r94
byte is pinned by it, and every checked doc claim still holds.
