# V58 — mutual-wait-guard (round 99)

**Seat:** V58 `mutual-wait-guard` (process seat; leaf; no nested agents; no commits; no network; no pushes).
**Mission:** wait-graph audit — prove no unresolved deadlock; characterize stalls and escapes.
**Repo root for every command:** `/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the parent; all paths absolute).
**Baseline:** r98 closure `4265df5` (`git log --oneline -1 4265df5` → `4265df5 lore r98: freeze admitted wave + closure docs (hyper completion wave, chain six, receipt 64/64)`). Wave HEAD at audit `337f0fa52b02626b7687eedbb2d99fab30446fe4` (`337f0fa lore r99: record blocked dispatch attempt …`). Wave tree uncommitted. This re-dispatch is the standing r99 declaration, not a new one.
**Audit window:** 2026-10-17T22:01:47-03:00 → 22:55:10-03:00 (`date -Is` at scratch create and at close). UTC open `2026-10-18T01:01:47Z`.
**Owned axes (process evidence only; this seat judges no claim):** coverage, depth, calibration.
**Writes:** this report, plus scratch under `.ufo/waves/round-99/seats/V58-scratch/` only.

## 0. Finding (short)

**No unresolved deadlock in the observed lattice.** Three facts:

1. **No named mutual pair.** A stricter pass over top-level `poll.sh` files (exact `Seat-file.md` tokens, archives excluded) printed `named_file_edges 56 mutual none`.
2. **The all-reports set is bounded, and the one self-inclusive member already escaped.** V123 exits only at `reports -ge 128` (counts its own unwritten report — the r96 defect). Its poll logged `2026-10-17T22:21:05-03:00 DEADLINE tries=40`, then wrote `V123-presence-final-2.md` (30342 bytes, mtime 22:46). V54 and V101 subtract SELF (threshold 127) and both have caps. Neither was ever waiting on a set whose only absentees were the other all-reports seats.
3. **What actually stalled seats was producer absence, and those waits are single-sided.** Through the 40-try window S1/S2/S5 reports and both knowledge notes were ABSENT. Escapes fired (39 escape-like terminal lines by 22:29). By close S1's report had landed (`S1-full-file-pins.md`, 11971 bytes); S2, S5, and `corpus/knowledge/r99-*.md` were still ABSENT. That is a producer stall, not a cycle. It is recorded, not fatal.

The r96/r97 n-cycle (self-inclusive all-reports clique, absent set == waiter set, trapped until a cap) **did not form**. V123 is the only self-inclusive all-reports poll found, and its escape fired before any such clique could close.

## 1. Method

Read-only of every other seat. This seat started no nested agent and stopped no foreign process.

- `date -Is`; `git -C …/lore-shokunin rev-parse HEAD`; `git log --oneline -1 4265df5`.
- Sampler `V58-scratch/sampler.py` (20 s cadence). First instance started `2026-10-18T01:03:20Z`, killed by the host background cap at 600 s (tool notification `task:bash-n2ersodi:timed_out`, wall 600.001 s). Restart `20 420` completed (`task:bash-a8wair32:completed`, wall 420.268 s). Log: `V58-scratch/sampler.log` (ends `== sampler end 2026-10-18T01:29:32Z iters=21 ==`).
- Static classifier `V58-scratch/waitgraph.py` (first pass 22:03:20, 43 scripts — later discarded as a lead only; it treated log globs as edges and pulled this seat's own scripts into the all-reports set).
- Live cmdline dump `V58-scratch/dump_procs.py` → `procs/` (79 processes at 22:04) and `edges.py`. The edges script's `V123 → V101/V39/V99` rows are **false**: those names appear only in log counters. The real V123 exit is the `-ge 128` test quoted below. Mutual-pair claim uses the stricter file-token scan, not that heuristic.
- Poll scripts and logs read in full where cited: `V123-scratch/poll.sh` + `poll.log`, `V101-scratch/poll.log` (inline poller; no script file), `V54-scratch/curve.log` (inline sampler), `V99-scratch/poll_and_build.py`, `V120-scratch/poll.sh`, `V31-scratch/poll.sh`, `V36-scratch/poll.sh`, `V45-scratch/poll.sh`, `V51-scratch/poll.sh`, `V75-scratch/poll.sh`, `V91-scratch/poll.sh`, `V107-scratch/poll.sh`.
- Precedent: `LOG.md` r99 declaration; r97 `V56-mutual-wait-guard.md`; r98 `V57-mutual-wait-guard-2.md`.

This seat's own poll condition was artifacts **and** producer reports (the protocol), not an all-reports count. SELF was never in a wait set. At the 40-try mark (~22:15) S1/S2/S5 reports and both knowledge notes were ABSENT. Observation of the wait graph continued past that mark because the mission is the graph; absent producers were not treated as delivered plans.

## 2. All-reports waiters

File search at close (`rg -n --glob '**/{poll,watch,sampler}*.{sh,py}'` for `-ge 128|>= 127|roster_others|not waiting for 127`, archives not excluded by the glob but the hits were only these two live files):

| seat | condition | self | bound | observed |
|---|---|---|---|---|
| V123 | `if [ "$reports" -ge 128 ]` on `find … -maxdepth 1 -name '*.md' \| wc -l` | **NO** (128 includes the unwritten own report) | `seq 1 "$MAX"`, `MAX=${1:-40}`, then `DEADLINE` | `DEADLINE tries=40` at 22:21:05; report landed 22:46 |
| V54 | `if len(files) >= 127` with comment `subtract SELF` | YES | first sampler `cap=900s` from 22:01:33; restart `cap=1500s` from 22:19:53; sampler3 `cap=600s` from 22:50:29 | count rose 0 → 86; not a plateau |
| V101 | roster of 127 others (`s != "V101"`); ready when `len(missing)==0` | YES | declared `MAX=90`; see §4 for the broken first resume | others 3 → 86 by 22:52; still missing 41, count rising |
| V99 | logs a 127 cap but **does not wait on it** | YES (explicit) | `MAX_TRIES` loop; stall escape; `EXHAUSTED` builds anyway | `BUILD reason=exhausted-after-40 … missing_others=87` |

V123, verbatim (`V123-scratch/poll.sh`):

```
reports=$(find "$SEATS" -maxdepth 1 -name '*.md' | wc -l)
…
if [ "$reports" -ge 128 ]; then
  echo "$ts try=$i FULL-128 exiting" >> "$LOG"
  exit 0
