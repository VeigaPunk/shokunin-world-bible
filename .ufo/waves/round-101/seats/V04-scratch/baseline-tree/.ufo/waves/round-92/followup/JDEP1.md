# JDEP1 — The certifier: `corpus/knowledge/holder-assessment-boundary.md` at `c4d4823`

Seat JDEP1, round-92 follow-up wave, world-bible lane. Judged tree: **delivered**
`c4d4823b9a8165a88e8199af136e62d6e961b6b9` (verdict evidence from the committed tree only; scratch
`/tmp/jdep1`), baseline `396c568`. Checker `corpus/fixtures/check_bible.py` sha256
`ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`, 428 lines — byte-identical to
the r90-delivered checker the doc names, and unchanged `396c568`…`c4d4823`. Target doc: 672 lines,
sha256 `8e1fe8774a70f06c31efd783b4313a1639c1da4bcfd830be92134e8964536728`.

**Per-check ruling: (a) PASS · (b) FAIL (blocking) · (c) PASS · (d) PASS · (e) PARTIAL.**

## Work performed

- Dependency state at t0: HEAD `c4d4823`, `git status --porcelain` empty, work commit subject confirms
  the r92 work wave. Both dependencies were therefore already satisfied when this seat started; one
  wait-check was run for the protocol receipt (below) and one on the sibling artifact `JDEP2.md`.
- Gate (a): extracted every fenced block from the doc (8 fences: 1 template, 3 `sh`, 3 `text`, 1
  helper `sh`) with an indentation-tolerant parser; ran each non-helper `sh` block verbatim from the
  lane root against the delivered checker and byte-diffed stdout against the following `text` block.
  Also replayed 19 further fixture cases the doc states in prose, plus the helper-absence and census
  claims.
- Gate (b): extracted all 140 `` `:NNN` `` anchor sites in the doc with their context lines, bucketed
  them by scope (delivered-context 92 / orphaned r89 tail 21 / baseline-`5eb9451` 13 / r87
  decision-table 12 / README 2), and checked every delivered-context and baseline site against the
  claimed content (`corpus/fixtures/check_bible.py` at HEAD; `git show 5eb9451:…` written to
  `/tmp/jdep1/base.py`).
- Gate (c): heading census and instruction-marker scan (script + `grep -nE`).
- Gate (d): C9 tick semantics three ways — doc text, checker code lines, and behavior
  (`r91-c1-null-chain`, `r91-c1-tick-unresolved`, `r89-c1-invalid-tick`, `r87-probe-source-prefix`)
  plus one scratch probe (`r89-fn2-unresolved-chain-break` with `record[1].from_holder=null`) for the
  null-follow-on-with-unresolved-expected-side limit at doc:295-297.
- Gate (e): read the r91 forensics worklist — `.ufo/waves/round-91/followup/JAXIS.md` (R1/R2/R3),
  `H5.md` (F1–F7), `CB1.md` + `CB1-docstate.json` (coherence-defect list) — and ruled each item
  against the committed tree.
- Lineage: diffed the doc against `ca7f9ef`/`e97613c` (sha `a4b1b331`, 630 lines) to confirm the
  r92 re-derivation is the r89-landed contract + r90 section text + anchor remap.

## Before → after measurements

**Tree and checker freeze.**

```sh
git rev-parse HEAD; git status --porcelain; sha256sum corpus/fixtures/check_bible.py; wc -l corpus/fixtures/check_bible.py
```

```text
c4d4823b9a8165a88e8199af136e62d6e961b6b9
(no output)
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
428 corpus/fixtures/check_bible.py
```

**Gate (a) — the three pasted blocks.** Commands are the doc's own (doc:346-350, :400-404, :456-460);
output captured separately and compared byte-for-byte with the following `text` block.

```text
--- sh block ending line 350: rc=0 stderr_bytes=0
  BYTE-IDENTICAL to text block ending 385 (29 lines)
--- sh block ending line 404: rc=0 stderr_bytes=0
  BYTE-IDENTICAL to text block ending 452 (45 lines)
--- sh block ending line 460: rc=0 stderr_bytes=0
  BYTE-IDENTICAL to text block ending 479 (16 lines)
```

3/3 blocks, 14/14 cases byte-identical, stderr empty — the doc's doc:41 claim ("All fourteen pasted
case blocks below replay byte-identically") holds at `c4d4823`.

**Gate (a), extra inline claims replayed** (19 fixture cases; every doc-stated figure matched).

