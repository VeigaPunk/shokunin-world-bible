# V57 notes (insurance) — round-98 mutual-wait monitor

Round start (t0): 2026-10-17T23:27:36Z (V20-scratch/round-start-utc.txt). 40-min bound: 00:07:36Z.
Baseline r97 closure: 9a3d648. Wave tree uncommitted during round.

## Method
- watch.py (detached, 20s sampler) → V57-scratch/watch.log; copies sha-pinned scripts → V57-scratch/scripts/.
- analyze.py (static wait-graph + liveness) → runs at checks.
- snap.sh (quick counts + key poll tails) → V57-scratch/checks.log.
- ps snapshots: ps-t1.txt (23:32Z), ps-t2.txt (23:37Z).

## Wait-graph findings (static, through 23:50Z)
- Cross-verifier edges (V→V), all one-directional, all resolved by target movement:
  V43→V19 (hit try=28 23:37:57), V49→V26 (hit try=24 23:37:26), V50→V27 (V27 logger),
  V51→V07 (V51 has no blocking poll; edge from its waitgraph.py analysis code).
- All-reports waiters (r96/r97 class): **V31 (adjudicator: 63 others, grep -v V31-adjudicator, 240-try cap → ~00:48:40Z)** and
  **V58 (presence-final: 63 nonself, grep -v V58-presence-final, 90-try cap → ~23:59:18Z)**.
  Both subtract SELF correctly. They mutually gate each other: {V31,V58} pair.
- Non-waiting absentees in endgame: V20 (poll timed out 23:41:27, working), V36 (monitor poll, cap ~00:19:02Z,
  stall-escape 60 tries unchanged), V51 (no poll).
- Loggers (cannot trap): V24 (POLL_END 23:41:46), V59 (POLL-TERMINAL 23:43:06), V27 (FIXTURE_PRESENT; exits at try 40).
- V20 poll: condition empty at try 40 23:41:07, but loop ended → POLL-TIMEOUT 23:41:27 (off-by-one; escape fired).

## Timeline (UTC)
- 23:27:29–36 wave starts; V14 poll started.
- 23:28:40 V31 poll start; 23:29:38 V58 poll start.
- 23:31:52 4/64 reports (S3 first producer report).
- 23:34:47 20/64; all 5 producer reports by ~23:36.
- 23:37:30 37/64.
- 23:40:30 53/64.
- 23:43:38 57/64.
- 23:46:41 58/64 — plateau; absent {V20,V31,V36,V51,V57(me),V58}.
- 23:52:39 58/64; V58 try=70 nonself=58; V31 try=64 reports=58.

## Prediction (to verify)
- ~23:59:18Z: V58 cap fires (POLL-TIMEOUT, exit 1) → V58 report lands ~23:59–00:01 (bounded escape of the pair).
- Then V31 gated on {V20,V36,V51,V57}; I write ~00:08Z; V31 then hits n=63 → writes → 64/64.
- No pair remains mutually blocked at t+40min (00:07:36Z): {V31,V58} resolved by V58 cap at t+31.7min.

## Observations (process hygiene, non-axis)
- V05 scratch at repo root `v05-self-test-scratch/` (outside .ufo/waves/round-98/seats/).
- V36 poll reads parent-repo path `/home/vgpnk/Projects/shokunin/.ufo/waves/round-98` (diagnostic only).
