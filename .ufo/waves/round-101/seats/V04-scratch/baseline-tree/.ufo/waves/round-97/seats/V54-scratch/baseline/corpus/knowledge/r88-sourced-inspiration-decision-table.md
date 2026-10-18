<!-- SCOPE (R1B): the support rule covers EVERY source-attributed in-world JSON fact —
     entity claims and first-appearance pointers, relation edges, timeline events, and
     equivalent records. Original form:: the support rule below covers EVERY source-attributed in-world JSON fact — entity claims and first-appearance pointers, relation edges, timeline events, and equivalent records. -->

# Sourced-inspiration decision table — round 88


This table governs how real-world inspiration is cited and how sourced claims are kept distinct from in-world canon. A reference-ledger entry records research provenance; it is not an in-world `sources.json` record, a license, or proof that a fictional claim is true.

| Decision | Rule / output | Attribution | Rights status | AI-training permission | evidence and integration check |
|---|---|---|---|---|---|
| A real-world work, tradition, or specific historical/mythological claim materially informs an element, or the work is named as a parallel | A citation is required. Identify the specific work/source and the parallel being drawn; use a passage-level locator when the comparison depends on a particular passage. Do not describe a resemblance as a sourced relationship if no source was used. | Identify only the creator, institution, work, edition, or source page supported by the evidence; do not invent an individual author. If the attribution itself is uncertain, write `Open question — ...`. | `Open question — not assessed; no rights grant asserted` is the default. A resolved value must state the status, the exact work/edition or expression it covers, and its evidence. | `Open question — not assessed; no permission inferred` is the default. `Permitted` or `prohibited` requires explicit terms or permission evidence and its scope. | r87 and M1/M2/M3 all cite named real-world works. M1 bounds the comparison to a translated Kojiki passage, M2 to a Völuspá image, and M3 to Spence's English summary. Recheck the selected cluster and ledger at integration. |
| No particular outside source materially informs the element and no real-world lineage is asserted | Citation is optional. Keep the element identified as original or as a general motif; do not imply a specific tradition, work, or factual basis. This row does not excuse omitting a source that actually informed the work. | `Not applicable — no sourced parallel asserted`; if a source is later identified, use the required row above. | `Not applicable — no reference recorded`; do not use this value to imply rights clearance for a source that was used. | `Not applicable — no reference recorded`; do not use this value to imply training permission. | None of r87 or M1/M2/M3 exercises this optional case; each names a specific source. Recheck any integration claim relying on a general-motif exception. |
| A citation field is not yet known or verified | Never leave a mandatory field blank. Record the open question and what evidence is needed; do not turn uncertainty into a positive claim. Resolve only when a source supports the resolution. | `Open question — attribution / edition not established: [what remains to verify]`. | `Open question — rights status not assessed: [what remains to verify]`. Public access or the age of an underlying work does not determine the rights in a modern edition, translation, or presentation. | `Open question — training permission not assessed: [what remains to verify]`. Attribution, public access, and a rights conclusion do not imply AI-training permission. | r87, M1, M2, and M3 keep rights and training permission open. M1 labels its attribution question open while naming the selected work, translator, and edition; M2/M3 separately identify their cited editions. Recheck field presence and independence in the selected cluster at integration. |
| A passage-specific parallel or claim is used | Supply both (1) a passage-level locator (work/title, edition or version, stable URL or identifier, and page/section/line span as available) and (2) the relevant source text in the delivered corpus, to the extent permitted by applicable terms. An external-only link is not delivered evidence: mark the passage `external-only / unverified` and do not rely on it to substantiate a specific claim. Do not reproduce text beyond the permitted scope; if text cannot be delivered, retain the citation as a research lead, not as verified support. | Keep the source attribution for the exact cited edition/page; do not infer an ancient author from a modern host or translation. | Keep rights status scoped to the text actually delivered (including edition/translation), not just the underlying work. If unclear, leave open. | State only what explicit terms or permission establish; if unclear, leave open. | r87's ETCSL note gives `lines 122–163` but delivers no ETCSL text. M1's Kojiki note and M2's Völuspá note each supply an excerpt and locator; M1's README locator check reports six passage locators resolving to four delivered lines. M3 supplies a page-209 Spence excerpt. Recheck the selected citation's locator and delivered text at integration. |
| An in-world claim is attributed to a delivered excerpt | Resolve its `source_id` to the in-world source record and map the claim to the exact delivered excerpt path and line span. For every claim, record a distinctive exact phrase or named anchor, then run a fixed-string, line-numbered search such as `grep -nF -- 'anchor phrase' <excerpt-path>`; a missing excerpt or zero match fails. A match is only a lexical preflight—also review that the passage supports the whole claim, not merely one word. A metadata-only source ID or clean JSON/schema check is not prose verification. | Real-world attribution stays in the reference ledger; an in-world `source_id` does not substitute for it. | No rights conclusion follows from a fictional source ID. | No training-permission conclusion follows from a fictional source ID. | **OBS-1 (repaired at r88 closure):** r87's `entities.json:33` hymn attribution was unsupported at r87; M4's excerpt patch (landed `2ea9ef1`) adds the Gate to the verse and matches 8/8 map clauses; M4's repoint patch cites `gate-witness` metadata but delivers no witness excerpt. M3 supplies paired-register prose and its named anchors; its external source clauses also resolve in a delivered excerpt. M1 has no in-world source excerpts, and M2's only in-world excerpt is the hush song while its JSON claims cite `lantern-compact`, `root-wick-slip`, and `salt-window-record`. Those metadata-only JSON claims are not auditable under this text-support rule; this is an evidence gap, not a claim that the JSON checker fails. Recheck the selected cluster's claim-to-excerpt map at integration. |
| A real-world reference is used | Register one Markdown row in `corpus/knowledge/reference-ledger.md`, even when one or more questions remain open. Use the existing four-column header: Work / attribution; Rights question; AI-training permission question; Use here. Keep the three questions in separate cells; use the final cell to state the limited purpose and passage/element, and whether text is delivered or external-only. `seed.md:26–29` requires separate questions but does not define row syntax; the current ledger supplies the four-column format. | Populate the first ledger cell with the supported work/source attribution, or an explicit open question. | Populate the second cell with a scoped status or explicit open question; never merge with attribution. | Populate the third cell with explicit permission/prohibition evidence or an explicit open question; never infer from the second cell. | Baseline ledger had three method rows and no ETCSL/Inana row. Landed: the ETCSL row (D3) at `2ea9ef1` and the Spence row at r88 closure; both keep the three questions in separate cells. M1/M2 references (Kojiki, Völuspá) were not landed and are not registered. |
| Inspired content conflicts with another in-world account | Preserve both source-cited accounts and record the contradiction (where applicable, with distinct claim pointers and a `why`); do not silently select, reconcile, or rewrite canon. A real-world parallel cannot adjudicate an in-world dispute. Any later editorial resolution needs a separate, explicit decision and its own source/evidence. | Do not recast an external parallel as an in-world witness. | A rights conclusion cannot decide fictional canon. | Training permission cannot decide fictional canon. | r87 reports Hara's gate account versus Sen's dune account without resolution; M2 reports two Hush Lantern first-light locations without selecting one. M1 and M3 have empty contradiction arrays, so they do not exercise the conflict branch. Recheck any selected-cluster disagreement at integration. |

