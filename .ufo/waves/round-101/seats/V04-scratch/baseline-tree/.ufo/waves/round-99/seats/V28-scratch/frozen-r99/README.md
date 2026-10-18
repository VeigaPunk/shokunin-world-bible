# In-world source support check

Run from the repository root with a cluster directory:

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
```

The cluster must contain `claim-to-excerpt-map.md` (or `claim-excerpt-map.md`) with exactly one inventory line in this form: `**Expected inventory:** N JSON facts; N editorial rows; N total mapped rows; N distinct excerpt anchors.` Fact tables must sit under `## JSON facts` or `## Editorial rows`. Parsed category counts, total rows, and distinct `(excerpt path, anchor)` pairs are checked against the declaration; a dropped section or unrecognized table header cannot pass silently. Exact duplicate mapped rows fail, while repeated anchors are reported because co-mapping can be legitimate.

Each fact row declares a fact ID or claim pointer, excerpt path and line span, delivery mode, and fixed-string anchor. Every grep hit must fall within that row's inclusive line span; a missing or invalid span, or any out-of-span hit, fails. Each mapped excerpt's mode must be declared either in the excerpt (`Delivery mode: ...` or `Delivery mode (R9): ...`) or in a separate excerpt-declaration table in the map; if both are present, they must agree. Accepted modes are `verbatim`, `translation`, `paraphrase`, and `summary`. The checker invokes `grep -nF --` once for each non-empty mapped anchor, without a shell.

Receipts report `JSON-FACTS`, `EDITORIAL-ROWS`, and `TOTAL-ROWS` separately. `SOURCE-SUPPORT N/N` counts only JSON facts in `verbatim` or `translation` mode with matching declarations and in-span anchors; editorial rows have their own `EDITORIAL-ANCHORS` count. `paraphrase` and `summary` rows are reported as `retelling-support-only` and never increase source support. A missing retelling anchor and an excerpt declaration unused by fact rows produce `WARN` without changing exit status; invalid modes, duplicate rows, inventory mismatches, map/cluster/read errors, and missing or out-of-span source anchors exit non-zero.

### Terminal statuses

For validation runs, the final result line and exit status are:

- `RESULT PASS` — no warnings or failures; exit 0.
- `RESULT PASS WITH WARNINGS` — warnings only; exit 0.
- `RESULT FAIL` — inventory or collected validation failures; exit 1.
- `RESULT ERROR` — invalid usage, cluster, or map errors; exit 2.

This is a reproducible lexical preflight, not a judgment that the whole claim is supported, that a translation is identified to the required text/version, or that a representation is faithful, permitted, or canonical. Review those matters under the corpus decision table.

### Checker regression discrimination

Run from the repository root to verify the delivered checker against the durable r91 differential fixtures:

```sh
python3 corpus/tools/discriminate_check.py
python3 corpus/tools/discriminate_check.py --checker e97613c
```

The default run prints `RESULT: DISCRIMINATION HELD` and exits 0 only when both fixtures match their delivered README outputs, each differs from the pinned `e97613c` output by one line pair, and the checker hash matches the pin. The second command feeds the `e97613c` checker source from Git to the same pair and prints `REGRESSION-DETECTED` with exit 2. The check uses only Python's standard library; `git show` reads the historical checker without creating a file.

### Round-93 addendum: boundary certification and result interpretation (2026-10-17)

This addendum extends the earlier tool instructions and supersedes any implication that a source-support receipt or a checker exit by itself replaces the R9 manual review.

#### Boundary-document checker

Run these examples from the repository root; the checker resolves its default root from its own script path, not the current working directory:

```sh
python3 corpus/tools/boundary_doc_check.py
python3 corpus/tools/boundary_doc_check.py --self-test
```

With no options, it checks `corpus/knowledge/holder-assessment-boundary.md` and `corpus/fixtures/check_bible.py` relative to that script-root. Optional `--doc` and `--checker` paths do not bypass the expected byte pins: substituted inputs are checked against the persisted pins and drift fails closed. The gate's registry entry, including its command, verdict map, pin location, scope, and self-test, is in `SKILL.md` under **Gate registry**.

The pins are recorded in `corpus/tools/boundary-doc-contract.json`. They cover every byte of the frozen boundary document, the delivered checker, and the legacy checker source. The document and delivered checker pins cite revision `65838f867d6ece8e7b8bdcc4ffc667a08a1b785e`; the exact legacy checker revision is `5eb9451baff217c19d5786405f9b2aa500b7c1b7`, including the declared legacy anchor `check_bible.py:212-224`. The default run checks pinned inputs before replay, anchor-range, or structure checks; a changed document exits 1 with `FINDING document_drift` and does not demonstrate an `anchor_range` finding.

