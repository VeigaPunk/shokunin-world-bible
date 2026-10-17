# V20 — c3-code-review (round 96)

Seat: V20 `c3-code-review`. Exclusive report path: this file. Scratch:
`.ufo/waves/round-96/scratch/V20/` (probe copies, frozen revision copy, waiter/poll logs).
Task per seat spec: after Q3, line-by-line review of `corpus/tools/dependency_freeze.py` —
digest-computation coverage (which files hashed; must include every file that feeds edges),
stable ID scheme, exit-2 classes complete, `--freeze` clearly separated from verify, no network,
stdlib-only; defects by severity. No commits, no pushes, no network, no nested agents. I wrote
only this report and my scratch dir; no corpus byte was written by this seat (audit in §8).

## 0. Artifact status (poll-wait) and reviewed revisions

Q3's two files were absent at seat start. Poll loop (20 s cadence, `.ufo/waves/round-96/scratch/V20/poll.log`)
plus a foreground wait: tools landed **17:42:45**; Q3's producer report
`.ufo/waves/round-96/seats/Q3-dependency-freeze.md` landed **17:47:26** — no ABSENT condition arose.

The tool changed twice during my review, so every claim below is revision-qualified:

| time | sha256 (`dependency_freeze.py`) | note |
|---|---|---|
| 17:42:49 | `f4b5208f1d4f3ac5e8e4b9123099440bb4b6e4816b5974dd62b58d86a8d8081b` | frozen by me for the line-by-line read (`scratch/V20/frozen/dependency_freeze_reviewed.py`) |
| 17:43:35 | `d17297bb2d49c5bb35783824bf0704513cc1f1a692f11878379bb1edad56282f` | mid-flight revision; self-test 5/14 (D1 below) |
| **17:44:37 → delivered** | **`a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980`** | final; matches Q3's report §"Verified revision" |

Contract `corpus/tools/dependency-freeze-contract.json` = `7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975`
(17:44:27), unchanged from Q3's declared hash. Delivered-revision diff vs my frozen copy is 112
lines and confined to `self_test_cases()` case-path binding and moving `parse_args` inside
`main`'s handler (`scratch/V20/reviewed-vs-delivered.diff`); `compare`, `build_model`,
`content_digest`, `verify`, `freeze` are byte-identical to what I read line by line.

Final battery on the delivered revision:

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
$ for d in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
    python3 corpus/tools/dependency_freeze.py corpus/fixtures/$d >/dev/null 2>&1; echo "$d exit=$?"; done
