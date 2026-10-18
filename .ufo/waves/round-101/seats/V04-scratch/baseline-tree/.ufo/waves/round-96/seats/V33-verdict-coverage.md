# V33 — verdict-coverage: C3 (dependency_freeze gate; chain frozen)

Round 96, seat V33. Baseline r95 closure `dcb2d92`; HEAD at test time
`60dba0c2aa344860b10a2fc63e00468d1b134f27`. Repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin` (all commands run from there with
`python3`). Scratch:
`.ufo/waves/round-96/seats/V33-scratch/`. Only this report and that scratch dir
were written by this seat; no commits, no pushes, no network, no nested agents.

Seat scope: one COVERAGE verdict on C3 — does the new
`corpus/tools/dependency_freeze.py` + `corpus/tools/dependency-freeze-contract.json`
gate cover the dependency-reduction blind spot BR-01 and the adjacent
addition/endpoint classes, and what are its bounds. The BR-01 demonstration is
re-run here independently of the producer.

**Revision under test (frozen for this verdict):**

```
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
```

Q3's producer report (`.ufo/waves/round-96/seats/Q3-dependency-freeze.md`) landed
at 17:47:36-03:00 and states the same two hashes verified here, so the verdict
below is against the delivered revision (see §6). Both artifacts were revised
twice during the round (tool `f4b5208f…` → `d17297bb…` → `a3b57978…`; contract
`2601c18a…` → `7d568cc4…`); every result below is stated against the hashes
above and was re-run after the last observed write.

## 1. The gap C3 claims to close — independently reproduced

C3's declared debt BR-01: "dropping `evin-ninth-bell` from the r94 tick-10
`depends_on` leaves every current gate green." Reproduced on scratch copies
(mutations applied by my own script `V33-scratch/mutate.py`; fixture-level gates
are `corpus/fixtures/check_bible.py`, `corpus/tools/map_obligations.py`,
`corpus/tools/support_check.py` — `boundary_doc_check.py` and
`discriminate_check.py` take no cluster argument and cannot see a fixture
mutation).

| scenario | mutation | check_bible | map_obligations | support_check |
|---|---|---|---|---|
| reduce | r94 `paired-crossing-decision.depends_on` loses `evin-ninth-bell` → `["aru-ninth-bell"]` | exit 0 CLEAN | exit 0 RESULT PASS | exit 0 RESULT PASS |
| add | r95 `aftermath-missing-evin.depends_on` gains `aru-ninth-bell` | exit 0 CLEAN | exit 0 RESULT PASS | exit 0 RESULT PASS |
| endpoint-valid | r94 relation `to` `evin` → `quiet-rise` (both real entities) | exit 0 CLEAN | exit 0 RESULT PASS | exit 0 RESULT PASS |
| endpoint-dangling | r94 relation `to` `evin` → `unknown-endpoint-x` | exit 1 | exit 0 RESULT PASS | exit 0 RESULT PASS |

```
$ python3 corpus/fixtures/check_bible.py .ufo/waves/round-96/seats/V33-scratch/br01-reduce
CLEAN: schema, citations, relations, timeline; 0 violations      # exit 0
$ python3 corpus/tools/map_obligations.py .ufo/waves/round-96/seats/V33-scratch/br01-reduce
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
RESULT PASS                                                       # exit 0
$ python3 corpus/tools/support_check.py .ufo/waves/round-96/seats/V33-scratch/br01-reduce
RESULT PASS                                                       # exit 0
```

Findings beyond the declared claim:

- The **addition** class is equally invisible to every baseline gate; C3's
  declared scope covers it, so this is in-scope, not scope creep.
- A **valid-endpoint swap** (endpoint changed to a different *existing* entity)
  is invisible to every baseline gate. `check_bible` catches only *dangling*
  endpoints (exit 1 on `unknown-endpoint-x`), so C3's `ENDPOINT-CHANGE` finding
  covers a genuinely separate gap rather than duplicating an existing gate.
- The reduce mutation leaves `map_obligations` at `14/14` because the map is
  completeness-checked against pointers, not value-checked for `depends_on`.
- Cross-check: V49 `gates-cross` reaches the same cross-gate conclusion from a
  separately built mutation (`.ufo/waves/round-96/seats/V49-gates-cross.md`
  §2), and V14 `c2-dependency-probe` reports the same structural blind spot in
  `check_bible` (empty `depends_on` key stays CLEAN).

## 2. Independent chain inventory (my own baseline for the pin)

Computed by me directly from the fixtures
(`V33-scratch/v33-independent-inventory-refreshed.txt`), before comparing with
the contract:

| fixture | dependency edges (event → sorted depends_on) | relation triples |
|---|---|---|
| r88-m3-maya-cluster | `{}` | `[]` |
| r94-paired-crossing | `{paired-crossing-decision: [aru-ninth-bell, evin-ninth-bell]}` | `aru→evin agreed_co_stewardship_for_this_crossing` |
| r95-crossing-aftermath | `{…paired-crossing-decision, aftermath-missing-evin: [paired-crossing-decision]}` | same |
| r96-crossing-response | `{…, response-evin-salt-court: [aftermath-missing-evin]}` | same |

My independent recomputation of the contract's aggregate content digest
(`sha256` over the sorted per-file `sha256`s of the five data files) matches
**all four pins exactly**:

| fixture | my recomputation | contract pin | match |
|---|---|---|---|
| r88-m3-maya-cluster | `15ef230e…279` | `15ef230e…279` | yes |
| r94-paired-crossing | `2527beb9…e75` | `2527beb9…e75` | yes |
| r95-crossing-aftermath | `d541ae64…ec9` | `d541ae64…ec9` | yes |
| r96-crossing-response | `d422a9b3…7f6` | `d422a9b3…7f6` | yes |

Chain provenance: `r96-crossing-response` data files were last written
17:40:16-03:00 (Q4's mid-seat correction), before Q3's freeze; the r96 pin
therefore covers the delivered revision, and Q5's later markdown files are
outside `data_files` and cannot invalidate it.

Preservation of the inherited chain: all five data files of each of
`r88-m3-maya-cluster`, `r94-paired-crossing`, and `r95-crossing-aftermath` are
blob-identical between the worktree and `dcb2d92`
(`git hash-object <file>` vs `git rev-parse dcb2d92:<file>`, 15/15 `same`), and
`git status --porcelain -- corpus/fixtures/` lists only the new
`corpus/fixtures/r96-crossing-response/` directory. So the three inherited pins
freeze unchanged, git-clean bytes, and C3's delivery modified no fixture
(content digests for all three also match the r95-closure values my earlier
pass recorded independently). Census:
`git ls-tree -d --name-only dcb2d92 corpus/fixtures/` → 169 dirs;
`find corpus/fixtures -maxdepth 1 -mindepth 1 -type d` → 170; the single delta
is `r96-crossing-response`.

## 3. Gate replay — my own runs on the frozen revision

Full transcript: `V33-scratch/v33-battery-current.txt`.

| # | scenario | expected | observed | verdict |
|---|---|---|---|---|
| 1–4 | chain clean r88 / r94 / r95 / r96 | exit 0 | exit 0, `RESULT PASS`, receipts `0/0`, `2/2`, `3/3`, `4/4` edges | as declared (4/4 clean) |
| 5 | **BR-01 reduce** r94 tick-10 | exit 1 `REDUCTION-DETECTED` | exit 1 `FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']` | as declared |
| 6 | add edge r95 | exit 1 `ADDITION-DETECTED` | exit 1 `FINDING ADDITION-DETECTED: event aftermath-missing-evin gained depends_on ['aru-ninth-bell']` | as declared |
| 7 | endpoint swap → existing entity | exit 1 `ENDPOINT-CHANGE` | exit 1 `FINDING ENDPOINT-CHANGE: … removed [aru, evin, …]; added [aru, quiet-rise, …]` | as declared |
| 8 | endpoint dangling | exit 1 | exit 1 `ENDPOINT-CHANGE` | fail-closed |
| 9 | r96 deepest edge drop | exit 1 | exit 1 `REDUCTION-DETECTED: response-evin-salt-court lost depends_on ['aftermath-missing-evin']` | coverage holds at chain depth |
| 10 | r96 mid edge drop (1 of 2 deps) | exit 1 | exit 1 `REDUCTION-DETECTED: paired-crossing-decision lost depends_on ['aru-ninth-bell']` | coverage holds |
| 11 | non-inventory byte tamper | exit 2 | exit 2 `DIGEST-MISMATCH` | as declared |
| 12 | format-only re-serialization | — | exit 2 `DIGEST-MISMATCH` | bound, see §4 |
| 13 | timeline emptied | exit 1 | exit 1, three `REDUCTION-DETECTED` (event-missing form) | fail-closed |
| 14 | `relations.json` removed | exit 2 | exit 2 `FILE-MISSING` | as declared |
| 15 | unpinned new event, no deps | — | exit 2 `DIGEST-MISMATCH` | fail-closed (not a silent 0) |
| 16 | non-chain fixture (`r93-m2-kojiki-cluster`) | — | exit 2 `UNPINNED-FIXTURE` | bound, see §4 |
| 17 | nonexistent directory, unpinned basename (`nonexistent-xyz`) | — | exit 2 `UNPINNED-FIXTURE` | fail-closed; see §4.3 |
| 17b | nonexistent directory, **pinned** basename (`…/not-here/r95-crossing-aftermath`) | exit 2 `FIXTURE-MISSING` | exit 2 `FINDING FIXTURE-MISSING: fixture directory not found` | matches the persisted `missing_fixture` expectation |
| 18 | fixture + `--freeze` together | exit 2 `INVALID-ARGUMENTS` | exit 2 `FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both` | fixed during the round |
| 19 | no arguments | exit 2 `INVALID-ARGUMENTS` | exit 2 `INVALID-ARGUMENTS` | as declared |
| 20 | `--self-test` | exit 0, 14/14 | `SELF-TEST 14/14`, `RESULT PASS`, exit 0 | as declared on the frozen revision |

