# V54 — endgame-monitor (round 99, re-dispatch)

**Seat:** V54 `endgame-monitor`. Mandate: landing curve, subtract-SELF compliance, stall characterization. Process record only — no claim verdict.

**Lane root for every command:** `/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the parent). Leaf seat: no nested agents, no commits, no pushes, no network. Exclusive writes: this report and `.ufo/waves/round-99/seats/V54-scratch/` only.

**Baseline / HEAD.** Declared baseline r98 closure `4265df5`. Observed HEAD throughout:

```
git -C /home/vgpnk/Projects/shokunin/lore-shokunin rev-parse --short HEAD
337f0fa
git -C … log -1 --oneline
337f0fa lore r99: record blocked dispatch attempt (xai-oauth credential pool missing) — zero increment
```

The standing r99 declaration in `LOG.md` (128 seats, C1 full-file pins + C2 lapse fixture and blind-spot table; poll-wait 20 s × 40; all-reports polls subtract SELF) was not rewritten by this seat. Wave tree uncommitted.

**Time base.** Local `-0300` (sampler, `stat`, `date`). `-0300 = UTC − 3 h`. Wave tree created `2026-10-17T22:00:48-0300` (`find` on `.ufo/waves/round-99`). First observed poller start `22:00:36` (pid 1665214, `ps -eo pid,lstart`). This seat's first sampler line: `# sampler start 2026-10-17T22:01:33-0300`. **Cutoff for the curve below: `2026-10-17T23:06:35-0300`.** This report is written after that cutoff and is not in the 101-count.

Expected roster, confirmed by V101's inline poller (`roster = S1–S5 + V01–V123`, then `s != "V101"`, `assert len(roster) == 127`): **128 seats**. An all-reports poll that subtracts SELF is done at 127 others.

---

## 1. Landing curve

### 1a. Arrival curve (birth time)

`stat -c %w` on every `seats/*.md` at `23:06:35`. Birth and mtime agree on the first and last files. Minute buckets (birth):

```
22:01 + 1 cum=  1     22:32 + 8 cum= 39     22:48 + 2 cum= 81
22:02 + 1 cum=  2     22:33 + 2 cum= 41     22:50 + 3 cum= 84
22:03 + 2 cum=  4     22:35 + 2 cum= 43     22:51 + 1 cum= 85
22:04 + 1 cum=  5     22:36 + 3 cum= 46     22:52 + 1 cum= 86
22:05 + 1 cum=  6     22:37 + 5 cum= 51     22:55 + 1 cum= 87
22:07 + 1 cum=  7     22:38 + 4 cum= 55     22:56 + 3 cum= 90
22:10 + 1 cum=  8     22:39 + 3 cum= 58     22:58 + 1 cum= 91
22:11 + 2 cum= 10     22:40 + 5 cum= 63     22:59 + 2 cum= 93
22:12 + 1 cum= 11     22:41 + 3 cum= 66     23:00 + 1 cum= 94
22:14 + 1 cum= 12     22:42 + 2 cum= 68     23:01 + 1 cum= 95
22:15 + 1 cum= 13     22:43 + 2 cum= 70     23:02 + 3 cum= 98
22:17 + 1 cum= 14     22:44 + 1 cum= 71     23:04 + 1 cum= 99
22:21 + 1 cum= 15     22:46 + 7 cum= 78     23:05 + 1 cum=100
22:22 + 2 cum= 17     22:47 + 1 cum= 79     23:06 + 1 cum=101
22:24 + 1 cum= 18
22:25 + 1 cum= 19
22:26 + 1 cum= 20
22:27 + 1 cum= 21
22:29 + 2 cum= 23
22:30 + 3 cum= 26
22:31 + 5 cum= 31
```

First arrival: `S3-fixture-author.md` birth `2026-10-17 22:01:40.692964933 -0300` (5069 bytes). Last at cutoff: `V117-integration-3.md` birth `23:06:32` (19426 bytes). **101/128 reports, SELF not yet written.** Shape: a thin head (14 by `22:17`, inside the 40×20 s window), then a long tail after poll caps, not a single dump. Peak minute `22:32` (+8) and `22:46` (+7).

Producer reports by birth: S3 `22:01:40`, S4 `22:03:54`, S1 `22:48:57` (`S1-full-file-pins.md`, 11971 bytes). **S2 and S5 reports absent at cutoff.**

