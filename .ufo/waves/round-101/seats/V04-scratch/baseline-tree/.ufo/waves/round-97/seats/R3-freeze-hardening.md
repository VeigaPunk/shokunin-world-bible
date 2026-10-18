# R3 freeze-hardening — round 97 seat report

- Seat: R3 (producer, exclusive byte-ownership). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline `f3e09f9`; all commands run from the lane repo root with `python3`.
- Owned paths written: `corpus/tools/dependency_freeze.py` and `corpus/tools/dependency-freeze-contract.json` (only). Scratch: `.ufo/waves/round-97/seats/R3-scratch/`. No commits, no pushes, no network, no writes outside those paths plus this report and scratch.
- Delivered revisions: tool sha256 `b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130`; contract sha256 `27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781`. Diff vs HEAD: tool `+147/-42`, contract `+366/-352` (the latter is mostly the indent normalization below).
- Self-test scratch is created with `dir=ROOT` (repo root), matching the lane precedent at `corpus/tools/map_obligations.py:831`; `/tmp` was inode-exhausted during this round (`df -i /tmp` → `IUsed 1048576 / IFree 0 / IUse% 100`), so the old `/tmp`-based scratch could not be relied on. No scratch dirs are left behind (checked after every run).

## Claim C2 items delivered

| Item | Delivered behavior |
|---|---|
| (a) scope guard | `--freeze` accepts only targets resolving inside `corpus/fixtures/**`; anything else exits 2 `SCOPE-REFUSED` with a stable detail. `corpus/fixtures` itself is refused too. Symlinks are resolved, so a link inside the scope pointing out is refused. |
| (b) path binding | Each pin's `fixture` (repo-relative path) is validated on read (`CONTRACT-INVALID` when missing/absolute/out-of-scope) and enforced at verify: the invoked fixture must resolve to `ROOT/pin["fixture"]`, else exit 2 `PATH-MISMATCH` naming both paths. |
| (c) digest naming | `DIGEST-MISMATCH` now names the changed file(s) with before/after sha256. |
| (d) self-test | 14 → 16 cases; `scope_refused` and `path_mismatch` persisted in `self_test.expected`; the harness now builds a per-case **mirror root** (tool + contract + fixture at the pinned repo-relative path) so the 14 legacy mutation cases keep working under strict binding while still exercising the real CLI in a subprocess. |

Two further fail-closed additions inside the same guard family (not separate self-test cases — the claim fixes the count at 16):

- `--freeze` also refuses a **same-named in-scope** target when an existing pin names a different path (`SCOPE-REFUSED`), closing the r96 NB-04 laundering vector's in-scope variant (freezing `corpus/fixtures/shadow/<name>` would otherwise silently rewrite the delivered pin).
- `freeze` now propagates the post-freeze `verify` exit code instead of always returning 0.

## Baseline (before any edit, delivered f3e09f9 revision)

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster   -> RESULT PASS exit 0 (digest 15ef230e…)
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing   -> RESULT PASS exit 0 (digest 2527beb9…)
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath -> RESULT PASS exit 0 (digest d541ae64…)
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response -> RESULT PASS exit 0 (digest d422a9b3…)
$ python3 corpus/tools/dependency_freeze.py --self-test | tail -2
SELF-TEST 14/14
RESULT PASS
```

## (b) before/after on the original r96 trick path

The r96 evidence path still exists and is byte-identical to the canonical r94 fixture (all five JSON tables: `SAME` for `entities/relations/timeline/sources/contradictions`), so the "before" was reproduced on the exact artifact r96 used:

```
$ python3 .ufo/.../R3-scratch/mirror/corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/V38-scratch/d3/r94-paired-crossing   # f3e09f9 bytes
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS
exit=0

