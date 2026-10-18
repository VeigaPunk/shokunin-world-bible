# JDEP3 — Register/namespace: cross-cluster referent comparison, register absence, R10-outcomes audit

- Seat: JDEP3, follow-up wave, round 93. Repo `lore-shokunin/` at HEAD `65838f867d6ece8e7b8bdcc4ffc667a08a1b785e` (r93 WORK commit; baseline `87779a0`).
- Verified state: `git rev-parse HEAD` → `65838f867d6ece8e7b8bdcc4ffc667a08a1b785e`; `git status --porcelain` → only `?? .ufo/waves/round-93/followup/` (my lane). All measurements below are from the committed tree.
- Axes: **(J1) cross-cluster referent disjointness** (must be empty, all three clusters, every id level), **(J2) R10 register abstention** (live register absent — and absent *correctly*), **(J3) no false R10-outcomes sections**, **(J4) namespace discipline** (no bare `source_id` collision per the r91 scoping rule).
- Evidence receipt: `.ufo/waves/round-93/followup/JDEP3-scan.md` (script + full observed output).

## Work performed

1. **Located all three sourced-mythology clusters** (fixture dirs at `corpus/fixtures/`): `r87-myth-cluster/` (14 files), `r88-m3-maya-cluster/` (11), `r93-m2-kojiki-cluster/` (12, new in r93).
2. **Extracted every referent at every id level** and compared across all three clusters (`/tmp/jdep3/compare.py`, output in `JDEP3-scan.md`):
   - L1 all JSON id-bearing values (`id`, `entity_id`, `place_id`, `source_id`, `first_appearance`, `event_id`, `from`, `to`, `depends_on` across entities/relations/timeline/sources/contradictions): r87 = 17 ids, r88 = 8, r93 = 7.
   - L2 entity display names (casefolded): 7 / 4 / 4.
   - L3 source titles (casefolded): 5 / 2 / 1.
   - Pairwise intersections L1∪L2∪L3: **all three EMPTY** (exact observed lines: `r87-myth-cluster ∩ r88-m3-maya-cluster: EMPTY`, `r87 ∩ r93: EMPTY`, `r88 ∩ r93: EMPTY`). Three-way intersection: **EMPTY**.
