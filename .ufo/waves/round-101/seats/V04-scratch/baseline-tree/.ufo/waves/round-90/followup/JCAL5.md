# JCAL5 — calibration judge #5 (method-varied): freeze hash-match, regenerated baseline, 0+4 delta, determinism

## Work performed

- **Axes:** (1) C1 calibration — the shipped X2 null-gate + X3 integer-only tick-gating
  composition judged against the C9 ruling (null chains and tick findings definite;
  genuinely unresolved non-null holder chain-breaks qualified); (2) compatibility — the
  160-tuple/exit preservation claim; (3) reproducibility — a method deliberately varied
  from the work-wave seats: `git archive` tar as the delivered-tree source, `python3 -I`
  isolated subprocesses, memfd checker execution, shuffled seed 9001, and a baseline
  regenerated from the pinned e97613c git tree rather than any seat receipt.
- **Delivered-tree source:** `git archive --format=tar -o /tmp/jcal5/ca7f9ef.tar ca7f9ef`
  (sha256 `8f7c4fe07853112ccc251ad706033855282df00a45a30da9853002688efd211b`). All 860
  JSON-named tar members (820 under `corpus/fixtures`, 40 elsewhere) were hashed against
  disk (0 mismatches), so the disk fixture tree equals the archive; the delivered checker
  bytes come from the tar member. Scratch was limited to `/tmp/jcal5/` (one tar + two
  scripts + two patch-composition dirs) because `/tmp` was at 100% inode use.
- **Checker execution:** delivered and baseline checkers were written to `os.memfd_create`
  descriptors and run as `python3 -I /proc/self/fd/<fd> <fixture-dir>` with `pass_fds`,
  cwd repository root. `-I` ignores `PYTHONHASHSEED`, so each subprocess ran with its own
  random hash seed (verified: two `python3 -I -c 'print(hash("jcal5-seed-probe"))'` runs
  printed different values).
- **Commands run (each with observed output below):**
  - `python3 -I /tmp/jcal5/driver.py` (driver sha256 `3c4882ee3334a3497bebf1ff58b2ee681d762f736b949edf9ba6406c1436a86d`)
  - `python3 -I /tmp/jcal5/probe.py` (probe sha256 `1f81a24603988b8f7ffe3e76ff174ae03b445df0aef8015ccd15cfcaeb6dd6a0`)
  - `find corpus/fixtures -type f \( -name entities.json -o -name sources.json -o -name relations.json -o -name timeline.json -o -name contradictions.json \) -printf '%h\n' | sort -u | wc -l`
  - `sha256sum .ufo/waves/round-90/patches/B1-tuples.json .ufo/waves/round-90/patches/B2-tuples.json`
- One scope bug was found and fixed inside my own driver before the recorded run: the
  first pass enumerated JSON-bearing directories across the whole tar (173, including 9
  pre-existing `corpus/live/**` dirs). The declared census scope is *recursive
  `corpus/fixtures`*; the corrected run restricts to that prefix (164). The 9 out-of-scope
  dirs are listed in the receipt and were present in both revisions.

## Before → after measurements

### 1. Freeze-then-verify (r88-I1): PASS — no blocking finding

Composition of the two committed patches on the pinned baseline checker, in both
application orders (`patch -p1 --fuzz=0` in scratch), delivered tar member, and delivered
disk copy:

```text
baseline_checker_sha256=e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556
composed_X2X3_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
composed_X3X2_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
delivered_checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
match_delivered_equals_X2X3=True
match_delivered_equals_disk=True
```

The delivered checker is byte-identical to e97613c + X2 + X3, order-independent. The
baseline hash independently reproduces the hash X3 recorded (`e2bb9639…`).

### 2. Regenerated baseline vs the canonical receipts

Baseline regenerated from `git ls-tree` at e97613c + the e97613c checker, not from
B1's file:

```text
baseline_dirs_from_git_ls_tree=160
baseline_sorted_a: exit_counts={'0': 32, '1': 128}, violation_lines_total=399, stderr_nonempty=0
.ufo/waves/round-90/patches/B1-tuples.json: rows=160 matches=160 mismatches=0
.ufo/waves/round-90/patches/B2-tuples.json: rows=160 matches=160 mismatches=0
```

