# V04 c1-selftest — round 99

- Seat: V04 c1-selftest (verifier, leaf). Lane repo
  `/home/vgpnk/Projects/shokunin/lore-shokunin`. Commands from the lane root
  with `python3` unless a scratch mirror's own tool is the subject. Baseline
  r98 closure `4265df5` (HEAD during the seat
  `337f0fa52b02626b7687eedbb2d99fab30446fe4`, the blocked-dispatch
  zero-increment commit; `git diff 4265df5 -- corpus/tools/dependency_freeze.py
  corpus/tools/dependency-freeze-contract.json` was empty before S1 wrote).
  No commits, no pushes, no network, no nested agents.
- Revision verified, equal before and after every probe, and still equal at
  the 23:06:45 reconfirm:
  `corpus/tools/dependency_freeze.py` sha256
  `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`;
  `corpus/tools/dependency-freeze-contract.json` sha256
  `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`.
  S1 report `S1-full-file-pins.md` sha256
  `1fda9ff7f02e75c9b34d0f0e514cbc8f799f596bb0cedc2d363fd6f33aee54a3`
  (11971 bytes, mtime 2026-10-17 22:48:57 -0300). That report describes the
  post-edit tool ("Re-run after the final detail-string edit: same 18/18").
- Writes: this report and `.ufo/waves/round-99/seats/V04-scratch/` only
  (poll log, baseline self-test log, `verify.py`, repro and perturb mirrors).
  The delivered tool and contract were not mutated (sha256 checked before and
  after).

Axes named, not scored: (1) self-test completeness, (2) inherited-expectation
identity, (3) Markdown-tamper expectation correctness, (4) fail-closed on a
scratch perturbation, (5) `corpus/` hash stability. No axis was harmed.

## 0. Poll-wait (20 s cadence; artifacts AND an S1 report; never a plan)

Log: `.ufo/waves/round-99/seats/V04-scratch/poll.log`.

- Tries 1–2 (22:01:26–22:01:46): both files still r98
  (`03d04365…` / `153ebc5b…`). No S1 report.
- Tries 3–22: tool moved `65c1ae30…` → `1728ed89…` → `6f81f8be…`; contract
  moved `73b28933…` → `8f9c1f53…` → `8c2561b0…`. Not verified (mid-write).
- Try 23 (22:08:46) was a false hit: the poll matched the directory
  `S1-scratch`, not a report. Recorded, not counted as delivery.
- Tries 24–40 (22:19:09–22:24:29), report required to be a file `S1*.md`:
  `s1_md=0` every try. Tool/contract stable at `6f81f8be…` / `8c2561b0…`
  from try 24 through try 40. `POLL_ABSENT tries=40`.
- Bounded stall-escape, 8 tries (22:43:15–22:45:35), recorded not fatal.
  The tool had already moved to `fb9bb9ff…` (mtime 22:38:11; the only diff
  against a saved `6f81f8be…` copy is the digest detail suffix, below).
  Report still absent. `STALL-ESCAPE-EXHAUSTED`.
- Post-escape confirmation at 22:49:30 found
  `.ufo/waves/round-99/seats/S1-full-file-pins.md`. Verification below is of
  that report plus the hash pair that was stable from the stall-escape
  through 23:06:45. The LOG.md declaration was not treated as the delivery.

The `6f81f8be…` → `fb9bb9ff…` diff (against
`.ufo/waves/round-99/seats/V62-scratch/mirror/corpus/tools/dependency_freeze.py`,
sha256 confirmed `6f81f8be…`) is one string:

```
-                  "fixture bytes changed outside the frozen inventory")])
+                  "pinned-file bytes changed outside the semantic inventory")])
```

