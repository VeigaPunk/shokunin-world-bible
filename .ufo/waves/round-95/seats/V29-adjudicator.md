# V29 — adjudicator (round 95) — FINAL all-axis adjudication

Seat: V29 adjudicator (leaf). Mandate: poll until all other 63 seat reports exist,
read them all, reconcile conflicts explicitly, apply the admission rule (admit only
if C1, C2, C3 each verify on the delivered revision AND no axis is harmed), produce
the per-axis verdict table, the ADMIT/REJECT recommendation, and exact admission
conditions; never re-roll a harmed or failed finding.

Baseline: r94 closure `fb118c4`. All commands run from the lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. No commits, no
pushes, no network, no nested agents. Writes by this seat: this report only;
scratch under `/tmp/v29/`.

## 0. Verified revision (frozen; re-checked before and after every first-hand batch)

```
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  corpus/tools/map_obligations.py
8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db  corpus/tools/map-obligations-contract.json
5d033c9db8a72801c9b8d5e609e01cddf1ace668711e24d0476b8cbd6879a264  corpus/tools/README.md
30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b  corpus/fixtures/r95-crossing-aftermath/README.md
f87ed42ad4d42143bb84f13539f2db8ca0d5f221aaf4eaffdbd6874b5ef1ab9a  corpus/knowledge/r95-aftermath-scope-note.md
```

Fixture JSON hashes (all stable since 16:18–16:21): entities `026af0bc…`, relations
`c279254b…`, contradictions `37517e5f…`, sources `fd9e30e8…`, timeline `3c0faad6…`,
fictional-excerpts `0ef6734a…`, inspiration-note `58f5390e…`, source-excerpt `b5edc2fd…`.
HEAD remains `fb118c42038ed27a747eec704b9aab41bb4b2ebe` (no commits this round).

## 1. Poll-wait record and report inventory

Poll cadence 20 s; targets = seat reports in BOTH `.ufo/waves/round-95/seats/`
(lane) and `/home/vgpnk/Projects/shokunin/.ufo/waves/round-95/seats/` (parent —
seats whose relative Write paths resolved against the session cwd landed there).
Producers were additionally gated on artifact existence + completeness before any
verification (P1 report + tool-hash stability).

