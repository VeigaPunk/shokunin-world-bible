# In-world source support check

Run from the repository root with a cluster directory:

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
```

The cluster must contain `claim-to-excerpt-map.md` (or `claim-excerpt-map.md`) with a Markdown fact table declaring a fact ID or claim pointer, excerpt path and line span, delivery mode, and fixed-string anchor. Every grep hit must fall within that row's inclusive line span; a missing or invalid span, or any out-of-span hit, fails. Each mapped excerpt's mode must be declared either in the excerpt (`Delivery mode: ...` or `Delivery mode (R9): ...`) or in a separate excerpt-declaration table in the map; if both are present, they must agree. Accepted modes are `verbatim`, `translation`, `paraphrase`, and `summary`. The checker invokes `grep -nF --` once for each non-empty mapped anchor, without a shell.

The per-fact status and `SOURCE-SUPPORT N/N` summary count only `verbatim` and `translation` entries whose anchor occurs in the excerpt and whose map/excerpt modes match. A `paraphrase` or `summary` row is printed as `retelling-support-only` and counted separately; even a matching phrase cannot increase source-support. The final `MODES N/N` reports matching declarations. Exit is 0 exactly when every source-support anchor matches within its declared line span and all modes are declared consistently; map/cluster/read errors and failed source-support anchors exit non-zero.

This is a reproducible lexical preflight, not a judgment that the whole claim is supported, that a translation is identified to the required text/version, or that a representation is faithful, permitted, or canonical. Review those matters under the corpus decision table.
