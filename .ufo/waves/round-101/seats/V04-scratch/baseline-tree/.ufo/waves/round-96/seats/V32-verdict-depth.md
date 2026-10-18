# V32 — verdict-depth (round 96)

Seat: V32 `verdict-depth`. Scope per seat spec: read the C2 verification seats, run 2
own spot replays, issue exactly one DEPTH verdict on the declared C2 before→after
("second-account-unresolved class", 5/1/4→5/1/5 preserving continuation) with named
bounds.

Baseline: r95 closure `dcb2d92` (HEAD `60dba0c` = r95 closure + SCORECARD only).
Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` for every path below; all
commands run from there with `python3`. Writes by this seat: this report plus scratch
`.ufo/waves/round-96/seats/V32-scratch/` (`replay.sh`, `replay-output.txt`,
`fixture-hashes.txt`, `selftest-f97e4b72.txt`). No commits, no pushes, no network, no
nested agents.

## 1. Poll record and method

Targets: Q4 fixture `corpus/fixtures/r96-crossing-response/` (8 tables/notes), Q5's
`README.md` + `claim-excerpt-map.md`, Q6's `corpus/knowledge/r96-response-scope-note.md`,
and the producer reports. Background poller (`bash-e2a9wovp`, 20 s cadence, 40 tries)
completed at 17:46:21 with all producer reports + both Q5 docs + the Q6 note present.

Observed timeline (all times -03:00, lane clock):

- 17:38:01 — fixture dir first sighted, 8 files, mid-write; Q5 docs absent.
- 17:39:48 — my first read: 8/8 Q4-owned files present; Q4 report absent.
- 17:40:16 — `sources.json`/`timeline.json` rewritten (1742→1741 B, 1678→1677 B);
  Q4's report documents this as its pre-receipt comma-placement correction
  (`  }\n,\n  {` → `  },\n  {`).
- 17:42 — Q4 report landed. 17:43 — Q5's `claim-excerpt-map.md` + `README.md` landed.
- 17:44 — Q6's knowledge note landed; Q1's hardened `map_obligations.py` landed.
- 17:46:21 — Q5 and Q6 reports landed; poller returned READY.

Fixture frozen for verification: 10-file sha256 capture at 17:44:00
(`V32-scratch/fixture-hashes.txt`); `sha256sum -c` re-verified **10/10 OK** at 17:45
and 17:47 — no write during the verify window. Key hashes: `timeline.json`
`ea0225f9…`, `sources.json` `9f973f63…`, `fictional-excerpts.md` `06b11bec…`, map
`5093d72e…`, `README.md` `ff52ced4…` — all equal Q4/Q5/V08/V09/V15/V53 captures. The
revision I verified is therefore the delivered one, not the 17:38 intermediate.

## 2. Before-state baselines (r95, replayed by me)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
exit=0
```

r95 counts parsed: entities 5 / relations 1 / events 4 / sources 4. Census baseline:
`git ls-tree -d --name-only dcb2d92 corpus/fixtures/ | wc -l` → **169**.

## 3. Spot replay 1 — check_bible on the delivered r96 fixture

```
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

`check_bible.py` is byte-unchanged all round (`ff9fd2aa…` = the r95 C9-watch pin).
Before → after: CLEAN exit 0 → CLEAN exit 0 (r95 untouched: `git diff dcb2d92 --
corpus/fixtures/r95-crossing-aftermath/` empty; my r95 replay still CLEAN exit 0).

## 4. Spot replay 2 — map_obligations + preservation battery

Q1's C1 hardening was landing during the round, so the tool was sampled at five
revisions; the fixture output is identical at every one (full battery kept verbatim at
`V32-scratch/replay-output.txt`):

| tool revision (sha256) | r96 output | exit |
|---|---|---|
| `d1c239cc…` (r95 delivered, 17:44:00) | `OBLIGATIONS raw=16 mapped=16` / `INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18` / `RESULT PASS` | 0 |
| `f97e4b72…` (17:45:03) | same | 0 |
| `44a6ffd4…` (17:45:40) | same | 0 |
| `c2c284c0…` (17:46:21) | same | 0 |
| `6634e176…` (17:47:08) | same | 0 |

Non-regression at the sampled revisions (last full set at `f97e4b72…`, spot-checked
later): r95 `raw=15 mapped=15` PASS, r94 `14/14` PASS, r93 `12/12` PASS, r88 `10/10`
PASS, all exit 0.

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14
...
PASS J16: source-support; mode=verbatim; anchor=found; 37:> Tick 12: I was at Salt Court through the same agreed bell.
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS
exit=0
```

Preservation battery (my own runs, `V32-scratch/replay.sh`):

```
counts: entities 5 relations 1 events 5 sources 5 contradictions 0
timeline ids [...,'aftermath-missing-evin','response-evin-salt-court']
source ids [...,'aru-aftermath-note','evin-response-note']
IDENTICAL: entities.json / relations.json / contradictions.json / inspiration-note.md / source-excerpt.md
timeline r95 prefix == r96 prefix: True;  sources r95 prefix == r96 prefix: True
fictional-excerpts.md: r95 1845 B / r96 2588 B, prefix identical: True   (diff = pure append 31a32,42)
```

Map-row inheritance (my own column-by-column parse): 17 r95 rows (J01–J15, S01–S02)
present in r96 with **zero cell differences modulo the declared cluster-path
re-qualification** (`r95-crossing-aftermath:` → `r96-crossing-response:`); exactly one
new row J16 (`timeline.json#/4`, span 33-42, anchor `Tick 12: I was at Salt Court
through the same agreed bell.`). All 17 inherited anchors still resolve inside their
declared spans in the r96 excerpt (0 misses, 0 outside-span).

Non-harm / census (my own runs):

```
$ git diff --stat dcb2d92 | tail -2
 LOG.md       | 67 +++
 SCORECARD.md | 32 +++
$ find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l   → 170   (169 at dcb2d92)
$ git status --porcelain
 M LOG.md
?? .ufo/waves/round-96/
?? corpus/fixtures/r96-crossing-response/
?? corpus/tools/dependency-freeze-contract.json
?? corpus/tools/dependency_freeze.py
```

One added fixture directory, zero inherited tuples changed, no stray corpus writes.

## 5. "Second account, same occasion, unresolved" — independent bounding

- **The class's records (delivered bytes).** `sources.json#/4` (`evin-response-note`,
  id line 27) — "fictional first-person note"; `timeline.json#/4`
  (`response-evin-salt-court`, id line 44) — tick 12, `entity_id evin`, `place_id
  salt-court`, `depends_on ["aftermath-missing-evin"]`, `source_id evin-response-note`;
  `fictional-excerpts.md:37-40` — "Tick 12: I was at Salt Court through the same agreed
  bell. / I make no accusation against Aru. / I select no winner between our two
  accounts. / Both accounts stand unresolved."; scope line 42 and reliability note
  (sources.json:30) repeat the bound.
