# V30 — verdict-coverage (round 97, single-wave)

**Seat scope (verbatim):** *V30 verdict-coverage — report
.ufo/waves/round-97/seats/V30-verdict-coverage.md — Read C2 seats; own
guard/path demos; one COVERAGE verdict with bounds.*

Claim under test: **C2 — `dependency_freeze` hardening**: (a) `--freeze`
scope-guarded to `corpus/fixtures/**`; (b) path binding — byte-identical
same-named copy at a foreign path exits 2 `PATH-MISMATCH`; (c)
`DIGEST-MISMATCH` names the changed file; (d) self-test 14→16; plus the r96
pin refresh through the guarded path and chain 4/4 at closure.

Repo root for every command: `/home/vgpnk/Projects/shokunin/lore-shokunin`
(session cwd is the parent repo; every path below absolute or `cd`-anchored).
Baseline: r96 closure `f3e09f9`; HEAD `2393934`.

## 0. Timeline and delivery

- 18:43 poll start (20 s cadence, 40 tries, `V30-scratch/poll.sh`).
- 18:51:38 tool bytes appear (`PATH-MISMATCH` present), 18:53:21 contract
  reaches 16 cases, 18:54:38 r96 pin refreshed, 18:55:14 contract rewritten
  (final bytes). 18:56:18 poll try 40 → `TIMEOUT-ABSENT` (R3 report not yet
  written); R3 report `R3-freeze-hardening.md` landed 18:56:23.
- Final bytes under test (stable through all final runs):
  tool `b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130`,
  contract `27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781`.
  Baseline bytes: tool `a3b57978…`, contract `c65ac3bd…`, self-test 14/14.

**Poll protocol note:** at poll end the *artifacts* were present but the
*producer report* was not; I verified the delivered artifacts (read-only and
scratch-confined) and read the report when it landed 5 s later. No plan was
verified; every claim below rests on executed commands against delivered bytes.

## 1. Pre-change hazard reproduction (baseline tool, my own mirror)

Mirror = tool + contract + fixtures copied under `V30-scratch/mirror/` so
`ROOT = parents[2]` resolves inside scratch; the real contract is never
written. Harness validated (freeze/verify round-trip in mirror).

- **B1** `--freeze $M/outside-fixtures/r96-crossing-response` (valid fixture
  outside `corpus/fixtures/`): `FROZEN r96-crossing-response … RESULT PASS
  exit=0`; pin label rewritten to `outside-fixtures/r96-crossing-response`.
- **B2** byte-identical foreign copy (`timeline.json` sha256 `ea0225f9…` both
  sides): `RESULT PASS exit=0` — no path binding.
- **B3** one trailing space appended to `timeline.json`: `FINDING
  DIGEST-MISMATCH: content digest dc135edb… != pin d422a9b3…; fixture bytes
  changed outside the frozen inventory` — no file name.
- **B4** mirror self-test: `SELF-TEST 14/14`.

## 2. After-state demos on the delivered revision

### 2.1 Real tree (read-only probes; hash-guarded deny)

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; done
r88  -> RESULT PASS  (DIGEST 15ef230e…)   exit=0
r94  -> RESULT PASS  (DIGEST 2527beb9…)   exit=0
r95  -> RESULT PASS  (DIGEST d541ae64…)   exit=0
r96  -> RESULT PASS  (DIGEST d422a9b3…)   exit=0     # chain 4/4 clean

$ python3 corpus/tools/dependency_freeze.py $S/foreign/r96-crossing-response     # byte-identical copy (timeline ea0225f9… both sides)
FINDING PATH-MISMATCH: pin r96-crossing-response names corpus/fixtures/r96-crossing-response
  (resolves to …/corpus/fixtures/r96-crossing-response); invoked fixture resolves to …/V30-scratch/foreign/r96-crossing-response
RESULT ERROR   exit=2

$ python3 corpus/tools/dependency_freeze.py --self-test
SELF-TEST 16/16
RESULT PASS   exit=0

