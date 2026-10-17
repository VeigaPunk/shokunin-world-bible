# V48 — pins-c9 (round 97)

**Seat:** V48 `pins-c9`. Scope: reproduce the C9 checker pin, record the C9
watch state (the watch's own pointer at row 5 says the next re-check is r97 —
i.e. due now, re-check 6), confirm that V23 `gates-boundary`'s discriminator
result satisfies the watch's re-check requirement, and list the row-6
check-log append content for L1 (the watch file
`corpus/knowledge/r91-c9-watch.md` is not owned by any r97 producer, so this
seat does not write it).

**Report path (only file written by this seat):** this file. Scratch:
`.ufo/waves/round-97/seats/V48-scratch/` (absolute
`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V48-scratch/`,
captures + poll logs + block draft). No commit, no push, no network, no nested
agents.

**Baseline:** r96 closure `f3e09f9` (declared). `git rev-parse HEAD` →
`2393934237ea076366f3db6dceeff033edb52ab1` (r96 close — SCORECARD admitted
section; child of `f3e09f9`, touches `SCORECARD.md` only). Python 3.14.7. All
commands run from the lane repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin`. Run stamps below; final
re-verification §5 at 2026-10-17TXX:XX:XX-03:00.

## 1. Checker pin reproduced

```
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Three-way blob identity (captured 18:43):

```
$ echo "HEAD blob: $(git rev-parse HEAD:corpus/fixtures/check_bible.py)"
HEAD blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
$ echo "worktree blob: $(git hash-object corpus/fixtures/check_bible.py)"
worktree blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
$ echo "f3e09f9 blob: $(git rev-parse f3e09f9:corpus/fixtures/check_bible.py)"
f3e09f9 blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
$ echo "2393934 blob: $(git rev-parse 2393934:corpus/fixtures/check_bible.py)"
2393934 blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
```

This equals the pin at `corpus/knowledge/r91-c9-watch.md:6`, at
`corpus/tools/discriminate_check.py:12` (`PIN = "ff9fd2aa…"`), and is printed
by the discriminator itself as `matches_pin=True` in both modes (§3). The
historical baseline blob still hashes to the r90 gate-pair baseline:

```
$ git show e97613cc276f5fa9cac49ff1900798cf6863c020:corpus/fixtures/check_bible.py | sha256sum
e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556  -
```

No C9-pinned byte changed this round (checked at 18:43 and re-checked in §5):

```
$ git diff f3e09f9 -- corpus/fixtures/check_bible.py corpus/tools/discriminate_check.py \
    corpus/fixtures/r91-c1-null-chain corpus/fixtures/r91-c1-tick-unresolved corpus/knowledge/r91-c9-watch.md
(empty; rc=0)
```

Recorded for the round but pinned by no contract: `sha256sum
corpus/tools/discriminate_check.py` →
`6c7b7cd8b6676619c6f00eb692c946cfe8d007dc963de5c4a2114757f6108eef` (identical
to the r96 record).

## 2. C9 watch state — next re-check is r97 (due), ruling retained

Read of `corpus/knowledge/r91-c9-watch.md` (289 lines): the check log holds five
dated rows — rows 1–5 for r92–r96 — and row 5 (`…/r91-c9-watch.md:287`) reads
`Next re-check: r97.` The r97 round is therefore the due round for re-check 6.

The watch's durable pair, run verbatim by this seat (captured 18:43:37; stderr
0 bytes both modes):

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

Gate-3 probe rerun:

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

Identical to the r93–r96 statements. **Gate 3 remains not met; the four-gate
falsification trigger remains unsatisfied; the ruling is retained.** Nothing in
r97 authors sequence-scope evidence for `r91-c1-tick-unresolved` (the new
`r97-crossing-acknowledgment` fixture is a different directory and no claim
touches this gate).

## 3. V23's discriminator satisfies the watch — confirmed

