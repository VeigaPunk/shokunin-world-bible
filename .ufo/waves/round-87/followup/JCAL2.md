# JCAL2 — Calibration judge #2 (adversarial)

Seat: JCAL2. Wave: round-87 follow-up (world-bible lane), fleet root `/home/vgpnk/Projects/shokunin`, repo `lore-shokunin/`.

**Measured revision: `2b48ca72033dfd1060b6f81c4cf27ad83deae57f` (`2b48ca7`), measured 2026-10-17.** Judged artifact: `corpus/fixtures/check_bible.py` at that revision, sha256 `3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237` (md5 `e088ac108b7f1e2dda8f1630d72cc161`). Pre-C1 comparison artifact: the same file at `28706dc`, sha256 `e8f241623aa84eb1dce192a03c9e70b8f4ba386344f0b22a99ba1ac0d4942132`, extracted with

```sh
git -C /home/vgpnk/Projects/shokunin/lore-shokunin show 28706dc:corpus/fixtures/check_bible.py > /tmp/jcal2/check_bible_OLD.py
```

No tracked file was written by this seat. All measurements are `/tmp` scratch or the three untracked artifacts beside this report (`JCAL2-pinned-census.json`, `JCAL2-falsity.json`, `JCAL2-receipt-audit.json`).

**Tree pinning.** At measurement time the working tree was **not** clean: `git status --porcelain` showed ` M corpus/knowledge/holder-assessment-boundary.md`, ` M l0-questions.md`, and untracked `corpus/fixtures/r87-probe-entry-shape/`, `corpus/fixtures/r87-probe-record-and-chain/` — sibling follow-up seats writing concurrently. Every number below is therefore measured on a pristine export:

```sh
git -C /home/vgpnk/Projects/shokunin/lore-shokunin archive 2b48ca7 | tar -x -C /tmp/jcal2/pin
```

The live-tree replay of the two sibling probe dirs is reported separately (attempt A8).

---

## Verdict recommendation — calibration axis: **improved**

Recommended verdict text: **improved**, with the harm-check record below as its bound, and with the two documentation/receipt defects in A9 and A10 carried as *integration debt*, not as calibration harm.

Justification in one line: on the delivered tree the change is strictly additive — 0 removed findings, 0 reworded findings, 0 exit-code changes across 147 corpus directories, 553 mutation cases, and 9 falsity/control constructions — and it converts the previously silent post-stop tail of an ambiguous-holder chain into explicit per-record non-assessment disclosure naming the holder field, the holder id, and the origin record.

Why not stronger than *improved*: four of my five constructed vectors show the new sentence's causal clause (`because ambiguous holder identity …`) naming a cause that does not hold (A6), and the disclosure is silent in the one suppression case where nothing at all is disclosed (A6 v4). None of that is a regression, and none of it is a resolution or canon claim; the axis moved because the delivered output is more informative than the pre-C1 output on the same inputs.

---

## A1. Inherited 133 fixture dirs: byte-identity and exit codes (confirms C1's "0 changed")

```sh
# /tmp/jcal2, pinned tree; OLD = 28706dc checker, NEW = 2b48ca7 checker
for n in <133 inherited dir names>; do
  python3 check_bible_OLD.py /tmp/jcal2/pin/corpus/fixtures/$n > a.txt
  python3 check_bible_NEW.py /tmp/jcal2/pin/corpus/fixtures/$n > b.txt
  cmp -s a.txt b.txt && [ exit codes equal ]
done
```

Observed: `inherited dirs=133  byte-identical stdout=133  differing=0  exit-code changes=0`.

**This confirms the C1 commit claim, and it is also vacuous for the changed code.** No inherited fixture ever reaches the ambiguity branch: `grep -l unassessed out/OLDxOLD.*.txt` and the same over the NEW checker both return nothing, and the pre-existing `*-ambiguous` fixtures (r7-item-ambiguous, r12-*, r18-*, r21-*, r25-*, r27-*, r31-*, r37-*, r59-*, r62-*) are about relation endpoints, places, actors, and sources, not provenance holders. H2.md:172 records the same result independently ("Across the 138-fixture corpus, no pre-existing fixture produces the new line"). The 133-tuple identity is therefore evidence of *no harm to inherited outputs*, not evidence about the new branch.

## A2. Full-corpus pinned census — the delivered delta is +11, not +5

