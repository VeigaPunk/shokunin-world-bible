# JCOV2 — coverage judge #2 (locator + index + support rule)

Tree judged: `2ea9ef13a928475b13fd578740ea521bed4bd649` (delivered, tree clean; `git status --porcelain` empty).
Baseline for deltas: `dfd1fbc3711f2b28597d74444819aca91fe6bc31` (extracted read-only to `/tmp/jcov2/baseline` via `git archive`).
Machine record: `followup/JCOV2-support.json`.

## Work performed

- Confirmed the delivered tree and the round's change set, then enumerated every passage-level locator in both clusters (`corpus/fixtures/r87-myth-cluster`, `corpus/fixtures/r88-m3-maya-cluster`) and resolved each one mechanically as an exact fixed string against its delivered excerpt file, with line numbers.
- Re-ran the same locator and support-rule checks against a `/tmp` extraction of baseline `dfd1fbc` so every before/after number below is a measured pair, not an inference.
- Ran the D1 support rule (`corpus/knowledge/r88-sourced-inspiration-decision-table.md`, row "An in-world claim is attributed to a delivered excerpt") over every source-attributed in-world JSON fact in both clusters: entity claims, `first_appearance` pointers, relation edges, and timeline events, per the R1B scope note at the head of that table.
- Resolved every id and file reference in both clusters' prose against the on-disk records.
- Probed the r88 "occupied-slot near-miss" claim with a disposable control in `/tmp/jcov2/ctrl-doublebook` (same actor, same tick, different place) to prove the checker's slot semantics actually distinguish the two cases.
- Verified both external passage locators (r87 ETCSL `lines 122–163`, r88 Spence printed p. 209) against the cited pages by `curl`, to judge whether the locator assertions are accurate rather than merely well-formed.
- All scratch work in `/tmp`; the only repo writes are this report and `followup/JCOV2-support.json`. No commit, no push, no tracked-file write.

## Before → after measurements

### Checker exit status (both clusters)

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster; echo "exit=$?"
python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster; echo "exit=$?"
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

### (a) Passage-level locator resolution

r87 clause map — 8 clauses, each checked as an exact substring of `lowwater-hymn-excerpt.md`:

```text
r87 clauses extracted: 8
  OK  line=3 :: At low water
  OK  line=3 :: the shell ring
  OK  line=3 :: beside the bowl
  OK  line=3 :: at the Mother-Tide Gate
  OK  line=4 :: The bowl keeps no name
  OK  line=4 :: no voice owns the tide
  OK  line=5 :: pass the reed-bell hand to hand
  OK  line=5 :: let the water return it
r87 clause_matches=8/8; gate_named=True
```

Baseline, same command against `/tmp/jcov2/baseline`: `r87 clauses extracted: 7`, `r87 clause_matches=7/7`, `gate_named=False`.

r88 clause map — 2 rows; each row's cited clause checked against `source-excerpt.md` and each row's fictional element against `fictional-excerpts.md`:

```text
r88 map rows: 2
  cited FAIL src-line=None :: He called out ‘Earth,’
  elem  OK  fic-line=6 :: We leave its name unowned in the rain.
  cited OK  src-line=5 :: and the solid land appeared.
  elem  OK  fic-line=5 :: The chalk stair stays a crossing, never a map.
r88 cited_clause_matches=1/2; fictional_element_matches=2/2
```

Cause, measured directly: `corpus/fixtures/r88-m3-maya-cluster/source-excerpt.md:5` delivers `He called out “Earth,” and the solid land appeared.` — double curly quotes. The map row (`symbolism-clause-map.md:7`) writes `“He called out ‘Earth,’”` with single curly quotes. The cluster did not exist at baseline, so this is a defect inside a new artifact, not a regression of an existing one.

r88 register locator "`paired-clock`, folio 3, lines 1–2" (`fictional-excerpts.md:4`) resolves to exactly two delivered lines:

```text
r88 paired-clock folio-3 lines-1-2 delivered lines=2 :: ['> Tick 9: Aru carried the north lantern at Quiet Rise.', '> Tick 9: Evin held the south bell at Salt Court.']
```

Both maps name their source file and both READMEs' file references resolve:

```text
r87 map names source file: True
r88 map names source file: True
```

External locators (not delivered text; judged by fetch):

```sh
curl -sL -o /tmp/jcov2/etcsl.html "https://etcsl.orinst.ox.ac.uk/section1/tr141.htm"   # 34853 bytes
curl -sL -o /tmp/jcov2/gutenberg.html "https://www.gutenberg.org/files/53080/53080-h/53080-h.htm"  # 1035633 bytes
```

- ETCSL `lines 122–163`: the page's line 122 reads `the seven gates of the underworld be bolted`, and its line 163 ends `When she entered the seventh gate, the pala dress, the garment of ladyship, was removed from her body.` The r87 note's characterization ("entry through seven gates and the removal of items of dress and regalia") is accurate.
- Spence printed p. 209: the linked text carries the page marker as `<span class="pagenum">[<a id="pb209" href="#pb209" name="pb209">209</a>]</span>`, and the delivered excerpt's first sentence (`The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event.`) begins immediately after it. The source uses `&ldquo;Earth,&rdquo;` — matching the delivered excerpt's double quotes, and confirming the map's single-quote rendering is a deviation from both. The excerpt's `[…]` elides a real intervening span (`We are told that the god Hurakan, the mighty wind, … passed over the universe, still wrapped in gloom.`); the elision is legitimate. Caveat: the literal string `[209]` does not occur in the raw HTML (it is split across markup) — it is the rendered form, which is what `source-excerpt.md` claims.

### (b) Clause→element index id targets

Every id and file reference in both clusters resolves; no dangling target:

```text
=== r87-myth-cluster ===
  file-ref README.md: contradictions.json/entities.json/inspiration-note.md/lowwater-hymn-excerpt.md/relations.json/sources.json/symbolism-clause-map.md -> OK
  id-ref   lowwater-hymn-excerpt.md: lowwater-hymn -> OK (sources)
  id-ref   symbolism-clause-map.md: lowwater-hymn -> OK (sources)
  file-ref symbolism-clause-map.md: lowwater-hymn-excerpt.md -> OK
=== r88-m3-maya-cluster ===
  file-ref README.md: fictional-excerpts.md/inspiration-note.md/source-excerpt.md/symbolism-clause-map.md -> OK
  id-ref   fictional-excerpts.md: paired-clock -> OK (sources)
  id-ref   fictional-excerpts.md: veil-verse -> OK (sources)
  file-ref inspiration-note.md: source-excerpt.md -> OK
  file-ref symbolism-clause-map.md: source-excerpt.md -> OK
  id-ref   symbolism-clause-map.md: veil-verse -> OK (sources)
```

Both indexes are phrase-level (the "element" column names authored verse lines, not record ids), so there is no id target to dangle; every phrase target resolves in a delivered excerpt line (r87 8/8, r88 2/2).

### (c) D1 support rule over every source-attributed in-world JSON fact

Same command shape in both clusters and in the baseline archive; verdicts are fixed-string, line-numbered anchor searches against the delivered excerpt for that source.

```text
SUMMARY r87-myth-cluster: facts=22 OK=8 not-OK=14
SUMMARY r88-m3-maya-cluster: facts=10 OK=10 not-OK=0
```

Baseline, same command: `SUMMARY r87-myth-cluster: facts=22 OK=7 not-OK=15`. (`r88-m3-maya-cluster` raises `FileNotFoundError` at baseline — the cluster is new.)

r88 detail (all six claim-bearing facts, plus the four `first_appearance` pointers):

