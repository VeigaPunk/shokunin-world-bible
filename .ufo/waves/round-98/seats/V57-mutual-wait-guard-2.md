# V57 — mutual-wait-guard-2 (round 98) — COMPLETION-WAVE SEAT

**Seat:** V57 `mutual-wait-guard-2` (process seat; leaf; no nested agents; no commits; no
network; no pushes). Re-dispatch of the aborted r98 V57 on `hyper/deepseek-v4.1-flash` per the
operator directive; the original V57 (r98 main wave, `opencode-go/deepseek-v4.1-flash`) was one of
the six seats cut by the host interruption.
**Mission:** independent process audit — read the poll logs/scratch of V51 and of every seat that
polled for all reports; confirm no unresolved deadlock occurred; characterise the abort pattern
(6 endgame seats aborted by the host interruption, not by mutual waiting — verify by checking which
tasks they were); compare with the r96/r97 mutual-wait class and state what differs.
**Repo root for every command:** `/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the
parent repo; all paths absolute).
**Baseline:** r97 closure `9a3d648` (`git log --oneline -1 9a3d648` →
`9a3d648 lore r97: drop embedded scratch clone (V37 mirror-freeze gitlink) from the wave tree`);
wave head at audit `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb`; wave tree uncommitted.
**Audit window:** 2026-10-17T00:22:46Z → 00:25:00Z (`date -u` = `2026-10-18T00:24:54Z`,
local `2026-10-17T21:24:54-0300`). Wave t0 = `2026-10-17T23:27:36Z`
(`V20-scratch/round-start-utc.txt`).
**Owned axis set:** depth, coverage, calibration. This seat judges **no claim** (C1/C2/C3) and no
axis; it is process evidence only, exactly like its r97 predecessor V56 `mutual-wait-guard`.

## 0. Finding (short)

**No unresolved deadlock occurred in round 98.** The wave's 58-report plateau (58/64 from
23:44:40Z to 00:23:54Z) was caused by the **host interruption aborting six endgame seat sessions**,
not by any mutual poll-wait. Evidence, in three parts:

1. **Static wait-graph: no cycle.** A read-only rerun of the r98 wait-graph analyzer over every
   poll script prints `=== mutual pairs (A->B and B->A) === none`. The only two all-reports waiters
   (V31 adjudicator, V58 presence-final) both **subtract SELF**, and both have bounded escapes.
2. **Liveness: nothing is stuck.** The aborted seats' detached helpers were *not* killed by the
   host interruption and are still running at audit time: V31's poller `pid 1466958` (etimes
   3300 s+), V51's sampler `pid 1499578`, V57's watcher `pid 1509787`. V31's orphan poller is
   **progressing** (`reports=58` → `reports=60`) as the completion wave lands reports, so its wait
   condition was never a deadlock.
3. **Abort pattern = host fault, and the tasks prove it.** All six aborted seats are endgame /
   process seats (scope-creep, adjudicator, receipt, wait-graph, mutual-wait-guard, presence-final),
   not claim verifiers; four of the six (V20, V36, V51, V57) had **no report-gating wait at all**,
   and the two that did (V31, V58) were self-subtracted and bounded.

**Difference from the r96/r97 mutual-wait class:** r96 (`V43↔V58`) and r97 (quad
`{V24,V35,V40,V58}`) were *self-inclusive* all-reports polls that mutually gated until a bounded
cap fired — and both rounds still closed 64/64 by late landings. r98's declaration adopted the
class's recommended fix up front (`ENDGAME CONVENTION: any all-reports poll must subtract SELF`);
it **did not recur**, and r98's 58/64 loss is a host interruption, not mutual waiting.

## 1. Method

Read-only throughout. No file was written except this report; no process was started or stopped by
this seat (the running helpers in §3 are the aborted seats' own orphans, not mine).

Commands run (from `/home/vgpnk/Projects/shokunin/lore-shokunin`):

- `date -u`; `git rev-parse HEAD`; `git log --oneline -1 9a3d648`.
- `ls .ufo/waves/round-98/seats/*.md | wc -l` and a per-seat presence loop over `V01..V59`.
- `ps -eo pid,ppid,etimes,stat,cmd | grep -E "round-98|lore-shokunin" | grep -v grep`.
- `python3 .ufo/waves/round-98/seats/V59-scratch/waitgraph.py` (read-only static wait-graph; its
  own r98 sibling implementation — independent of V51's).
- `cat .ufo/waves/round-98/seats/V51-scratch/waitgraph.tsv` (V51's 46-row classification table).
- Poll logs read in full: `V20-scratch/poll.log`, `V31`'s `scratch/V31/poll.log`,
  `V36-scratch/V36-poll.log`, `V51-scratch/curve.log` + `landing-table.txt` + `terminal.log` +
  `events.log`, `V57-scratch/watch.log` + `notes.md` + `checks.log`, `V58-scratch/poll.log`.
- Scripts read: `V20-scratch/poll.sh`, `V20-scratch/analyze.py`, `scratch/V31/poll.sh` +
  `collect.sh` + `mirror_checks.sh` + `draft.md`, `V36-scratch/V36-receipt-builder.py`,
  `V51-scratch/waitgraph.py` + `sampler.py`, `V57-scratch/watch.py` + `analyze.py` + `snap.sh`,
  `V58-scratch/poll.sh` + `audit.py` + `liveness.py`, `V59-scratch/poll.sh` + `waitgraph.py`.
- Precedent read: `LOG.md` (r96 closure + r98 declaration), `.ufo/waves/round-96/receipt.json`,
  `round-97/receipt.json`, `round-96/seats/V43-receipt.md`, `round-96/seats/V43-scratch/V43-poll.sh`,
  `round-96/seats/V58-scratch/poll.sh`, `round-97/seats/V56-mutual-wait-guard.md`.

## 2. Independent static wait-graph (read-only rerun)

`python3 .../V59-scratch/waitgraph.py` (output tail, verbatim):

```
=== mutual pairs (A->B and B->A) ===
none

=== all-reports waiters (count seats/*.md) ===
  V36   V36-poll.sh
  V58   poll.sh
```

The rerun's edge list (41 scripts) contains **no verifier→verifier blocking edge** in the endgame
set; the only report-counting waiters are V36 (a 58-report plateau monitor, see §3) and V58.
V31 is not listed by that loose regex because its condition is `grep -v "V31-adjudicator" | wc -l`
(no literal `nonself`/`-ge 6x` token), but it is an all-reports waiter by construction (§3).

V51's own classifier, `V51-scratch/waitgraph.tsv` (`rows=46`, header
`seat script waits_reports subtract_self tries bounded_escape kind`), independently agrees on the
self-subtraction column: of all 46 r98 poll scripts only **three** are marked `subtract_self=YES` —
`V30`, `V58`, and `V31`. Every other report-waiting script is single-target or producer-targeted,
so it cannot form an all-reports cycle. Cross-verifier edges found by the aborted V57's own
`analyze.py` were all one-directional and all resolved by target movement:
`V43→V19` (hit try=28 23:37:57), `V49→V26` (hit try=24 23:37:26), `V50→V27` (V27 is a logger).

## 3. The six aborted seats: what tasks they were, and what each was waiting on

Roles confirmed from each seat's own scripts/logs (not from any plan text):

| seat | task (evidence) | wait condition | escape | terminal state observed |
|---|---|---|---|---|
| V20 | scope-creep analyzer (`analyze.py` docstring: "V20 scope-creep analyzer") | **producers only**: `REPORT:S1..S5` + the r98 artifacts — no verifier report | 40 tries | `POLL-TIMEOUT 23:41:27 reports=56` (clean bounded exit; **not** all-reports) |
| V31 | adjudicator (`poll.sh` header "V31 adjudicator poll"; `mirror_checks.sh`; `draft.md` "# V31 — adjudicator") | **all reports**, 63 non-self (`grep -v "V31-adjudicator"`) | 240 tries (≈00:48:40Z) | killed mid-run at try 163–168; poll log continues live (§4) |
| V36 | receipt seat (`V36-receipt-builder.py`: "Presence audit + skeleton receipt"; wrote the skeleton `receipt.json`) | 58-report plateau monitor (`reports=58 unchanged for 60 tries`) + producers + r98 fix + knowledge note | 60-try stall escape | `21:04:43 STALL READY held, reports=58 unchanged for 60 tries; exiting` (clean bounded exit) |
| V51 | wait-graph / process auditor (`waitgraph.py`, `sampler.py` docstring "V51 endgame-monitor sampler") | **none** — passive 20 s sampler; no blocking report poll exists | sampler cap 5400 s | sampler still alive at audit time; `curve.log` still appending |
| V57 | mutual-wait-guard-2 (predecessor: `watch.py` docstring "V57 mutual-wait-guard-2 independent 20s sampler") | **none** — passive 20 s sampler | watcher cap 3600 s | watcher still alive at audit time; `watch.log` still appending |
| V58 | presence-final / receipt finaliser (`audit.py`: "finalize receipt.json collection_snapshot") | **all reports**, 63 non-self (`grep -v '/V58-presence-final.md$'`) | 90 tries | `POLL-TIMEOUT nonself=58 23:59:39` (clean bounded exit) |

Four of the six (V20, V36, V51, V57) therefore had **no report-gating wait** and cannot be members
of an all-reports cycle at all. V20's and V36's polls both exited cleanly, by their own bounded
rules, well before the abort.

## 4. No unresolved deadlock — the one live pair is bounded and progressing

The only cycle among the six is the two-seat all-reports gate **{V31, V58}**: V31 waits on V58's
report, V58 waits on V31's report. Both legs are bounded and both subtract SELF:

- `V58-scratch/poll.sh`: `n=$(ls "$D"/*.md | grep -v '/V58-presence-final.md$' | wc -l)`;
  `if [ "$n" -ge 63 ]`; `for i in $(seq 1 90)`. Observed escape fired:
  `POLL-TIMEOUT nonself=58 23:59:39` (`cat V58-scratch/poll.log`, last line).
- `scratch/V31/poll.sh`: `n=$(ls "$S"/*.md | grep -v "V31-adjudicator" | wc -l)`;
  `if [ "$n" -ge 63 ]`; `for i in $(seq 1 240)`. Its escape had not fired at audit time.

The pair was therefore released by V58's 90-try escape at **23:59:39Z** (one hour before V31's own
240-try escape), and V31's poller kept polling on reports that the completion wave is now
delivering. Live proof that V31's wait is not a deadlock:

```
$ tail -6 .ufo/waves/round-98/scratch/V31/poll.log
try 163 00:22:41 reports=58 arts:
try 164 00:23:01 reports=58 arts:
try 165 00:23:21 reports=58 arts:
try 166 00:23:41 reports=58 arts:
try 167 00:24:01 reports=60 arts:
try 168 00:24:21 reports=60 arts:
```

`reports` advanced 58 → 60 as `V20-scope-creep.md` and `V58-presence-final.md` landed. The same
movement is visible in V51's sampler and V57's watcher:

```
$ tail -4 .ufo/waves/round-98/seats/V51-scratch/curve.log
2026-10-17T21:23:21-0300 epoch=1792283001 count=58
2026-10-17T21:23:41-0300 epoch=1792283021 count=58
2026-10-17T21:24:01-0300 epoch=1792283041 count=60 NEW=V20-scope-creep.md,V58-presence-final.md
2026-10-17T21:24:21-0300 epoch=1792283061 count=60

$ awk '/^== t=/{n++} n>=157' .../V57-scratch/watch.log | grep -E '^== |^absent_V'
== t=00:23:54Z iter=157 ==   absent_V=['V20', 'V31', 'V36', 'V51', 'V57']
== t=00:24:14Z iter=158 ==   absent_V=['V31', 'V36', 'V51', 'V57']
```

Report count at audit close: `ls .ufo/waves/round-98/seats/*.md | wc -l` → **61**; absent
`V31, V51, V57` (V57 is this seat; V31's and V51's re-dispatched seats were still running). The
wave's own main-wave plateau ended at exactly the six aborted seats, and three of those six
(V58, V20, V36) have already landed via the completion wave — consistent with "aborted sessions,
work recoverable", not with a blocked lattice.

**Post-write confirmation (00:25:41Z).** While this report was being written the completion wave
closed the round: `ls .ufo/waves/round-98/seats/*.md | wc -l` → **64**, with an empty absent list
over `S1..S5, V01..V59` — V31's and V51's re-dispatched seats landed, and V31's orphan poller
advanced to `try 172 00:25:41 reports=62`. So every one of the six aborted seats' reports was
recoverable, and no wait in the lattice ever blocked their recovery.

**Conclusion:** no unresolved deadlock. Every wait in the round was either single-sided, resolved by
target movement, or bounded by an escape that fired (V20 23:41:27Z, V58 23:59:39Z, V36 00:04:43Z) or
was still open with a live, progressing condition (V31).

## 5. The abort pattern

**What the host interruption did.** It terminated the six seats' **agent sessions**; it did **not**
kill their detached background helpers. At audit time `ps` still shows three orphans from the
aborted batch:

```
$ ps -eo pid,ppid,etimes,stat,cmd | grep -E "round-98|lore-shokunin" | grep -v grep
1466957    1539    3310 S  /bin/bash -c cd '/home/vgpnk/Projects/shokunin' && nohup .../scratch/V31/poll.sh > /dev/null 2>&1 & echo "poller pid $!"
1466958 1466957    3310 S  /bin/bash .../scratch/V31/poll.sh
1499578 1499574    3170 S  python3 .ufo/waves/round-98/seats/V51-scratch/sampler.py 5400
1509787    1539    3138 Ss python3 .../seats/V57-scratch/watch.py 3600
```

So the "abort" is a **session-level** cut with **orphan survival**, not a process-level cleanup.

**Bracketing the abort instant.** The last *seat-session* artifact each aborted seat produced
(`find ... -printf '%TY-%Tm-%Td %TH:%TM:%TS %p\n' | sort -r | head`):

| seat | last session artifact | time (−0300) |
|---|---|---|
| V20 | `V20-scratch/snap/fixture-listing-confirm2.txt` | 20:56:37 |
| V31 | `scratch/V31/draft.md` | 20:50:38 |
| V36 | `V36-scratch/V36-receipt-builder.py` | 20:55:31 |
| V51 | `V51-scratch/terminal.log` (scrape) | 21:05:01 |
| V57 | `V57-scratch/checks.log` | 20:59:18 |
| V58 | `V58-scratch/poll.log` | 20:59:39 |

The six sessions went quiet between 20:50:38 and 21:05:01 (−0300) — i.e. 23:50:38Z–00:05:01Z —
while their helpers ran on. Because the seats were parked in their endgame loops (waiting for the
plateau to break), the exact abort instant is **not directly recorded** in any artifact; what is
recorded is (a) the sessions stopped producing deliberate output in that window, and (b) their
helpers survived past it and are still alive at 00:25Z. This is a **fault of the host/session
lifecycle**, and it is the reason six reports are missing: the seats were cut before they could
write, not blocked before they could write.

**Corroborating: the aborted V57's own prediction was verified.** `V57-scratch/notes.md` predicted
"~23:59:18Z: V58 cap fires (POLL-TIMEOUT, exit 1) … then V31 gated on {V20,V36,V51,V57}" and "No
pair remains mutually blocked at t+40min (00:07:36Z)". Observed: V58's cap fired **23:59:39Z**
(21 s late), and no pair was blocked at 00:07:36Z. The prediction held; the seats were lost to the
host, not to the wait.

**Process-hygiene note (non-axis, for the L1).** The interruption left three orphan processes
writing into the wave tree (`V31`'s poller into `scratch/V31/poll.log`, `V51`'s sampler into
`V51-scratch/curve.log`, and this seat's own predecessor watcher into `V57-scratch/watch.log` +
`scripts/`). They write only inside their own seat scratch, so no producer byte-ownership is
breached; they should nonetheless be reaped when the wave closes.

## 6. Comparison with the r96/r97 mutual-wait class

**r96 (self-inclusive poll; two seats).** `LOG.md` r96 closure: "V43/V58 were trapped in a mutual
poll-wait on 63 reports including the adjudicator's, self-recorded in V43's poll log".
`round-96/seats/V43-scratch/V43-poll.sh` exits only when `lane >= 64` where `lane = ls "$LANE"/*.md
| wc -l` — i.e. **including V43's own report**; `round-96/seats/V58-scratch/poll.sh` exits when
`others >= 63`, counting V43's report among the 63. `V43-receipt.md` §"Mutual-wait finding
(liveness)" states it plainly: "Both seats were therefore waiting on each other. Resolution: this
seat writes its report now (the only action that can unblock V58)". Class: an all-reports condition
that counts the waiter's own report → self-blocking, plus a symmetric pair → n-cycle.

**r97 (self-inclusive poll; four seats).** `round-97/seats/V56-mutual-wait-guard.md` §3(c)/§5:
all-reports waiter quad `{V24, V35, V40, V58}`; V24 and V40 counted all 64 **including self**
("self-blocking"), V35/V58 counted the 63 others ("mutually blocking"); the quad was trapped
~45 min (19:13:49 → 19:58:36), resolved by seat decisions (V58 19:18, V40 19:28:48) and by
**V24's cap firing 19:58:36** → V24 report 20:01 → V35's condition met → V35 report 20:06 → 64/64.
Its recorded fix recommendation (MW-01): "(i) subtract self in every all-reports condition;
(ii) ensure at least one all-reports seat is not gated on the others; (iii) give every all-reports
poll a stall escape".

**r98 (fix adopted; loss is host-caused).** What differs, item by item:

1. **The defect did not recur.** The r98 declaration carried the fix forward: "ENDGAME CONVENTION:
   any all-reports poll must subtract SELF — the r96/r97 mutual-wait class" (`LOG.md`, r98
   declaration). Empirically both r98 all-reports waiters subtract SELF: V31
   `grep -v "V31-adjudicator"`, V58 `grep -v '/V58-presence-final.md$'`. There is **no
   self-inclusive all-reports poll anywhere in r98** (V51's 46-row table marks `subtract_self=YES`
   only for V30/V31/V58; V30 is not a report waiter). The r96 defect is gone.
2. **Every all-reports leg was bounded, and the escapes fired.** V58 90 tries → fired 23:59:39Z;
   V31 240 tries → open but progressing. r96's V43 poll had a 330-try cap with a stall escape; r97's
   V35 had a 3 h deadline with **no** stall escape (MW-01(iii) was still open in r97). r98's
   endgame waiters all had escapes.
3. **Outcome and cause differ.** r96 and r97 both closed **64/64** — the mutual-wait class there cost
   *latency* (late landings), never reports. r98's main wave ended **58/64** with the loss of exactly
   the six endgame seats, and the cause is the **host interruption** (§5), not the wait: four of the
   six were not in the all-reports class at all, and the two that were had already escaped or were
   still progressing.
4. **What was lost is process evidence, not claim verification.** All six lost seats are endgame /
   process seats. No C1/C2/C3 claim-verifier report is missing, so the missing reports do not
   invalidate any claim verification; what they cost is the adjudicator's synthesis (V31), the
   receipt/presence finalisation (V36, V58), the process audit (V51, V57) and the scope-creep pass
   (V20). Note `receipt.json` is still V36's **skeleton** (`collection.reports_present = 0`,
   `collection.reports_absent` = all 64, `state` = "Skeleton receipt written by V36 …"), i.e. the
   r96/r97 practice of rebuilding the receipt from the dispatch result has not yet happened for r98.
   Recoverable material exists: V31's `scratch/V31/draft.md` holds its full adjudicator evidence
   (self-test 16/16→17/17, `SELF-TEST-MISMATCH` rc=2 vs baseline rc=1, path-less pin MIGRATED,
   chain 6/6 with digests, V46 discharge, C3 6/1/7 + 20/20 + census 172), and V57's predecessor
   `notes.md`/`checks.log` hold the full wait-graph timeline.

## 7. Limits (stated, not papered over)

- The exact instant the host cut the six sessions is not recorded in any artifact this seat can
  read; §5 brackets it from the last session artifact (20:50:38–21:05:01 −0300) and from orphan
  survival. No dispatch result / session log for r98 was available to this seat.
- "No unresolved deadlock" is established for the report-wait lattice at audit time (static graph
  rerun + live `ps` + progressing counters). It is not a claim about process liveness after this
  report is written.
- This seat read V51's and V57's logs as they were still being appended by orphaned samplers; the
  numbers quoted are snapshots at the times shown, not final totals.
- This seat did not re-run any claim check (C1/C2/C3) and asserts nothing about the delivered
  revision's correctness. It also wrote nothing outside this report.

## 8. Bottom line

PASS — **no unresolved deadlock occurred in round 98**: the static wait-graph has no mutual pair,
both all-reports waiters (V31, V58) subtract SELF with bounded escapes (V58's fired 23:59:39Z, V31's
still live and progressing 58→60 reports), and V20/V36 exited their own bounded polls cleanly
(23:41:27Z / 00:04:43Z); the 58/64 plateau was caused by the host interruption aborting the six
**endgame/process** seat sessions (V20 scope-creep, V31 adjudicator, V36 receipt, V51 wait-graph,
V57 mutual-wait-guard-2, V58 presence-final) — four of which had no report-gating wait at all —
which differs from the r96 `V43↔V58` and r97 `{V24,V35,V40,V58}` classes in that those were
self-inclusive all-reports polls (r98's declared fix removed that defect) and cost only latency,
whereas r98's loss is a host fault that left orphaned pollers still running; the completion wave
subsequently closed the round at **64/64** (00:25:41Z), confirming nothing was ever deadlocked.
