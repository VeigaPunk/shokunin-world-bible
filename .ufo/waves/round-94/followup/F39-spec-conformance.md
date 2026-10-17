# F39 — spec-conformance (round-94 FOLLOW-UP)

**Seat role:** FOLLOW-UP leaf, spec-conformance. Scope: map **every** acceptance line of `.ufo/waves/round-94/wave-spec.md` C1 (lines 9–19) and C2 (lines 21–27), plus the invariants/handoff block (lines 29–35), to **demonstrated** evidence — either a follow-up report that shows it, or my own replay — or mark it **NOT demonstrated**. Includes the three seat-named items: no modified existing bytes, report-last discipline, W20 gap acknowledged.

**Environment pin:** lane HEAD `65a93298cb100fdbf5732ac6de55f01a683c02d8`; WORK candidate `abbc3e0`; baseline `9c2eea3`. `git merge-base --is-ancestor 9c2eea3 abbc3e0` → YES; `abbc3e0 → 65a9329` → YES. `git status --porcelain` → `?? .ufo/waves/round-94/followup/` only (no tracked-file drift), so every command below ran on the committed candidate bytes. All commands run from the lane root with `python3`. Only this report file was written; my temp probes used `/tmp` and were deleted.

**Follow-up reports available at write time (read for cross-evidence, not modified):** `F01`, `F02`, `F03`, `F04`, `F05`, `F06`, `F07`, `F08`, `F09`, `F10`, `F11`, `F12`, `F13`, `F14`, `F15`, `F16`, `F17`, `F18`, `F19`, `F20`, `F22`, `F23`, `F24`, `F25`, `F26`, `F28`, `F30`, `F31`, `F32`, `F33`, `F34`, `F35`, `F36`, `F37`, `F38` (all `.md` in `.ufo/waves/round-94/followup/` at 15:47; F21/F27/F29/F40 absent at that time). The two verification rows this seat had initially marked **NOT demonstrated** (V4/V7) were re-checked against the newly arrived F04/F05 and are now DEMONSTRATED — the table below reflects the final state.

---

## A. C1 — acceptance lines (wave-spec.md:9–17)

