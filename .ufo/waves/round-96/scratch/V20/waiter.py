import os, time, sys
R = "/home/vgpnk/Projects/shokunin/lore-shokunin"
a = R + "/corpus/tools/dependency_freeze.py"
b = R + "/corpus/tools/dependency-freeze-contract.json"
out = R + "/.ufo/waves/round-96/scratch/V20/waiter.log"
for i in range(90):
    if os.path.exists(a) and os.path.exists(b):
        open(out, "a").write(f"PRESENT i={i} {time.strftime('%H:%M:%S')}\n")
        sys.exit(0)
    time.sleep(10)
open(out, "a").write(f"ABSENT-after-wait {time.strftime('%H:%M:%S')}\n")
