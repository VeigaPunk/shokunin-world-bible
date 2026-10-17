# SE2 — Sentinel (runs last)

Snapshot window: 2026-10-17 06:53:00 → 07:00:19 -0300. Two mandated 60 s wait-checks were
taken before any measurement. All evidence below is from the delivered tree at `ca7f9ef`
(git objects) or read-only execution against it; probes and checker copies live under
`/tmp/se2` and were not written into the repository.

## Work performed

- Ran the two 60 s wait-checks, then the five assigned sentinel checks: followup/ naming,
  git tracked-modification state, `HEAD == ca7f9ef`, no seat commits, fleet-report location.
- Added sentinel corroboration with read-only receipts: freeze-then-verify hash-match
  (r88-I1), 160→164 census comparison, an independent 164-directory exit/stdout comparison
  of the baseline checker vs the delivered checker, the C2 support-command replay, and a
  5-probe C1 before/after replay on the baseline FN-2 fixture.
- Sibling repos were only read (`git -C <repo> status --porcelain`, `rev-parse`); nothing
  was written there. SE2's only repository write is this file. No commit, no push, no patch
  application, no tracked-file change by this seat. All my Python runs set
  `PYTHONDONTWRITEBYTECODE=1`.

## Before → after measurements

### 1. followup/ naming

Exact command:

```sh
ls -la .ufo/waves/round-90/followup/
```

Observed (07:00:19): `CB1.md`, `H2-delta.json`, `H2.md`, `H3-r90-mutations.json`,
`H4-census.json`, `H4-lineage.json`, `H4-probes.json`, `H4.md`, `JCAL1-delta.json`,
`JCAL1.md`, `JCAL2-receipts.json`, `JCAL2.md`, `JCAL3-census-after.json`,
`JCAL4-probes.json`, `JCAL4.md`, `JCAL5-delta.json`, `JCOV2.md`,
`JCOV3-denominators.json`, `JCOV5-probes.json`, `JCOV5.md`, `JDEP2-probes.json`,
`JDEP2.md`, `JDEP3-probes.json`, `JDEP3.md`, `Q1-r90-debt.json`, `Q2.md`.

Every name matches `<SEAT>.md` or `<SEAT>-*.json|md`; zero non-conforming names, zero
nested or stray directories. The convention matches the r87/r88/r89 followup dirs
(spot-checked: `round-89/followup/SE2.md`, `SE2-snapshot.json`, `Q1-r89-debt.json`).
Seats were still landing artifacts during this window (26 files at 06:57–07:00): this is a
timestamped snapshot, not a claim about later arrivals.

### 2. HEAD and tracked modifications

Exact command:

```sh
printf 'head='; git rev-parse HEAD; printf 'tracked_diff_exit='; git diff --quiet; echo $?; \
printf 'index_diff_exit='; git diff --cached --quiet; echo $?; git status --porcelain --untracked-files=all
```

Observed:

```text
head=ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13
tracked_diff_exit=1
index_diff_exit=0
 M .ufo/waves/round-90/followup/Q1-r90-debt.json
?? .ufo/waves/round-90/followup/CB1.md
... (24 further untracked followup artifacts)
?? corpus/tools/__pycache__/support_check.cpython-314.pyc
```

- `HEAD == ca7f9ef` — confirmed exact.
- Index clean; exactly **one** tracked worktree modification:
  `.ufo/waves/round-90/followup/Q1-r90-debt.json`. This is Q1's own followup file — a path
  inside the wave's authorized write set (`followup/<SEAT>-*.json`) — being rewritten in
  place (its original r90 copy was committed inside `ca7f9ef`). It appeared between my first
  check (06:53, tree fully clean) and the 07:00 snapshot.
- `l0-questions.md` is untouched: `git status --porcelain -- l0-questions.md` is empty and
  its last commit is `e97613c`. K1's conditional one-line append therefore did not happen
  (consistent with the r90 debt ledger: Q89-048 said the kotodama acknowledgement is
  untriggered and not an r90 claim).
- All other untracked paths are new `followup/` artifacts plus the `__pycache__` file noted
  in Findings.

