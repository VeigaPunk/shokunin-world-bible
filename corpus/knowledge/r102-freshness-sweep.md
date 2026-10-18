# Round 102 — final stale-pin sweep (freshness, seat U2)

Date: 2026-10-18. Executed at the r102 closure on the delivered revision
(baseline r101 closure `542021a`; wave tree uncommitted during the round;
HEAD `8fa2e87` = r102 declaration). Scope: every `.md` under
`corpus/knowledge/` (22 notes) plus the three index surfaces
(`corpus/README.md`, `corpus/fixtures/README.md`,
`corpus/tools/README.md`). Method: every sha256-like token
(`[0-9a-f]{7,64}`) extracted and re-verified against delivered bytes or
git objects; every receipt claim (exit codes, row counts, census lines,
self-test counts) re-run or reproduced from delivered bytes where the
claim is about the delivered revision; a sample of the quoted commands
per note executed. History was not rewritten; corrections are dated
append-only addenda.

## Inventory

Token occurrences across the 25 swept files: **178**, distinct tokens
**98**. Classification and disposition:

| Class | Count | Verification | Result |
|---|---|---|---|
| Git commit pins | 21 distinct | `git cat-file -t` / `git log -1` per token | 20 exist (dates 2026-10-11…10-18 as claimed); **1 dangling — `b6ca1e90…`, Finding F1** |
| Live-file SHA-256 pins | 6 distinct | `sha256sum` on delivered bytes | 6/6 exact: checker `ff9fd2aa…`, `support_check.py` `55a5eb27…`, `map_obligations.py` `86b52949…`, boundary-doc contract pins `7f815a93…` (document) + `ff9fd2aa…` (checker), contract top-level revision `ebec6bb…` |
| Freeze digest chain (8 pins) | 8 distinct | re-ran `dependency_freeze.py` per fixture | 8/8 `RESULT PASS`, digests byte-identical: r88 `acf677a7…`, r94 `048b8ff3…`, r95 `97cffd7b…`, r96 `43911900…`, r97 `a28b9ea0…`, r98 `5ecf84e1…`, r99 `7fe7e3b0…`, r100 `77debadf…` |
| Per-pin contract revisions | 3 distinct | dumped `dependency-freeze-contract.json` | six inherited pins `337f0fa…`, r99 pin `b5fe472…`, r100 pin `ebec6bb…` — exactly as tools/README records |
| Historical blob digests | 11 distinct | `git show <rev>:<path> \| sha256sum` | all reproduced: checker `dcacffd6`@2ea9ef1, `e2bb9639`@1b09f3f+e97613c, `3ae4134d`@03c6746+2b48ca7; freeze tool `03d04365`@4265df5, `fb9bb9ff`@fe1ce46+6f86bf2; map tool `cc1df4dc`@abbc3e0, `d1c239cc`@dcb2d92, `2b0ba815`@f3e09f9, `86b52949`@9d25df9; contract `8c2561b0`@fe1ce46, `ea012b9c`@6f86bf2, `153ebc5b`@4265df5 |
| Arc-snapshot digests | 1 distinct | `sha256sum` + `find -size 139c` | all 7 `relations.json` (r94…r100) = `c279254bc7de0636…` @ 139 bytes, as r101 note claims |
| Record digest | 1 (`da934a7…`) | re-ran the note's heredoc replay | r93 R8 record replay `gate_result…PASS`, `R8 record fields: 5/5`, exit 0 |
| Repair pre/post hashes | 2 (`5093d72e`, `e851f068`) | blob hashes across history | `map@f3e09f9`=5093d72e, `map@9d25df9`=e851f068, unchanged through ceeef43 — r97 note claim exact |
| In-flight run receipts (uncommitted revisions) | 8 distinct (`9224a684`, `ca05159e`, `6634e176`, `8173bb97`, `70795150`, `c435239d`, `2142b991`, and the DIGEST-MISMATCH post-images) | `git log --all` grep = 0 (never committed) | **waived** — every citing note already carries a dated addendum flagging them in-flight with "re-measure before citing / do not cite as current" (r95 note addendum; r96 note addendum; r98 note Receipts section) |
| Historical probe-output digests (mutation post-images, scratch trees) | ~18 distinct (`892d17d3`, `0ef6734a`→`4b130960`, `d541ae64`, `29e384bf`→`dbcd5f11`, `b0725e21`, `b97a3b80`, `09858d77`, `1f73326f`, `fc4633b9`, `85b16b4f`, `f5d2c136`, `c811669e`, `17e9230e`, `eb24e084`, `76dc4f51`, `3c922d20`, `59a0f4fa`, `acf677a7`-as-r97-scratch) | presented as receipts of named scratch-tree runs; structural equivalents re-verified on delivered bytes (self-test `markdown_tamper`/`repointed_edge` cases green; r97/r98/r99/r100 FREEZE lines re-run verbatim) | **waived as historical**, pins they are compared against (`5ecf84e1…` etc.) verified live |
| W05 baseline pin `a13d1af3…` | 1 | file now hashes `3c1ee6bf…` — i.e. "no longer matches" is true | **waived** — fixtures/README carries dated pin notes (seventh consecutive round) recording exactly this |

