# V55 — crosscheck-coverage (round 97, single-wave)

**Seat scope (verbatim):** *V55 verdict-crosscheck-coverage — report
.ufo/waves/round-97/seats/V55-crosscheck-coverage.md — Independent coverage
verdict; compare V30.*

Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline `f3e09f9`
(HEAD `2393934`); every command below run from the lane repo root with
`python3`. Delivered revision under test: tool
`b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130`,
contract `27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781`
(both re-hashed unchanged after every run below; R3's report receipts the same
hashes).

**Poll-wait record.** First window (background, 20 s × up to 40 tries) ran to
try 30 before the harness 600 s cap; R1/R2/R4/R5/R6 reports and the r97
artifacts were all present by 18:53. Second window (`poll-r3.sh`) found R3's
report at **try 8, 2026-10-17T18:56:30-03:00** (`R3-freeze-hardening.md`).
Verification began only after the producer-owned artifacts were written and
was re-run end-to-end after R3's report landed; no plan was verified at any
point. Scratch: `.ufo/waves/round-97/seats/V55-scratch/` only; report path
above only; no commits, no network.

**Environment (host condition, r96 recurrence).** `/tmp` inodes exhausted —
`df -i /tmp` → `IUsed 1048575 / IFree 1 / IUse% 100`; an unredirected
`--self-test` crashed with `OSError: [Errno 28] No space left on device`.
All runs below set `TMPDIR` into seat scratch. The delivered self-test itself
now uses `dir=ROOT` (R3 residual 4) and left no `dependency-freeze-self-test-*`
strays (checked: `No such file or directory`).

## 1. Independent COVERAGE verdict

**PASS (coverage, bounded).** On the delivered revision, each C2 item and the
pin refresh are demonstrated by my own executed commands against a fake root
built from the delivered tool + contract (writes confined to scratch; the real
contract is never written by me — its sha256 is identical before/after my
real-tree deny probe). C2(a) scope guard, C2(b) path binding, C2(c) digest
naming, C2(d) self-test 14→16, r96 re-freeze (revision-only refresh), chain
4/4 clean. Details in §3–§4; bounds in §6.

## 2. Pre-change (baseline) reproduction — the three hazards existed

Baseline bytes: tool `a3b57978…`, contract `c65ac3bd…` (matches the r96
closure record). Baseline self-test and chain, reproduced under redirected
`TMPDIR`:

```
SELF-TEST 14/14
RESULT PASS          # exit 0
r88-m3-maya-cluster exit=0; r94-paired-crossing exit=0;
r95-crossing-aftermath exit=0; r96-crossing-response exit=0
```

Isolated fake root (`V55-scratch/fakeroot`, baseline tool + contract):

```
$ python3 corpus/tools/dependency_freeze.py foreign/r96-crossing-response   # B1: byte-identical copy at foreign path
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3…  RESULT PASS  exit=0                       # verified identically
$ python3 corpus/tools/dependency_freeze.py --freeze foreign/r96-crossing-response   # B2
FROZEN r96-crossing-response … RESULT PASS  exit=0          # accepted; pin rewritten
$ python3 -c "…['pins']['r96-crossing-response']['fixture']"  -> foreign/r96-crossing-response
# B3: case-change tamper in a foreign copy's timeline.json (non-inventory-modeled)
FINDING DIGEST-MISMATCH: content digest daeb21fd… != pin d422a9b3…; fixture bytes changed outside the frozen inventory
RESULT ERROR  exit=2                                        # no file named
```

## 3. Delivered-revision probes (all outputs from my runs; full logs in
`V55-scratch/probe-c2-final-run.log`, `probe-c2-run2.log`, `probe-c2-prelim.log`)

**P1 scope guard — 5 refusal classes, exit 2 `SCOPE-REFUSED`, no write:**

```
--freeze foreign/r96-crossing-response            -> SCOPE-REFUSED exit=2
--freeze <abs>/outofscope/r96-crossing-response   -> SCOPE-REFUSED exit=2
--freeze corpus/fixtures/../../foreign/r96-crossing-response -> SCOPE-REFUSED exit=2
--freeze corpus/tools                             -> SCOPE-REFUSED exit=2
--freeze corpus/fixtures                          -> "refuses corpus/fixtures itself" exit=2
contract sha after refusals = 27273be2… (equal to start)     # no write on refusal
```

**P10 in-scope same-named shadow (extra fail-closed behavior):**

