# V27 — presence-final (round 101, LAST seat)

- lane: lore-shokunin; round 101; seat V27 presence-final (finalize receipt); model `zai-coding-plan/glm-5.3-flash-low`; date 2026-10-18
- baseline: r100 closure `6f86bf2` — verified this seat: `git merge-base --is-ancestor 6f86bf2 HEAD` → exit 0 ("ANCESTOR-OK"); HEAD at round start `ebec6bb` = declaration-only commit (`git show --stat ebec6bb`: `LOG.md | 46 +++…`, 1 file changed). Wave tree uncommitted per convention.
- writes: this report only. No commits, no pushes, no network, no nested agents. All commands run from the lane root with `python3`/shell; every number below is this seat's own observed output.

## Axes

1. **Presence** — all non-SELF seat reports exist under `.ufo/waves/round-101/seats/` (SELF subtracted per ENDGAME CONVENTION).
2. **Producer artifacts** — U1's four owned files + U2's knowledge file present and identified by hash.
3. **Audit** — every report well-formed: quoted evidence, one-line bottom line, no plan verified anywhere.
4. **Receipt** — finalize `collection_snapshot`: per-report bytes/SHA-256/verdict class, plus the post-receipt delta for L1.

## Poll record (bounded escapes recorded, not fatal)

| window | span (-03) | tries | outcome |
|---|---|---|---|
| W1 | 00:04:44–00:17:45 | 40 × 20s | escape, exit 3, `ESCAPE others=3 elapsed=801s` |
| W2 | 00:18:55–00:25:15 | 20 × 20s | escape, exit 3, `ESCAPE-W2 others=8 elapsed=400s` |
| W3 | 00:29:19–00:40:19 | stall-based | `READY others=27` at 00:40:19, exit 0 (stall-escape arm: 20 min no-progress; never armed — reports kept landing) |
| W4 (closing) | 00:43:23–00:48:03 | 15 × 20s | exit 0 `W4-DONE others=29` (V24 landed ~00:43–44, V25 00:44–45, V13 final ~00:47) |

Final census (00:48:31): **29 non-SELF reports**, all `≥200 B`, all with seat-token headers and quoted terminal evidence; none empty, none tiny, no duplicate prefixes. Labels: `U1 U2 V01…V26 V28` (V27 = SELF). Declared complement was 28 seats (2 producers + 26 verifiers) → **one verifier-numbered label beyond the declared 26**; both predecessor seats' reconciliations are on file and conflict mildly (V25: roster `U1 U2 V01–V26`, excess `V28`, "roster erratum" per the r100 precedent 32-declared/34-dispatched; V13 §2: roster `U1 U2 V01–V24 V26 V28`, surplus `V25`). Both fits agree the round is one report over the declaration and that **no byte-ownership violation** occurred (every excess seat wrote only its own report + scratch). Recorded for L1; not adjudicable from filesystem evidence (V13's stated limit).

## Producer artifacts (present, hashed by this seat)

```
20823 B  00:31  corpus/knowledge/r101-r10-register-first-entry.md   sha256 19d4b23de0d86a4e…  (U2)
30142 B  00:07  corpus/tools/dependency_freeze.py                   sha256 60a78bc394409172…  (U1)
34095 B  00:08  corpus/tools/dependency-freeze-contract.json        sha256 b8fc63c3500d626d…  (U1)
49402 B  00:20  corpus/tools/README.md                              (U1, addendum)
18840 B  00:20  SKILL.md                                            (U1, freeze row)
```

`git status --porcelain` (final, verbatim): exactly `M` on the four U1-owned files + `??` on U2's entry, plus `?? .scratch/`, `?? .ufo/waves/round-101/`, and the pre-existing r98 stray `.ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md` (mtime 2026-10-17 22:32:40 — predates the round; corroborated by V13/V17/V23 parent sweeps: zero r101-attributable writes outside the lane).

## Collection snapshot (29 non-SELF reports, 00:48:31 -03; SHA-256 truncated to 12; last line truncated to ~90 chars)

