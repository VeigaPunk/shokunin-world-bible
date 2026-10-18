# V99 — receipt-3 (round 99)

**Seat:** V99 `receipt-3`. **Role:** independent receipt builder. Construct a 128-seat table from disk and compare it 1:1 against V39's receipt. Report drift. This seat judges no C1/C2 claim and no axis.

**Axes for this seat:** independence (table hashed from disk, not copied from V39), completeness (declared roster S1–S5 + V01–V123 = 128), fidelity (path, presence, sha256), honesty (post-snapshot landings are not rewritten into V39 errors), protocol (40×20 s poll, SELF subtracted, late landing recorded).

**Lane root:** `/home/vgpnk/Projects/shokunin/lore-shokunin`. **Baseline:** `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). **HEAD:** `337f0fa52b02626b7687eedbb2d99fab30446fe4`. Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report and `seats/V99-scratch/` only. V39 owns `receipt.json`.

## 1. Poll — receipt.json absent at the bound

Poll started 2026-10-17T22:20:19-0300. Cadence 20 s, max 40. Expected others = 127 (ENDGAME subtracts SELF). Required before a same-window compare: producer reports S1–S5, the declared artifact paths, `V39-receipt.md`, and `.ufo/waves/round-99/receipt.json`. That conjunction never fired.

```
POLL_START 2026-10-17T22:20:19-0300 max=40 sleep=20 self=V99
STATUS try=1 2026-10-17T22:20:19-0300 producers_missing=3 artifacts_missing=2 receipt=False v39_md=False top_md=14
PRODUCER_MISSING S1-full-file-pins.md S2-tools-docs.md S5-knowledge-author.md
ARTIFACT_MISSING corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md
STATUS try=40 2026-10-17T22:33:19-0300 producers_missing=3 artifacts_missing=2 receipt=False v39_md=True top_md=40
EXHAUSTED 2026-10-17T22:33:19-0300
BUILD reason=exhausted-after-40 present=40 excluding_self=40 missing_others=87 drifts=1 receipt=False v39_md=True
```

The single drift at exhaustion was `receipt_absent` on `.ufo/waves/round-99/receipt.json`. `V39-receipt.md` had landed at try 32 (11188 bytes, mtime 22:30). No stall-escape: the receipt file was not there to compare. Full log: `seats/V99-scratch/poll.log`.

Re-check two minutes after the bound, still absent:

```
$ date -Iseconds
2026-10-17T22:35:33-03:00
$ ls -l .ufo/waves/round-99/receipt.json .ufo/waves/round-99/seats/V39-receipt.md
ls: cannot access '.ufo/waves/round-99/receipt.json': No such file or directory
-rw-r--r-- 1 vgpnk vgpnk 11188 Oct 17 22:30 .ufo/waves/round-99/seats/V39-receipt.md
```

At that instant V39's markdown (sha later recorded as `acee8ae147c65f11bf2e84c31c42735ca0ce20a458ac3337ca3af4cf21753525`) already said the skeleton `receipt.json` had been written. The file was not on disk. That prose claim was false at 22:35:33.

## 2. What landed after the bound

V39 later corrected section 5 (current `V39-receipt.md` mtime 22:50:06, sha `d41012346169db4d3ad09420858f5c97248080cb8900b2a3ba22db5f499d47f3`) and disclosed the delay: first JSON write at 2026-10-17T22:37:23-0300, preserved at `seats/V39-scratch/receipt-223723.json`, then superseded.

This seat hashed the live file at 22:49:55 while it was still the first write:

```
receipt_bytes 50183
receipt_mtime 2026-10-17T22:37:23-0300
receipt_sha256 5d74851756c407864643281eb3b738d5a0fad00ea3052a1d39a615a0ddc205c7
seats 128
agent_id_values {None}
outcome_values {None}
collection.reports_present=46
```

A 1:1 pass against that first JSON (compare time ~22:51, before the rewrite) found 85 disk-present reports, 46 V39-present, 43 drifts, **0** of them on a file older than the receipt. Every drift had `file_newer_than_receipt: true`. That first JSON is no longer the live receipt. Its preserved bytes match: scratch copy sha `5d74851756c407864643281eb3b738d5a0fad00ea3052a1d39a615a0ddc205c7`.

The live receipt was rewritten at 22:51:41 (67825 bytes, snapshot field `2026-10-17T22:51:41-0300`, 85 present). That is the file compared below. It was stable across an 8 s re-hash (`7b0b5ef2…` both times).

## 3. Frozen compare of the live receipt

Commands at the compare instant (lane root):

```
$ date '+%Y-%m-%dT%H:%M:%S%z'
2026-10-17T23:02:47-0300
exit 0

$ git rev-parse HEAD
337f0fa52b02626b7687eedbb2d99fab30446fe4
exit 0

$ git rev-parse 4265df5
4265df5e86e4121bde4125b649b89bb1676676a5
exit 0

$ git merge-base --is-ancestor 4265df5 HEAD && echo baseline_is_ancestor=yes || echo baseline_is_ancestor=no
baseline_is_ancestor=yes
exit 0

$ sha256sum .ufo/waves/round-99/receipt.json .ufo/waves/round-99/seats/V39-receipt.md .ufo/waves/round-99/seats/V39-scratch/receipt-223723.json
7b0b5ef2b7308449469923e6286f98e45147d632dcb33b89b90a79c9e1304038  .ufo/waves/round-99/receipt.json
d41012346169db4d3ad09420858f5c97248080cb8900b2a3ba22db5f499d47f3  .ufo/waves/round-99/seats/V39-receipt.md
5d74851756c407864643281eb3b738d5a0fad00ea3052a1d39a615a0ddc205c7  .ufo/waves/round-99/seats/V39-scratch/receipt-223723.json
exit 0

