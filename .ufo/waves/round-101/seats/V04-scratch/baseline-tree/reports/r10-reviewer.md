# Round 10 independent reviewer — registry-witness fixture

## Scope and result

I inspected the raw `corpus/fixtures/r10-registry-witness/` JSON and `registrar-copy-excerpt.md`, the executor's mapping, the fixture README, and the round-10 LOG declaration. I independently ran:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r10-registry-witness
CLEAN: schema, citations, relations, timeline; 0 violations
exit status: 0
```

That is a structural/citation-ID result, not a prose entailment test. Comparing the five `consistent/` JSON files to `git show HEAD:.shokunin/lore/corpus/fixtures/consistent/<file>` found each byte-identical. In the new fixture each original JSON row is retained, in original order and unchanged; the new rows are appended. This confirms row preservation for the source fixture, not checker/source validation of the claims.

## Clause mapping and limits

The entire excerpt (`registrar-copy-excerpt.md`) is: “At first bell at Lantern Harbor, I, Sella, registrar there, recorded seeing Mira leave. At Mira’s request, I left the registry destination blank and kept the carbon.” It is explicitly labeled “invented fixture text (not recovered evidence).”

| Added item | Raw assertion / source | Matching clause | Review |
|---|---|---|---|
| Entity `sella` | name `Sella`; first appearance `registrar-copy` | “I, Sella” | Direct textual match. This is an authored fictional speaker, not independently attested identity. |
| Sella claim | “Sella is a registrar at Lantern Harbor.” / `registrar-copy` | “At first bell at Lantern Harbor, I, Sella, registrar there” | Direct match to the excerpt's self-description. Not external verification of her role. |
| Relation | `sella` → `mira`, `records_departure` / `registrar-copy` | “recorded seeing Mira leave” | Reasonable label for the act described. It establishes what this invented text says Sella recorded, not that departure independently occurred. |
| Event | `registry-entry`, tick 1, Sella at harbor; description says she records seeing Mira leave, leaves destination blank at Mira’s request, and keeps carbon / `registrar-copy` | “At first bell at Lantern Harbor”; “recorded seeing Mira leave”; “At Mira’s request, I left the registry destination blank and kept the carbon.” | All descriptive details are clause-backed. Harbor placement is supported by “At ... Lantern Harbor.” The excerpt states a blank destination, not an alternate destination. |

No added assertion says why Mira requested the omission; privacy, secrecy, concealment, or motive would be unsupported. The excerpt does not mention North Tower, the blue seal, or the courier-log; those remain baseline claims, not claims newly supported by `registrar-copy`. The source's reliability note appropriately bounds the text as invented and non-omniscient.

## Tick / observation-time caveat

The excerpt locates Sella's report at “first bell” and says she saw Mira leave. It does **not** define the checker tick scale or equate “first bell” with tick 1. Assigning `registry-entry` tick 1 and treating the account as a contemporaneous perspective on baseline `departure` tick 1 is a fixture-author mapping, not a source-derived conversion or an independently checked timestamp. The text makes it plausible that the two rows concern the same departure, but it cannot establish exact simultaneity or within-tick ordering. Empty `depends_on` is appropriate: equal local ticks do not satisfy strict-earlier dependency ordering. Do not describe the added event as independently synchronized/corroborating the baseline chronology.

## Depth versus filler; unsupported claims

The extension is compact and connected rather than mere row count: it adds a named registrar's recorded observation and a concrete registry omission/kept carbon, creating a bounded public-record/private-route contrast. The detail is supported by the invented excerpt and leaves the destination blank rather than fabricating a contradictory destination. This offers some narrative depth as an authored micro-bible, but is not independent corroboration, truth, or canon validation. The one notable overreach risk is calling it a “synchronized second perspective” or treating tick 1 as proof of exact shared time; the source supports a second *narrative account of seeing the departure*, not temporal synchronization. No other unsupported claim found in the added rows. The checker cannot detect any of these semantic boundaries.
