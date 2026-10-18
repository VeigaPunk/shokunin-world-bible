# V47 — support-regression (round 98)

**Seat role (as declared):** support_check receipts r87–r98 all replay unchanged (quote); r94-round silent-failure vectors still fail/warn on scratch. Leaf seat; report-only on the live tree; all writes under `.ufo/waves/round-98/seats/V47-scratch/` (absolute lane path) plus this report. No commits, no pushes, no network, no nested agents.

**Baseline:** r97 closure `9a3d648`. Every command below ran from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.

**Status: COMPLETE (2026-10-17, written across 20:30–20:40).** Receipts r87→r98 and the vector matrix are complete; the producer poll returned `POLL_DONE` at try 12 with all five producer reports and all artifacts present. Final status, final change set and the post-poll re-run are in §7.

## 1. Precondition — the tool under test is untouched by the round

```
$ sha256sum corpus/tools/support_check.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
$ git show 9a3d648:corpus/tools/support_check.py | sha256sum
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  -
$ git diff --stat 9a3d648 -- corpus/tools/support_check.py | wc -l
0
```

`55a5eb27…` is the same hash the r95 and r97 V52 seats recorded, so this seat answers a behavioral question: does the r91/r92 hardening still hold on the r98 tree?

Corpus change set vs `9a3d648` (whole-tree enumeration, `git diff --name-status` + untracked list):

- modified: `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` (S3 repair), `corpus/knowledge/r95-aftermath-scope-note.md`, `corpus/knowledge/r96-response-scope-note.md` (S5 addenda), `corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json` (S1).
- new: the ten `corpus/fixtures/r98-clerk-filing/` files, `corpus/knowledge/r98-clerk-scope-note.md`.
- **No r87–r97 fixture byte changed except the r95 map** (proven receipt-neutral in §3). No map other than r95's was touched, so eight of the nine receipts below are a function of frozen tool + frozen bytes.

## 2. Receipt battery — r87 → r98 (nine clusters, all `RESULT PASS`, exit 0)

Command per cluster: `python3 corpus/tools/support_check.py corpus/fixtures/<cluster>`; exit captured immediately after each run.

| Cluster | INVENTORY (JSON/ed./total/anchors) | RECEIPT | Support line (head) | Result | Exit |
|---|---|---|---|---|---|
| r87-myth-cluster | 14/14; 8/8; 22/22; 22/22 | 14 / 8 / 22 | `SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; … MODES 22/22; VALIDATED-ROWS 22/22` | `RESULT PASS` | 0 |
| r88-m3-maya-cluster | 10/10; 2/2; 12/12; 8/8 | 10 / 2 / 12 | `SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; … MODES 12/12; VALIDATED-ROWS 12/12` | `RESULT PASS` | 0 |
| r89-inspiration-paraphrase | 1/1; 0/0; 1/1; 1/1 | 1 / 0 / 1 | `SOURCE-SUPPORT 0/0; … RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1; VALIDATED-ROWS 1/1` | `RESULT PASS` | 0 |
| r93-m2-kojiki-cluster | 12/12; 3/3; 15/15; 15/15 | 12 / 3 / 15 | `SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; … MODES 15/15; VALIDATED-ROWS 15/15` | `RESULT PASS` | 0 |
| r94-paired-crossing | 14/14; 2/2; 16/16; 12/12 | 14 / 2 / 16 | `SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; … MODES 16/16; VALIDATED-ROWS 16/16` | `RESULT PASS` | 0 |
| r95-crossing-aftermath | 15/15; 2/2; 17/17; 13/13 | 15 / 2 / 17 | `SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; … MODES 17/17; VALIDATED-ROWS 17/17` | `RESULT PASS` | 0 |
| r96-crossing-response | 16/16; 2/2; 18/18; 14/14 | 16 / 2 / 18 | `SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; … MODES 18/18; VALIDATED-ROWS 18/18` | `RESULT PASS` | 0 |
| r97-crossing-acknowledgment | 17/17; 2/2; 19/19; 15/15 | 17 / 2 / 19 | `SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; … MODES 19/19; VALIDATED-ROWS 19/19` | `RESULT PASS` | 0 |
| r98-clerk-filing | 20/20; 2/2; 22/22; 18/18 | 20 / 2 / 22 | `SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; … MODES 22/22; VALIDATED-ROWS 22/22` | `RESULT PASS` | 0 |

