# V33 — receipt (round 95)

**Seat role:** round-95 single-wave receipt seat. Scope per seat spec: after all seats land, count
seat reports under `.ufo/waves/round-95/seats/` (expect 64, one per declared seat, no duplicate
prefixes, headers matching), write the receipt skeleton `.ufo/waves/round-95/receipt.json` with real
sha256 per report, flag any missing seat. Presence/collection only — this seat judges no claim
(C1/C2/C3) and no axis.

**Environment pin:** lane HEAD `fb118c4` (r94 closure), unchanged through the whole watch
(`git status --short` at final snapshot: ` M LOG.md`, ` M corpus/tools/map_obligations.py`,
` M corpus/tools/map-obligations-contract.json`, ` M corpus/tools/README.md`,
`?? corpus/fixtures/r95-crossing-aftermath/`, `?? corpus/knowledge/r95-aftermath-scope-note.md`,
`?? .ufo/waves/round-95/` — no commit, no push by this seat). All commands run from repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Writes: this report +
`.ufo/waves/round-95/receipt.json` (both explicitly assigned to this seat) + `/tmp/V33-*` scratch.
No corpus edits, no nested agents, no network.

## Roster (declared)

`LOG.md` round-95 declaration: "One batched AgentSwarm, 64 seats: 5 producer seats (exclusive file
ownership) + 59 verifier/judge seats … Seat reports exclusive under `.ufo/waves/round-95/seats/`."
Roster used: `P1`–`P5` (producers) + `V01`–`V59` (verifiers) = 64 seats. Observed scratch dirs
(`V01-scratch` … `V59-scratch`) and the landed reports confirm the `P<N>`/`V<NN>` forms.

## Method (commands actually run)

- Two background poll loops, 20 s cadence, counting `*.md` files directly under
  `.ufo/waves/round-95/seats/`:
  `ls .ufo/waves/round-95/seats/ | grep -cE '^(P[0-9]+|V[0-9]{2})-.*\.md$'`
  (round 1: 150 tries 16:16:35→17:07:42; round 2: 40 tries 17:07:05→17:20:25), logs
  `/tmp/V33-poll.log`, `/tmp/V33-poll2.log`.
- Final snapshot: `ls .ufo/waves/round-95/seats/*.md | wc -l` → `61` (this report not yet written).
- Hash/count/header check: `/tmp/V33-final-receipt.py` (reads every report, extracts seat prefix and
  header line 1, checks `^# <seat>\b` on line 1, detects duplicate prefixes, computes sha256).
- Receipt written by that script to `.ufo/waves/round-95/receipt.json` after this report landed.

## Collection result at final snapshot

- **62/64 seat reports present at the end of this seat's work** (61 pre-existing + this report):
  P1–P5 all present; V01–V08, V10–V17, V19–V28, V30–V32, V34–V45, V47–V58 all present, plus V59.
- **Missing: `V09`, `V18` — flagged ABSENT.** Evidence through ~70 min after dispatch start
  (16:16): no report file, no seat scratch dir, no writes observed for either.
  - `V09`: no trace found anywhere (no `V09-scratch`, nothing in `/tmp` under `*v09*`).
  - `V18`: worked (churn/preservation probes) with `/tmp/v18_*.txt` traces whose last mtime is
    **16:35:06** — then silence for ~45 min; no report written.
  - Independent corroboration: `V59-presence-final.md` (17:19–17:22 snapshot) and its receipt also
    list `V09`, `V18` as missing; `V57-concurrency-audit.md` (audit window closed 17:02:43)
    observed no further report writes.
  - Environmental finding: `df -i /tmp` → `tmpfs 1048576 1048576 0 100% /tmp` (inode table
    exhausted, observed 17:23); `cp` to `/tmp` failed with `[Errno 28] No space left on device`
    despite 8.5 G free bytes. Plausible cause of stalled seat activity; **not repaired by this
    seat** (outside write scope) and not proven as the cause for V09/V18.
- Collection curve (from the two poll logs, `HH:MM:SS total`):
  `16:17:41=0, 16:18:01=0, 16:19:41=1, 16:26:01=16, 16:30:22=35, 16:34:42=53, 16:39:42=55,
  16:43:42=56, 16:48:22=59, 16:52:42=59, 16:57:02=59, 17:01:42=59, 17:05:42=60, 17:07:22=60
  (round 1 end, DONE 17:07:42); round 2: 17:19:45=60, 17:20:05=61, DONE 17:20:25`; V59's report
  landed ~17:20 (observed 17:22:20). Full curve embedded in the receipt JSON.

