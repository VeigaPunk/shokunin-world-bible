# V76 c1-usage-surface — round 99

Seat: V76 (verifier, C1 usage surface). Lane `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5`. Commands from the lane root with `python3`. Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report and `.ufo/waves/round-99/seats/V76-scratch/` only. No live corpus file was written. Tool and contract hashes were equal before and after the final battery.

Axes probed (measurement only): exit code, RESULT-line count, traceback absence, finding identity, non-mutation of producer bytes.

Charge: no args, `--help`, unknown flags, `--freeze` without an argument, verify with a file instead of a directory — every non-clean path exits 2 with one RESULT line.

## Poll

Content gate: tool or contract hash moved off the r98 baseline (`dependency_freeze.py` `03d04365…`, contract `153ebc5b…`, 17 self-test cases, 5 JSON files per pin) and an `S1*.md` report exists. Cadence 20 s. Cap 40 tries from 22:01:41−03 (~22:15).

- 22:01:41 poll-0: tool and contract still the r98 baseline. No S reports. r99 fixture directory already present. No r99 pin.
- 22:02:01 tool hash changed (`c620324f…`, 27338 bytes); 22:02:04 it changed again (`65c1ae30…`, 29211 bytes). Contract still baseline.
- 22:04:23 contract header was schema 2 / self-test 18 / `markdown_tamper` present, but all six pins were still five-file (`payload_schema_version` absent). S3 and S4 reports present. S1 absent.
- 22:07:33 tool at `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067` (29104 bytes).
- 22:08:46 contract settled at `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628` (25987 bytes): `schema_version` 2, root `payload_schema_version` 2, six pins each `payload_schema_version` 2 with 10 files. `r99-window-lapse` not pinned. Self-test expectation count 18, including `markdown_tamper`. Contract hash did not move after this.
- 22:38:11 tool rewritten to `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c` (29110 bytes, +6). S1's report calls this the final message-string edit. Usage outcomes on this hash match the 22:31 replay of `6f81f8be…` (same exits, same finding IDs, same RESULT lines).
- S1 report `S1-full-file-pins.md` was absent through 22:31:54 and present at 22:50:49 (after the 40-try cap). S3 and S4 reports were present earlier. No other S reports observed.

Stall-escapes (recorded, not treated as fatal): the first poller was stopped after try 3 because it sampled hashes only after a 20 s sleep and missed a mid-write; poll2's shell timeout killed it at try 15 (300 s) in the same minute the six pins became full-file; poll3's cap epoch was wrong (`1760750130` vs local `1792286130`) and exited immediately at 22:14:42. Manual checks continued at 22:20, 22:22, 22:31, 22:41, and 22:50. No all-reports poll was run, so SELF subtraction did not apply.

S1's own report says `r99-window-lapse` was not pinned (C1's chain is the existing six). That matches the contract. S1 does not state a CLI usage-exit contract beyond the persisted `invalid_arguments` self-test case. No contradiction with the battery below.

## Bytes measured

Final battery (probe script, after the 22:38 edit; `TOOL_UNCHANGED True`, `CONTRACT_UNCHANGED True`):

```
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
```

Reconfirmed at 22:50:49, same pair, with `S1-full-file-pins.md` present. CLI in `main` (`corpus/tools/dependency_freeze.py:633-654`): optional `fixture`, `--freeze DIR`, `--self-test`. `CliParser.error` raises `ToolError("INVALID-ARGUMENTS")`, and `main` emits exit 2. Argparse `--help` calls `sys.exit(0)` inside `parse_args`, before that handler.

`corpus/tools/README.md` and `SKILL.md` had no Round 99 / `payload_schema` / `markdown_tamper` text at measurement time (S2 not observed; S1 says it did not write those files). The README freeze paragraph at line 274 is still the r98 exit-2 order. It does not claim `--help` exits 2. Not scored.

## Required invocations

Quoted block is the 22:31:54−03 replay (`6f81f8be…`). The 22:41 probe on `fb9bb9ff…` reproduced the same stdout, the same exit, one `RESULT ERROR`, empty stderr, no traceback, for each of these five. Working directory `/home/vgpnk/Projects/shokunin/lore-shokunin`.

no args — exit 2, one RESULT line:

```
$ python3 corpus/tools/dependency_freeze.py
FINDING INVALID-ARGUMENTS: expected a fixture directory, --freeze DIR, or --self-test
RESULT ERROR
EXIT 2
```

`--help` — clean path, exit 0, zero RESULT lines (not a non-clean path):