`ANCHORS repeated-references`: r88/r94/r95/r96/r97/r98 = 4 (each is the inherited J01/J02-style repeated anchor, unchanged); r87/r89/r93 = 0. `DUPLICATE-ROWS 0` everywhere. Every receipt matches its declared expectation: each map's own `**Expected inventory:**` line (r95 `15 JSON facts; 2 editorial rows; 17 total mapped rows; 13 distinct excerpt anchors`; r98 `20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors`) and the fixtures README/notes. r98 matches C3's declared "20 map obligations (17 inherited rows unchanged + first_appearance + claim + event)". r89's map is the fallback name `claim-to-excerpt-map.md`; its one row is `retelling-support-only` (`paraphrase`) and correctly contributes 0 to `SOURCE-SUPPORT`.

### Cross-round byte identity of the receipts

sha256 of the full stdout file, first 16 hex (`V47-scratch/receipts/*.pass2.out`):

```
r87-myth-cluster.pass2.out             952354ac759646a2
r88-m3-maya-cluster.pass2.out          b5c4075d65284f3d
r89-inspiration-paraphrase.pass2.out   ec3cd3fb29b7c0e6
r93-m2-kojiki-cluster.pass2.out        63f90ea53c147088
r94-paired-crossing.pass2.out          d0ff69820d619bc5
r95-crossing-aftermath.pass2.out       efae7be25d213fea
r96-crossing-response.pass2.out        ca7a6815077f87e8
r97-crossing-acknowledgment.pass2.out  a109856d383efa18
r98-clerk-filing.pass2.out             090fa430b8a3aff2
```

r87/r88/r93/r94 equal the r95 V52 manifest (`952354ac…`, `b5c4075d…`, `63f90ea5…`, `d0ff6982…`); r89/r95/r96/r97 equal the r97 V52 manifest (`ec3cd3fb…`, `efae7be2…`, `ca7a6815…`, `a109856d…`). The receipts have therefore not moved across the r95→r96→r97→r98 tool work. r98 is new this round; it was re-run five more times (two immediate re-runs plus the pass-2/3/4 batteries) and is byte-identical across all six runs (`090fa430b8a3aff2` every time).

### r98 detail

`diff` of the r97 receipt against the r98 receipt is exactly the count lines plus three added row lines — no other line moves:

```
< INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15
> INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
> PASS J18: source-support; mode=verbatim; anchor=found; 60:> I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN.
> PASS J19: source-support; mode=verbatim; anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
> PASS J20: source-support; mode=verbatim; anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
```

A row-level parse of the two maps (my own script, cells compared positionally) shows the 17 inherited rows J01–J17 differ from r97 in **exactly one cell each — the namespace column** (`r97-crossing-acknowledgment:` → `r98-clerk-filing:`, 17 differing cells total, no cell-count change), S01/S02 byte-identical, and the only new rows are J18 (`entities.json#/5/first_appearance`), J19 (`entities.json#/5/claims/0`), J20 (`timeline.json#/6`). The fixture README's three documented commands replay green: `check_bible` `CLEAN … 0 violations` exit 0; `support_check` 20/20 `RESULT PASS` exit 0; `map_obligations` `OBLIGATIONS raw=20 mapped=20` / `RESULT PASS` exit 0.

## 3. S3's r95 carried-wording repair is receipt-neutral (proven, not assumed)

`corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md`: frozen `9a3d648` bytes = `30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a`; repaired working-tree bytes = `80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61`.

Line-level diff of frozen vs repaired: **only line 49** (the prose sentence in `## Timeline normalization and scope`); 53 lines both sides; the 17 data rows (`| J…`, `| S0…`) and the `**Expected inventory:**` line are **byte-identical** (verified by positional comparison, `identical: True`).

Receipt-neutrality by replay: a scratch copy of the whole fixture with the frozen map substituted, run with the delivered tool, versus the live repaired map:

```
$ git show 9a3d648:corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md > V47-scratch/r95-pre/claim-excerpt-map.md
$ python3 corpus/tools/support_check.py V47-scratch/r95-pre            → EXIT=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath → EXIT=0
$ diff receipts/r95-old-map-support.out receipts/r95-new-map-support.out
DIFF: IDENTICAL (frozen 9a3d648 map vs repaired map)
$ sha256sum receipts/r95-old-map-support.out receipts/r95-new-map-support.out
efae7be25d213fea277cc1457413e65deb2720a56c20c594aa2a8b40673b9420  (both)
```

The frozen-map receipt hash equals the r97 seat's recorded r95 receipt (`efae7be2…`), so the repair moved no support receipt. Supplementary (not my axis): `map_obligations` also reads `raw=15 mapped=15` / `RESULT PASS` exit 0 on both the frozen and the repaired map.

## 4. Silent-failure vectors — delivered tool vs r90/r91 historical controls

Builder `V47-scratch/make_demos.py` copies the live fixtures read-only and asserts each replacement occurs exactly once. Controls: `V47-scratch/support_check_r90.py` = `git show a7c6a17:…` (sha256 `66a3c4bb…`, pre-hardening), `V47-scratch/support_check_r91.py` = `git show 6332115:…` (sha256 `9da149b8…`, first hardened). Transcripts under `V47-scratch/vectors/<demo>.<tool>.out|.err`.

| # | vector (scratch copy) | delivered tool | r90 control |
|---|---|---|---|
| T1 | r87 fact-table `ID` header → `Ref` | `JSON-FACTS 0/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 8/22` + 4 `WARN: unreferenced excerpt declaration` + `FAIL: inventory JSON facts mismatch: expected=14 parsed=0` / `RESULT FAIL`, **exit 1** | `SOURCE-SUPPORT 8/8 … MODES 8/8` / `RESULT PASS`, **exit 0 (silent)** |
| T2 | r87 `## Editorial rows` section dropped | `EDITORIAL-ROWS 0/8; TOTAL-ROWS 14/22` + `WARN … lowwater-hymn-excerpt.md` / `RESULT FAIL`, **exit 1** | `SOURCE-SUPPORT 14/14 … MODES 14/14` / `RESULT PASS`, **exit 0 (silent)** |
| T3 | r87 `E1` row duplicated | `JSON-FACTS 15/14; TOTAL-ROWS 23/22` + `FAIL: duplicate mapped row E1 appears 2 times` / `RESULT FAIL`, **exit 1** | `SOURCE-SUPPORT 23/23` / `RESULT PASS`, **exit 0 (inflated, silent)** |
| T4 | r87 hymn declaration `verbatim`→`summary` (referenced) | `EDITORIAL-ANCHORS 0/8; MODES 14/22` / `RESULT FAIL`, **exit 1** | `FAIL H1…` / exit 1 (already failing) |
| T5a | r88 Spence declaration flip on the current map (S1/S2 reference it) | `FAIL S1/S2 … excerpt-mode=summary`, `EDITORIAL-ANCHORS 0/2; MODES 10/12` / `RESULT FAIL`, **exit 1** | `FAIL S1/S2 …` exit 1 |
| T5b | r88 r90-era shape (editorial rows removed, inventory restated) + same flip | `WARN: unreferenced excerpt declaration: source-excerpt.md (mode=summary)` / `SOURCE-SUPPORT 10/10` unchanged / `RESULT PASS WITH WARNINGS`, **exit 0 (surfaced)** | `SOURCE-SUPPORT 10/10` / `RESULT PASS`, **exit 0 (silent)** |
| T6 | r89 paraphrase anchor made absent | `WARN entities.json#/0/claims/0: retelling-support-only; anchor=not-found`, `RETELLING-SUPPORT-ONLY 1 entries (0/1 anchors)`, `VALIDATED-ROWS 0/1`, `WARN: retelling anchor not found … excluded from source support` / `RESULT PASS WITH WARNINGS`, **exit 0** | `RETELLING-SUPPORT-ONLY 1 entries (0/1 anchors)` / `RESULT PASS`, exit 0 (count only, no WARN) |
| T7 | r87 inventory declaration line removed | stderr `FAIL: map must contain exactly one expected inventory declaration`, stdout `RESULT FAIL`, **exit 1** | `SOURCE-SUPPORT 22/22` / `RESULT PASS`, **exit 0 (silent)** |
| T8 | r87 distinct-anchor declaration 22→21 | `DISTINCT-ANCHORS 22/21` + `FAIL: inventory distinct excerpt anchors mismatch: expected=21 parsed=22` / `RESULT FAIL`, **exit 1** | `SOURCE-SUPPORT 22/22` / `RESULT PASS`, **exit 0 (silent)** |

