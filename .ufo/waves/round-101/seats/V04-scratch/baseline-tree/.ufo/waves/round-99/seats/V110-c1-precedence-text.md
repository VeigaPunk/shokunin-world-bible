# V110 c1-contract-precedence-text — round 99

Seat: V110. Lane `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5` (wave tree uncommitted; HEAD during the check `337f0fa52b02626b7687eedbb2d99fab30446fe4`). Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report and `.ufo/waves/round-99/seats/V110-scratch/` only. Lane corpus bytes were not modified.

Axis judged: calibration — whether `corpus/tools/dependency-freeze-contract.json` field `precedence` states an order that the delivered tool actually emits on a scratch copy carrying two fault classes at once.

## Poll

Artifacts were present before this verdict: `dependency_freeze.py` and `dependency-freeze-contract.json` (schema 2, payload 2, six pins, ten files each, 18 self-test cases). Poll tries 0–17 from 22:03; try 17 aborted because the tool hash changed at 22:38:11. Two stability checks at 22:47:19 and 22:47:39 saw the judged hashes unchanged. `S1-full-file-pins.md` was absent during the probes and present immediately after this report was first written (22:52). Re-hash at that moment matched the judged digests, so the probes were not stale. S1's report states the same semantic-first rule ("Verification still lets semantic findings decide first (exit 1)") and does not claim a different exit-2 run order. S2 and S5 reports were still absent. This is not a plan: the precedence string and the tool that implements it were on disk and hash-stable across the probes below. Poll log: `.ufo/waves/round-99/seats/V110-scratch/poll.log`.

Bytes judged (stable across the rerun and the 22:47 checks):

- `corpus/tools/dependency_freeze.py` sha256 `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c` (29110 bytes, mtime 2026-10-17 22:38:11 -0300)
- `corpus/tools/dependency-freeze-contract.json` sha256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628` (25987 bytes, mtime 2026-10-17 22:08:46 -0300)

An earlier probe set on tool sha256 `6f81f8be…` (22:07 bytes) produced the same finding IDs. It is not the judged revision. The 22:38 rewrite changed the digest detail suffix from `fixture bytes changed outside the frozen inventory` to `pinned-file bytes changed outside the semantic inventory` and did not change check order. All quotes below are from the `fb9bb9ff…` bytes.

Live control, lane root, judged tool, unmodified fixture:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
EXIT:0
```

## Claimed order

Contract field `precedence`, quoted in full:

> semantic inventory findings decide first (exit 1: REDUCTION-DETECTED, ADDITION-DETECTED, ENDPOINT-CHANGE); a content digest change the semantic inventory does not model exits 2 (DIGEST-MISMATCH) and names each changed pinned file, including the five Markdown files. Exit-2 (could-not-evaluate) checks run in this order and the first failing check decides: UNPINNED-FIXTURE (no pin for the fixture name) or CONTRACT-INVALID (unreadable contract, invalid pin, payload_schema_version other than 2, or a pin that does not digest all ten pinned files), FIXTURE-MISSING (fixture directory absent), PATH-MISMATCH (invoked path differs from the pin's recorded path), FILE-MISSING / MALFORMED-JSON / MALFORMED-MODEL (model build of the JSON tables), DIGEST-MISMATCH (inventory clean, any pinned-file bytes changed or missing), INVALID-ARGUMENTS (CLI usage), SELF-TEST-MISMATCH (--self-test observed outcome differs from the persisted case expectation); --freeze additionally raises SCOPE-REFUSED (target outside corpus/fixtures/**, or a same-named in-scope target that would rewrite an existing pin's recorded path) and FILE-MISSING when a declared pinned file is absent. A path-less legacy pin is migrated in place by --freeze instead of refused. Re-freeze is the payload upgrade path from a schema-1 JSON-only pin to payload_schema_version 2.

The only sentence that says "in this order" is the exit-2 list, and it says the first failing check decides (one finding, not a multi-line sort). The exit-1 parenthetical is an enumeration of the class that decides before digest. It is not labeled as an emission sequence. `FILE-MISSING / MALFORMED-JSON / MALFORMED-MODEL` is one slash-grouped stage, not an order among those three.

Code that implements that (judged file):

- `emit` sorts findings before printing (`dependency_freeze.py:103-105`).
- `verify` looks up the pin, then checks the directory, then the path, then builds the model, then emits exit 1 if `compare` found semantic findings, and only then checks the digest (`dependency_freeze.py:370-394`).
- `main` raises `INVALID-ARGUMENTS` before `verify` or `--self-test` (`dependency_freeze.py:641-651`).

## Method

Each case is a mirror root under `.ufo/waves/round-99/seats/V110-scratch/rerun/<case>/` holding copies of the judged tool and contract plus `corpus/fixtures/r95-crossing-aftermath`. The tool's `ROOT` is `Path(__file__).resolve().parents[2]`, so the mirror is the repo root for that run. Lane fixtures were not mutated. Invocation shape:

```
python3 <mirror>/corpus/tools/dependency_freeze.py <args>
```

cwd = the mirror root.

Required copy: drop `evin-ninth-bell` from `paired-crossing-decision.depends_on` and append a prose line to `README.md` (semantic reduction + pinned-file digest change).

## Required pair — matches

