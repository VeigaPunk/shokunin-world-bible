# V43 — pins-c9 (round 98)

**Seat:** V43 `pins-c9`. Scope: reproduce the C9 checker pin, record the C9
watch state (the watch's row 6 ends `Next re-check: r98` — due now, re-check 7),
confirm that V19 `gates-boundary`'s discriminator result satisfies the watch's
re-check requirement, and list the row-7 check-log append content for L1 (the
watch file `corpus/knowledge/r91-c9-watch.md` is owned by no r98 producer, so
this seat does not write it).

**Report path (only file written by this seat):** this file. Scratch:
`.ufo/waves/round-98/seats/V43-scratch/` (absolute
`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats/V43-scratch/`;
captures + poll log + row-7 block draft). No commit, no push, no network, no
nested agents.

**Baseline:** r97 closure `9a3d648` (declared). `git rev-parse HEAD` →
`dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb` (r97 close — SCORECARD admitted
section; child of `9a3d648`, touches `SCORECARD.md` only). Python 3.14.7. All
commands run from the lane repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin`. First battery captured
23:28:20–23:28:27 UTC; final re-verification §5 run at 23:39:19 UTC.

## 1. Checker pin reproduced

```
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Three-way blob identity:

```
$ echo "HEAD blob: $(git rev-parse HEAD:corpus/fixtures/check_bible.py)"
HEAD blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
$ echo "worktree blob: $(git hash-object corpus/fixtures/check_bible.py)"
worktree blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
$ echo "9a3d648 blob: $(git rev-parse 9a3d648:corpus/fixtures/check_bible.py)"
9a3d648 blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
```

This equals the pin at `corpus/knowledge/r91-c9-watch.md:6`, the discriminator's
own `PIN` constant (`corpus/tools/discriminate_check.py:12`), and is printed by
the discriminator itself as `matches_pin=True` in both modes (§2). The
historical baseline blob still hashes to the r90 gate-pair baseline:

```
$ git show e97613cc276f5fa9cac49ff1900798cf6863c020:corpus/fixtures/check_bible.py | sha256sum
e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556  -
```

No C9-pinned byte changed this round (checked at 23:28 and re-checked in §5):

```
$ git diff 9a3d648 -- corpus/fixtures/check_bible.py corpus/tools/discriminate_check.py \
    corpus/fixtures/r91-c1-null-chain corpus/fixtures/r91-c1-tick-unresolved corpus/knowledge/r91-c9-watch.md
(empty; rc=0)
$ git status --porcelain -- <same five paths>
(empty; rc=0)
```

Recorded for the round but pinned by no contract: `sha256sum
corpus/tools/discriminate_check.py` →
`6c7b7cd8b6676619c6f00eb692c946cfe8d007dc963de5c4a2114757f6108eef` (identical
to the r96/r97 record); watch-file hash `10245618b5eb8fb9258c20139a03897b5582582e7176a46113c549e80228c135`
equals `git show 9a3d648:corpus/knowledge/r91-c9-watch.md` (byte-identical).

## 2. C9 watch state — next re-check is r98 (due), ruling retained

Read of `corpus/knowledge/r91-c9-watch.md` (305 lines): the check log holds six
dated rows — rows 1–6 for r92–r97 — and row 6 (`…/r91-c9-watch.md:305`) reads
`Next re-check: r98.` The r98 round is therefore the due round for re-check 7.

The watch's durable pair, run verbatim by this seat (captured 23:28:26–27 UTC;
stderr 0 bytes both modes):

```
$ python3 corpus/tools/discriminate_check.py            # exit 0
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression

$ python3 corpus/tools/discriminate_check.py --checker e97613c   # exit 2
mode=e97613c checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
```

