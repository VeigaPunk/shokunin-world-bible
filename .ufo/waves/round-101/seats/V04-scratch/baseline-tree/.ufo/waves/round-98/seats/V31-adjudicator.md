# V31 — adjudicator (round 98) — COMPLETION-WAVE SEAT (re-dispatch on hyper)

- Seat: **V31 adjudicator — FINAL all-axis adjudicator for round 98.** Original V31 was
  aborted by the host interruption; this is the completion-wave re-dispatch
  (`hyper/deepseek-v4.1-flash`, per the operator directive).
- Lane root for every command: `/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the
  PARENT repo `/home/vgpnk/Projects/shokunin`; every path used here is absolute or lane-root
  anchored). Baseline: r97 closure `9a3d648`; HEAD during the wave
  `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb`; the wave tree is uncommitted.
- Leaf seat: no nested agents, no commits, no pushes, no network. **Writes: this report only**
  (absolute path above). Every first-hand run was executed against copies under `/tmp/v31-*`, so
  **no lane file was written or mutated by this seat** (verified: `git status --porcelain` at the
  end of my run is byte-for-byte the declared producer set — §9).
- Role: read every existing seat report (5 producers + all verifier/judge seats), run **my own**
  first-hand verification of the load-bearing C1/C2/C3 claims on the delivered revision,
  reconcile conflicts, apply the admission rule, produce the per-axis table and the
  ADMIT/REJECT recommendation with exact conditions. I re-roll no harmed finding.

---

## 1. First-hand verification on the delivered revision

**Method (out-of-lane, so the lane is untouched):** `cp -r corpus /tmp/v31-mirror/corpus`; the
tool resolves its root as `ROOT = Path(__file__).resolve().parents[2]`, so a mirror at
`/tmp/v31-mirror/corpus/tools/` is self-consistent. Pre-round bytes came from
`git show 9a3d648:<path>`. All commands below are quoted with observed output.

Delivered revisions measured (lane, `sha256sum`):

```
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json
1d299c16bf9a0b34526f4a799cdd3117867f6d4d278866b66366b78700d79b84  corpus/tools/README.md
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
8e9e1774c1072bd1476d86977804e945301e4583acbfcb80a81b37a2334d4827  corpus/knowledge/r95-aftermath-scope-note.md
a9b51f8ccd78e0dcd8b5e890183068e48cdccd195065c43212211b65ee25f048  corpus/knowledge/r96-response-scope-note.md
1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8  corpus/knowledge/r98-clerk-scope-note.md
32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926  corpus/fixtures/r98-clerk-filing/README.md
c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba  corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md
```

These equal the revisions the producers declare in their own reports (S1 `03d04365…`/`153ebc5b…`;
S2 `1d299c16…`; S3 `80440d61…` + the four r98 tables; S4 `32efc78f…`/`c1099d0e…`; S5
`1162262c…`/`8e9e1774…`/`a9b51f8c…`) and the freeze manifest V30/V48 re-digested three times.

### 1.1 C1(a) — `SELF-TEST-MISMATCH` exits 2, pinned as case 17

Shipped self-test on the delivered bytes (mirror):

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE clean: exit=0 expected=0 findings=[] ok
CASE reduction_edge_drop: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
… (all 16 inherited cases `ok`, including path_mismatch and scope_refused)
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
SELF-TEST 17/17
RESULT PASS
EXIT=0
```

Pre/post exit-class probe (my own design: r97 tool+**r97 contract** in `pre`, delivered tool+**delivered
contract** in `post`; `self_test.expected.clean.exit` flipped 0→1 in each):

```
--- pre (r97 tool + r97 contract, corrupted clean expectation) ---
SELF-TEST 15/16
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT FAIL
EXIT=1
--- post (delivered tool + delivered contract, corrupted clean expectation) ---
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
SELF-TEST 16/17
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR
EXIT=2
```

Case-set growth measured by parsing both contracts: r97 closure expectation set = **16** keys
(`['addition_edge_phantom','clean','digest_tamper',…,'unpinned_fixture']`); delivered = **17**
(the added key is exactly `self_test_mismatch`). No inherited expectation removed or re-pointed.
Alignment with `map_obligations.py` confirmed in-tree (`corpus/tools/map_obligations.py:877-879`:
`RESULT ERROR` / `return 2`).

