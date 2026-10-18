# V54 six-chain-integrity — round 98

Seat V54 (verifier, leaf). Mandate: independently recompute all six chain
fixtures' edge sets + digests from raw JSON and compare one-to-one against the
contract pins. Writes: this report + `.ufo/waves/round-98/seats/V54-scratch/`
only (absolute paths under the lane root). No commits, no network, no nested
agents.

Baseline: r97 closure `9a3d648` (pre-round bytes via `git show`); HEAD during
the wave `dd4df1b` (adds only `SCORECARD.md` vs 9a3d648 — `git diff --stat
9a3d648 dd4df1b -- corpus/` empty). Wave tree uncommitted. Poll-wait per
protocol (20 s cadence): **ARTIFACTS-PRESENT try 8, 23:32:51 UTC** (six pins +
r97/r98 fixture data files).

## 1. Method — independent recompute

Own implementation `V54-scratch/recompute.py`, **no import of the tool**:

- reads raw bytes of the five data files per fixture
  (`entities/relations/timeline/sources/contradictions.json`);
- per-file sha256 (hashlib);
- content digest = sha256 of the compact sorted-JSON `{name: per-file sha256}`
  map (the operational definition the pins carry);
- event inventory `id -> {depends_on: sorted set, endpoint: {tick, entity_id,
  place_id}}`; sorted relation triples `[from, to, type]`; counts.

Formula validation before the new pins existed: the same script reproduced all
four baseline pins byte-exact, and per-file digests were cross-checked with the
`sha256sum` CLI (see §4). Corroboration: the tool's own verify on all six
fixtures plus a mirror harness (tool + contract + fixtures copied into
scratch) for mutation probes.

## 2. Result — one-to-one vs the contract pins

```
$ python3 .ufo/waves/round-98/seats/V54-scratch/recompute.py . \
    --baseline .ufo/waves/round-98/seats/V54-scratch/baseline-contract-9a3d648.json \
    --json .ufo/waves/round-98/seats/V54-scratch/recompute-report.json
...
VERDICT PASS        (exit 0)
```

All six fixtures PASS on all six aspects — `fixture_path`, `files`,
`content_sha256`, `events`, `relations`, `counts` (final rerun on the last
contract bytes, `recompute-report-final.json`):

| fixture | pin content digest (== recomputed) | aspects | tool verify |
|---|---|---|---|
| r88-m3-maya-cluster | `15ef230ef806ea7e…fc3fc279` | 6/6 PASS | PASS exit 0 |
| r94-paired-crossing | `2527beb938b474a2…7ecebe75` | 6/6 PASS | PASS exit 0 |
| r95-crossing-aftermath | `d541ae641f3189e1…e66d2ec9` | 6/6 PASS | PASS exit 0 |
| r96-crossing-response | `d422a9b3d95c4e0b…657d7f6` | 6/6 PASS | PASS exit 0 |
| r97-crossing-acknowledgment | `3c922d20a01bbd3f…f83abea6` | 6/6 PASS | PASS exit 0 |
| r98-clerk-filing | `59a0f4fa3d4a47e0…d9b9b133` | 6/6 PASS | PASS exit 0 |

Pin set: **exactly six, no extras** (`pin count: 6`). Revisions:
r88/r94/r95 = `60dba0c2aa344860b10a2fc63e00468d1b134f27`; r96 =
`2393934237ea076366f3db6dceeff033edb52ab1`; r97/r98 =
`dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb` (= HEAD at freeze). The four
inherited pins are JSON-equal to the `9a3d648` baseline
(`BASELINE-EQUAL …: True` ×4); r97/r98 are new pins (absent from baseline).
Structured diff vs baseline: `pins added: ['r97-crossing-acknowledgment',
'r98-clerk-filing']`, `pins removed: []`, `scope changed: False`,
`exit_codes changed: False`, inherited 16 self-test cases `changed: none`.

## 3. Chain extension evidence

Observed (== pinned) counts per fixture, ticks 9→14:

```
r88: events=2 edges=0   r94: 3/2   r95: 4/3   r96: 5/4   r97: 6/5   r98: 7/6
```

New edges frozen by the two new pins:

- r97 pin: `acknowledgment-aru-records` tick 13 <- `['response-evin-salt-court']`
  (the tick-13 edge whose absence V46 recorded as an r97 FAIL);
- r98 pin: `clerk-filing-open` tick 14 <- `['acknowledgment-aru-records']`.

## 4. Cross-checks