```
SEAT                       BYTES  SHA256-12    VERDICT CLASS      LAST LINE (truncated)
U1-chain-eight.md           9758  7f67a3cde48d PASS               PASS — C1: guarded --freeze pinned r100-docket-review…
U2-r10-register.md          7933  c550a80f64d1 PASS               Bottom line: PASS — C2 delivered as declared…
V01-c1-chain.md             8178  21af1cfb7deb PASS               PASS — eight fixtures verify 8/8 clean…
V02-c1-discharge.md         7047  79ddb64d9da3 PASS(+cutoff notes) PASS (C1 discharge) / ABSENT (producer report)…
V03-c1-repointed.md         7492  52790db52791 PASS               PASS — the delivered gate pins the repointed-edge class…
V04-c1-selftest.md          6977  dea196fda3d8 PASS               PASS — delivered --self-test 19/19…
V05-c1-negative.md         12999  8ed1db78ee9d PASS               PASS — 75/75 battery cases…14/14 documented IDs…
V06-c1-code-review.md       9142  a9257395bba5 PASS               PASS — tool diff is +18/0…
V07-c2-procedure.md         7379  fe8f548e9fce PASS               PASS — C2 verifies on the delivered revision…
V08-c2-compatibility.md     9565  a07a57dd4a4b PASS               Bottom line: PASS — genuine, preservation-clean…
V09-c2-no-winner.md         9753  9dec930023d3 PASS               Bottom line: PASS — no winner-selection, world-truth…
V10-c2-crossrefs.md         7731  8ff86a20c676 PASS (qualified)   Bottom line: PASS (qualified) — 2 recorded ±2-line offsets…
V11-preservation-census.md  5366  b466c714a874 PASS               PASS — fixtures 174 and byte-identical to 6f86bf2…
V12-gates-boundary.md       5933  2295da36a065 PASS               Bottom line: PASS — boundary default run 14/14…
V13-scope-creep.md  (final) 9183  7a9410bcc338 PASS               PASS — zero round-101 scope creep…
V14-freshness.md           11325  354d3c8f5b80 PASS               PASS — new bytes are stale-pin-free…
V15-doc-parity.md          10754  213c62ded9b1 PASS               PASS — owned doc surfaces in parity…
V16-operability.md          9845  ffab8788a342 PASS               Bottom line: PASS — every documented command reproduces…
V17-adjacency.md            7729  22ed5caf29ec PASS               Bottom line: PASS — PROVINCE byte-identical…
V18-verdict-coverage.md     8516  b70097124dbe PASS               PASS — C1 coverage verified end-to-end by own replay…
V19-verdict-depth.md        8426  4d5f4c471e1e PASS               Bottom line: PASS — C2 depth IMPROVED (bounded)…
V20-verdict-calibration.md 12610  8cd1ca6c4306 PASS               PASS — calibration improved (bounded)…
V21-verdict-operability.md  9139  833bff22bd27 PASS               PASS — every delivered command reproduces…
V22-verdict-freshness.md   10333  d97653526b54 PASS               (multi-line bottom line) PASS — all delivered r101 artifacts are fresh…
V23-verdict-adjacency.md   14468  d2fc64291613 PASS               PASS — ADJACENCY unchanged / not harmed…
V24-adjudicator.md         14782  a076116b72f9 PASS/ADMITTED      PASS — ADMITTED with recorded conditions (AC-1…AC-4)…
V25-receipt.md              9600  14a1747fa351 PASS               PASS — 27/27 declared non-SELF reports present…
V26-cross-seat-audit.md     6126  3eaecff898a5 PASS               PASS — 6/6 quoted outputs REPRODUCED…
V28-late-bookkeeper.md      9766  b76fab131b2e ABSENT(failsafe)    ABSENT — at the 40-try cutoff…(absences since landed; corroborated)
```

Verdict census: **28 PASS** (one qualified: V10; V02/V26 carry accurate ABSENT-at-cutoff records superseded by later landings; V28's bottom line is the failsafe ABSENT at its own cutoff — every object it listed as absent demonstrably landed later, per V24's reconciliation) + **1 ABSENT-failsafe** = 29. No FAIL, no INCONCLUSIVE. No seat was judged on a plan: every audited report quotes commands and observed outputs.

## Cross-claim coherence (presence-level witness, not re-adjudication)