## 1. `--self-test` 18/18 PASS

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE clean: exit=0 expected=0 findings=[] ok
CASE reduction_edge_drop: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE addition_edge_phantom: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE event_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE event_endpoint_change: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_endpoint_flip: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE relation_added: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE digest_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
CASE malformed_json: exit=2 expected=2 findings=['MALFORMED-JSON'] ok
CASE missing_timeline: exit=2 expected=2 findings=['FILE-MISSING'] ok
CASE unpinned_fixture: exit=2 expected=2 findings=['UNPINNED-FIXTURE'] ok
CASE missing_fixture: exit=2 expected=2 findings=['FIXTURE-MISSING'] ok
CASE invalid_arguments: exit=2 expected=2 findings=['INVALID-ARGUMENTS'] ok
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
EXIT:0
```

Run at 2026-10-17T23:06:45-03:00. Same 18/18 exit 0 from the earlier battery
in `V04-scratch/verify.py` (log `delivered-selftest.log`). No
`dependency-freeze-self-test-*` residue at the repo root after either run.

## 2. Seventeen inherited cases: byte-identical expectations

Baseline CASE lines were captured before S1 wrote, on the r98 bytes
(`03d04365…` / `153ebc5b…`): `python3 corpus/tools/dependency_freeze.py
--self-test` → `SELF-TEST 17/17` / `RESULT PASS` / exit 0
(`V04-scratch/baseline-selftest.log`).

The 17 inherited `CASE` lines of the delivered run are byte-identical to
that log (`inherited_case_lines_byte_identical True`). The only added line
is `CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok`.

Persisted expectations versus
`git show 4265df5:corpus/tools/dependency-freeze-contract.json`: the 17
inherited objects are parsed-equal, and each object's raw file slice
(`"<key>": {` through the matching `}`) is byte-identical
(`file_slice_byte_identical True`). Added key only: `markdown_tamper`.
Removed: none. `self_test.base_fixture` remains `r95-crossing-aftermath`.

## 3. Hand-derived Markdown-tamper expectation

Case source (delivered tool, lines 576–580): mirror the tool, contract, and
`r95-crossing-aftermath`; append one byte `0x0a` to `fictional-excerpts.md`;
verify; expect exit 2.

Derivation, not copied from the contract. All ten pin file hashes of
`r95-crossing-aftermath` match the live fixture bytes. Content digest is
sha256 of `json.dumps({name: file_sha256}, sort_keys=True, separators=(",", ":"))`.
Live digest equals the pin `97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710`.
Appending `b"\n"` changes only `fictional-excerpts.md`
`0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282` →
`a89d278834f74cdeb87d0a46fca94cfd41a0f7cc4fa1c565b2b50c2b5912d7db`.
Markdown is not in the semantic inventory, so `compare()` is empty and the
digest branch fires. Predicted line:

```
FINDING DIGEST-MISMATCH: content digest dbf67f5c107b19eea87ad5311e634db2ae54b8760a92c0430060e61635ad6102 != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: fictional-excerpts.md (sha256 0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282 -> a89d278834f74cdeb87d0a46fca94cfd41a0f7cc4fa1c565b2b50c2b5912d7db); pinned-file bytes changed outside the semantic inventory
```

That is exit 2, finding id `DIGEST-MISMATCH` only, and the changed-file name
`fictional-excerpts.md`. The persisted object matches:

```
{"exit": 2, "finding_ids": ["DIGEST-MISMATCH"], "forbid_traceback": true, "names_file": "fictional-excerpts.md"}
```

Independent reproduction (scratch mirror, live fixture not edited):

```
$ python3 .ufo/waves/round-99/seats/V04-scratch/repro/corpus/tools/dependency_freeze.py \
    .ufo/waves/round-99/seats/V04-scratch/repro/corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest dbf67f5c107b19eea87ad5311e634db2ae54b8760a92c0430060e61635ad6102 != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: fictional-excerpts.md (sha256 0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282 -> a89d278834f74cdeb87d0a46fca94cfd41a0f7cc4fa1c565b2b50c2b5912d7db); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT=2
```

`REPRO_MATCHES_HAND_DERIVED True`. One finding. The filename is in the
`changed:` clause, not only somewhere in the process output.

## 4. Perturb in scratch → fails closed

Delivered tool and contract were not the subjects. Both probes copy them
under `V04-scratch/` and leave the lane hashes unchanged
(`live_tool_unchanged True`, `live_contract_unchanged True`).

Expectation perturb: scratch contract sets `markdown_tamper.names_file` to
`README.md` (the case still appends the newline). 

```
$ python3 .ufo/waves/round-99/seats/V04-scratch/perturb-expect/corpus/tools/dependency_freeze.py --self-test
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] MISMATCH
  observed stdout: [..., 'FINDING DIGEST-MISMATCH: content digest dbf67f5c… != pin 97cffd7b…; changed: fictional-excerpts.md (sha256 0ef6734a… -> a89d2788…); pinned-file bytes changed outside the semantic inventory', 'RESULT ERROR']
SELF-TEST 17/18
FINDING SELF-TEST-MISMATCH: cases failed: ['markdown_tamper']
RESULT ERROR
EXIT=2
```

The other 17 cases stayed `ok`. Exit is 2, not a false PASS. The mismatch
is the `names_file` check: exit and finding id already matched.

Behavior perturb: scratch tool replaces
`excerpt.write_bytes(excerpt.read_bytes() + b"\n")` with a no-op write of
the same bytes. Contract expectation left as delivered.

```
$ python3 .ufo/waves/round-99/seats/V04-scratch/perturb-noop/corpus/tools/dependency_freeze.py --self-test
CASE markdown_tamper: exit=0 expected=2 findings=[] MISMATCH
  observed stdout: ['FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1', 'DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710', 'RESULT PASS']
SELF-TEST 17/18
FINDING SELF-TEST-MISMATCH: cases failed: ['markdown_tamper']
RESULT ERROR
EXIT=2
```

A tamper that does not change bytes is not reported as the Markdown-tamper
case passing. Fail-closed.

## 5. `corpus/` hash-stable

Immediately before and after the battery's `--self-test`, sha256 of every
file under `corpus/` (1843 files) was identical
(`corpus_index_equal True`; indexes
`V04-scratch/corpus-before-selftest.sha256` and
`corpus-after-selftest.sha256`). Tool and contract sha256 unchanged.
No self-test temp dir left behind. An earlier index at 22:30 had 1841
files; that delta is outside the self-test bracket and is other seats'
writes, not this probe.

## 6. Bound (not a fail)

`names_file` is a substring test of stdout+stderr
(`names_file in output`), not a parse of the `changed:` list. For this
case the reproduced finding names `fictional-excerpts.md` in `changed:`,
and the expectation perturb shows the check is load-bearing. A coincidental
mention of the same filename elsewhere in the output would also satisfy it.
Recorded; it does not make the 18/18 result a false pass.

## Bottom line

**PASS** — on `fb9bb9ff…` / `8c2561b0…`, after `S1-full-file-pins.md` landed, `--self-test` is 18/18 exit 0; the 17 inherited CASE lines and expectation-object slices are byte-identical to the r98 baseline; the hand-derived Markdown-tamper line matches a scratch reproduction byte-for-byte (exit 2 `DIGEST-MISMATCH` naming `fictional-excerpts.md`); both scratch perturbations fail closed (exit 2 `SELF-TEST-MISMATCH`, 17/18); `corpus/` was hash-stable across the run.
