# V58 — presence-final (round 97)

**Seat role:** final presence seat of the round-97 single wave (64 seats: R1–R6 producers +
V01–V58 verifiers). Scope per seat spec: poll until the other 63 seat reports exist (bounded
stall-escape: proceed past 30 min and record who was missing), 64-report audit, producer-artifact
existence, finalize `.ufo/waves/round-97/receipt.json` collection snapshot with `agent_id` left
for L1. Presence/collection only — this seat judges no claim (C1/C2/C3) and no axis.

**Environment pin:** lane HEAD `2393934237ea076366f3db6dceeff033edb52ab1` (r96 SCORECARD-close
commit; declared r97 baseline `f3e09f9` verified ancestor — `git merge-base --is-ancestor f3e09f9
HEAD` → exit 0), unchanged through the watch. `git status --porcelain` at final snapshot:

```
 M LOG.md
 M corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
 M corpus/tools/README.md
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
 M corpus/tools/map-obligations-contract.json
 M corpus/tools/map_obligations.py
?? .ufo/waves/round-97/
?? corpus/fixtures/r97-crossing-acknowledgment/
?? corpus/knowledge/r97-acknowledgment-scope-note.md
```

No commits, no pushes by this seat. All commands run from
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Writes by this seat: this report,
`.ufo/waves/round-97/receipt.json` (explicitly assigned; double-assignment with V40's receipt seat
disclosed below), and `V58-scratch/` under the lane seats dir. No corpus edits, no nested agents,
no network.

**Roster (declared):** `LOG.md` round-97 declaration: "One batched AgentSwarm, 64 seats on
`opencode-go/deepseek-v4.1-flash`: 6 producer seats (exclusive byte-ownership) + 58 verifier/judge
seats on the poll-wait protocol (20 s cadence, 40 tries; ABSENT, never verify a plan)." Roster
used: `R1`–`R6` + `V01`–`V58` = 64 seats. Observed scratch dirs and landed reports confirm the
`R<N>`/`V<NN>` forms.

## Method (commands actually run)

- Collection watcher `V58-scratch/watch.sh` (20 s cadence; exits at 63 other-seat reports or
  1800 s), log `V58-scratch/collection-curve.txt`, started `18:43:47`. Host note: the first
  instance was killed at `18:53:47` by the host's default 600 s background-task timeout (same
  host-condition class as r96's /tmp inode note; no data lost — the curve to 18:53:27 was
  retained), restarted `18:57:49` with a 2400 s budget.
- Condensed curve (first change per value; exact logged `HH:MM:SS=count`):

```
18:43:47=0   18:47:47=1   18:48:47=8   18:49:07=9   18:50:27=11  18:51:27=19  18:52:27=24
18:53:27=30  18:57:49=37 (restart)    18:58:49=44  18:59:49=51  19:00:29=54  19:02:29=57
19:04:09=59 (held through 19:12:49)   19:13:09=60  19:14:09=60
```

- Audit script `V58-scratch/audit.py` (summary pass at `19:13:55`, then `--write` pass for the
  receipt): reads every report, extracts the seat prefix, checks `^# <seat>\b` on header line 1
  and within the first five lines, detects duplicate prefixes and unexpected `.md` entries,
  computes sha256 per report, checks the 17 declared producer-artifact paths
  (existence/bytes/sha256), snapshots `git status --porcelain`, preserves any pre-existing
  `receipt.json`.
- Per-report hash snapshot `V58-scratch/report-hashes.txt` (60 files, taken `19:14:44`).
- Parent-tree stray watch (r94-F01 cwd-defect class): `find
  /home/vgpnk/Projects/shokunin/.ufo/waves/round-97 -name '*.md'` →
  `find: '/home/vgpnk/Projects/shokunin/.ufo/waves/round-97': No such file or directory` (the
  parent wave dir does not exist); no parent `corpus/` tree exists either → no misplaced reports.

## Collection result (final snapshot 2026-10-17 19:14:44 −03:00)

- **60 of the other 63 seat reports present at the escape; missing: V24, V35, V40** — all three
  were active at the snapshot (evidence in the liveness section); nothing fabricated. 61/64
  including this report.
