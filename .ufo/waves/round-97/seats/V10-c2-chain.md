# V10 c2-chain — round 97 seat report

- Seat: V10 (verifier, chain). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline `f3e09f9`; all commands run from the lane repo root with `python3`. Leaf seat; no nested agents, no commits, no pushes, no network.
- Poll-wait protocol executed: R3 (`R3-freeze-hardening.md`, tool + contract) and R4 (`R4-fixture-author.md`, r96 repair + r97 fixture) absent at start; polled in 20 s cadence across four windows (12 + 13 + 13 + 5 tries ≈ 14 min). R4's report landed in window 2, R3's in window 4 (tool mtime 18:53:00, contract mtime 18:55:14). Both reports present before any verification below; nothing was verified from a plan.
- Scope of this seat: (1) chain verify 4/4 clean at the delivered paths; (2) the r96 pin refreshed by R3 matches the POST-REPAIR r96 fixture digest, recomputed independently by me; (3) the contract pins exactly four fixtures, each with a path. Supporting evidence (self-test, path-binding probe, revision hashes) recorded because it is cheap and load-bearing for the chain reading.
- Scratch (mine): `.ufo/waves/round-97/seats/V10-scratch/` (foreign-path copy probes; retained as evidence). Only write outside scratch is this report, at the absolute path `.ufo/waves/round-97/seats/V10-c2-chain.md`.

## 1. Chain verify 4/4 clean at the delivered paths — PASS

Delivered paths taken from the contract's own `fixture` fields (not typed from the claim):

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do echo "=== python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f"; python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; echo "EXIT=$?"; done
=== python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279
RESULT PASS
EXIT=0
=== python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS
EXIT=0
=== python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
EXIT=0
=== python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
RESULT PASS
EXIT=0
```

4/4 exit 0 `RESULT PASS`, one clean receipt per fixture; the receipts show observed counts equal to the pinned counts on every fixture. No finding lines, no tracebacks.

## 2. r96 pin vs POST-REPAIR r96 fixture — digest recomputed independently — PASS

The repair is the one in the tree (R4's declared after-hash reproduced):

```
$ sha256sum corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
$ git diff --stat -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
 corpus/fixtures/r96-crossing-response/claim-excerpt-map.md | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
