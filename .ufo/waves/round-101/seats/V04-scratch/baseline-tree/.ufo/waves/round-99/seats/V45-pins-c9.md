# V45 — pins-c9 (round 99)

**Seat:** V45 `pins-c9`. Scope: reproduce the C9 checker pin, record the C9
watch state (the watch's row 7 ends `Next re-check: r99` — due now, re-check 8),
confirm that V22 `gates-boundary`'s discriminator result satisfies the watch's
re-check requirement, and list the row-8 check-log append content for L1 (the
watch file `corpus/knowledge/r91-c9-watch.md` is owned by no r99 producer, so
this seat does not write it). Row-8 text is taken from V22's landed outputs,
not from a plan.

**Report path (only file written by this seat outside scratch):** this file.
Scratch: `.ufo/waves/round-99/seats/V45-scratch/` (absolute
`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V45-scratch/`;
captures, poll log, row-8 block draft). No commit, no push, no network, no
nested agents.

**Baseline:** r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`).
`git rev-parse HEAD` → `337f0fa52b02626b7687eedbb2d99fab30446fe4` (blocked-dispatch
LOG note; child of `111b9a3`, which is the r98 SCORECARD close, child of
`4265df5`). Python 3.14.7. All commands run from the lane repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin`. First battery captured
2026-10-18T01:02:17Z; final re-verification §5 at 2026-10-18T01:37:32Z; V22
report compared at 2026-10-18T01:53:07Z. Local date of the wave is 2026-10-17
(UTC had crossed midnight).

## 1. Checker pin reproduced

```
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Three-way blob identity (same at 01:02:17Z and again at 01:37:32Z):

```
$ echo "HEAD blob: $(git rev-parse HEAD:corpus/fixtures/check_bible.py)"
HEAD blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
$ echo "worktree blob: $(git hash-object corpus/fixtures/check_bible.py)"
worktree blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
$ echo "4265df5 blob: $(git rev-parse 4265df5:corpus/fixtures/check_bible.py)"
4265df5 blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
```

This equals the pin at `corpus/knowledge/r91-c9-watch.md:6`, the discriminator's
own `PIN` constant (`corpus/tools/discriminate_check.py:12`), the boundary
contract `checker.sha256`, and `git show 65838f867d6ece8e7b8bdcc4ffc667a08a1b785e:corpus/fixtures/check_bible.py | sha256sum`.
The discriminator prints it as `matches_pin=True` in both modes (§2). The
historical baseline blob still hashes to the r90 gate-pair baseline:

```
$ git show e97613cc276f5fa9cac49ff1900798cf6863c020:corpus/fixtures/check_bible.py | sha256sum
e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556  -
```

No C9-pinned byte changed this round (checked at 01:02 and re-checked in §5,
still empty at 01:53:07Z):

```
$ git diff 4265df5 -- corpus/fixtures/check_bible.py corpus/tools/discriminate_check.py \
    corpus/fixtures/r91-c1-null-chain corpus/fixtures/r91-c1-tick-unresolved corpus/knowledge/r91-c9-watch.md
(empty; rc=0)
$ git status --porcelain -- <same five paths>
(empty; rc=0)
```

Per-file sha256 of the two r91 fixture trees (6 files each) matched
`git show 4265df5:<path>` with zero diffs. Recorded for the round but pinned
by no C9 contract: `sha256sum corpus/tools/discriminate_check.py` →
`6c7b7cd8b6676619c6f00eb692c946cfe8d007dc963de5c4a2114757f6108eef` (identical
to `4265df5` and to the r96/r97/r98 record); watch-file hash
`ced043984ee1798de4442cf8a6a9f4eb2480244252eb9ae733b532ae327ab9dc` equals
`git show 4265df5:corpus/knowledge/r91-c9-watch.md`.

## 2. C9 watch state — next re-check is r99 (due), ruling retained

Read of `corpus/knowledge/r91-c9-watch.md` (321 lines): the check log's last
dated row is row 7 (`…/r91-c9-watch.md:319`) and reads `Next re-check: r99.`
The r99 round is therefore the due round for re-check 8. The file is
byte-identical to `4265df5`; this seat did not append the row.

The watch's durable pair, run verbatim by this seat (captured 01:02:17Z;
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

md5 of those two stdout captures: `fbf6ec9384fb5d52c6f616ae502f686a` (delivered)
and `c775d3f2595f92eb590044d1ecb29648` (control) — the same pair recorded by
the r97 and r98 pins-c9 seats. The discriminator output is byte-stable across
rounds.

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

Gate-3 probe rerun (01:02 and again 01:37, identical; capture
`V45-scratch/gate3-final.txt`):

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

Identical to the r93–r98 statements. **Gate 3 remains not met; the four-gate
falsification trigger remains unsatisfied; the ruling is retained.** Nothing
in the landed r99 fixture authors sequence-scope evidence for
`r91-c1-tick-unresolved`:

```
$ grep -RIl -E 'tick-unresolved|null-chain' corpus/fixtures/r99-window-lapse/
(no matches; rc=1)
```

`corpus/knowledge/r99-gate-blind-spot-table.md` and
`corpus/knowledge/r99-lapse-scope-note.md` were still absent at 01:53Z, so
that half could not be grepped. Their absence is not sequence-scope evidence.

## 3. V22's discriminator satisfies the watch — confirmed

V22 `gates-boundary`'s report landed at
`.ufo/waves/round-99/seats/V22-gates-boundary.md` (14,276 bytes, mtime
2026-10-17T22:41:56-0300 / 2026-10-18T01:41:56Z). This seat's poll cap had
already ended at 01:39:51Z (try 46); the report was found on a post-cap
presence check at 01:46:53Z. That is a late hit, recorded, not a plan: the
file was read and its discriminator blocks were diffed against this seat's
own captures.

Stdout blocks in the report (`sed -n '131,136p'` and `sed -n '140,145p'`,
which exclude the `$` command lines and the `[rc=N]` tags) are
**byte-identical** to this seat's independent runs:

```
$ diff -u V45-scratch/final-delivered.out V45-scratch/v22-report-delivered.txt
(empty)
$ diff -u V45-scratch/final-control.out V45-scratch/v22-report-control.txt
(empty)
$ md5sum V45-scratch/final-delivered.out V45-scratch/v22-report-delivered.txt
fbf6ec9384fb5d52c6f616ae502f686a  both
$ md5sum V45-scratch/final-control.out V45-scratch/v22-report-control.txt
c775d3f2595f92eb590044d1ecb29648  both
```

The same identity holds against V22's scratch final battery
(`V22-scratch/final-disc.out` / `final-disc-ctl.out`, rc files `[rc=0]` /
`[rc=2]`, stderr 0 bytes, stamped 2026-10-18T01:31:52Z) and against the
discriminator blocks in `V22-scratch/early-gates.txt` (that file's own header
says it is not the quoted final battery; the report is). V22's report does
not mention the watch or a row-8 append; producing that append is this seat's
job, from those outputs.

This is exactly the row-3–row-7 re-check shape (fresh pin + `DISCRIMINATION
HELD` + expected `REGRESSION-DETECTED` control), so V22's discriminator
**satisfies** the watch's r99 re-check requirement, independently corroborated
here. Side-claims this seat reproduced:

- checker pin three-way (contract `checker.sha256` = discriminator `PIN` =
  worktree sha256 = `git show 65838f86:corpus/fixtures/check_bible.py`) —
  all four equal `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`;
- the control is real, not nominal: the `e97613c` blob hashes to `e2bb9639…`
  (distinct bytes) and both fixtures flip to `README_exact=False` /
  `pinned_semantic_gate=FAIL` under it;
- the five C9 paths (checker, discriminator, both r91 fixture dirs, watch)
  are byte-identical to `4265df5` and clean in `git status`.

Not re-run here, so not claimed: V22's `boundary_doc_check.py` default /
`--self-test` results, the 86-path pin census (`checked 86 unique 86 bad 0`),
and the mutated-doc control. Those are V22's gate claims. They are not inputs
to the row-8 append.

## 4. Row-8 append content for L1 (listed, not written)

For L1 to append verbatim to `corpus/knowledge/r91-c9-watch.md` after line 321
(draft also in `V45-scratch/row8-block-draft.md`). The r98 closure row that
landed was shorter than the r98 pins-c9 proposal; L1 may condense this the
same way. The facts below are the ones V22's report and this seat both
observed.

````markdown
## 2026-10-17 — r99 re-check (eighth)

Eighth periodic re-check, executed at the r99 wave (2026-10-17) on the
delivered revision; the discriminator pair was run by seat V22 `gates-boundary`
and independently reproduced byte-for-byte by seat V45 `pins-c9`. Checker byte
pin verified fresh:

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Discriminator pair from the repository root: `python3 corpus/tools/discriminate_check.py`
→ `RESULT: DISCRIMINATION HELD` (exit 0); `python3 corpus/tools/discriminate_check.py --checker e97613c`
→ `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved` (exit 2,
expected control). stderr empty in both modes; the checker blob `20c56dbb…` is
identical at `4265df5` (declared baseline), `337f0fa` (HEAD), and the worktree.

| Date | Checker SHA-256 | Discrimination re-check |
|---|---|---|
| 2026-10-17 (r99) | `ff9fd2aa…d1421` | **DISCRIMINATION HELD** — re-check 8 (r99): delivered discrimination held; `e97613c` control REGRESSION-DETECTED as expected; ruling retained. Next re-check: r100. |

Gate 3 remains **not met**; the four-gate falsification trigger remains
unsatisfied; nothing in r99 changes the sequence-scope evidence state (the
sequence-scope probe rerun from the repository root again printed
`excerpt_files=` and `readme_line3=Fixture scaffolding only; not sourced story
evidence.`; `grep -RIl -E 'tick-unresolved|null-chain' corpus/fixtures/r99-window-lapse/`
→ no matches, rc=1).
````

## 5. Final re-verification (2026-10-18T01:37:32Z, before the V22 report compare)

Re-run of the pin + discriminator pair after S3 and S4 reports had landed.
None of the producer-owned paths is in the C9-pinned set. At that timestamp
the tracked delta vs `4265df5` was `LOG.md`, `SCORECARD.md`,
`corpus/tools/dependency_freeze.py`, and
`corpus/tools/dependency-freeze-contract.json` (the last two worktree-dirty;
S1's owned paths). Untracked: `.ufo/waves/round-99/` and
`corpus/fixtures/r99-window-lapse/`.

```
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
$ echo "HEAD blob: $(git rev-parse HEAD:corpus/fixtures/check_bible.py)"
HEAD blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
$ echo "worktree blob: $(git hash-object corpus/fixtures/check_bible.py)"
worktree blob: 20c56dbb90d9f59ca4fb85971154c0774f5ce0d0

$ python3 corpus/tools/discriminate_check.py            # exit 0, stderr 0 bytes
(delivered block; diff vs the 01:02 capture empty — byte-identical)
$ python3 corpus/tools/discriminate_check.py --checker e97613c   # exit 2, stderr 0 bytes
(control block; diff vs the 01:02 capture empty — byte-identical)

$ git diff 4265df5 -- <the five C9-pinned paths>   # empty; rc=0
$ git status --porcelain -- <the five C9-pinned paths>   # empty; rc=0
```

The five-path diff and status were empty again at 01:53:07Z, after V22's
report had been read. Final captures: `V45-scratch/final-delivered.out|.err`,
`final-control.out|.err`, `gate3-final.txt`, `final-sha.txt`.

## Bounds

- This seat verifies the C9 pin and watch state only. It makes no statement
  about C1/C2 claim content, the census, `boundary_doc_check.py`, or the
  discriminator's reach beyond the two pinned r91 fixture classes.
- "No pinned byte changed" is a point-in-time confirmation plus the `4265df5`
  diff/status above (last empty check 01:53:07Z). A later write outside the
  declared byte-ownership would not be caught here. The pin and discriminator
  commands are cheap (<0.5 s); L1 can re-run them at closure as the final
  check.
- The watch file remains at 321 lines with row 7 as its last row. The r99
  row-8 append is closure work — no r99 producer owns the watch path.
- Poll record (`V45-scratch/poll.log`): tries 1–30, then the first poller was
  killed by the tool's 600s timeout (try 30 at 01:13:59Z). Continuation tries
  31–40 started at 01:34:31Z (gap recorded, not a reset). Stall-escape tries
  41–46 ended `V22-ABSENT` at 01:39:51Z. The report file itself landed at
  01:41:56Z and was read at 01:46:53Z. SELF was never polled. The poll looked
  for producer names `S1-freeze-hygiene.md` / `S2-tools-docs.md` /
  `S5-knowledge-notes.md` (r98 names). At 01:53Z the landed producer reports
  were `S1-full-file-pins.md`, `S3-fixture-author.md`, and
  `S4-fixture-docs.md`. S2 and S5 reports were still absent. That name miss
  does not touch the C9 pin.
- V22's own poll also exhausted with S1/S2/S5 absent under those r98 names
  (their §7). Their discriminator battery is complete anyway; the missing
  producer reports are not an input to this row.

**Bottom line: PASS** — checker pin `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` reproduced (hash + blob identity at `4265df5`/`337f0fa`/worktree + historical `e97613c` blob `e2bb9639…`), stable across the §5 re-run with the five-path set diff-clean; C9 watch state is re-check 8 due at r99 with gate 3 still not met and the ruling retained; V22 `gates-boundary`'s discriminator (`DISCRIMINATION HELD` exit 0 / control `REGRESSION-DETECTED` exit 2, stderr empty) satisfies it and matches this seat's independent runs byte-for-byte (md5 `fbf6ec93…` / `c775d3f2…`); row-8 append content listed above for L1, not written to the watch.
