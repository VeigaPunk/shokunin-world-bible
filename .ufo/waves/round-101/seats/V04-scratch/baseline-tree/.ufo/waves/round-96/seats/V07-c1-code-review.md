# V07 — c1-code-review (round 96)

Seat: V07 `c1-code-review`. Scope per seat spec: after Q1 lands, line-by-line read of
`git diff dcb2d92 -- corpus/tools/map_obligations.py`; hunt false-positive paths in the gating
inventory rule (**would any delivered map trip it? run all**); dual_pointer detection precision
(legitimate prose containing pointer-like text); contract separation preserved; stdlib-only; no
live-tree writes; defects by severity.

Reviewed revision (frozen by me at review start, re-verified unchanged at report time):

```
md5   869c365d1c4ec106da198c78deca2708   corpus/tools/map_obligations.py
sha256 2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8   (matches Q1's report)
blob  010b8b63f49944a310ef907533123f255fa1af7b  (git hash-object)
git diff --numstat dcb2d92 → 115 insertions / 24 deletions, one file; 809 → 900 lines
baseline  dcb2d92:corpus/tools/map_obligations.py sha256 d1c239cc…  (matches Q1's pinned baseline)
```

Frozen copies: `V07-scratch/map_obligations_reviewed.py`, `V07-scratch/diff-reviewed.patch`
(280 lines). Baseline copies: `V07-scratch/map_obligations_git_baseline.py` and
`V07-scratch/map_obligations_baseline.py` (md5 `d31b8182953e9088a155f4ed2978af5b`, identical to
`git show dcb2d92:…`). Q1's report `Q1-tool-hardening.md` (17:51) was present before this review
began; its hash claims (`2b0ba815…`, `d1c239cc…`, 115/24, 900 lines) all verify against the bytes.
Scratch: `.ufo/waves/round-96/seats/V07-scratch/`. No commits, no pushes, no network; the only
writes outside the report are under that scratch dir.

## 1. What the diff does (read line-by-line, 280-line patch)

- `:1-19` module docstring: exit contract 0/1/2; the `**Expected inventory:**` declaration is
  gating for facts/editorial/total; the anchor count stays receipt-only.
- `:36` `LEGACY_CELL` keeps the r95 accepted grammar (token + optional parenthetical + optional
  colon-prose) but captures the tail in `(?P<tail>…)`.
- `:37-42` `POINTER_MENTION`: backticked canonical pointer, backticked legacy field path, bare
  `*.json#…`, bare `entities[i]`/`relations[i]`/`timeline[i]` (with a lookbehind so prose words do
  not fuse into a token).
- `:47-72` `SELF_TEST_CASES` split: `CORE_SELF_TEST_CASES` (inherited 22) +
  `ADDED_SELF_TEST_CASES = ("schema_drift", "inventory_mismatch")` → 24.
- `:191-195` `second_pointer_mention(tail)`; `:197-…` `parse_pointer_cell` now returns
  `(pointer, mention)` and the mention is computed **only** when the first token translated as a
  legacy field path.
- `:249-256` `inventory_counts` (strict `EXPECTED_INVENTORY` first, loose first-four-integers scan
  otherwise); `:275-285` `inventory_finding` (unparsable declaration → finding; absent → no finding;
  disagreement → finding).
- `:326-378` `parse_map_text` returns a fifth element `gating` carrying `dual_pointer` findings with
  row ID and line number; `:496-501`/`:593-600` `run_cluster`/`run_frozen` merge
  `[*gating, *drift, *compare, inventory]`.
- `:631-670` `write_test_fixture(…, declared=None)` can emit a declaration line;
  `:710-719` the two new case setups; `:794-800` the contract-matching rule; `:812` the
  `SELF-TEST CASES <pinned>/24 pinned` line.

## 2. Claim (a) — deletion class, closed on the delivered revision

My own probe (raw `claims` key and its map row both deleted, declaration left stale;
`V07-scratch/probes/deletion-class-stale-declaration`, base tool frozen from dcb2d92):

```
baseline  rc=0 | OBLIGATIONS raw=3 mapped=3~INVENTORY JSON-FACTS 3/4; EDITORIAL-ROWS 0/0; TOTAL-ROWS 3/4 MISMATCH~RESULT PASS
reviewed  rc=1 | OBLIGATIONS raw=3 mapped=3~INVENTORY JSON-FACTS 3/4; EDITORIAL-ROWS 0/0; TOTAL-ROWS 3/4 MISMATCH~FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 4/0/4; observed 3/0/3~RESULT FAIL
```

