# JCAL1 — Census judge #1, lore round-91 follow-up (world-bible lane)

Seat: JCAL1. Judged tree: **delivered** HEAD `c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7`
(`git status --porcelain` empty at seat start), baseline `a7c6a1773d5994246a76e4eff30d645f161920e0`.
Python 3.14.x. All scratch lived under `/dev/shm` (`/tmp` was at 100% inode use: `IFree 1705`;
this seat performed no `/tmp` writes). The only repo writes are
`.ufo/waves/round-91/followup/JCAL1.md` and `JCAL1-delta.json`.

**Verdict recommendation for calibration: improved (bounded).** The census claim is confirmed
exactly — 0 changed + 2 new of 166, 0 exit flips, 0 stderr changes, 164/164 common tuples
byte-stable — and both new fixtures discriminate the repaired lines against `e97613c` exactly
as declared, with the C9 watch block reproducing its pinned hash and outputs.

## Work performed

1. **Tree and checker identity.** Verified HEAD and clean state, then: delivered checker
   `sha256sum corpus/fixtures/check_bible.py` → `ff9fd2aa…`; `git show a7c6a17:corpus/fixtures/check_bible.py | sha256sum`
   → same `ff9fd2aa…`; `git diff a7c6a17..c2ab3d0 -- corpus/fixtures/check_bible.py | wc -c` → `0`.
   The r91 checker is **byte-identical to the baseline checker** (the "UNCHANGED (ff9fd2aa)"
   claim holds); `e97613c` extracts to `e2bb9639…`.
2. **Baseline receipts cross-check.** `.ufo/waves/round-91/patches/B1-tuples.json`
   (sha256 `5433f6af…`, 164 rows) and `B2-tuples.json` (sha256 `920defff…`, 164 rows) are
   field-identical on all 164 rows (`exit`, `stdout_sha256`, `violation_count`) — a
   double-receipt baseline anchor.
3. **Full delivered census.** All 166 direct child dirs of `corpus/fixtures`, each invoked as
   `python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<dir>` from the repo root, capturing
   exit / stdout SHA-256 / `VIOLATION:` count / stderr. Run **twice** for determinism.
4. **Delta vs baseline.** Field-level diff of the delivered census against both B1 and B2.
5. **Independent baseline regeneration.** `git archive a7c6a17 corpus/fixtures | tar -x -C /dev/shm/jcal1-r91-base-full`,
   then the extracted baseline checker over all 164 extracted dirs with cwd = extracted root and
   relative fixture paths — a direct before/after anchor that does not trust any receipt.
6. **Change investigation.** `git diff --name-status a7c6a17..c2ab3d0 -- corpus/fixtures/` to
   enumerate every content change; code read of `check_bible.py` input surface; and an
   A/B run of the delivered checker on **baseline-content copies** of every dir whose content changed.
7. **Discrimination spot-check** on the two added fixtures: delivered checker vs the extracted
   `e97613c` checker, with line-level classification of every difference.
8. **C9 watch reproduction**: ran the `corpus/knowledge/r91-c9-watch.md` block verbatim.
9. **Wait protocol**: two timestamped dependency checks 60 s apart on
   `.ufo/waves/round-91/followup/`.
10. **Sibling corroboration** (corroboration only, not verdict evidence): read `H4-census.json`
    and `JCAL5-delta.json` after my own measurements were complete.

## Before → after measurements

### Census (delivered vs baseline)

```text
command=python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<dir>  (cwd=repo root; 166 subprocesses per pass)
fixture_dir_count=166
pass1_seconds=4.0 pass2_seconds=4.0
determinism_identical= True
head_stats= {"dirs": 166, "exit_counts": {"1": 134, "0": 32}, "total_violations": 421, "stderr_nonempty": 0}
common= 164 added= ['corpus/fixtures/r91-c1-null-chain', 'corpus/fixtures/r91-c1-tick-unresolved'] gone= []
changed_vs_B1= []
exit_flips= []
changed_vs_B2= []
```

| | baseline `a7c6a17` (B1/B2, 164 dirs) | delivered `c2ab3d0` (166 dirs) |
|---|---|---|
| exit 0 / exit 1 | 32 / 132 | 32 / 134 |
| violation lines | 417 | 421 |
| stderr nonempty | 0 | 0 |
| changed tuples | — | **0** |
| exit flips | — | **0** |
| added / removed | — | **2 / 0** |

Arithmetic reconciles exactly: +2 dirs, +2 exit-1 dirs, +4 violations = +1 (`r91-c1-null-chain`)
+ 3 (`r91-c1-tick-unresolved`).

Added-dir tuples (full stdout in `JCAL1-delta.json`):