All eight vectors fail or warn on the delivered tool; six (T1, T2, T3, T5b, T7, T8) were silent passes under the r90 tool. The two documented non-silent deltas against the r91 control reproduce exactly:

```
$ python3 V47-scratch/support_check_r91.py V47-scratch/demos/T7-no-inventory   → EXIT=2, stdout lines: 0 (stderr: FAIL: map must contain exactly one expected inventory declaration)
$ python3 V47-scratch/support_check_r91.py V47-scratch/demos/T8-anchor-count-offby1 → EXIT=1, no RESULT line (stdout ends at the FAIL: inventory … mismatch line)
```

delivered tool: T7 exit 1 **with** a `RESULT FAIL` terminal line; T8 exit 1 **with** a `RESULT FAIL` terminal line. Neither change reintroduces silence.

### r94-round F15 mutants — closed classes and named blind spots

| mutant | delivered `support_check` | where it is closed |
|---|---|---|
| F15-b2 — fact row `J05` dropped **and** inventory restated to match | `INVENTORY JSON-FACTS 13/13; … TOTAL-ROWS 15/15` / `RESULT PASS`, exit 0 (**still silent by design**; map-only lexical check) | `map_obligations` → `OBLIGATIONS raw=14 mapped=13` / `FINDING missing_obligation: entities.json#/4/first_appearance has no map row` / `RESULT FAIL`, exit 1 |
| F15-b3 — row dropped, stale inventory kept | `JSON-FACTS 13/14; TOTAL-ROWS 15/16; DISTINCT-ANCHORS 11/12` + inventory `FAIL`s / `RESULT FAIL`, **exit 1** (r90: PASS exit 0) | support_check's own drift catch |
| F15-a — tick-10 `depends_on` reduced to one entry (raw JSON only) | `INVENTORY … 14/14 … 16/16` / `RESULT PASS`, exit 0 (**documented blind spot**: support_check never reads raw JSON); `map_obligations` also `OBLIGATIONS raw=14 mapped=14` / `RESULT PASS` exit 0 | `dependency_freeze` / `check_bible` territory (C2 seats), not this seat |
| F15-c — `J05` declared span `17`→`20` (anchor text unchanged) | `FAIL J05 … anchor=found; 17:…; span=20; outside-span=17`, `SOURCE-SUPPORT 13/14`, `VALIDATED-ROWS 15/16` / `RESULT FAIL`, **exit 1** (r90 also exit 1) | support_check's own span enforcement |
| F15-d — timeline event `source_id` `crossing-minute`→`paired-clock` | `SOURCE-SUPPORT 14/14` / `RESULT PASS`, exit 0 (**documented blind spot**) | `map_obligations` → `FINDING source_id_mismatch: timeline.json#/2 does not bind to 'paired-clock'` / `RESULT FAIL`, exit 1 |

