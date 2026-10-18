diff --git a/corpus/knowledge/holder-assessment-boundary.md b/corpus/knowledge/holder-assessment-boundary.md
--- a/corpus/knowledge/holder-assessment-boundary.md
+++ b/corpus/knowledge/holder-assessment-boundary.md
@@ -1,19 +1,12 @@
 # Holder-assessment boundary: reading provenance ambiguity disclosures
 
-<!-- Reconstructed at round-91 integration from seat CB1's r90 section-replacement
-     instructions (D1-D13) applied to the r89-landed contract (e97613c); replaces the
-     mis-landed instruction sheet from the r90 closure (defect found by CB1, round 91).
-     Skipped as named debt: D1 — Decision-table row 2 code refs. -->
-
-# Holder-assessment boundary: reading provenance ambiguity disclosures
-<!-- Refreshed at round-89 closure from seat CB1's verified proposal
-     (.ufo/waves/round-89/followup/CB1-boundary-refresh.md) with seat E1's
-     corrections applied; every anchor and pasted output re-derived from the
-     delivered tree at 1b09f3f (checker e2bb9639). -->
-
-> **Landed at round-89 closure** (replacing the r88-closure version). Drift inventory:
-> `.ufo/waves/round-89/followup/CB1.md` (CB1-R1…R19); corrections per
-> `.ufo/waves/round-89/followup/E1-boundary-update-proposal.md` §F applied.
+<!-- Refreshed at round-90 closure from seat CB1's verified proposal
+     (.ufo/waves/round-90/followup/CB1-boundary-refresh.md); every anchor and pasted
+     output re-derived from the delivered tree at ca7f9ef (checker ff9fd2aa). -->
+
+> **Landed at round-90 closure** (replacing the r89-closure version). Drift inventory:
+> `.ufo/waves/round-90/followup/CB1.md` (CB1-D1…D14); the r89-closure proposal
+> (`.ufo/waves/round-89/followup/CB1-boundary-refresh.md`) remains the prior landed revision.
 
 source: fleet round-1 shared diagnostic contract (holder-disclosure move,
 calibration axis), whose round-1 baseline paragraph is kept verbatim in "The
@@ -28,26 +21,21 @@
 three times after that: round-87 seat C1 added the per-record disclosure
 (commit `03c6746`, delivered tree `2b48ca7`); round-88 seat C1 replaced the
 holder-only latch with permanent first-stop cause tracking and armed the stop
-from shape-invalid records (integrated in `2ea9ef1`); round-89 seat X1 added the multi-cause summary, the raw-vs-resolved-index cause wording,
-and the not-uniquely-resolvable qualification of comparison findings (integrated in
-`1b09f3f`); round-90 composed seat X2's null guard — a null holder field never produces an
-identity clause — with seat X3's integer-only tick reading per seat C9's ruling: tick order
-is an integer comparison and holder-identity uncertainty does not qualify it, while genuinely
-unresolved non-null holder identities still qualify chain-continuity and first-record
-findings (integrated in `ca7f9ef`, checker `ff9fd2aa`). This revision was rewritten by
-round-90 seat CB1 against the delivered checker at `ca7f9ef`
-(`.ufo/waves/round-90/followup/CB1.md`)
-delivered checker at `1b09f3f`
-(`.ufo/waves/round-89/followup/CB1.md`); the r88 contract, decision table,
+from shape-invalid records (integrated in `2ea9ef1`); round-89 seat X1 added the
+multi-cause summary, the raw-vs-resolved-index cause wording, and the
+not-uniquely-resolvable qualification of comparison findings (integrated in
+`1b09f3f`); round-90 composed seat X2's null guard — a null holder field never
+produces an identity clause — with seat X3's integer-only tick reading per seat
+C9's ruling: tick order is an integer comparison and holder-identity uncertainty
+does not qualify it, while genuinely unresolved non-null holder identities
+still qualify chain-continuity and first-record findings (integrated in
+`ca7f9ef`, checker `ff9fd2aa`). This revision was rewritten by round-90 seat
+CB1 against the delivered checker at `ca7f9ef`
+(`.ufo/waves/round-90/followup/CB1.md`); the r88 contract, decision table,
 limits, and status sections it replaces are superseded, and the r87 replay
 evidence at `2b48ca7` is preserved only in
 `.ufo/waves/round-87/followup/I2.md`.
 
-verified-at: RUNTIME REPLAYED on the delivered tree at `1b09f3f` by round-89
-seat CB1; exact commands and observed output are pasted under "Commands" and
-in `.ufo/waves/round-89/followup/CB1.md`. The single `remain unassessed …
-first stop:` disclosure form, every named first-stop cause (including both
-raw-vs-resolved wordings), the multi-cause joining rule, the qualified
 verified-at: RUNTIME REPLAYED on the delivered tree at `ca7f9ef` by round-90 seat CB1;
 exact commands and observed output are pasted under "Commands" and in
 `.ufo/waves/round-90/followup/CB1.md`. All fourteen pasted case blocks below replay
@@ -58,14 +46,29 @@
 checker behavior only; it is not a five-gate score and not a claim about fictional truth. The
 baseline (`5eb9451`) triples remain as recorded in `reports/round-1/current-baseline.json`
 and `reports/round-1/baseline-probes.json`.
-`remain unassessed` template string or any named first-stop cause changes,
-Re-verify whenever the provenance branch of `corpus/fixtures/check_bible.py` changes — in
-particular the comparison gate (`:322`) and its branches, chain continuity (`:327-337`) and
-tick order (`:323-326`) — whenever the `remain unassessed` template string or any named
-first-stop cause changes, whenever the raw entity/source counters, the `is not uniquely
-resolvable` detail string, the null guard in `holder_identity_detail` (`:169-170`), or the
-`; ` cause-joining rule changes, or whenever any `corpus/live/runs/round-85/probe-inputs/`
-JSON byte changes.
+
+recheck: from the lane root, replay the five recorded r85 probe inputs with
+the delivered checker (see "Commands"), and re-run any fixture that combines
+`provenance` with a duplicated entity id. Re-verify whenever the provenance
+branch of `corpus/fixtures/check_bible.py` changes — in particular the
+comparison gate (`:322`) and its branches, chain continuity (`:327-337`) and
+tick order (`:323-326`) — whenever the `remain unassessed` template string or
+any named first-stop cause changes, whenever the raw entity/source counters,
+the `is not uniquely resolvable` detail string, the null guard in
+`holder_identity_detail` (`:169-170`), or the `; ` cause-joining rule changes,
+or whenever any `corpus/live/runs/round-85/probe-inputs/` JSON byte changes.
+The `corpus/fixtures/measure_holder_disclosure.py` helper named by the round-1
+contract does not exist at `ca7f9ef` (`python3
+corpus/fixtures/measure_holder_disclosure.py --revision HEAD` exits 2 with
+`No such file or directory`; `corpus/fixtures/` contains only
+`check_bible.py` as a Python file there); run it only in a revision that
+contains it, and treat its five-gate sample as a ceiling, never as a score
+for a tree that has not run it.
+
+## The contract (round-1 baseline paragraph, kept)
+
+Baseline `5eb9451` behavior, kept: a duplicated holder ID inside an item's
+`provenance` records silently invalidates that record, permanently latches
 the chain gate `can_check_chain = False` for that item, and the ONLY output
 is the global `entities[j].id: duplicate entities id {id!r}` finding — the
 ambiguous reference itself gets no line, and continuity plus tick-order