```text
corpus/fixtures/r91-c1-null-chain      exit 1, sha256 615dc0564f531352a574ef2f53c48be42f4e53ad1fac4aa88756e4bba2fada5b, 1 violation
corpus/fixtures/r91-c1-tick-unresolved exit 1, sha256 d754e96f7c01e6fb6eff12168a732d5a6125f428a9207bd74fc49bbdcbb25d88, 3 violations
```

Both dirs were added by work commit `6332115` (`git log --diff-filter=A`).

### Independent baseline regeneration (control)

```text
baseline_dirs_extracted= 164
baseline_checker_sha256= ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
corrected_control dirs= 164 counts= {1: 132, 0: 32} violations= 417
corrected_vs_B1= 0 vs_B2= 0 vs_delivered_census= 0 exit_flips= 0 []
```

The first control pass (absolute `/dev/shm` paths) reported 5 mismatches — `r5-missing-file`,
`r62-missing`, `r67-claim-source-unavailable-control/-empty/-whitespace` — and I investigated
each rather than dismissing it: the checker's `cannot load JSON` message embeds the directory
argument **verbatim**, so fixtures with deliberately missing section files emit path-dependent
stdout:

```text
rel path:  VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r67-claim-source-unavailable-control/sources.json'
abs path:  VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: '/dev/shm/jcal1-r91-base-full/corpus/fixtures/r67-claim-source-unavailable-control/sources.json'
r5-missing-file stdout sha256: relative 430d8efb9e124261fbfadb4a2b2a7295bcb9385316e994c012c2f03e3dbf8755 vs absolute b48909c5b4ed22509ecac9a24520f57da26437fece7214f540a7755bc67ef22d
```

Rerun with the in-force convention (relative paths; identical string regardless of cwd root)
gives **0 mismatches** against B1, B2, and the delivered census. Exits and violation counts are
path-invariant; only stdout bytes of those 5 fixtures move. B1, B2 and this census all used the
relative convention, so all three agree.

### Change investigation — every content change since baseline

```text
M corpus/fixtures/r87-myth-cluster/claim-excerpt-map.md
M corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md
M corpus/fixtures/r89-inspiration-paraphrase/claim-to-excerpt-map.md
A corpus/fixtures/r91-c1-null-chain/ (6 files: README + 5 section JSONs)
A corpus/fixtures/r91-c1-tick-unresolved/ (6 files: README + 5 section JSONs)
```

That is the complete content delta. The three modified files are map/prose markdown; the
checker's only input surface is the five section JSONs (`check_bible.py:43-47` iterates
`FIELDS` = sources/entities/relations/timeline/contradictions via `path.read_text`). Proved
empirically: delivered checker on **baseline-content copies** of all three dirs —

```text
corpus/fixtures/r87-myth-cluster        baseline_content_tuple=(0,afe570fcebf45fe3,0) head_tuple=(0,afe570fcebf45fe3,0) identical= True
corpus/fixtures/r88-m3-maya-cluster     baseline_content_tuple=(0,afe570fcebf45fe3,0) head_tuple=(0,afe570fcebf45fe3,0) identical= True
corpus/fixtures/r89-inspiration-paraphrase baseline_content_tuple=(0,afe570fcebf45fe3,0) head_tuple=(0,afe570fcebf45fe3,0) identical= True
```

For the other 161 common dirs the inputs are byte-identical across the range (git name-status)
and the checker is byte-identical, so outputs are identical by construction — and the corrected
baseline regeneration confirms it empirically 164/164. **No unexplained change exists.**

### Discrimination of the two added fixtures (delivered vs `e97613c`)

`r91-c1-null-chain` — exactly one line differs (hedged → definite); footer identical:

```text
e97613c    VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)
delivered  VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None
```

`r91-c1-tick-unresolved` — exactly the tick line differs; the qualified chain-break line is
byte-for-byte unchanged (and `entities[1]` line identical):

```text
e97613c    VIOLATION: entities[4].provenance[1].tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); provenance tick 1 must be greater than previous tick 3
delivered  VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
```

Both runs exit 1, stderr empty, violation counts unchanged (1 and 3). Cross-receipt: my
delivered-run sha on `r91-c1-null-chain` (`615dc056…`) equals B3's pinned delivered scratch-probe
sha, and my `e97613c` run sha (`3a337ba4…`) equals B3's pinned `e97613c` probe sha — the durable
fixture reproduces the scratch probe byte-for-byte.

### C9 watch reproduction (block run verbatim)

```text
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None
1 violation(s); no canon changed
exit=1
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed
exit=1
```

