# V14 — c3-anti-overclaim (round 98)

Seat: V14 (verifier). Adversarial anti-overclaim sweep of all round-98 new bytes +
inheritance checks on the delivered r98 fixture, the r95 repair, and the r98 knowledge
note. Baseline: r97 closure `9a3d648`. Lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin`; every command below ran from the lane
root with `python3`. Leaf seat: no nested agents, no commits, no network. Only writes:
this report (absolute path) and `.ufo/waves/round-98/seats/V14-scratch/` plus the V14
poll script/log under `.ufo/waves/round-98/`. No corpus byte was written by this seat.

**Verified revision snapshot (measured 2026-10-17T23:33:27Z):**

```
c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba  corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  corpus/fixtures/r98-clerk-filing/contradictions.json
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  corpus/fixtures/r98-clerk-filing/entities.json
29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de  corpus/fixtures/r98-clerk-filing/fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  corpus/fixtures/r98-clerk-filing/inspiration-note.md
32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926  corpus/fixtures/r98-clerk-filing/README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r98-clerk-filing/relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  corpus/fixtures/r98-clerk-filing/source-excerpt.md
32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3  corpus/fixtures/r98-clerk-filing/sources.json
eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af  corpus/fixtures/r98-clerk-filing/timeline.json
1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8  corpus/knowledge/r98-clerk-scope-note.md
80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
8e9e1774c1072bd1476d86977804e945301e4583acbfcb80a81b37a2334d4827  corpus/knowledge/r95-aftermath-scope-note.md
a9b51f8ccd78e0dcd8b5e890183068e48cdccd195065c43212211b65ee25f048  corpus/knowledge/r96-response-scope-note.md
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py
c435239d94da54625b447f77e85dc734be241a1a7e9e5d9a63694fc415d47c99  corpus/tools/dependency-freeze-contract.json
```

The four S3-delivered hashes (`entities.json` `db2d8e5d…`, `sources.json` `32ee15b1…`,
`timeline.json` `eb24e084…`, `fictional-excerpts.md` `29e384bf…`) equal S3's report
values exactly; `relations.json` `c279254b…` equals the r97 base hash.

## Poll / artifact ledger (S3–S5)

Content-aware poll (`.ufo/waves/round-98/V14-poll.sh`, 20 s cadence, 40 tries, started
23:29:12 local) requiring content markers, not existence — `clerk-maren` in
`entities.json`, `clerk-filing-note` in `sources.json`, `clerk-filing-open` in
`timeline.json`, `clerk` in excerpts/README, `J20` in the map, `clerk` in the knowledge
note, plus reports `S3-*`/`S4-*`/`S5-*`.

- **Placeholder hazard observed.** At 23:28 the r98 dir was a byte-identical r97 copy
  (harness then printed `README.md: identical=True`, `claim-excerpt-map.md:
  identical=True`, entities len=5, timeline len=6). An existence-only poll is satisfied
  by the placeholder; this seat switched to content markers at 23:29:12
  (`V14-poll.log` try 4 vs `V14-poll2.log`).
- S3 fixture bytes: JSON/excerpts present by 23:29.
- S4 map rewrite: by 23:30:32 (`map:J20` cleared). S4 README rewrite: by 23:30:52
  (`readme:clerk` cleared; 5829 B at 20:30 local).
- S5 dated addenda in r95/r96 scope notes: present by ~23:29 (`git status` M).
- S5 `corpus/knowledge/r98-clerk-scope-note.md`: present 20:33 local (15839 B),
  verified below.
- Reports: `S3-fixture-author.md` and `S4-fixture-docs.md` landed; `S5-*` — see Poll
  outcome at the end.

## Check 1 — relation row byte-identical (the seat's explicit byte check)

```sh
$ cmp corpus/fixtures/r98-clerk-filing/relations.json \
      <(git show 9a3d648:corpus/fixtures/r97-crossing-acknowledgment/relations.json) && echo IDENTICAL