For a positive run, the default command should print `CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)` and exit 0. This controlled negative changes a copy and demonstrates the earlier pin guard, not the anchor-range check:

```sh
tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT
cp corpus/knowledge/holder-assessment-boundary.md "$tmp"
printf '\nDeliberate R05 pin-drift probe.\n' >> "$tmp"
python3 corpus/tools/boundary_doc_check.py --doc "$tmp"
rc=$?
printf 'observed_exit=%s\n' "$rc"
test "$rc" -eq 1
```

Expect `FINDING document_drift` and exit 1. The `--self-test` command above loads the committed document, checker, legacy checker and receipt fixtures from the pinned Git revisions, then exercises them in an isolated temporary tree. It checks persisted expected exits and finding IDs, including a separate direct `anchor_range_control`; that control tests `check_bible.py:221-224` against the 220-line delivered checker while resolving the legacy `check_bible.py:212-224` anchor against revision `5eb9451baff217c19d5786405f9b2aa500b7c1b7`. The self-test uses no network and makes no live-tree writes. It is capability evidence, not certification of the current live document; run the default command separately.

The scope is deliberately limited to whole-file byte pins, recorded receipt replay (stdout and return code), explicit numeric anchor ranges against the delivered or declared legacy checker revision, and fenced-block/limited heading/instruction-marker structure. A matching byte pin proves identity to those recorded bytes, not that the document's prose is true, supported, permitted, or canonical. A valid numeric range does not establish that the cited code is relevant. There is no C9-marker gate and no AST-, content-aware, or general prose validation; generalized anchor inference is not delivered.

`support_check.py`'s `RESULT PASS` remains only a lexical source-support preflight for its mapped excerpts. It never replaces the R9 manual review of the boundary document or certifies that the whole claim is adequately supported.

#### `discriminate_check.py` outcomes

For the valid invocations above, interpret the result text and exit code together:

- `RESULT: DISCRIMINATION HELD` with exit 0 means the delivered-checker discrimination held.
- `REGRESSION-DETECTED` with exit 2 means the pinned regression was detected (the `--checker e97613c` invocation deliberately selects the old checker behavior).
- Exit 1 means could-not-evaluate, such as a `CHECK ERROR` or `RESULT: REVERT SIMULATION INCONCLUSIVE`; it is neither a held result nor a regression verdict.

Argparse syntax errors also use exit 2, so exit 2 alone is not proof of regression: use a valid invocation and require the `REGRESSION-DETECTED` result text. The earlier command examples remain unchanged; this addendum makes the missing could-not-evaluate case explicit.

### 2026-10-17 correction: the R9 manual-review object

This dated correction supersedes the phrase "the R9 manual review of the boundary document" in the sentence above; the filed sentence remains unrewritten as history. `corpus/knowledge/holder-assessment-boundary.md` carries no R9 gate, so it is not that review's object. The R9 manual gate applies to translation-backed R5 claims: a named non-submitter reviewer inspects the exact delivered translation item, and the outcome is recorded as a per-claim `R9 manual review` entry adjacent to the claim in its claim-to-excerpt map (`corpus/knowledge/r88-sourced-inspiration-decision-table.md`, R9 appendix — "Manual R9 gate (required for translation-backed R5 claims)" and "Required record"). Corrected reading of the superseded sentence: `support_check.py`'s `RESULT PASS` is a lexical preflight for its mapped excerpts; it never replaces that per-claim manual review and never certifies that the whole claim is adequately supported.

### Round-94 addendum: `map_obligations.py`

Added in r94 (admitted at round-94 closure). Run from the repository root:

```sh
python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing   # OBLIGATIONS raw=14 mapped=14 / RESULT PASS, exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster # OBLIGATIONS raw=12 mapped=12 / RESULT PASS, exit 0
python3 corpus/tools/map_obligations.py --self-test                           # 20/20 SELF-TEST PASS / RESULT PASS, exit 0
python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93  # SNAPSHOT digests=verified / RESULT PASS, exit 0
```

