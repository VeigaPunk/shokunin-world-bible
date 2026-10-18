# V123 — presence-final-2 (round 99)

**Seat:** V123 `presence-final-2`. **Role:** final failsafe presence audit. Write regardless of whether the wave has closed. 128-seat table, honest ABSENTs, producer artifact hashes, reconcile against V39 / V99 / V101 receipts. Judges **no claim** (C1/C2) and **no axis**. Does not verify a plan. Does not infer a missing report from scratch.

**Axes for this seat:** presence completeness (every declared seat accounted), byte honesty (sha256 only of files that exist), non-interference (this report and `V123-scratch/` only), cutoff honesty (protocol bound quoted; later landings not back-filled into the table).

**Lane root:** `/home/vgpnk/Projects/shokunin/lore-shokunin`. **Baseline:** r98 closure `4265df5`. **HEAD:** `337f0fa52b02626b7687eedbb2d99fab30446fe4`. Ancestor check exit `0` (`git merge-base --is-ancestor 4265df5 HEAD`). Wave tree uncommitted. Leaf seat: no nested agents, no commits, no pushes, no network.

Roster: **S1–S5 + V01–V123 = 128**, taken from `V99-scratch/roster.txt` (128 lines, prefixes parsed). Report presence = a top-level `seats/<SEAT>-*.md`. Scratch is not a report. This file is excluded from the pre-write count and listed as THIS.

## 1. Poll-wait (SELF subtracted)

Protocol: 20 s cadence, max 40 tries, ~13 min. Early stop only if reports ≥ 127 (others; SELF subtracted). That condition never fired.

Stall-escape 1 (recorded, not fatal): the first poll process was killed by a 300 s tool timeout after try 15 (`2026-10-17T22:07:23-03:00`). Tries 16–40 were restarted in a second process. Numbering in `V123-scratch/poll.log` is continuous.

Stall-escape 2 (recorded, not fatal): try 40 closed at `2026-10-17T22:21:05-03:00` with **14** top-level reports (`S=2 V=12`), V39/V99/V101 reports absent, `receipt.json` absent, knowledge files absent. The write was not made at that second because `V39-receipt.md` (a required reconciliation target) had not landed. V39's poll exhausted at 22:16:26; their report landed at 22:30:30. The table below was then generated at 22:46:33, not at 22:21 and not at 22:30. The gap is generator time plus continued landings, not a second 40-try poll. The wave was still landing. This table is a cutoff, not a closed census. Not extended to V101's 30-minute escape.

Quoted poll log (`V123-scratch/poll.log`):

```
2026-10-17T22:02:42-03:00 try=1 reports=1 S=1 V=0 dirs=89 arts=YYYYNNYY V39=0 V99=0 V101=0
2026-10-17T22:03:02-03:00 try=2 reports=2 S=1 V=1 dirs=94 arts=YYYYNNYY V39=0 V99=0 V101=0
...
2026-10-17T22:19:25-03:00 try=36 reports=14 S=2 V=12 dirs=115 arts=YYYYNNYY V39=0 V99=0 V101=0 receipt=0
2026-10-17T22:19:45-03:00 try=37 reports=14 S=2 V=12 dirs=115 arts=YYYYNNYY V39=0 V99=0 V101=0 receipt=0
2026-10-17T22:20:05-03:00 try=38 reports=14 S=2 V=12 dirs=116 arts=YYYYNNYY V39=0 V99=0 V101=0 receipt=0
2026-10-17T22:20:25-03:00 try=39 reports=14 S=2 V=12 dirs=116 arts=YYYYNNYY V39=0 V99=0 V101=0 receipt=0
2026-10-17T22:20:45-03:00 try=40 reports=14 S=2 V=12 dirs=116 arts=YYYYNNYY V39=0 V99=0 V101=0 receipt=0
2026-10-17T22:21:05-03:00 DEADLINE tries=40
```

`arts` flag order: dependency_freeze.py, contract, tools README, SKILL.md, blind-spot table, lapse-scope note, fixture README, fixture map. `YYYYNNYY` through try 40 means the two knowledge files were absent on every try and the other six paths existed as files (existence ≠ producer delivery).

## 2. Write-time snapshot commands

Cutoff timestamp (script start, before hashing): `2026-10-17T22:46:33-03:00`.

```
$ git rev-parse HEAD
337f0fa52b02626b7687eedbb2d99fab30446fe4
$ git rev-parse 4265df5
4265df5e86e4121bde4125b649b89bb1676676a5
$ git merge-base --is-ancestor 4265df5 HEAD; echo exit:$?
exit:0
$ git diff --stat HEAD -- LOG.md
(empty)
$ git status --porcelain
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
?? .ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md
?? .ufo/waves/round-99/
?? corpus/fixtures/r99-window-lapse/
```

Pre-write top-level `*.md` count (this file not yet written): **73**. Roster present excluding V123: **73**. Roster absent excluding V123: **54**. After this write, V123 is present, so on-disk reports become at least 74 if nothing else lands during the write. Files that appeared while hashing (not folded into the table): none.

Duplicate prefixes: none. Unexpected prefixes: none. Stray `*.md` (no seat prefix): none. Header/filename mismatches (seat token absent from the first line and the first 20 lines): none.

## 3. 128-seat table

Status PRESENT means the report file existed at the listdir that opened this snapshot. ABSENT means it did not. Scratch yes/no is not presence. sha256 is of the bytes hashed immediately after that listdir. V123 is THIS (this file).

