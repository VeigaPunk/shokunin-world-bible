# V40 — receipt (round 97)

**Seat role:** round-97 receipt seat. Scope per seat spec: after all seats land, presence audit
under `.ufo/waves/round-97/seats/` (expect 64 reports — R1–R6 producers + V01–V58 verifiers, one
per declared seat, exclusive paths), write the receipt skeleton
`.ufo/waves/round-97/receipt.json` with real sha256 per report, collection snapshot, `agent_id`
null for the integrator (L1). Presence/collection only — this seat judges no claim (C1/C2/C3) and
no axis.

**Environment pin:** lane HEAD `2393934237ea076366f3db6dceeff033edb52ab1` (r96 SCORECARD-close
commit), whose parent `f3e09f9` is the declared r97 baseline (`git merge-base --is-ancestor
f3e09f9 HEAD` → exit 0, "baseline f3e09f9 is ancestor of HEAD"). `git status --short` at final
snapshot (19:27 -0300):

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
`.ufo/waves/round-97/receipt.json` (explicitly assigned; double-assignment with V58 disclosed
below), and `V40-scratch/` under the lane seats dir. No corpus edits, no nested agents, no
network.

**Roster (declared):** `LOG.md` round-97 declaration: "One batched AgentSwarm, 64 seats on
`opencode-go/deepseek-v4.1-flash`: 6 producer seats (exclusive byte-ownership) + 58 verifier/judge
seats on the poll-wait protocol (20 s cadence, 40 tries; ABSENT, never verify a plan)." Roster
used: `R1`–`R6` + `V01`–`V58` = 64 seats.

## Method (commands actually run)

- Presence poll loop `V40-scratch/V40-poll.sh` (background task `bash-ep3tazrq`, 20 s cadence,
  log `V40-scratch/V40-poll.log`), counting `ls .ufo/waves/round-97/seats/*.md | wc -l` and
  parent-tree `.md` files. Curve (HH:MM:SS lane): `18:43:51=0, 18:50:11=10, 18:56:51=37,
  19:03:31=58, 19:10:12=59, 19:16:52=61`, then 61 held through `19:27:52 try=133` and 62 (this
  report) held through `19:43:52 try=181`, where the loop exited on its stall-escape:
  `19:43:52 STALL lane=62 unchanged for 45 tries (>=62 present); exiting`. Full terminal line in
  `V40-scratch/V40-poll.log`; V24/V35 absent throughout the whole ~60-minute watch.
- Audit + hashing script `V40-scratch/V40-receipt-builder.py --summary`, full output saved at
  `V40-scratch/V40-summary-final.txt` (snapshot 2026-10-17T19:27:28-0300).
- Parent-tree stray watch (r94-F01 cwd-defect class): `find /home/vgpnk/Projects/shokunin/.ufo/waves/round-97 -name '*.md'`
  → **no output** at every check; `parent_tree_md=0` throughout `V40-poll.log`.
- Candidate-revision existence + sha256 for all 26 producer-owned paths (R1–R6 spec):
  all 26 exist (no `MISS`). Full list in `receipt.json` → `candidate_revision_pinned`.
- Post-V58-snapshot edit diff: compared every hash in `V58-receipt-prior.json` against the file
  now on disk — exactly one changed: `V58-presence-final.md` (`a3fe83a7…` → `759cd9d3…`), V58's
  own report finalized after V58 wrote its own receipt snapshot (19:16:30).

## Collection state at snapshot (19:27:28 -0300)

- **61/64 seat reports present**: R1–R6 (all six producers) and 55 verifiers V01–V23, V25–V34,
  V36–V39, V41–V58 (excluding V24, V35, V40).
- **Absent: `V24`, `V35`, `V40` (this seat).** V24 and V35 never landed; both are past the
  round's poll-wait protocol window (20 s × 40 tries ≈ 13 min) by a wide margin — the lane held
  at 61 for ~11 minutes (19:16:52 → 19:27:52) and at 62 (this report) for a further 15 minutes
  (19:29:12 → 19:43:52), i.e. absent across the entire ~60-minute watch. V58-presence-final,
  which finalized its own snapshot at 19:16:30 with the same two absent, also gave up on them.
  Reported ABSENT, per protocol; no artifact from either seat was found anywhere in the lane or
  parent tree.