$ stat -c '%y %s %n' .ufo/waves/round-99/receipt.json .ufo/waves/round-99/seats/V39-receipt.md .ufo/waves/round-99/seats/V39-scratch/receipt-223723.json
2026-10-17 22:51:41.181551683 -0300 67825 .ufo/waves/round-99/receipt.json
2026-10-17 22:50:06.991445111 -0300 11442 .ufo/waves/round-99/seats/V39-receipt.md
2026-10-17 22:51:41.136144754 -0300 50183 .ufo/waves/round-99/seats/V39-scratch/receipt-223723.json
exit 0

$ find .ufo/waves/round-99/seats -maxdepth 1 -name '*.md' | wc -l
97
exit 0

$ find .ufo/waves/round-99/seats -maxdepth 1 -name 'S*.md' -printf '%f\n'
S3-fixture-author.md
S4-fixture-docs.md
S1-full-file-pins.md
exit 0

$ ls -l corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md 2>&1 || true
-rw-r--r-- 1 vgpnk vgpnk 20526 Oct 17 22:57 corpus/knowledge/r99-gate-blind-spot-table.md
-rw-r--r-- 1 vgpnk vgpnk 14990 Oct 17 22:57 corpus/knowledge/r99-lapse-scope-note.md
exit 0

$ find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l
173
exit 0
```

Independent table: one row per declared roster seat. Presence = the declared top-level `seats/<SEAT>-*.md` exists. sha256 is of that file's bytes at 23:02:47. Scratch directories are not reports. SELF (`V99`) was absent; this file did not exist yet.

Classification against `receipt.json` sha `7b0b5ef2b7308449469923e6286f98e45147d632dcb33b89b90a79c9e1304038`:

| class | count | rule |
|---|---:|---|
| AGREE | 112 | both absent, or both present and sha256 equal, and the file's mtime is not after the receipt |
| POST-SNAPSHOT | 16 | disk disagrees, and the file mtime is after 22:51:41 |
| DEFECT | 0 | disagree, and the file is not newer than the receipt (missed file, or hash of bytes V39 should have seen) |
| AMBIGUOUS | 0 | mtime within 1 s of the receipt and hash disagrees |

Of the 112 agreements: 81 both present and hash-equal, 31 both absent. Receipt `seats[]` length 128, same ids as the roster, no extras, no missing ids. `collection.present` (85) equals the seats with `report_status=present`. `collection.reports_expected=128`, `collection.reports_present=85`. Every `agent_id` is null. Every `outcome` is null. Duplicate report prefixes: none. Header/seat mismatch (first line starts with `# <seat>`): none. Unexpected top-level `.md`: none.

The 15-row table in `V39-receipt.md` section 3 (22:22:17 audit) matches both the live receipt's sha256 for those seats and the bytes still on disk (`md_vs_json` empty, `md_vs_disk` empty). Files present in this seat's 22:32:51 opening hash snapshot are all present in the live receipt (`opening_miss` empty).

`collection.producer_absent` is `["S2", "S5"]`. Disk agrees: `S1-full-file-pins.md` is present and hash-equal (`1fda9ff7f02e75c9b34d0f0e514cbc8f799f596bb0cedc2d363fd6f33aee54a3`); S2 and S5 reports are absent. `missing_candidate_paths` still lists both knowledge files. Those files exist now, mtime 22:57, which is after the 22:51:41 snapshot. That is receipt-field staleness from a later landing, not a seat-table defect, and it is not a C1/C2 verdict.

## 4. Post-snapshot drift (not charged as V39 hash errors)

These 16 rows differ from the live receipt. Each file's mtime is after `receipt_snapshot_utc`. V39's snapshot cannot contain bytes written later. Four are rewrites of files V39 had hashed; twelve are reports that did not exist at 22:51:41.

