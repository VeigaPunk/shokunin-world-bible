# V57 — crosscheck-coverage (round 96)

**Seat:** V57 `verdict-crosscheck-coverage`. Scope: independently derive the
COVERAGE verdict on C3 (`corpus/tools/dependency_freeze.py` +
`corpus/tools/dependency-freeze-contract.json`, BR-01 closure) and compare it
with V33 `verdict-coverage`. Report path (only file written besides scratch):
this file. Scratch:
`.ufo/waves/round-96/seats/V57-scratch/` (absolute
`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats/V57-scratch/`).
All commands from the lane repo root with `python3` (3.14.7); no commits, no
pushes, no network, no nested agents, live corpus never modified (all mutations
on scratch copies; live contract byte-checked before/after every probe).

**Baseline** r95 closure `dcb2d92`; HEAD at test time
`60dba0c2aa344860b10a2fc63e00468d1b134f27`.

**Revision under verdict (frozen):**

```
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
```

Artifacts were revised in-flight several times (`f4b5208f…` → `d17297bb…` →
`a3b57978…`; contract `2601c18a…` → `7d568cc4…`); every result below is stated
against the hashes above and was re-run after Q3's producer report landed
(`Q3-dependency-freeze.md`, 17:47, bottom line PASS) — no byte changed after
17:44:37, so the verdict covers the delivered revision.

Poll-wait protocol observed: 20 s cadence poll (`V57-scratch/poll.sh`,
log `V57-scratch/poll.log`) for both tool files + `Q3*.md` + `V33*.md` +
the r96 fixture; `ALL_PRESENT at try 26 17:47:33`. Preliminary runs on in-flight
bytes are labeled as such below.

## 1. Independent derivation of the coverage verdict

### 1.1 BR-01 gap reproduced with the pre-existing gates (my own copies)

Mutation: scratch copy named `r94-paired-crossing` under
`V57-scratch/mut-reduction/`, `evin-ninth-bell` dropped from the tick-10
`depends_on`. My own extractor (`V57-scratch/independent_edges.py`, written
before reading the C3 tool) confirms the edge inventory.

```
$ python3 corpus/fixtures/check_bible.py .ufo/waves/round-96/seats/V57-scratch/mut-reduction/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations      # exit 0
$ python3 corpus/tools/support_check.py .ufo/waves/round-96/seats/V57-scratch/mut-reduction/r94-paired-crossing
RESULT PASS                                                       # exit 0
```

The debt is real: the exact BR-01 reduction is invisible to the fixture-level
gates. (Mechanism, from code: `check_bible.py:393-414` checks member shape,
unknown ids and tick inversion, never an expected edge *set*; `support_check`
never reads `depends_on` values.)

### 1.2 Frozen-revision battery (my runs)

Clean chain — 4/4 exit 0, receipts and digests quoted verbatim:

```
$ for d in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do python3 corpus/tools/dependency_freeze.py corpus/fixtures/$d; echo "exit=$?"; done
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279 / RESULT PASS  exit=0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75 / RESULT PASS  exit=0
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9 / RESULT PASS  exit=0
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6 / RESULT PASS  exit=0
```

Mutation classes (scratch copies keep the pinned basename — pin lookup is
basename-keyed, `dependency_freeze.py:251-252`):

| probe (my copy) | observed |
|---|---|
| reduction: tick-10 loses `evin-ninth-bell` (BR-01) | exit 1 `FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']` |
| addition: tick-11 gains `aru-ninth-bell` | exit 1 `FINDING ADDITION-DETECTED: event aftermath-missing-evin gained depends_on ['aru-ninth-bell']` |
| self-loop addition | exit 1 `ADDITION-DETECTED: … gained depends_on ['paired-crossing-decision']` |
| relation `from`/`to` swapped | exit 1 `FINDING ENDPOINT-CHANGE: relation endpoints changed: removed [aru, evin, …]; added [evin, aru, …]` |
| r96 deepest edge dropped (V33 row-9 scenario, spot-check) | exit 1 `REDUCTION-DETECTED: event response-evin-salt-court lost depends_on ['aftermath-missing-evin']` (edges 3/4) |
| description byte drift (outside the modeled inventory) | exit 2 `FINDING DIGEST-MISMATCH: … != pin 2527beb9…; fixture bytes changed outside the frozen inventory` |
| `entities.json` / `sources.json` tamper | exit 2 `DIGEST-MISMATCH` (digest covers all five data files) |
| malformed `timeline.json` | exit 2 `MALFORMED-JSON` |
| `relations.json` removed | exit 2 `FILE-MISSING` |
| non-chain fixture (`r87-myth-cluster`) | exit 2 `UNPINNED-FIXTURE` (lists the four pins + `c3red`, see §1.5) |
| no arguments / `--self-test` + fixture | exit 2 `INVALID-ARGUMENTS` |
| r96 unpinned new event, no deps (V33 row-15 scenario, spot-check) | exit 2 `DIGEST-MISMATCH` (fail-closed, not silent 0) |

