# V18 — c3-addition-endpoint (round 96)

- Seat: V18, verifier. Claim under test: **C3 / coverage** — new gate
  `corpus/tools/dependency_freeze.py` + `corpus/tools/dependency-freeze-contract.json`
  closing BR-01, verified at the addition / endpoint / deletion mutation classes.
- Protocol: poll-wait 20 s cadence, 40 tries. `POLL_HIT try=29` (t=580 s, 17:47:20):
  tool present at try 14 (17:42), contract at try 15, Q3 producer report
  `.ufo/waves/round-96/seats/Q3-dependency-freeze.md` at try 29. All verification below
  ran **after** the producer report existed.
- Verified revision (hashed before and after the full battery; unchanged):

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
```

- Scratch: `.ufo/waves/round-96/V18-scratch/` (`mutate.py`, `probe.py`, `oracle.py`,
  `pincheck.py`, `extra_probes.py`, `battery.sh`, `logs/`, `sandbox/`, `scratch-root/`).
  Mutations were applied **only** to copies under `scratch-root/`; copies keep the pinned
  fixture basename (`pin_for()` keys on `fixture.resolve().name`). Corpus was read-only here.

## 1. Baseline — 4/4 clean on the real chain (exit 0)

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
    python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; echo "exit=$?"; done
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279 / RESULT PASS  exit=0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75 / RESULT PASS  exit=0
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9 / RESULT PASS  exit=0
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6 / RESULT PASS  exit=0
```

Digests equal the contract pins exactly. A scratch copy of r95 (basename preserved)
also exits 0 with identical output — the pin resolves by basename, not by path.

## 2. Declared mutation classes — each run twice, byte-identical output

**B3 phantom `depends_on` addition (r96 `response-evin-salt-court` += `phantom-tick-13`):**

```
FINDING ADDITION-DETECTED: event response-evin-salt-court gained depends_on ['phantom-tick-13']
RESULT FAIL            run1 exit=1 / run2 exit=1, identical_output=True
FREEZE r96-crossing-response: events 5/5; dependency-edges 5/4; relations 1/1
```

**B4 relation `from`/`to` flip (r96):**

```
FINDING ENDPOINT-CHANGE: relation endpoints changed: removed [aru, evin, agreed_co_stewardship_for_this_crossing];
  added [evin, aru, agreed_co_stewardship_for_this_crossing]
RESULT FAIL            run1 exit=1 / run2 exit=1, identical_output=True
```

**B5 true endpoint change (`aru` → `jorin`, r95):**

```
FINDING ENDPOINT-CHANGE: relation endpoints changed: removed [aru, evin, agreed_co_stewardship_for_this_crossing];
  added [jorin, evin, agreed_co_stewardship_for_this_crossing]
RESULT FAIL            run1 exit=1 / run2 exit=1, identical_output=True
```

**B6 event row deletion with its edges (r96 `aftermath-missing-evin`; the dangling edge in
`response-evin-salt-court` was stripped too) — FINDING class quoted:**

```
FINDING REDUCTION-DETECTED: event aftermath-missing-evin is missing; 1 frozen dependency edge(s) gone
FINDING REDUCTION-DETECTED: event response-evin-salt-court lost depends_on ['aftermath-missing-evin']
RESULT FAIL            run1 exit=1 / run2 exit=1, identical_output=True
FREEZE r96-crossing-response: events 4/5; dependency-edges 2/4; relations 1/1
```

Deletion class is `REDUCTION-DETECTED` (two lines: the removed event, and the dependent that
lost its edge). Counter receipt shows 4/5 events and 2/4 edges.

**B7 BR-01 reduction (r94 tick-10 loses `evin-ninth-bell`):**

```
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL            run1 exit=1 / run2 exit=1, identical_output=True
```

**B8 digest-only, inventory-neutral text tamper (r95 description edit):**

```
FINDING DIGEST-MISMATCH: content digest c4a415346bae4538e1bc080b4a6bb4d8a867f6790a22f30d81d86cc7a40fb35c
  != pin d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9;
  fixture bytes changed outside the frozen inventory
RESULT ERROR           run1 exit=2 / run2 exit=2, identical_output=True
```

## 3. Extra addition-class probes (mine, beyond the declared demos)