| # | Spec line | Acceptance item | Demonstrated evidence | Verdict |
|---|---|---|---|---|
| C1-1 | `:11` | NEW fixture at `corpus/fixtures/r94-paired-crossing/` | `find corpus/fixtures/r94-paired-crossing -type f` → 10 files; `git diff --name-status 9c2eea3 abbc3e0 -- corpus/fixtures/` → only `A` rows for this directory | DEMONSTRATED |
| C1-2 | `:11` | Preserves the r88 paired-register snapshot and all other existing corpus bytes | `git diff --name-status 9c2eea3 abbc3e0` → `152 A` + `2 M` (`LOG.md`, `SCORECARD.md` only); `git diff --name-status 9c2eea3 abbc3e0 -- corpus/fixtures/ \| grep -v r94-paired-crossing` → empty; `git diff --name-status 9c2eea3 HEAD -- corpus/tools/` → additions only; F33 §4 corroborates (r87/r88 fixtures + `support_check.py` byte-identical) | DEMONSTRATED |
| C1-3 | `:11` | Explicit continuation of `r88-m3-maya-cluster`, not an unrelated cluster or silent history change | `corpus/fixtures/r94-paired-crossing/README.md:1-4` states it; `sources.json` shares `paired-clock`/`veil-verse` with r88 and adds only `crossing-minute`; my parsed comparison: `r94 entities[0:4]==r88 entities: True`, `r94 timeline[0:2]==r88 timeline: True`; `source-excerpt.md` and `inspiration-note.md` byte-identical to r88 (`diff` → IDENTICAL) | DEMONSTRATED |
| C1-4 | `:13` | Before 4 entities / 0 relations / 2 tick-9 events at distinct places → after 5 / 1 / 3 | My own `json.load`: `counts r94 e/r/t: 5 1 3`; `r88 counts: 4 0 2`; `t9 places: quiet-rise salt-court`. F01 §2 (independent seat) same result | DEMONSTRATED |
| C1-5 | `:13` | One source-supported agreement/co-stewardship relation | `relations.json` = `{"from":"aru","to":"evin","type":"agreed_co_stewardship_for_this_crossing","source_id":"crossing-minute"}`; `map_obligations.py` r94 → `OBLIGATIONS raw=14 mapped=14 / RESULT PASS`; `support_check.py` → `PASS J11 … anchor=found` | DEMONSTRATED |
| C1-6 | `:13` | Tick-10 crossing decision depending explicitly on **BOTH** named tick-9 entries | `timeline.json` row 2: `tick 10`, `depends_on: ['aru-ninth-bell','evin-ninth-bell']` (my parsed print); F01 §3 asserts set-equality True + zero dangling refs | DEMONSTRATED |
| C1-7 | `:13` | New authored in-world minute supplies place identity, agreement, action, actors, relative ordering | `corpus/fixtures/r94-paired-crossing/fictional-excerpts.md:17-20` (place: "named rain-dark crossing between Quiet Rise and Salt Court"; ordering: "After both Tick 9 entries above"; actors: "Aru and Evin"; agreement: "share stewardship of the Chalk Stair"; action: "chalked one temporary route mark"); `sources.json` entry `crossing-minute` | DEMONSTRATED |
| C1-8 | `:13` | Inherited four entities and two events parsed-value identical | `r94 entities[0:4]==r88 entities: True`, `r94 timeline[0:2]==r88 timeline: True` (my run); inherited `sources.json` records `equal: True` (my run); `fictional-excerpts.md` lines 1–13 `diff` → IDENTICAL; F01 §4 reports 0 field-level diffs and identical key order | DEMONSTRATED |
| C1-9 | `:13` | Preserve inherited excerpts and bibliography | `diff r88/source-excerpt.md r94/source-excerpt.md` → IDENTICAL; `diff r88/inspiration-note.md r94/inspiration-note.md` → IDENTICAL; `diff <(sed -n '1,13p' r88/fictional-excerpts.md) <(sed -n '1,13p' r94/fictional-excerpts.md)` → IDENTICAL | DEMONSTRATED |
| C1-10 | `:13` | Map every old and new source-attributed record with canonical `file.json#/pointer`, exact in-span anchors, R9 modes | `claim-excerpt-map.md:5` expected inventory 14/2/16/12; my independent parse: 14 `J` rows each with exactly one inline-code `*.json#/…` pointer (5 `entities.json#/N/first_appearance`, 5 `entities.json#/N/claims/0`, 1 `relations.json#/0`, 3 `timeline.json#/N`) + 2 `S` rows in a separate section; `support_check.py` → `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12 … MODES 16/16; VALIDATED-ROWS 16/16; RESULT PASS` exit 0 | DEMONSTRATED |
| C1-11 | `:13` | Expected 14 obligations (5 first-appearance + 5 claims + 1 relation + 3 events) plus separate editorial comparisons | My own enumeration: `first_appearance 5 claims 5 relations 1 events 3 TOTAL 14`; tool r94 run `raw=14 mapped=14`; editorial rows are a separately headed section (`claim-excerpt-map.md:37`, "not JSON facts") | DEMONSTRATED |
| C1-12 | `:15` | Relation records the supported agreement only — not perpetual performance or an alliance | `relations.json` type `agreed_co_stewardship_for_this_crossing`; `sources.json#/2` reliability note ("not evidence of continuing performance, a standing alliance, or an external historical fact"); `README.md:9` ("It is not evidence of an alliance, a continuing practice, or perpetual performance"); `claim-excerpt-map.md:48` repeats the bound | DEMONSTRATED |
| C1-13 | `:15` | Tick/ID/dependency encodings distinguished from literal excerpt words | `README.md:11` ("The integer ticks and event-ID edges in `timeline.json` are editorial encodings … not literal JSON wording"); `claim-excerpt-map.md:48` same statement; the minute text carries no JSON syntax | DEMONSTRATED |
| C1-14 | `:15` | Shared r88 referents/source IDs intentional, explicitly compared, path-qualified | `README.md:5-7` namespace section (`(r88-m3-maya-cluster, paired-clock)` vs `(r94-paired-crossing, paired-clock)`); map columns "In-world source ID" + "Path-qualified source namespace"; `claim-excerpt-map.md:3` states IDs stay cluster-local and are qualified as pairs | DEMONSTRATED |
| C1-15 | `:15` | Unchanged facts are not contradictions | `contradictions.json` → `[]` in both fixtures (cat); inherited records parsed-equal (C1-8) | DEMONSTRATED |
| C1-16 | `:15` | New occasion must not rewrite the old tick-9 accounts or conflate their places | Inherited events parsed-identical with `place_id` `quiet-rise` / `salt-court` distinct; new event at a third place `chalk-stair`; F01 §3 dangling/self-reference scan → NONE | DEMONSTRATED |
| C1-17 | `:17` | Knowledge record names exact ETCSL, Spence, Kojiki comparators | `corpus/knowledge/r94-cross-myth-design-comparison.md:11-13` — ETCSL 1.4.1 lines 122–163; Spence 1913 Ch. V "The Creation-Story" p. 209; Kojiki Part III "Door of the Heavenly Rock-Dwelling" (Chamberlain 1882) | DEMONSTRATED |
| C1-18 | `:17` | …their delivered/external status | Same rows: `External-only` (ETCSL) / `Delivered mediated English` (Spence) / `Delivered translation` (Kojiki) — `grep -o` counts 1/1/1 | DEMONSTRATED |
| C1-19 | `:17` | …the supported fictional source, and where each analogy stops | Each row names the fictional support (`lowwater-hymn`, `veil-verse`, `m2-record-archive`) with file:line pointers, and each row ends with an explicit "Inference stop" clause (header `Inference stop` present, `:10`) | DEMONSTRATED |
| C1-20 | `:17` | Editorial design decisions, not cultural facts / shared canon / rights findings / taste claims | `r94-cross-myth-design-comparison.md:7` ("not merged canon or a cultural-history claim … never becomes an in-world witness"); "Cross-row limits" paragraph keeps rights and AI-training permission unassessed | DEMONSTRATED |
| C1-21 | `:17` | New shared-crossing consequence uses the existing Spence naming/place contrast without importing mythology as an in-world witness | `r94-cross-myth-design-comparison.md:19-26` addendum ("Spence's English passage does not support the meeting, agreement, dependency, or route mark"; consequence "supported only by its authored `crossing-minute`"); fixture `sources.json` contains no external source; map R9 declaration marks `source-excerpt.md` as "Delivered external comparison only; not an in-world source or support for JSON facts" | DEMONSTRATED |