The tool enumerates raw source-attributed obligations (entity `first_appearance` and each claim, relations, timeline events) and compares them one-to-one with canonical `file.json#/pointer` rows in the cluster's Markdown map. Exit contract: `0` clean; `1` failed comparison; `2` could-not-evaluate (unsupported map grammar, malformed raw JSON, invalid paths, usage errors). One terminal RESULT line on operational paths; note `--help` exits 0 with zero RESULT lines, so exit 0 alone is not a PASS. It closes the lexical blind spot where `support_check` PASSes although a raw JSON claim has no map row (demonstrated at round 94 on scratch copies); it does not judge textual entailment, delivery mode, source authentication, chronology, rights, permission, or canon. Self-test scratch is created under the repository root and is not gitignored (bounded residual BR-05, relocation candidate for r95). Expected exits and finding IDs are persisted in `corpus/tools/map-obligations-contract.json`; the frozen r93 snapshot pins four input digests under `.ufo/waves/round-94/frozen/map-obligations-r93/expected.json`.

### Round-95 addendum: `schema_drift`, 22-case self-test, r88 map dialect (2026-10-17)

This addendum extends the r94 instructions above; every earlier sentence remains as delivered history, including the open r94 residual BR-05 (the self-test scratch still lives under the repository root and is not gitignored — unchanged in r95).

#### Schema-drift class (closes r94 bounded residual BR-02)

Before: renaming an entity's `claims` container (claim content preserved) and removing that claim's map row produced `OBLIGATIONS raw=13 mapped=13` / `RESULT PASS`, exit 0 — a silent pass. The delivered revision treats a non-empty list of sourced-claim-shaped records (objects carrying non-empty `statement` and `source_id`) under an unexpected key on an entity object as schema drift. The same mutation on a scratch copy of `corpus/fixtures/r94-paired-crossing` now prints `FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'assertions'` and exits 1; `schema_drift` is the stable FINDING ID. Keeping the map row while renaming the key reports `phantom_obligation` and `schema_drift` together, still exit 1. The check is bounded to entity claim containers: it is not general JSON-schema or unknown-key validation.

#### Persisted self-test: 22 cases

`corpus/tools/map-obligations-contract.json` now persists 22 expectations: the 20 r94 cases plus `map_missing` (raw tables present, no conventional map file → exit 2, `FINDING map_missing`) and `invalid_arguments` (usage error, exercised with no cluster argument → exit 2, `FINDING invalid_arguments`). The tool compares the persisted case set with the implemented cases, not their order.

```sh
python3 corpus/tools/map_obligations.py --self-test   # 22 SELF-TEST PASS lines / RESULT PASS, exit 0
```

#### r88 map dialect (coverage; corpus unmodified)

`python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster` now exits 0 with `OBLIGATIONS raw=10 mapped=10`, `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12`, `RESULT PASS`. The dialect is enabled only by a JSON-facts pointer column whose normalized header is `JSON fact and fields` (the r88 map form); each row then carries one inline-code field-path token — `entities[i].first_appearance`, `entities[i].claims[j]`, `relations[i]`, or `timeline[i]` — which is translated to the canonical pointer before comparison. Canonical `file.json#/pointer` cells remain accepted in that table; field-path tokens are not accepted under a canonical header (the `legacy_grammar` self-test case stays exit 2 `unsupported_map`). Other legacy forms stay fail-closed: `corpus/fixtures/r87-myth-cluster` (co-mapped pointer cells) and `corpus/fixtures/r89-inspiration-paraphrase` both exit 2 `unsupported_map`. The r93 example (12/12) and r94 example (14/14) above, and the frozen r93 replay, remain `RESULT PASS` exit 0; those runs now print one additional `INVENTORY JSON-FACTS a/b; EDITORIAL-ROWS c/d; TOTAL-ROWS e/f` line when the map declares an `**Expected inventory:**`, so the r94 receipts above gain that line but keep their `OBLIGATIONS` and `RESULT` lines and exit codes. The inventory line is a receipt, not a gate: a declared count that disagrees with the parsed rows appends ` MISMATCH` to that line but does not by itself change the exit code, which only findings drive.

### Round-96 addendum: gating inventory mismatch, `dual_pointer`, 24-case self-test (2026-10-17)

This addendum extends the r95 instructions above; every earlier sentence remains as delivered history, including the open r94 residual BR-05 (the self-test scratch still lives under the repository root and is not gitignored — unchanged in r96).

#### Gating inventory mismatch (closes the r95 deletion class)

Before: on a scratch copy of `corpus/fixtures/r94-paired-crossing` with entity 0's `claims` key deleted and its `entities.json#/0/claims/0` map row removed, the r95 revision printed