```
$ python3 corpus/tools/dependency_freeze.py --help
usage: dependency_freeze.py [-h] [--freeze DIR] [--self-test] [fixture]

Freeze or verify per-fixture dependency inventories.

positional arguments:
  fixture       fixture directory to verify against its pin

options:
  -h, --help    show this help message and exit
  --freeze DIR  (re)build the pin for DIR (delivery-time only)
  --self-test   run isolated cases against persisted expectations
EXIT 0
```

unknown flag — exit 2, one RESULT line:

```
$ python3 corpus/tools/dependency_freeze.py --not-a-flag
FINDING INVALID-ARGUMENTS: unrecognized arguments: --not-a-flag
RESULT ERROR
EXIT 2
```

`--freeze` without an argument — exit 2, one RESULT line:

```
$ python3 corpus/tools/dependency_freeze.py --freeze
FINDING INVALID-ARGUMENTS: argument --freeze: expected one argument
RESULT ERROR
EXIT 2
```

verify with a file instead of a directory — exit 2, one RESULT line. Finding is `UNPINNED-FIXTURE` because `pin_for` keys on `Path.name` before `is_dir()` (`dependency_freeze.py:349-373`):

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath/timeline.json
FINDING UNPINNED-FIXTURE: no pin for 'timeline.json' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing'])
RESULT ERROR
EXIT 2
```

The absolute path of the same file produced the same finding and exit (probe case `verify-file`). A file whose basename matches a pin, and a missing path whose basename matches a pin, both exit 2 with one `RESULT ERROR` and `FINDING FIXTURE-MISSING` (probe cases `verify-file-pin-basename`, `verify-missing-pin-basename`). `--freeze` of `corpus/fixtures/r95-crossing-aftermath/timeline.json` exits 2 `FIXTURE-MISSING` and did not change the contract hash.

## Adjacent usage cases (probe script on `fb9bb9ff…`)

All from `python3 corpus/tools/dependency_freeze.py`. Every non-help row: exit 2, exactly one stdout `RESULT ERROR`, stderr empty, traceback 0. Full transcripts: `V76-scratch/usage-probe-final.txt` (overwritten by the post-edit probe; header records `TOOL_SHA_BEFORE fb9bb9ff…`).

| case | exit | RESULT lines | finding |
|---|---|---|---|
| `-h` | 0 | 0 | — |
| `--help --freeze` | 0 | 0 | — (argparse help short-circuits; the missing `--freeze` argument is not reported) |
| `-z` | 2 | 1 | INVALID-ARGUMENTS unrecognized arguments: -z |
| `--bogus <fixture-dir>` | 2 | 1 | INVALID-ARGUMENTS |
| `<fixture-dir> --bogus` | 2 | 1 | INVALID-ARGUMENTS |
| `--nope=1` | 2 | 1 | INVALID-ARGUMENTS |
| `--freeze=` | 2 | 1 | INVALID-ARGUMENTS (empty string is falsy; message is the no-args message, not "expected one argument") |
| `--freeze --` | 2 | 1 | INVALID-ARGUMENTS argument --freeze: expected one argument |
| `--` | 2 | 1 | INVALID-ARGUMENTS no-args message |
| `--freeze <dir> <dir>` | 2 | 1 | INVALID-ARGUMENTS pass either a fixture or --freeze DIR, not both |
| two fixture positionals | 2 | 1 | INVALID-ARGUMENTS unrecognized arguments |
| `--self-test <dir>` | 2 | 1 | INVALID-ARGUMENTS --self-test cannot be combined |
| `--self-test --freeze <dir>` | 2 | 1 | INVALID-ARGUMENTS --self-test cannot be combined |
| `--freeze` missing in-scope dir | 2 | 1 | FIXTURE-MISSING (contract hash unchanged) |
| unpinned missing path | 2 | 1 | UNPINNED-FIXTURE |

Help is the only probed path that exits 0. It never emits a RESULT line. That matches the sibling note already written for `map_obligations.py` in `corpus/tools/README.md:99` ("`--help` exits 0 with zero RESULT lines, so exit 0 alone is not a PASS"). It is not a miss of "non-clean paths exit 2".

## What this seat did not prove

- `--self-test` itself was not run here (S1 reports 18/18 exit 0; this seat did not replay it). Combining it with other args exits 2 before the self-test body.
- Docs (S2) were not updated at measurement time. Not a usage-surface fail.
- A file path whose basename is not a pin name is reported as `UNPINNED-FIXTURE`, not as "not a directory". The directory check runs only after the name binds to a pin. Both shapes still exit 2 with one RESULT line.

Bottom line: PASS — on delivered bytes `fb9bb9ff…` / `8c2561b0…` (S1 report present, post final message-string edit), every probed non-clean path exits 2 with exactly one `RESULT ERROR` and no traceback; `--help`/`-h` exit 0 with zero RESULT lines and are not non-clean paths.
