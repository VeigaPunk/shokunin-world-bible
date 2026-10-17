#!/bin/bash
# usage: harness.sh <arm-name>   -> copies delivered tool+contract into arms/<arm-name>/, runs --self-test
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
ARM=$REPO/.ufo/waves/round-96/seats/V03-scratch/arms/$1
mkdir -p "$ARM"
cp "$REPO/corpus/tools/map_obligations.py" "$ARM/map_obligations.py"
cp "$REPO/corpus/tools/map-obligations-contract.json" "$ARM/map-obligations-contract.json"
echo "ARM $1 tool=$(sha256sum "$ARM/map_obligations.py" | cut -c1-16) contract=$(sha256sum "$ARM/map-obligations-contract.json" | cut -c1-16)"
