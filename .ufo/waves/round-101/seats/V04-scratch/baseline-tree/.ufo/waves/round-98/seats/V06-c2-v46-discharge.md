# V06 — c2-v46-discharge (round 98)

- Seat: V06 c2-v46-discharge (verifier). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; session cwd is the PARENT, so every path below is absolute or lane-root-relative with `cd` first. Baseline r97 closure `9a3d648` (wave tree uncommitted during the round). All commands run from the lane repo root with `python3`.
- Bar as briefed: poll for S1; on a scratch copy of r97 drop the tick-13 `depends_on` edge → `REDUCTION-DETECTED` exit 1 (the exact mutation V46 showed unfrozen at r97); on the delivered r97 → clean.
- Writes: this report plus `.ufo/waves/round-98/seats/V06-scratch/` only (mutator, poll scripts, baseline mirror, delivered mirrors, foreign-path control). No commits, no pushes, no network, no nested agents, no corpus writes. The seats-dir realpath was checked before writing: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats`.

## Revision pinned for every measurement (re-checked after all runs, unchanged)

```
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py          (S1)
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json (S1, 6 pins)
73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b  corpus/fixtures/r97-crossing-acknowledgment/timeline.json
```

The r97 fixture is byte-identical to baseline `9a3d648` in all ten files (`git show 9a3d648:<file> | sha256sum` vs on-disk, every file `SAME`; timeline `73063a86…`), so the measured fixture bytes are the delivered r97 bytes.

Mid-flight note: S1's contract was still being written while I measured. First revision observed `c435239d…` (poll2 try 1); the final revision `153ebc5b…` differs **only** in the `provenance_note` string (structural diff of the parsed JSON shows a single changed line: the note gains the r98 paragraph); pins, `self_test.expected` (17 cases) and `revision` are identical. Every measurement quoted below was re-run on the final revision `153ebc5b…` after the change; no result comes from the superseded bytes.

## 0. Poll-wait record

Poll 1 (20 s cadence, 40 tries) checked artifacts AND an `S1*` entry in the seats dir:

```
try 15 20:32:26 | S1reports=[S1-scratch ] r98fix=yes r97fix=yes pins=[r88-m3-maya-cluster,r94-paired-crossing,r95-crossing-aftermath,r96-crossing-response]
try 16 20:32:46 | S1reports=[S1-scratch ] r98fix=yes r97fix=yes pins=[…,r97-crossing-acknowledgment,r98-clerk-filing]
POLL-SATISFIED at try 16
```

Caveat recorded honestly: the `S1*` glob matched S1's **scratch directory**, not its report file — the artifact condition (both new pins present) is what actually satisfied. Poll 2 was therefore started specifically for `S1*.md`; it satisfied at its try 7 (20:35:34) when `S1-freeze-hygiene.md` landed, with tool `03d04365…` and contract `153ebc5b…` byte-unchanged across every try (see §6). The discharge below rests on S1's delivered artifacts (tool + contract + pins), not on any plan text.

Baseline pre-state confirmed before S1 landed: contract `27273be2…` pinned exactly `['r88-m3-maya-cluster','r94-paired-crossing','r95-crossing-aftermath','r96-crossing-response']` — V46's r97 FAIL state.

## 1. Baseline reproduction — V46's recorded FAIL on r97 bytes

Baseline mirror built from `9a3d648` (`git show` for tool/contract, `git archive` for the fixture), at the fixture's pinned repo-relative path. Mutator (V46's exact mechanics, `json.dumps(timeline, indent=2) + "\n"`):

```
$ python3 .ufo/waves/round-98/seats/V06-scratch/mutate.py <baseline-mirror>/corpus/fixtures/r97-crossing-acknowledgment response-evin-salt-court acknowledgment-aru-records
event=acknowledgment-aru-records before=['response-evin-salt-court'] after=[]
```

The mutated bytes are **byte-identical to V46's r97 scratch copy** (strongest continuity evidence — same mutation, same bytes):

```
37a425b97af658d71b8dc8904f43fd75859905bac326489a71adb67004004eb1  <baseline-mirror>/…/timeline.json
$ cmp <baseline-mirror>/…/timeline.json .ufo/waves/round-97/seats/V46-scratch/r97-depdropped/timeline.json
BYTE-IDENTICAL to V46's mutated timeline
```

Baseline tool+contract on those mutated bytes — the recorded FAIL, not a catch:

```
$ python3 <baseline-mirror>/corpus/tools/dependency_freeze.py <baseline-mirror>/corpus/fixtures/r97-crossing-acknowledgment
FINDING UNPINNED-FIXTURE: no pin for 'r97-crossing-acknowledgment' in corpus/tools/dependency-freeze-contract.json
(pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response'])
RESULT ERROR                                                                                  EXIT=2
```

Intact baseline bytes gave the identical `UNPINNED-FIXTURE` exit 2 — matching V46 §2's control exactly.

## 2. Delivered revision — intact r97 is clean

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment          # in-place, delivered path
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6
RESULT PASS                                                                                   EXIT=0
```

Same result in the delivered mirror (tool + contract + fixture copies under `.ufo/waves/round-98/seats/V06-scratch/delivered-mirror/`), so the pass is not an artifact of the repo-root invocation:

```
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6
RESULT PASS                                                                                   EXIT=0
```

The pinned digest `3c922d20…` is the same digest V46 produced when it froze the fixture in its r97 scratch mirror — the delivered pin is the same inventory on the same bytes V46 demonstrated the catch with, now in the delivered contract (`pins['r97-crossing-acknowledgment'].content_sha256`, `fixture: "corpus/fixtures/r97-crossing-acknowledgment"`, counts `events 6 / dependency_edges 5 / relations 1 / entities 5 / sources 6`, frozen edge `acknowledgment-aru-records -> ['response-evin-salt-court']` at tick 13).

## 3. Delivered revision — the V46 mutation is caught (discharge)

Fresh mirror copy, V46's exact mutation (same mutator, same bytes; surgical check: all nine non-timeline files `IDENTICAL` to the delivered fixture, `timeline.json` sha `73063a86… → 37a425b9…`, `cmp` byte-identical to V46's mutated copy). Verification with the delivered tool + contract:

```
$ python3 <delivered-mirror-mut>/corpus/tools/dependency_freeze.py <delivered-mirror-mut>/corpus/fixtures/r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5; relations 1/1
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
RESULT FAIL                                                                                   EXIT=1
```

Edge count `4/5` and the named finding match V46 §4's scratch-mirror catch character for character. The observed precedence also matches the contract's declared order (`precedence`: semantic inventory findings decide first, exit 1; a content digest change the frozen inventory does not model exits 2): the mutation is modelled by the frozen inventory, so exit 1 `REDUCTION-DETECTED`, not exit 2 `DIGEST-MISMATCH`.

So: at r97 the identical bytes were `UNPINNED-FIXTURE` exit 2 (FAIL recorded); at the delivered r98 revision they are `REDUCTION-DETECTED` exit 1. **V46's recorded FAIL is discharged.**

Negative control (same mutated bytes, same delivered tool+contract, foreign path — proves the catch comes from the pinned path binding, not path luck):

```
FINDING PATH-MISMATCH: pin r97-crossing-acknowledgment names corpus/fixtures/r97-crossing-acknowledgment (resolves to …/delivered-mirror/corpus/fixtures/r97-crossing-acknowledgment); invoked fixture resolves to …/delivered-mirror/foreign/r97-crossing-acknowledgment
RESULT ERROR                                                                                  EXIT=2
```

## 4. The mutation is still invisible to the other gates (V46's class preserved)

On the same mutated mirror bytes, delivered tools: `check_bible.py` `CLEAN: schema, citations, relations, timeline; 0 violations` EXIT=0; `support_check.py` `RESULT PASS` (`VALIDATED-ROWS 19/19`) EXIT=0; `map_obligations.py` `OBLIGATIONS raw=17 mapped=17` / `RESULT PASS` EXIT=0. So the freeze pin is the sole catch for this class, exactly as V46 found — now armed on the r97 fixture.

## 5. Adjacent context (not this seat's bar, measured for the record)

- `pins['r98-clerk-filing']` exists (path `corpus/fixtures/r98-clerk-filing`, counts `events 7 / dependency_edges 6 / relations 1 / entities 6 / sources 7`, digest `59a0f4fa…`); verify on the delivered fixture: `FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1 … RESULT PASS` EXIT=0.
- The delivered contract's own `provenance_note` self-claims the discharge with the same sha (`37a425b9…`, exit 1 REDUCTION-DETECTED); this seat's independent run reproduces it.

## 6. Producer-report poll (final state)

Poll 2 (`S1*.md` only, 20 s cadence) ran alongside §2–§5. It satisfied at try 7 (20:35:34) when `S1-freeze-hygiene.md` landed; across all tries the tool stayed `03d04365…` and the contract `153ebc5b…` (byte-unchanged, including after the report landed — verified again at final write-audit). So S1's report is present, and every measurement quoted above was taken on the final delivered bytes. Cross-agreement: S1 §4 independently reports the same freeze digest `3c922d20…` and the same mutation sha `37a425b9…` with `REDUCTION-DETECTED` exit 1; this seat's runs reproduce those values independently (S1 measured through its own mirror, V06 through its own baseline/delivered mirrors).

## 7. Write audit

Delivered hashes re-checked after all runs: tool `03d04365…`, contract `153ebc5b…`, r97 timeline `73063a86…` (unchanged). `git status --porcelain` shows only producer-owned modifications (`corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json`, `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md`, the two scope notes, `LOG.md`) plus untracked round dirs and `corpus/fixtures/r98-clerk-filing/` + `corpus/knowledge/r98-clerk-scope-note.md`; nothing under `corpus/` was written by this seat. My writes live under `.ufo/waves/round-98/seats/V06-scratch/` (`mutate.py`, `poll.sh`, `poll2.sh`, `build_mirror.sh`, `baseline-mirror/`, `delivered-mirror/`, `delivered-mirror-mut/`) plus this report.

## Bottom line

**PASS** — on the delivered revision (tool `03d04365…`, contract `153ebc5b…`, 6 pins) the intact r97 fixture verifies clean (`FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1`, `RESULT PASS` EXIT=0, in-place and in a mirror) and V46's exact mutation — byte-identical to V46's r97 scratch copy (`cmp`, timeline `37a425b9…`) — is caught as `FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']` with `dependency-edges 4/5`, `RESULT FAIL` EXIT=1, where the identical baseline bytes gave `UNPINNED-FIXTURE` EXIT=2; the other three gates stay green on the mutated bytes, and the catch is bound to the pin's recorded path (`PATH-MISMATCH` EXIT=2 at a foreign path). V46's recorded r97 FAIL is discharged. S1's report (`S1-freeze-hygiene.md`) landed 20:35:34 with the measured bytes unchanged and independently reports the same digest/mutation sha; poll record in §0/§6.
