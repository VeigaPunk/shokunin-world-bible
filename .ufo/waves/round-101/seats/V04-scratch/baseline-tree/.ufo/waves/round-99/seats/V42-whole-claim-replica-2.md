# V42 — whole-claim-replica-2: constructibility of a ruling/resolution reading (round 99)

Seat: **V42 whole-claim-replica-2** (verifier). Second independent whole-claim replica, with one explicit obligation — **attempt to construct a ruling/resolution reading over the delivered bytes and report its constructibility**. Baseline: r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). Declaration: `LOG.md` Round 99 (standing; the blocked-dispatch entry is zero increment). All commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report and `.ufo/waves/round-99/seats/V42-scratch/` only. No corpus file was modified.

## 0. Poll-wait

Cadence 20 s, 40 tries, then a post-exhaustion presence check. Content-gated: the r99 directory first appeared as an r98 byte-copy (README `32efc78f…`, map `c1099d0e…`); those were not verified as the claim. S3's lapse bytes landed at 22:01:13; S4's map `d2fe20e5…` at 22:02:39 and README `b9320941…` at 22:03. Those fixture hashes were unchanged through the final receipt at 22:58.

| Time (-03:00) | Observation |
|---|---|
| 22:01:15 try 1 | fixture dir present; README/map still r98 hashes; knowledge absent; no S reports |
| 22:01:40 | `S3-fixture-author.md` present |
| 22:02:59 | README and map carry the lapse bound (not the r98 placeholder) |
| 22:03:54 | `S4-fixture-docs.md` present |
| 22:07:33–22:31 | freeze tool and contract stable at full-file pins (schema 2, 10 files, self-test expected 18); knowledge still absent |
| 22:48:57 | `S1-full-file-pins.md` present |
| 22:53:06 try 40 | `POLL_EXHAUSTED`. Reports: S1, S3, S4. No S2 report, no S5 report, no knowledge files |
| 22:55–22:57 | post-exhaustion: `SKILL.md` and `corpus/tools/README.md` had been edited (S2 docs, no S2 report). Freeze tool hash moved to `fb9bb9ff…`; chain and self-test re-run on that hash |
| 22:57:50 | `corpus/knowledge/r99-gate-blind-spot-table.md` and `r99-lapse-scope-note.md` present. S5 report still absent at 23:04 |

Stall-escape, not fatal: try 40 closed before S2's docs and S5's notes. Those bytes were read after they existed. No plan was verified. S2 and S5 producer reports were still absent at 23:04:37.

## 1. Revision identity (final fixture hashes, stable 22:03–22:58)

```
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  entities.json
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15  sources.json
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  timeline.json
```

README and map match S4's reported hashes. Tool at the re-run: `dependency_freeze.py` `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`; contract `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`. Knowledge: table `4670c0b7…` (20526 bytes), lapse note `96de708f…` (14990 bytes), both mtime 22:57:50.

## 2. Gate receipts on the delivered fixture

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT:0

$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
EXIT:0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
EXIT:0
```

`support_check` was re-run at 22:58 on the same fixture hashes. J01–J20 also PASS (anchors at lines 12/13/17/18/19/20/26/37/48/59/60).

## 3. Inheritance and census (own measurement vs `git show 4265df5`)

```
BYTE-IDENTICAL to r98: contradictions.json entities.json inspiration-note.md relations.json source-excerpt.md
sources.json prefix equal True; added ['clerk-lapse-note']          7 → 8
timeline.json prefix equal True; added ['clerk-lapse-recorded']     7 → 8
entities equal True n=6; relations equal True n=1; contradictions []
fictional-excerpts.md: r98 bytes are a byte prefix (4187 → 5114; append starts '## Round 99 lapse note')
map: r98 J-rows 20, r99 J-rows 21, new ['J21'], changed inherited modulo namespace swap r99-window-lapse→r98-clerk-filing: 0
census: baseline git ls-tree -d 4265df5 corpus/fixtures/ = 172; working dirs = 173; added ['r99-window-lapse']
```

Declared C2 component 1 shape replicates: 6/1/8, sources 8, 21 obligations (20 inherited + J21 `timeline.json#/7`), CLEAN, census 173. No new entity, claim, or relation. Actor remains `clerk-maren` (`kind: character`). No institution entity.