18 reports were rewritten after birth (mtime minute ≠ birth minute). Worked examples:

| Report | birth | mtime |
|---|---|---|
| `V11-c2-inherited-equality.md` | 22:07:59 | 22:11:54 |
| `V39-receipt.md` | 22:30:30 | 22:50:06 |
| `V123-presence-final-2.md` | 22:46:33 | 22:59:00 |

A mtime-only curve would move those later. Birth is the arrival curve.

### 1b. Sampler curve (20 s) and two host gaps

`V54-scratch/curve.log`. The host background cap killed the first two samplers; birth times (§1a) fill both gaps.

```
# sampler start 2026-10-17T22:01:33-0300 cadence=20s cap=900s seat=V54
2026-10-17T22:01:53-0300 count=1 new=S3-fixture-author.md
2026-10-17T22:02:53-0300 count=2 new=V80-c2-prose-prefix.md
2026-10-17T22:03:33-0300 count=3 new=V68-adjacency-2.md
2026-10-17T22:04:13-0300 count=4 new=S4-fixture-docs.md
2026-10-17T22:11:13-0300 count=9 new=V119-c2-anchors-3.md
# SAMPLER_HOST_TIMEOUT gap after 22:11:13; restart sample 2026-10-17T22:19:53-0300
# sampler restart 2026-10-17T22:19:53-0300 cadence=20s cap=1500s seen=14
# SAMPLER2_HOST_TIMEOUT observed restart-check 2026-10-17T22:48:51-0300 live_count=80
# sampler3 start 2026-10-17T22:50:29-0300 cadence=20s cap=600s seen=82
2026-10-17T22:56:49-0300 count=90 new=V58-mutual-wait-guard.md
2026-10-17T22:58:29-0300 count=91 new=V100-late-bookkeeper.md
2026-10-17T22:59:49-0300 count=93 new=V45-pins-c9.md,V79-c1-contract-validity.md
# SAMPLER3_CAP 2026-10-17T23:00:29-0300 count=93
```

No `NONSELF_127` line. The sampler stops at `len(files) >= 127` (SELF subtracted by construction) and **does not gate this report**. It never reached 127. Host tool notifications: first sampler `timed_out` at 600 s; second `timed_out` at 1500 s; third completed its own 600 s cap.

Early arrivals before every producer existed: V80 `22:02:52`, V68 `22:03:15`, both before S4 (`22:03:54`) and long before S1/S2/S5. Those seats did not wait out the protocol. Recorded as curve fact, not as a deadlock.

### 1c. Producer artifacts vs producer reports

`stat -c '%y %s %n'` at `23:05:44`:

```
22:38:11  29110  corpus/tools/dependency_freeze.py
22:08:46  25987  corpus/tools/dependency-freeze-contract.json
22:51:39  38397  corpus/tools/README.md
22:51:39  17287  SKILL.md
22:57:50  20526  corpus/knowledge/r99-gate-blind-spot-table.md
22:57:50  14990  corpus/knowledge/r99-lapse-scope-note.md
```

Earlier snapshot at `22:01:44` had the freeze pair still at the r98 pins (`dependency_freeze.py` sha `03d04365…`, contract `153ebc5b…`, mtimes `20:31:49` / `20:33:36`) and both knowledge files `MISSING`. `git diff --stat 4265df5 -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json` (taken while the report was still absent) showed `2 files changed, 206 insertions(+), 22 deletions(-)`.

Artifact order vs report order:

| Producer | artifact | report |
|---|---|---|
| S3 | r99 fixture present by `22:01:13` (three files already differ from r98) | `22:01:40` |
| S4 | README + map still r98-identical at `22:01:44`; later edited (not re-hashed here) | `22:03:54` |
| S1 | py `22:07:33`, contract `22:08:46`, py rewritten `22:38:11` | **`22:48:57`** (`S1-full-file-pins.md`, not `S1-freeze-hygiene.md`) |
| S2 | README + SKILL unchanged from `21:32`/`21:34` until **`22:51:39`** | **ABSENT at cutoff** |
| S5 | both knowledge files **`22:57:50`** | **ABSENT at cutoff** |

`receipt.json` birth/mtime `22:51:41` (67825 bytes) — before S5's knowledge files. Not this seat's artifact.

---

## 2. Subtract-SELF