`corpus/fixtures/check_bible.py` validates JSON structure, source-ID resolution, relations, and timeline rules; it does not read inspiration notes, excerpts, or symbolism maps. Its `CLEAN` result is not evidence that prose claims are supported. The r87 replay returned `CLEAN: schema, citations, relations, timeline; 0 violations` while OBS-1 remained undetected.

| Decision | Rule / output | Attribution | Rights status | AI-training permission | Evidence and integration check |
|---|---|---|---|---|---|
| R8 — A named source informed an element, but its text cannot be delivered | Decide R1 versus R2 from recorded provenance, not resemblance alone. Use a contemporaneous, non-expressive provenance note to record the source and locator, the element/aspect affected, and how consulting it changed the design; that establishes actual use, not the passage's contents. Screen materiality by stating whether the element depends on a source-specific claim, distinctive expression, sequence, or combination of details, rather than only a broad idea or general motif, and what remains if that dependency is removed. No source was consulted and no specific real-world lineage is asserted: R2 may apply. If a work is named as a parallel, keep R1's citation requirement even when it did not inform the element. A recorded source-use or unresolved influence question is not R2; keep it open. This is an editorial screen, not a legal conclusion. If only a general motif is recorded and no distinctive expression carries through, the element may remain as newly authored fiction, but mark the affected element in the note/map `external-only / unverified inspiration` and state in the ledger `Use here` that the text is not delivered; do not claim source-text support and require independent in-world support for each canon claim. If distinctive expression/sequence informed the element, or the screen is unresolved, withhold it from supported canon until it is re-derived without that dependency or a permitted text and review establish an appropriate basis. Record the decision and rationale in the inspiration note and element map and in the ledger `Use here`; do not merge attribution, rights, or training permission. **Owner:** the lore lane applies this row at integration; unresolved disputes are appended to `l0-questions.md` for the operator — the row is an editorial screen, never a rights or canon determination.| Identify the source and the consulted edition/version if known; record the author's influence statement separately from a verified passage claim. Do not infer that non-delivery means no source was used. | Keep `not assessed` unless evidence establishes status for the specific work/expression. This row makes no legal finding or rights grant. | Keep separately open unless explicit terms establish permission; neither attribution nor a materiality screen implies training permission. | JDEP3's S1 identifies ETCSL lines 122–163 as cited but undelivered and finds citation coverage without element disposition (`.ufo/waves/round-88/followup/JDEP3.md:21-38`; `JDEP3-probes.json`, `S1-rights-blocked-source`). Baseline probe: locator present, `source-excerpt.md` absent; the R8 terms scanned 0 times. Recheck the chosen element, influence note, and ledger row at integration. |
| R9 — An in-world claim is mapped to a delivered excerpt | Declare one delivery mode for each excerpt and repeat it in each claim-to-excerpt map entry: `verbatim`, `translation`, `paraphrase`, or `summary`. Identify the excerpt path and line span; identify the translator/version for a translation and the author/editor for a paraphrase or summary when known. Only delivered source words, or an identified translation tied to a named source text/version, may carry R5 source-claim support; a translation is the translator's rendering, not the source's exact wording. A paraphrase or summary is not the source's own text and cannot by itself establish source-text support; a fixed-string anchor found only there is not an R5 source anchor. Anchor a source-attributed claim in the eligible delivered source words or identified translation. If only a paraphrase/summary is available, label the underlying source text `not delivered / unverified`; the delivered representation supports only the existence of that retelling, not a claim about the source's own wording. Deliver the underlying text for a separate support review only when permitted; otherwise keep it as a research lead, or describe the claim as a secondary retelling and cite its actual intermediary. A fixed-string anchor proves only that the phrase occurs in the delivered representation; it does not establish delivery mode or fidelity. **Owner:** the lore lane applies this row at integration; unresolved disputes are appended to `l0-questions.md` for the operator — the row is an editorial screen, never a rights or canon determination.| Attribute the representation to the source only for a verbatim text or an identified translation; attribute editorial paraphrase/summary to its actual author or intermediary, without presenting it as a quotation. | Assess rights for the delivered expression and edition/translation separately; do not infer clearance from the mode label. | Assess permission separately for the delivered expression; no mode implies permission. | JDEP3 S2 shows a self-consistent paraphrase passing R5's anchor (`JDEP3.md:40-56`; `JDEP3-probes.json`, `S2-paraphrased-in-world-excerpt`). Independent replay used identical valid JSON with paraphrase vs verbatim excerpt: both checker runs were `CLEAN`, exit 0, and both anchor checks matched. At integration, require the mode in both excerpt and map, then replay the durable R9 fixture and inspect the underlying text/translation where applicable. For every translation-backed R5 claim, require the separate per-claim R9 manual-review record; the support command's `RESULT PASS`/`SOURCE-SUPPORT` is lexical preflight only and is not that receipt. |
| R10 — An inspired account conflicts with an account in another landed cluster | Before integrating a new cluster, compare overlapping source-attributed claims with relevant landed-cluster claims and confirm a shared referent, field, and occasion. If identity or occasion is unestablished, record a candidate discrepancy and missing evidence, not a confirmed contradiction. For each supported incompatible pair, add a durable entry to `corpus/knowledge/cross-cluster-contradictions.md` containing a stable ID, both relative cluster paths, both claim pointers (file plus event/entity ID and field or claim index), the conflicting assertions, the cited in-world sources, why they cannot both be true as stated, and status `unresolved`. Preserve both clusters and their claims; do not silently select, reconcile, or rewrite either. A real-world parallel cannot adjudicate the in-world disagreement. Keep `contradictions.json` for references the local fixture checker can resolve; do not represent a foreign-cluster pointer as locally validated. Until a corpus-wide checker exists, cross-cluster comparison and register-reference checks are an explicit manual integration gate. Any later editorial resolution must be a separate, sourced decision that retains the original conflict record. **Owner:** the lore lane applies this row at integration; unresolved disputes are appended to `l0-questions.md` for the operator — the row is an editorial screen, never a rights or canon determination.| Cite the source for each in-world account; keep any real-world parallel in the reference ledger, not as an in-world witness or tie-breaker. | A rights conclusion cannot settle canon. | Training permission cannot settle canon. | JDEP3 S3 records the single-directory CLI limit and no cross-cluster registry (`JDEP3.md:57-75`; `JDEP3-probes.json`, `S3-parallel-conflicts-with-landed-canon`). Independent replay: both landed clusters return `CLEAN` alone; the checker rejects two directories (exit 2) [scan re-verified at r89 closure: the only match is the r89 worked example]. At integration, manually verify both pointers and preserve unresolved status; a per-cluster `CLEAN` is not cross-cluster evidence. |

