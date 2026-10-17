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