V23 `gates-boundary`'s report landed at
`.ufo/waves/round-97/seats/V23-gates-boundary.md` (9,232 bytes; found by this
seat's foreground poll at try 15, 18:48:53). Its §3 discriminator blocks are
**byte-identical** to this seat's independent runs:

```
$ sed -n '62,67p' .ufo/waves/round-97/seats/V23-gates-boundary.md | diff .ufo/waves/round-97/seats/V48-scratch/delivered.out -
(empty; md5 fbf6ec9384fb5d52c6f616ae502f686a both sides)
$ sed -n '71,76p' .ufo/waves/round-97/seats/V23-gates-boundary.md | diff .ufo/waves/round-97/seats/V48-scratch/control.out -
(empty; md5 c775d3f2595f92eb590044d1ecb29648 both sides)
```

Captures: `V48-scratch/delivered.out|.err`, `control.out|.err`,
`v23-delivered-block.txt`, `v23-control-block.txt`. This is exactly the
row-3–row-5 re-check shape (fresh pin + `DISCRIMINATION HELD` + expected
`REGRESSION-DETECTED` control), so V23's discriminator **satisfies** the watch's
r97 re-check requirement, independently corroborated here. V23's side-claims
were also spot-reproduced by this seat:

- blob identity `20c56dbb…` at `f3e09f9`/`HEAD`/worktree — reproduced (§1);
- the control is real, not nominal: the `e97613c` blob hashes to `e2bb9639…`
  (distinct bytes) and both fixtures flip to `README_exact=False` /
  `pinned_semantic_gate=FAIL` under it — reproduced (§1, §2);
- V23 §6 ("final re-verification on the post-producer revision") was marked
  PENDING at read time (18:49); its §3 outputs — the content this seat's row-6
  block cites — are complete. Bounded as such.

## 4. Row-6 append content for L1 (listed, not written)

For L1 to append verbatim to `corpus/knowledge/r91-c9-watch.md` after line 289
(draft also in `V48-scratch/row6-block-draft.md`):

````markdown
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
````

## 5. Final re-verification (post-producer)

FILLED-LATER: re-run timestamps + outputs after producers land.

## Bounds

- This seat verifies the C9 pin and watch state only. It makes no statement
  about C1/C2/C3 claim content, the census, or the discriminator's reach beyond
  the two pinned r91 fixture classes.
- "No pinned byte changed" is a point-in-time confirmation plus the `f3e09f9`
  diff above; a later r97 producer write outside its declared byte-ownership
  would not be caught here. The pin and discriminator commands are cheap
  (<0.5 s) and were re-run in §5; L1 can re-run them at closure as the final
  check.
- Observed transiently in `git status` at 18:42–18:43: untracked
  `map-obligations-self-test-<suffix>/` dirs in the lane repo root (three
  different suffixes seen, all gone on re-check). Explained, not a breach:
  `corpus/tools/map_obligations.py:809` uses
  `tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)`
  (`ROOT` = lane repo root, line 79) — the self-test's scratch is created and
  auto-removed under the repo root. Recorded for the round's adjacency
  awareness; no pinned byte involved.
- The row-6 block above is a proposal for L1; it was not written to the watch
  file by this seat (no r97 producer owns that path). If L1 appends at closure,
  the wording "executed at the r97 wave (2026-10-17) on the delivered revision"
  may be adjusted to the closure formulation used by rows 1–5.

**Bottom line: PASS** — checker pin `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` reproduced (hash + blob identity at `f3e09f9`/`2393934`/worktree + historical `e97613c` blob `e2bb9639…`); C9 watch state is re-check 6 due at r97 with gate 3 still not met and the ruling retained; V23's discriminator (`DISCRIMINATION HELD` exit 0 / control `REGRESSION-DETECTED` exit 2, stderr empty) satisfies it and matches V48's independent runs byte-for-byte; row-6 append content listed above for L1.