### 3. No seat commits, no push

Exact command: `git reflog -15 --date=iso`, `git for-each-ref`, `git rev-list --count origin/main..HEAD`.

Observed: the reflog's only entries after `e97613c` are the L1's three work-commit entries
(`1e6c57e` 06:52:05 → `5dd79a2` 06:52:26 → `ca7f9ef` 06:52:50, all the same work-wave
message, i.e. amend chain). Refs: only `refs/heads/main` at `ca7f9ef`; no tags, no extra
branches, no `refs/stash`. `origin/main` remains `28706dc` and `git status -sb` reports
`## main...origin/main [ahead 9]` — nothing was pushed. **No seat commit exists.**

### 4. Sibling repos read-only

Exact command:

```sh
for r in <20 lane repos>; do s=$(git -C "$r" status --porcelain | head -3 | tr '\n' '|'); \
  h=$(git -C "$r" rev-parse --short HEAD); echo "$r head=$h dirty=[$s]"; done
```

Observed: all 19 sibling repos report `dirty=[]` (chousa `38f217e`, kotodama `49ac1a5`,
kama `6978097`, etc.). `lore-shokunin` is the only repo with dirt, and it is exactly the
followup artifacts in item 2. No cross-lane write occurred.

### 5. Fleet report single location

Exact commands:

```sh
ls -la /home/vgpnk/Projects/shokunin/.ufo/reports/round-90
ls -la /home/vgpnk/Projects/shokunin/.ufo/reports/round-{87,88,89}
find /home/vgpnk/Projects/shokunin -maxdepth 4 -name 'lore.md' -not -path '*/.git/*'
```

Observed: `.ufo/reports/round-90` → `No such file or directory`. Rounds 87/88/89 each hold
exactly one file, `lore.md` (19047 / 28198 / 44246 bytes). The only other `lore.md` under
the fleet root is an unrelated interactive-L1 prompt. So the one-report-per-round-per-lane
convention is intact with **no duplicate or divergent copies** — but the round-90 lane
report has not been written yet. P1 is the only seat authorized to write
`/home/vgpnk/Projects/shokunin/.ufo/reports/round-90/lore.md` (K1's authorized write is the
single l0-questions.md line, which did not occur). This is a delivery gap for the parent,
not a location violation.

### 6. Freeze-then-verify (r88-I1) — PASS

Exact command (scratch under /tmp):

```sh
git archive e97613c corpus/fixtures/check_bible.py | tar -x -C /tmp/se2/base; cd /tmp/se2/base
patch -p1 < .../patches/X2-c1-nullonly.patch; patch -p1 < .../patches/X3-c1-tickonly.patch
sha256sum corpus/fixtures/check_bible.py
sha256sum /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/check_bible.py
```

Observed:

```text
baseline  e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556
X2+X3     ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
delivered ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421   (diff → IDENTICAL)
X1 control 12866e734beb0e8fdfb641e9dab7cdaae7518fc0fdb8749a5e086981a0d1ae18
```

The delivered checker is byte-identical to X2+X3 composed on `e97613c`, and is *not* the
X1 composition — i.e. the C9 integer-only tick ruling is what actually shipped. **No
mismatch; no blocking finding** (independently corroborated by H2.md and JCAL4.md, which
report the same hash).

### 7. Census: 160 → 164 with the four claimed additions

Exact command:

```sh
git ls-tree e97613c corpus/fixtures/ | awk '$2=="tree"' | wc -l   # 160
git ls-tree HEAD    corpus/fixtures/ | awk '$2=="tree"' | wc -l   # 164
comm -13 <(git ls-tree e97613c ...) <(git ls-tree HEAD ...)
```

Observed new dirs: `r90-c1-rawpresent-from`, `r90-c1-rawpresent-source`,
`r90-c1-rawpresent-to`, `r90-c1-three-causes` — exactly the four declared. Name-status of
`e97613c..HEAD` shows no pre-existing JSON modified (content edits are the checker, five
r87 excerpt `.md`s, one r88-m3 excerpt `.md`, the knowledge decision table; everything else
is additions).

