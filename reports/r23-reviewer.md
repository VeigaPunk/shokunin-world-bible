# Round 23 non-author reviewer — witnessed-absence note class

## Scope

Read-only review of fixture `.shokunin/lore/corpus/fixtures/r23-note-class/` against critic bar in `.shokunin/lore/reports/r23-critic.md` and r15 baseline excerpt `.shokunin/lore/corpus/fixtures/r15-carbon-followup/sella-carbon-followup-excerpt.md`. No edits to fixtures, checker, LOG, or SCORECARD. No commit. No spawn. This report is the only write.

Source-text truth is unverified. Checker does not map prose. Fixture is newly authored fiction.

## Artifacts under review

**Excerpt** (`sella-absence-note-excerpt.md`, source id `sella-absence-note`):

> Later at Lantern Harbor, I, Sella, looked for Mira’s outbound route strip on the registry hook rack. I did not find it there.

Framing lines on the same file: witnessed-absence report; does not say why; does not say the strip never existed; does not mention a mark, a carbon, or Mira’s Blue Seal.

**Clause map** (`witnessed-absence-clause-map.md`) pairs:

| Operative clause (excerpt) | Map / fixture binding |
|---|---|
| “Later” | `timeline` event `strip-absence-note`, tick 3, `depends_on: ["departure"]` — order only, not a clock |
| “at Lantern Harbor” | `place_id` = `harbor` |
| “I, Sella” | `entity_id` = `sella` |
| “looked for Mira’s outbound route strip on the registry hook rack” | Sella claim + timeline description (search report; strip is not an entity row) |
| “I did not find it there” | same claim/description — witnessed-absence predicate |
| (no cause) | deliberately unmapped |
| (no proof of world-absence) | `sources[sella-absence-note].reliability_note` |
| (no Blue Seal / mark / carbon link) | deliberately unmapped |

**r15 comparison excerpt** (verbatim):

> Later, at Lantern Harbor, I looked again at the carbon I had kept. I saw a blurred blue oval mark on it. I cannot identify where the mark came from, and I do not attribute it to Mira’s Blue Seal.

## Critic bar checklist

Critic’s narrow non-collapse path (section 5): (a) named speaker reports named thing not present at bounded scene; (b) non-presence not entailed by r15 mark/origin/non-attribution; (c) speaker-bounded, newly authored, non-omniscient; (d) no causal seal smuggling; (e) at least one inspectable distinction unavailable from r15 alone.

| Critic requirement | Finding |
|---|---|
| Named thing reported missing | **Met.** Nominatum is “Mira’s outbound route strip” at “the registry hook rack.” Not “origin,” not “Blue Seal attribution,” not blank destination alone. |
| Not entailed by r15 | **Met.** r15 clauses are: later look at kept **carbon**; **positive** sensory report of blurred blue oval mark; unknown origin; explicit non-attribution to Mira’s Blue Seal. None asserts search for or non-finding of a route strip on a hook rack. |
| No Blue Seal identification | **Met** in excerpt, map, and JSON. Excerpt never names the seal. Timeline description: “no claim about Mira’s Blue Seal.” Source reliability_note: “not a claim about Mira’s Blue Seal.” Map row: no Blue Seal link. |
| No cause | **Met.** No theft, removal, motive, or “so/therefore” exclusion. Map and timeline both mark cause unmapped / none. |
| Speaker-bounded | **Met.** First person Sella; claim statement is “Sella **reports** that she looked… and did not find…”; reliability_note: report ≠ proof strip absent as fact. |
| Newly authored | **Met.** Excerpt header and source title/reliability_note label fictional private note, newly authored, not recovered. |
| Not r14 restatement of existing JSON only | **Met for depth surface.** New predicate is inspectable in prose (named missing strip at rack), not a relabel of non-attribution or unknown-origin alone. Baseline courier rows remain; they are not the absence claim. |
| Not r15 mark package under new taxonomy | **Met.** Object of attention is route strip / hook rack, not carbon/mark. No “looked again at the carbon,” no oval, no origin sentence, no non-attribution sentence. |

## Side-by-side: r15 vs r23 operative clauses

| r15 operative clause | r23 operative clause | Same claim? |
|---|---|---|
| looked again at the carbon I had kept | looked for Mira’s outbound route strip on the registry hook rack | No — different object and act (re-inspect retained carbon vs search rack for strip) |
| saw a blurred blue oval mark on it | *(none)* | No — r23 has no presence-of-mark clause |
| cannot identify where the mark came from | *(none)* | No — r23 is not unknown-origin of a present mark |
| do not attribute it to Mira’s Blue Seal | *(none)*; explicit avoidance | No — r23 does not perform non-attribution speech about the seal |
| *(no strip / rack non-finding)* | I did not find it there | r23-only nominatum absence |

