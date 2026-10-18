# JCAL1 — Calibration judge #1 (lore round-90 follow-up, world-bible lane)

Seat: JCAL1. Axis: **calibration (C1)**. Measured tree: `ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13`
(`HEAD`, `git diff --quiet HEAD --` exit 0, working tree clean at seat start), baseline `e97613cc276f5fa9cac49ff1900798cf6863c020`.

## Work performed

- Verified the delivered tree is clean and pinned at `ca7f9ef` before any measurement.
- Ran the **full delivered census**: all 164 direct child directories of `corpus/fixtures`, each invoked as `python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>` from the repository root, capturing exit status, SHA-256 of raw stdout, and violation count. `corpus/fixtures` holds exactly 164 dirs plus `README.md` and `check_bible.py`, so 164 is the complete delivered set.
- Diffed that census against the r90 baseline artifact `.ufo/waves/round-90/patches/B1-tuples.json` (160 dirs at `e97613c`), then investigated every non-matching row.
- **Independently replayed the baseline**: extracted the `e97613c` checker via `git archive` to scratch and ran it against the 160 common fixture directories of the *candidate* tree — 0 tuple mismatches, reproducing B1's artifact from the delivered tree.
- Ran the **freeze-then-verify** check (r88-I1): archived the baseline checker, applied `X2-c1-nullonly.patch` then `X3-c1-tickonly.patch` with default fuzz, and compared the resulting SHA-256 to the delivered checker.
- Built a five-case semantic probe matrix from `corpus/fixtures/r89-fn2-unresolved-chain-break` and ran every case through **both** the baseline checker and the delivered checker from one working directory, for a strict before/after wording comparison.
- Confirmed the four added fixtures behave as declared, checked the C1(iii) census-manifest claim, and re-ran the C2 support command as a no-collateral-harm control.
- Determinism guard: ran the full 164-dir census twice and compared.

Scratch note: `/tmp` was at 100% inode use for most of this run (`df -i /tmp` → `IUsed 1048576, IFree 0`), so probe scratch went to `/dev/shm` and the probe trees were deleted after capture. One leftover from the earlier baseline extraction remained at `/tmp/jcal1/corpus/fixtures/check_bible.py` from before exhaustion.

## Before → after measurements

### Freeze-then-verify (r88-I1) — PASS, no mismatches

```sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin
sha256sum corpus/fixtures/check_bible.py
mkdir -p /tmp/jcal1 && git archive e97613c corpus/fixtures/check_bible.py | tar -x -C /tmp/jcal1
cp /tmp/jcal1/corpus/fixtures/check_bible.py /tmp/jcal1/composed.py
patch -p1 --no-backup-if-mismatch /tmp/jcal1/composed.py < .ufo/waves/round-90/patches/X2-c1-nullonly.patch
patch -p1 --no-backup-if-mismatch /tmp/jcal1/composed.py < .ufo/waves/round-90/patches/X3-c1-tickonly.patch
sha256sum /tmp/jcal1/composed.py
```