Command: the driver embedded in `JCAL2-pinned-census.json` (enumerates every directory under `corpus/` at the pinned revision holding at least one of the five checker tables, runs both checkers, set-compares the `VIOLATION:` lines and exit codes).

Observed (`JCAL2-pinned-census.json`):

```text
dir_count            147
before_findings      281   (pre-C1 checker)
after_findings       292   (delivered checker)
added_findings        11
removed_findings       0
exit_code_flips        0
changed_dir_count      5
```

Changed dirs and line counts: `fixtures/r87-masked-break-from-ambiguous` +3, `fixtures/r87-masked-break-to-ambiguous` +3, `live/runs/round-85/probe-inputs/r85-harbor-repro` +2, `live/runs/round-85/probe-inputs/r85-isolated-ambiguous` +1, `live/runs/round-85/probe-inputs/r85-masked-ambiguous` +2.

**The C1 change does alter pre-existing tracked inputs** — three archived round-85 probe inputs, not fixtures. Additions only; nothing removed, nothing reworded, no exit code moved.

## A3. The archived live probes, one by one

```sh
python3 /tmp/jcal2/check_bible_OLD.py corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous
python3 /tmp/jcal2/check_bible_NEW.py corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous
```

| probe | pre-C1 findings | delivered findings | exit (both) |
|---|---|---|---|
| r85-control | 0 | 0 | 0 |
| r85-unique-break-control | 1 | 1 | 1 |
| r85-harbor-repro | 5 | 7 | 1 |
| r85-isolated-ambiguous | 3 | 4 | 1 |
| r85-masked-ambiguous | 3 | 5 | 1 |

Every pre-C1 line is preserved byte-for-byte and in order in the delivered output; the delivered checker only appends. `r85-masked-ambiguous` remains the case where the genuine downstream break (`provenance[2].from_holder 'harbor'` against expected `'vault'`, per the round-85 manifest) is still not reported *as a break* — C1 discloses the non-assessment, it does not detect the break. Any round record sentence of the form "the masked break is now reported" would be false; "the masked break's non-assessment is now disclosed per record" is true.

## A4. Mutation sweep — 553 adversarial inputs, 0 exit flips, 0 removals

Driver: `/tmp/jcal2/sweep.py` (loads both checkers via `importlib`, so exit codes are derived from "violations non-empty", which is what the CLI does).

Five mutations per fixture: duplicate the first entity row; duplicate the last entity row; flip an item-with-provenance to `character`; make `entities.json` unloadable; make `sources.json` unloadable. Each mutation is applied to a scratch copy under `/tmp/jcal2/mut/`.

Observed: `cases 553 | identical 540 | added-only 13 | removed_lines 0 | exit_flip 0 | reworded 0 | CRASHES: None`.

Two things follow. (a) **No exit code can move and no finding can be lost**: with 553 inputs, including inputs engineered to sit on the ambiguity boundary, there is no case where the delivered checker drops a line or flips a status. (b) A reworded finding would appear as one removal plus one addition; with zero removals anywhere in any scope, **no pre-existing finding was reworded** — that answers the mission's "altered/removed/reworded" question with a clean negative.

## A5. Overclaim check on the landed text

The landed sentence is:

```text
{record_label}: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity {field} {id!r} first occurred at {origin_label}
```

It asserts non-assessment and a cause. It does not assert a chain break, a satisfied chain, which duplicate row is real, or any canon fact; `check_bible.py:2` ("report, never resolve") holds. **No overclaim of resolution or canon.** Two wording defects, neither a resolution claim:

- **Double emission at the stop record.** The legacy item-global notice and the new line both fire at the stop record, so that record carries two near-duplicate disclosures, and the new one is self-referential there ("first occurred at <itself>"). Reproduced on `r85-isolated-ambiguous` (stop at `[2]`): 4 findings where 3 are distinct statements. JCAL1's qualification 2 records the same effect; independently confirmed here.
- **Ordering.** The disclosure for record *k* is appended at the top of the *k* loop iteration, so it precedes record *k*'s own field findings and follows record *k-1*'s. Cosmetic; deterministic.

## A6. Making the disclosure text false — five constructed vectors, each with a control

Driver and full transcripts: `JCAL2-falsity.json` (scratch trees under `/tmp/jcal2/falsity2/`). Each vector is a control pair: the *disclosure case* carries a duplicated holder id, the *control* does not, and both are otherwise identical. The control establishes that the chain comparisons are unassessed **without** the ambiguity — so the delivered sentence's causal clause is naming a cause that did not operate.