### 1.2 C1(b) — a path-less legacy pin is migrated in place by `--freeze`

Mirror with `pins.r95-crossing-aftermath.fixture` set to `null`; the same pin shape (verified
identical before/after edit: `fixture`, `revision 60dba0c2…`, `content_sha256 d541ae64…`, 5-file
set, events, relations) in both `pre` and `post` roots:

```
--- verify-only on the path-less pin (both revisions) ---
pre : FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs a repo-relative fixture path
      RESULT ERROR   EXIT=2
post: FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs a repo-relative fixture path
      RESULT ERROR   EXIT=2
--- --freeze on the path-less pin ---
pre : FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pin
      r95-crossing-aftermath already names None; freezing a same-named path elsewhere would
      rewrite the delivered pin
      RESULT ERROR   EXIT=2
post: FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
      DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
      RESULT PASS    EXIT=0
--- post: re-verify after migration ---
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS            EXIT=0
```

So: the pre-state is refused (manual contract edit was the only route), the delivered revision
migrates in place and then verifies; verification alone on an un-migrated path-less pin still
fails closed (exit 2). The r97 recorded-path guard is retained (S1 §2 post2, S2 §C1(b), V02,
V25 §4, V28 §2.2 all demonstrate the different-path `SCOPE-REFUSED`; I did not re-run that leg,
and record it as corroborated rather than re-measured by me).

### 1.3 C1(c) — contract `precedence` names the full exit-2 order and finding IDs

Delivered `precedence` field, read from the contract and byte-quoted:

> semantic inventory findings decide first (exit 1: REDUCTION-DETECTED, ADDITION-DETECTED,
> ENDPOINT-CHANGE); a content digest change the frozen inventory does not model exits 2
> (DIGEST-MISMATCH). Exit-2 (could-not-evaluate) checks run in this order and the first failing
> check decides: UNPINNED-FIXTURE (no pin for the fixture name) or CONTRACT-INVALID (unreadable
> contract or invalid pin), FIXTURE-MISSING (fixture directory absent), PATH-MISMATCH (invoked
> path differs from the pin's recorded path), FILE-MISSING / MALFORMED-JSON / MALFORMED-MODEL
> (model build), DIGEST-MISMATCH (inventory clean, bytes changed outside the frozen inventory),
> INVALID-ARGUMENTS (CLI usage), SELF-TEST-MISMATCH (--self-test observed outcome differs from the
> persisted case expectation); --freeze additionally raises SCOPE-REFUSED (target outside
> corpus/fixtures/**, or a same-named in-scope target that would rewrite an existing pin's
> recorded path). A path-less legacy pin is migrated in place by --freeze instead of refused.

Every exit-1 and exit-2 finding ID the tool can emit is named, plus `SCOPE-REFUSED` and the
migration sentence. (V07/V25 §5/V28 §2.3 additionally cross-check the named order against the
tool's check sequence; the text is prose and no checker parses it — a bound, not a defect.)

### 1.4 C2 — chain six fixtures, 6/6 clean; r97/r98 pins; V46 discharge

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath \
           r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
    python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; done
r88-m3-maya-cluster          events 2/2; edges 0/0; relations 0/0  DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279  RESULT PASS  exit=0
r94-paired-crossing          events 3/3; edges 2/2; relations 1/1  DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75  RESULT PASS  exit=0
r95-crossing-aftermath       events 4/4; edges 3/3; relations 1/1  DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9  RESULT PASS  exit=0
r96-crossing-response        events 5/5; edges 4/4; relations 1/1  DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6  RESULT PASS  exit=0
r97-crossing-acknowledgment  events 6/6; edges 5/5; relations 1/1  DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6  RESULT PASS  exit=0
r98-clerk-filing             events 7/7; edges 6/6; relations 1/1  DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133  RESULT PASS  exit=0
```

Contract pin set is exactly six (`r88-m3-maya-cluster`, `r94-paired-crossing`,
`r95-crossing-aftermath`, `r96-crossing-response`, `r97-crossing-acknowledgment`,
`r98-clerk-filing`), each with a repo-relative `fixture` path; the r98 pin carries
`clerk-filing-open` → `depends_on: ["acknowledgment-aru-records"]`, endpoint
`{tick: 14, entity_id: clerk-maren, place_id: chalk-stair}`.

**V46 discharge** — mirror control first, then V46's exact mutation:

```
--- control: intact r97 ---
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6
RESULT PASS            EXIT=0
--- mutate acknowledgment-aru-records.depends_on := [] ---
mutated sha256: 37a425b97af658d71b8dc8904f43fd75859905bac326489a71adb67004004eb1
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5; relations 1/1
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
RESULT FAIL            EXIT=1
--- other gates on the same mutated bytes ---
check_bible     CLEAN: schema, citations, relations, timeline; 0 violations   EXIT=0
map_obligations INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19 / RESULT PASS  EXIT=0
```

The mutated `timeline.json` sha256 `37a425b9…` is **byte-identical to the sha V46 recorded** in
its r97 report (`.ufo/waves/round-97/seats/V46-cross-gates.md:44`, `:109`), and the r97 pin digest
`3c922d20…` equals the digest V46 froze in its r97 scratch mirror (same file, line 101). The
discharge is real, not vacuous: at r97 the same bytes produced `UNPINNED-FIXTURE` exit 2 (V26 §2,
V06 §1). *(Method note: my first V46 run mislabelled its control — the mutation was applied before
the "intact" run. I re-ran the control on a fresh copy and it is the `RESULT PASS` line quoted
above; the corrected control is what I rely on.)*

### 1.5 C3 — r98-clerk-filing counts, obligations, census; r95 repair

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations          EXIT=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
… SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors);
  MODES 22/22; VALIDATED-ROWS 22/22 / RESULT PASS                    EXIT=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22 / RESULT PASS   EXIT=0
$ ls -d corpus/fixtures/*/ | wc -l
172
```

Parsed r98 counts (my own `json.load`): entities **6**, relations **1**, timeline **7**, sources
**7**, contradictions **0**; entity ids `[aru, evin, quiet-rise, salt-court, chalk-stair,
clerk-maren]`; source ids `[…, clerk-filing-note]`; ticks `[9,9,10,11,12,13,14]`. The appended
rows are exactly the declared ones — entity `clerk-maren` (kind `character`, name `Maren`,
`first_appearance clerk-filing-note`, one claim citing `clerk-filing-note`), source
`clerk-filing-note` (kind `fictional first-person note`, reliability note asserting no finding /
no verdict / no reconciliation / no resolution and not evidence of a breach, a continuing duty, a
winner, or an external historical fact), and event `clerk-filing-open` (tick 14, `entity_id
clerk-maren`, `place_id chalk-stair`, `depends_on ["acknowledgment-aru-records"]`, `source_id
clerk-filing-note`, description recording the filing and the matter OPEN with no finding and no
resolution). Census **172** (171 at r97 closure).

**r95 map repair (C3's repair half)** — whole-file diff vs the closure blob:

```
$ diff <(git show 9a3d648:corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md) \
       corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
49c49
< … The new relation encodes only the agreement for this crossing, not perpetual performance or alliance.
---
> … The relation encodes only the agreement for this crossing, not perpetual performance or alliance; the new tick-11 aftermath event records one reported non-arrival on one occasion.
$ git show 9a3d648:… | wc -l  →  53      $ wc -l < corpus/…  →  53
```

Exactly one line, one hunk, no table row / pointer / anchor / span / mode touched, line count
unchanged. Receipts unchanged by the repair: `support_check` r95 → `SOURCE-SUPPORT 15/15;
EDITORIAL-ANCHORS 2/2; MODES 17/17; VALIDATED-ROWS 17/17` / `RESULT PASS` exit 0;
`map_obligations` r95 → `raw=15 mapped=15` / `RESULT PASS` exit 0; `dependency_freeze` r95 →
`DIGEST d541ae64…` / `RESULT PASS` exit 0 (the map is not a pinned data file, so the pin is
unmoved). V15 and V47 additionally show the data-row block hash `206fe137…` identical pre/post,
which I corroborate by the one-line diff above rather than re-deriving.

### 1.6 The two dated correction addenda

`git diff --stat 9a3d648` gives `14 insertions / 0 deletions` for each of
`corpus/knowledge/r95-aftermath-scope-note.md` and `r96-response-scope-note.md` (pure appends,
historical text preserved). V29 re-derived their commit-history claims (committed blobs
`cc1df4dc`/`d1c239cc`/`2b0ba815`/`86b52949` and `8173bb97`/`97b76bb8`; the superseded shas
`9224a684…`/`6634e176…` absent from all commit trees) and V53 independently swept all 44 quoted
hashes across the three notes; I read those runs and reproduced the two current pins they hinge
on (`map_obligations.py 86b52949…`, `map-obligations-contract.json 2142b991…`).

---

## 2. Seat corpus and presence reconciliation

**Final state: 64/64 seat reports present — no presence gap at closure.** The seats directory now
holds 64 `.md` reports (roster diff: `missing: []`). The wave completed in two stages: at my first
cutoff the roster stood at 60/64 with `['V31','V36','V51','V57']` missing; then `V20-scope-creep.md`
and `V58-presence-final.md` landed (21:23:42, both read in full here), and finally `V36-receipt.md`
and `V51-endgame-monitor.md` (21:25:52) and `V57-mutual-wait-guard-2.md` landed. All six seats the
host aborted (V20, V31, V36, V51, V57, V58) delivered completion-wave reports; **V31 is this
report**. The last three landed *after* V36's own receipt snapshot (§4.1), which is why that
snapshot still reads 61 present — the true final roster is 64/64.

- Producer reports S1–S5: **all present**, read first-hand. Each declares the same delivered
  hashes I measured (§1); no producer report contradicts another on a measurable value.
- Verifier/judge reports: all 59 present. I read the load-bearing ones first-hand: V05, V06, V07,
  V08 (C2); V09, V11, V13, V15, V16 (C3); V17, V18 (preservation/mutations); V25–V30 (the six axis
  verdicts); V22, V23, V29, V33, V34, V35, V43, V44, V45, V47, V48, V49, V50, V53, V54, V55, V56,
  V59, V20, V58. V36/V51/V57 landed after my reconciliation pass; for those three I read their
  closing sections and the receipt V36 produced, not every line.

---

## 3. Per-claim reconciliation across the seats

**C1 (calibration).** Producers S1 (owner) and S2 (docs) claim PASS. Independent verifiers
V01 (mismatch pin), V02 (legacy migration), V03 (self-test), V04 (regression), V07 (precedence /
re-freeze scope), V08 (code review), V25 (verdict-calibration), V34, V35, V40, V52, V59, V48 all
reproduce the same four facts: exit-1→2 flip with the pinned 17th case, 16 inherited expectations
byte-identical, path-less migration with the recorded-path guard retained and verify-side
fail-closed intact, and the precedence text naming the full order. **My own runs agree on every
value.** One bounded contradiction is recorded (V25 §7, V30 obs 6, V22 item 12): the README's
carried "not gitignored" sentence — §4 below.

**C2 (coverage).** S1 (pins), S2 (docs) claim PASS; V05 (chain six), V06 (V46 discharge), V07
(re-freeze scope), V08 (code review), V18 (mutation matrix, incl. the r98 tick-14 edge through the
delivered pin), V26 (verdict-coverage), V49 (crosscheck), V54 (six-chain integrity), V48, V59 all
reproduce 6/6 clean and the V46 discharge on the exact mutation bytes `37a425b9…`. **My own runs
agree**, including the digest identity with V46's recorded r97 scratch digest. The only bound is
the declared one: the pin payload is the five JSON tables, so markdown/prose is unpinned (BR-01's
markdown half open) and non-inventory JSON changes are caught only as exit-2 `DIGEST-MISMATCH`.

**C3 (depth).** S3 (fixture), S4 (docs), S5 (note + addenda) claim PASS; V09 (checker), V10
(inherited equality), V11 (support/map), V12 (anchors), V13 (whole claim), V14 (anti-overclaim),
V15 (r95 repair), V16 (dependency probe), V27 (verdict-depth), V38, V39, V42, V45, V46, V47, V50,
V52, V55, V56, V59, V48 reproduce the before→after (5/1/6/6 → 6/1/7/7; 17→20 map obligations;
census 171→172), the CLEAN/PASS gates, the inherited-row preservation, and the r95 one-line
repair with unmoved receipts. **My own runs agree** on every value I measured (counts, gates,
census, one-line diff, r95 receipts). The anti-overclaim reading (no constructible
resolution/blame/winner assertion) is carried by V13/V14/V39/V50 with bounded, stated limits
(the checker is structural/lexical, not testimonial).

---

## 4. Conflicts reconciled explicitly

1. **`receipt.json` — skeleton superseded; the final receipt is correct except for its snapshot
   count.** When I first audited it, the receipt was V36's un-finalized skeleton
   (sha256 `50251f0e4e563ec301002a902027d8138398a0457479ca1afb51ebe93c637833`): `reports_present = 0`,
   `reports_absent = [all 64]`, and a `candidate_revision_pinned` taken at 20:29:02 whose values I
   re-hashed as **7 of 16 drifted** (`dependency_freeze.py`, the contract, `tools/README.md`, both
   scope notes, r98 `README.md`, r98 `claim-excerpt-map.md`), 9 match. (V58 §5 says "6 of 16" while
   its own table lists seven rows — a harmless arithmetic slip in V58; my count is 7.) **This is now
   resolved:** V36's completion-wave pass wrote the final receipt
   (sha256 `3f65a310ad1d2b8645c2d7b74b8c421373c6c59553f9e2b24d7ae2ac4bd2edf5`, snapshot
   2026-10-17T21:25:08-0300) which records `skeleton_superseded` (the old `50251f0e…` skeleton,
   `collection_reports_present: 0`), carries per-seat `report_path` + `report_sha256` rows for all 64
   seats, and whose **17 `candidate_revision_pinned` entries all match the delivered bytes (0
   drift)** with `missing_candidate_paths = []`. **One residual:** the receipt's
   `collection_snapshot` was taken 44 s before the last three reports landed, so it reads
   `reports_present = 61`, `missing = ['V31','V51','V57']`, and
   `missing_are_exactly_completion_wave_seats = False` — the true roster is 64/64 (§2).
2. **Parent-tree stray — V20 says FAIL with an attribution; V30/V17/V24/V59 record it as an
   unattributable note.** Both are right about the bytes; they differ on attribution. I verified
   both sides: `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` exists (105 bytes, mtime
   2026-10-17 20:30:10, content `python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py':
   [Errno 2] No such file or directory`), and `.ufo/waves/round-98/seats/V57-scratch/` holds
   `analyze.py` (5114 B) and `baseline-analyze.txt` (25 209 B) — the successful twin of the same
   redirect. V20's attribution to the aborted V57 is well-evidenced; V30's "no lore content, not
   attributable to a lore seat" is also literally true (the stray carries no lore bytes). I record
   the stray as a real, bounded out-of-lane blemish, **attributed to V57 (aborted) with high
   confidence**, inside the parent repo, not a lane file, not touched by any claim.
3. **Adjacency axis: V30/V24 PASS(bounded) vs V20 FAIL.** Not a contradiction once scoped: V20's
   FAIL is against the literal check "zero parent-tree strays" plus the 243 MB
   `V37-scratch/archive` mirror (flagged, not deleted) and three `V14-poll.*` files at the wave
   root; V30/V24's PASS is that `PROVINCE.md` is byte-identical, the lane change set is exactly
   the declared ownership, and no sibling-lane/domain tree was written. Both hold simultaneously.
   I grade adjacency **PASS (bounded, with a named out-of-lane stray and a cleanup flag)**.
4. **S2's README "lists only two files" is false as written.** Confirmed by me:
   `git diff --name-only 9a3d648 -- corpus/tools/` lists **three** paths — `corpus/tools/README.md`,
   `corpus/tools/dependency-freeze-contract.json`, `corpus/tools/dependency_freeze.py` — because
   the addendum's own README edit is in that scope. The substance (the other tools are
   byte-unchanged) is true. Recorded by V26 §7, V28 F1, V29 F-1, V33 NB.
5. **S2's README "not gitignored" claim is false.** Confirmed by me: `.gitignore:4` is
   `*-self-test-*/`, and `git check-ignore -v dependency-freeze-self-test-abc/
   map-obligations-self-test-xyz/ v05-self-test-scratch/` returns `.gitignore:4:*-self-test-*/`
   for all three. The README's r98 addendum (`:232`) re-asserts "the self-test scratch still lives
   under the repository root and **is not gitignored** — unchanged in r98", and `:99/:103/:123/:179`
   carry the same stale clause. The BR-05 residual it describes is closed by the gitignore rule
   (present since r97 commit `9d25df9`), so the sentence is stale and self-contradictory. Recorded
   by V25 §7, V30 obs 6, V22 item 12.
6. **V53's narrow FAIL (not re-rolled).** `corpus/knowledge/r98-clerk-scope-note.md:64` records S1's
   C1 landing as "`dependency_freeze.py` `03d04365…`, contract `c435239d…` at 20:32:51-03:00" —
   `dependency_freeze.py` is still correct, but the delivered contract is `153ebc5b…`, so the
   contract pin is a superseded mid-round intermediate. It was accurate when written (S1 moved the
   contract once more at 20:33:36), it is explicitly time-stamped, and the note itself instructs
   "Re-run all three commands and re-measure the tool revisions against the delivered revision
   before citing these receipts". V29 §F-2 and V21 treat it as a labelled, self-caveated snapshot;
   V48 §4.1 and V33 NB list it as a bound. I reproduce the bytes and record it as a **bounded,
   disclosed staleness — a closure repair item, not a C3 claim failure**; no receipt in the note
   depends on it, and the note's own checker pins are current. I do not re-roll it in either
   direction.
7. **V59's endgame ledger vs the final state.** V59 (§2) recorded 8 seats missing at its
   23:41:50Z cutoff (`V20 V24 V31 V32 V36 V51 V57 V58`); V24 and V32 landed after that cutoff, and
   all six host-aborted seats (V20, V31, V36, V51, V57, V58) landed completion-wave reports — the
   final roster is **64/64** (§2), with the last three landing ~44 s after V36's receipt snapshot
   (§4.1). V59's "no mutual-wait pair exists; the endgame was the co-wait cluster
   `{V31, V36, V58}` with bounded caps" is consistent with the observed aborts (the original V31
   was the 240-try all-reports waiter V59 saw alive) — no deadlock, an interrupt.
8. **Placeholder-window hazard (recorded, no claim impact).** Between S3's byte copy (20:28:24)
   and S4's rewrites (20:30), r98's `README.md`/`claim-excerpt-map.md` existed with r97 bytes; an
   existence-only poll is satisfied by the placeholder (S3 §D1, S4 §A, S5 poll, V11, V16, V26 §1,
   V48 §4.3). No C1/C2/C3 measurement rests on it (every seat and my own runs used content-gated
   or post-rewrite bytes).

---

## 5. Per-axis table (verdicts, no scalars)

| Axis | Round-98 movement | Verdict seat(s) | My adjudication |
|---|---|---|---|
| **Calibration** | improved (bounded) | V25 (PASS); V01–V04, V07, V34, V35, V40 corroborate | **improved (bounded)** — exit-1→2 pinned as case 17 (16 inherited unchanged), path-less legacy pin migrates with the guard retained, precedence text complete |
| **Coverage** | improved (bounded) | V26 (PASS); V05, V06, V18, V49, V54 corroborate | **improved (bounded)** — chain 6/6, r97/r98 pins, V46 discharge on the exact mutation bytes; pin payload = five JSON tables |
| **Depth** | improved (bounded) | V27 (PASS); V09–V16, V38, V39, V50, V55, V56 corroborate | **improved (bounded)** — 5/1/6/6 → 6/1/7/7, 17→20 obligations, CLEAN, census +1 clean, no constructible resolution reading |
| **Freshness** | improved (bounded) | V29 (PASS); V21, V53, V56 corroborate | **improved (bounded)** — the two carried stale note pins repaired by dated append-only addenda; two bounded conditions (S2 README diff sentence; the r98 note's time-indexed `c435239d…` snapshot) |
| **Operability** | PASS | V28 (PASS); V23, V19, V34, V35 corroborate | **PASS** — every documented command replays with its documented exit; two bounded findings (the `git diff` scope sentence; the internal self-test child env marker) |
| **Adjacency** | PASS (bounded) | V30 (PASS bounded); V24 (PASS); V17, V18, V19, V44, V59 corroborate | **PASS (bounded)** — `PROVINCE.md` and the province docs byte-identical; change set exactly the declared ownership; no sibling-lane writes. Named bounds: the parent-root stray `baseline-analyze.txt` (V57-attributed), the 243 MB `V37-scratch` mirror, three `V14-poll.*` wave-root files |

**No axis is harmed.** The three doc defects (README "not gitignored", README "lists only", the r98
note's stale contract pin) are doc-surface conditions — every gate and every quoted receipt still
replays — and the out-of-lane stray and scratch-bloat items are wave-process artifacts that touch
no lane byte. This matches the r96/r97 convention that such disclosed, non-gate-affecting items are
conditions, not material axis harm (V25 §8, V29 §F-1, V26 §7, V30 obs 6).

---

## 6. Admission rule application

Rule: *admit iff C1, C2 and C3 each verify on the delivered revision and no axis is harmed.*

- **C1 verifies** on the delivered revision (my runs §1.1–§1.3): exit-2 pin + 17/17 + legacy
  migration + precedence text.
- **C2 verifies** (§1.4): chain 6/6 clean with the declared digests; r97 and r98 pins present and
  load-bearing; V46's recorded r97 FAIL discharged on its exact mutation bytes (`37a425b9…`,
  `REDUCTION-DETECTED` exit 1) with the companion gates green.
- **C3 verifies** (§1.5): 6/1/7 counts with 7 sources, 20/20 map obligations, `check_bible` CLEAN,
  census 172, inherited rows preserved, and the r95 one-sentence repair with receipts unchanged.
- **No axis harmed** (§5): calibration / coverage / depth / freshness each improved (bounded);
  operability and adjacency PASS (bounded). Every bound is disclosed, gate-neutral, and named.

### RECOMMENDATION: **ADMIT** (round 98 is admissible), with conditions

Admit C1, C2 and C3, and record the following **exact admission conditions** (all are
documentation/finalization items; none touches a verified claim, a gate, or a pin):

- **AC-1 — refresh the final receipt's collection snapshot (owner: L1/V36).** Largely **satisfied**:
  V36's final receipt (`3f65a310…`, 21:25:08) already supersedes the skeleton, carries all 64 seat
  rows with `report_sha256`, has 17/17 pins matching the delivered bytes, and has
  `missing_candidate_paths = []`. The residual is the count: its `collection_snapshot` reads
  `reports_present = 61` / `missing = ['V31','V51','V57']` because it was taken 44 s before those
  three reports landed; update it to 64/64 (or add a dated snapshot note), and fill the L1-owned
  null fields (`agent_id`, `outcome`, `dispatch_tool_call_id`, `returned_summary`).
- **AC-2 — repair the two S2 README sentences (owner: closure doc pass).** (a) the "is not
  gitignored" clause at `:99/:103/:123/:179/:232` is false (`.gitignore:4 *-self-test-*/` covers
  it); (b) the "`git diff 9a3d648 -- corpus/tools/` lists only `dependency_freeze.py` and
  `dependency-freeze-contract.json`" sentence at `:284` is false as written (three files).
- **AC-3 — supersede the r98 note's time-indexed contract pin (owner: closure doc pass / S5).**
  `corpus/knowledge/r98-clerk-scope-note.md:64` should carry `153ebc5b…` or a dated supersession
  note; the sentence is self-guarded but the pin is presented as the landed revision. (V53 F1.)
- **AC-4 — clean the wave residue (owner: L1).** Remove/attribute
  `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` (the only out-of-lane stray; V57-attributed),
  decide on the 243 MB `.ufo/waves/round-98/seats/V37-scratch/archive/` mirror, and place the three
  `V14-poll.*` files under `seats/V14-scratch/`.
- **AC-5 — closure docs (owner: L1, as every round).** `corpus/fixtures/README.md` Round-98 section
  + census re-declaration, `corpus/README.md` bullets, `SKILL.md` freeze row, the
  `corpus/knowledge/r91-c9-watch.md` r98 row, and the `SCORECARD.md` admitted section (V22's
  thirteen stale-wording items; V35 item 5 confirms no r98 closure entry exists yet).
- **AC-6 — record the completion-wave tail in the closure notes (owner: L1).** **Resolved on
  substance:** all 64 seats delivered reports (§2), including the six host-aborted seats. The only
  remaining trace is AC-1's stale `61/64` count in the receipt snapshot; the closure should note
  that the last three reports (V36, V51, V57) landed ~44 s after V36's snapshot, so the receipt's
  `missing` list is a snapshot artifact, not a missing seat.

---

## 7. Bounds of this adjudication

- I verified C1/C2/C3 **behaviourally on the delivered revision** (my own runs, §1) and read the
  full seat corpus for the reconciliation. I did not re-derive every one of the 60 reports'
  measurements; where I rely on another seat's number I say so and cite the seat.
- My C1(b) run covers the path-less migration and the verify-side fail-closed leg; I did not
  re-run the different-path `SCOPE-REFUSED` leg and record it as corroborated (S1/S2/V02/V25/V28)
  rather than re-measured.
- The V46 discharge is verified on the delivered pin and V46's exact mutation bytes; the r98
  tick-14 edge equivalent is corroborated by V18/V26/V54, not re-run by me.
- Axis verdicts are the seats' with my own reconciliation; I add no scalar and re-roll no harmed
  finding (V53's narrow FAIL stands as recorded).
- This is an adjudication of the round's claims and axes only; it makes no canon-truth, rights,
  identity, or entailment ruling anywhere.

---

## 8. Write audit

- **Only file written: this report** (`.ufo/waves/round-98/seats/V31-adjudicator.md`, absolute
  path under the lane). All first-hand runs used copies under `/tmp/v31-mirror`, `/tmp/v31-c1`,
  `/tmp/v31-c1a`, `/tmp/v31-c1b`, `/tmp/v31-v46b`; **no lane file was written or modified**.
- `git status --porcelain` at the end of my run is byte-for-byte the declared producer set
  (`M` LOG.md, r95 map, r95/r96 notes, the three `corpus/tools/` files; `??` r98 fixture,
  r98 note, `.ufo/waves/round-98/`) — no stray, no deletion, no rename.
- No nested agents, no commits, no pushes, no network.

---

## Bottom line

**PASS — ADMIT round 98 (C1, C2, C3 all verified first-hand on the delivered revision; no axis
harmed), with six conditions (AC-1…AC-6), of which two are already resolved (the receipt is
finalized — only its 61/64 snapshot count needs a refresh — and the roster is complete at 64/64);
the live ones are: repair the two false S2 README sentences; supersede the r98 note's stale
`c435239d…` contract pin; clean the out-of-lane stray + V37 mirror + V14 wave-root files; do the
closure-doc pass.** C1: `--self-test 17/17` PASS exit 0, `SELF-TEST-MISMATCH` exit 1 (r97
bytes) → 2 (delivered) pinned as case 17, path-less legacy pin refused before / `MIGRATED`+PASS
after with verify-side fail-closed intact, precedence text names the full exit-2 order. C2: chain
6/6 clean, r97 `3c922d20…` / r98 `59a0f4fa…` pins, V46 discharge reproduced on its exact mutation
sha `37a425b9…` (`REDUCTION-DETECTED` exit 1, other gates green). C3: 6 entities / 1 relation /
7 events / 7 sources, `check_bible` CLEAN, `support_check` 20/20, `map_obligations` raw=20
mapped=20, census 172, r95 repair exactly one prose line with receipts unchanged. Axes:
calibration/coverage/depth/freshness improved (bounded), operability and adjacency PASS (bounded);
the one narrow FAIL (V53, stale note pin) and the receipt's 61/64 snapshot count are recorded, not re-rolled.
