# V61 c1-payload-2 — independent recompute of the 60 full-file pin digests

Seat: V61. Exclusive write: this report, plus scratch under `.ufo/waves/round-99/seats/V61-scratch/`. No corpus edits, no commits, no network. Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Compared the on-disk contract, not a plan.

## Method (not the tool, not hashlib)

`corpus/tools/dependency_freeze.py` hashes with `hashlib.sha256` (`sha256_bytes`, then `content_digest` = SHA-256 of `json.dumps(file_digests, sort_keys=True, separators=(",", ":"))`). This seat did not import that module and did not call `hashlib`.

Primary implementation: FIPS 180-4 SHA-256 written in `V61-scratch/recompute_digests.py` (padding, message schedule, Ch/Maj, K constants). Cross-check 1: `openssl dgst -sha256` (OpenSSL 3.6.4) on the same raw bytes via stdin. Cross-check 2: `/usr/bin/sha256sum` on the fixture paths. V05's round-99 report was not present (`S1_AND_V05_REPORTS_ABSENT` at 22:41:20-0300), so this seat did not read or copy V05's method. The three implementations here are all outside `hashlib`.

NIST vectors (pure == openssl == expected):

- `b""` → `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `b"abc"` → `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`
- 56-byte `abcdbcdecdef…nopq` → `248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1`

## What was on disk

Poll (20 s cadence) recorded the contract reaching 60 digests at try 21, then stayed on that hash through the comparison:

```
try=21 ts=2026-10-17T22:08:50-0300 s1=NONE contract=8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628 tool=6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067 schema=2 pins=6 digests=60 ten=True detail=r88-m3-maya-cluster:10|r94-paired-crossing:10|r95-crossing-aftermath:10|r96-crossing-response:10|r97-crossing-acknowledgment:10|r98-clerk-filing:10
READY_CONTRACT_ONLY
```

Re-read at 2026-10-17T22:41:20-0300, immediately before this report: contract still 25987 bytes, mtime `1792285726.2482495`, schema_version 2, payload_schema_version 2, six pins, each `payload_schema_version` 2, each `files` length 10. `r99-window-lapse` is not a pin. S1's producer report was still absent (only `S3-fixture-author.md` and `S4-fixture-docs.md`). The 60-digest payload had been byte-stable for about 32 minutes, so this is the delivered contract, not a plan.

Declared pinned set, matching `pinned_files` on the contract and on every pin: `entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`.

## Commands and observed output

From the lane root:

```
python3 .ufo/waves/round-99/seats/V61-scratch/recompute_digests.py
```

Exit 0. Tail of observed stdout:

```
CONTRACT_BYTES 25987
CONTRACT_SHA256_PURE 8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628
CONTRACT_SHA256_OPENSSL 8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628
COMPARED 60
FILE_MISMATCHES 0
CONTENT_MISMATCHES []
VECTOR_FAILURES 0
RESULT PASS
```

Third implementation, same six pins, same ten names, compared to `pins.*.files`:

```
sha256sum_compared=60 mismatches=0
```

Every file line in the first command was `pure == openssl == pin` and `MATCH`. Content lines (SHA-256 of the compact sorted digest JSON, hashed by the pure implementation and again by openssl) also matched the pin `content_sha256`.

## Per-fixture content digests (all MATCH)

| fixture | content_sha256 |
| --- | --- |
| r88-m3-maya-cluster | `acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae` |
| r94-paired-crossing | `048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef` |
| r95-crossing-aftermath | `97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710` |
| r96-crossing-response | `43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c` |
| r97-crossing-acknowledgment | `a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54` |
| r98-clerk-filing | `5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0` |

## The 60 file digests (disk == pin)

r88-m3-maya-cluster (`corpus/fixtures/r88-m3-maya-cluster`):

- entities.json `042b6cc0d70c4d747121d9b277ac031cf21e66822d3c9a3e5ffe0282bba2bddc` (1128)
- relations.json `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` (3)
- timeline.json `f74c664b17fd8d575235ab59432a0ce6f938380e9b5a8d07640aae1d38773493` (455)
- sources.json `aa252416abc2c863ec4ae86cf25bd4f6e6e841d89e8586255b53362897282d63` (476)
- contradictions.json `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` (3)
- README.md `55c9ba57ad7af5db0320fdc09142588c363c8b726d5ae1023dc01264f29b857c` (931)
- claim-excerpt-map.md `b3b79fe5b5b9272b898b5714291739503c4250c415b3959032fcdba84a73fd43` (4916)
- fictional-excerpts.md `e456bb1204b88792d4fe6396e9e8b0deb9ff6f47e1821b0e875738431b9bda89` (484)
- inspiration-note.md `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` (1956)
- source-excerpt.md `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` (640)

r94-paired-crossing:

- entities.json `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` (1449)
- relations.json `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` (139)
- timeline.json `f0209f90a6ce795211369bd900ac1d333d16eb0af123f1b170831e192660533c` (826)
- sources.json `2b627c4c166edf44e1e54bb006964a00e267ab4a4ce0b7b7c0681a0d9f0355d5` (798)
- contradictions.json `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` (3)
- README.md `36796479658cc4eaa95ac50cd38713a934df56d3c430f10b1bab6211ff2a360a` (3426)
- claim-excerpt-map.md `ed9527c551049a6964adc872fbff722b4bdd6a53aa8713fbb6a5d92254e89a47` (7109)
- fictional-excerpts.md `585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2` (1116)
- inspiration-note.md `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` (1956)
- source-excerpt.md `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` (640)

r95-crossing-aftermath:

- entities.json `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` (1449)
- relations.json `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` (139)
- timeline.json `3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177` (1254)
- sources.json `fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a` (1225)
- contradictions.json `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` (3)
- README.md `9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b` (4070)
- claim-excerpt-map.md `80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61` (8641)
- fictional-excerpts.md `0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282` (1845)
- inspiration-note.md `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` (1956)
- source-excerpt.md `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` (640)

r96-crossing-response:

- entities.json `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` (1449)
- relations.json `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` (139)
- timeline.json `ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9` (1677)
- sources.json `9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d` (1741)
- contradictions.json `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` (3)
- README.md `ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456` (4858)
- claim-excerpt-map.md `e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de` (10302)
- fictional-excerpts.md `06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3` (2588)
- inspiration-note.md `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` (1956)
- source-excerpt.md `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` (640)

r97-crossing-acknowledgment:

- entities.json `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` (1449)
- relations.json `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` (139)
- timeline.json `73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b` (2173)
- sources.json `438fb513a62496c41179ead3ea2a55a69ff4ce1fd191c3a7ebccb10651a8dc73` (2235)
- contradictions.json `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` (3)
- README.md `d9387b7d73264dfc6c01d27cc6bf24c58ef6bdb4461d2ae8fbfdb6376d9e019f` (5304)
- claim-excerpt-map.md `49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f` (12117)
- fictional-excerpts.md `8ba491cb249dd57f6aee8ca216133b07c06287c0240be658ea2e68da0cf5703c` (3410)
- inspiration-note.md `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` (1956)
- source-excerpt.md `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` (640)

r98-clerk-filing:

- entities.json `db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984` (1793)
- relations.json `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` (139)
- timeline.json `eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af` (2552)
- sources.json `32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3` (2725)
- contradictions.json `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` (3)
- README.md `32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926` (5829)
- claim-excerpt-map.md `c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba` (15028)
- fictional-excerpts.md `29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de` (4187)
- inspiration-note.md `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` (1956)
- source-excerpt.md `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` (640)

Parentheses are byte lengths read in binary mode. No pin key was missing from disk; no pin had an extra or missing name versus the declared ten. Identical digests across fixtures (empty `contradictions.json` `37517e5f…`, shared `inspiration-note.md` `58f5390e…`, shared `source-excerpt.md` `b5edc2fd…`, shared `relations.json` / `entities.json` on r94–r97) are the same bytes on disk, not a pin copy error.

## Not claimed

- S1's producer report was absent at 22:41:20-0300. This comparison is against the stable contract bytes, not against S1's narrative.
- `r99-window-lapse` is not among the 60. Whether S1 later pins it is outside this seat.
- This seat did not run `--freeze`, `--self-test`, or a Markdown-tamper probe. Digest equality does not by itself prove the exit-2 naming path.
- V05's implementation was not observed. Difference from the tool is observed: no `hashlib`, no import of `dependency_freeze`.

PASS: 60/60 pinned file digests and 6/6 content digests match the contract, recomputed from disk by a FIPS 180-4 implementation and confirmed by openssl and sha256sum.