3. **Overlap audits beyond exact keys** (to prove emptiness is not an artifact of a narrow key set):
   - L4 generic word tokens inside names+titles: r87∩r88 = {`bell`, `register`}, r87∩r93 = {`register`}, r88∩r93 = {`register`} — common nouns only (`Reed Bell` vs south bell; three distinct registers), no referent identity. Complements the README's own disclosed `Reed` lookalike (`Central Land of Reed-Plains` vs `Reed Bell`/`Reedwardens`).
   - L5 markdown layer: excerpt *filenames* share only structural scaffolding (`README.md`, `claim-excerpt-map.md`, `inspiration-note.md`, `symbolism-clause-map.md`) — dir-scoped by R8/R9 convention, not referents. External-work mentions fully disjoint: r87 = {ETCSL}, r88 = {Spence, K'iche}, r93 = {Kojiki, Chamberlain}.
   - L6 claim-map row labels (`E1`, `S1`, …) collide across clusters — map-local labels namespaced by cluster directory, not corpus ids. Named, not a violation.
4. **Referent-leak grep, word-boundary enforced**: for each of r87's 13 referent tokens into r88+r93 dirs, r88's 10 into r87+r93, r93's 5 into r87+r88 (`grep -rlE "\b<id>\b"`) — **zero files matched in every direction**. The only cross-cluster mentions anywhere are r93 README's explicit contrast references (see 6).
5. **Register absence verified + contract-checked**: `corpus/knowledge/cross-cluster-contradictions.md` does not exist (`ls: cannot access ... No such file or directory`); the only similarly named file is the r89 worked demo `corpus/knowledge/r89-cross-cluster-contradiction.md`, which explicitly disclaims register status. Per the R10 appendix (decided r90, `r88-sourced-inspiration-decision-table.md:87-99`) the register is created only on a source-backed shared referent+field+occasion with incompatible assertions; per the r91 namespace-scoping note a bare shared `source_id` is a namespace collision, never identity. Neither trigger exists (J1 empty; L1 shows no shared `source_id` either). **The register's absence is the correct state, not a gap.**
6. **R10-outcomes sections census (no false outcomes)**: repo-wide grep for `## R10 comparison outcomes` finds exactly one — `corpus/fixtures/r93-m2-kojiki-cluster/README.md:14` (r87/r88 READMEs have none, correct: only the *incoming* cluster carries the section; the rule is prospective per the r89 integration notes, and r87/r88 predate it). Audited every checkable claim in that section against my independent measurement:
   - entity/event inventory (teva, orni, slate-table, lorn-index, teva-files-index, orni-marks-index) — matches my L1 exactly;
   - "no exact key shared with either existing cluster" across entity IDs, display names, declared aliases/epithets, event IDs, relation/timeline endpoints — reproduces (L1/L2; no alias/epithet key exists in any cluster's entities.json, verified by grep);
   - `Reed` lookalike disclosure — corroborated by my L4 token audit;
   - "Source IDs are compared only as path-qualified namespace pairs" — consistent with the r91 rule; bare ids don't collide anyway;
   - "an independent M2-specific scan and semantic review remain pending before any integrated zero-referent conclusion" — the honest hedge; my J1/J4 constitute an independent post-landing scan, plus a bounded semantic read (below). The section asserts no outcome it cannot support. **Not a false R10-outcomes section.**
   - Wave-level R10 claims (`J3.md`, `M1/M2/M3/M5.md`) are all candidate-stage and bounded; `LOG.md`/`PROVINCE.md` carry no r93 R10-outcome claim at all (round record lands in phase 2). Nothing false found.
7. **Certified the measured tree**: replayed both README commands — `python3 corpus/fixtures/check_bible.py corpus/fixtures/r93-m2-kojiki-cluster` → `CLEAN: schema, citations, relations, timeline; 0 violations` (exit 0); `python3 corpus/tools/support_check.py corpus/fixtures/r93-m2-kojiki-cluster` → `RECEIPT JSON-FACTS 12; EDITORIAL-ROWS 3; TOTAL-ROWS 15 ... RESULT PASS` (exit 0). My comparison therefore ran against the certified cluster content.
8. **Sibling cross-check**: JCOV2 (`followup/JCOV2.md:52-84`) independently ran a normalized-key scan over the same three clusters and also observed empty intersections; JCOV1 keeps the zero-referent conclusion's semantic half as named debt. No sibling claims a register entry or an integrated R10 outcome — no inter-seat contradiction.

## Before → after measurements

Verification seat: no corpus or tool change was made or needed; before = after = committed `65838f8` (re-verified clean at close except `followup/`). The measured quantities:

| Quantity | Before/after (committed tree) | Command | Observed |
|---|---|---|---|
| Pairwise referent intersections (ids+names+titles) | unchanged | `python3 /tmp/jdep3/compare.py` | `EMPTY` ×3; three-way `EMPTY` |
| Word-boundary referent leaks between cluster dirs | unchanged | `grep -rlE "\b<id>\b" <other-two-dirs>` for 28 tokens | zero matches in all three directions |
| Live R10 register `corpus/knowledge/cross-cluster-contradictions.md` | unchanged (absent) | `ls corpus/knowledge/cross-cluster-contradictions.md` | `No such file or directory` |
| `## R10 comparison outcomes` headings in corpus | unchanged | repo-wide grep | exactly 1 (r93 README:14); claims reproduce; 0 in r87/r88 (correct) |
| Bare `source_id` collisions | unchanged | L1 set intersection | none (no rename/qualify trigger under the r91 rule) |
| r93 cluster certification | unchanged | `check_bible.py` + `support_check.py` (README replay) | `CLEAN ... 0 violations`; `RESULT PASS` |

Per-axis verdicts: **J1 improved** (the landed claim "zero shared referents" now has a post-landing, all-levels, three-cluster mechanical verification plus a bounded independent semantic read — previously only author-side candidate-stage scans existed for M-17); **J2 improved** (absence verified as the *correct* state against the r90/r91 rule text, closing J3's "rerun the R10 checks after the selected candidate lands" gap); **J3 improved** (one section exists, audited truthful, honest hedge preserved); **J4 unchanged** (no collision existed; rule state re-confirmed). No trade observed on any axis: all checks are read-only replays plus two lane files.

## Findings & named debt

- **The R10 negative case now holds on the landed tree at every level I can measure**: ids, display names, source titles (exact — all empty), plus token, filename, external-work, row-label, and word-boundary leak audits (all non-referent or empty). The commit-message claim "empty intersections with both existing clusters at every id level" reproduces exactly.
- **Bounded semantic read (adds to, not replaces, the pending review)**: I read all three clusters' entities/relations/timelines/sources/maps/READMEs in full. The three casts occupy disjoint worlds — shore/tide community (Hara, Sen, Shellweavers, Reedwardens, Reed Bell, Moon-Basin Vow), lantern-and-bell court (Aru, Evin, Quiet Rise, Salt Court), and archive office (Teva, Orni, Slate Table, Lorn Index). No shared person, place, item, faction, event, field, or occasion candidate; no in-world text references another cluster's referents (only README contrast mentions, which the README itself disclaims as identities). This is one reviewer's pass from this seat; whether the parent credits it as satisfying the README's "independent M2-specific scan and semantic review" hedge (J3 wanted M6-equivalence) is the parent's call — I do not claim to close M6's named debt.
- **Standing debt, unchanged and correctly still open**: the semantic half of the integrated zero-referent conclusion (README.md:15 hedge; JCOV1/JCOV2 keep it open). Also unchanged: source-edition/rights/training unknowns on the Kojiki translation (outside my axes).
- **Non-findings worth keeping visible** (not violations): (a) generic-token overlaps `bell`/`register` across names/titles — distinct referents each time; (b) claim-map row labels (`E1`, `S1`, …) collide by design, dir-scoped; (c) the four shared scaffolding filenames are convention, not referents. If a future corpus-wide validator is built (r91's named gap: checker is single-directory), these three classes are exactly what it should namespace explicitly.
- **AST/content-signature anchor validation** remains named r94 debt per the round commit; not my axis, not re-measured.

## Handoff

- For the parent (phase 2): the r93 README's R10 hedge can now cite two independent post-landing lexical scans (JDEP3 + JCOV2, both empty at every level) and one bounded semantic read (JDEP3). If the parent accepts a follow-up semantic review as M6-equivalent, the integrated zero-referent conclusion can be promoted; otherwise leave the hedge as-is — it is truthful either way.
- Register stays absent. First genuine cross-cluster referent+field+occasion conflict creates `corpus/knowledge/cross-cluster-contradictions.md`; nothing in r93 comes close to the trigger.
- My writes: `followup/JDEP3.md` (this file) + `followup/JDEP3-scan.md` (receipt). No other repo writes; scratch in `/tmp/jdep3/`; no commits/pushes.
- Dependencies honored: two 60s wait-checks done (all sibling seats' files present by check 2; JCOV1/JCOV2/JDEP2 read for cross-confirmation, no conflicts with my verdicts).
