# V41 — spec-conformance (round 96)

**Seat:** V41 spec-conformance (leaf, verifier). **Mandate:** map every LOG-declaration
line of the r96 declaration to demonstrated evidence or NOT-demonstrated; include invariants.
**Lane root:** `/home/vgpnk/Projects/shokunin/lore-shokunin` (all commands run from there with
`python3`). **Baseline:** r95 closure `dcb2d92` (worktree HEAD `60dba0c`, the r95 SCORECARD
closure commit — no commits this round).
**Writes by this seat:** this report, `.ufo/waves/round-96/seats/V41-scratch/` — and one
unintended corpus write disclosed as **F1** below (my probe caused a stray pin in Q3's
contract; I did not repair it because the owner and other seats quote the current bytes).

## 0. Verified revision (hashed before and after the whole battery; identical)

```
2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8  corpus/tools/map_obligations.py
97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6  corpus/tools/map-obligations-contract.json
965b29cd41a8af14293eb2e1948f58f310e58c6e752b8fe322c5445b20a91f24  corpus/tools/README.md
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9  corpus/fixtures/r96-crossing-response/timeline.json
9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d  corpus/fixtures/r96-crossing-response/sources.json
ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456  corpus/fixtures/r96-crossing-response/README.md
6db32ca24f5eff5baa3ebe589e8d3bcb6b256fec18dee2468211d7d0fae157c6  corpus/knowledge/r96-response-scope-note.md
```

`sha256sum` over all delivered artifacts was captured to `V41-scratch/final-hashes-before.txt`,
the full battery re-run, then re-captured to `final-hashes-after.txt`; `diff` reported no
difference — **the battery ran on frozen bytes and wrote none of them**.
The four tool/contract hashes match the producers' own report hashes (Q1 `2b0ba815…`,
Q2 `97b76bb8…` / `965b29cd…`, Q3 `a3b57978…` / `7d568cc4…`).

**Poll-wait record.** Artifacts and producer reports were polled at 20 s cadence
(`V41-scratch/poll.sh`, 45 tries; `poll2.sh` for Q2). Landed: Q4 report 17:42, Q3 17:47,
Q5/Q6 17:45–17:46, Q1 17:51, Q2 17:52. Final battery 17:53+. No producer was ABSENT.
Mid-flight revisions were **sampled but not credited**: at 17:43–17:44 the in-progress tool
crashed its own `--self-test` (`NameError: name 'SELF_TEST_CASES' is not defined`) and the
in-progress legacy dialect path returned cascades of `missing_obligation`; those bytes were
superseded before delivery and are recorded only as revision-sampling context (same convention
as r95 V29 §3.2).

## 1. Declaration → evidence map

### C1 — calibration (tool bundle)

