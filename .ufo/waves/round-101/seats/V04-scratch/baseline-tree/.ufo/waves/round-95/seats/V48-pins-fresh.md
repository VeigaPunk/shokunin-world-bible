# V48 — pins-fresh (round 95)

- Seat: V48 pins-fresh. Round 95, single wave, baseline r94 closure `fb118c4`.
- Repo root: `/home/vgpnk/Projects/shokunin/lore-shokunin`; all commands run from
  repo root with `python3`.
- Observed tree: `HEAD = fb118c42038ed27a747eec704b9aab41bb4b2ebe` (= baseline).
  Window: 2026-10-17 16:16–16:31 local (19:16–19:31 UTC).
- Scope per seat spec: (1) checker pin reproduced by `sha256sum`; (2) C9 watch
  file state — the `Next re-check: r95` pointer from the r94 closure; (3) confirm
  the round's own discriminator run (V17) satisfies that due check, listing what
  L1 must append (row 4) with the exact outputs to cite. Read-only; no corpus
  writes; no commits.

## 1. Checker pin reproduced

```sh
sha256sum corpus/fixtures/check_bible.py
```

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Matches the C9 watch pin (`corpus/knowledge/r91-c9-watch.md:6`, `:73`, `:226`)
exactly, and the same digest is declared at four further independent sites,
all consistent: `corpus/tools/discriminate_check.py:12` (`PIN = "ff9fd2aa…"`),
`corpus/tools/boundary-doc-contract.json:12` (`checker.sha256`),
`corpus/fixtures/README.md:1091`, and the r94 closure records
(`LOG.md:2659`, `:2671`, `:2719-2721`). No byte drift at the delivered revision:

```sh
git status --porcelain -- corpus/fixtures/check_bible.py
```

```text
(empty)
```

The round's producer writes (P1 `map_obligations.py`, P2
`map-obligations-contract.json` + `corpus/tools/README.md`, P5 scope note) are
visible as `M`/`??` in `git status`, but none of them touches a pinned byte:
`git diff --stat HEAD -- corpus/fixtures/check_bible.py
corpus/tools/discriminate_check.py corpus/knowledge/r91-c9-watch.md
corpus/knowledge/holder-assessment-boundary.md` → empty, rc=0. Boundary doc pin
also reproduces: `sha256sum corpus/knowledge/holder-assessment-boundary.md` →
`7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e`, equal to
`boundary-doc-contract.json` `document.sha256`.

## 2. C9 watch file state — the r95 due check

`corpus/knowledge/r91-c9-watch.md`: 257 lines, sha256
`38511f6625edb35721041463adc61cf7671306fe176eab7520dc4a6972393087` (stable
across my whole window: same hash at first and last read).

- The check-log carries rows 1–3: row 1 = first periodic re-check (r92), row 2 =
  r93 (seat X1), row 3 = r94 closure. The r94 row (`:253`) ends
  **"Next re-check: r95."** — the pointer is present and fresh.
- `grep -n "r95" corpus/knowledge/r91-c9-watch.md` → exactly one match, `:253`
  (the pointer itself). There is **no r95 section and no r95 row yet**: the
  fourth periodic re-check is **due this round and unappended**.
- The due-check definition comes from the r94 precedent
  (`.ufo/waves/round-94/work/W21.md` §"Due C9 watch review"): "the pinned
  checker hash, both repo-relative r91 fixture commands, and the registered
  discriminator". The r94 append itself recorded the hash plus the discriminator
  pair (delivered + `e97613c` control) in a dated section with a table row.

## 3. V17's round-95 run satisfies the due check

V17's report is `.ufo/waves/round-95/seats/V17-gates-boundary.md` (9327 bytes,
stable). Its §1.3–1.5 carry the due-check legs; I compared them line-by-line
against the pinned expectations and against my own independent runs:

| Leg | V17 evidence | My V48 corroboration | Match |
|---|---|---|---|
| checker hash | §1.5 → `ff9fd2aa…d1421  corpus/fixtures/check_bible.py` | same command, same output | exact |
| discriminator delivered | §1.3 full stdout, `EXIT=0` | rerun: byte-identical stdout, exit 0 | exact |
| discriminator control | §1.4 full stdout, `EXIT=2` | rerun: byte-identical stdout, exit 2 | exact |
| r91 fixture commands | executed inside the discriminator (`delivered_run`/`baseline_run` on both fixtures, `README_exact=True`) | also ran both standalone: null-chain exit 1 (1 violation line), tick-unresolved exit 1 (3 violation lines), matching the watch record | exact |