```text
r87-masked-break-from-ambiguous 5 violation(s), first stop from_holder 'dup' at [0] on records [0][1][2]   (doc:390-395)
r87-masked-break-to-ambiguous   5 violation(s), to_holder 'dup' at [0] on records [0][1][2]
r89-c1-invalid-tick             4; first stop malformed record (invalid tick) at entities[3].provenance[1]  (doc:481-486)
r89-c1-invalid-from-holder      3; r89-c1-invalid-to-holder 3; r89-c1-malformed-source-id 3 at entities[2].provenance[1]
r87-chain-unique-broken 1 violation(s); r87-chain-unique-valid CLEAN                                    (doc:200)
r87-probe-entry-shape           entities[4].provenance: expected array (+ duplicate item id 'rope' arming entities[5] and [6])
r90-c1-rawpresent-to/from/source  present in raw entities but / raw sources but absent from the resolved index  (doc:488-491)
r90-c1-three-causes             malformed record (invalid tick); holder reference …; source reference … in one joined clause
r91-c1-null-chain               1 violation: definite chain break, got None                                  (doc:294-296)
r91-c1-tick-unresolved          3 violations: definite tick line + separately qualified chain line
r61-independent-empty           provenance attached to a non-item entity alone, despite dangling holders/unknown sources (doc:268-270)
r61-independent-unavailable     source table unavailable alone, same
r7-item-ambiguous               ambiguous SOURCE only, comparisons still run, no disclosure                    (doc:321-324)
r87-probe-source-prefix         tick and chain lines prefixed from the ambiguous source, no stop
```

**Gate (a), non-fixture claims.**

```sh
python3 corpus/fixtures/measure_holder_disclosure.py --revision HEAD; echo "[rc=$?]"; ls corpus/fixtures/*.py; ls -d corpus/fixtures/*/ | wc -l; grep -rl '"provenance"' corpus/fixtures/*/entities.json | wc -l
```

```text
python3: can't open file '…/corpus/fixtures/measure_holder_disclosure.py': [Errno 2] No such file or directory
[rc=2]
corpus/fixtures/check_bible.py
166
35
```

Doc:517-521 and :60-66 say exactly this (rc 2, `No such file or directory`, `check_bible.py` the only
Python file there); 166 fixture dirs = the doc's 164 at `ca7f9ef` + the two r91 fixtures; 35 provenance
dirs = 33 + the two r91 fixtures (doc:579-590).

**Gate (b) — anchor census.**

```text
total `:NNN` sites in doc: 140
Counter({'delivered-context': 92, 'r89-fragment-orphan': 21, 'baseline-5eb9451': 13, 'r87-decision-table': 12, 'README': 2})
```

Delivered-context: **91 resolve, 1 stale** — doc:330 `:198-203` for the item-level first-stop tests,
whose delivered span is `:200-205` (the same bullet gives the correct range one line later at
doc:331). Baseline-scoped sites (doc:79-81, doc:526-533) all resolve against `git show 5eb9451`
(`:157-159` holder counts, `:212-214`/`:220-222` dangling, `:215-216`/`:223-224` silent branches,
`:234-237` latch, `:238-245` gate, `:246-247` no-resume, `:168` relation precedent, `:320-330` CLI).