| Declaration line | Evidence (command → observed) | Verdict |
|---|---|---|
| (a) before: deletion class exits 0 with shortfall only in the non-gating receipt | Frozen r95 tool copy (sha256 `d1c239cc…`), r95 copy with `entities[1].claims` deleted + map row J07 removed: `python3 baseline/map_obligations.py del2 --map claim-excerpt-map.md` → `OBLIGATIONS raw=14 mapped=14` / `INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH` / `RESULT PASS` / `EXIT=0` | DEMONSTRATED |
| (a) after: mismatch is GATING, exit 1 with stable `inventory_mismatch` | Same mutation, delivered tool: → `FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 15/2/17; observed 14/2/16` / `RESULT FAIL` / `EXIT=1` | DEMONSTRATED |
| (a) isolation: neither edit alone is silent | Row removed, key intact → exit 1 (`inventory_mismatch` + `missing_obligation`); key renamed, row kept (Q1/V01/V07) → exit 1 (`phantom_obligation` + `schema_drift`) | DEMONSTRATED |
| (b) contract 22 → 24 cases | `json.load(...)['self_test']['cases']` → `n cases: 24`; ids = the 22 r95 ids + `schema_drift` + `inventory_mismatch`, each pinned `{'exit': 1, 'finding_ids': [<own id>]}` | DEMONSTRATED |
| (b) `--self-test` 24/24 | `python3 corpus/tools/map_obligations.py --self-test` → 24 × `SELF-TEST PASS`, 0 FAIL, `RESULT PASS`, `EXIT=0`; includes `SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']` and `SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']` | DEMONSTRATED |
| (c) before: legacy dual-pointer cell silently ignored | Frozen r95 tool, r88 copy with P2 cell `` `entities[1].first_appearance` (Evin): `entities[1].claims[0]` `` → `OBLIGATIONS raw=10 mapped=10` / `RESULT PASS` / `EXIT=0` (no finding) | DEMONSTRATED |
| (c) after: stable `dual_pointer`, exit 1 | Delivered tool, same copy → `FINDING dual_pointer: row P2 (line 24) names a second pointer token 'entities[1].claims[0]' alongside entities.json#/1/first_appearance` / `RESULT FAIL` / `EXIT=1`. Second form (second pointer in the parenthetical: `` `entities[2].first_appearance` (Quiet Rise; `entities[2].claims[0]`) ``) → `FINDING dual_pointer: row P3 (line 25) …` / exit 1. Unmutated r88 → `RESULT PASS` exit 0 | DEMONSTRATED |
| Non-regression: frozen-r93 replay unchanged | `python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93` → `SNAPSHOT inputs=4 digests=verified` / `OBLIGATIONS raw=12 mapped=12` / `INVENTORY 12/12; 3/3; 15/15` / `FROZEN expected=PASS/0 findings=none matched` / `RESULT PASS` / `EXIT=0` (identical to my pre-delivery baseline capture) | DEMONSTRATED |
| Non-regression: r87/r89 fail-closed unchanged | Sweep of 12 `r87-*` + 11 `r89-*` dirs → `all_exit2=yes`; finding text byte-identical to the baseline tool: `FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer` (r87) and `…table needs one JSON fact pointer and one source-ID column` (r89) | DEMONSTRATED |
| Non-regression: r87–r96 fixture exit classes | Full sweep of all 170 fixture dirs → `exit 0: 5` = {r88-m3-maya-cluster, r93-m2-kojiki-cluster, r94-paired-crossing, r95-crossing-aftermath, **r96-crossing-response**}, `exit 2: 165`. Pre-delivery baseline was exit 0 = 4, exit 2 = 166 (r96 dir mid-write). The only class change is r96 2→0, which C2 declares | DEMONSTRATED |
| Non-regression: 0/1/2 contract | no-arg → exit 2; `--bogus` → exit 2; r95 fixture → exit 0; `exit_codes {0: PASS, 1: FAIL, 2: ERROR}` unchanged in the contract | DEMONSTRATED |
| Non-regression: r87–r96 fixture bytes | `git status --porcelain corpus/fixtures/r95-crossing-aftermath corpus/fixtures/r94-paired-crossing corpus/fixtures/r88-m3-maya-cluster` → empty (0 lines); r96 is the one added directory | DEMONSTRATED |

### C2 — depth (new fixture)