## 4. Core — constructibility of a ruling/resolution reading

Method: (a) token scan of all ten fixture files for the ruling/resolution class (`resolut*`, `reconcil*`, `blame`, `adjudicat*`, `ruling`/`ruled`, `verdict`, `finding`, `closed`/`closes`, `unfulfill*`, `lodged`, `breach`, `winner`, `window`); (b) hand reading of the appended section `fictional-excerpts.md:66-76` and of every surface that describes the lapse (`sources.json#/7`, `timeline.json#/7`, `README.md:9-15`, map J21 and line 69); (c) structural scan of the JSON; (d) scratch probes (§5); (e) comparison of the lapse's "original minute" presupposition against the minute text at `fictional-excerpts.md:17-20`.

The delivered note (lines 70-76):

```
> Tick 15: The crossing-window named in the original minute has closed.
> The agreement was unfulfilled.
> No claim was lodged.
> The matter stands as a historical open entry.
> I record no resolution, assign no blame, and reconcile nothing.
Scope: … It asserts no resolution, no blame, and no reconciliation, and it creates no new duty;
the crossing-scoped agreement above is unchanged, and the matter stays open.
```

The minute the note points at (`fictional-excerpts.md:17-20`, byte-prefix of r94) names no window and no close-term:

```
> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.
> After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.
> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
> Their tick-10 decision depends on both ninth-bell entries: …
```

`window` occurs in the r99 excerpt only in lines 70 and 76. It does not occur in the minute. `ninth-bell` is a label for the tick-9 entries, not a named close.

| # | Construction attempted | Evidence | Outcome |
|---|---|---|---|
| R1 | Window-closure applies a minute close-term and thereby resolves the agreement (expiration / default) | excerpt `:70`; README `:11` "the window closed per the original minute's terms"; map `:69` "closed per that minute's terms" | **Not constructible as a resolution.** The minute has no window and no close-term. "per the minute's terms" is not in the quoted note (lines 70-74). The same README/map sentences say nothing is resolved and it closes no one. There is no term to apply |
| R2 | "The agreement was unfulfilled" is a breach finding / a resolution that performance failed | excerpt `:71`; `timeline.json:84`; `sources.json:48` | Fails as a finding. It is a performance-status sentence and names no party, remedy, or winner. The reliability note says it "is not evidence of a breach finding". README `:11` says "no breach finding". Inherited Aru note `:29` already "assert[s] no other duty, no breach" |
| R3 | "No claim was lodged" is a procedural bar (claim-preclusion / negative ruling) | excerpt `:72` | Fails. It records that no claim was lodged. It does not bar later claims. `:73` and the scope sentence say the matter stays open. No petition or limitation is named. The six JSON claims are unchanged |
| R4 | "I record no resolution, assign no blame" is an implicit negative ruling (clean bill / finding of no fault) | excerpt `:74`; `sources.json:48` | Fails. The sentence asserts the absence of a resolution and of a blame assignment, not a finding that no one is at fault. It blocks a ruling in both directions |
| R5 | Blame Evin by combining inherited "Evin did not come" (`:27`) with "unfulfilled" | excerpt `:27` + `:71`; Evin's account `:37-40` | Fails. The lapse note names neither Aru nor Evin. Inherited notes assert no accusation and no winner. Map `:69` and README `:11`: "assigns blame to neither". `contradictions.json` is `[]` |
| R6 | "historical open entry" is an official status ruling that settles the matter as permanently open | excerpt `:73`; scope `:76` | Closest status-record reading. It names no order, discharge, or effect on the parties. It is the opposite of closure. Not a ruling on the merits |
| R7 | "window has closed" means the matter is closed, and "open entry" is only archival | excerpt `:70` vs `:73`; README `:11` "it closes no one" | The equation is contradicted by the same note. Window-close and matter-open are distinguished, not equated |
| R8 | The clerk's office adjudicates by recording the lapse | `entities.json#/5` `kind: character`; claim at `:69` is the filing, not the lapse; README `:15` "asserts no office beyond the filing" | Fails. No institution entity. "Salt Court" is a place. The registry is prose. The lapse adds no claim and no office |
| R9 | A hidden ruling actor, act, or effect in the JSON | 6 entities, 1 inherited relation, 8 events, `contradictions.json` `[]` | Fails. The added event is a record. `depends_on: ["clerk-filing-open"]` is an editorial edge, not a holding |
| R10 | The agreement itself is resolved / ended, even if the accounts are not | excerpt `:71` + `:70`; scope `:76` "the crossing-scoped agreement above is unchanged" | Fails. The agreement text is explicitly unchanged. "Unfulfilled" is not "terminated", "discharged", or "resolved". No new duty is created (`relations.json#/0` still `agreed_co_stewardship_for_this_crossing`) |