- All 6 producer reports present: `R1-map-pinning.md` (159 lines), `R2-contract-docs.md` (178),
  `R3-freeze-hardening.md` (156), `R4-fixture-author.md` (184), `R5-fixture-docs.md` (148),
  `R6-knowledge-note.md` (120).
- **Duplicate prefixes: none. Header/seat mismatches: none** (`header_seat_mismatches_line1: []`,
  `header_seat_mismatches_first5: []`). **Unexpected prefixes / unexpected `.md`: none.**
- Audit summary output (excerpt):

```json
{"reports_present_excl_self": 60, "reports_present_incl_self": 60,
 "missing": ["V24","V35","V40","V58"], "unexpected_prefixes": [], "unexpected_md": [],
 "dupes": {}, "mismatches1": [], "mismatches5": [],
 "artifacts_missing": {"R1": [], "R2": [], "R3": [], "R4": [], "R5": [], "R6": []},
 "head": "2393934237ea076366f3db6dceeff033edb52ab1", "baseline_ancestor": true,
 "prior_receipt": false, "receipt_written": false}
```

- Per-report sha256 snapshot (first 16 hex chars; full hashes in the receipt `seats[]`; as of the
  receipt write 19:16:30 — identical to the 19:14:44 snapshot except V56, noted below):

```
R1-map-pinning.md bc27c6a9dd413823          V19-c3-r96-repair-scope.md 87dedc19cc3aa083
R2-contract-docs.md 53ee1ef0236fd7e1       V20-c3-dependency-probe.md acb476486e30db10
R3-freeze-hardening.md 6383997d822f3be5    V21-preservation-census.md 1d2017f193d9b35f
R4-fixture-author.md bbea1e9b66d7bcfd      V22-preservation-mutations.md baf0e3ea8466684f
R5-fixture-docs.md cba2699827defe9e        V23-gates-boundary.md e5540a2b0f9965c8
R6-knowledge-note.md cbebae0038d87c2a      V25-freshness.md 400be8f52db45ea0
V01-c1-dual-pin.md 53d1dd5a8429e334        V26-doc-parity.md fc2902a86143ecc9
V02-c1-loader-tight.md ef7df10645558874    V27-operability.md 4d99a69137cbd773
V03-c1-regression-battery.md 3c51d13d52579230  V28-adjacency.md 7a1e5c82375467ed
V04-c1-negative-rerun.md c35e3254aeda63fd  V29-verdict-depth.md 77e9de0dbd1c7cfd
V05-c1-code-review.md 7c26bc1b7a0385a8    V30-verdict-coverage.md dcd08016ec427c13
V06-c2-guard-demo.md db62d153452d55c7      V31-verdict-calibration.md 6a0fd8fa40120aa9
V07-c2-path-binding.md 61d963349f4882d0    V32-verdict-operability.md 690d36c412973e02
V08-c2-digest-naming.md ac70ae2ff172ffbc  V33-verdict-freshness.md 9f999ecf5b061d86
V09-c2-selftest.md 051643f6790d782a        V34-verdict-adjacency.md 828d8c0147b360c3
V10-c2-chain.md 994e3dc778e15aa3           V36-shonen-format.md 6be73eca2f3af20f
V11-c2-code-review.md f310b9aad956fede     V37-debt.md 4e25246563b6f47e
V12-c2-refreeze-integrity.md 08e82e4f6dd5e93a  V38-spec-conformance.md a5f4c28da6acbd96
V13-c3-checker.md 26347030d67ef832         V39-integration-checklist.md 450ec4073fd881b5
V14-c3-inherited-equality.md 7d4274aec738abb5  V41-census-replica-2.md a6acbc47786525fd
V15-c3-support-map.md 9528323ff60b7bcf     V42-anchor-replica-2.md 88b5db37666728dc
V16-c3-anchors.md 9078d38fba74ddcb         V43-whole-claim-replica-2.md f8c7e217bd75b5f1
V17-c3-whole-claim.md 19cdf26f788b04f5     V44-c1-negative-2.md 2712fd7d687aa2b1
V18-c3-anti-overclaim.md aa9643074e3259b1  V45-c2-guard-2.md 4f46b83c6fd31736
V46-cross-gates.md 6bec592065310256        V52-support-regression.md 57d3e83c9f443e4c
V47-receipt-wording.md 1419e0950fd1c259    V53-cross-seat-audit.md 1b72e3da8c428d06
V48-pins-c9.md dd8d656c69fe8404            V54-crosscheck-depth.md dba6ad3ed6b3ba6f
V49-inherited-tools.md 58257e63c57ad95a    V55-crosscheck-coverage.md 78307a849843bd5c
V50-byte-prefix-2.md 2e1094877207ceed     V56-mutual-wait-guard.md 417473b4e8c73a3e
V51-relation-scope-2.md 83a8fcd2f510eaa6   V57-claim-text-audit.md ad3f8d19c952934e
```

