# V58 — presence-final (round 96)

**Seat role:** final presence seat of the round-96 single wave (64 seats: Q1–Q6 producers +
V01–V58 verifiers). Scope per seat spec: poll until the other 63 seat reports exist, 64-report
audit, producer-artifact existence, finalize `receipt.json` collection snapshot with `agent_id`
left for L1. Presence/collection only — this seat judges no claim (C1/C2/C3) and no axis.

**Environment pin:** lane HEAD `60dba0c2aa344860b10a2fc63e00468d1b134f27` (r95 close; declared r96
baseline `dcb2d928f53f35673744feaf114e3ac65e3d25ca` is its parent, verified ancestor), unchanged
through the watch. `git status --porcelain` at final snapshot: ` M LOG.md`,
` M corpus/tools/README.md`, ` M corpus/tools/map-obligations-contract.json`,
` M corpus/tools/map_obligations.py`, `?? .ufo/waves/round-96/`,
`?? corpus/fixtures/r96-crossing-response/`, `?? corpus/knowledge/r96-response-scope-note.md`,
`?? corpus/tools/dependency-freeze-contract.json`, `?? corpus/tools/dependency_freeze.py` — no
commit, no push by this seat. All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin`
with `python3`. Writes by this seat: this report, `.ufo/waves/round-96/receipt.json` (explicitly
assigned to this seat; double-assignment with V43 disclosed below), and `V58-scratch/` under the
lane seats dir. No corpus edits, no nested agents, no network.

**Roster (declared):** `LOG.md` round-96 declaration: one batched AgentSwarm, 64 seats — 6 producer
seats + 58 verifier/judge seats. Roster used: `Q1`–`Q6` + `V01`–`V58` = 64 seats; observed scratch
dirs and landed reports confirm the `Q<N>`/`V<NN>` forms.

## Method (commands actually run)

- Background poll loop `V58-scratch/poll.sh` (20 s cadence, max 270 tries; counts
  `^(Q[1-6]|V[0-9]{2})-.*\.md$` under the seats dir, subtracting self when present), log
  `V58-scratch/poll.log`. Started `17:39:18`; hit at `18:19:18` (2400 s wall, 120 tries):
  `18:19:18 POLL_HIT total=63 others=63 i=120`. Curve (HH:MM:SS total):
  `17:39:18=0, 17:41:18=2, 17:46:18=14, 17:48:18=20, 17:50:18=33, 17:55:18=53, 17:58:18=60,
  18:00:18=61, 18:04:18=62 (held through 18:17), 18:19:18=63`.
- Audit script `V58-scratch/audit.py` (summary pass, then `--write` pass for the receipt): reads
  every report, extracts the seat prefix, checks `^# <seat>\b` on header line 1, detects duplicate
  prefixes and unexpected `.md` entries, computes sha256 per report, checks each declared producer
  artifact's existence/bytes/sha256, snapshots `git status --porcelain`, and preserves any
  pre-existing `receipt.json` verbatim-in-field (`prior_receipt_preserved`).
- Parent-tree stray watch (r94-F01 cwd-defect class):
  `find /home/vgpnk/Projects/shokunin/.ufo/waves/round-96 -name '*.md'` →
  `find: ‘/home/vgpnk/Projects/shokunin/.ufo/waves/round-96’: No such file or directory` (the
  parent wave dir does not exist) → no misplaced reports. Independent corroboration: V43's poll
  log shows `parent_tree_md=0` for every try.
- Hash cross-checks: `sha256sum` on the 16 declared producer artifacts; direct byte comparison of
  Q4's five byte-copy files against `corpus/fixtures/r95-crossing-aftermath/`; a read-only
  `python3 -c` shape check of the r96 JSON tables (presence-level only, no claim adjudication).

## Collection result (final snapshot)

- **64/64 seat reports present at final snapshot** (63 others at `POLL_HIT`, plus this report; the
  summary pass ran with `missing: ["V58"]` — this seat only, written after the audit).
- **Duplicate prefixes: none** (64 files, 64 distinct seat prefixes).
- **Header/seat match: all pass** (`header_seat_mismatches: []`).
- **Unexpected report prefixes: none.** Non-`.md` entries under `seats/` are scratch dirs plus
  `V40-debt.json` (auxiliary debt record, not a seat report; same class as r95 `V31-debt.json`) —
  excluded from counts.
