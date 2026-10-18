# Round 34 non-author reviewer — hearsay modality

## Finding

The r34 excerpt says: “I, Tarin, heard that Sella placed an unlabeled paper envelope on the Lantern Harbor registry desk.” This supports only that Tarin reports hearing a placement assertion. Unlike r33’s “I, Tarin, saw Sella place…”, it does not report Tarin directly seeing the act. Accordingly the unchanged `entities[tarin].claims` (“Tarin reports seeing…”) and `timeline[2].description` (“Tarin reports seeing…”) are unsupported as direct-sight claims by the r34 excerpt. This is a prose-to-record modality mismatch, not proof that either JSON assertion or the event is false.

The Sella-attributed entity claim (“Tarin reports that Sella placed…”) remains an attributed placement assertion, now supported only as hearsay—neither verified nor established false. The excerpt does not name who Tarin heard it from, say whether that speaker witnessed anything, or establish reliability or truth. I infer no informant or transmission chain.

## Scope and metadata

The r33/r34 maps correctly contrast “saw” (reported direct observation, not independent verification) with “heard that” (hearing an assertion, not direct-sight support). `tarin`/`sella` and `harbor` alignments are editorial, fixture-local IDs, not independently proved identities. Timeline tick 3 is a local sequence label, not a time stated in the excerpt. No inference follows about envelope contents, owner, recipient, intent, other objects, or canon.

The five r34 JSON files match r33 unchanged; the mismatch is deliberate. The structural checker ignores Markdown/source prose, so a clean checker result would not validate this entailment distinction or make the direct-sight fields supported. It is not a source of truth.

**Verdict:** classify r34 as hearsay-only; direct-sight fields unsupported by this excerpt, not JSON/canon false.
