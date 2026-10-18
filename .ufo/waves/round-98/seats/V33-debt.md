# V33 — debt-ledger (round 98)

**Seat:** V33 debt-ledger. **Role:** compile the round's named bounds/debt into one honesty ledger — no re-adjudication, no axis score, no smoothing. Every item below is a bound, residual, carry-over, closure item or process observation that some seat or this seat named with evidence; nothing is inferred beyond what the pointers support.

**Compiled at:** 2026-10-17 ~23:41 UTC (20:41 -03) — **v1**, at cutoff with the round still landing reports (see PR-08). Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`; HEAD `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb` (`dd4df1b` r97 close); baseline `9a3d648`. Worktree at compile (exactly the declared producer set + the declaration):

```
 M LOG.md                                          (round-98 declaration)
 M corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md   (S3 repair, 1 line)
 M corpus/knowledge/r95-aftermath-scope-note.md     (S5 addendum, +14)
 M corpus/knowledge/r96-response-scope-note.md      (S5 addendum, +14)
 M corpus/tools/README.md                           (S2, +56)
 M corpus/tools/dependency-freeze-contract.json     (S1)
 M corpus/tools/dependency_freeze.py                (S1)
?? corpus/fixtures/r98-clerk-filing/                (S3+S4, 10 files)
?? corpus/knowledge/r98-clerk-scope-note.md         (S5)
?? .ufo/waves/round-98/
```

**Poll-wait record (my own):** background poll `V33-scratch/poll.sh` (20 s × 40) proved **existence-only and therefore unsafe on this round** — every producer path except the r98 fixture already existed at baseline, so try 1 (23:28:45) listed only the r98 note + reports as missing while S1/S2/S3/S4 bytes were still at baseline/placeholder state. Replaced by `V33-scratch/poll2.sh` (modification-vs-`9a3d648` via `git diff --name-only`, new-path existence, producer reports) → **ALL-PRESENT at try 19, 23:35:28 UTC** (log `V33-scratch/poll2.log`). The round's own placeholder hazard is recorded at NB-03/PR-01. No all-reports wait was attempted; no stall-escape was needed for the producer set; seats absent at this compile are named in PR-08. Never verified a plan; every number below was re-run on real files.

**Delivered revision pinned by this seat** (sha256, re-measured at compile 23:38–23:41):

- `corpus/tools/dependency_freeze.py` `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b` (S1 final; matches S1 report)
- `corpus/tools/dependency-freeze-contract.json` `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947` (S1 final; the interim `c435239d…` I first measured is superseded — ST-01)
- `corpus/tools/README.md` `1d299c16bf9a0b34526f4a799cdd3117867f6d4d278866b66366b78700d79b84`
- `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` `80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61`
- `corpus/fixtures/r98-clerk-filing/`: `entities.json` `db2d8e5d…`, `sources.json` `32ee15b1…`, `timeline.json` `eb24e084…`, `relations.json` `c279254b…`, `contradictions.json` `37517e5f…`, `fictional-excerpts.md` `29e384bf…`, `README.md` `32efc78f…`, `claim-excerpt-map.md` `c1099d0e…`, `inspiration-note.md` `58f5390e…`, `source-excerpt.md` `b5edc2fd…` (full 64-hex in the JSON)
- `corpus/knowledge/`: `r95-aftermath-scope-note.md` `8e9e1774…`, `r96-response-scope-note.md` `a9b51f8c…`, `r98-clerk-scope-note.md` `1162262c…`
- Unchanged tools cited by receipts: `map_obligations.py` `86b52949…`, `map-obligations-contract.json` `2142b991…`, `support_check.py` `55a5eb27…`, `check_bible.py` `ff9fd2aa…`

## My own reproduction (transcripts under `.ufo/waves/round-98/seats/V33-scratch/`)

- **C1(a)** — baseline mirror (m1, patched `clean` expectation): `SELF-TEST 15/16` / `FINDING SELF-TEST-MISMATCH: cases failed: ['clean']` / `RESULT FAIL` / **exit 1**. Delivered mirror (m1b, same patch): `SELF-TEST 16/17` / same finding / `RESULT ERROR` / **exit 2**. Delivered `--self-test` → `SELF-TEST 17/17` / `RESULT PASS` exit 0 (17 case lines `ok`, incl. `self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok`). Inherited expectations: 16 baseline keys byte-equal, `self_test_mismatch` the only addition; `base_fixture` still `r95-crossing-aftermath`.
- **C1(b)** — baseline mirror (m2, pin `fixture` key removed): `--freeze` → `FINDING SCOPE-REFUSED: … pin r95-crossing-aftermath already names None; freezing a same-named path elsewhere would rewrite the delivered pin` exit 2; verify → `FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs a repo-relative fixture path` exit 2. Delivered (m2b/m2b2, final contract): `MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath` → `FROZEN …` → `FREEZE … 4/4 … RESULT PASS` **exit 0**, contract's `fixture` field written. Refusal retained (m2c/m2c2, recorded path = a different in-scope path): `SCOPE-REFUSED … already names 'corpus/fixtures/r94-paired-crossing'` exit 2. Verify still fails closed until migration (m2e): `CONTRACT-INVALID` exit 2. Edge (m2d/m2f): `fixture: ""` and `fixture: 123` are also migrated (treated as path-less) — broader than the declared "path-less" wording, no harm observed (NB-11).
- **C1(c)** — contract `precedence` names the exit-1 IDs (`REDUCTION-DETECTED`, `ADDITION-DETECTED`, `ENDPOINT-CHANGE`) and the full exit-2 order with all 11 IDs (`UNPINNED-FIXTURE`/`CONTRACT-INVALID`, `FIXTURE-MISSING`, `PATH-MISMATCH`, `FILE-MISSING`/`MALFORMED-JSON`/`MALFORMED-MODEL`, `DIGEST-MISMATCH`, `INVALID-ARGUMENTS`, `SELF-TEST-MISMATCH`) plus `SCOPE-REFUSED` and the migration sentence — set-complete against the tool's emitted IDs.
- **C2** — chain on delivered paths: r88/r94/r95/r96/r97/r98 → **6/6 `RESULT PASS` exit 0**; new receipts `FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1` (digest `3c922d20…`) and `FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1` (digest `59a0f4fa…`). Mirror m4 (r97 tick-13 edge dropped): `FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']` / `dependency-edges 4/5` exit 1; same mutation on r98 (`clerk-filing-open` edge dropped) → `5/6` REDUCTION-DETECTED exit 1; baseline-tool control (m5, same dropped bytes) → `UNPINNED-FIXTURE` exit 2 (V46's FAIL pre-state). All 6 pins recomputed integral (per-file digests, content digest, counts, events, relations); contract diff vs baseline = precedence text + 17th expected case + the two new pins + `revision` + provenance note; the four inherited pins byte-unchanged.
- **C3** — r98 gates: `check_bible` `CLEAN … 0 violations` exit 0; `support_check` `SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; MODES 22/22; VALIDATED-ROWS 22/22` `RESULT PASS` exit 0; `map_obligations` `OBLIGATIONS raw=20 mapped=20 … RESULT PASS` exit 0; census `ls -d corpus/fixtures/*/ | wc -l` = **172**. r95 repair: whole-file diff exactly line 49 (stale "The new relation encodes…" → relation sentence + "the new tick-11 aftermath event records one reported non-arrival on one occasion"); pre/post `support_check` and `map_obligations` outputs byte-identical (`diff` empty, both exit 0); r95 pin digest `d541ae64…` unchanged. Four preserved r98 files `cmp`-identical to r97; parsed prefixes equal (corroborated by V10/V45). r97 fixture untouched.
- **S5 receipts** — r95/r96 addenda hashes match measured current revisions (`86b52949…`/`2142b991…`), receipts re-derived unchanged (`raw=15 mapped=15`, `raw=16 mapped=16`, both PASS); r98 note receipts reproduced (20/20; 22/22; 20 mapped; CLEAN) — corroborated by V53/V56.
- **Hygiene** — lane tree: no self-test strays at compile (`ls -d *self-test*` → only `v05-self-test-scratch/`, gitignore-covered per `git check-ignore -v`); zero seat strays in lane; parent-tree stray recorded at NB-07.