- **Producer reports Q1–Q6 all present and substantive** (272 / 124 / 209 / 297 / 115 / 115 lines)
  before this seat's audit.
- Independent corroboration: `V43-receipt.md` (landed 18:19) audited the same directory at 18:18
  with `duplicate prefixes: none`, `header_seat_mismatches: []`, `parent-tree strays: none`.

## Mutual-wait liveness finding (V43 ↔ V58) — reported exactly

- Both seats' specs assign `receipt.json`, and both poll before writing.
  `V43-scratch/V43-poll.sh` exits when `lane >= 64` (with a stall escape: 45 unchanged tries at
  `>=62`); `V58-scratch/poll.sh` exits when `others >= 63` (self subtracted). With 62 files present
  and both receipt seats unwritten, each seat's condition required the other's report — a mutual
  wait. `V43-poll.log` shows `lane=62` held from `18:04` through `18:17`.
- **Resolution:** V43 hit its stall escape and landed `V43-receipt.md` at 18:19 (`lane=63`), which
  unblocked this seat's poll (`POLL_HIT 18:19:18`). V43 then kept polling toward `lane=64`
  (completed when this report landed). No seat was lost; both reports exist. This is a liveness
  defect of the two-seat receipt assignment, not a seat failure — recorded for L1.
- V43's report additionally states it "finalizes `receipt.json` after V58 lands", so the receipt
  file may be written twice (V43 last). Double-assignment is disclosed; if V43's receipt was
  present when this seat wrote, its collection data is preserved as `prior_receipt_preserved`.

## Producer-artifact existence (declared byte-ownership)

All 16 declared artifact paths exist:

| producer | path | bytes | sha256 |
|---|---|---:|---|
| Q1 | `corpus/tools/map_obligations.py` | 37739 | `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` |
| Q2 | `corpus/tools/map-obligations-contract.json` | 3115 | `97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6` |
| Q2 | `corpus/tools/README.md` | 18342 | `965b29cd41a8af14293eb2e1948f58f310e58c6e752b8fe322c5445b20a91f24` |
| Q3 | `corpus/tools/dependency_freeze.py` | 20552 | `a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980` |
| Q3 | `corpus/tools/dependency-freeze-contract.json` | 12032 | `7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975` |
| Q4 | `corpus/fixtures/r96-crossing-response/entities.json` | 1449 | `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` |
| Q4 | `corpus/fixtures/r96-crossing-response/relations.json` | 139 | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` |
| Q4 | `corpus/fixtures/r96-crossing-response/contradictions.json` | 3 | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` |
| Q4 | `corpus/fixtures/r96-crossing-response/inspiration-note.md` | 1956 | `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` |
| Q4 | `corpus/fixtures/r96-crossing-response/source-excerpt.md` | 640 | `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` |
| Q4 | `corpus/fixtures/r96-crossing-response/sources.json` | 1741 | `9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d` |
| Q4 | `corpus/fixtures/r96-crossing-response/timeline.json` | 1677 | `ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9` |
| Q4 | `corpus/fixtures/r96-crossing-response/fictional-excerpts.md` | 2588 | `06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3` |
| Q5 | `corpus/fixtures/r96-crossing-response/README.md` | 4858 | `ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456` |
| Q5 | `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` | 10172 | `5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8` |
| Q6 | `corpus/knowledge/r96-response-scope-note.md` | 12768 | `6db32ca24f5eff5baa3ebe589e8d3bcb6b256fec18dee2468211d7d0fae157c6` |

Cross-checks against producer reports (all match): Q1 delivered tool `2b0ba815…`; Q2 contract
`97b76bb8…` + README `965b29cd…`; Q3 `a3b57978…` + `7d568cc4…`; Q5 `ff52ced4…` + `5093d72e…`;
Q4's declared hashes for the five inherited byte-copy files and its authored
`sources.json` / `timeline.json` / `fictional-excerpts.md`.

- **Q4 byte-copy claim independently re-verified by this seat:** entities / relations /
  contradictions / inspiration-note / source-excerpt are sha256-identical to
  `corpus/fixtures/r95-crossing-aftermath/` (e.g. entities `026af0bc…`, relations `c279254b…`,
  contradictions `37517e5f…`).
