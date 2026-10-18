# V56 — mutual-wait-guard (round 97)

**Seat:** V56 `mutual-wait-guard` (process seat; leaf; no nested agents; no commits; no network).
**Mission:** monitor whether any seat pair is trapped in a mutual poll-wait this round (check poll
logs in scratch dirs at intervals); if found, name the pair and the escape condition; record the
class for the process debt.
**Repo root for every command:** `/home/vgpnk/Projects/shokunin/lore-shokunin`
(session cwd is the parent repo; all paths absolute or `cd`-anchored here).
**Baseline:** r96 closure `f3e09f9`. **Observation window:** 18:43–20:07 local (2026-10-17),
20 s cadence throughout. **Lane at close: 64/64 reports present (20:06).**

## 0. Finding (short)

A **mutual poll-wait formed, was trapped live for ~45 min, and resolved entirely by bounded
escapes**: the four all-reports waiters **{V24, V35, V40, V58}** became the only absent reports at
19:13:49 (60/64), each waiting on the other three. Resolution chain (all observed):
V58 moved 19:18 (write at 60 others) → V40 moved 19:28:48 (write; declared V24/V35 ABSENT per
protocol) → **V24's poll cap fired 19:58:36** (`CAP all=62 stable=0 elapsed=4500s`, `exit 0`) →
V24-scope-creep.md 20:01 → **V35's condition (N≥63) met**, poll exited → V35-adjudicator.md 20:06
→ 64/64. No seat was lost, nothing fabricated; the pair {V24, V35} was the last leg and was
broken by V24's cap exactly as predicted. Class recorded for the process debt (§5 MW-01/MW-04).

## 1. Method

- 20 s sampler `V56-scratch/watch.py` (background, 60 min cap, ended 19:43 cleanly): snapshots
  report counts, tails of every `*scratch*/poll*.log`, new/changed `*.sh` (copied to
  `V56-scratch/scripts/`). Log: `V56-scratch/watch.log`.
- Static wait-graph analyzer `V56-scratch/waitgraph.py`: parses every poll script, maps each seat's
  wait condition to the seat that owns the awaited artifact/report; prints edges, direct mutual
  pairs (A→B ∧ B→A), all-reports waiters, absent reports, terminal markers
  (`POLL_HIT|READY|TIMEOUT|ABSENT|STALL|DEADLINE|CAP`).
- Liveness: `ps -eo pid,etimes,cmd`; state: `stat`, `tail` on the logs cited below.

## 2. Timeline (all times local, −03:00)

| time | event | evidence |
|---|---|---|
| 18:45:37 | R1 tool landed | `stat corpus/tools/map_obligations.py` |
| 18:46:12 | R2 contract 25 cases (`2142b991…`) | `stat`; `scratch-R1/poll-r2.log` |
| 18:46:19 | R1 poll hit try=4 (R1↔R2 mutual dependency resolved, ≤60 s) | `POLL_HIT try=4` |
| ~18:46:48–18:49:50 | R4↔R5 concurrent mutual polling window (~3 min; no deadlock) | §3(a2) |
| 18:49:50 | R5's r97 map landed (`49d4834e…`; 17 facts / 19 rows) | `scratch-R1/poll-r5.log` |
| 18:50:14 / 18:50:28 / 18:51:25 | R4 report → R5 poll hit try=11 → R5 report | `R4-fixture-author.md`, `R5-fixture-docs.md` |
| 18:51:34 | R1's R5-poll condition met (try=12) | `poll-r5.log` |
| 18:52:38 / 18:53:00 / 18:53:21 / 18:56:23 | R6 note / R3 tool (`PATH-MISMATCH`) / R3 contract / R3 report | `stat`; V45 log `path_mismatch_in_tool=2` |
| 18:56:0x–18:57:35 | poll-expiry cluster: V28/V30/V32/V33/V34/V43/V45 (R3 race), V29 (name mismatch) | §3(d) |
| 19:13:49 | **quad {V24,V35,V40,V58} formed** — only absent reports; 60 present | `V58-scratch/collection-curve.txt` `19:13:49=60` |
| 19:18:xx | **V58 escaped** (report + receipt at 60 others; watcher deadline 19:37:49 never reached) | `V58-presence-final.md` |
| 19:28:48 | **V40 escaped** (report; declared V24/V35 ABSENT per protocol) | `V40-receipt.md` |
| 19:58:36 | **V24's poll cap fired** (`CAP all=62 stable=0 elapsed=4500s`, `exit 0`) — predicted ≈19:58:3x | `V24-scratch/poll.log` |
| 20:01 | V24-scope-creep.md landed → 63/64 | `stat` (9952 bytes) |
| ~20:01–20:06 | V35's condition N≥63 met → its poll exited (process gone by 20:03:22) | `ps`; `V35-scratch/poll.sh` |
| 20:06 | **V35-adjudicator.md landed → 64/64; mutual wait fully resolved** | `stat` (31405 bytes) |