| Declaration line | Evidence | Verdict |
|---|---|---|
| Preserving copy of r95-crossing-aftermath | `cmp -s` per file: `BYTE-IDENTICAL` for entities.json, relations.json, contradictions.json, inspiration-note.md, source-excerpt.md; `CHANGED` for sources.json, timeline.json, fictional-excerpts.md (the three Q4/Q5-authored files) | DEMONSTRATED |
| New source `evin-response-note` | `sources.json` 4→5; appended entry id `evin-response-note`, reliability note asserting no accusation/no winner/unresolved | DEMONSTRATED |
| New tick-12 event `response-evin-salt-court` (evin, salt-court, depends_on `["aftermath-missing-evin"]`) | `timeline.json[4]` = `{tick: 12, entity_id: evin, place_id: salt-court, depends_on: ['aftermath-missing-evin'], source_id: evin-response-note}`; inherited `timeline[0:4]` parsed-equal to r95 (`True`) | DEMONSTRATED |
| Counts 5/1/4 → 5/1/5 | `json.load` counts: r95 `entities=5 relations=1 contradictions=0 sources=4 timeline=4`; r96 `5/1/0/5/5` (entities/relations/contradictions/sources/timeline) | DEMONSTRATED |
| No new claims/entities/relations | entities.json and relations.json byte-identical to r95 ⇒ no new claim/entity/relation records; inherited sources `[0:4]` parsed-equal | DEMONSTRATED |
| 16 map obligations (15 inherited + 1 new event) | Map rows J01–J15 + J16; normalized comparison (dropping the path-qualified namespace column) → `common: 15 normalized-mismatched: []`; only difference in raw bytes is the re-qualified namespace `r95-crossing-aftermath:` → `r96-crossing-response:`; `new in r96: ['J16']` = `timeline.json#/4`, span 33-42, `verbatim`. Declared inventory line: `16 JSON facts; 2 editorial rows; 18 total mapped rows; 14 distinct excerpt anchors` | DEMONSTRATED |
| `map_obligations` receipt | `python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response` → `OBLIGATIONS raw=16 mapped=16` / `INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18` / `RESULT PASS` / `EXIT=0` | DEMONSTRATED |
| `check_bible` CLEAN | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response` → `CLEAN: schema, citations, relations, timeline; 0 violations` / `EXIT=0` | DEMONSTRATED |
| Census 169 → 170 | `git ls-tree -d --name-only HEAD:corpus/fixtures \| wc -l` → `169`; `find corpus/fixtures -mindepth 1 -maxdepth 1 -type d \| wc -l` → `170` | DEMONSTRATED |
| Unresolved; no accusation, no winner, no contradiction asserted | Delivered prose carries the bounds explicitly: `fictional-excerpts.md:38-40` "I make no accusation against Aru." / "I select no winner between our two accounts." / "Both accounts stand unresolved."; `README.md:11` and `claim-excerpt-map.md:54` restate them; `contradictions.json` remains `[]` (byte-identical to r95) | DEMONSTRATED (lexical); semantic audit not attempted by this seat — depth seats V13/V32/V56 own that |
| Supporting receipt (not claimed, checked) | `support_check` r96 → `SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; MODES 18/18; VALIDATED-ROWS 18/18` / `RESULT PASS` / exit 0 | DEMONSTRATED |
| No canon-truth/rights/identity inference | The delivered README states the reuse of inherited IDs "does not imply a separate source, entity identity, or contradiction"; no positive evidence of an overclaim was found in the fixture prose. Full semantic judgment is outside this seat's lexical scope | PARTIAL (declared bound present; semantic audit not attempted) |

### C3 — coverage (new gate)

| Declaration line | Evidence | Verdict |
|---|---|---|
| New gate + persisted contract exist | `corpus/tools/dependency_freeze.py` (470 lines, stdlib only) + `corpus/tools/dependency-freeze-contract.json`; `git status` shows both as the only new tool files | DEMONSTRATED |
| Frozen per-fixture dependency-edge inventory + relation endpoints + content digests for the chain | Contract pins keyed `r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`, each with `events{id→{depends_on, endpoint{tick,entity_id,place_id}}}`, `relations` triples, per-file and `content_sha256` digests, and `counts` | DEMONSTRATED |
| Chain verifies 4/4 clean (exit 0) | `python3 corpus/tools/dependency_freeze.py corpus/fixtures/<each>` → r88 `events 2/2; dependency-edges 0/0; relations 0/0`, r94 `3/3; 2/2; 1/1`, r95 `4/4; 3/3; 1/1`, r96 `5/5; 4/4; 1/1`, all `RESULT PASS` `EXIT=0` | DEMONSTRATED |
| BR-01 mutation → exit 1 `REDUCTION-DETECTED` | Scratch copy named `r94-paired-crossing` (pin keyed by basename) with `evin-ninth-bell` dropped from the tick-10 `depends_on` → `dependency-edges 1/2` + `FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']` / `RESULT FAIL` / `EXIT=1` | DEMONSTRATED |
| Added edge → exit 1 | Phantom edge on `evin-ninth-bell` → `FINDING ADDITION-DETECTED: event evin-ninth-bell gained depends_on ['aru-ninth-bell']` / exit 1 | DEMONSTRATED |
| Endpoint change → exit 1 `ENDPOINT-CHANGE` | `place_id` chalk-stair→quiet-rise → `FINDING ENDPOINT-CHANGE: event paired-crossing-decision.place_id: 'chalk-stair' -> 'quiet-rise'` / exit 1; relation `from`/`to` flip → `FINDING ENDPOINT-CHANGE: relation endpoints changed: removed [aru, evin, …]; added [evin, aru, …]` / exit 1; event removed → `FINDING REDUCTION-DETECTED: event evin-ninth-bell is missing` / exit 1 | DEMONSTRATED |
| could-not-evaluate → exit 2 | Description-only edit (inventory-neutral) → `FINDING DIGEST-MISMATCH: content digest … != pin …; fixture bytes changed outside the frozen inventory` / `RESULT ERROR` / `EXIT=2`; unpinned fixture → `UNPINNED-FIXTURE` exit 2; missing dir → `UNPINNED-FIXTURE` exit 2; no-arg → `INVALID-ARGUMENTS` exit 2; `--self-test <dir>` → `INVALID-ARGUMENTS` exit 2 | DEMONSTRATED |
| `--self-test` persisted | `python3 corpus/tools/dependency_freeze.py --self-test` → `SELF-TEST 14/14` / `RESULT PASS` / `EXIT=0` (14 cases persisted in `self_test.expected`) | DEMONSTRATED |
| `--freeze` exists but is not used in the admitted path | `--freeze` exists (`parser.add_argument("--freeze", … "(re)build the pin for DIR (delivery-time only)")`). **Caveat:** it *was* invoked during the round and its write landed inside the delivered contract (F1) — the admitted verify/self-test path itself does not call it | DEMONSTRATED with caveat |
| Zero corpus modifications beyond the two new tool files | `git status --porcelain` → tracked modifications are `LOG.md` (declaration append, +67/0), `corpus/tools/map_obligations.py` (Q1), `map-obligations-contract.json` + `README.md` (Q2); untracked additions are `.ufo/waves/round-96/`, `corpus/fixtures/r96-crossing-response/`, `corpus/knowledge/r96-response-scope-note.md`, and Q3's two tool files. No fixture or other corpus file was modified by the C3 work | DEMONSTRATED |