- **C1**: 8/8 chain with byte-identical digests (`r88 acf677a7… … r100 77debadf5c0f6e2c27f18902f0710278eb4305c633ff73158df7082936325c19`) reported independently by U1, V01, V02, V05, V14, V15, V18, V24, V26 — zero digest disagreements across seats.
- **C3**: `SELF-TEST 19/19`, `repointed_edge` exit 1 with `['ADDITION-DETECTED','REDUCTION-DETECTED']` in one run — same receipt quoted by U1, V02, V03, V04, V05, V14, V15, V18, V20, V21, V24; baseline 18/18 independently locked pre-landing by V22/V26/V28.
- **C2**: non-conflict entry verified on its own bytes by V07, V08, V09, V10 (qualified), V19, V24; receipts (`relations.json` `c279254bc7de0636` ×7, 139 B) reproduced by four seats plus this seat's spot-check of the delivered citations.
- **Admission**: V24 — ADMITTED with non-blocking conditions AC-1…AC-4.

## Finalize receipt delta for L1 (why this seat exists last)

V25's skeleton receipt landed at `.ufo/waves/round-101/seats/receipt.json` (its report declares `.ufo/waves/round-101/receipt.json` — **one-level path discrepancy**, recorded). Observed state: `state` = skeleton, 29 seat rows, `agent_id`/`outcome` null (L1 fill), `excess_seat_ids: ["V28"]`. **Stale row:** the receipt's V13 row carries the stub bytes (`report_sha256 83b5e8220699…`, 2450 B) — V13 replaced its stub with the final report (9183 B, `7a9410bcc338…`, PASS) AFTER V25's snapshot froze. L1 must refresh the V13 row (hash/size/mtime) and reconcile the V25-vs-V13 roster fits above when filling the receipt. My own report (this file) postdates every snapshot taken by other seats.

## Defects and notes recorded (none blocking, none mine to fix)

1. **U2 entry citation locator (AC-1):** delivered entry lines 58 and 81 cite `corpus/fixtures/r94-paired-crossing/README.md:13` for the ticks-editorial clause; this seat's own check: `sed -n '11p'` = the clause verbatim ("The integer ticks and event-ID edges … are editorial encodings … not literal JSON wording in the minute."), `:13` = the `first_appearance` paragraph. Flagged independently by V08, V10 (anchor 18), V15 §7, V24 (defect 1). The `r96 README:9` and `r88 table:26/:110` sibling slips ARE fixed in the delivered bytes (verified by this seat at entry lines 54 and 84).
2. **U2 report overbreadth:** "every citation machine-verified (59/59) / no correction remains open" — the checker has no expectation for the `r94 README:13` cite (V15 §7), so the residual slip was never exercised. Report-accuracy defect; artifact substance verified by six seats.
3. **Roster count/label discrepancy:** declared 28 (2+26); delivered 29 non-SELF labels. Fits conflict (V25: V28 excess; V13: V25 surplus); V27 (this seat) sits outside both fits as a dispatch-assigned label. No ownership violation either way. L1 bookkeeping.
4. **Closure pendings (per lane convention, outside wave ownership):** `corpus/README.md:42` freeze bullet now false in three clauses; C9 watch row 10 owed ("Next re-check: r101"); blind-spot-table row 2 delivered as docs-of-record (tools README addendum + SKILL supersession bullet), literal row edit owed at closure if wanted (AC-2). r102 does not start on an unclosed r101 (AC-3).
5. **Hygiene:** V02/`v26` scratch at lane-root `.scratch/` (permitted, non-standard, gitignore gap); V04's ~78,800-file baseline mirror inside its own declared scratch; V26's disclosed-and-reverted `--freeze` probe left no trace in the delivered 3-hunk delta (V24 compare).

## Limits

Presence/consistency audit: I did not re-run the gates (the digest-level claims I cite are cross-seat corroborated; my own runs here were census, hash, git-status, and citation-locator checks only). Filesystem cannot prove authorship (V13's limit, inherited). The collection snapshot hashes are point-in-time (00:48:31); any report rewritten after that instant is out of scope for this snapshot except the V13 delta explicitly recorded above.

## Bottom line

PASS — 29/29 non-SELF reports present and well-formed (28 PASS verdicts incl. 1 qualified + 1 accurate ABSENT-at-cutoff failsafe record; zero FAIL/INCONCLUSIVE), both producers' artifacts landed and hashed, V24 admission on file with non-blocking AC-1…AC-4, skeleton receipt located with its one stale V13 row and path discrepancy recorded for L1; residual items are locator hygiene and pre-declared closure pendings, none blocking.