**Result.** On the delivered bytes **no ruling/resolution reading is constructible as an assertion**. The fixture asserts the declared lapse content — window-status, unfulfilled, no claim lodged, historical open entry — and negates resolution, blame, and reconciliation. The closest surviving constructions (R2/R6) are status records. The upgrade from status to ruling requires a party, a remedy, or a close of the matter, and every one of those is either absent or explicitly denied.

The class boundary is the same shape as the r98 filing review: positive institutional *status* (a window recorded closed; an agreement recorded unfulfilled; a matter recorded open) versus adjudicative *outcome* (finding, verdict, blame, reconciliation, winner). The timeline description (`timeline.json:84`) omits the denial sentence; even that JSON-only surface names no party and calls the matter a historical open entry.

## 5. Probes — the class is invisible to the three lexical gates

Scratch only, under `V42-scratch/`. Corpus not modified.

**Probe A — appended ruling event.** Added source `clerk-ruling-note` and tick-16 event `clerk-ruling-issued` ("issued an official ruling adopting Aru's account, assigning blame to Evin, and closing the matter"), depending on `clerk-lapse-recorded`.

```
$ python3 corpus/fixtures/check_bible.py …/V42-scratch/probe-a-ruling-row
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT 0
```

**Probe B — inverted the delivered denial into a ruling**, leaving the J21 anchor sentence intact. Excerpt line 74 became "I record the resolution, assign blame to Evin, and reconcile the accounts." The scope sentence and the `clerk-lapse-note` reliability note and the tick-15 description were rewritten to a ruling that closes the matter. Map untouched.

```
check_bible      CLEAN … 0 violations                         EXIT 0
support_check    SOURCE-SUPPORT 21/21 … RESULT PASS           EXIT 0
                 PASS J21 … 70:> Tick 15: The crossing-window named in the original minute has closed.
map_obligations  OBLIGATIONS raw=21 mapped=21 … RESULT PASS   EXIT 0
```

**Probe C — honesty, not the ruling class.** A second tick-15 event for `clerk-maren` at `salt-court` is caught as occupancy, not as a ruling:

```
VIOLATION: timeline[8]: double-booked 'clerk-maren' at tick 15 in timeline[7] ('chalk-stair') and 'salt-court'
EXIT 1
```

So the restraint is editorial. A clean `check_bible` / `support_check` / `map_obligations` run does not prove the absence of a ruling.

## 6. C1 cross-check (artifacts, re-run on `fb9bb9ff…` / contract `8c2561b0…`)

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
EXIT:0
```

Chain verify, each `RESULT PASS` exit 0: r88 `acf677a7…`, r94 `048b8ff3…`, r95 `97cffd7b…`, r96 `43911900…`, r97 `a28b9ea0…`, r98 `5ecf84e1…`. These match S1's reported digests. `r99-window-lapse` is `UNPINNED-FIXTURE` exit 2. S1's report and the lapse note both state that C1's chain is the existing six; the declaration's "6/6" does not require an r99 pin. Bound, not a contradiction: the new fixture's prose is not freeze-covered.

Scratch before/after, live fixtures untouched (`V42-scratch/before-mirror` holds `git show 4265df5` of the tool and contract). Removed the sentence `> I assert no finding.` from an r98 excerpt copy:

```
BEFORE (r98 tool): FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
                   DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
                   RESULT PASS                                          EXIT 0
AFTER  (delivered): FINDING DIGEST-MISMATCH: … changed: fictional-excerpts.md
                    (sha256 29e384bf… -> 7cc49d22…); pinned-file bytes changed outside the semantic inventory
                    RESULT ERROR                                         EXIT 2
