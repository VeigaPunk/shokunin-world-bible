# V71 — receipt-audit-2 (round 99)

Seat: **V71 receipt-audit-2**. Mandate: after V39 lands, audit its hashes and counts; correct or flag. No claim adjudication (C1/C2). No axis verdict.

Axes for this seat: snapshot hash fidelity, count consistency, currency (post-seal drift), non-interference (no corpus writes).

Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`) is an ancestor of HEAD `337f0fa52b02626b7687eedbb2d99fab30446fe4`. Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report and `.ufo/waves/round-99/seats/V71-scratch/` only.

## 0. Poll-wait (SELF subtracted)

Cadence 20 s, max 40 tries. Success condition was a stable top-level `seats/V39-*.md`, not a plan and not scratch. A host 600 s background cap killed the first poller at try 30 (22:14:01). Resume completed tries 31–40. That cap is a recorded stall-escape, not a second budget.

```
try=1  ts=2026-10-17T22:04:21-03:00 v39=ABSENT arts=YYYYY..YY prod=..YY. md=4
try=30 ts=2026-10-17T22:14:01-03:00 v39=ABSENT arts=YYYYY..YY prod=..YY. md=11
RESUME after host 600s cap; prior tries=30
try=40 ts=2026-10-17T22:26:32-03:00 v39=ABSENT receipt=ABSENT arts=YYYYY..YY prod=..YY. md=19
ABSENT after 40 tries (resume completed budget)
```

V39's own poll (`V39-scratch/poll.log`) exhausted at the same bound:

```
try=40 2026-10-17T22:16:26-0300 reports=13 roster_present=13/128 producer_missing=['S1', 'S2', 'S5'] artifact_missing=2 unexpected=-
POLL-EXHAUSTED tries=40; writing receipt from last observation. ABSENT stays ABSENT.
```

The report was absent at try 40. It landed after the budget, before this audit was written. Audited bytes are the landed files, not `V39-scratch/audit.json` as a plan.

Landing times observed:

- `V39-receipt.md` first version mtime 22:30:30, 11188 bytes, sha256 `acee8ae147c65f11bf2e84c31c42735ca0ce20a458ac3337ca3af4cf21753525` (measured by this seat at 22:38, size stable across a 3 s check).
- First `receipt.json` mtime 22:37:23, 50183 bytes, sha256 `5d74851756c407864643281eb3b738d5a0fad00ea3052a1d39a615a0ddc205c7`. Preserved at `seats/V39-scratch/receipt-223723.json` (same sha256, copy mtime 22:51).
- V39 rewrote the report at 22:50:06 (11442 bytes, sha256 `d41012346169db4d3ad09420858f5c97248080cb8900b2a3ba22db5f499d47f3`).
- Corrected `receipt.json` mtime/snapshot 22:51:41, 67825 bytes, sha256 `7b0b5ef2b7308449469923e6286f98e45147d632dcb33b89b90a79c9e1304038`. Still those bytes at 23:10:24.

The 22:38 measurement of `acee8ae1…` matches the preserved receipt's V39 row. The rewrite made that row stale; the corrected receipt re-pins `d4101234…`. That re-pin matches the report as of 23:10:24.

## 1. What was audited

Corrected receipt snapshot `2026-10-17T22:51:41-0300`. Report table in `V39-receipt.md` (the 22:22:17 15-row hash table) plus section 4 historical pins and section 5 count claims. Independent recomputation: `sha256sum` and `python3` SHA-256 of the named paths. Full machine result: `V71-scratch/audit-result.json` (run at 23:03:55 against the corrected receipt) and `V71-scratch/quoted-verify.txt` (23:08:00). A final delta was taken at 23:10:24 because seats were still writing.

## 2. Counts — sealed snapshot holds

Corrected `receipt.json` `collection`:

```
expected 128 present 85 excl 84 absent 43 present_len 85 absent_len 43
agent_id_non_null 0
outcome_non_null 0
dispatch None
```

`seats[]` is 128 rows. `present` and `absent` are disjoint and cover the roster S1–S5 + V01–V123. `reports_present_excl_self` is 84 (85 minus V39). Producer present `['S1','S3','S4']`, absent `['S2','S5']`. Duplicate prefixes: none. Header mismatches on receipt-present files: none. `dispatch_tool_call_id` / every `agent_id` / every `outcome` are null. No invented ids found.

Section 5 claims checked against the preserved first receipt:

- first write `2026-10-17T22:37:23-0300`, 46 present: matches `receipt-223723.json` (`reports_present` 46, `reports_absent_count` 82).
- "31 seats changed since the quoted audit": `len(changed_since_pre_receipt_audit)` on that file is 31. `pre_receipt_audit_utc` is `2026-10-17T22:22:17-0300`.
- preserved path exists and its sha256 equals the receipt this seat hashed at 22:38 (`5d748517…`).

The 15-row table and `collection.pre_receipt_present` name the same 15 seats. No count error inside the sealed snapshot.

No seat listed absent in the 22:51:41 receipt has a report mtime at or before that snapshot. The absences were not missed files. They were files that did not exist yet.

## 3. Hashes that still match

All 15 hashes in the 22:22:17 table match `sha256sum` at 23:08:00, and match `V39-scratch/audit.json`. Quoted:

```
$ sha256sum .ufo/waves/round-99/seats/S3-fixture-author.md ... V119-c2-anchors-3.md
3d81a75e0f154ed6c2297da8a9521391797a81740e0ede5443070b0c471cf73a  S3-fixture-author.md
61bfdec1f5b7bbcdda653230bb4be1b6c1913683af67e2ae02e4ee46a327f72f  S4-fixture-docs.md
9ee8c876b7ff1be1481c7219b06307163ed5a0553ef168bdda23e677f99f7f45  V10-c2-checker.md
a2f60b65b440efd0b178c5c314fc51ded510e8b8bd80db3c0ce6fd87b2d20e03  V11-c2-inherited-equality.md
b559cdb76adbebc6791e3b784d92188437f4195a828120ac9c9b522028fc9246  V12-c2-support-map.md
a7ef2d47c29e97cfe41f93800f0fc1a24ca6ad6a636734f4517300d70c2778dd  V13-c2-anchors.md
40af4141891fe1d0a91017080d5ce232e2e252743811ec61dc8c751e984ea0d6  V41-anchor-replica-2.md
321491fb9b0757f867b5e0cc45338bc106960908f64eb3b8c37aed47ab8c5410  V47-byte-prefix-2.md
d1ab2308693704bcb848559e051ede400414cac29807fe8a52f8a734b6d1ae97  V68-adjacency-2.md
e51103276a7db11c4a5c9ed188ec396c34962d320efd1910f0cbea151c8ce7f1  V77-c2-map-inventory.md
aaf5b0d1c47b44478bcac40af92c81bb2bce1025d41add69e1494283b08d2cee  V80-c2-prose-prefix.md
775bd16a31f906bc3cc2f4a14139504598ddd9c907725e4e864412d258b0a38f  V86-c2-no-new-entity.md
3668a34e84ee36a5ce2e3cdbffe9ce4eb34982f786b53f13013b0bcf39d0d1e2  V105-c2-event-description.md
8bcbd46a1f5888cc99bb7a8e29947a6ae5a81e5455b917ac00d7c5e25495c362  V109-c2-inherited-map-rows.md
9206493b7fe5fb982f53756d2f1d260d91e6ce265d3c7c7f14277a82efc66b35  V119-c2-anchors-3.md
```

Corrected receipt V39 row matches the report:

```
$ sha256sum .ufo/waves/round-99/seats/V39-receipt.md
d41012346169db4d3ad09420858f5c97248080cb8900b2a3ba22db5f499d47f3  V39-receipt.md
```

Claimed bytes 11442. Match.

At 23:10:24 these corrected-receipt pins still match live bytes: `dependency_freeze.py` `fb9bb9ff…` (29110), `dependency-freeze-contract.json` `8c2561b0…` (25987), `SKILL.md` `e0bcb61a…` (17287), and all ten `corpus/fixtures/r99-window-lapse/` files (hashes in `quoted-verify.txt`). Section 4's contract hash `8c2561b0…` is the same value.

Section 4's other three hashes are the 22:22 observation, not the corrected pin, and must not be used as the receipt pin:

- `dependency_freeze.py` section 4 says `6f81f8be…` (29104 bytes, mtime 22:07:33). Current and corrected pin are `fb9bb9ff…`. The 22:07 bytes were overwritten at 22:38:11; this seat did not recompute `6f81f8be…`.
- `corpus/tools/README.md` section 4 says `294dd56f…` (mtime 21:32:05). Corrected pin is `646784ae…`.
- `SKILL.md` section 4 says `22ffaa82…` (mtime 21:34:23). Corrected pin is `e0bcb61a…`, which still matches.

## 4. Flags and corrections (post-seal drift, not snapshot arithmetic)

The corrected receipt says it will not be rewritten to chase later landings. That is accurate as a snapshot. It is already stale as a current census. None of the mismatches below have a report mtime at or before 22:51:41, so they are not evidence V39 hashed the sealed bytes wrong. Snapshot bytes for the rewritten reports were not recoverable.

Correction time: **2026-10-17T23:10:24-03:00**. The wave was still landing. These hashes are a delta, not a new seal. `V120` was written in the same second as the scan; treat that one hash as possibly in-flight.

**Count correction.** Receipt says 85 present / 43 absent. At 23:10:24, top-level roster reports on disk: **111**. Still absent as reports: S2, S5, and 15 other seats (128 − 111 = 17, which is 43 receipt-absent minus 26 later landings). S2 and S5 reports were still absent. Both knowledge files exist (they were correctly listed missing at 22:51:41; they landed at 22:57:50).

**README pin is stale after the seal.** At 23:08:00 `sha256sum` still matched the pin `646784ae7407931a3721100fbcec49a2df35bdcd58275aec1df8327646f815d7`. At 23:10:24:

```
837a7f5dfe913047530c7f92f3dd6b3df1b1a83c77ede12ba0c349cc134a049c  corpus/tools/README.md
```

39310 bytes, mtime 23:08:16. Use `837a7f5d…` until S2 stops writing.

**Knowledge files, absent in the receipt, present now:**

```
4670c0b71668c56c53c0bac90091531d3f0e881c7dcb2ac572d09f96ae22182e  corpus/knowledge/r99-gate-blind-spot-table.md
96de708f8e984f6f61ee6387342c287a275328a6293da1d225b2ad00040ebb54  corpus/knowledge/r99-lapse-scope-note.md
```

Both mtime 22:57:50, sizes 20526 and 14990. S5's report was still absent, so these are files without an owner report.

**Seven receipt report hashes rewritten after 22:51:41** (claimed → live at 23:10:24):

| seat | claimed sha256 | live sha256 | live bytes | live mtime |
|---|---|---|---:|---|
| V40 | `08561fff…67cca85f` | `f5f733acaf4c248e3d46f1dba296aa4b5a37442171eef009a9eb5ba83f052fd8` | 13479 | 22:53:00 |
| V48 | `d814ff16…6f623461` | `9e29c40d8cd6d5b9f14b9704e56c97a09291db3f948535a40afbbbd08ddf94b0` | 19764 | 22:54:48 |
| V51 | `dc034db6…709f7adaf` | `02f0c48bd9afdc3cd31fe5ab2008afffbf4d2f9c10cbb99f92702950b0f385a4` | 22374 | 23:04:28 |
| V73 | `c2dabac2…eeab88130` | `51e230768bb5b98a64aace0d514c363dc909775ebc2674bd9d8f2dbd0c55e55f` | 21842 | 23:06:41 |
| V76 | `61e793b2…b68369b7f` | `b31cf1e875e6328c5d16dfb887a9d440c50b2eae53ef50af1c75b9939b079a02` | 9206 | 23:03:07 |
| V96 | `0a980347…1dd399a5` | `6252c6ce7b751a2bab1187dfee02c491d5a1881f5b273b082425a39fd7041131` | 23646 | 23:08:07 |
| V123 | `9b7cdf7e…e3e7c4e07` | `8fbf2cd5dfbf7eb3312c95718196f056363ac2df1f92fe85a63d4c79ae252f01` | 34646 | 23:10:09 |

V51 and V123 moved more than once between 23:03 and 23:10. The live column is the 23:10:24 read only.

**26 reports that landed after the seal** (receipt has them absent; mtime after 22:51:41). Hashes at 23:10:24:

- V01 `e0cc3787e8122bc8398ee5604aa358ca4e7890916013cda00f8fee204861e0d8` 12743
- V02 `411f57211e600c61a72a9e15c6e7be41b67a2832f9c30f432840525121635eb4` 14165
- V03 `cb24666587fdc30708639b8fa8afd9cfdc14c7e534238ec8d284da6f000b8796` 11496
- V04 `a3613f0193caffab66a7e34ec73b2af26620afc6e92a5ef3aa676fe75d805131` 11424
- V05 `366425b9145529ecf379c6c26276611b15fe55ea41398ca5fa9a8e18ac456440` 12138
- V08 `198e08b243f42d6eaee105ebfbdfa93ccd532679cef70c7709e3e6a3f3f13b34` 15015
- V09 `27d6b5b5de073e0a8bf7c0e992ebce98832debb1e784e799003f801a9ecd1dcd` 12536
- V16 `9ba8e20793e14670562a0fdd99fccb209468684ac804e3e1c9733b731979e31a` 9444
- V23 `55e5662cfd44c56e248c6713a4b430c7fdccd9c3e05851aa9e67e559417a4ac4` 13227
- V36 `e95508f31b8062994fcc7a87643bbe50c06a64e206bae053ddd621a373a71431` 17056
- V42 `e00435d967129c5139c8dfa0daccc8930db777608d13a25c36549d6318be6e9c` 19228
- V45 `a8c4f6bb3181bf9de01078aebf067cd1ae91789f11070e007d9d982df5f512a2` 15866
- V55 `36117e1c989d262780f4b8314be7ecea0a9df5c44ca20638d7f73c6d2a66f8fb` 18827
- V58 `2ead2d908fb8e9c5138e30346c5c7d4b26f14ed9c74b9ff3a9b5c388fbf094dd` 16812
- V69 `7121e7a2800bdb6bdb02a222bb04abb32f48f96a1c819a145e5d1309694a9e91` 15401
- V78 `fcc86f9e0eacf043ffef8fa037bbc3bc22b6011d8cfcb47566753c87b85d03cc` 15544
- V79 `47b7199d9a9d786729c2c2da899005ef2e0a550a8327594847bf9bc4b5de15db` 11655
- V85 `87b85e6689a7d1a264e2209416d5451776d2762e134dad5dbcbb1e61454a6be2` 6714
- V99 `6f7909c266f05c096958fc4bb61825e210090181acec850e21abcb82a9f14794` 33837
- V100 `41264099d7cf0af686af36192cd3f28874f012df02d68f52a5ca7b728c0b6491` 13886
- V104 `fc751aa296cdc1fefcc673176ff83d787674fa6c8b3f925ec1d4d538d992b0c4` 7352
- V110 `180f6b666ffda97dfe52c7cc4cf9811f01af077e1514484889d0eb68a3668b38` 11722
- V117 `e59afdd7ff79d23613dc62bc8cd1e8f9e82bff21f3b6e2207136f915e23a2e99` 19426
- V118 `458eca6fb4c7495238d9491e19e53fe6fa62b8a3cc6b1763aa4ec7c94044782e` 21030
- V120 `c9ce42b1994b7ac7760f673586af4050f4ceeaa4153cb6a1cdcb8d23e1304105` 16212 (same-second write; possibly in-flight)
- V121 `79ed0797b8b80092c3107b842acb8387fa7c4aeafb56809e427c8b411ab8ad61` 7466

V23, V36, and V79 changed again between the 23:03 pass and 23:10:24. The lines above are the later read.

## 5. What this seat did not do

Did not edit V39's report, `receipt.json`, or any corpus file. Did not treat the 22:22 scratch audit as the receipt. Did not judge C1 or C2. Did not invent agent ids. The 23:10:24 delta is not a replacement receipt; V39 said the skeleton would not chase later landings, and that choice is recorded rather than silently overwritten here.

**Bottom line:** PASS — sealed 22:51:41 receipt counts check (128 = 85 present + 43 absent, no missed pre-snapshot file) and every still-stable hash matches, including all 15 quoted 22:22 hashes and V39's own re-pin; FLAG post-seal drift and correct it (26 later reports, 7 rewritten report hashes, README `837a7f5d…`, both knowledge files present) as of 23:10:24, not as a snapshot arithmetic error.
