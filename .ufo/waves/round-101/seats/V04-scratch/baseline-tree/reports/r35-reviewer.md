# Round 35 non-author review

## Verdict: FAIL on shared-occasion support; otherwise bounded/conditional conflict only

I compared the r35 fixture with `r33-tarin-envelope/`, the Round 35 policy in `LOG.md`, and `reports/r35-critic.md`.

### Trace and checks

- Tarin’s excerpt says: “I, Tarin, saw Sella place an unlabeled paper envelope on the Lantern Harbor registry desk during Bell-7, the single seventh-watch registry-bell sounding on the day of this note.” It reports seeing the placement; it does not establish the event as fact. Relative to r33, this is the material addition: the Bell-7 occasion phrase. The inherited Sella entity claim and Tarin event description append substantially the same phrase and retain `tarin-note` attribution. Their source linkage is consistent with the excerpt, but neither makes the report independently verified.
- Sella’s separately cited first-person excerpt says she was physically at North Tower “throughout that same Bell-7 ringing” and “was not at Lantern Harbor at any point during it.” If that is the same ringing Tarin describes, the absence covers the entire relevant occasion, and the two reported locations are incompatible **if** the named Sella and Harbor/Tower alignments are accepted. This is an incompatibility between attributed reports, not a truth or canon finding.
- `sources.json` gives each excerpt its own fictional first-person source row; `sella-bell7-presence` cites `sella-bell7-note`, has actor `sella` and place `tower`. The source row is a citation, not authentication.
- `tarin-envelope-observation` has actor `tarin` and `place_id=harbor`; the clause map correctly treats Harbor as the scene of Tarin’s reported sighting, not as Tarin/Sella identity or a direct Sella-actor location assertion. The ledger’s A pointer therefore has this asymmetry; B points to Sella’s own reported Tower presence. Its `why` states the identity/place assumptions and preserves both accounts. It does not make the checker establish them.
- The maps correctly disclaim truth, canon, tick/time conversion, and unsupported envelope contents or associations. The clause map is Tarin-only; the manual map covers Sella’s added clauses and pointers. No stale r33 excerpt quote or material overclaim found in these reviewed records.

### Blocking ambiguity under the LOG policy

The LOG requires one shared single ringing **in both excerpts**, and says not to infer occasion identity from editorial label or matching tick. But each note defines Bell-7 as the single seventh-watch ringing “on the day of this note.” The excerpt files give no dates tying the two note-days together. Sella’s phrase “that same Bell-7 ringing” is an explicit assertion of sameness, but the per-note definitions do not independently identify the referent across notes: two notes on different days can each define their day’s unique ringing with the same label. Thus the shared referent is asserted, not established by the definitions/prose as required by the policy; the editorial map/ledger cannot cure that gap. This is the same-occasion concern raised by the critic, not a tick issue. Do not pass the policy’s shared-occasion criterion on the basis of “Bell-7” or tick 3.

### Limited conclusion

**Fail** the same-occasion criterion and therefore the round’s full semantic-conflict demonstration as presently sourced. If both reports are intended to describe one identical ringing and the editorial identity/place mappings hold, their claimed locations cannot both hold. The artifact should remain an unresolved apparent report conflict; no inference about external synchronization, clock time, source truth, canon, or envelope contents is warranted.
