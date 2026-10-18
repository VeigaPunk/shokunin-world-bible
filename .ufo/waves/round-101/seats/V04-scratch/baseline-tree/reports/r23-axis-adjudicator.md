# Round 23 axis adjudicator — lore shokunin

Role: independent axis adjudicator only.  
Repo: `/home/vgpnk/Projects/prymeagnt/lore`  
Claim under test: one new **witnessed-absence** note class in `.shokunin/lore/corpus/fixtures/r23-note-class/` (Sella reports looking for Mira’s outbound route strip on the registry hook rack and not finding it). Manual clause map; checker does not read prose.

Axes owned: **depth**, **coverage**, **calibration**.  
Verdict vocabulary only: improved | harmed | unchanged | unprovable-but-better. No scalars.  
Admit rule: admit only if at least one axis **improved** and none **harmed**.

Did not edit fixtures, checker, LOG, SCORECARD, README, or decision table. Did not commit. Did not spawn. This report is the only write.

Source-text truth is unverified. Fixture is newly authored fiction.

---

## Evidence read (primary, not summaries alone)

| Artifact | Path |
|---|---|
| Excerpt | `.shokunin/lore/corpus/fixtures/r23-note-class/sella-absence-note-excerpt.md` |
| Clause map | `.shokunin/lore/corpus/fixtures/r23-note-class/witnessed-absence-clause-map.md` |
| entities / timeline / sources / relations / contradictions | same fixture dir |
| Critic (falsification bar) | `.shokunin/lore/reports/r23-critic.md` |
| Reviewer | `.shokunin/lore/reports/r23-reviewer.md` |
| Independent verifier | `.shokunin/lore/reports/r23-independent-verifier.md` |
| r15 contrast excerpt | `.shokunin/lore/corpus/fixtures/r15-carbon-followup/sella-carbon-followup-excerpt.md` |

---

## Operative r23 clause (quoted)

From `sella-absence-note-excerpt.md` (source id `sella-absence-note`):

> Later at Lantern Harbor, I, Sella, looked for Mira’s outbound route strip on the registry hook rack. I did not find it there.

That pair is the inspectable surface: named speaker, named search object (outbound route strip on the registry hook rack), named place, and speaker-bounded non-finding. Framing on the same file and the clause map state: no cause; no claim the strip never existed; no mark, carbon, or Mira’s Blue Seal.

## r15 contrast (must not be the sole content of r23)

> Later, at Lantern Harbor, I looked again at the carbon I had kept. I saw a blurred blue oval mark on it. I cannot identify where the mark came from, and I do not attribute it to Mira’s Blue Seal.

r15 is a **presence** observation of a mark on a kept carbon, plus unknown origin and non-attribution to the Blue Seal. It does not assert search for or non-finding of a route strip on a hook rack.

---

## Fixture calibration guards (JSON + map)

- `entities.json`: `mira` still claims “Mira carried the blue seal.” (`courier-log`); `seal` still “The seal accompanied Mira.”; `sella` claim is report-shaped non-finding of the strip, not omniscient strip ontology.
- `relations.json`: only `mira` → `seal` `carries` from `courier-log` (retained).
- `timeline.json` event `strip-absence-note`: description includes “no cause, no proof the strip was absent as fact, and no claim about Mira’s Blue Seal.”
- `sources.json` `sella-absence-note.reliability_note`: report ≠ proof of world-absence; not a claim about Mira’s Blue Seal.
- `contradictions.json`: `[]` — strip non-finding is not written as undoing `carries`.
- Clause map: negative rows for cause, world-absence proof, Blue Seal, mark/carbon deliberately unmapped; class labeled witnessed absence and distinguished from r15 mark observation.

No prose treating the report as world-fact absence of the strip, no denial that Mira carries the seal, no mark attributed to the Blue Seal.

---

## Checker re-run (this adjudicator)

Command (repo root):

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r23-note-class
```

- **exit code: 0**
- stdout: `CLEAN: schema, citations, relations, timeline; 0 violations`

---

## Independent verifier measures (accepted after own check_bible re-run)

From `.shokunin/lore/reports/r23-independent-verifier.md` (baseline `d6ea676`):

| measure | result |
|---|---|
| check_bible r23-note-class | exit 0, CLEAN (reproduced here) |
| live transcript exact match | **72 / 72** |
| baseline fixture JSON unchanged | **359 / 359** (r22’s 319 is an older inventory; do not force 319) |
| r23-note-class at baseline | **absent** (`git cat-file -e` fails on d6ea676 path) |

Coverage judgment uses checker behavior on prior fixtures unchanged (72/72), not “new files exist.”

---

## Axis verdicts

### depth — **improved**

Critic bar (r23-critic §5 narrow path): (a) named speaker reports a named thing not present at a bounded scene; (b) that non-presence is not entailed by r15 mark / origin / non-attribution; (c) speaker-bounded, newly authored, non-omniscient; (d) no causal seal smuggling; (e) at least one inspectable distinction unavailable from r15 alone.

**Finding:** Met. The nominatum is **Mira’s outbound route strip on the registry hook rack**, with predicate **I did not find it there**. That is not r14 restatement of existing non-attribution/blank-destination/unknown-origin rows, and not the r15 mark package (no carbon re-inspection, no blurred blue oval, no origin sentence, no Blue Seal non-attribution speech). Shared Sella + Lantern Harbor + “Later” framing is continuity of speaker/place/genre, not identity of observation class. Depth here is a manual prose judgment (structure/tick alone would be insufficient); the strip/rack non-finding clauses are the inspectable novelty.

### coverage — **unchanged**

Parent rule: coverage stays unchanged if checker behavior on prior fixtures is unchanged (**72/72**). Verifier: 72/72 exact; 359/359 baseline JSON byte-same; only new JSON under `r23-note-class/`. The checker still does not read prose or the clause map, so the new note class does not expand checker-visible coverage of prior fixtures. No coverage harm (no baseline JSON drift, no broken prior runs).

### calibration — **unchanged**

Parent harm tests: prose treats the report as world-fact absence; denies Mira carries the seal; or attributes a mark to the Blue Seal.

**Finding:** None of those harms appear in excerpt, map, or JSON. Reliability_note and timeline description keep report ≠ world-proof absence; `carries` retained; no mark/Blue Seal language in the note class fields; empty contradictions ledger correctly avoids silent seal presence/absence merge. Not “improved” calibration (no stronger honest-stop machinery beyond correct local guards); not harmed.

---

## Admit decision

| Axis | Verdict |
|---|---|
| depth | **improved** |
| coverage | **unchanged** |
| calibration | **unchanged** |

- At least one **improved**: yes (depth).  
- Any **harmed**: no.  

**Admit: yes.**

---

## Limits

- No claim of recovered evidence, canon, or source-text truth.
- Checker exit 0 does not validate prose semantics.
- Admit applies to this round’s axis claim for the owned three axes only; does not rewrite LOG/SCORECARD (out of scope for this role).

## Non-actions

Did not edit fixtures, checker, LOG, SCORECARD, README, or decision table. Did not commit. Did not spawn.