### Process / admission lines

| Declaration line | Evidence | Verdict |
|---|---|---|
| Baseline = r95 closure `dcb2d92` | `git log --oneline -3` → `60dba0c` (r95 close SCORECARD), `dcb2d92` (r95 freeze admitted wave), `fb118c4` (r94 close). `dcb2d92` is the declared baseline; HEAD is the follow-on closure commit | DEMONSTRATED |
| 6 producer seats with exclusive byte-ownership | Q1–Q6 reports all present; each declares its owned files and `git status` matches (Q1→tool; Q2→contract+README; Q3→two new tool files; Q4→fixture JSON/excerpts; Q5→fixture README+map; Q6→knowledge note). One cross-seat write exists — mine (F1) | DEMONSTRATED (with F1) |
| Everything else read-only | No modification to SCORECARD.md, SKILL.md, PROVINCE.md, SHONEN.md, README.md, or any r87–r95 fixture: `git status --porcelain <those paths>` → empty | DEMONSTRATED |
| Seat reports exclusive under `.ufo/waves/round-96/seats/` | 50 reports in-lane at this report's write (still growing as verifiers land); `/home/vgpnk/Projects/shokunin/.ufo/waves/round-96/` does not exist ⇒ zero parent-tree strays this round (the r94/r95 defect class did not recur) | DEMONSTRATED |
| Same-lane rule: no `[x]`, no promotion | `grep -c '\[x\]' SHONEN.md` → 0; `grep -c '\[~\]' SHONEN.md` → 4; no promotion/push (no new commits) | DEMONSTRATED |
| Scores remain unmeasured | No scalar scores introduced in the artifacts this seat can read; per-axis verdicts only (as in V33/V34/V37/V32) | DEMONSTRATED (by absence) |
| "64 seats on `opencode-go/deepseek-v4.1-flash`; one batched AgentSwarm" | Not observable from inside this seat: no `.ufo/waves/round-96/receipt.json` exists yet, and I cannot see the dispatch. 50 of 64 seat reports were on disk at this report's write (verifiers still landing) | NOT-DEMONSTRATED (out of seat's observability) |
| "r97 does not start on an unclosed r96" | No r97 artifacts exist; LOG.md carries no r97 section | DEMONSTRATED (by absence, at this cutoff) |

## 2. Invariants

1. **No commits, no pushes, no network, no nested agents** — HEAD `60dba0c2aa344860b10a2fc63e00468d1b134f27`
   unchanged through the whole session; every command this seat ran was local Python/stdlib.
2. **Baseline tool bytes preserved** — the r95 revision (`sha256 d1c239cc…`, md5 `d31b8182…`) was
   copied to `V41-scratch/baseline/` before any producer write and used for every before/after
   comparison; it was never run with `--freeze`.
3. **Declaration is append-only** — `git diff --numstat` → `67 0 LOG.md` (declaration added;
   nothing removed).
4. **Delivered bytes stable during verification** — before/after `sha256sum` over all delivered
   artifacts identical across the C1+C2+C3 battery.