### R8 appendix — plausible but unrecorded influence (decided r90)

When evidence beyond commonplace resemblance or an explicit source-use claim triggers review,
record a dated, neutral `possible influence: unverified` note (in the inspiration note and
element map, creating them if absent): it records uncertainty, not influence. R2 (no source
used) requires BOTH the creator's no-source account AND the editor finding no contrary
source-specific evidence AND only a commonplace motif. Reserve the
`external-only / unverified inspiration` marker for established general-motif use with
independent in-world support; never place it on a merely possible influence. Withhold only the
affected detail pending re-derivation or permitted review; the element otherwise remains newly
authored fiction. **Owner:** the lore lane; unresolved disputes go to `l0-questions.md`.

**Failed-gate disposition (clarified r92):** **Owner:** the lore integration editor records the two-part R2 gate result, the affected element, and the separability decision in the inspiration note and element map; the creator supplies the provenance account; a named reviewer assesses and records the contrary source-specific evidence and whether an independently authored, independently supportable remainder exists. **Trigger:** either R2 condition fails or remains unresolved, and the reviewer cannot separate the source-dependent detail from the element while leaving such a remainder. **Decision:** withhold the **whole element from supported canon** until it is re-derived without the source-dependent material or a permitted source text is delivered and a separately reviewed R1 decision establishes a claim-specific basis. Do not leave the element in supported canon with an uncertainty notice: when the dependency is inseparable, the notice does not remove the unsupported dependency. Keep the dated `possible influence: unverified` note and mark R2 unavailable; this failed gate is not proof that a source was used, does not establish R1, and does not authorize the `external-only / unverified inspiration` marker by itself. Record the failed condition, contrary evidence, separability rationale, scope, and next action in the note/map. If the influence or separability question remains disputed, add the unresolved question and missing evidence to `l0-questions.md`. Remove the provisional note only after a later review records that both R2 conditions pass, or after a confirmed source-use decision is recorded under R1.