Observed output:

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
patching file /tmp/jcal1/composed.py
X2_exit=0
patching file /tmp/jcal1/composed.py
Hunk #1 succeeded at 321 (offset 2 lines).
X3_exit=0
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  /tmp/jcal1/composed.py
```

**The delivered checker is byte-identical to X2+X3 composed on `e97613c`.** The X3 hunk offset of +2 lines is the expected consequence of X2 adding two lines earlier in the file, not a conflict. Delivered-vs-baseline checker diff: `1 file changed, 4 insertions(+), 11 deletions(-)`. No integrator amendment — the freeze contract holds and every probe below therefore applies to the shipped artifact.

### Full census at `ca7f9ef` (164 dirs)

Command template: `python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>` from the repository root.

```text
fixture_count=164 exit_counts={0: 32, 1: 132} total_violations=417 stderr_nonempty=0
```

Both before and after totals, side by side:

| | baseline `e97613c` (B1) | delivered `ca7f9ef` |
|---|---|---|
| dirs | 160 | 164 |
| exit 0 / exit 1 | 32 / 128 | 32 / 132 |
| violations | 399 | 417 |
| stderr nonempty | 0 | 0 |
| artifact sha256 | `80bdc3b4…a42ad` | live run |

### Delta vs `B1-tuples.json` — the claim is exact

```text
baseline_n=160 head_n=164 common=160 new=4 gone=0 changed=0
```

- **0 changed tuples** of the 160 common dirs — compared on all three fields (exit, stdout SHA-256, violation count). Not merely "same exit count": **no stdout byte changed** for any pre-existing fixture.
- **0 removed dirs.**
- **4 added dirs**, all exit 1: `r90-c1-rawpresent-from` (5 violations), `r90-c1-rawpresent-to` (5), `r90-c1-rawpresent-source` (4), `r90-c1-three-causes` (4).
- Violation arithmetic closes exactly: 417 − 399 = 18 = 5+5+4+4, all of it new-dir contribution; changed-dir net delta = 0.
- **0 exit flips.** No directory changed exit status in either direction; the four new tuples are additions, not flips.

I investigated the one plausible source of change and cleared it: the work commit edits `.md` files **inside** two census directories (`r87-myth-cluster`, `r88-m3-maya-cluster` gained `claim-excerpt-map.md` and excerpt mode lines). Both directories are in the census and both left the checker tuple byte-identical (`exit 0`, stdout `afe570fc…`, 0 violations). Root cause is structural: `check_bible.py` reads only `<section>.json` (sections: `sources`, `entities`, `relations`, `timeline`, `contradictions`), so no `.md` edit can move a tuple.

### Baseline replay — B1's artifact independently reproduced

```text
baseline_checker_on_head_160: fixture_count=160 exit_counts={0: 32, 1: 128} total_violations=399 mismatches=0
```

Running the **`e97613c` checker** over the 160 common dirs of the **delivered tree** gives 0 mismatches against `B1-tuples.json`. This proves two things at once: B1's baseline artifact is genuine, and the 160 common dirs' JSON content is unchanged between the two commits. B2's artifact is byte-identical to B1's (`80bdc3b4…`), so two independent baseline censuses agree and my replay agrees with both.

### Determinism guard — 2 runs, 0 differences

```text
content_diffs=0 over all 164 dirs (exit, stdout_sha256, violation_count)
```

### C1 semantics: before → after probe matrix

Probes were built from `corpus/fixtures/r89-fn2-unresolved-chain-break`, varying `f3-seal`'s provenance, with the ancillary section JSON symlinked. Every case ran under both checkers with identical input.

| case | before (`e97613c`) | after (`ca7f9ef`) | exit | required by claim |
|---|---|---|---|---|
| `chain-unresolved` (genuinely unresolved non-null holder) | qualified: `possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'` | **identical, character for character** | 1 → 1 | referential: must stay qualified — **PASS** |
| `tick-relevant-unresolved` | `…tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: expected from_holder 'f3-dup' …; provenance tick 1 must be greater than previous tick 3` | `…tick: provenance tick 1 must be greater than previous tick 3` | 1 → 1 | tick findings definite — **PASS** |
| `null-from-chain` | `possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)` | `provenance chain break; expected from_holder 'mira', got None` | 1 → 1 | null chains definite — **PASS** |
| `unrelated-duplicate-tick` (control) | `…provenance tick 1 must be greater than previous tick 3` | **identical** | 1 → 1 | no regression — **PASS** |
| `null-to-then-nonnull-from` (scope control) | record rejected upstream as `malformed record (invalid to_holder)` | **identical** | 1 → 1 | scope — **PASS** |

The last row is the scope control for the X2 null gate: a null `to_holder` never reaches the guard, because `to_holder` null is rejected earlier as `required nonempty entity id`. Combined with the call-site audit — `previous_holder` is assigned from `to_holder` and so is never null for a valid predecessor, and the third call site sits inside `elif from_holder is not None` — the only reachable null input is `from_holder`, which is explicitly legal (`required null or nonempty entity id`). **The guard covers exactly and only the reachable null input.**

### C1(iii) and collateral surfaces

- `r89-fn2-control` (exit 1, 1 violation) and `r89-fn2-unresolved-chain-break` (exit 1, 2 violations) are both rows of the census manifest. The qualification is now regression-visible — the r89 bound "FN-2 is invisible to the 149-dir manifest" is closed.
- C2 control (reproduced, not a C2 verdict): `python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster` → `SOURCE-SUPPORT 22/22; MODES 22/22`, `RESULT PASS`, exit 0; `…r88-m3-maya-cluster` → `SOURCE-SUPPORT 10/10; MODES 10/10`, `RESULT PASS`, exit 0.

## Findings & named debt

