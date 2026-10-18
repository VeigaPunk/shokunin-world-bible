# r87 mythology cluster: claim-to-excerpt map

Scope: 14 JSON facts from S2's r89 map (6 entity claims, 4 relations, 4 timeline events) plus 8 editorial Low-Water Hymn readings, for 22 mapped rows total. The hymn readings are not JSON facts. Each excerpt declaration and row repeats its R9 delivery mode; anchors are lexical preflight only, so the whole claim and attribution must still be reviewed.

## Inventory

**Expected inventory:** 14 JSON facts; 8 editorial rows; 22 total mapped rows; 22 distinct excerpt anchors.

## R9 excerpt declarations

| Excerpt | In-world source | Delivery mode | Status |
|---|---|---|---|
| `gate-witness-excerpt.md` | `gate-witness` | `verbatim` | Newly authored fictional, unverified witness account. |
| `dune-register-excerpt.md` | `dune-register` | `verbatim` | Newly authored fictional, unverified register. |
| `shell-charter-excerpt.md` | `shell-charter` | `verbatim` | Newly authored fictional charter; pledge, not proof of performance. |
| `tide-bell-tally-excerpt.md` | `tide-bell-tally` | `verbatim` | Newly authored fictional tally; ordering is fixture-local. |
| `lowwater-hymn-excerpt.md` | `lowwater-hymn` | `verbatim` | Newly authored fictional verse; imagery is not an objective account. |

`verbatim` describes the delivered wording of these invented in-world texts; it is not a claim that they are historical documents, authenticated testimony, or external-source quotations. The named ETCSL parallel remains `external-only / unverified inspiration`: its cited passage is not delivered and supports none of these in-world claims.

## JSON facts (14; from S2's r89 map)