- `V03` v39=absent disk_mtime=2026-10-17T23:02:23-0300 disk_sha=cb24666587fdc30708639b8fa8afd9cfdc14c7e534238ec8d284da6f000b8796 v39_sha= (presence disk=True v39=absent)
- `V05` v39=absent disk_mtime=2026-10-17T22:56:23-0300 disk_sha=366425b9145529ecf379c6c26276611b15fe55ea41398ca5fa9a8e18ac456440 v39_sha= (presence disk=True v39=absent)
- `V23` v39=absent disk_mtime=2026-10-17T22:55:22-0300 disk_sha=a4d71ecad2a998cbf4989bd85647a11c012de4417dda022e0cba1c991a68c9f9 v39_sha= (presence disk=True v39=absent)
- `V36` v39=absent disk_mtime=2026-10-17T23:00:15-0300 disk_sha=5d87eb5152cb9e36fbce390d6b6431502651142c190e2c8179fe055e0ae28931 v39_sha= (presence disk=True v39=absent)
- `V40` v39=present disk_mtime=2026-10-17T22:53:00-0300 disk_sha=f5f733acaf4c248e3d46f1dba296aa4b5a37442171eef009a9eb5ba83f052fd8 v39_sha=08561fffc3f5c13a9b4868f304523f4de20518105472d8058d35243467cca85f (sha disk=f5f733acaf4c248e3d46f1dba296aa4b5a37442171eef009a9eb5ba83f052fd8 v39=08561fffc3f5c13a9b4868f304523f4de20518105472d8058d35243467cca85f)
- `V45` v39=absent disk_mtime=2026-10-17T22:59:43-0300 disk_sha=a8c4f6bb3181bf9de01078aebf067cd1ae91789f11070e007d9d982df5f512a2 v39_sha= (presence disk=True v39=absent)
- `V48` v39=present disk_mtime=2026-10-17T22:54:48-0300 disk_sha=9e29c40d8cd6d5b9f14b9704e56c97a09291db3f948535a40afbbbd08ddf94b0 v39_sha=d814ff16df17d7b8316e1224accdb88cfdf068444e803dc736a3566f6f623461 (sha disk=9e29c40d8cd6d5b9f14b9704e56c97a09291db3f948535a40afbbbd08ddf94b0 v39=d814ff16df17d7b8316e1224accdb88cfdf068444e803dc736a3566f6f623461)
- `V51` v39=present disk_mtime=2026-10-17T22:59:04-0300 disk_sha=72437b1c05884bfcb3f2fe0f3fee86a09321c85966cac18202487de8703410e2 v39_sha=dc034db60cbfff474b796f61e96870ee8e30a856962a69e00d52ba8709f7adaf (sha disk=72437b1c05884bfcb3f2fe0f3fee86a09321c85966cac18202487de8703410e2 v39=dc034db60cbfff474b796f61e96870ee8e30a856962a69e00d52ba8709f7adaf)
- `V58` v39=absent disk_mtime=2026-10-17T22:58:44-0300 disk_sha=3e16b8f6da5c2ac6750c9cd1da067327aa233d8dfe322dd150d5dbfe4cc1d651 v39_sha= (presence disk=True v39=absent)
- `V78` v39=absent disk_mtime=2026-10-17T23:02:21-0300 disk_sha=fcc86f9e0eacf043ffef8fa037bbc3bc22b6011d8cfcb47566753c87b85d03cc v39_sha= (presence disk=True v39=absent)
- `V79` v39=absent disk_mtime=2026-10-17T22:59:30-0300 disk_sha=35b83e6cd080b66cb7ec69b0f3c0e8a6da6107fa1bd43280862819d6f3bec64d v39_sha= (presence disk=True v39=absent)
- `V85` v39=absent disk_mtime=2026-10-17T22:56:23-0300 disk_sha=87b85e6689a7d1a264e2209416d5451776d2762e134dad5dbcbb1e61454a6be2 v39_sha= (presence disk=True v39=absent)
- `V100` v39=absent disk_mtime=2026-10-17T22:58:13-0300 disk_sha=41264099d7cf0af686af36192cd3f28874f012df02d68f52a5ca7b728c0b6491 v39_sha= (presence disk=True v39=absent)
- `V104` v39=absent disk_mtime=2026-10-17T23:01:36-0300 disk_sha=fc751aa296cdc1fefcc673176ff83d787674fa6c8b3f925ec1d4d538d992b0c4 v39_sha= (presence disk=True v39=absent)
- `V110` v39=absent disk_mtime=2026-10-17T23:01:36-0300 disk_sha=180f6b666ffda97dfe52c7cc4cf9811f01af077e1514484889d0eb68a3668b38 v39_sha= (presence disk=True v39=absent)
- `V123` v39=present disk_mtime=2026-10-17T22:59:00-0300 disk_sha=53afbdff7794996d7ee8635cfa7942e002967c0764220b11935fe27f7c1e0815 v39_sha=9b7cdf7e8d1e965266ecbc196b90737b7c39c268c0308d07539cbf0e3e7c4e07 (sha disk=53afbdff7794996d7ee8635cfa7942e002967c0764220b11935fe27f7c1e0815 v39=9b7cdf7e8d1e965266ecbc196b90737b7c39c268c0308d07539cbf0e3e7c4e07)

`V40`, `V48`, `V51`, and `V123` are sha mismatches on files V39 marked present. Their disk mtimes (22:53:00, 22:54:48, 22:59:04, 22:59:00) are after 22:51:41, so the receipt hash is the earlier bytes. This seat does not have those earlier bytes for these four, and does not call the receipt hash wrong.

## 5. Prose lag inside V39's own report (not a seat-table defect)

`V39-receipt.md` section 5 now says the JSON is the later observation and that the markdown is not rewritten to chase landings. The markdown bottom line still says "15 other reports hashed at the 22:22:17 audit" and "S1, S2, S5 reports … ABSENT". The live receipt has S1 present and 85 reports present. That is a wording lag V39 disclosed, not a sha256 disagreement on a stable file.

The 22:30 markdown's claim that `receipt.json` was already written was false at 22:35:33. The 22:50 correction admits the first write was 22:37:23. Current disk matches that correction: the preserved first JSON exists, and the live file is the 22:51:41 rewrite.

## 6. Seat table (frozen 2026-10-17T23:02:47-0300)

Full hashes for the 128 declared seats. `disk_sha256` is this seat's hash. `v39_sha256` is `receipt.json` `seats[].report_sha256`. Empty means absent on that side.

