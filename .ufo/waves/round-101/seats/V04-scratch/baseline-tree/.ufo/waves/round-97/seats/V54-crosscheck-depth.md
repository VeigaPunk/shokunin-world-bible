# V54 — crosscheck-depth (round 97)

Seat: V54 `verdict-crosscheck-depth`. Scope per seat spec: **independent depth verdict
derivation; compare V29**. This is my own derivation from delivered bytes and my own
commands, not a restatement of the producers' reports; the V29 comparison is in §6.

Lane repo: `/home/vgpnk/Projects/shokunin/lore-shokunin`; every command below ran from
that root with `python3`; every path I wrote is absolute under it (r94-F01 guard: the
only writes are this report and `.ufo/waves/round-97/seats/V54-scratch/`). Baseline
`f3e09f9` (HEAD `2393934`). No commits, no pushes, no network, no nested agents.

Scratch (mine): `V54-scratch/{poll.log, r96-pre-repair-digests.txt,
r96-baseline-support.txt, r96-baseline-mapobl.txt, v54-depth-check.py,
v54-map-check.py, depth-check-run1.txt, depth-check-run2.txt, map-check-run1.txt,
fixture-hashes-run2.txt, fixture-hashes-final.txt, baseline/ (git-archive copy of
corpus/ at f3e09f9)}`.

## 1. Method and poll record

- Pre-registered my independent checks before the artifacts landed: a fresh
  `git archive f3e09f9 corpus` baseline copy (pre-repair by construction) extracted at
  18:43 into scratch; the pre-repair working-tree digest set captured at **18:42:58**
  (`r96-pre-repair-digests.txt`, map `5093d72e…`); baseline receipts captured at
  18:44:01 with the then-frozen tools (`map_obligations.py` `2b0ba815…`,
  `support_check.py` `55a5eb27…`).
- Poll-wait protocol honoured: background poller 20 s cadence, artifacts + producer
  reports; two foreground top-ups. Observed landings (lane clock, -03:00): r96 map
  repair 18:43; r97 fixture dir 10 files 18:44:16–18:44:30 (map/README still r96 byte
  copies — R5 pending); R4 report ~18:50:28; R5 map `49d4834e…` / README `d9387b7d…`
  ~18:48:56–18:49:14; R6 note ~18:51; R5 report ~18:51; **R6 report 18:53:53**;
  **V29 report 18:54:23**. I never verified a plan and never fabricated a state: the
  pre-R5 state below is recorded as mid-flight, not as a defect.
- Final revision frozen at 18:55+ (`fixture-hashes-final.txt`); re-checked stable
  against my 18:51 run (`HASHES STABLE run2==final`).

## 2. Independent findings — C3 before→after

**F1 — preservation and extension of `r97-crossing-acknowledgment` (PASS).** My own
script `v54-depth-check.py` (run2, exit 0):

```
five copies byte-identical r96↔r97: entities.json 026af0bc / relations.json c279254b /
  contradictions.json 37517e5f / inspiration-note.md 58f5390e / source-excerpt.md b5edc2fd
timeline.json: len r96=5 len r97=6, first 5 parsed-equal: True
sources.json:  len r96=5 len r97=6, first 5 parsed-equal: True
fictional-excerpts.md: r96 is byte-prefix of r97: True   (appended section lines 44-53)
entities/relations/contradictions: r97 parsed-equal to r96 (5 / 1 / [])
```

