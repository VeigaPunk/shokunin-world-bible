#!/usr/bin/env python3
"""R5: build r97 claim-excerpt-map.md from the r96 post-repair map.

Every substitution is asserted (count-checked) so a silent no-op cannot pass.
Writes ONLY corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md.
"""
import hashlib
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SRC = ROOT / "corpus/fixtures/r96-crossing-response/claim-excerpt-map.md"
DST = ROOT / "corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md"

text = SRC.read_text(encoding="utf-8")
original = text

def sub(old, new, expect=1):
    global text
    count = text.count(old)
    assert count == expect, f"expected {expect} occurrence(s) of {old!r}, found {count}"
    text = text.replace(old, new)

# 1. title
sub("# r96 crossing-response: canonical claim-to-excerpt map",
    "# r97 crossing-acknowledgment: canonical claim-to-excerpt map")

# 2. scope counts
sub("all 16 source-attributed JSON obligations in this continuation (five first-appearance pointers, five entity claims, one relation, and five timeline events)",
    "all 17 source-attributed JSON obligations in this continuation (five first-appearance pointers, five entity claims, one relation, and six timeline events)")

# 3. expected inventory
sub("**Expected inventory:** 16 JSON facts; 2 editorial rows; 18 total mapped rows; 14 distinct excerpt anchors.",
    "**Expected inventory:** 17 JSON facts; 2 editorial rows; 19 total mapped rows; 15 distinct excerpt anchors.")

# 4. facts heading
sub("## JSON facts (16 canonical pointers)", "## JSON facts (17 canonical pointers)")

# 5. facts intro
sub("The 15 inherited rows carry the r94 JSON pointers, excerpt anchors, spans, and delivery modes unchanged; "
    "only the path-qualification column names this fixture's cluster path. The raw source IDs are cluster-local, "
    "resolved here as `r96-crossing-response:paired-clock` and `r96-crossing-response:crossing-minute`; the prior "
    "namespaces were `r95-crossing-aftermath:paired-clock` and `r95-crossing-aftermath:crossing-minute`. The new row "
    "resolves as `r96-crossing-response:evin-response-note`.",
    "The 16 inherited rows carry the r96 JSON pointers, excerpt anchors, spans, and delivery modes unchanged; "
    "only the path-qualification column names this fixture's cluster path. The raw source IDs are cluster-local, "
    "resolved here as `r97-crossing-acknowledgment:paired-clock` and `r97-crossing-acknowledgment:crossing-minute`; "
    "the prior namespaces were `r96-crossing-response:paired-clock` and `r96-crossing-response:crossing-minute`. "
    "The new row resolves as `r97-crossing-acknowledgment:aru-acknowledgment-note`.")

# 6. declaration row 1 (full line)
old_decl = ("| `fictional-excerpts.md:12-40` | `r96-crossing-response:paired-clock`; "
            "`r96-crossing-response:crossing-minute`; `r96-crossing-response:aru-aftermath-note`; "
            "`r96-crossing-response:evin-response-note` | `verbatim` | Newly authored fictional register, minute, "
            "aftermath note, and response note; JSON sources in this fixture. Inherited namespaces were "
            "`r95-crossing-aftermath:paired-clock`, `r95-crossing-aftermath:crossing-minute`, "
            "`r95-crossing-aftermath:aru-aftermath-note`, `r94-paired-crossing:paired-clock`, "
            "`r94-paired-crossing:crossing-minute`, and (before that) `r88-m3-maya-cluster:paired-clock`. |")
new_decl = ("| `fictional-excerpts.md:12-51` | `r97-crossing-acknowledgment:paired-clock`; "
            "`r97-crossing-acknowledgment:crossing-minute`; `r97-crossing-acknowledgment:aru-aftermath-note`; "
            "`r97-crossing-acknowledgment:evin-response-note`; `r97-crossing-acknowledgment:aru-acknowledgment-note` | "
            "`verbatim` | Newly authored fictional register, minute, aftermath note, response note, and acknowledgment "
            "note; JSON sources in this fixture. Inherited namespaces were `r96-crossing-response:paired-clock`, "
            "`r96-crossing-response:crossing-minute`, `r96-crossing-response:aru-aftermath-note`, "
            "`r96-crossing-response:evin-response-note`, `r95-crossing-aftermath:paired-clock`, "
            "`r95-crossing-aftermath:crossing-minute`, `r95-crossing-aftermath:aru-aftermath-note`, "
            "`r94-paired-crossing:paired-clock`, `r94-paired-crossing:crossing-minute`, and (before that) "
            "`r88-m3-maya-cluster:paired-clock`. |")