@@ -81,7 +84,7 @@
 permanent first-stop cause record:
 
 1. **One disclosure form, one line per affected record.** A single template,
-   verbatim (delivered `:206-208`):
+   verbatim (delivered `:208-210`):
 
    ```text
    {record_label}: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: {cause} at {origin_label}
@@ -96,7 +99,7 @@
 
 2. **Any first cause arms the stop, and the disclosure names it.** `{cause}`
    is every stop condition the checker reached at that record, in check order,
-   joined with `; ` (`:313-316`). `{origin_label}` is the record label that
+   joined with `; ` (`:315-318`). `{origin_label}` is the record label that
    armed it (`entities[3].provenance[1]`) or, for the three item-level
    conditions, the item label (`entities[3].provenance`). Ambiguous holder
    identity is one cause among several, not the only one.
@@ -105,30 +108,49 @@
    holder references get
    `{record_label}.{from_holder|to_holder}: ambiguous entity {id!r}` and the
    record remains invalid (mirrors the relation-endpoint format at
-   `check_bible.py:182`; delivered `:275` for `to_holder`, `:288` for
+   `check_bible.py:184`; delivered `:277` for `to_holder`, `:290` for
    `from_holder`). Several references at one record are joined by `, ` in the
-   order `to_holder` then `from_holder` (`:292-297`).
+   order `to_holder` then `from_holder` (`:294-299`).
 
 4. **A shape-invalid dict record can arm the stop.** When a record fails the
    exact-key-set check, the checker still inspects its nonempty string
    `to_holder` / `from_holder` values for duplicated entity IDs
-   (`:225-233`): each ambiguous field gets its own local `ambiguous entity`
+   (`:227-235`): each ambiguous field gets its own local `ambiguous entity`
    line, and — absent an earlier stop — the cause entry becomes
    `malformed record (unexpected field set); ambiguous holder identity {refs}`
-   (`:236-244`). A non-dict record cannot arm a holder-ambiguity cause: it
-   hits `malformed record (expected object)` first (`:215-221`).
+   (`:238-246`). A non-dict record cannot arm a holder-ambiguity cause: it
+   hits `malformed record (expected object)` first (`:217-223`).
 
 5. **The conservative permanent latch is preserved.** Comparisons do not
    resume within the run, and no break is inferred from ambiguity. All old
    diagnostics, exit behavior (`VIOLATION:` lines, `N violation(s); no canon
    changed`, `CLEAN: schema, citations, relations, timeline; 0 violations`),
    the comparison state machine, and every existing fictional JSON byte are
-Round-90 verification (seat CB1, `ca7f9ef`): the r89 checker (`e2bb9639`) and the delivered
-checker (`ff9fd2aa`), run against the same 160 fixture directories, produced 0 exit-code
-changes, 0 stderr changes, and 0 changed stdout tuples; four new directories
-(`r90-c1-rawpresent-to`, `r90-c1-rawpresent-from`, `r90-c1-rawpresent-source`,
-`r90-c1-three-causes`) were added in the same commit, making 164 fixture directories
-(B1's 160-row tuple receipt replayed, 0 mismatches).
+   preserved. Verified by CB1 for the 160 fixture directories at `1b09f3f`:
+   the r88 checker (`dcacffd6`) and the delivered checker (`e2bb9639`), run
+   against the same 160 input directories, produced 0 exit-code changes,
+   0 stderr changes, and 9 changed stdout tuples — the four pre-existing
+   directories `r87-probe-multi-invalid`, `r87-probe-record-and-chain`,
+   `r88-mixed-stop`, `r88-nonholder-stop`, plus five of the eleven new r89
+   directories (`r89-c1-multi-cause-valid`, `r89-f2-dangling-from`,
+   `r89-f2-dangling-to`, `r89-f2-invalid-source-id`,
+   `r89-fn2-unresolved-chain-break`). The other six new directories
+   (`r89-c1-invalid-from-holder`, `r89-c1-invalid-tick`,
+   `r89-c1-invalid-to-holder`, `r89-c1-malformed-source-id`,
+   `r89-fn2-control`, `r89-inspiration-paraphrase`) are tuple-identical
+   (`.ufo/waves/round-89/followup/CB1.md` §M1).
+
+   Round-90 verification (seat CB1, `ca7f9ef`): the r89 checker (`e2bb9639`) and the delivered
+   checker (`ff9fd2aa`), run against the same 160 fixture directories, produced 0 exit-code
+   changes, 0 stderr changes, and 0 changed stdout tuples; four new directories
+   (`r90-c1-rawpresent-to`, `r90-c1-rawpresent-from`, `r90-c1-rawpresent-source`,
+   `r90-c1-three-causes`) were added in the same commit, making 164 fixture directories
+   (B1's 160-row tuple receipt replayed, 0 mismatches).
+
+6. **Two tables are consulted.** The checker keeps a **raw** count of
+   `entities` / `sources` rows whose `id` is a nonempty string — counted
+   during JSON loading, before field validation (`:38-39`, `:72-76`) — and a
+   **resolved index** built only from rows that pass the field check
    (`:82-83`, `:85-91`, `:97`). Cause wording distinguishes "no raw row at
    all" from "raw rows exist but none reaches the resolved index" (items 9,
    10, 13 of the cause table).
@@ -136,34 +158,34 @@
 `{record_label}` is the existing provenance record path, e.g.
 `entities[3].provenance[1]` for the `seal` item's second transfer.
 
-## First-stop causes (delivered `1b09f3f`)
+## First-stop causes (delivered `ca7f9ef`)
 
 Three item-level conditions are tested once, before the record loop
-(`:198-203`); the rest are tested per record. Each is a literal cause entry,
+(`:200-205`); the rest are tested per record. Each is a literal cause entry,
 verbatim. `{raw_presence}` is `present in raw entities but` when the raw
 entity counter for the id is nonzero, otherwise `absent from raw entities and`
-(`:272`, `:285`); the source form uses `raw sources` (`:306`).
+(`:274`, `:287`); the source form uses `raw sources` (`:308`).
 
 | # | Cause string | Trigger | Code |
 |---|---|---|---|
-| 1 | `source table unavailable` | `sources.json` missing or unparseable | `:198-199` |
-| 2 | `provenance attached to a non-item entity` | `provenance` present on a non-`item` entity | `:200-201` |
-| 3 | `duplicate item id {id!r}` | the item's own id appears more than once | `:202-203` |
-| 4 | `malformed record (expected object)` | record is not a dict | `:215-221` |
-| 5 | `malformed record (unexpected field set)` | record's key set ≠ `{tick, from_holder, to_holder, source_id}`; if the rejected dict also carries an ambiguous nonempty holder string the entry becomes `malformed record (unexpected field set); ambiguous holder identity {refs}` | `:222-248` |
-| 6 | `malformed record (invalid tick)` | `tick` not a nonnegative `int` | `:257-260` |
-| 7 | `malformed record (invalid from_holder)` | `from_holder` neither `null` nor a nonempty string | `:261-264` |
-| 8 | `malformed record (invalid to_holder)` | `to_holder` not a nonempty string | `:265-268` |
-| 9 | `holder reference to_holder {id!r} {raw_presence} absent from the resolved index` | `to_holder` resolves to no entity in the resolved index; `{raw_presence}` says whether any raw entity row carries the id | `:269-273` |
-| 10 | `holder reference from_holder {id!r} {raw_presence} absent from the resolved index` | same for `from_holder` | `:279-286` |
-| 11 | `ambiguous holder identity {refs}` | `to_holder` and/or `from_holder` matches ≥ 2 entity rows in the resolved index; `{refs}` is `to_holder 'x'`, `from_holder 'y'` joined `, ` in that field order | `:274-278`, `:287-297` |
-| 12 | `malformed record (invalid source_id)` | `source_id` not a nonempty string | `:298-301` |
-| 13 | `source reference {id!r} {raw_presence} absent from the resolved index` | `source_id` resolves to no source row; `{raw_presence}` is `present in raw sources but` / `absent from raw sources and` | `:302-307` |
-| 14 | `source table unavailable` | per-record source status is `unavailable` | `:308-310` |
+| 1 | `source table unavailable` | `sources.json` missing or unparseable | `:200-201` |
+| 2 | `provenance attached to a non-item entity` | `provenance` present on a non-`item` entity | `:202-203` |
+| 3 | `duplicate item id {id!r}` | the item's own id appears more than once | `:204-205` |
+| 4 | `malformed record (expected object)` | record is not a dict | `:217-223` |
+| 5 | `malformed record (unexpected field set)` | record's key set ≠ `{tick, from_holder, to_holder, source_id}`; if the rejected dict also carries an ambiguous nonempty holder string the entry becomes `malformed record (unexpected field set); ambiguous holder identity {refs}` | `:224-250` |
+| 6 | `malformed record (invalid tick)` | `tick` not a nonnegative `int` | `:259-262` |
+| 7 | `malformed record (invalid from_holder)` | `from_holder` neither `null` nor a nonempty string | `:263-266` |
+| 8 | `malformed record (invalid to_holder)` | `to_holder` not a nonempty string | `:267-270` |
+| 9 | `holder reference to_holder {id!r} {raw_presence} absent from the resolved index` | `to_holder` resolves to no entity in the resolved index; `{raw_presence}` says whether any raw entity row carries the id | `:271-275` |
+| 10 | `holder reference from_holder {id!r} {raw_presence} absent from the resolved index` | same for `from_holder` | `:281-288` |
+| 11 | `ambiguous holder identity {refs}` | `to_holder` and/or `from_holder` matches ≥ 2 entity rows in the resolved index; `{refs}` is `to_holder 'x'`, `from_holder 'y'` joined `, ` in that field order | `:276-280`, `:289-299` |
+| 12 | `malformed record (invalid source_id)` | `source_id` not a nonempty string | `:300-303` |
+| 13 | `source reference {id!r} {raw_presence} absent from the resolved index` | `source_id` resolves to no source row; `{raw_presence}` is `present in raw sources but` / `absent from raw sources and` | `:304-309` |
+| 14 | `source table unavailable` | per-record source status is `unavailable` | `:310-312` |
 
 **Several causes can be named at once.** Every cause the record reached is
 appended to a list in check order and the whole list is joined with `; ` when
-the record is the arming record (`:256`, `:313-316`). Order is still the order
+the record is the arming record (`:258`, `:315-318`). Order is still the order
 of the checks, and item-level causes (rows 1-3) still pre-empt the record loop
 entirely, so a row-1..3 item shows exactly one cause. The shape-invalid entry
 (row 5) is one such entry, not a special case: it is itself a combined string,
@@ -175,13 +197,13 @@
 | Holder reference state | Output for that state (contract) | What the output does NOT say | Editor's safe action |
 |---|---|---|---|
 | Unique holder IDs; chain continuous; ticks strictly ascending | No holder findings; the item may contribute to `CLEAN` or unrelated findings elsewhere | Source text support, true custody, or canon — a citation resolves a fictional ID only (`corpus/fixtures/README.md:116-118`) | None on holders. |
-| Holder IDs each uniquely resolvable in the raw table and the resolved index; real discontinuity (wrong `from_holder`, non-null first `from_holder`, or `tick` ≤ previous) | Definite comparison findings: `{record_label}: provenance chain break; expected from_holder {…!r}, got {…!r}` and/or `{record_label}.tick: provenance tick {…} must be greater than previous tick {…}` (delivered `:343-344`, `:349-350`, `:333`; an ambiguous source citation earlier in the chain prefixes `input-structural finding, not sourced-canon; ` — ambiguous SOURCE is a different mechanism from ambiguous holder identity and does NOT stop comparisons) | Which field is wrong; the intended story; anything canon. Baseline evidence: `r85-unique-break-control` reported the record-2 break verbatim; delivered evidence: `r87-chain-unique-broken` (1 violation), `r87-chain-unique-valid` (`CLEAN`), `r89-fn2-control` | Choose the editorially-intended field, edit, rerun. |
-| A referenced holder ID is **not uniquely resolvable**: ≥ 2 raw entity rows carry it but exactly one survives the field check | The comparison still runs, but every finding that involves that ID is qualified: `{record_label}: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: {detail}; got {…!r}` (or, when only the observed side is unresolvable, `expected from_holder {…!r}; got {…!r}; {detail}`), and for ticks `{record_label}.tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: {details}; provenance tick {…} must be greater than previous tick {…}` (`:327-333`, `:334-344`, `:345-350`). `{detail}` is `{reference} {id!r} is not uniquely resolvable ({raw} raw entity rows carry this id, but only {indexed} is in the resolved index)` (`:168-173`) | That the chain is definitely broken, or definitely intact — the expected or observed holder is not a single row, so the mismatch may be an artifact of the rejected duplicate. It also does not name which raw row was rejected; read that row's own `VIOLATION:` line | Repair the duplicate first (rename or merge, per the checklist), rerun, and re-read the comparison as a definite finding. Delivered evidence: `r89-fn2-unresolved-chain-break` (expected side) versus `r89-fn2-control` (unqualified control). |
+| Holder IDs each uniquely resolvable in the raw table and the resolved index; real discontinuity (wrong `from_holder`, non-null first `from_holder`, or `tick` ≤ previous) | Definite comparison findings: `{record_label}: provenance chain break; expected from_holder {…!r}, got {…!r}` and/or `{record_label}.tick: provenance tick {…} must be greater than previous tick {…}` (delivered `:337`, `:326`, `:343`; an ambiguous source citation earlier in the chain prefixes `input-structural finding, not sourced-canon; ` — ambiguous SOURCE is a different mechanism from ambiguous holder identity and does NOT stop comparisons) | Which field is wrong; the intended story; anything canon. Baseline evidence: `r85-unique-break-control` reported the record-2 break verbatim; delivered evidence: `r87-chain-unique-broken` (1 violation), `r87-chain-unique-valid` (`CLEAN`), `r89-fn2-control` | Choose the editorially-intended field, edit, rerun. |
+| A referenced holder ID is **not uniquely resolvable**: ≥ 2 raw entity rows carry it but exactly one survives the field check | Chain-continuity and first-record findings that involve that ID are qualified: `{record_label}: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: {detail}; got {…!r}` (or, when only the observed side is unresolvable, `expected from_holder {…!r}; got {…!r}; {detail}`), and the first-record form `… possible provenance chain break, not a definite identity mismatch: {detail}; first record must have from_holder null` (`:330-335`, `:339-341`). Tick findings are NOT qualified: `{record_label}.tick: provenance tick {…} must be greater than previous tick {…}` with no identity note (`:323-326`). A null holder field contributes no clause and never triggers qualification (`:169-170`). `{detail}` is `{reference} {id!r} is not uniquely resolvable ({raw} raw entity rows carry this id, but only {indexed} is in the resolved index)` (`:171-175`) | That the chain is definitely broken, or definitely intact — the chain finding's expected or observed holder is not a single row, so the mismatch may be an artifact of the rejected duplicate. It does not make tick order, an integer comparison, uncertain. It also does not name which raw row was rejected; read that row's own `VIOLATION:` line | Repair the duplicate first (rename or merge, per the checklist), rerun, and re-read the chain comparison as a definite finding. A tick line already reads as definite while the duplicate remains. Delivered evidence: `r89-fn2-unresolved-chain-break` (expected side) versus `r89-fn2-control` (unqualified control); CB1's round-90 edge probe adds observed-side, null-observed/expected-unresolved, and unqualified-tick receipts (`CB1.md`) |
 | Dangling holder, either field (the ID resolves to no entity in the resolved index) | Explicit `{record_label}.{from_holder|to_holder}: dangling entity {id!r}` (kept) PLUS `{record_label}: … remain unassessed … first stop: holder reference {field} {id!r} {raw_presence} absent from the resolved index at {record_label}` at that record and at every later record of the item | Ambiguity — nothing is duplicated; a dangling ID and an ambiguous ID are different states. The clause does not say "unknown": a raw row may exist and have been rejected by the field check | Create or point to the intended single entity, rerun. If the clause says `present in raw entities but`, the row exists but fails validation — repair that row rather than inventing an entity. No `ambiguous entity` line is owed. Delivered evidence: `r89-f2-dangling-to`, `r89-f2-dangling-from`, `r87-probe-record-and-chain` (`entities[3].provenance[6]`, `[7]`). |
 | Ambiguous holder, either field (ID matches ≥ 2 entity rows in the resolved index) | Global duplicate `entities[j].id: duplicate entities id {id!r}` (kept) PLUS `{record_label}.{field}: ambiguous entity {id!r}` per ambiguous field PLUS the `… remain unassessed … first stop: ambiguous holder identity {refs} at {record_label}` disclosure at that record and at EVERY later record of the item. No definite chain-break or tick-order finding for that record or any later record of the item | A hidden break, a hidden clean result, or which duplicate row is "the real" vault. `r85-isolated-ambiguous` (internally consistent chain) and `r85-masked-ambiguous` (genuine downstream break) both hide the downstream state; delivered output differs only in how many records the disclosure names — 3 findings vs 4 — and the masked break stays unreported either way | Resolve identity (checklist below), rerun, review subsequent findings. |
 | Ambiguity on a record that also fails the key-set check | `{record_label}: expected exactly tick, from_holder, to_holder, source_id` PLUS the local `ambiguous entity` line(s) PLUS the disclosure naming the combined cause `malformed record (unexpected field set); ambiguous holder identity {refs}` at that record and every later one | That the record was a usable provenance event, or that the shape violation alone caused the gap — both causes are named together, and neither is a lore fact | Repair the shape and the identity; rerun; treat the whole tail as unassessed until a clean comparison run. Delivered evidence: `r88-shape-ambiguous-armed`, `r87-probe-shape-ambiguous`. |
 | A non-holder cause earlier in the item (dangling holder, unknown source, malformed record, duplicate item id, non-item, unavailable source table) | The disclosure names THAT cause, at the arming record and every later record. A different ambiguous holder introduced later still gets its own local `ambiguous entity` line but does not change the named cause | That the later ambiguity caused the earlier stop — the disclosure tracks the first stop, and later causes at *later* records are not appended to it (causes at the *same* record are: see the next row) | Fix the named first cause first; rerun; then repair the later findings, which appear as their own `VIOLATION:` lines. Delivered evidence: `r88-mixed-stop` (unknown source at `[0]`, ambiguity at `[1]`), `r88-nonholder-stop`. |
-| A referenced holder ID is **not uniquely resolvable**: ≥ 2 raw entity rows carry it but exactly one survives the field check | Chain-continuity and first-record findings that involve that ID are qualified: `{record_label}: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: {detail}; got {…!r}` (or, when only the observed side is unresolvable, `expected from_holder {…!r}; got {…!r}; {detail}`), and the first-record form `… possible provenance chain break, not a definite identity mismatch: {detail}; first record must have from_holder null` (`:330-335`, `:339-341`). Tick findings are NOT qualified: `{record_label}.tick: provenance tick {…} must be greater than previous tick {…}` with no identity note (`:323-326`). A null holder field contributes no clause and never triggers qualification (`:169-170`). `{detail}` is `{reference} {id!r} is not uniquely resolvable ({raw} raw entity rows carry this id, but only {indexed} is in the resolved index)` (`:171-175`) | That the chain is definitely broken, or definitely intact — the chain finding's expected or observed holder is not a single row, so the mismatch may be an artifact of the rejected duplicate. It does not make tick order, an integer comparison, uncertain. It also does not name which raw row was rejected; read that row's own `VIOLATION:` line | Repair the duplicate first (rename or merge, per the checklist), rerun, and re-read the chain comparison as a definite finding. A tick line already reads as definite while the duplicate remains. Delivered evidence: `r89-fn2-unresolved-chain-break` (expected side) versus `r89-fn2-control` (unqualified control); CB1's round-90 edge probe adds observed-side, null-observed/expected-unresolved, and unqualified-tick receipts (`CB1.md`) |
+| Two or more causes in one record that passes the key-set check (e.g. bad tick AND ambiguous holder AND unknown source) | Every individual finding is emitted, and the `first stop:` clause names **all** of them, in check order, joined with `; ` — e.g. `malformed record (invalid tick); ambiguous holder identity to_holder 'x'; source reference 'y' absent from raw sources and absent from the resolved index` | A ranking or a single root cause — the clause is an assessment-boundary statement, and the order is the checker's check order, not severity. Nor does it name the item-level causes, which pre-empt it entirely | Read the record's own `VIOLATION:` lines for the full defect list; repair them together. Delivered evidence: `r89-c1-multi-cause-valid` (tick + ambiguity); scratch probe `p3-triple-cause-valid` (tick + ambiguity + unknown source) in `.ufo/waves/round-89/followup/CB1.md` §M4. |
 | Later valid records in an item whose chain is already unassessed | Ordinary record-level diagnostics continue (schema, keys, dangling-vs-unique identity, source status) PLUS the disclosure on each of them; continuity/tick comparisons do not run for the rest of the item, per run | Comparison passed — the repeated disclosure is not a new defect per record, and absence of comparison findings after the stop is NOT a pass | Repair the named first cause, rerun; the gate is per run, so a fresh run after repair can assess the full chain. |
 | `provenance` present but not a list | `{item_label}.provenance: expected array` only — no disclosure is emitted for that item at all | That the (unreadable) contents would have been unassessed — the boundary is stated for the whole item instead | Repair the array shape; rerun. Delivered evidence: `r87-probe-entry-shape` (`entities[4].provenance: expected array`). |
 
@@ -227,6 +249,34 @@
 - Scope: exactly two assessments stop — provenance continuity (next
   `from_holder` equals previous `to_holder`; first record `from_holder`
   null) and tick order (strict increase) — at the first stop and ALL later
+  records of that item. The stop is permanent for that run; no later valid
+  record re-enables it (baseline `:234-237`, `:246-247`; preserved by the
+  contract; delivered latch `:315-321`, comparison gate `:322`).
+- One form, one boundary: the disclosure states the local status and the
+  first stop on every affected record. It is not a finding about the chain —
+  it reports that the comparison did not run. There is no separate item-level
+  notice at `1b09f3f`.
+- Causes are collected, not selected. Inside one record every reached cause
+  is appended in check order and joined with `; ` at the arming record
+  (`:258`, `:315-318`); no cause is dropped in favour of an earlier one. The
+  order of the joined string is the order of the checks: `malformed record
+  (invalid tick)` → `malformed record (invalid from_holder)` → `malformed
+  record (invalid to_holder)` → dangling `to_holder` → dangling `from_holder`
+  → `ambiguous holder identity` → `malformed record (invalid source_id)` →
+  unknown source → `source table unavailable`. Item-level causes (rows 1-3 of
+  the cause table) still pre-empt the record loop, so an item whose provenance
+  sits on a character entity is disclosed as `provenance attached to a
+  non-item entity` alone, even when its records also carry dangling holders
+  and unknown sources (`r61-independent-empty`, `r61-independent-unavailable`).
+- Cause wording separates "no raw row" from "raw row rejected by the field
+  check". The raw counters are accumulated before validation for dict rows
+  whose `id` is a nonempty string (`:72-76`); the resolved index holds only
+  rows that pass every field check (`:82-83`, `:85-91`). A dangling holder or
+  unknown source whose id appears on a rejected raw row is therefore disclosed
+  as `… present in raw entities but absent from the resolved index` (sources:
+  `… present in raw sources but …`), not as truly absent. The local finding
+  lines keep the older shape (`… dangling entity {id!r}`, `… unknown in-world
+  source {id!r}`); only the `first stop:` clause carries the distinction.
 - Comparison findings can be non-definite, but only for holder-identity comparisons. When a
   **non-null** holder id involved in a chain-continuity or first-record comparison has ≥ 2 raw
   entity rows of which exactly one is in the resolved index, the finding is rewritten as
@@ -240,6 +290,57 @@
   round-90 ruling). A plain duplicate whose rows both pass validation cannot reach a
   comparison at all: it makes the referencing record ambiguous and therefore invalid, which
   stops the chain instead.
+- The two r89 hedged shapes are repaired at `ca7f9ef`: a `from_holder: null` follow-on and a
+  tick inversion are definite structural findings, and the qualification above is bounded to
+  chain-continuity/first-record comparisons of genuinely unresolved non-null IDs. A null
+  follow-on whose expected side is itself an unresolved non-null id stays qualified — the
+  break is genuine, the expected holder is not a single row.
+- Emission order is asymmetric: on the record that arms the stop the
+  disclosure is appended after that record's own findings (`:222`, `:249`,
+  `:319-320`); on every later record it is emitted at the top of the record
+  loop, before them (`:214-216`).
+- A duplicated item id arms a separate stop on each duplicate row, each
+  naming its own origin (`entities[3].provenance` and
+  `entities[4].provenance`; probe `C-dupitemid` at r88, `r87-probe-entry-shape`).
+- Everything else continues: JSON loading, field schema, key-set checks,
+  holder shape validation, dangling-vs-duplicate classification, source
+  citation status, global duplicate-ID findings, and all relation,
+  timeline, and contradiction checks.
+- Three states, not two: after the stop the affected comparisons are
+  UNASSESSED — neither clean nor broken. Output alone cannot tell you
+  whether the masked tail contains a break; only resolving the named cause
+  and rerunning can. Do not resume, infer, or announce a break from the
+  stopped input itself. A qualified `possible … not a definite identity
+  mismatch` finding is a fourth, weaker state again: a comparison ran, but
+  one of its identities was not a single row.
+- No truth claims: nothing here asserts a hidden break, true custody,
+  entity identity, canon, source-text support, rights, or game mechanics.
+  The disclosure is about the checker's assessment boundary, not the
+  fictional world. Probe fixtures are authored inputs; chain breaks inside
+  them are injected test scaffolding, not lore.
+- Ambiguous SOURCE is not a stop cause. A source ID resolving to ≥ 2 rows
+  sets `chain_has_ambiguous_source` (`:313-314`) and only prefixes
+  comparison findings with `input-structural finding, not sourced-canon; `;
+  comparisons still run (`r7-item-ambiguous`, `r87-probe-source-prefix`).
+  The qualified FN-2 chain-break form emits that same prefix for a different
+  reason, so the prefix alone no longer identifies an ambiguous source.
+- Chain eligibility is no longer orthogonal to the disclosure: the three
+  conditions that used to disable the chain silently (no sources,
+  non-item entity, duplicated item id) are now named first stops
+  (`:198-203`). Comparisons require sources loaded, `kind == "item"`, and a
+  unique item id — unchanged (`:183` baseline; delivered `:200-205`) — but a
+  chain that was never eligible now says so per record instead of staying
+  silent.
+- Measurement ceiling: `score = 2 × passed` on the five-gate disclosure
+  sample; 10/10 means 5/5 specified gates passed. It is not whole-domain
+  calibration, not saturation, not promotion, and not evidence that an
+  external reader changed behavior. No such score exists for `ca7f9ef`:
+  the helper is absent there.
+
+## Commands (self-contained, run from the lane root)
+
+Delivered replay — the five recorded r85 probe inputs against the checker at
+`ca7f9ef` (run from the lane root; baseline triples for the same five inputs
 are pinned in `reports/round-1/current-baseline.json`):
 
 ```sh
