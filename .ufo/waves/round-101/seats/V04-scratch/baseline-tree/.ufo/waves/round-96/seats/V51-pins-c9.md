# V51 — pins-c9 (round 96)

**Seat:** V51 `pins-c9`. Scope: reproduce the C9 checker pin, record the C9 watch
state (the watch's own pointer says the next re-check is r96 — i.e. due now),
confirm that V26 `gates-boundary`'s discriminator result satisfies the watch's
re-check requirement, and list the row-5 check-log append content for L1 (the
watch file `corpus/knowledge/r91-c9-watch.md` is not owned by any r96 producer,
so this seat does not write it).

**Report path (only file written by this seat):** this file. Scratch:
`.ufo/waves/round-96/seats/V51-scratch/` (absolute
`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats/V51-scratch/`,
4 capture files). No commit, no push, no network, no nested agents.

**Baseline:** r95 closure `dcb2d92`; `git rev-parse HEAD` →
`60dba0c2aa344860b10a2fc63e00468d1b134f27` (r95 close — SCORECARD admitted
section; `dcb2d92..HEAD` touches `SCORECARD.md` only). All commands run from the
lane repo root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Final run stamps:
2026-10-17T17:42:18-03:00 (V51) and 2026-10-17T17:41:00-03:00 (V26).

## 1. Checker pin reproduced

```
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

This equals the pin at `corpus/knowledge/r91-c9-watch.md:6`, at
`corpus/tools/discriminate_check.py:12` (`PIN = "ff9fd2aa…"`), and is printed by
the discriminator itself as `matches_pin=True` in both modes (§3). Cross-checks:

```
$ echo "HEAD blob: $(git rev-parse HEAD:corpus/fixtures/check_bible.py)"
HEAD blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
$ echo "worktree blob: $(git hash-object corpus/fixtures/check_bible.py)"
worktree blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
$ echo "dcb2d92 blob: $(git rev-parse dcb2d92:corpus/fixtures/check_bible.py)"
dcb2d92 blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0

$ git show e97613cc276f5fa9cac49ff1900798cf6863c020:corpus/fixtures/check_bible.py | sha256sum
e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556  -
```

The historical baseline blob hashes to `e2bb9639…`, matching the `e97613c`
checker SHA-256 pinned in `.ufo/waves/round-91/patches/B3-before-state.json`
(`{"e97613c": {"sha256": "e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556"…}`).
The discriminator's `BASELINE = "e97613cc276f5fa9cac49ff1900798cf6863c020"`
(`discriminate_check.py:13`) is therefore a real commit in this repo and the
control exercises genuine historical bytes.

```
$ git diff --stat dcb2d92 -- corpus/fixtures/check_bible.py corpus/tools/discriminate_check.py \
    corpus/fixtures/r91-c1-null-chain corpus/fixtures/r91-c1-tick-unresolved corpus/knowledge/r91-c9-watch.md
(empty; rc=0)
```

No pinned byte changed between the r95 closure and the live tree. Recorded for
the round but pinned by no contract: `sha256sum corpus/tools/discriminate_check.py`
→ `6c7b7cd8b6676619c6f00eb692c946cfe8d007dc963de5c4a2114757f6108eef` (identical
in V26 §0).

## 2. C9 watch state — next re-check is r96 (due), ruling retained

Read of `corpus/knowledge/r91-c9-watch.md` (273 lines): the check log holds four
dated rows — row 1 (r92, first periodic re-check), row 2 (r93, seat X1), row 3
(r94), row 4 (r95, `…/r91-c9-watch.md:271`) — and row 4's pointer reads
`Next re-check: r96.` The r96 round is therefore the due round for re-check 5.

The watch's durable pair, run verbatim by this seat:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None
1 violation(s); no canon changed
exit=1

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed
exit=1
```

Both outputs are exactly the wording recorded in the watch's first periodic
re-check section (lines 84 and 93–97). Gate-3 probe rerun:

```
$ python3 - <<'PY'
from pathlib import Path
root=Path('corpus/fixtures/r91-c1-tick-unresolved')
print('excerpt_files='+','.join(sorted(p.name for p in root.glob('*excerpt*'))))
print('readme_line3='+root.joinpath('README.md').read_text(encoding='utf-8').splitlines()[2])
PY
excerpt_files=
readme_line3=Fixture scaffolding only; not sourced story evidence.
```

Identical to the r93 clarification and r94/r95 statements. **Gate 3 remains not
met; the four-gate falsification trigger remains unsatisfied; the ruling is
retained.** Nothing in r96 authors sequence-scope evidence for
`r91-c1-tick-unresolved` (the new `r96-crossing-response` fixture is a different
directory and no claim touches this gate).

## 3. V26's discriminator satisfies the watch — confirmed

V26's report landed at `.ufo/waves/round-96/seats/V26-gates-boundary.md` (12,240
bytes, complete; found by foreground poll at 17:41). Its §3 discriminator block
is **byte-identical** to this seat's independent runs:

```
$ python3 corpus/tools/discriminate_check.py            # captured 17:42:18-03:00, exit 0, stderr 0 bytes
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression

$ python3 corpus/tools/discriminate_check.py --checker e97613c   # exit 2, stderr 0 bytes
mode=e97613c checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
```

Captures: `V51-scratch/delivered.out|.err`, `control.out|.err`. This is exactly
the row-3/row-4 re-check shape (fresh pin + `DISCRIMINATION HELD` + expected
`REGRESSION-DETECTED` control), so V26's discriminator **satisfies** the watch's
r96 re-check requirement, and it is independently corroborated here. Two of
V26's side-claims were also spot-reproduced by this seat:

- blob identity `20c56dbb…` at `dcb2d92` / `HEAD` / worktree — reproduced (§1);
- `/tmp` inode exhaustion — reproduced: `df -i /tmp | tail -2` →
  `tmpfs 1048576 1048576 0 100% /tmp`. Any seat redirecting to `/tmp` may lose
  its capture silently; V51 wrote all captures under `V51-scratch/`.

## 4. Row-5 append content for L1 (listed, not written)

For L1 to append verbatim to `corpus/knowledge/r91-c9-watch.md` after line 273:

````markdown
## 2026-10-17 — r96 re-check (fifth)

Fifth periodic re-check, executed at the r96 closure (2026-10-17); the
discriminator pair was run by seat V26 `gates-boundary` and independently
reproduced byte-for-byte by seat V51 `pins-c9`. Checker byte pin verified fresh:

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Discriminator pair from the repository root: `python3 corpus/tools/discriminate_check.py`
→ `RESULT: DISCRIMINATION HELD` (exit 0); `python3 corpus/tools/discriminate_check.py --checker e97613c`
→ `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved` (exit 2,
expected control). stderr empty in both modes; the checker blob `20c56dbb…` is
identical at `dcb2d92`, `HEAD`, and the worktree.

| Date | Checker SHA-256 | Discrimination re-check |
|---|---|---|
| 2026-10-17 (r96) | `ff9fd2aa…d1421` | **DISCRIMINATION HELD** — re-check 5 (r96): delivered discrimination held; `e97613c` control REGRESSION-DETECTED as expected; ruling retained. Next re-check: r97. |

Gate 3 remains **not met**; the four-gate falsification trigger remains
unsatisfied; nothing in r96 changes the sequence-scope evidence state (the
sequence-scope probe rerun from the repository root again printed
`excerpt_files=` and `readme_line3=Fixture scaffolding only; not sourced story
evidence.`).
````

## Bounds

- This seat verifies the C9 pin and watch state only. It makes no statement
  about C1/C2/C3 claim content, the census, or the discriminator's reach beyond
  the two pinned r91 fixture classes.
- "No pinned byte changed" is a point-in-time confirmation (17:42) plus the
  `dcb2d92` diff above; a later r96 producer write outside its declared
  byte-ownership would not be caught here. The pin and discriminator commands
  are cheap (<0.5 s) and can be re-run at closure as the final check.
- The row-5 block above is a proposal for L1; it was not written to the watch
  file by this seat (no r96 producer owns that path).

**Bottom line: PASS** — checker pin `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` reproduced (hash + blob identity at `dcb2d92`/`HEAD`/worktree + historical `e97613c` blob `e2bb9639…` matching B3's pin); C9 watch state is re-check 5 due at r96 with gate 3 still not met and the ruling retained; V26's discriminator (`DISCRIMINATION HELD` exit 0 / control `REGRESSION-DETECTED` exit 2) satisfies it and matches V51's independent runs byte-for-byte; row-5 append content listed above for L1.