```text
[entity.claim] aru[0] src=paired-clock
    anchors: Aru->fictional-excerpts.md:10; Quiet Rise->fictional-excerpts.md:10
    VERDICT: OK
[entity.claim] evin[0] src=paired-clock  -> Evin->:11; Salt Court->:11  VERDICT: OK
[entity.claim] quiet-rise[0] src=paired-clock -> Quiet Rise->:10; Aru->:10  VERDICT: OK
[entity.claim] salt-court[0] src=paired-clock -> Salt Court->:11; Evin->:11  VERDICT: OK
[timeline] aru-ninth-bell  -> Aru->:10; Quiet Rise->:10  VERDICT: OK
[timeline] evin-ninth-bell -> Evin->:11; Salt Court->:11  VERDICT: OK
relations: none declared (relations.json = [])
first_appearance pointers: aru/evin/quiet-rise/salt-court -> paired-clock :: OK source record exists
```

r87 detail — the single supported claim-bearing fact and the 14 unsupported ones:

```text
[entity.claim] mother-tide-gate[0] src=lowwater-hymn
    anchors: Mother-Tide Gate->lowwater-hymn-excerpt.md:3
    VERDICT: OK
```

Unsupported (all four sources below have no delivered prose file in the cluster — the cluster ships only `lowwater-hymn-excerpt.md`):

| locator | kind | source_id |
|---|---|---|
| `hara.claims[0]` | entity.claim | gate-witness |
| `sen.claims[0]` | entity.claim | dune-register |
| `ash-dune-sanctuary.claims[0]` | entity.claim | dune-register |
| `shellweavers.claims[0]` | entity.claim | shell-charter |
| `reedwardens.claims[0]` | entity.claim | shell-charter |
| `reed-bell.claims[0]` | entity.claim | tide-bell-tally |
| `relations[0]` `relations[1]` `relations[2]` | relation | shell-charter |
| `relations[3]` | relation | dune-register |
| `timeline[first-lowwater-signal]` | timeline | gate-witness |
| `timeline[bell-tally-return]` | timeline | tide-bell-tally |
| `timeline[moon-basin-vow-gate-account]` | timeline | gate-witness |
| `timeline[moon-basin-vow-dune-account]` | timeline | dune-register |

The seven r87 `first_appearance` pointers all resolve to existing `sources.json` records, but four of the five pointed-to sources (`shell-charter`, `gate-witness`, `dune-register`, `tide-bell-tally`) deliver no prose — pointer resolution is not prose support.

### (d) OBS-1 repair