- **Presence-level shape check (not claim adjudication):** the r96 fixture parses as entities 5,
  relations 1, contradictions 0, sources 5 (4 inherited + new `evin-response-note`), timeline 5
  (new tick-12 `response-evin-salt-court`, actor `evin`, place `salt-court`,
  `depends_on: ["aftermath-missing-evin"]`) — matching the declared C2 after-state shape. Whether
  C2 itself verifies is for the verifier seats; this seat adjudicates nothing.
- `map-obligations-contract.json` `self_test.cases` currently holds 24 entries (Q2's declared
  22→24 pinning, presence-level count only).

## Receipt JSON

- Written by this seat to `.ufo/waves/round-96/receipt.json`: `record_owner: V58-presence-final`,
  `baseline_commit` `dcb2d92…`, `lane_head_at_snapshot` `60dba0c…`, 64 seat rows with real
  per-report sha256, `agent_id` / `outcome` **null** everywhere (L1 fills from the real dispatch
  result), `candidate_revision_pinned` (16 producer artifacts), `collection`, `producer_artifacts`,
  `collection_curve`, `lane_status_porcelain_at_snapshot`.
- No dispatch ID, agent ID, or served-backend echo is invented anywhere.
- **Final on-disk state (observed):** V43 (the other receipt seat) overwrote this path at 18:27
  with its own receipt (sha256 `fe0f9633645d5290c896e0da922905186cbfb1ca0ddc5d624f55a72dcfcf7d0e`,
  64 rows, all `agent_id`/`outcome` null, no missing, no duplicate prefixes, no header mismatches,
  `head_at_snapshot` `60dba0c…`), preserving this seat's receipt verbatim-in-field as
  `prior_receipt_by_V58` (sha256 `c2998971b2fa0204edc83de3bacae509ac8fd3efca17ab3986e822af0e2e7b7e`).
  The final receipt on disk is V43's write; both seats' collection data is preserved. After this
  receipt-finality sentence was added to this report, this seat re-pinned its own `V58` row hash in
  the final receipt to this report's final bytes and appended the corresponding
  `post_snapshot_edits_observed` entry (both hashes recorded there); no other receipt bytes were
  touched.

## sha256 per report (snapshot before this report existed; 63 rows)

