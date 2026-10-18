# V79 c1-contract-validity — round 99

Seat: V79. Exclusive write: this report. Scratch only under `.ufo/waves/round-99/seats/V79-scratch/`. No commit, no push, no network, no nested agent. Did not run `--freeze` or `--self-test` (those can rewrite the contract or create repo-root temp dirs). Isolated trees were built only in scratch by calling `self_test_cases`.

Axes: schema completeness (basename pin keys, repo-relative unique paths, 64-hex digests, schema version present); isolated-tree fixture resolvability; evidence fidelity; non-harm (do not verify the declaration before the contract bytes exist, do not write producer files).

Validated object: delivered `corpus/tools/dependency-freeze-contract.json`, with `corpus/tools/dependency_freeze.py` used only to resolve self-test case trees and to corroborate `validate_pin`. Not a validation of the LOG declaration.

## Poll

40 tries, 20 s cadence, `22:03:04`–`22:16:24`. Log: `.ufo/waves/round-99/seats/V79-scratch/poll.log`.

```
poll-start 2026-10-17T22:03:04-0300
try=1 ts=2026-10-17T22:03:04-0300 reports=S3-fixture-author.md, contract=[2026-10-17 20:33:36.611874789 -0300 19291] tool=[2026-10-17 22:02:04.079077994 -0300 29211] markers=0
try=19 ts=2026-10-17T22:09:04-0300 reports=S3-fixture-author.md,S4-fixture-docs.md, contract=[2026-10-17 22:08:46.248249589 -0300 25987] tool=[2026-10-17 22:07:33.506669398 -0300 29104] markers=18
try=40 ts=2026-10-17T22:16:04-0300 reports=S3-fixture-author.md,S4-fixture-docs.md, contract=[2026-10-17 22:08:46.248249589 -0300 25987] tool=[2026-10-17 22:07:33.506669398 -0300 29104] markers=18
poll-end 2026-10-17T22:16:24-0300
```

At poll end the contract artifact was present and stable (size 25987, mtime `22:08:46`, markers 18 from try 19). `S1*.md` was absent. That is not “verify a plan”: the bytes had already replaced the r98 contract (`153ebc5b…`, 19291 bytes, mtime `20:33:36`).

Stall-escape, recorded, not fatal: one later listing after the 40-try budget.

```
$ date +%Y-%m-%dT%H:%M:%S%z; ls -la /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/S*.md
2026-10-17T22:46:59-0300
-rw-r--r-- 1 vgpnk vgpnk 5069 Oct 17 22:01 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/S3-fixture-author.md
-rw-r--r-- 1 vgpnk vgpnk 9303 Oct 17 22:03 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/S4-fixture-docs.md
```

S1 report was still absent. Tool had moved after the poll (`22:38:11`, 29110 bytes). Contract mtime was still `22:08:46`.

At `22:50:38` the producer report existed and the contract hash had not moved:

```
$ date +%Y-%m-%dT%H:%M:%S%z
2026-10-17T22:50:38-0300
$ ls -la /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/S1*.md
-rw-r--r-- 1 vgpnk vgpnk 11971 Oct 17 22:48 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/S1-full-file-pins.md
$ sha256sum /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency-freeze-contract.json /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency-freeze-contract.json
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency_freeze.py
```

Those two hashes are the hashes at the end of the corrected checker below. S1’s report describes this pin set (ten files, `payload_schema_version` 2, chain of six, `r99-window-lapse` not pinned). Content digests S1 quotes match the independent recomputation in that checker.

## Schema snapshot

Reconfirmed at `2026-10-17T23:01:44-0300` with the same two hashes, after this report was first written. Command actually run:

```
$ python3 -c 'import json; from pathlib import Path; c=json.loads(Path("/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency-freeze-contract.json").read_text()); print("schema_version", c["schema_version"]); print("payload_schema_version", c["payload_schema_version"]); print("pinned_files", c["pinned_files"]); print("pin_keys", list(c["pins"])); print("fixture_paths", [p["fixture"] for p in c["pins"].values()]); print("payload_versions", sorted({p["payload_schema_version"] for p in c["pins"].values()})); print("file_counts", sorted({len(p["files"]) for p in c["pins"].values()})); print("base_fixture", c["self_test"]["base_fixture"]); print("n_expected", len(c["self_test"]["expected"])); print("markdown_tamper", c["self_test"]["expected"]["markdown_tamper"]); print("has_r99_pin", "r99-window-lapse" in c["pins"])'
schema_version 2
payload_schema_version 2
pinned_files ['entities.json', 'relations.json', 'timeline.json', 'sources.json', 'contradictions.json', 'README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md']
pin_keys ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing']
fixture_paths ['corpus/fixtures/r88-m3-maya-cluster', 'corpus/fixtures/r94-paired-crossing', 'corpus/fixtures/r95-crossing-aftermath', 'corpus/fixtures/r96-crossing-response', 'corpus/fixtures/r97-crossing-acknowledgment', 'corpus/fixtures/r98-clerk-filing']
payload_versions [2]
file_counts [10]
base_fixture r95-crossing-aftermath
n_expected 18
markdown_tamper {'exit': 2, 'finding_ids': ['DIGEST-MISMATCH'], 'names_file': 'fictional-excerpts.md', 'forbid_traceback': True}
has_r99_pin False
```

A raw JSON walk of the same file found no duplicate object keys (`DUPLICATE_KEYS none` in `V79-scratch/validate-out.txt`).

## Listed invariants

