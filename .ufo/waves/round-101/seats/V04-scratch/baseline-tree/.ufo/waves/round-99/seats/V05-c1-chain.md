# V05 c1-chain — round 99

Seat: V05 c1-chain (verifier, leaf). Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5`. Commands from the lane root with `python3`. No nested agents, no commits, no pushes, no network. Exclusive write: this report. Did not run `--freeze` and did not write producer-owned bytes.

Axes for this seat: (1) chain verify 6/6 clean, (2) each pin's ten file digests match delivered bytes (60 recomputed here), (3) the contract contains exactly six pins. No axis harmed.

## Poll-wait (20 s, max 40; artifacts AND S1 report)

Poll started `2026-10-17T22:01:01-03:00`. Watch: a seats file matching `S1*` (type file) plus the freeze tool/contract. `s1_files=none` on every try. Tool mtime moved at try 4; contract mtime moved at try 11. Terminal:

```
POLL_CHECK try=1 t=20s 2026-10-17T22:01:01-03:00 s1_files=none py_changed=no ct_changed=no seat_reports=1
POLL_CHECK try=4 t=80s 2026-10-17T22:02:01-03:00 s1_files=none py_changed=yes ct_changed=no seat_reports=1
POLL_CHECK try=11 t=220s 2026-10-17T22:04:21-03:00 s1_files=none py_changed=yes ct_changed=yes seat_reports=4
POLL_CHECK try=40 t=800s 2026-10-17T22:14:02-03:00 s1_files=none py_changed=yes ct_changed=yes seat_reports=11
POLL_TERMINAL status=ABSENT tries=40 elapsed=800s
POLL_END 2026-10-17T22:14:22-03:00
```

Not an all-reports poll, so subtract-SELF did not apply. Bounded stall-escape, recorded, not fatal: the 40-try window closed with no `S1*.md`. A later confirmation, before this report was written, found the producer report. Chain verify was not run during the absent window.

Post-window confirmation that still saw no report (`2026-10-17T22:47:29-03:00`): `s1_md_count=0`. The tool had been rewritten after the poll (`2026-10-17 22:38:11`, sha256 `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`); the contract was still the try-11 bytes (`8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`). Those in-flight bytes were not scored.

Report hit at `2026-10-17T22:49:43-03:00`:

```
2026-10-17+22:48:57.4849138040 11971 S1-full-file-pins.md
s1_md_count=1
```

Read in full (224 lines). It is a finished producer report (`Seat: S1`, owned paths match, trailing `PASS` line), not a plan. Conventional `S1-freeze-hygiene.md` was never written; this is the only `S1*.md`.

## Identity of the verified revision

Before and after the checks below, same mtimes and sha256 (verify did not rewrite them):

```
2026-10-17 22:38:11.814368253 -0300 29110 corpus/tools/dependency_freeze.py
2026-10-17 22:08:46.248249589 -0300 25987 corpus/tools/dependency-freeze-contract.json
2026-10-17 22:48:57.484913804 -0300 11971 .ufo/waves/round-99/seats/S1-full-file-pins.md
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
```

Window: `2026-10-17T22:53:09-03:00` start and end.

## Chain verify 6/6

`FREEZE` in the receipt is the tool's verify banner. `--freeze` was not passed.

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
EXIT=0
```

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
RESULT PASS
EXIT=0
```

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
EXIT=0
```

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
RESULT PASS
EXIT=0
```

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
RESULT PASS
EXIT=0
```

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
EXIT=0
```

6/6 `RESULT PASS`, all exit 0. No `FINDING` lines.

## Exactly six pins

Independent `json.loads` of `corpus/tools/dependency-freeze-contract.json` (25987 bytes), not the tool's verifier:

```
SCHEMA_VERSION 2
PAYLOAD_SCHEMA_VERSION 2
PIN_TYPE dict
PIN_COUNT 6
PIN_NAMES ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing']
SIX_PINS_EXACT True
```

`pinned_files` at the contract root, and on every pin, equals the declared ten: `entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`. Each pin has `payload_schema_version` 2 and `nfiles=10`. No seventh pin (`r99-window-lapse` is not in `pins`).

## 60 file digests, recomputed

`hashlib.sha256` of each delivered file's raw bytes, compared to `pins[name].files[fname]`. 60 checks, 0 mismatches. Content digest below is an extra check (canonical JSON of those ten digests, `sort_keys=True`, `separators=(",", ":")`, then sha256); it is not a substitute for the 60 file hashes. It matched every pin and matched the six `DIGEST` lines above.

```
PIN r88-m3-maya-cluster nfiles=10
  MATCH entities.json 042b6cc0d70c4d747121d9b277ac031cf21e66822d3c9a3e5ffe0282bba2bddc
  MATCH relations.json 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  MATCH timeline.json f74c664b17fd8d575235ab59432a0ce6f938380e9b5a8d07640aae1d38773493
  MATCH sources.json aa252416abc2c863ec4ae86cf25bd4f6e6e841d89e8586255b53362897282d63
  MATCH contradictions.json 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  MATCH README.md 55c9ba57ad7af5db0320fdc09142588c363c8b726d5ae1023dc01264f29b857c
  MATCH claim-excerpt-map.md b3b79fe5b5b9272b898b5714291739503c4250c415b3959032fcdba84a73fd43
  MATCH fictional-excerpts.md e456bb1204b88792d4fe6396e9e8b0deb9ff6f47e1821b0e875738431b9bda89
  MATCH inspiration-note.md 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
  MATCH source-excerpt.md b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
  CONTENT MATCH acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