## Integrity checks

- **Duplicate prefixes: none.** 61 files, 61 distinct seat prefixes at snapshot
  (`duplicate_report_prefixes: {}` in the receipt; no seat wrote two report files).
- **Header/seat match: all pass.** For every report, header line 1 matches `^# <seat>\b` with the
  filename's seat prefix (e.g. `# V38 — contract-review (round 95)`); `header_seat_mismatches: []`.
- **Unexpected prefixes: none** (all files match the declared roster forms).
- Auxiliary non-`.md` entries under `seats/` are scratch dirs (`V01-scratch` … `V59-scratch`) plus
  `scratch/`; `V31-debt.json` is the only non-scratch auxiliary file. These are not seat reports
  and were excluded from the count.

## Receipt JSON — double-assignment disclosed and prior content preserved

`receipt.json` was **assigned to two seats**: this seat's spec and, per its own report, V59
("presence-final" — "finalize `.ufo/waves/round-95/receipt.json`"). Sequence observed:

1. V59 wrote `receipt.json` at ~17:20–17:22 (`record_owner: V59`, snapshot 17:22:00, 61 seat rows,
   `reports_missing: [V09, V18, V33]`), sha256
   `1906d61e6650ae461e4982cf57b9d8ded0e42fdeaf0570921e8c52352c118275`.
2. This seat read that file into memory **before** overwriting the same path, then wrote its own
   skeleton per this seat's spec (`round: 95`, `phase: "single-wave-64-seat"`, `requested_model`,
   `requested_seats: 64`, `seats[]` with real sha256 per report, `collection_snapshot{}`).
   V59's receipt is preserved verbatim-in-field as `prior_receipt_by_V59` (its full
   `collection_snapshot`, state, owner and sha256), so no evidence is lost by the overwrite.

No seat ID, dispatch ID, or served-backend echo is invented anywhere: every `agent_id`/`outcome` is
`null` for the integrator (L1) to fill from the real AgentSwarm result.

## sha256 per report (snapshot before this report was written; 61 rows)

