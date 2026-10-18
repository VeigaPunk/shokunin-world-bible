# V22 — verdict-freshness (round 101)

Seat: V22, one FRESHNESS verdict. Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`.
Baseline: r101 declaration `ebec6bb` (2026-10-17T23:59:55-03:00), tree clean at declaration.
Freshness window: artifacts claiming r101 work must postdate the declaration timestamp.

## Baseline captured before producers landed

Working tree clean at declaration (`git status --short` → only unrelated
round-98 scratch `?? .ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md`).

Blob anchors at baseline (`git rev-parse HEAD:<f>` == `git hash-object <f>`, all four clean):

| file | baseline blob |
|---|---|
| `corpus/tools/dependency_freeze.py` | `ac590a83445a337049d8302bc52121b1116b83fc` |
| `corpus/tools/dependency-freeze-contract.json` | `936a2082e134b9d84d64b849417c3c6dbc26d600` |
| `corpus/tools/README.md` | `309341ba810de097352e1016168110c738352782` |
| `SKILL.md` | `27b9b6ff201c0e191777087e58fac2fb14f9891d` |

- `corpus/knowledge/r101-r10-register-first-entry.md`: **ABSENT at baseline** (checked
  before any producer write). Whatever lands there is provably a fresh, new file.
- Baseline pins chain (contract `pins` keys): `['r88-m3-maya-cluster',
  'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response',
  'r97-crossing-acknowledgment', 'r98-clerk-filing', 'r99-window-lapse']` — 7 fixtures,
  no `r100-docket-review`. C1 claims this grows to 8.
- Baseline self-test, run from lane root at 00:02 (-03), before any producer write:
  `python3 corpus/tools/dependency_freeze.py --self-test` →
  `SELF-TEST 18/18` / `RESULT PASS` / `EXIT=0`. Matches C3's claimed 18→19 delta
  (19 cases after the round, one new).
- Baseline `--freeze` semantics: `parser.add_argument("--freeze", metavar="DIR", ...)` —
  freeze accepts any DIR (guard claimed for r101 must appear in the diff).
- Target fixture exists: `corpus/fixtures/r100-docket-review/` present with the full
  file set (frozen in r100, predates this round).

## Freshness checks (delivered state)

Poll sequence 1 (20s × 40 tries, 00:02:56→00:15:56): C1 tool + contract landed at
try 17 (00:08:16) and stable since try 18. Poll sequence 2 (bounded stall-escape,
recorded not fatal — wave demonstrably mid-flight at the 40-try boundary: U1
delivered, fresh V-scratch dirs appearing through 00:11) continues for the
remaining pieces. Note: sequence-1's `U1rep` marker was a poller defect — it
matched U1's scratch *directory* (`U1-chain-eight-scratch/`), not a report file;
corrected in sequence 2 to match `U1*.md`/`U2*.md` files only.

### AX-F-TOOL — `corpus/tools/dependency_freeze.py` change is fresh and scoped

`git diff HEAD -- corpus/tools/dependency_freeze.py` = 43 lines, exactly three
changes: (1) module docstring paragraph "Round-101 hardening: the self-test grew
18 -> 19 with `repointed_edge` …"; (2) `"repointed_edge"` appended to
`FROZEN_CASES`; (3) the `repointed_edge` case builder in `self_test_cases()`
(repoints `aftermath-missing-evin` from `paired-crossing-decision` to
`aru-ninth-bell`, tick 9 < 11, expecting exit 1). No `--freeze` guard code was
changed this round — the guard (`scope_guard`, `SCOPE-REFUSED` same-name-path
refusal, `FILE-MISSING` refusal in `freeze()`, line ~401) is pre-existing r100
code that C1 *uses* for the pin, matching the declared ownership split
("guarded `--freeze` for the pin; direct edit for the self-test case").

### AX-F-CONTRACT — `dependency-freeze-contract.json` diff is exactly as disclosed

`git diff HEAD` = 168 lines, 2 hunks only:
1. top-level `revision`: `b5fe4729…` → `ebec6bb…` (the writer-managed refresh,
   disclosed as excepted in C1; note it now names the round's own HEAD);
2. one pure addition block (`@@ -677,6 +677,139 @@`): the `r100-docket-review`
   pin (10 pinned files, `content_sha256 77debadf…`, `revision ebec6bb…`) plus
   `self_test.expected.repointed_edge = {"exit": 1, "finding_ids":
   ["ADDITION-DETECTED", "REDUCTION-DETECTED"], "forbid_traceback": true}`.
No other pin's fields touched (python re-read: pins 7 → 8 keys, only
`r100-docket-review` added; expected cases 18 → 19).

### AX-F-C3 — delivered gate runs fresh: 19/19, both findings in one run

`python3 corpus/tools/dependency_freeze.py --self-test` (delivered state):
`CASE repointed_edge: exit=1 expected=1 findings=['ADDITION-DETECTED',
'REDUCTION-DETECTED'] ok` → `SELF-TEST 19/19` / `RESULT PASS` / `EXIT=0`.
Baseline before producer writes was `SELF-TEST 18/18` / `RESULT PASS` /
`EXIT=0` — the 18→19 delta is real, new, and behaves as C3 claims.

### AX-F-C1 — 8/8 chain verifies clean in the delivered state

`python3 corpus/tools/dependency_freeze.py corpus/fixtures/<f>` for all eight —
`r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath
r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing
r99-window-lapse r100-docket-review` — every one `exit=0 … RESULT PASS`
(digests witnessed; r100-docket-review `DIGEST 77debadf…` matches the new pin).
The chain was 7 at baseline; the eighth link is new in this round.

### AX-F-C2 — the knowledge entry is a fresh, new file; its receipts reproduce

`corpus/knowledge/r101-r10-register-first-entry.md` was **absent at baseline**
(checked before any producer write) and landed at mtime `2026-10-18
00:20:29 -03` — inside the window, as a new untracked file (`git status`:
`?? corpus/knowledge/r101-r10-register-first-entry.md`). Freshness markers
in the bytes: `verified-at: 2026-10-18T00:18-03:00`, "Receipts (measured
2026-10-18T00:18-03:00)", citations to the round-101 declaration's C2, and a
byte-identity chain that *includes* `r100-docket-review` — i.e. it describes
the round's own fresh 8-pin world, not a stale 7-pin one. Independent
corroboration of its core receipt, re-run by this seat from the lane root:
`sha256sum corpus/fixtures/<7 arc fixtures>/relations.json` → all seven
`c279254bc7de0636…`, `wc -c` = 139 bytes — exactly as the entry records.
Stronger still: that prefix is byte-identical to the `relations.json`
per-file hash inside the *new* contract pin
(`c279254bc7de0636d91823b6…c4a6ff9`) — the fresh knowledge entry and the
fresh pin agree on the same delivered bytes.

### AX-F-DOCS — README + SKILL.md updates are fresh and dated

Landed 00:20:30 and 00:20:06 respectively. `git diff HEAD` shows only:
tools README new "Round-101 addendum … (2026-10-18)" with dated supersession
of the seven-fixture wording; SKILL.md freeze row → eight-fixture chain,
"19 cases (… r101 added `repointed_edge` …)", "verifying 8/8 clean", "The
seven inherited pins retain every field from r100 closure `6f86bf2`", and a
new "dated supersession (2026-10-18, round 101)" bullet (the r100 bullet kept
as history). Counts move 18→19 and 7→8 exactly as claimed.

### Timing witness (all mtimes vs declaration 2026-10-17T23:59:55-03:00)

| file | mtime (-03) | fresh? |
|---|---|---|
| `corpus/tools/dependency_freeze.py` | 00:07:59 | yes |
| `corpus/tools/dependency-freeze-contract.json` | 00:08:32 | yes |
| `SKILL.md` | 00:20:06 | yes |
| `corpus/knowledge/r101-r10-register-first-entry.md` | 00:20:29 | yes |
| `corpus/tools/README.md` | 00:20:30 | yes |
| `seats/U1-chain-eight.md` | 00:21:40 | yes |

### Scope witness (nothing stale re-presented, nothing foreign mutated)

Final `git status --short`: exactly `M` on the four U1-owned files, `??` on
the U2 knowledge file, `?? .ufo/waves/round-101/` (wave reports/scratch),
`?? .scratch/` (V02 + v26 per-seat scratch at lane root, witnessed as
round-101 activity, not lane-content mutation), and the pre-existing
round-98 scratch note. The seven inherited pins' digests reproduce their
r99/r100 values (verified in my 8/8 run) — no inherited state was re-frozen
or silently altered.

### Corrections and defects recorded against this seat's own process

- Interim note above said the contract diff was "2 hunks"; that was
  head-truncation of a grep, not the file. Actual: **3 hunks** (`@@ -32,7`,
  `@@ -677,6 +677,139 @@`, `@@ -806,6 +939,14 @@`), matching U1's report.
- Poll sequence 1's `U1rep` marker was a false positive (matched U1's scratch
  *directory*, not a report file); sequence 2 corrected this to match
  `U1*.md`/`U2*.md` files.
- Poll try=8 (00:05:16) saw a transient contract change that reverted by
  try=9 — producer mid-flight activity; the delivered contract has been
  stable since 00:08:32 and is the state verified above.
- Bounded stall-escape (recorded, not fatal): poll sequences totalled 70
  tries (~23.5 min, 00:02:56→00:25:22), one beyond the protocol's 40-try cap,
  justified at the boundary by witnessed in-flight wave activity (U1
  delivered; fresh V-scratch dirs appearing through 00:11).

### ABSENT item

**U2's seat report `.md` is ABSENT at poll exhaustion** (70 tries; last check
after 00:26). U2's *artifact* is delivered and fresh-verified above — but no
U2 producer report exists yet to corroborate it (U1's report took ~13.7 min
after its own artifact landed; U2 may still be writing). Per protocol this is
reported ABSENT rather than assumed; it bounds the C2 freshness verdict to the
artifact's own evidence (which is complete: absent-at-baseline → delivered
in-window → receipts reproduce).

## Verdict

**FRESHNESS: PASS** — every delivered r101 artifact is demonstrably fresh:
the C2 knowledge file did not exist at baseline and appeared in-window with
receipts that reproduce on the delivered tree; the C1 tool/contract changes
are in-window, scoped exactly to the claimed hunks (pin + case + disclosed
revision refresh; the `--freeze` guard is pre-existing r100 code that was
used, not modified), and the full gates run clean on the delivered bytes
(19/19 self-test with both findings on `repointed_edge`; 8/8 chain with the
seven inherited digests unchanged); docs are dated 2026-10-18 round 101 with
correct supersession. Nothing stale was re-presented as new work and no
inherited pin changed. The only absence is U2's seat report (artifact
delivered and fresh-verified regardless).

**Bottom line: PASS — all delivered r101 artifacts are fresh (baseline-absent
C2 file + in-window C1/C3 changes with reproducing receipts and unchanged
inherited pins); U2's seat report ABSENT at 70 poll tries (bounded escape,
artifact verified directly).**