F15-b2/F15-a/F15-d are named blind spots of this tool, not regressions: the r94 round recorded them as such and they are closed by the r94/r96 `map_obligations` and `dependency_freeze` additions. This seat claims nothing about those tools' current behavior beyond what is quoted.

## 5. Bounds

- `support_check` is a lexical preflight (declared inventory, fixed-string anchors, declared spans, R9 mode consistency). None of these receipts proves entailment, mode fidelity, source authentication, chronology, rights, permission, or canon. The r98 fixture's own content claims (6/1/7 counts, the clerk class, the no-finding bound) belong to S3/S4/S5 and the C3 seats; this seat only replays the map↔excerpt receipt on the delivered bytes.
- The T-vectors are scratch mutations of live fixture copies; no live fixture byte was modified by this seat. Live-tree protection re-checked after the whole battery: r87 `3ad4e810…`, r88 `b3b79fe5…`, r93 `17f0e812…`, r94 `ed9527c5…`, r95 `80440d61…` (repaired), r96 `e851f068…`, r97 `49d4834e…`, r98 `c1099d0e…`, `support_check.py` `55a5eb27…`.
- Not verified by this seat: S1's `dependency_freeze` C1/C2 work, S2's README, S5's notes beyond their quoted support receipts. Producer reports observed: S3 `S3-fixture-author.md` and S4 `S4-fixture-docs.md` both independently quote the same r98 receipt (`20/20`, `22/22` rows, `RESULT PASS` exit 0) and the same r95 post-repair receipt (`15/15`, `17/17`, `RESULT PASS` exit 0).
- Write-scope hygiene: this seat wrote only `V47-scratch/**` and this report; no command of mine referenced the parent tree. **Observed stray (not mine, recorded for the adjacency seat):** an untracked `baseline-analyze.txt` exists at the parent repo root `/home/vgpnk/Projects/shokunin/` (mtime 20:30:10, 105 bytes) containing `python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py': [Errno 2] No such file or directory` — the residue of some other seat's failed command. No file of mine exists outside `lore-shokunin/.ufo/waves/round-98/seats/`; the seat's temporary `/tmp` outputs were removed at the end.

## 6. Poll-wait record

Poller `V47-scratch/poll.sh` (20 s cadence, 40 tries; logs to `V47-scratch/poll.log`), checking producer **artifacts** and **reports** together: `corpus/tools/README.md` modified (S2), `corpus/knowledge/r98-clerk-scope-note.md` present (S5), `S1..S5-*.md` reports present, `dependency_freeze` files modified (S1).

| Time (try) | reports | tools_readme_mod | r98_scope_note | r98_readme | dep_freeze_mod |
|---|---|---|---|---|---|
| 20:31:52 (1) | 1 | 0 | 0 | 1 | 2 |
| 20:32:12 (2) | 2 | 0 | 0 | 1 | 2 |
| 20:32:32 (3) | 2 | 0 | 1 | 1 | 2 |
| 20:32:52–20:34:12 (4–8) | 2–3 | 0→1 (try 7) | 1 | 1 | 2 |
| 20:34:32 (9) | 3 | 1 | 1 | 1 | 2 |
| 20:34:52 (10) | 4 | 1 | 1 | 1 | 2 |
| 20:35:32 (12) | **5** | 1 | 1 | 1 | 2 → `POLL_DONE` |

