# V42 anchor-replica-2 — round 97 seat report

- Seat: V42 (verifier, anchor-replica-2). Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`
  (session cwd is the parent repo; every path below is absolute under the lane root). Baseline
  `f3e09f9`. Writes: this report + `.ufo/waves/round-97/seats/V42-scratch/` only. No commits, no
  pushes, no network, leaf seat, no nested agents.
- Assignment: independent anchor re-verification (python method) of the r97 map — all 17 in-span,
  line numbers preserved.

## Method (independent, tool-free)

Own script `.ufo/waves/round-97/seats/V42-scratch/anchor_replica.py`: a from-scratch markdown-table
parser (no project tool invoked; no `grep` subprocess) that resolves each row's fixed-string anchor
against the referenced excerpt file by pure line-by-line substring search, then:

- **in-span** = every occurrence of the anchor falls inside the declared line span (strictest
  reading; all-outside-occurrences are failures);
- **line numbers preserved** = for rows shared with a baseline map, the five raw cells
  (pointer / path / span / mode / anchor) are byte-identical AND the resolved hit-line set is
  identical. Two baselines: post-repair r96 worktree map, and the committed `f3e09f9` map
  (saved via `git show f3e09f9:corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` into
  `V42-scratch/r96-map-committed.md`).

Commands (run from the lane root, snapshot 18:51:58):

```
$ python3 .ufo/waves/round-97/seats/V42-scratch/anchor_replica.py \
    --map corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md \
    --cluster corpus/fixtures/r97-crossing-acknowledgment \
    --baseline-map corpus/fixtures/r96-crossing-response/claim-excerpt-map.md \
    --baseline-cluster corpus/fixtures/r96-crossing-response --label r97-vs-postrepair-r96
== r97-vs-postrepair-r96: 17 rows, in-span 17/17 ==
... 17 ROW lines, all in-span ...
== preservation: matched=16 mismatches=0 ==
VERDICT PASS failures=0        (exit 0)   [full output: V42-scratch/verify-r97-postrepair.txt]

$ same --baseline-map .ufo/waves/round-97/seats/V42-scratch/r96-map-committed.md \
       --baseline-cluster corpus/fixtures/r96-crossing-response --label r97-vs-committed-f3e09f9
== r97-vs-committed-f3e09f9: 17 rows, in-span 17/17 ==
== preservation: matched=16 mismatches=0 ==
VERDICT PASS failures=0        (exit 0)   [full output: V42-scratch/verify-r97-committed.txt]
```

## Poll-wait record (never verified a plan)

- r97 dir appeared 18:44:16 (10-file base copy); R4's authored fixture files 18:44:30; the r97 map
  stayed the r96 base copy until adapted 18:48:56 (poll try 8, seen 18:49:06). R4 report
  `R4-fixture-author.md` landed ~18:50:28 (try 12); R5 report `R5-fixture-docs.md` landed 18:51:33
  (relaunched poll, try 2). Verification ran 18:51:58 onward on that frozen state.
- R6's report was absent at write time (its note `corpus/knowledge/r97-acknowledgment-scope-note.md`
  exists) — not an artifact this seat depends on.

## Results (verified revision: r97 map sha256 `49d4834e…`, r97 excerpts `8ba491cb…`, r96 post-repair map `e851f068…`)

1. **All 17 JSON-fact rows in-span (17/17).** Resolved hit lines: J01/J03/J06/J08/J12 → 12;
   J02/J04/J07/J09/J13 → 13; J05 → 17; J10 → 18; J11 → 19; J14 → 20 (span 18-20); J15 → 26
   (span 22-31); J16 → 37 (span 33-42); **J17 → 48 (span 44-53)**. No anchor had any occurrence
   outside its declared span.
2. **Line numbers preserved, 16/16, against both baselines** (post-repair r96 and committed
   f3e09f9): identical pointer/path/span/mode/anchor cells and identical hit-line sets for
   J01–J16. J17 correctly unmatched (`r97-only rows: ['J17']`, no r96-only rows).
3. **Raw-cell diff r96(post-repair) → r97: exactly 16 differing cells, all in the
   path-qualification column** (`r96-crossing-response:` → `r97-crossing-acknowledgment:`); every
   other cell byte-identical, including all spans, modes, and anchors. Saved:
   `V42-scratch/preservation-cells.txt`.
4. **Editorial rows S01/S02 in-span at line 5** (`source-excerpt.md` byte-identical between r96/r97).
5. **Distinct (path,anchor) pairs = 15/15**, matching the declared inventory count.
6. **Source preservation:** r97 `fictional-excerpts.md` lines 1–42 byte-identical to r96
   (`diff` empty on the prefix); r97 content is a pure append (lines 43–53). r96 excerpts sha
   `06b11bec…` → r97 `8ba491cb…`.
7. **Producer-claim cross-check:** my measured hashes equal the R4/R5 receipts (r97 map
   `49d4834e…`, r97 excerpts `8ba491cb…`, r96 post-repair map `e851f068…`); R5's inherited-anchor
   line table matches my independently resolved hit lines.

## Bounds

- Lexical anchor/span/preservation verification only — not whole-claim entailment, not an
  inventory/pointer/source-binding check (other seats), not a scope reading of the acknowledgment.
- Snapshot frozen at the hashes above (mtimes: r96 map 18:43:42, r97 excerpts 18:44:30, r97 map
  18:48:56). Re-verify if any of those files move after this report.
- No project tool was invoked by this seat, so the result is independent of the round's tool churn.

## Bottom line

**PASS** — all 17 r97 map obligations in-span with anchors resolving to the declared line numbers,
16/16 inherited rows preserved byte-exact except the namespace column with identical excerpt line
numbers (both baselines), J17 span 44-53 hit 48 in the appended section only, 15/15 distinct anchors.
