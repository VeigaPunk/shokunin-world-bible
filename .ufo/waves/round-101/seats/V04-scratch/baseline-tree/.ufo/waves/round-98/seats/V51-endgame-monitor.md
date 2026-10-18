# V51 — endgame-monitor (round 98, COMPLETION-WAVE re-dispatch)

**Seat:** V51 `endgame-monitor` — process-record seat of the round-98 single wave
(64 seats: S1–S5 producers + V01–V59 verifiers). Mandate: reconstruct the landing
curve from file mtimes under `.ufo/waves/round-98/seats/`, from the main-wave
receipt-wording/presence seats' reports (V42, V52, V59) and from the scratch poll
logs; determine whether the subtract-SELF convention was followed; record the
6-abort completion-wave class (which seats aborted, when their tasks were
re-dispatched); log the stall escapes.

Model: `hyper/deepseek-v4.1-flash` (re-dispatch; original V51 aborted by host
interruption — see §4). Lane root for every command:
`/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the parent repo, so
every path used here is lane-anchored or absolute — r94-F01 class). Baseline r97
closure `9a3d648`; observed HEAD `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb`
(`lore r97: close round — SCORECARD admitted section`); wave tree uncommitted.
Leaf seat: no nested agents, no commits, no pushes, no network. This report is my
only lane write; the two temp files I used for the table diff are under `/tmp/`
(`/tmp/tbl.txt`, `/tmp/act.txt`), outside the lane.

**Time base.** All seat-side logs are UTC (`date -u`); all mtimes and the L1/operator
records are local `-0300`. `-0300 = UTC − 3 h`, so e.g. `23:41:27Z = 20:41:27-0300`.
The round opened at **`2026-10-17T23:27:36Z`** (`V20-scratch/round-start-utc.txt`,
verbatim `2026-10-17T23:27:36Z`); the first poller (`V14-poll.sh`) started
`20:27:29` local.

---

## 1. Landing curve

### 1a. Arrival curve (creation-time; from the original V51 sampler)

`V51-scratch/sampler.py` (detached, 20 s cadence, `glob *.md` under `seats/`) wrote
`V51-scratch/curve.log`; the first line is verbatim:

```
# sampler start 2026-10-17T20:28:53-0300 cap=7200s
```

The sampler's own arrival table was rendered to `V51-scratch/landing-table.txt`
(header `=== landing table (arrival time per report, from 20s sampler) ===`,
footer `total distinct arrivals logged: 58`). I verified the table is complete for
the main wave: `comm` against the live `ls *.md` shows the table's 58 entries equal
the 58 main-wave reports exactly (the only extras now present are the two
completion-wave reports, §5). Key arrival marks (verbatim from `curve.log`):

```
2026-10-17T20:29:53-0300 epoch=1792279793 count=1 NEW=V15-c3-r95-repair.md
2026-10-17T20:31:20-0300 count=3  NEW=S3-fixture-author.md          (first producer report)
2026-10-17T20:33:40-0300 count=20 NEW=V06-c2-v46-discharge.md,V59-late-bookkeeper.md
2026-10-17T20:35:40-0300 count=22 NEW=S1-freeze-hygiene.md          (last producer report)
2026-10-17T20:40:40-0300 count=54 NEW=V33-debt.md
2026-10-17T20:42:40-0300 count=57 NEW=V24-adjacency.md
2026-10-17T20:44:40-0300 count=58 NEW=V32-shonen-format.md          (last main-wave arrival)
```

Producer reports by arrival: S3 `20:31:20`, S4 `20:32:20`, S5 `20:33:40`,
S2 `20:34:40`, S1 `20:35:40`. The main-wave arrival curve: first `20:29:53`
(V15), last `20:44:40` (V32), 58 reports in ~14.8 min, ~60 % of them inside
`20:33–20:38`.

### 1b. Mtime curve (last-write; from `ls -la --time-style=full-iso`)

Independent of the sampler, I bucketed the 58 main-wave reports by mtime
(`os.path.getmtime` over `seats/*.md`, the two completion-wave reports excluded):

```
20:31  +1  cum= 1       20:37  +10 cum=39
20:32  +5  cum= 6       20:38  + 6 cum=45
20:33  +4  cum=10       20:39  + 6 cum=51
20:34  +5  cum=15       20:40  + 2 cum=53
20:35  +2  cum=17       20:41  + 1 cum=54
20:36  +12 cum=29       20:42  + 1 cum=55
                        20:44  + 2 cum=57
                        20:46  + 1 cum=58
```

**The two curves disagree on endpoints, and that is real, not an error.**
`landing-table.txt` records *creation*; mtime records *last write*, so reports
edited after first landing move in the mtime curve. Worked examples:

| Report | arrival (sampler) | mtime | note |
|---|---|---|---|
| `V15-c3-r95-repair.md` | 20:29:53 | 20:32:28 | rewritten ~2.6 min after creation |
| `V11-c3-support-map.md` | 20:30:33 | 20:33:30 | rewritten |
| `V59-late-bookkeeper.md` | 20:35:00 | 20:46:51 | rewritten after V59's 20:41:50Z cutoff |

Consequences for anyone reading the mtime curve alone: the first report appears at
`20:31:25` (`S3-fixture-author.md`) rather than the true first arrival `20:29:53`
(V15), and the last mtime is `V59` at `20:46:51` rather than the true last arrival
`V32` at `20:44:40`. The arrival curve (§1a) is the accurate one; the mtime curve
is what a mtime-only reconstruction yields. Both are recorded here so the
difference is not re-learned.

### 1c. Corroborating poll records (main-wave receipt-wording / presence seats)

- **V42** (`V42-receipt-wording.md` §0): poller 20 s × 40 tries, "try 1 20:29:29 —
  `corpus/fixtures/r98-clerk-filing/` present as 10 **r97 byte-copies**"; "try 5
  20:30:49 — S4's r98 map landed; try 6 — S4's r98 README landed; try 11 20:32:49 —
  S1's r97+r98 pins landed; try 12–14 — S2's tools README, S5's notes/report landed;
  try 17 — S2's report landed; **try 19 20:35:29 — `ALL PRESENT`, S1's report
  landed**".
- **V52** (`V52-claim-text-audit.md` §0): "`try=17 ts=20:35:23 fixfiles=10 note=1
  nreports=5 reports=[S1-freeze-hygiene.md,S2-tools-docs.md,S3-fixture-author.md,
  S4-fixture-docs.md,S5-knowledge-notes.md,]` / `COMPLETE try=17`".
- **V59** (`V59-late-bookkeeper.md` §2): "Landing curve (reports incl. SELF, from
  `poll.log`): `23:30:06=1 … 23:33:46=15, 23:35:46=24, 23:37:46=41, 23:39:46=52,
  23:41:46=56`" — its own 20 s all-report count, consistent with §1a.

The producer-artifact (non-report) landings are also pinned by the aborted seats'
pollers: `V20-scratch/poll.log` try 1 `23:28:07` lists the r98 fixture tables plus
the r98 note as still missing, try 2 `23:28:27` shows only
`corpus/knowledge/r98-clerk-scope-note.md` missing, and try 15 `23:32:47` shows the
last artifact path (`…scope-note.md`) present. All 13 producer-artifact paths were
present by `23:32:46Z` (V59 §2).

---

## 2. Subtract-SELF convention — followed, with one substitution

The round-98 LOG declaration states the endgame convention: *"any all-reports poll
must subtract SELF — the r96/r97 mutual-wait class"*. Verdict per seat, from the
poll scripts themselves:

| Seat | Poll condition (verbatim) | Subtract SELF? |
|---|---|---|
| **V58** | `n=$(ls "$D"/*.md \| grep -v '/V58-presence-final.md$' \| wc -l)`; hit at `n ≥ 63` | **YES — explicit** |
| **V31** | `n=$(ls "$S"/*.md \| grep -v "V31-adjudicator" \| wc -l)`; hit at `n ≥ 63`; final line `grep -v V31` | **YES — explicit** |
| **V36** | `n=$(ls …/seats/*.md \| wc -l)` — **no subtraction**; replaced by a quiescence escape: `STALL READY held, reports=$n unchanged for $stall tries` with `$stall ≥ 60` | **NO — substituted** (bounded stall-escape) |
| **V20** | comment `# V20 poll: producer artifacts + all seat reports (self-excluded: V20)`, but the actual condition checks **only S1–S5 reports + artifacts** | intent declared, **not exercised** |
| **V42** | "the all-reports check enumerates `S1..S5` reports only (SELF = V42 never waited on)" | **YES** (narrowed to producers) |
| **V52** | "the endgame convention (subtract SELF) was never exercised because the loop's own all-five condition completed at try 17" | **YES** (not exercised) |
| **V59** | "Missing at cutoff (8 seats, SELF excluded)" | **YES** |
| **V51 / V57** | no all-reports waiter (sampler / watcher only) | **N/A** |

So: **the convention was followed by every seat that actually gated on an
all-reports count (V31, V58) and by the receipt-wording/presence seats (V42, V52,
V59).** The one deviation is V36, which did not subtract SELF but substituted a
bounded quiescence stall-escape (60 stable tries) that makes SELF-subtraction
unnecessary — its own report never lands while it is waiting, so the count
stabilizes and the escape fires. Net: **the r96/r97 mutual-wait class did not recur
as a deadlock.** No direct mutual pair (A→B ∧ B→A) existed at any sample; the
endgame took the co-wait-cluster form `{V31, V36, V58}`, and every member carried a
bounded cap (V58 90 tries, V36 stall-escape, V31 240 tries), so any one landing
reduced the set. This confirms V59 §3 independently.

---

## 3. Stall escapes (verbatim from the poll logs)

| Seat | Escape line (verbatim) | When | Cause |
|---|---|---|---|
| **V20** | `POLL-TIMEOUT 23:41:27 reports=56` | `20:41:27` | off-by-one: its producer-only condition was satisfied at `try 23 23:35:27` (`PRODUCERS-ALL-PRESENT … reports=22`) but `poll.sh` has no success-break, so it ran all 40 tries and the final `POLL-TIMEOUT` fired. |
| **V58** | `POLL-TIMEOUT nonself=58 23:59:39` | `20:59:39` | 90-try cap; `nonself` plateaued at 58 (never 63) because the 6 aborted seats wrote no reports. |
| **V36** | `21:04:43 STALL READY held, reports=58 unchanged for 60 tries; exiting` | `21:04:43` | quiescence escape (its `ready` condition was met but the report count was frozen at 58). |
| **V31** | *(none yet)* | cap ≈ `21:48` | 240-try cap; at report time it was still running (`try 163 00:22:41Z reports=58`). |
| **V51** (original) | *(none yet)* | cap 5400 s from `20:30:59` ≈ `22:00:59` | sampler still running. Header records `cap=7200s` while the process was launched `sampler.py 5400` — a cosmetic cap mismatch in the log header. |
| **V57** (original) | *(none yet)* | 3600 s from `20:31:31` ≈ `21:31:31` | watcher still running. |

Note the V20 off-by-one as a **poll-harness hygiene finding**: `V20-scratch/poll.sh`
logs `PRODUCERS-ALL-PRESENT` on every try after its condition is met but never
`exit`s, so a satisfied poll still ends in `POLL-TIMEOUT`. V57's `notes.md` recorded
the same: *"V20 poll: condition empty at try 40 23:41:07, but loop ended →
POLL-TIMEOUT 23:41:27 (off-by-one; escape fired)."*

---

## 4. The 6-abort completion-wave class

### 4a. Which seats aborted

Report presence at my open (~`21:22` local) was **58/64**: S1–S5 plus 53 verifiers.
The six absent reports are exactly the endgame seats:

```
$ ls *.md | sed 's/[-.].*//' | sort -V | tr '\n' ' '
S1 S2 S3 S4 S5 V01 … V19 V21 … V30 V32 V33 V34 V35 V37 … V50 V52 … V56 V59
$ ls *.md | wc -l          → 58
absent: V20 V31 V36 V51 V57 V58
```

V59 reached the same six independently, post-drift: *"at `23:44:33Z` and again at
`23:46:46Z` the count was **58** and the missing set had shrunk to
`V20 V31 V36 V51 V57 V58`"* (the earlier V59 cutoff of 8 missing also contained
`V24 V32`, which landed later). V36's own receipt-builder recorded the same set in
`V36-scratch/V36-summary-205436.txt` (`"absent": ["V20","V31","V36","V51","V57","V58"]`).
V58's completion-wave report names them as *"precisely the six endgame seats named
as aborted by the host interruption."*

### 4b. When they stopped (abort evidence)

Each aborted seat's **agent turn** stopped writing well after the report landings,
while its **detached background poller/sampler survived**. Last agent-turn write per
seat (from `find -newermt` over each scratch tree):

| Seat | Last agent-turn write | Detached survivor |
|---|---|---|
| V20 | `V20-scratch/snap/*-confirm2.txt` @ **20:56:36–37** (a second confirmation pass; `analyze.py` labels `early/mid/final/confirm2`) | none (poll ended 20:41:27) |
| V31 | `scratch/V31/draft.md` @ **20:50:38** | `scratch/V31/poll.sh` — pid **1466958**, alive, `try 163 00:22:41Z` |
| V36 | `V36-scratch/V36-receipt-builder.py` @ **20:55:31** | V36 poll ended itself at `21:04:43` (STALL) |
| V51 | `V51-scratch/terminal.log` @ **21:05:01**; `landing-table.txt` @ 20:56:59 | `V51-scratch/sampler.py 5400` — pid **1499578**, alive |
| V57 | `V57-scratch/checks.log` @ **20:59:18**; `notes.md` @ 20:52:59 | `V57-scratch/watch.py 3600` — pid **1509787**, alive |
| V58 | `V58-scratch/poll.log` (detached poll) ended `POLL-TIMEOUT … 23:59:39` = **20:59:39** | none |

The **last agent-turn write among the six is V51's `terminal.log` at
`21:05:01`**, so the host interruption landed at **≈`21:05` or later** (it cannot
have landed before the last write it did not prevent). At `21:24:51` the three
detached survivors above were still alive (`ps -eo pid,lstart,etime,cmd`):

```
1466958 Sat Oct 17 20:28:40 2026  56:10 /bin/bash …/round-98/scratch/V31/poll.sh
1499578 Sat Oct 17 20:30:59 2026  53:50 python3 .ufo/waves/round-98/seats/V51-scratch/sampler.py 5400
1509787 Sat Oct 17 20:31:31 2026  53:18 python3 …/seats/V57-scratch/watch.py 3600
```

They are **orphaned leftovers of the aborted turns** — hygiene items for the L1 to
reap (see §6).

### 4c. When their tasks were re-dispatched

The completion wave is a re-dispatch on **`hyper/deepseek-v4.1-flash`**, per the
operator directive recorded in the parent session's user-history
(`…/2f0010a6ea94c1305e889c40a50970cc.jsonl`, 298 lines): the operator wrote
*"on one of the 64 deepseek swarm rounds, use hyper as the provider"*, and the last
operator line — appended at **`21:19:45`** (that file's mtime) — is
*"i think they got stuck"*. Direct evidence the re-dispatched seats self-identify:

- `V20-scope-creep.md` header: `# V20 — scope-creep (round 98, COMPLETION-WAVE
  re-dispatch)` / `Model: hyper/deepseek-v4.1-flash (re-dispatch; original seat
  aborted mid-wave)`.
- `V58-presence-final.md` header: `(round 98, completion wave)` / `Completion-wave
  re-dispatch (original V58 aborted by host interruption)`.

Timing anchors for the re-dispatch:

| Anchor | Time |
|---|---|
| last aborted-turn write (V51 `terminal.log`) | `21:05:01` |
| operator "i think they got stuck" (parent user-history mtime) | `21:19:45` |
| my (V51) session's first environment read (`date -Is`) | `21:22:11` |
| first completion-wave report to land — `V58-presence-final.md` | `21:23:42` |
| second — `V20-scope-creep.md` | `21:24:00` |

So the re-dispatch happened **≈`21:19:45–21:22`**, i.e. **~15–17 min after the abort
(≈`21:05`)** and ~55 min after the round opened. At report time (`21:24:51`) the
completion wave had landed **2 of 6** reports (V58, V20); **V31, V36, V51 (this
seat), V57** were still in flight — absent set at open `{V31, V36, V51, V57}`.

### 4d. Class characterization

The 6-abort class is **not** the r96/r97 mutual-wait class. In r96/r97 the endgame
seats each blocked on the others' reports (a genuine co-dependency); here the six
seats' *agent turns* were killed by an external host interruption while their
*bounded* pollers kept running and self-terminated on schedule. The mutual-wait
convention still worked as designed (no deadlock, §2), and the residual failure was
an infrastructure abort, not a protocol deadlock. The recovery path was a bounded
re-dispatch of exactly the six missing seats, which is proceeding normally.

---

## 5. Completion-wave cross-check (live)

Two completion-wave reports landed during my window; both are consistent with my
reconstruction and both independently confirm the 6-abort set:

- **V58** (`V58-presence-final.md`, `21:23:42`): roster `S1–S5 + V01–V59` = 64 (no
  V60–V64), 58 present / 6 ABSENT at its cutoff, no duplicate prefixes, no
  header/filename mismatch, r98 fixture's 10 files present with hashes, the three
  knowledge notes present. It also audits the **V36 receipt** and finds it an
  unfinalized skeleton (`collection.reports_present: 0`, `reports_absent` = all 64)
  with **6/16 `candidate_revision_pinned` hashes drifted** (its `20:29:02` snapshot
  pinned r97-baseline bytes; live values differ, e.g. `dependency_freeze.py`
  `b06275f3…` → `03d04365…`). Bottom line INCONCLUSIVE (honest presence, stale
  receipt).
- **V20** (`V20-scope-creep.md`, `21:24:00`): `git status --porcelain -uall` =
  44 825 lines, 100 % mapped to declared buckets; report-path exclusivity PASS;
  `__pycache__`/`*-self-test-*` class clean and gitignored; **one parent-tree stray**
  `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` (F1) and a 243 MB
  `V37-scratch/` mirror flagged for L1 removal (F3). It also records the
  **round-98 root strays** `.ufo/waves/round-98/V14-poll.sh`, `V14-poll.log`,
  `V14-poll2.log` as a minor FINDING — a poller that wrote outside the
  `seats/`+`scratch/` convention. Bottom line FAIL (one parent-tree stray + the
  mirror).

**Minor discrepancy in the completion-wave presence report:** `V58-presence-final.md`
§1 lists `V51 | no scratch` and `V31 | no scratch`, but `V51-scratch/` exists
(the original run, `20:28–21:05`) and V31's scratch exists at
`.ufo/waves/round-98/scratch/V31/` (not `V31-scratch/`). Both are "no scratch *from
this re-dispatch*" in intent, but as written the claims are inaccurate — recorded
here so the process record is not left with an unchecked assertion.

---

## 6. Discrepancies, hygiene, and open items (for the L1)

1. **Arrival vs mtime curves differ** (§1b) — use §1a for the landing curve; the
   mtime-only curve misplaces the first and last reports.
2. **Three orphaned detached pollers** from the aborted turns are still running at
   `21:24:51` and will keep writing into the lane (`V31 poll.sh` → `21:48` cap,
   `V51 sampler.py 5400` → `~22:01`, `V57 watch.py 3600` → `~21:31`). They should be
   reaped; until then they keep appending to `scratch/V31/poll.log`,
   `V51-scratch/curve.log`, and `V57-scratch/watch.log`/`seen.json`.
3. **V20 poll off-by-one** (§3) — a satisfied poll still reports `POLL-TIMEOUT`.
4. **Sampler cap-header mismatch** — `curve.log` header says `cap=7200s`, the process
   was launched with `5400`.
5. **V14 root strays** in `round-98/` (recorded by V20) — outside the
   `seats/`+`scratch/` convention.
6. **V36 receipt is an un-finalized skeleton** with 6/16 drifted pinned hashes and
   zeroed collection counts — the L1 must finalize it against the live hashes
   (V58 §5, my §5).
7. **V58's scratch claims for V51/V31 are inaccurate** (§5).
8. **`receipt.json` predates the completion wave** — it records 0/64 and cannot
   reflect the 6 re-dispatched seats.

I judge **no claim (C1/C2/C3) and no axis**; this is the round's process record.

---

## 7. Bottom line

**PASS (endgame-monitor, completion-wave re-dispatch)** — the landing curve is
reconstructed and internally cross-checked (arrival curve: first `20:29:53` V15,
last `20:44:40` V32, 58 reports; mtime curve: `20:31:25`→`20:46:51`, with the
arrival/mtime divergence explained); the **subtract-SELF convention was followed**
by every seat that gated on an all-reports count (V31, V58) and by V42/V52/V59,
with V36 substituting a bounded quiescence stall-escape — **no mutual-wait deadlock
recurred**; the **6-abort completion-wave class is exactly `{V20, V31, V36, V51,
V57, V58}`**, their agent turns stopping at ≈`21:05` (last write V51 `terminal.log`
`21:05:01`) while detached pollers survived, and their tasks **re-dispatched on
`hyper/deepseek-v4.1-flash` at ≈`21:19:45–21:22`** (2 of 6 reports landed by
`21:24:00`); and the stall escapes are logged verbatim (V20 `POLL-TIMEOUT
23:41:27`, V58 `POLL-TIMEOUT nonself=58 23:59:39`, V36 `STALL … 21:04:43`, with V31
and the V51/V57 watchers still bounded and running) — with 8 open hygiene/accuracy
items recorded in §6.

---

## 8. Post-write drift (addendum)

While this report was being written, the remaining completion-wave reports landed.
Final landing times of all six re-dispatched seats (mtime, `ls -la --time-style=full-iso`):

```
21:23:42  V58-presence-final.md         21:25:31  V51-endgame-monitor.md (this seat)
21:24:00  V20-scope-creep.md            21:25:39  V31-adjudicator.md
21:24:50  V36-receipt.md                21:25:44  V57-mutual-wait-guard-2.md
```

So the completion wave is **complete: 6/6** re-dispatched seats wrote reports, and the
round-98 report set is now **64/64** (`ls *.md | wc -l` → `64`, excluding the
`V33-debt.json` companion artifact). The absent set went `{V31,V36,V51,V57}` (at my
open, `21:22`) → `{V31,V57}` (at `21:24:51`) → `{}` (at `21:25:44`). V36's report is
`V36-receipt.md` (the receipt seat's final pass — see §6 item 6 for the skeleton it
must supersede). Total re-dispatch latency from the operator's `21:19:45` "i think
they got stuck" to the last landing: **~6 min**. The three orphaned detached pollers
(§6 item 2) were still alive when this addendum was written.