### 8. Exit-change comparison, all 164 directories (SE2's own receipt)

Exact command (inline Python driver, `/tmp/se2/ck/check_base.py` = `e97613c` checker,
`check_deliv.py` = delivered):

```sh
for d in corpus/fixtures/*/; do run both checkers; compare (exit, stdout); done
```

Observed:

```text
dirs=164
base_exit_hist={0: 32, 1: 132}
delivered_exit_hist={0: 32, 1: 132}
differing_dirs=0
NEW r90-c1-rawpresent-from   base_exit=1 deliv_exit=1 same_stdout=True  (5 violations)
NEW r90-c1-rawpresent-source base_exit=1 deliv_exit=1 same_stdout=True  (4 violations)
NEW r90-c1-rawpresent-to     base_exit=1 deliv_exit=1 same_stdout=True  (5 violations)
NEW r90-c1-three-causes      base_exit=1 deliv_exit=1 same_stdout=True  (4 violations)
```

Zero exit changes and zero stdout changes across the whole delivered corpus. The four new
fixtures printing identically under both checkers is not drift: their READMEs declare
before-state == after-state for those shapes (they pin FN-1 raw-present wording and the
≥3-cause record, not the repaired hedges).

### 9. C2 support-command receipts (replayed)

Exact commands and observed output:

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
# SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
# RESULT PASS   exit=0
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
# SOURCE-SUPPORT 10/10; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10
# RESULT PASS   exit=0
```

Both receipts reproduce exactly as claimed.

### 10. C1 before/after probes (SE2's own replay)

Probes built under `/tmp/se2/probes` from `corpus/fixtures/r89-fn2-unresolved-chain-break`
(the FN-2 fixture), as C9's semantic set; baseline vs delivered checker.

```text
null-from-chain (prev holder resolvable)
  base : ... possible provenance chain break, not a definite identity mismatch: expected
         from_holder 'mira'; got None; from_holder None is not uniquely resolvable
         (0 raw entity rows carry this id, but only 0 is in the resolved index)
  deliv: ... provenance chain break; expected from_holder 'mira', got None        <- definite

tick-relevant-unresolved (non-null unresolved holder among compared)
  base : ...tick: input-structural finding, not sourced-canon; holder identity is not
         uniquely resolvable: expected from_holder 'f3-dup' ...; provenance tick 1 must
         be greater than previous tick 3
  deliv: ...tick: provenance tick 1 must be greater than previous tick 3            <- definite

chain-unresolved (genuinely unresolved non-null holder, no tick defect)
  base == deliv: ... possible provenance chain break, not a definite identity mismatch:
                 expected from_holder 'f3-dup' is not uniquely resolvable ...          <- stays qualified

unrelated-duplicate-tick
  base == deliv: ... provenance tick 1 must be greater than previous tick 3         <- definite

probe G, null from_holder with UNRESOLVED previous holder
  base : ... possible provenance chain break ...; got None; from_holder None is not
         uniquely resolvable (0 raw ... 0 ...)                                       <- vacuous clause
  deliv: ... possible provenance chain break, not a definite identity mismatch:
         expected from_holder 'f3-dup' is not uniquely resolvable ...; got None     <- vacuous clause gone,
                                                                                      qualifier kept