(60 rows above; V24, V35, V40 absent at snapshot; V58 is this report. Post-snapshot edit
noted: `V56-mutual-wait-guard.md` was updated at 19:15:54 — hash `0bd5ec4f…` → `417473b4…`,
self-described "updated while the wave runs"; its row above carries the post-edit hash and the
receipt pins the same bytes. Verified: no other report changed between the 19:14:44 table
snapshot and the 19:16:30 receipt write.)

## Liveness finding — V24/V40/V58 wait class at the escape (reported exactly)

- **V40 is the round's receipt seat** (`V40-scratch/V40-receipt-builder.py`, "receipt seat —
  presence audit + receipt skeleton builder"). Its `V40-poll.sh` waits for `lane >= 64` with a
  stall escape at `lane >= 62` unchanged for 45 tries. Log tail at snapshot:
  `19:14:12 try=92 lane=60 parent_tree_md=0` — it never reached its escape threshold (needs ≥62)
  and had not written `receipt.json` (`ls .ufo/waves/round-97/receipt.json` → No such file).
- **V24's `V24-scratch/poll.sh` waits for `ALL >= 64`** (R+V report count) with a 3×60 s
  stability check and a 75 min cap. `ALL` counts existing `R*.md`+`V*.md` files, so before V24
  writes its own report its maximum reachable value is 63 — the `>=64` condition cannot fire
  pre-self-write. Log tail: `19:14:10 t=1840s R=6 V=54 all=60 producers=[R1..R6] psig=e4d3ebbb98e6`.
- This seat's own condition was "63 others exist" — which required V24, V35, V40 themselves. With
  V35 mid-draft (`V35-scratch/report-draft2.md`, mtime 19:08:08) and V24/V40 unwritten, the three
  conditions formed a wait class; V58's 30-min escape (19:13:47) fired first and this seat
  proceeded, landing its report and bumping `lane` 60→61 for the other pollers. Same defect family
  as r96's V43↔V58 mutual wait (LOG r96 closure: "V43/V58 were trapped in a mutual poll-wait").
  V40's escape still needs ≥62 (this report + V35); V24's condition appears self-blocking —
  recorded for the L1 and V56.
- Corroboration: `V56-mutual-wait-guard.md` — first landed 18:58, then updated 19:15:54. Its
  early-window finding was "Direct mutual pairs (A→B and B→A): none at every pass (18:44–18:52)";
  its updated §5 MW-04 names the same class this seat records: "**MUTUAL WAIT QUAD {V24, V35,
  V40, V58} formed an n-cycle mutual poll-wait at 19:13:49** … Bounded escapes: V58 deadline
  ≈19:27:48 (first mover; V58 was already running its audit at 19:14), V24 cap ≈19:58, V40
  stall escape (lane ≥62 + 15 min) / cap ≈20:20, V35 3 h deadline ≈21:43", and MW-01 records
  that V24/V40 self-include their own reports in the exit condition while V35 subtracts itself.
  Last pre-escape landing was V37 (`V37-debt.md`, mtime 19:14:06, 25,389 B).

## Producer-artifact existence (declared byte-ownership)

All 17 declared artifact paths exist; hashes were stable from ~18:58 through the snapshot (V24's
`psig=e4d3ebbb98e6` unchanged 19:08:49→19:14:10):

