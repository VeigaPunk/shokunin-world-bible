# F26 — verdict-adjacency

**Role:** independent per-axis verdict for **ADJACENCY** on the r94 WORK candidate `abbc3e0` (baseline `9c2eea3`, follow-up declaration `65a9329`). Checks run read-only from the lane root on 2026-10-17 ~15:39–15:42 -03. No corpus/other-seat files were modified; this report is the seat's only write.

**Axis definition used:** province-clean (PROVINCE.md:3-11 — fictional-world records + sourced inspiration; refuses unsupported canon, silent contradiction resolution, real-world rights claims, game-mechanics verification); no sibling writes (other lane repos and other seats' artifacts untouched); mythology remains editorial (external comparators never become in-world witnesses or canon); no canon/rights/mechanics bleed.

## 1. Province-clean — PASS

- The candidate diff is additions plus two append-only documentation files:

  ```
  $ git diff --name-status 9c2eea3..abbc3e0 | awk '{print $1}' | sort | uniq -c
      152 A
        2 M
  $ git diff --name-status 9c2eea3..abbc3e0 | grep -v '^A'
  M	LOG.md
  M	SCORECARD.md
  $ git diff --shortstat 9c2eea3..abbc3e0
   154 files changed, 7554 insertions(+)
  ```

  Zero deletions: both `M` files are pure appends (`git diff 9c2eea3..abbc3e0 -- LOG.md SCORECARD.md | grep -E '^-[^-]'` → empty; same command on `65a9329` for LOG.md/README.md → empty).

- Every changed path is inside the round's allowed scope. Fixed prefix check (first attempt used a broken `^…$` alternation and was discarded):

  ```
  $ git diff --name-only 9c2eea3..abbc3e0 | grep -vE '^(\.ufo/waves/round-94/|corpus/fixtures/r94-paired-crossing/|corpus/knowledge/r94-cross-myth-design-comparison\.md|corpus/tools/map_obligations\.py|corpus/tools/map-obligations-contract\.json|LOG\.md|SCORECARD\.md)'
  (empty)
  ```

- No past wave, gate, or boundary file touched: `git diff --name-only 9c2eea3..abbc3e0 -- .ufo/waves/ | grep -v round-94` → empty; `git diff --quiet 9c2eea3..abbc3e0 -- SHONEN.md PROVINCE.md SKILL.md` → exit `0`; `git diff --name-only 9c2eea3..HEAD -- corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r87-myth-cluster` → empty.
- The new content itself is in-province: entities/relations/timeline fixture, a sourced-inspiration design-comparison record, and a map-completeness tool whose own contract scopes it to "no entailment, fidelity, chronology, rights, permission, or canon judgment" (`corpus/tools/map-obligations-contract.json:3`).
- The frozen r93 snapshot used by `--frozen` is a byte copy, not a mutation of the live fixture: `cmp` on `entities.json`, `relations.json`, `timeline.json`, `claim-excerpt-map.md` (live `corpus/fixtures/r93-m2-kojiki-cluster/` vs `.ufo/waves/round-94/frozen/map-obligations-r93/`) → `IDENTICAL` for all four.

## 2. No sibling writes — PASS

- Working tree is clean except the follow-up scratch dir: `git status --porcelain` → `?? .ufo/waves/round-94/followup/` (the live follow-up wave's own directory). No leftover product edits.
- No lore r94 string leaked into any sibling lane: `grep -rl "r94-paired-crossing\|crossing-minute\|r94-cross-myth" /home/vgpnk/Projects/shokunin/*-shokunin --include='*.md' --include='*.json' --include='*.py' | grep -v lore-shokunin` → empty.
- Sibling mtime sweep after 14:30 (`find <sibling> -newermt "2026-10-17 14:30"`) reported only `kotodama-shokunin` and `lore-shokunin`. kotodama's hits are its own round-6 work: its tree is clean (`git -C ../kotodama-shokunin status --porcelain | wc -l` → `0`) and the files belong to its own commits (`b815bf4` 15:38 "train: admit round-6 bounded source freshness checks", `19c5a86` 15:19 for `corpus/lessons/round-6-sources/07.json`). No other sibling had any write in the window.
- Round scripts do not write outside the lane: `grep -n "\.\./\|/home/vgpnk\|shutil.copy\|open(" .ufo/waves/round-94/work/*.py | grep -v "\.ufo/waves/round-94/work\|corpus/"` → empty.
- Within the repo, all 152 added files sit under `.ufo/waves/round-94/` (leaf artifacts), `corpus/fixtures/r94-paired-crossing/`, `corpus/knowledge/r94-cross-myth-design-comparison.md`, `corpus/tools/map_obligations.py`, `corpus/tools/map-obligations-contract.json` — no other seat's report or other wave edited.
- Nuance (observed, not a violation): the new tool's `--self-test` scratch is created under the repo root — `corpus/tools/map_obligations.py:604`: `with tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT) as temporary:`. I caught one live instance mid-run (`find . -maxdepth 1 -name 'map-obligations-self-test*'` at ~15:39 listed `map-obligations-self-test-3kp18777/`; `ls -ld` a minute later → `No such file or directory`). It is auto-removed on exit and left no persistent artifact (`git status --porcelain` clean apart from `followup/`). All write-capable calls in the tool are inside self-test helpers (`write_test_fixture:457`, `prepare_test_frozen:487`, `prepare_test_case:518`); a normal invocation wrote nothing — before/after `git status --porcelain` diff was empty, and the run itself returned `OBLIGATIONS raw=14 mapped=14` / `RESULT PASS` / `exit=0`.
- mtime-only touches predating the WORK wave, content-identical: `corpus/fixtures/r93-m2-kojiki-cluster/{claim-excerpt-map,inspiration-note,kojiki-chamberlain-excerpt,README}.md`, `corpus/knowledge/reference-ledger.md`, `corpus/tools/README.md`, `l0-questions.md` have mtimes 14:00–14:26 (wave-spec.md mtime is 14:39, checkpoint 15:19), but `git diff 9c2eea3..HEAD --stat -- <those paths>` → empty, i.e. zero content change across the round window. Not attributable to any r94 seat.

## 3. Mythology remains editorial — PASS

- The new comparison record self-classifies: `corpus/knowledge/r94-cross-myth-design-comparison.md:7` — "This is a sourced editorial decision record, not merged canon or a cultural-history claim… An outside passage never becomes an in-world witness"; line 17 — "not… evidence that an external passage supports fictional canon"; line 25 — "The actual r94 consequence is supported only by its authored `crossing-minute`; no outside text is an in-world source or witness." ETCSL stays `external-only` and "supports none of the r94 JSON" (line 25); the Spence English passage "does not support the meeting, agreement, dependency, or route mark" (line 25). External URLs were honestly recorded as unfetched (line 2).
- All 14 JSON obligations cite in-world sources (`paired-clock`, `crossing-minute` — `claim-excerpt-map.md:20-35`); the two Spence comparisons are separately labeled editorial rows that "do not make Spence an in-world witness, assign cultural meaning, or add canon" (`claim-excerpt-map.md:37-44`).
- The authored in-world minute imports no mythological figures: `fictional-excerpts.md:17-20` names only Chalk Stair, Aru, Evin, Quiet Rise, Salt Court. The fixture README bounds the continuation: "It supplies no in-world witness, cultural authority, or fictional canon" (`README.md:17`); the inspiration note says it "imports no named beings, plot, ritual, or cultural rule" and "is not an in-world source and supplies no fictional canon" (`inspiration-note.md:7,21`).

## 4. No canon/rights/mechanics bleed — PASS

- Canon: every new source-attributed JSON record carries an in-world `source_id` (read of `entities.json`, `relations.json`, `timeline.json`, `sources.json`), `contradictions.json` is `[]` (no silent resolution invented), and the relation is bounded in-language — "It is not evidence of an alliance, a continuing practice, or perpetual performance" (`README.md:9`; `sources.json:18` reliability note).
- Rights/training: a keyword scan (`grep -rn -iE "public domain|copyright|licen[cs]|permission|canon|mechanic|gameplay|damage|hit point|\bhp\b|quest|stats"` over all new r94 files) found rights/canon terms **only in explicit not-assessed/not-canon disclaimers** (`inspiration-note.md:15,19` — rights status undetermined, AI-training permission "has not been assessed or established"; `README.md:19`, `claim-excerpt-map.md:50`, knowledge doc line 17, contract scope). No "public domain" claim and no positive rights finding exists anywhere in the additions.
- Mechanics: zero mechanics terms in any new r94 file (same scan; matches shown are all `noncanonical_*` pointer-grammar identifiers in the tool). PROVINCE.md:9's refusal of game-mechanics verification is respected; SKILL.md:6-11 keeps rights/permission open rather than adjudicated in-lane.

## Limits and out-of-scope observations

- Sibling-write coverage is a bounded mtime sweep plus string-leak grep and clean-status checks of sibling trees, not a full cross-repo commit audit; concurrent sibling lanes (e.g. kotodama round-6) are active on their own repos.
- The mtime-only touches listed above are content-identical but their writer is unattributed; they predate the WORK wave.
- The transient self-test scratch under the repo root is documented above; it is the tool's designed isolation mechanism, cleaned on exit, and no live fixture or baseline was regenerated.
- This seat did not re-adjudicate source/proposition content (other FOLLOW-UP seats) or the W20 failed-output provenance gap (receipt/verdict seats); neither was used as evidence here.

**Bottom line: PASS — the r94 WORK candidate is province-clean, writes only its own lane's allowed paths with append-only documentation, keeps all mythology comparators editorial, and shows no canon/rights/mechanics bleed; the only nuance observed is the tool's auto-removed transient self-test scratch under the repo root (map_obligations.py:604), which left no persistent artifact.**
