# V29 — verdict-freshness (round 98) — DRAFT

Facts established so far (all re-runnable):
- Addenda landed 20:29:14 (mtime), append-only: numstat 14/0 each; diff vs 9a3d648 shows additions only at EOF.
- r95 note sha 8e9e1774…, r96 note sha a9b51f8c… (measurement time).
- Addenda claims verified:
  - committed map revisions cc1df4dc(r94 abbc3e0) / d1c239cc(r95 dcb2d92) / 2b0ba815(r96 f3e09f9) / 86b52949(r97 9d25df9) — my hashes of blobs.
  - contract: 8173bb97@dcb2d92, 97b76bb8@f3e09f9, 2142b991@9d25df9 — verified.
  - in-flight shas 9224a684 / 6634e176 (and ca05159e) appear in NO commit tree (git rev-list --all --objects grep → empty).
  - current pins 86b52949/2142b991, check_bible ff9fd2aa, support 55a5eb27 — my own sha256sum matches.
  - receipts: r95 map raw=15 PASS, support 15/15 2/2 17/17 PASS, check_bible CLEAN; r96 map raw=16 PASS, support 16/16 2/2 18/18 PASS, check_bible CLEAN; r95 fixture raw=15 PASS at same revision.
- No live corpus doc cites stale shas as current (grep corpus/ outside the two notes → no hits; SCORECARD:451 & LOG:2830/3059 are historical closure/declaration records).
- Pending at draft: S1 (dependency_freeze files), S2 (tools README), S5 r98 note. Re-verify at freeze.