| seat | file | sha256 |
|---|---|---|
| Q1 | Q1-tool-hardening.md | `70fe50e4148012f5a1890055bbed13a8c0b60194bc884b0ab3a28191f8f77867` |
| Q2 | Q2-contract-docs.md | `065592215865ff7a539d6d84bdfbcca475c56d6e15121f8045faaeb6de4cb578` |
| Q3 | Q3-dependency-freeze.md | `5e97f7e94fb83e08f661b6ca8c123adbbda512bbaeecac63404a8fb4ed3d035a` |
| Q4 | Q4-fixture-json.md | `c516810862fb35a6d95a7c4050cb35c0c10fd377a0d810523c933707ab6a6ac7` |
| Q5 | Q5-fixture-docs.md | `c1f5d4ccba3c5d28c0d9f5963ad31750d2c2437cf3fd7880bf197394d739541f` |
| Q6 | Q6-knowledge-note.md | `cd48b4bd7bc0a9fb8d3cc208c057a3bc5d7b9f29d9b4aa84e381ade7218dbd39` |
| V01 | V01-c1-deletion-demo.md | `0cfc1a7d8a80e7e197c2f84144eca11d6fd730fd00dd3e0898673fa1b0592bd8` |
| V02 | V02-c1-selftest.md | `7135e9f2a1df43fa38bc47d8f16aaa19ec5cc1f42982a11ab711d01342541f7e` |
| V03 | V03-c1-schema-drift-pinned.md | `e7e214d363b16d8b2c6a8a76f56cde122b29e7b7a7ec7ea7f4d8d41cac104de4` |
| V04 | V04-c1-dual-pointer.md | `b33f3fbdce9ab8d332591b54ccd1087c1beb7644a5262d8064eb8390b661f4db` |
| V05 | V05-c1-regression-battery.md | `ffc88d8c8d76654d931dddafea6438c826403f27bda37c39de38744386750fd4` |
| V06 | V06-c1-negative-rerun.md | `2aa1cc20bc685719b6e9bf4d60551ce603a737cb5cf0f8a2b64eea99305ad579` |
| V07 | V07-c1-code-review.md | `cfd606fce79d1a57b3c45ec79c9fed1be3dbceea99b60758685a5a6d8e56a612` |
| V08 | V08-c2-checker.md | `6011a624498f794a417b4c0f8829299cb34ec7e6f587fb57eff681f1a8c3bd38` |
| V09 | V09-c2-inherited-equality.md | `cf401d20eb0a9c130d866bc96fa7efd51dee47deeadd1ae95f1b6805c8fc2dc4` |
| V10 | V10-c2-support-map.md | `49f76e93be910f562b4dc5c9d0413f0f9f0cfa8261a7ce56db0f70905609c409` |
| V11 | V11-c2-anchors.md | `a8031c81e2ea276d20996ea5ebec164a76050988a983fdcae350f638906da135` |
| V12 | V12-c2-whole-claim.md | `b7ef2760313982285abcff7dc9bf6bd5b676c35041cc5c21d919e0e66ae7d524` |
| V13 | V13-c2-anti-overclaim.md | `9df0a84adab317846b943921617c50e2bc84f5b78bf172c71787324dcded8ce3` |
| V14 | V14-c2-dependency-probe.md | `f3949750ea7c22c6afe1d20b51ee4db5122061af3f77fbc3c9315e6a1ae93701` |
| V15 | V15-c2-ordering.md | `aeb3c75d963d2639ec242aefd186ed870fc316a8a087fbf00ee72af90ffb53db` |
| V16 | V16-c3-gate-clean.md | `d7b65e20e8e78acec8e00656faa5317fc53a5dfe02f78b2c57bda26bd63b0c28` |
| V17 | V17-c3-br01-demo.md | `0320b70a987826d07055c3518564f4c1dd1be64e24db42d24c0eda142789b00e` |
| V18 | V18-c3-addition-endpoint.md | `66e2cacdb8dbbaa9b590c508b9cf3677d3c5fafec8e95f192f7adc705d759be9` |
| V19 | V19-c3-selftest.md | `3055ee9f55faec6b8ed985424b01cde9f3d8e6476ba21f5a5121dd84afe5f6a7` |
| V20 | V20-c3-code-review.md | `4deeb73184c13875bac8efaaaa8f12824f5d21aa79aff24d4c9ec597a32325b7` |
| V21 | V21-c3-fail-closed.md | `1668f1f4be2eec1abdf7e57dfcaca253498f55945c1b96015011c4fa670bedaf` |
| V22 | V22-c3-tamper.md | `7c60475f960097594b34108e19a4f6360b6ef1f97bbe4f1692f039e52a1a04ba` |
| V23 | V23-c3-chain-scope.md | `782dafad80140171b259f883293cd84dc5c54cfb7fda7be881ac8feff10057f3` |
| V24 | V24-preservation-census.md | `e50f6912bc359c334cf79fad1434e9681dadd0eaf39f57219374e7e38404b00e` |
| V25 | V25-preservation-mutations.md | `119bd744d0cbc544e277de219ad7f20859ba640bd88156e8e9139343d0ceab02` |
| V26 | V26-gates-boundary.md | `a406f59d9e91af27adbb18d91a406327d0c08ba1613a08358e485a7ec0669b07` |
| V27 | V27-scope-creep.md | `dc90c319360dce7beffb5b2986975432d620a0e3167c640817030ced795addc9` |
| V28 | V28-freshness.md | `8c9af06f26c809bcea529560e15bd5405f016e678b58e96399dca60c9f8cf613` |
| V29 | V29-doc-parity.md | `001f8e48d3eb0ce31d54cf2020b690385fadb43dba5646e3db5050636bf5371d` |
| V30 | V30-operability.md | `d5a3755ce8e1753b0e48bb59e27c6f539b05036b25ce5307db2fc4184ef432ea` |
| V31 | V31-adjacency.md | `8bd62e876bf2fd29ecf2c48080d34f13e2b833f9ec82e62483d37267706bf969` |
| V32 | V32-verdict-depth.md | `3bdec05e0c8fe16bd2fa23caff84a7b677d47150c448f0a8a28a8d4be2e919b3` |
| V33 | V33-verdict-coverage.md | `33e8a3595b3da3b510c1a6aa773262e85a8a37337d1e58c0c6b16db8387cd970` |
| V34 | V34-verdict-calibration.md | `0eef3776a71f911cd55371ddcfa551c09d69d24333da3bb2f2d395fc3aef5a5a` |
| V35 | V35-verdict-operability.md | `ea79daa367f5cc31fb09485b838834bbb633b3e995a4d4dde1549c0d8a2db54d` |
| V36 | V36-verdict-freshness.md | `629c756bcbf82c87f280422c47e08626725ff0fec9ee2e56fae960b9961d9dfa` |
| V37 | V37-verdict-adjacency.md | `6d44b037dd2ec11c5f18f4ede9ab12eb404123d87de338244c17473864cd76b9` |
| V38 | V38-adjudicator.md | `d3ad7d54a0c3a5ad24c6bb61f54782b6979e5b3586c8962c99224bed6b9a2313` |
| V39 | V39-shonen-format.md | `0192817caa05e234dd1ba60d8a8bcf6884ab9e5c4d446c68af9b12870fb5ca8b` |
| V40 | V40-debt.md | `e7304e8898afc461f24579c0629b0c18253e03fe8ed39c47ebb06108574a90fc` |
| V41 | V41-spec-conformance.md | `470b5d29109e8668711dc42f591aae7e01c7cc7d942eb4adee34ee424b836f69` |
| V42 | V42-integration-checklist.md | `5ccd87392c9a9fa4bc9690d359739b7f9f2ae253b1893869dfb7f52a8e3dd850` |
| V43 | V43-receipt.md | `8d8c324ff46b39a93da9715d87b4d7f1315a05b7ad60c58578d468ddceb6e5ce` |
| V44 | V44-census-replica-2.md | `235c197010df4009f72315dc5773f64b2bab4aa3492c5253d6e1369fca0ad042` |
| V45 | V45-anchor-replica-2.md | `352e081e57a1551d7d02dafe6a97c06df64b95c71cc483ed1cf92bf086c902d4` |
| V46 | V46-whole-claim-replica-2.md | `eaf2371082b87dbc5e6edf45de5208d13ea150dda034636ea81cb21b16620b98` |
| V47 | V47-c1-negative-rerun-2.md | `2cb9d6e321a575733642940d20022d579af8663ddd21d812eb7b8d4144332d3b` |
| V48 | V48-c3-negative-2.md | `769d3d8a394706131f44278a4ed42af19be19b023ad44b614e89599d5c44b87e` |
| V49 | V49-gates-cross.md | `740d041a7f6b79c293f992073b3db25877ab64c2900a8edb6af8ec847de54b25` |
| V50 | V50-receipt-wording.md | `b3c84b0536ed16279ccce8e8aa77801dad39cdab0ba0641e5aae9c4d9ae31943` |
| V51 | V51-pins-c9.md | `d7ee17844d4c780592f3e9871b5d5dc4054c6f270e3727a91503a412ab351b94` |
| V52 | V52-inherited-tools.md | `5c025ab73aa461b0ada600376f08f007110dc8aaf688b15c8de8bee1b3924795` |
| V53 | V53-byte-prefix-2.md | `69281ed75a82351c064d4161ccf56d39ce3550443667f63eb4a781826b3409ee` |
| V54 | V54-relation-scope-2.md | `0957fcf24325bcad555c1b731b9560e858715e434fde4fb3a811305552951296` |
| V55 | V55-cross-seat-audit.md | `19087a6d081b3dbe7cb3af5cc8ee6bfc72e56bcecbdfd9cc999995482565ced7` |
| V56 | V56-crosscheck-depth.md | `ae3c8d3f8beb4641213c01413b6aa09f57eced43a8fb804d0d74a5cab34dbd61` |
| V57 | V57-crosscheck-coverage.md | `186bea6fce7a9c16f1ff0d57ea11b4dfb4c4cc79347163c19cd849e92537449f` |

**Post-snapshot edit in this table:** V38's row shows the hash at this table's snapshot
(`18:23:02`); V38 edited `V38-adjudicator.md` afterwards (mtime `18:24:51`, final sha256
`2414c6c541af098b7127e55c763d5dec85d113536e2a3f07ffdb46cd7df7f2da`) — the final receipt's
`post_snapshot_edits_observed` records this independently. All other rows match the final files.

This report's own sha256 is recorded in `receipt.json` (`seats[]` row V58) — a file cannot contain
its own hash, so the table stops at the 63 reports present when it was generated.

## Bottom line

**PASS** — 64/64 seat reports present and audited; no duplicates, no header mismatches, no
unexpected prefixes, no parent-tree strays; all 16 declared producer artifacts exist with hashes
cross-matching the producer reports; mutual-wait liveness finding (V43 ↔ V58) recorded with its
resolution; receipt written with `agent_id` left null for L1.
