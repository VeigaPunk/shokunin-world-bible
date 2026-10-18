# SE2 — Phase-2 sentinel (round 88, world-bible lane)

Seat SE2. Ran LAST after two 60s wait-checks. Audit target: delivered tree at
`2ea9ef13a928475b13fd578740ea521bed4bd649` (work commit, baseline `dfd1fbc`).
All measurements below are against the delivered tree, not scratch patches.

## Work performed

- Wait-check 1 completed `2026-10-17T03:13:44-03:00`; wait-check 2 completed
  `2026-10-17T03:15:0x-03:00`. Inventory started only after check 2.
- Independent re-measurement of the C1 census: re-ran the checker over all 145
  `B1-tuples.json` baseline paths plus the 4 new `r88-*` directories.
- Live probes of the four stop fixtures (`r88-shape-ambiguous-armed`,
  `r88-mixed-stop`, `r88-nonholder-stop`, `r87-probe-shape-ambiguous`).
- Verification of the C2 artifacts (`r87-myth-cluster` OBS-1 repair,
  `r88-m3-maya-cluster`, clause map) and the C3 artifacts
  (`corpus/knowledge/r88-sourced-inspiration-decision-table.md`,
  `corpus/knowledge/reference-ledger.md`).
- Write-scope sentinel: HEAD, reflog, `git status`, followup-file naming,
  fleet-report location, sibling-repo scan, `/tmp` scratch scan.
- Determinism control: every changed fixture re-run twice; no nondeterminism.

## Before → after measurements

### 1. C1 census — exits and content, independent recomputation

Baseline source: `.ufo/waves/round-88/patches/B1-tuples.json` (145 tuples,
`exit` / `stdout_sha256` / `violation_count`, captured by seat B1 at `dfd1fbc`).

Command (B1's exact template, repo root as cwd, once per fixture):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>
```

Observed:

```text
B1-template census: unchanged= 136 changed= 9
   r61-independent-empty
   r61-independent-unavailable
   r87-masked-break-from-ambiguous
   r87-masked-break-to-ambiguous
   r87-probe-entry-shape
   r87-probe-multi-invalid
   r87-probe-nonitem-kinds
   r87-probe-record-and-chain
   r87-probe-shape-ambiguous
exit_changed= 0   (all 145 baseline exits identical to B1)
```

This independently reproduces `patches/V1-delta.json`
(`changed_tuple_count: 9`, `unchanged_tuple_count: 136`,
`pre_r87_changed_paths: [r61-independent-empty, r61-independent-unavailable]`,
`exit_changes: []`) and the round claim "9 changed + 4 new of 149 dirs,
0 exit changes, 2 pre-r87 r61 additive disclosures".

New directories (4), exits observed:

```text
r88-m3-maya-cluster        exit=0   CLEAN: schema, citations, relations, timeline; 0 violations
r88-mixed-stop             exit=1   6 violation(s); no canon changed
r88-nonholder-stop         exit=1   4 violation(s); no canon changed
r88-shape-ambiguous-armed  exit=1   5 violation(s); no canon changed
```

Total fixture dirs with `entities.json` = 149 (145 + 4), matching the claim.

### 2. C1 calibration probes — exact output on the delivered tree

`r88-shape-ambiguous-armed` (claim i: shape-invalid dict + ambiguous holder arms
the stop), exit 1:

```text
VIOLATION: entities[4].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'f1-shape-dup' at entities[4].provenance[0]
VIOLATION: entities[4].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'f1-shape-dup' at entities[4].provenance[0]
```

Both the stopping record and the tail disclose the same actual first cause.

`r88-mixed-stop` (claim ii: no over-attribution to a later ambiguity), exit 1 —
the disclosure names the *first* cause, the unknown source, not the later
ambiguous holder:

```text
VIOLATION: entities[5].provenance[0]: ... first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
VIOLATION: entities[5].provenance[1]: ... first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
VIOLATION: entities[5].provenance[2]: ... first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
VIOLATION: entities[5].provenance[1].to_holder: ambiguous entity 'f1-mixed-dup'
```

`r88-nonholder-stop` (claim iii: non-holder stop causes disclose), exit 1:
all three records disclose `first stop: unknown source
'f1-nonholder-missing-source' at entities[3].provenance[0]`.

`r87-probe-shape-ambiguous` (the r87 residual), before → after:
B1 baseline recorded 2 findings and **no** disclosure line; delivered tree:

```text
5 violation(s); no canon changed
```

with the added disclosure `first stop: malformed record (unexpected field set);
ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]`. The
residual named in the wave spec is closed.

### 3. C2 coverage

- `r87-myth-cluster` OBS-1 repair: 8/8 clause rows in `symbolism-clause-map.md`
  resolve by exact string match in `lowwater-hymn-excerpt.md`
  (`clause_rows=8 matched=8`). Exit 0.
- `r88-m3-maya-cluster`: exit 0; `inspiration-note.md` cites Spence 1913
  ch. V "The Maya" p. 209 with Gutenberg 53080 and keeps attribution / rights /
  AI-training-permission as three separate sections; `source-excerpt.md`
  delivers the passage with the `[209]` page marker; `README.md` records the
  tick-9 occupied-slot near-miss explicitly as a near-miss, not a double-booking.
- Clause-map exact resolvability: 1 of 2 cited clauses matches exactly; the other
  (`He called out ‘Earth,’`) matches only after normalizing quote characters
  (excerpt has `“Earth,”`). See N1.

### 4. C3 depth

- `corpus/knowledge/reference-ledger.md:8` carries the ETCSL / Inana's descent
  row in the four-column form (Work-attribution | Rights | AI-training | Use).
- `corpus/knowledge/r88-sourced-inspiration-decision-table.md:1` carries the
  R1B scope note (support rule covers every source-attributed in-world JSON
  fact).

### 5. Sentinel audit — write scope, HEAD, commits

```text
$ git rev-parse HEAD
2ea9ef13a928475b13fd578740ea521bed4bd649