sub(old_decl, new_decl)

# 7. namespace rewrite on the 16 inherited fact rows only
lines = text.splitlines()
rewritten = 0
for i, line in enumerate(lines):
    if line.startswith("| J") and "r96-crossing-response:" in line:
        lines[i] = line.replace("r96-crossing-response:", "r97-crossing-acknowledgment:")
        rewritten += 1
assert rewritten == 16, f"expected 16 row lines rewritten, got {rewritten}"
text = "\n".join(lines) + "\n"

# 8. insert J17 row after the J16 row
lines = text.splitlines()
j16 = next(i for i, line in enumerate(lines) if line.startswith("| J16 |"))
assert not any(line.startswith("| J17 |") for line in lines), "J17 row already present"
lines.insert(j16 + 1, (
    "| J17 | `timeline.json#/5` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | "
    "`aru-acknowledgment-note` | `r97-crossing-acknowledgment:aru-acknowledgment-note` | `fictional-excerpts.md` | "
    "44-53 | `verbatim` | `Tick 13: I received Evin's response at the Chalk Stair.` |"))
text = "\n".join(lines) + "\n"

# 9. timeline paragraph: new event clause + corrected closing sentence
sub("; the new tick-12 response event is ordered after and depends on the tick-11 report (`aftermath-missing-evin`).",
    "; the inherited tick-12 response event is ordered after and depends on the tick-11 report (`aftermath-missing-evin`); "
    "the new tick-13 acknowledgment event is ordered after and depends on the tick-12 response (`response-evin-salt-court`).")
sub("The new tick-12 event encodes only Evin's second account of the same crossing occasion; it asserts no reconciliation, "
    "selects no winner between the accounts, and adds no duty beyond this crossing, not perpetual performance or alliance.",
    "The new tick-13 event encodes only Aru's receipt of Evin's response; it asserts no accusation, no reconciliation, "
    "selects no winner between the accounts, and adds no duty beyond this crossing.")

# 10. insert J17 paragraph after the J16 paragraph
lines = text.splitlines()
j16p = next(i for i, line in enumerate(lines) if line.startswith("J16's anchor is the tick-12 response sentence"))
assert not any("J17's anchor" in line for line in lines), "J17 paragraph already present"
lines.insert(j16p + 1, "")
lines.insert(j16p + 2, (
    "J17's anchor is the tick-13 receipt sentence (line 48); its declared span 44-53 is exactly the appended "
    "acknowledgment section, whose remaining quoted lines carry the retained account (`I hold to my own account; "
    "both accounts stand unresolved.`, line 49), the no-accusation/no-winner assertion (`I make no accusation "
    "against Evin, and I select no winner between us.`, line 50), and the no-reconciliation/no-new-duty statement "
    "(`I assert no reconciliation, no new duty, and no obligation beyond this crossing.`, line 51). The event "
    "records one acknowledgment of receipt: Aru reports receiving Evin's response while holding to his own "
    "account. It asserts no accusation and no reconciliation and selects no winner between the accounts; the two "
    "first-person accounts remain unresolved, and the record asserts no new duty, no continuing obligation, and "
    "no obligation beyond this crossing. The event's `entity_id` is Aru because the schema has one actor slot; "
    "its description names Evin's response, so the field does not exclude the other participant."))
text = "\n".join(lines) + "\n"

assert text != original, "no changes applied"
DST.write_text(text, encoding="utf-8")
print("WROTE", DST)
print("bytes:", len(text.encode("utf-8")), "lines:", text.count("\n"))
print("sha256:", hashlib.sha256(text.encode("utf-8")).hexdigest())