Checker: inline `python3` from the lane root, first pass written to `V79-scratch/validate-out.txt`. Contract sha before and after that pass: `8c2561b0…` unchanged. Tool sha during that pass: `fb9bb9ff…` unchanged. Summary lines:

```
CHECK PASS schema-version-present: schema_version=2 type=int; payload_schema_version=2
CHECK PASS pins-object: type=dict n=6
CHECK PASS pins-keyed-by-basename: 6 keys match fixture basenames; file keys are basenames
CHECK PASS paths-repo-relative-unique: 6 unique repo-relative fixture paths
CHECK PASS digests-64-hex: content_sha256 and every files value are 64 lowercase hex
CHECK PASS pin-payload-schema-version-present: every pin has payload_schema_version; values=[2]
EXPECTATION_SET missing=none extra=none
BASE_TEN_MISSING []
```

Rules applied, all six pins:

- Pin key is a basename (no slash) and equals `Path(fixture).name`.
- `fixture` is exactly `corpus/fixtures/<key>`: not absolute, no `..` or `.`, no empty component, unique, resolves inside the lane, and the directory exists.
- `files` keys are basenames, exactly the ten declared names, no extras.
- `content_sha256` and every `files` value match `^[0-9a-f]{64}$`.
- Root `schema_version` is present (`2`, int). Root `payload_schema_version` is present (`2`). Every pin’s `payload_schema_version` is present (`2`).

`r99-window-lapse` is not a pin. That is not a schema failure: the declaration’s chain is 6/6, and S1 states the same bound. This seat did not require a seventh pin.

## Isolated-tree fixture resolution

The first checker’s `VERDICT FAIL` in `validate-out.txt` is a checker error, not a contract error. It treated `missing_timeline`’s intentional `(scratch / "timeline.json").unlink()` (`dependency_freeze.py:541-544`) as an unresolvable fixture. The directory itself existed and was inside the mirror. Withdrawn.

Corrected checker, same contract and tool hashes, trees under `V79-scratch/isolated-tree-2/`. It calls the delivered `validate_pin` and `self_test_cases` (no CLI `--self-test`, no `--freeze`).

```
validate_pin:
  r88-m3-maya-cluster OK
  r94-paired-crossing OK
  r95-crossing-aftermath OK
  r96-crossing-response OK
  r97-crossing-acknowledgment OK
  r98-clerk-filing OK
validate_pin_errors 0
byte_mismatches none
CASE missing_timeline isolated_tool=True ...
  PIN_BIND match=True
  absent_files=['timeline.json'] expected_absent=['timeline.json']
CASE missing_fixture isolated_tool=True ...
  INTENTIONAL_ABSENT inside isolated mirror
CASE self_test_mismatch isolated_tool=True ...
  nested_base exists=True pin_bind=True ten_present=True
CASE markdown_tamper isolated_tool=True ...
  PIN_BIND match=True
  absent_files=none expected_absent=none
RESOLVE_FAILS none
RESOLVE_VERDICT PASS
contract_after 8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628
tool_after fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c
```

Classification, 18/18 built, expectation set equals `FROZEN_CASES`, `self_test.base_fixture` equals tool `SELF_TEST_BASE` (`r95-crossing-aftermath`):

- 13 mirror-tool cases that name `r95-crossing-aftermath` (`reduction_edge_drop` through `relation_added`, `digest_tamper`, `malformed_json`, `missing_timeline`, `markdown_tamper`): fixture directory exists inside that case’s mirror root, and `mirror_root / pin["fixture"]` resolves to the invoked directory. `missing_timeline` is missing only `timeline.json`, which the case deletes. The other twelve have all ten pinned files.
- `unpinned_fixture`: directory exists at `corpus/fixtures/unpinned_fixture` inside its mirror; basename is not a pin key.
- `missing_fixture`: path is `mirror/corpus/fixtures/missing_case/r95-crossing-aftermath`, inside the mirror, and absent. That is the case’s address, not a dangling path outside the tree.
- `self_test_mismatch`: no fixture operand; the nested base `corpus/fixtures/r95-crossing-aftermath` is copied into the mirror, pin-binds, and has all ten files.
- Four live-tool cases (`clean`, `invalid_arguments`, `path_mismatch`, `scope_refused`) do not invoke a mirrored tool. Their named paths exist (`r95` for the first two; the foreign copy and the scope target under the scratch workdir for the last two). They are resolvable where the builder points them. They are not a failure of the mirror pin-bind check, because they are not mirror invocations. `path_mismatch` is outside `corpus/fixtures` on purpose.

Mirror contract copied into `markdown_tamper` still has `fixture='corpus/fixtures/r95-crossing-aftermath'`, `payload_schema_version=2`, 10 file digests (first checker).

## Observation, not a listed invariant

Independent SHA-256 of the ten on-disk files, then the tool’s content-digest construction (`json.dumps` of per-file digests, `sort_keys=True`, `separators=(",", ":")`), matched every pin. No byte mismatch. Those content digests are the ones S1 quotes from `--freeze`:

- r88 `acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae`
- r94 `048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef`
- r95 `97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710`
- r96 `43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c`
- r97 `a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54`
- r98 `5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0`

This seat did not replay `--self-test` or a Markdown tamper. S1’s report claims self-test 18/18; that is their evidence, not this seat’s.

## Not done

Did not judge semantic inventory, BR-01 prose detectability, or the r99 fixture. Did not treat the first checker’s `missing_timeline` false fail as a contract fail.

PASS — listed schema invariants hold on contract `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628` (pins keyed by basename, six unique `corpus/fixtures/<name>` paths, 64-hex digests, schema version 2 present, 18 self-test fixtures resolvable in the isolated trees the builder actually constructs).
