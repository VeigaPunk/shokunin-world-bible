# Round 23 critic — falsify “witnessed-absence” depth claim

Claim under test: a *witnessed-absence* note, clause-mapped, is a new observation class and improves **depth** without harming **coverage** or **calibration**.

Scope: leaf critic only. Baseline HEAD lacks `.shokunin/lore/corpus/fixtures/r23-note-class` (`git cat-file -e` fails). Comparison baseline is the admitted r15 private-note fixture and the rejected r14 depth-restatement pattern. `check_bible.py` validates schema/citations/relations/timeline structure; it does **not** map source prose. Source-text truth is unverified. No canon claim.

## Raw r15 clauses (quoted for comparison)

From `.shokunin/lore/corpus/fixtures/r15-carbon-followup/sella-carbon-followup-excerpt.md` (source ID `sella-carbon-followup`):

> Later, at Lantern Harbor, I looked again at the carbon I had kept. I saw a blurred blue oval mark on it. I cannot identify where the mark came from, and I do not attribute it to Mira’s Blue Seal.

From the same fixture’s earlier register excerpt (`registrar-copy-excerpt.md`):

> At first bell at Lantern Harbor, I, Sella, registrar there, recorded seeing Mira leave. At Mira’s request, I left the registry destination blank and kept the carbon.

From `timeline.json` event `carbon-followup` description (already mapped):

> Sella reports looking again at the carbon she kept and observing a blurred blue oval mark whose origin she cannot identify; she does not attribute it to Mira’s Blue Seal.

From `entities.json` / relation baseline still present in r15:

- Mira claim: “Mira carried the blue seal.” (`courier-log`)
- Seal claim: “The seal accompanied Mira.”
- Relation: `mira` → `seal` type `carries`

These are fixture observations, not recovered evidence.

---

## 1. Collapse into r14 restatement

Round 14’s depth move was rejected because newly authored excerpts **only restated existing JSON rows** (route, carry, registry/watch-bell claims) without a new inspectable uncertainty or event class. Critic pattern: prose volume + phrase↔row maps ≠ depth; circular authoring of text to match rows is legibility, not deeper lore.

**Ways r23 “witnessed absence” collapses the same way:**

1. **Negation of an already-mapped positive is still restatement.**  
   If the new note only says, in effect, “Sella does not attribute the mark to Mira’s Blue Seal,” that clause is **already present** in r15 excerpt sentence 3 and in the `carbon-followup` timeline description. Clause-mapping that sentence into a new “class” label does not add a world detail; it relabels an existing boundary. That is r14-style documentation depth, not new observation depth.

2. **Absence of destination / blank field already exists.**  
   Registrar prose already encodes a kind of absence: “I left the registry destination blank.” If r23’s “witnessed absence” is operationalized as “Sella reports the destination was not written,” it collapses into the r10/r15 `registry-entry` row, not a new class.

3. **Absence of identified origin already exists.**  
   “I cannot identify where the mark came from” is already an explicit non-identification. Treating “origin not identified” as a fresh witnessed-absence class double-counts r15 without a new predicate (e.g., a *named object/event reported missing from a named scene*).

4. **File/row inflation without new predicate.**  
   Adding `r23-note-class/` with entities/timeline/sources that mirror r15 IDs, plus a README that defines “witnessed absence” as a taxonomy term, matches r14’s failure mode: more files, same claims. Depth unchanged under the r14 standard.

**Minimal non-collapse requirement (for others, not implemented here):** the note must report that a **named speaker** reports a **named thing was not present** at a **bounded place/time**, where that non-presence is **not already asserted** by r15 mark/origin/non-attribution clauses or by the blank-destination registry act.

---

## 2. Collapse into r15 mark observation

r15’s private-note observation class (as mapped) is roughly:

| Clause | Kind |
|---|---|
| “I looked again at the carbon I had kept” | later inspection of retained object |
| “I saw a blurred blue oval mark on it” | **positive** sensory report of a mark |
| “I cannot identify where the mark came from” | unknown origin |
| “I do not attribute it to Mira’s Blue Seal” | explicit **non-attribution** (speech act about cause/identity), not “the seal was absent” |

**Collapse paths:**

1. **Non-attribution ≠ witnessed absence of the seal.**  
   “I do not attribute it to Mira’s Blue Seal” does **not** say “I did not see the Blue Seal,” “the Blue Seal was not on the carbon,” or “Mira was not carrying the seal.” If the r23 class is filled with non-attribution wording, it is still the r15 mark package.

2. **Unknown origin ≠ absence of a named object.**  
   Failure to identify source is epistemic limit on a **present** mark, not a report that something expected was missing.

3. **“Blurred blue oval” remains a presence observation.**  
   Any fixture that still centers seeing the mark, then tags a side clause as “absence,” smuggles r15’s primary observation under a new heading. Depth claim fails if the inspectable novelty is only the taxonomy name.

4. **Shared speaker/place/object chain.**  
   Same speaker (Sella), same place (Lantern Harbor), same object (kept carbon), same follow-up after `registry-entry`: without a *different* missing nominatum (e.g., a named stamp, second carbon, witness, seal impression *as object*), the scenario is r15 redux.

5. **Timeline dependency clone.**  
   Another tick-3 event depending on `registry-entry` with Sella@harbor and source kind “private note” is structurally r15’s `carbon-followup`. Structure + speaker + carbon without a new absence predicate = duplicate class.

---

## 3. Prose smuggling: Blue Seal attribution, causation, source-text truth

Even with a disclaimer sentence, calibration can be harmed the same ways r15-critic flagged:

1. **Color/shape priming.**  
   “Blue” + “oval” beside entity name “Blue Seal” and relation `carries` invites readers to treat non-attribution as coy understatement. Titles like `seal-trace-note`, IDs like `seal-absence`, or claims “mark inconsistent with Blue Seal” convert resemblance into negative identification (still attribution-shaped).

2. **Causal smuggling via “so / therefore / must not / could not have.”**  
   Example bad clause: “I saw no Blue Seal, so the mark cannot be Mira’s.” That asserts causation/exclusion beyond a bare witnessed absence. r15 already risks this; r23 must not “improve depth” by strengthening causal exclusion.

3. **Scope creep from ‘not on the carbon’ → ‘Mira had no seal’.**  
   A local absence (seal not observed on this paper / in this room) must not be written as global denial of the `carries` relation or of Mira’s possession. That would **harm calibration** relative to existing courier-log rows and invent contradiction without a contradictions ledger entry.

4. **Omniscient or checker-as-truth language.**  
   Phrases such as “verified absent,” “proves the seal was never there,” “excerpt confirms,” or “clause map validates source truth” smuggle **source-text truth** the checker does not establish. Honest framing: speaker *reports* non-presence; fixture is newly authored fiction; map is editorial traceability only.

5. **Motive / investigative framing.**  
   “I checked specifically for the Blue Seal” or “I saved the carbon to look for seal traces” invents purpose not in registrar-copy (“At Mira’s request… kept the carbon”). That smuggles intent and can imply expected presence (a seal *should* have left a mark).

6. **Entity-row backfill.**  
   Adding seal claims like “The Blue Seal was not on Sella’s carbon” as omniscient entity truth (vs Sella-bounded report) launders a witness claim into item ontology—calibration harm and soft canon.

---

## 4. Adding files/rows without new inspectable uncertainty is not depth

Depth (substantive, per r14 reject + r15 critic) requires a **richer world account** or **additional inspectable lore distinction**, not:

- more paths under `corpus/fixtures/`
- more JSON rows that restate old sentences
- a glossary term “witnessed absence” without a fixture clause that only that term fits
- a clause map that pairs each old r15 sentence to a row
- checker-clean structure with no new uncertainty surface

**What counts as inspectable uncertainty (examples of the bar, not proposals):**  
a named expected item/person/marking **reported missing**; conflict between two witnesses on presence; explicit “I looked for X and did not see X” where X is named and not already settled; a contradictions row that records presence vs absence reports without resolving them.

**What does not count:**  
renaming non-attribution; blank destination already mapped; unknown origin already mapped; README taxonomy; duplicate micro-bible of r15.

If r23 ships only taxonomy + maps + mirrored rows, **depth is unchanged** regardless of coverage of new filenames.

---

## 5. What forces depth unchanged or a reject

### Depth unchanged (adjudicator should refuse “improved”)

- Final excerpt’s operative clauses are paraphrase-equivalent to the four r15 quoted sentences above.
- “Absence” is implemented only as non-attribution or unknown origin.
- No named nominatum is reported missing that is distinct from “identified origin” / “Blue Seal attribution.”
- JSON descriptions copy r15 `carbon-followup` text with a class label in metadata only.
- Sole “novelty” is the directory name `r23-note-class` or a schema enum value unused by divergent prose.

### Reject (harm or false axis claim)

- **Calibration harm:** prose, titles, claims, or relations imply the mark is/isn’t seal-caused; deny `carries` from a local non-sighting; treat clause maps or green `check_bible.py` as prose-truth or canon; invent Mira/Sella motives for the carbon.
- **Coverage harm (if claimed expanded):** fixtures that break loader/schema, dangling source IDs, or duplicate pair violations without tests—or “coverage” claimed for a class the checker cannot see (prose-only) while advertising checker coverage.
- **False depth advertising:** LOG/SCORECARD claims “new observation class” when independent reading finds only r14 restatement or r15 mark package.
- **Contradictions silent merge:** presence (courier seal) and absence (Sella) written as both simply true with no ledger/qualification.

### Narrow path that could still support depth *without* this critic endorsing implementation

Only if **all** hold: (a) first-person report that a **named** thing was **not present** at a bounded scene; (b) that non-presence is **not** entailed by r15’s mark/origin/non-attribution text; (c) uncertainty remains speaker-bounded, newly authored, non-omniscient; (d) no causal seal smuggling; (e) manual clause review shows at least one inspectable distinction a reader could not get from r15 files alone. Even then, depth is **unprovable from structure alone**—non-author prose review required. This report does **not** assert such a fixture exists (baseline absence of `r23-note-class`).

---

## 6. Axis summary (critic stance, not verdict)

| Axis | Pressure result |
|---|---|
| **depth** | Claim is **easily falsified** by r14 restatement and r15 non-attribution/unknown-origin overlap. Default prior: depth **unchanged** until a distinct missing-nominatum clause is inspectable. |
| **coverage** | New files do not automatically improve coverage of checker-visible behaviors; prose classes are outside `check_bible.py`. Neutral at best; do not trade fake depth for untested surface area. |
| **calibration** | High harm risk if Blue Seal adjacency, causation, or source-truth language creeps in—same failure mode as r15-critic items 1–2. |

## Recommendation (not evidence)

Treat “witnessed absence” as **not yet demonstrated** at baseline. Do not admit a depth win for taxonomy or for re-mapping “I do not attribute it to Mira’s Blue Seal.” Require a side-by-side clause table against the r15 quotes above; any row that only rephrases those quotes is disqualifying for depth. Preserve fictional / non-recovered labels; never equate checker exit 0 with source-text truth.

I did not edit the checker, fixtures, LOG, SCORECARD, or any file other than this report. I did not commit.