## B. C1 — verification paragraph (wave-spec.md:19)

| # | Verification item | Demonstrated evidence | Verdict |
|---|---|---|---|
| V1 | Parsed counts 4/0/2→5/1/3 | My `json.load` run (C1-4); F01 §2 | DEMONSTRATED |
| V2 | Inherited-record equality | My parsed comparison (C1-8); F01 §4 (0 field-level diffs, key order identical) | DEMONSTRATED |
| V3 | Explicit two-event dependency | C1-6 (my parsed `depends_on`); F01 §3 | DEMONSTRATED |
| V4 | Excerpt proposition review | Author-side review exists (`r94-cross-myth-design-comparison.md:27-33`, self-labelled "author seat only"), and the **independent** review is now delivered by F04 (`F04-c1-whole-claim.md`, "independent manual whole-proposition review", bottom line **PASS**: "all four new `crossing-minute` obligations and every new actor/place/agreement proposition are entailed by `fictional-excerpts.md:17-20` or by explicitly labeled editorial metadata … with no contents, perpetual-performance, or alliance overreach"). F01 §5 had declared whole-claim entailment out of its own scope. | DEMONSTRATED |
| V5 | `check_bible.py` CLEAN | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing` → `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0 (my run); F01 §1 adds empty stderr + r88 control | DEMONSTRATED |
| V6 | `support_check.py` PASS over the declared mapped rows | My run → `RESULT PASS`, exit 0, `SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; MODES 16/16; VALIDATED-ROWS 16/16`; F33 §3 same receipt | DEMONSTRATED |
| V7 | Independent manual whole-claim **and comparison** review in FOLLOW-UP | F04 (`F04-c1-whole-claim.md`, "independent manual whole-proposition review"): "PASS — all four new `crossing-minute` obligations and every new actor/place/agreement proposition are entailed by `fictional-excerpts.md:17-20` or by explicitly labeled editorial metadata … with no contents, perpetual-performance, or alliance overreach." F05 (`F05-c1-comparison.md`): "PASS — all three comparators are named exactly …, each row's delivered-vs-external status matches its r87/r88/r93 record, every analogy boundary and inference stop is explicit, the doc makes no cultural-fact/shared-canon/rights claim, the cited Spence contrast matches the r88-m3 delivered excerpt wording verbatim" (six minor non-blocking observations O1–O6). | DEMONSTRATED |
| V8 | Counts alone do not prove source support | The candidate's own texts say so (`README.md:19` "The `support_check.py` receipt is lexical preflight only, not whole-claim entailment …"; `claim-excerpt-map.md:50` "not manual whole-claim entailment or a verdict on source authenticity, truth, rights, permission, or canon"); support/structural tools are self-declared lexical/structural preflights; my map/pointer checks prove coverage, not entailment | DEMONSTRATED (as a stated and honoured boundary) |

