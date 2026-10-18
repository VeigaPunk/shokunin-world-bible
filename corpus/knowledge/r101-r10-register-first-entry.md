source: `corpus/fixtures/r94-paired-crossing/{README.md,entities.json,relations.json,sources.json,timeline.json,fictional-excerpts.md}`; `corpus/fixtures/r95-crossing-aftermath/{README.md,relations.json,sources.json,timeline.json,fictional-excerpts.md,contradictions.json}`; `corpus/fixtures/r96-crossing-response/{README.md,relations.json,sources.json,timeline.json,fictional-excerpts.md,contradictions.json}`; `corpus/fixtures/r100-docket-review/fictional-excerpts.md`; `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (R10 row and R10 appendix); `corpus/knowledge/r89-cross-cluster-contradiction.md`; `corpus/knowledge/r93-r8-worked-example.md`; `corpus/knowledge/r95-aftermath-scope-note.md`; `corpus/knowledge/r96-response-scope-note.md`; `corpus/knowledge/r100-crossing-arc-synthesis.md`; `corpus/fixtures/r35-bell7-conflict/{contradictions.json,timeline.json,manual-clause-pointer-map.md}`; `corpus/fixtures/README.md` (Round 35 section); `LOG.md` (r93 closure R10 negative case; round-101 declaration C2)
verified-at: 2026-10-18T00:18-03:00 — read every cited local record this pass from the lane root; re-measured the relation byte-identity across all seven arc snapshots (see Receipts), re-derived the excerpt prefix chain r94⊂r95⊂r96, confirmed both notes' presence in the delivered r100 snapshot, and confirmed `corpus/knowledge/cross-cluster-contradictions.md` does not exist. No external URL was fetched. This is an author-seat worked entry, not an independent admission, not a contradiction finding, and not a canon assertion.
recheck: before integrating any crossing-arc claim, and whenever a cited fixture, note, decision-table row, or the byte-identity chain changes; re-derive the Receipts commands before relying on them, and re-read both notes' whole authored sections rather than the quoted lines alone.
citation-convention: in the record table, bare `file.json#/pointer` references resolve inside the full fixture path named in the same row; all other citations are lane-root-relative paths, and ranges refer to the delivered files. Source IDs are cluster-local: compare path-qualified pairs, never bare IDs (`corpus/knowledge/r88-sourced-inspiration-decision-table.md:99-100`).

# R10 register — first worked entry: an examined NON-conflict at the agreed bell

## Scope and limits

This is the first real exercise of the R10 procedure on a demonstrated shared referent, applied to the crossing arc's two occasion-sharing accounts. It is a worked **non-conflict** record: the examination demonstrates the shared referent, field, and occasion, finds the two assertions compatible, and therefore creates no register entry. The procedure stood unexercised at r93 closure: the finite universe of the then-delivered clusters yielded "zero shared referents or supported conflicts" (`LOG.md:2656-2658`, r93 R10 negative case), and the r89 format demo used an explicitly hypothetical second cluster (`corpus/knowledge/r89-cross-cluster-contradiction.md:5`). Both clusters examined here are landed, present, and byte-preserved in this repository.

The register destination `corpus/knowledge/cross-cluster-contradictions.md` remains uncreated (verified absent this pass), exactly as the R10 appendix requires: "the register's first real entry awaits a genuine conflict" (`corpus/knowledge/r88-sourced-inspiration-decision-table.md:97`). This document is a knowledge record of the examination, not an append to that register.

No canon, testimony-truth, chronology, rights, or training-permission conclusion is drawn anywhere in this entry.

## Procedure applied