| seat | status | file | bytes | sha256 | mtime | scratch |
|---|---|---|---:|---|---|---|
| S1 | ABSENT | `S1-full-file-pins.md` | - | `-` | - | yes |
| S2 | ABSENT | `S2-tools-docs.md` | - | `-` | - | yes |
| S3 | PRESENT | `S3-fixture-author.md` | 5069 | `3d81a75e0f154ed6c2297da8a9521391797a81740e0ede5443070b0c471cf73a` | 2026-10-17T22:01:40-03:00 | no |
| S4 | PRESENT | `S4-fixture-docs.md` | 9303 | `61bfdec1f5b7bbcdda653230bb4be1b6c1913683af67e2ae02e4ee46a327f72f` | 2026-10-17T22:03:54-03:00 | yes |
| S5 | ABSENT | `S5-knowledge-author.md` | - | `-` | - | yes |
| V01 | ABSENT | `V01-c1-payload.md` | - | `-` | - | yes |
| V02 | ABSENT | `V02-c1-markdown-tamper.md` | - | `-` | - | yes |
| V03 | ABSENT | `V03-c1-before-after.md` | - | `-` | - | yes |
| V04 | ABSENT | `V04-c1-selftest.md` | - | `-` | - | yes |
| V05 | ABSENT | `V05-c1-chain.md` | - | `-` | - | no |
| V06 | PRESENT | `V06-c1-refreeze-scope.md` | 7312 | `c1a6cc2b2298275fdb9fa473fc2ccfeb5bef24c0a34da098654fa97035a414a5` | 2026-10-17T22:36:13-03:00 | no |
| V07 | PRESENT | `V07-c1-code-review.md` | 4789 | `e489f74e4bdb931e18c6121bbbb6573978d4af501902235d960769881a44fb0d` | 2026-10-17T22:33:01-03:00 | yes |
| V08 | ABSENT | `V08-c1-negative-rerun.md` | - | `-` | - | yes |
| V09 | ABSENT | `V09-c1-cross-gates.md` | - | `-` | - | yes |
| V10 | PRESENT | `V10-c2-checker.md` | 6894 | `9ee8c876b7ff1be1481c7219b06307163ed5a0553ef168bdda23e677f99f7f45` | 2026-10-17T22:04:39-03:00 | yes |
| V11 | PRESENT | `V11-c2-inherited-equality.md` | 13546 | `a2f60b65b440efd0b178c5c314fc51ded510e8b8bd80db3c0ce6fd87b2d20e03` | 2026-10-17T22:11:54-03:00 | yes |
| V12 | PRESENT | `V12-c2-support-map.md` | 10805 | `b559cdb76adbebc6791e3b784d92188437f4195a828120ac9c9b522028fc9246` | 2026-10-17T22:21:50-03:00 | yes |
| V13 | PRESENT | `V13-c2-anchors.md` | 12948 | `a7ef2d47c29e97cfe41f93800f0fc1a24ca6ad6a636734f4517300d70c2778dd` | 2026-10-17T22:05:32-03:00 | yes |
| V14 | PRESENT | `V14-c2-whole-claim.md` | 15308 | `abb85e5253be270b26cf80c0e340fadacb3b069e5a9e2a28c2409109060b0e25` | 2026-10-17T22:31:38-03:00 | no |
| V15 | PRESENT | `V15-c2-anti-overclaim.md` | 15969 | `ae3a8aaf227ea8d109c11af29a34b86864829c321c8c25524aabc38d8adfffb3` | 2026-10-17T22:46:05-03:00 | yes |
| V16 | ABSENT | `V16-c2-dependency-probe.md` | - | `-` | - | yes |
| V17 | PRESENT | `V17-c2-table-audit.md` | 4687 | `3ce0c56f46d7981c0c1f8f48c41c53f10bcbc12f8c06946a5a24581cffb5ca08` | 2026-10-17T22:37:38-03:00 | yes |
| V18 | PRESENT | `V18-c2-table-completeness.md` | 4221 | `e562493941c02b28b2c3f5bfd897dffe8dc51d3476f9cb0e06b50d21633fea31` | 2026-10-17T22:32:00-03:00 | yes |
| V19 | PRESENT | `V19-c2-note-review.md` | 3508 | `64cd0a9caab45b9d3b8e569e80b535925e835168b26c6e57c1b9b47b633dbc38` | 2026-10-17T22:36:48-03:00 | yes |
| V20 | PRESENT | `V20-preservation-census.md` | 7979 | `506482b1484cec085467fdf59b2929bc300b0a46328b1c2f962566c7fb0d33d0` | 2026-10-17T22:42:32-03:00 | yes |
| V21 | PRESENT | `V21-preservation-mutations.md` | 6039 | `2b61809b282dc60385272f2b858fbff5a65b7b619b45ae7f8bc5446c4b699362` | 2026-10-17T22:38:02-03:00 | yes |
| V22 | PRESENT | `V22-gates-boundary.md` | 14276 | `9d049d6103e382e08e055b87fcbfe57c94dbf3aba16a027bad9fbad7510f4e2a` | 2026-10-17T22:41:56-03:00 | yes |
| V23 | ABSENT | `V23-scope-creep.md` | - | `-` | - | yes |
| V24 | ABSENT | `V24-freshness.md` | - | `-` | - | yes |
| V25 | PRESENT | `V25-doc-parity.md` | 17556 | `1749c2cffd2e911ada45ef3f90638e86ab75379d43ef106a6514772c0d5ac596` | 2026-10-17T22:39:44-03:00 | yes |
| V26 | PRESENT | `V26-operability.md` | 7117 | `51fe5d09917edf37af5600a61beaab44e623994f72f4ba54dc7d6fa3e660eb9b` | 2026-10-17T22:35:35-03:00 | yes |
| V27 | PRESENT | `V27-adjacency.md` | 8931 | `61c956cfcd879521cf8b034f9d4c2d1e882021e88d35d876edcfd7d3d10cc42e` | 2026-10-17T22:38:08-03:00 | yes |
| V28 | ABSENT | `V28-verdict-calibration.md` | - | `-` | - | yes |
| V29 | PRESENT | `V29-verdict-depth.md` | 18341 | `1f8eb8316b844dd64cd832561976dfddbd98c2674778a2d2fef8d5eb156b5e1e` | 2026-10-17T22:33:40-03:00 | yes |
| V30 | ABSENT | `V30-verdict-coverage.md` | - | `-` | - | yes |
| V31 | ABSENT | `V31-verdict-operability.md` | - | `-` | - | yes |
| V32 | PRESENT | `V32-verdict-freshness.md` | 5550 | `e94a49e63825fcdeaad4561b45dec05d8676b255317dbe3008e778ca098ad711` | 2026-10-17T22:32:25-03:00 | yes |
| V33 | PRESENT | `V33-verdict-adjacency.md` | 7506 | `61ba3ac0f6f3aced04ff5d3764086f7136cb7869ccd5ab24a25b512ec9448138` | 2026-10-17T22:27:58-03:00 | yes |
| V34 | ABSENT | `V34-adjudicator.md` | - | `-` | - | no |
| V35 | PRESENT | `V35-shonen-format.md` | 27008 | `96a7e622dd230570bc21d799600ccf29641f2e6bbd7cd63cff74dbddfd284580` | 2026-10-17T22:43:11-03:00 | yes |
| V36 | ABSENT | `V36-debt.md` | - | `-` | - | yes |
| V37 | ABSENT | `V37-spec-conformance.md` | - | `-` | - | yes |
| V38 | ABSENT | `V38-integration-checklist.md` | - | `-` | - | yes |
| V39 | PRESENT | `V39-receipt.md` | 11188 | `acee8ae147c65f11bf2e84c31c42735ca0ce20a458ac3337ca3af4cf21753525` | 2026-10-17T22:30:30-03:00 | yes |
| V40 | PRESENT | `V40-census-replica-2.md` | 11708 | `09c89289c34964e819bab74dc41394da18872497822fc6939268c286b1d4cd5e` | 2026-10-17T22:40:54-03:00 | yes |
| V41 | PRESENT | `V41-anchor-replica-2.md` | 9792 | `40af4141891fe1d0a91017080d5ce232e2e252743811ec61dc8c751e984ea0d6` | 2026-10-17T22:17:06-03:00 | yes |
| V42 | ABSENT | `V42-whole-claim-replica-2.md` | - | `-` | - | yes |
| V43 | ABSENT | `V43-c1-negative-2.md` | - | `-` | - | yes |
| V44 | PRESENT | `V44-c2-table-2.md` | 2483 | `926689d83fd6b6ae25302178eae39c6112aff19d5be7ecea9820eb2a1afb5a7d` | 2026-10-17T22:31:21-03:00 | yes |
| V45 | ABSENT | `V45-pins-c9.md` | - | `-` | - | yes |
| V46 | PRESENT | `V46-inherited-tools.md` | 8486 | `6442e5ce7f3fc3ace785985467fd03449e492079fe30d2ce2f5cb280f26b2957` | 2026-10-17T22:40:40-03:00 | yes |
| V47 | PRESENT | `V47-byte-prefix-2.md` | 14225 | `321491fb9b0757f867b5e0cc45338bc106960908f64eb3b8c37aed47ab8c5410` | 2026-10-17T22:15:20-03:00 | yes |
| V48 | PRESENT | `V48-relation-scope-2.md` | 17294 | `7c1e611d330c6e99d3e1acadb78f8bfeef378d456ac2802516e60a306ea33949` | 2026-10-17T22:46:08-03:00 | yes |
| V49 | PRESENT | `V49-support-regression.md` | 42856 | `93e523516f99e96143bf2549ded5dc1e6129579801bb99cf5ef488fdb67a8530` | 2026-10-17T22:39:20-03:00 | yes |
| V50 | ABSENT | `V50-cross-seat-audit.md` | - | `-` | - | yes |
| V51 | PRESENT | `V51-crosscheck-depth.md` | 17197 | `dc034db60cbfff474b796f61e96870ee8e30a856962a69e00d52ba8709f7adaf` | 2026-10-17T22:41:28-03:00 | yes |
| V52 | PRESENT | `V52-crosscheck-calibration.md` | 4890 | `d4253addd96a9b99faa0fa702292696d08844ea70b8a4f3fd5f254dad2950073` | 2026-10-17T22:37:55-03:00 | yes |
| V53 | ABSENT | `V53-receipt-wording.md` | - | `-` | - | yes |
| V54 | ABSENT | `V54-endgame-monitor.md` | - | `-` | - | yes |
| V55 | ABSENT | `V55-claim-text-audit.md` | - | `-` | - | yes |
| V56 | PRESENT | `V56-fixture-readme.md` | 15101 | `32ad2bd635d605f2f67ea5ba27172b8f5c4ef63953abc06fe4ba58f31234ad0b` | 2026-10-17T22:30:09-03:00 | yes |
| V57 | PRESENT | `V57-knowledge-note.md` | 5332 | `6ee61f14291e9294cab0af4da5d41128250cbf17520406c8d689bc5008954c54` | 2026-10-17T22:40:16-03:00 | yes |
| V58 | ABSENT | `V58-mutual-wait-guard.md` | - | `-` | - | yes |
| V59 | PRESENT | `V59-blind-spot-vs-debt-2.md` | 3796 | `081654f0717731d0bca720e177965233689428bf4503dab0cf60b2590b7ea49c` | 2026-10-17T22:46:16-03:00 | yes |
| V60 | PRESENT | `V60-table-row-format.md` | 5176 | `9340e8903b2bde4fb491dee5611840737e3bc9eafdd7b5f2484cb97e874715ef` | 2026-10-17T22:41:21-03:00 | yes |
| V61 | ABSENT | `V61-c1-payload-2.md` | - | `-` | - | yes |
| V62 | PRESENT | `V62-c1-markdown-tamper-2.md` | 10695 | `cea35ca945d844d432f3521364127553174c4b67b3a53f09155ac218447d8f81` | 2026-10-17T22:38:28-03:00 | yes |
| V63 | PRESENT | `V63-c2-chain-order.md` | 9660 | `d7f9b865ee7eedf6a225b39e22c7509592e482157c77dec8b3c5790ac36900db` | 2026-10-17T22:44:03-03:00 | yes |
| V64 | PRESENT | `V64-c2-lapse-scope.md` | 6663 | `cb40cb22e96aeafe00bb0a574558c7f09690f22932b697481c47b1baf6bd2e7c` | 2026-10-17T22:32:20-03:00 | yes |
| V65 | PRESENT | `V65-freshness-2.md` | 13808 | `66747998274bc01ead066ccf76de1d05155a125f05746c4312b2936dbcb90663` | 2026-10-17T22:36:11-03:00 | yes |
| V66 | ABSENT | `V66-doc-parity-2.md` | - | `-` | - | yes |
| V67 | ABSENT | `V67-operability-2.md` | - | `-` | - | yes |
| V68 | PRESENT | `V68-adjacency-2.md` | 7930 | `d1ab2308693704bcb848559e051ede400414cac29807fe8a52f8a734b6d1ae97` | 2026-10-17T22:03:15-03:00 | no |
| V69 | ABSENT | `V69-crosscheck-coverage-2.md` | - | `-` | - | yes |
| V70 | PRESENT | `V70-census-3.md` | 12052 | `443f75094fca12234c9691f9ef4aef29a509f948927293ccd6b0b081ca46aaf5` | 2026-10-17T22:43:41-03:00 | yes |
| V71 | ABSENT | `V71-receipt-audit-2.md` | - | `-` | - | yes |
| V72 | ABSENT | `V72-spec-conformance-2.md` | - | `-` | - | yes |
| V73 | PRESENT | `V73-shonen-2.md` | 18762 | `bc262e9cc342ac99c5865ae0fca6d1fef3515d0158481a4209a16a29ab5921d0` | 2026-10-17T22:42:07-03:00 | yes |
| V74 | ABSENT | `V74-debt-2.md` | - | `-` | - | yes |
| V75 | ABSENT | `V75-integration-2.md` | - | `-` | - | yes |
| V76 | PRESENT | `V76-c1-usage-surface.md` | 8611 | `61e793b24ed1139317ec3e320c28068882365918265a5435411e458b68369b7f` | 2026-10-17T22:37:32-03:00 | yes |
| V77 | PRESENT | `V77-c2-map-inventory.md` | 8641 | `e51103276a7db11c4a5c9ed188ec396c34962d320efd1910f0cbea151c8ce7f1` | 2026-10-17T22:10:52-03:00 | yes |
| V78 | ABSENT | `V78-cross-gates-2.md` | - | `-` | - | yes |
| V79 | ABSENT | `V79-c1-contract-validity.md` | - | `-` | - | yes |
| V80 | PRESENT | `V80-c2-prose-prefix.md` | 7122 | `aaf5b0d1c47b44478bcac40af92c81bb2bce1025d41add69e1494283b08d2cee` | 2026-10-17T22:02:52-03:00 | yes |
| V81 | ABSENT | `V81-r99-frozen.md` | - | `-` | - | yes |
| V82 | PRESENT | `V82-crosscheck-operability.md` | 7817 | `00eb1b0984dcf9490ce07f8de3ef1eed79901c9cb9c52fe1ee75ba4ce9d7fa39` | 2026-10-17T22:41:53-03:00 | yes |
| V83 | ABSENT | `V83-host-conditions.md` | - | `-` | - | yes |
| V84 | PRESENT | `V84-pins-in-notes.md` | 4224 | `4ae504003ddd528831a7c2ba77d3d10d426e9f7d731950017fd712da12d8eade` | 2026-10-17T22:32:49-03:00 | yes |
| V85 | ABSENT | `V85-c1-ten-file-proof.md` | - | `-` | - | yes |
| V86 | PRESENT | `V86-c2-no-new-entity.md` | 9403 | `775bd16a31f906bc3cc2f4a14139504598ddd9c907725e4e864412d258b0a38f` | 2026-10-17T22:12:15-03:00 | yes |
| V87 | PRESENT | `V87-scope-final.md` | 9744 | `bb4c2e2ece01c90508a76736767b5d5eb5de875df4bd032230f54c3c4ee4f86b` | 2026-10-17T22:46:10-03:00 | yes |
| V88 | PRESENT | `V88-freshness-3.md` | 5296 | `490969f7794145b5ad08b300e65f3f64e57a45620941554f58c5f97a991b659c` | 2026-10-17T22:36:36-03:00 | yes |
| V89 | PRESENT | `V89-c1-migration-preserved.md` | 5108 | `e5ec213ce86452150708704c5cf12cd9fb24ab12499fcbaa29ad40ccc0443ae6` | 2026-10-17T22:32:54-03:00 | yes |
| V90 | PRESENT | `V90-c2-editorial-rows.md` | 6868 | `d454448ea3d7fe80132a62344f3a1df64e7fc1c67c53bfdd7721ade222147bfe` | 2026-10-17T22:22:39-03:00 | yes |
| V91 | PRESENT | `V91-crosscheck-freshness.md` | 8228 | `9b28f301cb2add447b5a01fdfdab8bde4a488e919467207d09f8fad62c4468dc` | 2026-10-17T22:31:57-03:00 | yes |
| V92 | ABSENT | `V92-cross-seat-2.md` | - | `-` | - | yes |
| V93 | PRESENT | `V93-census-4.md` | 7553 | `be720d2a8b3550ce256805878bc2de18c224e2f92993e1df779a830c20140ff6` | 2026-10-17T22:37:33-03:00 | yes |
| V94 | PRESENT | `V94-c1-two-mutation.md` | 10470 | `2fe23cbb773962f93361ca343856559f124189affd7e52f5c59af6433480284f` | 2026-10-17T22:29:36-03:00 | yes |
| V95 | PRESENT | `V95-c2-lapse-wording.md` | 15612 | `ca217cff89d10a58caf40703e8f7a55e36064fc77e198c402e70daccc0b2a11e` | 2026-10-17T22:24:23-03:00 | yes |
| V96 | ABSENT | `V96-registry-accuracy.md` | - | `-` | - | yes |
| V97 | PRESENT | `V97-c1-selftest-isolation.md` | 5090 | `92eb427c8a196c8d71255feee50e8ab2c9082f04a2c60465827357ee9e8be5b7` | 2026-10-17T22:32:55-03:00 | yes |
| V98 | PRESENT | `V98-c2-table-citations.md` | 5185 | `4b47296c3afab19be1f0ad4477607f83bdcdd51aba8283a1021fac24bc16b53b` | 2026-10-17T22:26:44-03:00 | yes |
| V99 | ABSENT | `V99-receipt-3.md` | - | `-` | - | yes |
| V100 | ABSENT | `V100-late-bookkeeper.md` | - | `-` | - | yes |
| V101 | ABSENT | `V101-presence-final.md` | - | `-` | - | yes |
| V102 | PRESENT | `V102-c1-doc-commands.md` | 4526 | `e7714246a1ac5ac897d708f0ebd3fe27e0bb255e57c54f9966d3681c5eef3422` | 2026-10-17T22:29:08-03:00 | no |
| V103 | PRESENT | `V103-c2-note-crossrefs.md` | 6484 | `c9f231b981a461381f72484cc5e51ca21f83a752876396d54b234a6142f6b33b` | 2026-10-17T22:40:13-03:00 | yes |
| V104 | ABSENT | `V104-c1-schema-version.md` | - | `-` | - | yes |
| V105 | PRESENT | `V105-c2-event-description.md` | 9976 | `3668a34e84ee36a5ce2e3cdbffe9ce4eb34982f786b53f13013b0bcf39d0d1e2` | 2026-10-17T22:11:49-03:00 | yes |
| V106 | PRESENT | `V106-c1-chain-foreign-all.md` | 5150 | `57fbd7dfb4ad9ea7db2ef42a4b8bb67a1e739646d8fa9e0d9cde8e7b413eedd6` | 2026-10-17T22:37:39-03:00 | yes |
| V107 | ABSENT | `V107-crosscheck-adjacency.md` | - | `-` | - | yes |
| V108 | PRESENT | `V108-c1-tamper-restore.md` | 7663 | `9b686d6ef18f6a6ed4410178dbaa71004207074d3b1678ca3bb5dfddf35ab76b` | 2026-10-17T22:31:55-03:00 | yes |
| V109 | PRESENT | `V109-c2-inherited-map-rows.md` | 5160 | `8bcbd46a1f5888cc99bb7a8e29947a6ae5a81e5455b917ac00d7c5e25495c362` | 2026-10-17T22:14:24-03:00 | yes |
| V110 | ABSENT | `V110-c1-precedence-text.md` | - | `-` | - | yes |
| V111 | PRESENT | `V111-c2-arc-summary.md` | 17360 | `774aadfa62fbe3da4066e503c7b43697835a5129ab1b119af001dd78258ccddb` | 2026-10-17T22:39:15-03:00 | yes |
| V112 | PRESENT | `V112-c1-payload-docs.md` | 9526 | `e84c22121fc6bfd55e7914d3c5de28c5c2c5669eeef2d6ab3885144aaaa31323` | 2026-10-17T22:38:50-03:00 | yes |
| V113 | PRESENT | `V113-c2-inventory-line.md` | 8621 | `b1e963422de1b54d3384c434a5aceb280c5c7231b670125909eb9a9866502101` | 2026-10-17T22:22:48-03:00 | yes |
| V114 | ABSENT | `V114-freshness-4.md` | - | `-` | - | yes |
| V115 | PRESENT | `V115-c1-verify-vs-freeze.md` | 9080 | `71fcd5048e1c357402210393f721105ef3a26670ce5b4439d424fa494bd431fa` | 2026-10-17T22:32:53-03:00 | yes |
| V116 | PRESENT | `V116-c2-clerk-continuity.md` | 10090 | `0779931664e7fc0b8a4ca504c83f8b2aaea6228cc1c1cd8b71f813b798d9e737` | 2026-10-17T22:25:55-03:00 | no |
| V117 | ABSENT | `V117-integration-3.md` | - | `-` | - | yes |
| V118 | ABSENT | `V118-c1-negative-3.md` | - | `-` | - | yes |
| V119 | PRESENT | `V119-c2-anchors-3.md` | 9125 | `9206493b7fe5fb982f53756d2f1d260d91e6ce265d3c7c7f14277a82efc66b35` | 2026-10-17T22:11:01-03:00 | yes |
| V120 | ABSENT | `V120-verdict-summary.md` | - | `-` | - | yes |
| V121 | ABSENT | `V121-frozen-r93.md` | - | `-` | - | yes |
| V122 | PRESENT | `V122-c2-table-vs-skill.md` | 6037 | `1c402656a615eea28083415b3ae1915448f4c8965b1d492a21b62c914fcd5a54` | 2026-10-17T22:31:31-03:00 | yes |
| V123 | THIS | `V123-presence-final-2.md` | - | `-` | - | yes |