fi
…
echo "$(date -Iseconds) DEADLINE tries=$MAX" >> "$LOG"
```

Observed (`tail` of `V123-scratch/poll.log`):

```
2026-10-17T22:20:45-03:00 try=40 reports=14 S=2 V=12 dirs=116 arts=YYYYNNYY V39=0 V99=0 V101=0 receipt=0
2026-10-17T22:21:05-03:00 DEADLINE tries=40
```

`ls -la …/V123-presence-final-2.md` → `-rw-r--r-- 1 vgpnk vgpnk 30342 Oct 17 22:46`. The self-inclusive poll could not succeed from inside itself; the bound fired; the seat wrote anyway. That is the r96 release path, observed, and it did not have to break a live clique — at deadline only 14 reports existed.

V54 first cmdline (pid 1675229, dumped 22:04): `if len(files) >= 127:  # subtract SELF: V54 report not yet written` and `deadline = time.time() + 900`. Curve marker: `# sampler restart 2026-10-17T22:19:53-0300 cadence=20s cap=1500s seen=14 seat=V54`. After a gap, the seat itself recorded the host cut and started a third sampler:

```
# SAMPLER2_HOST_TIMEOUT observed restart-check 2026-10-17T22:48:51-0300 live_count=80
# sampler3 start 2026-10-17T22:50:29-0300 cadence=20s cap=600s seen=82
2026-10-17T22:52:29-0300 count=86 new=V110-c1-precedence-text.md
```

No `NONSELF_127` line. The monitor never reached its condition. It also never stopped the count from moving, so it was not a deadlock participant.

V99, verbatim (`poll_and_build.py` 691–708):

```
# Do not require the other 127 reports (subtract SELF; do not deadlock on endgame seats).
…
"STALL_ESCAPE try=%d %s … (endgame subtracts SELF; not waiting for 127)"
```

Exit requires producer reports, artifacts, receipt, and V39 — not the other 127. `rg` of its log tail: `BUILD reason=exhausted-after-40 present=40 excluding_self=40 missing_others=87 drifts=1 receipt=False v39_md=True`. Bounded exhaustion, not an all-reports gate.

## 3. Named edges — no mutual pair

