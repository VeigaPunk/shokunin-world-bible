# F32 — checker-discriminator (FOLLOW-UP verification seat)

**Role:** Confirm r94 changed zero checker bytes, and that the durable discriminator still separates the delivered checker from the pre-repair baseline (positive run + expected negative control).

**Scope of this seat:** read-only checks. No corpus/, tool, fixture or sibling-report writes. Lane cwd `/home/vgpnk/Projects/shokunin/lore-shokunin`.

**Lane state at check time:** `HEAD = 65a93298cb100fdbf5732ac6de55f01a683c02d8`; ancestry confirmed `9c2eea3` → `abbc3e0` → `65a9329` (`git merge-base --is-ancestor` printed YES for both pairs). Working tree clean (`git status --porcelain` empty).

---

## Check 1 — no checker bytes changed in the r94 WORK range

**Claim under test:** `git diff 9c2eea3..abbc3e0 -- corpus/fixtures/check_bible.py` is empty.

```
$ git diff 9c2eea3..abbc3e0 -- corpus/fixtures/check_bible.py; echo "EXIT=$?"
EXIT=0
```

Output is empty — **zero bytes emitted**. Exit 0 (git diff exits 0 whether or not there is a diff; the empty body is the evidence). Redirected and measured to be certain:

```
$ git diff 9c2eea3..abbc3e0 -- corpus/fixtures/check_bible.py > /tmp/f32_cb.diff 2>&1; echo "diff_exit=$?"; wc -c /tmp/f32_cb.diff
diff_exit=0
0 /tmp/f32_cb.diff
```

**Independently corroborated four ways:**

| Evidence | Command | Observed |
|---|---|---|
| name-status empty | `git diff --name-status 9c2eea3..abbc3e0 -- corpus/fixtures/check_bible.py` | empty (no `M`/`A`/`D` row) |
| blob identical across the whole chain | `git rev-parse <rev>:corpus/fixtures/check_bible.py` | `20c56dbb90d9f59ca4fb85971154c0774f5ce0d0` at `9c2eea3`, at `abbc3e0`, and working tree (`git hash-object`) — all three equal |
| stat empty | `git diff 9c2eea3..abbc3e0 --stat -- corpus/fixtures/check_bible.py` | empty output, `EXIT2=0` |
| follow-up decl commit also clean | `git diff abbc3e0..65a9329 -- corpus/fixtures/check_bible.py` | empty; `git show --stat 65a9329` = `LOG.md \| 20 +++` only (1 file changed) |

**Adjacent-drift sweep (same range):**

- `git diff --name-status 9c2eea3..abbc3e0 -- corpus/tools/` → only `A corpus/tools/map-obligations-contract.json`, `A corpus/tools/map_obligations.py`. `corpus/tools/discriminate_check.py` is **untouched** (explicit query returned empty), so the discriminator used below is the same tool the WORK wave measured.
- `git diff --name-status 9c2eea3..abbc3e0 -- corpus/fixtures/` filtered of `r94-paired-crossing` → empty. The only fixture addition is the new r94 directory; no pre-existing fixture moved.
- Whole-range diff contains 115 lines *mentioning* the string `check_bible.py` (`git diff 9c2eea3..abbc3e0 | grep -c 'check_bible.py'` → `115`). These are textual references inside fixture READMEs / claim-excerpt maps / `.ufo` wave artifacts, **not** edits to the file — the name-status check above is the discriminator that rules out modification.

**Result: CONFIRMED — r94 changed no checker bytes.**

---

## Check 2 — discriminator on the delivered checker (expected exit 0)

```
$ python3 corpus/tools/discriminate_check.py; echo "EXIT=$?"
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
EXIT=0
```

**Quoted RESULT line:**

> `RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression`

Exit code **0** as expected. Both durable fixtures (`r91-c1-null-chain`, `r91-c1-tick-unresolved`) exit 1 with empty stderr, reproduce their README-delivered stdout exactly, and pass the pinned semantic gate. `changed_line_pairs=1/1` means the delivered checker differs from the e97613c baseline by exactly one output line per fixture — i.e. the discriminator has a real one-line signal to detect, not a vacuous pass.

---

## Check 3 — expected negative control on the pre-repair baseline (expected exit 2)

```
$ python3 corpus/tools/discriminate_check.py --checker e97613c; echo "EXIT=$?"
mode=e97613c checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
EXIT=2
```

**Quoted RESULT line:**

> `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present`

Exit code **2** as expected. Both fixtures' baseline outputs fail the delivered-semantics gate, so the discriminator is genuinely sensitive: it does not hold for the pre-repair baseline.

### Interpretation note on this mode (not a defect, but easy to misread)

`matches_pin=True` appears in **both** modes, and `README_exact=False` in the control mode. Neither is anomalous. Reading `corpus/tools/discriminate_check.py`:

- `corpus/tools/discriminate_check.py:82-85` always hashes the working-tree delivered checker and compares to `PIN`, regardless of mode. Hence `matches_pin=True` in both runs.
- `corpus/tools/discriminate_check.py:93` — `selected = new if mode == "delivered" else old`. The control mode does not swap in a different checker *file*; it runs the baseline source fetched by `baseline_source()` (`git show e97613cc...:corpus/fixtures/check_bible.py`, `discriminate_check.py:45-50`) through an exec wrapper (`discriminate_check.py:53-64`).
- `discriminate_check.py:109` prints `README_exact` as `selected.stdout == expected['the delivered checker']` — in control mode `selected` is the *baseline* output, so `False` is the correct and expected rendering, not a comparison failure.

So the control's meaning is precise: **the pre-repair baseline's output must fail the delivered-semantics gate → exit 2.** That is exactly what was observed. The baseline commit is real and genuinely different from delivered — `e97613cc276f5fa9cac49ff1900798cf6863c020` exists (`git cat-file -t` → `commit`), its checker blob is `c5cb5786986670ce1120574f045f80d23dc543cf` at 435 lines, versus delivered blob `20c56dbb90d9f59ca4fb85971154c0774f5ce0d0` at 428 lines (`wc -l corpus/fixtures/check_bible.py` → `428`).

### Determinism

Both invocations were run twice; output was byte-identical across runs:

```
delivered run1 exit=0   delivered run2 exit=0
e97613c  run1 exit=2    e97613c  run2 exit=2
delivered: identical across runs
e97613c: identical across runs
```

---

## Check 4 — the hash pin is real and consistent in three independent places

```
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py

$ grep -n '^PIN' corpus/tools/discriminate_check.py
12:PIN = "ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421"

$ python3 -c "import json;d=json.load(open('corpus/tools/boundary-doc-contract.json'));print(d['checker']['sha256'])"
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
```

`sha256sum`, the discriminator's `PIN` constant, and the independent boundary-doc contract all agree on `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`. The pin is not a stale constant pointing at a checker that no longer exists on disk.

---

## Check 5 — cross-check against the WORK-wave W21 artifacts

My two runs are **byte-identical** to W21's WORK-wave artifacts:

```
$ diff .ufo/waves/round-94/work/W21-discriminate-delivered.out /tmp/f32_d1.out && echo "delivered: byte-identical to W21"
delivered: byte-identical to W21
$ diff .ufo/waves/round-94/work/W21-discriminate-e97613c-short.out /tmp/f32_e1.out && echo "e97613c: byte-identical to W21 short-form"
e97613c: byte-identical to W21 short-form
```

- `.ufo/waves/round-94/work/W21-discriminate-e97613c-short.out` — `mode=e97613c ... pinned_semantic_gate=FAIL` on both fixtures, ending `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present`; `.exit` = `2`.
- `.ufo/waves/round-94/work/W21-discriminate-delivered.out` — `RESULT: DISCRIMINATION HELD ...`; `.exit` = `0`.

The WORK-wave measurement and this independent FOLLOW-UP re-measurement therefore agree at the byte level, on both the positive run and the control.

**Worth flagging to the L1 (already self-corrected by W21, no action needed):** W21's *first* control attempt, `.ufo/waves/round-94/work/W21-discriminate-e97613c.out`, recorded

```
discriminate_check.py: error: argument --checker: invalid choice: 'e97613cc276f5fa9cac49ff1900798cf6863c020' (choose from 'delivered', 'e97613c')
```

with `.exit` = `2`. That is an **argparse usage error whose exit code coincidentally equals the intended control's exit code (2)**. Had W21 stopped there, the seat would have reported a "passing" control for the wrong reason. W21.md (`W21.md`, "Gate runs" section) explicitly diagnosed this and re-ran the short form, producing the valid artifact above — so the WORK wave's final control evidence is sound. My independent re-run confirms the short form is the correct invocation and that the registry/tool accepts exactly `{delivered, e97613c}` (`discriminate_check.py:146`).

---

## Summary

| Check | Expected | Observed | Verdict |
|---|---|---|---|
| `git diff 9c2eea3..abbc3e0 -- corpus/fixtures/check_bible.py` | empty | empty, 0 bytes; blob `20c56db…` identical at both revs and worktree | PASS |
| `python3 corpus/tools/discriminate_check.py` | exit 0, DISCRIMINATION HELD | exit 0, `RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression` | PASS |
| `python3 corpus/tools/discriminate_check.py --checker e97613c` | exit 2, REGRESSION-DETECTED | exit 2, `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present` | PASS |

No counter-evidence found. No claim in this seat's brief was contradicted. One adjacent observation recorded for the L1: the discriminator's control mode exercises the *baseline source via `git show`*, not a second on-disk checker file, and reports `matches_pin=True` in both modes by design (`discriminate_check.py:82-85,93,109`) — correct behavior, but a reader could misread the mixed `matches_pin=True` / `README_exact=False` combination as a contradiction.

**Bottom line: PASS — r94 changed zero checker bytes (empty diff, identical blob `20c56dbb90d9f59ca4fb85971154c0774f5ce0d0` across 9c2eea3/abbc3e0/worktree), and the durable discriminator behaves exactly as specified: exit 0 `RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression` on delivered, exit 2 `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present` on the e97613c control, both deterministic across repeated runs.**