r88-m3-maya-cluster exit=0
r94-paired-crossing exit=0
r95-crossing-aftermath exit=0
r96-crossing-response exit=0
$ python3 corpus/tools/dependency_freeze.py --self-test | tail -2
SELF-TEST 14/14
RESULT PASS        # exit 0
```

## 1. What the tool does (line-by-line, delivered revision)

- `:25-31` `ROOT = parents[2]`; `CONTRACT_PATH` is a module constant in the owning repo;
  `DATA_FILES` = the five JSON tables; `REQUIRED_FILES = (relations.json, timeline.json)`;
  `RESULTS = {0: PASS, 1: FAIL, 2: ERROR}`.
- `:73-80 content_digest(files)` — SHA-256 over `json.dumps({name: sha256(raw)}, sort_keys=True,
  separators=(",",":"))`. The composite encodes **presence/absence** as well as bytes, because
  absent files simply have no key.
- `:102-162 build_model` — reads only `DATA_FILES` **that exist** (`:106-110`); fails
  `FILE-MISSING` if a `REQUIRED_FILES` entry is absent (`:111-113`); re-parses; `MALFORMED-MODEL`
  for non-array tables, empty/duplicate event ids, non-string `depends_on`, non-scalar
  `tick`/`entity_id`/`place_id`, non-string relation `from`/`to`/`type`. Events are keyed by id with
  `depends_on` stored as `sorted(set(deps))` (`:140`); relations are stored as `[from, to, type]`
  triples, `sorted` (`:158`); `counts` adds `entities`/`sources` only when those tables are arrays.
- `:169-211 compare` — per frozen event: missing event → `REDUCTION-DETECTED`; lost deps →
  `REDUCTION-DETECTED`, gained deps → `ADDITION-DETECTED` (per event, detail names the ids);
  endpoint keys `tick`/`entity_id`/`place_id` differ → `ENDPOINT-CHANGE`. Unpinned events with
  non-empty deps → `ADDITION-DETECTED`. Relations compared as `Counter` of triples: lost+gained →
  `ENDPOINT-CHANGE`, only lost → `REDUCTION-DETECTED`, only gained → `ADDITION-DETECTED`.
- `:214-257 read_contract` / `validate_pin` / `pin_for` — contract shape validation; pins keyed by
  **fixture basename** (`fixture.resolve().name`, `:252`); unknown basename → `UNPINNED-FIXTURE`.
- `:260-284 verify` — **semantic findings decide first**: `if findings: emit(1, …); return 1`
  (`:271-274`), and only then the composite-digest comparison → `DIGEST-MISMATCH`, exit 2
  (`:275-280`). One terminal `RESULT` line on every path (verified by every probe below).
- `:287-318 freeze` — builds the pin (including `fixture` label and `git rev-parse HEAD` revision),
  writes `CONTRACT_PATH` (`:312`), then re-reads and re-verifies the just-written pin.
- `:321-395 self_test_cases` / `:398-442 run_self_test` — 14 isolated cases under
  `tempfile.TemporaryDirectory` (`:411`), each run as a real CLI subprocess with the persisted
  expectations from `self_test.expected`; case-set mismatch with the implemented set →
  `CONTRACT-INVALID` (`:403-406`).
- `:445-466 main` — `--self-test` / `--freeze DIR` / `<fixture>` mutually exclusive
  (`:452-455`), argparse errors routed to `ToolError` → `INVALID-ARGUMENTS` exit 2.

## 2. Digest computation coverage (required dimension)

**What is hashed:** the five JSON tables that are present at freeze time — `entities.json`,
`relations.json`, `timeline.json`, `sources.json`, `contradictions.json` (`:28`, `:105-110`) — with
per-file SHA-256s stored in `pin["files"]` and a composite `content_sha256` over the sorted
name→digest map (`:77-80`, `:159-160`).

**Do the hashed files include everything that feeds edges?** For the JSON layer, yes:

- `timeline.json` feeds the edge inventory (`id` → `depends_on`) **and** the endpoint model
  (`tick`, `entity_id`, `place_id`); `relations.json` feeds the endpoint triples. Both are hashed
  and modeled.
- `entities.json`, `sources.json`, `contradictions.json` do not carry edges themselves but they
  gate the interpretation of edges in `check_bible` (`entities_available` / `sources_available`);
  they are hashed, so any change — including **deletion**, which drops the key from the digest map —
  exits 2. Probe: deleting `entities.json` from a pinned copy →
  `FINDING DIGEST-MISMATCH … RESULT ERROR`, exit 2.
- The composite backstops every mutation class the semantic model does not represent: duplicate
  `depends_on` entries (collapsed by `sorted(set(...))`), pure reordering of `depends_on`, an
  unpinned event with no deps, and description-only edits all exit 2 `DIGEST-MISMATCH`
  (probes in §7). This is exactly the contract's declared precedence.

**Gap (D4):** only JSON tables are hashed. The markdown layer — `claim-excerpt-map.md`,
`fictional-excerpts.md`, `README.md`, `inspiration-note.md`, `source-excerpt.md` — is not. BR-01's
own text (`round-94/followup/F29-debt.md:42`) names the prose cross-check ("Nothing cross-checks the
JSON dependency set against the map/excerpt wording 'depends on both ninth-bell entries'"), and that
half stays open: replacing that sentence with "follows the ninth-bell entries" in a pinned copy of
r94 leaves **all three gates green** (`check_bible` exit 0, `map_obligations` exit 0,
`dependency_freeze` exit 0 — §7 probe `mdonly`).

**Diagnostic limit (D8):** `pin["files"]` is written and shape-validated but never compared;
`verify` only compares the composite, so a `DIGEST-MISMATCH` finding cannot name which file changed.

## 3. Stable ID scheme and determinism

Finding IDs are **class-level** and stable: `REDUCTION-DETECTED`, `ADDITION-DETECTED`,
`ENDPOINT-CHANGE` (exit 1); `DIGEST-MISMATCH`, `MALFORMED-JSON`, `MALFORMED-MODEL`,
`FILE-MISSING`, `FIXTURE-MISSING`, `UNPINNED-FIXTURE`, `CONTRACT-INVALID`, `INVALID-ARGUMENTS`
(exit 2); `SELF-TEST-MISMATCH`. Instances are distinguished by the detail text (e.g.
`event paired-crossing-decision lost depends_on ['evin-ninth-bell']`). `emit()` sorts findings
(`:68`), the model uses `sorted(set(...))`, relations are sorted, and the digest uses `sort_keys`,
so output is order-stable.

```
$ for s in 0 1 2; do PYTHONHASHSEED=$s python3 corpus/tools/dependency_freeze.py \
    .ufo/waves/round-96/scratch/V20/probes/reduction/r94-paired-crossing > scratch/V20/det-$s.txt 2>&1; done