## Verdicts recorded as the seats state them at v1

- **calibration (C1):** **PASS** — V01, V02, V03, V04 (regression), V35, V52, V34 (spec-conformance PASS).
- **coverage (C2):** **improved and verified (bounded)** — V26; V05, V06, V07, V08, V54, V18 PASS; V46's recorded r97 FAIL **discharged** (V06 first-hand).
- **depth (C3):** **improved (bounded)** — V27, V50 (crosscheck); V09–V16, V38, V39, V42, V45, V46, V52, V55, V56, V18, V35 PASS.
- **freshness:** **improved (bounded)** — V29 (addenda accurate, append-only, repair the carried stale pins; F-1/F-2 disclosed).
- **operability:** **PASS** — V23 (documented commands run as written; F1/F2 prose staleness recorded).
- **adjacency/hygiene:** **PASS (bounded)** — V17 (census 172/38/134/421/0), V19 (gates CERTIFIED, discriminator HELD), V22 (pre-integration doc parity PASS), V44 (inherited tools byte-identical, STRAYS=0), V59 (presence ledger; no mutual-wait pair).
- **FAILs recorded, not re-rolled:** **V53 (narrow)** — S5's r98 note cites contract `c435239d…` (accurate when written 20:32:51, superseded by `153ebc5b…` at 20:33:36); every other quoted hash verifies; no receipt depends on it (see NB-06/ST-05).
- Not my axis: no adjudicator seat exists in r98's roster; this ledger is not an admission ruling.

