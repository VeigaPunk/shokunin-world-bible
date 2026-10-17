# JCAL3 — Fixture/README judge (r91 follow-up)

Seat JCAL3, world-bible lane, round-91 follow-up. Verdict evidence: delivered tree at
head `c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7` (tree clean). Checker under judgment:
`corpus/fixtures/check_bible.py`; delivered file = `a7c6a17` blob = `c2ab3d0` blob,
SHA-256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`.
e97613c control blob `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`
(extracted to scratch `/tmp/jcal3/check_976.py`; scratch-only, per rules).

## Work performed

- Dependency wait-checks (committed pattern, 2×60 s): HEAD polled at
  `2026-10-17T08:32:34-03:00` and `2026-10-17T08:33:34-03:00`; both reads `c2ab3d0…`.
  Dependencies present; no gap.
- Both-checker replay of the two new fixtures. Delivered checker run in-tree; e97613c
  checker extracted with `git show e97613c:corpus/fixtures/check_bible.py` to scratch and
  run against the same fixture dirs. stdout/stderr/exit captured separately
  (`/tmp/jcal3/{deliv,old}-{null,tick}.{out,err}`).
- Line-by-line README verification: regex-extracted each README's
  `## Expected output with e97613c` / `## Expected output with the delivered checker`
  blocks and compared bytes + SHA-256 against the actual runs (`/tmp/jcal3/readme_compare.py`).
- Read both READMEs, all ten fixture JSON files, and the checker source in full; verified the
  README construction claims against data (item-chain-valid copy diff; residual-holder and
  tick-order trace).
- JSON validity: `python3 -c "json.load(...)"` on all 10 fixture JSON files; checker's
  duplicate-member hook as a second validator (runs emit no load errors for these fixtures).
- Corpus-wide id audit: raw id scan over all 166 fixture dirs (`audit_ids.py`),
  delivered-checker run over all 166 fixtures in one loop (`allcheck.txt`), and
  cross-fixture replay counts for the 8 ids used by the new fixtures (`id_replay.py`).
- C9 watch audit: hash pins at file/a7c6a17/c2ab3d0/e97613c; r91 no-change diff;
  landed-file ↔ S1 patch byte-compare; per-claim replay (hash command, null/tick outputs);
  trigger and owner read; owner cross-checked against wave-spec and `S1.md`.
- Census/delta check: `git diff --name-status a7c6a17 c2ab3d0 -- corpus/fixtures`;
  directory counts at both commits; `diff -r item-chain-valid r91-c1-null-chain`.
- Cross-checked sibling receipts `H4-c1-discrimination.json`, `H4-census.json`,
  `JCAL5-delta.json` (they carry the same per-fixture output hashes measured here).

## Before → after measurements

"Before" = claims/expectation blocks and the pre-r91 e97613c control; "after" = measured at
`c2ab3d0`. All commands run from `lore-shokunin/`.

1. Checker pins (before→after):
   - `sha256sum corpus/fixtures/check_bible.py` → `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`
   - `git show a7c6a17:corpus/fixtures/check_bible.py | sha256sum` → same `ff9fd2aa…`
   - `git diff --stat a7c6a17 c2ab3d0 -- corpus/fixtures/check_bible.py` → empty (exit 0);
     r91 did not touch the checker.
   - `git show e97613c:… | sha256sum` → `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`
     (equals the hash pinned in B3-before-state.json).