1. **Freeze-then-verify PASSES with no mismatch.** Delivered `corpus/fixtures/check_bible.py` = `ff9fd2aa…` = X2+X3 composed on `e97613c`. No blocking finding. Every piece of evidence in this report is evidence about the shipped artifact, not about a patch.
2. **The census claim is confirmed exactly as stated**: 164 dirs, 0 changed + 4 added of the 160-dir baseline, 0 removed, 0 exit flips. Nothing needed investigating after the two cluster directories were cleared — no unexplained change exists.
3. **Calibration improvement is real and correctly bounded.** Both named r89 hedged shapes are repaired on the delivered tree (vacuous null-holder clause gone; tick finding definite), and — the harder half — the repair does **not** over-correct: the genuinely unresolved non-null holder case keeps its exact previous qualified wording. The two directions are simultaneously satisfied on one artifact.
4. **No regression anywhere in the delivered graph**: not one stdout byte of any pre-existing fixture moved, exit counts held at 32/128 on the common set, stderr stayed empty, and two full sweeps agree. A repair that leaves the whole 160-dir census byte-stable is the strongest available no-harm evidence.
5. **Named debt — C9's ruling remains a ruling.** The integer-only tick reading is commissioned by C9's reasoning (tick order is an integer comparison), not by an observed case that distinguishes it from the X1 gate. My `tick-relevant-unresolved` probe confirms the delivered behavior matches the ruling; it does not show that tick order is the *only* right reading. Falsification path stays open for r91 as C9 named it: promote the losing X1 gate if a case emerges where a tick finding needed identity context. This is a bound on the axis, not a defect in the deliverable.
6. **Named debt — documentation-parity gap (recurrence of a r89-repaired class).** `corpus/fixtures/README.md` carries a per-round section for rounds 87, 88 and 89 listing that round's fixtures with commit hashes. There is **no round-90 section**, and `grep -n "r90-c1" corpus/fixtures/README.md` returns nothing, so the four new fixtures are indexed nowhere in the top-level fixture README. Each new fixture does carry its own in-directory `README.md`, matching the per-fixture pattern, so this is an index/parity gap rather than missing documentation. It does not harm the calibration axis — the calibration object is the checker's wording, which is verified above, and no calibration capability is lost — but r89's closure explicitly repaired doc-parity as a named harm, so its recurrence deserves recording. Fix is one paragraph in the delivered README at the r91 closure; it is a `corpus/` write and outside this seat's authorized surface.
7. **Observation — untracked repo artifacts from concurrent sibling seats, not from the delivered commands.** At seat start `git status --porcelain` was empty. Early in the run `corpus/tools/__pycache__/support_check.cpython-314.pyc` (mtime 06:56:12) appeared, coinciding with this seat's C2 control run. Running the delivered receipt as `__main__` does **not** produce it: I removed the directory, re-ran `support_check.py` alone, and observed `NOT_REAPPEARED`. It reappeared later in the run, alongside sibling follow-up artifacts landing in the same window (`H2-delta.json`, `H3-r90-mutations.json`, `H4-census.json`, `H4-probes.json`, `H4-lineage.json`, `JCAL2-receipts.json`, `JCAL5-delta.json`). Consistent explanation: sibling seats import `support_check` as a module. I removed the cache once as hygiene but left the second occurrence in place rather than racing concurrently-running seats over a regenerable bytecode directory. No tracked file is affected either way (`git diff --quiet HEAD --` and `git diff --cached --quiet` both exit 0 at seat end). Reported so the closure record does not mistake it for this seat's output.
8. **Verdict recommendation: calibration — `improved (bounded)`.** Improved on measured, freeze-verified evidence: both hedged shapes repaired, genuine uncertainty preserved verbatim, full census byte-stable, manifest visibility gained. Bounded by finding 5 (a ruling rather than a falsifying case) and finding 6 (doc-parity gap). Not `unchanged` — the two defects were real and are now provably gone; not unqualified `improved` — the tick reading's exclusivity is still an open, explicitly falsifiable question.

## Handoff

- `.ufo/waves/round-90/followup/JCAL1.md` — this report.
- `.ufo/waves/round-90/followup/JCAL1-delta.json` — machine-readable census, delta, freeze-then-verify record, probe matrix and verdict.
- **Blocking findings: none.** The r88-I1 freeze check matches; no mismatch to report.
- **Verdict to rule at closure: calibration `improved (bounded)`**, with the two named debts (C9 ruling open to r91 falsification; round-90 README parity row).
- Reproduce the two central receipts (cwd repository root):

  ```sh
  python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-fn2-control
  python3 corpus/fixtures/check_bible.py corpus/fixtures/r90-c1-rawpresent-from
  ```

  Observed: the first prints `provenance chain break; expected from_holder 'f3-dup', got 'mira'` and exits 1; the second prints the five raw-present/naming violations and exits 1.
- No commit, push, or tracked write was made by this seat. Repo writes were limited to the two files above; scratch lived under `/dev/shm` and `/tmp` and was removed (probe trees) or left as pre-existing (`/tmp/jcal1/corpus/fixtures/check_bible.py` baseline copy, 1 file).