Present others (73): S3, S4, V06, V07, V10, V11, V12, V13, V14, V15, V17, V18, V19, V20, V21, V22, V25, V26, V27, V29, V32, V33, V35, V39, V40, V41, V44, V46, V47, V48, V49, V51, V52, V56, V57, V59, V60, V62, V63, V64, V65, V68, V70, V73, V76, V77, V80, V82, V84, V86, V87, V88, V89, V90, V91, V93, V94, V95, V97, V98, V102, V103, V105, V106, V108, V109, V111, V112, V113, V115, V116, V119, V122

ABSENT others (54): S1, S2, S5, V01, V02, V03, V04, V05, V08, V09, V16, V23, V24, V28, V30, V31, V34, V36, V37, V38, V42, V43, V45, V50, V53, V54, V55, V58, V61, V66, V67, V69, V71, V72, V74, V75, V78, V79, V81, V83, V85, V92, V96, V99, V100, V101, V104, V107, V110, V114, V117, V118, V120, V121

Producer reports absent: S1, S2, S5. At the same snapshot, `S1-scratch`, `S2-scratch`, and `S5-scratch` all existed (`S5-scratch is_dir=True`). Scratch is not a report. An earlier look (22:22) had no `S5-scratch`; it existed by this cutoff.

## 4. Producer artifact hashes

