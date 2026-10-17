# V45 — c2-guard-2: PATH-MISMATCH / shadow-copy demos (round 97)

Seat: V45 `c2-guard-2`. Claim under test: **C2 — `dependency_freeze` hardening** (scope guard, path binding,
DIGEST-MISMATCH naming, self-test 14→16, r96 re-freeze through the guarded path).
This seat's scope: independent PATH-MISMATCH / shadow-copy demos with fresh scratch, plus comparison with V07.
All commands run from repo root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`; all writes confined
to `.ufo/waves/round-97/seats/V45-scratch/` (created fresh 18:43 this round) and this report.

**Revision under test (final delivered):** tool sha256
`b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130`;
contract sha256 `27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781`.
Both match R3's delivered-revision declaration (`R3-freeze-hardening.md`) and were re-confirmed unchanged at
report write time. Full raw battery log: `V45-scratch/demos-after.log`.

**Environment note:** `/tmp` tmpfs inodes exhausted this round (`df -i /tmp` → `IUsed 1048575 / IFree 1 / 100%`);
the delivered self-test scratch uses `dir=ROOT` (repo root) and is unaffected by `TMPDIR`; no stray
`dependency-freeze-self-test-*` dirs were present at any final check (one transient dir from a concurrent seat's
run was observed mid-run and cleaned; none persisted).

## Timeline / poll

- Poll started 18:43:22 (script `V45-scratch/poll.sh`, log `V45-scratch/poll.log`; 20 s cadence, 40 tries).
- try 28 (18:52:22): hardened tool bytes landed (`PATH-MISMATCH` present).
- ~18:54–18:56: contract updated (self-test expectations) and r96 re-frozen; final contract hash `27273be2…`.
- try 40 (18:56:22): poll TIMEOUT — R3's report not yet written; artifact bytes already stable and complete.
- 18:56:26 (V07's poll) / observed by me at 18:57:09: `R3-freeze-hardening.md` landed. My battery had run 18:56:06 against the same final sha256s.

## Before-state evidence (pre-r97 tool, all read-only on the real tree)

Tool bytes: `a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980` — byte-identical to committed
`f3e09f9` (`git show f3e09f9:corpus/tools/dependency_freeze.py | sha256sum` → same; snapshot `V45-scratch/tool-pre-r97.py`).

- **B-A** byte-identical shadow of r96 at a foreign path verified IDENTICALLY:
  `python3 corpus/tools/dependency_freeze.py .ufo/.../V45-scratch/shadow/r96-crossing-response` →
  `FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1` / `DIGEST d422a9b3…` /
  `RESULT PASS`, exit 0.
- **B-B** DIGEST-MISMATCH did not name the file: shadow with `sources.json` re-indented (parsed-equal: True) →
  `FINDING DIGEST-MISMATCH: content digest e6e64779… != pin d422a9b3…; fixture bytes changed outside the frozen inventory`, exit 2 — no file name.
- **B-C** `--freeze` had no scope guard (scratch fakerepo `fakerepo-old/`, no real bytes touched):
  `--freeze fakerepo-old/elsewhere/r95-crossing-aftermath` → `FROZEN …` / `RESULT PASS`, exit 0, and the pin's
  `fixture` was rewritten to `elsewhere/r95-crossing-aftermath`.

## After-state demos (delivered tool `b06275f3…` / contract `27273be2…`)

Shadow fixtures: byte-identical (`cp -a`, `diff -r` clean, checked in battery) copies of r96-crossing-response and
r88-m3-maya-cluster at foreign paths under `V45-scratch/shadow/`. Independent of V09 (r95) and V07 (r94 staged).

| # | Probe | Observed | Exit |
|---|---|---|---|
| A2 | real r96 / real r88 (controls) | `RESULT PASS` both, digests `d422a9b3…` / `15ef230e…` | 0 / 0 |
| A1 | shadow r96 (byte-identical, foreign) | `FINDING PATH-MISMATCH: pin r96-crossing-response names corpus/fixtures/r96-crossing-response (resolves to …/corpus/fixtures/r96-crossing-response); invoked fixture resolves to …/V45-scratch/shadow/r96-crossing-response` | 2 |
| A1 | shadow r88 (byte-identical, foreign) | same class, names both resolved paths | 2 |
| A7 | tampered foreign copy (sources.json re-indent, parsed-equal) | `PATH-MISMATCH` — binding precedes semantic/digest checks (order evidence) | 2 |
| A6 | symlink → real fixture | `RESULT PASS` (binding is resolve-based) | 0 |
| A6 | symlink → foreign shadow | `PATH-MISMATCH` (resolves to shadow) | 2 |
| A8 | renamed copy at foreign path (`r96-crossing-response-renamed`) | `UNPINNED-FIXTURE` (name lookup precedes binding; non-regression) | 2 |
| A3 | `--freeze` shadow r96 / shadow r88 (real tree) | `SCOPE-REFUSED` both; contract sha256 `27273be2…` unchanged before/after the two probes | 2 / 2 |

Freeze-guard edges (scratch fakerepo `fakerepo-new/`, mirror of tool+contract+fixtures; real contract never touched):

| # | Probe | Observed | Exit |
|---|---|---|---|
| E1 | `--freeze` same-name elsewhere INSIDE scope (`corpus/fixtures/elsewhere/r95-crossing-aftermath`) | `SCOPE-REFUSED: … pin r95-crossing-aftermath already names 'corpus/fixtures/r95-crossing-aftermath'; freezing a same-named path elsewhere would rewrite the delivered pin` | 2 |
| E2 | `--freeze` scope root itself | `SCOPE-REFUSED: --freeze refuses corpus/fixtures itself; the frozen scope is corpus/fixtures/**` | 2 |
| E3 | `--freeze` new-name in-scope fixture (`r95-copy-new`) | accepted: `FROZEN r95-copy-new … RESULT PASS`; new pin `('r95-copy-new', 'corpus/fixtures/r95-copy-new')` | 0 |
| E4 | `--freeze` symlink inside scope pointing to `/etc` | `SCOPE-REFUSED: … (resolves to /etc); the frozen scope is corpus/fixtures/**` | 2 |
| A4 | `--freeze` in-scope (fakerepo) acceptance | `FROZEN r95-crossing-aftermath … RESULT PASS` | 0 |
| A5 | fakerepo fixture with single-file byte change (`sources.json` re-indent, parsed-equal) | `FINDING DIGEST-MISMATCH: content digest 9bb5b786… != pin d541ae64…; changed: sources.json (sha256 fd9e30e8… -> 107520e7…); fixture bytes changed outside the frozen inventory` — **names the changed file** | 2 |

- Self-test: `SELF-TEST 16/16` / `RESULT PASS`, exit 0; new cases `scope_refused` → `['SCOPE-REFUSED']` and
  `path_mismatch` → `['PATH-MISMATCH']` both ok; contract `self_test.expected` has exactly 16 entries (checked).
- Chain 4/4 clean: r88 `15ef230e…`, r94 `2527beb9…`, r95 `d541ae64…`, r96 `d422a9b3…`, all `RESULT PASS` exit 0.

## Contract / re-freeze verification (independent of R3's prose)

- `git diff` on the contract: semantic additions are exactly the two `self_test.expected` entries
  (`scope_refused`, `path_mismatch`) + a provenance note; pins count 4→4.
- r96 pin: `revision` `60dba0c2aa344860b10a2fc63e00468d1b134f27` → `2393934237ea076366f3db6dceeff033edb52ab1`
  (current HEAD); `fixture`, `content_sha256` (`d422a9b3…`), `files`, `events`, `relations`, `counts` unchanged.
  r88/r94/r95 pins untouched (revision still `60dba0c2…`). Top-level `revision` → `2393934…`.
- Measured: R4's cosmetic repair touched only `claim-excerpt-map.md` (not a `DATA_FILES` entry), so the digest did
  not move — the refresh is a revision/format refresh through the guarded `--freeze` path, as R3's report also
  records. The whole file was reindented (indent 1→2) by the tool's writer; documented in the contract's
  provenance note. This is content-preserving; no semantic field beyond the listed ones changed.

## R3 report comparison (`R3-freeze-hardening.md`, landed 18:57)

- Delivered sha256s in R3's report match my independently recorded ones exactly (`b06275f3…`, `27273be2…`).
- Every overlapping probe matches: old-tool `a3b57978…` shadow verifies exit 0 / delivered tool `PATH-MISMATCH`
  exit 2 (R3 on the r96-V38 r94 copy; me on fresh r96+r88 copies); no-write proof on `--freeze` refusal
  (R3 `8015e1f9…` unchanged at their probe time; me `27273be2…` unchanged); same-name in-scope refusal +
  new-name acceptance; symlink-out refusal; DIGEST-MISMATCH naming (R3 `timeline.json`, me `sources.json`);
  self-test 16/16; chain 4/4; no stray scratch.
- R3's "recorded discrepancy" quotes a claim phrase "the digest changes by the repair". That phrase does not
  appear in the round declaration: `LOG.md:3009–3011` says only "…is re-frozen THROUGH the guarded `--freeze`
  path (pin refresh), demonstrating the guard end-to-end". I confirm R3's measured facts (digest unchanged,
  revision moved) but the declaration as written does not assert a digest change; the flag is a precision note
  against R3's own paraphrase, not a declaration contradiction.
- R3's residual (README `corpus/tools/README.md:175` still lists the three r97 hazards as open and says 14/14;
  R2-owned) is consistent with what I read on disk; it is an open doc-parity item for adjudication, not a
  deliverable defect.

## V07 comparison (`V07-c2-path-binding.md`, landed 18:56:26)

V07's report landed after my first write and is now compared directly. **No divergence on any overlapping probe:**

| Probe | V07 (r94 fixture) | V45 (r96 + r88 fixtures) | Agreement |
|---|---|---|---|
| Foreign byte-identical same-named copy | old tool `a3b57978…` exit 0 → delivered tool exit 2 `PATH-MISMATCH` naming both resolved paths | same flip on two fixtures | ✓ |
| Delivered path control | r94 `RESULT PASS` exit 0 | r96 + r88 `RESULT PASS` exit 0 | ✓ |
| Binding semantics | resolution-based (D: absolute / trailing-slash / `..` / bare-name spellings all PASS; H3 symlink alias to delivered fixture PASS) | A6 symlink→real PASS, symlink→foreign `PATH-MISMATCH` | ✓ complementary |
| Differently-named copy | `UNPINNED-FIXTURE` exit 2 | A8 `UNPINNED-FIXTURE` exit 2 | ✓ |
| Precedence | mutated foreign copy → `PATH-MISMATCH` before digest (I2) | tampered foreign copy → `PATH-MISMATCH` (A7) | ✓ |
| Chain / self-test | 4/4 clean; 16/16 | 4/4 clean; 16/16 | ✓ |
| Pin paths | all four repo-relative, canonical | contract inspection: same four paths | ✓ |
| r96 re-freeze | revision → `2393934…`, digest unchanged | independently measured identical | ✓ |
| Transient self-test scratch | one live dir observed, cleaned (18:57:33→18:58:06) | one live dir observed, cleaned; none persisted | ✓ |

V07 explicitly deferred the scope-guard internals, `DIGEST-MISMATCH` naming, and self-test harness internals to other
seats; those are exactly this seat's battery (A3–A5, E1–E4), so the two seats are complementary halves of the C2
guard verification. Both bottom lines: PASS.

## Cross-seat context

V09 (`V09-c2-selftest.md`) independently reproduced the same two before-state hazards on r95 (foreign copy exit 0;
out-of-scope `--freeze` accepted) and reported the `/tmp` inode exhaustion; my baselines on r96/r88 and my
after-state battery agree with their harness observations (14/14 pre-change under TMPDIR redirect). Across V07
(r94), V09 (r95), and V45 (r96, r88), four of the four pinned fixtures were shadow-copy-probed independently.

## Bottom line

**PASS** — on the delivered revision (tool `b06275f3…`, contract `27273be2…`), every C2 guard behavior was
independently reproduced with fresh scratch: byte-identical same-named copies at foreign paths now exit 2
`PATH-MISMATCH` on two fixtures (r96, r88) while the real paths stay exit 0; `--freeze` refuses out-of-scope,
scope-root, same-named-in-scope, and symlink-out targets with exit 2 `SCOPE-REFUSED` and provably no contract
write; in-scope freeze acceptance and new-name pinning work (exit 0); `DIGEST-MISMATCH` names the changed file
with before/after sha256; self-test 16/16; chain 4/4; r96 re-frozen through the guarded path with only the pin
revision moving. R3's report matches all my measurements; V07's independent battery (r94 fixture) agrees on every
overlapping probe with no divergence.
