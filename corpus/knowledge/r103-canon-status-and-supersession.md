source: S024 — https://www.mediawiki.org/wiki/Wikibase/DataModel/Primer — §Statements and §Ranks (oldid 8399774); S025 — https://www.wikidata.org/wiki/Help:Ranking — §What ranks are not and §Deprecated rank (accessed 2026-10-19); S026 — https://www.w3.org/TR/prov-dm/ — §5.1.8 Invalidation, §5.2.2 Revision, §5.5.2 Alternate (REC-prov-dm-20130430); S027 — https://en.wikipedia.org/wiki/Star_Wars_expanded_to_other_media — §Holocron database and canonicity (accessed 2026-10-19; tier-C illustration only, never canon support)
verified-at: 2026-10-19
recheck: re-run `grep -rniE 'retcon|canon[ -](tier|status)|supersed' corpus/knowledge corpus/fixtures corpus/tools` each round and before integrating any cluster that declares a supersession, rank, or canon-tier record; re-open S024–S026 on a 180d cadence or before the lane encodes rank semantics in a checker.
coverage-row: CM-e

# Canon status and supersession of in-world records (CM-e)

Verification record (2026-10-19): all four cited sources opened in-round; the negative sweep below re-run (0 hits for `retcon`, 0 canon-tier hits); `corpus/fixtures/check_bible.py` and the r101 R10 record re-read for the line cites used here. Admitted at the round-103 Q06 gate (`corpus/lessons/round-103.md` `## Gate`).

## The decision this settles (Q06)

When a later in-world record contradicts, corrects, or declares an earlier account void, which lane records change — may the earlier claim be overwritten or deleted, and who may mark an account superseded? The baseline corpus leaves this unsettled: the sweep

```
grep -rniE 'retcon|canon[ -](tier|status)|supersed' corpus/knowledge corpus/fixtures corpus/tools SKILL.md PROVINCE.md corpus/README.md | grep -vE 'editorial|addendum|ledger convention|debt ledger'
```

returns 0 in-world governance hits (run 2026-10-19; the only matches are dated *editorial* supersessions of lane prose, e.g. `corpus/tools/README.md:296`, never record-level canon rules). `PROVINCE.md:9` refuses uncited canon and silent contradiction resolution but states no procedure for a *declared* supersession. `contradictions.json` preserves incompatible pairs but has no status or outcome field (`corpus/fixtures/check_bible.py:31`). This entry settles that concrete decision.

## Method grounds (opened in-round)

Wikibase models assertions, not facts: "Wikibase will not be about the truth, but about statements and their references." (S024 §Statements, oldid 8399774). Three consequences for the lane's method:

- **Rank is presentation, not deletion.** Wikibase's three ranks — preferred, normal, deprecated — select which statement answers a query without removing the rest; deprecated covers "statements that are being discussed, or known to be erroneous, but still listed for the sake of completion" (S024 §Ranks). The superseded record is still a record.
- **Deprecation is a mark, not an erasure.** Wikidata's help states that "Marking erroneous statements as deprecated instead of simply deleting such statements has three benefits" (S025 §Deprecated rank): others learn not to re-add the value, the evolution of ideas stays legible, and the base remains a secondary record of what sources claimed.
- **Rank does not adjudicate.** Ranks "are not a way of asserting your view for a disputed value" (S025 §What ranks are not); a disputed value stays disputed. The lane's `unresolved` status is the same move.

PROV-DM separates three relations the lane's vocabulary currently conflates:

- **Revision** — "a revision is a derivation for which the resulting entity is a revised version of some original" (S026 §5.2.2). The original still exists as its own entity; revision is a link between two existing records, not an in-place edit.
- **Invalidation** — "the start of the destruction, cessation, or expiry of an existing entity by an activity" (S026 §5.1.8). Something ends an entity's availability; in lane terms the *marking* is an act that needs its own record and source.
- **Alternate** — "Two alternate entities present aspects of the same thing" (S026 §5.5.2). Two accounts of one referent coexist; neither cancels the other — exactly the contradictions ledger's posture.

As a tier-C illustration only, the Holocron precedent shows that tiered canon is a declared licensing convention, not a derivable fact: the franchise database "was divided into five levels of canon (in order of precedence)" and an entire corpus was later "declared it non-canonical" by owner declaration on a single date (S027). Tiers exist because someone with authority declared them; absent that declaration, there is no tier to check.

## Append sequence for a declared supersession

1. Land the new account as an ordinary sourced claim/event/relation with its own `source_id` resolving in `sources.json`. Nothing about its content confers supersession authority (Q02).
2. If the new account *declares* the earlier one void, encode that declaration as its own sourced statement or a `supersedes`-type relation citing the declaring document.
3. If the pair is supported-incompatible — same referent, field, occasion, incompatible assertions — append a `contradictions.json` row or route cross-cluster to the R10 register; both accounts stay.
4. Annotate the earlier record's context by append (a dated addendum or declared-convention file), never by rewriting or deleting it.
5. Editorial (out-of-world) retcons ride a declared convention record, not an in-world source row; `sources.json` rows name in-world documents only.

## Decision table: supersession in this lane's records

