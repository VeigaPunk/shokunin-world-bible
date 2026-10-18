# V03 — C1 full negative battery

Axes: coverage, calibration, operability, and byte-ownership safety. Seat scope is C1 negative verification only, not an all-axis admission or C2/C3 verdict.

**Result: 73/73 scenarios matched, twice each (146 direct battery CLI calls), with stable finding IDs and byte-identical complete stdout/stderr across both repeats. All three semantic exit-1 IDs and all eleven documented exit-2 IDs were exercised.** Two additional read-only live r99 calls also passed.

## Delivered revision, ownership, and readiness

Read `LOG.md` through the round-100 declaration and T1's completed `.ufo/waves/round-100/seats/T1-chain-seven.md`; no lane `AGENTS.md` exists. The declared baseline is `fe1ce46`; actual live HEAD was `b5fe472957ab1e4e9c90f5613acc14cd24a288ae` (the round-100 declaration commit). No commit, push, network, or nested-agent call was made by this seat.

All direct shell/Python commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. All writes were confined to this exclusive report and the declared absolute scratch tree `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/`. Tool/contract/fixture mirrors were generated as new scratch files; no delivered file was edited and no live `--freeze` was invoked. Mirrored self-tests create and remove their temporary subtrees inside their own scratch roots.

Bounded poll: 20-second intervals, maximum 40 attempts; ready on attempt 10, after about 180 seconds. Both producer report and artifacts were required. Actual final polling output:

```text
POLL 10/40 reports=['.ufo/waves/round-100/seats/T1-chain-seven.md'] r99_pinned=True docs_r100=[True, True] fixture_ten=True
READY T1 artifact+report present
```

No stall-escape or all-reports poll was needed; the self-subtraction convention was therefore not applicable.

Snapshot identity:

- Delivered tool SHA-256: `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`.
- Delivered contract SHA-256: `ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5`.
- r99 aggregate payload digest: `7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e`.
- Contract has exactly seven pins; `r99-window-lapse` is pinned, whereas the real non-chain `r93-m2-kojiki-cluster` is not.

## Actual battery command and observations

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/run_negative_battery.py
```

Exit 0. Eight independent case roots were processed concurrently; each case was invoked twice sequentially against unchanged case inputs. Expected distributions were 2 clean controls, 11 semantic-failure cases, and 60 error cases. Complete observed summary:

```json
{
  "cases": 73,
  "runs": 146,
  "matching_cases": 73,
  "stable_ids": 73,
  "stable_full_output": 73,
  "contracts_unchanged": true,
  "live_inputs_unchanged": true,
  "exit1_ids": [
    "ADDITION-DETECTED",
    "ENDPOINT-CHANGE",
    "REDUCTION-DETECTED"
  ],
  "exit2_ids": [
    "CONTRACT-INVALID",
    "DIGEST-MISMATCH",
    "FILE-MISSING",
    "FIXTURE-MISSING",
    "INVALID-ARGUMENTS",
    "MALFORMED-JSON",
    "MALFORMED-MODEL",
    "PATH-MISMATCH",
    "SCOPE-REFUSED",
    "SELF-TEST-MISMATCH",
    "UNPINNED-FIXTURE"
  ],
  "failed_case_ids": []
}
```

Every invocation had exactly the expected terminal `RESULT PASS`, `RESULT FAIL`, or `RESULT ERROR`; stderr was empty and there were no tracebacks. The intentional exit-1/exit-2 results below are successful negative controls, not delivery failures.

The integral evidence annex [V03-scratch/full-transcript.md](V03-scratch/full-transcript.md) quotes **all 146 literal commands, both complete observed outputs per case, observed return codes, and stability judgments**. It is not a command plan or recollection. The machine-readable counterpart is [V03-scratch/results.json](V03-scratch/results.json); each case also has `cases/<case-id>/observed.json`. The case IDs below are exact annex headings and exact scratch directory names.

## Semantic exit-1 battery: all three stable IDs

Each row below ran twice, returned exit 1 both times, printed only the listed finding ID, and ended `RESULT FAIL`. The normal invocation is the literal per-case tool path followed by the per-case `corpus/fixtures/r99-window-lapse` path; both full commands/outputs are quoted in the annex.

| Case ID | Mutation | Observed ID, twice |
| --- | --- | --- |
| `semantic_drop_tick15_edge` | r99 `clerk-lapse-recorded.depends_on` becomes `[]` | `REDUCTION-DETECTED` |
| `semantic_add_tick15_edge` | Add `v03-phantom` to that dependency list | `ADDITION-DETECTED` |
| `semantic_remove_tick15_event` | Remove `clerk-lapse-recorded` | `REDUCTION-DETECTED` |
| `semantic_add_event_with_dependency` | Add `v03-added-event` depending on the lapse | `ADDITION-DETECTED` |
| `semantic_event_endpoint_tick` | Lapse tick 15 becomes 150 | `ENDPOINT-CHANGE` |
| `semantic_event_endpoint_entity_id` | Lapse actor becomes `aru` | `ENDPOINT-CHANGE` |
| `semantic_event_endpoint_place_id` | Lapse place becomes `salt-court` | `ENDPOINT-CHANGE` |
| `semantic_relation_endpoint_flip` | Swap relation `from`/`to` | `ENDPOINT-CHANGE` |
| `semantic_relation_remove` | Relations become `[]` | `REDUCTION-DETECTED` |
| `semantic_relation_add` | Add `aru` → `clerk-maren`, `v03-unpinned` | `ADDITION-DETECTED` |
| `semantic_precedes_digest` | Drop tick-15 dependency and change excerpt bytes | `REDUCTION-DETECTED` only; no `DIGEST-MISMATCH` |

The C1-specific discharge was independently replayed with this actual command, twice:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_drop_tick15_edge/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/semantic_drop_tick15_edge/corpus/fixtures/r99-window-lapse
```