Shared surface only: speaker Sella (named in r23; implied in r15 follow-up chain), place Lantern Harbor, “Later” temporal framing, private-note genre. Shared speaker/place/genre does not collapse the nominatum under the critic’s own test (“different missing nominatum”).

## JSON calibration pass (entities, timeline, sources)

**entities.json**

- `mira` claim remains “Mira carried the blue seal.” (`courier-log`) — **not denied**.
- `seal` claim remains “The seal accompanied Mira.” — **not denied**.
- `sella` claim is report-shaped: looked for strip on rack and did not find it — not “the strip was absent” as world fact; strip is not a separate entity row with omniscient absence ontology.

**timeline.json** event `strip-absence-note`

- Description quotes the report and adds: “Fixture input only: no cause, no proof the strip was absent as fact, and no claim about Mira’s Blue Seal.”
- Does **not** claim world-absence of the strip.
- Does **not** deny Mira carries the seal.
- Structure is tick-3 / Sella@harbor / depends_on departure — similar *shape* to r15’s follow-up tick, but description and source_id are strip-absence, not carbon-followup mark package. Critic warned that structure alone can clone r15; here the **predicate text** diverges, which is what the bar asked for.

**sources.json** `sella-absence-note`

- reliability_note: report is not proof the strip was absent as fact; not a claim about Mira’s Blue Seal.
- kind: fictional private note; newly authored framing consistent with excerpt.

**relations.json**

- Still `mira` → `seal` type `carries` from `courier-log`. No absence relation that undoes carry.

**contradictions.json**

- Empty. Local non-finding of a strip is not written as contradicting `carries`. Appropriate: different nominatum; no silent merge of seal presence vs seal absence.

No titles/IDs of the form `seal-absence` / `seal-trace`. Source title is “Sella’s rack note.” Event id is `strip-absence-note`.

## Smuggling scan (critic §3)

- Color/shape priming toward Blue Seal: **absent** from r23 excerpt.
- Causal “so / must not”: **absent**.
- Scope creep non-finding strip → Mira had no seal: **absent** in prose and JSON; `carries` retained.
- Omniscient “verified absent” / checker-as-truth: **absent**; map states checker does not read the map; reliability_note denies proof.
- Motive (“checked specifically for Blue Seal” / saved carbon to hunt seal traces): **absent**.
- Entity-row backfill of seal-not-on-carbon as item truth: **absent**.

## Verdict

**Clause map holds.** The five positive excerpt clauses map to speaker, place, search act, and non-finding without inventing cause, world-proof absence, Blue Seal identity, or mark/carbon content. Negative map rows (no cause, no world-absence proof, no Blue Seal, no mark/carbon) match the prose and JSON.

**Depth is supported** relative to the critic’s stated bar: a distinct **named missing nominatum** (Mira’s outbound route strip on the registry hook rack), speaker-bounded, newly authored, not entailed by r15’s four operative sentences, without Blue Seal identification or cause. It does **not** collapse into r15’s mark / unknown-origin / non-attribution package, and it is not merely r14-style restatement of non-attribution as a taxonomy label.

**Caveats (not collapses):**

1. Depth remains a **manual prose judgment**; structure/tick pattern alone would be insufficient (critic §2.5 / §4). Support rests on the strip/rack non-finding clauses quoted above.
2. Checker exit status (not re-run in this review) still does not establish source-text truth.
3. Courier-log seal `carries` and strip non-finding coexist without a contradictions row; that is correct only while they stay different nominata—do not later rewrite the strip note as seal absence.
4. Shared Sella + Lantern Harbor + “Later” framing is intentional continuity, not identity of observation class.

### Operative clauses quoted for adjudication

**r23 (support depth):**

> Later at Lantern Harbor, I, Sella, looked for Mira’s outbound route strip on the registry hook rack. I did not find it there.

**r15 (must not be the sole content of r23):**

> Later, at Lantern Harbor, I looked again at the carbon I had kept. I saw a blurred blue oval mark on it. I cannot identify where the mark came from, and I do not attribute it to Mira’s Blue Seal.

**JSON guard (calibration):** timeline description fragment — “no cause, no proof the strip was absent as fact, and no claim about Mira’s Blue Seal”; mira/seal claims and `carries` retained.

## Non-actions

Did not edit fixtures, checker, LOG, or SCORECARD. Did not commit. Did not spawn.