$ git reflog -3
2ea9ef1 HEAD@{0}: commit: lore r88: C1 stop-cause repair + C2 Maya cluster + C3 inspiration table — work wave (37 luna-max seats)
dfd1fbc HEAD@{1}: commit: lore r87: ... follow-up integration
2b48ca7 HEAD@{2}: commit: lore r87: work-wave evidence ...

$ git status --porcelain
 M l0-questions.md
?? .ufo/waves/round-88/followup/

$ git diff --numstat l0-questions.md
1	0	l0-questions.md
```

- HEAD unchanged at `2ea9ef1`; reflog shows **no commit by any seat** after the
  work commit. No stash, no new branch. Commit identity is
  `lore-shokunin <lore@shokunin.local>` (the r80 wrong-identity incident does not
  recur). `main` is ahead 5 of `origin/main` (pre-existing, no push).
- Only tracked modification anywhere is `l0-questions.md`: exactly one inserted
  line, zero deletions, `lore | round-88 | ...` in the existing format — the
  authorized K1 append.
- followup/ naming: 29 files at the final snapshot, every one matching
  `^[A-Za-z0-9]+(-[A-Za-z0-9._-]+)?\.(md|json)$` (`<SEAT>.md` or
  `<SEAT>-*.json|md`). Zero naming violations.
- `git status --porcelain --untracked-files=all` has no entry outside
  `.ufo/waves/round-88/followup/` other than `l0-questions.md`.
- No file in the tracked tree was modified after the work commit except
  `l0-questions.md` (mtime scan since `03:10:35`).
- Fleet report: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-88/` **does not
  exist** at audit time, and no `lore.md` appears anywhere under
  `.ufo/reports/`. The "fleet report exists only at ..." clause is therefore
  vacuously satisfied; see N3.
- Fleet root `git status` clean. Sibling repos: no tracked modification in any
  of them. `kotodama-shokunin` has untracked `corpus/**` files (mtimes
  02:30–03:12) — attributed to kotodama's own mint swarms per its `LOG.md`
  ("operator dispatch of four 16-agent corpus-seeding swarms"), not to a lore
  seat; see N4.
- Scratch: `/tmp` holds the expected round-88 scratch trees
  (`/tmp/lore-*`, `/tmp/lore88`, `/tmp/jcov3-r88`, ...). No repo writes there
  beyond the authorized followup dir.

## Findings & named debt

- **No rule violations found.** Every check in the SE2 block passed; there is
  nothing to report verbatim as a violation.
- **N1 (C2, low).** `r88-m3-maya-cluster/symbolism-clause-map.md` cites
  `“He called out ‘Earth,’”` while the delivered excerpt has `He called out
  “Earth,”` (nested-quote style differs). The attribution is supported, but the
  claim "every attributed claim mechanically resolvable in the delivered
  excerpt" holds 1/2 by exact match and 2/2 only after quote normalization.
  Debt: either normalize the clause quoting or state the match rule.
- **N2 (process, medium).** stdout-hash comparisons against
  `patches/B1-tuples.json` are command-template sensitive. My first pass ran
  `cwd=corpus/fixtures; python3 check_bible.py <dir>` and reported **14**
  apparent content changes; 5 of them (`r5-missing-file`, `r62-missing`,
  `r67-claim-source-unavailable-{control,empty,whitespace}`) were false
  positives, because the relative fixture path is embedded in the
  `cannot load JSON: [Errno 2] ... '<path>/contradictions.json'` message.
  Re-running B1's exact template (`python3 corpus/fixtures/check_bible.py
  corpus/fixtures/<dir>` from the repo root) reproduced exactly 9. All 14 were
  deterministic across repeat runs, so this is a template artifact, not flake.
  Any judge using these hashes must pin the command template.
- **N3 (process).** The round-88 fleet report is absent at audit time; P1 had
  not landed it. My inventory is a `2026-10-17T03:15:32-03:00` snapshot — the
  followup dir grew from 16 to 29 files during my run, so the sentinel check
  should be re-run once all seats stop.
- **N4 (scope, informational).** `kotodama-shokunin/corpus/**` untracked writes
  overlap the wave window but belong to kotodama's own mint activity. No lore
  seat wrote outside the authorized paths.

## Handoff

- This report: `lore-shokunin/.ufo/waves/round-88/followup/SE2.md`.
- Delivered tree audited at `2ea9ef1`; HEAD unchanged; tree clean except the
  authorized K1 `l0-questions.md` append and the untracked followup dir.
- Independent C1 census reproduces V1's 136/9/0 and the 149-dir count.
- Remaining for the parent: re-run this sentinel after all seats stop (N3), and
  re-check `/home/vgpnk/Projects/shokunin/.ufo/reports/round-88/lore.md` once P1
  writes it. N1 and N2 are carried as debt.