IDENTICAL
```

Observed: whole-file byte identity, so the single relation row is byte-identical; sha256
`c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` on both sides.
`contradictions.json` (`[]`), `inspiration-note.md`, `source-excerpt.md` are likewise
byte-identical to r97 (harness section A). The r98 fixture is a 10-file set equal to
r97's file set (harness A2: 4 files `identical=True`, 6 modified).

## Check 2 — inherited rows parsed-equal + append-only excerpt

```
entities.json: r98 len=6 base len=5; prefix[5] parsed-equal=True
sources.json:  r98 len=7 base len=6; prefix[6] parsed-equal=True
timeline.json: r98 len=7 base len=6; prefix[6] parsed-equal=True
fictional-excerpts.md: r98 startswith base bytes: True (base=3410B r98=4187B)
```

New rows exactly as declared: `clerk-maren` (kind `character`, `first_appearance`
`clerk-filing-note`, one attributed claim), `clerk-filing-note` (reliability note
asserting no finding/verdict/reconciliation/resolution), `clerk-filing-open` (tick 14,
`entity_id` `clerk-maren`, `place_id` `chalk-stair`, `depends_on`
`["acknowledgment-aru-records"]`).

## Check 3 — map rows J01–J20

Harness: 19 inherited rows (J01–J17, S01–S02) → 22 rows; inherited-row diffs in all
columns except the path-qualification column: `NONE`; new rows `J18`, `J19`, `J20`
appended after J17. Anchor/span verification against the delivered excerpt:

```
J18 span 60    anchor found line 60  "> I am Maren, clerk of the Chalk Stair registry, …"
J19 span 59-60 anchor found line 59  "> Tick 14: I filed both pending accounts at the Chalk Stair registry."
J20 span 55-64 anchor found line 59  (same filing sentence; span = the appended section)
```

`support_check` independently anchors all three (`PASS J18/J19/J20`). The map's declared
inventory (20 facts / 2 editorial / 22 rows / 18 anchors) matches the receipts exactly.

## Check 4 — r98 receipts (measured on the delivered revision)

```sh
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations          # exit 0
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing | grep -E 'INVENTORY|DISTINCT|ANCHORS|DUPLICATE'
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; MODES 22/22; VALIDATED-ROWS 22/22 / RESULT PASS  # exit 0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20 / INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22 / RESULT PASS  # exit 0
```

## Check 5 — census and strays

`git ls-tree -d --name-only 9a3d648 corpus/fixtures/ | wc -l` = 171; `ls -d
corpus/fixtures/*/ | wc -l` = 172; `comm` of the two sets: exactly one added dir
`corpus/fixtures/r98-clerk-filing/`, zero removed. `git status -uall` outside
`.ufo/waves/round-98/` shows only the declared round paths — no strays (r94-F01 class
did not recur in this seat's view).

## Check 6 — r95 map repair (repair half of C3) and pin no-harm

```sh
$ diff <(git show 9a3d648:corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md) \
       corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
49c49   # exactly one line, prose in "Timeline normalization and scope"
$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath | tail -3
RESULT PASS  (JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; exit 0)
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath | tail -2
OBLIGATIONS raw=15 mapped=15 / RESULT PASS  (exit 0)
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9 / RESULT PASS (exit 0)
```

Data rows byte-unchanged (17/17 equal), receipts unchanged, r95 pin still PASS at the
contracted digest; r96 map sha unchanged `e851f068…` (S3 cross-claim verified). The
repaired sentence is accurate for r95: the relation is inherited, and the round's new
row is the tick-11 event.

## Check 7 — S5 addenda and r98 note: every factual claim verified

**r95/r96 addenda** are append-only (`+14` lines each; historical text unrewritten) and
dated. Every hash they cite was re-derived from the closure commits this pass:

```
map_obligations.py            r94 fb118c4 cc1df4dc…  r95 60dba0c d1c239cc…  r96 2393934 2b0ba815…  r97 dd4df1b 86b52949…  (all match)
map-obligations-contract.json r95 60dba0c 8173bb97…  r96 2393934 97b76bb8…  r97 dd4df1b 2142b991…  (all match)
check_bible.py ff9fd2aa…, support_check.py 55a5eb27… re-measured current (match)
```

Re-run receipts: r95 `raw=15 mapped=15` PASS, r96 `raw=16 mapped=16` PASS, both
`support_check` PASS, r97 `raw=17 mapped=17` PASS. No stale pin remains uncorrected in
those two notes.

**r98 scope note** (`corpus/knowledge/r98-clerk-scope-note.md`): every cited line
checked. `sources.json:39/40/42` (id/title/reliability note), `entities.json:63/66/69/70`
(id/first_appearance/statement/source_id), `timeline.json:66/73` (id/description),
`fictional-excerpts.md:55-64` quotes, map rows at `:39/:40/:41` and bounded readings at
`:62/:64/:66` — all exist and match. Cross-fixture precedent claims verified: r10
`sources.json#/2` = `registrar-copy`, `timeline.json#/2` = `registry-entry`,
`relations.json#/1` = `records_departure`; `corpus/fixtures/README.md:209-210` carries
"does **not** assert a different destination or settle whether Sella's report is true";
`2026-10-12-lore-decision-table.md:112` carries "an authored second perspective, not
external corroboration or canon resolution" and "The checker does not parse the excerpt
or certify that source text entails the JSON." Its receipts block matches this seat's
re-run (Check 4), and its tool-revision history is accurate: at 20:31 local the freeze
tool read r97-closure bytes (`b06275f3…`/`27273be2…`, measured by this seat at 23:30Z),
and S1's revisions `03d04365…`/`c435239d…` landed at 20:32:51 local — this seat
re-measured exactly those values afterwards.

## Anti-overclaim sweep (the seat's core)

Method: the diff-derived new-line set across every round-98 changed path (r95 map line;
r95/r96 addenda; `dependency_freeze.py`; `dependency-freeze-contract.json`; all 6
changed/rewritten r98 fixture files; the r98 scope note), then vocabulary scan
(`finding|verdict|resolution|resolv|canon|rights|permission|identity|official|
adjudicat|authoritativ|authentic|guilt|fault|breach|winner|settle|determin|declar|
binding|judgment|instituti|certif`) plus a manual read of every hit and every new line.

**Result: zero overclaims.** Every flagged occurrence is one of:

- an explicit negation — `fictional-excerpts.md:61` "I assert no finding.", `:62` "I
  reach no verdict and reconcile nothing.", `:64` "It is an institutional filing only: it
  asserts no finding and no resolution, reaches no verdict, and reconciles nothing";
  `sources.json#/6` "It asserts no finding, no verdict, no reconciliation, and no
  resolution; it is not evidence of a breach, a continuing duty, a winner between the
  accounts, or an external historical fact";
- an attribution — `entities.json#/5/claims/0` "The filing note names Maren, the clerk
  of the Chalk Stair registry, as the officer who filed both pending accounts.";
- disclaimer boilerplate inherited or restated — "not … a verdict on source
  authenticity, truth, rights, permission, or canon".

Axis spot-checks: **canon** — no canon claim; `README.md:19` "supplies no in-world
witness, cultural authority, or fictional canon". **rights** — `README.md:19` "Rights
and AI-training permission remain unassessed; neither is granted or inferred here";
`inspiration-note.md` inherited byte-identical (rights/AI-training sections unchanged);
scope note line 72 "Rights and AI-training permission remain unassessed here."
**identity** — `README.md:15` "`first_appearance: clerk-filing-note` identifies the
source that first presents the clerk Maren as a named entity in this JSON bible; it
asserts no office beyond the filing, no finding, and no other record."; scope note:37
"the note's own attributed self-description … not independent identity proof."

### Official-ruling reading — construction attempt (required by the seat brief)

Attempt R: read the tick-14 registry filing as an official institutional ruling — e.g.
"the Chalk Stair registry ruled/recorded the matter OPEN as an official status
determination", or "issued a no-finding determination".

Every variant of R is blocked by explicit counter-text present in the delivered bytes:

1. `fictional-excerpts.md:61` "I assert no finding."
2. `fictional-excerpts.md:62` "I reach no verdict and reconcile nothing."
3. `fictional-excerpts.md:64` "It is an institutional filing only …"
4. `sources.json#/6` reliability note: "no finding, no verdict, no reconciliation, and
   no resolution"; the OPEN record itself is attributed ("the clerk **reports** …
   recording the matter OPEN") and bounded as "not evidence of … an external historical
   fact".
5. `README.md:11` "The filing does not overturn, confirm, adjudicate, or reconcile the
   accounts"; "not evidence of … an adjudication".
6. `README.md:15` "no office beyond the filing, no finding, and no other record."
7. `claim-excerpt-map.md:62` (J18 bounded reading) "it assigns no authority beyond the
   filing itself."
8. `claim-excerpt-map.md:66` (J20 bounded reading) "It asserts no finding, no verdict,
   no reconciliation, and no resolution".
9. Scope note:34 "it is not proof that the accounts were in fact filed as world fact,
   not independent corroboration, and not an adjudication."

**Verdict: the official-ruling reading is NOT constructible** — each variant requires
ignoring at least one explicit counter-text, and the institutional act is bounded to a
first-person filing ("institutional filing only", "no authority beyond the filing
itself", "not an adjudication"). This matches the r97 anti-overclaim standard (no
constructible resolution/blame reading).

### Soft spots recorded (not findings)

1. **Act-framing in the event description.** `timeline.json#/6` says "the clerk filed
   both pending accounts and recorded the matter OPEN", whereas r95/r97 event
   descriptions use report-framing ("Aru reports waiting/receiving …"). The attribution
   chain is intact in three other places (reliability note "the clerk reports filing";
   map J20 "The event records one institutional filing"; README:11 "it records only
   that the clerk filed …"; scope note:34 "not proof that the accounts were in fact
   filed as world fact"), so this is not an overclaim — flagged for wording discipline
   on the next beat.
2. **"officer" wording** in the entity claim ("as the officer who filed both pending
   accounts") is bounded by README:15 "asserts no office beyond the filing" and scope
   note:37.
3. **Round-declaration count.** The declaration says "byte copies of the other 7 files
   from 9a3d648"; the delivered 10-file set is 4 S3-extended + 4 byte-identical
   (`contradictions.json`, `inspiration-note.md`, `relations.json`,
   `source-excerpt.md`) + 2 placeholder-copied-then-rewritten by S4 (`README.md`,
   `claim-excerpt-map.md`). S3's report documents exactly this. Delivered bytes are a
   10-file preserving copy matching r97's file set; the "7" is a declaration
   imprecision with no delivered-byte impact.
4. **Placeholder-poll hazard (r98 class).** Between S3's copy and S4's rewrites the r98
   README/map existed with r97 bytes; an existence-only poll is satisfied by the
   placeholder (my first poll did, at try 4). Content-marker polling and byte comparison
   are required. Recorded for the next round's poll protocol.

## Poll outcome (final)

All S3–S5 artifacts and all three producer reports landed within the poll window: the
content-aware poll printed `ALL-PRESENT at try 14 23:33:38` local (started 23:29:12; the
40-try ceiling was never reached). Reports present: `S3-fixture-author.md` (20:31),
`S4-fixture-docs.md` (20:32), `S5-knowledge-notes.md` (20:34). No ABSENT item, no
stall-escape needed, and no plan was verified. The verified-revision snapshot was
re-checked after the last report landed (23:34:10Z): all hashes unchanged from the table
at the top of this report. S4's and S5's report bottom lines agree with this seat's
independent measurements (S4: 20 rows, 17 inherited identical, README 6/1/7, 7 sources,
20 obligations; S5: r98 receipts 20/20 / 22/22 / 20 mapped, CLEAN, exit 0). The only
poll hazard observed was the placeholder class recorded above.

## Limits of this verification

- This seat verified anti-overclaim and inheritance on the delivered bytes; it did not
  re-verify C1 behavior (S1's exit-2/migration semantics) or C2 chain semantics, which
  belong to the C1/C2 seats. The delivered S1 diff was swept for prose overclaims: the
  contract `precedence` text is a disclaimer-bearing description ("no chronology truth,
  entailment, source, rights, or canon judgment") and the docstring's claims match the
  visible code changes (case tuple `self_test_mismatch`, `MIGRATED …` branch, child-env
  guard). Chain state observed read-only: six pins incl. r97 and r98; r97 freeze PASS
  `3c922d20…`, r98 freeze PASS `59a0f4fa…` (both equal their contract pins).
- S2 `corpus/tools/README.md` was not present in the tree at snapshot time
  (`git status` clean for that path); its prose was therefore not swept.
- No network was used; no commits; no corpus writes.

## Bottom line

**PASS** — the anti-overclaim sweep found zero overclaims across all round-98 delivered
bytes, and the official-ruling reading is not constructible (nine explicit counter-texts
named above); the relation row is byte-identical (`c279254b…`), inherited rows are
parsed-equal, map rows J01–J17 are identical modulo namespace with J18–J20 correctly
anchored and spanned, r98 receipts read CLEAN + 20/20 facts / 2/2 editorial / 22/22 rows
/ 18/18 distinct anchors / 20 mapped obligations (all exit 0), census is 171→172 with
exactly one added dir, the r95 repair is a single prose line with data rows and receipts
unchanged and the r95 pin still PASS (`d541ae64…`), and every hash/receipt claim in the
S5 addenda and the r98 scope note was independently re-derived and matched. Recorded,
not findings: the tick-14 act-framing soft spot, the round declaration's "7 files" count
vs the delivered 4 byte-identical + 2 placeholder-rewritten files, and the r98
placeholder-poll hazard.