Declaration-only mutations (`inv-declared-high`, `inv-declared-low`, `inv-declared-total-wrong`,
`inv-editorial-wrong`, `inv-malformed`) all flip 0 → 1 with the same finding ID; the matching
control `legit-inv-match` stays 0, `inv-absent` stays 0, `inv-anchors-wrong` stays 0 (anchors are
indeed receipt-only, matching the new docstring), `deletion-class-redeclared` stays 0 (a
self-consistent re-declaration remains undetectable — the honest bound). Q1's §2 r95-copy demo
reproduces exactly.

## 3. Claim (b) — pinning works, but the two new pins are droppable (D1)

Against Q2's live 24-case contract (`corpus/tools/map-obligations-contract.json`,
sha256 `97b76bb8…`, git `a577a8b6…`, cases 24 including `schema_drift` and `inventory_mismatch`),
run in a scratch mirror of the repo layout so the tool reads its own contract:

```
SELF-TEST CASES 24/24 pinned
… SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']
… SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
RESULT PASS   exit 0
```

Against the pre-Q2 22-case contract it prints `SELF-TEST CASES 22/24 pinned` … `RESULT PASS` exit 0
(Q1 §3). Core-case expectations are still enforced: a tampered contract that flips `phantom` to
exit 0/[] yields `FINDING self_test_mismatch` / `RESULT ERROR` exit 2 (`V07-scratch/review-tampered`).