```
OBLIGATIONS raw=13 mapped=13
INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
RESULT PASS
```

exit 0 — a silent pass. After: the same scratch copy prints

```
OBLIGATIONS raw=13 mapped=13
INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 14/2/16; observed 13/2/15
RESULT FAIL
```

exit 1. `inventory_mismatch` is the stable FINDING ID; the detail embeds declared and observed counts. The declaration is gating for the three counts this tool observes (JSON facts, editorial rows, total rows); an `**Expected inventory:**` line whose counts cannot be parsed at all also gates, with the same ID (fail-closed: corrupting the declaration cannot disable the gate). The declared anchor count remains a receipt field only — anchor counting belongs to `support_check.py`. A map with no declaration is unchanged: no inventory finding and no receipt line. The `INVENTORY` receipt line is still printed and still appends ` MISMATCH`; it is now backed by a gate, so this addendum supersedes the r95 sentence "The inventory line is a receipt, not a gate".

#### `dual_pointer` in legacy-dialect cells (closes r95 V37-D1)

Before: a legacy-dialect cell naming a second pointer token in its parenthetical or colon prose was silently ignored — the r95 revision exited 0. After: it is a finding. On a scratch copy of `corpus/fixtures/r88-m3-maya-cluster` with row P1's cell changed to `` `entities[0].first_appearance` (Aru; also `entities[0].claims[0]`) ``:

```
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
FINDING dual_pointer: row P1 (line 23) names a second pointer token 'entities[0].claims[0]' alongside entities.json#/0/first_appearance
RESULT FAIL
```

exit 1. The scan covers a second backticked or bare legacy token — field path or bare entity/relation/timeline index, e.g. `entities[9].claims[0]` or `entities[0]` — and a backticked or bare canonical `file.json#/…` pointer, in the parenthetical or in colon prose; the row is still read by its first token, so no cascading `missing_obligation` noise is produced. The scan is lexical and fail-closed in the over-detecting direction: prose that happens to name such a token also trips it, and no delivered corpus map does. Canonical-header cells with an embedded pointer in their note remain `unsupported_map` exit 2 (unchanged), and no legacy-grammar relaxation was introduced.

#### Persisted self-test: 24 cases