The convention: any all-reports poll subtracts SELF. Producer-only waits subtract SELF by not including the verifier. Bounded escapes are recorded, not fatal.

### 2a. Seats that actually gate on an all-reports count

Searched live `*-scratch/poll.sh` and V58's `procs/` dumps for `\b127\b|\b128\b`. The only exit conditions found:

**V123 — self-inclusive, escaped.** `V123-scratch/poll.sh`:

```
reports=$(find "$SEATS" -maxdepth 1 -name '*.md' | wc -l)
if [ "$reports" -ge 128 ]; then
  echo "$ts try=$i FULL-128 exiting" >> "$LOG"
  exit 0
fi
```

No `grep -v`, no SELF token, threshold 128. Observed (`V123-scratch/poll.log`):

```
2026-10-17T22:20:45-03:00 try=40 reports=14 S=2 V=12 dirs=116 arts=YYYYNNYY V39=0 V99=0 V101=0 receipt=0
2026-10-17T22:21:05-03:00 DEADLINE tries=40
```

The count plateaued at 14. The bound fired. The seat later wrote `V123-presence-final-2.md` (birth `22:46:33`, mtime `22:59:00`). It could not have hit 128 from inside its own poll. It also could not have deadlocked anyone: at deadline only 14 reports existed, so the missing set was not the waiter set.

**V101 — explicit subtraction, still polling at cutoff.** Inline poller dumped at `V58-scratch/procs/V101__1699476.txt` (that pid was dead by `22:34`; a second loop continued, see §3):

```
roster = [f"S{i}" for i in range(1,6)] + [f"V{i:02d}" if i < 100 else f"V{i}" for i in range(1,124)]
roster = [s for s in roster if s != "V101"]
assert len(roster) == 127, len(roster)
…
# ready when 127 others present
if len(missing) == 0 and len(dups) == 0:
    … break
if n == MAX:   # MAX = 90
    fh.write(f"STALL_ESCAPE try={n} others={len(present)} missing={len(missing)} …")
```

`V101-scratch/poll.log` at `23:05:25`:

```
try2=65 ts=23:05:25 others=100 missing=27 dups=0 extra=[] prod_missing=['S2', 'S5'] art_missing=0 receipt=1 delta=0
  missing_seats=S2,S5,V04,V08,V09,V30,V34,V37,V38,V42,V43,V50,V53,V54,V55,V67,V69,V71,V72,V74,V75,V99,V107,V117,V118,V120,V121
```

(`V117` has since landed at `23:06:32`; the log line is one minute older.) V101 subtracts SELF. It is one-sided: it waits for the others; the others' exit conditions (checked below) do not wait for 127. No V101 report at cutoff.

**V54 (this seat) — sampler only.** `if len(files) >= 127` with the comment `subtract SELF: V54 report not yet written`. Not an exit gate for the report. This file is written at 101 others, not at 127.

**V99 — states the subtraction and does not wait.** `V99-scratch/poll_and_build.py` lines 693 and 708:

```
# Do not require the other 127 reports (subtract SELF; do not deadlock on endgame seats).
"STALL_ESCAPE try=%d %s … (endgame subtracts SELF; not waiting for 127)"
```

Observed terminal line of `V99-scratch/poll.log`:

```
BUILD reason=exhausted-after-40 present=40 excluding_self=40 missing_others=87 drifts=1 receipt=False v39_md=True
```

No `V99-*.md` at cutoff (the build did not land a seat report under that prefix). The poll itself did not wait for 127.

**V39** logs `roster_present={n}/128` as a counter. That string is in `V58-scratch/procs/V39__1698941.txt`. It is not an `-ge 128` exit. Not counted as an all-reports gate.

### 2b. Producer-set waits (SELF subtracted by construction)

Most `poll.sh` files that say "subtract SELF" gate on `S1`–`S5` reports and artifacts, not on `seats/*.md` reaching 127/128. That is the convention applied to a narrowed wait set: SELF is not in the set, so the r96 mutual-wait cannot form among those seats. Examples read in full or in the success function:

- V32 `reports_ok`: `find … -name 'S[1-5]*.md' | wc -l` then `[ "$n" -ge 5 ]`. Comment: `ENDGAME: subtract SELF (V32 is not a producer).` Terminal: `POLL_EXPIRE try=40 2026-10-17T22:22:20-0300`.
- V49: `ls S1-*.md … S5-*.md | wc -l` and `[ "$reports" -ge 5 ]`. Comment: `Never counts SELF.` Terminal: `POLL_TIMEOUT after 40 tries`.
- V52: waits on `S1-*.md` and `S2-*.md` only. Comment: `SELF (V52) is not in the wait set.`
- V45 counts `*.md` excluding `V45-pins-c9.md` but the exit is producers + V22 + artifacts, not the count.
- V71 comment says it subtracts SELF; the exit is a V39 report, not an all-reports count. Terminal: `ABSENT after 40 tries`.

Comment-only "subtract SELF" on a producer-only gate is compliant. It is not the same evidence as a 127-threshold.

### 2c. Mutual pairs

No all-reports clique closed. V123 (128, escaped at 14 reports) and V101 (127, still open, missing set is producers plus late verifiers, not "only the other waiters") do not wait on each other as a cycle: V123 already wrote; V101's missing list at `23:05:25` does not require V123.

A scan of still-missing seats' scratch scripts for a 127/128 **poll** gate found none that exit on that count:

- V99: explicit non-wait (quoted above).
- V107 `poll-escape.sh` line 4: `Does not wait on SELF or all 128 reports.`
- V71 `audit.py` asserts a roster size of 128 as an audit check, not a poll exit.
- V101 `audit.py` asserts `len(ROSTER) == 128` the same way. Its poll is the inline 127-other loop, already classified.

V58's report (`V58-mutual-wait-guard.md`, landed `22:56:49`) independently recorded `named_file_edges 56 mutual none` and the same V123 `DEADLINE`. That report's close (`22:55:10`) still called both knowledge files ABSENT. They landed at `22:57:50`. V58 is right about the graph at its close and stale about S5's artifacts after that. Not re-litigated here.

**Verdict:** the r96/r97 mutual-wait class did not recur. One self-inclusive all-reports poll (V123) existed, escaped on its bound at 14 reports, and wrote anyway. Every other all-reports condition found subtracts SELF or refuses to wait on 127.

---

## 3. Stall characterization

The binding stall is **producer latency past the 40×20 s window**, not a verifier cycle.

The protocol window from the first poller (`22:00:36`) ends about `22:14`. First observed terminal lines are in that band and the minutes after (late starters). At those times S1/S2/S5 reports did not exist. S1's tool and contract already did (`22:07:33` / `22:08:46`). S1's scratch was still being written at `22:43:30` (`S1-scratch/before-nonanchor/…/fictional-excerpts.md`). S5's scratch was still being written at `22:40:49` (`S5-scratch/work2/`). S2's scratch was empty at `22:29` and held a `before-r95/` tree by `22:47`, with README/SKILL unchanged until `22:51:39`.

So the 40-try ABSENT lines are true: the reports were absent. They are not evidence the producers had aborted. Early V58 proc dumps of S1/S2/S5 poller pids were dead by `22:34`; the producer agents kept writing scratch after those poller pids exited.

### 3a. Verbatim escapes (bounded, not fatal)

| Seat | Line | When |
|---|---|---|
| V123 | `2026-10-17T22:21:05-03:00 DEADLINE tries=40` | after plateau `reports=14` |
| V04 | `POLL_ABSENT tries=40 … s1_md=0` | poll 40 at `22:24:29` |
| V32 | `POLL_EXPIRE try=40 2026-10-17T22:22:20-0300` | sreports only S3+S4 |
| V50 | `ESCAPE-EXHAUSTED 22:29:53` | after `STALL-ESCAPE START 22:27:13` and 8 extra tries; producers still `[S3-fixture-author.md S4-fixture-docs.md]`, both knowledge files missing |
| V30 | `ESCAPE-EXPIRED after 15 ts=2026-10-17 22:34:07 -0300` | `s1=no s5=no` the whole escape; `seats_md` rose 22→41 during it |
| V99 | `BUILD reason=exhausted-after-40 … missing_others=87` | wrote without the other 127 |
| V101 | scripted `STALL_ESCAPE` at `MAX=90`, plus a second loop | at cutoff `try2=65`, `others=100`, `prod_missing=['S2','S5']`, `art_missing=0` — still inside a bound, not a hang with no cap on the first loop |