Existence and bytes only. Not a C1 or C2 verdict. A file whose owner report is ABSENT is not a confirmed delivery.

```
PRESENT fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c bytes=29110 mtime=2026-10-17T22:38:11-03:00 DIFF-vs-4265df5 DRIFT-vs-V39  corpus/tools/dependency_freeze.py
PRESENT 8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628 bytes=25987 mtime=2026-10-17T22:08:46-03:00 DIFF-vs-4265df5 MATCH-V39  corpus/tools/dependency-freeze-contract.json
PRESENT 294dd56f29ce1fd40be3a80d365b33724c9cd1969d3f7b7abb271fd1adaaa207 bytes=32577 mtime=2026-10-17T21:32:05-03:00 SAME-as-4265df5 MATCH-V39  corpus/tools/README.md
PRESENT 22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5 bytes=16802 mtime=2026-10-17T21:34:23-03:00 SAME-as-4265df5 MATCH-V39  SKILL.md
PRESENT b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049 bytes=6176 mtime=2026-10-17T22:03:19-03:00  corpus/fixtures/r99-window-lapse/README.md
PRESENT d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d bytes=17119 mtime=2026-10-17T22:02:39-03:00  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
PRESENT 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570 bytes=3 mtime=2026-10-17T21:36:10-03:00  corpus/fixtures/r99-window-lapse/contradictions.json
PRESENT db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984 bytes=1793 mtime=2026-10-17T21:36:10-03:00  corpus/fixtures/r99-window-lapse/entities.json
PRESENT fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d bytes=5114 mtime=2026-10-17T22:01:13-03:00  corpus/fixtures/r99-window-lapse/fictional-excerpts.md
PRESENT 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37 bytes=1956 mtime=2026-10-17T21:36:10-03:00  corpus/fixtures/r99-window-lapse/inspiration-note.md
PRESENT c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9 bytes=139 mtime=2026-10-17T21:36:10-03:00  corpus/fixtures/r99-window-lapse/relations.json
PRESENT b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd bytes=640 mtime=2026-10-17T21:36:10-03:00  corpus/fixtures/r99-window-lapse/source-excerpt.md
PRESENT 8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15 bytes=3293 mtime=2026-10-17T22:01:13-03:00  corpus/fixtures/r99-window-lapse/sources.json
PRESENT 2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069 bytes=2998 mtime=2026-10-17T22:01:13-03:00  corpus/fixtures/r99-window-lapse/timeline.json
ABSENT  corpus/knowledge/r99-gate-blind-spot-table.md
ABSENT  corpus/knowledge/r99-lapse-scope-note.md
```