- **All producer artifacts present**: the 26 pinned paths (5 tool files + 10 r96 fixture files +
  10 r97 fixture files + 1 knowledge note) all exist with recorded sha256.
- **Declared repair visible in pins**: `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`
  now hashes `e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de` (post-repair),
  where the r96 receipt pinned `5093d72e…` (pre-repair) — this is the R4 cosmetic repair
  declared in the round-97 C3 claim, not drift. The r96 data files (`entities/relations/
  contradictions/timeline/sources/inspiration-note/source-excerpt`) are byte-identical to the r96
  receipt pins (`026af0bc…`, `c279254b…`, `37517e5f…`, `ea0225f9…`, `9f973f63…`, `58f5390e…`,
  `b5edc2fd…`); r97 copies of entities/relations/contradictions/inspiration-note/source-excerpt
  are byte-identical to those (preserving copy), while r97 `timeline.json`, `sources.json` and
  `fictional-excerpts.md` differ (new event / 6th source / new excerpt — the C3 additions).

## Integrity checks (snapshot 19:27:28)

- **Duplicate prefixes: none** (61 files, 61 distinct seat prefixes).
- **Header/seat match: all pass** (`header_seat_mismatches: []`).
- **Unexpected `.md` in seats dir: none** (all other entries are scratch dirs, excluded).
- **Parent-tree strays: none detected** (`misplaced: []`, `parent_tree_duplicate_copies: []`).

## Double-assignment disclosure (receipt path)

V58-presence-final also wrote `.ufo/waves/round-97/receipt.json` per its own seat spec
(same class as r96 V43/V58 and r95 V33/V59). Its file was read and byte-copied to
`V40-scratch/V58-receipt-prior.json` (sha256 `238df7fe40ac0d6119dcb01fe41a8e2fcec10a7789f0f8ce7ce13dabe239e62e`)
before this seat wrote the path; it is preserved in-field as `prior_receipt_by_V58` inside this
seat's receipt. V58's snapshot (19:16:30, 60/64 present) is superseded by this seat's.

## sha256 per report (snapshot 19:27:28 -0300; excludes V24, V35 absent and V40 = this report)