**Worked example:** a proposed lore element consists entirely of the same seven threshold names in the same order as *Kesh Hymn* lines 12–19. The creator denies using a source, but the reviewer records the contrary sequence evidence; no independently authored, supportable remainder survives removing that sequence. R2 is unavailable. Hold the whole element out of supported canon, preserve the neutral note and evidence in the inspiration note/map, and route any unresolved dispute to `l0-questions.md`. Do not keep the element as newly authored fiction merely by attaching a notice. The hold does not itself prove copying or source use.

### R9 appendix — translator known, source/version unknown (decided r90; reprint boundary clarified r91)

**Owner:** The lore integration owner verifies bibliographic identity and R5 scope; the
excerpt/map submitter supplies the exact delivered item, its citation, and the transcribed
passage.

**Trigger:** A delivered `translation` excerpt relies on a later reprint as the bibliographic tie
to its translator/source work, or a claim about that translation relies on a reprint record while
the delivered printing or source/version remains uncertain.

**Decision:** Translator name alone, without a reliable link to a named source work, FAILS R5
support. Keep `Delivery mode: translation`; record the translator and supported source-work/version
evidence. When no source-work link is established, record
`Source text/version: unidentified; unverified`; if the work is known but its exact source
edition/version is not, name the work and record that limit separately. Do not label the delivered
translation itself `not delivered`. A later reprint can qualify for the narrow R9 exception only
when an auditable, item-specific record identifies the actual delivered reprint and its
edition/year (and a stable identifier or copy locator), names the translator and source work,
and ties the cited passage to that translation; verify the passage against that exact copy.
Accept a title/imprint/copyright page or publisher/authoritative-library catalogue entry; a
generic reprint notice, untraceable secondary entry, translator name, or anchor alone is
insufficient. Record the precise reprint/printing and record citation in the excerpt/map. If the
tie is verified, allow support only for a claim about wording in that identified reprint. The
reprint tie does not prove that its text is unchanged from the earlier printing: do not extend
support to the earlier translation's wording or an edition-specific variant unless that exact
edition is independently identified and compared. If the item-specific tie or source work is
unverified, retain `Source text/version: unidentified; unverified` and fail R5 source-claim
support; describe only the checked copy's wording if the reprint itself is what is being reported.