5. **r95 continuation untouched** — r95 fixture (and r88/r94) show no git-visible change; the r96
   fixture's inherited JSON is parsed-equal to r95's and the map's inherited rows differ only in
   the declared path-qualified namespace column.
6. **Producer reports exist before verification** — no artifact was credited before its producer
   report was on disk (Q4 17:42, Q5/Q6 17:45, Q3 17:47, Q1 17:51, Q2 17:52; my final battery 17:53).
7. **Fail-closed preserved** — every error path observed (usage, unpinned/missing fixture, digest
   drift, malformed inputs) exits 2; every semantic failure exits 1; no path silently passes.

## 3. Findings

**F1 — stray `c3red` pin in the delivered contract; caused by this seat (self-disclosed).**
At 17:43, before I knew the tool writes through to the delivered contract, my first exploratory
harness ran `python3 corpus/tools/dependency_freeze.py --freeze .ufo/waves/round-96/seats/V41-scratch/c3red`
(recorded in `V41-scratch/c3-interim.log`, `EXIT=0`, `DIGEST eff4b354…`). The tool's `freeze()`
ends with `contract["pins"][name] = pin … CONTRACT_PATH.write_text(...)` — an unguarded write to
the delivered contract. Result: the delivered contract's pin set is
`['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response']`
with `c3red.fixture = .ufo/waves/round-96/seats/V41-scratch/c3red` (a scratch path that will be
pruned), instead of the declared four pins. Q3's report §7, V33's `v33-stray-pin-evidence.txt`
and V21/V22/V23/V57 all record it; Q3 chose to leave it because other seats quote the contract
hash. I did **not** repair it (that would be a second write to a file I do not own and would
invalidate quoted hashes). **Recommended admission condition:** delete the `c3red` key at closure
(or explicitly accept it), and give `--freeze` a scope guard so a verifier probe cannot launder
into the delivered artifact.

**F2 — mid-flight revisions are unsafe to credit (sampled, not counted).** At 17:43–17:44 the
in-progress `map_obligations.py` raised `NameError: name 'SELF_TEST_CASES' is not defined` on
`--self-test` (exit 1, 0 PASS lines) and its legacy dialect path emitted cascades of
`missing_obligation`/`phantom_obligation` on the *unmutated* r88 fixture. Both vanished in the
delivered revision. Not a delivery defect; recorded as evidence that per-seat "before" captures
must be revision-pinned.

**F3 — `corpus/fixtures/README.md` has no Round-96 section.** Its last census line (`:1194`)
still reads "169 fixture directories" at the r95 closure. The r96 declaration claims census
169→170 but (correctly, per its own byte-ownership list) did not claim a fixtures-README update.
Documentation lag, not a claim failure; flag for the closure note.

**F4 — `dependency_freeze` is not registered in `SKILL.md`/gate registry.** Consistent with the
declaration ("zero corpus modifications beyond the two new tool files") and with V33's bound
("no admitted-path registration"), but the new gate is therefore discoverable only through
`corpus/tools/` and Q3's report.

**F5 — environment: `/tmp` inode-exhausted** (`df -i /tmp` → `1048576 1048576 0 100%`), as
reported independently by Q2 §5 and Q1. Python's `tempfile` falls back to `/var/tmp`
(`tempfile.mkdtemp()` → `/var/tmp/tmpfz_cyb6j`), so the C3 self-test still passes; any tool that
hard-codes `/tmp` would fail. Not claimed fixed this round (BR-05 class remains carried).

## 4. Bottom line

**PASS (bounded)** — every falsifiable r96 declaration line verifies on the frozen delivered
revision (C1 24/24 self-test + gating `inventory_mismatch` + `dual_pointer` both reproduced
against the r95 baseline; C2 5/1/5, 5 sources, 16/16 obligations, CLEAN, census 170; C3 chain
4/4 clean with the BR-01 reduction, addition and endpoint demos at their exact exits and stable
FINDING IDs), with two caveats: the delivered `dependency-freeze-contract.json` carries one
stray `c3red` pin that **my own** `--freeze` probe wrote (F1, owner-informed, unrepaired), and
the dispatch-level lines ("64 seats on `opencode-go/deepseek-v4.1-flash`", one batched swarm)
are NOT-DEMONSTRATED from inside this seat (no r96 receipt.json; 50 of 64 reports on disk at
this report's write).
