# Seat U2 — freshness (round 102 capstone)

Seat: U2, lore-shokunin lane, round 102 (final round). Model:
zai-coding-plan/glm-5.3-flash-low. Baseline: r101 closure `542021a`
(HEAD at work time `8fa2e87`, the r102 declaration commit). Date:
2026-10-18.

## Verdict

**PASS** — the C3 freshness claim verifies on the delivered revision.

## Owned bytes delivered

1. `corpus/knowledge/r102-freshness-sweep.md` — the final stale-pin
   sweep record: all 22 knowledge notes + 3 index READMEs dispositioned,
   full token inventory (178 occurrences / 98 distinct), receipt re-run
   log, findings F1/F2, waiver register.
2. `corpus/knowledge/2026-10-12-malformed-error-patterns.md` — dated
   correction addendum (2026-10-18, r102, U2): the baseline-report
   commit pin `b6ca1e902f2bf08b8acddaef665d9764f8636981` is **dangling**
   — `git cat-file -t` fails in this repo (0 matches in `git log --all`)
   and in the parent project repo; the note predates the lane's repo
   layout (`.shokunin/lore/…` paths, committed here at r5 `60f4956`).
   The addendum supersedes only the unreachable `git diff b6ca1e9…`
   comparison instruction and re-verifies all six table rows fresh on
   the delivered revision (checker `ff9fd2aa…`): consistent exit 0 CLEAN;
   the five r5-* rows exit 1 with exactly the documented diagnostics.
   History unrewritten.
3. `corpus/knowledge/r91-c9-watch.md` — dated r102 re-check addendum
   (re-check 11, the watch's due r102 landing): checker pin
   `ff9fd2aa…d1421` reproduced byte-exact;
   `python3 corpus/tools/discriminate_check.py` → `RESULT: DISCRIMINATION
   HELD` exit 0; `--checker e97613c` → `REGRESSION-DETECTED` exit 2
   (expected control). Records that the cadence ends with r102 (no
   further round scheduled) unless the lane resumes.

No other files written; no commits; no pushes; no network.

## What was verified (evidence class)

- **Live pins 6/6 exact:** checker `ff9fd2aa…`, `support_check.py`
  `55a5eb27…`, `map_obligations.py` `86b52949…`, boundary-doc contract
  pins `7f815a93…` + `ff9fd2aa…`, freeze-contract revision `ebec6bb…`.
- **Freeze chain 8/8 re-run green** with byte-identical digests
  (`acf677a7…` r88 through `77debadf…` r100); FREEZE receipt lines
  r97–r100 verbatim (events 6/6→9/9); per-pin revisions six×`337f0fa…`
  + `b5fe472…` + `ebec6bb…` exact; `r101-repointed-edge` →
  `UNPINNED-FIXTURE` exit 2 exactly as corpus/README documents.
- **Self-tests:** freeze `SELF-TEST 19/19` RESULT PASS exit 0; map 25
  cases PASS; boundary_doc_check CERTIFIED exit 0 + self-test PASS +
  drift probe exit 1 `FINDING document_drift`.
- **Census re-run:** 174 dirs / 40 clean / 134 negative / 421 violation
  lines / 0 stderr / 0 other — matches the fixtures-README r100
  re-declaration and the LOG's "census 174 unchanged".
- **Tool receipts re-run verbatim:** support_check r94/r95/r99 full
  receipts; map_obligations 10 fixtures raw=mapped exact (10, 12, 14,
  15, 16, 17, 20, 21, 22); S2-scratch (J14 anchor missing / map PASS /
  CLEAN) and T1-scratch (REDUCTION-DETECTED) scratch-mirror receipts
  reproduced.
- **Git-object pins 20/21 exist; 13 historical blob digests reproduced**
  via `git show <rev>:<path> | sha256sum` (checker lineage
  `dcacffd6`/`e2bb9639`/`3ae4134d`; freeze-tool `03d04365`/`fb9bb9ff`;
  map-tool `cc1df4dc`/`d1c239cc`/`2b0ba815`/`86b52949`; contracts
  `8c2561b0`/`ea012b9c`/`153ebc5b`); r96 map repair pair
  `5093d72e`→`e851f068` reproduced.
- **Cross-references:** 7×139-byte arc snapshots `c279254b…`;
  provenance-carrying dirs 29@1b09f3f / 33@ca7f9ef; 160 dirs @1b09f3f;
  register file correctly absent; excerpt/quote checks verbatim; r93
  heredoc replay 5/5 vs pinned `da934a7…`.

## Waivers (already covered in-file; no new addenda)

In-flight never-committed revision pins (`9224a684`, `ca05159e`,
`6634e176`, `8173bb97`, `70795150`, `c435239d`, `2142b991`) — each
flagged by its own note's dated addendum; W05 pin `a13d1af3…` — covered
by fixtures-README dated pin notes; historical probe post-image digests
and superseded chain-size/self-test-count wordings — each carries its
dated supersession in tools/README.

## Caveats / residue

- U1's producer bytes (`r102-push-synthesis-r95-r102.md`,
  `r102-debt-ledger.json`) were **not yet present** in
  `corpus/knowledge/` at my write time (06:35 lane-local); my sweep does
  not depend on them, but C1/C2 verification is not mine to judge.
- The LOG.md r5 entry referencing the same dangling `b6ca1e90…` commit
  is outside my write set (lane log); flagged in the sweep record for
  the log owner.
- The 1986-era external citation freshness (URLs etc. in
  reference-ledger) is out of scope for a no-network seat; the ledger's
  own dated correction of 2026-10-17 stands.

Bottom line: **PASS** — 25/25 surfaces dispositioned, 1 stale pin found
and corrected by dated addendum, C9 r102 re-check landed, every live
pin/receipt/census/self-test claim reproduced against delivered bytes.