**But the added pins are optional.** `load_test_expectations()` (`:794-800`) fails only on
*unknown* contract cases and on *missing core* cases; it does not require the added two. Taking the
delivered 24-case contract and deleting exactly the two new case objects
(`V07-scratch/review-deleted`):

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 22/24 pinned
RESULT PASS
deleted-pin self-test rc=0
```

That is the round's own deletion class reproduced one layer up: the persisted pin of the two new
behaviors can be removed without any gate noticing. Q1 declares this as residual #4
("subset-tolerant by design", transitional while Q2's contract lagged); now that the 24-case
contract is live the tolerance has no remaining purpose and `missing = SELF_TEST_CASES - expected`
would restore the pre-r96 rule.

## 4. Claim (c) — V37-D1 closed; precision findings (D2, D4)

All seven of my dual-pointer probes flip 0 → 1 with the stable `dual_pointer` finding (parenthetical
and colon-prose; canonical, legacy and foreign-file second tokens; hidden second pointer that is
also an unmapped real obligation):

```
dual-paren-canonical   rc=0 → rc=1 | FINDING dual_pointer: row E1 (line 7) names a second pointer token 'relations.json#/0' alongside entities.json#/0/claims/0
dual-colon-canonical   rc=0 → rc=1 | … 'timeline.json#/0' …
dual-paren-legacy-phantom rc=0 → rc=1 | … 'entities[9].claims[0]' …
dual-colon-legacy-phantom rc=0 → rc=1 | … 'entities[9].claims[0]' …
dual-paren-legacy-real-unmapped rc=1 → rc=1 | dual_pointer + missing_obligation: relations.json#/0 has no map row
```

Stable across `PYTHONHASHSEED` 0/1/42 (byte-identical stdout).

**Precision.** Legitimate r88-grammar cells stay clean: `` (`statement`, `source_id`) ``,
`(Aru)`, `(row E1)`, `(Aru, \`statement\`)`, colon prose, a backticked anchor token
(`` `fictional-excerpts.md:12` ``), "see timeline.json for the event", and a canonical token under
a legacy header (fallback) — all unchanged exit 0. But the rule is text-level, not grammar-level
(D2):

```
legit-bare-text-bracket  rc=0 → rc=1 | FINDING dual_pointer: … 'entities[9] …'      # prose: "the entities[9] row was struck"
legit-bare-text-hash     rc=0 → rc=1 | FINDING dual_pointer: … 'entities.json#/0/name …'  # prose: "see entities.json#/0/name"
dual-equiv-restated      rc=0 → rc=1 | FINDING dual_pointer: … 'entities.json#/0/claims/0' …  # same pointer restated
```

A mention is treated as a mapping; a restatement of the identical pointer is flagged as a second
one. Fail-closed and bounded (no delivered map uses the legacy dialect), but a future r88-style row
whose prose cites a pointer-like string hard-fails.

**Asymmetry (D4).** The canonical path screens notes only for `.json#`; a canonical-header cell
whose note says "also entities[9]" still exits 0 (`canonical-note-bare-legacy-token`), while the
new legacy tail screen catches both forms. Pre-existing behavior, unchanged by this diff — noted
for calibration honesty only.

## 5. False-positive hunt — every delivered map, run

Full corpus battery, baseline tool vs reviewed tool over all 179 `entities.json` dirs
(`V07-scratch/corpus-baseline.tsv`, `corpus-after.tsv`): **one** rc change, and it is not the tool:

```
corpus/fixtures/r96-crossing-response  rc=2 (map_missing) → rc=0 PASS   # Q5's map landed mid-round
```

Exit distribution after: 5 × rc=0 (r88, r93, r94, r95, r96), 174 × rc=2. The five clusters that
reach the comparison stage and their declarations, all exactly matched so the new gate cannot fire:
r88 10/2/12/8, r93 12/3/15/15, r94 14/2/16/12, r95 15/2/17/13, r96 16/2/18.

- **r87** (the only delivered legacy-header map) keeps exit 2 `unsupported_map: pointer cells must
  contain one canonical inline-code pointer` with identical detail text: its cells start with
  field-suffixed tokens (`entities[0].claims[0].statement`), `legacy_pointer` returns None, the
  canonical fallback rejects the cell before any tail scan — the three backticked tokens per row do
  **not** become a `dual_pointer`. This was the highest-risk interaction and it is clean.
- **r89** keeps exit 2 `table needs one JSON fact pointer and one source-ID column`.
- **Pointer-cell surface** of all seven delivered maps enumerated
  (`V07-scratch/pointer-surface-final.txt`): 16/14/15/12 multi-token cells in r96/r94/r95/r93 are
  all `pointer + backticked entity name` with exactly one pointer-shaped token; r88's T-rows are
  `timeline[i]` + a field-list parenthetical; no delivered cell carries two pointer tokens.
- Frozen r93 replay in the scratch mirror: `SNAPSHOT inputs=4 digests=verified` / `OBLIGATIONS
  raw=12 mapped=12` / `FROZEN expected=PASS/0 findings=none matched` / `RESULT PASS` exit 0.

## 6. Contract separation, exit contract, hygiene

- **Contract separation preserved.** `dual_pointer` is raised only when the first token translated
  as a legacy field path; a legacy-header cell whose first token is canonical keeps the old screen
  (`truelegacy-canonical-first-with-note` → exit 2 `unsupported_map`), and the clean form still
  falls back (`truelegacy-canonical-first-clean` → exit 0). Canonical-header tables are untouched
  (`dual-canonical-note-pointer` → exit 2, unchanged). The dialect gate is still keyed to the exact
  normalized header (`pointer-and-fields-header-legacy-token` → exit 2). Exit 1 = findings, exit 2 =
  errors, unchanged.
- **Exit/RESULT audit** (`V07-scratch/contract_audit.py`): 179 corpus runs + 32 probe runs, 0
  violations — no stderr, exactly one `RESULT ` line, exits ⊆ {0,1,2}, no PASS with findings, no
  exit 2/1 without a FINDING.
- **Usage surface** matches Q1 §5: no args → `invalid_arguments` 2; `--bogus` → 2;
  `--self-test <cluster>` → 2; `--map /etc/hosts` → `foreign_path` 2; `--help` → 0.
- **Stdlib-only:** AST scan → `argparse, collections, hashlib, json, os, pathlib, re, subprocess,
  sys, tempfile`; non-stdlib `[]`. No new imports.
- **No live-tree writes:** corpus tree digest `FILES 1800 CORPUS-TREE-MD5 ac464582e5f413714b3b65bb64c31c1f`
  identical before and after the cluster, `--map`, frozen and `--self-test` runs; zero
  `map-obligations-self-test-*` residue under the repo root after my runs (BR-05 scratch-under-root
  behavior unchanged).
- All write calls in the file (`:635-758`) are inside the self-test fixture helpers; the
  cluster/frozen paths write nothing.

## 7. Defects by severity

**D1 — MEDIUM (the new pins are optional; the deletion class survives at the contract layer).**
Deleting `schema_drift` and `inventory_mismatch` from the delivered 24-case contract leaves
`--self-test` at `SELF-TEST CASES 22/24 pinned` / `RESULT PASS` exit 0 (`V07-scratch/review-deleted`).
The pre-r96 rule made exactly that an exit-2 error; the new subset tolerance (needed only while
Q2's contract lagged) removed the enforcement for the two cases this round adds. Declared by Q1 as
residual #4, but it weakens claim (b)'s "persisted pinning" framing. Fix: require
`SELF_TEST_CASES ⊆ expected` now that the 24-case contract is live.

**D2 — LOW (dual_pointer is text-level).** Bare prose mentions and same-pointer restatements in a
legacy cell's tail fire `dual_pointer` exit 1. No live impact (no delivered legacy map; r88 clean);
bounded, fail-closed, and the finding text names the token so the author can rephrase.

**D3 — LOW (positional loose inventory parse).** `inventory_counts` (`:249`) takes the first four
integers of an off-form declaration: `**Expected inventory:** 2 notes; 4 JSON facts; 0 editorial
rows; 4 total mapped rows; 0 anchors.` gates with a misleading receipt
(`JSON-FACTS 4/2; EDITORIAL-ROWS 0/4; FINDING … 2/4/0; observed 4/0/4`). Fail-closed; no delivered
map has an off-form declaration.

**D4 — LOW (screen asymmetry).** Canonical-header notes are screened only for `.json#`, so
`(also entities[9])` passes there while the legacy tail screen catches it. Pre-existing, unchanged.

**D5 — INFO (conflicting duplicate declarations).** First parseable declaration wins; a second,
conflicting but parseable declaration is silently ignored (`inv-duplicate-lines` exit 0), while a
second unparsable one gates. Carried behavior.

**D6 — INFO (doc parity: resolved by Q2's addendum, one stale sentence left in place).** At the
start of my battery `corpus/tools/README.md` was byte-unchanged from baseline (`c6a2d7b8…`) and its
r95 section (line 119) still read "The inventory line is a receipt, not a gate … does not by itself
change the exit code", which the new gate contradicts. Q2's Round-96 addendum landed before this
report was finalized and explicitly names that sentence: "the `INVENTORY` receipt line … is now
backed by a gate, so this addendum supersedes the r95 sentence 'The inventory line is a receipt, not
a gate'", and documents the gating counts, the unparsable-declaration case, the anchor field staying
receipt-only, `dual_pointer` with its example finding, and the 24-case contract. Code and docs now
agree; the superseded r95 sentence is left standing verbatim in its historical section, so a reader
of that section alone can still be misled.

**D7 — INFO (BR-05 unchanged).** Self-test scratch still lives under the repository root; transient
`map-obligations-self-test-*` dirs appear while many seats run `--self-test` concurrently. Zero
residue observed after my runs.

**D8 — INFO (dual_pointer has no persisted self-test case).** The 22→24 contract adds only
`schema_drift` and `inventory_mismatch`; claim (c)'s behavior is covered by ad-hoc probes only.
Consistent with the claim's wording, but combined with D1 it could regress silently.

## 8. What I did not verify

`--freeze`-style rebuild paths and `support_check.py` are out of this seat's scope; the r96 fixture
content (C2) and `dependency_freeze.py` (C3) were not reviewed here beyond running `map_obligations`
over the delivered r96 cluster. Q2's contract was reviewed only as far as the tool consumes it
(case IDs, count, and the `legacy_pointer_dialect`/`exit_codes` blocks); its prose is V38's scope.
Q1's §9 cross-checks were not re-run independently.

## Bottom line

**PASS** — on the delivered revision `2b0ba815…` (byte-identical to my frozen copy) the C1 code
verifies: the r95 deletion class now exits 1 with the stable `inventory_mismatch` finding, all three
V37-D1 legacy hidden-second-pointer forms now exit 1 with the stable `dual_pointer` finding, the
24-case self-test passes 24/24 against Q2's live contract, no delivered map (179 dirs, all seven
maps) changes exit code or finding text except r96 gaining PASS as its map landed, r87/r89 stay
fail-closed exit 2, the frozen r93 replay stays exit 0, and the code is stdlib-only with no
live-tree writes; the one real defect is D1 (MEDIUM: the two new self-test pins are droppable —
deleting them from the contract still yields `RESULT PASS` exit 0), with D2–D4 as bounded precision
residuals and D5–D8 informational.
