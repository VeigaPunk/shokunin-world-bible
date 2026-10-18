# V50 — crosscheck-depth (round 98)

Seat: V50 `verdict-crosscheck-depth`. Scope per seat spec: **independent depth verdict
derivation; compare V27**. This is my own derivation from delivered bytes and my own
commands, not a restatement of the producers' reports; the V27 comparison is in §4.

Lane repo: `/home/vgpnk/Projects/shokunin/lore-shokunin`; every command below ran from
that root with `python3`; every path I wrote is absolute under it (r94-F01 guard: the
only writes are this report and `.ufo/waves/round-98/seats/V50-scratch/`). Baseline
r97 closure `9a3d648`. No commits, no pushes, no network, no nested agents.

Scratch (mine): `V50-scratch/{poll.sh, baseline-hashes.txt, round-start-porcelain.txt,
pre-receipts.txt, depth-check.py, depth-check-run1.txt, depth-check-run2.txt,
r95-pre/ (fixture copy with map restored from 9a3d648), r95-datarows-pre.txt,
r95-datarows-post.txt, r95-pre-support.txt, r95-post-support.txt, r95-pre-mapobl.txt,
r95-post-mapobl.txt, r95-repair-receipts.txt, r98-hashes-run2.txt, r98-hashes-final.txt,
census.py}`.

## 1. Method and poll record

- Pre-registered checks before the fixture settled: baseline hashes of the r95 map and
  the ten r97 fixture files (captured 20:29:28, `baseline-hashes.txt`); tool hashes;
  a scratch pre-repair r95 copy built from `git show 9a3d648:…` (map `30281ff1…`) so the
  repair's receipt-neutrality could be measured against committed bytes regardless of
  when I first observed the tree. Honest timing note: S3's r95 repair (map
  `80440d61…`, mtime 20:28) beat my first working-tree hash capture by ~1 minute, so my
  "pre-repair" receipts come from the scratch copy, not from a pre-repair tree capture.
- Background poller `V50-scratch/poll.sh` launched 20:29:31 local (20 s cadence, 40
  tries), gated on: the six r98 fixture files, `corpus/knowledge/r98-clerk-scope-note.md`,
  producer reports `S1-…S5-*.md`, and `V27-*.md`. Observed landings (local): S3 seed
  copies 20:28:24; S3's four authored files 20:28:55; S4 map 20:30:21; S4 README
  20:30:41; S3 report ~20:31; S5 scope note ~20:32; S4 report ~20:33; S5 report
  ~20:33:51; S2 report ~20:34:5x; S1 report 20:35:31-20:35:33; V27 report 20:36:51+.
  At this report's first write (20:35) the S1 and V27 reports were still absent; §4 and
  the addendum record the final state.
- **Placeholder hazard (recorded, not a defect of the delivered revision).** The r98
  directory was seeded as a 10-file byte copy of r97; between 20:28:24 and S4's writes,
  `README.md` and `claim-excerpt-map.md` existed with r97 bytes. An existence-only poll
  is satisfied by that placeholder. My own depth checks were content-gated: the map
  checks ran only after `J20` was present (run1 ~20:30:4x), and the final revision was
  hash-pinned at 20:32:26 (`r98-hashes-run2.txt`) and re-checked unchanged at my final
  pass (`HASHES STABLE run2==final`). The fixture's last write is README 20:30:41.
- Final revision (10-file sha256, `r98-hashes-final.txt`): map `c1099d0e…`, README
  `32efc78f…`, entities `db2d8e5d…`, sources `32ee15b1…`, timeline `eb24e084…`,
  excerpts `29e384bf…`, contradictions `37517e5f…`, relations `c279254b…`,
  inspiration-note `58f5390e…`, source-excerpt `b5edc2fd…`.

## 2. Independent findings — C3 before→after

**F1 — preservation and extension of `r97-crossing-acknowledgment` (PASS).** My own
script `depth-check.py` (run2, exit 0; `FAILS: none`):