@@ -382,26 +483,30 @@
 `r89-c1-invalid-tick` (`first stop: malformed record (invalid tick) at
 entities[3].provenance[1]`, 4 violations), `r89-c1-invalid-from-holder` (3),
 `r89-c1-invalid-to-holder` (3), `r89-c1-malformed-source-id`
-The six single-cause branches without their own durable fixture each have one now, and replay
-as one cause plus one disclosure per affected record: `r89-c1-invalid-tick` (`first stop:
-malformed record (invalid tick) at entities[3].provenance[1]`, 4 violations),
-`r89-c1-invalid-from-holder` (3), `r89-c1-invalid-to-holder` (3), `r89-c1-malformed-source-id`
-(`entities[2].provenance[1]`, 3). Round-90 added durable fixtures for the two `present in raw …
-but absent from the resolved index` wordings (`r90-c1-rawpresent-to`, `r90-c1-rawpresent-from`,
-`r90-c1-rawpresent-source`) and for a three-cause valid-key record (`r90-c1-three-causes`,
-`malformed record (invalid tick); holder reference to_holder … ; source reference …`); their
-delivered output is pasted in the r90 work wave (`.ufo/waves/round-90/F1.md`) and replayed by
-CB1 at `ca7f9ef`. Still scratch-only, with no durable fixture in the tree: the observed-side and
-first-record FN-2 chain forms, and the null-chain definite form. The tick-under-unresolved-holder
-FN-2 sub-branch no longer exists — r90's integer-only tick reading removed it (seat C9's ruling);
-its would-be fixture was never built and is not owed. Evidence for the remaining shapes is
-CB1's round-90 edge probe (`/__cb1_probe__`, receipts in
-`.ufo/waves/round-90/followup/CB1.md`) and the r90 seats' probes (B3, C5, C9). Round-88's
-scratch evidence for the remaining families (non-dict record, non-item provenance, duplicate
-item id, unavailable source table, both-fields ambiguity at one record, tick-masks-ambiguity) is
-recorded in `/tmp/cb1/probes2`, `/tmp/cb1/probes3` and
+(`entities[2].provenance[1]`, 3).
+
+Round-90 added durable fixtures for the two `present in raw … but absent from the resolved
+index` wordings (`r90-c1-rawpresent-to`, `r90-c1-rawpresent-from`,
+`r90-c1-rawpresent-source`) and for a three-cause valid-key record
+(`r90-c1-three-causes`, `malformed record (invalid tick); holder reference to_holder … ;
+source reference …`); their delivered output is pasted in the r90 work wave
+(`.ufo/waves/round-90/F1.md`) and replayed by CB1 at `ca7f9ef`. Still scratch-only, with no
+durable fixture in the tree: the observed-side and first-record FN-2 chain forms. The
+null-chain definite form is now durably pinned by `r91-c1-null-chain`; the tick-under-unresolved-
+holder FN-2 qualification branch no longer exists under r90's integer-only tick reading, while
+`r91-c1-tick-unresolved` durably pins the definite integer-only tick finding and its separate
+qualified chain-break. Evidence for the remaining scratch-only shapes is CB1's round-90 edge
+probe (`/__cb1_probe__`, receipts in `.ufo/waves/round-90/followup/CB1.md`) and the r90 seats'
+probes (B3, C5, C9). Round-88's scratch evidence for the remaining families (non-dict record,
+non-item provenance, duplicate item id, unavailable source table, both-fields ambiguity at one
+record, tick-masks-ambiguity) is recorded in `/tmp/cb1/probes2`, `/tmp/cb1/probes3` and
 `.ufo/waves/round-88/followup/CB1.md` §3; note that `/tmp` reached inode exhaustion on
 2026-10-17, so that scratch may not survive.
