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
