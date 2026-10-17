#!/bin/bash
# V11 c2-code-review probe transcript driver (r97). Read-only w.r.t. the live tree.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
S=.ufo/waves/round-97/seats/V11-scratch
echo "### tool/contract hashes"
sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
echo "### P1 self-test"
python3 corpus/tools/dependency_freeze.py --self-test; echo "exit=$?"
echo "### P2 chain verify"
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment; do
  [ -d corpus/fixtures/$f ] || { echo "--- $f ABSENT"; continue; }
  echo "--- $f"; python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; echo "exit=$?"
done
echo "### P3 foreign identical copy (expect PATH-MISMATCH exit 2)"
python3 corpus/tools/dependency_freeze.py $S/foreign/r96-crossing-response; echo "exit=$?"
echo "### P4 foreign tampered copy (precedence probe)"
python3 corpus/tools/dependency_freeze.py $S/foreign-tampered/r96-crossing-response; echo "exit=$?"
echo "### P5 scope-guard probe: --freeze on empty scratch dir (no JSON; safe either way)"
python3 corpus/tools/dependency_freeze.py --freeze $S/empty-target; echo "exit=$?"
echo "### P6 scope-guard probe: --freeze on a populated foreign copy (only if P5 shows a guard)"
python3 corpus/tools/dependency_freeze.py --freeze $S/foreign/r96-crossing-response; echo "exit=$?"
echo "### contract hash after probes (must be unchanged)"
sha256sum corpus/tools/dependency-freeze-contract.json