The row applied is the delivered R10 row (`corpus/knowledge/r88-sourced-inspiration-decision-table.md:26`): "Before integrating a new cluster, compare overlapping source-attributed claims with relevant landed-cluster claims and confirm a shared referent, field, and occasion." Its register gate admits only supported *incompatible* pairs: "Only a source-backed shared referent, field, and occasion with incompatible assertions enters `corpus/knowledge/cross-cluster-contradictions.md` (status `unresolved`)" (`:93-94`). The entry format it mandates for such pairs — stable ID, both relative cluster paths, both claim pointers, the assertions, the cited in-world sources, the rationale, status — is mirrored below with the outcome inverted and the register fields that presuppose conflict (incompatibility rationale, `unresolved` status) replaced by the compatibility finding. The namespace rule of the r91 decision is applied: source IDs are cluster-local and comparison keys are path-qualified pairs (`:99-100`). The record-and-replay conventions follow the r93 worked-example discipline: scope and limits first, a field-by-field record, a crosswalk from each finding to the exact decision text, replayable receipts, and dated corrections appended without rewriting (`corpus/knowledge/r93-r8-worked-example.md:3-5`, `:26-34`, `:75-79`).

## The record: `r101-crossing-agreed-bell-nonconflict-01`

| Field | Recorded value |
|---|---|
| Stable ID | `r101-crossing-agreed-bell-nonconflict-01` |
| Outcome | Examined NON-conflict. Shared referent demonstrated; shared field and shared occasion identified; the two assertions are COMPATIBLE as stated; no conflict; both claims preserved. No winner, no world-truth assertion, no register entry, no ledger pair. |
| Relative cluster paths | `corpus/fixtures/r95-crossing-aftermath/` (claim A's origin snapshot) and `corpus/fixtures/r96-crossing-response/` (claim B's origin snapshot); shared referent anchored at `corpus/fixtures/r94-paired-crossing/`. All three are declared continuations of one lineage (`r96-crossing-response/README.md:3`), so the path-qualified comparison is within one continuation line, per the namespace rule. |
| Claim A (Aru's account) | `timeline.json#/3` (`aftermath-missing-evin`, tick 11, `entity_id: aru`, `place_id: chalk-stair`, `depends_on: ["paired-crossing-decision"]`, `source_id: aru-aftermath-note`); assertion text at `corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md:26-27` |
| Claim B (Evin's account) | `timeline.json#/4` (`response-evin-salt-court`, tick 12, `entity_id: evin`, `place_id: salt-court`, `depends_on: ["aftermath-missing-evin"]`, `source_id: evin-response-note`); assertion text at `corpus/fixtures/r96-crossing-response/fictional-excerpts.md:37` |
| Cited in-world sources | `sources.json#/3` (`aru-aftermath-note`, id at `corpus/fixtures/r95-crossing-aftermath/sources.json:21`) and `sources.json#/4` (`evin-response-note`, id at `corpus/fixtures/r96-crossing-response/sources.json:27`); shared referent sourced to `sources.json#/2` (`crossing-minute`, id at `corpus/fixtures/r94-paired-crossing/sources.json:15`) |
| Shared referent | Demonstrated — see below |
| Shared field | Performance status of the crossing-scoped agreement at the agreed bell — see below |
| Shared occasion | The agreed bell — see below |
| Compatibility rationale | No assertion in either note contradicts any assertion in the other; both accounts, as accounts, depict the agreed stewardship as not performed at the Chalk Stair during the agreed bell. The register gate's "incompatible assertions" condition (`r88 table:93-94`) is therefore not met. |
| Preservation | Both claims retained byte-exact through the lineage; neither rewritten, reconciled, or superseded. `contradictions.json` remains `[]` in both clusters (verified this pass). |

## The two accounts, quoted exactly

Claim A — Aru's first-person note, `corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md:26-29` (source `aru-aftermath-note`):

> Tick 11: I waited at the Chalk Stair through the agreed bell.
> Evin did not come.
> The agreement we chalked covered this crossing only.
> I assert no other duty, no breach, and no obligation beyond this crossing.

Claim B — Evin's first-person note, `corpus/fixtures/r96-crossing-response/fictional-excerpts.md:37-40` (source `evin-response-note`):

> Tick 12: I was at Salt Court through the same agreed bell.
> I make no accusation against Aru.
> I select no winner between our two accounts.
> Both accounts stand unresolved.

## Referent, field, occasion — demonstrated

**Shared referent (demonstrated).** Both accounts measure performance against the same agreement: the crossing-scoped co-stewardship relation `relations.json#/0` — `{"from": "aru", "to": "evin", "type": "agreed_co_stewardship_for_this_crossing", "source_id": "crossing-minute"}` — byte-identical across all seven arc snapshots r94 through r100 (sha256 prefix `c279254bc7de0636`, 139 bytes each; measured this pass, see Receipts). Its source is the r94 minute (`crossing-minute`, `sources.json#/2`), whose excerpt bounds it: "There, they agreed, for this crossing only, to share stewardship of the Chalk Stair." (`corpus/fixtures/r94-paired-crossing/fictional-excerpts.md:19`). Claim A invokes that same agreement by the participants' own act: "The agreement we chalked covered this crossing only." (`r95 fictional-excerpts.md:28`). Claim B answers claim A on that same occasion without disturbing it; the r96 README records that the tick-12 event "records only Evin's second account of the same occasion" (`corpus/fixtures/r96-crossing-response/README.md:9`). The referent is one path-qualified record carried unchanged, not two similarly named records: per the r100 dossier, "The reviewed relation is still the one crossing-only agreement sourced to `crossing-minute`" (`corpus/knowledge/r100-crossing-arc-synthesis.md:46`).

**Shared field (identified).** The field both assertions bear on is the *performance status* of that agreement at the agreed bell — whether Evin came to the Chalk Stair to share the stewardship during that bell. Claim A asserts Evin's non-arrival ("Evin did not come." — `r95 fictional-excerpts.md:27`); claim B asserts Evin's own presence at Salt Court through the same bell (`r96 fictional-excerpts.md:37`). This is a semantic field of the two authored accounts, not a JSON field: unlike the r35 precedent, where the compared field was literally `place_id` on two events, no ledger pair is created here, because the R10 register gate admits only incompatible assertions and this field receives none. The accounts also name different actors at different places, so they are not two values of one occupancy field (`corpus/knowledge/r96-response-scope-note.md:31`).

**Shared occasion (identified).** The occasion is the agreed bell — the bell of the crossing whose stewardship the r94 minute's agreement scopes. The two notes reference it by the same phrase: claim A's "the agreed bell" (`r95 fictional-excerpts.md:26`) and claim B's "the same agreed bell" (`r96 fictional-excerpts.md:37`) — Evin's "the same" ties his bell to the one Aru named, and both notes anchor it to the chalked agreement ("The agreement we chalked", `r95:28`; the relation's source `crossing-minute`). The demonstration rests on this common reference to one recorded agreement, **not** on tick equality: the integer ticks are editorial encodings, not literal JSON wording in the sources (`corpus/fixtures/r94-paired-crossing/README.md:11`), and the minute itself names only the two ninth-bell entries and the tick-10 meeting (`corpus/fixtures/r94-paired-crossing/fictional-excerpts.md:20`), so "the agreed bell" as a performance occasion is carried by the two notes' shared reference, which is what the examination records.

## Examination outcome: COMPATIBLE — no conflict

Comparing the assertions under the demonstrated referent, field, and occasion:

- Claim A asserts that Evin did not come to the Chalk Stair during the agreed bell.
- Claim B asserts that Evin was at Salt Court through that same bell.
- Nothing in claim B asserts an arrival at the Chalk Stair, and nothing in claim A asserts where Evin was instead. No assertion in either note is incompatible with any assertion in the other. As accounts, both depict the agreed stewardship as not performed at the Chalk Stair during the agreed bell; neither note accuses, selects a winner, or declares the other false (`r96 fictional-excerpts.md:38-40`).

The register gate therefore fails on its final condition: the pair has a source-backed shared referent, field, and occasion, but the assertions are compatible, and "only a source-backed shared referent, field, and occasion with incompatible assertions enters" the register (`corpus/knowledge/r88-sourced-inspiration-decision-table.md:93-94`). Consequences, all verified this pass:

1. No entry is created in `corpus/knowledge/cross-cluster-contradictions.md`; the file does not exist and stays uncreated (`:97`: "the register's first real entry awaits a genuine conflict").
2. No `contradictions.json` pair is added in either cluster; both remain `[]` (`r95` and `r96`, verified this pass), consistent with the r90 rule that unresolved *identity/occasion candidates* go to comparison records and `l0-questions.md`, not the live register (`:93`) — and here no candidate discrepancy survives at all.
3. Register status `unresolved` is not used: there is no conflict to hold unresolved. Testimony-level non-adjudication is preserved separately — neither account is declared true, false, or corroborated.

## Verdict

Examined. Shared referent demonstrated (one byte-identical crossing-scoped agreement relation across the lineage); shared field identified (performance status of that agreement at the agreed bell); shared occasion identified (the agreed bell, by the two notes' common reference to the one recorded agreement). Outcome: the claims are COMPATIBLE — a demonstrated NON-conflict. No conflict exists; both claims are preserved unrewritten; no winner is selected; no world truth is asserted about whether Evin came to the Chalk Stair, whether non-performance occurred, or whether either account is accurate. The register gains its first real exercise without gaining a first entry.

## Non-establishment bounds

- **No testimony truth.** Compatibility is a relation between two authored accounts, not corroboration and not a world finding. This entry does not establish that Evin was at Salt Court, that Evin did not come to the Chalk Stair, that non-performance occurred, or that either source is authentic. Both accounts stand non-adjudicated, per their own closing lines and the arc invariant (`corpus/knowledge/r100-crossing-arc-synthesis.md:10`, `:54`).
- **No chronology authentication.** "The agreed bell" is a phrase in the two notes, not an authenticated time; ticks 9–12 and the `depends_on` edges are editorial encodings (`r94 README.md:11`). Tick equality or adjacency is nowhere used as identity or occasion evidence.
- **No expansion of duty.** The referent agreement is crossing-scoped ("for this crossing only", `r94 fictional-excerpts.md:19`). Neither account converts it into a standing duty, and the reported non-arrival asserts no breach (`r95 fictional-excerpts.md:29`; `corpus/fixtures/r95-crossing-aftermath/README.md:11`). This entry adds no duty, breach, fault, or alliance finding.
- **Namespace scoping.** The compared source IDs `(r95-crossing-aftermath, aru-aftermath-note)` and `(r96-crossing-response, evin-response-note)` are path-qualified pairs (`r88 table:99-100`); no ID collision arises, and a collision would have triggered the namespace check before any referent comparison, never the register.
- **Checker limits.** No gate result is cited as cross-cluster evidence: the R10 row itself says "cross-cluster comparison and register-reference checks are an explicit manual integration gate" and "a per-cluster `CLEAN` is not cross-cluster evidence" (`r88 table:26`); the integration boundary adds that "R10's proposed corpus-level register is a manual procedure until a corpus-wide validator exists. Do not mark any of those surfaces mechanically verified solely from a clean fixture replay." (`:110`). The receipts below measure bytes and pointers only.
- **No canon, rights, or training-permission conclusion.** This entry is an editorial comparison record; it settles nothing about canon and grants no permission.

## Precedent cross-references

- **r100 six-beat dossier** (`corpus/knowledge/r100-crossing-arc-synthesis.md`). The dossier's docket (`:32-38`) places claim A at beat 1 (r95) and claim B at beat 2 (r96) of the six-beat arc after the r94 minute seed, under the unresolved-throughout invariant (`:10`, `:48`). Its occupancy observation anticipates this outcome: "Aru's account places Aru at the Chalk Stair; Evin's account places Evin at Salt Court. Different actors at different places do not, by themselves, assert one actor's incompatible occupancy, and this arc files no contradiction between them." (`:50`). This entry re-derives that outcome through the R10 row's own referent/field/occasion gate rather than asserting it, and adds what the dossier does not record: the byte-identity receipt for the shared referent across all seven snapshots and the explicit register-gate finding.
- **r35 two-sided-preservation precedent** (`corpus/fixtures/r35-bell7-conflict/`). The r35 fixture preserves two reports of one named ringing as an editorial ledger pair (`contradictions.json#/0`, `bell7-location-reports`, field `place_id` on `timeline.json#/2-3`) with both accounts retained unresolved and "Neither wins." (`corpus/fixtures/README.md:761`; map limits at `manual-clause-pointer-map.md:3`, `:21`). The same preservation discipline is applied here with the opposite gate outcome: r35's `why` states its incompatibility conditionally on identity/place/occasion assumptions and so records an apparent conflict; this examination's conditionally-stated incompatibility does not arise, so no ledger row exists and preservation is carried by the byte-identical lineage instead. The two records are different classes, as the r96 scope note already distinguishes (`corpus/knowledge/r96-response-scope-note.md:13`, `:40`).

## Receipts (measured 2026-10-18T00:18-03:00, from the lane root)

Relation byte-identity across the arc (command and observed output, abbreviated to the hash prefix):

```sh
python3 - <<'PY'
import hashlib, json
from pathlib import Path
for fx in ["r94-paired-crossing","r95-crossing-aftermath","r96-crossing-response","r97-crossing-acknowledgment","r98-clerk-filing","r99-window-lapse","r100-docket-review"]:
    b = Path(f"corpus/fixtures/{fx}/relations.json").read_bytes()
    print(fx, hashlib.sha256(b).hexdigest()[:16], len(b))
PY
```

```text
r94-paired-crossing c279254bc7de0636 139
r95-crossing-aftermath c279254bc7de0636 139
r96-crossing-response c279254bc7de0636 139
r97-crossing-acknowledgment c279254bc7de0636 139
r98-clerk-filing c279254bc7de0636 139
r99-window-lapse c279254bc7de0636 139
r100-docket-review c279254bc7de0636 139
```

`relations.json#/0` parsed value: `{"from": "aru", "to": "evin", "type": "agreed_co_stewardship_for_this_crossing", "source_id": "crossing-minute"}`. Claim pointers verified by parsing: `r95 timeline.json#/3` = `aftermath-missing-evin` (tick 11, aru, chalk-stair, `["paired-crossing-decision"]`, `aru-aftermath-note`); `r96 timeline.json#/4` = `response-evin-salt-court` (tick 12, evin, salt-court, `["aftermath-missing-evin"]`, `evin-response-note`). Excerpt prefix chain: `r95 fictional-excerpts.md` starts with the complete `r94` file (`True`), `r96` starts with the complete `r95` file (`True`), and both quoted note sections are present in `corpus/fixtures/r100-docket-review/fictional-excerpts.md` at lines 26 and 37. `contradictions.json` is `[]` in both compared clusters. `corpus/knowledge/cross-cluster-contradictions.md` is absent (`ls` → "No such file or directory").

One recorded variance, not silently normalized: the r90 appendix asks compared-but-dismissed overlaps to be recorded in the incoming cluster README under `## R10 comparison outcomes` (`r88 table:90-92`); the three arc READMEs instead carry their comparison records under the heading `## Namespace and occasion comparison` (`corpus/fixtures/r94-paired-crossing/README.md:5`, `r95:5`, `r96:5`). This entry is filed as the durable record of the examined pair; no README is edited from this seat.

## Limits of this record

This is an author-seat knowledge record, not independent verification, admission, or a non-author review. It extends only to the cited paths and does not authenticate any fictional source, adjudicate any character, or decide truth, breach, chronology, rights, or permission. Both compared fixtures are declared continuations of one lineage (`r96-crossing-response/README.md:3`); source IDs remain cluster-local and path-qualified comparison is not identity evidence beyond what the byte receipts above show. The r89 demo remains the format example; this document does not append to any register. Rights and AI-training permission remain unassessed.
