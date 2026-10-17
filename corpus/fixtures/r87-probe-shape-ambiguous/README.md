Probe (round 87, C2 depth + calibration bound; closes JDEP3 U-4 / JCAL1 residual): the ambiguous-holder record [0] also violates the key-set gate, and that gate's 'continue' precedes the holder check, so the holder-ambiguity stop is never armed: the genuine break at record [1] (from_holder 'mira' after a None reset would be a first-record violation if assessed) is neither reported nor disclosed. Expected: 2 findings, exit 1: duplicate 'dup' id, key-set violation. Zero 'unassessed' lines. Pre-existing behavior, unchanged by C1; candidate r88 calibration/depth move.

---

**r88 revision note** (commit at r88 closure; measured on the delivered tree: exit 1, 5 findings): the delivered checker now reports 5 findings including 2 first-stop disclosures; the "unchanged by C1" sentence above describes the r87 checker and is inverted at r88 — this fixture is exactly the residual the r88 C1 repair armed.