$ md5sum scratch/V20/det-*.txt
3d8557a90304ec5371145a8ef6727296  det-0.txt
3d8557a90304ec5371145a8ef6727296  det-1.txt
3d8557a90304ec5371145a8ef6727296  det-2.txt
```

Style note (D6): this tool uses UPPERCASE-HYPHEN IDs while the sibling `map_obligations.py` uses
lowercase_underscore (`schema_drift`, `inventory_mismatch`). Internally consistent with its own
contract; cross-tool inconsistency only.

## 4. Exit-2 class audit

Implemented and reachable (all observed exit 2 with one terminal `RESULT ERROR` line and no
traceback): `FIXTURE-MISSING`, `UNPINNED-FIXTURE`, `FILE-MISSING`, `MALFORMED-JSON`,
`MALFORMED-MODEL`, `DIGEST-MISMATCH`, `CONTRACT-INVALID`, `INVALID-ARGUMENTS`. The set covers every
could-not-evaluate condition I could construct from the domain (missing/unknown fixture, unusable
contract, unreadable/absent required file, bad bytes, bad shape, unmodeled content change, bad
usage). No uncaught-exception path was observed in any probe.

**Pinning gap (D4→F4):** the persisted self-test pins 14 cases; **`MALFORMED-MODEL` and
`CONTRACT-INVALID` have no persisted case**, although both are implemented and I verified them
directly (probes `model` and `contract` in §7). The unmodeled-addition path (`newevent`) is also
only implicitly covered by `digest_tamper`. Same class as r95 NB-07 (head behavior unpinned).

## 5. `--freeze` separation, network, stdlib, live-tree writes

- **Separation:** `--freeze DIR` and a positional fixture are mutually exclusive, as is
  `--self-test` (`:452-455`); the only `write_text` in the tool is `:312` inside `freeze`; `verify`
  and `run_self_test` perform no live-tree writes. `verify` is the admitted path; `--freeze` is
  documented as delivery-time only.
- **Isolation of the self-test:** scratch lives in `tempfile.TemporaryDirectory`
  (`:411`, observed under `/var/tmp` via `TMPDIR`) and is removed on exit — no leftovers, no
  repo-root scratch (better than the carried BR-05 pattern of `map_obligations`).
  `git status --short` before/after a `--self-test` run was identical.
- **No network / stdlib only:** imports are `argparse, hashlib, json, re, shutil, subprocess, sys,
  tempfile, collections, pathlib`; no `socket`/`urllib`/`http`/`requests` token anywhere.
  `subprocess` is used only for a local `git rev-parse HEAD` (`:292`) and for the self-test's own
  CLI subprocesses (`:417`).

## 6. Defects by severity

| ID | severity | defect | evidence |
|---|---|---|---|
| D1 | HIGH — **fixed mid-flight, not in delivered bytes** | Self-test closure bug: every scratch-case lambda captured the reassigned local `scratch`, so 9 of 14 cases ran against the last-built directory (`missing_timeline/`) and all failed. Observed `SELF-TEST 5/14 / FINDING SELF-TEST-MISMATCH / RESULT FAIL` exit 1 on revisions `f4b5208f` (17:42:49) and `d17297bb` (17:43:35). Same edit also moved `INVALID-ARGUMENTS` validation inside `main`'s handler (previously a raw traceback, exit 1). Fixed at 17:44:37 (`a3b57978`): 14/14 PASS, exit 0, confirmed by my own run. Disclosed by Q3 §5. | my two failing runs, on the revisions current at 17:42:49 and 17:43:35 (`missing_timeline` path in every failing case); delivered revision 14/14 |
| D2 | HIGH (delivered; disclosed, deferred by Q3) | `--freeze` has no scope guard: it writes the live contract for **any** directory, keyed by basename (`:26`, `:310-312`). Live effect in the delivered artifact: a stray pin `c3red` → `.ufo/waves/round-96/seats/V41-scratch/c3red` with a **reduced** inventory (`paired-crossing-decision → ['aru-ninth-bell']`, `dependency_edges 1` vs r94's 2), i.e. a mutation blessed into the delivered contract. I reproduced the mechanism end-to-end in an isolated copy tree (never against the live contract): `--freeze` on a reduced scratch copy printed `FROZEN r94-paired-crossing: events 3; dependency-edges 1; relations 1` then `RESULT PASS`, and the copy's contract recorded the reduced deps. Impact on verify semantics: none (no corpus fixture is named `c3red`); the hazard is that any future `--freeze` on a scratch copy silently rewrites a delivered pin. Recommendation: delete `pins.c3red` at closure and/or add a `corpus/fixtures/` scope guard in r97. | contract `pins` list; `scratch/V20/freezetest/`; live contract sha256 unchanged before/after my test (`sha256sum -c` → OK) |
| D3 | MEDIUM | **No path binding.** Pins are keyed by basename only (`:252`); `pin["fixture"]` is written (`:302`) but never read anywhere in the tool (`grep '"fixture"'` → only `:302` and the CLI positional at `:448`). A pristine copy of r94 at another path verifies with a **byte-identical receipt** to the delivered fixture (`diff` → empty), exit 0, and the receipt names only `r94-paired-crossing`. Consequence: a "chain 4/4 clean" receipt does not prove the delivered paths were the ones verified, and same-named copies are indistinguishable. Suggested fix: compare `fixture.resolve()` against `ROOT / pin["fixture"]` (repo-relative pins) or print the resolved path in the receipt. | probe `pristine` + `diff shadow-receipt.txt real-receipt.txt` → identical |
| D4 | MEDIUM (scope/claim calibration) | BR-01's prose half remains open: the markdown layer is not hashed or modeled, so removing the dependency wording from `fictional-excerpts.md` leaves `dependency_freeze` exit 0 while `check_bible` and `map_obligations` are also green. The JSON edge-reduction half of BR-01 is genuinely closed; the wording cross-check named in the debt is not. Recommend recording as a bounded residual for r97 rather than reading C3 as full BR-01 closure. | probe `mdonly`: three gates exit 0 |
| F4 | LOW | `MALFORMED-MODEL` and `CONTRACT-INVALID` are implemented but have no persisted self-test case (14 pinned cases vs 8 exit-2 classes). Both verified reachable by me (exit 2 + `RESULT ERROR`). | probes `model`, `contract` |
| F5 | LOW | `SELF-TEST-MISMATCH` is emitted with **exit 1** (`:439-440`), while Q3's report §1 table classifies it under exit 2 and the sibling `map_obligations.py:855-857` uses exit 2. One convention should win; the delivered tool is self-consistent but diverges from its sibling and from its own producer's table. | `sed -n '436,442p'`; `grep -A3 self_test_mismatch corpus/tools/map_obligations.py` |
| F6 | LOW | `freeze()` calls `verify(...)` but discards its result and `return 0` (`:317-318`); a freshly written pin that failed its own re-verification would still exit 0 (the FAIL text is printed, the exit code is not). | `sed -n '312,319p'` |
| F7 | LOW (cosmetic) | Deleting a frozen event with **zero** dependencies reports `REDUCTION-DETECTED: event … is missing; 0 frozen dependency edge(s) gone` — correct semantics (exit 1), odd wording. | `compare` `:175-179` |
| F8 | LOW (diagnostics) | `DIGEST-MISMATCH` reports only the composite digest; the stored per-file digests are never compared, so the finding cannot name the changed file. The FINDING line also omits the fixture name (the receipt line above it carries it). | `:275-280`; contract `files` block |

Nothing in D2–F8 invalidates a declared C3 class: every declared exit/finding behavior reproduces
on the delivered revision (see §7). D1 is the only defect that made a *declared* behavior fail, and
it is absent from the delivered bytes.

## 7. Probes (scratch copies named `r94-paired-crossing` so the basename pin resolves)

All copies live under `.ufo/waves/round-96/scratch/V20/probes/`; the delivered corpus was never
mutated. `python3 corpus/tools/dependency_freeze.py <copy>` in every row.

| probe | mutation | observed |
|---|---|---|
| reduction (BR-01) | drop `evin-ninth-bell` from tick-10 `depends_on` | `dependency-edges 1/2`; `FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']`; `RESULT FAIL`; exit 1 |
| addition | add `phantom-ninth-bell` | `dependency-edges 3/2`; `FINDING ADDITION-DETECTED: … gained depends_on ['phantom-ninth-bell']`; exit 1 |
| endpoint | tick-10 `place_id` `chalk-stair` → `salt-court` | `FINDING ENDPOINT-CHANGE: event paired-crossing-decision.place_id: 'chalk-stair' -> 'salt-court'`; exit 1 |
| relorder | relation replaced by a different triple | `FINDING ENDPOINT-CHANGE: relation endpoints changed: removed [aru, evin, agreed_co_stewardship_for_this_crossing]; added [zzz, yyy, probe_type]`; exit 1 |
| digest | description text edited (inventory unchanged) | `FINDING DIGEST-MISMATCH: content digest 2e622e9a… != pin 2527beb9…`; exit 2 |
| entities | `entities.json` deleted | `FINDING DIGEST-MISMATCH …`; exit 2 |
| dupdep | duplicate `depends_on` entry (set-collapse) | `FINDING DIGEST-MISMATCH …`; exit 2 |
| reorder | `depends_on` list reversed | `FINDING DIGEST-MISMATCH …`; exit 2 |
| newevent | unpinned event with empty `depends_on` added | receipt `events 4/3`; `FINDING DIGEST-MISMATCH …`; exit 2 |
| model | `timeline.json` = `[{"id": ""}]` | `FINDING MALFORMED-MODEL: timeline[0] needs a nonempty string id`; exit 2 |
| contract | contract copy with `pins` removed (isolated tree) | `FINDING CONTRACT-INVALID: contract root must be an object with a pins object`; exit 2 |
| pristine | unmodified copy at a different path | exit 0; receipt byte-identical to the delivered fixture's receipt (`diff` empty) |
| mdonly | prose `depends on both ninth-bell entries` → `follows the ninth-bell entries` in `fictional-excerpts.md` | `dependency_freeze` exit 0 (`RESULT PASS`), `check_bible` exit 0, `map_obligations` exit 0 |