Representative transcripts:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
RESULT PASS                                                        # exit 0

$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/V33-scratch/replay/reduce/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 1/2; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL                                                        # exit 1

$ python3 corpus/tools/dependency_freeze.py --self-test
SELF-TEST 14/14
RESULT PASS                                                        # exit 0
```

Determinism (mine, `V33-scratch/v33-determinism.txt`): the reduce verdict is
byte-identical under `PYTHONHASHSEED` 0 / 1 / 42 / 12345; repeat runs of the
chain and of `--self-test` are byte-identical; the self-test output was
byte-identical across two runs. No leftover self-test scratch: the tool uses
`tempfile.TemporaryDirectory`, and no `dependency-freeze-self-test-*` directory
remains under the repo root or `/tmp` (contrast the carried BR-05 residual for
`map_obligations`).

**Defects present on earlier in-flight revisions, fixed on the delivered one**
(recorded because they were live during the round, and because the tool's own
persisted self-test caught them rather than passing silently):

- at tool `f4b5208f…`/`d17297bb…`: `--self-test` → `SELF-TEST 2/14`, exit 1,
  because the self-test's copied cases carry the case name as directory
  basename while pin lookup is basename-keyed, so 12 cases returned
  `UNPINNED-FIXTURE`/exit 2 instead of their expected finding;
- at the same revisions: `INVALID-ARGUMENTS` raised an uncaught `ToolError`
  traceback and exited 1, because the two `fail()` guards in `main()` sat
  outside the `try/except ToolError` block.

Both observations are independently confirmed by Q3's report §5 (which also
records that argument validation was moved inside the handler) and by V49 §6,
and both are resolved at `a3b57978…` (14/14; `INVALID-ARGUMENTS` exit 2 with a
FINDING line).

## 4. Bounds — what this gate does not do

1. **The delivered contract is polluted by a stray, reduction-bearing pin.**
   `pins` on the frozen contract is
   `['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response']`.
   The extra pin's own `fixture` field is
   `.ufo/waves/round-96/seats/V41-scratch/c3red` — another seat's scratch
   directory — and it freezes the **BR-01 reduction**
   (`paired-crossing-decision.depends_on = ['aru-ninth-bell']`,
   `dependency_edges: 1`). It verifies clean:

   ```
   $ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/V41-scratch/c3red
   FREEZE c3red: events 3/3; dependency-edges 1/1; relations 1/1
   DIGEST eff4b354c092a9c4a3ea6de6857ee1a21be1ab4bafac957568b6813dac8dbd28
   RESULT PASS                                                        # exit 0
   ```

   Origin: `--freeze` writes to `CONTRACT_PATH` (repo-root relative) with no
   path guard, and `pin_for` keys pins by `fixture.resolve().name`; V41's
   scratch logs (`V41-scratch/c3-freeze.out`, `c3-interim.log`) show a
   `--freeze` run on that copy. The four chain pins are untouched
   (`r94-paired-crossing` still pins `2527beb9…`), so the declared chain
   coverage is not weakened by this pin — but the delivered contract is not
   clean, and the same mechanism is a live laundering path: freezing a scratch
   copy *named* `r94-paired-crossing` overwrites the real pin.
   Evidence: `V33-scratch/v33-stray-pin-evidence.txt`.

   This finding is **corroborated by the producer**: Q3's report §7
   ("Anomaly — a foreign pin in the delivered contract (reported, not hidden)")
   names the same pin, the same `fixture` path, the same digest `eff4b354…`,
   the same counts `{events 3, edges 1, relations 1}`, and the same V41
   evidence trail, and states the pin was left in place on purpose because
   verifier receipts (including `V33-scratch/v33-battery-current.txt`) already
   quote the pinned list — removing it mid-round would invalidate recorded
   observations. Q3's assessment matches mine: harmless to verification
   semantics (no corpus fixture is named `c3red`), but a real tool hazard, with
   the recommended closure action either deleting `pins.c3red` or adding a
   `--freeze` scope guard refusing paths outside `corpus/fixtures/`. Q3
   deliberately did not implement the guard mid-round to keep the tool hash
   stable for in-flight probes. I did not remove the pin either: the contract is
   Q3's byte-owned file, and the finding is a closure decision for L1.
2. **`--freeze` laundering, demonstrated end-to-end in a scratch mirror root**
   (`V33-scratch/mirror/`, so Q3's contract was never written by this seat):
   on a reduced copy named `r94-paired-crossing`, `verify` → exit 1
   `REDUCTION-DETECTED`; then `--freeze <that copy>` → `FROZEN …`,
   `RESULT PASS`, exit 0 — the reduction is now the pin. C3 declares `--freeze`
   "not used in the admitted path", which is what keeps this a bound rather
   than a hole; nothing in the tool prevents its use.
3. **Pins are basename-keyed, not path-keyed.** A fixture at any path whose
   directory name matches a pinned name is verified against that pin; a
   *renamed* fixture (legitimate move) exits 2 `UNPINNED-FIXTURE`. This is why
   the stray `c3red` pin verifies at all, and why my own replay copies had to
   preserve the directory name. The same ordering makes the receipt for a
   nonexistent directory depend on its basename: `…/not-here/r95-crossing-aftermath`
   → exit 2 `FIXTURE-MISSING`, while `nonexistent-xyz` → exit 2
   `UNPINNED-FIXTURE` (both fail closed; the pin lookup runs first, which is
   also why the self-test's `missing_fixture` case uses a pinned basename).
4. **Coverage is chain-scoped, not corpus-wide.** The four pinned fixtures are
   the crossing chain; every other fixture (`r93-m2-kojiki-cluster` tested)
   exits 2 `UNPINNED-FIXTURE`. The gate is a freeze of a named chain, not a
   corpus-wide dependency invariant.
5. **Byte-sensitive beyond the inventory.** A whitespace-only re-serialization
   with identical values exits 2 `DIGEST-MISMATCH` (not 0). That is
   fail-closed, but it means any legitimate reformatting of a pinned fixture
   requires a re-freeze, and the re-freeze is exactly the unguarded path in
   bound 2.
6. **Not registered anywhere.** `grep -rn "dependency_freeze"` outside the
   contract and this round's seat scratch finds no entry in `SKILL.md`,
   `corpus/tools/README.md`, or any runner: the gate protects only when
   invoked. C3's declaration is "zero corpus modifications beyond the two new
   tool files", so this is consistent with the claim, but the capability is
   not wired into an admitted path.
7. **Judgment scope unchanged.** The gate compares frozen structure
   (dependency edges, event endpoints, relation triples) and bytes. It does not
   judge chronology truth, entailment, source authenticity, rights, permission,
   or canon — matching the contract's own `scope` line.

## 5. Coverage verdict (C3)

**COVERAGE: covered (bounded) for the declared classes on the declared chain —
no coverage failure; one disclosed residual requiring a closure decision.**

What is proven, all on the frozen revision and by my own runs rather than by
reading the producer's claims:

- the declared chain is frozen and verifies 4/4 clean, and my independently
  recomputed content digests match all four pins byte-for-byte;
- the BR-01 reduction class is caught with a stable FINDING ID and exit 1, at
  three different chain positions and depths (r94 tick-10; r96 mid-event; r96
  deepest event), where all four pre-existing gates exit 0;
- the adjacent addition and endpoint classes are caught the same way,
  including the valid-endpoint swap that no pre-existing gate sees;
- changes the inventory does not model exit 2 rather than 0 (fail-closed);
- the exit contract 0/1/2 holds across 20 scenarios, the verdicts are
  deterministic under hash-seed variation, and `--self-test` passes 14/14 with
  persisted expectations and no scratch residue.

What is not proven / not claimed: that the frozen inventories are the *right*
ones beyond the pin (the pin is only as good as its freeze-time review); that
the gate runs anywhere automatically (bound 6); or that the freeze survives
the unguarded `--freeze` path (bounds 1–2).

Residual requiring a closure decision: the delivered
`corpus/tools/dependency-freeze-contract.json` at `7d568cc4…` carries the stray
`c3red` pin freezing a reduced fixture from another seat's scratch directory
(§4.1). It does not break the declared chain verification, it is disclosed by
the producer's own report §7 rather than hidden, and both the producer and this
seat assess it as harmless to verification semantics but a real tool hazard.
Recommended closure action (either is one small change): delete `pins.c3red`,
or add a `--freeze` scope guard refusing paths outside `corpus/fixtures/`.
Re-verifying the chain afterwards is a one-command check
(`python3 corpus/tools/dependency_freeze.py corpus/fixtures/<chain member>`).

## 6. Poll-wait record

Per protocol: polled 20 s cadence for `corpus/tools/dependency_freeze.py` +
`dependency-freeze-contract.json` and any `Q3*.md` producer report. First
sighting of the tool at 17:42 (contract 8113 B, 3 pins); contract grew to
10348 B (4 pins) during my first read, and to `7d568cc4…` (5 pins, including
the stray `c3red`) at 17:44 — so the artifacts were revised twice while I
tested, and every result above was re-run against the final hashes. **Q3's
producer report landed at 17:47:36-03:00** (`.ufo/waves/round-96/seats/Q3-dependency-freeze.md`,
12100 B); the artifacts were unchanged between my final battery and that report,
and Q3's report states the same two hashes verified here
(`a3b57978…` / `7d568cc4…`), so the verdict above is against the delivered
revision and no re-run was needed. Q3's report independently corroborates
§1–§3 of this seat (cross-gate blindness, the 4/4 clean chain, the finding IDs)
and discloses the `c3red` anomaly (§4.1).

## Bottom line

**PASS (bounded, one disclosed residual)** — on the delivered revision
(`dependency_freeze.py` `a3b57978…`, contract `7d568cc4…`, confirmed identical
in Q3's producer report) the C3 gate covers the declared chain and the
reduce/addition/endpoint/digest classes where every pre-existing gate is blind,
verifies 4/4 clean with my independently recomputed digests matching all four
pins, and holds the 0/1/2 exit contract deterministically; bounds are
chain-scoped pins, basename keying, byte sensitivity, no admitted-path
registration, and an unguarded `--freeze` that already laundered a reduction
into the delivered contract as the stray `c3red` pin — disclosed by Q3's report
§7, harmless to chain verification, and recommended for deletion or a
`--freeze` scope guard at closure.