## C. C2 — acceptance lines (wave-spec.md:21–27)

| # | Spec line | Acceptance item | Demonstrated evidence | Verdict |
|---|---|---|---|---|
| C2-1 | `:23` | Bounded stdlib CLI `corpus/tools/map_obligations.py` | File exists (691 lines, `git diff` → `A`); imports are stdlib only (`argparse, hashlib, json, os, re, subprocess, sys, tempfile, collections.Counter, pathlib` — `grep`); `python3 -I corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing` → `RESULT PASS` exit 0 (isolated mode, no site-packages); two consecutive runs byte-identical (`cmp` → IDENTICAL) | DEMONSTRATED |
| C2-2 | `:23` | Persisted independent self-test expectations in `corpus/tools/map-obligations-contract.json` | Contract file is a separate `A` file with `exit_codes` and 20 `self_test.cases` each carrying `exit` + `finding_ids`; `--self-test` → 20/20 `SELF-TEST PASS`, `RESULT PASS`, exit 0. Independence proven by my tamper probes on a relocated copy: expected-exit tampered → exit 2 `FINDING self_test_mismatch`; finding-ID tampered → exit 2 `self_test_mismatch`; case removed → exit 2 `FINDING self_test_contract: contract self-test cases do not match the implemented cases`; contract absent → exit 2 `self_test_contract` | DEMONSTRATED |
| C2-3 | `:23` | Enumerates entities (`first_appearance` + each claim), relations, timeline; one-to-one against canonical pointer rows | Raw enumeration independently recomputed: 5 + 5 + 1 + 3 = 14 = tool's `raw=14`; r94 run `raw=14 mapped=14`; my duplicate-row probe → `mapped=15`, `FINDING duplicate_mapping` exit 1, i.e. rows are compared one-to-one | DEMONSTRATED |
| C2-4 | `:23` | Demonstrable independently on the existing r93 canonical map | `python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster` → `OBLIGATIONS raw=12 mapped=12 / RESULT PASS` exit 0 (my run); F11 §1 base copy 12/12 | DEMONSTRATED |
| C2-5 | `:23` | C1 can verify without it through existing tools and manual inspection | `check_bible.py` + `support_check.py` replayed by me (V5/V6); manual map reading is possible and partially done (my pointer-row parse); the *independent* manual review is V4/V7 (pending) | DEMONSTRATED for the tool-independence claim; manual inspection exists but is not yet independent |
| C2-6 | `:25` | Before: lexical support reads map/excerpts not raw JSON, so an added raw JSON claim can retain PASS — counterexample demonstrated **without modifying live fixtures** | `python3 .ufo/waves/round-94/work/W02-unmapped-demo.py` → `support_check exit=0 terminal=['RESULT PASS']` / `map_obligations exit=1 findings=['FINDING missing_obligation: entities.json#/0/claims/1 has no map row']` / `counterexample=PASS`, exit 0. The demo works on copies; `git status --porcelain -- corpus/` empty after the run (F11 §6 shows the same for its scratch) | DEMONSTRATED |
| C2-7 | `:25` | After: the new checker fails it as a missing obligation | Same W02 run (`FINDING missing_obligation …` exit 1); my own probe: appended unmapped claim not needed — F11 case (a) shows `raw=13 mapped=12 / FINDING missing_obligation` exit 1 | DEMONSTRATED |
| C2-8 | `:25` | Also fails duplicate mapping, phantom/non-obligation pointers, source-ID mismatches, with stable finding IDs | My independent `/tmp` probes on a copy of the r94 fixture: duplicate row → exit 1 `duplicate_mapping: relations.json#/0 appears 2 times`; source column changed → exit 1 `source_id_mismatch: entities.json#/4/first_appearance does not bind to 'crossing-minute'`; pointer moved to `sources.json#/0` → exit 2 `foreign_path`; pointer index changed to `timeline.json#/9` → exit 1 `missing_obligation` + `phantom_obligation`. F11 §2 confirms all six required controls byte-identically across two runs each | DEMONSTRATED |
| C2-9 | `:25` | Unsupported bracket/prose/co-mapped grammar, malformed raw JSON and invalid paths must be could-not-evaluate, never an empty successful inventory | My probes: co-mapped cell (two pointers) → exit 2 `unsupported_map: pointer cells must contain one canonical inline-code pointer`; malformed `entities.json` (`{`) → exit 2 `malformed_json`; nonexistent cluster path → exit 2 `cluster_missing`. Self-test additionally covers `legacy_grammar`, `invalid_pointer`, `empty_segment`, `noncanonical_index`, `noncanonical_claim_index`, `traversal_path`, `symlink_path` (all exit 2). F11 §2(f) adds map-path routes `map_missing`/`foreign_path`/`unsafe_path`, all exit 2 | DEMONSTRATED (with the boundary noted in §G.2) |
| C2-10 | `:25` | Scope is the canonical one-obligation-per-row form used by r93 and the new r94 fixture; no claim of general migration of older maps | Contract `scope` field ("one-to-one map completeness and source-ID binding …"); `SCORECARD.md:374` limits the claim to "canonical one-obligation-per-row mapping/source-ID scope"; no migration claim found in the tool, contract, LOG or SCORECARD | DEMONSTRATED |
| C2-11 | `:27` | CLI contract 0/1/2; one terminal RESULT PASS/FAIL/ERROR; stable FINDING IDs | Observed across my 8 probes + `--self-test`: every run printed exactly one `RESULT …` line; exit 0 with `RESULT PASS`, 1 with `RESULT FAIL`, 2 with `RESULT ERROR`; contract `exit_codes` `{0:PASS,1:FAIL,2:ERROR}`; finding IDs stable and sorted (`emit`, tool:63-67; F11 §3 byte-identical repeats) | DEMONSTRATED |
| C2-12 | `:27` | `--self-test` isolated inputs, independently persisted expected exits + finding IDs | See C2-2; the self-test invokes the real CLI via `subprocess` (tool:615) on scratch inputs, not in-process calls. F07 (`F07-c2-selftest.md`) independently parsed the printed exits/FINDING IDs against all 20 contract expectations → zero mismatches over 4 runs; F12 (`F12-c2-contract.md`) replayed all 20 cases and confirms the contract is a committed read-only input the tool can never regenerate (missing ⇒ exit 2 `self_test_contract`; tampered ⇒ exit 2 `self_test_mismatch`) | DEMONSTRATED |
| C2-13 | `:27` | No network, no live-tree writes, no baseline regeneration, no dependencies | No network module imported (stdlib list, `grep` for `urllib\|requests\|socket\|http` → none); no write to any live path: pre/post hash snapshot around `--self-test` → `UNCHANGED` for r94 fixture, r93 fixture, frozen snapshot, tool, contract, `check_bible.py`, `support_check.py`; no residue (`glob map-obligations-self-test-*` → none); no baseline regeneration code path (only `--frozen` verification, which read-only compares digests). F12 corroborates ("stdlib-only with no network and no writes to live content (scratch confined to a removed temp dir under `ROOT`)") and F07 corroborates hash stability with `corpus/` and `git status` as concurrency-immune evidence | DEMONSTRATED (with the boundary noted in §G.1) |
| C2-14 | `:27` | Checks mapping completeness/source-ID agreement only — not entailment, fidelity, authentication, chronology, rights, permission, canon | Contract `scope` field and `SCORECARD.md:374` state the same limit; nothing in the tool reads excerpt prose | DEMONSTRATED (as a stated and honoured boundary) |