Knowledge files ABSENT: ['corpus/knowledge/r99-gate-blind-spot-table.md', 'corpus/knowledge/r99-lapse-scope-note.md'].

`corpus/tools/README.md` and `SKILL.md` match `4265df5` and HEAD. Their mtimes (21:32 and 21:34) predate this re-dispatch (~22:00). S2 has not delivered an edit. `dependency_freeze.py` and `dependency-freeze-contract.json` differ from `4265df5` / HEAD and match the hashes V39 quoted at 22:22:17; S1's report is still ABSENT, so those bytes are an in-flight tree, not a confirmed S1 delivery.

`corpus/fixtures/r99-window-lapse/` has the ten declared files. S3 and S4 reports are PRESENT. This seat does not re-run `check_bible`, `support_check`, or `map_obligations`.

## 5. Reconciliation against V39 / V99 / V101

### V39 receipt

`V39-receipt.md` at snapshot: PRESENT bytes=11188 sha256=acee8ae147c65f11bf2e84c31c42735ca0ce20a458ac3337ca3af4cf21753525 mtime=2026-10-17T22:30:30-03:00.

V39's report (read before this snapshot) states a 22:22:17 audit of **15/128** present, **113** absent, producer reports S1/S2/S5 absent, both knowledge files absent, duplicate prefixes none, header mismatches none, and says `.ufo/waves/round-99/receipt.json` is the skeleton. `V39-scratch/audit-summary.txt`:

```
{
 "snapshot": "2026-10-17T22:22:17-0300",
 "present_incl_self": 15,
 "present_excl_self": 15,
 "absent": 113,
 "producer_absent": [
  "S1",
  "S2",
  "S5"
 ],
 "missing_candidates": [
  "corpus/knowledge/r99-gate-blind-spot-table.md",
  "corpus/knowledge/r99-lapse-scope-note.md"
 ],
 "duplicates": {},
 "header_mismatches": 0,
 "unexpected_md": [],
 "parent_tree_md": [],
 "fixture_files": [
  "README.md",
  "claim-excerpt-map.md",
  "contradictions.json",
  "entities.json",
  "fictional-excerpts.md",
  "inspiration-note.md",
  "relations.json",
  "source-excerpt.md",
  "sources.json",
  "timeline.json"
 ],
 "head": "337f0fa52b02626b7687eedbb2d99fab30446fe4",
 "baseline_ancestor": true
}
```

`receipt.json` at this snapshot: **PRESENT bytes=50183 sha256=5d74851756c407864643281eb3b738d5a0fad00ea3052a1d39a615a0ddc205c7**.

That is a claim-vs-disk check, not a rewrite of V39. If `receipt.json` is ABSENT here, V39's prose that the skeleton was written is not matched by the filesystem at this cutoff. If it is PRESENT, its sha256 is above and it was not treated as a finalized L1 receipt (V39 leaves `agent_id` null).