| vector | disclosure case | named cause | actual cause of non-assessment | control also unassessed? | control emits the sentence? |
|---|---|---|---|---|---|
| v1 non-item | item flipped to `character`, holder `harbor` duplicated | `ambiguous holder identity to_holder 'harbor'` | `kind != 'item'` — chain comparisons out of scope | yes (`only valid on item entities`) | no |
| v2 bad sources | `sources.json` = `{ not json`, holder duplicated | `ambiguous holder identity to_holder 'harbor'` | `sources_available` false — gate off for every record | yes (`sources.json: cannot load JSON`) | no |
| v3 malformed earlier | record `[0]` key set wrong, holder duplicated at `[1]` | `ambiguous holder identity to_holder 'harbor' first occurred at …[1]` | record `[0]` already latched the gate off | yes (`expected exactly tick, from_holder, to_holder, source_id`) | no |
| v4 duplicate item id | the item's **own** id duplicated, all holders unique | — (no sentence emitted) | `entity_id_counts[item['id']] != 1` | yes — and **nothing is disclosed at all** | no |
| v5 `first occurred at` scope | two item chains both hit duplicate id `dup` | `… first occurred at entities[6].provenance[0]` | — | the sentence is emitted, but the ambiguity first occurred earlier in the document, at `entities[3].provenance[0]` | no |

Exact delivered output for v4 (the silent case):

```text
VIOLATION: entities[4].id: duplicate entities id 'seal'
VIOLATION: relations[0].to: ambiguous entity 'seal'
2 violation(s); no canon changed
```

Two entity rows share the id `seal`, one of them is the item that owns the provenance chain; the chain comparisons are suppressed for the whole item and **no notice, no disclosure, and no unassessed line of any kind is emitted**. This is the coverage hole in the disclosure's guarantee: the disclosure is armed only by an ambiguous *holder reference*, so an item whose own id is duplicated is silently unassessed. S1.md:13 identified the precondition ("a duplicate own item ID with provenance also has no fixture"; "these preconditions suppress chain comparisons silently; there is no initial per-record unassessed notice") but did not construct it; A6 v4 is that construction, and it is unchanged by C1 (pre-C1 and delivered output are identical here).

v5 is the only vector where the *delivered sentence itself* can be read as false on a natural input: with two item chains and one duplicated entity id, the second chain's disclosure says the ambiguity "first occurred at entities[6].provenance[0]" while it in fact first occurred at `entities[3].provenance[0]`, earlier in the same document. Chain-local scope is the intended reading, but the sentence does not say "in this item's chain". Cheap fix if wanted: `first occurred in this chain at …`.

None of v1–v5 is a pre-C1/delivered behavior difference in the "removed or reworded" sense: v1–v3 and v5 are additions-only, v4 is byte-identical pre/post.

## A7. Mirror gap: a duplicate row that fails schema admission hides the ambiguity entirely (pre-existing, not C1)

`check_bible.py` counts entity ids over **admitted** rows only (`:157-160`), and a row missing a required field is dropped before that (`:64-77`). So a duplicate twin that is itself schema-invalid is invisible to both the `duplicate entities id` check and the `ambiguous entity` gate.

```sh
# scratch copy of r87-masked-break-to-ambiguous with entities[5].name deleted
python3 check_bible_NEW.py /tmp/jcal2/falsity/mirror2
```

Observed (identical under the pre-C1 checker):

```text
VIOLATION: entities[5].name: required nonempty str
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'dup', got 'mira'
2 violation(s); no canon changed
```

The input still contains two rows with `id == "dup"` — verified by re-reading the mutated file — yet the checker emits no ambiguity diagnostic and no disclosure, and asserts the chain break **unqualified**, as it would for a genuinely unique holder. This is the mirror image of the defect C1 repaired: pre-C1, ambiguity hid a break; here, a malformed twin hides the ambiguity and an unqualified break is asserted against an identity that is not unique in the file. It is **pre-existing and unchanged by C1** (byte-identical pre/post), so it is not a C1 harm — but it bounds what the C1 disclosure can be read as meaning: **absence of the disclosure is not evidence that holder identity is unique.** S1.md:18 states the mechanism ("counts use admitted entity rows; no row is selected") without this consequence.