- **CLI sha256sum**: all 20 baseline pinned files OK; all 10 new-pin files OK
  (`CLI-CROSSCHECK PASS`, `CLI-CROSSCHECK-NEW PASS`).
- **Tool 6/6**: `python3 corpus/tools/dependency_freeze.py corpus/fixtures/<fx>`
  × 6 → `RESULT PASS` exit 0 each; each `DIGEST` line equals the pin content
  digest (quoted in §2).
- **Pre-pin snapshot**: `V54-scratch/presnapshot-r97-r98.json` (taken before
  the pins landed, ~23:32 UTC) r97 `3c922d20…` / r98 `59a0f4fa…` == final pin
  digests — no byte drift across the freeze.
- **Self-test (aux)**: `python3 corpus/tools/dependency_freeze.py --self-test`
  → `CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH']
  ok`, `SELF-TEST 17/17`, `RESULT PASS` exit 0.
- **Mutation probes (mirror harness, `V54-scratch/mirror/`)** — the new pins
  are load-bearing:
  - drop the r97 tick-13 edge in the mirror → timeline sha
    `37a425b97af658d71b8dc8904f43fd75859905bac326489a71adb67004004eb1`,
    `FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost
    depends_on ['response-evin-salt-court']`, exit 1. This sha **exactly
    reproduces the mutation bytes the contract provenance note cites for V46's
    r97 scratch mirror** — an independent reproduction of C2's demonstration.
  - drop the r98 tick-14 edge in the mirror → timeline sha
    `ddec7a072fa21919ca1faeae49f7ee7b7f1eae20bcd36653942eee58cceec34f`,
    `FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on
    ['acknowledgment-aru-records']`, exit 1.

## 5. Stability and the post-verification contract edit

First verification round ran against contract sha `c435239d…`; S1 then edited
the contract (provenance note for the r97/r98 pinning; mtime 20:33 local /
23:33 UTC, sha `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`).
All six pin payloads in the edited contract are **identical to the
verification-time snapshot** (`pins identical to verification-time snapshot:
True` ×6), the tool sha is unchanged (`03d04365…`), and the full recompute +
tool verify were re-run on the final bytes: PASS (§2). Contract sha stable at
`153ebc5b…` at last check (23:35 UTC).

## 6. Producer reports / stall record

All five producer reports present: S1 `S1-freeze-hygiene.md` landed 23:35:29 UTC
(poll `V54-scratch/V54-poll-s1.log`, try 6), S2 `S2-tools-docs.md`, S3, S4, S5
present; the S5 note `corpus/knowledge/r98-clerk-scope-note.md` present. The
bounded S1 wait is closed — no stall-escape was needed. Cross-check against S1's
report: its quoted tool sha `03d04365…` and contract sha `153ebc5b…` equal my
measurements; its freeze digests (r97 `3c922d20…`, r98 `59a0f4fa…`) and chain
6/6 receipts equal my independent recompute; its V46-discharge mutation timeline
sha `37a425b9…` equals my independent mirror reproduction byte-for-byte.
ENDGAME convention honored: SELF (V54) was never in any wait set.

## 7. Failures / caveats

- No contradiction found against the six-chain claim. Nothing failed.
- Cosmetic artifact of my own script only: `BASELINE-EQUAL r97/r98: False` is
  printed because those two are new pins (absent in the baseline; `None == pin`
  evaluates False), not a pin defect — the intended NEW-PIN label was shadowed
  in my script's output. The pin payloads themselves are correct.
- The pins bind the five JSON tables only; `claim-excerpt-map.md` /
  `README.md` / `fictional-excerpts.md` are not pinned — consistent with the
  declared pin payload. The r95 map repair (S3) leaves pinned data untouched
  (r95 pin still verifies PASS at `d541ae64…`).
- Not in scope, noted only: S3's report flags an untracked `baseline-analyze.txt`
  stray in the parent repo (outside this lane; not written by this seat).

## Bottom line

**PASS** — six pins independently recomputed from raw JSON: 6/6 fixtures ×
6 aspects one-to-one match; tool verify 6/6 clean with DIGEST == pin; CLI
digest cross-checks PASS; inherited pins unchanged; r97 tick-13 and r98 tick-14
edges frozen and load-bearing (independent REDUCTION-DETECTED reproductions,
the r97 mutation bytes matching V46's cited sha); no contradictions found; all
five producer reports present (S1 landed 23:35:29, cross-checked; artifacts
verified on the final bytes).