Byte reconciliation of the 15 reports V39 hashed at 22:22:17, re-hashed now:

```
MATCH S3-fixture-author.md 3d81a75e0f154ed6c2297da8a9521391797a81740e0ede5443070b0c471cf73a
MATCH S4-fixture-docs.md 61bfdec1f5b7bbcdda653230bb4be1b6c1913683af67e2ae02e4ee46a327f72f
MATCH V10-c2-checker.md 9ee8c876b7ff1be1481c7219b06307163ed5a0553ef168bdda23e677f99f7f45
MATCH V11-c2-inherited-equality.md a2f60b65b440efd0b178c5c314fc51ded510e8b8bd80db3c0ce6fd87b2d20e03
MATCH V12-c2-support-map.md b559cdb76adbebc6791e3b784d92188437f4195a828120ac9c9b522028fc9246
MATCH V13-c2-anchors.md a7ef2d47c29e97cfe41f93800f0fc1a24ca6ad6a636734f4517300d70c2778dd
MATCH V41-anchor-replica-2.md 40af4141891fe1d0a91017080d5ce232e2e252743811ec61dc8c751e984ea0d6
MATCH V47-byte-prefix-2.md 321491fb9b0757f867b5e0cc45338bc106960908f64eb3b8c37aed47ab8c5410
MATCH V68-adjacency-2.md d1ab2308693704bcb848559e051ede400414cac29807fe8a52f8a734b6d1ae97
MATCH V77-c2-map-inventory.md e51103276a7db11c4a5c9ed188ec396c34962d320efd1910f0cbea151c8ce7f1
MATCH V80-c2-prose-prefix.md aaf5b0d1c47b44478bcac40af92c81bb2bce1025d41add69e1494283b08d2cee
MATCH V86-c2-no-new-entity.md 775bd16a31f906bc3cc2f4a14139504598ddd9c907725e4e864412d258b0a38f
MATCH V105-c2-event-description.md 3668a34e84ee36a5ce2e3cdbffe9ce4eb34982f786b53f13013b0bcf39d0d1e2
MATCH V109-c2-inherited-map-rows.md 8bcbd46a1f5888cc99bb7a8e29947a6ae5a81e5455b917ac00d7c5e25495c362
MATCH V119-c2-anchors-3.md 9206493b7fe5fb982f53756d2f1d260d91e6ce265d3c7c7f14277a82efc66b35
```

Tool/doc hashes V39 quoted vs this snapshot are in §4 (`MATCH-V39` / `DRIFT-vs-V39`).

Count drift vs V39's 15: this snapshot has 73 other reports. The difference is later landings, not a contradiction of V39's earlier audit. V39 said the wave was still landing and that a later seat may supersede the skeleton. That prediction holds.

### V99 receipt-3

`V99-*.md` at snapshot: ABSENT.

`V99-scratch/poll-status.json` (their poll, not a receipt):

```
{
 "exhausted": true,
 "last": {
  "try": 40,
  "at": "2026-10-17T22:33:19-0300",
  "producer_missing": [
   "S1-full-file-pins.md",
   "S2-tools-docs.md",
   "S5-knowledge-author.md"
  ],
  "artifacts_missing": [
   "corpus/knowledge/r99-gate-blind-spot-table.md",
   "corpus/knowledge/r99-lapse-scope-note.md"
  ],
  "receipt": false,
  "v39_md": true,
  "top_md": 40,
  "top_md_excluding_self_cap": 127,
  "receipt_sha": null,
  "stable_receipt_polls": 0,
  "stable_md_polls": 0
 },
 "at": "2026-10-17T22:33:19-0300"
}
```

No V99 receipt to compare 1:1. Their poll, when last read, had not produced `V99-receipt-3.md`. Absence is recorded. Their scratch roster was used only as the seat-name source; it is not a receipt.

### V101 presence-final

`V101-*.md` at snapshot: ABSENT.

`V101-scratch/poll.log` mtime `2026-10-17T22:46:24-03:00`. Last lines:

```
try2=7 ts=22:46:04 others=71 missing=56 dups=0 extra=[] prod_missing=['S1', 'S2', 'S5'] art_missing=2 receipt=1 delta=0
  art_missing=corpus/knowledge/r99-gate-blind-spot-table.md,corpus/knowledge/r99-lapse-scope-note.md
try2=8 ts=22:46:24 others=73 missing=54 dups=0 extra=[] prod_missing=['S1', 'S2', 'S5'] art_missing=2 receipt=1 delta=2
  art_missing=corpus/knowledge/r99-gate-blind-spot-table.md,corpus/knowledge/r99-lapse-scope-note.md
```

The log stops at try 15 / 22:08:09 and was not updated through this cutoff. No V101 report. No evidence in that log that they finalized `receipt.json`. ABSENT. Not inferred from the frozen log.

## 6. What this seat does not claim