**Manual R9 gate (required for translation-backed R5 claims):** **Owner:** the excerpt/map submitter supplies the delivered item and bibliographic evidence; a named lore integration reviewer who is not the submitter verifies them and records the outcome. If the integration owner is also the submitter, a second reviewer must be named. **Trigger:** before any claim mapped to `Delivery mode: translation` is accepted as R5 source-claim support or integrated as supported canon. **Review:** inspect the exact delivered translation item (or an item-specific record that identifies it), verify the actual printing/edition and year, with a stable identifier or copy locator, translator, named source work, and that the cited passage is present in that exact copy and supports the whole claim. Record any unknown source-version limitation; support is bounded to wording in the identified delivered translation, not the original source wording, an earlier printing, or an edition-specific variant. Public catalog availability is not required, but a privately held item qualifies only if the reviewer can inspect the exact copy or a complete, legible scan with its copy locator; a submitter-only assertion is insufficient. If identity, passage, or reviewer access is not established, record `FAIL` (or `OPEN` before review) and do not grant R5 support.

**Required record:** add an `R9 manual review` entry adjacent to each translation-backed claim in its claim-to-excerpt map. Include the claim pointer; excerpt path and span; delivered printing/edition and year plus a stable identifier or copy locator; translator; source work and source-text/version field (including explicit unknown status); evidence citation and inspection method; reviewer name/role and review date; disposition `PASS`, `FAIL`, or `OPEN`; and the exact claim scope permitted. Only a recorded manual `PASS` can clear this gate.

**Receipt boundary:** `corpus/tools/support_check.py` is a lexical preflight. Its `RESULT PASS` (or `RESULT PASS WITH WARNINGS`) and `SOURCE-SUPPORT` count report map/inventory/mode/anchor checks; they do not establish translation-version identity, the delivered printing, bibliographic linkage, translation fidelity, or the R9 manual outcome. A successful lexical preflight is necessary but not sufficient for a translation-backed R5 claim. Never present that command's output as the R9 review receipt; cite the separate per-claim manual-review entry. The existing verification command checks wording completeness only and cannot perform this review.

**Worked example:** the submitter maps a line from a privately held 2011 reprint of the 1901 translation by M. A. Translator and supplies a scan and copy locator. `support_check.py` may report `RESULT PASS` because the declared mode and anchor match; that is only lexical preflight. A non-submitter integration reviewer inspects the exact scan, confirms the 2011 item, translator, named source work, and passage, then records a dated `R9 manual review` `PASS` scoped only to “the identified 2011 reprint's translation says …”. The result does not support what the 1901 printing or original source says. If the reviewer cannot inspect the exact copy or the evidence does not tie the passage to the named work, record `FAIL`/`OPEN`, retain `Source text/version: unidentified; unverified` where applicable, and grant no R5 source-claim support regardless of the lexical command's result.

**Verification command (textual completeness only; it does not validate the source):**

```sh
python3 -c 'from pathlib import Path; s=Path(".ufo/waves/round-91/patches/D2-edges.patch").read_text(); keys=("**Owner:**","**Trigger:**","later reprint can qualify","item-specific record","source work","verify the passage against that exact copy","identified reprint","earlier printing","**Worked example:**","Source text/version: unidentified; unverified","**Verification command"); missing=[k for k in keys if k not in s]; print(f"R9 reprint decision completeness: {len(keys)-len(missing)}/{len(keys)}"); raise SystemExit(bool(missing))'
```

### R10 appendix — matching name/ID, different occasions (decided r90)

Shared names/IDs trigger comparison but do not prove identity (events are not entities;
occasion and field must match). Record compared-but-dismissed overlaps (paths, claim pointers,
supported occasion/scope, rationale) in the incoming cluster README under
`## R10 comparison outcomes`; unresolved identity/occasion candidates and missing evidence go
to that section and `l0-questions.md`, NOT the live register. Only a source-backed shared
referent, field, and occasion with incompatible assertions enters
`corpus/knowledge/cross-cluster-contradictions.md` (status `unresolved`). Both clusters are
preserved; a real-world parallel cannot adjudicate the in-world disagreement. **Owner:** the
lore lane at integration; the register's first real entry awaits a genuine conflict.