$ python3 corpus/tools/dependency_freeze.py --freeze corpus/tools
FINDING SCOPE-REFUSED: --freeze refuses corpus/tools …; the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR   exit=2
contract sha256 before=27273be2… after=27273be2… unchanged=YES
```

Also `--freeze corpus/fixtures` → `SCOPE-REFUSED … refuses corpus/fixtures
itself` exit 2. No `dependency-freeze-self-test-*` strays at repo root after
any self-test run.

### 2.2 Mirror battery (writes confined to scratch)

- **D1/D2** deny `corpus/knowledge` and an absolute outside-repo path:
  `SCOPE-REFUSED` exit 2, mirror contract hash unchanged after each refusal.
- **D3** allow `mirror/corpus/fixtures/r96-crossing-response`: `FROZEN …
  RESULT PASS` exit 0 (guard is permissive in scope, not merely blocking).
- **D4** byte-identical foreign copy (mirror tool): `PATH-MISMATCH` exit 2.
- **D5** legit path: `RESULT PASS` exit 0.
- **D6** whitespace-only tamper at the legit path: `FINDING DIGEST-MISMATCH:
  content digest dc135edb… != pin d422a9b3…; changed: timeline.json
  (sha256 ea0225f9… -> 4d7f164f…); fixture bytes changed outside the frozen
  inventory` exit 2 — **claim (c) confirmed**.
- **D7** symlink at a foreign path → resolves to the pinned fixture: binding
  passes (no `PATH-MISMATCH`); the tampered target then yields the D6
  `DIGEST-MISMATCH`. Binding/guard are `resolve()`-based.
- **D8** symlink inside `corpus/fixtures/` → `corpus/knowledge`:
  `SCOPE-REFUSED` (the refusal names the resolved target) — escape blocked.
- **D9** nested dir inside a fixture: accepted (`FROZEN nested … RESULT PASS`)
  — `corpus/fixtures/**` is prefix-scoped, by declaration.
- **D10** mirror self-test 16/16.
- **E1** same-named copy elsewhere *under fixtures* (`corpus/fixtures/subdir/r96-crossing-response`):
  `SCOPE-REFUSED: … pin r96-crossing-response already names
  'corpus/fixtures/r96-crossing-response'; freezing a same-named path
  elsewhere would rewrite the delivered pin` exit 2; original pin untouched.
- **E2** foreign copy with an *unpinned* name: `UNPINNED-FIXTURE` exit 2
  (name lookup precedes binding).

### 2.3 The 16-case pin is load-bearing

Dropping one pinned case from the mirror contract's `self_test.expected`
(`scope_refused`) and re-running:

```
FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=['scope_refused'] extra=[]
RESULT ERROR   exit=2
```

Restored → `SELF-TEST 16/16 RESULT PASS`. So a missing pinned case fails the
suite closed (the freeze analog of C1's tightened loader), and the two new
expectations are `scope_refused` (exit 2, `SCOPE-REFUSED`) and `path_mismatch`
(exit 2, `PATH-MISMATCH`) — exactly the classes the claim names.

### 2.4 Pin refresh and chain

- r96 pin: `revision` `60dba0c2… -> 23939342…` (current HEAD), `fixture`,
  `files`, `events`, `relations`, `counts`, `content_sha256` (`d422a9b3…`)
  unchanged; top-level `revision` → `2393934…`; pins count 4 → 4.
- Chain verify 4/4 clean with the expected digests (§2.1).
- **Recorded discrepancy (not mine alone):** any claim text implying the
  refresh moved the digest is inaccurate — `DATA_FILES` covers only the five
  JSON tables and R4's cosmetic repair touched only `claim-excerpt-map.md`, so
  the digest could not move. R3's report and R4's report reach the same
  conclusion; my measurement confirms `d422a9b3…` before and after.
- Contract rewrite `625ccfac… -> 27273be2…` at 18:55:14 is a reindent
  (`indent=2` writer vs `indent=1` at HEAD; `+366/-352`) plus the revision and
  field text; I verified the final pins/cases/scope directly and R3's semantic
  diff accounts for every field.

## 3. C2 seats read

- **R3 (producer)** — final report: matches every one of my measurements
  (hashes, `SCOPE-REFUSED` no-write proof, `PATH-MISMATCH` on the original r96
  shadow path, digest naming, 16/16, pin refresh with unchanged digest,
  residuals). Residuals it records: R2-owned README stale; r97 not pinned.
- **V09 (c2-selftest)** — read at 18:47 (pre-delivery): baseline + perturbation
  harness validated (one flipped expectation → 13/14 FAIL), `/tmp` hazard.
  Its 16/16 section was still PENDING at my last read; my own §2.1/§2.3 runs
  cover the same checks independently.
- **V45 (c2-guard-2)** — read at 18:47 (pre-delivery): before-state B-A/B-B/B-C
  match my B2/B3/B1 exactly. After-state A1–A7 still PENDING at my last read.
- **V26 (doc-parity)** — C2 doc inventory; confirms the README/SKILL stale
  wording as integration-time items.
- **V49 (inherited-tools)** — baseline manifest; C2 paths are the declared
  R3-owned set.
- **V08 (c2-digest-naming)** — scratch only; no report filed at read time.
- V09/V45 reports may be updated after my read; my verdict does not depend on
  them.

## 4. COVERAGE verdict (C2) and bounds

**VERDICT: PASS (bounded).** On the delivered revision, C2(a)–(d) and the pin
refresh are each demonstrated by my own executed commands: guard deny/allow
with no-write proof; foreign byte-identical copy → exit 2 `PATH-MISMATCH`;
legit paths → exit 0; `DIGEST-MISMATCH` names the changed file with before/after
sha256; self-test 16/16 with both new classes pinned and the case set
load-bearing; r96 re-frozen through the guarded path; chain 4/4 clean. The
0/1/2 exit contract and the verify receipt format are unchanged.

**Bounds (measured, not assumed):**

1. `--freeze` guard is write-scoped; verify of a foreign path is rejected only
   for *pinned* names (`PATH-MISMATCH`); an unpinned foreign name exits 2
   `UNPINNED-FIXTURE` (E2). No pin can be laundered through the verify path.
2. Binding and scope are `resolve()`-based: a foreign-path symlink resolving to
   the pinned fixture is accepted as that path (D7); a symlink inside fixtures
   resolving outside is refused (D8); `corpus/fixtures/**` is prefix-scoped, so
   nested in-scope targets are pinnable by declaration (D9), with same-named
   shadowing under fixtures separately refused (E1).
3. The pin payload is the five JSON tables only; markdown (`claim-excerpt-map.md`
   and siblings) is invisible to this gate — which is why the r96 repair left
   the digest unchanged. BR-01's prose half remains out of this tool's scope
   (already documented as open).
4. `r97-crossing-acknowledgment` is not pinned (chain stays the declared four
   fixtures); running the tool on it exits 2 `UNPINNED-FIXTURE` by design. Its
   edges are covered instead by `map_obligations` (`raw=17 mapped=17 RESULT
   PASS` measured). Pinning it is an r98 candidate (R3 residual 2).
5. Two extra fail-closed behaviors are delivered but not separate self-test
   cases (the claim fixes the count at 16): the in-scope same-named freeze
   refusal (reported under the pinned `SCOPE-REFUSED` id) and `freeze`
   propagating the post-freeze verify exit code.
6. **Doc parity gap (open, R2-owned):** `corpus/tools/README.md:175` still
   lists the three r96 hazards as open and "14/14" as of 18:55; no
   `PATH-MISMATCH`/`SCOPE-REFUSED`/16-case text. R3's residual 1 and V26's
   inventory agree. Not a tool-coverage hole; an integration-time doc item.
7. **Environment:** `/tmp` inode exhaustion this round; the delivered self-test
   now uses `dir=ROOT` (no `/tmp` dependency, no strays). All runs here also set
   `TMPDIR` into seat scratch.

## 5. Bottom line

**PASS (coverage, bounded)** — every C2 item verified on the delivered bytes
(tool `b06275f3…`, contract `27273be2…`) by independent guard/path/digest/self-test
demos plus a load-bearing contract-perturbation check; chain 4/4 clean, r96 pin
refreshed through the guarded path (digest unchanged — recorded discrepancy in
the refresh rationale); bounds listed in §4 (verify-side name gating, resolve()
symlink semantics, JSON-only pin payload, r97 unpinned, README stale, /tmp
environment).
