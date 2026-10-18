# V01 c1-payload-schema — round 99

Seat: V01 c1-payload-schema. Lane `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5`; HEAD during the round `337f0fa` (`git rev-parse --short HEAD` at poll start). Commands from the lane root with `python3`. Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report and `.ufo/waves/round-99/seats/V01-scratch/` only. Did not run `--freeze` (that rewrites S1's contract).

Axes: completeness (every chain pin carries all ten file digests; no pin omits a declared file); schema recording (`payload_schema_version` on every pin, and the schema version recorded in the contract); evidence fidelity (quoted commands); poll discipline (artifacts and the S1 report, not a plan).

Declared ten: `entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`.

## Poll-wait

Cadence 20 s. Official budget 40 tries. Producer report required: a file `S1*.md` directly under `.ufo/waves/round-99/seats/`. Owned artifacts: `corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json`.

Official poll, 22:01:34–22:14:34. Contract still the r98 five-file pins at try 01. Tool bytes moved from try 02. Top-level `schema_version` became 2 by try 10 while pins were still 5 files. Try 23 (22:08:54) was the first observation of six pins at 10 files each, contract 25987 bytes. Tries 23–40 held that size. No `S1*.md` on any of the 40 tries.

```
POLL-START 22:01:34 base_c_mtime=1792280016.6118748 base_p_mtime=1792279909.4825668 sizes 19291/26644
try 01 22:01:34 reports=- changed=False c_size=19291 p_size=26644 schema_val=None pin_n=None
try 10 22:04:34 reports=- changed=True c_size=21007 p_size=29048 schema_val=2 pin_n={'r88-m3-maya-cluster': 5, 'r94-paired-crossing': 5, 'r95-crossing-aftermath': 5, 'r96-crossing-response': 5, 'r97-crossing-acknowledgment': 5, 'r98-clerk-filing': 5}
try 23 22:08:54 reports=- changed=True c_size=25987 p_size=29104 schema_val=2 pin_n={'r88-m3-maya-cluster': 10, 'r94-paired-crossing': 10, 'r95-crossing-aftermath': 10, 'r96-crossing-response': 10, 'r97-crossing-acknowledgment': 10, 'r98-clerk-filing': 10}
try 40 22:14:34 reports=- changed=True c_size=25987 p_size=29104 schema_val=2 pin_n={'r88-m3-maya-cluster': 10, 'r94-paired-crossing': 10, 'r95-crossing-aftermath': 10, 'r96-crossing-response': 10, 'r97-crossing-acknowledgment': 10, 'r98-clerk-filing': 10}
RESULT ABSENT
```

Stall-escape 1 (recorded, not fatal): tries 41–48, 22:27:52–22:30:12. Still no `S1*.md`. Contract mtime/size unchanged (`25987`). `S_reports=['S3-fixture-author.md', 'S4-fixture-docs.md']` only. Closed `STALL-ESCAPE ABSENT`.

The producer was still writing after that close. At 22:38:09 `S1-scratch` had grown an `after/mirror`, and at 22:43:10 the live tool was `29110` bytes, mtime `2026-10-17 22:38:11` (was `29104`). A second stall-escape was taken because the owned tool was mid-edit, not because the budget was ignored.

Stall-escape 2, tries 49–60, start 22:45:21. Try 59 and try 60 had the same contract/tool signature. Report appeared on try 60.

```
try 49 22:45:21 S1=- S=['S3-fixture-author.md', 'S4-fixture-docs.md'] c=1792285726/25987 p=1792287492/29110 scratch_mtime=1792287810.3238096
try 60 22:49:01 S1=['S1-full-file-pins.md'] S=['S1-full-file-pins.md', 'S3-fixture-author.md', 'S4-fixture-docs.md'] c=1792285726/25987 p=1792287492/29110 scratch_mtime=1792287972.0053496
LANDED_STABLE S1-full-file-pins.md
```

Stability re-stat at 22:50:31, then again 2 s later: report `11971` bytes, mtime `2026-10-17 22:48:57.484913804 -0300`, unchanged. Contract mtime still `2026-10-17 22:08:46.248249589 -0300`, `25987` bytes. Tool mtime `2026-10-17 22:38:11.814368253 -0300`, `29110` bytes. Report closes `PASS — C1 delivered (payload_schema_version 2, ten-file pins, chain 6/6, ...)`. Verification below is against those stable bytes, not against the report's claims.

## Contract structure

Post-landing read of `corpus/tools/dependency-freeze-contract.json` (`sha256 8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`, 25987 bytes). Top-level keys, in file order:

`schema_version`, `payload_schema_version`, `tool`, `scope`, `precedence`, `data_files`, `pinned_files`, `required_files`, `exit_codes`, `revision`, `pins`, `self_test`, `provenance_note`.

Quoted from the same JSON load (`WHEN 2026-10-17T22:53:37-0300`):

```
schema_version 2
payload_schema_version 2
pinned_files ['entities.json', 'relations.json', 'timeline.json', 'sources.json', 'contradictions.json', 'README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md']
pinned_files_eq_ten True
data_files ['entities.json', 'relations.json', 'timeline.json', 'sources.json', 'contradictions.json']
PIN_COUNT 6
PIN_NAMES ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing']
R99_IN_PINS False
```

The root schema fields and the declared ten are the command output above, not a paraphrase. `scope` and `precedence` also name `payload_schema_version` 2 and the ten-file `CONTRACT-INVALID` rule; those sentences are long and are not re-copied here. The structural fact this seat needs is the two integer fields plus `pinned_files`, all quoted from the load.

`data_files` remains the five JSON tables (model build). `pinned_files` is the ten-file digest set. Both schema fields are contract data, not only prose: `schema_version` 2 and `payload_schema_version` 2 at the root.

Delivered tool constants (`corpus/tools/dependency_freeze.py`, `sha256 fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`, 29110 bytes), quoted from the same run:

```
DATA_FILES = ("entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json")
MARKDOWN_FILES = (
    "README.md",
    "claim-excerpt-map.md",
    "fictional-excerpts.md",
    "inspiration-note.md",
    "source-excerpt.md",
)
PINNED_FILES = DATA_FILES + MARKDOWN_FILES
PAYLOAD_SCHEMA_VERSION = 2
```

`validate_pin` refuses a pin whose `payload_schema_version` is not 2, whose `pinned_files` is not that ten, or whose `files` map is not exactly those ten sha256 digests (`CONTRACT-INVALID`). That is the enforcement of the recorded schema; this seat's check is the stored pins.

## Every chain pin

Chain pins are the six objects under `pins`. There is no seventh. `r99-window-lapse` is not a pin (`R99_IN_PINS False`). That matches the r99 declaration's C1 chain (6/6, the existing continuation fixtures) and S1's report that r99 was left unpinned because it is other seats' bytes. Not an omitted chain pin.

For each pin, the check required `payload_schema_version == 2`, `pinned_files` equal to the declared ten, `files` containing exactly those ten keys, each value a 64-hex sha256, each digest equal to `sha256(fixture_file)`, and `content_sha256` equal to `sha256` of the canonical JSON object `{name: digest}` with `sort_keys=True` and `separators=(",", ":")` (the tool's `content_digest`).

```
r88-m3-maya-cluster schema=2 files=10 missing=[] extra=[] bad=[] disk_missing=[] mismatch=[] content_match=True pinned_files_eq=True
r94-paired-crossing schema=2 files=10 missing=[] extra=[] bad=[] disk_missing=[] mismatch=[] content_match=True pinned_files_eq=True
r95-crossing-aftermath schema=2 files=10 missing=[] extra=[] bad=[] disk_missing=[] mismatch=[] content_match=True pinned_files_eq=True
r96-crossing-response schema=2 files=10 missing=[] extra=[] bad=[] disk_missing=[] mismatch=[] content_match=True pinned_files_eq=True
r97-crossing-acknowledgment schema=2 files=10 missing=[] extra=[] bad=[] disk_missing=[] mismatch=[] content_match=True pinned_files_eq=True
r98-clerk-filing schema=2 files=10 missing=[] extra=[] bad=[] disk_missing=[] mismatch=[] content_match=True pinned_files_eq=True
GAPS []
CONTRACT_RECORDS_SCHEMA 2 2
ALL_OK True
```

No pin omits a declared file. No pin carries an extra file key. No digest failed the sha256 shape check. All six content aggregates match the pin.

Representative pin payload (`pins["r88-m3-maya-cluster"]`), quoted from the `json.dumps` of the loaded contract in the same post-landing run. The other five pins use the same `payload_schema_version` / `pinned_files` shape; their `content_sha256` values are in the per-pin lines below.

```
"fixture": "corpus/fixtures/r88-m3-maya-cluster",
"payload_schema_version": 2,
"pinned_files": [
  "entities.json",
  "relations.json",
  "timeline.json",
  "sources.json",
  "contradictions.json",
  "README.md",
  "claim-excerpt-map.md",
  "fictional-excerpts.md",
  "inspiration-note.md",
  "source-excerpt.md"
],
"content_sha256": "acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae",
"files": {
  "README.md": "55c9ba57ad7af5db0320fdc09142588c363c8b726d5ae1023dc01264f29b857c",
  "claim-excerpt-map.md": "b3b79fe5b5b9272b898b5714291739503c4250c415b3959032fcdba84a73fd43",
  "contradictions.json": "37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570",
  "entities.json": "042b6cc0d70c4d747121d9b277ac031cf21e66822d3c9a3e5ffe0282bba2bddc",
  "fictional-excerpts.md": "e456bb1204b88792d4fe6396e9e8b0deb9ff6f47e1821b0e875738431b9bda89",
  "inspiration-note.md": "58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37",
  "relations.json": "37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570",
  "source-excerpt.md": "b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd",
  "sources.json": "aa252416abc2c863ec4ae86cf25bd4f6e6e841d89e8586255b53362897282d63",
  "timeline.json": "f74c664b17fd8d575235ab59432a0ce6f938380e9b5a8d07640aae1d38773493"
}
```

Per-pin content digests (all `payload_schema_version=2`, `nfiles=10`):

```
r88-m3-maya-cluster content_sha256=acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
r94-paired-crossing content_sha256=048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
r95-crossing-aftermath content_sha256=97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
r96-crossing-response content_sha256=43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
r97-crossing-acknowledgment content_sha256=a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
r98-clerk-filing content_sha256=5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
```

## Read-only verify

Positional fixture argument is verify, not freeze (`dependency_freeze.py` help: `fixture` = "fixture directory to verify against its pin"; writes happen only in `freeze()` via `--freeze`). After the six calls, contract mtime was still `2026-10-17 22:08:46` and sha256 still `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`. The `FREEZE` line is the receipt label (observed/pin counts), not a write.

```
--- r88-m3-maya-cluster ---
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
EXIT:0
--- r94-paired-crossing ---
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
RESULT PASS
EXIT:0
--- r95-crossing-aftermath ---
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
EXIT:0
--- r96-crossing-response ---
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
RESULT PASS
EXIT:0
--- r97-crossing-acknowledgment ---
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
RESULT PASS
EXIT:0
--- r98-clerk-filing ---
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
EXIT:0
```

## Not this seat

Markdown-tamper self-test (17→18), `DIGEST-MISMATCH` naming on a prose edit, and the 6/6 re-freeze procedure are S1's other C1 claims. This seat checked the stored payload schema and that verify accepts the pins. It did not re-run `--self-test` or `--freeze`.

`r99-window-lapse` is absent from `pins`. That is consistent with C1's six-fixture chain. It is not a missing digest on a chain pin.

## Bottom line

PASS — six chain pins each carry all ten file digests and payload_schema_version 2; the contract records schema_version 2 and payload_schema_version 2; no pin omits a declared file.
