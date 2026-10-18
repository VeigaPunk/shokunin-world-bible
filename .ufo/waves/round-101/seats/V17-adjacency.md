# V17 — adjacency (2026-10-18)

Seat scope: PROVINCE byte-identity, write confinement, and rights/mechanics boundaries after production. Axes: charter preservation; lane confinement; producer byte-ownership separation; wave-mechanics hygiene. Baseline r100 closure `6f86bf2`; observed live HEAD `ebec6bb` (r101 declaration commit). This is a bounded adjacency verdict over the delivered tree — not round-wide admission and not a machine-wide filesystem audit. C1/C2/C3 content depth is other seats' scope; this seat judges only where bytes landed and what the province/machinery absorbed.

## Delivery prerequisite

Protocol poll (every 20 s, 40-try cap), artifacts = the five producer-owned byte targets, reports = `U1-*.md` and `U2-*.md` under `.ufo/waves/round-101/seats/`:

- **Poll 1** (40/40): exhausted at artifacts 2/5 (`corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json`), U1=none, U2=none. Recorded, not fatal.
- **STALL-ESCAPE-1** (bounded, 40 tries, try numbers 41–80): artifacts reached 5/5 at try 50, U1 report present from try 54, **U2 report absent through try 80**. Terminal state quoted from the poll log:

```text
escape1-try=80 artifacts=5/5 U1=.ufo/waves/round-101/seats/U1-chain-eight.md U2=none
=== final git status ===
 M SKILL.md
 M corpus/tools/README.md
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
?? .scratch/
?? .ufo/waves/round-101/
?? .ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md
?? corpus/knowledge/r101-r10-register-first-entry.md
```

- **STALL-ESCAPE-2** (bounded, 10 tries): `escape2-try=3 U2=.ufo/waves/round-101/seats/U2-r10-register.md 00:32:19` → `POLL_HIT`. Full delivery (5/5 artifacts + both producer reports) present. During escape-1's U2 window U2 was demonstrably active, not dead: `U2-scratch/` mtime 00:21, knowledge artifact written 00:31, report 00:32 — latency, not a violation. Both escapes are recorded above per the endgame convention; neither was fatal.

Both producer reports were read after readiness. U1 claims exactly its four owned writes plus declared scratch `U1-chain-eight-scratch/`; U2 claims exactly one authored file `corpus/knowledge/r101-r10-register-first-entry.md`. No plan was verified as implementation; the checks below ran on the delivered bytes. No poll was self-inclusive (globs matched `U1-*`/`U2-*` only; this report was written after all polls closed).

## 1. Province preservation — PASS

Actual read-only audit (declared scratch `V17-scratch/audit.py`, run from the lane root), terminal output on the fully delivered tree:

```text
PROVINCE_BASE_SHA256  94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
PROVINCE_HEAD_SHA256  94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
PROVINCE_WORK_SHA256  94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
PROVINCE_BYTE_IDENTICAL_VS_BASELINE True
PROVINCE_BYTE_IDENTICAL_VS_HEAD    True
GIT_DIFF_BASELINE_PROVINCE_EXIT 0
```