- Not 128/128. Not a closed wave.
- Not a C1 verdict (full-file pins, 18/18, 6/6) and not a C2 verdict (lapse fixture, blind-spot table). The blind-spot table and lapse-scope note were absent, so those claims were not verified. No plan was verified in their place.
- Not an adjudication. Later seats (V101's 30-minute escape, V99 if it writes after this cutoff, the L1) may supersede these counts.
- No `receipt.json` was written by this seat. That path belongs to V39 / V101.

## 7. Honesty

Try 40 (22:21:05) saw 14 reports. The §3 table sees 73 other reports plus this file, at 22:46:33. Both numbers are quoted from commands, not smoothed. At that cutoff S1, S2, and S5 reports were absent and both knowledge files were absent. `receipt.json` as hashed in §5 is the file that existed at 22:46:33. It is not the later rewrite in §8.

## 8. Post-cutoff observation (not a replacement census)

The §3 table is not rewritten. This section is a later read, quoted so the 22:46 ABSENTs are not mistaken for the live tree at handoff. The wave was still landing during this read (top-level `*.md` was 94 at 23:01:00 and 97 other reports at 23:04:09). Not folded into the table. Not a C1/C2 verdict.

23:01:00 read of `receipt.json` (rewritten after the hash in §5):

```
date 2026-10-17T23:01:00-03:00
receipt_sha256 7b0b5ef2b7308449469923e6286f98e45147d632dcb33b89b90a79c9e1304038
receipt_bytes 67825
receipt_snapshot_utc 2026-10-17T22:51:41-0300
dispatch_tool_call_id None
reports_expected 128
reports_present 85
reports_present_excl_self 84
reports_absent_count 43
producer_present ['S1', 'S3', 'S4']
producer_absent ['S2', 'S5']
missing_candidate_paths ['corpus/knowledge/r99-gate-blind-spot-table.md', 'corpus/knowledge/r99-lapse-scope-note.md']
pinned_freeze fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c
duplicate_report_prefixes {}
header_seat_mismatches []
agent_id_null 128 / 128
V99 ABSENT
V101 ABSENT
md_now 94
freeze_now fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c bytes 29110
knowledge ['r99-gate-blind-spot-table.md', 'r99-lapse-scope-note.md']
```

That 23:01 receipt is a V39 skeleton (`dispatch_tool_call_id` null, every `agent_id` null). Its `reports_present=85` is later than V39's prose census (15 at 22:22:17) and later than the §5 hash (`5d748517…`, 50183 bytes, which matched an earlier skeleton whose collection said `reports_present=46` at `receipt_snapshot_utc` 22:37:23). Three receipt observations, three counts. None is 128. The §5 hash is stale against the 23:01 file. `pinned_freeze` at 23:01 matches the §4 live hash `fb9bb9ff…`, not V39's earlier quoted `6f81f8be…`. The same 23:01 read is internally split: `missing_candidate_paths` still names both knowledge files, but the files were already on disk (`knowledge` list above). The receipt snapshot (22:51:41) is older than the 23:01 filesystem.

23:04:09 delta against the §3 ABSENT list (24 of 54 cutoff-ABSENT seats had a report; 30 still had none). Knowledge files and S2-owned docs existed as bytes; S2 and S5 reports did not. V99 and V101 reports still absent. `receipt.json` was not re-hashed at 23:04.

```
cutoff_present 73
cutoff_absent 54
now_other_reports 97
landed_since_cutoff 24
LANDED S1:S1-full-file-pins.md, V03:V03-c1-before-after.md, V05:V05-c1-chain.md, V16:V16-c2-dependency-probe.md, V23:V23-scope-creep.md, V24:V24-freshness.md, V28:V28-verdict-calibration.md, V31:V31-verdict-operability.md, V36:V36-debt.md, V45:V45-pins-c9.md, V58:V58-mutual-wait-guard.md, V61:V61-c1-payload-2.md, V66:V66-doc-parity-2.md, V78:V78-cross-gates-2.md, V79:V79-c1-contract-validity.md, V81:V81-r99-frozen.md, V83:V83-host-conditions.md, V85:V85-c1-ten-file-proof.md, V92:V92-cross-seat-2.md, V96:V96-registry-accuracy.md, V100:V100-late-bookkeeper.md, V104:V104-c1-schema-version.md, V110:V110-c1-precedence-text.md, V114:V114-freshness-4.md
STILL_ABSENT S2, S5, V01, V02, V04, V08, V09, V30, V34, V37, V38, V42, V43, V50, V53, V54, V55, V67, V69, V71, V72, V74, V75, V99, V101, V107, V117, V118, V120, V121
date 2026-10-17T23:04:09-03:00
ART 4670c0b71668c56c53c0bac90091531d3f0e881c7dcb2ac572d09f96ae22182e 20526 corpus/knowledge/r99-gate-blind-spot-table.md
ART 96de708f8e984f6f61ee6387342c287a275328a6293da1d225b2ad00040ebb54 14990 corpus/knowledge/r99-lapse-scope-note.md
ART fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c 29110 corpus/tools/dependency_freeze.py
ART 646784ae7407931a3721100fbcec49a2df35bdcd58275aec1df8327646f815d7 38397 corpus/tools/README.md
ART e0bcb61ab909146e34773dd56219cb1631070c1700a2481f8ad1181f3d864443 17287 SKILL.md
S1 PRESENT S1-full-file-pins.md
S2 ABSENT
S5 ABSENT
V99 ABSENT
V101 ABSENT
```

`corpus/tools/README.md` and `SKILL.md` were byte-identical to `4265df5` at the 22:46 cutoff (`294dd56f…`, `22ffaa82…`). At 23:04:09 they differed. S2's report was still absent, so those bytes are not a confirmed S2 delivery. The two knowledge files existed at 23:04:09; S5's report did not, so they are not a confirmed S5 delivery. No plan was verified in place of either missing report.

**Bottom line: INCONCLUSIVE — 128-seat table locked at 2026-10-17T22:46:33-03:00 with 73/127 other reports (V123 is this file) and S1/S2/S5 plus both knowledge files ABSENT at that instant; post-cutoff read at 23:04:09 found 24 of those 54 since landed (including S1) and the knowledge files plus S2-owned docs present as bytes, but S2, S5, V99, and V101 reports still ABSENT and the wave still landing, so this is not a closed 128-seat census.**
