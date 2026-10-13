# Round 55 regression scout — pinned baseline and controls

## Finding

**Material-depth recommendation: NO-GO absent a concrete consequence beyond a conditional juxtaposition.** The proposed Mira first-person report differs from the rejected r53 satchel-handling note: it puts a claimed placement at the same named rack Sella later reports searching. That permits a reader to compare two attributed rack accounts. But the relation remains conditional on the described strip being the same physical referent and the reported placement/search being compatible in sequence; placement does not establish continued presence. Without an independently inspectable consequence surviving those uncertainties, the additional report risks manufactured tension rather than demonstrated material depth. No r55 candidate exists in this work; I did not run a candidate checker or claim candidate results.

## Literal r23 control

The excerpt is `.shokunin/lore/corpus/fixtures/r23-note-class/sella-absence-note-excerpt.md:5`: “Later at Lantern Harbor, I, Sella, looked for Mira’s outbound route strip on the registry hook rack. I did not find it there.” Its map, `.shokunin/lore/corpus/fixtures/r23-note-class/witnessed-absence-clause-map.md:9-20`, maps this only as Sella’s reported search/non-finding; “Later”/tick order is fixture order, not clock or duration. It explicitly leaves cause, world-absence and Blue Seal/carbon/mark links unmapped. The excerpt does not assert prior rack placement.

R23’s current controls also include `entities.json` (Sella’s attributed claim; strip is not an item entity), `timeline.json` (Sella event tick 3 depending on departure; editorial ordering), and `contradictions.json` (`[]`). These do not establish a single physical strip, rack occupancy, or causal relationship. The proposed Mira wording (“placed what I called my outbound route strip on that registry hook rack as I departed”) is hypothetical—not a source excerpt or fixture. Unlike r53’s proposed satchel handling, it names the location of the reported action at the search site, which makes the comparison more concrete, but still does not establish presence at Sella’s later search.

## Precedent and limits

R53 rejected the hypothetical satchel handling because neither same-strip identity nor compatible sequence was established, and handling did not explain the non-finding (`.shokunin/lore/reports/r53-reviewer.md`, “Decision” and “Evidence and comparison”; `.shokunin/lore/reports/r53-axis-adjudicator.md`, “Source and materiality judgment”). The r55 rack placement narrows the location gap, but does not remove the identity/sequence gap or supply a consequence. R43’s admitted comparison is a contrast, not a rule for any two accounts: Jorin’s report located Vela at the same specifically named east steps where Vela herself reported standing, yielding a directly inspectable conditional location overlap (`.shokunin/lore/reports/r43-axis-adjudicator.md`, “Clause, precedent and falsification check”). It did not prove a shared occasion. R30’s admitted calibration move concerned explicit negation versus near-miss support, not adding an account to deepen a narrative (`.shokunin/lore/reports/r30-axis-adjudicator.md`, “Manual semantic decision and axis boundaries”).

R10’s Sella registrar excerpt reports her seeing Mira leave, leaving destination blank at Mira’s request, and keeping the carbon (`.shokunin/lore/corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md:5`). R15’s excerpt reports Sella later looking again at the carbon she says she kept, seeing an unknown-origin blurred blue oval, and not attributing it to Mira’s Blue Seal (`.shokunin/lore/corpus/fixtures/r15-carbon-followup/sella-carbon-followup-excerpt.md:5`). These controls concern carbon/mark, not route-strip identity, rack placement, or custody; they imply no link to this hypothetical.

## Baseline / delta / falsifier

The r55 declaration pins baseline report commit `0fbc33860ea35cdf5f4a2fb3435bab36fd4126ff`, 95 active fixture directories and 474 fixture JSON paths (`.shokunin/lore/LOG.md:936-940`). This is the replay contract, not work performed by this scout. If a candidate is later authorized, archive the pinned baseline separately; from each respective repository root run the same root-relative argv for every old fixture:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>
```

Compare raw stdout bytes, stderr bytes, and exit code for each of 95 cases; compare all 474 old JSON paths/bytes and checker bytes. Preserve r23’s original files byte-for-byte. An isolated clone would add a fixture directory and its actual files; report observed inventory rather than assuming a file count. There is no observed candidate delta or old-vs-live replay here. Baseline preservation and structural CLEAN, if later obtained, cannot validate prose truth.

**Falsifier:** a built, independently reviewed, minimally attributed comparison that gives a concrete reader-facing consequence while keeping identity and compatible timing explicitly unresolved could overturn this NO-GO. Conversely, any claim that this proves continuous rack presence, physical strip identity, removal/theft, actual contradiction, custody, or world-absence falsifies calibration. Mira rack placement remains hypothetical. Nothing here establishes canon, rights, permission, or any Blue Seal/carbon relation.