BR-01 baseline reproduced by me independently before the gate existed: on a scratch copy of
`r94-paired-crossing` with the same reduction, `check_bible` printed
`CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0.

## 8. Own-artifact audit

`git status --short` at 17:48 (lane root):

```
 M LOG.md
 M corpus/tools/map_obligations.py
?? .ufo/waves/round-96/
?? corpus/fixtures/r96-crossing-response/
?? corpus/knowledge/r96-response-scope-note.md
?? corpus/tools/dependency-freeze-contract.json
?? corpus/tools/dependency_freeze.py
```

No path outside `.ufo/waves/round-96/` was written by this seat; the two `corpus/tools/*` entries
are Q3's. I deliberately did **not** run `--freeze` against the live tool (that would have added or
rewritten a live pin); the `--freeze` mechanism was exercised only in the copied tree
`scratch/V20/freezetest/`, and `sha256sum -c scratch/V20/live-contract-before.txt` confirms the live
contract is unchanged (`OK`). Incidental observation, not mine and not re-adjudicated:
`?? map-obligations-self-test-q10ds0b_/` appeared in the lane root during the round — the r94 BR-05 /
r95 NB-06 repo-root scratch class, recurring under another seat's `map_obligations --self-test`.

**Bottom line: PASS (bounded) — the delivered revision (`dependency_freeze.py` `a3b57978…`,
contract `7d568cc4…`) implements the declared 0/1/2 contract, pins all five JSON tables that feed
the chain's edge inventory, verifies r88/r94/r95/r96 4/4 clean and 14/14 self-test, and closes the
JSON dependency-reduction class of BR-01 (my independent reduction probe exits 1
`REDUCTION-DETECTED`); carried defects: D2 `--freeze` has no scope guard and the delivered contract
already holds a foreign reduced scratch pin `c3red`, D3 pins bind by basename only so receipts do
not identify the verified path, D4 the prose/wording half of BR-01 is still unfrozen, plus four LOW
items (F4–F8); D1 (self-test 5/14) was a real mid-flight defect on revisions `f4b5208f`/`d17297bb`
and is fixed in the delivered bytes.**