Report inventory at adjudication (union of both paths, by seat id): **60 reports
present (other-seat)** — P1–P5 all present; verifier reports V01–V28, V30–V32,
V34–V46, V47–V56, V58 (V46 and V56 landed after this seat's first poll pass and are
folded in here). Misplacement: V09 and V18 exist only at the parent path (content
complete, both PASS); V30 was written at the parent path and later re-landed in-lane
at a new revision (V56 verified the lane copy as current). V30's own report records
the cwd-resolution defect that produced the strays ("harness cwd made three seat
reports land at the fleet root").

Seats whose reports were still ABSENT at the final poll cutoff (with what was
missing, per the ABSENT rule): **V33, V57, V59** — no report file in either path at
cutoff; their evidence is not available to this adjudication and nothing about them
is inferred. (V59 had a scratch dir under `seats/V59-scratch/` with the receipt
generator `gen_receipt.py`, i.e. the seat ran; no report and no receipt
`.ufo/waves/round-95/receipt.json` were filed by cutoff — V56 confirms both absent
at its 16:45 cutoff. V57's absence is noted again below for the roster.)

**Roster note (for L1):** V56's seat brief named **V57** as the adjudicator seat;
V57 filed no report anywhere. This seat (V29) is the adjudicator per its own
brief and files this report; the roster discrepancy must be recorded rather than
smoothed (condition 5).

Adjudication evidence base: **60 of 63 other-seat reports read** (all producer
reports; all landed verifier reports, including the two still-misplaced ones;
every report's bottom line and findings extracted, with the verdict/evidence seats
read in full); 3 seats ABSENT.

## 2. First-hand verification on the frozen revision (own commands)

### 2.1 C1 — calibration

```
$ python3 corpus/tools/map_obligations.py --self-test
… 22 × "SELF-TEST PASS …" including
SELF-TEST PASS map_missing exit=2 findings=['map_missing']
SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments']
RESULT PASS
EXIT=0                      # PASS lines=22, FAIL lines=0

$ python3 -c "json contract" → cases: 22
{'id': 'map_missing', 'exit': 2, 'finding_ids': ['map_missing']}
{'id': 'invalid_arguments', 'exit': 2, 'finding_ids': ['invalid_arguments']}
```

BR-02 mutation demo (scratch copies; two independent variants):

```
Variant A (mine): r94 copy, entities[0].claims → claimz (content preserved), map row
  entities.json#/0/claims/0 (J06) removed:
  OLD tool (git fb118c4):  OBLIGATIONS raw=13 mapped=13 / RESULT PASS / EXIT=0   (silent — the defect)
  DELIVERED tool:          OBLIGATIONS raw=13 mapped=13
                           INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
                           FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'claimz'
                           RESULT FAIL / EXIT=1

Variant B (V01-style): entities[4].claims → assertions, J10 removed:
  DELIVERED tool: exit 1, FINDING schema_drift: entities.json#/4: … under unexpected key 'assertions'
```

Isolation controls on the delivered revision:

```
row removed, key intact     → FINDING missing_obligation … / RESULT FAIL / exit 1
key renamed, row kept       → FINDING phantom_obligation … + FINDING schema_drift … / exit 1
```

Non-regression (delivered revision):

```
r93  OBLIGATIONS raw=12 mapped=12 / INVENTORY 12/12; 3/3; 15/15 / RESULT PASS / exit 0
r94  OBLIGATIONS raw=14 mapped=14 / INVENTORY 14/14; 2/2; 16/16 / RESULT PASS / exit 0
--frozen .ufo/waves/round-94/frozen/map-obligations-r93
     SNAPSHOT inputs=4 digests=verified / FROZEN expected=PASS/0 findings=none matched / RESULT PASS / exit 0
usage: no-arg / --bogus / --self-test+dir → FINDING invalid_arguments / exit 2 (all three)
```

### 2.2 C2 — depth

```
counts (json.load): entities 5→5, relations 1→1, sources 3→4, timeline 3→4, contradictions 0→0
new event: aftermath-missing-evin tick 11 actor aru place chalk-stair
           depends_on ["paired-crossing-decision"] source aru-aftermath-note

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS / exit 0

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations / exit 0

census: find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l → 169
inherited map rows via the delivered tool's own parser:
  r94 rows: 14  r95 rows: 15
  inherited pointers present in r95: 14 / 14; parsed-value mismatches: NONE
  new rows in r95: ['timeline.json#/3'] → ['aru-aftermath-note']
```

### 2.3 C3 — coverage

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS / exit 0                      # before: exit 2 unsupported_map (verified at baseline)

fail-closed sweep: all 12 r87-* fixtures and all 11 r89-* fixtures → exit 2
  (r87-myth-cluster: unsupported_map "pointer cells must contain one canonical inline-code pointer";
   r89-inspiration-paraphrase: unsupported_map "table needs one JSON fact pointer and one source-ID column")

support_check receipts (unchanged vs my baseline captures):
  r88  SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; MODES 12/12; VALIDATED-ROWS 12/12 / exit 0
  r93  SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; MODES 15/15; VALIDATED-ROWS 15/15 / exit 0
  r94  SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; MODES 16/16; VALIDATED-ROWS 16/16 / exit 0
```

Full-corpus regression sweep (delivered tool over all 169 fixture dirs):
exit 0 = {r88-m3-maya-cluster, r93-m2-kojiki-cluster, r94-paired-crossing,
r95-crossing-aftermath}; exit 1 = none; exit 2 = 165; `schema_drift` occurrences = 0.
Baseline tool sweep (same dirs, r95 map absent at that instant): exit 0 = {r93, r94},
exit 2 = 167. Only the two intended fixtures changed class; no schema_drift false
positive exists on the corpus.

### 2.4 Scope / harm checks

```
git status --porcelain: M LOG.md; M corpus/tools/{map_obligations.py,map-obligations-contract.json,README.md};
  ?? .ufo/waves/round-95/; ?? corpus/fixtures/r95-crossing-aftermath/; ?? corpus/knowledge/r95-aftermath-scope-note.md
git diff --numstat fb118c4: LOG.md +57/0 (append-only declaration); tools/README.md +20/0; contract 8/1; tool +130/12
git diff fb118c4 -- corpus/fixtures/r94-paired-crossing → empty
git diff fb118c4 -- SCORECARD.md SKILL.md PROVINCE.md SHONEN.md → empty
support_check.py / boundary_doc_check.py / check_bible.py blobs = fb118c4 blobs (unchanged)
```

## 3. Report reconciliation — every conflict found, resolved explicitly

1. **C3 denominator ("12/12 … obligations", LOG.md:2792).** Delivered reality:
   `OBLIGATIONS raw=10 mapped=10` + `INVENTORY … TOTAL-ROWS 12/12` (10 JSON facts +
   2 editorial rows). Independently confirmed by P1 §6.1, P2 §6.2, V02 §8.1, V03
   §3[13], V05, V24 §1d, V25 B6, V26 §5, V58 F1. **Resolution: declaration wording
   slip, not a verification failure** — the tool prints both numbers correctly
   labeled; the declared substance (exit 2 `unsupported_map` → exit 0 PASS, zero
   corpus modification, receipts unchanged) holds. Must be restated in the closure
   note (condition 2).
2. **r88 interim failures at mid-flight revisions.** V05 and V24 (both interim)
   measured r88 still exit 2 at revision `3f87fe8b` (legacy translator unreachable);
   both re-verified PASS on the frozen `d1c239cc`. **Resolution: no conflict on the
   delivered revision**; mid-flight revisions are sampled, not credited (V25's
   convention, applied consistently).
3. **V23's "V09/V13 ABSENT".** Superseded: V09 exists at the parent path (PASS);
   V13 landed 6 s after V23's poll cutoff (PASS). V54 documented this and V23's
   on-disk revision now reads "through the poll cutoff". **Resolution: absence
   claims are cutoff-relative; no C2 evidence gap.**
4. **r87 finding detail-string change.** V03/V06/V25-B5: same ID (`unsupported_map`),
   same exit 2, but the reason moved from the header check to the pointer-cell check
   (the new dialect gate accepts the legacy header, then rejects the co-mapped cell).
   **Resolution: fail-closed preserved** — the declared invariant is exit-2
   fail-closed behavior, which holds; the text change is recorded for the closure note.
5. **V37 D1 — MEDIUM (legacy-dialect hidden second pointer).** Under a legacy
   `JSON fact and fields` header, a cell naming a second pointer in its parenthetical
   or colon-prose is silently ignored and the run PASSes (canonical dialect rejects
   the same cell). Bounded: not exploited by any delivered corpus map (r88's cells
   carry exactly one pointer token); r87's co-map still exits 2; the completeness
   direction is unaffected. **Resolution: genuine soundness residual in the new
   acceptance path, recorded as found (not re-rolled, not waived); r96 debt item.**
   It does not fail C3 as declared, because C3's clauses are r88 PASS / r87+r89
   exit 2 / receipts unchanged — all verified.
6. **Residual deletion class (BR-01-adjacent).** V03 NEG-2, V25 variant D: deleting
   the `claims` key and its row still exits 0, with the shortfall visible only in the
   non-gating `INVENTORY … MISMATCH` receipt. **Resolution: outside C1's declared
   mutation class; reported as an open bound (P1 §6.3–6.4, V03 §5, V02, V25-B3),
   r96 debt item.**
7. **`schema_drift` not pinned by the persisted self-test.** V02 caveat 1, V25-B4:
   `grep -c schema_drift corpus/tools/map-obligations-contract.json` = 0; 22/22 would
   not catch drift-check removal. **Resolution: C1 declared only the two new cases
   (`map_missing`, `invalid_arguments`), both present and load-bearing (V02 §6,
   V25 §3 perturbations); the drift behavior rests on mutation demos. Reported, not
   waived; r96 debt item.**
8. **P5 note stale tool-revision pin (`9224a684…` vs delivered `d1c239cc…`).**
   V19 F-1, V27. Self-caveated in the note ("re-run … against the delivered
   revision"). **Resolution: freshness UNCHANGED (no improvement, no material harm);
   closure may append a correction.**
9. **P3 "14 inherited rows" label vs 12 JSON rows.** V09 Step 2, V54-B6. The 14 is
   the map-obligation count; JSON tables hold 12 inherited rows. **Resolution: label
   slip; the equality claim itself verified (byte and parsed-value).**
10. **P1 §4 "All other 150 fixtures identical".** V58: the sweep covers 169 dirs
    (168 identical + 1 changed). **Resolution: producer-report arithmetic slip;
    declaration unaffected; my own sweep confirms exactly one class change.**
11. **V55 PENDING → completed; V32 A.1/A.2 "not demonstrated".** V55 finished after
    V25 (PASS, consistent). V32's open admission lines refer to the missing
    adjudicator verdict — this report is that verdict. **Resolution: no conflict.**
12. **P4's "Addendum — post-P1 re-run" empty.** V12 §7, V23 §8, V54 §7. P4's own
    receipt to fill; P4's core receipts were independently re-verified on the
    delivered revision by V10/V42/V45. **Resolution: minor closure item, not a
    defect in the delivered fixture bytes.**
13. **Misplaced reports V09, V18, V30** (parent repo path). V08 process note, V23 §8,
    V54 §7, V32, V18's own scan. **Resolution: process item; collect at closure
    (condition 5).**
14. **V56 landed after the first poll pass; V57 roster note; receipt.json absent.**
    V56 (integration-checklist, PASS) enumerates L1's pre-closure checklist and
    confirms: the r95 receipt `.ufo/waves/round-95/receipt.json` was ABSENT at its
    16:45 cutoff (V59's generator exists at `seats/V59-scratch/gen_receipt.py`; agent
    IDs are filled only by L1 from the dispatch result — never invented); V46 and V57
    absent everywhere; V09/V18 stranded in the parent. Its P0 gate expected an
    adjudicator report and found none at cutoff — **this report is that verdict.**
    **Resolution: folded in; no conflict with this adjudication's conditions 3/5,
    which are extended below (receipt fill, roster accounting).**
15. **V46 (receipt-wording, PASS) — declaration wording corrections WC-1…WC-7.**
    Independently re-measured: C1, C2, C3 all verify on the pinned revision; two
    required corrections — WC-1 (the r88 "12/12 … obligations" denominator, same as
    item 1 above) and WC-2 ("with the same anchors/spans/modes" is misattributed:
    `map_obligations` reads neither the excerpt-path, span, mode, nor anchor columns;
    r88's anchors/spans/modes are covered by the unchanged `support_check` receipt
    `MODES 12/12`) — plus precision items WC-3 (14 inherited rows are parsed-value,
    not byte-identical), WC-4 (attribute every bare ratio), WC-5 (r87 detail-string
    change), WC-6 (`schema_drift` detail embeds the renamed key; the ID is stable),
    WC-7 (record the new `INVENTORY` receipt surface). Its propagation warning: V01's
    bottom line repeats "r88 now 12/12 PASS" — drafting closure text from seat bottom
    lines would propagate the slip. **Resolution: folded into condition 2.**

No unresolved conflict remains in the evidence base; no seat's PASS verdict
contradicts another's on the frozen revision.

## 4. Per-axis verdict table (no scalars)

| Axis (declared) | Verdict | Basis (first-hand + verdict seats) |
|---|---|---|
| **calibration (C1)** | **IMPROVED / PASS (bounded)** | V25 (CALIBRATION PASS, bounds B1–B7), V55 crosscheck PASS, V01/V02/V03/V04/V16/V37, my mutation demo + 22/22 self-test + sweep |
| **depth (C2)** | **IMPROVED (bounded)** | V23 (DEPTH improved), V54 crosscheck PASS, V08/V09/V10/V11/V12/V13/V14 + replicas V35/V36/V50, my receipts |
| **coverage (C3)** | **IMPROVED / PASS (bounded)** | V24 (COVERAGE PASS), V05/V06/V07/V39/V40/V41, my receipts + fail-closed sweep |
| operability (witnessed) | PASS / improved (bounded) | V26, V21, V45, V47, V48, V49 |
| freshness (witnessed) | UNCHANGED (no improvement, no material harm) | V27, V19 |
| adjacency (witnessed) | PASS | V28, V22, V18 |

Harm check (all axes): r94 fixture byte-untouched; `support_check.py`,
`boundary_doc_check.py`, `check_bible.py`, `discriminate_check.py` byte-unchanged;
PROVINCE/SKILL/SCORECARD/SHONEN unmodified; no sibling-lane or domain-tree writes
(V18, V22, V28); census inherited tuples unchanged (V20, V34, V15); no scalar score
anywhere. The only accepted changes are the declared producer bytes plus the
append-only LOG.md declaration.

## 5. Admission decision

**Rule (as declared): admit iff C1, C2, and C3 each verify on the delivered revision
and no axis is harmed.**

- C1 verifies: BR-02 class closed at exit 1 with stable `schema_drift` (my variant A
  and B, plus V01/V02/V03/V16/V25/V37 reproductions); 22-case persisted self-test,
  22/22 PASS exit 0, both new cases load-bearing; r93 12/12, r94 14/14, frozen r93
  replay exit 0, r87/r89 exit 2, usage paths exit 2 — all unchanged.
- C2 verifies: 5/1/4, 4 sources, 15/15 map obligations (14 inherited parsed-identical
  + 1 new), check_bible CLEAN, census 168→169, byte-preservation, crossing-only scope
  (adversarial whole-claim reviews).
- C3 verifies: r88 exit 2 → exit 0 PASS (10 obligations; TOTAL-ROWS 12/12), r87/r89
  stay exit 2, zero corpus modification, support_check receipts unchanged.
- No axis harmed (see §4).

**RECOMMENDATION: ADMIT** — with the exact conditions below. REJECT is not supported
by the evidence: no declared claim failed, and every harmed-or-unprovable check was
reported as such rather than forced. The D1 defect and the named residuals are
recorded as found and carried as conditions/debt; they are not re-rolled.

### Admission conditions (exact)

1. **Freeze the verified bytes.** Commit exactly the delivered revision: tool
   `d1c239cc…`, contract `8173bb97…`, tools README `5d033c9d…`, fixture bytes as
   pinned in §0, P5 note `f87ed42a…`, LOG.md declaration. Any further edit to these
   bytes invalidates the C1/C3 receipts and requires re-verification before closure.
2. **Append-only declaration corrections** (V58 F1/F4/F5 + V46 WC-1…WC-7):
   restate C3's r88 result as "10/10 obligations (+ `INVENTORY … TOTAL-ROWS 12/12`)"
   — not "12/12 obligations"; drop or re-attribute the "with the same anchors/spans/
   modes" clause (that coverage is `support_check`'s `MODES 12/12`, not
   `map_obligations`); record the r87 finding detail-string change under unchanged
   ID/exit; attribute every bare ratio (12/12, 14/14, 15/15 = raw source-attributed
   obligations = mapped JSON-fact rows; the 17/17 companion is the map's total rows);
   state that the 14 inherited rows are parsed-value (not byte-) identical; record
   the new non-gating `INVENTORY` receipt surface. Do not draft this text from seat
   bottom lines (V01's repeats the slip — V46 §4).
3. **Complete the unowned closure doc sites** (with measured numbers):
   `corpus/fixtures/README.md` Round-95 append (census 169 dirs / 35 clean / 134
   negative / 421 violation lines / zero stderr, one added directory, zero inherited
   changes); `corpus/README.md` bullets `:21`, `:29`, `:30`, `:35` (the `:35`
   "20 persisted cases" line is stale); `SKILL.md:86–89` gate-registry row
   (`schema_drift`, 22 cases, r88 dialect); `corpus/knowledge/r91-c9-watch.md` r95
   re-check row (DISCRIMINATION HELD; next re-check r96).
4. **Carry the residuals into the r96 debt ledger, unsmoothed:** BR-01-adjacent
   deletion class (exit 0, MISMATCH receipt only); `schema_drift` not pinned by any
   persisted self-test case; drift scope limited to claim-shaped records under
   unexpected entity keys (relations/timeline/nested/shape-changed variants silent);
   V37-D1 legacy-dialect hidden-second-pointer soundness gap; BR-05 repo-root
   self-test scratch; P5 note's stale tool-revision pin (append a correction or keep
   self-caveated); P4's empty post-P1 addendum receipt.
5. **Collect misplaced reports** V09 and V18 from the parent repo into the lane's
   `.ufo/waves/round-95/seats/` before the wave dir is committed (V30 has since
   been re-landed in-lane at a new revision — treat the lane copy as current);
   record seats V33, V57, V59 as ABSENT in the closure note (no report filed by
   cutoff), and record the roster discrepancy that V56's brief named V57 as the
   adjudicator while V57 filed nothing and V29 filed the adjudication.
5b. **Fill the round receipt** `.ufo/waves/round-95/receipt.json` from the dispatch
   result (V59's generator; `agent_id`/`outcome` only from the real dispatch,
   never invented — r94 F40/CC-15 precedent), including the duplicate/missing-seat
   accounting and the collection curve.
6. **No promotion.** SHONEN stays four `[~]`, no `[x]`, no capability row
   (same-lane seats are the lane).
7. **Re-run at closure on the committed revision:** `--self-test`, r93/r94/r95,
   `--frozen` r93 replay, r88/r87/r89 sweep, and the three fixture receipts; commit
   only the declared paths (pathspec-limited).

## 6. Bottom line

**ADMIT (recommended) — C1, C2, C3 each verify first-hand on the frozen delivered
revision (tool `d1c239cc…`, contract `8173bb97…`) and no axis is harmed; the
admission carries the exact conditions in §5, including the C3 "12/12" denominator
correction (V46 WC-1/WC-2), the unowned closure doc sites, the receipt fill, and
the unsmoothed residuals (V37-D1 legacy-dialect hidden-pointer gap, deletion-class
silent PASS, drift not self-test-pinned, BR-05). Three seats (V33, V57, V59) filed
no report by cutoff and are recorded ABSENT; two misplaced reports (V09, V18) must
be collected from the parent repo at closure (V30 has been re-landed in-lane).**