Stability: two consecutive runs of the reduction verdict are byte-identical
(`diff run1.txt run2.txt` empty), and the live tool/contract hashes are
unchanged by all verification runs (no `--freeze` side effect from verify).

`--self-test`: `SELF-TEST 14/14` / `RESULT PASS` / exit 0
(`V57-scratch/selftest-final.txt`; 14 `ok` lines counted). Isolation: cases run
under `tempfile.TemporaryDirectory` (`/var/tmp/…`), and no
`dependency-freeze-self-test-*` residue remains after the run. `--freeze`
tested only in a sandbox mirror root (`V57-scratch/freeze-test/`, tool+contract
copied): rebuilds the pin and then verifies PASS; the live contract stayed
`7d568cc4…` byte-identical throughout.

### 1.3 Independent pin comparison (no tool code used)

`V57-scratch/compare_contract.py` (my own implementation of the contract's
declared semantics) re-derived each pin from the fixture bytes: event id →
sorted `depends_on` set, event endpoints, relation triples, per-file sha256s,
the aggregate `content_sha256` (sha256 over the canonical JSON of per-file
sha256s), and counts. Result:

```
r88-m3-maya-cluster: ALL-MATCH
r94-paired-crossing: ALL-MATCH
r95-crossing-aftermath: ALL-MATCH
r96-crossing-response: ALL-MATCH
OVERALL: ALL PINS MATCH MY INDEPENDENT EXTRACTION
```

This independently confirms the C3 claim that the four pins freeze the
delivered bytes — including the r96 pin (`timeline.json` `ea0225f9…`,
`sources.json` `9f973f63…`) against Q4's final write (17:40:16, after a
mid-write state I observed at 17:38 — the pin covers the delivered revision).

### 1.4 Corpus modification audit

At my final snapshot, `git status --porcelain` (corpus paths):

```
 M corpus/tools/map_obligations.py                 # Q1 (declared)
?? corpus/fixtures/r96-crossing-response/          # Q4/Q5 (declared)
?? corpus/knowledge/r96-response-scope-note.md     # Q6 (declared)
?? corpus/tools/dependency-freeze-contract.json    # Q3 (declared)
?? corpus/tools/dependency_freeze.py               # Q3 (declared)
```