Both observed outputs were exactly:

```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 6/7; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-lapse-recorded lost depends_on ['clerk-filing-open']
RESULT FAIL
observed_exit=1 stderr=''
```

## Exit-2 battery: every documented class

The documented ID set was taken from `dependency-freeze-contract.json`'s `precedence`, `README.md:274`, and the current gate registry. The table counts scenarios, not repeated invocations; each scenario was replayed twice and ended `RESULT ERROR`. Full commands/outputs for every individual variant appear in the annex.

| Observed stable ID | Cases / direct replays | Actual case coverage |
| --- | --- | --- |
| `CONTRACT-INVALID` | 16 / 32 | Missing/malformed/non-object contract; non-object pin; absent/absolute/out-of-scope fixture path; payload schema 1; short pinned-file list; bad content digest; omitted file digest; invalid events/event entry/relations; missing or extra self-test expectation |
| `DIGEST-MISMATCH` | 18 / 36 | A trailing newline in each of all ten declared files; absence of each of the eight non-required pinned files; changed/missing filename required in output |
| `FILE-MISSING` | 3 / 6 | Missing required `timeline.json`; missing required `relations.json`; guarded scratch `--freeze` with missing `README.md` |
| `FIXTURE-MISSING` | 1 / 2 | Absent directory with the known pinned r99 basename (`missing_known_fixture`) |
| `INVALID-ARGUMENTS` | 5 / 10 | No args; fixture plus `--freeze`; `--self-test` plus fixture; `--self-test` plus `--freeze`; unknown option |
| `MALFORMED-JSON` | 3 / 6 | Invalid timeline JSON, non-UTF-8 timeline, invalid optional `sources.json` |
| `MALFORMED-MODEL` | 8 / 16 | Timeline/relations root objects; empty/duplicate event ID; dependency not a list/empty dependency ID; non-scalar endpoint; relation missing `from` |
| `PATH-MISMATCH` | 1 / 2 | Byte-identical, same-named r99 fixture at a foreign mirror path |
| `SCOPE-REFUSED` | 3 / 6 | Foreign freeze target; `corpus/fixtures` itself; same-named nested in-scope fixture that would overwrite a different recorded path |
| `SELF-TEST-MISMATCH` | 1 / 2 | Change only persisted `self_test.expected.clean.exit` from 0 to 1 |
| `UNPINNED-FIXTURE` | 1 / 2 | Copy of the actual non-chain r93 fixture; not an invented missing basename |

Ten-file variants use the exact suffixes `entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, and `source-excerpt.md` in case IDs `digest_newline_<filename>` and `missing_<filename>`. Their complete receipts name the affected file. Missing required JSON tables produce `FILE-MISSING`; other missing pinned files produce `DIGEST-MISMATCH`. This distinction is observed, not flattened into a generic error.

Specific required non-chain command, twice:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/unpinned_real_nonchain_r93/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/unpinned_real_nonchain_r93/corpus/fixtures/r93-m2-kojiki-cluster
```

