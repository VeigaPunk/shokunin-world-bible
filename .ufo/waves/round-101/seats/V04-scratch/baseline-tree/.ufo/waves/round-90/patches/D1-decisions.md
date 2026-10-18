# D1 — R8–R10 decision appendices (proposal)

**Target:** append the following three clarifications after the R10 table row and before `## Integration boundary` in `corpus/knowledge/r88-sourced-inspiration-decision-table.md`. They clarify the current rows; they do not change schemas, create fixtures, or assert new canon. The current r87 ETCSL inspiration note already carries its R8 element marker; the R8 example below is a separate hypothetical unrecorded-influence case.

Axes: governance completeness, traceability, bounded verification.

### R8 appendix — plausible influence without a record

**Owner:** the lore integration owner opens and maintains the record; the creator supplies the best available provenance account. The reviewer identifies the specific element, proposed source, and evidence that triggered review.

**Trigger:** a named source is plausibly linked to an element by a specific correspondence beyond a commonplace motif, or the creator/reviewer raises a possible source-use claim, but no contemporaneous provenance note records it. A generic resemblance alone is not evidence that the source was consulted and does not trigger a presumption of influence.

**Decision:** opening the review is not a finding that the source influenced the element. The integration owner records a dated `possible influence: unverified` note and marks the affected element in the note/map `external-only / unverified inspiration`; create the note/map entry if neither exists. Do not invent a contemporaneous record or silently classify the case as R2. Request a creator account. If the creator states no source was consulted and review finds only a commonplace motif, record the dated response and basis, remove the provisional unverified marker, then R2 may apply (a named parallel still requires R1 citation). If the creator confirms use of only a general motif, record that account as retrospective, keep the marker and independent in-world support, and the element may remain newly authored fiction under R8. If the account is unavailable, disputed, or identifies distinctive expression/sequence, keep the question open in `l0-questions.md` and withhold only the affected element from supported canon until resolved or re-derived. Rights and training permission remain separate open questions.

**Worked example:** a creator tells the integrator that a proposed low-water crossing may have been influenced by a named myth, but has no contemporaneous provenance note; review finds only a commonplace threshold motif. The integrator records `possible influence: unverified`, adds the element marker (creating the note/map entry if needed), and requests the creator's account; the possibility is not promoted to a source-use fact. If the creator later confirms only general-motif influence, the dated retrospective record preserves the marker and independent in-world support, but does not use the undelivered myth text as evidence. If no account arrives, the element remains withheld rather than being presumed original under R2.

**Verification command (textual completeness only; it does not adjudicate influence):**

```sh
python3 -c 'from pathlib import Path; s=Path(".ufo/waves/round-90/patches/D1-decisions.md").read_text(); a=s.split("\n### R8 appendix",1)[1].split("\n### R9 appendix",1)[0].split("**Verification command",1)[0]; keys=("Owner:","Trigger:","Worked example:","possible influence: unverified","external-only / unverified inspiration","l0-questions.md"); miss=[k for k in keys if k not in a]; print(f"R8 proposal completeness: {len(keys)-len(miss)}/{len(keys)}"); raise SystemExit(bool(miss))'
```

### R9 appendix — named translator, unknown source version

**Owner:** the lore integration owner checks source identity/version and translation evidence; the excerpt submitter supplies the available bibliographic details. If those cannot be established, the owner records the limitation rather than inferring it.

**Trigger:** an excerpt is declared as a translation and names a translator, but the source text or version cannot be identified or verified, while a claim proposes to rely on it as R5 source-text support.

**Decision:** keep the true `Delivery mode: translation` in both excerpt and map; record the translator and `Source text/version: unidentified; unverified`. The translation is delivered, but is not eligible for R5 source-claim support until it is tied to an identified source text/version and reviewed. Do not label the delivered translation itself `not delivered`. If the underlying source text is in fact absent from the corpus, label that source text `not delivered / unverified`; do not infer absence when it has not been checked. The excerpt may support only a carefully attributed statement about what that unverified translation says, not a source-text claim. If source/version evidence is later established, recheck the translation and claim before granting source support; otherwise use a verified version or cite an actual intermediary as such. A mode label or matching anchor alone proves neither identity nor fidelity.

**Worked example:** a delivered line reads “The keeper set the ring upon the fourth stair.” Its excerpt header names M. A. Translator, but no source title or version can be established. The excerpt and map retain `Delivery mode: translation`, note `Source text/version: unidentified; unverified`, and exclude the line from R5 source-claim support. The translation is not described as absent; if its underlying source text is confirmed absent, only that source text receives `not delivered / unverified`.