C3's own footprint is exactly the two new tool files; no fixture file is
modified (`git hash-object` vs `git rev-parse dcb2d92:` → 15/15 inherited data
files blob-identical for r88/r94/r95, matching V33's claim). Observed in
passing (not C3): a transient repo-root stray `map-obligations-self-test-3q8sbs4z/`
appeared in one `git status` (17:48) and was gone moments later — the known
BR-05 residual class for `map_obligations`, live again mid-round but not
present at my final snapshot.

### 1.5 Anomaly independently confirmed: the `c3red` pin

The delivered contract carries a fifth pin not in the declared chain:

```
pins: ['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response']
c3red | fixture ".ufo/waves/round-96/seats/V41-scratch/c3red" | counts {events 3, dependency_edges 1, relations 1}
```

I read the pinned scratch fixture directly: `paired-crossing-decision
depends_on == ['aru-ninth-bell']` — i.e. the pin freezes the BR-01 *reduction*
from another seat's scratch path. Origin trail: `V41-scratch/c3-freeze.out`
shows `FROZEN c3red … RESULT PASS` (a `--freeze` run on that copy wrote the
live contract, since `freeze()` writes `CONTRACT_PATH` with no scope guard).
Impact on the declared chain: none — all four chain pins match my independent
extraction (§1.3), and `c3red` is not a corpus fixture. The hazard is the
unguarded write path itself (`--freeze` on any copy *named* like a pinned
fixture would overwrite that pin); Q3 disclosed the anomaly in its report §7
and deliberately left it in place so as not to invalidate verifier receipts
that already quote the pinned list (V33's battery transcript, V22 scratch).
V41's own report was still absent at my final write.

### 1.6 In-flight self-test defect (observed, then fixed)

At the revision I first read (`f4b5208f…`, 17:43) the self-test had a
late-binding closure bug (`cases[name] = (lambda: [scratch], …)` capturing the
reassigned variable). My run at ~17:44 (consistent with `d17297bb…`, the
revision V49 also tested) produced:

```
SELF-TEST 5/14
FINDING SELF-TEST-MISMATCH: cases failed: ['addition_edge_phantom', 'digest_tamper', 'event_endpoint_change', 'event_removed', 'malformed_json', 'reduction_edge_drop', 'relation_added', 'relation_endpoint_flip', 'relation_removed']
RESULT FAIL   exit 1
```

— all nine failed cases executed against the last-built `missing_timeline`
scratch. At the frozen revision `a3b57978…` the same command gives
`SELF-TEST 14/14` / `RESULT PASS` / exit 0; Q3's report §5 records the same
defect and fix. Corroborated independently by V49 §5 (same 5/14 signature).

## 2. Comparison with V33

V33's report was read in two revisions: `448ed389…` (interim, before Q3's
producer report landed) and the final `33e8a359…` (after; supersedes the
former). All comparisons below use the final revision.

**Points of agreement (my independent runs vs V33):** frozen revision hashes;
4/4 chain clean with digests recomputed independently and matching all four
pins; BR-01 exit 1 with the same FINDING text; addition/endpoint classes;
digest guard exit 2 for non-inventory bytes; `--self-test` 14/14; basename
keying; chain-scoped coverage (non-chain fixtures exit 2); byte sensitivity
(reformatting → exit 2); no registration in SKILL.md/READMEs (I re-ran the
grep: no hits); 15/15 inherited blobs identical to `dcb2d92`; the `c3red`
stray pin and its origin; the in-flight self-test defect and its fix; and
V33's final verdict language — "no coverage failure; one disclosed residual
requiring a closure decision" — matches my reading. Two of V33's extra
scenarios I re-ran independently and reproduced exactly (r96 deepest edge
drop → exit 1; unpinned new event → exit 2), and its `FIXTURE-MISSING` vs
`UNPINNED-FIXTURE` basename nuance matches my runs (§1.2 rows).

**Divergences:**

1. **`c3red` framing — resolved between V33's own revisions.** V33's interim
   revision (`448ed389…`) called the stray pin a "blocking delivery defect"
   and asked for removal before admission; its final revision (`33e8a359…`,
   written after Q3's report landed) restates it as a disclosed residual with
   a recommended delete-or-guard closure action. My independent read —
   confirmed pin, chain verification unaffected, hygiene defect for closure —
   agrees with V33's final framing and with Q3's own assessment (report §7).
   Whether it blocks admission is a call for L1/L2, not for this seat; all
   three accounts rest on the same verified facts.
2. **In-flight self-test narrative (unchanged in V33's final revision).** V33
   §3 describes the earlier failure as `SELF-TEST 2/14` with 12 cases
   returning `UNPINNED-FIXTURE` (a basename-nonpreserving copy symptom),
   attributed to `f4b5208f…`/`d17297bb…`. At `f4b5208f…` I read a
   name-*preserving* `copy_case` with late-binding lambdas, and both my run
   and V49's show the 5/14 closure signature, not 2/14. V33 most likely
   tested an even earlier unhashed revision. Not material to the verdict
   (both defects were fixed at `a3b57978…`, which passes 14/14), but the hash
   attribution in V33 §3 should not be relied on.

**Where I go beyond V33:** my pin comparison was implemented from scratch
(`compare_contract.py`, no import of the tool) and covers events/endpoints/
relations/files/content-digest/counts per fixture; I additionally probed
digest coverage of `entities.json`/`sources.json`, self-loop addition, and the
sandboxed `--freeze` path; and I pinned my verdict to the post-Q3-report
revision and to both V33 report revisions.

## 3. Bounds of this verdict

What is shown: on the frozen revision, the declared chain is frozen and
verifies 4/4 clean with pins matching an independent extraction; the BR-01
reduction and adjacent addition/endpoint classes fail closed with stable
FINDING IDs and exit 1 where every pre-existing fixture gate exits 0; the
0/1/2 exit contract holds across my probes; `--self-test` passes 14/14 with
persisted expectations and no scratch residue; C3's corpus footprint is the
two declared files. What is not shown: that the frozen inventories are
semantically *right* beyond the pin (the pin is only as good as its
freeze-time review); that the gate runs automatically anywhere (it is not
registered in any runner/README/SKILL — it protects only when invoked); that
the unguarded `--freeze` write path is safe (it already wrote the `c3red`
pin into the delivered contract); or anything about axes other than coverage.

## Bottom line

**PASS (bounded) — coverage verdict independently derived and V33 cross-checked:**
on the frozen revision (`dependency_freeze.py` `a3b57978…`, contract
`7d568cc4…`) the dependency-freeze gate covers the declared chain and the
BR-01 reduce/addition/endpoint/digest classes (4/4 clean, exit 1/2 as
declared, self-test 14/14), with my from-scratch pin extraction matching all
four pins; V33's final report (`33e8a359…`) agrees on every material point,
including "no coverage failure; one disclosed residual requiring a closure
decision". Confirmed caveats: the stray `c3red` reduction-bearing pin from
V41's unguarded `--freeze` probe sits in the delivered contract (resolve at
closure; V33's interim "blocking" framing was softened in its final revision),
and V33's in-flight 2/14 self-test hash attribution is inaccurate — neither
changes the verdict, and no coverage harm was found.