## 3. Mutual-wait candidates examined

**(a) R1 ↔ R2 (producer pair) — resolved, no trap.**
R1 polled for R2's 25-case contract (`scratch-R1/poll-r2.sh`); R2's `probes.sh` is headed "run only
against the POST-R1 delivered tool" and its report records polling for the tool (stable sha
`86b52949…` from poll try 9). R1's tool landed 18:45:37, R2's contract 18:46:12, R1's poll hit at
try=4 (18:46:19). Wait ≤ ~60 s; both bounded by 40-try timeouts. **Not trapped.**

**(a2) R4 ↔ R5 (producer pair) — concurrent mutual polling window (~3 min), no deadlock.**
R4 polled for R5's map ("R5's map landed while I polled (11 × 20 s)", `R4-fixture-author.md`);
R5 polled for R4's report (`R5-fixture-docs.md`: first poll on the exact name `R4-fixture-json.md`
missed, relaunched with an `R4*.md` glob → `READY try=11 … 18:50:28`). The two polls overlapped
≈18:46:48–18:49:50. Resolution: R5's map landed ~18:49:50 → R4's poll hit → R4 report 18:50:14 →
R5's poll hit 18:50:28. **Why it could not trap:** R5's map was built deterministically from the
r96 post-repair map (`make_r97_map.py`, no wait on R4's report) — the blocking relation had no
cycle (R4.report→R5.map was a leaf edge). Mutually *polling*, not mutually *waiting*.

**(b) R1 → R5 → R4 → R3 (producer chain) — serial, resolved, no cycle.**
R1 waited for R5's report (`poll-r5.log` try=12, 18:51:34). R5 waited for R4's report (above). R4
did **not** wait on R3's guarded tool: "R3 owns that call; I did not run `--freeze`" — its report
landed 18:50:14, before R3's delivery. R3 delivered 18:53:00/18:53:21 and reported 18:56:23. No
back-edges; the chain was serial and unblocked.

**(c) Endgame all-reports waiters — MUTUAL WAIT QUAD, trapped ~45 min, resolved by bounds.**
All-reports waiter set **{V24, V35, V40, V58}** (V26/V32 require only the six producer reports;
not blocking):

- `V35-scratch/poll.sh`: `N = ls "$SEATS"/*.md | grep -v 'V35-adjudicator.md' | wc -l`; exits when
  `N >= 63`; deadline 10800 s, **no stall escape** (started ≈18:42:51, pid 1176733).
- `V40-scratch/V40-poll.sh`: exits when `lane >= 64` (counts all `*.md` incl. own); stall escape
  `stall >= 45 && lane >= 62`; cap 290 tries (started ≈18:43:51, pid 1188098).
- `V24-scratch/poll.sh`: exits when `ALL >= 64` **and** 3 stable signatures; cap 4500 s with
  `exit 0` (started ≈18:43:34, pid 1185365).
- `V58-scratch/watch.sh`: exits when 63 *other* reports exist; deadline 1800 s (first instance
  killed at 18:53:47 by the host's 600 s background-task timeout — V58's own report documents
  this; restarted 18:57:49).

**Formation:** at 19:13:49 (V37-debt.md landed) the lane held 60 present and the only absent
reports were exactly these four — each requiring the other three, an n-cycle mutual poll-wait (the
r96 `V43↔V58` class, four-seat). All four poll processes verified live at 19:15:14 via `ps`.

**Trapped interval:** 19:13:49 → 19:58:36 (V24's cap) — **~45 min** during which the four seats'
reports were mutually gated. Resolution chain (observed end-to-end):

1. **V58 moved 19:18** — wrote at 60 others ("missing: V24, V35, V40 … active at the snapshot");
   its watcher deadline 19:37:49 was never reached.
2. **V40 moved 19:28:48** — wrote with "V24 and V35 never landed; both are past the round's
   poll-wait protocol window … Reported ABSENT, per protocol".
3. **V24's cap fired 19:58:36** — `V24-scratch/poll.log`: `2026-10-17 19:58:36 CAP all=62
   stable=0 elapsed=4500s` (script then `exit 0`); V24-scope-creep.md landed 20:01 → 63/64.
4. **V35's condition met** (N=63 after V24's report) — its poll exited (process gone by 20:03:22);
   V35-adjudicator.md landed 20:06 → **64/64**.

The pair **V24 ↔ V35** was the last leg (V35 short by exactly V24's report; V24 needing all 64)
and was broken by V24's cap exactly as predicted (≈19:58:3x).

**(d) Cross-verifier and producer-report edges — escapes fired, no traps.**
- V48→V23: resolved — V23 report landed 18:48; V48's poll log shows `absent` through try=13.
- V44→V04: resolved — V04 landed 18:48; V44 poll `READY try=17 r1=… r2=… v04=…`.
- V45→R3: **poll expired 1 s before the target** — try=40 at 18:56:22 `r3_report=none` →
  `TIMEOUT after 40 tries`; R3's report landed 18:56:23. Same near-miss class: V30
  (`try=40 … r3report=0 18:56:18` → `TIMEOUT-ABSENT`), V28/V32/V33/V34/V43
  (`TIMEOUT*` 18:56:0x–18:57:35) — all single-sided verifier→producer waits whose 40-try windows
  (≈13.3 min) expired as R3's report landed at ≈15.4 min.
- **V29 → name-mismatch timeout:** `V29-scratch/poll.log` `try 40 18:55:42 missing: R4-fixture-json.md`
  → `TIMEOUT 18:56:02 missing: R4-fixture-json.md`; R4's actual report is `R4-fixture-author.md`
  (18:50:14). R5 hit the same mismatch and recovered via glob.

## 4. Escape conditions (bounded-wait inventory)

| seat | condition | escape | observed |
|---|---|---|---|
| R1 | R2 contract 25 cases | 40 tries × 20 s | POLL_HIT try=4 (18:46:19) |
| R1 | R5 map row + report | 40 tries × 20 s | hit try=12 (18:51:34) |
| R5 | R4 report | 40 tries × 20 s | READY try=11 (18:50:28) |
| V28/V30/V32/V33/V34/V43 | producer reports/artifacts | 40 tries × 20 s | TIMEOUT* ~18:56:0x (R3 race) |
| V29 | R4 report (exact name) | 40 tries × 20 s | TIMEOUT 18:56:02 (name mismatch) |
| V45 | R3 tool + R3 report | 40 tries × 20 s | TIMEOUT 18:56:22 (1 s before R3) |
| V58 | 63 other reports | watcher deadline 1800 s | moved 19:18 at 60 others (seat proceeded) |
| V40 | lane ≥ 64 (incl. self) | stall ≥45 at lane ≥62; cap 290 tries | moved 19:28:48 at lane 61 (seat proceeded) |
| V24 | ALL ≥ 64 + stable ×3 | cap 4500 s, `exit 0` | **cap fired 19:58:36** → report 20:01 |
| V35 | 63 other reports | deadline 10800 s, no stall escape | **condition met** after V24 → report 20:06 |

## 5. Class for process debt

- **MW-01 (all-reports n-cycle; recurrence).** The r96 `V43↔V58` class recurred larger: four seats
  whose poll conditions each require every other report (V24/V40 count all 64 incl. self —
  self-blocking; V35/V58 count the 63 others — mutually blocking). At the endgame they are the only
  absentees, so the set is an n-cycle: nobody can hit a condition until someone moves without it.
  In r97 the four seats' reports were mutually gated for ~45 min (19:13:49–19:58:36) until V24's
  cap fired; V58/V40 moved only by seat decision. **Recommended fix (process debt):** (i) subtract
  self in every all-reports condition (V58's r96 script did; V24/V40 do not); (ii) ensure at least
  one all-reports seat is not gated on the others (stagger or exempt the adjudicator/receipt pair);
  (iii) give every all-reports poll a stall escape — V35 has none (only a 3 h deadline).
- **MW-02 (producer cross-polling).** R1↔R2 and R4↔R5: producers poll each other's deliverables on
  the same 40-try protocol. Both resolved (R1↔R2 ~60 s; R4↔R5 ~3 min window, non-cyclic). The
  pattern is dispatcher-order-sensitive (R1's tool had to precede R2's contract; R5's map preceded
  R4's report). Recorded.
- **MW-03 (poll-window race + report-name mismatch).** The 40-try window (13.3 min) closed at
  ≈18:56:0x–18:57:35 while R3's report landed at ≈15.4 min → eight single-sided timeouts (escapes
  fired as designed, but by seconds). Separately V29 pinned the declared name
  `R4-fixture-json.md` while R4 wrote `R4-fixture-author.md` → guaranteed timeout; R5 recovered via
  glob. Recommended: declare-name binding in the dispatch, or glob-tolerant conditions; size poll
  windows to the producer tail.
- **MW-04 (endgame quad — full observed resolution).** Quad {V24,V35,V40,V58} formed 19:13:49,
  trapped ~45 min, resolved by V58 (19:18), V40 (19:28:48), V24's cap (19:58:36 → report 20:01),
  V35's condition met (report 20:06); 64/64 at 20:06. Named pair-set + escape ladder + observed
  timings recorded here for the process ledger. V40/V58 both filed ABSENT declarations for V24/V35
  with real counts (no fabrication).

## 6. Bottom line

PASS — a mutual poll-wait was found, named, and its resolution observed end-to-end: quad
{V24, V35, V40, V58} formed at 19:13:49 (60/64, each waiting on the other three), trapped ~45 min,
then unwound by V58 (19:18), V40 (19:28:48), **V24's cap at 19:58:36** (the last pair's escape,
exactly as predicted), V24's report 20:01, and V35's report 20:06 → **64/64 resolved**. Class
(all-reports n-cycle, r96 recurrence) recorded for the process debt; no seat was lost and no
artifact was fabricated anywhere in the window.