**Verification command (textual completeness only; it does not verify a translation):**

```sh
python3 -c 'from pathlib import Path; s=Path(".ufo/waves/round-90/patches/D1-decisions.md").read_text(); a=s.split("\n### R9 appendix",1)[1].split("\n### R10 appendix",1)[0].split("**Verification command",1)[0]; keys=("Owner:","Trigger:","Worked example:","Delivery mode: translation","Source text/version: unidentified; unverified","not eligible for R5 source-claim support","not delivered / unverified"); miss=[k for k in keys if k not in a]; print(f"R9 proposal completeness: {len(keys)-len(miss)}/{len(keys)}"); raise SystemExit(bool(miss))'
```

### R10 appendix — matching name, different occasions

**Owner:** the lore integration owner performs and records the comparison; the owners of both clusters provide source pointers and occasion evidence. A reviewer checks the proposed identity and scope before a conflict is registered.

**Trigger:** an integration comparison finds matching referent names or IDs across clusters, including records whose stated occasions differ. A matching string is a candidate-search key only: the same name or ID is not proof of identity.

**Decision:** establish referent type, identity, claim field, and temporal/occasion scope from the in-world sources. For event claims, different source-supported occasions mean distinct event occurrences unless the sources establish that they describe the same single event; ticks, names, and IDs alone do not establish that. For entity claims, different occasions alone do not prove different entity identity; compare the scope of the assertions and whether they can coexist. A contradiction requires supported identity, overlapping relevant scope/occasion, and incompatible assertions about the same field.

Record every compared-and-dismissed name/ID overlap in the incoming cluster's `README.md` under `## R10 comparison outcomes`, with both cluster paths and claim pointers, the compared occasions/scope, and the reason it is not a contradiction. If identity or occasion remains unestablished, record the candidate and missing evidence in that section and append an operator question to `l0-questions.md`; preserve both claims and do not add a candidate to the live contradiction register. Only a supported incompatible pair goes in `corpus/knowledge/cross-cluster-contradictions.md` with the R10 fields and `unresolved` status. A per-cluster checker result is not evidence for this manual cross-cluster decision.

**Worked example:** two hypothetical clusters use `moon-basin-vow` as a timeline event name/ID. One source places an occurrence at Mother-Tide Gate on Saltmonth 4; another places an occurrence at Reed Arch on Saltmonth 9 and describes a later ceremony. The shared string does not prove one event; with the different occasions supported, record the comparison as dismissed in the incoming cluster README and add no live-register entry. If either source instead asserts that both pointers describe the same single vow but its occasion is unresolved, record a candidate and missing evidence in the README and `l0-questions.md`, not as a confirmed contradiction. If evidence later establishes one shared occasion and incompatible places, then add the unresolved pair to the live register.

**Verification command (textual completeness only; it does not prove cross-cluster identity):**

```sh
python3 -c 'from pathlib import Path; s=Path(".ufo/waves/round-90/patches/D1-decisions.md").read_text(); a=s.split("\n### R10 appendix",1)[1].split("**Verification command",1)[0]; keys=("Owner:","Trigger:","Worked example:","same name or ID is not proof of identity","different occasions","README.md","l0-questions.md","cross-cluster-contradictions.md","overlapping relevant scope/occasion"); miss=[k for k in keys if k not in a]; print(f"R10 proposal completeness: {len(keys)-len(miss)}/{len(keys)}"); raise SystemExit(bool(miss))'
```

## Integration boundary

These are proposed governance clarifications, not checker changes. Their verification commands only confirm that the draft contains the specified decision elements; each applied case still requires the named manual source and scope review. No corpus, fixture, register, or other seat artifact is changed by this patch.
**Adjacent method reference (not a transfer of lore authority):** chousa's source boundary refuses URL targets without fetching and checks claims against byte-exact local spans (`chousa-shokunin/corpus/knowledge/claim-verification-r2.md:45–58`); lore's R8 disposition remains governed by this appendix.
**Adjacent fidelity/anchor limits (reference only):** chousa documents that a clean conversion does not verify the original and notes substring-based anchor limits (`chousa-shokunin/corpus/knowledge/archives-verified-r9.md:177–185; chousa-shokunin/corpus/knowledge/anchor-boundaries-r4.md:31–37`); this lore R9 appendix governs delivery-mode and support eligibility.