- **"Same occasion" is record-bounded.** The note says "the same agreed bell" (line 37);
  the tick-12 event's editorial `depends_on` edge points at the tick-11 aftermath report
  (`aftermath-missing-evin`), and the README (`:9`) and map (`:50`, `:54`) declare the
  order/dependence as editorial encodings. No external chronology is asserted.
- **"Unresolved / no accusation / no winner" — scope audit (my grep over all 10 files).**
  Every occurrence of accusation/winner/breach/duty/obligation/alliance/perpetual is
  inside a negating or scoping clause; zero occurrences of betray/fault/guilt/blame/
  abandonment; `contradictions.json` = `[]` (2 B, byte-identical to r95). The status
  "unresolved" is asserted by the note's own lines, not by any checker.
- **Novelty bound (my own scan).** 23 fixtures have ≥2 first-person-note sources; 22 of
  them (the r35/r36/r37/r39/r40/r41/r43/r62/r72/r73/r83 Bell-7 family) carry a
  **non-empty** `contradictions.json` (one editorial row, 1022 B, "Neither wins." at
  `corpus/fixtures/README.md:761`). r96 is the **first fixture in the corpus with two
  first-person accounts and an empty contradiction ledger**; r95 had one account
  (`aru-aftermath-note`) and r91's unresolved fixture is tick-ordering scaffolding with
  no notes. The declared class name therefore holds as a corpus-bounded first.