- Gate named in the delivered excerpt: `lowwater-hymn-excerpt.md:3` now reads `At low water we set the shell ring beside the bowl at the Mother-Tide Gate.` (baseline line 3 had no Gate phrase; `gate_named=False`).
- Clause matches: 8/8 (baseline 7/7 with the Gate clause absent).
- Cluster exits 0: `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0.
- Corroborating diff, `git diff --name-status dfd1fbc..2ea9ef1 -- corpus/fixtures/r87-myth-cluster`: exactly three files modified — `entities.json` (the Gate claim's statement reworded to what the verse actually says), `lowwater-hymn-excerpt.md` (Gate phrase added), `symbolism-clause-map.md` (Gate clause row added; "beside the bowl" limit clarified). This is the M4 excerpt variant, not the metadata-only repoint variant.

### Slot semantics (r88 near-miss claim)

```text
r88 tick values: [9, 9]
r88 distinct (entity,tick) slots: {'aru@t9': ['quiet-rise'], 'evin@t9': ['salt-court']}
collision_slots= []
```

Control (`/tmp/jcov2/ctrl-doublebook`, event 1 reassigned to actor `aru`, place `salt-court`, tick 9):

```text
VIOLATION: timeline[1]: double-booked 'aru' at tick 9 in timeline[0] ('quiet-rise') and 'salt-court'
1 violation(s); no canon changed
```

The README's "occupied-slot near-miss, not a double-booking" is mechanically correct: the checker keys slots on `(entity_id, tick)` (`check_bible.py:354`), so two different actors at one tick are not a collision, while the same actor twice at one tick with different places is.

## Findings & named debt

1. **Verdict recommendation — coverage axis (C2): improved.** Both clusters exit 0; the r88 cluster is entirely new and its ten in-world JSON facts are all supported (10/10) with every locator and id reference resolving; the r87 cluster's OBS-1 attribution moved from unsupported to supported (22 facts: OK 7 → 8; clause map 7/7 → 8/8 with the Gate now named). Nothing measured got worse relative to baseline. The one new-artifact defect below is a repair item inside the new cluster, not a regression.
2. **Named defect (repair item, one character class) — r88 cited-clause locator does not resolve exactly.** `symbolism-clause-map.md:7` cites `“He called out ‘Earth,’”`; the delivered `source-excerpt.md:5` and the external source both use double quotes. The map's own closing sentence claims it "indexes the two exact clauses in the delivered excerpt," which is falsified for that row. Cited-clause locators are therefore 1/2, not 2/2. Fix: change the row's inner quotes to `“Earth,”`.
3. **Named debt — r87 carries 14 unsupported source-attributed in-world JSON facts.** Under the D1 rule as scoped by the R1B note at the head of the delivered table ("EVERY source-attributed in-world JSON fact"), the r87 cluster's 6 entity claims, 4 relation edges, and 4 timeline events citing `gate-witness`, `dune-register`, `shell-charter`, and `tide-bell-tally` have no delivered prose to check against. This is pre-existing (baseline 15 unsupported) and improved by one; it is an evidence gap, not a checker violation and not a claim that the facts are false. The table's OBS-1 row registers the r87 OBS-1 instance but does not register this wider r87 metadata-only set.
4. **Named debt — external-only locators are unmarked.** `grep -rn "external-only\|unverified\|not delivered"` over both clusters' `*.md` returns no matches, while the delivered table requires an external-only passage to be marked `external-only / unverified`. Both external locators are nonetheless *accurate* (verified by fetch, above): r87's ETCSL `lines 122–163` and r88's Spence printed p. 209. The r87 note predates the rule; the r88 note delivers its passage text so only its page-marker sentence is external.
5. **Observation — the r88 cluster's C2 content claims check out.** "Distinct actors and distinct places" at tick 9 is true; the register locator resolves to exactly two lines; the verse's two element phrases resolve to `fictional-excerpts.md:5–6`; the symbolism map explicitly frames its readings as editorial and non-creation.
6. **Scope note for the record.** This seat judged only the delivered tree's locators, index targets, support-rule verdicts, and OBS-1 repair. It did not judge C1 calibration behaviour, the census deltas, or C3's table/ledger content beyond confirming that `reference-ledger.md` holds 4 data rows × 4 columns with exactly one ETCSL row, and that `r88-sourced-inspiration-decision-table.md` holds 7 data rows × 6 columns with the R1B scope note and the `grep -nF` support-rule example present.

## Handoff

- `followup/JCOV2.md` — this report; `followup/JCOV2-support.json` — machine record with per-fact verdicts, anchor→line hits, locator rows, and the two external fetch results.
- For the L1 integration step: (i) fix the single-quote rendering at `corpus/fixtures/r88-m3-maya-cluster/symbolism-clause-map.md:7` (or drop the word "exact" from that map's closing sentence), then re-run the cited-clause check to reach 2/2; (ii) decide whether the r87 metadata-only set (14 facts) and the unmarked external-only locators are registered as round debt or repaired by delivering `gate-witness`/`dune-register`/`shell-charter`/`tide-bell-tally` prose excerpts.
- Recommended axis verdict: **improved** for coverage, conditional on item (i) being treated as a named defect rather than silently carried.
- No commit or push was made; no tracked file other than the two deliverables above was written.