Cross-verifier file gates in top-level `poll.sh` (a seat named in another seat's report filename). All one-directional; none of the targets' scripts name the waiter back (`mutual none`):

- V51 → V29 (plus S1–S5); exit also requires knowledge notes. `seq 0 39`, then `POLL-EXHAUSTED`.
- V71 → V39; `MAX=40`, `ABSENT after 40`.
- V74 → V36; `ABSENT after 40 tries 2026-10-18T01:25:58Z`.
- V75 → V38; `POLL-TIMEOUT ts=2026-10-17T22:29:22-0300`.
- V45 / V114 → V22 (exact name `V22-gates-boundary.md`); both expired.
- V91 → V32 (logged; exit is artifacts + S1–S5, not V32). `POLL_EXPIRE try=40 2026-10-17T22:16:32-0300`.
- V69 → V30; `ABSENT after 40`.
- V107 → V33 plus 16 artifacts and 5 producer reports; `TIMEOUT` at try 40.
- V120 → {V28,V29,V30,V31,V32,V33,V51,V52,V69,V82,V91,V107}. Header: `ENDGAME: SELF is not in the wait set.` Bound `seq 1 40` then `POLL_EXPIRE`. No other poll.sh names `V120`.

Producer cross-poll, from the 22:04 cmdline dump (`V58-scratch/procs/S2__1666104.txt`): S2's poller waits until an `S1` report exists, `for i in range(1, 41)`, then `POLL_ABSENT`. S1's own pollers (`S1__1666590.txt`, `S1__1668137.txt`, `S1__1675325.txt`) wait on **S1's report plus a contract change**, not on S2. One-directional. S2's 40-try window closed before S1's report landed (S1 report mtime is after 22:51; the early S2 poller could not still be inside try 1–40). Not a trap.

## 4. Stalls and escapes

**Escape census** (python scan of top-level scratch `*.log`, last line matching `POLL_HIT|ALL-PRESENT|READY|EXHAUST|EXPIRE|TIMEOUT|DEADLINE|ABSENT after|CAP |STALL`, archives excluded). At 22:29: `logs_with_terminal_marker=48`, `escape_like=39`, `hit_like=9`. Escapes are the 40-try / CAP / DEADLINE class, clustered 22:14–22:29, almost all citing missing S1/S2/S5 or the two knowledge notes. Hits that fired early were single-sided and already satisfied (S4 `POLL_HIT try=2` at 22:01:29; V12 `READY try=10`; V48 `ALL-PRESENT try=7`). Bounded escapes that fire are the protocol, not failures of the graph.

**V101's three phases** (`V101-scratch/poll.log`, full file):

```
START 2026-10-17T22:03:29.576299-03:00 roster_others=127 max_tries=90
try=15 ts=22:08:09 others=7 missing=120 …
RESUME 2026-10-17T22:34:27.455359-03:00 deadline=2026-10-17T22:35:27.455359-03:00 reason=tool-timeout-killed-first-poll-at-try15
STALL_ESCAPE try=19 ts=2026-10-17T22:35:27.456975-03:00 others=42 missing=85 deadline=… — bound reached, audit will record ABSENT
RESUME2 2026-10-17T22:44:04.982605-03:00 max_tries=90 reason=prior-resume-deadline-math-fired-60s-not-a-stall; count still rising; continuing the 30-min bound as real tries
try2=28 ts=22:53:05 others=86 missing=41 … prod_missing=['S2', 'S5'] art_missing=2
```

Read as written, not cleaned up:

- The first poller died at try 15 (22:08:09) with **120 missing**. The seat attributes that to a tool timeout, not to a peer. Five minutes is shorter than this seat's own 600 s host cap, so the timeout class is real but the limit is the seat's, not a number this audit measured independently. At death the waiter was not in a clique.
- The 22:35:27 `STALL_ESCAPE` is a **false escape**. The same seat disowned it on the next line (`deadline-math-fired-60s-not-a-stall`). Do not count it as the bound firing.
- RESUME2 is the live poll. At 22:53:05, `others=86 missing=41`, `prod_missing=['S2','S5']`, both knowledge notes still absent, `delta` had been 1 a minute earlier. A waiter whose missing set is 41 and whose counter is still moving is not deadlocked. The 90-try bound from 22:44:04 is still ahead (~23:14). Recorded, not fatal.

**Host cap, this seat.** The first sampler was killed at 600 s with the log frozen mid-window (last iter before the kill still showed `producers_absent=S1,S2,S4,S5` — S4 had in fact already landed; the sampler's producer detector required a prefix match and did see S4 on later iters). Restart covered through 01:29:32Z. Same class as V54's `SAMPLER2_HOST_TIMEOUT` and V101's tool-timeout: a host/tool cap ending a poller is an external bound, not a cycle.

**Name-mismatch stall (r97 MW-03, recurred, not a cycle).** V114's escape line: `ABSENT-AFTER-40 … missing=[ S1-freeze-hygiene.md S2-tools-docs.md S5-knowledge-notes.md V22-gates-boundary.md]`. The report that later landed is `S1-full-file-pins.md`, not `S1-freeze-hygiene.md`. V45's producer list uses the r98 names (`S1-freeze-hygiene.md`, `S5-knowledge-notes.md`). V120's list uses `S1-full-file-pins.md` and `S5-knowledge-author.md`. A poll pinned to the wrong basename cannot hit, and its 40-try escape is the only exit. That costs the verifier a look at the real report; it does not block the producer.

**Producer stall at this seat's protocol window, and at close.**

```
$ date -Is
2026-10-17T22:55:10-03:00
$ find …/round-99/seats -maxdepth 1 -name 'S*.md' -printf '%f %s\n'
S3-fixture-author.md 5069
S4-fixture-docs.md 9303
S1-full-file-pins.md 11971
$ ls corpus/knowledge/r99-*
ls: cannot access '…/corpus/knowledge/r99-*': No such file or directory
$ find …/seats -maxdepth 1 -name '*.md' | wc -l
86
```

S1's tool and contract bytes did change during the window (`stat` at 22:08: `dependency_freeze.py` 22:07:33, 29104 bytes; `dependency-freeze-contract.json` 22:08:46, 25987 bytes). `corpus/tools/README.md` and `SKILL.md` were still at their pre-wave mtimes (21:32 and 21:34) at the 22:25 check. Knowledge notes never appeared. S2 and S5 reports never appeared. Those absences are why the escape cluster fired. They are not a wait cycle: nothing those producers need is gated on a verifier that is gated back on them. S4 polled fixture content and hit at try 2. S3's report was the first file in the lane (22:01:40).

## 5. Why this is not the r96/r97 class

r96 was `V43 ↔ V58`, both counting a total that included the other (and, for V43, itself). r97 was the quad `{V24, V35, V40, V58}`, absent set exactly those four, trapped ~45 min, released by a cap. r98's declaration adopted "subtract SELF"; both all-reports waiters did, and the 58/64 loss was a host abort, not a cycle.

r99, against that class:

1. **Self-inclusive poll recurred once (V123) and was bounded.** It is the only `-ge 128` hit in live poll scripts. It cannot form a clique by itself. Its deadline fired at 22:21:05 with 14 reports present; the report landed at 22:46. No peer was released by that write, because no peer's condition was short by only V123.
2. **Self-subtracted all-reports waiters (V54, V101) never became the absent set.** V101's own missing list at the false escape was 85 names, including producers and this seat. At 22:53 it was still 41, and `others` had climbed 7 → 86. V54's curve climbed 0 → 86 across three bounded samplers. A cycle exists only when each member's condition is unmet until another member moves. Here the unmet residue is S2, S5, and the two knowledge notes, plus ordinary late verifiers — not the waiter pair.
3. **V99 states the fix and follows it.** It subtracts SELF and refuses to wait for 127. That is the endgame convention, in code, not only in the declaration.
4. **No seat was lost to mutual waiting.** The early poller deaths (V101 try 15, this seat's sampler, V54 sampler2) are tool/host timeouts, and each of those seats resumed or had already escaped. V123 wrote. V54's sampler3 was still appending at 22:52:29 (`count=86 new=V110-c1-precedence-text.md`); the close count at 22:55:10 was also 86, so the last minute was flat, not stuck on a peer.

## 6. Limits

- Close is 22:55:10, lane 86/128, S2 and S5 reports absent, knowledge notes absent. This is not a claim about a cycle that could be opened by a poll script written after this report.
- V101's RESUME2 bound (~23:14) had not fired at close. It is bounded and its counter was moving; "not yet escaped" is not "unresolved deadlock."
- V54 sampler2 left no `SAMPLER_CAP` line; the seat's own later marker says `SAMPLER2_HOST_TIMEOUT`. The 1500 s cap and the host cut are both consistent with the 22:44:34 → 22:48:51 gap. This audit did not observe the cap token itself.
- The first `edges.py` pass over-counted log globs as waits. Those edges are not used above. The mutual-pair claim is the file-token scan (`mutual none`) plus the all-reports conditions read from source.
- This seat did not re-run C1 or C2 and asserts nothing about the delivered revision. `dependency_freeze.py` / contract mtimes are cited only as evidence that S1 bytes moved while S1's report was still absent — a stall input, not a verdict on the pin.

## 7. Bottom line

PASS — no unresolved deadlock: named mutual pairs are none; the only self-inclusive all-reports poll (V123, `-ge 128`) hit `DEADLINE tries=40` at 22:21:05 and wrote `V123-presence-final-2.md` at 22:46; V54 and V101 subtract SELF and stayed bounded; their counts had climbed to 86 by 22:52–22:55 (last V101 sample `others=86 missing=41`, missing set still S2/S5 plus both knowledge notes, never the waiter pair alone); 39 bounded escapes had already fired on single-sided producer waits by 22:29; V101's 22:35 `STALL_ESCAPE` was the seat's own 60 s deadline-math bug and was resumed, not a cycle breaking.