- **No contradiction is asserted, and that is defensible on the bytes.** The two
  accounts name different actors at different places (Aru at the Chalk Stair, Evin at
  Salt Court) and Aru's claim is Evin's non-arrival *at the Chalk Stair*, which Evin's
  Salt Court account neither confirms nor refutes. The nearest precedent (r35) differs
  exactly here: r35 encodes an editorial apparent conflict row; r96 keeps
  `contradictions.json` empty and asserts the unresolved status in-record.

## 6. C2 verification seats read (statuses at report time)

- **V08 c2-checker — PASS**: CLEAN exit 0 ×3 on the delivered revision; counts
  5/1/5/5/0; tick-12 event attributes exact; independent dangling/duplicate sweep
  zero findings; r95 untouched (10/10 blobs) and still CLEAN.
- **V09 c2-inherited-equality — PASS**: key-order-sensitive parsed-value equality of
  every inherited row (entities 5/5, relations 1/1, `timeline[:4]` 4/4, `sources[:4]`
  4/4, contradictions `[] == []`), with falsifiability controls (order-only, value,
  drop-row mutations all caught); r95 byte-untouched vs `dcb2d92`; both `cmp` prefix
  claims hold.
- **V14 c2-dependency-probe — PASS**: probes (key-drop, unknown id, tick inversion,
  row-removal) each exit 1; **P1b blind spot**: an *emptied* `depends_on` stays CLEAN
  exit 0 — carried BR-01 (C3's remit, not a C2 defect; the delivered fixture is
  genuinely CLEAN).
- **V15 c2-ordering — PASS**: ticks exactly `9,9,10,11,12`, every `depends_on`
  strictly backward, chain prefix-extension monotone (0→2→3→4 edges); r19/r20
  calibration classes reproduce, including chain-level injections.
- **V53 byte-prefix-2 — PASS**: five files byte-identical; JSON tables append-only;
  excerpts strict byte-prefix; all on the frozen revision matching Q4's hashes.
- **V10, V11, V25 — reports ABSENT at my last check (17:47:08)**; V11's scratch shows a
  `report-draft.md` and `READY`, but no seat report was on disk. Their findings are
  neither quoted nor inferred.

## 7. DEPTH VERDICT (exactly one)

**DEPTH — IMPROVED (bounded).** On the delivered revision, the lane's fixture corpus
gains its first **second first-person account of the same occasion, left unresolved**:
before r95 = 5/1/4 entities/relations/events, 4 sources, 15 map obligations, one
first-person account (Aru's tick-11 report); after r96 = 5/1/5, 5 sources, 16 map
obligations (15 inherited rows carried unchanged + the new tick-12 row, J16), with the
tick-12 event dependency-linked to the tick-11 report, the unresolved status asserted
in-record (no accusation, no winner, "both accounts stand unresolved"), an empty
contradiction ledger, `check_bible` CLEAN exit 0, `map_obligations raw=16 mapped=16`
PASS exit 0, `support_check` 18/18 PASS exit 0, census 169→170 with zero inherited
changes. No harm observed in my scope: r95/r94/r88 fixtures, `check_bible.py`, and
`support_check.py` byte-unchanged vs `dcb2d92`; no new claims, entities, or relations
(three tables byte-identical); no contradiction created.

Named bounds:

1. **Structural/lexical only.** The verdict rests on delivered bytes (hashes §1) plus
   hand scope review; no testimony truth, canon adjudication, chronology, rights, or
   identity claim. The "unresolved" status is an authored in-record assertion
   (`fictional-excerpts.md:39-40`), not a checker-verified property.
2. **"First" is corpus-bounded.** First two-first-person-account fixture with an empty
   contradiction ledger within this lane's delivered corpus (23 multi-note fixtures
   scanned; the other 22 carry a non-empty editorial ledger). Not a claim about any
   wider corpus.