Mutation: `depends_on` `['aru-ninth-bell', 'evin-ninth-bell']` → `['aru-ninth-bell']`; `README.md` appended with `\n<!-- v110 prose tamper -->\n`.

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 2/3; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
exit 1
```

Documented: semantic findings decide first; a digest change the inventory does not model is exit 2 and is not reached. Observed: one FINDING, `REDUCTION-DETECTED`, exit 1. `DIGEST-MISMATCH` is absent. Match.

Same suppression when the second class is a missing pinned Markdown file (reduction + `README.md` unlinked), observed on the pre-rewrite bytes and unchanged in `verify`: exit 1, only `REDUCTION-DETECTED`. Not re-quoted on `fb9bb9ff…`; the short-circuit is the same lines 384-387.

## Other fixture pairs — match the stated order

Clean mirror of the same fixture, no mutation: exit 0, `RESULT PASS`, digest `97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710` (same as the live control).

| Pair | Observed FINDING | Exit | vs documented |
|---|---|---|---|
| malformed `timeline.json` (`[{\n`) + README append | `MALFORMED-JSON` only | 2 | model-build before `DIGEST-MISMATCH` |
| foreign path + README append | `PATH-MISMATCH` only | 2 | path bind before digest |
| `timeline.json` deleted + README append | `FILE-MISSING` only | 2 | model-build before digest |
| missing directory whose basename is the pinned name, at a non-pin path | `FIXTURE-MISSING` only | 2 | directory check before `PATH-MISMATCH` |
| unpinned name `not-a-pinned-fixture` + README append | `UNPINNED-FIXTURE` only | 2 | pin lookup before digest |
| pin `payload_schema_version` set to 1 + edge drop | `CONTRACT-INVALID` (`1 != 2`) only | 2 | invalid pin before semantic compare |
| pin `files` missing the `README.md` digest + edge drop | `CONTRACT-INVALID` (needs sha256 for all 10 files) only | 2 | same, on the pre-rewrite bytes; `validate_pin` text is unchanged |
| README deleted, inventory otherwise clean | `DIGEST-MISMATCH` naming `README.md (sha256 9d27af4a… -> None)` | 2 | digest names a missing pinned file, including Markdown |
| `--freeze` on the in-scope mirror fixture with `README.md` deleted | `FILE-MISSING: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pinned file(s) missing: README.md` | 2 | freeze clause |
| `--freeze` on an out-of-scope directory | `SCOPE-REFUSED` only | 2 | freeze clause; scope is checked before model build |

`--self-test` combined with the tampered fixture path, same mirror tool:

```
FINDING INVALID-ARGUMENTS: --self-test cannot be combined with a fixture or --freeze
RESULT ERROR
exit 2
```

That is consistent with `INVALID-ARGUMENTS` being checked before `SELF-TEST-MISMATCH`. It does not reach the self-test.

## Mismatch — written exit-2 sequence vs observed

The text lists `DIGEST-MISMATCH` before `INVALID-ARGUMENTS` and says those checks run in that order and the first failing check decides. A copy that is both digest-tampered and illegally invoked should therefore report `DIGEST-MISMATCH` if that sentence is a run order.

Mutation: append one newline to `README.md` (digest fault only; inventory unchanged). Invocation passes both a fixture and `--freeze`:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath --freeze corpus/fixtures/r95-crossing-aftermath
FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both
RESULT ERROR
exit 2
```

`DIGEST-MISMATCH` is not emitted. `main` raises `INVALID-ARGUMENTS` at `dependency_freeze.py:643-644` before `verify` runs, so the later-listed check decides. That does not match the claimed order.

## Not counted as an order failure

Two (and three) exit-1 findings on one copy are all emitted, digest still suppressed. Line order is `sorted()` on `(finding_id, detail)`, not the parenthetical sequence.

Edge drop plus `place_id` `chalk-stair` → `salt-court`:

```
FINDING ENDPOINT-CHANGE: event paired-crossing-decision.place_id: 'chalk-stair' -> 'salt-court'
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
exit 1
```

Edge drop plus a gained `phantom-ninth-bell` plus the same endpoint change plus a README append:

```
FINDING ADDITION-DETECTED: event paired-crossing-decision gained depends_on ['phantom-ninth-bell']
FINDING ENDPOINT-CHANGE: event paired-crossing-decision.place_id: 'chalk-stair' -> 'salt-court'
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
exit 1
```

Observed line order is `ADDITION-DETECTED`, `ENDPOINT-CHANGE`, `REDUCTION-DETECTED`. The parenthetical lists `REDUCTION-DETECTED`, `ADDITION-DETECTED`, `ENDPOINT-CHANGE`. The text does not say that list is an emission order; it says those findings decide first as a class. Digest stayed suppressed, which is what that sentence claims. Recorded so the line-order difference is not hidden.

`FILE-MISSING` and `MALFORMED-JSON` are slash-grouped. A copy with malformed `relations.json` (`{`) and `timeline.json` deleted emits only `MALFORMED-JSON` (relations is parsed before the required-file check). No sub-order was claimed.

`README.md` and `SKILL.md` were not the text judged. Their mtimes (21:32 and 21:34) predate the contract rewrite; S2's report was absent. The contract field is the precedence text.

## Verdict

The required two-class copy matches: semantic reduction wins, digest is not emitted. The exit-2 fixture pairs that the text orders also match, including Markdown named in `DIGEST-MISMATCH` and schema-2 `CONTRACT-INVALID` before a semantic fault. The claimed run order does not match when a digest fault and an illegal invocation are simultaneous: the text puts `DIGEST-MISMATCH` first, the tool emits `INVALID-ARGUMENTS`.

Bottom line: FAIL — claimed exit-2 order lists DIGEST-MISMATCH before INVALID-ARGUMENTS and says the first failing check decides, but a README-tampered copy invoked as `fixture --freeze fixture` emits only INVALID-ARGUMENTS (exit 2).