$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/V38-scratch/d3/r94-paired-crossing   # delivered
FINDING PATH-MISMATCH: pin r94-paired-crossing names corpus/fixtures/r94-paired-crossing (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r94-paired-crossing); invoked fixture resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats/V38-scratch/d3/r94-paired-crossing
RESULT ERROR
exit=2
```

Controlled mirror pair (same tool instance, canonical vs byte-identical copy in one mirror root) — old tool: receipts `diff` → `IDENTICAL` (exit 0 both sides); delivered tool: canonical `RESULT PASS exit 0`, copy `exit 2 PATH-MISMATCH`. The old tool sha used for the "before" is `a3b57978…`, matching V49's r96 receipt for Q3's delivered revision.

## (a) scope guard, with no-write proof

```
$ python3 corpus/tools/dependency_freeze.py --freeze .ufo/waves/round-97/seats/R3-scratch/scope-probe/target
FINDING SCOPE-REFUSED: --freeze refuses .ufo/... (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/...); the frozen scope is corpus/fixtures/** (integration-time operation only)   RESULT ERROR   exit=2
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/tools            -> SCOPE-REFUSED exit 2
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures         -> "refuses corpus/fixtures itself" SCOPE-REFUSED exit 2
$ python3 corpus/tools/dependency_freeze.py --freeze /tmp/outside-probe      -> SCOPE-REFUSED exit 2
$ python3 <mirror tool> --freeze <mirror>/corpus/fixtures/evil-link          -> "resolves to /etc" SCOPE-REFUSED exit 2
contract sha before=8015e1f9… after=8015e1f9… unchanged=YES
```

In-scope same-named shadow + control (mirror root, so the delivered contract was never at risk):

```
$ python3 <mirror tool> --freeze <mirror>/corpus/fixtures/shadow/r95-crossing-aftermath
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/shadow/r95-crossing-aftermath: pin r95-crossing-aftermath already names 'corpus/fixtures/r95-crossing-aftermath'; freezing a same-named path elsewhere would rewrite the delivered pin   RESULT ERROR   exit=2
mirror contract unchanged=YES
$ python3 <mirror tool> --freeze <mirror>/corpus/fixtures/new-in-scope     # fresh in-scope name
FROZEN new-in-scope: events 4; dependency-edges 3; relations 1 … RESULT PASS exit=0
```

Pin-side self-validation (mirror contract repointed to `corpus/tools/dependency_freeze.py`):

```
FINDING CONTRACT-INVALID: pin r94-paired-crossing names corpus/tools/dependency_freeze.py, outside corpus/fixtures/**   RESULT ERROR   exit=2
```

## (c) DIGEST-MISMATCH names the changed file

Prose drift invisible to the edge inventory, in a mirror:

```
FINDING DIGEST-MISMATCH: content digest f6e5c1a8… != pin 2527beb9…; changed: timeline.json (sha256 f0209f90a6ce795211369bd900ac1d333d16eb0af123f1b170831e192660533c -> 5b45c05a3a0a2933e4c8067b5ea3051e9dcf754afb85be8ec70354796e87c1d3); fixture bytes changed outside the frozen inventory
RESULT ERROR
exit=2
```

## (d) self-test 16/16

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE clean: exit=0 expected=0 findings=[] ok
… 13 legacy cases unchanged and ok …
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
SELF-TEST 16/16
RESULT PASS
```

## Pin refresh through the guarded path — measured result (a claim discrepancy, recorded exactly)

```
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r96-crossing-response
FROZEN r96-crossing-response: events 5; dependency-edges 4; relations 1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
RESULT PASS
exit=0
```

Semantic pre/post contract diff (`json` compare of the pre-freeze copy in scratch vs the delivered file):

- `pins.r88-m3-maya-cluster`, `pins.r94-paired-crossing`, `pins.r95-crossing-aftermath`: **byte-identical**.
- `pins.r96-crossing-response`: only `revision` changed, `60dba0c2aa344860b10a2fc63e00468d1b134f27 -> 2393934237ea076366f3db6dceeff033edb52ab1`; `content_sha256` **unchanged** (`d422a9b3…`), `files`, `events`, `relations`, `counts`, `fixture` unchanged.
- top-level `revision` → `2393934…`; `self_test` (16 expectations), `scope`, `precedence`, `data_files`, `required_files`, `exit_codes`, `tool`, `schema_version` identical apart from the deliberate text updates below.
- pins count 4 → 4.

**Recorded discrepancy:** the claim says the pin refresh happens because "the digest changes by the repair". Measured, it does **not**: `DATA_FILES` covers only the five JSON tables and R4's cosmetic repair touched only `claim-excerpt-map.md`, so `d422a9b3…` is unchanged (R4's report reaches the same conclusion in its "Freeze pin vs the repair" note). The refresh is therefore a guard/format/revision refresh through the guarded path, not a digest change; I report it as such rather than claiming the digest moved.

**Formatting note:** the tool's writer uses `json.dumps(..., indent=2)`, while the file at HEAD was hand-formatted at indent 1, so the rewrite reindented the whole file (contract numstat `+366/-352`). Content-preserving; every semantic field is accounted for above.

## Final receipts on the delivered revision

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; done
r88-m3-maya-cluster: RESULT PASS (15ef230e…)
r94-paired-crossing: RESULT PASS (2527beb9…)
r95-crossing-aftermath: RESULT PASS (d541ae64…)
r96-crossing-response: RESULT PASS (d422a9b3…)          # chain 4/4 clean
$ python3 corpus/tools/dependency_freeze.py --self-test | tail -2
SELF-TEST 16/16
RESULT PASS
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment   -> CLEAN exit 0 (unchanged by this seat)
$ python3 corpus/tools/boundary_doc_check.py  -> CERTIFIED exit 0
$ python3 corpus/tools/discriminate_check.py  -> RESULT: DISCRIMINATION HELD exit 0
$ ls -d dependency-freeze-self-test-*   -> No such file or directory   (no stray scratch)
```

Unchanged by the hardening: the verify receipt format (`FREEZE <name>: events a/b; dependency-edges c/d; relations e/f` + `DIGEST` + `RESULT`), the 0/1/2 exit contract, and the semantic-first precedence. The r96 fixture's other receipts are R4's to report; nothing in this seat touches them.

## Residuals and notes for adjudication

1. **README is stale and is not mine to write.** `corpus/tools/README.md:175` (R2-owned) still says self-test "14/14" and lists the three r96 hazards as open (`--freeze` has no scope guard; receipts not path-bound; `DIGEST-MISMATCH` does not name the changed file) — all three are closed here, and the new ids (`SCOPE-REFUSED`, `PATH-MISMATCH`, plus `CONTRACT-INVALID` for out-of-scope pin paths) are undocumented there. R2's report (`R2-contract-docs.md`) does not mention `dependency_freeze` at all, so this is an open doc-parity item for the round (README byte-ownership is R2's).
2. **`r97-crossing-acknowledgment` is not pinned** — the chain stays the four fixtures the claim declares (`--self-test`/chain receipts above). Running the tool on it gives `UNPINNED-FIXTURE` exit 2 by design. Pinning it is a candidate for r98 (it has one new `depends_on` edge the BR-01 class covers).
3. **Mirror-root caveat (semantics, not a hole):** a copied tool + contract rooted elsewhere still verifies copies, because binding is to the running tool's own `ROOT`. That is the intended meaning of "the pinned path"; the delivered tool refuses every path that is not the delivered fixture's.
4. **Environment:** `/tmp` inode exhaustion this round is why the self-test scratch moved to `dir=ROOT`; the delivered self-test therefore no longer depends on the system temp dir. `TMPDIR` does not affect it (`dir=` wins).
5. The in-scope same-named freeze refusal is an addition beyond the four enumerated C2 items; it is deliberately *not* a 17th self-test case (the claim fixes the count at 16) and is reported under the already-pinned `SCOPE-REFUSED` id.
6. No commits were made; the contract now records `2393934…` as the top-level and r96-pin revision (HEAD at refresh time).

## Bottom line

**PASS** — C2 delivered and verified on the delivered revision: scope-guarded `--freeze` (`SCOPE-REFUSED`, no write on refusal, symlink and same-named-shadow refusals included), pin path binding that turns the original r96 shadow-copy trick into exit 2 `PATH-MISMATCH`, `DIGEST-MISMATCH` naming the changed file, self-test 14→16 pinned in the contract with 16/16 green, r96 re-frozen through the guarded path (digest measured unchanged by R4's repair — the claim's digest-change parenthetical is inaccurate), chain 4/4 clean; the only unresolved item is the R2-owned README paragraph still describing the pre-r97 tool.
