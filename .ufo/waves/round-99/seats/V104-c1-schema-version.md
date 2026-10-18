# V104 c1-schema-version — round 99

Seat: V104 (verifier, c1-schema-version). Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5`. Commands from the lane root with `python3`, or from a scratch mirror of the delivered tool as noted. Leaf seat: no nested agents, no commits, no pushes, no network. Exclusive writes: this report and `.ufo/waves/round-99/seats/V104-scratch/` (`poll.log`, `version-probe.txt`, `version-probe-live3.txt`, tool snapshots, mirrors). Live `corpus/tools/` was not written.

Axis: calibration. Question: what the payload schema version governs, and whether a scratch contract with the wrong version exits 2 under a named finding.

## Poll

S1 report absent on tries 1–35 (20 s cadence, `V104-scratch/poll.log`). Try 36 (`2026-10-17T22:49:13-03:00`) found `.ufo/waves/round-99/seats/S1-full-file-pins.md` (224 lines, a finished producer report, not a plan). Read in full.

Artifact hashes at the verdict, matching the live3 probe and try 36:

- `corpus/tools/dependency_freeze.py` 29110 bytes `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`
- `corpus/tools/dependency-freeze-contract.json` 25987 bytes `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`

Try 19 changed only the tool (29104 `6f81f8be…` → 29110 `fb9bb9ff…`). Diff against the prior snapshot is one string in the `DIGEST-MISMATCH` detail (`fixture bytes changed outside the frozen inventory` → `pinned-file bytes changed outside the semantic inventory`). The version check did not move. Contract hash was stable from the re-freeze through try 36.

## What the version governs

The enforced version is the per-pin field `payload_schema_version`, compared to the constant `PAYLOAD_SCHEMA_VERSION = 2` (`dependency_freeze.py:59`). `--freeze` stamps that constant onto the pin it writes (`dependency_freeze.py:432`). `validate_pin` refuses any other value before path bind, model build, inventory compare, or digest compare (`dependency_freeze.py:309-312`):

```
if pin.get("payload_schema_version") != PAYLOAD_SCHEMA_VERSION:
    fail("CONTRACT-INVALID",
         f"pin {name} payload_schema_version {pin.get('payload_schema_version')!r} "
         f"!= {PAYLOAD_SCHEMA_VERSION} (full-file pin of {len(PINNED_FILES)} files)")
```

`read_contract` does not read contract-root `schema_version` or root `payload_schema_version`. A search of the delivered tool finds no `contract.get("schema_version")` and no `contract["schema_version"]`. Those root fields are documentary. The delivered contract sets both to 2, and `precedence` classifies a pin version other than 2 as `CONTRACT-INVALID`.

The number does not select a payload shape or a digest algorithm.

- File set is the separate constant `PINNED_FILES` (five JSON tables + five Markdown files) plus equality checks on `pinned_files` and on `files` keys (`dependency_freeze.py:313-323`). A version-2 pin with only the five JSON digests still exits 2 `CONTRACT-INVALID` on the digest-key check, not on the version check.
- `content_digest` hashes file bytes only (`dependency_freeze.py:113-116`). The version field is not an input.
- `compare()` does not look at the version. There is no version-1 interpreter. A schema-1 pin is refused, not read as JSON-only. Re-freeze overwrites a same-path pin with a version-2 pin; it does not branch on the old version. That matches the contract sentence "Re-freeze is the payload upgrade path from a schema-1 JSON-only pin to payload_schema_version 2."

So version 2 governs pin admission: the pin is not evaluated unless `payload_schema_version` equals 2. It labels the full-file payload in the error text. It does not govern which bytes are hashed, which semantic findings fire, or the contract-root version fields.

Delivered pins, all six, have `payload_schema_version` 2, `pinned_files` length 10, and ten file digests including the five Markdown names. No self-test case covers a version mismatch. `self_test.expected` is the 18 cases ending in `markdown_tamper`; none is a schema-version case.

## Scratch contract, wrong version

Mirror: `V104-scratch/mirror-live3/`, copy of the delivered tool (`fb9bb9ff…`) and contract (`8c2561b0…`) plus `corpus/fixtures/r95-crossing-aftermath`. Only the scratch contract was mutated. Live contract hash after the probe still `8c2561b0…`. Driver output: `V104-scratch/version-probe-live3.txt`.

Control, delivered r95 pin left at version 2:

```
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
```

exit 0. Same digest S1 recorded for r95.

Wrong versions, same pin otherwise, `python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath` from that mirror:

| scratch pin `payload_schema_version` | exit | finding |
|---|---|---|
| 1 | 2 | `CONTRACT-INVALID: pin r95-crossing-aftermath payload_schema_version 1 != 2 (full-file pin of 10 files)` |
| 3 | 2 | same form, `3 != 2` |
| `"2"` (string) | 2 | `payload_schema_version '2' != 2` |
| missing key | 2 | `payload_schema_version None != 2` |
| 1, and `content_sha256` set to 64 zeros | 2 | still `CONTRACT-INVALID` naming version 1, not `DIGEST-MISMATCH` |

`RESULT ERROR` on each. No traceback. The named finding is `CONTRACT-INVALID`, which is the id the precedence text assigns to "payload_schema_version other than 2". There is no `SCHEMA-MISMATCH` or `VERSION-MISMATCH` id.

Earlier probe on the same version check (`V104-scratch/version-probe.txt`, tool then `6f81f8be…`, version logic identical) also showed version 0 → exit 2 `0 != 2`, `True` → exit 2 `True != 2`, and a version-1 pin whose fixture directory was absent still `CONTRACT-INVALID` rather than `FIXTURE-MISSING`. Setting only the r95 pin to version 1 left r94 verify at exit 0 (`DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef`). The check is per invoked pin.

Root fields ignored, pin left at 2 (`version-probe-live3.txt`):

```
=== root schema 99 pin 2 exit=0 ===
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
```

The earlier probe also set root `schema_version` to 1 and root `payload_schema_version` to 99 together; exit 0, same digest.

## Bound, not a failed mismatch case

`payload_schema_version` 2.0 (float) exits 0 with the same PASS receipt. `2.0 != 2` is false in Python, and the precedence text says "other than 2", not "not an int equal to 2". String `"2"` is rejected. This is a type-strictness gap, not a miss of the integer/missing/string wrong-version case.

S1's own before-refreeze observation matches the missing-key case: `FINDING CONTRACT-INVALID: pin r94-paired-crossing payload_schema_version None != 2 (full-file pin of 10 files)`. S1 does not claim the root fields are enforced by the tool, and the tool does not enforce them.

PASS — a scratch pin with the wrong `payload_schema_version` exits 2 `CONTRACT-INVALID` naming the observed value and expected 2. The version governs pin admission only; it does not select the ten-file payload, enter the digest, or get read from the contract root. Bound: float 2.0 is admitted; root `schema_version` is unread; no persisted self-test case covers the mismatch.
