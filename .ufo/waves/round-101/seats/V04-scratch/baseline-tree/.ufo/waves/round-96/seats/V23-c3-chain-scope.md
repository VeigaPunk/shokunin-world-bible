# V23 — c3-chain-scope (round 96)

- Seat: V23, verifier. Scope: after Q3, verify (a) the frozen chain is exactly the
  four declared fixtures (no more, no fewer), (b) the r88 ROOT cluster edges (two
  tick-9 events, no dependencies) froze correctly, (c) scope wording in the tool
  README/README docs matches (reads-only gate, no canon semantics).
- Verified revision (hashed after Q3's report landed; Q3's report §0 quotes the
  same two hashes):

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
$ ls -la --time-style=full-iso corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
-rw-r--r-- 1 vgpnk vgpnk 12032 2026-10-17 17:44:27.305998265 -0300 corpus/tools/dependency-freeze-contract.json
-rw-r--r-- 1 vgpnk vgpnk 20552 2026-10-17 17:44:37.812881330 -0300 corpus/tools/dependency_freeze.py
```

- Poll-wait: Q3's two artifacts appeared at 17:42; `Q3-dependency-freeze.md` at
  ~17:46 (poll cycle 25, 20 s cadence). No verification of a plan; everything
  below was measured on bytes on disk. My own writes stayed inside
  `.ufo/waves/round-96/seats/V23-scratch/` and this report.

---

## Check (a) — frozen chain is exactly the four declared fixtures: **FAIL**

As delivered, the contract carries **five** pins, not four:

```
$ python3 -c "import json;c=json.load(open('corpus/tools/dependency-freeze-contract.json'));print(sorted(c['pins']))"
['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response']
```

- extra: `['c3red']` — missing: `[]`. So "no fewer" holds (all four declared
  fixtures are pinned and each verifies); "no more" is violated by one foreign pin.
- The contract has no other declared fixture list — `pins` *is* the frozen set
  (`top keys: ['schema_version','tool','scope','precedence','data_files',
  'required_files','exit_codes','revision','pins','self_test']`), so the extra
  key is the whole of the deviation.
- `c3red` is not a corpus fixture and was not authored by Q3:

```
$ python3 -c "import json;c=json.load(open('corpus/tools/dependency-freeze-contract.json'));print(c['pins']['c3red']['fixture']);print(c['pins']['c3red']['counts'])"
.ufo/waves/round-96/seats/V41-scratch/c3red
{'events': 3, 'dependency_edges': 1, 'relations': 1, 'entities': 5, 'sources': 3}
```

- Provenance (read-only): `.ufo/waves/round-96/seats/V41-scratch/c3-freeze.out`
  reads `FROZEN c3red: events 3; dependency-edges 1; relations 1` / `RESULT PASS`
  — V41 exercised the `--freeze` path on its own mutated copy at 17:44. Contract
  mtime `17:44:27` matches that probe.
- Q3 reports the anomaly itself (§7) and deliberately left the pin because two
  verifier receipts (V22, V33) already quote the five-key list; that reasoning is
  sound for mid-round stability, but the delivered artifact still does not match
  the declared C3 shape ("expect 4/4 clean", "the frozen chain is exactly the
  four declared fixtures").

**Mechanism (reproduced in isolation, no writes to the delivered file).** `freeze()`
writes the contract path resolved from the tool's own location
(`ROOT = Path(__file__).resolve().parents[2]`, `CONTRACT_PATH = ROOT/"corpus/tools/dependency-freeze-contract.json"`),
line 312: `CONTRACT_PATH.write_text(json.dumps(contract, indent=2, ensure_ascii=False) + "\n", ...)`.
There is no path guard, so `--freeze <any dir>` from any cwd rewrites the delivered
contract. On a throwaway copy of the tree under my scratch dir:

```
$ python3 .ufo/.../V23-scratch/isolated/corpus/tools/dependency_freeze.py --freeze .ufo/.../V23-scratch/isolated/corpus/fixtures/r95-scratch-probe
FROZEN r95-scratch-probe: events 4; dependency-edges 3; relations 1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
...
RESULT PASS   EXIT=0
isolated copy pins before: ['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response']
isolated copy pins after:  ['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r95-scratch-probe', 'r96-crossing-response']
```

The `--freeze` write is the only write the tool performs outside its self-test
temp dir; verify mode is reads-only. Q3's recommendation (closure-time deletion
of `pins.c3red`, or a scope guard refusing paths outside `corpus/fixtures/`) is
the right shape; my measurement confirms both the hazard and its reproduction.

**Supporting "no sweep / fail-closed" measurements (all on the delivered revision):**

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r87-myth-cluster   # 5th, unpinned
FINDING UNPINNED-FIXTURE: no pin for 'r87-myth-cluster' in corpus/tools/dependency-freeze-contract.json (pinned: ['c3red', ...])
RESULT ERROR   EXIT=2
$ python3 corpus/tools/dependency_freeze.py .ufo/.../nonexistent/r96-crossing-response
FINDING FIXTURE-MISSING: fixture directory not found: ...   RESULT ERROR   EXIT=2
$ python3 corpus/tools/dependency_freeze.py
FINDING INVALID-ARGUMENTS: expected a fixture directory, --freeze DIR, or --self-test   RESULT ERROR   EXIT=2
```