+
+Five-gate measurement entry point (clean chain; unique-holder real break;
+dangling-holder explicitness both fields; ambiguous-to local disclosure plus
+downstream scope/no definite comparisons; ambiguous-from symmetric behavior;
+JSON with `measured_revision`, `total=5`, `passed`, `score=2*passed`, raw
 returncode/stdout/stderr per case; tests the requested revision's checker AND
 input data in isolated temporary trees):
 
@@ -409,7 +514,7 @@
 python3 corpus/fixtures/measure_holder_disclosure.py --revision <commit>
 ```
 
-That helper does not exist at `1b09f3f` — `python3
+That helper does not exist at `ca7f9ef` — `python3
 corpus/fixtures/measure_holder_disclosure.py --revision HEAD` exits 2 with
 `can't open file ... No such file or directory` — so no five-gate score is
 recorded for this tree. Run the helper only in a revision that contains it;
@@ -426,7 +531,17 @@
   baseline paragraph of "The contract" cites; re-checked against
   `git show 5eb9451:corpus/fixtures/check_bible.py` (330 lines) by round-89
   seat CB1.
-- Checker at delivered `1b09f3f` (`corpus/fixtures/check_bible.py`, 435
+- Checker at the r90-delivered tree `ca7f9ef` (`corpus/fixtures/check_bible.py`, 428
+  lines, sha256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`):
+  raw entity/source counters declared `:38-39`, accumulated `:72-76`; schema-valid rows
+  collected `:82-83`; `index()` `:85-91`; sources index `:93`; entities index `:97`; holder
+  count collection `:164-166`; `holder_identity_detail` `:168-175`; relation-endpoint ambiguity
+  precedent `:184`; provenance loop `:187-345`; `only valid on item entities` `:193`;
+  `expected array` + `continue` `:194-196`; item-level first-stop tests `:200-205`; disclosure
+  template `:208-210`; top-of-loop emission `:214-216`; non-dict branch `:217-223`; key-set
+  branch with the shape-invalid holder scan `:224-250`; field validation and cause collection
+  `:251-314`; latch `:315-321`; comparison gate and FN-2 qualification `:322-345`; CLI/exit
+  behavior `:418-428`. The checker stayed byte-identical through r91 closure `396c568`.
   lines, sha256 `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`):
   raw entity/source counters declared `:38-39`, accumulated `:72-76`;
   schema-valid rows collected `:82-83`; `index()` `:85-91`; sources index
@@ -461,89 +576,96 @@
   carry identical transfers `(null→mira,0)`, `(mira→vault,3)`,
   `(harbor→tower,4)`; masked adds a second `vault` row. Isolated carries a
   continuous chain ending in the duplicated `vault` at record `[2]`.
-- In-tree provenance fixtures at `1b09f3f`: 29 directories carry
+- In-tree provenance fixtures at the r90-delivered tree `ca7f9ef`: 33 directories carry
+  `provenance` (29 at `1b09f3f`); 13 provenance records across ten of them reference a duplicated
+  holder id — `r87-masked-break-from-ambiguous`, `r87-masked-break-to-ambiguous`,
+  `r87-probe-multi-invalid`, `r87-probe-nonitem-kinds`, `r87-probe-record-and-chain` (three
+  records), `r87-probe-shape-ambiguous`, `r88-mixed-stop`, `r88-shape-ambiguous-armed`,
+  `r89-c1-multi-cause-valid`, `r89-fn2-unresolved-chain-break` (plus the r85 live probes outside
+  `corpus/fixtures`). The four round-90 fixtures carry provenance but no duplicated holder
+  references (dangling raw-present ids only). `r7-item-ambiguous` is ambiguous SOURCE only;
+  `r61-*` are dangling holders on a non-item entity. Measured by
+  `.ufo/waves/round-90/followup/CB1.md` (r90) and §M7 of the r89 CB1 report. At r91 closure the
+  two additional durable calibration fixtures are `r91-c1-null-chain` and
+  `r91-c1-tick-unresolved`; this is fixture coverage, not a checker change.
-  `provenance`; 13 provenance records across ten of them reference a
-  duplicated holder id — `r87-masked-break-from-ambiguous`,
-  `r87-masked-break-to-ambiguous`, `r87-probe-multi-invalid`,
-  `r87-probe-nonitem-kinds`, `r87-probe-record-and-chain` (three records),
-- In-tree provenance fixtures at `ca7f9ef`: 33 directories carry `provenance` (29 at
-  `1b09f3f`); 13 provenance records across ten of them reference a duplicated holder id —
-  `r87-masked-break-from-ambiguous`, `r87-masked-break-to-ambiguous`,
-  `r87-probe-multi-invalid`, `r87-probe-nonitem-kinds`, `r87-probe-record-and-chain` (three
-  records), `r87-probe-shape-ambiguous`, `r88-mixed-stop`, `r88-shape-ambiguous-armed`,
-  `r89-c1-multi-cause-valid`, `r89-fn2-unresolved-chain-break` (plus the r85 live probes
-  outside `corpus/fixtures`). The four round-90 fixtures carry provenance but no duplicated
-  holder references (dangling raw-present ids only). `r7-item-ambiguous` is ambiguous SOURCE
-  only; `r61-*` are dangling holders on a non-item entity. Measured by
-  `.ufo/waves/round-90/followup/CB1.md` (r90) and §M7 of the r89 CB1 report.
+  `r87-probe-shape-ambiguous`, `r88-mixed-stop`,
+  `r88-shape-ambiguous-armed`, `r89-c1-multi-cause-valid`,
+  `r89-fn2-unresolved-chain-break` (plus the r85 live probes outside
+  `corpus/fixtures`). `r7-item-ambiguous` is ambiguous SOURCE only;
+  `r61-*` are dangling holders on a non-item entity. Measured by
+  `.ufo/waves/round-89/followup/CB1.md` §M7.
+- Round-85 reports: `reports/round-85/r85-author.md` (probe design,
+  `:38-75`), `r85-verifier.md`, `r85-sealed-reviewer.md` (operative danger:
+  correct first action, false sense of finality),
+  `r85-axis-adjudicator.md` (verdict ADMIT, bounded; repair reserved as a
+  separate candidate needing tuple replay).
 - Fleet round-1 evidence: `reports/round-1/current-baseline.json` and
   `reports/round-1/baseline-probes.json` (parent-recorded CLI triples at
   `5eb9451`; all recorded stderr empty); `reports/round-1/critic.md`
   (counterexample table this guidance encodes);
   `reports/round-1/current-dispatch.json` (seat write scopes — seat
   `R1Guide` holds the scope for this file).
-- Rules text: `corpus/fixtures/README.md:110-119` (provenance discipline,
+- Rules text: `corpus/fixtures/README.md:110-119` (provenance discipline, no inferred history,
+  citation ≠ support) and `:121-128` (round-7 duplicate-source rule mirrored by this holder
+  contract). The README carries `## Round 88` (`:1008-1011`) and `## Round 89` (`:1012-1015`)
+  sections. There was no `## Round 90` section at `ca7f9ef`; it landed in the subsequent r90
+  closure at `a7c6a17` and documents the r90 fixtures. The r87 decision table
+  (`corpus/knowledge/r87-provenance-chain-decision-table.md`) is superseded and still quotes
+  removed strings; treat it as history.
-  no inferred history, citation ≠ support) and `:121-128` (round-7
-  duplicate-source rule mirrored by this holder contract). The README's
-  `## Round 88` section (`:1008-1012`) states the r88 stop-cause repair and
-  points readers to this document as the contract; there is no
-- Rules text: `corpus/fixtures/README.md:110-119` (provenance discipline, no inferred history,
-  citation ≠ support) and `:121-128` (round-7 duplicate-source rule mirrored by this holder
-  contract). The README carries `## Round 88` (`:1008-1011`) and `## Round 89` (`:1012-1015`)
-  sections; the Round 89 section states the r89 cause branches and points readers to this
-  document as the first-stop cause contract. There is no `## Round 90` section at `ca7f9ef`, so
-  the r90 integer-only tick reading, the null guard, and the four new fixtures are stated only
-  here (and in the r90 wave artifacts) until a Round 90 section lands. The r87 decision table
-  (`corpus/knowledge/r87-provenance-chain-decision-table.md`) is superseded and still quotes
-  removed strings; treat it as history.
-- OBSERVED on the delivered tree (round-89 seat CB1, `1b09f3f`; exact
-  commands and output in "Commands" and
-  `.ufo/waves/round-89/followup/CB1.md`): the five r85 probe triples pasted
-  above (byte-identical to the r88 replay); the six durable r88/r89
-  non-holder-cause fixture outputs pasted above; the multi-cause fixture and
-  the FN-2 fixture pair pasted above; the six r89 single-cause fixtures; the
-  165-directory two-revision census (0 exit changes, 0 stderr changes, 9
-  changed stdout tuples); the 29-directory provenance inventory with 13
-  duplicated-holder records.
-- OBSERVED only in scratch probes at `1b09f3f` (no durable fixture): both
-  `present in raw … but absent from the resolved index` wordings; a
-  three-cause valid-key record; the four FN-2 sub-branches (expected-side,
-  observed-side, tick, first-record). Command form and output in
-  `.ufo/waves/round-89/followup/CB1.md` §M5-§M6.
-- OBSERVED only in round-88 scratch probes at `2ea9ef1` (no durable fixture
-  of their own; some now covered by older fixtures): non-dict record
-  (`r87-probe-record-and-chain`), both-fields ambiguity at one record
-  (`r87-probe-record-and-chain`), non-item provenance and unavailable source
-  table (`r61-*`), duplicate item id (`r87-probe-entry-shape`). Evidence in
+  `## Round 89` section at `1b09f3f`, so the r89 amendments (multi-cause
+  summary, raw-vs-resolved wording, FN-2 qualification) are stated only
+  here. The r87 decision table
+  (`corpus/knowledge/r87-provenance-chain-decision-table.md`) is superseded
+  and still quotes removed strings; treat it as history.
+- Lane declaration: `SCORECARD.md` fleet-round-1 calibration declaration
+  (unmeasured tie, falsifiability tie-break).
+
+## Status split
+
+- OBSERVED on the delivered trees (round-89 seat CB1 at `1b09f3f`; round-90 seat CB1 at
+  `ca7f9ef`; exact commands and output in "Commands" and the respective CB1 reports): the five
+  r85 probe triples pasted above; six durable r88/r89 non-holder-cause fixture outputs; the
+  multi-cause fixture and FN-2 fixture pair; six r89 single-cause fixtures; 14/14 pasted-block
+  parity at r90; and the r90 fixture-only census (160 → 164 directories, 0 changed tuples, 0
+  exit changes, 0 stderr). The r89 165-directory count includes 160 fixture directories plus
+  five live r85 probes; it is a different scope. The r90 provenance inventory is 33 directories
+  with 13 duplicated-holder records across ten fixtures. The two r91 calibration fixtures
+  `r91-c1-null-chain` and `r91-c1-tick-unresolved` were added later; their README outputs were
+  independently replayed against both the e97613c and delivered checkers, and differ only on the
+  intended repaired lines.
+- OBSERVED only in scratch probes at `ca7f9ef` (no durable fixture): the observed-side and
+  first-record FN-2 chain forms. The null-chain definite form is durably pinned by
+  `r91-c1-null-chain`; the old tick-under-unresolved-holder qualification branch was removed by
+  the integer-only tick ruling, and `r91-c1-tick-unresolved` now pins the definite tick line
+  while preserving the separate qualified chain break. Round-90 edge-probe commands and output
+  are in `.ufo/waves/round-90/followup/CB1.md`.
+- OBSERVED only in round-88 scratch probes at `2ea9ef1` (no durable fixture of their own; some
+  now covered by older fixtures): non-dict record (`r87-probe-record-and-chain`), both-fields
+  ambiguity at one record (`r87-probe-record-and-chain`), non-item provenance and unavailable
+  source table (`r61-*`), duplicate item id (`r87-probe-entry-shape`). Evidence in
   `.ufo/waves/round-88/followup/CB1.md` §3, scratch under `/tmp/cb1/`.
-- OBSERVED at baseline `5eb9451` (parent-recorded JSON): masked and
-  isolated emitted ONLY the global duplicate; unique control emitted the
-  definite record-2 break; control was CLEAN; harbor-repro showed
-  timeline-endpoint ambiguity voiced while holder references stayed
-  silent.
-- SUPERSEDED: the r87 two-notice contract (`2b48ca7`) and its replay block;
-  preserved in `.ufo/waves/round-87/followup/I2.md` and
-  `corpus/knowledge/r87-provenance-chain-decision-table.md`. The latter still
-  quotes both removed notice strings (measured at `1b09f3f`: `:60`, `:61`,
-  `:99`, `:169-172`, `:179-182`, `:216-218`, `:222-223`, `:238-240`,
-  `:268-269`, `:271`, `:281-283`) and still expects r87-era output (row 33,
-  `:104`: an `item-level notice` the delivered checker never prints); it is
-  marked SUPERSEDED-and-pinned at its header (r88 closure) anywhere in the tree.
-- REPLAYED, not scored: no five-gate `passed` count exists for `1b09f3f`;
-  the documented helper is absent at that revision.
-- UNKNOWN / UNMEASURED: whether any fixture outside the 29 listed above
-  combines `provenance` with a duplicated holder id (none does in
-  `corpus/fixtures`); any external reader behavior change; whether a raw row
-  rejected for a non-`id` field can ever leave a dangling reference whose
-  id it does not carry (it cannot, by construction — the raw counter is
-  keyed on the row's own `id`).
+- OBSERVED at baseline `5eb9451` (parent-recorded JSON): masked and isolated emitted ONLY the
+  global duplicate; unique control emitted the definite record-2 break; control was CLEAN;
+  harbor-repro showed timeline-endpoint ambiguity voiced while holder references stayed silent.
+- SUPERSEDED: the r87 two-notice contract (`2b48ca7`) and its replay block; preserved in
+  `.ufo/waves/round-87/followup/I2.md` and
+  `corpus/knowledge/r87-provenance-chain-decision-table.md`. The latter still quotes both removed
+  notice strings (measured at `1b09f3f`: `:60`, `:61`, `:99`, `:169-172`, `:179-182`,
+  `:216-218`, `:222-223`, `:238-240`, `:268-269`, `:271`, `:281-283`) and still expects r87-era
+  output (row 33, `:104`: an `item-level notice` the delivered checker never prints); it is marked
+  SUPERSEDED-and-pinned at its header (r88 closure) anywhere in the tree.
+- REPLAYED, not scored: no five-gate `passed` count exists for `ca7f9ef`; the documented helper
+  is absent there.
+- UNKNOWN / UNMEASURED: whether any fixture outside the listed in-tree census combines
+  `provenance` with a duplicated holder id; any external reader behavior change; whether a raw
+  row rejected for a non-`id` field can ever leave a dangling reference whose id it does not
+  carry (it cannot, by construction — the raw counter is keyed on the row's own `id`).
 
 ## Measured results (parent-owned slot)
 
-No five-gate score is recorded for the delivered tree `1b09f3f`: the
-documented measurement helper is absent at that revision. The behavioral
-replay that stands in for it is the five-case delivered output pasted under
-"Commands", the durable fixture outputs pasted there, and CB1's scratch
-cause/precedence/FN-2 probes recorded in
-`.ufo/waves/round-89/followup/CB1.md`; every contract, table, and limits line
-above is stated as-of that replay.
+No five-gate score is recorded for the delivered tree `ca7f9ef`: the documented measurement
+helper is absent at that revision. The behavioral replay that stands in for it is the five-case
+delivered output pasted under "Commands", the durable fixture outputs pasted there, the 14/14
+pasted-block replay, the r90 census, and CB1's scratch cause/precedence/FN-2 probes recorded in
+`.ufo/waves/round-90/followup/CB1.md`; every contract, table, and limits line above is stated
+as-of that replay.
