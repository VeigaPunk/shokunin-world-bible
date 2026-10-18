# V27 — verdict-freshness (round 95)

Seat: V27 verdict-freshness. Role: independent per-axis verdict for **FRESHNESS** —
were the freshness findings (V19, V20) repaired, merely absent, or still reproducing on
the **delivered bytes**, and what did the round actually deliver on this axis? Basis:
V19's finding F-1 and its sections 2–6, and V20's doc-parity findings A–E, each re-checked
by me on the delivered revision; V48/V17 pin evidence re-run as corroboration. Read-only;
this file is the sole artifact written (scratch work in `/tmp/v27-br02`, outside the repo;
no repo scratch dir, no commits, no network, no nested agents).

## Read state and freeze

- HEAD `fb118c42038ed27a747eec704b9aab41bb4b2ebe` (= baseline `fb118c4`). Working tree:
  `M LOG.md` (r95 declaration, 57 added lines), `M corpus/tools/{map_obligations.py,
  map-obligations-contract.json,README.md}`, untracked `corpus/fixtures/r95-crossing-aftermath/`,
  untracked `.ufo/waves/round-95/`. Nothing else in `corpus/` is modified.
- Delivered artifact set measured by me (`sha256sum`, 14 files); **all 14 hashes equal
  V19's verified-revision list exactly**, so the delivered set is frozen since V19's
  verification window:

```
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  corpus/tools/map_obligations.py
8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db  corpus/tools/map-obligations-contract.json
5d033c9db8a72801c9b8d5e609e01cddf1ace668711e24d0476b8cbd6879a264  corpus/tools/README.md
f87ed42ad4d42143bb84f13539f2db8ca0d5f221aaf4eaffdbd6874b5ef1ab9a  corpus/knowledge/r95-aftermath-scope-note.md
30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b  corpus/fixtures/r95-crossing-aftermath/README.md
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  corpus/fixtures/r95-crossing-aftermath/entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r95-crossing-aftermath/relations.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  corpus/fixtures/r95-crossing-aftermath/contradictions.json
fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a  corpus/fixtures/r95-crossing-aftermath/sources.json
3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177  corpus/fixtures/r95-crossing-aftermath/timeline.json
0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282  corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  corpus/fixtures/r95-crossing-aftermath/inspiration-note.md
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  corpus/fixtures/r95-crossing-aftermath/source-excerpt.md
```

## Verdict question, answered directly

The freshness findings are **not repaired and not absent**: V19 F-1 reproduces exactly on
the delivered bytes, and V20 A/B/C/E (doc/index sites) are still missing or stale. The
seat-owned file that V20's finding D covers (P2's `corpus/tools/README.md` addendum)
**landed in-round** and its documented receipts reproduce verbatim. No live pin has
drifted, no stale text was deleted to make anything disappear, and every new deliverable
byte is pin-free. V20's remaining items are index/README additions — **L1 integration
work by my seat instruction, not seat-work findings** — and the round's declaration of
them as pending is honest. Net movement of the axis: **none** (see verdict).

## V19 finding F-1 — stale revision pin in the delivered knowledge note (REPRODUCES)

V19 reported that `corpus/knowledge/r95-aftermath-scope-note.md:51` pins
`map_obligations.py` `9224a684…` while the delivered tool is `d1c239cc…`. Re-run:

```
$ sed -n '51p' corpus/knowledge/r95-aftermath-scope-note.md
Tool revisions at these receipts (2026-10-17T16:25-03:00): `check_bible.py` sha256 `ff9fd2aa…`, `support_check.py` `55a5eb27…`, `map_obligations.py` `9224a684…`. The C1 tool revision was still in flight during this round: … Re-run all three commands against the delivered revision before citing these receipts.

$ sha256sum corpus/tools/map_obligations.py corpus/tools/support_check.py corpus/fixtures/check_bible.py
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  corpus/tools/map_obligations.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

`9224a684…` was P1's revision at 16:25 and is **not** the delivered revision. **Reproduces
→ unrepaired.** Characterisation, verified in the same bytes: the block is a *timestamped
historical receipt provenance* ("at these receipts (2026-10-17T16:25-03:00)"), not a claim
that the hash is current, and the same paragraph carries the explicit re-run caveat; the
receipt values it qualifies are green at the delivered revision (V19 §3, re-run below), so
the note's receipt content is accurate and only the provenance hash is superseded. This is
the same self-limiting pattern V19 §5 accepted for the r94 census line — but unlike the
census line it is a content hash, and the lane treats content pins as currency, so I record
it as a **real bounded defect** and name a closure action (drop the value or re-pin).

## V19 sections 2–6 — status on delivered bytes (all confirmed)

- **§2 header PASS — confirmed.** `sed -n '1,3p'` shows `source:`/`verified-at:`/`recheck:`
  before the title; the `source:` line expands to 21 paths, all present
  (`cited paths: 21 missing: NONE`).
- **§3 replay commands PASS — re-run independently, all exit 0.**
  `check_bible` → `CLEAN: schema, citations, relations, timeline; 0 violations`;
  `support_check` → `INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17;
  DISTINCT-ANCHORS 13/13` / `SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; … MODES 17/17;
  VALIDATED-ROWS 17/17` / `RESULT PASS`; `map_obligations` → `OBLIGATIONS raw=15 mapped=15`
  / `INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17` / `RESULT PASS`.
  Census `ls -d corpus/fixtures/*/ | wc -l` → `169`.
- **§4 carried r94 wording PASS — spot-checked the strongest claim.** The map's own
  sentence ("the 14 inherited rows carry the r94 JSON pointers, excerpt anchors, spans, and
  delivery modes unchanged; only the path-qualification column names this fixture's cluster
  path") is exact: splitting the J01–J14 rows of both maps, the **only differing column is
  the path-qualification column (split index 4)**; J15 is the sole added row.
- **§5 citations PASS — spot-checked.** `sources.json:21` → `"id": "aru-aftermath-note",`;
  `timeline.json:33` → `"id": "aftermath-missing-evin",`; `claim-excerpt-map.md:36` → the
  J15 row.
- **§6 new-bytes behaviour claims PASS — re-run.** Contract persists 22 cases including
  `map_missing` and `invalid_arguments` (ids listed in order); `--self-test` → 22
  `SELF-TEST PASS` lines / `RESULT PASS`, exit 0; r88 `exit 0` (`raw=10 mapped=10`,
  `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12`); r87 `exit 2`
  `unsupported_map: pointer cells must contain one canonical inline-code pointer`; r89
  `exit 2` `unsupported_map: table needs one JSON fact pointer and one source-ID column`;
  frozen replay → `RESULT PASS` exit 0; r93 12/12, r94 14/14, r95 15/15 all `RESULT PASS`.
  The mid-round transient (22 implemented cases vs 20 persisted, `self_test_contract`
  `RESULT ERROR` exit 2) was observed by me too and is closed at delivery.

## V20 findings A–E — status on delivered bytes

| # | Finding | Status at delivered bytes | Owner |
|---|---|---|---|
| A | `corpus/fixtures/README.md` has no Round-95 section; last census is the r94 `168/34/134/421` line at `:1173` | `grep -c "r95\|Round 95"` → `0`; `:1173` unchanged | L1 (index) |
| B | `corpus/README.md` lacks r95 bullets; `:29` says "including the **r93** re-check entry"; `:35` says "(round 94)" + "**20** persisted cases" | `grep -c "r95"` → `0`; both lines verbatim as flagged | L1 (index) |
| C | `corpus/knowledge/r91-c9-watch.md` owes the r95 re-check row ("Next re-check: r95", `:253`) | exactly one `r95` match — the pointer itself; no r95 row; file sha256 `38511f66…` stable (matches V48) | L1 (unowned) |
| D | `corpus/tools/README.md` Round-95 addendum pending; r94 addendum `:95` "20/20" and `:99` exit contract would go stale | **LANDED** (`### Round-95 addendum: schema_drift, 22-case self-test, r88 map dialect`); every documented receipt reproduced by me, including the BR-02 demo verbatim (below) | P2 (seat) |
| E | `SKILL.md:86-89` registry row missing `schema_drift`, says "20 cases", scope "r93 and r94 clusters" | `grep -c "22 cases\|schema_drift"` → `0`; row unchanged | L1 (unowned) |

**V20-D receipt reproduction (seat-owned bytes, verified verbatim).** On scratch copies of
`r94-paired-crossing` (outside the repo):

```
# rename entities[0].claims -> assertions AND drop the map row (the README's before/after demo)
old tool (git show fb118c4:…/map_obligations.py): exit 0, OBLIGATIONS raw=13 mapped=13, RESULT PASS   (silent pass)
delivered tool: exit 1
  INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
  FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'assertions'
  RESULT FAIL
# rename with the map row KEPT (README: "reports phantom_obligation and schema_drift together, still exit 1")
delivered tool: exit 1
  FINDING phantom_obligation: entities.json#/0/claims/0 is not a raw source-attributed obligation
  FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'assertions'
  RESULT FAIL
```

The README's quoted finding text matches byte-for-byte. This is the one V20 finding whose
fix was seat work, and it is done and accurate.

## Independent pin corroboration (V48/V17 re-run)

- `sha256sum corpus/fixtures/check_bible.py` → `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`,
  equal to `boundary-doc-contract.json` `checker.sha256` and `corpus/tools/discriminate_check.py`'s pin.
- `sha256sum corpus/knowledge/holder-assessment-boundary.md` → `7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e`,
  equal to the contract's `document.sha256`.
- Frozen r93 snapshot digests vs live r93 bytes: **4/4 MATCH** (entities, relations,
  timeline, claim-excerpt-map); `--frozen …/map-obligations-r93` → `RESULT PASS` exit 0.
- `boundary_doc_check.py` → `CERTIFIED …` exit 0; `discriminate_check.py` → `DISCRIMINATION
  HELD` exit 0 (V48/V17 report the `e97613c` control at exit 2 as expected).
- **r94 closure repairs still fresh, not regressed:** `corpus/fixtures/README.md:1154`
  Round-94 section present (census line `:1173`); `corpus/README.md:21,:30,:35` carry the r94
  bullets; `corpus/tools/README.md` registers the tool; `SKILL.md:83-89` registry row
  present; `r91-c9-watch.md` carries the dated line-54 erratum (`:257`) and row 3 (`:253`).
- **New bytes carry no pins:** `grep -rn "HEAD|commit|git [a-z]|pin|sha256|hex-hash"` over
  the r95 fixture, its README/map, and the knowledge note → no matches (my own run of V19 §1's
  rule; the only hash tokens in new bytes are P5's note `:51`, i.e. F-1 itself).

## What improved, what was repaired, what was harmed

- **Repaired by this round: nothing.** No carried freshness finding was repaired by seat
  work (F-1 was created by this round; V20 A/B/C/E are L1 sites; the r94-era repairs were
  already in place at baseline and stayed intact).
- **Maintained against the round's own change:** the tool change would have reopened the
  r94 S1-class gap (README vs delivered tool: 20/20, no `schema_drift`, no r88 dialect) had
  P2 not landed; the dated Round-95 addendum keeps `corpus/tools/README.md` in parity with
  the delivered bytes, and its receipts reproduce. This is freshness *maintenance*, not
  net improvement (the round also created the need).
- **Newly harmed: one bounded item, F-1** — a superseded content-hash pin in the durable
  knowledge note, self-caveated in the same paragraph, receipt values verified green.
  Under the r94 convention (F27: disclosed findings carried as conditions are not netted as
  axis harm) this is a **condition**, not axis damage; under a strict pin-currency reading
  it is a bounded harm. I record both readings rather than smoothing the item.

## Verdict

**FRESHNESS: UNCHANGED** — no freshness finding was repaired and none was removed by the
round's own writes; every live pin (checker `ff9fd2aa…`, boundary document `7f815a93…`,
frozen r93 digests 4/4, C9 watch `38511f66…`) is fresh and unchanged; every new deliverable
byte is pin-free and its documented receipts reproduce verbatim on the delivered revision;
the round's one new stale item (F-1) is a bounded, self-caveated superseded hash whose
receipt values hold at the delivered revision, carried as a closure condition; V20's
remaining items are index/README integration owned by L1, not seat work, and their pending
status is declared, not concealed. Nothing on this axis improved, and nothing regressed
materially.

**Conditions for L1 at closure (named, from the findings — none are seat-work claims):**

1. **C-F1 (from V19 F-1):** drop `9224a684…` from
   `corpus/knowledge/r95-aftermath-scope-note.md:51` or re-pin it to the closure revision;
   the surrounding caveat already tells readers to re-run against the delivered revision.
2. **C-DOC (from V20 A/B/C/E + V19 §5):** append the Round-95 section to
   `corpus/fixtures/README.md` with the census `169 / 35 clean / 134 negative / 421
   violation lines / zero stderr` (my own count: 169 directories); add the
   `fixtures/r95-crossing-aftermath` and `knowledge/r95-aftermath-scope-note` bullets and
   refresh `corpus/README.md:29` and `:35`; append the fourth C9 re-check row to
   `corpus/knowledge/r91-c9-watch.md` (V48 §4 gives the exact outputs and wording); refresh
   `SKILL.md:86-89` (`schema_drift`, 22 cases, r88 dialect, residual status).
3. **C-WORD (observation, calibration-adjacent):** the round declaration's "12/12 PASS over
   the r88 map's obligations" counts editorial rows as obligations; P1 §6.1 discloses that
   the delivered receipt is `10/10` obligations + `2/2` editorial = `12/12` total rows. Any
   closure citation should use the delivered receipt wording.

## Limits

- I re-ran V19's and V20's checks and my own pin/receipt sweeps; I did not re-derive C1/C2/C3
  semantics, did not re-run the full 169-directory census sweep (I counted directories only;
  V20's 169/35/134/421 sweep is cited, not re-measured), and did not audit producer scratch.
- I reproduced all 14 per-file hashes of V19's frozen artifact set, but **not** V19's
  aggregate md5 `696eba461472d801b2bad74c142390ce` — the concatenation format is not
  specified, and my sorted-digest md5 is `b38679edf239d2f7a37d4dcb51dede4b`. Per-file
  equality is the freeze evidence I rely on.
- Timing: V19's report landed at 16:32 local (my poller caught it on try 44); my verification
  window is 16:33–16:45 local. V20 landed at 16:26. Both were read in full (V19 229 lines,
  V20 191 lines).

**Bottom line: UNCHANGED — V19's F-1 stale tool-revision pin in `r95-aftermath-scope-note.md:51`
reproduces on the delivered bytes (unrepaired, self-caveated, receipt values green) and V20's
A/B/C/E doc sites remain pending, but all live pins are fresh, every new deliverable byte is
pin-free, the one seat-owned doc fix (P2's Round-95 addendum) landed with verbatim-reproducing
receipts, and V20's items are L1 integration work — so r95 delivered no freshness improvement
and no material harm.**
