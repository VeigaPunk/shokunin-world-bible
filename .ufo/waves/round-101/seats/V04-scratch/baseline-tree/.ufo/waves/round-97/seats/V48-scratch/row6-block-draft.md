## 2026-10-17 — r97 re-check (sixth)

Sixth periodic re-check, executed at the r97 wave (2026-10-17) on the
delivered revision; the discriminator pair was run by seat V23 `gates-boundary`
and independently reproduced byte-for-byte by seat V48 `pins-c9`. Checker byte
pin verified fresh:

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Discriminator pair from the repository root: `python3 corpus/tools/discriminate_check.py`
→ `RESULT: DISCRIMINATION HELD` (exit 0); `python3 corpus/tools/discriminate_check.py --checker e97613c`
→ `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved` (exit 2,
expected control). stderr empty in both modes; the checker blob `20c56dbb…` is
identical at `f3e09f9` (declared baseline), `2393934` (HEAD), and the worktree.

| Date | Checker SHA-256 | Discrimination re-check |
|---|---|---|
| 2026-10-17 (r97) | `ff9fd2aa…d1421` | **DISCRIMINATION HELD** — re-check 6 (r97): delivered discrimination held; `e97613c` control REGRESSION-DETECTED as expected; ruling retained. Next re-check: r98. |

Gate 3 remains **not met**; the four-gate falsification trigger remains
unsatisfied; nothing in r97 changes the sequence-scope evidence state (the
sequence-scope probe rerun from the repository root again printed
`excerpt_files=` and `readme_line3=Fixture scaffolding only; not sourced story
evidence.`).
