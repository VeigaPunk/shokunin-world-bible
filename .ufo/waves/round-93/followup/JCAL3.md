# JCAL3 — Discrimination judge (round-93 follow-up)

Seat mission: on 65838f8, run `corpus/tools/discriminate_check.py` in both documented modes (delivered → exit 0 DISCRIMINATION HELD; `--checker e97613c` historical → exit 2 REGRESSION-DETECTED) and verify the C9 watch check-log has exactly two distinct dated rows.

## Work performed

- Tree state verified before judging: HEAD `65838f8` ("lore r93: C1 venue repair + dossier + cert tool, C2 third cluster (Kojiki family), C3 watch re-check 2 + discriminate tool — work wave"), `git status --porcelain` empty; `git diff 65838f8 -- corpus/fixtures/check_bible.py corpus/tools/discriminate_check.py corpus/knowledge/r91-c9-watch.md` → `0` lines (judged artifacts are exactly the committed tree).
- Two 60s readiness wait-checks (both POLL_HIT immediately):
  - `bash .ufo/waves/poll_wait.sh corpus/tools/discriminate_check.py 60` → `POLL_HIT path=corpus/tools/discriminate_check.py elapsed=0s checks=0`, exit 0
  - `bash .ufo/waves/poll_wait.sh corpus/knowledge/r91-c9-watch.md 60` → `POLL_HIT path=corpus/knowledge/r91-c9-watch.md elapsed=0s checks=0`, exit 0
- Independent pin re-check: `sha256sum corpus/fixtures/check_bible.py` → `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py` (matches the PIN in the tool and the watch header).
- Ran both modes per the documented invocation (`corpus/tools/README.md:31-33`), from repo root, no scratch writes needed; outputs captured verbatim in the next section.
- Check-log row count: `sed -n '/## Check log/,/### /p' corpus/knowledge/r91-c9-watch.md | grep -c '^| 20'` → `2`.
- Before-state probes against baseline 87779a0 (read-only `git show`): tool absent (`git show 87779a0:corpus/tools/discriminate_check.py` → exit 128), baseline `corpus/tools/README.md` has 0 `discriminate` mentions, watch check-log had `1` dated row, baseline checker hashes to the same `ff9fd2aa…d1421` (checker unchanged across the round, as claimed).

## Before → after measurements

**Mode 1 — delivered (documented default):**

```sh
python3 corpus/tools/discriminate_check.py
```

```text
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
exit=0
```

**Mode 2 — historical `e97613c` checker (documented second command):**

```sh
python3 corpus/tools/discriminate_check.py --checker e97613c
```

```text
mode=e97613c checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
exit=2
```

**Check-log dated rows** (`corpus/knowledge/r91-c9-watch.md:47-50`):

```text
row 1: | 2026-10-17 | ff9fd2aa…(full 64 hex) | **DISCRIMINATION HELD** — all four C5 scenarios retained their r91 distinctions; no drift alarm.
row 2: | 2026-10-17 (r93) | ff9fd2aa…d1421 | **DISCRIMINATION HELD** — re-check 2 (seat X1, r93): all four gates reproduce; gate 3 not met; trigger unsatisfied; ruling retained. Next re-check: r94.
```

**Before → after (baseline 87779a0 → HEAD 65838f8):**

| Axis | 87779a0 | 65838f8 | Verdict |
|---|---|---|---|
| Lane tool | absent (exit 128 from `git show`) | `corpus/tools/discriminate_check.py`, documented invocation, stdlib-only | **improved** |
| Mode 1 behavior | n/a | exit 0, `RESULT: DISCRIMINATION HELD`, both fixtures exit 1 / stderr empty / README-exact / 1-line-pair diff vs baseline / semantic gate PASS | **improved** (claim proven) |
| Mode 2 behavior | n/a | exit 2, `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved` | **improved** (claim proven) |
| Check-log dated rows | 1 | 2 (distinct rows, both re-check narratives present in-file) | **improved** (claim proven) |
| Checker `corpus/fixtures/check_bible.py` | `ff9fd2aa…d1421` | same hash, `matches_pin=True` | **unchanged** (by design, as claimed; no harm) |
| Trade scan | — | every probe returned the documented outcome; no axis degraded | **no trade** |

## Findings & named debt

- Both claims hold exactly as stated: exit 0 HELD on delivered; exit 2 REGRESSION-DETECTED with the historical checker per the documented `--checker e97613c` invocation (`corpus/tools/README.md:33`).
- In mode 2 the per-fixture `pinned_semantic_gate=FAIL` / `README_exact=False` lines are the expected discriminator signal, not a tool malfunction: the tool evaluates those gates against the *selected* run (the baseline source fed via `git show`, no file created), whose documented behavior hedges the tick line and the null-chain line. The final `REGRESSION-DETECTED` verdict is what the promotion spec (`exit 0 HELD / exit 2 REGRESSION-DETECTED`) requires.
- Check-log nuance (observation, not harm): the two rows are distinct but share the calendar date `2026-10-17`, distinguished only by the `(r93)` suffix in the Date cell; row 2 also abbreviates the SHA-256 (`ff9fd2aa…d1421`) while row 1 carries the full 64 hex. A future reader counting *distinct calendar dates* would see one. If the r94 re-check row keeps the same date, consider a fuller date cell (e.g. `2026-10-17 (r94)`) — the current convention stays unambiguous only as long as the suffix is kept.
- Provenance note on row 1's narrative: it records the first re-check at HEAD `396c568` (r91 closure) while its `/tmp` scratch names carry an `r92` prefix — consistent with a re-check run during the r92 work wave against the r91-closure tree; no action needed.
- Out-of-scope context from the claims: the AST-anchor-validation debt named r94 lives in `corpus/tools/boundary_doc_check.py` (CERT tool), not in this harness; this seat found no new debt in `discriminate_check.py`. Its baseline expectation pull (`git show e97613cc276f…:corpus/fixtures/check_bible.py`) depends on that commit staying reachable — worth one line in any future prune/rewrite policy, but not actionable this round.

## Handoff

- Harness is lane-owned and self-contained (stdlib only, no scratch, no temp files); r94's C3 seat can reproduce this seat's battery with the two commands above plus the row-count grep.
- Per check-log row 2, the next scheduled C9 re-check is **r94**; it should append row 3 and, if the date still collides, keep the `(r94)` suffix convention.
- Checker remains pinned at `ff9fd2aa…d1421`; any drift alarm should first rerun mode 2 to confirm the harness still discriminates before reopening the r91 ruling.
- No blockers; nothing was committed, pushed, or written outside this followup report.
