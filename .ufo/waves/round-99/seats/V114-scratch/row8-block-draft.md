## 2026-10-17 — r99 re-check (eighth)

Eighth periodic re-check, measured at the r99 wave (local 2026-10-17; V22 battery `2026-10-18T01:31:52Z` through `01:37:11Z`). The discriminator pair was run by seat V22 `gates-boundary` and independently reproduced byte-for-byte by seat V114 `freshness-4` (`cmp` of the two captured stdouts was empty). Checker byte pin verified fresh:

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Discriminator pair from the repository root: `python3 corpus/tools/discriminate_check.py` → `RESULT: DISCRIMINATION HELD` (exit 0); `python3 corpus/tools/discriminate_check.py --checker e97613c` → `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved` (exit 2, expected control). stderr empty in both modes. The checker blob `20c56dbb90d9f59ca4fb85971154c0774f5ce0d0` is identical at `4265df5` (declared baseline), `337f0fa` (HEAD), and the worktree.

| Date | Checker SHA-256 | Discrimination re-check |
|---|---|---|
| 2026-10-17 (r99) | `ff9fd2aa…d1421` | **DISCRIMINATION HELD** — re-check 8 (r99 wave): delivered discrimination held; `e97613c` control REGRESSION-DETECTED as expected; ruling retained. Next re-check: r100. |

Gate 3 remains **not met**; the four-gate falsification trigger remains unsatisfied; nothing in r99 changes the sequence-scope evidence state. The sequence-scope probe, rerun from the repository root by V114, again printed `excerpt_files=` and `readme_line3=Fixture scaffolding only; not sourced story evidence.` A search of `corpus/fixtures/r99-window-lapse/` for `tick-unresolved` and `null-chain` returned no matches (rc=1).
