# V21 — c3-fail-closed (round 96)

- Seat: V21, verifier. Claim under test: **C3** — `corpus/tools/dependency_freeze.py` +
  `corpus/tools/dependency-freeze-contract.json`, fail-closed sweep.
- Verified revision (frozen; hashes quoted by Q3's report and identical at my measurement):
  tool `a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980`,
  contract `7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975`.
- Poll-wait: tool + contract appeared at poll try 15 (~17:41); Q3's producer report
  `Q3-dependency-freeze.md` landed at ~17:52 and all definitive results below were measured
  after it existed. No ABSENT condition. The tool was still being edited while I probed
  (hashes changed `f3a854fc…` → `d17297bb…` → `a3b57978…`); interim revisions showed exactly the
  two defects Q3's report §5 says the self-test caught in its own first runs (late-binding case
  lambdas; mutual-exclusion `ToolError` outside `main`'s handler → traceback exit 1) — the final
  revision fixes both, and nothing below is measured on an interim revision.

## Method

Pin lookup is keyed by fixture **basename** (tool `pin_for`), so scratch cases that must reach a
pinned evaluation are placed in dirs named exactly `r94-paired-crossing`; unpinned-name cases use
their own names. Positive controls first: without them, exit 2 on everything would pass vacuously.

## Positive controls (expect exit 0)

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
    python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; echo "[exit=$?]"; done
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279
RESULT PASS          [exit=0]
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS          [exit=0]
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS          [exit=0]
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
RESULT PASS          [exit=0]
```

## Fail-closed probes (all expect exit 2)

P1 — unpinned fixture dir (exists, has timeline.json, not in chain):

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r93-m2-kojiki-cluster
FINDING UNPINNED-FIXTURE: no pin for 'r93-m2-kojiki-cluster' in corpus/tools/dependency-freeze-contract.json (pinned: ['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response'])
RESULT ERROR          [exit=2]
```

P2 — malformed timeline JSON (scratch copy under the pinned basename, bytes `[{"id": "aru-ninth-bell", "tick": 9,`):

```
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/V21-scratch/cases/malformed-tl/r94-paired-crossing
FINDING MALFORMED-JSON: timeline.json: Expecting property name enclosed in double quotes: line 1 column 37 (char 36)
RESULT ERROR          [exit=2]
```

P3 — missing fixture dir, both name classes:

```
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/V21-scratch/cases/missing-dir/r94-paired-crossing
FINDING FIXTURE-MISSING: fixture directory not found: .ufo/waves/round-96/seats/V21-scratch/cases/missing-dir/r94-paired-crossing
RESULT ERROR          [exit=2]

$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/does-not-exist-r96
FINDING UNPINNED-FIXTURE: no pin for 'does-not-exist-r96' in corpus/tools/dependency-freeze-contract.json (pinned: ['c3red', ...])
RESULT ERROR          [exit=2]
```

P4 — usage errors (six forms, all exit 2 `INVALID-ARGUMENTS`, no traceback on any):

```
$ python3 corpus/tools/dependency_freeze.py
FINDING INVALID-ARGUMENTS: expected a fixture directory, --freeze DIR, or --self-test     [exit=2]
$ python3 corpus/tools/dependency_freeze.py --bogus corpus/fixtures/r94-paired-crossing
FINDING INVALID-ARGUMENTS: unrecognized arguments: --bogus                                 [exit=2]
$ python3 corpus/tools/dependency_freeze.py --freeze
FINDING INVALID-ARGUMENTS: argument --freeze: expected one argument                        [exit=2]
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing corpus/fixtures/r95-crossing-aftermath
FINDING INVALID-ARGUMENTS: unrecognized arguments: corpus/fixtures/r95-crossing-aftermath  [exit=2]
$ python3 corpus/tools/dependency_freeze.py --self-test corpus/fixtures/r94-paired-crossing
FINDING INVALID-ARGUMENTS: --self-test cannot be combined with a fixture or --freeze       [exit=2]
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing --freeze corpus/fixtures/r94-paired-crossing
FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both        [exit=2]
```

P5 — non-chain fixtures with no pins (not a silent pass):

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/consistent
FINDING UNPINNED-FIXTURE: no pin for 'consistent' in corpus/tools/dependency-freeze-contract.json (pinned: ['c3red', ...])      [exit=2]
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/item-chain-valid
FINDING UNPINNED-FIXTURE: no pin for 'item-chain-valid' in corpus/tools/dependency-freeze-contract.json (pinned: ['c3red', ...]) [exit=2]
```

Supplementary probes (also exit 2):

```
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/V21-scratch/cases/no-timeline/r94-paired-crossing
FINDING FILE-MISSING: timeline.json is missing from .ufo/…/cases/no-timeline/r94-paired-crossing   [exit=2]

$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/V21-scratch/cases/digest-tamper/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
FINDING DIGEST-MISMATCH: content digest af388b771ad67e270279f4a0d943dc707a87106c763eb23fcb203508fd988e3e != pin 2527beb9…; fixture bytes changed outside the frozen inventory
RESULT ERROR          [exit=2]

$ python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/does-not-exist-freeze
FINDING FIXTURE-MISSING: fixture directory not found: corpus/fixtures/does-not-exist-freeze     [exit=2]
```

## Self-test (persisted) and byte-stability

```
$ python3 corpus/tools/dependency_freeze.py --self-test
… 14 cases ok …
SELF-TEST 14/14
RESULT PASS          [exit=0]
```

Full battery on the frozen revision: 18 probes → `4 [exit=0]` (positive controls) and
`14 [exit=2]` (all fail-closed probes), zero unexpected exits. Contract sha256 before and after
the entire sweep: `7d568cc4…` unchanged — no probe mutated the delivered contract
(the `--freeze`-plus-fixture usage error returns before any write; the only `--freeze` call made
was on a nonexistent dir, which fails at `FIXTURE-MISSING`). Logs:
`.ufo/waves/round-96/seats/V21-scratch/probes-final.log`, `selftest-final.log`.

## Anomaly observed (not this seat's claim; reported for the record)

The delivered contract carries a fifth pin `c3red` whose `fixture` path is
`.ufo/waves/round-96/seats/V41-scratch/c3red` (a verifier scratch dir). Independently observed:

```
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/V41-scratch/c3red
FREEZE c3red: events 3/3; dependency-edges 1/1; relations 1/1
DIGEST eff4b354c092a9c4a3ea6de6857ee1a21be1ab4bafac957568b6813dac8dbd28
RESULT PASS          [exit=0]
```

Q3's report §7 documents this (V41 exercised `--freeze` on its own scratch copy; the tool's
`--freeze` writes `CONTRACT_PATH` unconditionally) and left it in place because V22/V33 receipts
quote the pinned list. It does not weaken the fail-closed sweep (no corpus fixture is named
`c3red`; the four chain pins and all unpinned-name refusals above are unaffected), but the
`--freeze` out-of-corpus write hazard is real and belongs to C3's adjudication.

## Write audit

Written by this seat only: this report and
`.ufo/waves/round-96/seats/V21-scratch/` (`run-probes.sh`, `probes-*.log`, `selftest-final.log`,
`cases/`, `r94-copy/`, `r95-copy/`, `r94-copy-malformed/`). No commits, no network, no nested
agents; no corpus file touched (contract sha unchanged before/after, quoted above).

## Bottom line

PASS — on the frozen revision (tool `a3b57978…`, contract `7d568cc4…`) every fail-closed probe
exits 2 with a stable finding (unpinned dir, malformed timeline, missing dir both name classes,
six usage errors, non-chain no-pins, missing timeline, digest tamper, freeze on missing dir),
positive controls are 4/4 chain fixtures exit 0, `--self-test` is 14/14 exit 0, and the delivered
contract is byte-stable across the sweep; one anomaly reported for adjudication: a foreign
`c3red` scratch pin written into the contract by V41's `--freeze` probe.
