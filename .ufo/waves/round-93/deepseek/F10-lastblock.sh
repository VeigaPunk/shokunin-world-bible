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