New event (exact, parsed): `timeline.json#/5` = `acknowledgment-aru-records`, tick 13,
`entity_id aru`, `place_id chalk-stair`, `depends_on ["response-evin-salt-court"]`,
`source_id aru-acknowledgment-note`; new source `sources.json#/5` =
`aru-acknowledgment-note` (fictional first-person note, reliability note = "receipt
only … not evidence of a resolution, a reconciliation, an accusation, a winner
between the accounts, a continuing duty, or an external historical fact"). Note text
`fictional-excerpts.md:48-51`: "Tick 13: I received Evin's response at the Chalk
Stair. / I hold to my own account; both accounts stand unresolved. / I make no
accusation against Evin, and I select no winner between us. / I assert no
reconciliation, no new duty, and no obligation beyond this crossing."

**F2 — map completeness and inherited-row discipline (PASS).** My own column parse
(`v54-map-check.py`, exit 0): r97 map sha `49d4834e…`; declaration "17 JSON facts;
2 editorial rows; 19 total mapped rows; 15 distinct excerpt anchors"; row ids
J01–J17 + S01/S02; **J01–J16 differ from the r96 map rows in exactly 1 cell each —
the path-qualification namespace column (`r96-crossing-response:` →
`r97-crossing-acknowledgment:`)**; S01/S02 identical; new row J17 = `timeline.json#/5`
(`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) →
`aru-acknowledgment-note` / `r97-crossing-acknowledgment:aru-acknowledgment-note` /
`fictional-excerpts.md` / span `44-53` / `verbatim` / anchor "Tick 13: I received
Evin's response at the Chalk Stair." (line 48). No rows gone. Obligation arithmetic
checks out independently: 5 first_appearance + 5 claims + 1 relation + 6 events = 17.

**F3 — gates on the delivered revision (PASS; final tool revisions recorded).**

```
map_obligations.py 86b52949 / contract 2142b991 / support_check.py 55a5eb27 / check_bible.py ff9fd2aa
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS                                        exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment
RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; … MODES 19/19; VALIDATED-ROWS 19/19
RESULT PASS                                        exit=0
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
CLEAN: schema, citations, relations, timeline; 0 violations   exit=0
```

**F4 — census and non-harm (PASS).** `git ls-tree -d --name-only
f3e09f9:corpus/fixtures | wc -l` = **170**; filesystem now = **171**; fixture files
1010 → 1020 (the 10 new r97 files). `git diff --stat f3e09f9 --
corpus/fixtures/r94-paired-crossing corpus/fixtures/r95-crossing-aftermath` = empty;
`check_bible.py` and `support_check.py` byte-unchanged vs `f3e09f9` (ff9fd2aa /
55a5eb27); `git status` shows no stray corpus writes outside the declared set
(LOG.md, r96 map repair, C1/C2 tool files, new r97 fixture + R6 note).

**F5 — repair half of C3 (PASS).** `git diff f3e09f9 -- …/r96-crossing-response/`
touches only `claim-excerpt-map.md`, exactly 2 hunks: line 44 delimiter
`|---|---|---|---|---|---:|---|---|` → `|---|---|---|---|---:|---|---|` (8 → 7 cells,
matching its 7-cell header/data rows) and line 50 "The new relation encodes…" →
"The new tick-12 event encodes…". My parser confirms: post-repair cell counts header
7 / delimiter 7 / rows 7, and `grep -c "new relation"` = 0. **All 23 non-delimiter
pipe rows (3 headers + 16 J rows + 2 S rows + 2 excerpt-declaration rows) are
byte-identical baseline↔post-repair** (`identical row bytes (zip): 23/23`), i.e.
pointers, anchors, spans, and modes untouched. Receipts unchanged by the repair:
`support_check` and `map_obligations` stdout byte-identical between the f3e09f9
baseline copy and the repaired dir (`stdout-identical=True` both), and the frozen-tool
(`2b0ba815…`) outputs on the baseline copy are byte-identical to the final-tool
(`86b52949…`) outputs (diff empty ×2). r96 final receipts: `raw=16 mapped=16` PASS,
`16/16 … 18/18` PASS, CLEAN exit 0.

**F6 — J17 is load-bearing, not silently satisfied (evidence, not a defect).** At
18:44:36 the r97 map was still a byte copy of the r96 map (both `e851f068…`) and
`map_obligations` correctly reported `OBLIGATIONS raw=17 mapped=16` /
`FINDING missing_obligation: timeline.json#/5 has no map row` / `RESULT FAIL` exit 1.
After R5's map landed the same command is `raw=17 mapped=17 … RESULT PASS` exit 0.

**F7 — adversarial scope review, my own (PASS, bounded).** I attempted to construct
from the delivered bytes: (a) a resolution ("accounts reconciled") — blocked by
":49 both accounts stand unresolved" and ":51 I assert no reconciliation";
(b) an accusation/admission — blocked by ":50 I make no accusation against Evin" and
the absence of any betray/fault/blame/admission term; (c) a winner — blocked by
":50 I select no winner between us"; (d) corroboration of either account's truth —
blocked by the reliability note ("records receipt only … not evidence of a resolution
… or an external historical fact"); (e) a new duty/obligation — blocked by ":51 no
new duty, and no obligation beyond this crossing" plus the inherited crossing-only
relation; (f) a contradiction — `contradictions.json` stays `[]` (byte-identical
r95/r96/r97) and the record names different actors at different places. My own grep
of the 10 fixture files + R6 note found every accusation/winner/reconciliation/
resolution/duty occurrence inside a negating or scoping clause.

## 3. My independent depth verdict

**DEPTH — IMPROVED (bounded).** On the delivered revision the crossing arc gains its
third beat: a receipt-only acknowledgment by one named participant with the dispute
preserved unresolved. Before (r96): 5 entities / 1 relation / 5 events / 5 sources /
16 map obligations; after (r97): 5/1/6, 6 sources, 17 map obligations (16 inherited
rows carried unchanged modulo the declared namespace re-qualification + new tick-13
row J17), tick-13 dependency-linked to the tick-12 response, `check_bible` CLEAN,
`map_obligations raw=17 mapped=17` PASS, `support_check` 19/19 PASS, census 170→171,
zero inherited changes (byte-identical five copies; parsed-value prefix timeline/
sources; strict byte-prefix excerpts; column-level map inheritance), empty
contradiction ledger, and no new claims/entities/relations. No harm observed in my
scope: r94/r95 fixtures, `check_bible.py`, `support_check.py` byte-unchanged; the r96
repair is byte-minimal and receipt-neutral.

Named bounds: (1) structural/lexical evidence + hand scope review only — no testimony
truth, canon, chronology, rights, or identity claim; (2) the "acknowledgment-without-
reconciliation" label is an authored in-record status — the literal term occurs
nowhere in `corpus/` outside the r97 fixture and the R6 note (my grep: 0 matches),
and no gate reads prose; (3) "receipt-only" and "dispute preserved" are the record's
own assertions, bounded by the reliability note; the tick integer/event ID/
`depends_on` edge are editorial encodings; (4) `check_bible` cannot see an emptied
`depends_on`, a wrong-but-earlier edge, or a deleted terminal row (carried V20
blind spots) — the tick-13 edge is verified as bytes + map row + prose, not by a
rule; (5) inherited-unchanged is four-level (byte / parsed prefix / byte prefix /
column-modulo-namespace), not map-file byte equality; (6) tool-revision flux: my
depth receipts were produced at `map_obligations.py` `86b52949…` / contract
`2142b991…`, with the frozen `2b0ba815…` outputs identical on the r96 depth receipts;
(7) the C2 coupling "re-freeze r96 through the guarded `--freeze` path" is R3's
in-flight deliverable (at my final check `dependency_freeze.py`/contract were just
modified) — I did not verify C2 and my depth verdict does not depend on it; R4 notes
the r96 pin's `files` map lists only the five JSON tables, so the cosmetic repair
does not move the pinned digest; (8) `corpus/fixtures/README.md:1217` still states the
r96 census (170) while the tree has 171 — a closure-side bookkeeping/freshness item,
not a depth harm.

## 4. Crosscheck vs V29

Read `.ufo/waves/round-97/seats/V29-verdict-depth.md` (landed 18:54:23). V29's
verdict: **DEPTH — IMPROVED (bounded)**, bottom line PASS. Comparison of the
substance:

| Check | V29 | V54 (me) | Agreement |
|---|---|---|---|
| before→after | 5/1/5 → 5/1/6, 5→6 sources, 16→17 obligations | same | yes |
| `map_obligations` r97 | `raw=17 mapped=17` PASS exit 0 @86b52949 | same @86b52949 | yes |
| `support_check` r97 | 17/17, 19/19, PASS exit 0 | same | yes |
| `check_bible` r97 | CLEAN exit 0 | same | yes |
| census | 171 (170 at r96) | 171 (git baseline 170) | yes |
| inherited map rows | 18 compared, 0 differing modulo namespace re-qualification | J01–J16 differ only in the namespace cell; S01/S02 identical | yes (same finding, different reporting shape) |
| r96 repair | map `5093d72e…`→`e851f068…`, exactly 2 lines, receipts byte-identical | same, plus 23/23 non-delimiter rows byte-identical and frozen==current tool outputs | yes |
| pre-R5 mid-flight | `raw=17 mapped=16 … missing_obligation` FAIL (recorded as mid-flight) | same observation at 18:44:36 | yes |
| class label novelty | `grep -rni acknowledg` outside r97/R6 = 0 | independently re-ran: 0 matches | yes |
| tool byte-stability | check_bible/support_check unchanged vs f3e09f9 | re-ran: ff9fd2aa / 55a5eb27 = baseline | yes |
| README census staleness | flagged (bound 8) | independently confirmed at `README.md:1217` | yes |
| R6 report status | ABSENT at V29's final check | landed 18:53:53; I read it (PASS, artifact + receipts) | timing difference only; no substantive divergence |
| V14 status | PRELIMINARY PASS at V29's read | not re-adjudicated by me | no conflict |

**No material divergence.** V29's bounds and mine coincide in substance (structural
evidence only; authored class label; record-bounded receipt; assertion-level
unresolved status; checker blind spots; tool-revision flux; namespace-modulo map
inheritance). Two differences are scope/timing, not disagreement: (a) V29 recorded
R6's report as ABSENT while I could read it (landed before my final pass); (b) V29
additionally read and reconciled the other C3 seats (V13/V14/V19/V20/V50/V51/V52),
which my seat spec did not require — my independent derivations reproduce V29's
numbers on every shared receipt, so the crosscheck is **AGREE**.

## 5. Bottom line

**PASS — independent depth verdict: improved (bounded); V29 crosscheck: AGREE, no
material divergence** — the delivered r97 fixture verifies as the crossing arc's
third beat (receipt-only acknowledgment, dispute preserved unresolved) with
5/1/5→5/1/6, 5→6 sources, 16→17 map obligations (J17 load-bearing and verified),
CLEAN/PASS receipts on the delivered revision, four-level preservation, empty
contradiction ledger, byte-minimal receipt-neutral r96 repair, census 170→171, and
the named bounds in §3.