**Namespace scoping (decided r91):** `source_id` values are cluster-local identifiers.
A `source_id` shared across clusters is a NAMESPACE COLLISION, not identity evidence — comparison keys are
`(cluster-relative path, source_id)` pairs; a bare shared id triggers the namespace check (rename or
qualify one side) before any referent comparison. A collision alone never enters the register.

(Provenance: merged from seats D1/D2 per seat R1's recommendation; retroactivity checked —
the r87 ETCSL marker, the r88-m3 delivered Spence passage, and r87's intra-cluster Hara/Sen
record are unaffected.)

## Integration boundary

These are governance rows, not checker or schema changes. R8's materiality screen is not rights advice; R9's anchor check is not fidelity evidence; R10's proposed corpus-level register is a manual procedure until a corpus-wide validator exists. Do not mark any of those surfaces mechanically verified solely from a clean fixture replay.


**Integration notes (r89 closure).** R8–R10 are prospective. R9's delivery-mode
declaration applies to clusters landed from r89 onward; the r87/r88 clusters
are annotated at their next content touch (named debt, r89 ledger). R10's
register is created on first real cross-cluster conflict; the worked example
is `corpus/knowledge/r89-cross-cluster-contradiction.md`. R8 does not
retroactively affect the landed Spence row (its text is delivered).

Method cross-references (r90, seat K1): R8/R9's screens re-derive limits already
documented by chousa-shokunin — claim-vs-source verification
(`chousa-shokunin/corpus/knowledge/claim-verification-r2.md:45-58`), archives
verified against live sources (`archives-verified-r9.md:177-185`), and
fixed-string anchor boundaries (`anchor-boundaries-r4.md:31-37`). Chousa owns
the research method; lore consumes it as record craft.

### r93 correction — historical evidence cells (2026-10-17)

This dated correction supersedes the current-status reading of the evidence cells in rows 12 and 17 above; it does not rewrite their filed bytes. Those cells describe round-88 candidates, not the r93 landed state. The round and path disambiguation is:

- The unselected r88 M1 Kojiki proposal was `.ufo/waves/round-88/patches/M1-cluster2.patch`, proposing `corpus/fixtures/r88-myth-cluster2/`. The r88 M1 report describes it as a candidate patch (`.ufo/waves/round-88/M1.md`); the r88 M5 convergence review recommends r88 M3 instead and marks r88 M1 not recommended (`.ufo/waves/round-88/M5.md`, candidate table). It was not the landed r93 cluster.
- The r88 M2 Völuspá candidate is `.ufo/waves/round-88/patches/M2-cluster2.patch`, proposing `corpus/fixtures/r88-norse-cluster/` (`.ufo/waves/round-88/M2.md`). That round-88 M2 is distinct from r93 M2.
- The landed r93 M2 Kojiki cluster is `corpus/fixtures/r93-m2-kojiki-cluster/`; its README identifies it as the R93 M2 cluster. Its Chamberlain/Kojiki reference is registered in `corpus/knowledge/reference-ledger.md` (the row pointing to `corpus/fixtures/r93-m2-kojiki-cluster/kojiki-chamberlain-excerpt.md`). This correction records landing and registration only; it makes no rights, training-permission, source-support, or manual-review finding.

The R8 worked record is `corpus/knowledge/r93-r8-worked-example.md`. It is a hypothetical seven-threshold-names case with a record-to-decision crosswalk, not a live source-use decision: its scope statement explicitly disclaims an observed submission, source-use/copying finding, rights assessment, and canon assertion.

### r93 replacement R9 completeness check (2026-10-17)

The original R9 **Verification command** above is superseded and historical: it reads `.ufo/waves/round-91/patches/D2-edges.patch`, not the delivered R9 appendix. Use this replacement from the repository root. It reads this delivered decision-table file, slices the R9 appendix at its heading and stops before that appendix's Verification command, then checks the prose categories below; it does not establish source identity, fidelity, rights, permission, or a manual review outcome.

