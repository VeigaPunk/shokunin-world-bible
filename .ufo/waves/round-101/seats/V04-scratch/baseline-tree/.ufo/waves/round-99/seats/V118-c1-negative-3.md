# V118 c1-negative-3 — round 99

Seat: V118 c1-negative-3 (verifier, read-only on lane bytes; leaf seat). Lane `/home/vgpnk/Projects/shokunin/lore-shokunin`. Commands with `python3`. Baseline r98 closure `4265df5`. No commits, no pushes, no network, no nested agents.

Question: exit-2 class completeness against the contract `precedence` text — every documented exit-2 ID demonstrated live, and the first-failing-check order checked where two classes could fire.

Revision scored (equal before and after every probe, and equal to the bytes S1's report describes as the post message-string edit):

- `corpus/tools/dependency_freeze.py` sha256 `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`
- `corpus/tools/dependency-freeze-contract.json` sha256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`

Writes: this report, and scratch under `.ufo/waves/round-99/seats/V118-scratch/` (poll log, matrix, mirrors). Delivered tool/contract were not written. A refused `--freeze` on the delivered tool left the contract hash unchanged (`DELIVERED_CONTRACT_UNCHANGED_AFTER_REFUSED_FREEZE True`).

Axes: completeness (every precedence exit-2 ID live), fidelity (first failing check vs the precedence sentence), isolation (mutations only in scratch mirrors).

## 0. Poll-wait

Cadence 20s, 40 tries. Log `.ufo/waves/round-99/seats/V118-scratch/poll.log`. Tries 1–15 were the first poller (killed by its 300s tool timeout at try 15, not by the protocol cap). Tries 16–40 continued in a second poller and exhausted:

```
try=1  t=22:02:21 report=none tool=changed ct=same    toolsha=65c1ae309385feed ctsha=153ebc5b2092948e
try=5  t=22:03:41 report=none tool=changed ct=same    toolsha=1728ed892442c498
try=7  t=22:04:21 report=none tool=changed ct=changed toolsha=1728ed892442c498 ctsha=73b28933f1488280
try=8  t=22:04:41 report=none tool=changed ct=changed toolsha=1728ed892442c498 ctsha=8f9c1f5316141b61
try=16 t=22:25:10 report=none toolsha=6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067 ctsha=8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628
try=40 t=22:33:10 report=none same hashes as try=16
POLL_EXHAUSTED tries=16-40
```

S1's report was absent through try 40. After the window the tool moved one detail string (`6f81f8be…` → `fb9bb9ff…`: `fixture bytes changed outside the frozen inventory` → `pinned-file bytes changed outside the semantic inventory`). Contract hash did not move. Bounded stall-escape, recorded, not fatal: the matrix was re-run on `fb9bb9ff…` / `8c2561b0…` (77/77, hashes unchanged across the run). At scoring (23:04) `S1-full-file-pins.md` was present (mtime 22:48) and S2's report was still absent. No all-reports poll; dependency was S1. The scored bytes are the post-edit pair, not a plan.

## 1. Documented exit-2 set

Precedence text (contract, quoted in full from the scored file):

> semantic inventory findings decide first (exit 1: REDUCTION-DETECTED, ADDITION-DETECTED, ENDPOINT-CHANGE); a content digest change the semantic inventory does not model exits 2 (DIGEST-MISMATCH) and names each changed pinned file, including the five Markdown files. Exit-2 (could-not-evaluate) checks run in this order and the first failing check decides: UNPINNED-FIXTURE (no pin for the fixture name) or CONTRACT-INVALID (unreadable contract, invalid pin, payload_schema_version other than 2, or a pin that does not digest all ten pinned files), FIXTURE-MISSING (fixture directory absent), PATH-MISMATCH (invoked path differs from the pin's recorded path), FILE-MISSING / MALFORMED-JSON / MALFORMED-MODEL (model build of the JSON tables), DIGEST-MISMATCH (inventory clean, any pinned-file bytes changed or missing), INVALID-ARGUMENTS (CLI usage), SELF-TEST-MISMATCH (--self-test observed outcome differs from the persisted case expectation); --freeze additionally raises SCOPE-REFUSED (target outside corpus/fixtures/**, or a same-named in-scope target that would rewrite an existing pin's recorded path) and FILE-MISSING when a declared pinned file is absent. A path-less legacy pin is migrated in place by --freeze instead of refused. Re-freeze is the payload upgrade path from a schema-1 JSON-only pin to payload_schema_version 2.

Parsed finding IDs: the three exit-1 IDs plus these 11 exit-2 IDs, no extras (`PRECEDENCE_MISSING_FROM_TEXT []`, `PRECEDENCE_EXTRA_IDS []`):

`UNPINNED-FIXTURE`, `CONTRACT-INVALID`, `FIXTURE-MISSING`, `PATH-MISMATCH`, `FILE-MISSING`, `MALFORMED-JSON`, `MALFORMED-MODEL`, `DIGEST-MISMATCH`, `INVALID-ARGUMENTS`, `SELF-TEST-MISMATCH`, `SCOPE-REFUSED`.

Code literals (`fail("…")` plus emit tuples) are exactly those 11 plus the three exit-1 IDs. No exit-2 ID is emitted that the precedence text does not name, and none that it names is absent from the code.

Self-test (18 cases) pins 9 of the 11 exit-2 IDs. Not persisted as their own cases: `CONTRACT-INVALID`, `MALFORMED-MODEL`. Both were hand-demonstrated below. `markdown_tamper` adds `names_file: fictional-excerpts.md`, which the runner consults (`names_file in output`).

`corpus/tools/README.md` and `SKILL.md` had no r99 freeze row at scoring (`DOC_HAS_R99 False` both; S2 report absent). README's historical text names the same 11 exit-2 IDs and no extra. SKILL names a subset (`DIGEST-MISMATCH`, `PATH-MISMATCH`, `SCOPE-REFUSED`, `SELF-TEST-MISMATCH`) and no extra. The documented set scored is the precedence text.

## 2. Method

Harness `.ufo/waves/round-99/seats/V118-scratch/exit2_matrix.py`, log `matrix.log`. It copies the scored tool, contract, and six chain fixtures into scratch and mutates only those copies. Delivered-entrypoint rows that cannot write (or that refuse before write) run the lane tool directly. Full log has every command. Compact result: 77 rows, 0 FAIL. Re-run on `fb9bb9ff…` is the scored log (`END tool=fb9bb9ff… unchanged=True`, `END contract=8c2561b0… unchanged=True`).

Clean chain on the delivered tool, all `RESULT PASS` exit 0, digests identical to S1's report:

| fixture | digest | exit |
|---|---|---|
| r88-m3-maya-cluster | `acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae` | 0 |
| r94-paired-crossing | `048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef` | 0 |
| r95-crossing-aftermath | `97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710` | 0 |
| r96-crossing-response | `43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c` | 0 |
| r97-crossing-acknowledgment | `a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54` | 0 |
| r98-clerk-filing | `5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0` | 0 |

Mirror `--self-test` of the scored tool: `SELF-TEST 18/18` / `RESULT PASS` / exit 0, including `CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok`.

## 3. Every exit-2 ID, live

Each row is exit 2, `RESULT ERROR`, and that finding ID. Commands are the ones the harness actually ran.

**INVALID-ARGUMENTS** (delivered tool, no args):

```
$ python3 corpus/tools/dependency_freeze.py
FINDING INVALID-ARGUMENTS: expected a fixture directory, --freeze DIR, or --self-test
RESULT ERROR
EXIT=2
```

Also exit 2 `INVALID-ARGUMENTS`: unknown flag `--not-a-real-flag`; fixture and `--freeze` together; `--self-test` combined with a fixture; `--self-test` combined with `--freeze`.

**FIXTURE-MISSING** (pinned name, directory absent — decided after the pin lookup, not as UNPINNED):

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/missing-parent/r95-crossing-aftermath
FINDING FIXTURE-MISSING: fixture directory not found: …/corpus/fixtures/missing-parent/r95-crossing-aftermath
RESULT ERROR
EXIT=2
```

**UNPINNED-FIXTURE** (name not in the pin set, even when the directory is also absent — first check):

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/v118-not-a-pin
FINDING UNPINNED-FIXTURE: no pin for 'v118-not-a-pin' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing'])
RESULT ERROR
EXIT=2
```

Same ID on the real unpinned fixture `corpus/fixtures/r99-window-lapse` (exit 2). Agrees with S1: r99 is not a C1 chain pin. A present directory named `v118-not-a-pin` inside a mirror also exits 2 `UNPINNED-FIXTURE`, not `DIGEST-MISMATCH`.

**PATH-MISMATCH** (byte copy at a foreign path, delivered tool):

```
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-99/seats/V118-scratch/foreign/r95-crossing-aftermath
FINDING PATH-MISMATCH: pin r95-crossing-aftermath names corpus/fixtures/r95-crossing-aftermath (resolves to …/corpus/fixtures/r95-crossing-aftermath); invoked fixture resolves to …/V118-scratch/foreign/r95-crossing-aftermath
RESULT ERROR
EXIT=2
```

**SCOPE-REFUSED** (delivered tool, target outside `corpus/fixtures/**`; contract hash unchanged after):

```
$ python3 corpus/tools/dependency_freeze.py --freeze .ufo/waves/round-99/seats/V118-scratch/outside-target
FINDING SCOPE-REFUSED: --freeze refuses …/V118-scratch/outside-target (resolves to …/outside-target); the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR
EXIT=2
```

Mirror also: `--freeze` of `corpus/fixtures` itself → `FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures itself; the frozen scope is corpus/fixtures/**` exit 2, contract unchanged. Mirror same-named in-scope path → `FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/nested/r95-crossing-aftermath: pin r95-crossing-aftermath already names 'corpus/fixtures/r95-crossing-aftermath'; freezing a same-named path elsewhere would rewrite the delivered pin` exit 2, contract unchanged.

**FILE-MISSING** (model build, required table):

```
FINDING FILE-MISSING: timeline.json is missing from …/cases/missing-timeline/corpus/fixtures/r95-crossing-aftermath
RESULT ERROR
EXIT=2
```

Unreadable timeline (`chmod 000`): `FINDING FILE-MISSING: timeline.json is unreadable: [Errno 13] Permission denied: …` exit 2.

`--freeze` when a declared pinned file is absent (new in-scope name, so not SCOPE-REFUSED), contract unchanged:

```
FINDING FILE-MISSING: --freeze refuses corpus/fixtures/v118-incomplete: pinned file(s) missing: inspiration-note.md
RESULT ERROR
EXIT=2
```

**MALFORMED-JSON**:

```
FINDING MALFORMED-JSON: timeline.json: Expecting property name enclosed in double quotes: line 2 column 1 (char 3)
RESULT ERROR
EXIT=2
```

Non-UTF-8 timeline also exit 2 `MALFORMED-JSON` (`is not UTF-8`). Not `DIGEST-MISMATCH`.

**MALFORMED-MODEL** (not a persisted self-test case):

```
FINDING MALFORMED-MODEL: timeline.json and relations.json must be JSON arrays
RESULT ERROR
EXIT=2
```

Also exit 2 `MALFORMED-MODEL`: duplicate event id (`repeats event id`); `depends_on` not strings; non-scalar `tick` (`must be a scalar`); relation missing `from/to/type`.

**CONTRACT-INVALID** (not a persisted self-test case). Parentheticals in the precedence sentence, each live:

- unreadable / missing: `FINDING CONTRACT-INVALID: contract not found: corpus/tools/dependency-freeze-contract.json` exit 2. Also bad JSON, non-UTF-8, and `chmod 000` on the contract file.
- root shape: `pins` as a list → `contract root must be an object with a pins object`.
- invalid pin: pin not an object; absolute fixture path (`needs a repo-relative fixture path`); path `corpus/tools` (`outside corpus/fixtures/**`); empty string and JSON `null` fixture on verify (path-less is not accepted by verify).
- `payload_schema_version` other than 2: missing, `1`, and `3` each exit 2 with `payload_schema_version … != 2 (full-file pin of 10 files)`.
- pin that does not digest all ten files:

```
FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs sha256 digests for all 10 pinned files (entities.json, relations.json, timeline.json, sources.json, contradictions.json, README.md, claim-excerpt-map.md, fictional-excerpts.md, inspiration-note.md, source-excerpt.md)
RESULT ERROR
EXIT=2
```

Also exit 2 `CONTRACT-INVALID`: `pinned_files` list short (that check fires before the files-digest check); extra file key in `files`; bad file sha; `events` not an object; invalid event entry; bad relation triple. Self-test shape: `self_test.expected` not an object; expectation set mismatch `missing=['clean'] extra=[]` (this is `CONTRACT-INVALID`, not `SELF-TEST-MISMATCH`).

**DIGEST-MISMATCH** names the file. Trailing newline on each of the ten pinned files, separately, inventory otherwise clean, each exit 2 and the finding names that file only. JSON trailing newline stays valid JSON, so this is not `MALFORMED-JSON`. Two examples:

```
FINDING DIGEST-MISMATCH: content digest f79cefa3… != pin 97cffd7b…; changed: timeline.json (sha256 3c0faad6… -> bd64e666…); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT=2
```

```
FINDING DIGEST-MISMATCH: content digest c619deac… != pin 97cffd7b…; changed: README.md (sha256 9d27af4a… -> 983c528c…); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT=2
```

Same class, exit 2, file named, for `entities.json`, `relations.json`, `sources.json`, `contradictions.json`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`.

Two files in one edit, both named (precedence: "names each changed pinned file"):

```
FINDING DIGEST-MISMATCH: … changed: README.md (sha256 9d27af4a… -> 983c528c…), source-excerpt.md (sha256 b5edc2fd… -> 5426ef14…); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT=2
```

Deleted pinned file that is not required to build the model, named with `-> None` (agrees with S1's fictional-excerpts deletion):

```
FINDING DIGEST-MISMATCH: … changed: README.md (sha256 9d27af4a… -> None); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT=2
```

`entities.json` deleted (pinned JSON table, not a required model-build file) is the same class, not `FILE-MISSING`: `changed: entities.json (sha256 026af0bc… -> None)`.

**SELF-TEST-MISMATCH** (mirror contract, `self_test.expected.clean.exit` flipped 0→1):

```
CASE clean: exit=0 expected=1 findings=[] MISMATCH
…
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 17/18
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR
EXIT=2
```

## 4. First failing check vs the precedence sentence

Held, on the verify pipeline:

- Unpinned name, directory also absent → `UNPINNED-FIXTURE` only, not `FIXTURE-MISSING`.
- Pinned name, directory absent → `FIXTURE-MISSING` only.
- Schema-1 pin and a missing directory of that name → `CONTRACT-INVALID` (`payload_schema_version 1 != 2`) only, not `FIXTURE-MISSING`. Schema check also beats a simultaneously wrong `pinned_files` list and a missing file digest (one finding, the schema sentence).
- Foreign path with `timeline.json` deleted → `PATH-MISMATCH` only, not `FILE-MISSING`.
- Truncated timeline (also a byte change) → `MALFORMED-JSON` only, not `DIGEST-MISMATCH`.
- Missing `timeline.json` plus a README byte change → `FILE-MISSING` only, not `DIGEST-MISMATCH`. Model-build `FILE-MISSING` decides before digest. That matches the precedence grouping "FILE-MISSING / MALFORMED-JSON / MALFORMED-MODEL (model build of the JSON tables)" ahead of digest, and the digest clause's "inventory clean" qualifier. A missing required table never reaches an inventory-clean digest check.
- Semantic change that also changes bytes decides exit 1, not exit 2. Dropped `depends_on` on `paired-crossing-decision`:

```
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 2/3; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['aru-ninth-bell']
RESULT FAIL
EXIT=1
```

Endpoint place shift → exit 1 `ENDPOINT-CHANGE` only. Phantom `depends_on` → exit 1 `ADDITION-DETECTED` only. No `DIGEST-MISMATCH` on those rows.

Freeze-only clauses, both demonstrated, and the exception sentences:

- Path-less pin (`fixture: null`) on verify → exit 2 `CONTRACT-INVALID` (`needs a repo-relative fixture path`). Same pin on `--freeze` of the canonical path → `MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath` then `RESULT PASS` exit 0. Not `SCOPE-REFUSED`.
- Schema-1 pin on verify → exit 2 `CONTRACT-INVALID`. `--freeze` of the canonical complete fixture upgrades: exit 0, `payload_schema_version=2`, all ten file keys present. Matches "Re-freeze is the payload upgrade path".
- Same-named incomplete copy: `--freeze` exits 2 `SCOPE-REFUSED` only, not `FILE-MISSING`. The same-name guard runs before freeze's missing-pinned check. Both IDs still fire on their own (complete foreign path → `SCOPE-REFUSED`; new name missing `inspiration-note.md` → `FILE-MISSING`). The precedence sentence does not order those two freeze-only checks against each other.

## 5. Agreement with S1

`S1-full-file-pins.md` describes this same post-edit tool. Independent agreement, not a copy of S1's probes:

- Chain 6/6, the six digests above, byte-identical to S1's listed digests.
- Delete or edit of a non-required pinned file → exit 2 `DIGEST-MISMATCH` naming the file, including `-> None` on delete. S1 showed that for `fictional-excerpts.md`; this seat showed it for all ten files and for a two-file edit.
- `--freeze` missing a declared file → exit 2 `FILE-MISSING`, no contract write.
- `payload_schema_version` other than 2 → exit 2 `CONTRACT-INVALID`.
- `r99-window-lapse` → exit 2 `UNPINNED-FIXTURE`.
- `r88-m3-maya-cluster/symbolism-clause-map.md` is outside the ten. Appending bytes to that file on a mirror and verifying: `DIGEST acf677a708…` / `RESULT PASS` / exit 0. The extra file is not an exit-2. Agrees with S1 and with the provenance note.

No ID or exit-code disagreement with S1. S1 did not claim the full 11-ID matrix; this seat did. S1's bound (an anchored "depends on" sentence is already `support_check` exit 1) is outside this seat's question and is not contradicted here.

## 6. Bounds (recorded, none hide an exit-2 ID)

1. **INVALID-ARGUMENTS list position.** The precedence sentence places `INVALID-ARGUMENTS` after `DIGEST-MISMATCH`. CLI usage is checked before dispatch, so `python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath --freeze corpus/fixtures/r95-crossing-aftermath` exits 2 `INVALID-ARGUMENTS` and never reaches a digest check. The ID is live. The written order of that one pre-dispatch check is loose. Same shape as the r98 bound. Not a missing class.
2. **`corpus/fixtures` itself.** Precedence says SCOPE-REFUSED for a target outside `corpus/fixtures/**` or a same-named rewrite. The tool also refuses the scope root (`--freeze refuses corpus/fixtures itself`). Same ID, one extra trigger. Exit 2, no write.
3. **Self-test pin coverage is narrower than the precedence sentence.** `CONTRACT-INVALID` and `MALFORMED-MODEL` are not persisted cases. `names_file` is enforced only on `markdown_tamper`. Neutralization on a scratch copy of the scored tool, DIGEST detail patched to `changed: redacted` (delivered tool not patched): clean self-test had been 18/18; the redacted runner printed `CASE digest_tamper: … findings=['DIGEST-MISMATCH'] ok` and `CASE markdown_tamper: … findings=['DIGEST-MISMATCH'] MISMATCH`, then `SELF-TEST 17/18` / `FINDING SELF-TEST-MISMATCH: cases failed: ['markdown_tamper']` / exit 2. So the 18th case does pin naming of `fictional-excerpts.md`. It does not pin naming for the other nine files. Behavior still names all ten (section 3). The gap is the persisted case, not the gate.
4. **Pin content-digest lie.** Fixture bytes unchanged, pin `content_sha256` set to 64 zeros: exit 2 `DIGEST-MISMATCH` with `changed: (no per-file digest difference; the pin's file digests disagree with its content digest)`. Broader than "bytes changed or missing", still the documented ID.
5. **S2 docs.** README and SKILL had no r99 freeze row at scoring. Historical README already names all 11 exit-2 IDs. No extra documented ID was left undemonstrated.

## 7. Write audit

Scored hashes `fb9bb9ff…` / `8c2561b0…` before the re-run, after the re-run, after the neutralization, and at 23:04 when this report was written. Matrix mutations and the redacted runner live only under `V118-scratch/`. Not mine: S1's tool/contract edits, S3/S4 fixture bytes, and the absence of an S2 report.

## Bottom line

**PASS** — all 11 precedence exit-2 IDs were demonstrated live (exit 2, that ID) on `fb9bb9ff…`/`8c2561b0…`; code IDs match the precedence set with no extras; first-failing-check order held on the verify pipeline; 77/77 matrix rows; chain digests match S1. Recorded bounds (INVALID-ARGUMENTS list position, self-test not pinning CONTRACT-INVALID/MALFORMED-MODEL or nine-file naming, scope-root trigger) do not hide an ID. S1's report was absent through try 40 and present before scoring; that stall-escape is recorded, not a missing gate.