## A8. Duplicate-identity choice: none — order-independence test

`r87-masked-break-to-ambiguous` replayed with the entity list reordered (duplicate rows first; whole list reversed):

```text
base exit 1 | dups-first exit 1 | reversed exit 1
base == dups-first : False
base == reversed   : False
```

The differences are index relabelling only (`entities[3]` ↔ `entities[5]`, `entities[2]`), with the same six findings and the same wording; exit codes identical. The checker never selects among duplicate rows — consistent with the source, which contains no selection, sorting, or `[0]`-indexing over candidate rows in the provenance branch. **No identity is chosen.**

Separately, the two sibling probe dirs present as untracked files during my run were replayed from the live tree with the pinned checkers: `r87-probe-entry-shape` produces **identical** output under the pre-C1 and delivered checkers (exit 1 both) — it is not a discriminator for C1; `r87-probe-record-and-chain` gains 3 disclosure lines (32 → 35 findings, exit 1 both). Anyone citing the I1 probe set as C1 evidence should note that only one of the two discriminates.

## A9. Receipt audit: the wave's own census artifacts disagree with the delivered artifact

`JCAL2-receipt-audit.json`. The three calibration census receipts were computed against candidate patches, not against the delivered checker.

| artifact | dirs | findings / changed | quoted added line matches the delivered wording? |
|---|---|---|---|
| `patches/X2-tuple-delta.json` | 142 | 3 changed dirs | **no** — `… unassessed for this record because holder identity 'harbor' is ambiguous at …` |
| `patches/X3-tuple-delta.json` | 142 | 2 changed dirs | **no** — `… remain unassessed because holder identity was ambiguous earlier` |
| `patches/X4-tuple-delta.json` | 142 | 274 → 279 (+5) | **yes** — `… unassessed because ambiguous holder identity to_holder 'harbor' first occurred at …` |
| JCAL2 (pinned, this seat) | 147 | 281 → 292 (+11) | — (measured directly) |

Three concrete defects, all in the *receipts*, not in the code:

1. **X2 and X3 quote text the delivered checker never emits.** Their added-line strings are candidate wording; the delivered sentence is `unassessed because ambiguous holder identity {field} {id!r} first occurred at {origin_label}`. Any round artifact that cites X2/X3 for the disclosure's wording would misquote the delivered output.
2. **X3 undercounts.** It reports 2 changed dirs and misses `r85-isolated-ambiguous` entirely, and for `r85-harbor-repro` it lists one added line where the delivered tree adds two (it omits the disclosure at the stop record itself). X2 (3 dirs, 2 lines for harbor-repro) is closer to the delivered truth; neither matches it.
3. **X4's scope excludes C1's own fixtures.** X4's 142 dirs are the 133 fixtures plus 9 live dirs as they existed at the baseline; C1 added four fixture dirs, two of which (`r87-masked-break-from-ambiguous`, `-to-ambiguous`) carry 6 of the 11 delivered added lines. X4's quoted lines are the delivered ones and its +5 is correct *for its scope*; the delivered delta over the baseline scope plus C1's own dirs is +11. X2's and X3's 142 is the same baseline scope, so all three under-report the delivered delta by the same omission.

Net: for the calibration axis the round record should cite **X4 (wording) plus this seat's pinned census (magnitude)**; X2 and X3 are superseded and should not be cited for wording.

## A10. Documentation contradiction on the delivered tree

At the judged revision `2b48ca7`, `corpus/knowledge/holder-assessment-boundary.md` is still the `28706dc` text (sha256 `a4588cbce33cad562c89e1d25017c36f2d50a73726cee9914f591f9be6ebb939`; `git log -- corpus/knowledge/holder-assessment-boundary.md` shows only `28706dc`). Its ambiguous-holder contract row (`:73`) reads:

```text
… PLUS, at the first ambiguous-holder record only, the single `…continuity and tick-order comparisons unassessed…` notice.
```