Pin lookup is by fixture **basename** (`pin_for` → `fixture.resolve().name`), so
a tampered copy of a pinned fixture anywhere on disk is compared against that
fixture's pin — intended for the self-test, and the reason the extra pin is
harmless to verification semantics (no corpus fixture is named `c3red`). It is
also why a deleted pinned fixture cannot be silently skipped: a real copy at a
foreign path verifies against the pin (r88 copy at
`.ufo/.../V23-scratch/r88-m3-maya-cluster` → `RESULT PASS` exit 0), and an absent
directory exits 2.

## Check (b) — r88 ROOT cluster edges froze correctly: **PASS**

The r88 pin holds exactly the two tick-9 events with no dependencies, no
relations, and no dependency edges:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279
RESULT PASS   EXIT=0
```

Pin contents, compared against my own independent recomputation of
`timeline.json`/`relations.json` (`ref_inventory.py` in my scratch dir):

- `aru-ninth-bell`: `depends_on: []`, endpoint `{tick: 9, entity_id: aru, place_id: quiet-rise}`
- `evin-ninth-bell`: `depends_on: []`, endpoint `{tick: 9, entity_id: evin, place_id: salt-court}`
- `relations: []`; `counts: {events: 2, dependency_edges: 0, relations: 0, entities: 4, sources: 2}`

All four declared pins matched my independent recomputation on edges, relation
triples, per-file SHA-256 digests, and entity/source counts:

```
r88-m3-maya-cluster: edges_ok=True rel_ok=True digests_ok=True counts(events/edges/rels/ent/src)=2/0/0/4/2 recomputed(ent/src)=4/2 => OK
r94-paired-crossing: edges_ok=True rel_ok=True digests_ok=True counts(...)=3/2/1/5/3 recomputed(ent/src)=5/3 => OK
r95-crossing-aftermath: edges_ok=True rel_ok=True digests_ok=True counts(...)=4/3/1/5/4 recomputed(ent/src)=5/4 => OK
r96-crossing-response: edges_ok=True rel_ok=True digests_ok=True counts(...)=5/4/1/5/5 recomputed(ent/src)=5/5 => OK
ALL PINS MATCH INDEPENDENT RECOMPUTATION: True
```

Chain continuation verified at the dependency layer: r96 adds exactly one event
(`response-evin-salt-court`, tick 12, `depends_on: ["aftermath-missing-evin"]`);
the other four events and the single relation triple are unchanged from r95;
r88→r94→r95 inheritance is identical throughout. Independent mutation probes on
scratch copies of r95 (delivered revision) give the declared classes:

```
reduction (drop evin-ninth-bell)  -> FREEZE ... dependency-edges 2/3; FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']; EXIT=1
addition  (phantom-ninth-bell)    -> dependency-edges 4/3; FINDING ADDITION-DETECTED: event aftermath-missing-evin gained depends_on ['phantom-ninth-bell']; EXIT=1
endpoint  (chalk-stair->salt-court)-> FINDING ENDPOINT-CHANGE: event paired-crossing-decision.place_id: 'chalk-stair' -> 'salt-court'; EXIT=1
```

Persisted self-test, delivered revision: `SELF-TEST 14/14` / `RESULT PASS`,
`EXIT=0`. Fail-closed check on the persisted expectation set, run on an isolated
tree copy with `digest_tamper` deleted from `self_test.expected`:

```
FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=['digest_tamper'] extra=[]
RESULT ERROR   EXIT=2
```

## Check (c) — scope wording matches (reads-only gate, no canon semantics): **PARTIAL**

Present and matching, verified by reading the delivered bytes:

- Contract `scope` field: `"frozen per-fixture dependency-edge inventory (event id ->
  sorted depends_on set), event endpoints (tick, entity_id, place_id), relation
  endpoint triples (from, to, type), and JSON content digests for the crossing
  continuation chain; no chronology truth, entailment, source, rights, or canon
  judgment"` — reads-only inventory, explicit no-canon clause.
- Contract `precedence`: semantic inventory findings decide first (exit 1); a
  content digest change the inventory does not model exits 2 — matches observed
  behaviour exactly (reduction/addition/endpoint → 1; digest-only tamper → 2).
- Tool module docstring: pins/compares inventories, "the semantic inventory
  decides first, and a content change the inventory does not model is reported as
  could-not-evaluate"; `grep -n -i "canon"` finds no canon claim in the tool.

**The README/registry side is absent — the new gate is documented nowhere
outside its own two files.** Checked at 17:51–17:53, after Q2's README write
(`corpus/tools/README.md` mtime `17:51:04`):

