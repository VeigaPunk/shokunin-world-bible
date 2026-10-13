# Round 54 — final non-author Sol axis adjudication

**Verdict: REJECT before executor.** Depth unchanged; coverage unchanged; calibration unchanged in the delivered tree. No delivered axis is harmed, but no material axis improved. The displayed-sheet/blue-oval Jorin account is hypothetical and unbuilt: there is no r54 fixture, source excerpt, clause map, candidate checker run, or candidate output.

## Independent pinned corpus and raw replay

I read the r54 LOG declaration, post-scout policy, verifier clarification and final dispatch; all eight r54 scout reports; the non-author reviewer, amended verifier, and separate replay clarifier; the literal r10/r15 excerpts; and the r43/r49 axis adjudications. I independently extracted `git archive 585a00f1b5c22001bb590a55276f0c22193ca305 .shokunin/lore/corpus` to a separate temporary root (`/tmp/lore-r54-sol-axis-rzgs1zor`), without relying on the prior verifier's runs. The archive and live corpus each have **1,149 file paths**, the same path set and exact file bytes (0 differing). The immediate fixture-directory names match **95/95**; all **474 fixture JSON paths** match by path and bytes (230,650 bytes total), and `fixtures/check_bible.py` matches byte-for-byte (14,845 bytes).

From *each respective repository root*, I ran all 95 names with the identical root-relative argv:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<name>
```

For every name, I compared raw stdout bytes, raw stderr bytes and exit code, without normalizing output: **95/95 exact tuples**, 0 mismatches across 190 processes. Each root has 24 exit-0 and 71 exit-1 runs; all stderr is empty. The initial verifier wording described archived runs without an explicit live comparison. Its amended report and the separate clarifier now explicitly report both-root 95/95 comparison; my replay independently confirms this. These receipts establish unchanged *old* corpus/checker behavior only. They do not test or predict output for an unbuilt Jorin candidate, verify fictional prose, or establish physical facts.

## Source, precedent and materiality

R10's expressly invented `r10-registry-witness/registrar-copy-excerpt.md` has Sella say she left the registry destination blank and **“kept the carbon.”** R15's expressly newly authored `r15-carbon-followup/sella-carbon-followup-excerpt.md` has Sella say **“Later, at Lantern Harbor, I looked again at the carbon I had kept. I saw a blurred blue oval mark on it. I cannot identify where the mark came from, and I do not attribute it to Mira’s Blue Seal.”** Even the continuity of “the carbon I had kept” is Sella's attributed account, not authenticated object identity; her own later observation already introduces the mark and its unknown origin. No r54 Jorin text has been authored in the corpus.

The proposed Jorin line would differ from r49's rejected *Sella-only* handoff allegation: Jorin would separately **report seeing** a blurred blue oval on a sheet Sella **called** her kept carbon, without claiming receipt or a holder transition. That permits a conditional comparison of two reported appearances, but does not identify the sheet independently. It does not establish the same physical carbon or same physical mark; it does not place Jorin's reported viewing before or after Sella's inspection, prove persistence or custody, or determine who made the mark. A similar phrase from another fictional speaker can be narratively suggestive, yet without a distinct source-grounded consequence its main apparent force is corroboration that relies on those missing identity/time assumptions. Merely adding a source, observer row or structurally CLEAN run would not supply the missing link.

R43 admitted a *narrow* comparison because Jorin reported seeing **Vela** at the **same named east steps** where Vela herself reported standing. Its adjudication did not infer a shared Bell-7 occasion or objective event. Here the proposed shared referent is only a sheet identified by Sella, and the mark's appearance is already in her r15 report; r43 is not blanket permission to count every second voice as material depth. R49 rejected the unbuilt handoff and warned that a `to_holder` edge would misrepresent an attributed claim as receipt/custody. Avoiding that edge protects calibration but is not itself a gain. The r54 reviewer and most scouts likewise found no consequence beyond another similarly described observation; the precedent scout allowed only a *conditional possibility*, not demonstrated materiality. I independently agree with the no-go.

| Axis | Judgment | Reason |
|---|---|---|
| **Depth** | **Unchanged** | No built Jorin account or material new consequence. Even if the bounded hypothetical were authored, a second similar-looking reported oval does not materially extend r15 without assuming the displayed sheet and mark are the same object/mark and a compatible sequence. |
| **Coverage** | **Unchanged** | No new fixture, checker rule or input class; the exact 95 old tuples and 474 JSON paths are preserved. Baseline preservation is not added coverage. |
| **Calibration** | **Unchanged** | No delivered change. The carefully qualified hypothetical need not harm calibration, but representing same-carbon identity, continuous mark, actual showing/transfer/receipt, provenance, or corroboration as settled would harm it. Source IDs and checker CLEAN could not prove any of these. |

The admission rule requires at least one **materially improved** axis and none harmed; therefore **REJECT**. Reconsider only if an authored, independently reviewed Jorin account supplies a specific useful cross-account consequence that survives unresolved physical identity and timing, keeps each speaker attributed, and passes independently checked preservation and clause mapping. No factual Blue Seal connection, mark origin, actual custody, objective canon, real-world rights or permission follows from these fictional excerpts. I wrote only this report; no corpus, checker, LOG, README or SCORECARD edit or commit.
