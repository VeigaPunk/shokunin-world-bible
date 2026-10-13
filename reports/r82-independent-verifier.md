# Round 82 independent verifier — pinned baseline and source-pointer audit

## Scope and method

Pinned baseline: `7876a15fb4784e77e2a4062758d65bdafbacc8b7` (the current `HEAD`). I independently made a `git archive` of `.shokunin/lore/corpus` and extracted it outside the repository to `/tmp/r82-independent-7876a15/`. No corpus candidate was tested. I did not edit corpus, checker, config, or `LOG.md`, and did not commit, push, or merge. The only file I am writing is this report.

## Baseline corpus and checker replay

Compared root-relative corpus path sets and raw file bytes between the pinned archive and worktree:

- Pinned archive: **1,356 files**; worktree: **1,356 files**.
- Same paths and byte-identical contents: **1,356/1,356**; changed, missing, or extra paths: **0**.
- The pinned checker SHA-256 is `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`.
- No `r82` candidate/path occurs in the pinned corpus.

Enumerated the **132** fixture directories at the pin. For every fixture, from both the archive root and worktree root, ran the same root-relative command:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

Compared raw `(exit status, stdout bytes, stderr bytes)` tuples without normalization: **132/132 exact matches**, consisting of **27 exit 0** and **105 exit 1**, with no mismatch. This verifies pinned-baseline preservation and CLI parity only; no candidate checker result is claimed.

## Exact r35 source-to-structure trace

The inspected corpus files are authored fictional materials. `fixtures/r35-bell7-conflict/sources.json` identifies `tarin-note` as a newly authored fictional first-person note reporting Tarin's observation, and `sella-bell7-note` as a newly authored fictional account reporting Sella's claimed presence; neither reliability note calls it omniscient truth.

- Tarin's excerpt says: “I, Tarin, saw Sella place an unlabeled paper envelope on the Lantern Harbor registry desk during Bell-7, the sole seventh-watch registry-bell sounding on the seventh day of Embermonth, year 12.” Its second paragraph explicitly says Bell-7/date are claims in the fictional note, not authenticated chronology, clock time, or timeline tick.
- This is attributed structurally to `tarin-note`: `timeline.json` `/2`, event `tarin-envelope-observation`, has `entity_id: tarin`, `place_id: harbor`, `source_id: tarin-note`; `entities.json` `/5/claims/0` records the placement as Tarin's report about Sella. The `harbor` place is the reported observation scene, not evidence that Sella was there independent of Tarin's report.
- Sella's excerpt says she was physically at North Tower throughout “that same Bell-7 ringing,” was not at Lantern Harbor during it, and calls Bell-7 the sole seventh-watch registry-bell on that same stated seventh day. It likewise limits the label/date to claims in a fictional note.
- Its structural pointer is `timeline.json` `/3`, event `sella-bell7-presence`, with `entity_id: sella`, `place_id: tower`, `source_id: sella-bell7-note`. The `tower` field represents Sella's own reported location. `contradictions.json` `/0` (`bell7-location-reports`) points `claim_a` to event `/2` `place_id` and `claim_b` to event `/3` `place_id`; its rationale conditions the apparent conflict on name/place alignment and both accounts referring to the stated occasion. It distinguishes Tarin's observation scene from Sella's location and keeps both reports unresolved.
- `manual-clause-pointer-map.md` expressly calls itself an editorial map, not a checker guarantee. Equal `tick: 3` values are local sequence labels, not date, clock time, simultaneity, synchronization, or proof of a shared ringing. Source IDs and pointers show fixture attribution/structure, not authenticity, truth, or entailment.

## r36 eighth-day contrast

In `fixtures/r36-bell7-wrong-date/`, Tarin's excerpt remains dated to the seventh day while the changed Sella excerpt explicitly says the eighth day, despite retaining “that same Bell-7.” The copied `timeline.json` Sella event description and `contradictions.json` rationale still say seventh day. `date-contrast-map.md` accurately describes those structured clauses as inherited and stale relative to the changed excerpt. The exact source-text comparison therefore does not establish one shared occasion in r36; the repeated Bell-7 wording and equal local tick do not cure the stated date difference. This comparison does not establish either account false or settle fictional chronology/canon.

## Sealed reader reports: stated decision evidence

I read the two sealed reader reports after their recorded initial answers. Their own descriptions of the before/after evidence are:

- `r82-baseline-reader.md` says its pre-proposal answer requested a contemporaneous, uniquely identified ringing record and underlying notes connecting **each** account to that identifier; separately, Tarin's original observation/identification evidence and an independent, same-interval Sella location record. It says the existing r35/r36 materials already identify the unresolved assumptions but do not themselves direct those specific record requests. In its post-read reflection, it says the proposal's requests substantially match its initial choices and that it cannot claim a materially different action.
- `r82-proposal-reader.md` says its pre-proposal answer requested independently attributable, scope/completeness-checked links from each account to one identified ringing, then separately tested person identification and the Harbor-scene versus Sella-location distinction. Its reflection says this is more operationally explicit than the maps, but its sealed baseline independently reached substantially the same evidence-seeking actions; it characterizes the difference as specificity/guardrail refinement rather than a materially different next action, including against the general r74 evidence-request pattern.

These entries report the readers' actual stated before/after choices, not a new adjudication of materiality by me. They also do not demonstrate that any requested record exists. The baseline archive has no r82 corpus candidate; this replay says nothing about candidate quality.

## Limits

This verifier establishes raw baseline corpus parity, raw CLI parity, and the contents/pointers of the cited authored fictional files. It does not establish source authenticity, independent corroboration, any report's truth, canon, real-world rights or permissions, or mechanics. No evidence request above is asserted to be fulfilled or to identify a real artifact.