| Row | JSON fact and fields | `source_id` | Excerpt path:line | R9 mode | Exact anchor |
|---|---|---|---|---|---|
| E1 | `entities[0].claims[0].statement`, `entities[0].claims[0].source_id`, co-map `entities[0].first_appearance`: “Hara identifies herself as the keeper of the Mother-Tide Gate in her witness slip.” | `gate-witness` | `gate-witness-excerpt.md:7` | `verbatim` | `I am Hara, keeper of the Mother-Tide Gate` |
| E2 | `entities[1].claims[0].statement`, `entities[1].claims[0].source_id`, co-map `entities[1].first_appearance`: “Sen identifies himself as a recorder at Ash-Dune Sanctuary in the register.” | `dune-register` | `dune-register-excerpt.md:7` | `verbatim` | `I, Sen, serve as recorder at Ash-Dune Sanctuary` |
| E3 | `entities[3].claims[0].statement`, `entities[3].claims[0].source_id`, co-map `entities[3].first_appearance`: “Sen's register names Ash-Dune Sanctuary as a record-keeping place.” | `dune-register` | `dune-register-excerpt.md:8` | `verbatim` | `Ash-Dune Sanctuary is a record-keeping place` |
| E4 | `entities[4].claims[0].statement`, `entities[4].claims[0].source_id`, co-map `entities[4].first_appearance`: “The charter names the Shellweavers as one signatory faction.” | `shell-charter` | `shell-charter-excerpt.md:9` | `verbatim` | `Shellweavers signed this charter as a signatory faction` |
| E5 | `entities[5].claims[0].statement`, `entities[5].claims[0].source_id`, co-map `entities[5].first_appearance`: “The charter names the Reedwardens as one signatory faction.” | `shell-charter` | `shell-charter-excerpt.md:10` | `verbatim` | `Reedwardens signed this charter as a signatory faction` |
| E6 | `entities[6].claims[0].statement`, `entities[6].claims[0].source_id`, co-map `entities[6].first_appearance`: “The watch tally records a reed bell being carried for the low-water signal.” | `tide-bell-tally` | `tide-bell-tally-excerpt.md:11` | `verbatim` | `We carried the Reed Bell for the low-water signal` |
| R1 | `relations[0].from`, `relations[0].to`, `relations[0].type`, `relations[0].source_id`: “Shellweavers are allied with Reedwardens.” | `shell-charter` | `shell-charter-excerpt.md:11` | `verbatim` | `By this charter, Shellweavers stand allied with Reedwardens` |
| R2 | `relations[1].from`, `relations[1].to`, `relations[1].type`, `relations[1].source_id`: “Reedwardens are allied with Shellweavers.” | `shell-charter` | `shell-charter-excerpt.md:12` | `verbatim` | `By this charter, Reedwardens stand allied with Shellweavers` |
| R3 | `relations[2].from`, `relations[2].to`, `relations[2].type`, `relations[2].source_id`: “Shellweavers keep watch with Reed Bell.” | `shell-charter` | `shell-charter-excerpt.md:13` | `verbatim` | `Under this charter's pledge, Shellweavers keep watch with the Reed Bell` |
| R4 | `relations[3].from`, `relations[3].to`, `relations[3].type`, `relations[3].source_id`: “Sen records at Ash-Dune Sanctuary.” | `dune-register` | `dune-register-excerpt.md:9` | `verbatim` | `At Ash-Dune Sanctuary, Sen kept the register` |
| T1 | `timeline[0].description`, `timeline[0].source_id`: “Hara's witness slip reports that she sounded the Reed Bell at the Mother-Tide Gate before the Moon-Basin Vow.” | `gate-witness` | `gate-witness-excerpt.md:8` | `verbatim` | `I sounded the Reed Bell at the Mother-Tide Gate before the Moon-Basin Vow` |
| T2 | `timeline[1].description`, `timeline[1].source_id`: “Sen's tally records the return of the first low-water signal before the Moon-Basin Vow.” | `tide-bell-tally` | `tide-bell-tally-excerpt.md:12` | `verbatim` | `At Ash-Dune Sanctuary, Sen's tally records the return of the first low-water signal before the Moon-Basin Vow` |
| T3 | `timeline[2].description`, `timeline[2].source_id`: “Hara's slip places the single Moon-Basin Vow of Saltmonth 4 at the Mother-Tide Gate during the first low-water bell.” | `gate-witness` | `gate-witness-excerpt.md:9` | `verbatim` | `I record the single Moon-Basin Vow of Saltmonth 4 at the Mother-Tide Gate during the first low-water bell` |
| T4 | `timeline[3].description`, `timeline[3].source_id`: “Sen's register places that same single Moon-Basin Vow of Saltmonth 4 at Ash-Dune Sanctuary during the first low-water bell.” | `dune-register` | `dune-register-excerpt.md:10` | `verbatim` | `I record that same single Moon-Basin Vow of Saltmonth 4 at Ash-Dune Sanctuary during the first low-water bell` |

## Editorial rows (8 Low-Water Hymn clauses; not JSON facts)

These rows map the interpretive readings in `symbolism-clause-map.md`; they are not extra JSON canon claims. The excerpt supplies the quoted words, while each reading remains editorial and bounded by that map's stated limit.

| ID | Clause reading | Source | Excerpt path:line | R9 mode | Exact anchor |
|---|---|---|---|---|---|
| H1 | Low water: a moment of exposure or transition in the poem | `lowwater-hymn` | `lowwater-hymn-excerpt.md:5` | `verbatim` | `At low water` |
| H2 | The shell ring: a possible image of a collectively made boundary | `lowwater-hymn` | `lowwater-hymn-excerpt.md:5` | `verbatim` | `the shell ring` |
| H3 | The bowl: a possible place for shared attention | `lowwater-hymn` | `lowwater-hymn-excerpt.md:5` | `verbatim` | `beside the bowl` |
| H4 | The Mother-Tide Gate: a named place-setting for the verse's actions | `lowwater-hymn` | `lowwater-hymn-excerpt.md:5` | `verbatim` | `at the Mother-Tide Gate` |
| H5 | The bowl keeps no name: a reading of withheld or unclaimed identity | `lowwater-hymn` | `lowwater-hymn-excerpt.md:6` | `verbatim` | `The bowl keeps no name` |
| H6 | No voice owns the tide: a possible refusal of exclusive control over a recurring force | `lowwater-hymn` | `lowwater-hymn-excerpt.md:6` | `verbatim` | `no voice owns the tide` |
| H7 | Passing the reed-bell hand to hand: a possible image of shared responsibility | `lowwater-hymn` | `lowwater-hymn-excerpt.md:7` | `verbatim` | `pass the reed-bell hand to hand` |
| H8 | Letting the water return it: a possible image of release or renewal | `lowwater-hymn` | `lowwater-hymn-excerpt.md:7` | `verbatim` | `let the water return it` |

## Scope and review notes

- **R3 pledge scope:** the charter source record says it records a reciprocal pledge, not whether either faction kept it. R3's anchor supports only the pledged/assigned duty; it does not establish performance. Do not silently read `keeps_watch_with` as proof of completed watch.
- **T3/T4:** Hara's gate slip and Sen's register give incompatible locations for the same single Saltmonth 4 vow during the first low-water bell. Preserve both cited accounts as unresolved; neither excerpt refutes the other or selects canon.
- **Hymn limits:** the eight readings are interpretive, not new canon. The shell ring is not a legal seal or alliance; the bowl has no asserted entity identity; the verse does not prove joint Bell handling, supernatural return, or an objective event.
- **Full D1 crosswalk:** S2's 14 rows co-map six `first_appearance` pointers. The remaining pointer, `entities[2].first_appearance=lowwater-hymn`, resolves to the verse and is anchored at H4's line 5. The additional existing JSON claim `entities[2].claims[0]` (“The Low-Water Hymn places the shell ring and bowl at the Mother-Tide Gate.”) is also co-mapped to H4's line 5; it is not a fifteenth row in the task's 14-fact S2 set or a ninth hymn clause. This makes the 22-row task scope explicit without hiding the wider D1 crosswalk.
- `check_bible.py` validates JSON structure and source-ID resolution only; neither its `CLEAN` result nor an anchor match establishes prose fidelity, source authenticity, truth, or canon.