```
OK byte-identical contradictions.json | r97=37517e5f3dc66819 r98=37517e5f3dc66819
OK byte-identical inspiration-note.md | r97=58f5390e5928ebad r98=58f5390e5928ebad
OK byte-identical relations.json      | r97=c279254bc7de0636 r98=c279254bc7de0636
OK byte-identical source-excerpt.md   | r97=b5edc2fd3c2e3d4f r98=b5edc2fd3c2e3d4f
OK entities 5->6 | 5->6      OK relations 1 | 1      OK timeline 6->7 | 6->7
OK sources 6->7 | 6->7       OK contradictions [] | []
OK entities[:5] parsed-equal   OK sources[:6] parsed-equal   OK timeline[:6] parsed-equal
OK clerk-maren fields | {"id":"clerk-maren","kind":"character","name":"Maren",
   "first_appearance":"clerk-filing-note","claims":[{"statement":"The filing note names
   Maren, the clerk of the Chalk Stair registry, as the officer who filed both pending
   accounts.","source_id":"clerk-filing-note"}]}
OK clerk-filing-note id/title | Maren's Chalk Stair Registry Filing Note
OK clerk-filing-open fields | {"id":"clerk-filing-open","tick":14,"entity_id":"clerk-maren",
   "place_id":"chalk-stair","depends_on":["acknowledgment-aru-records"],
   "source_id":"clerk-filing-note", ...}
OK r97 excerpts is byte-prefix of r98 | r97=3410B r98=4187B delta=777B
OK obligation arithmetic == 20 | 6 fa + 6 claims + 1 rel + 7 ev = 20
```

New-source reliability note (verbatim, `sources.json#/6`): "Newly authored fictional
note; the clerk reports filing both pending accounts at the Chalk Stair registry and
recording the matter OPEN. It asserts no finding, no verdict, no reconciliation, and no
resolution; it is not evidence of a breach, a continuing duty, a winner between the
accounts, or an external historical fact."

Dependency chain (own parse): ticks `[9, 9, 10, 11, 12, 13, 14]` nondecreasing; all six
edges strictly earlier, including `clerk-filing-open -> acknowledgment-aru-records`
(exists=True, strictly-earlier=True).

**F2 — map completeness and inherited-row discipline (PASS).** My own column parse
(`depth-check.py`): r98 map `c1099d0e…` declares "20 JSON facts; 2 editorial rows; 22
total mapped rows; 18 distinct excerpt anchors"; row ids J01–J20 + S01/S02; **all 19
inherited rows (J01–J17, S01, S02) differ from the r97 rows in exactly the namespace
cell (`r97-crossing-acknowledgment:` → `r98-clerk-filing:`), 0 other diffs**; new rows
J18/J19/J20 exactly:

```
J18 entities.json#/5/first_appearance (clerk-maren) | span 60  | anchor `I am Maren, clerk of the Chalk Stair registry`
J19 entities.json#/5/claims/0                       | span 59-60 | anchor `I filed both pending accounts at the Chalk Stair registry.`
J20 timeline.json#/6                                | span 55-64 | anchor `Tick 14: I filed both pending accounts at the Chalk Stair registry.`
```

No row gone; obligation arithmetic 6+6+1+7 = 20 checks out independently.

**F3 — gates on the delivered revision (PASS; final tool revisions recorded).**

```
check_bible.py ff9fd2aa / support_check.py 55a5eb27 / map_obligations.py 86b52949 (contract 2142b991)
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations              exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS                                                             exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors);
MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS                                                             exit=0
```

**F4 — census and non-harm (PASS).** `git ls-tree -d --name-only 9a3d648:corpus/fixtures
| wc -l` = **171**; filesystem `ls -d corpus/fixtures/*/ | wc -l` = **172**. My own full
census (repo-relative `check_bible` over every fixture dir, `census.py`):
`{"fixture_dirs": 172, "clean_exit0": 38, "negative_exit1": 134, "violation_lines": 421,
"non_0_1_exits": []}` — r97 was 171/37/134/421/0, so exactly one clean increment, no
inherited tuple change. Non-harm (all vs `9a3d648`, `git diff --stat` empty): r97, r94,
r88-m3 fixtures; `check_bible.py`; `map_obligations.py` + its contract; `support_check.py`.