The two durable fixtures were also run directly (the watch's "Reproducible
boundary probe"), exit 1 both, stderr empty:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None
1 violation(s); no canon changed

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed
```

Both match the watch's stated expectations exactly (definite integer tick
finding; separately qualified chain-break line; one deliberate
invalid-duplicate row diagnostic).

Gate-3 probe rerun (23:28 and again 23:39, identical):

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

Identical to the r93–r97 statements. **Gate 3 remains not met; the four-gate
falsification trigger remains unsatisfied; the ruling is retained.** Nothing in
r98 authors sequence-scope evidence for `r91-c1-tick-unresolved`: the new
`r98-clerk-filing` fixture is a different directory and does not touch the
class — `grep -rl "tick-unresolved\|null-chain" corpus/fixtures/r98-clerk-filing/`
→ no matches, rc=1.

## 3. V19's discriminator satisfies the watch — confirmed

V19 `gates-boundary`'s report landed at
`.ufo/waves/round-98/seats/V19-gates-boundary.md` (11,694 bytes, mtime
23:37:47 UTC; found by this seat's foreground poll at try 28/40, 23:37:57 UTC —
ALL-PRESENT: V19 report + S1–S5 producer reports + all declared artifacts).
Its §3 discriminator blocks are **byte-identical** to this seat's independent
runs:

```
$ sed -n '69,74p' .ufo/waves/round-98/seats/V19-gates-boundary.md | diff .ufo/waves/round-98/seats/V43-scratch/delivered.out -
(empty; md5 fbf6ec9384fb5d52c6f616ae502f686a both sides)
$ sed -n '78,83p' .ufo/waves/round-98/seats/V19-gates-boundary.md | diff .ufo/waves/round-98/seats/V43-scratch/control.out -
(empty; md5 c775d3f2595f92eb590044d1ecb29648 both sides)
```

The md5 pair is the same pair recorded by the r97 seats (V23/V48) — the
discriminator output is byte-stable across rounds. This is exactly the
row-3–row-6 re-check shape (fresh pin + `DISCRIMINATION HELD` + expected
`REGRESSION-DETECTED` control), so V19's discriminator **satisfies** the
watch's r98 re-check requirement, independently corroborated here. V19's
side-claims were also spot-reproduced by this seat:

- checker pin three-way agreement (contract `checker.sha256` = discriminator
  `PIN` = delivered bytes) — reproduced in §1 (the contract half is V19's
  `pin-provenance.txt` result, `checker three-way equal: True`; the delivered
  half is this seat's hash);
- the control is real, not nominal: the `e97613c` blob hashes to `e2bb9639…`
  (distinct bytes) and both fixtures flip to `README_exact=False` /
  `pinned_semantic_gate=FAIL` under it — reproduced (§1, §2);
- V19's wider pinned set (21 paths / 68 tracked files: boundary doc + checker +
  boundary contract + both gate scripts + 14 replayed fixture dirs + the two
  r91 READMEs) is byte-identical to `9a3d648` and HEAD; the two r91
  discriminator READMEs in that set are covered by this seat's five-path
  diff/status as well.
- Secondary corroboration, same round: V22 `doc-parity` §2d independently ran
  the same pair at 20:35 (report §2d) with the same pin/exit results and
  records the r98 watch row as due/absent; V15 `c3-r95-repair` confirmed the
  `check_bible.py` pin equal to `git show 9a3d648:<path>` at pre-run time.

## 4. Row-7 append content for L1 (listed, not written)

For L1 to append verbatim to `corpus/knowledge/r91-c9-watch.md` after line 305
(draft also in `V43-scratch/row7-block-draft.md`):

````markdown
## 2026-10-17 — r98 re-check (seventh)

Seventh periodic re-check, executed at the r98 wave (2026-10-17) on the
delivered revision; the discriminator pair was run by seat V19 `gates-boundary`
and independently reproduced byte-for-byte by seat V43 `pins-c9`. Checker byte
pin verified fresh:

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Discriminator pair from the repository root: `python3 corpus/tools/discriminate_check.py`
→ `RESULT: DISCRIMINATION HELD` (exit 0); `python3 corpus/tools/discriminate_check.py --checker e97613c`
→ `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved` (exit 2,
expected control). stderr empty in both modes; the checker blob `20c56dbb…` is
identical at `9a3d648` (declared baseline), `dd4df1b` (HEAD), and the worktree.

| Date | Checker SHA-256 | Discrimination re-check |
|---|---|---|
| 2026-10-17 (r98) | `ff9fd2aa…d1421` | **DISCRIMINATION HELD** — re-check 7 (r98): delivered discrimination held; `e97613c` control REGRESSION-DETECTED as expected; ruling retained. Next re-check: r99. |

Gate 3 remains **not met**; the four-gate falsification trigger remains
unsatisfied; nothing in r98 changes the sequence-scope evidence state (the
sequence-scope probe rerun from the repository root again printed
`excerpt_files=` and `readme_line3=Fixture scaffolding only; not sourced story
evidence.`; `grep -rl "tick-unresolved\|null-chain" corpus/fixtures/r98-clerk-filing/`
→ no matches, rc=1).
````

## 5. Final re-verification (post-producer, 2026-10-17T23:39:19Z)

Re-run of the pin + discriminator pair after all producer reports and V19's
report had landed (none of the producer-owned paths is in the C9-pinned set;
the settled change set was exactly the declared ownership: S1
`dependency_freeze.py` + contract, S2 `tools/README.md`, S3 r95 map + r98
fixture, S4 r98 fixture docs, S5 knowledge notes + addenda, plus the L1 round
declaration in `LOG.md`):

```
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
$ echo "HEAD blob: $(git rev-parse HEAD:corpus/fixtures/check_bible.py)"
HEAD blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
$ echo "worktree blob: $(git hash-object corpus/fixtures/check_bible.py)"
worktree blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0

$ python3 corpus/tools/discriminate_check.py            # exit 0, stderr 0 bytes
(delivered block; diff vs earlier capture empty — byte-identical)
$ python3 corpus/tools/discriminate_check.py --checker e97613c   # exit 2, stderr 0 bytes
(control block; diff vs earlier capture empty — byte-identical)

$ git diff 9a3d648 -- <the five C9-pinned paths>   # empty; rc=0
$ git status --porcelain -- <the five C9-pinned paths>   # empty; rc=0
```

Final captures: `V43-scratch/final-delivered.out|.err`,
`final-control.out|.err`, `gate3-final.txt`.

## Bounds

- This seat verifies the C9 pin and watch state only. It makes no statement
  about C1/C2/C3 claim content, the census, or the discriminator's reach beyond
  the two pinned r91 fixture classes.
- "No pinned byte changed" is a point-in-time confirmation plus the `9a3d648`
  diff/status above; a later r98 write outside the declared byte-ownership
  would not be caught here. The pin and discriminator commands are cheap
  (<0.5 s) and were re-run in §5; L1 can re-run them at closure as the final
  check.
- The watch file remains at 305 lines with row 6 as its last row; the r98
  row-7 append is closure work — no r98 producer owns the watch path (V22 §2d
  and V19's bounds say the same).
- Count note (not a finding): the seat brief's phrase "byte copies of the
  other 7 files from `9a3d648`" — the r97 fixture holds 10 files total, 4 of
  which S3 authored for r98, so 6 files are preserving copies (all observed
  byte-identical to `r97-crossing-acknowledgment` at 23:28; the two S4-owned
  docs `README.md` / `claim-excerpt-map.md` were among those copies until S4
  landed its versions at ~23:33, per ownership). If the brief's count included
  the r95 map repair, it reconciles. No C9-pinned path involved.
- Poll record: single-seat poll (`V43-scratch/poll.sh`, log `poll.log`), 20 s
  cadence, ALL-PRESENT at try 28/40 (23:37:57 UTC); the last missing item was
  V19's report (found 10 s after its mtime). No all-reports wait was needed
  (SELF subtracted by construction — this seat never polled for its own
  report); no stall escape required.

**Bottom line: PASS** — checker pin `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` reproduced (hash + blob identity at `9a3d648`/`dd4df1b`/worktree + historical `e97613c` blob `e2bb9639…`), stable across the §5 post-producer re-run with the five-path set diff-clean; C9 watch state is re-check 7 due at r98 with gate 3 still not met and the ruling retained; V19 `gates-boundary`'s discriminator (`DISCRIMINATION HELD` exit 0 / control `REGRESSION-DETECTED` exit 2, stderr empty) satisfies it and matches this seat's independent runs byte-for-byte (md5 `fbf6ec93…` / `c775d3f2…`); row-7 append content listed above for L1.