Matches the watch's pinned hash, its one-violation null-chain expectation, and its
definite-tick-with-qualified-chain-break expectation. The watch's falsification trigger is
present (`r91-c9-watch.md` §Falsification trigger, four gates + probe).

### Wait protocol

```text
check=1 ts=2026-10-17T08:34:05-03:00 followup_md_receipts=0   (H4 json receipts landed just before)
check=2 ts=2026-10-17T08:35:05-03:00 followup_md_receipts=1   (H4.md, JCAL5-delta.json, H4-c1-discrimination.json)
POLL_TERMINAL: two 60s checks done; census dependency = committed tree at c2ab3d0 (already present)
```

The census depends only on the committed tree, which was present at seat start; no dependency
artifact was missing and no wait gap affected the measurements. Sibling receipts landed during
the checks and were read afterwards for corroboration: `H4-census.json` counts (166 dirs, 0
changed, 2 added, exits 0:32/1:134, violations 421, shared 164, removed 0, exit_changes 0) and
`JCAL5-delta.json` added-row stdout/hashes agree with my independent census.

### Seat-end state

```text
git diff --stat HEAD   -> empty (no tracked modifications)
git status --porcelain -> ?? .ufo/waves/round-91/followup/   (untracked wave area: sibling + my receipts)
```

## Findings & named debt

1. **The census claim is confirmed exactly.** 166 dirs = 164 common (0 changed, 0 exit flips,
   0 stderr changes, every tuple byte-identical) + 2 added; totals 417 → 421 violations,
   exits 32/132 → 32/134. No change required investigation beyond the closure of item 2 — and
   the one anomaly that did appear (item 4) was in my control method, not in the tree.
2. **No unexplained change.** The complete content delta is the three inert map-markdown edits
   plus the two new fixture dirs; inertness is proven by code read + A/B runs, and the direct
   baseline regeneration reproduces the delivered census 164/164 with zero mismatches.
3. **Both added fixtures are durable and discriminating on the delivered tree.** Each differs
   from `e97613c` on exactly the repaired line(s); the genuinely unresolved chain-break sibling
   line keeps its qualified wording verbatim. A silent revert of either gate now changes a
   census tuple, which is the declared C1 detectability property. B3's pinned shas coincide
   with my runs, and the C9 watch block reproduces.
4. **Named debt (new, evidence-integrity class, non-blocking): path-convention sensitivity.**
   For the five fixtures with deliberately missing section files, stdout (hence its sha) depends
   on the directory string passed to the checker, because `cannot load JSON` echoes the path.
   The in-force convention (relative `corpus/fixtures/<dir>`; B1, B2, this census) is consistent
   across all three receipts. Any future census must keep it or it will report five spurious
   sha mismatches; exits and counts are invariant. Recorded with receipts in `JCAL1-delta.json`
   → `path_convention_finding`.
5. **Observation (doc-parity class, outside this seat's axis and write surface).**
   `grep -n "r91" corpus/fixtures/README.md` returns nothing; the r91 fixtures carry their own
   in-directory READMEs (with pinned per-checker expected outputs) but no top-level index row —
   the same class r90 JCAL1 named. Not a calibration harm; recorded for the closure record.
6. **Bounds of this verdict.** This seat judged the census/delta, the two durable fixtures'
   discrimination, the checker-identity claim, and the C9 block reproduction. C2 coverage and
   C3 depth are sibling lanes and were not judged here; the wider C9 governance (falsification
   trigger adequacy) is a sibling lane. No blocking finding was found.

## Handoff

- `.ufo/waves/round-91/followup/JCAL1.md` — this report.
- `.ufo/waves/round-91/followup/JCAL1-delta.json` — machine-readable receipt: full 166-row
  delivered census, added-dir tuples + stdout, delta vs B1/B2, corrected baseline regeneration
  (plus the first-pass artifact and path-convention finding), content-delta investigation,
  discrimination records, C9 reproduction, wait protocol, sibling corroboration, verdict block.
- **Verdict to rule at closure: calibration — improved (bounded).** Bounded by finding 6;
  named debt from finding 4; observation from finding 5.
- **Blocking findings: none.** The freeze holds (checker byte-identical baseline→delivered);
  the only census movement is the two declared fixtures.
- Reproduce the central receipt (cwd repository root):

  ```sh
  sha256sum corpus/fixtures/check_bible.py
  python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
  python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
  ```

  Observed: pinned hash printed; null-chain reports the definite `got None` chain break (exit 1,
  1 violation); tick-unresolved reports the definite tick line with the qualified chain-break
  line retained (exit 1, 3 violations).
- No commit and no push were made. Repo writes were limited to the two files above; scratch
  (`/dev/shm/jcal1-r91-*`) was removed after the receipts were captured.