The delivered checker emits that notice **and** a per-record disclosure at the stop record and at every later record (`r85-masked-ambiguous`: 3 → 5 findings; `r87-masked-break-to-ambiguous`: 3 → 6). So at the delivered revision the lane's own boundary document contradicts the lane's own checker, and its `verified-at:` line still reads `STATIC PENDING PARENT RUNTIME … no execution has yet demonstrated them`. This is exactly the refresh the parent listed as outstanding: I2's uncommitted working-tree edit (sha256 `5c8c3fe67dde545cefbda2fcd8963c55b527c5a5ce50860eba32ceb8efcb3b6d`) already replaces `:73` with the per-record wording and re-stamps `verified-at: RUNTIME REPLAYED … 2b48ca7`. **Integration consequence: the C1 calibration claim should not be recorded as landed until I2's boundary-doc edit is part of the round's delivered tree**; as of `2b48ca7` the contradiction is live. CB1's `integration_watch.c1_after_state` predicted precisely this.

## A11. The sealed round-85 receipts were already stale before C1 (independently reproduced; H4.md has it)

```sh
git -C /home/vgpnk/Projects/shokunin/lore-shokunin show 174c062:corpus/fixtures/check_bible.py > /tmp/jcal2/check_bible_R85.py
sha256sum /tmp/jcal2/check_bible_R85.py   # 88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81
                                          # == corpus/live/runs/round-85/manifest.txt pin
```

All five `corpus/live/runs/round-85/probe-r85-*.txt` receipts reproduce **exactly** (body and exit code) under that r85-era checker, and do **not** reproduce under `28706dc`:

| probe | receipt (r85 checker) | at 28706dc | at 2b48ca7 |
|---|---|---|---|
| r85-control | matches (0) | matches (0) | matches (0) |
| r85-unique-break-control | matches (1) | matches (1) | matches (1) |
| r85-harbor-repro | matches (1, 2 findings) | 5 findings | 7 findings |
| r85-isolated-ambiguous | matches (1, 1 finding) | 3 findings | 4 findings |
| r85-masked-ambiguous | matches (1, 1 finding) | 3 findings | 5 findings |

The drift originates in the `28706dc` "harden check_bible" commit, not in C1; C1 widens it. H4.md:174-198 reports the same finding with the same three hashes, so this is a confirmation, not a new discovery — recorded here so the round record does not present `probe-r85-*.txt` as the C1 before-state.

---

## Attempt ledger

| # | attempt | result |
|---|---|---|
| A1 | 133 inherited fixture dirs, stdout + exit codes, pinned tree | 133/133 byte-identical, 0 exit changes — **confirms, and vacuous for the new branch** |
| A2 | full-corpus pinned census (147 dirs) | 281 → 292, **+11**, 0 removed, 0 exit flips, 5 changed dirs |
| A3 | 5 archived r85 live probes individually | 3 changed, additions only, no exit movement |
| A4 | 553-case mutation sweep (5 mutations × 138 fixtures, minus skips) | 0 exit flips, 0 removed, 0 reworded, 540 identical, 13 added-only |
| A5 | overclaim hunt on the landed sentence | no resolution/canon claim; two wording defects (double emission at the stop record, ordering) |
| A6 | 5 falsity vectors with controls | v1–v3: causal clause names a cause the control disproves. v4: **silently unassessed, nothing disclosed**. v5: `first occurred at` can be read as false document-wide |
| A7 | schema-invalid duplicate twin | ambiguity gate blind, unqualified chain break asserted; **pre-existing, unchanged by C1**; bounds the disclosure's meaning |
| A8 | duplicate-identity choice: reorder test | no identity chosen; output identical modulo index labels; `r87-probe-entry-shape` does not discriminate C1 |
| A9 | receipt audit of X2/X3/X4 | X2/X3 quote candidate wording; X3 undercounts; X4 scope omits C1's own fixtures; delivered magnitude is +11 |
| A10 | boundary doc vs delivered checker at 2b48ca7 | `holder-assessment-boundary.md:73` contradicts the delivered checker; I2's uncommitted edit fixes it |
| A11 | sealed r85 receipts vs three checker generations | receipts reproduce only under the r85 checker; drift predates C1 (H4.md concurs) |

## Open items handed to integration (not this seat's to write)

1. Land I2's boundary-doc edit, or the delivered tree's knowledge doc contradicts the delivered checker (A10).
2. Cite X4 + this seat's pinned census for the calibration magnitude; X2/X3 must not be cited for the disclosure's wording (A9).
3. Do not describe C1 as reporting the masked break — it discloses the non-assessment only (A3).
4. If the lane wants the disclosure's causal clause to be true in all reachable states, the fix is either to emit it only when the holder ambiguity is what latched the gate, or to word it without `because`; and to emit *something* for the duplicate-own-id case (A6 v4). Both are new work, not regressions.
