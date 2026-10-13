# Round 36 citation scout — fictional source, canon, and rights bounds

## Calibration target

R35’s favorable case is explicitly conditional: its two newly authored fictional notes name the same sole Bell-7 ringing on the seventh day of Embermonth, year 12, while the checker reports structural cleanliness. R36’s proposed near-miss changes only Sella’s source prose to the eighth day; all five JSON tables remain byte-identical. The calibration is whether review declines the *same-occasion* conflict when source text no longer supports it—not whether either account is true or a canon winner can be chosen. `.shokunin/lore/LOG.md:574-575`.

## Evidence and bounds

- Both source records identify authored fiction, not authoritative truth: `r35-bell7-conflict/sources.json:15-24`. Tarin’s note reports his observation; Sella’s account reports her claimed presence. This attribution does not authenticate the account or make the reports independent corroboration.
- The favorable structured descriptions state the shared seventh-day Bell-7 date (`r35-bell7-conflict/timeline.json:23-38`); the ledger’s rationale is expressly conditional and calls the date/ringing claims fictional, the conflict editorial, and the matter unresolved (`r35-bell7-conflict/contradictions.json:3-12`). Tick 3 and the `place_id` pointers alone do not supply the missing source-text entailment.
- The R36 experiment is specified as a sole Sella excerpt date change to day eight, with all five JSON tables unchanged and explicitly no inference that either account is false or that Sella was at Harbor on day seven (`.shokunin/lore/LOG.md:574-575`). In that case unchanged timeline and `why` still assert the seventh-day shared occasion, but Sella’s altered prose does not support it. Cite/pointer validity or a clean checker result cannot cure that mismatch or establish a same occasion.
- Real-world method citations are distinct from story sources (`corpus/knowledge/reference-ledger.md:1-10`). The ledger expressly leaves reuse rights and AI-training permission unassessed and infers no permission from public access (`corpus/knowledge/reference-ledger.md:5-7`). Neither citation nor fictional-source conventions grant rights to reproduce real-world works or train on them.

## Risks

1. Treating a resolvable `source_id`, a clean structural checker, repeated structured claims, or a ledger `why` as proof that the cited excerpt entails the claim, that a reported event occurred, or that an account is canon.
2. Treating R36’s date mismatch as proof either fictional account is false, or proof Sella was at Harbor on day seven. It only defeats the shared-occasion premise on the specified evidence; preserve both reports as attributed and unresolved.
3. Quietly retaining R35’s same-ringing contradiction rationale after Sella’s source date changes while the JSON remains untouched. That is a source-to-claim/map inconsistency, not a validated conflict.
4. Inferring license, quotation/reuse authority, or AI-training permission from citation, public availability, or fictional attribution.

## Falsifiable check

Compare the exact R35 and R36 Sella source excerpts against Tarin’s unchanged excerpt, the five unchanged JSON tables, and the manual comparison map. Pass calibration only if a reviewer can verify the day-seven/day-eight difference in the source text, notes that unchanged Sella timeline and ledger rationale still say day seven, and therefore declines the *shared-occasion* conflict as unsupported in R36—without declaring either account false, resolving canon, or claiming Sella was at Harbor on day seven. Also verify every source-derived factual phrase is supported by its cited excerpt and no rights/training permission is inferred. Fail if the reviewer accepts the same-occasion conflict solely from pointers/clean checker/JSON, overlooks the mismatch, upgrades reports to truth, or asserts permission absent from the rights record. This check is falsified by source text that does not contain the stipulated date contrast, JSON tables that are not byte-identical, or a reviewer who does not make the bounded decision above.