```
$ grep -c -i "freeze" corpus/tools/README.md
0
$ grep -n "^#" corpus/tools/README.md | tail -3
121:### Round-96 addendum: gating inventory mismatch, `dual_pointer`, 24-case self-test (2026-10-17)
...
$ grep -n -i "dependency_freeze\|dependency-freeze" SKILL.md
(none; SKILL.md:44 carries the "## Gate registry" section)
```

Q2's r96 addendum documents the C1 bundle only (`map_obligations` gating
inventory mismatch, `dual_pointer`, 24-case self-test) and never mentions the
freeze gate. The repository convention, stated in the README itself
(`README.md:51`) and followed for `boundary_doc_check`, `discriminate_check`,
`support_check` and `map_obligations`, is a **Gate registry** entry in `SKILL.md`
carrying name, entry command, verdict map, pin location, scope and self-test —
`dependency_freeze` has no such entry, and no `Q2-*.md` report existed after
38 poll cycles (~15 min; poll stopped by me at 17:53). So the
tool-README/registry half of this check cannot be performed: there is no
delivered prose describing the gate as reads-only outside the contract and the
docstring. `corpus/fixtures/r96-crossing-response/README.md` (Q5, delivered)
bounds `support_check.py` as "lexical preflight only, not ... canon review" but
says nothing about the freeze gate — it neither satisfies nor contradicts this
check. Neither the README nor SKILL.md misdescribes the gate; the defect is
absence, not contradiction, and `SKILL.md` was byte-owned by no seat this round.

## Transient observation worth recording (pre-final revision)

My first `--self-test` run (17:43–17:44, before Q3's 17:44:37 edit) returned
`SELF-TEST 4/14` — ten cases all reporting the `missing_timeline` scratch path
(Python late binding in the case lambdas: every `lambda: [scratch]` closed over
the same variable) plus a raw traceback and exit 1 on `invalid_arguments` (guard
raised outside `main`'s handler). V41's `V41-scratch/c3-selftest.out` at 17:44
independently records `SELF-TEST 5/14` for an intermediate revision. Q3 §5
documents both defects as caught by its own first runs and fixed before the final
run. I re-ran against the delivered revision and got `SELF-TEST 14/14` exit 0, so
**the delivered artifact is green**; but any seat whose receipt was taken between
~17:42 and ~17:44:37 measured a red self-test and a differently-behaving CLI
(exit 1 + traceback instead of exit 2 `INVALID-ARGUMENTS`). Those receipts are
revision-stale, not wrong, and should not be read as failures of the final bytes.

## Cross-seat corroboration (read-only, after filing my own measurements)

Independent C3 verifier seats filed while I worked, all converging on the same
delivered revision and the same anomaly:

- `V16-c3-gate-clean.md:225-246` — independently confirms the `c3red` pin and
  that it freezes a **reduced mutant** inventory (3 events, 1 dependency edge),
  and recommends removing `pins.c3red` before the round is sealed; it also hit
  the pre-fix late-binding self-test failure on intermediate revision `d17297bb…`.
- `V19-c3-selftest.md:80-84` — re-checked all five pins including `c3red`
  (`file-digest mismatches=none; count mismatches=none`).
- `V21-c3-fail-closed.md` — positive controls 4/4 chain fixtures exit 0,
  `--self-test` 14/14, contract byte-stable across its sweep, one anomaly: the
  foreign `c3red` pin.
- `V48-c3-negative-2.md`, `V57-crosscheck-coverage.md` — same anomaly, same
  conclusion: harmless to the admitted path, real `--freeze` hazard for closure.

V33's battery log (`.ufo/waves/round-96/seats/V33-scratch/v33-battery-current.txt:113,119`)
and V22's snapshot (`V22-c3-tamper.scratch/snapshots/rev-1743/dependency-freeze-contract.json:257`)
quote the five-key pinned list, which is the concrete reason Q3 gives for not
removing the pin mid-round — I verified both citations exist as described.

## Write audit

Wrote only this report and `.ufo/waves/round-96/seats/V23-scratch/` (reference
inventory, isolated tree copies, hash snapshots). No commits, no network, no
nested agents, no corpus writes. The delivered `corpus/tools/dependency-freeze-contract.json`
was **not** touched by this seat — the `--freeze` reproduction ran against a copy
of the tree under my scratch dir.

## Bottom line

**FAIL** — (b) the r88 ROOT cluster froze correctly and (c) the contract/docstring
scope wording matches reads-only/no-canon with the tool README still absent, but
(a) is violated: the frozen chain is **not** exactly the four declared fixtures —
the delivered contract carries a fifth foreign pin `c3red` (V41 scratch copy,
written by `--freeze` at 17:44:27), a hazard I reproduced in isolation; the gate
itself verifies 4/4 clean, self-tests 14/14, and fails closed, so the deviation is
scope shape, not detection semantics.