```
$ --freeze corpus/fixtures/samenamed/r96-crossing-response
FINDING SCOPE-REFUSED: … pin r96-crossing-response already names 'corpus/fixtures/r96-crossing-response';
freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR  exit=2        # contract sha unchanged
```

**P2 guard is permissive in scope (fake root only):**

```
$ --freeze corpus/fixtures/r96-crossing-response   -> FROZEN … FREEZE 5/5 4/4 1/1  RESULT PASS exit=0
$ --freeze <abs>/corpus/fixtures/r94-paired-crossing -> FROZEN r94-paired-crossing … RESULT PASS exit=0
```

**P3 path binding (byte-identity first — all five foreign-copy files equal the
pin's `files` digests, incl. `timeline.json ea0225f9…`):**

```
$ verify foreign/r96-crossing-response            -> FINDING PATH-MISMATCH … exit=2
$ verify corpus/fixtures/nested/r96-crossing-response -> FINDING PATH-MISMATCH … exit=2
$ verify corpus/fixtures/r96-crossing-response    -> FREEZE 5/5 4/4 1/1  RESULT PASS exit=0
```

**P8 symlinks (resolve-based):** symlink inside fixtures → foreign target:
`--freeze` → `SCOPE-REFUSED` exit 2; `verify` → `PATH-MISMATCH` exit 2.

**P4 digest naming (tamper at the pinned path):**

```
FINDING DIGEST-MISMATCH: content digest daeb21fd… != pin d422a9b3…;
changed: timeline.json (sha256 ea0225f9… -> be77a509…); fixture bytes changed outside the frozen inventory
RESULT ERROR  exit=2
```

**P5 self-test 16/16 and load-bearing set:**

```
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
SELF-TEST 16/16  RESULT PASS  exit=0
contract self_test.expected count = 16
# load-bearing: drop scope_refused from a scratch contract copy ->
FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=['scope_refused'] extra=[]
RESULT ERROR  exit=2
```

**P6 chain 4/4 / P7 r97:**

```
r88 exit=0; r94 exit=0; r95 exit=0; r96 exit=0            # 4/4 clean
$ verify corpus/fixtures/r97-crossing-acknowledgment
FINDING UNPINNED-FIXTURE: … (pinned: [four chain fixtures])  exit=2
$ verify foreign/unpinned-copy (unpinned foreign name)    -> UNPINNED-FIXTURE exit=2
```

**P11 real-tree deny + hash guard:** `--freeze corpus/knowledge` →
`SCOPE-REFUSED` exit 2; real contract sha `27273be2…` before = after.

**Coverage census (my own script, `V55-scratch/census.py`, repo-relative
check_bible invocation per `corpus/fixtures/README.md`):**

```
DIRS 171; CLEAN 37; NEGATIVE 134; OTHER 0; VIOLATION-LINES 421
```

Delta proof via git: `git ls-tree -d --name-only f3e09f9 corpus/fixtures/`
→ 170; current → 171; only added name `r97-crossing-acknowledgment`; none
removed. So census 170→171 with the new fixture clean (36→37), negatives and
violation lines unchanged.

**Fixture receipts (frozen revision):** r96 `support_check` PASS
`SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; MODES 18/18; VALIDATED-ROWS
18/18` (unchanged by the repair), r96 `map_obligations` PASS `raw=16
mapped=16`; r97 `support_check` PASS `17/17; 2/2; MODES 19/19; VALIDATED-ROWS
19/19`, r97 `map_obligations` PASS `raw=17 mapped=17`; `check_bible` CLEAN
exit 0 for both.

## 4. Contract state after the guarded re-freeze

Semantic diff (baseline contract vs delivered): r96 pin **revision only**
`60dba0c2… -> 23939342…`; top-level `revision` → `2393934…`; two new
`self_test.expected` entries (`scope_refused`, `path_mismatch`); `scope` and
`provenance_note` text updates. `pins.r96-crossing-response.content_sha256`
**unchanged** (`d422a9b3…`), `fixture`/`files`/`events`/`relations`/`counts`
unchanged; other three pins byte-identical; pins 4 → 4.

**Recorded discrepancy (concurring with R3, R4, V30):** the refresh is a
guard/format/revision refresh through the guarded path, **not** a digest
change — `DATA_FILES` covers only the five JSON tables and R4's cosmetic
repair touched only `claim-excerpt-map.md`, so the digest could not move.
Any claim text implying the repair moved the pin digest is inaccurate; the
delivered behavior and the declaration's "(pin refresh)" both hold.

## 5. Crosscheck vs V30 (`V30-verdict-coverage.md`, final text read 18:58:43)

V30's final verdict: **PASS (coverage, bounded)**, measured on the same final
hashes (`b06275f3…` / `27273be2…`). Comparison:

| Check | V30 | V55 (mine) | Agreement |
|---|---|---|---|
| Baseline hazards B1/B2/B3 + 14/14 | reproduced (mirror) | reproduced (fake root) | yes |
| Scope deny classes, no-write proof | `corpus/knowledge`, abs outside, `corpus/fixtures` itself | + traversal spelling, `corpus/tools`, scope dir itself; sha guard | yes |
| In-scope allow | mirror r96; nested dir accepted (D9) | same-path + abs in-scope accepted (P2) | yes |
| Foreign copy → `PATH-MISMATCH` | D4 (timeline byte-identical) | P3a/P3b (all five files byte-identical) | yes |
| Legit path → PASS | D5 | P3c | yes |
| `DIGEST-MISMATCH` names file | D6 (`timeline.json`, ws tamper) | P4 (`timeline.json`, case tamper) | yes |
| Symlink semantics | D7 resolve-to-pinned accepted; D8 escape refused | P8a refused; P8b foreign-target → `PATH-MISMATCH` | yes |
| Same-named in-scope shadow refused | E1 | P10 | yes |
| Unpinned foreign name → `UNPINNED-FIXTURE` | E2 | reproduced | yes |
| Self-test 16/16 + load-bearing set | §2.3 drop `scope_refused` → `CONTRACT-INVALID` | P5 + same perturbation | yes |
| Chain 4/4 | §2.1 | P6 | yes |
| r96 refresh revision-only | §2.4 | §4 | yes |
| r97 unpinned (chain 4) | bound 4 | P7 | yes |
| README stale (R2-owned) | bound 6 | observed (`README.md:175`, `corpus/README.md:38`, `SKILL.md:98`) | yes |
| /tmp inode exhaustion; `dir=ROOT` scratch | §2.1/§4.7 | §environment | yes |

Method differences (coverage of the crosscheck, not disagreement): V30 used a
scratch mirror battery D1–D15 + E1/E2; I used a fake root rebuilt from the
delivered bytes plus real-tree read-only probes. V30's real-tree contract hash
in its earlier D14/D15 (`625ccfac…`) is an **intermediate** revision (18:54:38
refresh, before R3's 18:55:14 final write); both of us verified the final
`27273be2…`. No contradiction found between the two verdicts; both are
`PASS (coverage, bounded)` with the same bounds.

## 6. Bounds for adjudication

1. **r97 fixture is not pinned** — `UNPINNED-FIXTURE` exit 2 by design; the
   declared chain is the four fixtures. BR-01 JSON-edge coverage does not yet
   extend to the r97 fixture (r98 candidate, R3 residual 2). Its edges are
   covered lexically by `map_obligations` (`raw=17 mapped=17`).
2. **Doc surfaces still describe the pre-r97 tool** — `corpus/tools/README.md:175`
   ("14/14"; the three hazards listed as open), `corpus/README.md:38`
   ("14-case persisted self-test"), `SKILL.md:98` ("14 cases"). R2's report
   does not mention `dependency_freeze` (`grep -c` = 0). Not a C2 claim
   failure (the declaration assigns no doc updates for C2) — a freshness
   witness for closure.
3. **Pin payload is the five JSON tables only** — markdown/prose invisible;
   this is why the repair left the digest unchanged; BR-01's prose half stays
   open as already documented.
4. **Binding/scope are `resolve()`-based** — a symlink resolving to the pinned
   path is treated as that path; an escape symlink is refused; any in-scope
   directory is pinnable (prefix scope), with same-named shadowing refused.
5. **Mirror-root caveat** — binding is to the running tool's own `ROOT`; a
   copied tool+contract rooted elsewhere verifies its own copies (intended
   meaning of "the pinned path").
6. **Two extra fail-closed behaviors beyond the four enumerated items** (not
   separate self-test cases; the count is fixed at 16): in-scope same-named
   freeze refusal (P10) and `freeze` propagating the post-freeze verify exit
   code.

## 7. Bottom line

**PASS (coverage, bounded)** — C2(a)–(d), the guarded r96 re-freeze
(revision-only; digest measured unchanged), and chain 4/4 each verified by my
own independent commands on the delivered revision; crosscheck vs V30:
**agrees — same verdict and bounds, no contradiction found.**