3. **Same-occasion is record-bounded.** "The same agreed bell" is the note's own
   wording plus an editorial `depends_on` edge; no external synchronization or
   chronology is proven.
4. **No-contradiction is an assertion, not a proof.** The different-actor/different-place
   reasoning is stated in README `:11` and map `:54`; if a future reader imports an
   expectation that the same bell implies the same place, that is an interpretive step
   the record does not make.
5. **Checker blind spot (carried).** `check_bible` cannot see an emptied `depends_on`
   (V14 P1b: CLEAN exit 0); the tick-12→tick-11 edge is verified as delivered bytes +
   prose + map row, not by a checker rule. C3's `dependency_freeze` gate covers this
   class (V49/V33), but that is another axis.
6. **Tool-revision flux (sampled, not settled).** `map_obligations.py` changed
   repeatedly during the round (`d1c239cc` → `f97e4b72` → `44a6ffd4` → `c2c284c0` →
   `6634e176` and still moving at my last check); r96 gives `16/16` PASS at every
   sampled revision, and r95/r94/r93/r88 are unchanged at the sampled revision. At
   `44a6ffd4` and `f97e4b72`, `--self-test` raised `NameError: name 'SELF_TEST_CASES'
   is not defined` (exit 1) while the fixture path stayed green — C1's axis, recorded
   here as a cross-check, not a C2 defect.
7. **Preserving continuation at named levels.** Byte-level for the five copies,
   parsed-value prefix for `timeline`/`sources`, strict byte-prefix for the excerpts
   (1845 B), and column-level equality modulo cluster-path re-qualification for the 17
   inherited map rows — not map-file byte equality.

## 8. Non-axis observations (for the integrator)

- **Environment defect:** `/tmp` (16 G tmpfs) hit **100 % inode exhaustion** (`df -i`
  Inodes IUsed 1048576, IFree 0) during this round; any write to `/tmp` failed with
  "No space left on device" (my first census scratch write, and V09's temp-file prefix
  check reported a false negative for the same reason). Seats staging scratch in `/tmp`
  may report spurious failures this round. This seat used repo-local scratch only.
