# JCOV4 — Coverage judge #4 (fresh-eyes discipline audit)

Seat: JCOV4. Wave: round-87 follow-up (world-bible lane), fleet root `/home/vgpnk/Projects/shokunin`, repo `lore-shokunin/`.
Measured tree: HEAD `2b48ca7` (work-wave evidence commit), tree clean at start.
Mission: audit the prose files of `corpus/fixtures/r87-myth-cluster/` (README, inspiration-note.md,
lowwater-hymn-excerpt.md, symbolism-clause-map.md) against PROVINCE.md's refusal list, with fresh eyes —
i.e. **before** reading C7.md or M4.md — then compare verdicts and record agreements/disagreements.

## Refusal list under audit (PROVINCE.md:9, verbatim)

> Refuses: claiming canon without an in-world citation; silently resolving contradictions; real-world
> rights claims (art-east-asian-design); game mechanics verification (game-dev-2d).

Encoded for this audit as four axes:
- **R1** canon claim without an in-world citation
- **R2** silently resolving a contradiction
- **R3** real-world rights claim
- **R4** game-mechanics verification (game-dev-2d domain)

---

## Part A — fresh-eyes verdict (recorded BEFORE reading C7.md / M4.md)

Discipline receipt: Part A was written at **2026-10-17T01:40:48-03:00** (see the timestamped
`md5sum` block below), with C7.md and M4.md unopened in this session. File hashes of the audited tree:

```
1a27794c39a36dc95e7b0af2e2bbc712  corpus/fixtures/r87-myth-cluster/inspiration-note.md
25d93d743e4ed272adca23033b593498  corpus/fixtures/r87-myth-cluster/lowwater-hymn-excerpt.md
681e88784d2e219d304960c4bd451b71  corpus/fixtures/r87-myth-cluster/README.md
2b84d06aa296140eea2786566c41c547  corpus/fixtures/r87-myth-cluster/symbolism-clause-map.md
838ec2bb9f15ced62a490474348518b3  corpus/fixtures/r87-myth-cluster/contradictions.json
d50ae1803590d9be0d7836717a317a74  corpus/fixtures/r87-myth-cluster/entities.json
55ae30060a6491a9336b6a717f11586f  corpus/fixtures/r87-myth-cluster/relations.json
c16ce3c4ae8751cdaf9f06dccbc9b96c  corpus/fixtures/r87-myth-cluster/sources.json
8cef5edfaa67840c9574c4f9c95aed13  corpus/fixtures/r87-myth-cluster/timeline.json
```

