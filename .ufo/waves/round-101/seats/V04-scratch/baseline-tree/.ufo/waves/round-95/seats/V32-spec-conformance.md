# V32 — spec-conformance (round 95)

Seat: V32 `spec-conformance`. Scope per seat spec: map **every line** of the round-95
LOG declaration (LOG.md tail, `## Round 95 — declaration before dispatch (2026-10-17)`)
to **demonstrated** evidence (a seat-report pointer or this seat's own replay) or to
**not demonstrated**; include the invariants (producer byte-ownership, read-only
elsewhere, no commits by seats, poll-wait honesty).

Baseline: r94 closure `fb118c4`. Frozen revision verified (hashes taken at 16:26–16:40
local, after all five producers had reported):

```
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  corpus/tools/map_obligations.py
8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db  corpus/tools/map-obligations-contract.json
5d033c9db8a72801c9b8d5e609e01cddf1ace668711e24d0476b8cbd6879a264  corpus/tools/README.md
30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b  corpus/fixtures/r95-crossing-aftermath/README.md
f87ed42ad4d42143bb84f13539f2db8ca0d5f221aaf4eaffdbd6874b5ef1ab9a  corpus/knowledge/r95-aftermath-scope-note.md
```

Scratch (declared seat scratch, the only other write): `.ufo/waves/round-95/seats/V32-scratch/`
(`baseline/map_obligations_baseline.py` = `git show fb118c4:…`, mutation copies,
`spec-lines.md` checklist).

Verification window: 16:16–16:41 local. The wave was still in flight at cutoff
(50 lane reports + 2 stranded in the umbrella repo, still growing); the revision above
was hash-stable across my final battery, and matches V05's independently frozen
revision (`map_obligations.py d1c239cc…`, contract `8173bb97…`).

## 1. Method

Every claim below was replayed by this seat on the frozen revision unless marked
otherwise; producer/verifier reports are cited as corroboration, never as substitutes.
Commands are quoted with their observed output and exit codes. My own "before" captures
were taken on the byte-verified baseline tool
(sha256 `cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790` =
`git show fb118c4:corpus/tools/map_obligations.py`).

## 2. Declaration line-by-line mapping

### 2.1 Declaration context

| Line | Status | Evidence |
|---|---|---|
| L0.1 operator regimen (r95–r98 64-seat `deepseek-v4.1-flash`; r99 grok; r100 sol) | NOT DEMONSTRATED | No on-disk dispatch record for r95 exists: `.ufo/waves/round-95/` contains only `seats/` and `scratch/` — no `wave-spec.json`, no `*-receipt.json` (r94 had both, `.ufo/waves/round-94/{wave-spec.json,work-receipt.json,followup-receipt.json}`). The seat composition/model cannot be checked from artifacts; recorded as unverifiable context, not a defect. |
| L0.2 baseline = r94 closure `fb118c4` | DEMONSTRATED | `git log --oneline -1` → `fb118c4 lore r94: close round …`; `git reflog -1` → `fb118c4`. |
| L0.3 one batched AgentSwarm, 64 seats (5 producer + 59 verifier) | PARTIAL | Exactly 5 producer reports exist (`P1-tool-code.md`…`P5-knowledge-note.md`) — the 5-seat producer count is demonstrated. The 64-seat total is not: at cutoff 52 seat reports exist (50 in the lane seats dir + 2 stranded in the umbrella repo, §4.2), still growing. No receipt to confirm one-batch dispatch. |
| L0.4 verifiers poll-wait (20 s × 40), report ABSENT rather than verify a plan | DEMONSTRATED | V05's interim report (read at 16:20) declared `Status of this file: **interim**` and `Bottom line (interim): INCONCLUSIVE — C3 cannot be verified yet: P1's corpus/tools/map_obligations.py is still byte-identical to HEAD fb118c4`; it was later rewritten to PASS on `d1c239cc`. V01 read at 16:20 had `Phase 2 — AFTER (delivered tool) PENDING — waiting on P1 delivery` / `## Bottom line PENDING`. V55 is still `## 9. Bottom line PENDING`. V23/V24 record absent seats as ABSENT (`V06/V15/V18 were ABSENT`; `two absent designated seats: V09/V13`). No report I read claimed results on artifacts that did not exist at its write time. My own poll loop logged the same artifact timeline (§5). |
| L0.5 seat reports exclusive under `.ufo/waves/round-95/seats/` | DEVIATION | Two seats wrote to the umbrella repo's path instead: `/home/vgpnk/Projects/shokunin/.ufo/waves/round-95/seats/{V09-c2-inherited-equality.md, V30-shonen-format.md}` (mtimes 16:23 / 16:19) — absent from the lane's seats dir. V08's report documents the same class and V14 self-corrected (V14 is now present in the lane). |
| L0.6 scores remain unmeasured | DEMONSTRATED | `SCORECARD.md` and `SKILL.md` are unmodified vs `fb118c4` (`git diff --stat HEAD -- SCORECARD.md SKILL.md` empty); the round's verdict reports are per-axis prose, no scalar score anywhere. |
| L0.7 owned axes depth/coverage/calibration; operability/freshness/adjacency witnessed | DEMONSTRATED (as witnessed) | Verdict seats exist for the owned axes — `V23-verdict-depth.md` ("DEPTH verdict: improved (bounded)"), `V24-verdict-coverage.md` ("PASS — C3 coverage verified on frozen revision d1c239cc"), `V55-crosscheck-calibration.md` (still PENDING at cutoff) — and witnessed-axis seats exist: V21 operability, V19 freshness, V22 adjacency. |

### 2.2 C1 — calibration

| Line | Status | Evidence |
|---|---|---|
| C1.a close BR-02 (schema-drift) + BR-03 (self-test gaps) in `map_obligations` | DEMONSTRATED | `git diff --stat HEAD -- corpus/tools/map_obligations.py` → `127 insertions(+), 11 deletions(-)`; the delivered file contains `schema_drift` (line 386), the two new self-test cases, and the contract/implementation guard. P1 §6/§7, P2 §1–§6. |
| C1.b BEFORE: renamed `claims` key + removed map row → silent `RESULT PASS` exit 0 | DEMONSTRATED (own replay) | On a scratch copy of `r94-paired-crossing` (entity 0 `claims`→`claim_records`, J06 row deleted): baseline tool → `OBLIGATIONS raw=13 mapped=13` / `RESULT PASS` / `exit=0`. Corroborated by V01 §Phase 1 (three independent copies, controls showing neither edit alone is silent). |
| C1.c AFTER: that mutation class → exit 1 with stable `schema_drift` FINDING | DEMONSTRATED (own replay) | Delivered tool on the same copy: `OBLIGATIONS raw=13 mapped=13` / `INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH` / `FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'claim_records'` / `RESULT FAIL` / `exit=1`. Same on a copy of the new r95 fixture (key `assertions`): `FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'assertions'`, exit 1. |
| C1.d persisted contract carries 22 cases incl. `map_missing`, `invalid_arguments` | DEMONSTRATED (own replay) | `python3 -c` over the contract → `cases: 22`; `map_missing: [{'id': 'map_missing', 'exit': 2, 'finding_ids': ['map_missing']}]`; `invalid_arguments: [{'id': 'invalid_arguments', 'exit': 2, 'finding_ids': ['invalid_arguments']}]`. Structural diff vs baseline: `r94 entries byte-identical (json-equal, order-preserved)? True`; one new top-level key `legacy_pointer_dialect` (disclosed by P2 §6.1). |
| C1.e r93 12/12 unchanged | DEMONSTRATED | `OBLIGATIONS raw=12 mapped=12` / `INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15` / `RESULT PASS` / exit 0 (baseline was `raw=12 mapped=12` PASS exit 0; one new INVENTORY receipt line, disclosed by P1 §6.2). |
| C1.f r94 14/14 unchanged | DEMONSTRATED | `OBLIGATIONS raw=14 mapped=14` / `TOTAL-ROWS 16/16` / `RESULT PASS` / exit 0. |
| C1.g frozen-r93 digest replay unchanged | DEMONSTRATED | `--frozen .ufo/waves/round-94/frozen/map-obligations-r93` → `SNAPSHOT inputs=4 digests=verified` / `FROZEN expected=PASS/0 findings=none matched` / `RESULT PASS` / exit 0 (baseline identical). |
| C1.h r87/r89 fail-closed unchanged | DEMONSTRATED (with nuance) | r89 → `FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column` exit 2 (detail byte-identical to baseline). r87 → exit 2 `unsupported_map`, but the **detail string changed**: baseline `table needs one JSON fact pointer and one source-ID column` → delivered `pointer cells must contain one canonical inline-code pointer`. Exit code and finding ID unchanged; receipts quoting r87's exact detail text would drift. |
| C1.i mutation demo on scratch copies, old tool from git vs delivered | DEMONSTRATED | This report's §2.2 C1.b/C1.c rows are exactly that demo, run on copies under `V32-scratch/`; the baseline tool was extracted with `git show fb118c4:…`. V01 and P1 §6.1 ran the same demo independently. |
| C1.j `--self-test` exit 0 | DEMONSTRATED | `python3 corpus/tools/map_obligations.py --self-test` → 22 `SELF-TEST PASS` lines, `RESULT PASS`, exit 0. Mid-round this failed closed (`FINDING self_test_contract: contract self-test cases do not match the implemented cases`, exit 2) while the contract still held 20 cases; resolved when P2 landed. Disclosed by P1 §6.6 and P2 §1. |

### 2.3 C2 — depth

| Line | Status | Evidence |
|---|---|---|
| C2.a first reported non-performance against a crossing-scoped agreement | DEMONSTRATED (corpus-bounded) | `grep -rn "non-performance\|nonperformance" corpus/` matches only `corpus/knowledge/r95-aftermath-scope-note.md` (the r95 class record). The r23 precedent is a different object: `r23-note-class` records "a named speaker says a named thing was not found at a named place" vs r95's person-non-arrival. "First" is bounded to the corpus as V23 §7 states. |
| C2.b fixture = preserving copy + `aru-aftermath-note` + tick-11 event `aftermath-missing-evin` (aru, chalk-stair, depends_on `[paired-crossing-decision]`) | DEMONSTRATED (own replay) | Fixture has exactly the 10 r94 filenames. `sources.json` → 4 ids `['veil-verse','paired-clock','crossing-minute','aru-aftermath-note']`; `timeline.json` → 4 ids, 4th = `aftermath-missing-evin` with `tick: 11`, `entity_id: "aru"`, `place_id: "chalk-stair"`, `depends_on: ["paired-crossing-decision"]`, `source_id: "aru-aftermath-note"`. Five declared byte-copies are sha256-identical to r94 (`entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`, `source-excerpt.md`); `fictional-excerpts.md` is append-only (`r94 bytes prefix of r95? True`, 1116→1845 bytes). Corroborated by V09 (stranded, §4.2) and V50. |
| C2.c scoped to this crossing only; no other duty or breach asserted | DEMONSTRATED (own replay) | Appended note: `Tick 11: I waited at the Chalk Stair through the agreed bell. / Evin did not come. / The agreement we chalked covered this crossing only. / I assert no other duty, no breach, and no obligation beyond this crossing.` All six `breach` occurrences in the fixture are negations/scope bounds; `contradictions.json` is `[]`; README:11 and map:51 repeat the bound. |
| C2.d BEFORE: 5 entities / 1 relation / 3 events / 3 sources, 14 map obligations | DEMONSTRATED (own replay) | r94: `entities 5`, `relations 1`, `timeline 3`, `sources 3`; baseline tool on r94 → `raw=14 mapped=14` PASS. |
| C2.e AFTER: 5/1/4, 4 sources, 15 map obligations (14 inherited unchanged + new row; no new claims/entities/relations) | DEMONSTRATED (own replay) | Counts confirmed above; map rows parsed: `r94 rows: [J01..J14] 14`, `r95 rows: [J01..J15] 15`, `new rows in r95: ['J15']`; delivered tool → `OBLIGATIONS raw=15 mapped=15` / `INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17` / `RESULT PASS` exit 0; support_check r95 → `SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; MODES 17/17; VALIDATED-ROWS 17/17` PASS. No new claims/entities/relations: `entities.json` and `relations.json` byte-identical to r94. |
| C2.f `check_bible` CLEAN exit 0 | DEMONSTRATED | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath` → `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0. Corroborated by V08. |
| C2.g inherited r94 rows parsed-value identical | DEMONSTRATED (own replay) | Row-level parse of both maps (pointer, source ID, excerpt path, span, mode, anchor), excluding the expected cluster-path qualification column: `inherited rows compared: 14 diffs(excluding namespace column): 0`. Corroborated by V11/V35 (spans/anchors) and V09 (JSON parsed equality). |
| C2.h census 168→169 | DEMONSTRATED (own replay) | `git ls-tree -d fb118c4 corpus/fixtures/ | wc -l` → `168`; `ls -d corpus/fixtures/*/ | wc -l` → `169`. Corroborated by V15/V20/V45. |
| C2.i no perpetual-breach, canon-truth, or identity inference | DEMONSTRATED (bounded, own replay) | Every `breach`/`obligation` mention in the fixture is a negation or scope bound (§C2.c); `contradictions.json` `[]`; the map/README disclose the single-actor-slot encoding so `entity_id: aru` is not an exclusion of Evin; V13 anti-overclaim and V36 whole-claim seats exist. Judgment of prose beyond these checks is out of tool scope and rests on those seats, not on this one. |

### 2.4 C3 — coverage

| Line | Status | Evidence |
|---|---|---|
| C3.a tool surface only, zero corpus modifications | DEMONSTRATED | Only `corpus/tools/map_obligations.py` changed (P1's file). `git diff --stat HEAD -- corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r87-myth-cluster corpus/fixtures/r89-inspiration-paraphrase corpus/fixtures/r93-m2-kojiki-cluster corpus/fixtures/r94-paired-crossing` → empty. V05 §6 recorded 54 fixture-file hashes pre/post. |
| C3.b BEFORE: r88 exits 2 `unsupported_map` | DEMONSTRATED (own replay) | Baseline tool on r88 → `FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column` / `RESULT ERROR` / exit 2. |
| C3.c AFTER: 12/12 PASS over the r88 map's obligations, same anchors/spans/modes | DEMONSTRATED (with wording caveat) | Delivered tool on r88 → `OBLIGATIONS raw=10 mapped=10` / `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12` / `RESULT PASS` / exit 0. **Caveat:** r88 has **10** raw source-attributed obligations; "12/12" is the map's **total mapped row count** (10 JSON facts + 2 editorial rows). The tool prints both numbers correctly labeled; counting the 2 editorial rows as obligations would emit `phantom_obligation` and exit 1. Flagged independently by P1 §6.1, P2 §6.2, V05, V24. Anchors/spans/modes are not read by the tool at all (V05 hand-checked 12/12 in-span; V41 verified the dialect premise). |
| C3.d r87/r89 legacy forms remain exit 2 fail-closed | DEMONSTRATED | r87 exit 2 `unsupported_map` (detail string changed, §C1.h); r89 exit 2 `unsupported_map` byte-identical detail. Also r88 negatives `r88-mixed-stop`, `r88-nonholder-stop`, `r88-shape-ambiguous-armed` → exit 2 `map_missing`. |
| C3.e support_check receipts on r88 (10 JSON + 2 editorial) and r93/r94 unchanged | DEMONSTRATED (own replay) | `support_check.py` itself is byte-unchanged vs HEAD (`git diff --stat` empty). Receipts: r88 `SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; MODES 12/12` PASS; r93 `12/12; 3/3; MODES 15/15` PASS; r94 `14/14; 2/2; MODES 16/16` PASS — all equal to my baseline captures. Corroborated by V07/V52. |

### 2.5 Admission rule and process lines

| Line | Status | Evidence |
|---|---|---|
| A.1 admit iff C1, C2, C3 verify and no axis harmed | NOT DEMONSTRATED (round open) | C1/C2/C3 each verify on the frozen revision per §2.2–§2.4, but no all-axis adjudicator report exists at cutoff and `V55-crosscheck-calibration` is still `PENDING`, so no admission verdict can be sourced. This is the L1's call, not this seat's. |
| A.2 per-axis verdicts, no scalars; harmed/unprovable reported as such | PARTIAL | Per-axis verdict reports exist and are prose, not scalars: V23 depth `improved (bounded)`, V24 coverage `PASS` (with the "12/12" bound and ABSENT seats named), V55 calibration still PENDING. No scalar score found anywhere in the round. |
| A.3 same-lane seats are the lane; no `[x]`, no promotion, no capability row before a demonstrated final result | DEMONSTRATED (as not-yet-promoted) | `SCORECARD.md` and `SKILL.md` unmodified vs `fb118c4`; no capability row added this round. |
| A.4 r96 does not start on an unclosed r95 | DEMONSTRATED (as not-started) | No `round-96` artifacts exist under `.ufo/waves/`; LOG.md carries no r96 declaration. |

## 3. Invariants

| Invariant | Status | Evidence |
|---|---|---|
| I.1 producer byte-ownership (P1 tool; P2 contract+README; P3 fixture JSON/excerpts; P4 fixture README+map; P5 knowledge note) | DEMONSTRATED | Modified tracked files are exactly `corpus/tools/{map_obligations.py, map-obligations-contract.json, README.md}`; new untracked producer artifacts are exactly `corpus/fixtures/r95-crossing-aftermath/` (10 files) and `corpus/knowledge/r95-aftermath-scope-note.md`. Each file sits inside its declared owner's scope; P1/P2's reports and P3/P4/P5's reports corroborate. `git status --porcelain -uall` shows **no untracked file outside** `.ufo/waves/round-95/`, the fixture dir, and the knowledge note (1654 / 10 / 1 files by root). |
| I.2 everything else read-only (seat reports excepted) | DEMONSTRATED (one deviation) | Same sweep: no writes to r87/r88/r89/r93/r94 fixtures, no other corpus file, no SCORECARD/SKILL, no other tool. Deviation: two verifier reports written to the umbrella repo instead of the lane (§4.2). |
| I.3 no commits by seats | DEMONSTRATED | `git log --oneline -1` → `fb118c4` (baseline); `git reflog -1` → `fb118c4`; `git stash list` empty. All producer work is uncommitted working-tree state. |
| I.4 poll-wait honesty | DEMONSTRATED | §L0.4 evidence: interim/PENDING/INCONCLUSIVE/ABSENT states declared where artifacts were missing, then rewritten only after delivery; no fabricated results found in the reports read. |

## 4. Deviations, contradictions, and residuals (evidence, not forced resolution)

1. **C3's "12/12 obligations" is a total-row count, not an obligation count** (§2.4 C3.c).
   The tool's labeled receipt reconciles both numbers; the declaration's phrasing is
   loose, and every independent seat that touched it (P1, P2, V05, V24) flagged the same.
2. **Two seat reports stranded outside the lane** (§L0.5): `V09-c2-inherited-equality.md`
   and `V30-shonen-format.md` under `/home/vgpnk/Projects/shokunin/.ufo/waves/round-95/seats/`.
   V23 consequently records V09 as "absent". V14 self-corrected into the lane after V08's note.
3. **Mid-round fail-closed window:** `--self-test` exited 2 `self_test_contract` while the
   contract held 20 cases and the tool implemented 22 (my replay at 16:25–16:26; disclosed
   by P1 §6.6 / P2 §1). This is correct fail-closed behavior, not a defect, but any
   verifier that sampled only that window would have seen a red self-test.
4. **r87's finding detail string changed** while exit code and finding ID did not
   (§C1.h) — receipt-text drift only.
5. **P1's declared bounds reproduced by my own probes:** a rename whose inner records are
   not full claim-shaped (`assertions: [{"source_id": …}]`) is still a silent
   `RESULT PASS` exit 0 (drift scan is bounded to `entities.json` claim containers); a
   tampered `**Expected inventory:**` line prints ` MISMATCH` but exits 0 (receipt, not gate).
   Both match P1 §6.3/§6.4 and P2 §5.
6. **BR-05 remains open:** the self-test scratch is created under the repository root and
   is not gitignored (`git check-ignore` found no rule). I observed a transient
   `map-obligations-self-test-hws_2w11/` directory during a self-test run; it was removed
   when the run finished, so no lasting leftover, but the residual is unchanged in r95
   (stated as such in the P2 README addendum).
7. **No r95 dispatch receipt / wave-spec on disk** (§L0.1/L0.3): the 64-seat composition
   and single-batch dispatch cannot be checked from artifacts, unlike r94.
8. **Round still open at cutoff:** 52 of the declared 64 seat reports existed (still
   growing); V55's calibration verdict is `PENDING`; no adjudicator verdict. Nothing in
   §2.2–§2.4 depends on those seats — every product claim above was replayed first-hand.

## 5. Poll-wait timeline (this seat's own loop)

```
try 1-4  16:16:48–16:17:49  fixture absent, scope note absent, P reports 0
try 5+   16:18:09           fixture dir appears (8 files: P3 copies)
try 20   16:23:09           corpus/knowledge/r95-aftermath-scope-note.md appears (P5)
16:20:13 P3 report; 16:20:11 V01; 16:18:14 V38 …
16:24:11/16:26:27  map_obligations.py rewritten twice by P1 (r88 still exit 2 at 16:24, exit 0 by 16:25)
16:27:15  contract updated to 22 cases (P2) → --self-test flips 2 → 0
16:27:37  P1 report; 16:29:37 P2 report; README addendum 16:28
```

## 6. Bottom line

PASS (bounded) — on the hash-frozen delivered revision (`map_obligations.py d1c239cc…`,
contract `8173bb97…`, map `30281ff1…`), every falsifiable C1/C2/C3 clause of the round-95
LOG declaration is demonstrated by first-hand replay (schema_drift exit 1 vs baseline
exit 0 on the exact BR-02 mutation; 22/22 self-test exit 0; r93 12/12, r94 14/14, r95 15/15,
frozen-r93 PASS; r88 exit 2 → exit 0 with the labeled 10 obligations + 2 editorial rows
= TOTAL-ROWS 12/12; r87/r89 still exit 2; 5/1/4 events, 4 sources, 14 inherited rows
parsed-identical, census 168→169, check_bible CLEAN), the byte-ownership/read-only/
no-commits/poll-wait invariants hold except two verifier reports stranded in the umbrella
repo (V09, V30), and the still-open admission/verdict lines (A.1/A.2; V55 PENDING) are
named as not-yet-demonstrated rather than forced.