```
   bytes  sha256                                                            path
   38693  86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
    3189  2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
   24293  6278e59b8df01c1cb63ca6080cb959999f400d95128b96e84e5476f4c4ebb992  corpus/tools/README.md
   25044  b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130  corpus/tools/dependency_freeze.py
   12025  27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781  corpus/tools/dependency-freeze-contract.json
   10302  e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
    1449  026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  corpus/fixtures/r97-crossing-acknowledgment/entities.json
     139  c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r97-crossing-acknowledgment/relations.json
       3  37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  corpus/fixtures/r97-crossing-acknowledgment/contradictions.json
    1956  58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  corpus/fixtures/r97-crossing-acknowledgment/inspiration-note.md
     640  b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  corpus/fixtures/r97-crossing-acknowledgment/source-excerpt.md
    2235  438fb513a62496c41179ead3ea2a55a69ff4ce1fd191c3a7ebccb10651a8dc73  corpus/fixtures/r97-crossing-acknowledgment/sources.json
    2173  73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b  corpus/fixtures/r97-crossing-acknowledgment/timeline.json
    3410  8ba491cb249dd57f6aee8ca216133b07c06287c0240be658ea2e68da0cf5703c  corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md
    5304  d9387b7d73264dfc6c01d27cc6bf24c58ef6bdb4461d2ae8fbfdb6376d9e019f  corpus/fixtures/r97-crossing-acknowledgment/README.md
   12117  49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f  corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md
   15033  5e3b4225c30de8a2a75b675b59acb5c597b290e5a45f2caa01663da586e042b5  corpus/knowledge/r97-acknowledgment-scope-note.md
```

Presence-level byte observation (no content judgement): the five declared inherited byte-copies
in `r97-crossing-acknowledgment/` hash exactly to the r96 pinned hashes in the r96 receipt
(`entities` 026af0bc…, `relations` c279254b…, `contradictions` 37517e5f…, `inspiration-note`
58f5390e…, `source-excerpt` b5edc2fd…), and `r96-crossing-response/claim-excerpt-map.md` now
hashes e851f068… (≠ r96 pin 5093d72e…, consistent with the declared cosmetic repair; its content
is other seats' scope).

## Receipt finalization

- `.ufo/waves/round-97/receipt.json` written by
  `python3 .ufo/waves/round-97/seats/V58-scratch/audit.py --write` immediately after this report
  (first pass 19:16:30; a second pass re-pins this report's final bytes after the V56 row fix
  above): real collection snapshot (60 other reports present + this report; `reports_absent`
  `["V24","V35","V40"]` with empty `reports` objects on those seat rows), 64 `seats[]` rows with
  `agent_id: null` / `outcome: null`, full per-report sha256, `candidate_revision_pinned` = the
  17 artifact hashes above, `baseline_commit f3e09f9…`, `head_at_snapshot 2393934…`,
  `collection_curve`, lane porcelain, and an `agent_id_note` stating none were invented
  (dispatch_tool_call_id / returned_summary / served_backend_echo left null for L1). The snapshot
  object is carried under both `collection` and `collection_snapshot` (identical alias, for
  r94/r95 vs r96 receipt naming).
- No prior `receipt.json` existed at the first write (V40's receipt seat had not written); the
  second pass preserves the first pass under `prior_receipt_preserved`. If V40 writes later it
  will supersede or coexist — **double-assignment of receipt.json is disclosed** (same class as
  r96 V43/V58). A byte-copy of this seat's final receipt is preserved at
  `V58-scratch/receipt-final.json` so no snapshot is lost to a later overwrite.
- Verification (post-write): receipt JSON parses; the `V58` row hash equals the sha256 of this
  report as written; live-vs-receipt drift `[]` at re-check; re-run summary reports 61/64 present.

## Bottom line

PASS — presence audit and receipt finalization completed: 61/64 reports present at snapshot
(60 others + this report; V24, V35, V40 absent-at-escape and recorded with active-work evidence,
not fabricated), exclusive paths and seat-ID headers clean, no parent-tree strays, all 17
producer artifacts present, receipt finalized with real counts and null `agent_id` for L1 fill.