| seat | file | sha256 |
|---|---|---|
| R1 | R1-map-pinning.md | `bc27c6a9dd413823313d3729bbbcd796530c1793caaccece33ccb79e707d9c13` |
| R2 | R2-contract-docs.md | `53ee1ef0236fd7e1883b9c7900fccd2d12461dc193d4582dbb2c47108beaeae1` |
| R3 | R3-freeze-hardening.md | `6383997d822f3be5f985cbb33a7af12ae7e1b0922e96bb6e6e81cc5d65b01764` |
| R4 | R4-fixture-author.md | `bbea1e9b66d7bcfd7cf720ee87a995d12fac7177dbdec9dd1fe4a10ab25bae79` |
| R5 | R5-fixture-docs.md | `cba2699827defe9ef2d09e8219105620e675fa9caef6134faabe151e09f0befa` |
| R6 | R6-knowledge-note.md | `cbebae0038d87c2acaa2dd915ee6a7bfaa6587f48d987dd02f7ca004e76cbb93` |
| V01 | V01-c1-dual-pin.md | `53d1dd5a8429e3349fc8ba198097b2f68933f0edc9dd17b7fc666f3629a23eef` |
| V02 | V02-c1-loader-tight.md | `ef7df10645558874ac55bf145c39b3ef8f6b348a8849a5c3caee06b6a855b202` |
| V03 | V03-c1-regression-battery.md | `3c51d13d5257923059b1a3246f29d313132542ffc8bbe9d2e13357f05e8069fd` |
| V04 | V04-c1-negative-rerun.md | `c35e3254aeda63fdf1d8568399d4f8678594c6652e659e2f53e94c852babbf85` |
| V05 | V05-c1-code-review.md | `7c26bc1b7a0385a88127cd051224d67c577a65edc9f8165b5982528b924db31f` |
| V06 | V06-c2-guard-demo.md | `db62d153452d55c75b9fefc341c1dce3d7bb1ceaec49cc0d0ccb001569d89856` |
| V07 | V07-c2-path-binding.md | `61d963349f4882d0fdc39500833eb5cc19ca02aecadfddca4ddf73252d8929eb` |
| V08 | V08-c2-digest-naming.md | `ac70ae2ff172ffbc73565ebc830c080d8e3d3c80054b05f29181f9f590cf7bc4` |
| V09 | V09-c2-selftest.md | `051643f6790d782a8c3d00d2f8088dac04930813314733a9267207eda5c9413e` |
| V10 | V10-c2-chain.md | `994e3dc778e15aa3384f8c1b101af19bc3d406e19e8ff885de6e2b3305597bb2` |
| V11 | V11-c2-code-review.md | `f310b9aad956fede394fe56194e60313580d70c63d05ca6a7df7adb1f897f4bf` |
| V12 | V12-c2-refreeze-integrity.md | `08e82e4f6dd5e93a95dbd107f46cf3a8e8b1924ab9b7010b270c8c3edc9803f9` |
| V13 | V13-c3-checker.md | `26347030d67ef8322ffa0e986d9f17831bfd84392eb61291e0bb6ded232b8206` |
| V14 | V14-c3-inherited-equality.md | `7d4274aec738abb578a41faeda189e6fa9ed0b2ca88a6c08e72b1df5158e3ba7` |
| V15 | V15-c3-support-map.md | `9528323ff60b7bcf55164236309c2a43357d22b17966acdb60bd4b5c65bd9210` |
| V16 | V16-c3-anchors.md | `9078d38fba74ddcbd96f02780c35a80b44067cd3ecd002e74ffdd925c5aa8dc6` |
| V17 | V17-c3-whole-claim.md | `19cdf26f788b04f50a2dae9ca04b5ecf33599a07c6404a482e23f1615ac74e1d` |
| V18 | V18-c3-anti-overclaim.md | `aa9643074e3259b12c0827cd3d5e98219a49bf3fa374a23b525629bde6fa2f07` |
| V19 | V19-c3-r96-repair-scope.md | `87dedc19cc3aa0836d47f539e6adf11d96c4c6b03ecf8e2ed727f4e20c7129e9` |
| V20 | V20-c3-dependency-probe.md | `acb476486e30db10d28c92de9bf85588ac9b12bf64cdfff77ace01e610cffdc4` |
| V21 | V21-preservation-census.md | `1d2017f193d9b35fbbb18fe5e7fe01f380141476d8e44619e2e19cfea8e29847` |
| V22 | V22-preservation-mutations.md | `baf0e3ea8466684ff142b9788c6669fc7147913f4669d3c2a8c656b2547fd987` |
| V23 | V23-gates-boundary.md | `e5540a2b0f9965c843924ad707f08fe053dbca86135896f3cd66f78b2adfd6a7` |
| V25 | V25-freshness.md | `400be8f52db45ea016a614815db20ab6ee0e92c9c12223b535806b7fb2e9b28f` |
| V26 | V26-doc-parity.md | `fc2902a86143ecc933c649ee0b5be6402fd0ae5b35408f40342ea4dddcd1d52a` |
| V27 | V27-operability.md | `4d99a69137cbd77375deca62f01d9806b2e664fb3d6091a3a948279e74bd6955` |
| V28 | V28-adjacency.md | `7a1e5c82375467edd759ef9e806c15c70ea82c7d65bfab9bf0db2d7c685bf432` |
| V29 | V29-verdict-depth.md | `77e9de0dbd1c7cfd65b4d206d5e34ea35780a18a3387c9da2562f0e72c47eee9` |
| V30 | V30-verdict-coverage.md | `dcd08016ec427c135f258def167f315adcaac0c4c23e1d64df46ff13d9bef0e3` |
| V31 | V31-verdict-calibration.md | `6a0fd8fa40120aa9c673cce00c4b6c52ad132ccdba68f36dde8e8f4e2430f4c4` |
| V32 | V32-verdict-operability.md | `690d36c412973e02717d04878db10baa77c87fec12bf34ad3b90e3218bfb3402` |
| V33 | V33-verdict-freshness.md | `9f999ecf5b061d86e2833815455e484c02752e566d7caa114671dfe454653619` |
| V34 | V34-verdict-adjacency.md | `828d8c0147b360c3a5a23745d88781cf6c28b1d7484e47dee69a370a61eb33b7` |
| V36 | V36-shonen-format.md | `6be73eca2f3af20fb512eedf9d60297d9a5d1db0a5f41bc5b28a997fe4291ae0` |
| V37 | V37-debt.md | `4e25246563b6f47ee6e7ad47801130636a19e8b3ac5fa9f0f6eb4e80717a6850` |
| V38 | V38-spec-conformance.md | `a5f4c28da6acbd96813127285f1ab76d61c5060390ac7d9878a1acf00ef7b24f` |
| V39 | V39-integration-checklist.md | `450ec4073fd881b5ae6f270fe2405a412fe39e6a077de2efce0c4eb0aad0a9d1` |
| V41 | V41-census-replica-2.md | `a6acbc47786525fd785c4e5e7b79dc6b5b97a8c0633210f93e2e26c691b9bcbe` |
| V42 | V42-anchor-replica-2.md | `88b5db37666728dc2a8f682f2af1dbc31f66dc2b0a7fd6e0d442d5183d67a77d` |
| V43 | V43-whole-claim-replica-2.md | `f8c7e217bd75b5f138f161d16d3943a8d95edf16688bd6ed857c54278a210f66` |
| V44 | V44-c1-negative-2.md | `2712fd7d687aa2b18a3cf4b54da08dedad1eeccbd3cf96046edfa112af394f7a` |
| V45 | V45-c2-guard-2.md | `4f46b83c6fd31736c21f12e255a95f688a61cbbca6778900a465bb8e297c8756` |
| V46 | V46-cross-gates.md | `6bec5920653102565cbdab95baea3ec7602e58d603c35eebbf0144ee534e1d5f` |
| V47 | V47-receipt-wording.md | `1419e0950fd1c2594800caaf8f303f25032386d74e07af3649bcf3384f1da7b5` |
| V48 | V48-pins-c9.md | `dd8d656c69fe84046e439a11633c0172e391dcc86ce06b482f74073b451dfd7e` |
| V49 | V49-inherited-tools.md | `58257e63c57ad95add1a314361889c79ad096f504a8ce6dc91bb069eaf47386e` |
| V50 | V50-byte-prefix-2.md | `2e1094877207ceedbd42f7c2a5a68eb0c32662a0f9e19672256e34214bede21e` |
| V51 | V51-relation-scope-2.md | `83a8fcd2f510eaa6032f3acc02c8aba6cbc86e67b6e055a1cecb916f62d21c63` |
| V52 | V52-support-regression.md | `57d3e83c9f443e4cb3bd02e37db42644c240b21a7793f2780c34e6443404ad76` |
| V53 | V53-cross-seat-audit.md | `1b72e3da8c428d0651dd8142b5807efc62a510223f87b7e5baaff7b31a3eee89` |
| V54 | V54-crosscheck-depth.md | `dba6ad3ed6b3ba6f684933876dda016d2ba795ecc1b0dc170fe064cdf4b5b42f` |
| V55 | V55-crosscheck-coverage.md | `78307a849843bd5c0f826200eac0b6665e7e844b924a15c02986b3ac20e8ec08` |
| V56 | V56-mutual-wait-guard.md | `417473b4e8c73a3e9f9986a37997a362acfb7d04638bf9ce278c84fdda802605` |
| V57 | V57-claim-text-audit.md | `ad3f8d19c952934e8e65b5c17f487fae87a1cf785f7b7e49e11f65f32be6a9e3` |
| V58 | V58-presence-final.md | `759cd9d308bbe31fce2193d8d7df3104b41f32c6e541cc11605032624a61d626` |

Post-snapshot edit observed: V58's own report was edited after V58's 19:16:30 receipt snapshot
(`a3fe83a7…` → `759cd9d3…`); this table and `receipt.json` record the final bytes. No other
report changed after V58's snapshot. V40's row in `receipt.json` carries the hash of this file
as written.

## Bottom line

PASS — presence audit complete and receipt skeleton written; 61/64 seat reports present with
sha256 pinned (all 6 producers + 55 verifiers), V24 and V35 ABSENT (past the poll-wait protocol
window, never landed), V40 = this receipt seat; no duplicates, no header mismatches, no
parent-tree strays; V58's prior receipt preserved byte-for-byte; `agent_id` left null for L1.