| probe on scratch copy of r96 | observed |
|---|---|
| new event row **with** `depends_on` | exit 1 `FINDING ADDITION-DETECTED: unpinned event intruder-tick-13 introduces depends_on ['response-evin-salt-court']` (x2 identical) |
| new event row **without** `depends_on` (inventory-neutral) | exit 2 `FINDING DIGEST-MISMATCH: … 278e3994… != pin d422a9b3…` (x2 identical) |
| new relation triple | exit 1 `FINDING ADDITION-DETECTED: relation edge(s) added: [evin, aru, second_account_same_occasion]` (x2 identical) |

Nuance, not a defect: an added event with **no** dependency edge is not classified as an
"addition" — it exits 2 DIGEST-MISMATCH. That is exactly the precedence documented in the
contract ("a content digest change the frozen inventory does not model exits 2") and it is
fail-closed (never silently PASS), but a reviewer expecting `ADDITION-DETECTED` for every
added row should know the boundary: only rows that carry dependency edges are classified.

## 4. Self-test, persisted expectations, and fail-closed coupling

```
$ python3 corpus/tools/dependency_freeze.py --self-test   # x2
SELF-TEST 14/14 / RESULT PASS / exit=0   (both runs)
```

Isolated sandbox (copy of tool + contract + base fixture under
`V18-scratch/sandbox/`, delivered bytes untouched — hashes re-checked unchanged):

```
unchanged copy      -> SELF-TEST 14/14 / RESULT PASS / exit=0
one persisted case dropped from the contract copy
                    -> FINDING CONTRACT-INVALID: self-test expectation set mismatch;
                       missing=['relation_added'] extra=[]
                       RESULT ERROR / exit=2
```

The persisted-expectation coupling is real and fails closed: an edited expectation set is
refused (exit 2), it does not silently re-baseline.

Exit-2 surfaces: unpinned name → `UNPINNED-FIXTURE` exit 2; missing dir → `UNPINNED-FIXTURE`
exit 2; no args → `INVALID-ARGUMENTS` exit 2; `--self-test` + fixture → `INVALID-ARGUMENTS`
exit 2. No traceback on any path observed.

## 5. Independent pin-vs-oracle cross-check (my own oracle, not the tool's code)

`.ufo/waves/round-96/V18-scratch/oracle.py` recomputes `{event: sorted depends_on}` and relation
endpoints from the fixtures; `pincheck.py` diffs the contract pins against it and re-hashes every
pinned file:

```
r88-m3-maya-cluster: edges_match=True endpoints_match=True counts_match=True per_file_digests_match=True
r94-paired-crossing: edges_match=True endpoints_match=True counts_match=True per_file_digests_match=True
r95-crossing-aftermath: edges_match=True endpoints_match=True counts_match=True per_file_digests_match=True
r96-crossing-response: edges_match=True endpoints_match=True counts_match=True per_file_digests_match=True
ORACLE-CROSSCHECK PASS
```

Pins match reality independently; r96 counts 5 events / 4 dependency edges / 1 relation /
5 entities / 5 sources are confirmed from the files, not from prose. Q5's `README.md` and
`claim-excerpt-map.md` are now present in r96 and the pin still verifies clean (exit 0) —
the digest covers the five JSON tables only, as documented.

## 6. BR-01 two-sided evidence (the debt C3 claims to close)

Before (scratch copy of r94 with `evin-ninth-bell` dropped from the tick-10 `depends_on`), all
existing gates green — reproduced independently at 17:40, **before** the new gate existed:

```
check_bible      CLEAN: schema, citations, relations, timeline; 0 violations   exit=0
support_check    RESULT PASS                                                   exit=0
map_obligations  OBLIGATIONS raw=14 mapped=14 / RESULT PASS                     exit=0
```

After (same mutation, new gate): exit 1 `REDUCTION-DETECTED` (§2 B7). The reduction that was
invisible to every prior gate is now a hard failure.

## 7. Observations / defects (reported exactly)