## Per-note dispositions

| Note | Verified this pass | Disposition |
|---|---|---|
| `seed.md` | no pins, no receipts (mint proposal) | FRESH (no claims to go stale) |
| `2026-10-12-lore-consistency-checklist.md` | statuses all "unmeasured" (initial backlog, honest) | FRESH |
| `2026-10-12-lore-decision-table.md` | no hex pins; scope-limits prose only | FRESH |
| `2026-10-12-malformed-error-patterns.md` | 5+1 rows re-run, all exact; `corpus/live/runs/20261012T164316Z/` exists | **STALE PIN FOUND — F1 `b6ca1e90…` dangling; dated addendum appended this pass** |
| `r74-slate-wording-decision-table.md` | no pins, no receipts | FRESH |
| `r87-provenance-chain-decision-table.md` | snapshot `2b48ca7` exists; checker@2b48ca7 = `3ae4134d…` as pinned | FRESH |
| `r88-sourced-inspiration-decision-table.md` | commits `2ea9ef1`, `1b09f3f` exist; r88 checker `dcacffd6` reproduced | FRESH |
| `r89-cross-cluster-contradiction.md` | no pins, no receipts | FRESH |
| `r91-c9-watch.md` | checker pin reproduced; pair re-run (see C9 below) | FRESH; **due r102 re-check landed as dated addendum this pass (F2)** |
| `r93-r8-worked-example.md` | heredoc replay exit 0, 5/5 fields vs pinned `da934a7…` | FRESH |
| `r94-cross-myth-design-comparison.md` | no live pins; lineage commits exist | FRESH |
| `r95-aftermath-scope-note.md` | receipts re-run exact (15/15, 17/17, 13/13); in-flight pin `9224a684` self-flagged by its own r98 addendum | FRESH (waiver in place) |
| `r96-response-scope-note.md` | receipts re-run (16/16 family); in-flight pins `6634e176`/`8173bb97` self-flagged by dated addendum | FRESH (waiver in place) |
| `r97-acknowledgment-scope-note.md` | map repair hashes `5093d72e`→`e851f068` reproduced from blobs; current r97 map `49d4834e` unchanged since creation; `e851f068` still true of r96 map today | FRESH |
| `r98-clerk-scope-note.md` | freeze tool `03d04365`@4265df5 and contract `153ebc5b`@4265df5 reproduced; in-flight `c435239d`/`2142b991` timestamped as in-flight in the note itself | FRESH |
| `r99-gate-blind-spot-table.md` | baseline tool `03d04365`@4265df5; contract `8c2561b0`@fe1ce46; live pin digest `5ecf84e1` reproduced by re-run; checker pin current | FRESH (probe post-images historical by construction) |
| `r99-lapse-scope-note.md` | all three tool pins = delivered bytes; support/map receipts re-run exact (21/21, 23/23, 19/19; raw=21); census-at-r99 `173` correctly historical (174 today) | FRESH |
| `r100-crossing-arc-synthesis.md` | tool pins = delivered bytes; `:46` quote verbatim | FRESH |
| `r100-provenance-semantics-boundary.md` | freeze tool `fb9bb9ff`@fe1ce46/6f86bf2 (past-tense claim exact); contract `ea012b9c`@6f86bf2 | FRESH |
| `r101-r10-register-first-entry.md` | 7×139-byte snapshots `c279254b…` verified; register file correctly absent; excerpt quotes verbatim | FRESH |
| `holder-assessment-boundary.md` | document digest = contract pin `7f815a93…`; legacy revision `5eb9451` exists; 160 dirs @1b09f3f; provenance-carrying 29@1b09f3f / 33@ca7f9ef; checker byte-identical from 65838f8→HEAD; boundary_doc_check CERTIFIED exit 0; drift probe exit 1 `document_drift` | FRESH |
| `reference-ledger.md` | citation rows carry their own dated 2026-10-17 correction; delivered excerpts exist in the named fixtures | FRESH |
| `corpus/README.md` | freeze 19-case self-test ✓, map 25-case self-test ✓, eight-pin chain listing ✓, "r101 fixtures outside the pins" ✓ (UNPINNED-FIXTURE observed for `r101-repointed-edge`, as documented) | FRESH |
| `corpus/fixtures/README.md` | census chain 168→169→172→173→174 all dated; **census re-run today = 174 dirs / 40 clean / 134 negative / 421 violation lines / 0 stderr**; per-round OBLIGATIONS receipts re-run exact (r94 14, r95 15, r96 16, r97 17, r98 20, r99 21, r100 22; r88 10, r93 12); checker pin + exit receipts exact; W05 pin note self-covers | FRESH |
| `corpus/tools/README.md` | full read; self-test progression 14→17→18→19 (19/19 today); chain 4→6→7→8 (8/8 today, digests exact); FREEZE receipt lines r97–r100 verbatim; guarded pin revisions exact; S2-scratch receipts (J14 anchor missing / map PASS / CLEAN) and T1-scratch REDUCTION receipt reproduced verbatim; superseded-numbers sentences all carry dated supersessions | FRESH |