```

I reimplemented the tool's digest algorithm (`sha256(json.dumps({name: sha256(raw)}, sort_keys=True, separators=(",",":")))`) in a standalone script and recomputed from current tree bytes — no tool code imported:

```
=== independent recompute vs pins (delivered revision) ===
r88-m3-maya-cluster: recomputed=15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279 pin=15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279 MATCH=True
r94-paired-crossing: recomputed=2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75 pin=2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75 MATCH=True
r95-crossing-aftermath: recomputed=d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9 pin=d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9 MATCH=True
r96-crossing-response: recomputed=d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6 pin=d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6 MATCH=True
ALL PIN DIGESTS MATCH: True
```

Per-file digests: all five r96 `files` entries matched the post-repair bytes (the loop printed no `FILE DIFF` line for any fixture). So the pin matches the fixture **as delivered**, including after R4's repair.

**Precision note (a claim-wording discrepancy, not a failure).** The seat brief says "the r96 pin refreshed by R3 matches the POST-REPAIR r96 map digest". Measured, the cosmetic repair could not move the pin digest at all: the pin's `content_sha256` covers only the five JSON tables (`DATA_FILES`), and R4's repair touched only `claim-excerpt-map.md`, which is not a pinned file. The digest I recomputed from the pre-repair tree earlier in this session (before R3 landed, `18:46`) was **already** `d422a9b3…` — identical. The "refresh" is therefore a revision/format refresh through the guarded path, exactly as R3 recorded in its report ("the claim's digest-change parenthetical is inaccurate") and R4 in its "Freeze pin vs the repair" note. What is true and verified: the refreshed pin matches the post-repair fixture byte-for-byte, and the refresh landed after the repair (contract mtime `18:55:14` > map mtime `18:43:42`), with the pin's `revision` bumped to the then-current HEAD:

```
$ git rev-parse HEAD
2393934237ea076366f3db6dceeff033edb52ab1
contract top revision: 2393934237ea076366f3db6dceeff033edb52ab1
r96 pin revision:     2393934237ea076366f3db6dceeff033edb52ab1
```

Provenance-consistency (guarded-path writer, not hand-edit): the contract at HEAD was hand-formatted at indent 1, the delivered file is at indent 2 — the tool's writer emits `json.dumps(..., indent=2)`, consistent with a rewrite by `freeze()`; `revision` fields auto-set to HEAD are consistent with the same. R3's declared delivered hashes reproduce exactly:

```
tool sha256: b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130
contract sha256: 27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781
```
(match R3's report values `b06275f3…` / `27273be2…`).

## 3. Contract pins exactly four fixtures with paths — PASS

```
pin count: 4
r88-m3-maya-cluster | fixture: 'corpus/fixtures/r88-m3-maya-cluster' | content_sha256: 15ef230e… | revision: 60dba0c2…
r94-paired-crossing | fixture: 'corpus/fixtures/r94-paired-crossing' | content_sha256: 2527beb9… | revision: 60dba0c2…
r95-crossing-aftermath | fixture: 'corpus/fixtures/r95-crossing-aftermath' | content_sha256: d541ae64… | revision: 60dba0c2…
r96-crossing-response | fixture: 'corpus/fixtures/r96-crossing-response' | content_sha256: d422a9b3… | revision: 2393934…
pins count: 4 (exactly four: True)
r88-m3-maya-cluster: fixture='corpus/fixtures/r88-m3-maya-cluster' exists=True rel_ok=True inside_scope=True
r94-paired-crossing: fixture='corpus/fixtures/r94-paired-crossing' exists=True rel_ok=True inside_scope=True
r95-crossing-aftermath: fixture='corpus/fixtures/r95-crossing-aftermath' exists=True rel_ok=True inside_scope=True
r96-crossing-response: fixture='corpus/fixtures/r96-crossing-response' exists=True rel_ok=True inside_scope=True
```

Exactly four pin keys, no fifth (`c3red` stayed removed), every pin carries a repo-relative `fixture` path, each resolves inside `corpus/fixtures/**` and to an existing directory, and each pinned name equals the directory basename it points at. The four `content_sha256` values match my independent recompute (section 2).

## Supporting checks (cheap, chain-load-bearing)

Self-test on the delivered revision (R3's C2(d); supports the pin file's integrity):

```
$ python3 corpus/tools/dependency_freeze.py --self-test | tail -4
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
SELF-TEST 16/16
RESULT PASS
```
Contract `self_test.expected` holds exactly the 16 expected case names (14 legacy + `scope_refused` + `path_mismatch`).

Path binding is load-bearing on the refreshed r96 pin (my probe, scratch copy, five JSON tables byte-identical to the delivered fixture):

```
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-97/seats/V10-scratch/foreign/r96-crossing-response
FINDING PATH-MISMATCH: pin r96-crossing-response names corpus/fixtures/r96-crossing-response (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r96-crossing-response); invoked fixture resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V10-scratch/foreign/r96-crossing-response
RESULT ERROR
EXIT=2
--- byte-identity ---
entities.json SAME / relations.json SAME / timeline.json SAME / sources.json SAME / contradictions.json SAME
--- delivered path still PASS ---
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
RESULT PASS
EXIT=0
```

(First probe attempt with a copy named `r96-copy` exited 2 `UNPINNED-FIXTURE` — name lookup precedes path binding; the same-named probe above is the one that exercises binding.) No stray `dependency-freeze-self-test-*` dirs left in the repo root (`ls -d` → not found).

## Bounds

- This seat verified the chain/pin/contract faces only. The scope-guard refusal cases, `DIGEST-MISMATCH` naming, contract loader strictness, and the r97 fixture's own content are other seats' claims; I did not duplicate them beyond the self-test run above.
- `r97-crossing-acknowledgment` is deliberately unpinned (R3 residual 2) and was not part of my chain; running the tool on it yields `UNPINNED-FIXTURE` exit 2 by design.
- No claim in this report rests on a producer's quoted output: every value above was re-observed or recomputed at the delivered paths.

## Bottom line

**PASS** — chain verify 4/4 clean at the four contract-declared delivered paths (exit 0 each, digests quoted); the refreshed r96 pin matches the POST-REPAIR r96 fixture on my independent recompute (content `d422a9b3…` plus all five per-file digests; the repair itself could not move the digest because the map md is not a pinned file — recorded as a claim-wording discrepancy, not a defect); the contract pins exactly four fixtures, each with an existing repo-relative path inside `corpus/fixtures/**`.
