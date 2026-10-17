# R93 M2 claim-to-excerpt map

Scope: all source-attributed JSON pointers in this cluster plus the three bounded Kojiki comparison clauses. Each row repeats the R9 delivery mode and an exact anchor. The translation rows are editorial comparisons only, not source support for fictional canon.

**Expected inventory:** 12 JSON facts; 3 editorial rows; 15 total mapped rows; 15 distinct excerpt anchors.

## R9 excerpt declarations

| Excerpt path and lines | Source | Delivery mode | Status |
|---|---|---|---|
| `archive-record-excerpt.md:5-12` | `m2-record-archive` | `verbatim` | Newly authored fictional in-world register. |
| `kojiki-chamberlain-excerpt.md:8-10` | Chamberlain translation of *The Kojiki* | `translation` | External editorial comparison only; no R5 JSON support is claimed. |

`verbatim` describes the delivered wording of the invented in-world register. `translation` describes Chamberlain's English rendering, not the source-language text. Fixed-string matches are lexical preflight only.

## JSON facts (12 source-attributed pointers)

| ID | JSON fact pointer and fields | In-world source ID | Excerpt path | R9 delivery mode | Exact anchor |
|---|---|---|---|---|---|
| E1 | `entities.json#/0/first_appearance` (`teva`) | `m2-record-archive` | `archive-record-excerpt.md:5` | `verbatim` | `M-17 identifies Teva as the initial recorder` |
| E2 | `entities.json#/0/claims/0` (`statement`, `source_id`) | `m2-record-archive` | `archive-record-excerpt.md:6` | `verbatim` | `Teva names the paper folio "Lorn Index" as the sheet she opened for the check.` |
| E3 | `entities.json#/1/first_appearance` (`orni`) | `m2-record-archive` | `archive-record-excerpt.md:7` | `verbatim` | `Orni writes on the margin: "not weighed; mark unmeasured."` |
| E4 | `entities.json#/1/claims/0` (`statement`, `source_id`) | `m2-record-archive` | `archive-record-excerpt.md:8` | `verbatim` | `The folio identifies Teva and Orni as its two annotators.` |
| E5 | `entities.json#/2/first_appearance` (`slate-table`) | `m2-record-archive` | `archive-record-excerpt.md:5` | `verbatim` | `Slate Table as its filing place` |
| E6 | `entities.json#/2/claims/0` (`statement`, `source_id`) | `m2-record-archive` | `archive-record-excerpt.md:9` | `verbatim` | `The inventory lists the Slate Table as the place holding the folio.` |
| E7 | `entities.json#/3/first_appearance` (`lorn-index`) | `m2-record-archive` | `archive-record-excerpt.md:6` | `verbatim` | `paper folio "Lorn Index"` |
| E8 | `entities.json#/3/claims/0` (`statement`, `source_id`) | `m2-record-archive` | `archive-record-excerpt.md:12` | `verbatim` | `The register gives no measured weight for the Lorn Index.` |
| E9 | `relations.json#/0` (`from`, `to`, `type`, `source_id`) | `m2-record-archive` | `archive-record-excerpt.md:10` | `verbatim` | `Teva files the Lorn Index on the Slate Table.` |
| E10 | `relations.json#/1` (`from`, `to`, `type`, `source_id`) | `m2-record-archive` | `archive-record-excerpt.md:11` | `verbatim` | `Orni adds "not weighed; mark unmeasured" to the Lorn Index at the Slate Table.` |
| E11 | `timeline.json#/0` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `m2-record-archive` | `archive-record-excerpt.md:10` | `verbatim` | `Entry A: Teva files the Lorn Index on the Slate Table.` |
| E12 | `timeline.json#/1` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `m2-record-archive` | `archive-record-excerpt.md:11` | `verbatim` | `Entry B: after Entry A, Orni adds "not weighed; mark unmeasured" to the Lorn Index at the Slate Table.` |

## Editorial rows (3 external comparisons; not JSON facts)

| ID | Bounded source clause / editorial comparison | Source excerpt path | R9 delivery mode | Exact anchor |
|---|---|---|---|---|
| S1 | The named passage says eternal night prevails; the comparison asks how a record marks an unknown field. | `kojiki-chamberlain-excerpt.md:8` | `translation` | `eternal night prevailed` |
| S2 | The named passage says the deities assemble; the comparison is only to separately attributed marks on one fictional folio. | `kojiki-chamberlain-excerpt.md:9` | `translation` | `eight hundred myriad deities assemble in a divine assembly` |
| S3 | The named passage says the lands again become light; the comparison is only to making the record's unknown measurement explicit. | `kojiki-chamberlain-excerpt.md:10` | `translation` | `again became light` |

These editorial rows do not make the Kojiki translation an in-world source, establish cultural meaning, or support any fictional JSON fact. The checker reports their lexical anchors separately as `EDITORIAL-ANCHORS`; its result is not a non-submitter R9 manual review.