Baseline bytes were taken with `git show 6f86bf2:PROVINCE.md`; work-tree bytes with a direct file read; the SHA-256 triple above is exact-byte equality, not prose similarity. `PROVINCE.md` is also unchanged across `6f86bf2..ebec6bb` (the pre-round close + declaration commits), so the r100 closure value (`94a7a77e…`, the same digest r100's V22 recorded) still holds at r101's delivered tree. `PROVINCE.md`'s read-only siblings clause and no-real-world-rights clause needed no re-reading: the file did not move.

## 2. Write confinement — PASS, with two recorded mechanics notes

Method: `git diff --name-only HEAD` (tracked changes) and `git ls-files --others --exclude-standard` (untracked), classified against the producer byte-ownership sets from the round declaration. Terminal audit lines:

```text
TRACKED_CHANGES    ["corpus/tools/dependency-freeze-contract.json", "corpus/tools/dependency_freeze.py", "corpus/tools/README.md", "SKILL.md"]
UNAUTHORIZED_TRACKED []
OUTSIDE_RESOLUTIONS [".ufo/waves/round-101/seats/V04-scratch/baseline-tree/.ufo/waves/round-97/seats/R3-scratch/new-mirror/corpus/fixtures/evil-link", …V45-scratch…/evil-link, …V06-scratch…/evil-link]
SKILL_PREFIX_IDENTICAL True
SKILL_PREFIX_LEN_BASE_WORK 14677 14677
```

Every tracked delta is a U1-owned path. New untracked content outside `seats/` is exactly `corpus/knowledge/r101-r10-register-first-entry.md` (U2's owned file, 20,823 bytes) plus the pre-existing round-98 stray, which is byte-for-byte the same entry that predated the round — not a round-101 write. Delta shapes corroborate ownership claims: `git diff --numstat` → `4 3 SKILL.md`, `59 0 corpus/tools/README.md` (append-only), `142 1 dependency-freeze-contract.json`, `18 0 dependency_freeze.py` (append-only). SKILL edits live entirely inside the freeze section: the bytes before `### Dependency-edge freeze check` are baseline-identical (prefix check above) and the diff hunk is `@@ -93,10 +93,11 @@` — the freeze rows only (chain seven→eight, 18→19 cases, new dated-supersession row). No rights, permission, canon, or mechanics language appears outside that section.

Mechanics note 1 — `V04-scratch` holds ~78,800 untracked files (a full baseline-tree mirror for tamper probes), including three symlinks named `evil-link` → `/etc`. All are inside V04's own declared scratch area under `seats/`; a symlink creates no outside write. Recorded as observed, not adjudicated (V04's seat scope).

Mechanics note 2 — lane-root `.scratch/` holds 26 untracked files: seat scratch for V02 and a `v26` seat (fixture mirrors + a poll helper) placed at the repository root instead of under `.ufo/waves/round-101/seats/`. This is the undeclared-location variant of allowed per-seat scratch; `.gitignore` does not cover `.scratch/`, so it will surface in closure `git status` unless the convention is recorded or the directory ignored. No lane-owned content was touched by it.

One transient observation from poll 1: try 9 briefly counted 1/5 artifacts with no persistent trace by try 10 (a mid-write git-status race on an owned file). Not reproducible, no effect on any verdict.

## 3. Rights/mechanics scan — PASS

- **No commits, no pushes:** HEAD at close is still `ebec6bb` (`git log --oneline -1` → `ebec6bb lore r101: declare GLM 28-seat round before dispatch`); the wave tree is uncommitted exactly as the round requires.
- **Producer claims match observed bytes:** U1's "exactly these four `M`" and U2's single-authored-file claim each reproduce the tree state in section 2; neither claims, and the tree shows, no third write path.
- **Seat-report hygiene:** all round-101 seat output lives under `.ufo/waves/round-101/seats/` (16 reports + per-seat scratch dirs at close, including U1's and U2's declared scratch); no report or scratch escaped to another round's or lane's area. The heavy/hidden scratch variants noted in section 2 are location variance inside the seats area or the recorded `.scratch/` note — no cross-seat byte intrusion was found.
- **Province/machinery untouched beyond the freeze surface:** the only machinery bytes that changed are the freeze gate's own four owned files; `PROVINCE.md` section 1 shows zero drift.

## Bounds

Bounded to this lane's git-visible tree during the observed window (poll 1 start through terminal audit). Not verified here: C1/C2/C3 substantive correctness, V-seat verdict quality, anything outside the lane root, or post-report producer writes.

**Bottom line: PASS — PROVINCE byte-identical to baseline `6f86bf2`, all writes confined to the two producers' owned paths (plus recorded scratch-location variance), no commits; delivery completed during bounded escape-2 with U2's report at 00:32:19.**