`corpus/tools/map-obligations-contract.json` now persists 24 expectations: the 22 r95 cases plus `schema_drift` (the isolated fixture drops the claim's map row and renames entity 0's `claims` container to `assertions` with content preserved → exit 1, exactly `FINDING schema_drift`) and `inventory_mismatch` (the intact fixture's map declares 5 JSON facts / 0 editorial rows / 5 total mapped rows while 4 rows exist → exit 1, exactly `FINDING inventory_mismatch`). The tool requires the contract to pin every core case and to pin no unimplemented case, then exercises exactly the pinned cases:

```sh
python3 corpus/tools/map_obligations.py --self-test   # SELF-TEST CASES 24/24 pinned / 24 SELF-TEST PASS lines / RESULT PASS, exit 0
```

#### Unchanged

All prior behavior holds on the delivered corpus: r88/r93/r94/r95/r96 exit 0 (`OBLIGATIONS` 10/10, 12/12, 14/14, 15/15, 16/16), the frozen r93 replay exits 0, r87/r89 stay fail-closed exit 2 `unsupported_map`, the 0/1/2 exit contract and usage errors are unchanged, the `INVENTORY` receipt surface is unchanged, and the `support_check` receipts are unchanged.

### Round-96 addendum: `map_obligations` hardening + new gate `dependency_freeze.py`

`map_obligations` (round 96): three hardening closes, all demonstrated before/against the r95 tool (`git show dcb2d92:…`): (1) a declared-vs-observed inventory mismatch is now **gating** — the r95 deletion class (a claims key and its map row both removed) exits 1 with stable FINDING `inventory_mismatch` (previously exit 0 with the shortfall only in the non-gating INVENTORY receipt); bound: a *consistently regenerated* declaration still exits 0 — the gate compares declared vs observed, and a coherent regeneration is indistinguishable. (2) The persisted self-test carries 24 cases (added `schema_drift`, `inventory_mismatch`), both proven load-bearing by neutralization and expectation-flip perturbations. (3) The V37-D1 gap is closed: legacy-dialect cells naming a second pointer in parenthetical or colon-prose exit 1 with stable FINDING `dual_pointer` (r88's real single-pointer cells still PASS). Residuals (r97 debt): the two added pins are droppable under the subset-tolerant loader (23/24 still passes); `dual_pointer` has no persisted self-test case.

`dependency_freeze.py` (round 96, new gate): frozen dependency-edge regression check closing BR-01's JSON-edge half. Verifies each pinned fixture's event→depends_on edge set, relation endpoints, and content digest against `corpus/tools/dependency-freeze-contract.json`. Entry: `python3 corpus/tools/dependency_freeze.py <fixture-dir>` (`0` clean / `1` `REDUCTION-DETECTED` / `ADDITION-DETECTED` / `ENDPOINT-CHANGE` / `2` could-not-evaluate); self-test: `python3 corpus/tools/dependency_freeze.py --self-test` (14/14, persisted in the contract). The chain `r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response` freezes 4/4 clean. The carried BR-01 mutation (dropping `evin-ninth-bell` from the r94 tick-10 `depends_on` — invisible to every prior gate) exits 1 `REDUCTION-DETECTED`. Hazards (r97 debt): `--freeze <dir>` rewrites the delivered contract and has no `corpus/fixtures/` scope guard — integration-time only; receipts are not path-bound (a same-named copy at a foreign path verifies identically); BR-01's markdown/prose half remains open; `DIGEST-MISMATCH` does not name the changed file.

### Round-97 addendum: `dual_pointer` pinned, subset-tolerant loader closed, 25-case self-test (2026-10-17)

This addendum extends the r96 instructions above; every earlier sentence remains as delivered history, including the open r94 residual BR-05 (the self-test scratch still lives under the repository root and is not gitignored — unchanged in r97).

#### `dual_pointer` persisted self-test case (closes the r96 residual)

The r96 `dual_pointer` finding had no persisted self-test case — its behavior was demonstrated by mutation demos only. `corpus/tools/map-obligations-contract.json` now pins it as the 25th case: `{"id": "dual_pointer", "exit": 1, "finding_ids": ["dual_pointer"]}`. The case's isolated fixture is a legacy-dialect map (pointer-column header `JSON fact and fields`) whose first row cell is

```
`entities[0].first_appearance` (also named `entities[1].first_appearance`)
```

Hand-derived expectation, reproduced on a scratch cluster of the same shape before the pin was added: the row is still read by its first token, so the run prints `OBLIGATIONS raw=4 mapped=4` and exactly one `FINDING dual_pointer: row E1 (line 7) names a second pointer token 'entities[1].first_appearance' alongside entities.json#/0/first_appearance`, `RESULT FAIL`, exit 1 — no cascading `missing_obligation` or `phantom_obligation`. The same fixture with the parenthetical removed prints `OBLIGATIONS raw=4 mapped=4` / `RESULT PASS`, exit 0, so the case isolates the `dual_pointer` emission and no other finding.

#### Subset tolerance closed (loader tightened)

Before (r96 revision, tool sha256 `2b0ba815…`): a contract that dropped either r96-added pin still ran green — dropping `schema_drift` printed `SELF-TEST CASES 23/24 pinned` … `RESULT PASS`, exit 0. After (delivered revision): the loader requires the contract to pin every implemented case, and a dropped case fails closed before any case is exercised:

```
FINDING self_test_contract: contract drops implemented self-test cases: schema_drift
RESULT ERROR
```

exit 2 — and likewise for a dropped core case (`complete`). Both probes ran with a byte-identical copy of the delivered tool next to a scratch contract copy; the delivered contract was not modified (the loader reads the contract from the tool's own directory, so the probe moved both).

#### The `dual_pointer` pin is load-bearing

Neutralizing the emission in a scratch tool copy (`second_pointer_mention()` short-circuited to `return None`) turns the pinned case red:

```
SELF-TEST FAIL dual_pointer exit=0 findings=none
FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
RESULT ERROR
```

exit 2. The pin therefore fails when the behavior it records is removed.

#### Persisted self-test: 25 cases

```sh
python3 corpus/tools/map_obligations.py --self-test   # SELF-TEST CASES 25/25 pinned / 25 SELF-TEST PASS lines / RESULT PASS, exit 0
```

The tool requires the contract to pin every implemented case and to pin no unimplemented case, and it exercises exactly the pinned cases.

#### Unchanged

Re-run on the delivered revision: r88 (10/10), r93 (12/12), r94 (14/14), r95 (15/15), r96 (16/16) all exit 0 with their receipts, the frozen r93 replay exits 0 (`SNAPSHOT inputs=4 digests=verified` / `FROZEN expected=PASS/0 findings=none matched`), r87/r89 stay fail-closed exit 2 `unsupported_map`, and the 0/1/2 exit contract, the `INVENTORY` receipt surface, and the `support_check` receipts are unchanged. The two r96-carried residuals for this tool (droppable added pins, unpinned `dual_pointer`) are closed here; the r94 BR-05 scratch-placement residual remains open.

### Round-97 supersession: dependency_freeze hazards closed

The "Hazards (r97 debt)" paragraph of the Round-96 addendum above is superseded as of 2026-10-17 (round 97): `--freeze` is now scope-guarded to `corpus/fixtures/**` (foreign targets exit 2 `SCOPE-REFUSED` with no write); pins are path-bound (a byte-identical same-named copy at a foreign path exits 2 `PATH-MISMATCH`); `DIGEST-MISMATCH` names the changed file; the self-test carries 16 persisted cases. Remaining bounds (r98 candidates): the pin payload covers the five JSON tables only — fixture Markdown is not pinned (the r96 re-freeze was a revision-only refresh; the map digest `e851f068…` is deliberately not in the pin set); BR-01's markdown/prose half remains open; the frozen chain is the declared four fixtures (`r97-crossing-acknowledgment` unpinned). Both tools' self-test scratch directories are created at the repository root and covered by `.gitignore` (`*-self-test-*/`).

### Round-98 addendum: `SELF-TEST-MISMATCH` exit 2, legacy pin migration, six-fixture chain, 17-case self-test (2026-10-17)

This addendum extends the r97 instructions above; every earlier sentence remains as delivered history, including the open r94 residual BR-05 (the self-test scratch still lives under the repository root and is not gitignored — unchanged in r98).

#### Superseded numbers (prior text kept as delivered history)

- The Round-96 `dependency_freeze.py` paragraph above reads "self-test: `python3 corpus/tools/dependency_freeze.py --self-test` (14/14, persisted in the contract)" and "The chain `r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response` freezes 4/4 clean." Superseded 2026-10-17 (round 98): the persisted self-test carries 17 cases, and the chain is six fixtures verifying 6/6 clean.
- The Round-97 supersession above reads "the self-test carries 16 persisted cases" and "the frozen chain is the declared four fixtures (`r97-crossing-acknowledgment` unpinned)". Superseded 2026-10-17 (round 98): 17 persisted cases, and `r97-crossing-acknowledgment` and `r98-clerk-filing` are now pinned, so the declared chain is six fixtures.
- The rest of that supersession still stands: the pin payload covers the five JSON tables only (fixture Markdown is still not pinned) and BR-01's markdown/prose half remains open.

#### `SELF-TEST-MISMATCH` exits 2 (aligned with `map_obligations`)

Before (r97 revision, `git show 9a3d648:corpus/tools/dependency_freeze.py`), a persisted expectation that disagreed with the observed CLI outcome printed `SELF-TEST 15/16`, `FINDING SELF-TEST-MISMATCH: cases failed: ['clean']`, `RESULT FAIL` and exited 1 — the self-test could not evaluate its own contract, yet it reported the code this tool reserves for a detected reduction. After (delivered revision) the same disagreement prints `SELF-TEST 16/17`, the same finding, `RESULT ERROR` and exits 2, matching `map_obligations.py`'s could-not-evaluate treatment of its own self-test mismatch. Both runs used a scratch tree holding the revision beside a copy of the contract with one expectation flipped (`self_test.expected.clean.exit` 0 → 1); the delivered contract was not modified.

#### Path-less legacy pins are migrated by `--freeze`

Before, a pin written before r97's path binding records no fixture path and `--freeze` refused it:

```
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pin r95-crossing-aftermath already names None; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR
```

exit 2 — the only route forward was a manual contract edit. After, the same invocation prints `MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath`, freezes the pin and exits 0; the fixture then verifies `RESULT PASS` exit 0. Verification alone still fails closed until the migration runs (`FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs a repo-relative fixture path`, exit 2). The r97 same-named-path guard is unchanged: a pin that records a *different* path is still refused, exit 2 `SCOPE-REFUSED`. Demonstrated on a scratch tree whose contract copy carries `pins.r95-crossing-aftermath.fixture = null`; the delivered contract was not modified:

```sh
# inside a scratch tree holding its own copy of the tool and contract
# (pins.r95-crossing-aftermath.fixture = null), run from that tree's root:
python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r95-crossing-aftermath   # MIGRATED … / RESULT PASS, exit 0
```

#### Chain extended to six fixtures

```sh
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath \
         r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
  python3 corpus/tools/dependency_freeze.py "corpus/fixtures/$f"; echo "$f exit=$?"
done
```

All six print `FREEZE …`, `DIGEST …`, `RESULT PASS` and exit 0. The two added receipts are `FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1` (digest `3c922d20a01bbd3f…`) and `FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1` (digest `59a0f4fa3d4a47e0…`). The r97 pin discharges the r97 round's recorded unfrozen-edge finding (V46): on a scratch copy of the fixture with the tick-13 edge dropped — `acknowledgment-aru-records` losing `depends_on: ["response-evin-salt-court"]` — the pin reports `FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']` and exits 1, while the unmodified scratch copy exits 0. Before the pin existed that mutation was unreachable: the fixture only produced `UNPINNED-FIXTURE` exit 2.

#### Contract `precedence` text and the 17th case

`corpus/tools/dependency-freeze-contract.json` now spells out the exit-2 order and the finding IDs: semantic inventory findings decide first (exit 1: `REDUCTION-DETECTED`, `ADDITION-DETECTED`, `ENDPOINT-CHANGE`); then exit-2 (could-not-evaluate) checks run in order and the first failing check decides — `UNPINNED-FIXTURE` (no pin for the fixture name) or `CONTRACT-INVALID` (unreadable contract or invalid pin), `FIXTURE-MISSING`, `PATH-MISMATCH`, `FILE-MISSING` / `MALFORMED-JSON` / `MALFORMED-MODEL`, `DIGEST-MISMATCH`, `INVALID-ARGUMENTS`, `SELF-TEST-MISMATCH`; `--freeze` additionally raises `SCOPE-REFUSED`. The text also records that a path-less legacy pin is migrated in place by `--freeze` instead of refused.

The persisted self-test carries 17 cases: the 16 inherited cases with byte-identical expectations (compared case-by-case against `git show 9a3d648:corpus/tools/dependency-freeze-contract.json`) plus `self_test_mismatch` (`exit: 2`, exactly `FINDING SELF-TEST-MISMATCH`), which exercises the class above.

```sh
python3 corpus/tools/dependency_freeze.py --self-test   # SELF-TEST 17/17 / RESULT PASS, exit 0
```

#### Unchanged

`map_obligations.py` is unchanged in r98 (`--self-test` still prints `SELF-TEST CASES 25/25 pinned` … `RESULT PASS`, exit 0), as are `support_check.py` and `boundary_doc_check.py`; `git diff 9a3d648 -- corpus/tools/` lists only `dependency_freeze.py` and `dependency-freeze-contract.json`. The 0/1/2 exit contract, the `FREEZE` / `DIGEST` / `RESULT` receipt surface, and the scope and path-binding behavior are unchanged. The r94 BR-05 scratch-placement residual remains open.

#### Dated correction (2026-10-17, round-98 closure, adjudication AC-2)

Two sentence classes in the historical addenda above are factually stale on the delivered revision and are superseded as classes (prior text kept as delivered history): (1) every "the self-test scratch … is not gitignored" sentence (r94–r97 addenda) — the r97 closure added `*-self-test-*/` to `.gitignore`, so both tools' repo-root self-test scratch has been gitignored since then (`git check-ignore -v` confirms); the BR-05 bound survives only as "scratch is created at the repository root", not as a gitignore gap. (2) Any prior sentence reading that a round's change "lists only two files" is corrected to the measured counts (the r98 round modified seven tracked files: `dependency_freeze.py`, `dependency-freeze-contract.json`, this README, the r95 map, and the three knowledge notes; see V20-scope-creep's bucket table).

### Round-99 addendum: full-file pin payload, Markdown-tamper detectability, 18-case self-test, chain re-frozen 6/6 (2026-10-17)

This addendum extends the r98 instructions above; every earlier sentence remains as delivered history. The r94 BR-05 residual remains only as "scratch is created at the repository root" (the r98 dated correction on gitignore still stands).

#### Superseded payload sentences (prior text kept as delivered history)

- The Round-98 addendum above reads "The rest of that supersession still stands: the pin payload covers the five JSON tables only (fixture Markdown is still not pinned) and BR-01's markdown/prose half remains open." Superseded 2026-10-17 (round 99): the pin payload covers all ten declared files per fixture, and BR-01's prose half is edit-detectable, not semantics-provable.
- The Round-97 supersession above reads "the pin payload covers the five JSON tables only — fixture Markdown is not pinned … BR-01's markdown/prose half remains open". That bound was still current at r98 and is superseded 2026-10-17 (round 99) by the same close.
- The Round-98 sentence "The persisted self-test carries 17 cases" and the command comment `# SELF-TEST 17/17 / RESULT PASS, exit 0` are superseded 2026-10-17 (round 99): the persisted self-test carries 18 cases. The same command now prints `SELF-TEST 18/18`.

#### Full-file pin payload (schema versioned)

`corpus/tools/dependency-freeze-contract.json` is `schema_version` 2 and `payload_schema_version` 2. Each of the six chain pins carries `payload_schema_version` 2 and a sha256 for every declared file:

`entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`.

The five JSON-table digests are unchanged from the r98 pins (`git show 4265df5:corpus/tools/dependency-freeze-contract.json`); the content digest moved because the payload now includes the five Markdown files. The delivered pins record revision `337f0fa52b02626b7687eedbb2d99fab30446fe4`, written by the guarded `--freeze` (scope still `corpus/fixtures/**`; a target outside that scope exits 2 `SCOPE-REFUSED` with no write). `--freeze` rewrites the contract and is integration-time only — do not re-run it against the delivered contract to re-check. A pin whose `payload_schema_version` is not 2, or whose `files` object does not digest all ten, exits 2 `CONTRACT-INVALID`. `--freeze` also refuses when a declared pinned file is absent (`FILE-MISSING`).

#### Markdown-tamper detectability

BR-01's prose half is now "any prose edit is detectable", not "dependency semantics provable". Any edit to any of the ten pinned files exits 2 `DIGEST-MISMATCH` naming that file. The gate reports the byte change; it does not judge whether the remaining prose still states the dependency.

Before, on a scratch tree holding `git show 4265df5:corpus/tools/dependency_freeze.py` and the matching contract, with a copy of `corpus/fixtures/r95-crossing-aftermath`: removing the first `depends on` from `fictional-excerpts.md` still printed `RESULT PASS` and exited 0 (digest `d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9`, unchanged). Command, from that scratch root:

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
```

After, the same command in a scratch tree holding the delivered tool and contract, after the same removal:

```
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest 892d17d3a9a91aab99f1da6aaac66e3854d286dcba9a2178e3a0b8b034d011b8 != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: fictional-excerpts.md (sha256 0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282 -> 4b13096081476ac2d92694ee26830d981c5095e786f06b64d67b34f9d4ce37fd); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

exit 2. A trailing newline appended to each of the ten pinned files, each in its own scratch copy of r95, likewise exited 2 `DIGEST-MISMATCH` naming that file. The 18th persisted case, `markdown_tamper`, pins this class (`exit: 2`, finding `DIGEST-MISMATCH`, `names_file: fictional-excerpts.md`): the isolated case appends a newline to `fictional-excerpts.md`.

Bound: the declared ten are the pin set. `corpus/fixtures/r88-m3-maya-cluster/symbolism-clause-map.md` is outside that set; appending a marker to it on a scratch copy still printed `RESULT PASS` and exited 0 (digest `acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae`).

#### Chain re-frozen 6/6

```sh
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath \
         r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
  python3 corpus/tools/dependency_freeze.py "corpus/fixtures/$f"; echo "$f exit=$?"
done
```

All six print `FREEZE …`, `DIGEST …`, `RESULT PASS` and exit 0. Digests on the delivered revision: r88 `acf677a7085be3f6…`, r94 `048b8ff39e4a5232…`, r95 `97cffd7bfe6e0c92…`, r96 `43911900923c110b…`, r97 `a28b9ea0d65ec355…`, r98 `5ecf84e19121ea12…`.

#### Persisted self-test: 18 cases

```sh
python3 corpus/tools/dependency_freeze.py --self-test   # SELF-TEST 18/18 / RESULT PASS, exit 0
```

The run printed 18 `CASE … ok` lines, including the 17 prior case ids, then `SELF-TEST 18/18` and `RESULT PASS`, exit 0. `SELF-TEST-MISMATCH` still exits 2.

#### Unchanged

The 0/1/2 exit contract, the clean-run `FREEZE` / `DIGEST` / `RESULT` receipt surface, path binding (`PATH-MISMATCH`), and the `--freeze` scope guard are unchanged. Semantic inventory findings still decide first (exit 1). This addendum does not change `map_obligations.py`, `support_check.py`, or `boundary_doc_check.py`.