```sh
python3 - <<'PY'
from pathlib import Path
import sys

text = Path("corpus/knowledge/r88-sourced-inspiration-decision-table.md").read_text(encoding="utf-8")
_, tail = text.split("### R9 appendix — translator known, source/version unknown", 1)
r9, _ = tail.split("**Verification command (textual completeness only; it does not validate the source):**", 1)
clauses = {
    "manual gate": (
        "**Manual R9 gate (required for translation-backed R5 claims):**",
        "Only a recorded manual `PASS` can clear this gate.",
    ),
    "per-claim record": (
        "**Required record:** add an `R9 manual review` entry adjacent to each translation-backed claim",
        "claim pointer; excerpt path and span",
        "delivered printing/edition and year plus a stable identifier or copy locator",
        "reviewer name/role and review date",
        "disposition `PASS`, `FAIL`, or `OPEN`",
        "exact claim scope permitted",
    ),
    "receipt boundary": (
        "**Receipt boundary:** `corpus/tools/support_check.py` is a lexical preflight.",
        "necessary but not sufficient for a translation-backed R5 claim",
        "Never present that command's output as the R9 review receipt",
    ),
    "exact-copy safeguards": (
        "inspect the exact delivered translation item",
        "actual printing/edition and year, with a stable identifier or copy locator",
        "reviewer can inspect the exact copy or a complete, legible scan with its copy locator",
    ),
    "FAIL/OPEN safeguards": (
        "record `FAIL` (or `OPEN` before review)",
        "do not grant R5 support",
    ),
}

def check(body):
    return {name: all(clause in body for clause in required) for name, required in clauses.items()}

actual = check(r9)
mutated = check(r9.replace(clauses["manual gate"][1], "", 1))
mutation_control = not mutated["manual gate"] and all(
    passed for name, passed in mutated.items() if name != "manual gate"
)
for name, passed in actual.items():
    print(f"{name}: {'PASS' if passed else 'FAIL'}")
print(f"R9 delivered-appendix categories: {sum(actual.values())}/{len(actual)}")
print(f"required prose-clause removal: {'FAIL as expected' if mutation_control else 'did not fail'}")
if not all(actual.values()) or not mutation_control:
    raise SystemExit(1)
PY
```

### r93 R9 completeness-verifier correction (2026-10-17)

**Correction to the prior r93 replacement check above:** its selected clauses let the verifier pass after removal of R9's `Owner`, `Trigger`, or `Decision` fieldheads and the source-work/version record requirement. Preserve that command as history, but do not use it as the completeness check. This replacement inspects only the delivered R9 appendix text between its appendix heading and the original Verification command. Every required literal is checked inside that slice, never against this correction, its command source, or another file. Its mutation controls remove each individual required field/clause in memory and require the matching named textual finding; this is still textual completeness only, not translation/source/permission semantic verification or a manual review.

Run from the repository root:

```sh
python3 - <<'PY'
from pathlib import Path
import sys

path = Path("corpus/knowledge/r88-sourced-inspiration-decision-table.md")
text = path.read_text(encoding="utf-8")
heading = "### R9 appendix — translator known, source/version unknown"
verification = "**Verification command (textual completeness only; it does not validate the source):**"
_, tail = text.split(heading, 1)
r9, _ = tail.split(verification, 1)
required = (
    ("R9-OWNER", "**Owner:** The lore integration owner verifies bibliographic identity and R5 scope;"),
    ("R9-TRIGGER", "**Trigger:** A delivered `translation` excerpt relies on a later reprint as the bibliographic tie"),
    ("R9-DECISION", "**Decision:** Translator name alone, without a reliable link to a named source work, FAILS R5\nsupport."),
    ("R9-SOURCE-VERSION-UNKNOWN", "When no source-work link is established, record\n`Source text/version: unidentified; unverified`;"),
    ("R9-KNOWN-WORK-UNKNOWN-EDITION", "if the work is known but its exact source\nedition/version is not, name the work and record that limit separately."),
    ("R9-REPRINT-EDITION-IDENTITY", "A later reprint can qualify for the narrow R9 exception only\nwhen an auditable, item-specific record identifies the actual delivered reprint and its\nedition/year (and a stable identifier or copy locator),"),
    ("R9-TRANSLATOR-SOURCE-PASSAGE-TIE", "names the translator and source work,\nand ties the cited passage to that translation; verify the passage against that exact copy."),
    ("R9-ACCEPTABLE-EDITION-EVIDENCE", "Accept a title/imprint/copyright page or publisher/authoritative-library catalogue entry;"),
    ("R9-INSUFFICIENT-REPRINT-EVIDENCE", "generic reprint notice, untraceable secondary entry, translator name, or anchor alone is\ninsufficient."),
    ("R9-RECORD-EXACT-PRINTING", "Record the precise reprint/printing and record citation in the excerpt/map."),
    ("R9-EARLIER-EDITION-BOUNDARY", "The\nreprint tie does not prove that its text is unchanged from the earlier printing:"),
    ("R9-UNVERIFIED-SOURCE-FAILS", "If the item-specific tie or source work is\nunverified, retain `Source text/version: unidentified; unverified` and fail R5 source-claim\nsupport;"),
    ("R9-DO-NOT-MISLABEL-DELIVERY", "Do not label the delivered\ntranslation itself `not delivered`."),
    ("R9-MANUAL-GATE", "**Manual R9 gate (required for translation-backed R5 claims):**"),
    ("R9-MANUAL-OWNER", "the excerpt/map submitter supplies the delivered item and bibliographic evidence; a named lore integration reviewer who is not the submitter verifies them and records the outcome."),
    ("R9-SECOND-REVIEWER", "If the integration owner is also the submitter, a second reviewer must be named."),
    ("R9-MANUAL-TRIGGER", "**Trigger:** before any claim mapped to `Delivery mode: translation` is accepted as R5 source-claim support or integrated as supported canon."),
    ("R9-EXACT-ITEM-REVIEW", "inspect the exact delivered translation item (or an item-specific record that identifies it), verify the actual printing/edition and year, with a stable identifier or copy locator, translator, named source work, and that the cited passage is present in that exact copy and supports the whole claim."),
    ("R9-UNKNOWN-VERSION-LIMIT", "Record any unknown source-version limitation; support is bounded to wording in the identified delivered translation, not the original source wording, an earlier printing, or an edition-specific variant."),
    ("R9-PRIVATE-COPY-ACCESS", "a privately held item qualifies only if the reviewer can inspect the exact copy or a complete, legible scan with its copy locator; a submitter-only assertion is insufficient."),
    ("R9-MANUAL-FAIL-OPEN", "If identity, passage, or reviewer access is not established, record `FAIL` (or `OPEN` before review) and do not grant R5 support."),
    ("R9-REQUIRED-RECORD", "**Required record:** add an `R9 manual review` entry adjacent to each translation-backed claim in its claim-to-excerpt map."),
    ("R9-RECORD-CLAIM-POINTER", "claim pointer; excerpt path and span;"),
    ("R9-RECORD-EDITION-IDENTIFIER", "delivered printing/edition and year plus a stable identifier or copy locator;"),
    ("R9-RECORD-TRANSLATOR", "translator;"),
    ("R9-RECORD-SOURCE-VERSION", "source work and source-text/version field (including explicit unknown status);"),
    ("R9-RECORD-EVIDENCE-METHOD", "evidence citation and inspection method;"),
    ("R9-RECORD-REVIEWER-DATE", "reviewer name/role and review date;"),
    ("R9-RECORD-DISPOSITION", "disposition `PASS`, `FAIL`, or `OPEN`;"),
    ("R9-RECORD-CLAIM-SCOPE", "exact claim scope permitted."),
    ("R9-MANUAL-PASS-ONLY", "Only a recorded manual `PASS` can clear this gate."),
    ("R9-RECEIPT-BOUNDARY", "**Receipt boundary:** `corpus/tools/support_check.py` is a lexical preflight."),
    ("R9-RECEIPT-NOT-IDENTITY-OR-FIDELITY", "they do not establish translation-version identity, the delivered printing, bibliographic linkage, translation fidelity, or the R9 manual outcome."),
    ("R9-RECEIPT-NOT-RECEIPT", "Never present that command's output as the R9 review receipt;"),
    ("R9-RECEIPT-PER-CLAIM-ENTRY", "cite the separate per-claim manual-review entry."),
    ("R9-LEXICAL-PREFLIGHT-BOUNDARY", "A successful lexical preflight is necessary but not sufficient for a translation-backed R5 claim."),
)

def findings(body):
    return [name for name, clause in required if body.count(clause) != 1]

baseline_missing = findings(r9)
print(f"R9 appendix-only baseline: {'PASS' if not baseline_missing else 'FAIL'} ({len(required) - len(baseline_missing)}/{len(required)} requirements)")
if baseline_missing:
    print("baseline findings: " + ", ".join(baseline_missing))

controls_passed = 0
for name, clause in required:
    mutated = r9.replace(clause, "", 1)
    observed = findings(mutated)
    passed = observed == [name]
    controls_passed += passed
    print(f"remove {name}: {'FAIL as expected' if passed else 'NOT DETECTED'}; findings={','.join(observed) or 'none'}")
print(f"R9 clause-removal controls: {controls_passed}/{len(required)}")
if baseline_missing or controls_passed != len(required):
    raise SystemExit(1)
PY
```