The poll terminated on its own condition at try 12 (`POLL_DONE`), well inside the 40-try budget: all five producer reports present (`S1-freeze-hygiene.md`, `S2-tools-docs.md`, `S3-fixture-author.md`, `S4-fixture-docs.md`, `S5-knowledge-notes.md`), `corpus/tools/README.md` modified, `corpus/knowledge/r98-clerk-scope-note.md` present. No stall-escape was needed, and no wait was spent on SELF (the poller never counted V47's own report).

Producers observed landing during the seat's window: S3's r98 JSON tables + `fictional-excerpts.md` (20:28), S3's r95 repair and S5's r95/r96 addenda (20:28–20:32), S4's r98 `README.md` + `claim-excerpt-map.md` (between 20:29 and 20:31 — the map was still a byte-copy of r97's at 20:29:08, per my own `diff -q` and V11's log), S5's `r98-clerk-scope-note.md` (20:32), S1's `dependency_freeze.py` + contract (20:31–20:32). The r98 receipt was first measured on the in-flight r97 map copy (17/17) and re-measured after S4's map landed (20/20); only the post-landing receipt is claimed. No plan was verified at any point.

## 7. Final status after the poll window

**Poll outcome: complete at try 12 (20:35:32) — no producer artifact or report was absent.** Final change set vs `9a3d648` (whole corpus tree): modified — `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md`, `corpus/knowledge/r95-aftermath-scope-note.md`, `corpus/knowledge/r96-response-scope-note.md`, `corpus/tools/README.md`, `corpus/tools/dependency-freeze-contract.json`, `corpus/tools/dependency_freeze.py`; new — the ten `corpus/fixtures/r98-clerk-filing/` files and `corpus/knowledge/r98-clerk-scope-note.md`. `corpus/tools/support_check.py` is untouched (`55a5eb27…`, empty diff vs `9a3d648`).

**Receipt battery re-run after the poll (pass 4) is byte-identical to pass 3 and pass 2 for all nine clusters** — r87 `952354ac…`, r88 `b5c4075d…`, r89 `ec3cd3fb…`, r93 `63f90ea5…`, r94 `d0ff6982…`, r95 `efae7be2…`, r96 `ca7a6815…`, r97 `a109856d…`, r98 `090fa430…`; all `RESULT PASS`, exit 0. Live map hashes after the whole battery: r87 `3ad4e810…`, r88 `b3b79fe5…`, r89 `72514061…`, r93 `17f0e812…`, r94 `ed9527c5…`, r95 `80440d61…`, r96 `e851f068…`, r97 `49d4834e…`, r98 `c1099d0e…` — unchanged from before the demos. The delivered r98 receipt (20/20, 22/22 rows, 18/18 anchors) and the post-repair r95 receipt (15/15, 17/17 rows) are independently quoted with identical numbers by S3's, S4's and V11's reports.

**Bottom line: PASS — every `support_check` receipt r87→r98 replays unchanged/exactly as declared (r87 14+8, r88 10+2, r89 1 paraphrase, r93 12+3, r94 14+2, r95 15+2, r96 16+2, r97 17+2, r98 20+2; all `RESULT PASS`, exit 0; r87/r88/r93/r94/r89/r95/r96/r97 stdout byte-identical to the r95/r97 manifests, r98 `090fa430…` stable across six runs), S3's r95 carried-wording repair is proven receipt-neutral (data rows and inventory byte-identical; frozen-map and repaired-map outputs identical, `efae7be2…`), and all eight r94-round silent-failure vectors still fail/warn on scratch against r90/r91 controls (T1/T2/T3/T7/T8 exit 1 vs r90 silent exit 0; T5b and T6 WARN + `RESULT PASS WITH WARNINGS` vs r90 silent exit 0; T4/T5a fail on both) — with the three r94 F15 mutants that remain silent in `support_check` (b2, a, d) reported exactly as the documented, tool-scoped blind spots they are, each closed by `map_obligations` (`missing_obligation`, `source_id_mismatch`) or C2's gate, not by this tool.**