B1 and B2 are byte-equal (`80bdc3b45ea785ea7e04dea776d95da0bd6dad088f60ae95100f21039cae42ad`).
My regenerated baseline reproduces all 320 recorded rows under `python3 -I`.

### 3. The 0+4 delta, reproduced

```text
delivered_dirs_from_tar=164
added=['corpus/fixtures/r90-c1-rawpresent-from', 'corpus/fixtures/r90-c1-rawpresent-source',
       'corpus/fixtures/r90-c1-rawpresent-to', 'corpus/fixtures/r90-c1-three-causes']
removed=[]
unchanged_tuple_count=160
changed_tuple_count=0
exit_status_changes=[]
stderr_changes=[]
baseline=  {'directories': 160, 'exit_counts': {'0': 32, '1': 128}, 'violation_lines_total': 399, 'stderr_nonempty': 0}
delivered= {'directories': 164, 'exit_counts': {'0': 32, '1': 132}, 'violation_lines_total': 417, 'stderr_nonempty': 0}
```

Independent shell count: `find … | sort -u | wc -l` → `164`. New-fixture tuples (all
exit 1, stderr empty, violation lines): rawpresent-from 5, rawpresent-to 5,
rawpresent-source 4, three-causes 4. Their stdout shows the intended FN-1 raw-present
wording (`… 'x' present in raw entities but absent from the resolved index …`) for
to_holder / from_holder / source_id, and the three-causes record joins three causes in
one first-stop string (`malformed record (invalid tick); holder reference … absent from
raw entities and absent from the resolved index; source reference … absent from raw
sources and absent from the resolved index`).

### 4. Determinism

Seven full census runs: baseline sorted ×2 + shuffled seed 9001, delivered-on-160,
delivered ×2 + shuffled seed 9001. All tuple digests repeat exactly:

```text
baseline_sorted_a_eq_b=True
baseline_sorted_a_eq_shuffled=True
delivered_sorted_a_eq_b=True
delivered_sorted_a_eq_shuffled=True
baseline tuple digest (and delivered_on_160, byte-identical): ae060c77b9841a88b82c0f3c7fe332c629fba94d9a94269591e42a5df06bd5d0
delivered 164 tuple digest: b258447ffce0315dedab576a52eb43f011f2915f276fa4b8d9c7a1b7292d2649
hash_seed_probe={'runs': ['3201065308388920219 1', '2248198522866249206 1'], 'hash_values_differ': True}
```

Note the delivered-on-160 digest is the *same* digest as the regenerated baseline: every
one of the 160 tuples is byte-identical across the two revisions.

### 5. Calibration probes under the delivered checker (method-varied)

Two in-memory fixtures executed through a `Path.read_text` hook, `python3 -I`, delivered
bytes from the tar vs baseline bytes from `git show`:

- **P1 (null-from chain + tick inversion)** — baseline exit 1:

  ```text
  VIOLATION: entities[2].provenance[1].tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index); provenance tick 1 must be greater than previous tick 2
  VIOLATION: entities[2].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)
  ```

  delivered exit 1:

  ```text
  VIOLATION: entities[2].provenance[1].tick: provenance tick 1 must be greater than previous tick 2
  VIOLATION: entities[2].provenance[1]: provenance chain break; expected from_holder 'mira', got None
  ```

  `P1-null-from: exit_flip=False`.

- **P2 (unresolved non-null compared holder `dup` + tick inversion)** — baseline exit 1:

  ```text
  VIOLATION: entities[4].provenance[1].tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: from_holder 'dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); provenance tick 1 must be greater than previous tick 2
  VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got 'dup'; from_holder 'dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index)
  ```

  delivered exit 1:

  ```text
  VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 2
  VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got 'dup'; from_holder 'dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index)
  ```

  `P2-unresolved-compared-holder: exit_flip=False`. The tick line loses the identity
  qualifier (C9's integer-only reading); the chain-break line keeps it (genuinely
  unresolved non-null holder).

### 6. Durable-fixture spot checks on the delivered tree

- `r89-fn2-unresolved-chain-break` delivered exit 1, stdout sha `66ed1438…` — byte-equal
  to its B1/B2 manifest row; the chain break stays qualified. `r89-fn2-control` delivered
  exit 1, stdout sha `4283f695…` — byte-equal to its manifest row; definite chain break.
  The FN-2 pair is in both canonical manifests and its delivered outputs still match them.