A depth-2 scan of `*-scratch/poll.log` around `22:29` found 50 logs whose last matching line was a terminal (`ABSENT after 40`, `POLL_EXPIRE`, `POLL-EXHAUSTED`, `DEADLINE`, `TIMEOUT`). The common missing set in those lines is S1 and/or S2 and/or S5 reports and the two knowledge files. Full list: `V54-scratch/stall-terminals.txt`.

V52's own comment in a still-running shell at `22:29` recorded a host cut of its first poll: `process timeout killed the first poll at try 30; stall-escape recorded`, then `seq 31 40`. Same class as this seat's sampler caps: host tool timeout, then a bounded resume. Not a protocol deadlock.

### 3b. What the stall was not

- Not "artifacts never arrived." S1's pair changed inside the window; S2's docs and S5's notes arrived after it.
- Not "S1 never finished." `S1-full-file-pins.md` landed `22:48:57`, about 34 minutes after the contract write and about 34 minutes after the first poller's 40-try budget expired.
- Not a closed clique of endgame seats waiting on each other's reports. See §2c.

### 3c. Filename mismatch (hygiene, not the cause)

Several polls hardcode `S1-freeze-hygiene.md` (`V45`, `V53`, `V55`, `V38`, `V46`, `V78` `poll.sh`). The landed file is `S1-full-file-pins.md`. Those exact-name polls had already printed ABSENT before `22:48`, so the mismatch did not create the original stall. A poll still running on the exact r98-style name would still miss S1 after the report existed. Polls that glob `S1-*.md` would not.

---

## 4. Open at cutoff (`23:06:35`, 101 reports, SELF excluded)

Missing prefixes (27), from the birth-table pass:

```
S2 S5 V04 V08 V09 V30 V34 V37 V38 V42 V43 V50 V53 V54 V55
V67 V69 V71 V72 V74 V75 V99 V101 V107 V118 V120 V121
```

`V54` is this seat (about to write). `V117` is in V101's `23:05:25` missing list and landed at `23:06:32`, so that log line is already one seat stale. S2 and S5 **artifacts** are present; their **reports** are not. V101 is still in a second poll loop waiting for 127 others, with a scripted stall escape on the first loop (`MAX=90`) and no observed `STALL_ESCAPE` line yet on the second loop.

V58's close-time claim that both `corpus/knowledge/r99-*.md` files were ABSENT is superseded by the `22:57:50` `stat` above.

This seat's two sampler gaps (`22:11:13`–`22:19:53`, and `22:44:34`–`22:48:51`) are host tool caps. Birth times cover them. They are hygiene, not missing evidence.

---

## 5. Bottom line

**PASS (endgame-monitor; wave still open at cutoff)** — birth-time arrival curve is 101 reports from `S3` at `22:01:40` to `V117` at `23:06:32`, with the sampler curve agreeing where it was alive and the two host gaps filled from `stat -c %w`; subtract-SELF held for every all-reports gate except V123's threshold-128 poll, which escaped on `DEADLINE tries=40` at `22:21:05` with `reports=14` and then wrote, and no mutual-wait clique formed; the stall class is producer reports (S1 at `22:48:57`, S2 and S5 still absent) landing after the 40×20 s window while artifacts for S1 were already in at `22:07`/`22:08`, with the bounded escapes in §3a recorded and not fatal.

---

## 6. Post-write drift (`23:11:25`)

While this file was being written, the two producer reports that §1c and §4 called ABSENT landed. `ls -la --time-style=full-iso seats/S*.md` at `23:11:25`:

```
22:48:57  11971  S1-full-file-pins.md
23:10:49  11040  S2-tools-docs.md
22:01:40   5069  S3-fixture-author.md
22:03:54   9303  S4-fixture-docs.md
23:10:56   7536  S5-knowledge-author.md
```

`ls seats/*.md | wc -l` → `117` (includes this report). That is 116 others, up from 101 at the `23:06:35` birth cutoff. The §1/§4 ABSENT claims are true of the cutoff and false of `23:11:25`. The stall class does not change: S2's report is ~19 minutes after its README/SKILL write (`22:51:39`) and ~70 minutes after the wave tree opened; S5's report is ~13 minutes after the knowledge files (`22:57:50`). Both are still well outside the 40×20 s window that produced the §3a escapes. `find -newermt '2026-10-17 23:06:32'` also shows mtime updates on already-born reports (V73, V23, V79, V96, V123 among them); those are rewrites, not new arrivals, same class as §1a.