## Findings

**F1 — dangling commit pin (corrected).**
`2026-10-12-malformed-error-patterns.md:9` cites baseline commit
`b6ca1e902f2bf08b8acddaef665d9764f8636981`; the object does not exist in
this repository (`git cat-file -t` fails; 0 matches in `git log --all`)
nor in the parent project repo. The note predates the lane's repo layout
(`.shokunin/lore/…` repo-root paths; committed here at r5 `60f4956`).
Dated correction addendum appended to that note this pass (2026-10-18,
round 102, U2), including a fresh re-verification of all six table rows
on the delivered revision. The LOG.md r5 entry referencing the same
commit is outside this seat's write set and is left to the lane log
owner.

**F2 — the C9 watch's due r102 re-check landed.** The watch's tenth
entry (r101) scheduled "Next re-check: r102". Executed this pass:
checker pin reproduced byte-exact; `discriminate_check.py` →
`RESULT: DISCRIMINATION HELD` exit 0; `--checker e97613c` →
`REGRESSION-DETECTED` exit 2 (expected control). Dated addendum appended
to `r91-c9-watch.md` (re-check 11) noting the cadence ends with r102
(no further round scheduled) unless the lane resumes.

**Waivers (stale-by-age but already covered — no new addenda):**
in-flight tool/contract revision pins (`9224a684`, `ca05159e`,
`6634e176`, `8173bb97`, `70795150`, `c435239d`, `2142b991`) — each
already flagged in-file by dated addenda as never-committed run
receipts; W05 preservation pin `a13d1af3…` — covered by the fixtures
README's dated pin notes; historical probe-output digests — receipts of
named scratch-tree runs whose comparison pins verify live; superseded
chain-size and self-test-count wordings in tools/README — each carries
its dated supersession.

## Receipt re-run log (commands actually executed, lane root)

- `sha256sum corpus/fixtures/check_bible.py` → `ff9fd2aa…d1421` (pin exact)
- `python3 corpus/tools/discriminate_check.py` → HELD, exit 0; `--checker e97613c` → REGRESSION-DETECTED, exit 2
- `python3 corpus/tools/dependency_freeze.py corpus/fixtures/<f>` for the 8 pinned fixtures → 8/8 `RESULT PASS`, digests identical to pins; `r101-repointed-edge` → `UNPINNED-FIXTURE` exit 2 as documented
- `python3 corpus/tools/dependency_freeze.py --self-test` → `SELF-TEST 19/19` / `RESULT PASS` exit 0
- `python3 corpus/tools/map_obligations.py --self-test` → 25 `SELF-TEST PASS` lines / `RESULT PASS` exit 0
- `python3 corpus/tools/boundary_doc_check.py` → `CERTIFIED (bounded: …)` exit 0; `--self-test` → PASS exit 0; `--doc <drifted copy>` → exit 1 `FINDING document_drift`
- `python3 corpus/tools/support_check.py corpus/fixtures/{r94-paired-crossing,r95-crossing-aftermath,r99-window-lapse}` → receipts byte-match quoted text (14/16, 15/17+13/13, 21/23+19/19)
- `python3 corpus/tools/map_obligations.py corpus/fixtures/<10 fixtures>` → OBLIGATIONS raw=mapped exact per quoted receipt
- full census (checker over all 174 fixture dirs) → 174 dirs, 40 clean, 134 negative, 421 violation lines, 0 stderr, 0 other exits
- `git cat-file -t` / `git show <rev>:<path> | sha256sum` for every commit and historical blob pin (see Inventory)
- r5 table re-run (6 rows, all exact, quoted in the F1 addendum)
- r93 heredoc replay → exit 0, 5/5 fields

## Bottom line

25/25 swept surfaces dispositioned: 23 fresh as-is, 1 fresh via waiver
register already recorded in-file, 1 stale pin found and corrected by
dated addendum (`b6ca1e90…`, F1); the C9 r102 re-check landed (F2); no
live pin, receipt, census, or self-test claim failed against delivered
bytes. The C3 freshness claim verifies on the delivered revision.