- `r87-probe-source-prefix` delivered stdout sha `88f2724f…` (unchanged from baseline,
  matches its manifest row): the tick line keeps `input-structural finding, not
  sourced-canon;` because `chain_has_ambiguous_source` is true — the independent
  ambiguous-source prefix, as X3's report declared.
- **Cross-check against the rejected alternative:** X1's receipt records this same fixture
  as its single changed tuple (`88f2724f…` → `57981447…`, X1 drops the ambiguous-source
  prefix from the tick line). The shipped composition keeps the prefix and changes 0
  tuples; this is the C9-ruled reading, not an integration error.

## Findings & named debt

- **Per-axis verdicts (delivered tree ca7f9ef):**
  - *C1 calibration — improved.* Freeze hash-match PASS (composed = delivered, both
    orders). Probes P1/P2 show both hedged shapes the r89 audit named now return definite
    wording, while genuinely unresolved non-null holder chain-breaks stay qualified
    (P2 chain lines, fn2-unresolved), exactly as the C9 ruling states. The C9 supersession
    of the spec's original X1 boundary is recorded in the spec amendments, not silent.
  - *Compatibility — improved.* Regenerated baseline matches B1/B2 160/160; delta is
    0 changed of 160 with 0 exit changes and 0 stderr changes; delivered 164 dirs
    {0: 32, 1: 132}, 417 violation lines.
  - *Reproducibility/determinism — improved.* Repeats, shuffled seed 9001, and
    differing per-process hash seeds all yield identical tuple digests; the full 164-tuple
    post-repair receipt is committed as `followup/JCAL5-delta.json` (106,603 bytes,
    sha256 `0745a894041c473278d390536d60dc3c4e6bbfe12327720408f362c3bf9af3f6`).
  - No axis is harmed by the delivered composition; no blocking finding.
- **Named debt (forward-looking, none contradicting the C1 claim):**
  1. The two repaired shapes are census-invisible: no fixture in the 160 distinguishes the
     two revisions (0 changed tuples), so regression visibility for the *definite* null-chain
     and tick wording rests on non-durable `/tmp` probe receipts (B3/C5/C9 and P1/P2 here).
     r91 candidate: add durable fixtures for a null-from chain + tick inversion and a
     compared-unresolved-holder tick so the repaired wording is manifest-pinned.
  2. The 4 new fixtures have no row in a tracked manifest (B1/B2 are baseline-only, 160
     rows); my 164-row receipt lives in the untracked follow-up evidence dir. r91 could
     fold the 4 rows into the canonical manifest.
  3. C9's declared falsification path remains open: if a case emerges where tick ordering
     genuinely needs holder-identity context, the integer-only reading is revisited.
- **Boundary note:** the census scope is recursive `corpus/fixtures` (164 dirs). A 5-name
  scan over the whole corpus also matches 9 `corpus/live/**` dirs (173 total, unchanged
  between revisions); counts outside the declared scope should not be compared to the
  160/164 figures.

## Handoff

- Deliverables (only repo writes by this seat): `.ufo/waves/round-90/followup/JCAL5.md`
  and `.ufo/waves/round-90/followup/JCAL5-delta.json`. No commit, no push, no other
  tracked write.
- `JCAL5-delta.json` contains: archive + checker hashes, the freeze block with both patch
  orders, the three dir enumerations, seven run summaries with tuple digests, full
  160-row baseline and delivered-on-baseline tuple maps, the 4 new-fixture stdout texts,
  B1/B2 replay results, spot checks, and the hash-seed probe.
- Scratch (not committed): `/tmp/jcal5/ca7f9ef.tar` (`8f7c4fe0…`), `/tmp/jcal5/driver.py`
  (`3c4882ee…`), `/tmp/jcal5/probe.py` (`1f81a246…`), `/tmp/jcal5/verify/` (patch
  composition scratch). Dependencies: none outstanding — all inputs were committed at
  ca7f9ef; no gaps.
- For the round judge: the freeze-then-verify rule passes with no mismatch, the 0+4 delta
  and determinism reproduce under a method the work-wave seats did not use, and the only
  delta between the shipped reading and the rejected X1 alternative is the deliberately
  retained ambiguous-source prefix on `r87-probe-source-prefix`.