```

One-byte append to each of the ten pinned files, each restored after, on a path-bound r98 mirror of the delivered tool: all ten exited 2 `DIGEST-MISMATCH` naming that file (`entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`).

S2's report was absent at 23:04. The docs were not: `SKILL.md:98-100` now says 18 cases, ten files, and "BR-01's prose half is now 'any prose edit is detectable', not 'dependency semantics provable'". `corpus/tools/README.md:296-310` and `:344` supersede the five-table / 17-case sentences and state the same bound. That matches the measured behavior. It does not make the freeze a semantic proof, which probe B already shows.

## 7. C2 component 2 — read after it landed; not every row re-replayed

Both knowledge files exist (22:57:50). S5's producer report did not. The lapse note (`r99-lapse-scope-note.md`) states the same class boundary this seat measured: denials are negations, not positive assertions; window-closed is not matter-closed; the r94 minute "does not say the window has closed" and must not be read as containing the lapse (`:36`, `:47`). That agrees with §4. It does not replace this seat's reading.

The blind-spot table has rows 1, 1b, 2, 3, 4, 5, 6, 7, 8, 9. I did **not** re-run every quoted command. Independent receipts this seat does have: chain 6/6 and self-test 18/18 (§6); the prose-removal before/after (§6, row 6's class, on a different sentence than S5's J14 edit); probe B (ruling inversion stays green for all three lexical gates). Spot-replay of S5's existing row-1 twin, not a fresh mutant:

```
$ python3 corpus/fixtures/check_bible.py .ufo/waves/round-99/seats/S5-scratch/work/m1-empty-deps
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT 0
$ python3 corpus/tools/map_obligations.py .ufo/waves/round-99/seats/S5-scratch/work/m1-empty-deps
OBLIGATIONS raw=21 mapped=21
RESULT PASS
EXIT 0
```

That matches the table's row-1 lexical half. The freeze half of row 1 was not re-run here. Component 2 is present and consistent with the measurements this seat made; it is not independently replay-verified row by row by this seat.

## 8. Bounded observations

- **O1 — "named in the original minute" is a pointer, not a quoted close-term.** The minute (`fictional-excerpts.md:17-20`) contains neither `window` nor a close. README `:11` and map `:69` add "per the original minute's terms" / "per that minute's terms", which lines 70-74 do not say. That gloss does not construct R1: there is still no term, and the same paragraphs deny resolution. The lapse note discloses the same limit. Flag for anyone treating the README gloss as minute text.
- **O2 — scan-window false positives.** `README.md:9` "assign blame" / "verdict" sit under "does not … assign blame, or convert either account into a verdict". `README.md:11` "adjudication" sits under "is not evidence of … an adjudication". Map `:18` "resolved here as" is namespace resolution. `unresolved` contains the token `resolved`. `sources.json:36` "a winner" sits under "is not evidence of". No surface asserts a finding, verdict, blame assignment, or resolution.
- **O3 — r99 is unpinned.** `UNPINNED-FIXTURE` exit 2. Declared 6/6 holds. The lapse fixture's markdown is not edit-detected until someone pins it.
- **O4 — S2 and S5 reports absent at 23:04.** Docs and knowledge files were present. Do not treat the missing reports as missing bytes.

## 9. Limits

Same-lane replica on the delivered bytes: lexical scan, clause reading, scratch probes. Not source authentication, canon truth, rights, or an admission decision. Not a full replay of every blind-spot row. Producer reports for S1, S3, and S4 were read; S2 and S5 reports were not, because they were absent. No network.

**Bottom line: PASS — a ruling/resolution reading is not constructible as an assertion on the delivered r99 bytes: every resolution/blame/reconciliation/verdict token is negated or is a status record, the matter stays open, no party is blamed, and the minute names no close-term that a window-closure could apply; C2 component 1 replicates (6/1/8, 21 obligations, check_bible CLEAN, support_check 21/21, map raw=21 mapped=21, census 173); C1 artifacts replicate on `fb9bb9ff…` (chain 6/6, self-test 18/18, prose removal DIGEST-MISMATCH naming the file; the class is invisible to the three lexical gates); C2 component 2's files landed after poll exhaustion and were read, not row-replayed in full; S2 and S5 reports were still ABSENT at 23:04.**