Stronger than a visual compare: I captured my delivered-mode stdout to
`/tmp/v48-disc-now.txt` and `diff`ed it against V17's own scratch captures
`seats/scratch/V17/disc1.txt` and `disc2.txt` —

```text
IDENTICAL to V17 disc1
IDENTICAL to V17 disc2
```

V17 also ran the boundary gate (default `CERTIFIED` exit 0; `--self-test` 8/8
PASS) and a 600 s pin watcher over the round window (13 change points, zero pin
violations). V20's report (`V20-doc-parity.md` §C) independently captured the
same three receipts, making three independent captures of the same bytes.
**Verdict: the due r95 re-check is satisfied on V17's run** — hash pin fresh,
delivered discrimination HELD, control REGRESSION-DETECTED as expected. The
ruling's gate-3 state is unchanged and was re-verified, not copied blind:
`excerpt_files=` and `readme_line3=Fixture scaffolding only; not sourced story
evidence.` (reproduced by me; same as r93/r94 records).

Reading trap for L1 when citing V17 §1.4: `discriminate_check.py` prints the
*working-tree* checker hash and `matches_pin=True` in both modes; the mode field
(`mode=e97613c`) is what identifies the control run. V17 flagged this; correct.

## 4. What L1 must append (row 4)

Append-only, at EOF of `corpus/knowledge/r91-c9-watch.md`, following the r94
pattern (dated section + table row; historical text stays unrewritten). Row
numbering is cumulative: r92=1, r93=2, r94=3 → this is **row 4 / re-check 4**.

Exact outputs to cite (all reproduced by V17 §1.3–1.5 and by this seat; any of
the three captures is citeable):

1. Pin:

```sh
sha256sum corpus/fixtures/check_bible.py
```

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

2. Delivered discriminator (`python3 corpus/tools/discriminate_check.py`, exit 0):

```text
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
```

3. Control (`python3 corpus/tools/discriminate_check.py --checker e97613c`,
   exit 2, expected):

```text
mode=e97613c checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
```

4. Optional (W21's fuller due set; not in the r94 append): the two fixture
   commands — `python3 corpus/fixtures/check_bible.py
   corpus/fixtures/r91-c1-null-chain` → exit 1,
   `VIOLATION: entities[3].provenance[1]: provenance chain break; expected
   from_holder 'mira', got None` / `1 violation(s); no canon changed`;
   `python3 corpus/fixtures/check_bible.py
   corpus/fixtures/r91-c1-tick-unresolved` → exit 1, three lines (invalid
   `first_appearance` row, definite tick inversion, qualified unresolved-holder
   chain break) — both byte-match the r94 W21 artifacts.

5. Table row 4:

```text
| 2026-10-17 (r95) | `ff9fd2aa…d1421` | **DISCRIMINATION HELD** — re-check 4 (r95): delivered discrimination held; the `e97613c` control reported REGRESSION-DETECTED as expected; ruling retained. Next re-check: r96. |
```

6. Gate-3 sentence to carry (re-verified this round): gate 3 remains **not met**
   and the four-gate falsification trigger remains unsatisfied — the
   unresolved-tick fixture has no `*excerpt*` files and its README line 3 reads
   `Fixture scaffolding only; not sourced story evidence.`; nothing in r95
   changes the sequence-scope evidence state recorded in the r93 clarification.

The r95 run should be attributed to seat V17
(`.ufo/waves/round-95/seats/V17-gates-boundary.md`), with this seat's and
V20's captures as corroboration. No producer byte-owns the watch file; the
append is L1's at closure.

## 5. Limits

- I verified the watch file was byte-stable across my window but cannot observe
  writes after handoff; if L1 appends, the file hash changes by design.
- I did not re-run the full 169-directory corpus sweep (not this seat's scope),
  nor adjudicate any axis.
- The r95 row's final wording is L1's to write; section 4 is a spec with
  reproduced outputs, not a performed edit.

Bottom line: **PASS** — checker pin `ff9fd2aa…d1421` reproduced by `sha256sum`
(working tree unchanged at baseline `fb118c4`); the C9 watch still carries
"Next re-check: r95" (`:253`, row 3 last, no r95 append); V17's round-95
discriminator run (`V17-gates-boundary.md` §1.3–1.5) reproduces the pinned
outputs byte-for-byte against my independent runs and its own scratch captures,
satisfying the due check — L1 must append the fourth periodic re-check row
(row 4, DISCRIMINATION HELD / control REGRESSION-DETECTED / "Next re-check:
r96") at EOF with the outputs listed in §4.
