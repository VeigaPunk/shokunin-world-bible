# V17 — verdict-freshness (round 102, capstone)

Seat: V17, lane lore, model zai-coding-plan/glm-5.3-flash-low. Mandate: Read C2/U2 seats; one FRESHNESS verdict (final sweep) with bounds. Baseline read: HEAD `8fa2e87` ("lore r102: declare capstone round before dispatch"), parent `60e88bf`, `542021a` — matches the declared r101-closure baseline.

## Verdict

**ABSENT — the C3 deliverable never landed.** After the full poll-wait protocol (40 tries × 20 s ≈ 13.3 min, 06:19:30–06:32:50 -03:00), none of the three r102 artifacts and neither the U2 producer report nor the C2 seat report existed. There is no final sweep to verdict; per protocol a plan is never verified. Transcript (verbatim from the poll loop's log):

```
try 1: artifacts=0/3 U2=0 C2=0 seat_md=0
...
try 9: artifacts=0/3 U2=0 C2=0 seat_md=1
...
try 19: artifacts=0/3 U2=0 C2=0 seat_md=2
...
try 40: artifacts=0/3 U2=0 C2=0 seat_md=2
POLL-EXHAUSTED after 40 tries
```

Final confirmation at report time:

```
$ ls corpus/knowledge/ | grep r102            → (no output)
$ ls corpus/knowledge/r102-* | wc -l          → 0
$ ls .ufo/waves/round-102/seats/*.md          → V11-gates.md, V13-doc.md  (no U2-*, no C2-*)
$ date -Iseconds                              → 2026-10-18T06:35:13-03:00
```

What was awaited: `corpus/knowledge/r102-freshness-sweep.md` (C3), `corpus/knowledge/r102-push-synthesis-r95-r102.md` + `corpus/knowledge/r102-debt-ledger.json` (U1, readiness over-conditions), `seats/U2-*.md`, `seats/C2-*.md`. Two verifier reports (V11, V13) landed mid-wait; producers did not. ENDGAME CONVENTION: this is a bounded stall-escape — recorded, not fatal to the round; producers may land after this report's cutoff and the integrator should re-poll.

## Independent freshness ground truth (read-only, delivered revision HEAD `8fa2e87`)

`git status --porcelain corpus/` → empty: every delivered knowledge byte equals its committed state. What I could measure of freshness **all held** — no stale pin found in the delivered tree:

- **Tool pins reproduce byte-exact** (`sha256sum`, lane root):
  - `corpus/fixtures/check_bible.py` → `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` — matches the pin cited 22× across knowledge notes and the r101 LOG "checker pin `ff9fd2aa…` reproduced" claim.
  - `corpus/tools/support_check.py` → `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c` ✓
  - `corpus/tools/map_obligations.py` → `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9` ✓ (matches the r97-current revision named in the r95/r96 round-98 correction addenda).
- **Census reproduces**: `find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l` → `174`, matching the r100 note's `CENSUS 174` (173 at r99 + one fixture).
- **C9 re-check 11 evidence reproduces** (the watch's due-r102 item, `corpus/knowledge/r91-c9-watch.md:367`: "Next re-check: r102"):
  - `python3 corpus/tools/discriminate_check.py` → `RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression`, exit 0, `matches_pin=True`, both fixtures `pinned_semantic_gate=PASS`.
  - `python3 corpus/tools/discriminate_check.py --checker e97613c` → `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present`, exit 2 (expected control), `pinned_semantic_gate=FAIL` on both.
  - Whatever the sweep claims for C9 must equal exactly this outcome, filed as a dated "eleventh re-check" section + table row in r91-c9-watch.md per the file's established per-closure format.
- **SHONEN.md**: exactly four `[~]`, no `[x]` (direct read, 12 lines) — matches the LOG's "SHONEN unchanged" claim.
- **Git-valid tokens**: of 104 distinct SHA-like tokens in `corpus/knowledge/*.md`, 17 resolve as git objects — all 17 as **commits** (`git cat-file -t`, e.g. `03c6746`, `1b09f3f`, `28706dc`, `2b48ca7`, `2ea9ef1`, `396c568`, `4265df5`, `5eb9451`, `a7c6a17`, `ca7f9ef`, `dcb2d92`, `e97613c` + 5 full-length forms). Existence-level freshness holds for every git-resolvable citation.
- **Addendum-scope instructions live**: r95/r96 notes carry dated round-98 S5 correction addenda with the instruction "on the next touch of this note, re-derive all three receipts and re-measure the tool revisions before citing them". Any r102 touch of those notes must honor this; the receipts themselves remain fresh per the sha256sums above.

## Bounds (what this verdict does NOT establish)

1. **The final sweep's own claims are unverified** — the artifact does not exist. My checks bound the *delivered tree*, not the sweep. C3 remains unproven.
2. **Coverage surface undefined**: 87/104 SHA-like tokens are receipt-style hashes, not git objects (e.g. tool/scratch digests). "Every SHA-like token and receipt claim re-verified against delivered bytes" is only falsifiable by re-deriving each receipt; I re-derived 4 (three tool digests + census). The other 83 are unverified by this seat.
3. **`lane_rounds.lore == 102` is closure-time**: root `MANIFEST.json` read mid-wave shows `rounds[]: 214, last = round 101 closure, lane_rounds.lore {'lore': 101}, admitted: True`. The capstone claim is prospective; no wave seat can verify it before the closure commit (none of us may commit). Not a defect — a sequencing bound.
4. **Mid-wave snapshot**: producers landing after 06:35:13-03:00 invalidate the ABSENT count; the poll transcript above is the evidence of record for the window. Re-verification is a single `ls corpus/knowledge/ | grep r102` away.
5. **Roster arithmetic discrepancy (observed, not my axis)**: my dispatch says "20 seats: 2 producers + 18 verifiers, roster U1–U2 + V01–V19" — that is 21 rows; LOG.md's declaration says "U1–U2, V01–V18" (20). Same class as the r100/r101 roster errata; flagged for the integrator's count work.
6. C2/U2 seats were never read — they do not exist. The mandate's "Read C2/U2 seats" is discharged as not-yet-possible, evidence above.

## Bottom line

**ABSENT — r102-freshness-sweep.md, U2 and C2 reports did not exist after the full 40-try poll; no FRESHNESS verdict on the final sweep is possible.** Everything measurable on the delivered tree was fresh: 3/3 tool pins byte-exact, census 174, C9 pair HELD/exit-2-control, 17/17 git tokens resolve, SHONEN four-`[~]` — the sweep, when it lands, starts from a tree with no staleness this seat could find.