PIN r94-paired-crossing nfiles=10
  MATCH entities.json 026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b
  MATCH relations.json c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
  MATCH timeline.json f0209f90a6ce795211369bd900ac1d333d16eb0af123f1b170831e192660533c
  MATCH sources.json 2b627c4c166edf44e1e54bb006964a00e267ab4a4ce0b7b7c0681a0d9f0355d5
  MATCH contradictions.json 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  MATCH README.md 36796479658cc4eaa95ac50cd38713a934df56d3c430f10b1bab6211ff2a360a
  MATCH claim-excerpt-map.md ed9527c551049a6964adc872fbff722b4bdd6a53aa8713fbb6a5d92254e89a47
  MATCH fictional-excerpts.md 585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2
  MATCH inspiration-note.md 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
  MATCH source-excerpt.md b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
  CONTENT MATCH 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
PIN r95-crossing-aftermath nfiles=10
  MATCH entities.json 026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b
  MATCH relations.json c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
  MATCH timeline.json 3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177
  MATCH sources.json fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a
  MATCH contradictions.json 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  MATCH README.md 9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b
  MATCH claim-excerpt-map.md 80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61
  MATCH fictional-excerpts.md 0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282
  MATCH inspiration-note.md 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
  MATCH source-excerpt.md b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
  CONTENT MATCH 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
PIN r96-crossing-response nfiles=10
  MATCH entities.json 026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b
  MATCH relations.json c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
  MATCH timeline.json ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9
  MATCH sources.json 9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d
  MATCH contradictions.json 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  MATCH README.md ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456
  MATCH claim-excerpt-map.md e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de
  MATCH fictional-excerpts.md 06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3
  MATCH inspiration-note.md 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
  MATCH source-excerpt.md b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
  CONTENT MATCH 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
PIN r97-crossing-acknowledgment nfiles=10
  MATCH entities.json 026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b
  MATCH relations.json c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
  MATCH timeline.json 73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b
  MATCH sources.json 438fb513a62496c41179ead3ea2a55a69ff4ce1fd191c3a7ebccb10651a8dc73
  MATCH contradictions.json 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  MATCH README.md d9387b7d73264dfc6c01d27cc6bf24c58ef6bdb4461d2ae8fbfdb6376d9e019f
  MATCH claim-excerpt-map.md 49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f
  MATCH fictional-excerpts.md 8ba491cb249dd57f6aee8ca216133b07c06287c0240be658ea2e68da0cf5703c
  MATCH inspiration-note.md 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
  MATCH source-excerpt.md b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
  CONTENT MATCH a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
PIN r98-clerk-filing nfiles=10
  MATCH entities.json db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984
  MATCH relations.json c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9
  MATCH timeline.json eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af
  MATCH sources.json 32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3
  MATCH contradictions.json 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  MATCH README.md 32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926
  MATCH claim-excerpt-map.md c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba
  MATCH fictional-excerpts.md 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de
  MATCH inspiration-note.md 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
  MATCH source-excerpt.md b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
  CONTENT MATCH 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
CHECKED 60
MISMATCH_COUNT 0
```

PASS — chain 6/6 clean (all six quoted, exit 0); 60/60 ten-file digests match delivered bytes; contract pins are exactly the six chain fixtures.