2. README expectation blocks vs actual per-checker runs — `python3 /tmp/jcal3/readme_compare.py` → `ALL_MATCH` (byte-identical, expected==actual SHA-256):
   - null-chain × e97613c: `3a337ba4bba9c829f9b2bba9657e61d8838ad491d44c0861fa1d6f9d40e05c89`
     (this equals B3-before-state.json's `stdout_sha256` for its null probe — the shipped
     fixture reproduces B3's scratch probe byte-for-byte).
   - null-chain × delivered: `615dc0564f531352a574ef2f53c48be42f4e53ad1fac4aa88756e4bba2fada5b`
   - tick-unresolved × e97613c: `71b4ea433d85ba52f11482a5d089c564641702989763ced39d61c5eee3748e85`
   - tick-unresolved × delivered: `d754e96f7c01e6fb6eff12168a732d5a6125f428a9207bd74fc49bbdcbb25d88`
   - all four runs: exit 1, stderr 0 bytes (matches every "exit 1; stderr empty" claim).

3. Actual outputs (delivered tree):
   - `python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain` →
     `VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None`
     `1 violation(s); no canon changed`
   - `python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved` →
     line1 `VIOLATION: entities[1].first_appearance: required nonempty str`
     line2 `VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3`
     line3 `VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'`
     `3 violation(s); no canon changed`

4. Discrimination exactly on the repaired lines:
   - `diff old-null.out deliv-null.out` → `1c1` only; the count line is byte-identical.
   - `diff old-tick.out deliv-tick.out` → `2c2` only; `first_appearance` and the qualified
     chain-break lines are byte-identical; only the tick line changes (hedged →
     `provenance tick 1 must be greater than previous tick 3`).

5. README construction claims:
   - `diff -r corpus/fixtures/item-chain-valid corpus/fixtures/r91-c1-null-chain` → only
     `entities.json` seal provenance rows differ (two hunks: row record replaced), plus
     README.md added; sources/relations/timeline/contradictions identical. Delivered run
     emits exactly the one intended null-`from_holder` violation.
   - Tick fixture data confirms the README trace: `f3-dup` twice raw (rows 1 and 2, row 1
     invalid `first_appearance: ""`), once in the resolved index; record 0 `tick 3` →
     `to_holder f3-dup`; record 1 `tick 1`, `from_holder mira`.

6. JSON validity: all 10 files (`contradictions/entities/relations/sources/timeline` × 2)
   parse as JSON arrays; no duplicate object members (checker hook); no load errors.
   `VALID corpus/fixtures/r91-c1-*/…` × 10.

7. Corpus-wide id audit (166 dirs):
   - Raw scan: 37 duplicate-id groups total; 36 are pre-existing by-design fixtures
     (e.g. r18-*, r25-*, r27-*, r87-*, r89-fn2-unresolved-chain-break, r9-dup-*).
     The 37th is the new `r91-c1-tick-unresolved` (`f3-dup` rows [1,2]). `r91-c1-null-chain`
     has zero duplicates.
   - The new duplicate is shadowed: row 1 is invalid, so it never enters the resolved index;
     the checker emits **no** duplicate-id violation for this fixture (the ambiguity surfaces
     exactly as designed: qualified chain-break with raw/index counts). README documents this
     as the "deliberate invalid-duplicate row diagnostic".
   - All-166 delivered run: 166 fixture blocks, `exit0=32 exit1=134` (matches JCAL5's
     independent shuffled-driver summary); the two new fixtures' blocks match the READMEs.
   - Cross-fixture replay: `f3-dup`/`f3-seal` appear in exactly 3 fixtures
     (r89-fn2-control, r89-fn2-unresolved-chain-break, r91-c1-tick-unresolved — the r89-fn2
     lineage). Shared scaffolding ids are the corpus norm: `mira` 141/166, `harbor` 140,
     `seal` 135, `tower` 134, `courier-log` 132, `archive-ledger` 127. So "corpus-wide id
     uniqueness" holds per dataset (valid rows) but is not a cross-fixture invariant.

8. Census/delta (independent of B1/B2):
   - `git ls-tree -d a7c6a17 corpus/fixtures | wc -l` → 164; at `c2ab3d0` → 166 (2 new).
   - `git diff --name-status a7c6a17 c2ab3d0 -- corpus/fixtures` → 12 `A` (the two new
     fixture dirs), 3 `M`, 0 `D`. The `M` files are C2's documented wording fix:
     `r87-myth-cluster/claim-excerpt-map.md`, `r88-m3-maya-cluster/claim-excerpt-map.md`,
     `r89-inspiration-paraphrase/claim-to-excerpt-map.md` (no dataset JSON changed).
     "0 changed + 2 new of 166" is exact at the dataset level; at file level 3 pre-existing
     fixture docs were modified (documented by C2, identical in JCAL5's file_level_delta).

9. C9 watch (`corpus/knowledge/r91-c9-watch.md`, added in `6332115`):
   - `sha256sum` → `698a84567e8d34dffed8276af537ff7385099e2a52943dd4823c29e2df98ad2c`;
     equal at `6332115` and `c2ab3d0` blobs (no post-landing edit).
   - Landed file vs `patches/S1-r91-c9-watch.patch` (content lines): `diff` exit 0 —
     byte-identical; S1 patch delivered its designed artifact.
   - Hash-pin claim: `sha256sum corpus/fixtures/check_bible.py` prints exactly the pinned
     `ff9fd2aa…` (verified in step 1).
   - Probe claim: null fixture reports the exact substring + exit 1 + one violation ✓;
     tick fixture emits the definite line + retains the qualified line + exit 1 + three
     violations including the invalid-duplicate diagnostic ✓ (step 3).
   - e97613c-pin claim: B3-before-state.json hedges the null line with a **byte-identical**
     stdout (hash match) and hedges the tick line at shape level — B3's scratch probe used
     ticks 2→1 ("previous tick 2") while the shipped fixture uses 3→1 ("previous tick 3").
     The READMEs and this replay pin the shipped fixture byte-exactly.

## Findings & named debt

Axis verdicts (this seat's scope; evidence above, delivered tree only):

- **C1 calibration — fixtures + READMEs: improved (bounded).** Both-checker expectation
  blocks are byte-exact; the old→delivered diffs isolate exactly the repaired lines; the
  fixtures are valid, well-formed, and their construction prose matches the data.
- **C1 C9 watch — pin/trigger/owner: improved (bounded).** Hash pin correct at every
  checkpoint; the falsification trigger is specific (four conjunctive gates, probe template
  with control, required record list, decision rule, explicit "no automatic checker change");
  owner named (S1) with a defined handoff.
- **Fixture hygiene / id uniqueness: r91 additions improved; corpus unchanged (no harm).**
  Ten of ten JSON files valid; no new duplicate-id violation introduced; the single raw
  duplicate is by design and shadowed; no id outside the established scaffolding.
- **Census precision: verified improved.** "0 changed + 2 new of 166" is exact for datasets;
  the 3 modified files are C2's documented doc-level edits.
- Not judged by this seat: C2 support-command hardening, C3 R8/R9/R10 decisions
  (other seats' lanes).

Named debt / notes (none blocking):

1. (Minor, r91) `B3-before-state.json`'s tick receipt is shape-exact but not byte-exact
   against the shipped fixture ("previous tick 2" vs "previous tick 3"). The byte-exact
   e97613c replay now lives in the READMEs and hashes above; a future replay of B3's
   scratch path must not be mistaken for a fixture mismatch.
2. The C9 watch hands off to "the next C1 calibration owner at closure" — role-level. The
   r91 closure record should name the successor explicitly so the watch has a concrete
   bearer.
3. "Corpus-wide id uniqueness" is a per-dataset property here, not a corpus invariant
   (shared scaffolding ids recur across fixtures). If a cross-fixture registry expectation
   is ever added, 36 pre-existing raw-duplicate groups plus `r91-c1-tick-unresolved`'s
   `f3-dup` pair would each need a declared exemption.

Nothing found to reopen or repair; no fixture/checker change is requested by this seat.

## Handoff

- Wrote `lore-shokunin/.ufo/waves/round-91/followup/JCAL3.md` (this report) and
  `lore-shokunin/.ufo/waves/round-91/followup/JCAL3-receipt.json` (machine-readable
  hashes/verdicts). These are the only tracked writes; no commits, no pushes.
- Sibling repos untouched; no l0-questions.md or P1-report writes (not authorized).
- Scratch `/tmp/jcal3` swept at close; every script and output hash is recorded above.
- Parent/closure: fold the three axis verdicts into the r91 closure; consider naming the
  C9 successor (note 2); no dependency on further seats for this seat's scope.