| Situation | Record decision | Required citation and boundary |
|---|---|---|
| A later in-world record contradicts an earlier one | Both stay. The later account is a new claim/event/relation carrying its own `source_id`; the earlier record is never overwritten or deleted (append-only). If the pair is supported-incompatible, add a `contradictions.json` row or route to the R10 register. | The new record's own in-world source. PROV-DM `alternateOf`: two accounts of one thing coexist without one erasing the other (S026 §5.5.2). |
| A later in-world record *declares* an earlier account superseded ("the corrected filing", "record X was struck from the minutes") | Encode the declaration as a sourced claim (or a `supersedes`/`invalidates` relation type) citing the declaring source. The earlier record stays, now carrying the context that a source declared it void. | The declaring in-world document's `source_id`. Q02: a `superseded` label never authenticates itself — it is a claim like any other, needing statement + resolvable `source_id` (`check_bible.py:156-161`). |
| An editor (out-of-world) marks an account deprecated or retconned | Record it as editorial metadata *outside* `sources.json` in-world sources — a dated addendum, editorial row, or declared convention file — never as an in-world source. | Editorial encodings must be labelled editorial (Q04); the lane's own dated-addendum convention (`corpus/tools/README.md:296`; the `dated supersession` bullets under SKILL.md `### Dependency-edge freeze check`) is the precedent form. |
| Canon tiers across media/editions/series of the fiction | A tier ordering is a *declared convention*: it may only be enforced if a declared convention record (in-world canon law, or an editorial declaration file) states it. Without one, no tier ordering exists and none may be checked. | Q01: a predicate fails a bible only where a declared convention makes the property obligatory; undeclared tier conflicts warn (exit 0) or route an L0 question, never fail. S027 illustrates that tiers are owner declarations, not derivable facts. |
| Two accounts stand unresolved and a "canon answer" is requested | Refuse to pick. `check_bible.py:2` reports, never resolves; `PROVINCE.md:9` refuses canon without an in-world citation and silent resolution. | Wikidata: ranks communicate consensus and are "not a way of asserting your view for a disputed value" (S025). An unresolved pair stays `unresolved`. |

## In-world revision vs out-of-world retcon

These must not be conflated.

An **in-world revision** is an event inside the fiction: a clerk's corrected filing, a re-dated minute, a recanted testimony. It enters as a new sourced record, may pair into `contradictions.json`, and resembles PROV-DM revision — the corrected record "is a revised version of some original" that still exists (S026 §5.2.2). Both the original and the revision remain citable.

An **out-of-world retcon** is an authorial act about the fiction: it changes what the world-bible asserts without any in-world event. The lane has no fixture or check for it; encoding one requires a declared editorial convention (a dated addendum naming the revised assertion, its superseded text, and the authorial warrant).

PROV-DM invalidation marks an entity's end (S026 §5.1.8); a retcon never deletes the earlier record. The append-only rule means the superseded assertion remains, marked — exactly as Wikibase keeps deprecated statements "for the sake of completion" and to prevent re-adding (S024 §Ranks; S025).

## Interaction with the R10 register and the contradictions ledger

The R10 register `corpus/knowledge/cross-cluster-contradictions.md` (not yet created: it opens only when the first supported incompatible pair lands) admits only supported *incompatible* pairs and preserves both accounts (`corpus/knowledge/r88-sourced-inspiration-decision-table.md:93-97`); the r101 worked record demonstrates a compatible pair creates no entry (`corpus/knowledge/r101-r10-register-first-entry.md:25`).

A declared supersession does **not** remove a register pair or a ledger row: `unresolved` records that two sources conflicted, which remains true even after a third source declares a winner. The declaring source's record is appended beside the pair, and a register note may record the declaration — but the earlier account is never rewritten to agree.

Identity, custody, and the declaration each carry their own source (Q03).

## What `check_bible.py` does NOT do here (line cites)

- The contradictions schema is `{id, claim_a, claim_b, why}` — no status, outcome, winner, or supersession field exists to check (`check_bible.py:31`).
- Claim sides may only name `event_id` plus a field in `{'place_id','tick','depends_on'}` (`:118`); no claim-status or rank field is admitted.
- Validation is shape and reference resolution only (`:119-150`): each side must resolve to exactly one timeline event with a resolvable `source_id`; identical sides are rejected (`:146-150`). Values are never compared, ranked, or reconciled.
- Entity claims require a nonempty `statement` and `source_id`, nothing more (`:156-161`); a `supersedes` assertion is just another sourced claim.
- The checker prints `no canon changed` even on violations (`:426`) and `CLEAN` certifies only "schema, citations, relations, timeline" (`:428`). Any future canon-tier predicate needs a declared convention before it may fail a bible (Q01).

## Falsifiable claims and falsifiers

1. The baseline contains no in-world canon-governance rule. Falsifier: one durable file matching the sweep above that governs `retcon`/tier/supersession of records (editorial supersessions excluded).
2. `contradictions.json` rows cannot encode a winner/status under the delivered schema. Falsifier: a contradictions field other than `id/claim_a/claim_b/why` accepted by `check_bible.py` at its delivered `FIELDS` (:31).
3. Every `supersedes`/`retcon`/`deprecated` marker on a record must itself cite a source (in-world) or a declared editorial convention. Falsifier: an admitted marker justified only by its own label (Q02 violation).
4. No checker may fail a bible on canon-tier grounds absent a declared tier convention. Falsifier: a check that exits 1 on tier ordering with no declared-convention input (Q01 violation).
5. Superseded accounts remain in the corpus. Falsifier: a lane edit that deletes an earlier sourced record to enforce a supersession.

## Scope limits

This entry governs records the lane owns — `entities.json` claims, `relations.json`, `timeline.json`, `contradictions.json`, the R10 register, and declared editorial conventions.

It does not authenticate any fictional source, decide which account is true, grant rights or training permission, or certify real-world "canon" claims.

S027 is tier-C illustration: community/secondary art informs method and never establishes in-world canon or sole support.

S024–S026 describe real-world data models; they shape this entry's *method* (rank, revision, invalidation, alternate), not any fictional content. Real-world source appraisal remains chousa's province (SKILL.md:7-9).