**Groups:** **NB** = new bound/debt named in r98 (r99+ candidate); **CO** = carried r97-ledger item with r98 status; **CL** = closure item for the r98 closure commit; **PR** = process/artifact observation; **ST** = stale/superseded during compile.

---

## NB — new bounds/debt named in r98

| ID | Axis | Description | Evidence pointer | Proposed owner |
|---|---|---|---|---|
| NB-01 | docs/freshness | **`corpus/tools/README.md` says the self-test scratch is "not gitignored" — false in the delivered text.** Lines 99/103/123/179/232; the new r98 sentence at `:232` re-asserts "not gitignored — unchanged in r98". The committed `.gitignore` (pattern `*-self-test-*/` added at r97 closure `9d25df9`, present in `9a3d648`) covers both tools; `git check-ignore -v dependency-freeze-self-test-abc/ map-obligations-self-test-xyz/` → `.gitignore:4:*-self-test-*/`; the same file's r97 sentence (`:228`) says "covered by `.gitignore`"; S1's report states "gitignored". | my greps/check-ignore; V39 O1; V23 F1; V34/V52 residuals; S1 report §5 | closure errata (r98) or r99 doc pass |
| NB-02 | docs | **Literal self-reference imprecision:** `corpus/tools/README.md:283` "`git diff 9a3d648 -- corpus/tools/` lists only `dependency_freeze.py` and `dependency-freeze-contract.json`" — the command lists three files (the README itself is the third). Intent (no other tool code changed) holds. | my `git diff --name-only`; V39 O2; V23 F2; V52 corrections | closure errata / r99 |
| NB-03 | process | **Placeholder-poll hazard (r98 class).** S3's copy-then-extend order left r98 `README.md`/`claim-excerpt-map.md` as r97 byte copies 20:28:24→20:30:21/20:30:41; an existence-only poll is satisfied by the placeholder (V09's first poll did; S4's did at t=20 s; mine would have at try 1). Content-marker polling (or byte comparison) is required. | S3 §D1; S4 §A; V09/V10/V11/V12/V14/V38/V39/V46/V55 poll records; my poll.sh vs poll2.sh | r99 wave design (content-gated polls) |
| NB-04 | process | **Declaration arithmetic imprecision:** the r98 declaration says S3 delivers "byte copies of the other 7 files from 9a3d648"; the delivered 10-file set is 4 S3-extended + 4 byte-identical + 2 placeholder-copied-then-S4-rewritten. No delivered-byte impact. | declaration text; S3 §A; V14 soft spot 3; my file count/cmp | record (r98 declaration) |
| NB-05 | coverage | **Checker blind spots recur (carried class, now demonstrated on the r98 event):** with `check_bible`, an emptied `depends_on`, a wrong-but-earlier edge, and a deleted terminal event all stay `CLEAN` (V16 P5/P8/P9); `support_check` blind spots F15-b2/F15-a/F15-d remain tool-scoped (V47 §3). | V16 §"Boundaries"; V47 §3; V50 §3 item 4; r97 NB-15 | accepted/carried (map/README/pin layers carry the other half) |
| NB-06 | calibration/process | **Tool-revision flux inside the round, with one stale pin surviving into a delivered note:** contract `27273be2…`→`c435239d…`→`153ebc5b…`; tool `b06275f3…`→`1a01fd17…`→`03d04365…`; S5's r98 note line 64 cites `c435239d…` as current (V53 F1). | V53 F1; V15 §"S1's C1 edit landed mid-verification"; my two contract measurements; S1 report | closure errata (r98) / r99 receipt discipline |
| NB-07 | process/hygiene | **Parent-tree stray write (r94-F01 class, in the PARENT repo):** `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` (105 B, mtime 20:30, untracked) containing `python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py': [Errno 2] No such file or directory` — an unattributed seat's shell-redirect artifact; lane tree clean. | my read + parent `git status`; S2 §cross-seat; S3 D5; S1 §6; V39 O7; V44 §; V47 §4; V45 §7; V52; V54 | closure hygiene pass (L1) |
| NB-08 | docs/freshness | **r98 fixture README replay block lists the three commands with no recorded exits** — the r94 BR-17 / r95 NB-11 / r96 CO-09 / r97 NB-20 class recurs a fifth time (`grep -n exit corpus/fixtures/r98-clerk-filing/README.md` → none; V55 ran every command green, but the README does not record it). | my grep; r98 README `:23-29`; r97 NB-20 | r99 (fixture docs) |
| NB-09 | docs/freshness | **r98 scope note carries one stale sentence:** "those two files still read their r97-closure bytes at this pass's measurement" — true at S5's 20:28:35 pass, false on the delivered revision (S1's C1 files landed 20:31–20:33). The note instructs re-measurement before citing, so disclosed. | V39 O4; my note read; S5 report | closure errata / r99 |
| NB-10 | process | **V14's bottom line overstates its sweep scope:** "zero overclaims across all round-98 delivered bytes" while its own limits say S2's `corpus/tools/README.md` "was not present … therefore not swept". The overclaim result itself is not contradicted (the README items found are doc-accuracy, not overclaims). | V14 §Limits vs §Bottom line | record |
| NB-11 | calibration | **`--freeze` migration is broader than "path-less":** a pin whose `fixture` is `""` or a non-string (e.g. `123`) is also migrated in place (m2d/m2f) rather than refused. Consistent with "legacy pin migration" in spirit; recorded because the declaration says "path-less". | my m2d/m2f probes; S1 report §5 ("covers path-less pins only") | accepted / r99 wording |
| NB-12 | process | **V59 one-way blocked waiter:** V43 → V19 (no mutual-wait pair found); V58's presence poll mid-flight at cutoff (`nonself=15 total=15` at try 14, 23:33:58Z). Endgame-class record, not fatal. | V59 §5/§6; V58 scratch poll log | process (r99 wave) |