### Replay command (the fixture's own declared replay, README.md:11-13)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
```

### A.1 README.md — verdict: no refusal violated (R1–R4 all respected)

Every assertive sentence was checked against the delivered data files:

| README claim | Line | Verification |
|---|---|---|
| "newly authored world-bible cluster" | 3 | self-discloses authorship; not a canon claim → R1 OK |
| "one sourced `allied_with` edge in each direction" | 3 | `relations.json:2-13` — shellweavers→reedwardens and reedwardens→shellweavers, both `source_id: shell-charter`. True. |
| "timeline contains an explicit `depends_on` edge" | 3 | `timeline.json:16-18` `bell-tally-return` depends_on `first-lowwater-signal`. True. |
| contradiction "between two uniquely sourced, resolvable timeline-event references" | 5 | `contradictions.json:5-11` — both event IDs resolve; `gate-witness` vs `dune-register` are distinct. True. |
| "**The contradiction is reported, not resolved.**" | 5 | `contradictions.json` carries no resolution/winner field; `why` states "reported and left unresolved". True → R2 OK |
| "checker validates the event and source references but does not judge source truth or select canon" | 5 | `check_bible.py` reads only `<section>.json` (`check_bible.py:42`); no truth/canon logic. True → R1/R2 OK |
| hymn + clause map "separate invented verse from editorial interpretation" | 7 | true of both files, see A.3/A.4 |
| inspiration-note "keeps attribution, rights, and AI-training permission as three distinct questions" | 7 | true, see A.2 → R3 OK |
| replay command | 11-13 | runs CLEAN, exit 0 (above) |

No canon assertion, no resolution, no rights conclusion, no mechanics content → **R1/R2/R3/R4 respected.**

### A.2 inspiration-note.md — verdict: no refusal violated (R1–R4 all respected)

- **R3 (rights):** explicit refusal, not a claim — line 13 "The rights status of the ETCSL site's modern
  presentation, editorial work, and translation has not been determined here"; line 17 AI-training permission
  "has not been assessed or established". The three questions are structurally separate (§Attribution,
  §Rights, §AI-training-permission). The line-13 sentence "The age of an underlying ancient composition does
  not by itself answer the rights question for a modern translation or edition" is a methodological caution,
  not a rights conclusion. **No rights claim made.**
- **R1 (canon):** line 19 "It is not an in-world source and supplies no fictional canon." Correct and explicit.
- **R2:** no contradiction is touched by this file; nothing resolved.
- **R4:** no mechanics content.
- **Citation accuracy (in-province, checked):** line 5 asserts the page's opening lines describe Inana's
  descent and that "lines 122–163 describe entry through seven gates and the removal of items of dress and
  regalia". I fetched the cited page
  (<https://etcsl.orinst.ox.ac.uk/section1/tr141.htm>, composite text, retrieved 2026-10-17): lines 1–5 do
  describe the descent; 114–122 is Erec-ki-gala's order to bolt the seven gates; 123–128 Neti bolts them;
  129–133 the first gate (turban removed) … 159–163 the seventh gate (pala dress removed). The quoted range
  122–163 therefore does contain all seven gate entries and the removals. **Claim holds.** Minor imprecision:
  the formal entry sequence begins at 123/129; line 122 is the tail of the preceding speech. Cosmetic only.
- **Motif-level claim (line 5):** "does not retell that composition or import its characters, plot, sequence,
  or named objects" — checked against the fixture's invented imagery (shore threshold, shared bowl, shell
  ring, reed bell): none of the composition's named objects (pala dress, lapis beads, measuring rod, Neti,
  Erec-ki-gala) or its plot appear in the fixture. **Holds.**

### A.3 lowwater-hymn-excerpt.md — verdict: no refusal violated (R1–R4 respected)

- **R1:** line 1 attributes the verse to the in-world source ID `lowwater-hymn`; that ID exists in
  `sources.json:9-13` with a reliability note ("its imagery is not an objective account of supernatural
  events"). Line 7 "not an authenticated ritual or objective world account". **Citation present, canon
  claim disclaimed.**
- **R2/R4:** nothing to resolve; no mechanics.
- **Observation OBS-1 (scope gap, low severity, not a violation):** `entities.json:27-36` gives
  `mother-tide-gate` `first_appearance: "lowwater-hymn"` and the claim *"The Low-Water Hymn names the
  Mother-Tide Gate as a shore threshold."* The delivered excerpt text does **not** contain the string
  "Mother-Tide Gate" or any proper place name (it says only "At low water … beside the bowl … the tide").
  The file is labelled an *excerpt*, so the entity claim is not falsified — it may hold of the undelivered
  remainder of the hymn — but that remainder is not in the tree, so the claim is **unverifiable from the
  delivered prose**, and the checker cannot see it (`check_bible.py` reads JSON only). Neither README nor
  the excerpt discloses that the hymn is only partially delivered. Severity: low; the excerpt label plus the
  `first_appearance` semantics carry it. Flagged because a fresh-eyes reader cannot close this loop.

### A.4 symbolism-clause-map.md — verdict: no refusal violated (R1–R4 respected)

- **R1:** line 3 attributes the source text to in-world ID `lowwater-hymn`; line 15 "These are interpretive
  readings of authored words, not new canon."
- **R2:** every "Limit" cell refuses canon-ization rather than asserting it — e.g. line 8 "Not a legal seal,
  faction emblem, or proof of alliance"; line 12 "Does not prove that the Shellweavers or Reedwardens jointly
  handled the fixture's Reed Bell"; line 13 "Does not assert supernatural return, causation, or an objective
  event." This is the correct posture for the refused axis.
- **R4:** none.
- **Clause fidelity (checked):** all seven quoted clauses appear verbatim in the excerpt
  ("At low water", "the shell ring", "beside the bowl", "The bowl keeps no name", "no voice owns the tide",
  "pass the reed-bell hand to hand", "let the water return it"). No clause is invented or paraphrased into
  a stronger claim.
- **Self-description accuracy:** line 15 "The checker does not read this map or the excerpt" — verified:
  `check_bible.py:42` loads `directory / (section + '.json')` only; no `.md` path is opened. True.

### A.5 Cross-file / whole-fixture checks

- **R2 sweep for a *second*, unreported contradiction:** the only place disagreement is the Moon-Basin Vow
  (`timeline.json:23-43`, both `tick: 3`, both `depends_on: bell-tally-return`, differing `place_id`), and it
  *is* reported in `contradictions.json`. No other cross-record conflict was found that is silently smoothed:
  `hara`/`mother-tide-gate` (keeper at her gate) and `sen`/`ash-dune-sanctuary` (recorder at the register's
  place) are mutually consistent; `reed-bell` `first_appearance` matches the tally that names it. **No silent
  resolution found anywhere.**
- **R4 sweep:** no prose file mentions a stat, rule, mechanic, balance number, or the game-dev-2d domain.
  The token "tick" occurs only as a `timeline.json` schema field, never as prose.

### A.6 Fresh-eyes bottom line

**Zero refusal-list violations across the four prose files.** All four refusals are not merely avoided but
actively disclaimed in the delivered text. Two low-severity observations (README "resolvable" phrasing
ambiguity; OBS-1 hymn-excerpt scope gap) and one verified-citation note (ETCSL line range holds). The
discipline signal is strong: the fixture states its own provenance and its own limits in the same file that
makes the claim.

---

## Part B — comparison with C7.md (and M4.md)

Opened after Part A was written. Read: `.ufo/waves/round-87/C7.md` (coverage judge #1) and
`.ufo/waves/round-87/M4.md` (compliance review).

### B.0 Are we judging the same object?

C7 and M4 judged *candidate* clusters, not the delivered tree: C7 reviewed the M3 draft in
`/tmp/r87-M3` (C7.md:4-5), M4 applied the three patches to fresh `28706dc` archives (M4.md:20-43).
Neither measured the delivered tree at `2b48ca7`; that measurement is this seat's contribution
(Part A receipts). To confirm the comparison is apples-to-apples I re-derived the structural counts on
the delivered tree:

```
$ python3 -c "... count entities/relations/timeline/sources ..."
entities=7 factions=2 relations=4 reciprocal=True events=4 depends_on_edges=3 contradictions=1 missing_source_refs=[]
```

C7.md:51 reports for M3 `entities=7, factions=2, relations=4, reciprocal=True, events=4,
depends_on_edges=3, missing_source_refs=[], contradictions=1`; M4.md:56 reports the same triple. **Exact
match on every field** → the delivered cluster *is* the M3 candidate, so C7/M4's judgments and mine cover
the same content.

### B.1 Agreements (C7 and M4 both, independently reached)

| Point | C7.md | M4.md | JCOV4 (fresh eyes, Part A) |
|---|---|---|---|
| R1 canon-without-citation | M3 PASS (C7.md:73) | Pass (M4.md:70-71) | No violation; citations present, canon disclaimed (A.1–A.4) |
| R2 silent contradiction resolution | PASS — contradiction explicitly recorded, unresolved (C7.md:73) | Pass (M4.md:71) | Confirmed; no second, unreported conflict exists (A.5) |
| R3 real-world rights claims | PASS — three questions separate, no rights/permission claim (C7.md:73) | Pass (M4.md:70) | Confirmed, R3 respected (A.2) |
| R4 game-mechanics verification | "No mechanics or art-rights bleed found" (C7.md:73) | Pass (M4.md:72) | Confirmed: no mechanics content in any prose file (A.5) |
| Checker reads JSON only, not prose | C7.md:5 | M4.md:71,75 | Independently verified at `check_bible.py:42` (A.4) |
| ETCSL citation verifiable | C7.md:73 "fetching the cited page confirmed the seven-gate passage at lines 122–163" | M4.md:59 "text describing Inana's descent and the seven gates/removal of dress" | **Independent third fetch agrees** (A.2) |

On every refusal item, and on the two machine-checkable side claims (checker scope, ETCSL passage), the
three seats agree. C7's M3 = PASS and M4's M3 = Pass are corroborated by a fresh-eyes pass that reached
the same conclusion without having read either.

### B.2 Disagreements / refinements

1. **Narrow refinement of C7's named debt — the *delivered* in-world text is not fully auditable either.**
   C7.md:74 lists source-text auditability as named debt, but frames it as "M3 includes the Low-Water Hymn
   excerpt, while its witness slip, local register, charter, and tally are still metadata-only" — i.e. the
   hymn is treated as the one fictional source whose text *is* delivered and therefore auditable. My audit
   finds that the delivered hymn excerpt does **not** carry the content of the one claim attributed to it:
   `entities.json:33` asserts *"The Low-Water Hymn names the Mother-Tide Gate as a shore threshold"*, but

   ```
   $ grep -n "Gate\|Sanctuary\|Basin\|Ash" lowwater-hymn-excerpt.md
   (no output)
   ```

   the excerpt contains no proper place name at all. So C7's debt understates the gap: even the one
   in-world text that was delivered leaves its attributed claim unverifiable from the delivered prose. This
   is my seat's only substantive addition, and it is a *widening* of C7's debt, not a contradiction of its
   PASS (the excerpt is labelled an excerpt, so the claim is not falsified — it may hold of the undelivered
   remainder).
2. **M4's debt is stated more broadly than C7's and absorbs my finding.** M4.md:75 says the checker "does
   not inspect Markdown notes/maps or validate semantic support, so all interpretation remains editorial
   rather than machine-verified" — that generic statement covers OBS-1, though M4 did not name this
   specific instance. Between C7 (narrow) and M4 (broad) my finding sits with M4's framing.
3. **No disagreement on any R1–R4 verdict.** I found no violation that C7 or M4 missed, and no C7/M4
   finding I judge to be a false positive.

### B.3 Axis verdict (this seat)

Per-axis, on the delivered tree at `2b48ca7`, no scalars:

- **Refusal-list conformance of the delivered prose** — **improved**. 4/4 refusal items respected, zero
  violations, each one actively disclaimed rather than merely unmentioned. Baseline: the cluster directory
  did not exist before this round (M4.md:9-18 shows the replay failing with 5 "No such file" violations),
  so the delivery moves this axis from absent to conforming.
- **Provenance self-disclosure** — **improved**. Every prose file states its own provenance and its own
  limits in the same file that makes its claim (A.1–A.4).
- **Citation verifiability** — **improved, with named debt**. The ETCSL range is independently verifiable
  and verified; the `mother-tide-gate` ← hymn claim is not verifiable from the delivered prose (OBS-1).
  Named debt, not a violation.
- **Machine-checkability of prose discipline** — **unchanged**. `check_bible.py` still reads JSON only
  (`check_bible.py:42`); no prose policy is machine-enforced, which C7 (C7.md:5), M4 (M4.md:75) and I all
  observe independently.
- **No axis harmed** by this delivery on the evidence gathered.

### B.4 Handoff

- Output: this file only — `.ufo/waves/round-87/followup/JCOV4.md`. **No tracked file written, nothing
  committed, no push, no registry write**; my seat block authorized no named tracked file and none was needed.
- For the round's record: my verdict corroborates C7's M3 PASS on the delivered tree (the one place neither
  C7 nor M4 measured), and adds one named debt — OBS-1 — that a record artifact should carry forward if the
  round claims "in-world texts delivered and auditable". If the round prefers, OBS-1 is closable by either
  (a) adding the Mother-Tide Gate's naming to the delivered hymn excerpt, or (b) changing
  `mother-tide-gate.first_appearance` to a source whose text is delivered, or (c) recording the excerpt's
  scope limit explicitly. No such fix was made by this seat (no authorization, and the mission is judging).
- Follow-up worth noting to the parent: C7 and M4 both judged pre-landing candidates; a future round should
  measure delivered trees directly so that "judged" and "shipped" cannot drift apart.