```

This reproduces the shipped C1 behavior: null-from chains with a resolvable predecessor and
tick findings return to definite wording; a genuinely unresolved non-null holder keeps the
chain-break qualification. Probe G independently reproduces JCAL4-F1's counter-example to
the unqualified sentence "null chains ⇒ definite" (the qualifier is retained when the
*previous* holder is unresolved — the safe, under-claiming direction).

## Findings & named debt

- **No blocking finding.** `HEAD == ca7f9ef`; index clean; the delivered checker
  hash-matches X2+X3 composed on `e97613c`; 0 exit changes and 0 stdout changes over all
  164 fixture directories; C2 receipts (22/22, 10/10, exit 0) reproduce. No seat committed,
  nothing was pushed, no sibling repo was written.
- **F1 — documentation parity (named debt, non-blocking).** `corpus/fixtures/README.md`
  gained no Round 90 section: it still ends at "Round 89" (line 1012) and does not index
  the four new fixture dirs, the two new claim→excerpt maps, or `corpus/tools/`. The
  README is unchanged between `e97613c` and `ca7f9ef`. Rounds 88 and 89 each closed with a
  documentation-parity repair, so this is a fresh instance of a recurring class; the
  "canonical census manifest" wording of C1(iii) likewise has no *textual* delta — it
  holds only in the runtime sense (the FN-2 pair is a census member and stays
  tuple-identical). H2.md reaches the same reading; flagged for the closure decision.
- **F2 — untracked `corpus/tools/__pycache__/support_check.cpython-314.pyc` (named debt).**
  Untracked and not ignored — `.gitignore` contains only `.ufo/interactive-sessions/`, and
  `git check-ignore -v` exits 1 for the path. It is created by sibling seats running the
  new support command (H2 reports the same; my runs set `PYTHONDONTWRITEBYTECODE=1`). A
  `git add -A` closure commit would sweep it in. This is a live instance of Q89-044, which
  is still open in the audit ledger.
- **F3 — the round-90 fleet report is missing.** `.ufo/reports/round-90/lore.md` does not
  exist at 07:00:19 (rounds 87–89 each have exactly one `lore.md`; no stray or duplicate
  copies of a round-90 report exist anywhere else). Delivery gap for P1, not a location
  violation.
- **F4 — the only tracked modification is Q1's own followup file.**
  `followup/Q1-r90-debt.json` was rewritten in place at 06:59–07:00; the path is inside the
  followup write set, so authority is intact, but the worktree is no longer "tracked-clean",
  and the reviewer should expect this diff at closure. `l0-questions.md` remains unmodified
  (K1's optional append did not occur).
- **F5 — claim-text precision (corroborated, not originated).** The delivered behavior is
  correct in direction, but the summary sentence "null chains and tick findings return to
  definite wording" is overstated for one sub-case: with an unresolved *previous* holder the
  null-from chain line keeps its qualifier (probe G). JCAL4-F1/F4 name the same sub-case and
  its consequence for E1 conformance; my replay confirms their receipt byte-for-byte.
- **F6 — the repaired shapes are not durably pinned.** The four new fixtures pin the FN-1
  raw-present wording and the ≥3-cause record (their outputs are identical under baseline
  and delivered checkers); the null-chain/tick definite strings are evidenced only by probe
  receipts, and the FN-2 pair pins only the qualified half. JCAL4-F3 and H2 carry this as an
  r91 fixture candidate; it is a coverage bound, not a defect of the delivered change.
- **Snapshot caveat.** The followup wave was still in flight during this seat's window
  (CB1/H2/H3/H4/JCAL*/JCOV*/JDEP*/Q1/Q2 landed 06:57–07:00). Everything above is a
  timestamped snapshot of the delivered tree plus my own replays; later arrivals may add
  artifacts but cannot change the committed `ca7f9ef` bytes.

## Handoff

- SE2's only repository write is this file. No commit, no push, no tracked-file change, no
  patch application; scratch lives under `/tmp/se2`.
- Reproduce SE2's receipts:
  - freeze check — `git show e97613c:corpus/fixtures/check_bible.py | sha256sum` and the
    X2→X3 patch composition described in item 6;
  - exit parity — the inline driver in item 8 over `corpus/fixtures/*/`;
  - C2 receipts — the two `support_check.py` invocations in item 9;
  - C1 probes — rebuild from `r89-fn2-unresolved-chain-break` as in item 10.
- For the closure commit the parent still needs to decide: (a) ignore or remove
  `corpus/tools/__pycache__/`; (b) whether to add a Round 90 fixture-index/README section
  and to treat the FN-2 census-manifest item as satisfied in the runtime sense; (c) write
  `.ufo/reports/round-90/lore.md`; (d) accept F5's sub-case qualifier in the C1 claim text
  and F6/F3's carry-forward into r91.
