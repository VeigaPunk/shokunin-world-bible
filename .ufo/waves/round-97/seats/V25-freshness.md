# V25 — freshness (round 97)

Seat: V25 freshness. Brief: *after producers* — stale-pin sweep of new bytes; knowledge note metadata; README commands replay; carried wording accuracy (r96 README now references repair? note for L1). Leaf seat: no nested agents, no commits, no network. Only write: this report; scratch under `.ufo/waves/round-97/seats/V25-scratch/`. All commands ran from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. I did not verify C1/C2/C3 semantics (other seats' scope); this report covers freshness only, with producer-doc parity noted where it is a freshness fact.

**Poll-wait:** producers were polled (20 s cadence) from 18:43. My first poll loop had a glob bug — `R[1-6]*` matched the scratch directories `R2-scratch`/`R4-scratch` as "reports" — spotted and killed before any verification, replaced with an `R[1-6]*.md` file-only poll at 18:43:55. Report arrivals: R1 18:48:15, R2 18:48:55, R4 18:50:15, R5 18:51:35, R6 18:53:55, R3 18:56:35 (all six present; fixture directory 18:44:35, knowledge note 18:50:55). No verification ran against a plan; every receipt below was taken on the frozen snapshot **after** all six reports existed (final receipts re-run 18:58:20).

## Frozen snapshot verified (17 new/modified bytes)

| byte | sha256 (12-hex prefix) | mtime |
|---|---|---|
| `corpus/tools/map_obligations.py` | `86b529496214` | 18:45:37 |
| `corpus/tools/map-obligations-contract.json` | `2142b9917694` | 18:46:12 |
| `corpus/tools/README.md` | `6278e59b8df0` | 18:47:13 |
| `corpus/tools/dependency_freeze.py` | `b06275f3bbde` | 18:53:00 |
| `corpus/tools/dependency-freeze-contract.json` | `27273be27d33` | 18:55:14 |
| `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` | `e851f068cfd7` | 18:43:42 |
| `corpus/knowledge/r97-acknowledgment-scope-note.md` | `5e3b4225c30d` | 18:52:38 |
| `r97 …/README.md` | `d9387b7d7326` | 18:49:14 |
| `r97 …/claim-excerpt-map.md` | `49d4834e124f` | 18:48:56 |
| `r97 …/fictional-excerpts.md` | `8ba491cb249d` | 18:44:30 |
| `r97 …/sources.json` | `438fb513a624` | 18:44:30 |
| `r97 …/timeline.json` | `73063a863a68` | 18:44:30 |
| `r97 …/entities.json` | `026af0bc2cda` | 18:44:16 |
| `r97 …/relations.json` | `c279254bc7de` | 18:44:16 |
| `r97 …/contradictions.json` | `37517e5f3dc6` | 18:44:16 |
| `r97 …/inspiration-note.md` | `58f5390e5928` | 18:44:16 |
| `r97 …/source-excerpt.md` | `b5edc2fd3c2e` | 18:44:16 |

All 17 shas match the producer reports exactly (R1 §delivered revision; R2 §delivered revision; R3 §delivered revisions; R4 §map sha + post-R5 cross-check; R5 §Deliverables + file hashes; R6 §Receipts). Snapshot re-checked at 18:58:12: `sha256sum -c` on the frozen list → **all OK, zero failures** (no byte moved between freeze and report). `git status --porcelain` shows exactly these tracked modifications/untracked additions plus the round's `LOG.md` declaration and `.ufo/waves/round-97/`.

## Check 1 — stale-pin sweep of new bytes (no HEAD pins): PASS

Sweep over all 17 bytes:

```sh
grep -nE '\bHEAD\b|rev-parse|latest revision|current revision' <the 17 files>
```

Observed: exactly one hit, a runtime call, not a stored pin:

```
corpus/tools/dependency_freeze.py:365:  result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, ...)
```

`--freeze` runs this at freeze time and writes the resulting fixed sha into pin metadata. Every revision pin in the new bytes resolves:

```sh
git rev-parse --verify 2393934237ea076366f3db6dceeff033edb52ab1^{commit}  # 2393934… (r96 closure, HEAD at refresh)
git rev-parse --verify 60dba0c2aa344860b10a2fc63e00468d1b134f27^{commit}  # 60dba0c2aa34… (r95 closure; r88/r94/r95 pins)
```

The refreshed contract (`27273be2…`) records top-level and r96-pin `revision` = `2393934…`; the r96 pin's five `files` digests are byte-identical to the files at that revision (checked all five with `git show 2393934:… | sha256sum` vs the working tree → `SAME` ×5). The r96 `content_sha256` is unchanged (`d422a9b3…`), matching R3's measured discrepancy note. No delivered byte contains a live HEAD reference or a dangling pin; `grep -rn '\.ufo/waves/round-9[67]'` over the delivered bytes → **no hits** (no scratch-path pins; the r96 `c3red` class does not recur).

One carried residual, same class as r96's Q6 note:

- `corpus/knowledge/r97-acknowledgment-scope-note.md:64` pins `map_obligations.py` `70795150…` (contract `97b76bb8…`). Neither is the delivered revision (`86b52949…` / `2142b991…`): `70795150…` was a real in-flight intermediate (V03/V04 polls at 18:45; R6's report records its 18:46 run) and `97b76bb8…` is the r96 contract. The note self-caveats ("Re-run all three commands against the delivered revision before citing these receipts"); I re-ran all three at the delivered revision — receipt values are identical (17/17 etc., below), so the recorded receipts remain true. The pin line itself is stale-vs-delivered, self-caveated: correctable next touch, not a false pin.

## Check 2 — knowledge note metadata header: PASS

`corpus/knowledge/r97-acknowledgment-scope-note.md:1-4` carries the standard header plus one addition: `source:` (cited-path list), `verified-at: 2026-10-17 — read every cited local record…`, `recheck: …`, and a new `citation-convention:` line (bare `file:line` resolves against the fixture named in the row/paragraph). The r95/r96 notes have three lines; the fourth is an addition, not an omission — it was declared by R6 to disambiguate its own citation audit.

Spot-checked citations all resolve (line numbers as cited):

```sh
sed -n '33p;36p' r97/sources.json        # aru-acknowledgment-note id / reliability_note — exact
sed -n '55p'      r97/timeline.json      # acknowledgment-aru-records id — exact
sed -n '19p;44,53p' r97/fictional-excerpts.md   # "for this crossing only" line 19; section 44-53; quoted lines 48-51 exact
sed -n '38p;57p'  r97/claim-excerpt-map.md      # J17 row; bounded reading — exact
sed -n '746p;761p;771p' corpus/fixtures/README.md  # Round 35 section / "Neither wins." / section end — exact
sed -n '226,230p' corpus/knowledge/2026-10-12-lore-decision-table.md  # r23 witnessed-absence row — exact
ls -d corpus/fixtures/*/ | wc -l        # 171 (note: 171; 170 at r96 closure) — exact
```

The note's receipt block (`:52-64`) reproduces under the delivered revision (see Check 3). `verified-at` date is the current round date.

## Check 3 — README commands replay: PASS

**r97 fixture README** (3 commands, "Replay from the repository root"), replayed on the frozen snapshot:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
# CLEAN: schema, citations, relations, timeline; 0 violations          exit 0
python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment
# INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15
# SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; … MODES 19/19; VALIDATED-ROWS 19/19
# RESULT PASS                                                         exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
# OBLIGATIONS raw=17 mapped=17
# INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
# RESULT PASS                                                         exit 0
```

**tools README, Round-97 addendum command:**

```sh
python3 corpus/tools/map_obligations.py --self-test
# SELF-TEST CASES 25/25 pinned … 25 SELF-TEST PASS lines … RESULT PASS  exit 0
```

**Earlier tools README commands still replay on the new revision** (no stale command):

```sh
python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster    # raw=10 mapped=10 PASS exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster  # raw=12 mapped=12 PASS exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing    # raw=14 mapped=14 PASS exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath # raw=15 mapped=15 PASS exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response  # raw=16 mapped=16 PASS exit 0
python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
# SNAPSHOT inputs=4 digests=verified / FROZEN expected=PASS/0 findings=none matched / RESULT PASS exit 0
# fail-closed preserved: r87-myth-cluster exit 2, r89-inspiration-paraphrase exit 2
```

**dependency_freeze commands** (Round-96 section): `--self-test` replays (`SELF-TEST 16/16` / `RESULT PASS` exit 0 — the section's printed count "(14/14)" is stale text, see Check 4); the chain replays clean 4/4 (`r88 15ef230e…`, `r94 2527beb9…`, `r95 d541ae64…`, `r96 d422a9b3…`, all exit 0). `dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment` → `FINDING UNPINNED-FIXTURE … RESULT ERROR` exit 2 — the r97 fixture is deliberately not in the pinned chain (R3 §Residuals 2), and no README command claims otherwise.

Repo gates on the frozen snapshot: `boundary_doc_check.py` → `CERTIFIED …` exit 0; `discriminate_check.py` → `RESULT: DISCRIMINATION HELD …` exit 0; no `*-self-test-*` scratch residue at the repo root.

## Check 4 — carried wording accuracy: PASS (with unowned stale docs flagged)

**r96 → r97 fixture README diff** (`diff` r96 vs r97 README): every count-bearing line updated and verified against delivered bytes — 5/1/5/5 → **5 entities / 1 relation / 6 events / 6 sources** (`len()` of the JSON tables); "the four inherited events… four inherited sources" → five/five; added source `aru-acknowledgment-note` / added event `acknowledgment-aru-records`; tick-12 now *inherited*, new tick-13 depends on `response-evin-salt-court` (`timeline.json[5]`); "16 obligations" → "17 … (the 16 inherited rows carried unchanged plus the new tick-13 event row)"; replay commands point at `r97-crossing-acknowledgment` (replayed above). Count-free paragraphs (editorial tick/ID encoding, `first_appearance: crossing-minute`, Spence design prompt, rights sentence) are carried verbatim and remain true.

**r97 map declarations** match the delivered bytes: `**Expected inventory:** 17 JSON facts; 2 editorial rows; 19 total mapped rows; 15 distinct excerpt anchors` vs `support_check` `DISTINCT-ANCHORS 15/15`; the editorial table's delimiter row is 7 cells matching its 7-cell header/rows; `grep -c "new relation"` = 0. Inherited row discipline independently re-checked at byte level: all 16 inherited rows are byte-identical modulo the namespace column (`r96-crossing-response:` ↔ `r97-crossing-acknowledgment:`), J17 the only new row; r97 `sources.json`/`timeline.json` are pure appends over the r96 arrays (diffs show additions only); the five copy files (`entities/relations/contradictions.json`, `inspiration-note.md`, `source-excerpt.md`) are byte-identical to r96.

**r96 README now references the repair?** No — and nothing in it became false. `corpus/fixtures/r96-crossing-response/README.md` has no blemish/repair text (`grep -n 'repair\|blemish\|delimiter'` → none); its one count ("16 source-attributed JSON pointer obligations") and its tick-12 wording remain exact after the repair. The repair is recorded where the round record expects it: the r97 knowledge note §"Cosmetic repair of the r96 map" and R4's report. The r96 fixture README needs no repair reference; **the item that does become stale is the round-level fixtures README** (below).

**Stale carried wording in read-only, unowned files (notes for L1 / closure doc pass — I confirm all independently):**

1. `corpus/fixtures/README.md:1213` — "Known cosmetic debts (no gate reads them; r97 candidates): the r96 map's editorial-table delimiter row has one extra cell, and one carried sentence says 'new relation'…" — **both debts are closed this round** (map `e851f068…`; delimiter 7 cells; `grep -c "new relation"` = 0). `:1217` still states the r96 census **170**; measured now 171. (R5 §Caveats, R6 §Adjacent observations flag the census; I confirm both.)
2. `SKILL.md:87` — "24 cases … `dual_pointer` behavior is demonstrated by mutation demos, not pinned by a persisted case; the two r96-added pins are droppable … both r97 debt" — **closed by the delivered R1/R2 bytes** (25/25 pinned; loader fails closed; neutralization red). `SKILL.md:89`'s "round-95/96 r97-debt items" is partially stale likewise. `SKILL.md:96`/`:99` still describe the chain as exactly the four fixtures — **still accurate** (r97 is not pinned; R3 §Residuals 2).
3. `corpus/README.md:37` — "`--self-test` (24 persisted cases)" → delivered 25; `:38` — "14-case persisted self-test" → delivered 16, and the chain description "(r88-m3 → r94 → r95 → r96)" remains accurate.

**Within-wave doc gap (R2-owned byte):** `corpus/tools/README.md:175` still says self-test "(14/14, persisted in the contract)" and lists all three r96 `dependency_freeze` hazards as open ("no `corpus/fixtures/` scope guard", "receipts are not path-bound", "`DIGEST-MISMATCH` does not name the changed file") — all three are closed by the delivered `b06275f3…`/`27273be2…`, and `grep -n 'SCOPE-REFUSED\|PATH-MISMATCH\|16/16' corpus/tools/README.md` → **no hits** (the new finding ids are undocumented there). R3 flagged this as an open doc-parity item (its report §Residuals 1); R2's report does not mention `dependency_freeze` at all. The map_obligations counterpart *was* superseded in place (`:173` "Residuals (r97 debt)" → Round-97 addendum "closed here"), so the round's own convention makes the `dependency_freeze` paragraph the one missing supersession. This is the only producer-doc parity gap I found; it does not affect any command or gate (all replay green), but it leaves the r97 hardening undocumented in the tools README for a reader of `:175`.

## Observations (low severity, disclosed; none block freshness)

1. **R6 note revision pins are stale-vs-delivered** (`70795150…`/`97b76bb8…` vs `86b52949…`/`2142b991…`), self-caveated; all three receipts reproduce at the delivered revision — same carried residual class as r96's Q6 note.
2. **tools README `:175` supersession missing** (R2-owned) — the round's only producer-doc gap; listed under Check 4.
3. **C2 claim's digest-change parenthetical falsified:** the claim said the r96 re-freeze happens because "the digest changes by the repair"; measured, the r96 `content_sha256` is unchanged (`d422a9b3…` — `data_files` covers only the five JSON tables; the repair touched only `claim-excerpt-map.md`). R3 records the discrepancy; I independently confirm (contract diff: r96 pin `revision` only, `60dba0c2…` → `2393934…`).
4. **Same carried "new relation" sentence remains in `r94`/`r95` maps:** r94's instance is accurate (r94 added the relation); r95's instance is carried-imprecise (r95 added an event) — outside this round's declared repair scope (r96 map only). Noted for the r98 candidate list.
5. **The claim's "chain verifies 4/4 clean at closure"** holds; `r97-crossing-acknowledgment` is not pinned and exits 2 `UNPINNED-FIXTURE` by design — no doc claims a 5-fixture chain.
6. **Environment:** `/tmp` inode exhaustion this round (R3 §; `/tmp` was full in r96 too) — all my outputs went to scratch under the lane repo; no delivered byte depends on `/tmp`. My own poll-glob bug (scratch dirs counted as reports) is disclosed at the top; no verification ever ran on in-flight bytes except the prep observations explicitly labeled as such, all re-measured at freeze.

## Bottom line

**PASS** — on the frozen r97 producer snapshot (all six reports present, all 17 delivered bytes sha-verified and unchanged at report time), the stale-pin sweep finds no HEAD pins and no dangling revisions (only the runtime `git rev-parse HEAD` inside `--freeze`; contract revisions `2393934…`/`60dba0c2…` resolve; r96 pin files match at its recorded revision), the knowledge note carries the standard metadata header (plus a declared citation convention) with every spot-checked citation resolving and census 171 correct, the r97 fixture README's three commands and the tools README Round-97 addendum replay to their documented outputs (25/25 self-test, r88–r96 battery, frozen replay, r87/r89 exit 2, dependency_freeze 16/16 + chain 4/4), and the carried wording is accurate with every count updated — with the flagged closure-side stale docs (`corpus/fixtures/README.md:1213/1217`, `SKILL.md:87/89`, `corpus/README.md:37/38`) and the one within-wave gap (tools README `:175` not superseded, R2-owned) reported as notes for L1, none blocking freshness.