## D. Invariants and handoff (wave-spec.md:29–35)

| # | Spec line | Invariant | Evidence | Verdict |
|---|---|---|---|---|
| I-1 | `:31` | No existing fixture, checker, gate, knowledge record or past wave modified by authors | `git diff --name-status 9c2eea3 HEAD` non-`A` rows = `M LOG.md`, `M README.md`, `M SCORECARD.md` only. No `corpus/fixtures/*` (non-r94), `corpus/tools/*` pre-existing, `corpus/knowledge/*` pre-existing or `.ufo/waves/round-{87..93}/*` path is modified. F32 §1 corroborates for `check_bible.py` (empty diff, identical blob `20c56db…`); F33 §4 for r87/r88 fixtures and `support_check.py` | DEMONSTRATED |
| I-2 | `:31` | Documentation/registry additions appended after the tools/files exist and their commands run | The documentation (LOG `:2664-2674`, SCORECARD `:369-383`) cites the actual commands and their observed exits; W25.md (proposal-only seat) shows the doc proposals were correctly **not** applied while the products were absent (`corpus/tools/README.md` still unmodified). Authoring *order* itself is not independently recoverable from the committed tree | Partially demonstrated (content-consistent; sequencing is author-asserted) |
| I-3 | `:32` | Each leaf owns only its assigned new files plus `work/<ID>*` artifacts | `ls .ufo/waves/round-94/work/ \| grep -v '^W[0-9][0-9]'` → none; corpus additions are exactly the declared fixture/tool/contract/knowledge files | DEMONSTRATED (tree-observable part) |
| I-4 | `:32` | No commits, pushes, sibling writes, nested agents, quota/config scans | `git log --format='%h %an <%ae> %s' -6` → every r94 commit is authored by `lore-shokunin <lore@shokunin.local>` (L1 identity); no leaf-authored commit appears; the follow-up dir is still untracked (`?? .ufo/waves/round-94/followup/`) | DEMONSTRATED for commits (leaf-level behaviour inside a shared working tree is not independently provable from the final tree) |
| I-5 | `:33` | Knowledge opens with source/verified-at/recheck metadata | `corpus/knowledge/r94-cross-myth-design-comparison.md:1-3` (`source:`, `verified-at:`, `recheck:` all present) | DEMONSTRATED |
| I-6 | `:33` | Corpus corrections and LOG are append-only | `git diff --numstat 9c2eea3 HEAD -- LOG.md SCORECARD.md README.md` → `39 0`, `16 0`, `2 0`; removed-content-line counts `git diff … \| grep -c '^-[^-]'` → `0 / 0 / 0`. No corpus correction exists in the range (all corpus paths are `A`) | DEMONSTRATED |
| I-7 | `:33` | Report existence is not completion; fleet report lands only after committed work and actual FOLLOW-UP | `ls reports/ \| grep -i 'r94\|round-94'` → no r94 fleet report (991 entries, none r94); LOG `:2666` ("no final fleet report or MANIFEST round entry is filed here")/SCORECARD `:379` ("No final report or MANIFEST entry exists at this checkpoint") state no final report exists; the follow-up reports are untracked and uncommitted | DEMONSTRATED |
| I-8 | `:34` | WORK proposals and same-lane checks are not outside non-author verification | LOG `:2668` ("Author-side proposition review is not outside non-author verification or the required FOLLOW-UP"); knowledge addendum `:39` ("author-side … must not be presented as FOLLOW-UP PASS or C1 admission"); SCORECARD `:373` ("not independent judgment") | DEMONSTRATED |
| I-9 | `:34` | No capability row or final verdict before its demonstrated final result; no promotion or `[x]` | `grep -n 'map_obligations' SCORECARD.md` → only the r94 checkpoint prose (`:374`), not the capability table; `SCORECARD.md:377` "no new admitted row yet; C2 is a demonstrated candidate awaiting FOLLOW-UP"; `grep -n '\[x\]' SHONEN.md` → no match; SHONEN remains four `[~]` | DEMONSTRATED |
| I-10 | `:35` | Record actual tool results and agent IDs only after the dispatch returns | `work-receipt.json` carries `tool_call_id call_736fa1c0e53e49f3b1077bb35fcbc684` and 32 `agent-588…619` rows; `sha256sum .ufo/waves/round-94/work-results.xml` → `06bdafa04cdd8132e280270061719ab8df08e2a348b522e05cfb9979e5bec3bc` = the receipt's `raw_result_sha256` | DEMONSTRATED |
| I-11 | `:35` | A pending FOLLOW-UP is not failed, completed or admitted | `.ufo/waves/round-94/wave-spec.json` → `"followup": {… "status":"not-dispatched","result":null}`; LOG `:2672-2673` ("Next required work … r95 must not start before r94 is judged"; "The candidate remains pending real FOLLOW-UP") and SCORECARD `:379` describe it as pending | DEMONSTRATED |
| I-12 | `:35` | r95 must not start before r94 is judged | `ls .ufo/waves/` → `round-87 … round-94`, no round-95; SCORECARD `:379` "r95–r98 remain unstarted" | DEMONSTRATED |