Both complete observed outputs:

```text
FINDING UNPINNED-FIXTURE: no pin for 'r93-m2-kojiki-cluster' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing', 'r99-window-lapse'])
RESULT ERROR
observed_exit=2 stderr=''
```

Specific self-test mismatch command, twice:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V03-scratch/cases/selftest_expectation_flip/corpus/tools/dependency_freeze.py --self-test
```

Both outputs included the exact lines below; complete 18-case receipts are in annex lines 1567–1627:

```text
CASE clean: exit=0 expected=1 findings=[] MISMATCH
SELF-TEST 17/18
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR
observed_exit=2 stderr=''
```

The separate clean mirror `selftest_clean_control` ran `--self-test` twice with the unchanged delivered contract and r95 base, producing 18 `CASE ... ok` lines, `SELF-TEST 18/18`, `RESULT PASS`, exit 0 both times. Thus the mismatch is induced by the isolated expectation flip, not a red delivered suite.

## Direct live receipt and preservation

After the scratch battery, this direct live command was invoked twice read-only:

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
```

Both complete outputs:

```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
observed_exit=0 stderr=''
```

The battery compares each case contract's before/after hash on both invocations, including refused freeze probes; every hash was unchanged. A separate post-battery audit verified all 73 copied tools byte-identical to the current delivered tool and all 33 original input files unchanged. Final audit also checked the two T1 documentation files against snapshot hashes. Observed output:

```text
EXPECTED_EXITS {0: 2, 1: 11, 2: 60}
REPEATS_PER_CASE [2]
LIVE_INPUT_HASHES_UNCHANGED 33
MIRROR_TOOLS_BYTE_IDENTICAL 73
FINAL_LIVE_BYTE_CHECK 33 inputs + 2 docs unchanged
```

The manifest contains the complete per-input hashes and the T1 report hash. No live `--self-test` was needed: it would create temporary root scratch outside this seat's declared writable subtree; byte-identical mirrored self-tests exercised the real CLI instead.

## Evidence and bounds

Owned deliverables:

- `.ufo/waves/round-100/seats/V03-c1-negative.md` — this report.
- `.ufo/waves/round-100/seats/V03-scratch/run_negative_battery.py` — one-shot generator/driver; it refuses to overwrite already generated files, so replay individual annex commands rather than blindly rerunning the generator in place.
- `.ufo/waves/round-100/seats/V03-scratch/manifest.json` — original source/report/document hashes, seven-pin list, revision, concurrency/repeat parameters.
- `.ufo/waves/round-100/seats/V03-scratch/results.json` — all 146 commands/outputs/exits and checks.
- `.ufo/waves/round-100/seats/V03-scratch/full-transcript.md` — integral human-readable evidence annex.
- `.ufo/waves/round-100/seats/V03-scratch/snapshot/` — immutable copies of the tool, contract, r99/r95/r93 fixture files.
- `.ufo/waves/round-100/seats/V03-scratch/cases/<case-id>/` — 73 isolated tool/contract/fixture cases plus `observed.json` per case; exact IDs are enumerated in `results.json`. Self-test temporary trees were cleaned automatically.

Evidence digests:

```text
manifest.json      5104 bytes  b0a6d7be6a880e11133ee7746eb74013a9879d63c57c36f47abb3d9b14ac96bc
results.json     169239 bytes  ff3ce469d028356445c2715490a1ed153e164ad5b200743e43b9d993ab8a121a
full-transcript.md 100711 bytes  6aeb27b08c18b3d550612c621a523849ff0c2f58984984678bda7b3abf429b91
```

No failing or inconclusive scenario remains within this seat's assigned battery. These probes demonstrate the documented CLI classes on the delivered bytes, not exhaustive fuzzing, dependency/prose semantics, source truth, chronology authentication, or C2/C3 admission. T1's tool-managed top-level contract revision refresh is disclosed in its report; this seat did not rewrite or erase it. The new r100 fixture remains outside the declared frozen chain, as documented.

PASS — 73/73 negative/control scenarios matched twice (146 CLI calls); all three semantic IDs and all eleven documented exit-2 IDs stable, including real non-chain UNPINNED; no delivered bytes changed.