| seat | class | disk | v39 | disk_sha256 | v39_sha256 | disk_mtime |
|---|---|---|---|---|---|---|
| S1 | AGREE | present | present | 1fda9ff7f02e75c9b34d0f0e514cbc8f799f596bb0cedc2d363fd6f33aee54a3 | 1fda9ff7f02e75c9b34d0f0e514cbc8f799f596bb0cedc2d363fd6f33aee54a3 | 2026-10-17T22:48:57-0300 |
| S2 | AGREE | absent | absent |  |  |  |
| S3 | AGREE | present | present | 3d81a75e0f154ed6c2297da8a9521391797a81740e0ede5443070b0c471cf73a | 3d81a75e0f154ed6c2297da8a9521391797a81740e0ede5443070b0c471cf73a | 2026-10-17T22:01:40-0300 |
| S4 | AGREE | present | present | 61bfdec1f5b7bbcdda653230bb4be1b6c1913683af67e2ae02e4ee46a327f72f | 61bfdec1f5b7bbcdda653230bb4be1b6c1913683af67e2ae02e4ee46a327f72f | 2026-10-17T22:03:54-0300 |
| S5 | AGREE | absent | absent |  |  |  |
| V01 | AGREE | absent | absent |  |  |  |
| V02 | AGREE | absent | absent |  |  |  |
| V03 | POST-SNAPSHOT | present | absent | cb24666587fdc30708639b8fa8afd9cfdc14c7e534238ec8d284da6f000b8796 |  | 2026-10-17T23:02:23-0300 |
| V04 | AGREE | absent | absent |  |  |  |
| V05 | POST-SNAPSHOT | present | absent | 366425b9145529ecf379c6c26276611b15fe55ea41398ca5fa9a8e18ac456440 |  | 2026-10-17T22:56:23-0300 |
| V06 | AGREE | present | present | c1a6cc2b2298275fdb9fa473fc2ccfeb5bef24c0a34da098654fa97035a414a5 | c1a6cc2b2298275fdb9fa473fc2ccfeb5bef24c0a34da098654fa97035a414a5 | 2026-10-17T22:36:13-0300 |
| V07 | AGREE | present | present | e489f74e4bdb931e18c6121bbbb6573978d4af501902235d960769881a44fb0d | e489f74e4bdb931e18c6121bbbb6573978d4af501902235d960769881a44fb0d | 2026-10-17T22:33:01-0300 |
| V08 | AGREE | absent | absent |  |  |  |
| V09 | AGREE | absent | absent |  |  |  |
| V10 | AGREE | present | present | 9ee8c876b7ff1be1481c7219b06307163ed5a0553ef168bdda23e677f99f7f45 | 9ee8c876b7ff1be1481c7219b06307163ed5a0553ef168bdda23e677f99f7f45 | 2026-10-17T22:04:39-0300 |
| V11 | AGREE | present | present | a2f60b65b440efd0b178c5c314fc51ded510e8b8bd80db3c0ce6fd87b2d20e03 | a2f60b65b440efd0b178c5c314fc51ded510e8b8bd80db3c0ce6fd87b2d20e03 | 2026-10-17T22:11:54-0300 |
| V12 | AGREE | present | present | b559cdb76adbebc6791e3b784d92188437f4195a828120ac9c9b522028fc9246 | b559cdb76adbebc6791e3b784d92188437f4195a828120ac9c9b522028fc9246 | 2026-10-17T22:21:50-0300 |
| V13 | AGREE | present | present | a7ef2d47c29e97cfe41f93800f0fc1a24ca6ad6a636734f4517300d70c2778dd | a7ef2d47c29e97cfe41f93800f0fc1a24ca6ad6a636734f4517300d70c2778dd | 2026-10-17T22:05:32-0300 |
| V14 | AGREE | present | present | abb85e5253be270b26cf80c0e340fadacb3b069e5a9e2a28c2409109060b0e25 | abb85e5253be270b26cf80c0e340fadacb3b069e5a9e2a28c2409109060b0e25 | 2026-10-17T22:31:38-0300 |
| V15 | AGREE | present | present | ae3a8aaf227ea8d109c11af29a34b86864829c321c8c25524aabc38d8adfffb3 | ae3a8aaf227ea8d109c11af29a34b86864829c321c8c25524aabc38d8adfffb3 | 2026-10-17T22:46:05-0300 |
| V16 | AGREE | absent | absent |  |  |  |
| V17 | AGREE | present | present | 3ce0c56f46d7981c0c1f8f48c41c53f10bcbc12f8c06946a5a24581cffb5ca08 | 3ce0c56f46d7981c0c1f8f48c41c53f10bcbc12f8c06946a5a24581cffb5ca08 | 2026-10-17T22:37:38-0300 |
| V18 | AGREE | present | present | e562493941c02b28b2c3f5bfd897dffe8dc51d3476f9cb0e06b50d21633fea31 | e562493941c02b28b2c3f5bfd897dffe8dc51d3476f9cb0e06b50d21633fea31 | 2026-10-17T22:32:00-0300 |
| V19 | AGREE | present | present | 64cd0a9caab45b9d3b8e569e80b535925e835168b26c6e57c1b9b47b633dbc38 | 64cd0a9caab45b9d3b8e569e80b535925e835168b26c6e57c1b9b47b633dbc38 | 2026-10-17T22:36:48-0300 |
| V20 | AGREE | present | present | 506482b1484cec085467fdf59b2929bc300b0a46328b1c2f962566c7fb0d33d0 | 506482b1484cec085467fdf59b2929bc300b0a46328b1c2f962566c7fb0d33d0 | 2026-10-17T22:42:32-0300 |
| V21 | AGREE | present | present | 2b61809b282dc60385272f2b858fbff5a65b7b619b45ae7f8bc5446c4b699362 | 2b61809b282dc60385272f2b858fbff5a65b7b619b45ae7f8bc5446c4b699362 | 2026-10-17T22:38:02-0300 |
| V22 | AGREE | present | present | 9d049d6103e382e08e055b87fcbfe57c94dbf3aba16a027bad9fbad7510f4e2a | 9d049d6103e382e08e055b87fcbfe57c94dbf3aba16a027bad9fbad7510f4e2a | 2026-10-17T22:41:56-0300 |
| V23 | POST-SNAPSHOT | present | absent | a4d71ecad2a998cbf4989bd85647a11c012de4417dda022e0cba1c991a68c9f9 |  | 2026-10-17T22:55:22-0300 |
| V24 | AGREE | present | present | f9ea2e1abcfc810f660e892008e0c1afebe7b291cae0bf108909e4d9895983ef | f9ea2e1abcfc810f660e892008e0c1afebe7b291cae0bf108909e4d9895983ef | 2026-10-17T22:47:33-0300 |
| V25 | AGREE | present | present | 1749c2cffd2e911ada45ef3f90638e86ab75379d43ef106a6514772c0d5ac596 | 1749c2cffd2e911ada45ef3f90638e86ab75379d43ef106a6514772c0d5ac596 | 2026-10-17T22:39:44-0300 |
| V26 | AGREE | present | present | 51fe5d09917edf37af5600a61beaab44e623994f72f4ba54dc7d6fa3e660eb9b | 51fe5d09917edf37af5600a61beaab44e623994f72f4ba54dc7d6fa3e660eb9b | 2026-10-17T22:35:35-0300 |
| V27 | AGREE | present | present | 61c956cfcd879521cf8b034f9d4c2d1e882021e88d35d876edcfd7d3d10cc42e | 61c956cfcd879521cf8b034f9d4c2d1e882021e88d35d876edcfd7d3d10cc42e | 2026-10-17T22:38:08-0300 |
| V28 | AGREE | present | present | 84058e09fb813032d715897f43f808078d95badce05ddfe3a5640dba2451a344 | 84058e09fb813032d715897f43f808078d95badce05ddfe3a5640dba2451a344 | 2026-10-17T22:50:40-0300 |
| V29 | AGREE | present | present | 1f8eb8316b844dd64cd832561976dfddbd98c2674778a2d2fef8d5eb156b5e1e | 1f8eb8316b844dd64cd832561976dfddbd98c2674778a2d2fef8d5eb156b5e1e | 2026-10-17T22:33:40-0300 |
| V30 | AGREE | absent | absent |  |  |  |
| V31 | AGREE | present | present | b7b19a4b7dc226983e63b226274598e48836ac7ebd7152b5f3f8c8e15e87991d | b7b19a4b7dc226983e63b226274598e48836ac7ebd7152b5f3f8c8e15e87991d | 2026-10-17T22:51:03-0300 |
| V32 | AGREE | present | present | e94a49e63825fcdeaad4561b45dec05d8676b255317dbe3008e778ca098ad711 | e94a49e63825fcdeaad4561b45dec05d8676b255317dbe3008e778ca098ad711 | 2026-10-17T22:32:25-0300 |
| V33 | AGREE | present | present | 61ba3ac0f6f3aced04ff5d3764086f7136cb7869ccd5ab24a25b512ec9448138 | 61ba3ac0f6f3aced04ff5d3764086f7136cb7869ccd5ab24a25b512ec9448138 | 2026-10-17T22:27:58-0300 |
| V34 | AGREE | absent | absent |  |  |  |
| V35 | AGREE | present | present | 96a7e622dd230570bc21d799600ccf29641f2e6bbd7cd63cff74dbddfd284580 | 96a7e622dd230570bc21d799600ccf29641f2e6bbd7cd63cff74dbddfd284580 | 2026-10-17T22:43:11-0300 |
| V36 | POST-SNAPSHOT | present | absent | 5d87eb5152cb9e36fbce390d6b6431502651142c190e2c8179fe055e0ae28931 |  | 2026-10-17T23:00:15-0300 |
| V37 | AGREE | absent | absent |  |  |  |
| V38 | AGREE | absent | absent |  |  |  |
| V39 | AGREE | present | present | d41012346169db4d3ad09420858f5c97248080cb8900b2a3ba22db5f499d47f3 | d41012346169db4d3ad09420858f5c97248080cb8900b2a3ba22db5f499d47f3 | 2026-10-17T22:50:06-0300 |
| V40 | POST-SNAPSHOT | present | present | f5f733acaf4c248e3d46f1dba296aa4b5a37442171eef009a9eb5ba83f052fd8 | 08561fffc3f5c13a9b4868f304523f4de20518105472d8058d35243467cca85f | 2026-10-17T22:53:00-0300 |
| V41 | AGREE | present | present | 40af4141891fe1d0a91017080d5ce232e2e252743811ec61dc8c751e984ea0d6 | 40af4141891fe1d0a91017080d5ce232e2e252743811ec61dc8c751e984ea0d6 | 2026-10-17T22:17:06-0300 |
| V42 | AGREE | absent | absent |  |  |  |
| V43 | AGREE | absent | absent |  |  |  |
| V44 | AGREE | present | present | 926689d83fd6b6ae25302178eae39c6112aff19d5be7ecea9820eb2a1afb5a7d | 926689d83fd6b6ae25302178eae39c6112aff19d5be7ecea9820eb2a1afb5a7d | 2026-10-17T22:31:21-0300 |
| V45 | POST-SNAPSHOT | present | absent | a8c4f6bb3181bf9de01078aebf067cd1ae91789f11070e007d9d982df5f512a2 |  | 2026-10-17T22:59:43-0300 |
| V46 | AGREE | present | present | 6442e5ce7f3fc3ace785985467fd03449e492079fe30d2ce2f5cb280f26b2957 | 6442e5ce7f3fc3ace785985467fd03449e492079fe30d2ce2f5cb280f26b2957 | 2026-10-17T22:40:40-0300 |
| V47 | AGREE | present | present | 321491fb9b0757f867b5e0cc45338bc106960908f64eb3b8c37aed47ab8c5410 | 321491fb9b0757f867b5e0cc45338bc106960908f64eb3b8c37aed47ab8c5410 | 2026-10-17T22:15:20-0300 |
| V48 | POST-SNAPSHOT | present | present | 9e29c40d8cd6d5b9f14b9704e56c97a09291db3f948535a40afbbbd08ddf94b0 | d814ff16df17d7b8316e1224accdb88cfdf068444e803dc736a3566f6f623461 | 2026-10-17T22:54:48-0300 |
| V49 | AGREE | present | present | 93e523516f99e96143bf2549ded5dc1e6129579801bb99cf5ef488fdb67a8530 | 93e523516f99e96143bf2549ded5dc1e6129579801bb99cf5ef488fdb67a8530 | 2026-10-17T22:39:20-0300 |
| V50 | AGREE | absent | absent |  |  |  |
| V51 | POST-SNAPSHOT | present | present | 72437b1c05884bfcb3f2fe0f3fee86a09321c85966cac18202487de8703410e2 | dc034db60cbfff474b796f61e96870ee8e30a856962a69e00d52ba8709f7adaf | 2026-10-17T22:59:04-0300 |
| V52 | AGREE | present | present | d4253addd96a9b99faa0fa702292696d08844ea70b8a4f3fd5f254dad2950073 | d4253addd96a9b99faa0fa702292696d08844ea70b8a4f3fd5f254dad2950073 | 2026-10-17T22:37:55-0300 |
| V53 | AGREE | absent | absent |  |  |  |
| V54 | AGREE | absent | absent |  |  |  |
| V55 | AGREE | absent | absent |  |  |  |
| V56 | AGREE | present | present | 32ad2bd635d605f2f67ea5ba27172b8f5c4ef63953abc06fe4ba58f31234ad0b | 32ad2bd635d605f2f67ea5ba27172b8f5c4ef63953abc06fe4ba58f31234ad0b | 2026-10-17T22:30:09-0300 |
| V57 | AGREE | present | present | ed26bba57f0e0f78ad5754313331eaef56f433f2f1f7c6f245107b56cad4391c | ed26bba57f0e0f78ad5754313331eaef56f433f2f1f7c6f245107b56cad4391c | 2026-10-17T22:47:51-0300 |
| V58 | POST-SNAPSHOT | present | absent | 3e16b8f6da5c2ac6750c9cd1da067327aa233d8dfe322dd150d5dbfe4cc1d651 |  | 2026-10-17T22:58:44-0300 |
| V59 | AGREE | present | present | 081654f0717731d0bca720e177965233689428bf4503dab0cf60b2590b7ea49c | 081654f0717731d0bca720e177965233689428bf4503dab0cf60b2590b7ea49c | 2026-10-17T22:46:16-0300 |
| V60 | AGREE | present | present | 9340e8903b2bde4fb491dee5611840737e3bc9eafdd7b5f2484cb97e874715ef | 9340e8903b2bde4fb491dee5611840737e3bc9eafdd7b5f2484cb97e874715ef | 2026-10-17T22:41:21-0300 |
| V61 | AGREE | present | present | 7b1cc4c731035e3705c4bdb6eb84b313dfd492af710d836ec11c8edf1952042b | 7b1cc4c731035e3705c4bdb6eb84b313dfd492af710d836ec11c8edf1952042b | 2026-10-17T22:46:50-0300 |
| V62 | AGREE | present | present | cea35ca945d844d432f3521364127553174c4b67b3a53f09155ac218447d8f81 | cea35ca945d844d432f3521364127553174c4b67b3a53f09155ac218447d8f81 | 2026-10-17T22:38:28-0300 |
| V63 | AGREE | present | present | d7f9b865ee7eedf6a225b39e22c7509592e482157c77dec8b3c5790ac36900db | d7f9b865ee7eedf6a225b39e22c7509592e482157c77dec8b3c5790ac36900db | 2026-10-17T22:44:03-0300 |
| V64 | AGREE | present | present | cb40cb22e96aeafe00bb0a574558c7f09690f22932b697481c47b1baf6bd2e7c | cb40cb22e96aeafe00bb0a574558c7f09690f22932b697481c47b1baf6bd2e7c | 2026-10-17T22:32:20-0300 |
| V65 | AGREE | present | present | 66747998274bc01ead066ccf76de1d05155a125f05746c4312b2936dbcb90663 | 66747998274bc01ead066ccf76de1d05155a125f05746c4312b2936dbcb90663 | 2026-10-17T22:36:11-0300 |
| V66 | AGREE | present | present | 81847eb4a5661d42e241e7df47d35195bc465bf245a4bd79c21d5190e956706b | 81847eb4a5661d42e241e7df47d35195bc465bf245a4bd79c21d5190e956706b | 2026-10-17T22:50:52-0300 |
| V67 | AGREE | absent | absent |  |  |  |
| V68 | AGREE | present | present | d1ab2308693704bcb848559e051ede400414cac29807fe8a52f8a734b6d1ae97 | d1ab2308693704bcb848559e051ede400414cac29807fe8a52f8a734b6d1ae97 | 2026-10-17T22:03:15-0300 |
| V69 | AGREE | absent | absent |  |  |  |
| V70 | AGREE | present | present | 443f75094fca12234c9691f9ef4aef29a509f948927293ccd6b0b081ca46aaf5 | 443f75094fca12234c9691f9ef4aef29a509f948927293ccd6b0b081ca46aaf5 | 2026-10-17T22:43:41-0300 |
| V71 | AGREE | absent | absent |  |  |  |
| V72 | AGREE | absent | absent |  |  |  |
| V73 | AGREE | present | present | c2dabac28dcf06d72c4b110317d07ee35e66988517ffff4c97d8e35eeab88130 | c2dabac28dcf06d72c4b110317d07ee35e66988517ffff4c97d8e35eeab88130 | 2026-10-17T22:51:10-0300 |
| V74 | AGREE | absent | absent |  |  |  |
| V75 | AGREE | absent | absent |  |  |  |
| V76 | AGREE | present | present | 61e793b24ed1139317ec3e320c28068882365918265a5435411e458b68369b7f | 61e793b24ed1139317ec3e320c28068882365918265a5435411e458b68369b7f | 2026-10-17T22:37:32-0300 |
| V77 | AGREE | present | present | e51103276a7db11c4a5c9ed188ec396c34962d320efd1910f0cbea151c8ce7f1 | e51103276a7db11c4a5c9ed188ec396c34962d320efd1910f0cbea151c8ce7f1 | 2026-10-17T22:10:52-0300 |
| V78 | POST-SNAPSHOT | present | absent | fcc86f9e0eacf043ffef8fa037bbc3bc22b6011d8cfcb47566753c87b85d03cc |  | 2026-10-17T23:02:21-0300 |
| V79 | POST-SNAPSHOT | present | absent | 35b83e6cd080b66cb7ec69b0f3c0e8a6da6107fa1bd43280862819d6f3bec64d |  | 2026-10-17T22:59:30-0300 |
| V80 | AGREE | present | present | aaf5b0d1c47b44478bcac40af92c81bb2bce1025d41add69e1494283b08d2cee | aaf5b0d1c47b44478bcac40af92c81bb2bce1025d41add69e1494283b08d2cee | 2026-10-17T22:02:52-0300 |
| V81 | AGREE | present | present | dc5c377ecd8ea067e76dcb0ff587882f241b7baa313183f82e95bc040c2289a8 | dc5c377ecd8ea067e76dcb0ff587882f241b7baa313183f82e95bc040c2289a8 | 2026-10-17T22:46:38-0300 |
| V82 | AGREE | present | present | 00eb1b0984dcf9490ce07f8de3ef1eed79901c9cb9c52fe1ee75ba4ce9d7fa39 | 00eb1b0984dcf9490ce07f8de3ef1eed79901c9cb9c52fe1ee75ba4ce9d7fa39 | 2026-10-17T22:41:53-0300 |
| V83 | AGREE | present | present | b980f8d8ac33757a6e4bfd6ba8084fdabcabcd816a3b89a321e1f5ddda949def | b980f8d8ac33757a6e4bfd6ba8084fdabcabcd816a3b89a321e1f5ddda949def | 2026-10-17T22:46:36-0300 |
| V84 | AGREE | present | present | 4ae504003ddd528831a7c2ba77d3d10d426e9f7d731950017fd712da12d8eade | 4ae504003ddd528831a7c2ba77d3d10d426e9f7d731950017fd712da12d8eade | 2026-10-17T22:32:49-0300 |
| V85 | POST-SNAPSHOT | present | absent | 87b85e6689a7d1a264e2209416d5451776d2762e134dad5dbcbb1e61454a6be2 |  | 2026-10-17T22:56:23-0300 |
| V86 | AGREE | present | present | 775bd16a31f906bc3cc2f4a14139504598ddd9c907725e4e864412d258b0a38f | 775bd16a31f906bc3cc2f4a14139504598ddd9c907725e4e864412d258b0a38f | 2026-10-17T22:12:15-0300 |
| V87 | AGREE | present | present | bb4c2e2ece01c90508a76736767b5d5eb5de875df4bd032230f54c3c4ee4f86b | bb4c2e2ece01c90508a76736767b5d5eb5de875df4bd032230f54c3c4ee4f86b | 2026-10-17T22:46:10-0300 |
| V88 | AGREE | present | present | 490969f7794145b5ad08b300e65f3f64e57a45620941554f58c5f97a991b659c | 490969f7794145b5ad08b300e65f3f64e57a45620941554f58c5f97a991b659c | 2026-10-17T22:36:36-0300 |
| V89 | AGREE | present | present | e5ec213ce86452150708704c5cf12cd9fb24ab12499fcbaa29ad40ccc0443ae6 | e5ec213ce86452150708704c5cf12cd9fb24ab12499fcbaa29ad40ccc0443ae6 | 2026-10-17T22:32:54-0300 |
| V90 | AGREE | present | present | d454448ea3d7fe80132a62344f3a1df64e7fc1c67c53bfdd7721ade222147bfe | d454448ea3d7fe80132a62344f3a1df64e7fc1c67c53bfdd7721ade222147bfe | 2026-10-17T22:22:39-0300 |
| V91 | AGREE | present | present | ca0e4d2930bc29c4e1e9f88ef3ee0f8c418073a9c8725f60b30099a4e4674cd2 | ca0e4d2930bc29c4e1e9f88ef3ee0f8c418073a9c8725f60b30099a4e4674cd2 | 2026-10-17T22:47:03-0300 |
| V92 | AGREE | present | present | fd3a2cee038e911c1d873217eac144a2cf0713b24c38c87f4629ccbc6083ea57 | fd3a2cee038e911c1d873217eac144a2cf0713b24c38c87f4629ccbc6083ea57 | 2026-10-17T22:46:52-0300 |
| V93 | AGREE | present | present | be720d2a8b3550ce256805878bc2de18c224e2f92993e1df779a830c20140ff6 | be720d2a8b3550ce256805878bc2de18c224e2f92993e1df779a830c20140ff6 | 2026-10-17T22:37:33-0300 |
| V94 | AGREE | present | present | 2fe23cbb773962f93361ca343856559f124189affd7e52f5c59af6433480284f | 2fe23cbb773962f93361ca343856559f124189affd7e52f5c59af6433480284f | 2026-10-17T22:29:36-0300 |
| V95 | AGREE | present | present | ca217cff89d10a58caf40703e8f7a55e36064fc77e198c402e70daccc0b2a11e | ca217cff89d10a58caf40703e8f7a55e36064fc77e198c402e70daccc0b2a11e | 2026-10-17T22:24:23-0300 |
| V96 | AGREE | present | present | 0a980347c1e0f471a4bc7ec29101a28446f73cbfb304f8ce89dfa0831dd399a5 | 0a980347c1e0f471a4bc7ec29101a28446f73cbfb304f8ce89dfa0831dd399a5 | 2026-10-17T22:48:02-0300 |
| V97 | AGREE | present | present | 92eb427c8a196c8d71255feee50e8ab2c9082f04a2c60465827357ee9e8be5b7 | 92eb427c8a196c8d71255feee50e8ab2c9082f04a2c60465827357ee9e8be5b7 | 2026-10-17T22:32:55-0300 |
| V98 | AGREE | present | present | 4b47296c3afab19be1f0ad4477607f83bdcdd51aba8283a1021fac24bc16b53b | 4b47296c3afab19be1f0ad4477607f83bdcdd51aba8283a1021fac24bc16b53b | 2026-10-17T22:26:44-0300 |
| V99 | AGREE | absent | absent |  |  |  |
| V100 | POST-SNAPSHOT | present | absent | 41264099d7cf0af686af36192cd3f28874f012df02d68f52a5ca7b728c0b6491 |  | 2026-10-17T22:58:13-0300 |
| V101 | AGREE | absent | absent |  |  |  |
| V102 | AGREE | present | present | e7714246a1ac5ac897d708f0ebd3fe27e0bb255e57c54f9966d3681c5eef3422 | e7714246a1ac5ac897d708f0ebd3fe27e0bb255e57c54f9966d3681c5eef3422 | 2026-10-17T22:29:08-0300 |
| V103 | AGREE | present | present | c9f231b981a461381f72484cc5e51ca21f83a752876396d54b234a6142f6b33b | c9f231b981a461381f72484cc5e51ca21f83a752876396d54b234a6142f6b33b | 2026-10-17T22:40:13-0300 |
| V104 | POST-SNAPSHOT | present | absent | fc751aa296cdc1fefcc673176ff83d787674fa6c8b3f925ec1d4d538d992b0c4 |  | 2026-10-17T23:01:36-0300 |
| V105 | AGREE | present | present | 3668a34e84ee36a5ce2e3cdbffe9ce4eb34982f786b53f13013b0bcf39d0d1e2 | 3668a34e84ee36a5ce2e3cdbffe9ce4eb34982f786b53f13013b0bcf39d0d1e2 | 2026-10-17T22:11:49-0300 |
| V106 | AGREE | present | present | 57fbd7dfb4ad9ea7db2ef42a4b8bb67a1e739646d8fa9e0d9cde8e7b413eedd6 | 57fbd7dfb4ad9ea7db2ef42a4b8bb67a1e739646d8fa9e0d9cde8e7b413eedd6 | 2026-10-17T22:37:39-0300 |
| V107 | AGREE | absent | absent |  |  |  |
| V108 | AGREE | present | present | 9b686d6ef18f6a6ed4410178dbaa71004207074d3b1678ca3bb5dfddf35ab76b | 9b686d6ef18f6a6ed4410178dbaa71004207074d3b1678ca3bb5dfddf35ab76b | 2026-10-17T22:31:55-0300 |
| V109 | AGREE | present | present | 8bcbd46a1f5888cc99bb7a8e29947a6ae5a81e5455b917ac00d7c5e25495c362 | 8bcbd46a1f5888cc99bb7a8e29947a6ae5a81e5455b917ac00d7c5e25495c362 | 2026-10-17T22:14:24-0300 |
| V110 | POST-SNAPSHOT | present | absent | 180f6b666ffda97dfe52c7cc4cf9811f01af077e1514484889d0eb68a3668b38 |  | 2026-10-17T23:01:36-0300 |
| V111 | AGREE | present | present | 774aadfa62fbe3da4066e503c7b43697835a5129ab1b119af001dd78258ccddb | 774aadfa62fbe3da4066e503c7b43697835a5129ab1b119af001dd78258ccddb | 2026-10-17T22:39:15-0300 |
| V112 | AGREE | present | present | e84c22121fc6bfd55e7914d3c5de28c5c2c5669eeef2d6ab3885144aaaa31323 | e84c22121fc6bfd55e7914d3c5de28c5c2c5669eeef2d6ab3885144aaaa31323 | 2026-10-17T22:38:50-0300 |
| V113 | AGREE | present | present | b1e963422de1b54d3384c434a5aceb280c5c7231b670125909eb9a9866502101 | b1e963422de1b54d3384c434a5aceb280c5c7231b670125909eb9a9866502101 | 2026-10-17T22:22:48-0300 |
| V114 | AGREE | present | present | e0615f5ec440f1e45be8079c25e594631b242b3fcaecff1ebab4ec4cbbc553be | e0615f5ec440f1e45be8079c25e594631b242b3fcaecff1ebab4ec4cbbc553be | 2026-10-17T22:50:01-0300 |
| V115 | AGREE | present | present | 71fcd5048e1c357402210393f721105ef3a26670ce5b4439d424fa494bd431fa | 71fcd5048e1c357402210393f721105ef3a26670ce5b4439d424fa494bd431fa | 2026-10-17T22:32:53-0300 |
| V116 | AGREE | present | present | 0779931664e7fc0b8a4ca504c83f8b2aaea6228cc1c1cd8b71f813b798d9e737 | 0779931664e7fc0b8a4ca504c83f8b2aaea6228cc1c1cd8b71f813b798d9e737 | 2026-10-17T22:25:55-0300 |
| V117 | AGREE | absent | absent |  |  |  |
| V118 | AGREE | absent | absent |  |  |  |
| V119 | AGREE | present | present | 9206493b7fe5fb982f53756d2f1d260d91e6ce265d3c7c7f14277a82efc66b35 | 9206493b7fe5fb982f53756d2f1d260d91e6ce265d3c7c7f14277a82efc66b35 | 2026-10-17T22:11:01-0300 |
| V120 | AGREE | absent | absent |  |  |  |
| V121 | AGREE | absent | absent |  |  |  |
| V122 | AGREE | present | present | 1c402656a615eea28083415b3ae1915448f4c8965b1d492a21b62c914fcd5a54 | 1c402656a615eea28083415b3ae1915448f4c8965b1d492a21b62c914fcd5a54 | 2026-10-17T22:31:31-0300 |
| V123 | POST-SNAPSHOT | present | present | 53afbdff7794996d7ee8635cfa7942e002967c0764220b11935fe27f7c1e0815 | 9b7cdf7e8d1e965266ecbc196b90737b7c39c268c0308d07539cbf0e3e7c4e07 | 2026-10-17T22:59:00-0300 |

## 7. Honesty

This seat did not run C1 or C2 checks and does not treat the knowledge files' 22:57 mtimes as a delivery verdict. S2 and S5 reports were absent at the poll bound and were still absent at 23:02:47; the receipt records the same absence. Absent stays absent. No plan was verified in their place.

The wave was still landing reports during the compare (the 16 post-snapshot rows). A later rewrite of `receipt.json` after 23:02:47 would supersede this table; the sha compared is `7b0b5ef2b7308449469923e6286f98e45147d632dcb33b89b90a79c9e1304038`. This report does not quote its own sha256. `V99` was absent in both tables at the snapshot; writing this file is after that snapshot and is not a V39 miss.

**Bottom line:** PASS — 0 stable-file defects versus live `receipt.json` sha `7b0b5ef2b7308449469923e6286f98e45147d632dcb33b89b90a79c9e1304038` (snapshot 2026-10-17T22:51:41-0300): 112/128 AGREE, 16 post-snapshot drifts recorded and not charged as V39 hash errors; `receipt.json` was ABSENT at poll try 40 and was compared only after it landed.