| seat | file | sha256 |
|---|---|---|
| P1 | P1-tool-code.md | `ae6c8e2afb998a6f34ab5952c77763532b9456b5dd174a495be24640e415991c` |
| P2 | P2-contract-docs.md | `96a4cf14fe8b48fb4e0dc01a6afd4e457b49877d8374e60ac1a54ebabb9eaeaf` |
| P3 | P3-fixture-json.md | `ca366270cfe543ea67cb6839417d1ddea2c43673813fe478ff30473ff802d4bc` |
| P4 | P4-fixture-docs.md | `2309168503a1380d11aec6809dfc8b4a4d84fae9f6844450ba6d0de777e3d2ae` |
| P5 | P5-knowledge-note.md | `c15f6e8f76ec5789cafb4c45bc5e2805b601f6bab9455c71c9d02b7927b39479` |
| V01 | V01-c1-before-after.md | `6997e25f13c4657525a33ec39bdf053a5e47b48666d0dbdb3e5809f686cb2a0d` |
| V02 | V02-c1-selftest.md | `de83e471c9621ee9fbf96c40675b32168f6fc965a7d4c675025053ea899f3a23` |
| V03 | V03-c1-regression.md | `c36831b5468ca1af59244b99d8e8e4b08e40f37e974489623330483d3e40d226` |
| V04 | V04-c1-negative-rerun.md | `fd9e78f6d8d71ae94bb3d3f421402ab963e8f0448782e1bd7df71d0da21534e3` |
| V05 | V05-c3-dialect-r88.md | `1875644d2a8dc647316b4bd1e51e2d5715d0256f6d9d60588c38079aef5f6696` |
| V06 | V06-c3-fail-closed.md | `6864976810686c02a498e7f7d2b84a58a1083d59bc216cea23221305f296f371` |
| V07 | V07-c3-receipts-unchanged.md | `40f95a931a3e13fcd37618fe5bc4e5d1f3339d5eb8bf78524d15944de09967b8` |
| V08 | V08-c2-checker.md | `9b42876a9dac58d7731c8e637d2ac58ff76f13e291168697b14bdd8a45621907` |
| V10 | V10-c2-support-map.md | `436157297ff05bd4022cc19a01038cc220bcf4110bf593da5a2dc4e776661d84` |
| V11 | V11-c2-anchors.md | `0bdc0019c3556d447946c4da883e4a55ebac8288d64fdf5c9e69861707cc7211` |
| V12 | V12-c2-whole-claim.md | `23c95c6e51927d624a9d54edaadda2143e3856808e0c0d52d9a42befe265bcad` |
| V13 | V13-c2-anti-overclaim.md | `d2c4110d62ce109c0dbcd6d3013c1794756f11c2e767c73a2423cd7486f863b7` |
| V14 | V14-c2-dependency-probe.md | `28bb507915e206cc8e4c9b24b6aa7ed386998ee32e8bf08eb2170a79b24aa662` |
| V15 | V15-preservation-census.md | `e60c4699c1c59965dba7245027608fbf4e1e83a8420c411b9eca2aef870552d6` |
| V16 | V16-preservation-mutations.md | `5a2338ef40467ea86fabb4b63c72e3442b41876b7658eb18d613b5b4ba3f073a` |
| V17 | V17-gates-boundary.md | `374e0abfa8f754f38a80e408cd152acd45655289a1534a9a7518755dc2ac9c9d` |
| V19 | V19-freshness.md | `40dc2fb8b9a6e4b9709805beae43d0a0a22e21b327dcec2652bc480a701e1099` |
| V20 | V20-doc-parity.md | `476e17c6667d4e9027ff1b720824c931e10fb0db233f3bf4157db184d36154ab` |
| V21 | V21-operability.md | `f25b1bff799d95ed31b7350d31d655685198f5b579ead5091f3883996567ae1a` |
| V22 | V22-adjacency.md | `f2ce2ea60762ba6bfb9ef97c0ca36a20d95114951da1e2681e4233e204f0f3b4` |
| V23 | V23-verdict-depth.md | `41f53a29b39804ce049c554fc11979aed5a1a97d51a352a0c22a4d838ffb5147` |
| V24 | V24-verdict-coverage.md | `b96d55b6f5af77d641e0f50fa2247fde8f8552206784a57a03780bda9ccbeb54` |
| V25 | V25-verdict-calibration.md | `d4d6cdc081f99529bbb97826a2555ed4183a564342730d2fb179a0e9d214572d` |
| V26 | V26-verdict-operability.md | `f1694bcb61f7cff14b22cf08170bdc58f92b0c700219baf967b32b7dc79550ff` |
| V27 | V27-verdict-freshness.md | `bd44470f488327fd7d81d948cde2b3c485f1566e3d33e488f947adbd455ffa1f` |
| V28 | V28-verdict-adjacency.md | `3603e2dab9d1b3d382633a177c8a11fe973594df8805c82acc7202fa90f35ab3` |
| V29 | V29-adjudicator.md | `9d5bff1c0868b07d553c6c53a2cd152494cacfa2c32b9a807b211e66d245b90b` |
| V30 | V30-shonen-format.md | `833ac442e54db48a068f8aad287cca50e7a10f9be280cae621f1e8f6b2b0c888` |
| V31 | V31-debt.md | `6a692a657323dfe91a580fb87ce9ec5c547bb23fa12377e4694ca5a3f55978d4` |
| V32 | V32-spec-conformance.md | `2654350d545c5f11b2c803178b463ddf6117aca70f0946f118ff3545cb38766b` |
| V34 | V34-census-replica-2.md | `f84c68359fc57a8a1ccb2dd08ee865d50f02ac59d85df17747dd5dceee3c824f` |
| V35 | V35-anchor-replica-2.md | `fd5c66ef493ad3adffc87f9337598584413ba814d20ffba7aa78b406467a5f9d` |
| V36 | V36-whole-claim-replica-2.md | `bb389def73d6309105454c75aefd04ad58d4535d8fe0186f3238dd0903ca980a` |
| V37 | V37-code-review-c1.md | `7815d7448da755b053de3143cb5307ea1ff2d197d113d8d6bed67e76f4b6b5d6` |
| V38 | V38-contract-review.md | `2b85354e9bcc28294605288b990119a992a140f520ed0ed008cda6bba7f5d22b` |
| V39 | V39-dialect-audit-2.md | `a5f74eb19f29ae132864a6a62dd235f9d33fbad0b9781ab3e5ea4b9928f90bd6` |
| V40 | V40-negative-dialect.md | `80ce62ed5056a617655df7ee6ffbf2d41f1c98e7cd2ec2590cff618b29971d04` |
| V41 | V41-r88-doc-consistency.md | `779f3d0ebf8cf6a76f3a3aa76ba899fda6cab262b3e1f438c6a1e27c0d1c6d90` |
| V42 | V42-fixture-readme.md | `eedb0215732314222015e7bf16b8f12e470207503b67e0bd16bd8819999cfad6` |
| V43 | V43-knowledge-note.md | `5eca9ac42b8fd80bc4a3cdd9d4d9e4a18a715c3864ac36b108f94681a101580c` |
| V44 | V44-exit-contract-c2.md | `30e7e53104ada68ee0176a75c5463fbf02c7499b81016f0332704d975915ba43` |
| V45 | V45-census-paths.md | `5f95b09e606f5ec3602112ddf6f064d7bfec0dcc5d7873535bd2909b403afab2` |
| V46 | V46-receipt-wording.md | `788003b21013555117a81f200e38d77a0c7504a25118503c80fe3f6d4394fd20` |
| V47 | V47-dormancy-check.md | `add318b5cac7920b2e1585114f19b58181157dd378e33934b1374f7861200a7f` |
| V48 | V48-pins-fresh.md | `c7cf4129ab3fc0ba465a9c0d32647e379807730f3270571adabc266efb1bce25` |
| V49 | V49-inherited-tools.md | `d1f8b344e76219af9e7b6385506145769e7c4ced0cc56603647b4fd297055e56` |
| V50 | V50-byte-prefix.md | `43ac629b1d8398b6d8ac97675291ea6eabe29978e5fe31b9d6d9f45a7c994163` |
| V51 | V51-relation-scope.md | `f4d8a01790c0f438a1d6e7e8c50949a5c94c617daa6a1cd8160e9b5ba25a3b12` |
| V52 | V52-support-regression.md | `7627ecbe5ca19d4e0f6a614d316d9b70931db200201b4aaeef9c05afca41490c` |
| V53 | V53-cross-seat-audit.md | `f97ed82de67e1923fac9e6db926caa1a14642483db2a8d18df2c88a24457fe0b` |
| V54 | V54-crosscheck-depth.md | `ea3ade63a2ae59c6812b6c34a834e40c5db377d5247b38e782f375ccfd720e14` |
| V55 | V55-crosscheck-calibration.md | `40ccf9588f66737d7521809907283b266441d0a4b2c16a34d17566c5f20c1a85` |
| V56 | V56-integration-checklist.md | `b8e52c49beaa95d77d29b9da28050314c3e21dbbdaf5380a420174e4f6864e5b` |
| V57 | V57-concurrency-audit.md | `08d8ccfa3ef94516a645f3629d83929c04de70ec5b3c2a0c1a1343cd4e9569c7` |
| V58 | V58-claim-text-audit.md | `1ec1913255341bf84155d0c178e8635b3c1d9e098db073b693d42488d1c69c41` |
| V59 | V59-presence-final.md | `1b550601b03192ee8a16a6db67d9dceaf20f9a39b152f0a9be60aa0a6c22a851` |

V33 (this report): its sha256 is recorded in `receipt.json` (`seats[]`, `report_path`
`.ufo/waves/round-95/seats/V33-receipt.md`) — a file cannot contain its own hash, so the table above
stops at the 61 reports present when the snapshot was taken.

## Bottom line

**PASS** — receipt skeleton written at `.ufo/waves/round-95/receipt.json` with real sha256 per
report and real collection data (62/64 seats present: P1–P5 + V01–V08/V10–V17/V19–V28/V30–V32/
V34–V45/V47–V59 + V33); **V09 and V18 flagged ABSENT** (no report/scratch/writes through ~70 min);
no duplicate prefixes, no header mismatches; receipt double-assignment with V59 disclosed and its
receipt preserved as `prior_receipt_by_V59`; `/tmp` inode exhaustion (100%) recorded as an
environment finding.