- **V15 observation 1 is stale:** it reports a lone-comma line (`}\n,\n  {`) in
  `sources.json`; the delivered revision has none (`grep -n "^\s*,$"` over all r96 JSON
  → no match; Q4's disclosed 17:40:16 rewrite fixed it). V15's substantive checks ran
  on the correct hashes; only that cosmetic note describes the superseded intermediate.
- Q1's `map_obligations.py` was still iterating at my last check (17:47:08) with the
  contract still at the 22-case revision `8173bb97…`; Q1/Q2 reports were not on disk.
  The C1 verdict seats (V34) own that state.
- Q4's mid-seat rewrite (17:40:16) was disclosed in its report and preceded all
  receipts; no post-report drift was observed on the 10-file freeze.

## Bottom line

**PASS — DEPTH verdict: improved (bounded)** — the delivered r96 fixture verifies as
the corpus's first verified second-first-person-account continuation left unresolved
(5/1/4→5/1/5, 4→5 sources, 15→16 map obligations, J16 load-bearing, CLEAN/PASS receipts,
byte/value/prefix preservation, empty contradiction ledger, adversarial scope
discipline), with the named bounds in §7 (structural-only evidence, corpus-bounded
"first", record-bounded same-occasion, checker dependency blind spot, sampled tool
revisions, and three C2 seats — V10/V11/V25 — absent at report time).


---

## Addendum (17:48–17:50) — late-landing C2 seats and one strengthened bound

Three more C2 seats landed after my report was written; their findings are folded in
here (the §6 "ABSENT" note for V11 is superseded; V10/V25 remain absent at 17:48:45).

- **V11 c2-anchors — PASS**: all 16 JSON anchors (J01–J16) + 2 editorial anchors
  resolve in-span; all 17 inherited anchors identical at the same line numbers as
  r95; J16 occurs only at `fictional-excerpts.md:37`; zero drift; its independent
  `grep -nF` found-lines (12,13,17,18,19,20,26,37) match `support_check`'s receipt.
- **V45 anchor-replica-2 — PASS**: third independent line-slice method; 16/16 in-span,
  pointer-resolution check 16/16 bind (`J16 timeline.json#/4` →
  `evin-response-note`, match=True); negative control (one-line span shift) correctly
  fails (`misses=['J01']`, exit 1), so the green is not vacuous.
- **V46 whole-claim-replica-2 — PASS**: no accusation, winner, or contradiction reading
  is constructible as an assertion; all class tokens appear only under negation. Its
  scratch probes show the structural gate cannot detect these classes — I reproduced
  one independently: appending a contradiction row over the account pair
  (`aftermath-missing-evin.place_id` vs `response-evin-salt-court.place_id`) to a
  scratch copy gives
  `python3 corpus/fixtures/check_bible.py …/V32-scratch/probe-contra` →
  `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0.
  **Strengthened bound for §7.1/§7.4:** the empty ledger and the negated surfaces are
  an editorial choice verified by manual review; no delivered gate can confirm or
  refute an asserted contradiction, accusation, or winner. The class's restraint rests
  on the bytes, not on a checker outcome.
- **O1 (V46, verified by me):** `claim-excerpt-map.md:18` reads "The 15 inherited rows
  carry the r94 JSON pointers …" — imprecise for J15 alone, whose pointer
  (`timeline.json#/3`) was created at r95 (the r95 map's equivalent sentence covered
  J01–J14 and was exact). Row content is unaffected (my column comparison: zero
  differences modulo cluster-path re-qualification); cosmetic doc fidelity only.
- Fixture stability final re-check 17:48:45: 10/10 hashes OK, unchanged since 17:44:00.

**Bottom line (updated): PASS — DEPTH verdict: improved (bounded)** — the delivered r96
fixture verifies as the corpus's first verified second-first-person-account
continuation left unresolved (5/1/4→5/1/5, 4→5 sources, 15→16 map obligations, J16
load-bearing, CLEAN/PASS receipts at five sampled tool revisions, byte/value/prefix
preservation, empty contradiction ledger, adversarial whole-claim review PASS), with
the named bounds in §7 plus the addendum bound (gate-invisibility of the
contradiction/accusation/winner classes — editorial restraint confirmed by manual
review, not by checker outcomes); V10/V25 seat reports absent at final check.

### Final fold-in (17:49–17:50) — V12 landed; V10/V25 still absent

- **V12 c2-whole-claim — PASS**: every proposition of the response note (lines 37–40)
  traces to exact excerpt clauses and to `timeline.json#/4` / `sources.json#/4`; no
  accusation/winner/contradiction asserted; description and reliability note out-claim
  nothing; gate receipts CLEAN / 18/18 / 16/16 at pinned `6634e176…`. Its O2 trace note
  (line 42's "no breach" comes from the reliability-note disclaimer, not the quoted
  lines — safe direction) is consistent with my scope audit.
- **F1 (V12, verified by me): minor delivered-bytes defect in Q5's map.**
  `claim-excerpt-map.md:44` delimiter row has 8 cells while header line 43 and data rows
  45–46 have 7 (`|---|---|---|---|---|---:|---|---|`); under strict GFM the S01/S02
  editorial table would not render as a table. No gate is affected
  (`EDITORIAL-ROWS 2/2` on every run). Cosmetic; flagged for the integrator, does not
  touch the C2 substance.
- **V10, V25 — reports still absent at 17:49:13** (final check); not quoted, not inferred.
- Fixture frozen revision unchanged through 17:49:13 (10/10 hashes OK).
