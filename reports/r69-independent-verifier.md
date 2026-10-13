# Round 69 independent verifier — pinned baseline preservation and probes

## Verdict and scope

**No candidate was present or validated.** This report independently verifies the pinned no-change baseline and replays the requested ledger controls against an archived copy of that baseline. Preservation of old behavior is not candidate validation and does not establish that the declared gate improves calibration. The matched probes show the current behavior, including a same-reference finding for empty references and for matching valid IDs with invalid fields; they do not decide whether suppressing either finding would be beneficial.

No checker, fixture, or other repository file was changed by this verifier. No source-text, canon, rights, chronology, or game-mechanics conclusion is made.

## Pinned archive and full corpus comparison

The Round 69 declaration in `.shokunin/lore/LOG.md` pins clean baseline `583f97e40f0c5d0bcd0c51be1a408e7d3005b9c6`. `git rev-parse HEAD` returned that exact hash. I made an independent archive outside the repository at `/tmp/lore-r69-independent-583f97e` with `git archive 583f97e40f0c5d0bcd0c51be1a408e7d3005b9c6 .shokunin/lore/corpus/fixtures | tar -x ...`.

A recursive relative-path-to-raw-bytes comparison of archived `.shokunin/lore/corpus/fixtures` against the working-tree directory found **709/709 files with identical paths and bytes**: 0 missing paths, 0 extra paths, and 0 differing file contents. This includes the fixture corpus and its checker. The fixture tree contains 130 fixture directories.

From the archive root and from the working tree root, I ran the archived and working-tree checker respectively for each of the 130 fixture directories, capturing process return code, raw stdout bytes, and raw stderr bytes as tuples. Results were **130/130 identical tuples**; all 130 stderr streams were empty. Thus the current corpus/checker behavior matches the pinned baseline. Because no candidate checker was supplied, this is strictly a baseline preservation comparison, not candidate regression validation.

## Matched baseline probes

To isolate the requested cases, I copied archived fixture `r62-loaded` to temporary directories outside the repository and changed only each temporary `contradictions.json` pair. I ran the pinned archived checker on each. All probes have exit code 1 and empty stderr. The copied base also emits the unrelated existing `timeline[3].source_id: unknown in-world source 'missing-sella-note'` finding; it is present in the outputs below and is not attributed to the pair condition.

| Probe | Pair input | Pair-related baseline output |
|---|---|---|
| matched empty-both | both sides `{event_id: "", field: "place_id"}` | two `event_id: required nonempty string` findings **and** `claim_a and claim_b references must differ` |
| valid-ID / invalid-field | both sides `{event_id: "tarin-envelope-observation", field: "bogus"}` | two `field: expected one of ['depends_on', 'place_id', 'tick']` findings **and** `claim_a and claim_b references must differ` |
| valid-same | both sides `{event_id: "tarin-envelope-observation", field: "place_id"}` | `claim_a and claim_b references must differ` |
| valid-different | A `{event_id: "tarin-envelope-observation", field: "place_id"}`; B `{event_id: "sella-bell7-presence", field: "place_id"}` | no same-reference finding; the fixture’s `claim_b` unresolved-source finding remains |

The exact pair-related output for empty-both and valid-ID/invalid-field confirms that current `.get()` equality can add the pair finding even without a structurally valid reference pair. The valid-same and valid-different controls confirm the present positive and negative behavior. These are baseline observations only; no candidate delta was measured.

## Independent cross-checks and limits

The eight scout reports are `.shokunin/lore/reports/r69-{ledger,prior,fixture,schema}-scout.md`, `r69-critic.md`, `r69-simplifier.md`, `r69-scribe.md`, and `r69-regression-scout.md`. Their relevant baseline observations agree with this replay. In particular, `r69-regression-scout.md` identifies `.shokunin/lore/corpus/fixtures/r62-malformed-side/` as the existing fixture with the same-reference output, and `.shokunin/lore/reports/r69-critic.md` notes its same nonempty event ID plus identical invalid `bogus` fields. This verifier's valid-ID/invalid-field probe independently reproduces the same pair finding using a valid timeline base; it is not confounded by the malformed timeline in `r62-malformed-side`.

The round declaration's broader requirement for matched malformed-both, malformed-one, valid-identical, and valid-different controls is not fully exercised here: the requested matched empty-both control was used, alongside valid-ID/invalid-field and the valid controls. No claim about behavior on all malformed-one variants is made. More importantly, the requested checks cannot establish candidate correctness or improvement without a candidate and separate review of the changed fixture outcome.
