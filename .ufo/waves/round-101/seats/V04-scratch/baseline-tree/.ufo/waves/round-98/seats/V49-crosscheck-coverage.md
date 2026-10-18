# V49 — crosscheck-coverage (round 98, single-wave)

**Seat scope (verbatim):** *V49 verdict-crosscheck-coverage — report
.ufo/waves/round-98/seats/V49-crosscheck-coverage.md — Independent coverage
verdict; compare V26.*

Claim under test — **C2 (coverage):** "extend the frozen chain through the
round's own fixture. After S3 authors `r98-clerk-filing`, S1 pins BOTH
`r97-crossing-acknowledgment` and `r98-clerk-filing` via the guarded `--freeze`;
the chain becomes six fixtures (r88-m3, r94, r95, r96, r97, r98) verifying 6/6
clean; V46's recorded FAIL (the r97 tick-13 edge unfrozen) is discharged by the
pin, demonstrated by a scratch REDUCTION-DETECTED on the r97 edge."

Lane root for every command: `/home/vgpnk/Projects/shokunin/lore-shokunin`
(session cwd is the PARENT repo; every path below is absolute or lane-root
anchored). Baseline r97 closure `9a3d648`; HEAD during the wave
`dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb` (wave tree uncommitted). Leaf seat:
no nested agents, no commits, no pushes, no network. Writes: this report plus
`.ufo/waves/round-98/scratch/V49/` only (realpath of the seats dir checked
before writing: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats`).

## 0. Revision pinned for every measurement (re-checked after all runs)

```
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py          (S1)
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json (S1, 6 pins, 17 cases)
73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b  corpus/fixtures/r97-crossing-acknowledgment/timeline.json
eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af  corpus/fixtures/r98-clerk-filing/timeline.json
dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb  (git rev-parse HEAD)
```

All four hashes re-measured after the battery and unchanged (23:37:49).
V26's mid-flight note (contract `c435239d…` → `153ebc5b…`, `provenance_note`
paragraph only) is consistent: **every number quoted below is from the battery
run on the final `153ebc5b…` revision** (run 23:36, re-verified after).

## 1. Poll-wait record (20 s cadence, 40 tries; never verify a plan)

My poll set: S1 report, S3 report, contract pins r97+r98, r98 JSON tables,
V26 report. **SELF (V49) was never in any wait set**; no all-reports poll was
attempted (endgame convention honoured).

```
try 5  23:31:06 missing: CONTRACT-PINS REPORT:S1 REPORT:V26      (S3 report had landed)
try 21 23:36:26 missing: REPORT:V26
try 24 23:37:26 ALL-PRESENT
```

No stall escape needed. Two early observations from the same window:
(a) S1's contract was first seen with 6 pins at 23:32:53 and its report landed
before my battery (S1 report mtime 20:33 local = 23:33 UTC; contract mtime
20:33:36 local); (b) the r98 fixture existed as a *placeholder byte-copy of
r97* before S4's rewrites (S3 §D1 hazard) — my poll checked parsed content
(`clerk-maren` in entities, 7 timeline rows), not existence, and the r98
verification below is against the frozen tables, not the placeholder docs.

## 2. Pre-state (baseline bytes, contract `27273be2…`-era, 23:29) — V46's FAIL reproduced live

Before any producer landed, the delivered tool on the delivered tree:

```
=== r88-m3-maya-cluster === RESULT PASS  exit=0
=== r94-paired-crossing === RESULT PASS  exit=0
=== r95-crossing-aftermath === RESULT PASS  exit=0
=== r96-crossing-response === RESULT PASS  exit=0
=== r97-crossing-acknowledgment ===
FINDING UNPINNED-FIXTURE: no pin for 'r97-crossing-acknowledgment' in corpus/tools/dependency-freeze-contract.json
(pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response'])
RESULT ERROR  exit=2
```

This is exactly the state V46's r97 FAIL recorded (`.ufo/waves/round-97/seats/V46-cross-gates.md` §3).

## 3. Post-state — chain 6/6, independent pin recompute (final revision)

Chain replay, delivered tool on delivered paths (`.ufo/waves/round-98/scratch/V49/battery-run1.txt`):

```
--- r88-m3-maya-cluster ---  FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
  DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279   RESULT PASS  exit=0
--- r94-paired-crossing ---  events 3/3; dependency-edges 2/2; relations 1/1
  DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75   RESULT PASS  exit=0
--- r95-crossing-aftermath ---  events 4/4; dependency-edges 3/3; relations 1/1
  DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9   RESULT PASS  exit=0
--- r96-crossing-response ---  events 5/5; dependency-edges 4/4; relations 1/1
  DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6   RESULT PASS  exit=0
--- r97-crossing-acknowledgment ---  events 6/6; dependency-edges 5/5; relations 1/1
  DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6   RESULT PASS  exit=0
--- r98-clerk-filing ---  events 7/7; dependency-edges 6/6; relations 1/1
  DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133   RESULT PASS  exit=0
```

Independent recompute (`V49-scratch/recompute.py`; does **not** import the
tool — re-derives event→sorted-depends_on sets, tick/entity_id/place_id
endpoints, relation triples, per-file sha256 and the compact sorted-JSON
content digest from raw bytes, then compares to the contract):

```
PIN r88-m3-maya-cluster: revision=60dba0c2… OK      PIN r94-paired-crossing: revision=60dba0c2… OK
PIN r95-crossing-aftermath: revision=60dba0c2… OK   PIN r96-crossing-response: revision=23939342… OK
PIN r97-crossing-acknowledgment: revision=dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb OK
PIN r98-clerk-filing: revision=dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb OK
RECOMPUTE ALL-PINS-MATCH   exit=0
```

Pin set is **exactly the six declared chain fixtures, no extras**; the four
inherited digests are byte-identical to the pre-round contract (r95's map
repair does not touch the pinned five-JSON payload — S3 §A; V15 confirms).
r98 pin payload: `counts {events 7, dependency_edges 6, relations 1, entities 6,
sources 7}`, `clerk-filing-open` tick 14, `depends_on ['acknowledgment-aru-records']`,
endpoint `{tick: 14, entity_id: clerk-maren, place_id: chalk-stair}`.

Inheritance check (r98 must be a preserving copy of r97's frozen inventory):

```
r98 pin preserves every r97 pinned event exactly: True
r98-only events: ['clerk-filing-open']
r98 relations == r97 relations: True
```

On-disk cross-checks: r98 `timeline.json` `eb24e084…` (byte-prefix identical to
r97's `73063a86…` for rows 0–5; entities/sources/relations prefix-identical;
excerpt prefix byte-identical at `8ba491cb…`) — matches S3's report §B hashes
character-for-character.

Revision sanity (not this seat's verdict): `--self-test` → `SELF-TEST 17/17`,
`RESULT PASS`, exit 0.

## 4. "Via the guarded `--freeze`" — independent reproduction

Mirror root `V49-scratch/mirror2/` holds byte copies of the delivered tool and
contract plus the r97/r98 fixtures at their pinned repo-relative paths; the
delivered contract was never written (all my `--freeze` runs are in mirrors).

```
$ python3 <mirror2>/corpus/tools/dependency_freeze.py --freeze <mirror2>/corpus/fixtures/r97-crossing-acknowledgment
FROZEN r97-crossing-acknowledgment: events 6; dependency-edges 5; relations 1
DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6        exit=0
$ python3 <mirror2>/corpus/tools/dependency_freeze.py --freeze <mirror2>/corpus/fixtures/r98-clerk-filing
FROZEN r98-clerk-filing: events 7; dependency-edges 6; relations 1
DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133        exit=0
PIN-REPRODUCIBILITY r97-crossing-acknowledgment: EXACT-MATCH   (full pin payload == delivered pin)
PIN-REPRODUCIBILITY r98-clerk-filing: EXACT-MATCH
```

Guard still armed (mirror probe, out-of-scope target):

```
FINDING SCOPE-REFUSED: --freeze refuses .ufo/waves/round-98/scratch/V49/outscope (resolves to …);
the frozen scope is corpus/fixtures/** (integration-time operation only)   RESULT ERROR  exit=2
mirror contract unchanged: True
```

**Bound:** I did not witness S1's original invocation; the "guarded `--freeze`"
attribution rests on (a) S1's report §4 receipts, (b) the contract
`provenance_note` r98 paragraph, (c) my exact reproduction of both pin payloads
through the delivered guarded path on identical bytes, and (d) the pins'
`revision` `dd4df1b…` = HEAD at freeze time. No contradiction found.

## 5. V46 discharge — own mirror replay at V46's exact bytes

Mutation (drop the r97 tick-13 edge, V46's class), then verify against the
delivered r97 pin payload:

```
MUTATION event=acknowledgment-aru-records before=['response-evin-salt-court'] after=[]
mutated r97 timeline sha256: 37a425b97af658d71b8dc8904f43fd75859905bac326489a71adb67004004eb1
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5; relations 1/1
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
RESULT FAIL   exit=1
```

`37a425b9…` is **byte-identical** to the sha V46 recorded for its r97 scratch
copy (V46 §1/§4; S1 §4; V06; V54). Control: the same mirror on the intact r97
copy → `events 6/6; dependency-edges 5/5; relations 1/1`, `RESULT PASS`, exit 0.
So round-97's `UNPINNED-FIXTURE` exit 2 on identical bytes is now
`REDUCTION-DETECTED` exit 1 — the r97 tick-13 edge is frozen and load-bearing.

Bonus (the sixth fixture's own new edge): dropping `acknowledgment-aru-records`
from `clerk-filing-open` (mutated r98 timeline sha
`ddec7a072fa21919ca1faeae49f7ee7b7f1eae20bcd36653942eee58cceec34f`):

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL   exit=1
```

## 6. Coverage bounds — independently probed (all on the delivered pins)

- **Non-inventory JSON change** (trailing space in `clerk-filing-open.description`):
  `FINDING DIGEST-MISMATCH: content digest c8d3c40a… != pin 59a0f4fa…; changed: timeline.json
  (sha256 eb24e084… -> 2f6684c9…); fixture bytes changed outside the frozen inventory`, exit 2 —
  caught, but as could-not-evaluate, not an exit-1 finding.
- **Markdown change** (line appended to r98 `README.md`, timeline restored first):
  `DIGEST 59a0f4fa…` / `RESULT PASS`, exit 0 — markdown is outside the pin payload;
  BR-01's prose half remains open (declared).
- **Foreign-path copy** (delivered tool, r98 copied under `V49-scratch/foreign/`):
  `FINDING PATH-MISMATCH: pin r98-clerk-filing names corpus/fixtures/r98-clerk-filing
  (resolves to …); invoked fixture resolves to …/.ufo/waves/round-98/scratch/V49/foreign/r98-clerk-filing`,
  exit 2 — the catch is bound to the pin's recorded path.
- **Declared-list bound:** an unpinned fixture is refused only when invoked
  (`UNPINNED-FIXTURE` exit 2 — pre-state §2); nothing enumerates
  `corpus/fixtures/**`.

## 7. Cross-check against V26 (`.ufo/waves/round-98/seats/V26-verdict-coverage.md`)

Every shared value agrees; no contradiction between the two verdicts.

| item | V26 | V49 (mine) | match |
|---|---|---|---|
| chain 6/6 digests | 15ef230e…/2527beb9…/d541ae64…/d422a9b3…/3c922d20…/59a0f4fa… | identical, all `RESULT PASS` exit 0 | yes |
| pin recompute | 6/6 match, exactly six pins | `RECOMPUTE ALL-PINS-MATCH` | yes |
| pin revisions | r88/r94/r95 `60dba0c2…`, r96 `23939342…`, r97/r98 `dd4df1b…` | identical | yes |
| r97 discharge mutation sha | `37a425b9…` → REDUCTION-DETECTED exit 1 | identical bytes, identical finding/exit | yes |
| r98 edge drop | `ddec7a07…` → REDUCTION-DETECTED exit 1 | identical bytes, identical finding/exit | yes |
| guarded reproducibility | r97/r98 digests equal delivered pins | EXACT-MATCH both | yes |
| self-test | 17/17 PASS | 17/17 PASS | yes |
| bounds (digest half, markdown, path) | exit 2 / PASS / exit 2 | independently reproduced | yes |
| stray audit | declared paths only | declared paths only | yes |

V26's recorded **minor contradiction** (S1 §6 / S2 wording that
`git diff 9a3d648 -- corpus/tools/` "lists only" the tool + contract)
independently reproduced:

```
$ git diff --name-only 9a3d648 -- corpus/tools/
corpus/tools/README.md
corpus/tools/dependency-freeze-contract.json
corpus/tools/dependency_freeze.py
```

Three files (the third is S2's own addendum). Wording slip, not a coverage
defect — substance (`map_obligations.py`, `map-obligations-contract.json`,
`support_check.py`, `boundary_doc_check.py` byte-unchanged) is true.

V26's **parent-repo stray observation** independently reproduced (read-only):
`/home/vgpnk/Projects/shokunin/baseline-analyze.txt`, 105 bytes, mtime 20:30,
contents `python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py':
[Errno 2] No such file or directory` — outside the lane, unattributed, left
untouched for the L1.

Neighbor C2 seats agree on every shared value as well: V06-c2-v46-discharge
(same `37a425b9…`, exit 1; foreign-path `PATH-MISMATCH` control) and
V54-six-chain-integrity (same `ddec7a07…`; both new edges frozen and
load-bearing).

## 8. Bounds of this coverage verdict

1. Pin payload = the five JSON tables only; markdown is not pinned (probe §6).
2. Exit-1 findings cover `depends_on` edges, event endpoints, relation triples;
   all other JSON changes are at most exit-2 `DIGEST-MISMATCH`.
3. The chain is a declared list, not self-enforcing (§6).
4. Pin `revision` names HEAD `dd4df1b` while wave bytes are uncommitted; the
   binding is the content digest, which I reproduced through the guarded path.
   S1's original command history is not witnessed (§4 bound).
5. "Discharged" means: the pin exists, the delivered fixture verifies clean,
   and V46's exact mutation bytes yield `REDUCTION-DETECTED` exit 1 — verified
   here independently and consistent with V06/V26/V54. V46's r97 FAIL remains
   recorded in r97 history.
6. No canon-truth, rights, identity, or entailment inference; the verdict is
   about the frozen dependency inventory only.

## 9. Write audit

`git status --porcelain` at write time shows exactly: `M LOG.md` (round-98
declaration), `M corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md`
(S3 repair), `M corpus/knowledge/r95-aftermath-scope-note.md` +
`M corpus/knowledge/r96-response-scope-note.md` (S5), `M corpus/tools/README.md`
(S2), `M corpus/tools/dependency-freeze-contract.json` +
`M corpus/tools/dependency_freeze.py` (S1), `?? .ufo/waves/round-98/`,
`?? corpus/fixtures/r98-clerk-filing/`, `?? corpus/knowledge/r98-clerk-scope-note.md`
— nothing else; no strays, no commits. Final hash sweep after all my runs:
tool `03d04365…`, contract `153ebc5b…`, r97 timeline `73063a86…`, r98 timeline
`eb24e084…` — unchanged across my whole measurement window. My writes live only
under `.ufo/waves/round-98/scratch/V49/` (poll.sh, poll.log, recompute.py,
battery.sh, battery-run1.txt, baseline-chain.txt, mirror/mirror2/mirror3,
foreign, outscope, discharge_probe.py) plus this report.

## Bottom line

**PASS — COVERAGE verdict: improved and verified (bounded), independently
concurring with V26.** On the frozen revision (tool `03d04365…`, contract
`153ebc5b…`, exactly six pins) the chain verifies 6/6 clean; all six pins pass
an independent raw-byte recompute (event sets, endpoints, relation triples,
per-file and content digests); the r97/r98 pins reproduce EXACT-MATCH through
the guarded `--freeze` with the scope guard still armed; and V46's recorded r97
FAIL is discharged — its exact mutation bytes (`37a425b9…`) now yield
`REDUCTION-DETECTED` exit 1 where round-97 yielded `UNPINNED-FIXTURE` exit 2 —
bounded to the five-JSON-table payload, the declared six-fixture list, and
exit-2-only detection for non-inventory JSON changes, with BR-01's markdown
prose half still open. No contradiction found against V26 beyond its own
recorded (and here reproduced) doc-wording slip.