1. **Stray `c3red` pin in the delivered contract — confirmed by my own evidence trail, and
   independently reported by Q3 (§7 of its report).** The delivered contract at
   `7d568cc4…` carries a fifth pin:

   ```
   pins: ['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response']
   c3red: fixture ".ufo/waves/round-96/seats/V41-scratch/c3red"
          content_sha256 eff4b354c092a9c4a3ea6de6857ee1a21be1ab4bafac957568b6813dac8dbd28
          counts {events 3, dependency_edges 1, relations 1}
   ```

   My own trail: (a) my first read of the contract at 17:43 (hash `2601c18a…`) showed exactly
   four pins; (b) at 17:46 the tool's `UNPINNED-FIXTURE` detail printed the five-name list;
   (c) `V41-scratch/c3-freeze.out` shows `FROZEN c3red: events 3; dependency-edges 1; relations 1`
   with digest `eff4b354…`; (d) verifying that scratch dir against the stray pin returns
   `FREEZE c3red: … RESULT PASS exit=0` with the scratch's `paired-crossing-decision` reduced to
   `['aru-ninth-bell']`. So a verifier's `--freeze` call rewrote the delivered artifact and left
   a scratch path inside it. Impact on verification semantics: none observed (pins are
   basename-keyed; no corpus fixture is named `c3red`); impact on delivered bytes: real —
   the admitted contract references a seat scratch dir that is not part of the delivery.
   Hazard: **any** invocation of `--freeze` (on any path, from any cwd) rewrites the delivered
   contract; there is no scope guard refusing out-of-corpus paths. Q3 deliberately did not add
   the guard mid-round to keep the hash frozen for the verifier battery; it recommends deleting
   `pins.c3red` at closure or adding a `--freeze` scope guard. I concur, and add that the
   `UNPINNED-FIXTURE` message leaks the scratch path to every user of the tool.
2. **The artifact moved during the round — verification is only valid for the frozen revision.**
   My first read (17:43) was tool `d17297bb…` / contract `2601c18a…`; by 17:44:27–37 they were
   `7d568cc4…` / `a3b57978…`. V41's `c3-interim.log` on the earlier revision shows
   `SELF-TEST 5/14` with nine cases failed (the late-binding lambda defect Q3 documents in its
   §5); the current revision is 14/14. The baseline I first ran (17:44:25) was against the old
   tool; every result quoted in this report was re-run on the frozen revision with the hashes
   re-checked before and after the battery. Any r96 receipt citing the old hashes should be
   re-pinned.
3. Transient system condition, not a gate defect: at 17:45:50 four of my `/tmp`-redirected
   commands failed with `No space left on device` (tmpfs `/tmp` 16 G, 6.7 G used at 17:46).
   The gate's own `--self-test` scratch is `tempfile.TemporaryDirectory()` (system temp) — it
   succeeded in every run I made, but a full `/tmp` would make `--self-test` fail. Worth knowing
   for the fleet (58 verifier seats share this host).

## 8. Write audit

```
$ git status --porcelain corpus/
 M corpus/tools/map_obligations.py                # Q1 (C1), not mine
?? corpus/fixtures/r96-crossing-response/         # Q4/Q5
?? corpus/knowledge/r96-response-scope-note.md    # Q6
?? corpus/tools/dependency-freeze-contract.json   # Q3
?? corpus/tools/dependency_freeze.py              # Q3
```

My writes: this report plus `.ufo/waves/round-96/V18-scratch/` only (absolute paths under the
lane repo; parent-tree scan `find … -newermt "17:30" -not -path "*/lore-shokunin/*"` shows no
V18 file — the r94-F01 cwd defect class did not recur here). No commits, no network, no nested
agents, no `--freeze` invocation by me (it would have mutated the delivered contract), and the
delivered tool/contract hashes were identical before and after my battery.

## Bottom line

PASS — on the frozen revision (`dependency_freeze.py a3b57978…`, contract `7d568cc4…`) every
declared C3 behavior verifies: baseline 4/4 clean, phantom addition → exit 1 `ADDITION-DETECTED`,
relation flip and true endpoint change → exit 1 `ENDPOINT-CHANGE`, event-row deletion with its
edges → exit 1 with two `REDUCTION-DETECTED` lines, BR-01 reduction → exit 1 (before: all prior
gates green), digest-only change → exit 2 `DIGEST-MISMATCH`, persisted self-test 14/14 with a
fail-closed `CONTRACT-INVALID` coupling, and pins independently match an outside oracle — with
one delivered-bytes defect flagged for closure: the stray `c3red` scratch pin (written into the
contract by a verifier's `--freeze` call; harmless to semantics, should be deleted at closure,
and `--freeze` deserves a scope guard).