Orphaned r89 tail (doc:545-556): **14 of 21 sites do not resolve to the claimed content** against the
delivered checker — `:182` (dangling, not the ambiguity precedent at `:184`), `:185-352` (loop is
`:187-345`), `:191` (`:193`), `:192-194` (`:194-196`), `:198-203` (`:200-205`), `:206-208`
(`:208-210`), `:212-214` (`:214-216`), `:215-221` (`:217-223`), `:222-248` (`:224-250`), `:249-312`
(`:251-314`), `:313-319` (`:315-321`), `:320-352` (`:322-345`), `:425-435` (`:418-428`, and `:429-435`
is past the delivered file's 428 lines), plus `:168-173` truncated against the function's `:168-175`.
Only `:38-39`, `:72-76`, `:82-83`, `:85-91`, `:93`, `:97`, `:164-166` coincide.

**Gate (c) — structure.**

```text
sha256 8e1fe8774a70f06c31efd783b4313a1639c1da4bcfd830be92134e8964536728
lines 672   H1 count 1 [(1, '# Holder-assessment boundary: reading provenance ambiguity disclosures')]
headings 10   dup normalised: {}
marker scan rc=1 (no hits)
```

**Gate (d) — C9 semantics.** Text: doc:201, :254, :280-289, :293-297. Code: `:323-326` compares
validated integers only, prefix from `chain_has_ambiguous_source` (`:325`), no
`holder_identity_detail` call in the tick branch; `:169-170` returns `None` for a null side. Behavior:
`r91-c1-tick-unresolved` emits the definite tick line plus a separately qualified chain line;
`r91-c1-null-chain` emits the definite `got None` break; `r87-probe-source-prefix` shows the only
ambiguous-tick prefix path; the scratch probe returned

```text
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got None
2 violation(s); no canon changed
```

which is exactly the doc:295-297 limit ("A null follow-on whose expected side is itself an unresolved
non-null id stays qualified").

**Gate (e) — census recheck.**

```text
at ca7f9ef: dirs with provenance = 33
  records referencing a duplicated holder id: 12 across 10 dirs
```

The doc (doc:581-590) says "13 provenance records across ten of them" at `ca7f9ef`; the ten fixtures
it names hold 12 there (13 is the HEAD count, adding `r91-c1-tick-unresolved`). Off-by-one wording,
non-blocking.

## Findings & named debt

**F1 — gate (b) FAIL, blocking: the delivered-checker evidence bullet is spliced to its orphaned r89
tail (doc:534-556).** The r92 edit replaced only the bullet's head line with the `ca7f9ef` `ff9fd2aa`
text and left the r89 era's continuation in place, beginning mid-clause at doc:545 —
`lines, sha256 `e2bb9639…`):` — after doc:544 has already asserted the delivered checker's
`:418-428` CLI span and byte-stability through `396c568`. Consequence: 21 anchor sites appear with no
revision head, 14 of them wrong for the delivered checker (F1 mapping above; one past EOF). This is
the same splice failure mode H5-F6 and CB1 charged at r91, reproduced at r92. Fix is mechanical:
either restore the bullet head (`Checker at delivered `1b09f3f` (`corpus/fixtures/check_bible.py`, 435
lines, sha256 `e2bb9639…`)`) or delete the orphaned tail (the r89 line refs are superseded).

**F2 — one stale unlabelled delivered-context anchor: doc:330 `:198-203`** (D6/D7-class residue; the
cause table and contract items were remapped, this limits bullet was not).

**F3 — two more orphaned tails (same splice class).** doc:591-596 repeats the fixture-inventory tail
already stated at doc:583-587, with the old `§M7 of the r89 CB1 report` attribution; doc:615-619
repeats the Rules-text tail already stated at doc:608-614. Both are CB1's "duplicated paragraph"
class, unfixed (CB1 also named the decision-table duplicate row and the missing limit bullets — those
are fixed).

**F4 — carried-over garbled sentence at doc:656:** "it is marked SUPERSEDED-and-pinned at its header
(r88 closure) anywhere in the tree" reads as a truncated clause; it is identical at `ca7f9ef`
(`a4b1b331`), so it is pre-existing, not r92-introduced, and not repaired by the re-derivation.

**F5 — census off-by-one at doc:581-590** ("13 … across ten of them" at `ca7f9ef`; measured 12/10).

**F6 — JAXIS R2 still open (non-doc):** the README has `## Round 90` (:1016) then `## Round 92`
(:1020); there is no `## Round 91` section and no `r91-c1` mention anywhere in
`corpus/fixtures/README.md`. The r91 fixture pair is documented only in
`corpus/knowledge/r91-c9-watch.md`, whose check-log row 1 (2026-10-17, DISCRIMINATION HELD) and
pinned pair I replayed byte-for-byte.

**Verified-good (no debt):** gates (a), (c), (d); the restored headings (`## The contract` :68,
`## Commands` :340, `## Status split` :623) and all cross-references into them; the 14 second-cause
table rows; the limits section's 14 bullets; the r90 hedged-shapes bullet; baseline anchors; the r87
decision-table quote line refs (doc:653-654 — strings at `:60`, `:61`, `:99`, … confirm); the probe
input claim (`masked` and `unique-break-control` carry identical `(null→mira,0)`, `(mira→vault,3)`,
`(harbor→tower,4)` transfers; masked adds the second `vault` row).

## Handoff

- **Ruling:** (a) PASS 3/3 blocks, 14/14 cases · (b) **FAIL (blocking)** · (c) PASS · (d) PASS ·
  (e) PARTIAL (R1 residual, R2 open, H5-F6 partial, CB1 duplicated paragraph open; F1/F2/F3 are the
  same blocking defect).
- **For the L1:** gate (b) is blocking, so the r92 C1 claim cannot be recorded as a clean depth gain
  while F1 stands. The repair is one bullet head (or one tail deletion) plus one range fix at
  doc:330; both are documentation-only and checker-free (`ff9fd2aa` unchanged).
- **Evidence:** `.ufo/waves/round-92/followup/JDEP1-certification.json` (per-check PASS/FAIL, anchor
  deviation map, census recheck). Scratch left at `/tmp/jdep1` (6 files + probe dir) — sweep at close.
- **Dependency receipts:** `POLL_HIT path=corpus/knowledge/holder-assessment-boundary.md elapsed=0s`
  then `POLL_CHECK t=60s path=.ufo/waves/round-92/followup/JDEP2.md present=no` /
  `POLL_TERMINAL status=0 reason=deadline elapsed=60s` (`/tmp/jdep1/poll.txt`). Sibling artifacts
  landed during my run (H3, H4, JCAL1/2/3/5, JCOV1/2/3, JDEP4, K1; JCAL4 arrived at close);
  `JDEP2.md` never appeared, so the C1 claim's JDEP2 residual-edge language is not independently
  readable here and is not certified by this seat. No sibling artifact reports the doc's orphan-tail
  or `:198-203` defect and none contradicts this (b) FAIL.
- **R3 update (sibling evidence, not my measurement):** `JCAL2.md:159` finds the C9 watch's re-check
  landed but its next-recheck pointer (owner/due) and the pinned `e97613c` hash still absent — so
  JAXIS R3 is ADDRESSED for the receipt pair and PARTIAL for the watch's forward pointer.
- **Correction:** the r92 work claim "the boundary doc re-derived ANCHOR-BASED and certified" is
  accurate as to method and replay, but **not** as to certification: the doc is not certifiable as
  delivered until F1-F3 are repaired.