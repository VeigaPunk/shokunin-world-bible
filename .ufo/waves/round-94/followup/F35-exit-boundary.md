# F35 — exit-boundary probe of `map_obligations.py`

**Seat:** F35 (exit-boundary), round-94 FOLLOW-UP verification/judging wave, lore-shokunin lane
**Role:** probe CLI edges of the new tool; confirm RESULT-line discipline and the exit-code reservation (1 = failed comparison only)
**Tool under test:** `corpus/tools/map_obligations.py` (691 lines), contract `corpus/tools/map-obligations-contract.json`
**Repo state at probe time:** HEAD `65a93298cb100fdbf5732ac6de55f01a683c02d8`; `git status --porcelain` before my runs showed only `?? .ufo/waves/round-94/followup/` (the follow-up wave's own untracked dir)
**Environment:** Python 3.14.7, all commands run from repo root
**Method:** every invocation was a real subprocess (`subprocess.run([sys.executable, "corpus/tools/map_obligations.py", ...], capture_output=True, text=True)`), stdout/stderr captured separately. I wrote nothing except this report. All outputs below are actual observed output, quoted verbatim.

---

## 1. Mandated probes — all four behave as specified

### P1 — no argument (expected: exit 2, RESULT ERROR) — PASS

```
$ python3 corpus/tools/map_obligations.py
exit=2
stdout='FINDING invalid_arguments: cluster directory is required\nRESULT ERROR\n'
stderr=''
RESULT_line_count=1  last_stdout_line='RESULT ERROR'
```

### P2 — nonexistent fixture path (expected: exit 2) — PASS

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-no-such-cluster-xyz
exit=2
stdout="FINDING cluster_missing: cannot resolve cluster: [Errno 2] No such file or directory: '/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r94-no-such-cluster-xyz'\nRESULT ERROR\n"
stderr=''
RESULT_line_count=1  last_stdout_line='RESULT ERROR'
```

Related boundary (extra probe F): a path that exists but is a file, not a directory:

```
$ python3 corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json
exit=2
stdout='FINDING cluster_missing: cluster is not a directory\nRESULT ERROR\n'
stderr=''
RESULT_line_count=1  last_stdout_line='RESULT ERROR'
```

### P3 — unknown flag (expected: exit 2) — PASS, both alone and with a cluster

```
$ python3 corpus/tools/map_obligations.py --definitely-not-a-flag
exit=2
stdout='FINDING invalid_arguments: unrecognized arguments: --definitely-not-a-flag\nRESULT ERROR\n'
stderr=''
RESULT_line_count=1  last_stdout_line='RESULT ERROR'

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing --definitely-not-a-flag
exit=2
stdout='FINDING invalid_arguments: unrecognized arguments: --definitely-not-a-flag\nRESULT ERROR\n'
stderr=''
RESULT_line_count=1  last_stdout_line='RESULT ERROR'
```

### P4 — `--frozen` with missing dir (expected: exit 2) — PASS

```
$ python3 corpus/tools/map_obligations.py --frozen corpus/fixtures/r94-no-such-frozen-xyz
exit=2
stdout='FINDING snapshot_tampered: frozen snapshot directory is missing or unreadable\nRESULT ERROR\n'
stderr=''
RESULT_line_count=1  last_stdout_line='RESULT ERROR'
```

---

## 2. RESULT-line discipline: exactly one terminal RESULT line on every operational path

Across **20 operational invocations** (all probes in this report except `--help`; see §5), every run produced:

- exactly one line starting with `RESULT `,
- it was the **last non-empty stdout line**,
- stderr was **empty** in all 20 runs,
- no `Traceback` in any stdout.

The tool's own self-test asserts this per-case too (`map_obligations.py:625-635`: `len(result_lines) == 1` and `result_lines[0] == f"RESULT {RESULTS[expectation['exit']]}"` and `not result.stderr`), and its 20/20 pass (§4) is evidence those assertions held for every isolated case.

Extra edge probes, all exit 2, one terminal `RESULT ERROR` each (quoted):

```
H --self-test --frozen x            -> exit=2 'FINDING invalid_arguments: --self-test cannot be combined with cluster, --map, or --frozen\nRESULT ERROR\n'
I <cluster> --frozen <snapshot>     -> exit=2 'FINDING invalid_arguments: --frozen cannot be combined with cluster or --map\nRESULT ERROR\n'
J --map claim-excerpt-map.md        -> exit=2 'FINDING invalid_arguments: cluster directory is required\nRESULT ERROR\n'
K <r94 cluster> --map nope.md       -> exit=2 "FINDING map_missing: cannot resolve map: [Errno 2] No such file or directory: '<cwd>/corpus/fixtures/r94-paired-crossing/nope.md'\nRESULT ERROR\n"
L <r94 cluster> --map /etc/hostname -> exit=2 'FINDING foreign_path: map path is outside the cluster\nRESULT ERROR\n'
M --frozen /tmp                     -> exit=2 'FINDING unsafe_path: frozen snapshot must be inside the owning repository\nRESULT ERROR\n'
N --frozen <contract .json file>    -> exit=2 'FINDING snapshot_tampered: frozen snapshot path is not a directory\nRESULT ERROR\n'
Q --frozen                          -> exit=2 'FINDING invalid_arguments: argument --frozen: expected one argument\nRESULT ERROR\n'
R <cluster> --map                   -> exit=2 'FINDING invalid_arguments: argument --map: expected one argument\nRESULT ERROR\n'
```

(All of H–R had `stderr=''` and `RESULT_line_count=1`; not repeated per line to keep this readable.)

---

## 3. Exit 1 is reserved for failed comparisons — PASS

Two independent lines of evidence:

**Code census** — exit 1 can only be produced at two sites, both comparison outcomes:

```
$ grep -n 'emit(1\|emit(0\|emit(2\|return 1\|return 2\|1 if findings\|code = 1' corpus/tools/map_obligations.py
331:    return emit(1 if findings else 0, findings)          # run_cluster
427:        code = 1 if findings else 0                       # run_frozen replay
440:            return emit(2, [*findings, mismatch])
441:        return emit(2, [mismatch])
...
668:        return emit(2, [(error.finding_id, error.detail)])   # argparse errors
683:        return emit(2, [("invalid_arguments", "cluster directory is required")])
687:        return emit(2, [(error.finding_id, error.detail)])   # ToolError
```

Every other emission is 2 (or 0 via `1 if findings else 0` with no findings). `RESULTS` at `map_obligations.py:41` maps 0/1/2 → PASS/FAIL/ERROR, consistent with the contract `corpus/tools/map-obligations-contract.json:19-23`.

**Observed runs** — all 20 operational invocations outside the self-test produced only 0 or 2; exit 1 appeared exclusively in the self-test's five comparison-failure cases (§4), each with a genuine comparison finding (`missing_obligation`, `duplicate_mapping`, `phantom_obligation`, `source_id_mismatch`, and the frozen replay of `missing_obligation`).

Read-only corpus sweep — every fixture in `corpus/fixtures/` that has a conventional map, run through the CLI:

```
corpus/fixtures/r87-myth-cluster/        maps=['claim-excerpt-map.md']       exit=2 result_lines=1 last=RESULT ERROR
corpus/fixtures/r88-m3-maya-cluster/     maps=['claim-excerpt-map.md']       exit=2 result_lines=1 last=RESULT ERROR
corpus/fixtures/r89-inspiration-paraphrase/ maps=['claim-to-excerpt-map.md'] exit=2 result_lines=1 last=RESULT ERROR
corpus/fixtures/r93-m2-kojiki-cluster/   maps=['claim-excerpt-map.md']       exit=0 result_lines=1 last=RESULT PASS
corpus/fixtures/r94-paired-crossing/     maps=['claim-excerpt-map.md']       exit=0 result_lines=1 last=RESULT PASS
SUMMARY by exit code: Counter({2: 3, 0: 2})
```

The three exit-2 fixtures are pre-existing clusters authored under older map grammars; e.g. `r88-m3-maya-cluster` (the parent that r94 continues) yields:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster
exit=2
FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
RESULT ERROR
```

That is a grammar mismatch, not a failed comparison, so it does not produce exit 1 — consistent with the reservation. (Flagging for the parent: the r88 parent fixture is not itself accepted by the new tool; only the new r94 map uses the required column grammar. This matches the contract's `map_grammar` and is not a contradiction of the C1/C2 claims, but it is a real boundary fact.) The same applies to the alternate maps:

```
O r88 --map symbolism-clause-map.md -> exit=2 'FINDING unsupported_map: map must contain exactly one JSON facts section\nRESULT ERROR\n'
P r93 --map symbolism-clause-map.md -> exit=2 'FINDING unsupported_map: map must contain exactly one JSON facts section\nRESULT ERROR\n'
```

---

## 4. Tool `--self-test` (real CLI subprocesses per case) — 20/20 PASS, observed exit=1 only for comparison failures

`python3 corpus/tools/map_obligations.py --self-test` spawns the real CLI per case (`map_obligations.py:609-621`) and reports its return code. Observed output, verbatim:

```
SELF-TEST PASS complete exit=0 findings=none
SELF-TEST PASS missing exit=1 findings=['missing_obligation']
SELF-TEST PASS duplicate exit=1 findings=['duplicate_mapping']
SELF-TEST PASS phantom exit=1 findings=['phantom_obligation']
SELF-TEST PASS source_id_mismatch exit=1 findings=['source_id_mismatch']
SELF-TEST PASS malformed_json exit=2 findings=['malformed_json']
SELF-TEST PASS co_mapped_grammar exit=2 findings=['unsupported_map']
SELF-TEST PASS legacy_grammar exit=2 findings=['unsupported_map']
SELF-TEST PASS invalid_pointer exit=2 findings=['invalid_pointer']
SELF-TEST PASS empty_segment exit=2 findings=['invalid_pointer']
SELF-TEST PASS noncanonical_index exit=2 findings=['invalid_pointer']
SELF-TEST PASS noncanonical_claim_index exit=2 findings=['invalid_pointer']
SELF-TEST PASS foreign_path exit=2 findings=['foreign_path']
SELF-TEST PASS traversal_path exit=2 findings=['unsafe_path']
SELF-TEST PASS symlink_path exit=2 findings=['unsafe_path']
SELF-TEST PASS frozen_complete exit=0 findings=none
SELF-TEST PASS frozen_tampered exit=2 findings=['snapshot_tampered']
SELF-TEST PASS frozen_missing_digests exit=2 findings=['unpinned']
SELF-TEST PASS frozen_expected_failure exit=1 findings=['missing_obligation']
SELF-TEST PASS frozen_verdict_mismatch exit=2 findings=['frozen_verdict_mismatch']
RESULT PASS
EXIT=0
```

Exit 1 occurs exactly for the five comparison-failure cases; every error case is exit 2 and the two clean cases are exit 0. The self-test emits exactly one `RESULT` line (the final `RESULT PASS`) — note it is preceded by 20 non-`RESULT` progress lines, so a naive "last line is RESULT" check must key on the `RESULT ` prefix, which it does.

**Disclosure (transient writes):** the self-test creates a `tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)` — i.e. a temp dir under the repo root — and removes it on exit (`map_obligations.py:604`). I did not write anything myself. Residue check immediately after:

```
$ ls -d map-obligations-self-test-* 2>/dev/null || echo 'no tempdirs left'
no tempdirs left
$ git status --porcelain
?? .ufo/waves/round-94/followup/
```

No residue; git status unchanged from before the run.

---

## 5. The one counterexample to the strict "every path" wording: `--help`

```
$ python3 corpus/tools/map_obligations.py --help
exit=0
stdout='usage: map_obligations.py [-h] [--map MAP] [--frozen FROZEN] [--self-test]\n ... --self-test      exercise isolated CLI cases\n'
stderr=''
RESULT_line_count=0
```

`--help` is the only probed path with **zero** RESULT lines: argparse prints usage and raises `SystemExit(0)`, which `map_obligations.py:669-670` converts to return code 0. So:

- "exactly one terminal RESULT line on every path" is true for **every operational path** (20/20 probed, plus the self-test's own per-case assertion) but **false for the argparse built-in `--help`**, which is not a comparison verdict. I report it as observed rather than smoothing the universal phrasing.
- It does not break the exit-1 reservation (no exit 1), but it does mean exit 0 is not exclusively "PASS": `--help` also exits 0.

---

## 6. r94 control run (exit-0 side of the boundary)

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
exit=0
stdout='OBLIGATIONS raw=14 mapped=14\nRESULT PASS\n'
stderr=''
RESULT_line_count=1  last_stdout_line='RESULT PASS'
```

Raw-array counts checked directly against the fixture (read-only):

```
entities=5 relations=1 timeline=3 entity_claims=5
computed obligations = 5*1 first_appearance + 5 claims + 1 relations + 3 timeline = 14
timeline ticks: [9, 9, 10]
crossing depends_on: [[], [], ['aru-ninth-bell', 'evin-ninth-bell']]
```

Consistent with the claimed 5 entities / 1 relation / 3 events and 14 obligations, and the tick-10 event depending on both tick-9 events.

The committed frozen snapshot also verifies clean:

```
$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
exit=0
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
FROZEN expected=PASS/0 findings=none matched
RESULT PASS
RESULT_line_count=1
```

(The persisted snapshot's `expected.json` pins `exit_code: 0`; no persisted snapshot pins exit 1, so direct exit-1 evidence comes from the self-test's spawned CLI subprocesses, quoted in §4.)

---

## 7. Verdict detail

| Probe | Expected | Observed | Verdict |
|---|---|---|---|
| no argument | exit 2 RESULT ERROR | exit 2, `invalid_arguments: cluster directory is required`, 1 RESULT line | PASS |
| nonexistent fixture path | exit 2 | exit 2, `cluster_missing`, 1 RESULT line | PASS |
| unknown flag (alone / with cluster) | exit 2 | exit 2, `invalid_arguments: unrecognized arguments`, 1 RESULT line each | PASS |
| `--frozen` missing dir | exit 2 | exit 2, `snapshot_tampered`, 1 RESULT line | PASS |
| exactly one terminal RESULT line | every path | true for all 20 operational paths + self-test assertions; `--help` (argparse builtin) is the sole zero-RESULT path, exit 0 | PASS (with the stated `--help` exception) |
| exit 1 reserved for failed comparisons | yes | code census: only `map_obligations.py:331,427`; observed exit 1 only in the 5 self-test comparison-failure cases; all other 20 probes exit 0/2 | PASS |

---

**Bottom line: PASS** — all four mandated edges return exit 2 with exactly one terminal `RESULT ERROR` line and empty stderr; exit 1 is produced only by failed comparisons (two code sites, five self-test cases, zero counterexamples across ~20 other invocations); the sole caveat is the argparse `--help` path, which exits 0 with zero RESULT lines and is not a comparison path.