## E. Seat-named items

| Item | Evidence | Verdict |
|---|---|---|
| **No modified existing bytes** | Whole-range `git diff --name-status 9c2eea3 HEAD` → 152 `A` + exactly 3 `M`: `LOG.md` (+39/−0), `SCORECARD.md` (+16/−0), `README.md` (+2/−0). The README delta is the operator-directed `**Wiki:**` header line, introduced by the integration merge `b8b50c8` (`git diff --numstat b8b50c8^1 b8b50c8` → `8 0 LOG.md`, `2 0 README.md`), and logged as documentation-only (`LOG.md` merge entry). It is not a fixture, checker, gate, knowledge record or past wave. No corpus byte outside the new fixture/tool/contract/knowledge files changed | DEMONSTRATED |
| **Report-last discipline** | No r94 fleet report exists (`ls reports/`), the follow-up reports live in an untracked directory, and both the wave spec (`:33`) and the round records state report existence is not completion. The WORK wave filed `work/W*.md` alongside their artifacts, and the candidate commit was made before any FOLLOW-UP report existed (commit times: `abbc3e0` 15:19, `65a9329` 15:35, first follow-up report 15:39) | DEMONSTRATED |
| **W20 gap acknowledged** | `ls .ufo/waves/round-94/work/ \| grep -c '^W[0-9][0-9]\.md$'` → `31`; `ls …/W20.md` → No such file. Raw record at `work-results.xml:219` is `outcome="completed"` but its body is truncated JSON followed by unescaped tool-call fragments (`…"…not a product verdict."}` ,` / `to=multi_tool_use.parallel` / `{"tool_uses":[{"recipient_name":"functions.Read"…`). Acknowledged in three places: `work-receipt.json:56-57` (`standalone_seat_reports: 31`, `known_seat_output_defects` W20/`agent-607` `usable_completion:false`), `LOG.md:2673` ("Checkpoint provenance audit correction"), `SCORECARD.md:383` ("Checkpoint provenance limit") | DEMONSTRATED |

## F. Independent replay log (raw observed output, this seat)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations            exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 2; TOTAL-ROWS 16
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS                                                           exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14 / RESULT PASS                            exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster
OBLIGATIONS raw=12 mapped=12 / RESULT PASS                            exit=0
$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
FROZEN expected=PASS/0 findings=none matched / RESULT PASS            exit=0
$ python3 corpus/tools/map_obligations.py --self-test
20 × SELF-TEST PASS … / RESULT PASS                                   exit=0
$ python3 .ufo/waves/round-94/work/W02-unmapped-demo.py
support_check exit=0 terminal=['RESULT PASS']
map_obligations exit=1 findings=['FINDING missing_obligation: entities.json#/0/claims/1 has no map row']
counterexample=PASS                                                   exit=0
$ python3 .ufo/waves/round-94/work/W02-frozen-demo.py
frozen_baseline exit=0 / mutated_copy exit=2 finding=['FINDING snapshot_tampered: …']
mutation_to_tamper=PASS                                               exit=0
$ python3 .ufo/waves/round-94/work/W01-preservation.py
INHERITED: 4/4 entity records, 2/2 timeline events, and 2/2 source records parsed-value equal
COUNTS: 4/0/2 -> 5/1/3 entities/relations/events
TICK 10: both aru-ninth-bell and evin-ninth-bell dependencies present
MAP: 14 unique canonical JSON pointers                                exit=0
```

My own isolated `/tmp` probes on a **copy** of the r94 fixture (all deleted afterwards):

```
[A-clean-copy]       exit=0  OBLIGATIONS raw=14 mapped=14 | RESULT PASS
[B-malformed-json]   exit=2  FINDING malformed_json: cannot parse entities.json: Expecting property name … | RESULT ERROR
[C-co-mapped-grammar] exit=2 FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer | RESULT ERROR
[D-invalid-pointer]  exit=1  FINDING missing_obligation: timeline.json#/2 has no map row | FINDING phantom_obligation: timeline.json#/9 is not a raw source-attributed obligation | RESULT FAIL
[E-foreign-path]     exit=2  FINDING foreign_path: pointer names unsupported input file 'sources.json' | RESULT ERROR
[F-invalid-path-arg] exit=2  FINDING cluster_missing: cannot resolve cluster: [Errno 2] No such file or directory: … | RESULT ERROR
[G-duplicate-mapping] exit=1 FINDING duplicate_mapping: relations.json#/0 appears 2 times | RESULT FAIL
[H-source-id-mismatch] exit=1 FINDING source_id_mismatch: entities.json#/4/first_appearance does not bind to 'crossing-minute' | RESULT FAIL
```

Contract-independence probes on a relocated copy (`/tmp/f39-root/corpus/tools/`):

```
[A as-delivered copy]      exit=0  RESULT PASS
[B exit-tampered]          exit=2  FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations | RESULT ERROR
[C finding-id-tampered]    exit=2  FINDING self_test_mismatch: … | RESULT ERROR
[D contract-absent]        exit=2  FINDING self_test_contract: cannot load self-test contract: [Errno 2] … | RESULT ERROR
[E case-removed]           exit=2  FINDING self_test_contract: contract self-test cases do not match the implemented cases | RESULT ERROR
```

Live-tree safety around `--self-test` (pre/post SHA-256 snapshot, mine):

```
UNCHANGED corpus/fixtures/r94-paired-crossing        dcba06fbb0d96448…
UNCHANGED corpus/fixtures/r93-m2-kojiki-cluster      ca8c882b2ce15deb…
UNCHANGED .ufo/waves/round-94/frozen/map-obligations-r93  5c41741062470e08…
UNCHANGED corpus/tools/map_obligations.py            cc1df4dc406870b6…  (matches F11's quoted digest)
UNCHANGED corpus/tools/map-obligations-contract.json 349a1956714c4496…
UNCHANGED corpus/fixtures/check_bible.py             ff9fd2aa6811a813…  (matches the round pin)
UNCHANGED corpus/tools/support_check.py              55a5eb2753901be7…
residue dirs: none
```

## G. Boundary observations carried to the L1 (no acceptance line failed)

1. **Self-test scratch lives inside the repo root, and the tool only self-tests from its delivered location.** `map_obligations.py:42` computes `ROOT = Path(__file__).resolve().parents[2]`; `:604` creates `tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)`. Consequence observed directly: a copy of the tool at `/tmp/f39-reloc/map_obligations.py` run with `--self-test` → `FINDING self_test_error: [Errno 13] Permission denied: '/map-obligations-self-test-sx4pzy3k'` / `RESULT ERROR` exit 2 (ROOT resolves to `/`), while the same copy run against a cluster argument works (`RESULT PASS` exit 0) and the delivered path self-tests clean. The scratch directory is transient (removed; no residue; pre/post hashes unchanged), so no live byte is written — but the tool is not relocatable for `--self-test`, and the scratch write lands under the lane root rather than the system temp dir. `boundary_doc_check.py:633` uses the default temp dir for comparison. Independently corroborated: F12 records the same placement ("scratch confined to a removed temp dir under `ROOT`"), and F07 observed a concurrent seat's transient `map-obligations-self-test-9f7uvbhs/` directory appear and vanish in the lane tree during its run.
2. **A syntactically canonical but out-of-range pointer is a comparison failure, not could-not-evaluate.** My probe D (`timeline.json#/9`) → exit 1 `missing_obligation` + `phantom_obligation`; F11 §5.1 independently reports the same semantics ("`phantom_obligation` is a set-membership check, not document resolution"). Reading wave-spec.md:25's "invalid paths must be could-not-evaluate" as filesystem paths and unsupported *grammar* as could-not-evaluate, the delivered behaviour is consistent (both routes verified at exit 2); the residual gap is that a map row pointing at a real-but-out-of-range index is reported as FAIL, and the contract's self-test does not cover `map_missing` / `invalid_arguments` (F11 §5.3). Bounded, documented, not contradicted.
3. **Two items in this seat's brief are tree-limited rather than fully provable:** leaf-level behaviour inside the shared working tree (who wrote which file before commit) and documentation *sequencing* (I-2). Both are recorded as partially demonstrated above rather than smoothed over.

## Bottom line

**PASS** — every C1 (lines 11–17) and C2 (lines 23–27) acceptance line, both verification paragraphs (line 19), and all twelve invariants/handoff items (lines 31–35) are DEMONSTRATED on the committed candidate at HEAD `65a9329`, each by my own replay and/or a named follow-up report: F01/F33 (structural + lexical receipts, parsed equality), F04/F05 (the independent whole-claim and comparison reviews, both PASS), F07/F11/F12 (self-test, negative controls, contract independence), F32 (checker bytes + discriminator). Only two items are labelled partially demonstrated and both are tree-limited rather than contradicted: leaf-level authorship inside the shared working tree (I-4) and documentation *sequencing* (I-2). Two bounded nuances are recorded for the L1: `--self-test` scratch is rooted inside the repo tree and the tool is not relocatable for `--self-test` (`map_obligations.py:42,604`, corroborated by F07/F12), and an out-of-range-but-well-formed pointer yields FAIL (exit 1) rather than ERROR (exit 2), with `map_missing`/`invalid_arguments` absent from the self-test case list (F11 §5.3). The W20 gap is acknowledged in the receipt, LOG and SCORECARD, and no pre-existing corpus, checker, gate, knowledge or past-wave byte is modified anywhere in the round.