## CO — carried r97-ledger items, r98 status

Pointers into `.ufo/waves/round-97/seats/V37-debt.{md,json}` for items not re-argued here.

| ID | r97 item | r98 status | Evidence |
|---|---|---|---|
| CO-01 | NB-01 (r97 fixture unpinned from the freeze chain) | **CLOSED** — r97 pinned `3c922d20…`; the tick-13 edge drop is now `REDUCTION-DETECTED` exit 1 (baseline control `UNPINNED-FIXTURE` exit 2); V46's FAIL discharged. | my m4/m5; V06; V18; V34; V35; V52 |
| CO-02 | NB-02 (refreshed r96 pin not covering the repaired map; markdown never hashed) | **OPEN/carried** — r98 pins again cover the five JSON tables only; fixture Markdown unpinned. | V07 (contract diff = 2 pins); V05; my pin-integrity check |
| CO-03 | NB-03 (tools README `:175` pre-r97) | **CLOSED (superseded)** — S2's Round-98 addendum carries explicit "Superseded numbers" for the 14/14 and 4/4 claims. | S2 addendum; my README read |
| CO-04 | NB-04 (SKILL.md / corpus README registry rows stale) | **OPEN — now stale again for r98** (rows say 16 cases, four-fixture chain, "r97 not yet pinned"): `SKILL.md:96,98,99`, `corpus/README.md:38`. | my greps; V22 §2 | 
| CO-05 | NB-05 (fixtures README Round-97 absent; census) | **PARTIAL** — r97 closure added Round-97 + census 171; r98 needs Round-98 append + census 172 (V22 §2a measured 172/38/134/421). | V22 §2a; V17; my census |
| CO-06 | NB-06 (stale note pins r95/r96) | **CLOSED** — S5's dated addenda; V53 verified all 15+23 pins; V29 PASS. | V53; V29; my re-derivation |
| CO-07 | NB-07 (r97 note's own caveat) | **STANDING, receipts still current** — r97 note's pins (`86b52949…`) verify at compile; no addendum added (not S5's declared scope). | V53 §r95/r96/r98 (86b52949 MATCH); my sha256 |
| CO-08 | NB-08 (`dual_pointer` legacy-dialect scope) | **OPEN/accepted** — map_obligations untouched in r98. | V44 (tools byte-identical); S2 addendum "unchanged in r98" |
| CO-09 | NB-09 (consistent regeneration exits 0) | **OPEN/accepted** — not re-raised in r98. | (no r98 seat re-opened it) |
| CO-10 | NB-10 (BR-05: self-test scratch at repo root; "not gitignored") | **gitignore half CLOSED at r97 closure; wording half REOPENED as NB-01** — scratch still lands at repo root (relocation candidate); the r98 addendum re-asserts the false "not gitignored" clause. | my check-ignore; V39 O1; V23 F1; S1/S2 reports disagree |
| CO-11 | NB-11 (`/tmp` inode exhaustion) | **NOT RECURRING** — `df -i /tmp` → 2% used at compile; seats redirected TMPDIR proactively (V16). | my df; V16 §Host condition |
| CO-12 | NB-14 (r96 map lost standalone relation-bound sentence) | **NOT RE-RAISED** — status from r97 closure stands. | (no r98 seat re-opened it) |
| CO-13 | NB-15 (checker blind spots) | **RECURRED** — see NB-05. | NB-05 pointers |
| CO-14 | NB-16 (poll-wait/endgame hazards) | **RECURRED in new form** — placeholder hazard (NB-03); one-way waiter V43→V19; endgame counts (NB-12). | NB-03/NB-12 pointers |
| CO-15 | NB-17 (freeze verify-side bounds: name-gated lookup; JSON-only payload; symlink semantics) | **OPEN/carried** — unchanged by r98. | V07; V05; my pin check |
| CO-16 | NB-18 (`SELF-TEST-MISMATCH` exit divergence) | **CLOSED** — C1(a). | my m1/m1b; V01; V03; V04; V34 |
| CO-17 | NB-19 (tool-revision flux within the round) | **RECURRED** — see NB-06. | NB-06 pointers |
| CO-18 | NB-20 (fixture README replay without exits) | **RECURRED (5th)** — see NB-08. | NB-08 pointer |
| CO-19 | r97 CO-07 (BR-01 prose/markdown half) | **OPEN** — carried; S1 report §5 restates. | S1 §5; S2 addendum "rest of that supersession still stands" |
| CO-20 | r97 CO-09 (`MALFORMED-MODEL` unpinned) | **OPEN** — 17 cases still do not pin `MALFORMED-MODEL` (my contract read; S1 diff shows only `self_test_mismatch` added). | my expected-set diff |
| CO-21 | r97 CO-17 (C9 watch row-6) | **row-6 written at r97 closure; r98 row-7 ABSENT (due)** — V22 §2d measured the watch ends at row-6. | V22 §2d; V19 (control `e97613c` rc=2) |

## CL — closure items for the r98 closure commit

| ID | Axis | Description | Evidence pointer | Proposed owner |
|---|---|---|---|---|
| CL-01 | freshness/coverage | **fixtures README Round-98 append + census re-declaration** (172 dirs / 38 clean / 134 negative / 421 lines / zero non-0/1) + supersede the `:1236` "four fixtures / 16 cases / r97 not yet pinned" statements + record the r95 map one-sentence repair + the new fixture bullet; W05 pin note (fifth consecutive). | V22 §2a; V17; V34; my census | r98 closure (L1) |
| CL-02 | freshness/docs | **`corpus/README.md` bullets**: `:38` freeze row → 17 cases, six-fixture chain (r88→r98), r97+r98 pinned, exit-2 `SELF-TEST-MISMATCH`; add the r98 fixture bullet. | V22 §2b/2c; my greps | r98 closure |
| CL-03 | freshness/docs | **`SKILL.md` registry rows refresh** (`:96` chain six; `:98` 17 cases; `:99` six chain fixtures). | V22 §2c; my greps | r98 closure |
| CL-04 | freshness | **C9 watch row-7 append** (r98), with the r97 row-6 block as precedent and V19's control (`e97613c` rc=2) recorded. | V22 §2d; V19 | r98 closure |
| CL-05 | docs | **Errata for the three delivered-text errors:** NB-01 ("not gitignored"), NB-02 ("lists only"), NB-09 (r98 note's "still read their r97-closure bytes") and V53's F1 contract pin (`c435239d…` → `153ebc5b…`) — fix or dated erratum; producer-owned bytes. | NB-01/02/06/09 pointers; V52 corrections; V34 residuals | r98 closure (L1) |
| CL-06 | process | **Parent-tree stray sweep/record:** `baseline-analyze.txt` (NB-07) — attribution is outside this lane; record in the closure and leave/clean per L1. | NB-07 pointers | r98 closure (L1) |
| CL-07 | process | **Receipt fill / bookkeeping / commit split** (producer paths vs integration files; no promotion; no push; SHONEN four `[~]`, zero `[x]` at HEAD). | V35 §; V22 §1 | r98 closure |
| CL-08 | process | **Do-not-touch constraints:** PROVINCE/SHONEN/SKILL/READMEs/C9 producer-untouched (V22 verified byte-identical at inventory); pins not to be moved by closure edits. | V22 §1; V44; V17 | r98 closure |
| CL-09 | process | **Roster accounting:** 47 seat files at this compile (5 producers + 42 verifiers incl. this ledger's absence); 16 verifier reports still absent (PR-08) — the L1 must record them at closure, not this v1. | my listing | r98 closure (L1) |
| CL-10 | coverage | **r98 fixture README replay exits (NB-08)** — carry to r99 fixture docs (no r98 producer owns the file after delivery). | NB-08 pointer | r99 |

## PR — process/artifact observations (record, no re-adjudication)

| ID | Description | Evidence pointer |
|---|---|---|
| PR-01 | **Placeholder-poll hazard** (NB-03): recorded live by V09 (first poll satisfied by placeholder), S3 §D1, S4 §A, V10, V11, V12, V14, V38, V39, V46, V55, and my own poll.sh v1. Content-gated polls closed every affected seat. | NB-03 pointers |
| PR-02 | **Tool/contract revision flux:** contract seen at `c435239d…` (20:32:41) then final `153ebc5b…` (20:33:36); tool seen at `1a01fd17…` mid-write (V15) then final `03d04365…` (20:31:49). My interim battery ran on `c435239d…` and was re-run on the final bytes (all held). | my sha256 measurements; V15; V53 F1; S1 report |
| PR-03 | **V53's narrow FAIL recorded, not re-rolled:** the only mismatch among 44 quoted hashes in S5's three notes is the r98 note's `c435239d…` contract pin; it was accurate when written and no receipt depends on it. | V53 |
| PR-04 | **Parent-tree stray** (NB-07) recorded by S1, S2, S3, V10, V13, V39, V42, V44, V45, V47, V52, V54, V59 — unattributed, outside the lane, lane strays = 0. | NB-07 pointers |
| PR-05 | **Declaration "7 files" imprecision** (NB-04) recorded by S3 §A and V14 soft spot 3. | NB-04 pointers |
| PR-06 | **S3 report D1 stale clause** ("README still byte-identical to r97 at report time") superseded by S4's 20:30:41 rewrite; V09 and V46 re-checked and recorded. | S3 §D1; S4 §E; V09; V46 |
| PR-07 | **S2's report declares S1's report ABSENT at hand-off** (bounded stall-escape, artifacts verified); S1's report landed 20:35:34–20:36:24 and was read by V06/V53 and this seat. | S2 poll record; V06 §0/§6; S1 report |
| PR-08 | **Seats present at this compile:** 47 `.md` files — S1–S5 and V01–V19, V22, V23, V26, V27, V29, V34, V35, V38–V42, V44–V47, V50, V52–V56, V59. **Absent at compile (16 verifier reports):** V20, V21, V24, V25, V28, V30, V31, V32, V36, V37, V43, V48, V49, V51, V57, V58. v1 folds in nothing that lands after this write; L1 must reconcile at closure (CL-09). | my listing 23:41 |
| PR-09 | **V59 failsafe presence ledger:** no mutual-wait pair; one one-way blocked waiter (V43 → V19); V58's all-reports poll mid-flight at cutoff (`nonself=15 total=15`, try 14, 23:33:58Z). | V59 §5–6; V58 scratch |
| PR-10 | **`v05-self-test-scratch/` at the lane root is not a stray** — gitignore-covered (`*-self-test-*/`); transient `dependency-freeze-self-test-*` dirs appeared and cleared during runs. | V53 §Adjacency; my check-ignore; my `ls -d` |
| PR-11 | **V14 bottom-line scope wording** (NB-10): "all round-98 delivered bytes" vs its own unswept-S2-README limit. | NB-10 pointer |
| PR-12 | **Independent corroboration of my two README findings** by V23 (F1/F2), V39 (O1/O2), V34/V52 (residuals) — the items are seat-visible, not ledger-only. | NB-01/02 pointers |
| PR-13 | **`/tmp` condition cleared this round** (CO-11): 2% inode use at compile; no `Errno 28` in any r98 report. | my df; V16 |

## ST — stale/superseded during compile

| ID | Description | Evidence pointer |
|---|---|---|
| ST-01 | My interim C1/C2 battery measured on contract `c435239d…` is superseded by the re-run on `153ebc5b…` (pins/provenance only change; every result held). | my scratch m1b/m2b2/m4 runs; PR-02 |
| ST-02 | r98 `README.md`/`claim-excerpt-map.md` placeholder bytes (r97 copies) superseded by S4's rewrites (map 20:30:21 `c1099d0e…`, README 20:30:41 `32efc78f…`). | S3 §D1; S4 §D; V09/V46 |
| ST-03 | S3's D1 clause ("README still r97 copy") superseded within its own report window (PR-06). | PR-06 pointers |
| ST-04 | S5's r98 note contract pin `c435239d…` superseded by `153ebc5b…` (V53 F1; NB-06). | V53 |
| ST-05 | V11/V14/V15/V22/V47 interim states (IN PROGRESS) superseded by their final PASS at their own finalization. | seat files |
| ST-06 | S2's addendum sentence "not gitignored — unchanged in r98" is superseded-by-fact at delivery (NB-01) — awaiting closure errata. | NB-01 pointers |
| ST-07 | Mid-flight r98 map `raw=20 mapped=17` failures (S3/V09/S4 interim) superseded by `raw=20 mapped=20` PASS on S4's delivered map. | S3 §C; V09 §interim; S4 §B |

---

## Compile-time notes (my own checks, stated plainly)

1. All sha256s above were re-measured at compile (23:38–23:41); the delivered tool/contract/fixture/note hashes match S1–S5's declared revisions and the verifier frozen sets (V05/V07/V17/V44/V54 cross-checks agree).
2. I reproduced the three claims' head receipts myself (C1 a/b/c with baseline controls; C2 pins/chain/edges with baseline control; C3 gates + repair invariance + census + copy identity), rather than citing seat output alone; seat outputs are used for the *bounds* they name, with pointers.
3. Nothing here is a verdict: FAIL-class/stale/absent items are recorded as observed; whether any NB/CO/CL item blocks r98 admission is the L1's ruling, not this ledger's. V53's narrow FAIL is recorded exactly with its scope, and its cause (S1's post-note contract rewrite) is named without re-rolling.
4. The 16 seats absent at compile are named in PR-08; no adjudicator report exists in this round's roster, so none is folded in. This is v1: nothing that lands after this write is included.
5. Producer byte-ownership was honoured as far as I read (the r96 V41-class breach did not recur; V44/V17/V59 checked lane-locality and strays); my writes are this report, its JSON, and `V33-scratch/` only. The parent-tree stray (NB-07) is not this lane's seat write.

**Bottom line: PASS (ledger compiled) — 12 new bounds named in r98 (the false "not gitignored" clause in the tools README; the over-literal "lists only" sentence; the placeholder-poll hazard; the declaration's "7 files" arithmetic; recurring checker blind spots; the stale `c435239d…` contract pin in the r98 note + in-round revision flux; the parent-tree stray; the fifth recurrence of the no-exits replay block; the r98 note's stale C1 sentence; V14's sweep-scope wording; the broader-than-declared migration edge; the V43→V19 one-way waiter), 21 carried r97 items with explicit r98 status (4 closed: r97 unpinned, tools-README numbers, stale note pins, SELF-TEST-MISMATCH divergence; 4 recurring: checker blind spots, poll/endgame hazards, revision flux, replay-without-exits; the rest open/accepted with pointers), 10 closure items, 13 process observations and 7 supersession notes, transcribed with evidence pointers from 47 seat files plus my own reproduction of the three round claims on the final delivered revision (tool `03d04365…`, contract `153ebc5b…`, chain 6/6, self-test 17/17, census 172, receipts invariant); verdicts recorded as the seats state them at v1 (calibration PASS — V01–V04/V34/V35/V52; coverage improved bounded — V26 + V05–V08/V18/V54; depth improved bounded — V27/V50 + V09–V16/V38/V39/V42/V45/V46/V55/V56; freshness improved bounded — V29; operability PASS — V23; adjacency PASS bounded — V17/V19/V22/V44/V59; one narrow FAIL recorded, not re-rolled: V53).**

## v1.1 addendum (2026-10-17 ~23:44 UTC) — late landings folded

Eight verifier reports landed between v1's write and this addendum; folded in here. Nothing in v1 is retracted; the v1 body above stands as the 23:41 snapshot, with the following supersessions:

- **Seat counts (supersede PR-08/CL-09):** 56 seat `.md` files at this addendum (5 producers + 51 verifiers incl. this ledger); verifier reports still absent: **V20, V24, V31, V32, V36, V51, V57, V58** (8). The v1 "16 absent" list is superseded.
- **Late verdicts recorded as their seats state them:** V21 freshness PASS (addenda append-only, accurate, pins repaired); V25 **calibration improved (bounded)** — bounds incl. "README BR-05 gitignore contradiction in S2's file" (corroborating NB-01) and "path-less migration trusts invocation"; V28 operability PASS; V30 adjacency PASS (caveats: disclosed `/tmp`, lane-internal scratch, **two verifier files written at the wave top level**, one non-lore parent-root stray); V37 census replica PASS (archive 171/37/134/421 → delivered **172/38/134/421**, zero non-0/1 exits); V43 pins/C9 PASS — **C9 row-7 content supplied for L1**, so CL-04's append is content-ready (CO-21 updated); V48 cross-seat audit PASS (6/6 load-bearing quoted outputs reproduced, 0 mismatched); V49 coverage crosscheck PASS (concurring with V26).
- **New process observation — PR-14:** two verifier files were written at the wave top level (`.ufo/waves/round-98/`, e.g. V14's poll script/log) rather than under `seats/`; lane-internal, no corpus impact (recorded by V30).
- **V24-adjacency landed after v1.1's write (PASS):** PROVINCE/SHONEN/SKILL/README byte-identical; change set lane-local and exactly the declared producer byte-ownership; its one caveat is the outside-lane fleet-root stray (NB-07) with **evidence pointing to V57** for the attribution. Verifier reports still absent at this final line: **V20, V31, V32, V36, V51, V57, V58**.
- V53's narrow FAIL stands (not re-rolled). NB-01/NB-02 are now independently corroborated by V23, V25, V34, V39 and V52.

**v1.1 bottom line: unchanged from v1 (PASS, ledger compiled) with the count corrections above — 8 late reports folded; 8 verifier reports still absent at this addendum; the v1 bounds, closure items, process observations and supersession notes stand as written.**
