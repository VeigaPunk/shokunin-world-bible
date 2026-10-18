# V108 c1-tamper-restore

Seat: V108. Claim under test: C1 verify has no latch / remembered dirty state. Method: tamper then restore on a scratch mirror only; a later verify must be clean again.

Axes: detectability (edit → exit 2 naming the file), no-latch (restore → exit 0; partial restore drops only the restored name), isolation (scratch mirror; live tool/contract hashes unchanged), statelessness (verify does not rewrite the pin or add sidecars).

## Poll

40 tries, 20 s cadence, `2026-10-17T22:02:26-03:00` → `POLL-EXHAUSTED 2026-10-17T22:15:27-03:00`. Log: `.ufo/waves/round-99/seats/V108-scratch/poll.log`.

Present and hash-stable from try 24 through try 40, and still those hashes at the `2026-10-17T22:29:12-03:00` recheck:

- `corpus/tools/dependency_freeze.py` sha256 `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067` (29104 bytes). Contains `PINNED_FILES` (five JSON + five Markdown) and self-test case `markdown_tamper`.
- `corpus/tools/dependency-freeze-contract.json` sha256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628` (25987 bytes). `schema_version` 2, `payload_schema_version` 2. Pins: `r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`, `r97-crossing-acknowledgment`, `r98-clerk-filing`. No `r99-window-lapse` pin.

Producer reports at poll end and at 22:29:12:

- `S1-freeze-hygiene.md` ABSENT
- `S2-tools-docs.md` ABSENT
- `S3-fixture-author.md` present (5069 bytes)
- `S4-fixture-docs.md` present (9303 bytes)
- `S5-knowledge-notes.md` ABSENT

Stall-escape (recorded, not fatal): S1's narrative report never landed, but the C1 bytes were stable for >7 minutes after try 24. Verified those delivered bytes. Did not verify a plan and did not run `--freeze` on the lane tree.

## Setup

Scratch mirror only: `.ufo/waves/round-99/seats/V108-scratch/mirror/`. Copied the delivered tool, contract, and fixtures `r94`–`r99` plus `r88`. Tool `ROOT` is the mirror (`Path(__file__).parents[2]`), so pins bind inside the mirror. Harness: `.ufo/waves/round-99/seats/V108-scratch/tamper_restore.py`. Lane cwd. `python3`.

Live hashes before and after the harness were identical (`LIVE_UNCHANGED True`):

```
LIVE_BEFORE {'tool': '6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067', 'contract': '8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628'}
LIVE_AFTER  {'tool': '6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067', 'contract': '8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628'}
```

## Baseline (scratch mirror, delivered pins)

Each command is `python3 <mirror>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/<name>`.

| fixture | exit | result |
|---|---|---|
| r94-paired-crossing | 0 | `RESULT PASS` digest `048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef` |
| r95-crossing-aftermath | 0 | `RESULT PASS` digest `97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710` |
| r96-crossing-response | 0 | `RESULT PASS` digest `43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c` |
| r97-crossing-acknowledgment | 0 | `RESULT PASS` digest `a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54` |
| r98-clerk-filing | 0 | `RESULT PASS` digest `5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0` |
| r88-m3-maya-cluster | 0 | `RESULT PASS` digest `acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae` |
| r99-window-lapse | 2 | `FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse'` |

r99 is a delivery gap for the declared 6/6 re-freeze. It is not a latch finding. Tamper-restore used pinned `r98-clerk-filing` (clean baseline), then a second pin `r95-crossing-aftermath`.

## Tamper-then-restore (r98-clerk-filing)

Target pin digest throughout: `5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0`. Each verify is a new process. Edits are byte appends on the scratch copy; restore writes the original bytes back.

1. Append `\nV108-TAMPER fictional-excerpts\n` to `fictional-excerpts.md`.

```
EXIT 2
FINDING DIGEST-MISMATCH: content digest ef0a7f1a39a306dc06eb74f2a8722865c3fee18371ccf9d6b4585d3bf28a13ea != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: fictional-excerpts.md (sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> 9660d381e09b40c14f7eb3e67ee653bad06ec1a8d9e832c681188a83da457d1c); fixture bytes changed outside the frozen inventory
RESULT ERROR
```

Names only `fictional-excerpts.md`. Inventory line stayed `events 7/7; dependency-edges 6/6; relations 1/1` (not a semantic FAIL).

2. Restore `fictional-excerpts.md` (4187 bytes, sha256 `29e384bf…`).

```
EXIT 0
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
```

3. After that clean restore, append `\nV108-TAMPER readme\n` to `README.md`. Exit 2, `DIGEST-MISMATCH`, changed file is only `README.md` (`32efc78f…` → `772268bf…`). The prior fictional-excerpts tamper is not remembered. Restore `README.md` → exit 0, same pin digest.

4. Tamper `source-excerpt.md` and `claim-excerpt-map.md` together. Exit 2 names both:

```
changed: claim-excerpt-map.md (sha256 c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba -> c0ffbbeb9f6ec16be2057ae4bae91cde85fd277d651fefd3c147bb21d16b2867), source-excerpt.md (sha256 b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd -> 9c0fce7b244e9029505411d5825998762a0868d01c091dea2d4c3378498a82e8)
```

Restore only `source-excerpt.md`. Next process exit 2 names only `claim-excerpt-map.md` (no `source-excerpt.md (sha256` residue). Restore `claim-excerpt-map.md` → exit 0, digest `5ecf84e1…`.

5. Re-tamper `inspiration-note.md` after a clean pass (no sticky-clean). Exit 2 names only `inspiration-note.md`. Restore → exit 0, digest `5ecf84e1…`.

6. Append one newline to `contradictions.json` (semantic inventory unchanged: still 7/7, 6/6, 1/1; no `REDUCTION-DETECTED` / `ADDITION-DETECTED` / `ENDPOINT-CHANGE`). Exit 2 names only `contradictions.json` (`37517e5f…` → `5239a775…`). Restore the 3 original bytes → exit 0, digest `5ecf84e1…`.

After all cycles:

```
CONTRACT_SHA_AFTER 8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628
CONTRACT_UNCHANGED True
TREE_ADDED []
TREE_REMOVED []
FIXTURE_BYTES_RESTORED True
FAILURES []
HARNESS_RESULT PASS
```

Verify did not rewrite the pin and did not create a sidecar. `verify()` in the delivered tool only prints; the only contract write is `--freeze`, which this seat did not invoke.

## Second pin (r95-crossing-aftermath)

Same scratch tool, fresh processes, `2026-10-17T22:29:12-03:00`:

- clean: exit 0, digest `97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710`
- append `\nV108-R95-TAMPER\n` to `fictional-excerpts.md`: exit 2, `DIGEST-MISMATCH`, changed `fictional-excerpts.md` (`0ef6734a…` → `68e1cda8…`)
- restore original 1845 bytes (sha256 match True): exit 0, digest `97cffd7b…` again

A following r98 verify was still exit 0, digest `5ecf84e1…`. The r95 cycle did not stick to the other pin.

## Not claimed

- Not a 6/6 chain result. `r99-window-lapse` is unpinned (exit 2 `UNPINNED-FIXTURE`).
- S1/S2/S5 producer reports were absent. This seat verified stable delivered bytes, not those reports.
- No lane `--freeze`, no self-test (self-test writes a temp dir under the tool root). Live tool and contract hashes unchanged.

PASS — scratch tamper-then-restore returns exit 0 with the original pin digest; mismatch names only still-dirty files; no latch.