**F5 — repair half of C3 (PASS).** `git diff --numstat 9a3d648 --
corpus/fixtures/r95-crossing-aftermath/` → `1 1 claim-excerpt-map.md`, single hunk,
line 49; the changed sentence is exactly the declared carried-wording fix ("The new
relation encodes…" → "The relation encodes … not perpetual performance or alliance;
the new tick-11 aftermath event records one reported non-arrival on one occasion.").
All 17 data rows (J01–J15, S01–S02) byte-identical (`cmp` of extracted rows →
`DATAROWS-IDENTICAL 17 rows`). Receipts measured pre/post with my own scratch pre-copy
(map restored from `9a3d648`, `30281ff1…`) vs the delivered tree (`80440d61…`):

```
diff r95-pre-support.txt  r95-post-support.txt  → SUPPORT-RECEIPT-IDENTICAL
diff r95-pre-mapobl.txt   r95-post-mapobl.txt   → MAPOBL-RECEIPT-IDENTICAL
check_bible: CLEAN exit 0 both sides
(post values: support_check 15/15 … VALIDATED-ROWS 17/17 RESULT PASS; map_obligations raw=15 mapped=15 RESULT PASS)
```

**F6 — adversarial scope review, my own (PASS, bounded).** I attempted to construct
from the delivered bytes: (a) a finding/verdict — blocked by ":61 I assert no finding."
and ":62 I reach no verdict and reconcile nothing."; (b) a resolution — blocked by the
reliability note ("no … resolution") and ":64 asserts no finding and no resolution";
(c) a reconciliation/winner — blocked by ":62 reconcile nothing." and the note's
"no winner between the accounts"; (d) a duty/breach — blocked by the inherited
crossing-only relation and the retained "no obligation beyond this crossing" bounds;
(e) a contradiction — `contradictions.json` stays `[]` (byte-identical across
r95–r98) with the different-actor/different-place reasoning; (f) canon-truth/identity/
authority — blocked by the reliability note ("not evidence of … an external historical
fact"), the map's J18 bound ("it does not assert that no other record anywhere names a
clerk, and it assigns no authority beyond the filing itself"), and the README's rights
sentence. My own grep of every `finding|verdict|reconcil|resolut|winner|OPEN` occurrence
in the four new/edited files returns only negated or scoped clauses plus the record's
own `OPEN` status; the only non-negated `resolves` strings in the fixture are namespace/
provenance sentences (`claim-excerpt-map.md:18`, `source-excerpt.md:7`).

**F7 — mid-flight states observed and superseded (evidence, not defects).** (a) The
r98 dir was an r97 byte copy 20:28:24–20:30:21/20:30:41 (placeholder phase; S4's writes
replaced README/map); (b) while the map was still the r97 copy, `map_obligations`
reported `raw=20 mapped=17` with exactly the three expected `missing_obligation`
findings (`entities.json#/5/first_appearance`, `entities.json#/5/claims/0`,
`timeline.json#/6`) — i.e. the three new rows are load-bearing; S3's and V16's reports
record the same observation independently. Both states are recorded as mid-flight, not
as defects of the delivered revision.

## 3. My independent depth verdict

**DEPTH — IMPROVED (bounded).** On the delivered revision the crossing arc gains its
fourth beat: a named office-holder's institutional filing record that asserts no
finding. Before (r97): 5 entities / 1 relation / 6 events / 6 sources / 17 map
obligations; after (r98): 6/1/7, 7 sources, 20 map obligations (17 inherited rows
carried unchanged modulo the declared namespace re-qualification + J18 first_appearance
+ J19 claim + J20 event), tick-14 event dependency-linked to the tick-13
acknowledgment, `check_bible` CLEAN exit 0, `map_obligations raw=20 mapped=20` PASS
exit 0, `support_check` 20/20 + 2/2 + 22/22 PASS exit 0, census 171→172
(38/134/421/0, one clean increment), empty contradiction ledger, and the r95 repair
byte-minimal (one prose line) with byte-identical receipts. No harm observed in my
scope: r88/r94/r97 fixtures and the three depth tools byte-unchanged vs `9a3d648`.

Named bounds:

1. **Structural/lexical evidence + hand scope review only** — no testimony truth,
   canon, chronology, rights, or identity claim. `check_bible`/`support_check`/
   `map_obligations` receipts are preflight, not entailment or adjudication.
2. **"Institutional filing record asserting no finding" is an authored in-record
   class label** — no gate reads prose; the "fourth beat" framing is the record's own
   description (README `:1`, scope note §"The observation class").
3. **The filing is record-bounded** — "I filed both pending accounts…" is the note's
   own first-person wording; tick `14`, event ID `clerk-filing-open`, and the
   `depends_on` edge are editorial encodings (README `:13`; map `:54`); `OPEN` is the
   record's own status, not a world fact.
4. **Checker blind spots (carried, V16 P5/P8/P9)** — `check_bible` cannot see an
   emptied `depends_on`, a wrong-but-earlier edge, or a deleted terminal row; the
   tick-14→tick-13 edge is verified as bytes + prose + map row, not by a rule. (Note
   the new edge is nonetheless load-bearing for removal-type probes: with the
   acknowledgment event no longer terminal, deleting it now fails, V16 P4.)
5. **Preservation is four-level, not map-file byte equality** — byte (4 copies),
   parsed prefix (entities/sources/timeline), strict byte-prefix (excerpts, +777 B),
   column equality modulo namespace (19 inherited map rows).
6. **Declaration-vs-delivery wording note** — the declaration says "harbor clerk of the
   Chalk Stair registry"; the delivered JSON entity/claim says "clerk of the Chalk
   Stair registry" ("harbor clerk" appears in the excerpts scope line and README). The
   record itself bounds office claims ("asserts no office beyond the filing"); I record
   this as a wording variance, not a depth defect.
7. **Tool-revision flux** — depth receipts were produced at `check_bible.py`
   `ff9fd2aa…`, `support_check.py` `55a5eb27…`, `map_obligations.py` `86b52949…`
   (all byte-equal to `9a3d648`). S1's C1/C2 files moved during the round
   (`dependency_freeze.py` `39a57a98…` → `03d04365…`; contract `8b9b540e…` →
   `153ebc5b…`, six pins); my depth verdict does not depend on C1/C2 and I did not
   adjudicate them. (This bullet supersedes the mid-churn wording in the first version
   of this report, which recorded the pins as not yet landed — see addendum item 2.)
8. **Mid-flight placeholder hazard** (§F7, §1) — recorded for verifiers; all my
   receipts are on the content-gated, hash-pinned final revision.
9. **Scope-note revision** — `corpus/knowledge/r98-clerk-scope-note.md` moved
   `a73cd57b…` → `1162262c…` (72 lines, mtime 20:33:01) before my final read; the
   delivered revision carries the class definition and bounds I cite (grep: "fourth
   beat" at `:14`); no fixture byte is affected.

## 4. Crosscheck vs V27

Read `.ufo/waves/round-98/seats/V27-verdict-depth.md` (first visible to my poll at
20:36:51, final mtime 20:37:12; V27's scope: "read the C3 seats (S3, S4, S5), run 2 own
replays, issue exactly one DEPTH verdict"). V27's verdict: **DEPTH IMPROVED — bounded**,
bottom line PASS — identical in direction and substance to mine. Comparison of the
shared measurements:

| Check | V27 | V50 (me) | Agreement |
|---|---|---|---|
| before→after | 5/1/6/6 → 6/1/7/7; 17→20 obligations | same | yes |
| `check_bible` r98 | CLEAN exit 0 @`ff9fd2aa` | same | yes |
| `map_obligations` r98 | `raw=20 mapped=20` PASS @`86b52949` | same | yes |
| `support_check` r98 | 20/20; 2/2; 22/22; 18/18 distinct anchors PASS | same | yes |
| census | 172/38/134/421/0 (own script) | same (own script) | yes |
| inheritance | 4 byte copies; parsed prefix ×3; excerpts +777 B; map rows modulo namespace, 0 other diffs | same (19 inherited rows incl. S01/S02) | yes |
| r95 repair | 1 line (49c49); receipts identical pre/post | same (own scratch pre-copy; 3 receipts byte-identical) | yes |
| chain pins | r97 `3c922d20…`, r98 `59a0f4fa…` verify PASS | same (my 6/6 run: digests equal) | yes |
| class-text probes | reliability note + excerpt lines 59–62; corpus-wide closure-language scan finds only negative bounds | same substance (own negation-context grep) | yes |
| placeholder hazard | recorded | recorded | yes |

**No material divergence.** Two scope/timing differences, neither substantive:
(a) V27 additionally read the three C3 producer reports (S3/S4/S5) as its gate and
records S1's report as ABSENT at its final pass; S1's report was first visible to my
poll at 20:35:31 (final mtime 20:35:33) — after V27's 20:35:04 final receipt pass —
a timing artifact of the endgame class, not a disagreement; (b) V27's §6.3 notes the
contract hash churn (`c435239d…` → `153ebc5b…`) that I also observed mid-round. V27's
bounds (delivered revision, record-scoped class, structural/lexical checker bound,
C1/C2 out of scope, rights/canon unassessed) coincide with mine in substance; my
independent derivations reproduce every shared number, so the crosscheck is **AGREE**.

## 5. Bottom line

**PASS — independent depth verdict: improved (bounded); V27 crosscheck: AGREE, no
material divergence** — the delivered r98 fixture verifies as the crossing arc's fourth
beat (institutional filing asserting no finding) with 5/1/6→6/1/7, 6→7 sources, 17→20
map obligations (J18–J20 load-bearing), CLEAN/PASS receipts on the hash-pinned
revision, four-level preservation, empty contradiction ledger, byte-minimal
receipt-neutral r95 repair, census 171→172, and the named bounds in §3.

## Addendum (after first write) — V27 landed; final endgame state

1. **V27 crosscheck completed** — `.ufo/waves/round-98/seats/V27-verdict-depth.md`
   (first visible to my poll at 20:36:51, mtime 20:37:12) read in full; §4 above
   records the AGREE comparison. No material divergence in verdict, numbers, or
   bounds.
2. **Correction to §3 bound 7 (first-version wording).** The first version of this
   report said the r97/r98 pins were "not yet in the contract" at my final check. That
   was true of my first contract read (20:32:4x: four pins) but stale by my report's
   write time: S1's delivered contract `153ebc5b…` carries six pins, and my own runs
   verify the chain 6/6 clean — `python3 corpus/tools/dependency_freeze.py
   corpus/fixtures/{r88-m3-maya-cluster,r94-paired-crossing,r95-crossing-aftermath,
   r96-crossing-response,r97-crossing-acknowledgment,r98-clerk-filing}` all
   `RESULT PASS` exit 0, with r98 `DIGEST 59a0f4fa…` and r97 `DIGEST 3c922d20…`.
   The bullet in §3 is superseded by this note; the correction changes no depth
   measurement.
3. **Late producer reports** — S1 `S1-freeze-hygiene.md` (20:35:33, PASS), S2
   `S2-tools-docs.md`, S5 `S5-knowledge-notes.md` (PASS) all landed within my poll
   budget; none of them touches a depth receipt I took (the three depth tool revisions
   are unchanged throughout).
4. **Cross-lane hygiene observation (not mine)** — `/home/vgpnk/Projects/shokunin/
   baseline-analyze.txt` (105 B, mtime 20:30:10; parent worktree, outside any lane;
   content is captured `python3: can't open file '…/analyze.py'` stderr) exists in the
   parent tree — the r94-F01 stray-write class recurring. Found independently by V45
   (§7 of its report) and recorded by S1's report; I did not create it and did not
   remove it (not my ownership). All of my own writes resolved under the lane.
5. **Final state check** — the fixture's 10-file hash set is unchanged from 20:32:26
   to my final pass (`HASHES STABLE run2==final`); the last fixture write is README
   20:30:41; the three depth gates re-ran green at my final pass. No stray writes by
   this seat; this report and `V50-scratch/` are my only artifacts.
